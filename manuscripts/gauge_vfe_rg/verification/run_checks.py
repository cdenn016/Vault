#!/usr/bin/env python3
"""Deterministic numerical corroborations for gauge_vfe_rg.

The checks in this file are deliberately narrower than theorems.  A PASS means
that the named, current protocol met its declared numerical endpoint.  It does
not prove a mathematical statement and it does not recreate an incompletely
specified historical run.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import platform
import re
import sys
import traceback
from collections import namedtuple
from dataclasses import asdict, is_dataclass
from pathlib import Path
from typing import Any, Callable

import mpmath
import numpy as np
import scipy
import scipy.linalg as sla
import sympy as sp


HERE = Path(__file__).resolve().parent
TEX_ROOT = HERE.parent
REPO_ROOT = TEX_ROOT.parents[1]
CLAIMS_PATH = HERE / "claims.json"
DEFAULT_OUTPUT = HERE / "current-results.json"
RUNNER_PATH = Path(__file__).resolve()
VERIFICATION_PATH = HERE / "VERIFICATION.md"
REQUIREMENTS_PATH = HERE / "requirements.txt"
NUMERICAL_TOKEN = r"\status{NUMERICAL}"
FLOAT_TOL = 1.0e-10
FACTORIZATION_PROTOCOL_SEED = 20260803
FACTORIZATION_PROTOCOL_CONDITIONS = (
    1.0,
    1.0e2,
    1.0e4,
    1.0e6,
    1.0e8,
    1.0e10,
    1.0e12,
    1.0e14,
)
FACTORIZATION_PROTOCOL_STRATUM_COUNTS = {
    "general": 2400,
    "exact_block_diagonal": 200,
    "near_decoupled": 200,
    "scale": 120,
    "permutation": 120,
    "nested_refinement": 80,
    "mpmath_100_digit": 18,
}
FACTORIZATION_CONDITIONING_TRIGGER = 1.0e-4
FACTORIZATION_BOUNDARY_WITNESS = (
    (0.012995137302571503, -0.08809796529646897, -0.01062753379868217, 0.07034656148572713),
    (-0.08809796529646897, 0.5974163750322803, 0.07207680102574178, -0.47702552029541695),
    (-0.01062753379868217, 0.07207680102574178, 0.008696311837782767, -0.05755126421432782),
    (0.07034656148572713, -0.47702552029541695, -0.05755126421432782, 0.3808968174377439),
)
FACTORIZATION_BOUNDARY_WITNESS_DIGEST = (
    "45310a74550d3759fed0f83f71a6cf3b0f45942499361d723a2248bbe243e2e3"
)
FACTORIZATION_BOUNDARY_WITNESS_GAP = 22.777105858844084
FACTORIZATION_BOUNDARY_WITNESS_EXCURSION = 4.440892098500626e-16
FACTORIZATION_BOUNDARY_WITNESS_ALLOWANCE = 9.432369402326953e-16


def _jsonable(value: Any) -> Any:
    if isinstance(value, dict):
        return {str(k): _jsonable(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [_jsonable(v) for v in value]
    if isinstance(value, np.ndarray):
        return _jsonable(value.tolist())
    if isinstance(value, (np.bool_,)):
        return bool(value)
    if isinstance(value, (np.integer,)):
        return int(value)
    if isinstance(value, (np.floating,)):
        value = float(value)
    if isinstance(value, float):
        if not math.isfinite(value):
            return str(value)
        return value
    if isinstance(value, Path):
        return str(value)
    return value


def manifest_entry(path: Path, data: bytes | None = None) -> dict[str, Any]:
    payload = path.read_bytes() if data is None else data
    return {
        "repository_relative_path": path.resolve().relative_to(REPO_ROOT).as_posix(),
        "byte_count": len(payload),
        "sha256": hashlib.sha256(payload).hexdigest(),
    }


def fro_relative(a: np.ndarray, b: np.ndarray) -> float:
    denom = max(float(np.linalg.norm(a, ord="fro")), float(np.linalg.norm(b, ord="fro")), 1.0)
    return float(np.linalg.norm(a - b, ord="fro") / denom)


def random_spd(rng: np.random.Generator, n: int, jitter: float = 0.5) -> np.ndarray:
    m = rng.standard_normal((n, n))
    return m @ m.T + jitter * np.eye(n)


def random_gl_plus(rng: np.random.Generator, n: int, scale: float = 0.25) -> np.ndarray:
    return sla.expm(scale * rng.standard_normal((n, n)))


def random_frame_with_condition(
    rng: np.random.Generator, n: int, condition_number: float
) -> np.ndarray:
    q1, _ = np.linalg.qr(rng.standard_normal((n, n)))
    q2, _ = np.linalg.qr(rng.standard_normal((n, n)))
    singular = np.geomspace(1.0, condition_number, n)
    frame = q1 @ np.diag(singular) @ q2.T
    if np.linalg.det(frame) < 0:
        frame[:, 0] *= -1
    return frame


def incidence_map(assignments: list[int], k: int) -> np.ndarray:
    n = len(assignments)
    nc = max(assignments) + 1
    scalar = np.zeros((n, nc))
    scalar[np.arange(n), assignments] = 1.0
    return np.kron(scalar, np.eye(k))


def assemble_interaction(
    self_terms: list[np.ndarray], weights: dict[tuple[int, int], np.ndarray]
) -> tuple[np.ndarray, np.ndarray]:
    n = len(self_terms)
    k = self_terms[0].shape[0]
    lap = np.zeros((n * k, n * k))
    for (i, j), w in weights.items():
        si = slice(i * k, (i + 1) * k)
        sj = slice(j * k, (j + 1) * k)
        lap[si, si] += w
        lap[sj, sj] += w
        lap[si, sj] -= w
        lap[sj, si] -= w
    precision = lap.copy()
    for i, a in enumerate(self_terms):
        si = slice(i * k, (i + 1) * k)
        precision[si, si] += a
    return precision, lap


def result(
    check_id: str,
    title: str,
    claim_ids: list[str],
    *,
    status: str,
    seed: int | list[int] | None,
    sample_count: int | str,
    expected: dict[str, Any],
    tolerances: dict[str, Any],
    observed: dict[str, Any],
    evidence_kind: str = "reproduced_output",
    interpretation: str,
) -> dict[str, Any]:
    return _jsonable(
        {
            "check_id": check_id,
            "title": title,
            "claim_ids": claim_ids,
            "status": status,
            "seed": seed,
            "sample_count": sample_count,
            "expected": expected,
            "tolerances": tolerances,
            "observed": observed,
            "evidence_kind": evidence_kind,
            "interpretation": interpretation,
        }
    )


def check_gauss_projection() -> dict[str, Any]:
    seed = 20260728
    rng = np.random.default_rng(seed)
    k = 3
    lam = random_spd(rng, k, 0.75)
    vals, vecs = np.linalg.eigh(lam)
    lam_half = (vecs * np.sqrt(vals)) @ vecs.T
    tol = 1.0e-10

    def admissible(t: np.ndarray) -> bool:
        w = lam @ t
        conditions = [
            np.linalg.norm(w - w.T, ord="fro") <= tol,
            np.linalg.eigvalsh((w + w.T) / 2).min() >= -tol,
            np.linalg.eigvalsh((lam - w + (lam - w).T) / 2).min() >= -tol,
            np.linalg.eigvalsh((t.T @ lam @ t - w + (t.T @ lam @ t - w).T) / 2).min()
            >= -tol,
        ]
        return all(conditions)

    generic_passes = sum(admissible(rng.standard_normal((k, k))) for _ in range(4000))
    projection_passes = 0
    max_idempotency = 0.0
    max_condition_residual = 0.0
    for rank in range(k + 1):
        q, _ = np.linalg.qr(rng.standard_normal((k, k)))
        x = q @ np.diag([1.0] * rank + [0.0] * (k - rank)) @ q.T
        w = lam_half @ x @ lam_half
        t = np.linalg.solve(lam, w)
        max_idempotency = max(max_idempotency, float(np.linalg.norm(x @ x - x, ord="fro")))
        max_condition_residual = max(
            max_condition_residual,
            float(np.linalg.norm(lam @ t - w, ord="fro")),
        )
        projection_passes += int(admissible(t))
    passed = generic_passes == 0 and projection_passes == 4 and max_idempotency <= tol
    return result(
        "CHK-GAUSS-PROJECTION",
        "Generic gains against exact projection controls",
        ["NUM-GAUSS-PROJECTION"],
        status="PASS" if passed else "FAIL",
        seed=seed,
        sample_count="4000 generic gains plus ranks 0,1,2,3",
        expected={"generic_admissible_count": 0, "projection_admissible_count": 4},
        tolerances={"matrix_feasibility": tol, "idempotency": tol},
        observed={
            "generic_admissible_count": generic_passes,
            "projection_admissible_count": projection_passes,
            "max_projection_idempotency_residual": max_idempotency,
            "max_lambda_t_minus_w_residual": max_condition_residual,
        },
        interpretation="A deterministic rerun corroborates the projection characterization; it does not prove generic measure zero.",
    )


def check_gauss_trivialization() -> dict[str, Any]:
    seed = 20260728
    rng = np.random.default_rng(seed)
    k = 3
    ui = random_gl_plus(rng, k)
    uj = random_gl_plus(rng, k)
    omega = ui @ np.linalg.inv(uj)
    r = random_spd(rng, k)
    raw = np.linalg.solve(r, omega)
    weight = ui.T @ np.linalg.solve(r, ui)
    raw_asym = float(np.linalg.norm(raw - raw.T, ord="fro"))
    weight_asym = float(np.linalg.norm(weight - weight.T, ord="fro"))
    min_weight = float(np.linalg.eigvalsh(weight).min())
    passed = raw_asym > 1.0e-6 and weight_asym <= FLOAT_TOL and min_weight > 0
    return result(
        "CHK-GAUSS-TRIVIALIZATION",
        "Asymmetric raw transported block versus symmetric trivialized weight",
        ["NUM-GAUSS-TRIVIALIZATION"],
        status="PASS" if passed else "FAIL",
        seed=seed,
        sample_count=1,
        expected={"raw_asymmetry": "> 1e-6", "trivialized_symmetry": "<= tolerance", "minimum_eigenvalue": "> 0"},
        tolerances={"symmetry": FLOAT_TOL},
        observed={
            "raw_asymmetry_frobenius": raw_asym,
            "trivialized_asymmetry_frobenius": weight_asym,
            "trivialized_minimum_eigenvalue": min_weight,
        },
        interpretation="The current matrices are fully emitted by the deterministic code; the manuscript's historical magnitudes used different omitted matrices.",
    )


def check_gauss_conditioning() -> dict[str, Any]:
    seed = 20260728
    rng = np.random.default_rng(seed)
    n, k, draws = 6, 3, 200
    min_eigenvalues: list[float] = []
    condition_numbers: list[float] = []
    for _ in range(draws):
        weights: dict[tuple[int, int], np.ndarray] = {}
        for i in range(n):
            for j in range(i + 1, n):
                if rng.random() < 0.6:
                    m = rng.standard_normal((k, k))
                    weights[(i, j)] = m @ m.T + 0.1 * np.eye(k)
        self_terms = []
        for _i in range(n):
            m = rng.standard_normal((k, k))
            self_terms.append(m @ m.T / k)
        precision, _ = assemble_interaction(self_terms, weights)
        eig = np.linalg.eigvalsh(precision)
        min_eigenvalues.append(float(eig[0]))
        condition_numbers.append(float(eig[-1] / eig[0]))

    complete_weights = {
        (i, j): random_spd(rng, k, 0.1)
        for i in range(n)
        for j in range(i + 1, n)
    }
    _, lap = assemble_interaction([np.zeros((k, k)) for _ in range(n)], complete_weights)
    eig_lap = np.linalg.eigvalsh(lap)
    rank_tol = max(float(eig_lap[-1]), 1.0) * 1.0e-10
    nullity = int(np.count_nonzero(np.abs(eig_lap) <= rank_tol))
    consensus_residual = float(
        np.linalg.norm(lap @ np.kron(np.ones((n, 1)), np.eye(k)), ord="fro")
    )

    symmetric_offdiag_controls = 0
    for _ in range(draws):
        unstructured = random_spd(rng, n * k)
        all_blocks_symmetric = True
        for i in range(n):
            for j in range(i + 1, n):
                block = unstructured[i * k : (i + 1) * k, j * k : (j + 1) * k]
                all_blocks_symmetric &= np.linalg.norm(block - block.T, ord="fro") <= 1.0e-10
        symmetric_offdiag_controls += int(all_blocks_symmetric)
    passed = min(min_eigenvalues) > 0 and nullity == k and symmetric_offdiag_controls == 0
    return result(
        "CHK-GAUSS-CONDITIONING",
        "Interaction-family conditioning under a fully specified current sampler",
        ["NUM-GAUSS-CONDITIONING"],
        status="PASS" if passed else "FAIL",
        seed=seed,
        sample_count={"interaction_draws": draws, "unstructured_controls": draws},
        expected={
            "all_interaction_precisions_positive_definite": True,
            "complete_graph_zero_self_nullity": k,
            "unstructured_controls_in_family": 0,
        },
        tolerances={"rank_relative": 1.0e-10, "offdiagonal_symmetry": 1.0e-10},
        observed={
            "positive_definite_count": sum(x > 0 for x in min_eigenvalues),
            "smallest_eigenvalue": min(min_eigenvalues),
            "median_condition_number": float(np.median(condition_numbers)),
            "maximum_condition_number": max(condition_numbers),
            "zero_self_control_nullity": nullity,
            "consensus_residual_frobenius": consensus_residual,
            "unstructured_controls_with_all_symmetric_offdiagonal_blocks": symmetric_offdiag_controls,
        },
        interpretation="This replaces, rather than recreates, the manuscript's incompletely specified conditioning run.",
    )


def check_kron_exact_witness() -> dict[str, Any]:
    w1 = sp.Matrix([[2, 1], [1, 1]])
    w2 = sp.Matrix([[1, 0], [0, 2]])
    d = sp.diag(3, 4)
    product = w1 * d.inv() * w2
    asymmetry = sp.simplify(product - product.T)
    d1 = sp.diag(2, 3)
    d2 = sp.diag(5, 7)
    d3 = sp.diag(11, 13)
    diagonal_product = sp.simplify(d1 * d2.inv() * d3)
    passed = asymmetry != sp.zeros(2) and diagonal_product == diagonal_product.T
    return result(
        "CHK-KRON-EXACT-WITNESS",
        "Exact rational matrix-Kron nonclosure witness and commuting control",
        ["REVIEW-R07-KRON-NONCLOSURE"],
        status="PASS" if passed else "FAIL",
        seed=None,
        sample_count="one exact counterexample and one exact commuting control",
        expected={"counterexample_product_symmetric": False, "commuting_control_symmetric": True},
        tolerances={"arithmetic": "exact rational"},
        observed={
            "counterexample_product": [[str(x) for x in product.row(i)] for i in range(product.rows)],
            "counterexample_asymmetry": [[str(x) for x in asymmetry.row(i)] for i in range(asymmetry.rows)],
            "commuting_control_product": [
                [str(x) for x in diagonal_product.row(i)] for i in range(diagonal_product.rows)
            ],
        },
        evidence_kind="exact_symbolic_witness",
        interpretation="This exact finite witness closes nonclosure of the unrestricted matrix family, not a genericity theorem.",
    )


def check_kron_monte_carlo() -> dict[str, Any]:
    seed = 20260728
    rng = np.random.default_rng(seed)
    draws = 200
    k3_symmetric = 0
    k3_relative_asymmetry: list[float] = []
    scalar_symmetric = 0
    for _ in range(draws):
        w1 = random_spd(rng, 3)
        w2 = random_spd(rng, 3)
        d = random_spd(rng, 3)
        p = w1 @ np.linalg.solve(d, w2)
        rel = float(np.linalg.norm(p - p.T, ord="fro") / max(np.linalg.norm(p, ord="fro"), 1.0))
        k3_relative_asymmetry.append(rel)
        k3_symmetric += int(rel <= 1.0e-10)
        s1 = float(rng.uniform(0.1, 3.0))
        s2 = float(rng.uniform(0.1, 3.0))
        sd = float(rng.uniform(0.1, 3.0))
        scalar_symmetric += int(abs(s1 * s2 / sd - s2 * s1 / sd) <= 1.0e-15)
    passed = k3_symmetric == 0 and scalar_symmetric == draws
    return result(
        "CHK-KRON-MONTE-CARLO",
        "Current matrix-Kron genericity sweep with scalar control",
        ["REVIEW-R07-KRON-NONCLOSURE"],
        status="PASS" if passed else "FAIL",
        seed=seed,
        sample_count={"K=3": draws, "K=1": draws},
        expected={"K3_symmetric_count": 0, "K1_symmetric_count": draws},
        tolerances={"relative_asymmetry": 1.0e-10, "scalar_equality": 1.0e-15},
        observed={
            "K3_symmetric_count": k3_symmetric,
            "K1_symmetric_count": scalar_symmetric,
            "K3_minimum_relative_asymmetry": min(k3_relative_asymmetry),
            "K3_maximum_relative_asymmetry": max(k3_relative_asymmetry),
        },
        interpretation="The sweep is controlled numerical evidence only; the exact witness is the load-bearing nonclosure evidence.",
    )


def check_restriction_schur() -> dict[str, Any]:
    seed = 20260728
    rng = np.random.default_rng(seed)
    n, r = 9, 4
    j = random_spd(rng, n)
    q, _ = np.linalg.qr(rng.standard_normal((n, n)))
    b, bp = q[:, :r], q[:, r:]
    marginal = np.linalg.inv(bp.T @ np.linalg.inv(j) @ bp)
    restricted = bp.T @ j @ bp
    rhs = bp.T @ j @ b @ np.linalg.inv(b.T @ j @ b) @ b.T @ j @ bp
    identity_residual = fro_relative(restricted - marginal, rhs)
    gap_eig = np.linalg.eigvalsh((restricted - marginal + (restricted - marginal).T) / 2)
    rank_tol = max(float(gap_eig[-1]), 1.0) * 1.0e-10
    gap_rank = int(np.count_nonzero(gap_eig > rank_tol))

    mu = rng.standard_normal(n)
    mu_perp = bp.T @ mu
    closed_cost = 0.5 * float(mu_perp @ marginal @ mu_perp)
    mu_star = mu - np.linalg.solve(j, bp) @ marginal @ mu_perp
    direct_cost = 0.5 * float((mu_star - mu) @ j @ (mu_star - mu))
    constraint_residual = float(np.linalg.norm(bp.T @ mu_star))

    eigvals, eigvecs = np.linalg.eigh(j)
    be, bpe = eigvecs[:, :r], eigvecs[:, r:]
    orth_gap = bpe.T @ j @ bpe - np.linalg.inv(bpe.T @ np.linalg.inv(j) @ bpe)
    orth_residual = float(np.linalg.norm(orth_gap, ord="fro"))
    passed = (
        identity_residual <= 1.0e-11
        and gap_eig.min() >= -1.0e-10
        and gap_rank <= r
        and abs(closed_cost - direct_cost) <= 1.0e-10
        and constraint_residual <= 1.0e-10
        and orth_residual <= 1.0e-10
    )
    return result(
        "CHK-RESTRICTION-SCHUR",
        "Marginal precision, restricted precision, and constrained mean cost",
        ["NUM-RESTRICTION-SCHUR", "NUM-CG-MEAN-TIE"],
        status="PASS" if passed else "FAIL",
        seed=seed,
        sample_count=1,
        expected={
            "schur_identity": True,
            "gap_positive_semidefinite": True,
            "gap_rank_at_most": r,
            "closed_cost_equals_direct_cost": True,
            "orthogonal_control_gap": 0,
        },
        tolerances={"relative_identity": 1.0e-11, "spectral": 1.0e-10, "cost": 1.0e-10},
        observed={
            "schur_identity_relative_residual": identity_residual,
            "gap_minimum_eigenvalue": float(gap_eig.min()),
            "gap_rank": gap_rank,
            "closed_cost": closed_cost,
            "direct_cost": direct_cost,
            "constraint_residual": constraint_residual,
            "orthogonal_control_residual": orth_residual,
        },
        interpretation="The check independently reconstructs the block-inversion and KKT endpoints.",
    )


def gaussian_kl(
    mu_q: np.ndarray, cov_q: np.ndarray, mu_p: np.ndarray, cov_p: np.ndarray
) -> float:
    n = mu_q.size
    precision_p = np.linalg.inv(cov_p)
    delta = mu_p - mu_q
    sign_q, logdet_q = np.linalg.slogdet(cov_q)
    sign_p, logdet_p = np.linalg.slogdet(cov_p)
    if sign_q <= 0 or sign_p <= 0:
        raise ValueError("KL received a non-positive covariance")
    return 0.5 * float(
        np.trace(precision_p @ cov_q)
        + delta @ precision_p @ delta
        - n
        + logdet_p
        - logdet_q
    )


def check_ig_expectation_metric() -> dict[str, Any]:
    seed = 7
    rng = np.random.default_rng(seed)
    n = 4
    precision = random_spd(rng, n, 2.0)
    covariance = np.linalg.inv(precision)
    mu = 0.15 * rng.standard_normal(n)
    moment2 = covariance + np.outer(mu, mu)
    g_expectation = (
        (1.0 + float(mu @ precision @ mu)) * precision
        + np.outer(precision @ mu, precision @ mu)
    )
    eps_values = [1.0e-3, 5.0e-4, 2.5e-4]
    expectation_errors: list[float] = []
    moment_errors: list[float] = []
    for _ in range(6):
        u = rng.standard_normal(n)
        u /= np.linalg.norm(u)
        predicted_exp = float(u @ g_expectation @ u)
        predicted_moment = float(u @ precision @ u)
        raw_exp: list[float] = []
        raw_moment: list[float] = []
        for eps in eps_values:
            mu_eps = mu + eps * u
            cov_eps = moment2 - np.outer(mu_eps, mu_eps)
            raw_exp.append(2.0 * gaussian_kl(mu_eps, cov_eps, mu, covariance) / eps**2)
            raw_moment.append(
                2.0 * gaussian_kl(mu_eps, covariance, mu, covariance) / eps**2
            )
        extrap_exp = 2.0 * raw_exp[-1] - raw_exp[-2]
        extrap_moment = 2.0 * raw_moment[-1] - raw_moment[-2]
        expectation_errors.append(abs(extrap_exp - predicted_exp) / max(abs(predicted_exp), 1.0))
        moment_errors.append(abs(extrap_moment - predicted_moment) / max(abs(predicted_moment), 1.0))
    generalized = sla.eigvalsh(g_expectation, precision)
    mahalanobis = float(mu @ precision @ mu)
    predicted_spectrum = np.sort(
        np.array([1.0 + mahalanobis] * (n - 1) + [1.0 + 2.0 * mahalanobis])
    )
    spectrum_error = float(np.max(np.abs(np.sort(generalized) - predicted_spectrum)))
    passed = max(expectation_errors) <= 2.0e-5 and max(moment_errors) <= 2.0e-5 and spectrum_error <= 1.0e-10
    return result(
        "CHK-IG-EXPECTATION-METRIC",
        "Expectation-chart Fisher metric from finite-difference KL",
        ["NUM-IG-EXPECTATION-METRIC", "NUM-IG-REGISTER-CHART"],
        status="PASS" if passed else "FAIL",
        seed=seed,
        sample_count={"directions": 6, "epsilon_values": eps_values},
        expected={
            "expectation_chart_matches_closed_form": True,
            "moment_chart_matches_precision": True,
            "generalized_spectrum_matches_formula": True,
        },
        tolerances={"relative_quadratic_form": 2.0e-5, "spectrum_absolute": 1.0e-10},
        observed={
            "worst_expectation_chart_relative_error": max(expectation_errors),
            "worst_moment_chart_relative_error": max(moment_errors),
            "mahalanobis_squared": mahalanobis,
            "observed_generalized_spectrum": generalized,
            "predicted_generalized_spectrum": predicted_spectrum,
            "spectrum_max_absolute_error": spectrum_error,
        },
        interpretation="This reproduces the finite-difference route under a fully specified current base point; it does not recreate the omitted 2,000,000-sample score run.",
    )


def check_ig_pullback_pushforward() -> dict[str, Any]:
    seed = 99
    rng = np.random.default_rng(seed)
    n, k, draws = 12, 5, 200
    minimum_eigenvalue = math.inf
    max_identity_error = 0.0
    for _ in range(draws):
        lam = random_spd(rng, n)
        q, _ = np.linalg.qr(rng.standard_normal((n, n)))
        b, bp = q[:, :k], q[:, k:]
        lhs = b.T @ lam @ b - np.linalg.inv(b.T @ np.linalg.inv(lam) @ b)
        rhs = b.T @ lam @ bp @ np.linalg.inv(bp.T @ lam @ bp) @ bp.T @ lam @ b
        minimum_eigenvalue = min(
            minimum_eigenvalue, float(np.linalg.eigvalsh((lhs + lhs.T) / 2).min())
        )
        max_identity_error = max(max_identity_error, fro_relative(lhs, rhs))
    lam = random_spd(rng, n)
    _, eigenvectors = np.linalg.eigh(lam)
    b, bp = eigenvectors[:, :k], eigenvectors[:, k:]
    orth_gap = b.T @ lam @ b - np.linalg.inv(b.T @ np.linalg.inv(lam) @ b)
    orth_residual = float(np.linalg.norm(orth_gap, ord="fro"))
    passed = minimum_eigenvalue >= -1.0e-10 and max_identity_error <= 1.0e-11 and orth_residual <= 1.0e-10
    return result(
        "CHK-IG-PULLBACK-PUSHFORWARD",
        "Pullback versus pushforward Fisher metric",
        ["NUM-IG-PULLBACK-PUSHFORWARD"],
        status="PASS" if passed else "FAIL",
        seed=seed,
        sample_count=draws,
        expected={"all_gaps_positive_semidefinite": True, "schur_identity": True, "orthogonal_control_gap": 0},
        tolerances={"spectral": 1.0e-10, "relative_identity": 1.0e-11},
        observed={
            "minimum_gap_eigenvalue": minimum_eigenvalue,
            "maximum_identity_relative_error": max_identity_error,
            "orthogonal_control_residual": orth_residual,
        },
        interpretation="The numerical check corroborates the proved Schur identity and Loewner order.",
    )


def check_generalized_spectrum() -> dict[str, Any]:
    seed = 20260728
    rng = np.random.default_rng(seed)
    n, k = 6, 3
    weights: dict[tuple[int, int], np.ndarray] = {}
    for i in range(n):
        for j in range(i + 1, n):
            if rng.random() < 0.6:
                weights[(i, j)] = random_spd(rng, k, 0.1)
    self_terms = [random_spd(rng, k, 0.2) for _ in range(n)]
    precision, lap = assemble_interaction(self_terms, weights)
    baseline = sla.eigvalsh(lap, precision)
    baseline_ordinary = np.linalg.eigvalsh(precision)
    max_generalized_error = 0.0
    ordinary_maxima: list[float] = []
    ordinary_minima: list[float] = []
    actual_conditions: list[float] = []
    for _ in range(12):
        blocks = [random_frame_with_condition(rng, k, 22.0) for _i in range(n)]
        transform = sla.block_diag(*blocks)
        actual_conditions.append(float(np.linalg.cond(transform)))
        lap_t = transform.T @ lap @ transform
        precision_t = transform.T @ precision @ transform
        current = sla.eigvalsh(lap_t, precision_t)
        max_generalized_error = max(
            max_generalized_error, float(np.max(np.abs(np.sort(current) - np.sort(baseline))))
        )
        ordinary = np.linalg.eigvalsh(precision_t)
        ordinary_maxima.append(float(ordinary[-1]))
        ordinary_minima.append(float(ordinary[0]))
    maximum_spread = max(ordinary_maxima) / min(ordinary_maxima)
    minimum_spread = max(ordinary_minima) / min(ordinary_minima)
    passed = max_generalized_error <= 1.0e-9 and max(maximum_spread, minimum_spread) > 1.1
    return result(
        "CHK-GENERALIZED-SPECTRUM",
        "Generalized spectrum under block congruence",
        [
            "NUM-IG-GAUGE-INVARIANTS",
            "NUM-IG-REGISTER-GAUGE",
            "NUM-RG-GENERALIZED-SPECTRUM",
        ],
        status="PASS" if passed else "FAIL",
        seed=seed,
        sample_count=12,
        expected={"generalized_spectrum_invariant": True, "ordinary_spectrum_not_invariant": True},
        tolerances={"generalized_eigenvalue_absolute": 1.0e-9},
        observed={
            "maximum_generalized_eigenvalue_error": max_generalized_error,
            "ordinary_largest_eigenvalue_spread": maximum_spread,
            "ordinary_smallest_eigenvalue_spread": minimum_spread,
            "transform_condition_numbers": actual_conditions,
            "baseline_ordinary_condition_number": float(baseline_ordinary[-1] / baseline_ordinary[0]),
        },
        interpretation="Congruence invariance is a property of the pencil; ordinary eigenvalues provide the negative control.",
    )


def check_cg_aggregation() -> dict[str, Any]:
    seed = 20260728
    rng = np.random.default_rng(seed)
    n, k = 7, 3
    assignments = [0, 0, 1, 1, 1, 2, 2]
    weights = {
        (i, j): random_spd(rng, k, 0.1)
        for i in range(n)
        for j in range(i + 1, n)
    }
    self_terms = [random_spd(rng, k, 0.1) for _ in range(n)]
    precision, lap = assemble_interaction(self_terms, weights)
    s = incidence_map(assignments, k)
    coarse = s.T @ precision @ s

    nc = 3
    coarse_self = [
        sum((self_terms[i] for i in range(n) if assignments[i] == c), np.zeros((k, k)))
        for c in range(nc)
    ]
    coarse_weights: dict[tuple[int, int], np.ndarray] = {}
    for ci in range(nc):
        for cj in range(ci + 1, nc):
            coarse_weights[(ci, cj)] = sum(
                (
                    w
                    for (i, j), w in weights.items()
                    if {assignments[i], assignments[j]} == {ci, cj}
                ),
                np.zeros((k, k)),
            )
    predicted, _ = assemble_interaction(coarse_self, coarse_weights)
    formula_error = fro_relative(coarse, predicted)
    consensus_residual = float(
        np.linalg.norm(lap @ np.kron(np.ones((n, 1)), np.eye(k)), ord="fro")
    )
    perturbed_weights = {key: value.copy() for key, value in weights.items()}
    v = rng.standard_normal(k)
    delta = 100.0 * np.outer(v, v)
    perturbed_weights[(0, 1)] += delta
    perturbed_precision, _ = assemble_interaction(self_terms, perturbed_weights)
    internal_effect = float(np.linalg.norm(s.T @ perturbed_precision @ s - coarse, ord="fro"))
    passed = formula_error <= 1.0e-11 and consensus_residual <= 1.0e-10 and internal_effect <= 1.0e-9
    return result(
        "CHK-CG-AGGREGATION",
        "Coarse block identity and internal-edge annihilation",
        ["NUM-CG-AGGREGATION"],
        status="PASS" if passed else "FAIL",
        seed=seed,
        sample_count=1,
        expected={"coarse_formula": True, "fine_consensus_null": True, "internal_edge_effect_on_coarse_operator": 0},
        tolerances={"relative_formula": 1.0e-11, "absolute_residual": 1.0e-9},
        observed={
            "coarse_formula_relative_error": formula_error,
            "fine_consensus_residual": consensus_residual,
            "internal_edge_perturbation_norm": float(np.linalg.norm(delta, ord="fro")),
            "coarse_operator_change": internal_effect,
        },
        interpretation="The check evaluates the exact congruence and independently assembled coarse parameters.",
    )


def check_graph_holonomy() -> dict[str, Any]:
    seed = 20260728
    rng = np.random.default_rng(seed)
    k = 3
    rank_rtol = 1.0e-9

    def scale_relative_nullity(matrix: np.ndarray) -> tuple[int, float, np.ndarray]:
        singular = np.linalg.svd(matrix, compute_uv=False)
        tolerance = rank_rtol * max(float(singular[0]), 1.0)
        return int(np.count_nonzero(singular <= tolerance)), tolerance, singular

    def twisted_laplacian(
        edges: list[tuple[int, int, np.ndarray]], weights: list[np.ndarray]
    ) -> np.ndarray:
        out = np.zeros((3 * k, 3 * k))
        for (i, j, theta_ij), weight in zip(edges, weights):
            residual = np.zeros((k, 3 * k))
            residual[:, i * k : (i + 1) * k] = np.eye(k)
            residual[:, j * k : (j + 1) * k] = -theta_ij
            out += residual.T @ weight @ residual
        return out

    frames = [random_gl_plus(rng, k) for _ in range(3)]
    flat_edges = [
        (0, 1, frames[0] @ np.linalg.inv(frames[1])),
        (1, 2, frames[1] @ np.linalg.inv(frames[2])),
        (2, 0, frames[2] @ np.linalg.inv(frames[0])),
    ]
    weights = [random_spd(rng, k, 1.0) for _ in flat_edges]
    flat_loop = flat_edges[0][2] @ flat_edges[1][2] @ flat_edges[2][2]
    flat_defect = float(np.linalg.norm(flat_loop - np.eye(k), ord="fro"))
    flat_laplacian = twisted_laplacian(flat_edges, weights)
    flat_nullity, flat_rank_tolerance, flat_singular = scale_relative_nullity(flat_laplacian)

    trivialized = [
        np.linalg.inv(frames[i]) @ theta_ij @ frames[j]
        for i, j, theta_ij in flat_edges
    ]
    trivialization_residual = max(
        float(np.linalg.norm(item - np.eye(k), ord="fro")) for item in trivialized
    )

    angle = 0.7
    rotation = np.array(
        [
            [math.cos(angle), -math.sin(angle), 0.0],
            [math.sin(angle), math.cos(angle), 0.0],
            [0.0, 0.0, 1.0],
        ]
    )
    retwisted_edges = [
        (0, 1, np.eye(k)),
        (1, 2, np.eye(k)),
        (2, 0, rotation),
    ]
    retwisted_loop = rotation
    retwisted_laplacian = twisted_laplacian(retwisted_edges, weights)
    retwisted_nullity, retwisted_rank_tolerance, retwisted_singular = (
        scale_relative_nullity(retwisted_laplacian)
    )
    fixed_nullity, fixed_tolerance, fixed_singular = scale_relative_nullity(
        retwisted_loop - np.eye(k)
    )

    conditioner = random_frame_with_condition(rng, k, 1.0e4)
    stressed_loop = conditioner @ rotation @ np.linalg.inv(conditioner)
    stressed_edges = [
        (0, 1, np.eye(k)),
        (1, 2, np.eye(k)),
        (2, 0, stressed_loop),
    ]
    stressed_laplacian = twisted_laplacian(stressed_edges, weights)
    stressed_nullity, stressed_rank_tolerance, stressed_singular = (
        scale_relative_nullity(stressed_laplacian)
    )
    stressed_fixed_nullity, stressed_fixed_tolerance, stressed_fixed_singular = (
        scale_relative_nullity(stressed_loop - np.eye(k))
    )

    gauges = [random_gl_plus(rng, k) for _ in range(3)]
    transformed = {
        (i, j): gauges[i] @ theta_ij @ np.linalg.inv(gauges[j])
        for i, j, theta_ij in flat_edges
    }
    transformed_loop = (
        transformed[(0, 1)] @ transformed[(1, 2)] @ transformed[(2, 0)]
    )
    conjugacy_residual = float(
        np.linalg.norm(
            transformed_loop - gauges[0] @ flat_loop @ np.linalg.inv(gauges[0]),
            ord="fro",
        )
    )
    cut_a = random_gl_plus(rng, k)
    cut_equal = float(
        np.linalg.norm(cut_a @ np.linalg.inv(cut_a) - np.eye(k), ord="fro")
    )
    cut_b = random_gl_plus(rng, k)
    cut_distinct = float(
        np.linalg.norm(cut_a @ np.linalg.inv(cut_b) - np.eye(k), ord="fro")
    )
    passed = (
        flat_defect <= 1.0e-10
        and trivialization_residual <= 1.0e-10
        and flat_nullity == k
        and retwisted_nullity == fixed_nullity == 1
        and stressed_nullity == stressed_fixed_nullity == 1
        and conjugacy_residual <= 1.0e-10
        and cut_equal <= 1.0e-10
        and cut_distinct > 1.0e-3
    )
    return result(
        "CHK-GRAPH-HOLONOMY",
        "Graph holonomy, twisted-Laplacian kernels, and conditioned-similarity control",
        ["NUM-CG-HOLONOMY", "NUM-RG-HOLONOMY"],
        status="PASS" if passed else "FAIL",
        seed=seed,
        sample_count="one coboundary triangle, one retwisted triangle, one condition-1e4 similarity stress case, and cut-pair controls",
        expected={
            "flat_loop": "identity",
            "flat_laplacian_nullity": k,
            "retwisted_laplacian_nullity": "dim ker(H-I)",
            "conditioned_similarity_nullity": "dim ker(S H S^-1-I)",
            "two_cut_edge_walk_identity_iff_equal": True,
        },
        tolerances={
            "identity_and_conjugacy_absolute": 1.0e-10,
            "rank_relative_singular_value": rank_rtol,
            "nontrivial_cut_defect": 1.0e-3,
        },
        observed={
            "flat_loop_defect": flat_defect,
            "trivialization_residual": trivialization_residual,
            "flat_laplacian": {
                "nullity": flat_nullity,
                "rank_tolerance": flat_rank_tolerance,
                "singular_values": flat_singular,
            },
            "retwisted": {
                "laplacian_nullity": retwisted_nullity,
                "fixed_space_dimension": fixed_nullity,
                "laplacian_rank_tolerance": retwisted_rank_tolerance,
                "fixed_space_rank_tolerance": fixed_tolerance,
                "laplacian_singular_values": retwisted_singular,
                "H_minus_I_singular_values": fixed_singular,
            },
            "conditioned_similarity_stress": {
                "condition_number": float(np.linalg.cond(conditioner)),
                "laplacian_nullity": stressed_nullity,
                "fixed_space_dimension": stressed_fixed_nullity,
                "laplacian_rank_tolerance": stressed_rank_tolerance,
                "fixed_space_rank_tolerance": stressed_fixed_tolerance,
                "laplacian_singular_values": stressed_singular,
                "H_minus_I_singular_values": stressed_fixed_singular,
            },
            "conjugacy_residual": conjugacy_residual,
            "equal_cut_walk_defect": cut_equal,
            "distinct_cut_walk_defect": cut_distinct,
        },
        interpretation="The weighted graph-Laplacian nullity is compared directly with the loop fixed space. The conditioned-similarity case is a numerical stress test, not a substitute for the exact kernel proof.",
    )


def check_cg_maximal_clusters() -> dict[str, Any]:
    vertices = (0, 1, 2)
    k = 2
    angle = 0.73
    rotation = np.array(
        [[math.cos(angle), -math.sin(angle)], [math.sin(angle), math.cos(angle)]]
    )
    directed = {
        (0, 1): np.eye(k),
        (1, 0): np.eye(k),
        (1, 2): np.eye(k),
        (2, 1): np.eye(k),
        (2, 0): rotation,
        (0, 2): rotation.T,
    }

    def trivializable(subset: frozenset[int]) -> tuple[bool, float]:
        root = min(subset)
        potentials: dict[int, np.ndarray] = {root: np.eye(k)}
        queue = [root]
        while queue:
            i = queue.pop(0)
            for j in sorted(subset):
                if (i, j) not in directed or j in potentials:
                    continue
                # Theta_ij = T_i T_j^{-1}, hence T_j = Theta_ij^{-1} T_i.
                potentials[j] = np.linalg.inv(directed[(i, j)]) @ potentials[i]
                queue.append(j)
        if len(potentials) != len(subset):
            return False, math.inf
        residual = 0.0
        for (i, j), theta_ij in directed.items():
            if i in subset and j in subset:
                residual = max(
                    residual,
                    float(
                        np.linalg.norm(
                            theta_ij - potentials[i] @ np.linalg.inv(potentials[j]),
                            ord="fro",
                        )
                    ),
                )
        return residual <= 1.0e-10, residual

    subsets = [
        frozenset(i for i in vertices if mask & (1 << i))
        for mask in range(1, 1 << len(vertices))
    ]
    subset_results = {}
    admissible: list[frozenset[int]] = []
    for subset in subsets:
        is_admissible, residual = trivializable(subset)
        subset_results["".join(map(str, sorted(subset)))] = {
            "vertices": sorted(subset),
            "trivializable": is_admissible,
            "maximum_transport_residual": residual,
        }
        if is_admissible:
            admissible.append(subset)
    maximal = [s for s in admissible if not any(s < t for t in admissible)]

    def all_set_partitions(items: tuple[int, ...]) -> list[list[frozenset[int]]]:
        if not items:
            return [[]]
        first, rest = items[0], items[1:]
        output: list[list[frozenset[int]]] = []
        for partition in all_set_partitions(rest):
            output.append([frozenset({first})] + partition)
            for index in range(len(partition)):
                expanded = list(partition)
                expanded[index] = frozenset(set(expanded[index]) | {first})
                output.append(expanded)
        canonical: dict[tuple[tuple[int, ...], ...], list[frozenset[int]]] = {}
        for partition in output:
            key = tuple(sorted(tuple(sorted(block)) for block in partition))
            canonical[key] = [frozenset(block) for block in key]
        return list(canonical.values())

    partitions = all_set_partitions(vertices)
    admissible_partitions = [
        partition
        for partition in partitions
        if all(block in admissible for block in partition)
    ]
    loop = directed[(0, 1)] @ directed[(1, 2)] @ directed[(2, 0)]
    loop_defect = float(np.linalg.norm(loop - np.eye(k), ord="fro"))
    passed = (
        loop_defect > 1.0e-3
        and len(subsets) == 7
        and len(admissible) == 6
        and len(maximal) == 3
        and len(partitions) == 5
        and len(admissible_partitions) == 4
        and not subset_results["012"]["trivializable"]
    )
    return result(
        "CHK-CG-MAXIMAL-CLUSTERS",
        "Algorithmic non-flat triangle holonomy and partition enumeration",
        ["REVIEW-CG-MAXIMAL-CLUSTERS"],
        status="PASS" if passed else "FAIL",
        seed=None,
        sample_count="all seven induced nonempty subgraphs and all five algorithmically generated set partitions",
        expected={
            "full_triangle_cycle_nonidentity": True,
            "admissible_nonempty_subsets": 6,
            "maximal_admissible_subsets": 3,
            "generated_set_partitions": 5,
            "admissible_partitions": 4,
        },
        tolerances={
            "transport_identity_absolute": 1.0e-10,
            "nonidentity_cycle_defect": 1.0e-3,
            "enumeration": "exact integer counts",
        },
        observed={
            "triangle_loop_defect": loop_defect,
            "subset_results": subset_results,
            "admissible_nonempty_subsets": len(admissible),
            "maximal_admissible_subsets": len(maximal),
            "generated_set_partitions": len(partitions),
            "admissible_partitions": len(admissible_partitions),
            "maximal_sets": [sorted(x) for x in maximal],
            "admissible_partition_blocks": [
                [sorted(block) for block in partition]
                for partition in admissible_partitions
            ],
        },
        evidence_kind="algorithmic_exact_enumeration_with_floating_transport_witness",
        interpretation="Admissibility is computed from restricted transport consistency. No subset is classified by cardinality, and no partition list is supplied by hand.",
    )


def lambda_interaction(
    n: int, k: int, weights: dict[tuple[int, int], np.ndarray], lam: float
) -> np.ndarray:
    out = np.zeros((n * k, n * k))
    for (i, j), w in weights.items():
        si = slice(i * k, (i + 1) * k)
        sj = slice(j * k, (j + 1) * k)
        out[si, si] += w
        out[sj, sj] += w
        out[si, sj] -= lam * w
        out[sj, si] -= lam * w
    return out


def check_cg_lambda_continuum() -> dict[str, Any]:
    seed = 20260728
    rng = np.random.default_rng(seed)
    n, k = 7, 3
    assignments = [0, 0, 1, 1, 1, 2, 2]
    nc = max(assignments) + 1
    aggregation = incidence_map(assignments, k)
    weights = {
        (i, j): random_spd(rng, k, 0.1)
        for i in range(n)
        for j in range(i + 1, n)
        if rng.random() < 0.55
    }
    self_terms = [random_spd(rng, k, 0.2) for _ in range(n)]
    inside = [-1.0, -0.5, 0.0, 0.5, 0.9, 1.0]
    min_inside = {
        str(lam): float(
            np.linalg.eigvalsh(lambda_interaction(n, k, weights, lam)).min()
        )
        for lam in inside
    }
    coarse_formula_errors = {}
    coarse_minimum_eigenvalues = {}
    for lam in inside:
        fine = lambda_interaction(n, k, weights, lam)
        for i, self_term in enumerate(self_terms):
            si = slice(i * k, (i + 1) * k)
            fine[si, si] += self_term
        aggregated = aggregation.T @ fine @ aggregation

        coarse_weights: dict[tuple[int, int], np.ndarray] = {}
        for ci in range(nc):
            for cj in range(ci + 1, nc):
                coarse_weights[(ci, cj)] = sum(
                    (
                        weight
                        for (i, j), weight in weights.items()
                        if {assignments[i], assignments[j]} == {ci, cj}
                    ),
                    np.zeros((k, k)),
                )
        coarse_self_terms = []
        for ci in range(nc):
            additive_self = sum(
                (
                    self_terms[i]
                    for i in range(n)
                    if assignments[i] == ci
                ),
                np.zeros((k, k)),
            )
            internal = sum(
                (
                    weight
                    for (i, j), weight in weights.items()
                    if assignments[i] == ci and assignments[j] == ci
                ),
                np.zeros((k, k)),
            )
            coarse_self_terms.append(additive_self + 2.0 * (1.0 - lam) * internal)
        predicted = lambda_interaction(nc, k, coarse_weights, lam)
        for ci, self_term in enumerate(coarse_self_terms):
            si = slice(ci * k, (ci + 1) * k)
            predicted[si, si] += self_term
        coarse_formula_errors[str(lam)] = fro_relative(aggregated, predicted)
        coarse_minimum_eigenvalues[str(lam)] = float(
            np.linalg.eigvalsh(aggregated).min()
        )

    two_node = {(0, 1): np.eye(k)}
    outside_min = {
        str(lam): float(np.linalg.eigvalsh(lambda_interaction(2, k, two_node, lam)).min())
        for lam in [-1.2, 1.2]
    }
    symbolic_lambda = sp.symbols("lambda", real=True)
    symbolic_two_node = sp.Matrix(
        [[1, -symbolic_lambda], [-symbolic_lambda, 1]]
    )
    symbolic_characteristic = sp.factor(
        symbolic_two_node.charpoly().as_expr()
    )
    symbolic_eigenvalues = {
        str(eigenvalue): int(multiplicity)
        for eigenvalue, multiplicity in symbolic_two_node.eigenvals().items()
    }
    consensus = np.kron(np.ones((n, 1)), np.eye(k))
    residuals = {
        str(lam): float(np.linalg.norm(lambda_interaction(n, k, weights, lam) @ consensus, ord="fro"))
        for lam in inside
    }
    scaled = [residuals[str(lam)] / (1.0 - lam) for lam in inside if lam < 1.0]
    scaled_spread = max(scaled) - min(scaled)
    lap = lambda_interaction(n, k, weights, 1.0)
    signless = lambda_interaction(n, k, weights, -1.0)
    convex_error = 0.0
    for lam in inside:
        predicted = 0.5 * (1 + lam) * lap + 0.5 * (1 - lam) * signless
        convex_error = max(convex_error, fro_relative(lambda_interaction(n, k, weights, lam), predicted))
    passed = (
        min(min_inside.values()) >= -1.0e-9
        and max(outside_min.values()) < -0.1
        and max(coarse_formula_errors.values()) <= 1.0e-11
        and min(coarse_minimum_eigenvalues.values()) > 0
        and residuals["1.0"] <= 1.0e-9
        and scaled_spread <= 1.0e-9
        and convex_error <= 1.0e-12
    )
    return result(
        "CHK-CG-LAMBDA-CONTINUUM",
        "Positive-semidefinite lambda interval and translation-invariance control",
        ["NUM-CG-LAMBDA-CONTINUUM", "NUM-CG-TRANSLATION"],
        status="PASS" if passed else "FAIL",
        seed=seed,
        sample_count="six in-interval values and two exact two-node controls",
        expected={
            "inside_interval_positive_semidefinite": True,
            "outside_controls_indefinite": True,
            "aggregated_operator": "independently assembled coarse self/coupling form",
            "consensus_residual_proportional_to_1_minus_lambda": True,
            "two_node_exact_eigenvalues": ["1-lambda", "1+lambda"],
        },
        tolerances={
            "spectral": 1.0e-9,
            "coarse_formula_relative": 1.0e-11,
            "relative_identity": 1.0e-12,
            "symbolic": "exact",
        },
        observed={
            "inside_minimum_eigenvalues": min_inside,
            "coarse_formula_relative_errors": coarse_formula_errors,
            "coarse_minimum_eigenvalues": coarse_minimum_eigenvalues,
            "outside_two_node_minimum_eigenvalues": outside_min,
            "two_node_symbolic_characteristic_polynomial": str(
                symbolic_characteristic
            ),
            "two_node_symbolic_eigenvalues": symbolic_eigenvalues,
            "consensus_residuals": residuals,
            "scaled_residual_spread": scaled_spread,
            "convex_decomposition_max_relative_error": convex_error,
        },
        interpretation="For every tested lambda, the coarse parameters are assembled independently from block sums and compared with the congruence. The exact two-node symbolic witness establishes sharp failure outside the interval.",
    )


def check_cg_pair_merge() -> dict[str, Any]:
    seed = 20260728
    rng = np.random.default_rng(seed)
    n, k = 7, 2
    m = rng.standard_normal((n * k, n * k))
    lam = (m + m.T) / 2
    maps = [
        [0, 0, 1, 2, 3, 4, 5],
        [0, 1, 1, 2, 3, 4],
        [0, 1, 1, 2, 3],
        [0, 1, 2, 2],
    ]
    scalar_product = np.eye(n)
    current = lam.copy()
    for assignment in maps:
        p = np.zeros((len(assignment), max(assignment) + 1))
        p[np.arange(len(assignment)), assignment] = 1.0
        scalar_product = scalar_product @ p
        s = np.kron(p, np.eye(k))
        current = s.T @ current @ s
    one_shot_s = np.kron(scalar_product, np.eye(k))
    one_shot = one_shot_s.T @ lam @ one_shot_s
    error = float(np.linalg.norm(current - one_shot, ord="fro"))
    expected_assignment = np.array([0, 0, 1, 1, 1, 2, 2])
    assignment_error = float(
        np.linalg.norm(scalar_product - incidence_map(expected_assignment.tolist(), 1))
    )
    passed = error <= 1.0e-12 and assignment_error == 0
    return result(
        "CHK-CG-PAIR-MERGE",
        "Pair-merge factorization of a partition congruence",
        ["NUM-CG-PAIR-MERGE"],
        status="PASS" if passed else "FAIL",
        seed=seed,
        sample_count="one matrix and four pair merges",
        expected={
            "sequential_minus_one_shot_residual": "<= declared tolerance",
            "incidence_product_residual": "<= declared tolerance",
            "pair_merge_count": 4,
        },
        tolerances={"absolute_matrix_residual": 1.0e-12},
        observed={"matrix_residual": error, "incidence_product_residual": assignment_error},
        interpretation="The check is a floating-point evaluation of matrix associativity already proved in the text.",
    )


def check_cg_biadditive() -> dict[str, Any]:
    seed = 20260728
    rng = np.random.default_rng(seed)
    n, k = 8, 3
    x = rng.uniform(0.2, 2.0, size=n)
    m = random_spd(rng, k)
    a = random_spd(rng, k)
    weights = {(i, j): x[i] * x[j] * m for i in range(n) for j in range(i + 1, n)}
    self_terms = [x[i] * a for i in range(n)]
    assignments = [0, 0, 0, 1, 1, 2, 2, 2]
    s = incidence_map(assignments, k)
    precision, _ = assemble_interaction(self_terms, weights)
    coarse = s.T @ precision @ s
    xc = np.array([sum(x[i] for i in range(n) if assignments[i] == c) for c in range(3)])
    predicted_weights = {(i, j): xc[i] * xc[j] * m for i in range(3) for j in range(i + 1, 3)}
    predicted_self = [xc[i] * a for i in range(3)]
    predicted, _ = assemble_interaction(predicted_self, predicted_weights)
    error = fro_relative(coarse, predicted)
    passed = error <= 1.0e-12
    return result(
        "CHK-CG-BIADDITIVE",
        "Bi-additive coupling and additive self closure",
        ["NUM-CG-BIADDITIVE"],
        status="PASS" if passed else "FAIL",
        seed=seed,
        sample_count=1,
        expected={"coarse_parameters_equal_block-summed_form": True},
        tolerances={"relative_matrix": 1.0e-12},
        observed={"relative_matrix_error": error, "coarse_node_weights": xc},
        interpretation="The equality is checked directly from the fine and coarse assembled operators.",
    )


def check_cg_epsilon_divergence() -> dict[str, Any]:
    seed = 20260728
    rng = np.random.default_rng(seed)
    n, r = 12, 6
    m = n - r
    lam = random_spd(rng, n)
    q, _ = np.linalg.qr(rng.standard_normal((n, n)))
    b, bp = q[:, :r], q[:, r:]
    c_parallel = np.linalg.inv(b.T @ lam @ b)
    cov_p = np.linalg.inv(lam)
    volume = 0.5 * np.linalg.slogdet(bp.T @ cov_p @ bp)[1]
    eps_values = [1.0e-3, 1.0e-4, 1.0e-6, 1.0e-8]
    measured: dict[str, float] = {}
    predicted_leading: dict[str, float] = {}
    remainders: dict[str, float] = {}
    trace_perp = float(np.trace(bp.T @ lam @ bp))
    for eps in eps_values:
        cov_q = b @ c_parallel @ b.T + eps * bp @ bp.T
        value = gaussian_kl(np.zeros(n), cov_q, np.zeros(n), cov_p)
        leading = 0.5 * m * math.log(1.0 / eps) - 0.5 * m + volume
        measured[str(eps)] = value
        predicted_leading[str(eps)] = leading
        remainders[str(eps)] = value - leading
    expected_remainders = {str(eps): 0.5 * eps * trace_perp for eps in eps_values}
    remainder_error = max(
        abs(remainders[str(eps)] - expected_remainders[str(eps)]) for eps in eps_values
    )
    slope = measured[str(1.0e-8)] - measured[str(1.0e-6)]
    predicted_slope = 0.5 * m * math.log(100.0)
    passed = abs(slope - predicted_slope - (expected_remainders[str(1.0e-8)] - expected_remainders[str(1.0e-6)])) <= 1.0e-8 and remainder_error <= 1.0e-8
    return result(
        "CHK-CG-EPSILON-DIVERGENCE",
        "Regularized identification divergence",
        ["NUM-CG-EPS-DIVERGENCE"],
        status="PASS" if passed else "FAIL",
        seed=seed,
        sample_count={"epsilon_values": eps_values},
        expected={"leading_slope": "(m/2) log(1/epsilon)", "remainder": "(epsilon/2) trace(B_perp^T Lambda B_perp)"},
        tolerances={"absolute_identity": 1.0e-8},
        observed={
            "m": m,
            "measured_costs": measured,
            "leading_predictions": predicted_leading,
            "measured_remainders": remainders,
            "expected_remainders": expected_remainders,
            "maximum_remainder_error": remainder_error,
            "two_decade_increment": slope,
            "predicted_leading_two_decade_increment": predicted_slope,
        },
        interpretation="The current check evaluates the full Gaussian KL and the analytic asymptotic expression independently.",
    )


GapStep = namedtuple(
    "GapStep",
    (
        "value",
        "left_block",
        "right_block",
        "singular_values",
        "scipy_singular_values",
        "numpy_singular_values",
        "min_one_minus_rho_squared",
        "cholesky_residual",
        "solve_residual",
        "residual_tolerance",
        "backward_error",
        "clipping_applied",
        "clipping_amount",
        "residual_derived_clip_bound",
        "boundary_fallback_applied",
        "high_precision_fallback_applied",
        "conditioning_triggered",
        "precision_condition_number",
        "boundary_acceptance_limit",
        "evaluation_method",
    ),
)
GapStep.__doc__ = "One two-block increment in a declared telescoping merge order."

GapResult = namedtuple(
    "GapResult",
    (
        "value",
        "steps",
        "merge_order",
        "backward_error_bound",
        "singular_values",
        "min_one_minus_rho_squared",
        "maximum_cholesky_residual",
        "clipping_applied",
        "clipping_amount",
        "residual_derived_clip_bound",
        "boundary_fallback_applied",
        "high_precision_fallback_applied",
        "conditioning_triggered",
    ),
)
GapResult.__doc__ = "Stable factorization-gap value and diagnostics."

FactorizationProtocolCase = namedtuple(
    "FactorizationProtocolCase",
    (
        "case_id",
        "stratum",
        "dimension",
        "condition_number",
        "replica",
        "matrix_seed",
        "partition",
    ),
)
FactorizationCaseRecord = namedtuple(
    "FactorizationCaseRecord",
    (
        "case_id",
        "stratum",
        "dimension",
        "condition_number",
        "achieved_condition_number",
        "matrix_digest",
        "partition_digest",
        "value",
        "backward_error_bound",
        "clipping_applied",
        "boundary_fallback_applied",
        "high_precision_fallback_applied",
    ),
)
FactorizationHighPrecisionControl = namedtuple(
    "FactorizationHighPrecisionControl",
    ("case_id", "decimal_digits", "reference_value"),
)
FactorizationProtocolReport = namedtuple(
    "FactorizationProtocolReport",
    (
        "protocol_name",
        "seed",
        "schedule_digest",
        "historical_generator_recovered",
        "cases",
        "high_precision_controls",
        "case_failures",
    ),
)


def _even_power_of_two_exponent(matrix: np.ndarray) -> int:
    """Return an even binary exponent that range-normalizes ``matrix``."""

    maximum = float(np.max(np.abs(matrix), initial=0.0))
    if maximum == 0.0:
        return 0
    exponent = math.frexp(maximum)[1]
    return exponent if exponent % 2 == 0 else exponent + 1


def _power_of_two_scaled(matrix: np.ndarray, exponent: int) -> np.ndarray:
    """Scale by an exact power of two while suppressing harmless underflow."""

    with np.errstate(under="ignore"):
        return np.ldexp(matrix, -exponent)


def _power_of_two_scaling_loses_nonzero(
    matrix: np.ndarray, scaled: np.ndarray
) -> bool:
    return bool(np.any((matrix != 0.0) & (scaled == 0.0)))


def _safe_symmetric_midpoint(matrix: np.ndarray) -> np.ndarray:
    """Midpoint transpose pairs without changing already equal entries."""

    transposed = matrix.T
    with np.errstate(under="ignore"):
        midpoint = 0.5 * matrix + 0.5 * transposed
    return np.where(matrix == transposed, matrix, midpoint)


def _adaptive_mp_digits(matrix: np.ndarray, *, minimum: int) -> int:
    """Resolve the full binary64 dynamic range with guard digits."""

    nonzero = np.abs(matrix[matrix != 0.0])
    if nonzero.size == 0:
        return minimum
    largest_exponent = math.frexp(float(np.max(nonzero)))[1]
    smallest_exponent = math.frexp(float(np.min(nonzero)))[1]
    dynamic_decimal_digits = math.ceil(
        (largest_exponent - smallest_exponent) * math.log10(2.0)
    )
    return max(minimum, dynamic_decimal_digits + 80)


def _stable_relative_matrix_residual(
    reference: np.ndarray, approximation: np.ndarray
) -> float:
    """Compute a range-safe Frobenius relative residual."""

    exponent = _even_power_of_two_exponent(reference)
    reference_scaled = _power_of_two_scaled(reference, exponent)
    approximation_scaled = _power_of_two_scaled(approximation, exponent)
    denominator = max(
        float(np.linalg.norm(reference_scaled, ord="fro")),
        np.finfo(float).tiny,
    )
    return float(
        np.linalg.norm(reference_scaled - approximation_scaled, ord="fro")
        / denominator
    )


def _validated_precision(lam: np.ndarray) -> tuple[np.ndarray, np.ndarray, float]:
    raw = np.asarray(lam)
    if np.iscomplexobj(raw):
        raise TypeError("factorization gap requires a real precision matrix")
    try:
        matrix = np.asarray(raw, dtype=np.float64)
    except (TypeError, ValueError) as exc:
        raise TypeError("factorization gap requires a numeric precision matrix") from exc
    if matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1] or matrix.shape[0] == 0:
        raise ValueError("factorization gap requires a nonempty square precision matrix")
    if not np.isfinite(matrix).all():
        raise ValueError("factorization gap requires finite precision entries")
    exponent = _even_power_of_two_exponent(matrix)
    matrix_scaled = _power_of_two_scaled(matrix, exponent)
    scaling_lost_nonzero = _power_of_two_scaling_loses_nonzero(
        matrix, matrix_scaled
    )
    scaled_norm = max(
        float(np.linalg.norm(matrix_scaled, ord="fro")),
        np.finfo(float).tiny,
    )
    symmetry_residual = float(
        np.linalg.norm(matrix_scaled - matrix_scaled.T, ord="fro") / scaled_norm
    )
    symmetry_tolerance = 64.0 * matrix.shape[0] * np.finfo(float).eps
    if symmetry_residual > symmetry_tolerance:
        raise ValueError(
            "factorization gap precision is nonsymmetric beyond its scale-aware tolerance"
        )
    # Work on a globally range-normalized matrix whenever that exact power-of-
    # two scaling preserves every nonzero.  If the dynamic range is too large,
    # keep the exact binary64 entries and require an exact-dyadic MP Cholesky
    # certificate before any binary64 diagnostic can accept the input.
    matrix = _safe_symmetric_midpoint(
        matrix if scaling_lost_nonzero else matrix_scaled
    )
    high_precision_cholesky = None
    if scaling_lost_nonzero:
        try:
            with mpmath.workdps(_adaptive_mp_digits(matrix, minimum=200)):
                high_precision_cholesky = mpmath.cholesky(
                    _mp_exact_matrix(matrix), tol=mpmath.mpf("0")
                )
        except (ValueError, ZeroDivisionError) as high_precision_exc:
            raise ValueError(
                "factorization gap requires a positive definite precision"
            ) from high_precision_exc
    try:
        cholesky = np.linalg.cholesky(matrix)
    except np.linalg.LinAlgError as exc:
        # A finite binary64 SPD matrix can outstrip a binary64 diagnostic even
        # though its exact stored entries remain positive definite.  Confirm
        # that exact input by high-precision Cholesky before rejecting it.
        try:
            if high_precision_cholesky is None:
                with mpmath.workdps(_adaptive_mp_digits(matrix, minimum=200)):
                    high_precision_cholesky = mpmath.cholesky(
                        _mp_exact_matrix(matrix), tol=mpmath.mpf("0")
                    )
            cholesky = np.asarray(
                [
                    [
                        float(high_precision_cholesky[row, column])
                        for column in range(matrix.shape[0])
                    ]
                    for row in range(matrix.shape[0])
                ],
                dtype=float,
            )
        except (ValueError, ZeroDivisionError) as high_precision_exc:
            raise ValueError(
                "factorization gap requires a positive definite precision"
            ) from high_precision_exc
    cholesky_exponent = _even_power_of_two_exponent(matrix)
    matrix_for_residual = _power_of_two_scaled(matrix, cholesky_exponent)
    cholesky_for_residual = _power_of_two_scaled(
        cholesky, cholesky_exponent // 2
    )
    cholesky_residual = _stable_relative_matrix_residual(
        matrix_for_residual,
        cholesky_for_residual @ cholesky_for_residual.T,
    )
    if not math.isfinite(cholesky_residual):
        raise ValueError("factorization gap Cholesky residual is nonfinite")
    return matrix, cholesky, cholesky_residual


def validate_partition(
    lam: np.ndarray, blocks: Any
) -> tuple[tuple[int, ...], ...]:
    """Validate an SPD precision and an exact, nonempty coordinate partition."""

    matrix, _, _ = _validated_precision(lam)
    if isinstance(blocks, (str, bytes)):
        raise TypeError("partition must be an iterable of index blocks")
    try:
        raw_blocks = list(blocks)
    except TypeError as exc:
        raise TypeError("partition must be an iterable of index blocks") from exc
    if not raw_blocks:
        raise ValueError("partition must contain at least one block")
    normalized: list[tuple[int, ...]] = []
    seen: set[int] = set()
    for raw_block in raw_blocks:
        if isinstance(raw_block, (str, bytes)):
            raise TypeError("partition blocks must contain integer indices")
        try:
            entries = list(raw_block)
        except TypeError as exc:
            raise TypeError("partition blocks must be iterable") from exc
        if not entries:
            raise ValueError("partition blocks must be nonempty")
        block: list[int] = []
        for entry in entries:
            if isinstance(entry, (bool, np.bool_)) or not isinstance(
                entry, (int, np.integer)
            ):
                raise TypeError("partition indices must be integers")
            index = int(entry)
            if index < 0 or index >= matrix.shape[0]:
                raise ValueError("partition index is outside the precision matrix")
            if index in seen:
                raise ValueError("partition blocks overlap or repeat an index")
            seen.add(index)
            block.append(index)
        normalized.append(tuple(block))
    if seen != set(range(matrix.shape[0])):
        raise ValueError("partition must cover every precision coordinate exactly once")
    return tuple(normalized)


def _mp_exact_float(value: float) -> mpmath.mpf:
    numerator, denominator = float(value).as_integer_ratio()
    return mpmath.mpf(numerator) / denominator


def _mp_exact_matrix(matrix: np.ndarray) -> mpmath.matrix:
    return mpmath.matrix(
        [[_mp_exact_float(float(value)) for value in row] for row in matrix]
    )


def _mp_left_solve(lower: mpmath.matrix, right: mpmath.matrix) -> mpmath.matrix:
    solved = mpmath.matrix(lower.rows, right.cols)
    for column in range(right.cols):
        vector = mpmath.lu_solve(lower, right[:, column])
        for row in range(lower.rows):
            solved[row, column] = vector[row]
    return solved


def _mp_cholesky_logdet(
    matrix: mpmath.matrix,
) -> tuple[mpmath.matrix, mpmath.mpf]:
    """Certify MP positive definiteness and return its Cholesky logdet."""

    cholesky = mpmath.cholesky(matrix, tol=mpmath.mpf("0"))
    logdet = 2 * mpmath.fsum(
        mpmath.log(cholesky[index, index])
        for index in range(cholesky.rows)
    )
    if not mpmath.isfinite(logdet):
        raise ValueError("high-precision SPD log determinant is nonfinite")
    return cholesky, +logdet


def _high_precision_two_block(
    matrix: np.ndarray,
    left: tuple[int, ...],
    right: tuple[int, ...],
    *,
    digits: int = 200,
) -> tuple[mpmath.mpf, tuple[mpmath.mpf, ...]]:
    """Evaluate the exact binary64 input at high precision on the fallback path."""

    with mpmath.workdps(_adaptive_mp_digits(matrix, minimum=digits)):
        first = _mp_exact_matrix(matrix[np.ix_(left, left)])
        second = _mp_exact_matrix(matrix[np.ix_(right, right)])
        cross = _mp_exact_matrix(matrix[np.ix_(left, right)])
        whole = _mp_exact_matrix(matrix[np.ix_(left + right, left + right)])
        _, logdet_whole = _mp_cholesky_logdet(whole)
        left_cholesky, logdet_first = _mp_cholesky_logdet(first)
        right_cholesky, logdet_second = _mp_cholesky_logdet(second)
        left_solved = _mp_left_solve(left_cholesky, cross)
        canonical = _mp_left_solve(right_cholesky, left_solved.T).T
        singular = mpmath.svd(canonical, compute_uv=False)
        rho_squared = tuple(
            sorted(
                (singular[index] * singular[index] for index in range(singular.rows)),
                reverse=True,
            )
        )
        if rho_squared and rho_squared[0] >= 1:
            raise ValueError(
                "high-precision exact-input canonical correlation is not below one"
            )
        gap = (logdet_first + logdet_second - logdet_whole) / 2
        if not mpmath.isfinite(gap) or gap < 0:
            raise ValueError("high-precision exact-input gap is not finite and nonnegative")
        return +gap, tuple(+value for value in rho_squared)


def _high_precision_partition_gap(
    matrix: np.ndarray, partition: tuple[tuple[int, ...], ...], *, digits: int
) -> mpmath.mpf:
    with mpmath.workdps(_adaptive_mp_digits(matrix, minimum=digits)):
        whole_matrix = _mp_exact_matrix(matrix)
        _, whole_logdet = _mp_cholesky_logdet(whole_matrix)
        block_log_sum = mpmath.mpf("0")
        for block in partition:
            block_matrix = _mp_exact_matrix(matrix[np.ix_(block, block)])
            _, block_logdet = _mp_cholesky_logdet(block_matrix)
            block_log_sum += block_logdet
        return +(block_log_sum - whole_logdet) / 2


def _outward_float_upper(value: mpmath.mpf, *, digits: int = 220) -> float:
    with mpmath.workdps(digits):
        if value < 0 or not mpmath.isfinite(value):
            raise ValueError(
                "outward upper conversion requires a finite nonnegative value"
            )
        rounded = float(value)
        if _mp_exact_float(rounded) < value:
            rounded = math.nextafter(rounded, math.inf)
        return rounded


def _roundoff_scale(*values: float, dimension: int, multiplier: float = 64.0) -> float:
    magnitude = max((abs(float(value)) for value in values), default=0.0)
    magnitude = max(magnitude, np.finfo(float).tiny)
    return multiplier * max(1, dimension) * np.finfo(float).eps * magnitude


def _step_result(step: GapStep) -> GapResult:
    return GapResult(
        value=step.value,
        steps=(step,),
        merge_order=((step.left_block, step.right_block, step.left_block + step.right_block),),
        backward_error_bound=step.backward_error,
        singular_values=(step.singular_values,),
        min_one_minus_rho_squared=step.min_one_minus_rho_squared,
        maximum_cholesky_residual=step.cholesky_residual,
        clipping_applied=step.clipping_applied,
        clipping_amount=step.clipping_amount,
        residual_derived_clip_bound=step.residual_derived_clip_bound,
        boundary_fallback_applied=step.boundary_fallback_applied,
        high_precision_fallback_applied=step.high_precision_fallback_applied,
        conditioning_triggered=step.conditioning_triggered,
    )


def _positive_mp_to_float(value: mpmath.mpf) -> float:
    """Preserve the sign of a positive MP diagnostic after binary64 cast."""

    if value <= 0 or not mpmath.isfinite(value):
        raise ValueError("high-precision positive diagnostic left its domain")
    rounded = float(value)
    return rounded if rounded > 0.0 else math.nextafter(0.0, 1.0)


def _high_precision_only_two_block_result(
    matrix: np.ndarray,
    left: tuple[int, ...],
    right: tuple[int, ...],
    *,
    precision_condition_number: float,
    reason: str,
) -> GapResult:
    """Fail over to an exact-dyadic MP value when binary64 diagnostics fail."""

    high_precision_gap, exact_squared = _high_precision_two_block(
        matrix, left, right, digits=200
    )
    with mpmath.workdps(_adaptive_mp_digits(matrix, minimum=220)):
        singular_values = tuple(
            float(mpmath.sqrt(value)) for value in exact_squared
        )
        exact_max_squared = exact_squared[0] if exact_squared else mpmath.mpf("0")
        min_one_minus = _positive_mp_to_float(
            mpmath.mpf(1) - exact_max_squared
        )
    unit_roundoff = np.finfo(float).eps / 2.0
    gamma_n = matrix.shape[0] * unit_roundoff / (
        1.0 - matrix.shape[0] * unit_roundoff
    )
    residual_tolerance = float(64.0 * gamma_n)
    step = GapStep(
        value=float(high_precision_gap),
        left_block=left,
        right_block=right,
        singular_values=singular_values,
        scipy_singular_values=(),
        numpy_singular_values=(),
        min_one_minus_rho_squared=min_one_minus,
        cholesky_residual=0.0,
        solve_residual=0.0,
        residual_tolerance=residual_tolerance,
        backward_error=0.0,
        clipping_applied=False,
        clipping_amount=0.0,
        residual_derived_clip_bound=0.0,
        boundary_fallback_applied=False,
        high_precision_fallback_applied=True,
        conditioning_triggered=True,
        precision_condition_number=precision_condition_number,
        boundary_acceptance_limit=float(
            64.0 * matrix.shape[0] * np.finfo(float).eps
        ),
        evaluation_method=f"exact-binary64-mpmath-200d-{reason}-fallback",
    )
    return _step_result(step)


def two_block_factorization_gap(
    lam: np.ndarray, left_block: Any, right_block: Any
) -> GapResult:
    """Compute a stable two-block determinant gap from canonical correlations."""

    matrix, _, _ = _validated_precision(lam)
    left, right = validate_partition(matrix, [left_block, right_block])
    first = matrix[np.ix_(left, left)]
    second = matrix[np.ix_(right, right)]
    cross = matrix[np.ix_(left, right)]
    exact_block_diagonal = not np.count_nonzero(cross)
    global_exponent = _even_power_of_two_exponent(matrix)
    global_probe = _power_of_two_scaled(matrix, global_exponent)
    global_scaling_lost = _power_of_two_scaling_loses_nonzero(
        matrix, global_probe
    )
    try:
        with np.errstate(over="ignore", under="ignore", invalid="ignore"):
            precision_condition_number = (
                math.inf
                if global_scaling_lost
                else float(np.linalg.cond(global_probe, p=2))
            )
    except np.linalg.LinAlgError:
        precision_condition_number = math.inf
    conditioning_triggered = bool(
        not math.isfinite(precision_condition_number)
        or precision_condition_number * np.finfo(float).eps
        >= FACTORIZATION_CONDITIONING_TRIGGER
    )
    if global_scaling_lost or not math.isfinite(precision_condition_number):
        return _high_precision_only_two_block_result(
            matrix,
            left,
            right,
            precision_condition_number=precision_condition_number,
            reason="range-or-condition",
        )

    try:
        left_exponent = _even_power_of_two_exponent(first)
        right_exponent = _even_power_of_two_exponent(second)
        first_scaled = _power_of_two_scaled(first, left_exponent)
        second_scaled = _power_of_two_scaled(second, right_exponent)
        cross_scaled = _power_of_two_scaled(
            cross, left_exponent // 2 + right_exponent // 2
        )
        left_cholesky = np.linalg.cholesky(first_scaled)
        right_cholesky = np.linalg.cholesky(second_scaled)

        left_solved = sla.solve_triangular(
            left_cholesky, cross_scaled, lower=True, check_finite=False
        )
        canonical = sla.solve_triangular(
            right_cholesky, left_solved.T, lower=True, check_finite=False
        ).T
        scipy_singular = np.asarray(
            sla.svdvals(canonical, check_finite=False), dtype=float
        )

        # A second binary64 solve is a boundary diagnostic only.  The ordinary
        # value path remains the SciPy triangular-solve construction above.
        numpy_left_solved = np.linalg.solve(left_cholesky, cross_scaled)
        numpy_canonical = np.linalg.solve(
            right_cholesky, numpy_left_solved.T
        ).T
        numpy_singular = np.asarray(
            np.linalg.svd(numpy_canonical, compute_uv=False), dtype=float
        )
    except (np.linalg.LinAlgError, ValueError, FloatingPointError):
        return _high_precision_only_two_block_result(
            matrix,
            left,
            right,
            precision_condition_number=precision_condition_number,
            reason="binary64-linear-algebra",
        )
    if not np.isfinite(scipy_singular).all() or not np.isfinite(numpy_singular).all():
        return _high_precision_only_two_block_result(
            matrix,
            left,
            right,
            precision_condition_number=precision_condition_number,
            reason="binary64-svd",
        )
    scipy_squared = scipy_singular * scipy_singular
    numpy_squared = numpy_singular * numpy_singular
    raw_max_squared = max(
        float(np.max(scipy_squared, initial=0.0)),
        float(np.max(numpy_squared, initial=0.0)),
    )
    boundary_acceptance_limit = float(
        64.0 * matrix.shape[0] * np.finfo(float).eps
    )
    first_scale = max(
        float(np.linalg.norm(first_scaled, ord=np.inf)), np.finfo(float).tiny
    )
    second_scale = max(
        float(np.linalg.norm(second_scaled, ord=np.inf)), np.finfo(float).tiny
    )
    cholesky_residual = max(
        float(
            np.linalg.norm(
                first_scaled - left_cholesky @ left_cholesky.T, ord=np.inf
            )
            / first_scale
        ),
        float(
            np.linalg.norm(
                second_scaled - right_cholesky @ right_cholesky.T,
                ord=np.inf,
            )
            / second_scale
        ),
    )
    solve_scale = max(
        float(np.linalg.norm(left_cholesky, ord=np.inf))
        * float(np.linalg.norm(canonical, ord=np.inf))
        * float(np.linalg.norm(right_cholesky.T, ord=np.inf))
        + float(np.linalg.norm(cross_scaled, ord=np.inf)),
        np.finfo(float).tiny,
    )
    solve_residual = float(
        np.linalg.norm(
            left_cholesky @ canonical @ right_cholesky.T - cross_scaled,
            ord=np.inf,
        )
        / solve_scale
    )
    unit_roundoff = np.finfo(float).eps / 2.0
    gamma_n = matrix.shape[0] * unit_roundoff / (
        1.0 - matrix.shape[0] * unit_roundoff
    )
    residual_tolerance = float(64.0 * gamma_n)
    if (
        not math.isfinite(cholesky_residual)
        or not math.isfinite(solve_residual)
        or cholesky_residual > residual_tolerance
        or solve_residual > residual_tolerance
    ):
        return _high_precision_only_two_block_result(
            matrix,
            left,
            right,
            precision_condition_number=precision_condition_number,
            reason="binary64-residual-health",
        )
    backward_error = math.nextafter(
        max(cholesky_residual, solve_residual),
        math.inf,
    )

    raw_margin = 1.0 - raw_max_squared
    boundary_fallback = bool(raw_margin <= boundary_acceptance_limit)
    high_precision_fallback = boundary_fallback or (
        conditioning_triggered and not exact_block_diagonal
    )
    clipping_amount = max(0.0, raw_max_squared - 1.0)
    clipping_applied = clipping_amount > 0.0
    residual_derived_clip_bound = 0.0
    if boundary_fallback:
        high_precision_gap, exact_squared = _high_precision_two_block(
            matrix, left, right, digits=200
        )
        fallback_digits = _adaptive_mp_digits(matrix, minimum=220)
        with mpmath.workdps(fallback_digits):
            exact_max_squared = (
                exact_squared[0] if exact_squared else mpmath.mpf("0")
            )
            raw_max_exact = _mp_exact_float(raw_max_squared)
            evaluation_discrepancy = abs(raw_max_exact - exact_max_squared)
            residual_derived_clip_bound = _outward_float_upper(
                evaluation_discrepancy, digits=fallback_digits
            )
            if clipping_applied and evaluation_discrepancy > _mp_exact_float(
                boundary_acceptance_limit
            ):
                raise ValueError(
                    "binary64 canonical-correlation discrepancy exceeds the operational boundary guard"
                )
            min_one_minus = _positive_mp_to_float(
                mpmath.mpf(1) - exact_max_squared
            )
        if clipping_applied and clipping_amount > residual_derived_clip_bound:
            raise ValueError(
                "binary64 canonical-correlation excursion exceeds its exact-input allowance"
            )
        value = float(high_precision_gap)
        evaluation_method = "exact-binary64-mpmath-200d-boundary-fallback"
    elif exact_block_diagonal:
        value = 0.0
        min_one_minus = 1.0
        evaluation_method = "exact-zero-cross-block-control"
    elif conditioning_triggered:
        high_precision_gap, exact_squared = _high_precision_two_block(
            matrix, left, right, digits=200
        )
        value = float(high_precision_gap)
        with mpmath.workdps(_adaptive_mp_digits(matrix, minimum=220)):
            exact_max_squared = (
                exact_squared[0] if exact_squared else mpmath.mpf("0")
            )
            min_one_minus = _positive_mp_to_float(
                mpmath.mpf(1) - exact_max_squared
            )
        evaluation_method = "exact-binary64-mpmath-200d-conditioning-fallback"
    else:
        if raw_max_squared >= 1.0:
            raise ValueError("canonical correlation lies outside the log1p domain")
        value = -0.5 * math.fsum(math.log1p(-float(square)) for square in scipy_squared)
        min_one_minus = float(np.min(1.0 - scipy_squared, initial=1.0))
        evaluation_method = "scipy-cholesky-triangular-solve-svd-log1p"
    if not math.isfinite(value) or value < 0.0 or min_one_minus <= 0.0:
        raise ValueError("factorization gap evaluation left its finite positive domain")

    step = GapStep(
        value=value,
        left_block=left,
        right_block=right,
        singular_values=tuple(float(value) for value in scipy_singular),
        scipy_singular_values=tuple(float(value) for value in scipy_singular),
        numpy_singular_values=tuple(float(value) for value in numpy_singular),
        min_one_minus_rho_squared=min_one_minus,
        cholesky_residual=cholesky_residual,
        solve_residual=solve_residual,
        residual_tolerance=residual_tolerance,
        backward_error=backward_error,
        clipping_applied=clipping_applied,
        clipping_amount=clipping_amount,
        residual_derived_clip_bound=residual_derived_clip_bound,
        boundary_fallback_applied=boundary_fallback,
        high_precision_fallback_applied=high_precision_fallback,
        conditioning_triggered=conditioning_triggered,
        precision_condition_number=precision_condition_number,
        boundary_acceptance_limit=boundary_acceptance_limit,
        evaluation_method=evaluation_method,
    )
    return _step_result(step)


def factorization_gap(lam: np.ndarray, blocks: Any) -> GapResult:
    """Telescope stable two-block increments along the declared block order."""

    matrix, _, _ = _validated_precision(lam)
    partition = validate_partition(matrix, blocks)
    if len(partition) == 1:
        return GapResult(
            value=0.0,
            steps=(),
            merge_order=(),
            backward_error_bound=0.0,
            singular_values=(),
            min_one_minus_rho_squared=1.0,
            maximum_cholesky_residual=0.0,
            clipping_applied=False,
            clipping_amount=0.0,
            residual_derived_clip_bound=0.0,
            boundary_fallback_applied=False,
            high_precision_fallback_applied=False,
            conditioning_triggered=False,
        )

    merged = partition[0]
    steps: list[GapStep] = []
    merge_order: list[
        tuple[tuple[int, ...], tuple[int, ...], tuple[int, ...]]
    ] = []
    for current in partition[1:]:
        combined = merged + current
        submatrix = matrix[np.ix_(combined, combined)]
        local_left = tuple(range(len(merged)))
        local_right = tuple(range(len(merged), len(combined)))
        local = two_block_factorization_gap(submatrix, local_left, local_right)
        step = local.steps[0]._replace(left_block=merged, right_block=current)
        steps.append(step)
        merge_order.append((merged, current, combined))
        merged = combined

    total = math.fsum(step.value for step in steps)
    backward_error_bound = math.fsum(step.backward_error for step in steps)
    return GapResult(
        value=total,
        steps=tuple(steps),
        merge_order=tuple(merge_order),
        backward_error_bound=backward_error_bound,
        singular_values=tuple(step.singular_values for step in steps),
        min_one_minus_rho_squared=min(
            step.min_one_minus_rho_squared for step in steps
        ),
        maximum_cholesky_residual=max(step.cholesky_residual for step in steps),
        clipping_applied=any(step.clipping_applied for step in steps),
        clipping_amount=max(step.clipping_amount for step in steps),
        residual_derived_clip_bound=max(
            step.residual_derived_clip_bound for step in steps
        ),
        boundary_fallback_applied=any(
            step.boundary_fallback_applied for step in steps
        ),
        high_precision_fallback_applied=any(
            step.high_precision_fallback_applied for step in steps
        ),
        conditioning_triggered=any(step.conditioning_triggered for step in steps),
    )


def _factorization_case_seed(
    case_id: str, dimension: int, condition_number: float, stratum: str, *, seed: int
) -> int:
    material = (
        f"{seed}|{case_id}|{dimension}|{condition_number:.17g}|{stratum}".encode()
    )
    return int.from_bytes(hashlib.sha256(material).digest()[:8], "big", signed=False)


def _factorization_partition(
    dimension: int, stratum: str
) -> tuple[tuple[int, ...], ...]:
    if stratum == "nested_refinement" and dimension >= 3:
        cut = max(1, dimension // 3)
        return (
            tuple(range(cut)),
            tuple(range(cut, 2 * cut)),
            tuple(range(2 * cut, dimension)),
        )
    cut = dimension // 2
    return (tuple(range(cut)), tuple(range(cut, dimension)))


def _default_factorization_schedule(
    seed: int,
) -> tuple[FactorizationProtocolCase, ...]:
    cases: list[FactorizationProtocolCase] = []
    for dimension in range(2, 17):
        for condition_number in FACTORIZATION_PROTOCOL_CONDITIONS:
            for replica in range(20):
                case_id = (
                    f"general-d{dimension}-c{condition_number:.0e}-r{replica:02d}"
                )
                stratum = "general"
                cases.append(
                    FactorizationProtocolCase(
                        case_id=case_id,
                        stratum=stratum,
                        dimension=dimension,
                        condition_number=condition_number,
                        replica=replica,
                        matrix_seed=_factorization_case_seed(
                            case_id,
                            dimension,
                            condition_number,
                            stratum,
                            seed=seed,
                        ),
                        partition=_factorization_partition(dimension, stratum),
                    )
                )
    for stratum, count in FACTORIZATION_PROTOCOL_STRATUM_COUNTS.items():
        if stratum == "general":
            continue
        for replica in range(count):
            dimension = 2 + replica % 15
            condition_number = FACTORIZATION_PROTOCOL_CONDITIONS[
                replica % len(FACTORIZATION_PROTOCOL_CONDITIONS)
            ]
            case_id = f"{stratum}-{replica:03d}"
            cases.append(
                FactorizationProtocolCase(
                    case_id=case_id,
                    stratum=stratum,
                    dimension=dimension,
                    condition_number=condition_number,
                    replica=replica,
                    matrix_seed=_factorization_case_seed(
                        case_id,
                        dimension,
                        condition_number,
                        stratum,
                        seed=seed,
                    ),
                    partition=_factorization_partition(dimension, stratum),
                )
            )
    if len(cases) != 3138:
        raise RuntimeError("factorization protocol schedule is not exactly 3,138 cases")
    return tuple(cases)


def _regenerate_factorization_case(
    case: Any, *, seed: int
) -> tuple[np.ndarray, tuple[tuple[int, ...], ...]]:
    expected_seed = _factorization_case_seed(
        case.case_id,
        int(case.dimension),
        float(case.condition_number),
        case.stratum,
        seed=seed,
    )
    if int(case.matrix_seed) != expected_seed:
        raise ValueError(f"factorization protocol seed mismatch for {case.case_id}")
    rng = np.random.default_rng(expected_seed)
    dimension = int(case.dimension)
    condition_number = float(case.condition_number)
    spectrum = np.geomspace(1.0, 1.0 / condition_number, dimension)
    partition = _factorization_partition(dimension, case.stratum)
    if tuple(tuple(int(index) for index in block) for block in case.partition) != partition:
        raise ValueError(f"factorization protocol partition mismatch for {case.case_id}")
    if case.stratum == "exact_block_diagonal":
        generated_blocks = []
        for indices in partition:
            orthogonal, _ = np.linalg.qr(
                rng.standard_normal((len(indices), len(indices)))
            )
            generated_blocks.append(
                orthogonal
                @ np.diag(
                    np.geomspace(1.0, 1.0 / condition_number, len(indices))
                )
                @ orthogonal.T
            )
        matrix = np.zeros((dimension, dimension))
        offset = 0
        for block in generated_blocks:
            size = block.shape[0]
            matrix[offset : offset + size, offset : offset + size] = block
            offset += size
    else:
        orthogonal, _ = np.linalg.qr(rng.standard_normal((dimension, dimension)))
        matrix = orthogonal @ np.diag(spectrum) @ orthogonal.T
        if case.stratum == "near_decoupled":
            block_diagonal = np.zeros_like(matrix)
            for indices in partition:
                block_diagonal[np.ix_(indices, indices)] = matrix[
                    np.ix_(indices, indices)
                ]
            matrix = (
                0.999 * block_diagonal
                + 0.001 * matrix
                + np.eye(dimension) * 1.0e-12
            )
        elif case.stratum == "scale":
            matrix *= 10.0 ** ((int(case.replica) % 7) - 3)
        elif case.stratum == "permutation":
            permutation = rng.permutation(dimension)
            matrix = matrix[np.ix_(permutation, permutation)]
            inverse_permutation = np.argsort(permutation)
            partition = tuple(
                tuple(
                    sorted(
                        int(index) for index in inverse_permutation[list(indices)]
                    )
                )
                for indices in partition
            )
    matrix = (matrix + matrix.T) / 2.0
    np.linalg.cholesky(matrix)
    return matrix, partition


def _factorization_matrix_digest(matrix: np.ndarray) -> str:
    return hashlib.sha256(
        np.ascontiguousarray(matrix, dtype=np.float64).tobytes()
    ).hexdigest()


def _factorization_partition_digest(
    partition: tuple[tuple[int, ...], ...]
) -> str:
    normalized = tuple(
        tuple(int(index) for index in block) for block in partition
    )
    return hashlib.sha256(
        json.dumps(normalized, separators=(",", ":")).encode()
    ).hexdigest()


def _factorization_schedule_payload(cases: Any) -> list[dict[str, Any]]:
    fields = (
        "case_id",
        "stratum",
        "dimension",
        "condition_number",
        "replica",
        "matrix_seed",
        "partition",
    )
    return [
        asdict(case)
        if is_dataclass(case)
        else {name: getattr(case, name) for name in fields}
        for case in cases
    ]


def run_factorization_gap_protocol(
    *, seed: int = FACTORIZATION_PROTOCOL_SEED, schedule: Any = None
) -> FactorizationProtocolReport:
    """Run the frozen, case-bound 3,138-case factorization-gap protocol."""

    if seed != FACTORIZATION_PROTOCOL_SEED:
        raise ValueError(
            f"factorization protocol seed must be {FACTORIZATION_PROTOCOL_SEED}"
        )
    cases = (
        tuple(schedule)
        if schedule is not None
        else _default_factorization_schedule(seed)
    )
    if len(cases) != 3138:
        raise ValueError("factorization protocol requires exactly 3,138 cases")
    case_ids = [case.case_id for case in cases]
    if len(set(case_ids)) != len(case_ids):
        raise ValueError("factorization protocol case identities must be unique")
    stratum_counts = {
        name: sum(case.stratum == name for case in cases)
        for name in FACTORIZATION_PROTOCOL_STRATUM_COUNTS
    }
    if stratum_counts != FACTORIZATION_PROTOCOL_STRATUM_COUNTS:
        raise ValueError(
            "factorization protocol stratum counts do not match the frozen schedule"
        )
    for stratum in FACTORIZATION_PROTOCOL_STRATUM_COUNTS:
        stratum_cases = [case for case in cases if case.stratum == stratum]
        if {int(case.dimension) for case in stratum_cases} != set(range(2, 17)):
            raise ValueError(
                f"factorization protocol stratum {stratum} omits a dimension"
            )
        if {
            float(case.condition_number) for case in stratum_cases
        } != set(FACTORIZATION_PROTOCOL_CONDITIONS):
            raise ValueError(
                f"factorization protocol stratum {stratum} omits a condition tier"
            )
    schedule_payload = _factorization_schedule_payload(cases)
    frozen_schedule_payload = _factorization_schedule_payload(
        _default_factorization_schedule(seed)
    )
    if schedule_payload != frozen_schedule_payload:
        raise ValueError(
            "factorization protocol schedule differs from the frozen case-bound schedule"
        )
    schedule_digest = hashlib.sha256(
        json.dumps(schedule_payload, sort_keys=True).encode()
    ).hexdigest()

    records: list[FactorizationCaseRecord] = []
    controls: list[FactorizationHighPrecisionControl] = []
    case_failures: list[dict[str, Any]] = []
    for case in cases:
        matrix = None
        partition = None
        try:
            matrix, partition = _regenerate_factorization_case(case, seed=seed)
            achieved_condition_number = float(np.linalg.cond(matrix))
            if not math.isfinite(achieved_condition_number):
                raise ValueError(
                    "digest-bound achieved condition number is nonfinite"
                )
            gap = factorization_gap(matrix, partition)
            records.append(
                FactorizationCaseRecord(
                    case_id=case.case_id,
                    stratum=case.stratum,
                    dimension=int(case.dimension),
                    condition_number=float(case.condition_number),
                    achieved_condition_number=achieved_condition_number,
                    matrix_digest=_factorization_matrix_digest(matrix),
                    partition_digest=_factorization_partition_digest(partition),
                    value=gap.value,
                    backward_error_bound=gap.backward_error_bound,
                    clipping_applied=gap.clipping_applied,
                    boundary_fallback_applied=gap.boundary_fallback_applied,
                    high_precision_fallback_applied=gap.high_precision_fallback_applied,
                )
            )
            if case.stratum == "mpmath_100_digit":
                with mpmath.workdps(100):
                    reference = _high_precision_partition_gap(
                        matrix, partition, digits=100
                    )
                    reference_text = mpmath.nstr(reference, n=100)
                controls.append(
                    FactorizationHighPrecisionControl(
                        case_id=case.case_id,
                        decimal_digits=100,
                        reference_value=reference_text,
                    )
                )
        except Exception as exc:
            case_failures.append(
                {
                    "case_id": case.case_id,
                    "stratum": case.stratum,
                    "dimension": int(case.dimension),
                    "nominal_condition_number": float(case.condition_number),
                    "matrix_digest": (
                        _factorization_matrix_digest(matrix)
                        if matrix is not None
                        else None
                    ),
                    "partition_digest": (
                        _factorization_partition_digest(partition)
                        if partition is not None
                        else None
                    ),
                    "exception_type": type(exc).__name__,
                    "exception_message": str(exc),
                }
            )
    return FactorizationProtocolReport(
        protocol_name="new-deterministic-factorization-gap-3138",
        seed=seed,
        schedule_digest=schedule_digest,
        historical_generator_recovered=False,
        cases=tuple(records),
        high_precision_controls=tuple(controls),
        case_failures=tuple(case_failures),
    )


def check_cg_factor_gap() -> dict[str, Any]:
    seed = 20260728
    rng = np.random.default_rng(seed)
    n = 8
    lam = random_spd(rng, n, 1.0)
    target_mean = rng.standard_normal(n)
    target_covariance = np.linalg.inv(lam)
    fine_blocks = [[0, 1], [2, 3], [4, 5], [6, 7]]

    optimum_blocks = [
        np.linalg.inv(lam[np.ix_(block, block)]) for block in fine_blocks
    ]
    optimum_covariance = sla.block_diag(*optimum_blocks)
    analytic_gap_result = factorization_gap(lam, fine_blocks)
    analytic_gap = analytic_gap_result.value
    analytic_gap_reference = float(
        _high_precision_partition_gap(
            lam,
            tuple(tuple(block) for block in fine_blocks),
            digits=200,
        )
    )
    direct_optimum_kl = gaussian_kl(
        target_mean,
        optimum_covariance,
        target_mean,
        target_covariance,
    )
    optimum_residual = abs(analytic_gap - direct_optimum_kl)
    analytic_gap_reference_error = abs(analytic_gap - analytic_gap_reference)
    direct_kl_reference_error = abs(direct_optimum_kl - analytic_gap_reference)
    analytic_gap_endpoint_tolerance = _roundoff_scale(
        analytic_gap, analytic_gap_reference, dimension=n, multiplier=512.0
    )
    direct_kl_endpoint_tolerance = _roundoff_scale(
        direct_optimum_kl,
        analytic_gap_reference,
        dimension=n,
        multiplier=1024.0,
    )
    optimum_tolerance = (
        analytic_gap_endpoint_tolerance + direct_kl_endpoint_tolerance
    )

    perturbation_draws = 5000
    perturbation_deltas: list[float] = []
    perturbation_tolerances: list[float] = []
    for _ in range(perturbation_draws):
        perturbed_blocks = []
        for optimum_block in optimum_blocks:
            symmetric = rng.standard_normal(optimum_block.shape)
            symmetric = (symmetric + symmetric.T) / 2.0
            symmetric /= max(float(np.linalg.norm(symmetric, ord="fro")), 1.0)
            amplitude = float(rng.uniform(0.05, 0.25))
            chol = np.linalg.cholesky(optimum_block)
            perturbed_blocks.append(
                chol @ sla.expm(amplitude * symmetric) @ chol.T
            )
        perturbed_covariance = sla.block_diag(*perturbed_blocks)
        perturbed_kl = gaussian_kl(
            target_mean,
            perturbed_covariance,
            target_mean,
            target_covariance,
        )
        perturbation_deltas.append(perturbed_kl - analytic_gap_reference)
        perturbation_tolerances.append(
            _roundoff_scale(
                perturbed_kl,
                analytic_gap_reference,
                dimension=n,
                multiplier=1024.0,
            )
        )
    improving_perturbations = sum(
        delta < -tolerance
        for delta, tolerance in zip(perturbation_deltas, perturbation_tolerances)
    )

    partitions = [
        [[0], [1], [2], [3], [4], [5], [6], [7]],
        [[0, 1], [2], [3], [4], [5], [6], [7]],
        [[0, 1], [2, 3], [4], [5], [6], [7]],
        [[0, 1, 2, 3], [4], [5], [6], [7]],
        [[0, 1, 2, 3], [4, 5], [6, 7]],
        [list(range(n))],
    ]
    gap_results = [factorization_gap(lam, partition) for partition in partitions]
    gaps = [gap.value for gap in gap_results]
    gap_references = [
        float(
            _high_precision_partition_gap(
                lam,
                tuple(tuple(block) for block in partition),
                digits=200,
            )
        )
        for partition in partitions
    ]
    gap_reference_errors = [
        abs(gap.value - reference)
        for gap, reference in zip(gap_results, gap_references)
    ]
    gap_reference_tolerances = [
        _roundoff_scale(
            gap.value, reference, dimension=n, multiplier=512.0
        )
        for gap, reference in zip(gap_results, gap_references)
    ]
    monotonicity_tolerances = [
        left_tolerance + right_tolerance
        for left_tolerance, right_tolerance in zip(
            gap_reference_tolerances, gap_reference_tolerances[1:]
        )
    ]
    high_precision_monotone = all(
        left >= right
        for left, right in zip(gap_references, gap_references[1:])
    )
    binary64_monotone = all(
        left.value + tolerance >= right.value
        for left, right, tolerance in zip(
            gap_results, gap_results[1:], monotonicity_tolerances
        )
    )
    monotone = (
        high_precision_monotone
        and binary64_monotone
        and all(
            error <= tolerance
            for error, tolerance in zip(
                gap_reference_errors, gap_reference_tolerances
            )
        )
    )
    single_block_tolerance = gap_reference_tolerances[-1]

    scales = [1.0, 10.0, 100.0]
    scaled_gap_results = [factorization_gap(c * lam, fine_blocks) for c in scales]
    scaled_gaps = [gap.value for gap in scaled_gap_results]
    scaled_gap_references = [
        float(
            _high_precision_partition_gap(
                c * lam,
                tuple(tuple(block) for block in fine_blocks),
                digits=200,
            )
        )
        for c in scales
    ]
    scaled_gap_reference_errors = [
        abs(gap.value - reference)
        for gap, reference in zip(scaled_gap_results, scaled_gap_references)
    ]
    scaled_gap_endpoint_tolerances = [
        _roundoff_scale(
            gap.value, reference, dimension=n, multiplier=512.0
        )
        for gap, reference in zip(scaled_gap_results, scaled_gap_references)
    ]
    scale_spread = max(scaled_gaps) - min(scaled_gaps)
    scale_reference_spread = max(scaled_gap_references) - min(
        scaled_gap_references
    )
    scale_reference_roundoff_tolerance = _roundoff_scale(
        *scaled_gap_references, dimension=n, multiplier=1024.0
    )
    scale_tolerance = (
        scale_reference_roundoff_tolerance
        + 2.0 * max(scaled_gap_endpoint_tolerances)
    )

    q, _ = np.linalg.qr(rng.standard_normal((n, n)))
    retained_dimension = 4
    b = q[:, :retained_dimension]
    b_perp = q[:, retained_dimension:]
    mu_perp = b_perp.T @ target_mean
    mean_tie_costs = {}
    volume_terms = {}
    for c in scales:
        scaled_lam = c * lam
        marginal_precision = np.linalg.inv(
            b_perp.T @ np.linalg.inv(scaled_lam) @ b_perp
        )
        mean_tie_costs[str(c)] = 0.5 * float(
            mu_perp @ marginal_precision @ mu_perp
        )
        volume_terms[str(c)] = 0.5 * float(
            np.linalg.slogdet(
                b_perp.T @ np.linalg.inv(scaled_lam) @ b_perp
            )[1]
        )
    base_mean_tie = mean_tie_costs["1.0"]
    base_volume = volume_terms["1.0"]
    mean_tie_errors = {
        str(c): abs(mean_tie_costs[str(c)] - c * base_mean_tie)
        for c in scales
    }
    mean_tie_tolerances = {
        str(c): _roundoff_scale(
            mean_tie_costs[str(c)], c * base_mean_tie, dimension=n, multiplier=256.0
        )
        for c in scales
    }
    m = n - retained_dimension
    volume_shift_errors = {
        str(c): abs(
            (volume_terms[str(c)] - base_volume) + 0.5 * m * math.log(c)
        )
        for c in scales
    }
    volume_shift_tolerances = {
        str(c): _roundoff_scale(
            volume_terms[str(c)] - base_volume,
            -0.5 * m * math.log(c),
            dimension=n,
            multiplier=256.0,
        )
        for c in scales
    }
    numerical_outputs_finite = all(
        math.isfinite(value)
        for value in (
            analytic_gap,
            direct_optimum_kl,
            analytic_gap_reference,
            analytic_gap_reference_error,
            direct_kl_reference_error,
            optimum_residual,
            *perturbation_deltas,
            *perturbation_tolerances,
            *gaps,
            *gap_references,
            *gap_reference_errors,
            *gap_reference_tolerances,
            *monotonicity_tolerances,
            *scaled_gaps,
            *scaled_gap_references,
            *scaled_gap_reference_errors,
            *scaled_gap_endpoint_tolerances,
            scale_spread,
            scale_reference_spread,
            scale_reference_roundoff_tolerance,
            scale_tolerance,
            *mean_tie_costs.values(),
            *mean_tie_errors.values(),
            *mean_tie_tolerances.values(),
            *volume_terms.values(),
            *volume_shift_errors.values(),
            *volume_shift_tolerances.values(),
        )
    )
    passed = (
        numerical_outputs_finite
        and analytic_gap_reference_error <= analytic_gap_endpoint_tolerance
        and direct_kl_reference_error <= direct_kl_endpoint_tolerance
        and optimum_residual <= optimum_tolerance
        and improving_perturbations == 0
        and monotone
        and abs(gaps[-1]) <= single_block_tolerance
        and all(
            error <= tolerance
            for error, tolerance in zip(
                scaled_gap_reference_errors, scaled_gap_endpoint_tolerances
            )
        )
        and scale_reference_spread <= scale_reference_roundoff_tolerance
        and scale_spread <= scale_tolerance
        and all(
            mean_tie_errors[key] <= mean_tie_tolerances[key]
            for key in mean_tie_errors
        )
        and all(
            volume_shift_errors[key] <= volume_shift_tolerances[key]
            for key in volume_shift_errors
        )
    )
    return result(
        "CHK-CG-FACTOR-GAP",
        "Gaussian factorization optimum, perturbation control, monotonicity, and scale laws",
        ["NUM-CG-FACTOR-GAP", "NUM-CG-GAP-MONOTONE", "NUM-CG-SCALE"],
        status="PASS" if passed else "FAIL",
        seed=seed,
        sample_count={
            "analytic_optimum_instances": 1,
            "seeded_symmetric_block_perturbations": perturbation_draws,
            "nested_partitions": len(partitions),
            "scale_values": scales,
        },
        expected={
            "direct_KL_at_analytic_optimum": "closed-form factorization gap",
            "perturbations_improving_beyond_tolerance": 0,
            "nested_gap_nonincreasing": True,
            "single_block_gap": 0,
            "factor_gap_scale_invariance": True,
            "mean_tie_cost": "linear in c",
            "volume_shift": "-(m/2) log c",
        },
        tolerances={
            "policy": "independent 200-digit exact-binary64 references with separately declared endpoint-roundoff allowances; backward residuals are health diagnostics only",
            "analytic_gap_endpoint_roundoff": analytic_gap_endpoint_tolerance,
            "direct_KL_endpoint_roundoff": direct_kl_endpoint_tolerance,
            "analytic_optimum_cross_endpoint": optimum_tolerance,
            "perturbation_improvement_range": [
                min(perturbation_tolerances),
                max(perturbation_tolerances),
            ],
            "monotonicity_pairwise": monotonicity_tolerances,
            "single_block": single_block_tolerance,
            "scale_exact_input_reference_roundoff": scale_reference_roundoff_tolerance,
            "scale_production_endpoint_roundoff": scaled_gap_endpoint_tolerances,
            "scale_identity": scale_tolerance,
            "mean_tie_identity": mean_tie_tolerances,
            "volume_shift_identity": volume_shift_tolerances,
        },
        observed={
            "all_numerical_outputs_finite": numerical_outputs_finite,
            "analytic_optimum": {
                "closed_form_gap": analytic_gap,
                "direct_KL": direct_optimum_kl,
                "exact_binary64_reference_200d": analytic_gap_reference,
                "gap_reference_absolute_error": analytic_gap_reference_error,
                "direct_KL_reference_absolute_error": direct_kl_reference_error,
                "absolute_residual": optimum_residual,
                "gap_backward_error_bound": analytic_gap_result.backward_error_bound,
            },
            "perturbation_control": {
                "draws": perturbation_draws,
                "improving_beyond_tolerance": improving_perturbations,
                "minimum_KL_minus_optimum": min(perturbation_deltas),
                "median_KL_minus_optimum": float(np.median(perturbation_deltas)),
            },
            "monotonicity": {
                "nested_partition_gaps": gaps,
                "exact_binary64_references_200d": gap_references,
                "reference_absolute_errors": gap_reference_errors,
                "nonincreasing": monotone,
                "high_precision_reference_nonincreasing": high_precision_monotone,
                "binary64_nonincreasing_with_endpoint_allowance": binary64_monotone,
                "single_block_gap": gaps[-1],
                "gap_backward_error_bounds": [
                    gap.backward_error_bound for gap in gap_results
                ],
            },
            "scale": {
                "factorization_gaps": dict(zip(map(str, scales), scaled_gaps)),
                "exact_binary64_references_200d": dict(
                    zip(map(str, scales), scaled_gap_references)
                ),
                "production_reference_absolute_errors": dict(
                    zip(map(str, scales), scaled_gap_reference_errors)
                ),
                "factorization_gap_spread": scale_spread,
                "exact_input_reference_spread": scale_reference_spread,
                "factorization_gap_backward_error_bounds": dict(
                    zip(
                        map(str, scales),
                        (gap.backward_error_bound for gap in scaled_gap_results),
                    )
                ),
                "mean_tie_costs": mean_tie_costs,
                "mean_tie_linear_scaling_errors": mean_tie_errors,
                "volume_terms": volume_terms,
                "volume_shift_errors": volume_shift_errors,
                "transverse_dimension_m": m,
            },
        },
        interpretation="The KL optimum is evaluated independently from the determinant formula. Seeded SPD-preserving block perturbations are a control, while universal monotonicity and scaling remain algebraic statements proved in the manuscript.",
    )


def check_cg_factor_gap_stress() -> dict[str, Any]:
    schedule = _default_factorization_schedule(FACTORIZATION_PROTOCOL_SEED)
    protocol = run_factorization_gap_protocol(schedule=schedule)
    records = protocol.cases
    by_id = {record.case_id: record for record in records}
    controls = {control.case_id: control for control in protocol.high_precision_controls}
    protocol_case_failures = list(protocol.case_failures)

    all_case_oracle_failures: list[dict[str, Any]] = []
    all_case_oracle_cases = 0
    all_case_oracle_errors: list[float] = []
    all_case_oracle_tolerances: list[float] = []
    for case in schedule:
        all_case_oracle_cases += 1
        matrix = None
        partition = None
        try:
            matrix, partition = _regenerate_factorization_case(
                case, seed=protocol.seed
            )
            record = by_id.get(case.case_id)
            if record is None:
                raise ValueError("production record is missing")
            reference_mp = _high_precision_partition_gap(
                matrix, partition, digits=100
            )
            reference = float(reference_mp)
            error = abs(record.value - reference)
            tolerance = max(
                _roundoff_scale(
                    record.value,
                    reference,
                    dimension=record.dimension,
                    multiplier=512.0,
                ),
                1.0e-4 * abs(reference),
                2.0e-8,
            )
            all_case_oracle_errors.append(error)
            all_case_oracle_tolerances.append(tolerance)
            if (
                not math.isfinite(record.value)
                or not math.isfinite(reference)
                or error > tolerance
            ):
                all_case_oracle_failures.append(
                    {
                        "case_id": case.case_id,
                        "stratum": case.stratum,
                        "dimension": int(case.dimension),
                        "nominal_condition_number": float(
                            case.condition_number
                        ),
                        "achieved_condition_number": record.achieved_condition_number,
                        "matrix_digest": record.matrix_digest,
                        "partition_digest": record.partition_digest,
                        "production_value": record.value,
                        "reference_value_100d": mpmath.nstr(reference_mp, n=100),
                        "absolute_error": error,
                        "declared_acceptance": tolerance,
                        "disposition": "FAIL",
                    }
                )
        except Exception as exc:
            all_case_oracle_failures.append(
                {
                    "case_id": case.case_id,
                    "stratum": case.stratum,
                    "dimension": int(case.dimension),
                    "nominal_condition_number": float(case.condition_number),
                    "matrix_digest": (
                        _factorization_matrix_digest(matrix)
                        if matrix is not None
                        else None
                    ),
                    "partition_digest": (
                        _factorization_partition_digest(partition)
                        if partition is not None
                        else None
                    ),
                    "exception_type": type(exc).__name__,
                    "exception_message": str(exc),
                    "disposition": "ERROR",
                }
            )

    control_errors: dict[str, float] = {}
    control_tolerances: dict[str, float] = {}
    for case_id, control in controls.items():
        record = by_id[case_id]
        reference = float(control.reference_value)
        control_errors[case_id] = abs(record.value - reference)
        control_tolerances[case_id] = max(
            _roundoff_scale(
                record.value, reference, dimension=record.dimension, multiplier=256.0
            ),
            1.0e-4 * abs(reference),
            2.0e-8,
        )
    stratum_counts = {
        name: sum(record.stratum == name for record in records)
        for name in FACTORIZATION_PROTOCOL_STRATUM_COUNTS
    }
    achieved_condition_ranges = {
        name: {
            "minimum": min(
                record.achieved_condition_number
                for record in records
                if record.stratum == name
            ),
            "maximum": max(
                record.achieved_condition_number
                for record in records
                if record.stratum == name
            ),
        }
        for name in FACTORIZATION_PROTOCOL_STRATUM_COUNTS
        if any(record.stratum == name for record in records)
    }
    achieved_global_range = {
        "minimum": min(
            (record.achieved_condition_number for record in records),
            default=math.nan,
        ),
        "maximum": max(
            (record.achieved_condition_number for record in records),
            default=math.nan,
        ),
    }
    nominal_versus_achieved_controls = {
        case_id: {
            "nominal_condition_number": by_id[case_id].condition_number,
            "achieved_condition_number": by_id[case_id].achieved_condition_number,
        }
        for case_id in (
            "exact_block_diagonal-015",
            "near_decoupled-015",
        )
        if case_id in by_id
    }

    witness_matrix = np.asarray(FACTORIZATION_BOUNDARY_WITNESS, dtype=float)
    witness_partition = ((0, 1), (2, 3))
    try:
        witness_gap = factorization_gap(witness_matrix, witness_partition)
        witness_step = witness_gap.steps[0]
        witness_exact_value = float(
            _high_precision_partition_gap(
                witness_matrix, witness_partition, digits=200
            )
        )
        witness_digest = _factorization_matrix_digest(witness_matrix)
        witness_excursion = witness_step.clipping_amount
        witness_allowance = witness_step.residual_derived_clip_bound
        witness_passed = (
            witness_digest == FACTORIZATION_BOUNDARY_WITNESS_DIGEST
            and math.isclose(
                witness_exact_value,
                FACTORIZATION_BOUNDARY_WITNESS_GAP,
                rel_tol=0.0,
                abs_tol=math.ulp(FACTORIZATION_BOUNDARY_WITNESS_GAP),
            )
            and witness_excursion == FACTORIZATION_BOUNDARY_WITNESS_EXCURSION
            and witness_allowance == FACTORIZATION_BOUNDARY_WITNESS_ALLOWANCE
            and witness_step.clipping_applied
            and math.isclose(
                witness_gap.value,
                witness_exact_value,
                rel_tol=0.0,
                abs_tol=math.ulp(witness_exact_value),
            )
        )
        boundary_witness = {
            "matrix_digest": witness_digest,
            "exact_input_value": witness_exact_value,
            "rho_squared_excursion": witness_excursion,
            "outward_allowance": witness_allowance,
            "production_value": witness_gap.value,
            "clipping_diagnostic_applied": witness_step.clipping_applied,
            "evaluation_method": witness_step.evaluation_method,
            "status": "PASS" if witness_passed else "FAIL",
        }
    except Exception as exc:
        witness_passed = False
        boundary_witness = {
            "matrix_digest": _factorization_matrix_digest(witness_matrix),
            "exception_type": type(exc).__name__,
            "exception_message": str(exc),
            "status": "FAIL",
        }

    global_near_1e14 = math.isfinite(achieved_global_range["maximum"]) and math.isclose(
        achieved_global_range["maximum"], 1.0e14, rel_tol=2.0e-2
    )
    passed = (
        len(records) == 3138
        and stratum_counts == FACTORIZATION_PROTOCOL_STRATUM_COUNTS
        and len(controls) == 18
        and not protocol_case_failures
        and all_case_oracle_cases == 3138
        and not all_case_oracle_failures
        and witness_passed
        and global_near_1e14
        and all(math.isfinite(record.value) for record in records)
        and all(
            math.isfinite(record.achieved_condition_number)
            for record in records
        )
        and all(
            control_errors[case_id] <= control_tolerances[case_id]
            for case_id in controls
        )
    )
    case_payload_digest = hashlib.sha256(
        json.dumps(
            [record._asdict() for record in records],
            sort_keys=True,
            separators=(",", ":"),
        ).encode()
    ).hexdigest()
    return result(
        "CHK-CG-FACTOR-GAP-STRESS-3138",
        "Frozen stable Gaussian factorization-gap stress protocol",
        ["NUM-CG-FACTOR-GAP-BOUNDARY-PROTOCOL"],
        status="PASS" if passed else "FAIL",
        seed=protocol.seed,
        sample_count={
            "total_cases": len(records),
            "strata": stratum_counts,
            "mpmath_100_digit_controls": len(controls),
            "all_case_100_digit_references": all_case_oracle_cases,
            "focused_positive_excursion_witnesses": 1,
        },
        expected={
            "protocol_name": "new-deterministic-factorization-gap-3138",
            "historical_generator_recovered": False,
            "all_values_finite": True,
            "all_3138_values_within_declared_100_digit_reference_acceptance": True,
            "all_high_precision_controls_within_declared_tolerance": True,
            "boundary_witness": {
                "matrix_digest": FACTORIZATION_BOUNDARY_WITNESS_DIGEST,
                "exact_input_value": FACTORIZATION_BOUNDARY_WITNESS_GAP,
                "rho_squared_excursion": FACTORIZATION_BOUNDARY_WITNESS_EXCURSION,
                "outward_allowance": FACTORIZATION_BOUNDARY_WITNESS_ALLOWANCE,
                "status": "PASS",
            },
            "achieved_condition_coverage_near_1e14": "global only",
        },
        tolerances={
            "matrix_value_comparison": "independent 100-digit exact-binary64 reference; max(endpoint-scaled binary64 roundoff, 1e-4 relative, 2e-8 absolute)",
            "backward_error_role": "health diagnostic only; excluded from every forward-value acceptance",
            "near_boundary_policy": "64*n*binary64 epsilon operational guard plus 200-digit exact-input evaluation; not a general perturbation theorem",
        },
        observed={
            "protocol_name": protocol.protocol_name,
            "historical_generator_recovered": protocol.historical_generator_recovered,
            "schedule_digest": protocol.schedule_digest,
            "case_payload_digest": case_payload_digest,
            "stratum_counts": stratum_counts,
            "nominal_condition_number_range": {
                "minimum": min(FACTORIZATION_PROTOCOL_CONDITIONS),
                "maximum": max(FACTORIZATION_PROTOCOL_CONDITIONS),
            },
            "achieved_condition_number_range_global": achieved_global_range,
            "achieved_condition_number_ranges_by_stratum": achieved_condition_ranges,
            "achieved_condition_coverage_near_1e14_global_only": global_near_1e14,
            "nominal_versus_achieved_controls": nominal_versus_achieved_controls,
            "finite_values": sum(math.isfinite(record.value) for record in records),
            "clipping_cases": sum(record.clipping_applied for record in records),
            "boundary_fallback_cases": sum(
                record.boundary_fallback_applied for record in records
            ),
            "high_precision_fallback_cases": sum(
                record.high_precision_fallback_applied for record in records
            ),
            "maximum_control_error": max(control_errors.values(), default=0.0),
            "maximum_control_tolerance": max(
                control_tolerances.values(), default=0.0
            ),
            "all_case_oracle_cases": all_case_oracle_cases,
            "all_case_oracle_failures": len(all_case_oracle_failures),
            "all_case_oracle_failure_details": all_case_oracle_failures,
            "maximum_all_case_oracle_error": max(
                all_case_oracle_errors, default=0.0
            ),
            "maximum_all_case_oracle_acceptance": max(
                all_case_oracle_tolerances, default=0.0
            ),
            "protocol_case_failures": protocol_case_failures,
            "boundary_witness": boundary_witness,
        },
        interpretation="This is a new frozen stress protocol, not a recovered historical experiment. Every one of the 3,138 schedule cases is compared with its own 100-digit exact-input reference; the 18 designated controls remain a named stratum. The separate 4-by-4 positive-excursion fixture binds the declared boundary policy but was not produced by the ordinary 3,138-case schedule.",
    )


def check_cg_frame_cancellation() -> dict[str, Any]:
    seed = 20260728
    rng = np.random.default_rng(seed)
    k = 3
    u = random_gl_plus(rng, k)
    mu = rng.standard_normal(k)
    sigma = random_spd(rng, k)
    g = random_gl_plus(rng, k)
    bar_mu = np.linalg.solve(u, mu)
    bar_sigma = np.linalg.solve(u, sigma) @ np.linalg.inv(u).T
    u2, mu2, sigma2 = g @ u, g @ mu, g @ sigma @ g.T
    bar_mu2 = np.linalg.solve(u2, mu2)
    bar_sigma2 = np.linalg.solve(u2, sigma2) @ np.linalg.inv(u2).T
    mean_error = float(np.linalg.norm(bar_mu2 - bar_mu))
    covariance_error = float(np.linalg.norm(bar_sigma2 - bar_sigma, ord="fro"))
    passed = mean_error <= 1.0e-10 and covariance_error <= 1.0e-10
    return result(
        "CHK-CG-FRAME-CANCELLATION",
        "Canonical-frame Gaussian parameters under common reframing",
        ["NUM-CG-FRAME-CANCELLATION"],
        status="PASS" if passed else "FAIL",
        seed=seed,
        sample_count=1,
        expected={"canonical_mean_unchanged": True, "canonical_covariance_unchanged": True},
        tolerances={"absolute": 1.0e-10},
        observed={"mean_error": mean_error, "covariance_error": covariance_error},
        interpretation="The check is a direct substitution into the orbit-invariant parameter pair.",
    )


def check_cg_equivariance() -> dict[str, Any]:
    cases = [(2, 3), (3, 4), (4, 5), (5, 6), (5, 3)]
    rows = []
    passed = True
    for k, n in cases:
        angle = 2.0 * math.pi / n
        v = np.eye(k)
        v[:2, :2] = np.array(
            [[math.cos(angle), -math.sin(angle)], [math.sin(angle), math.cos(angle)]]
        )
        order_residual = float(np.linalg.norm(np.linalg.matrix_power(v, n) - np.eye(k), ord="fro"))
        rank = int(np.linalg.matrix_rank(np.eye(k) - v, tol=1.0e-10))
        det = float(np.linalg.det(v))
        rows.append({"K": k, "n": n, "determinant": det, "order_residual": order_residual, "rank_I_minus_v": rank})
        passed &= det > 0 and order_residual <= 1.0e-10 and rank == 2
    return result(
        "CHK-CG-EQUIVARIANCE",
        "Finite-order GL+ witnesses for the equivariance obstruction",
        ["NUM-CG-EQUIVARIANCE"],
        status="PASS" if passed else "FAIL",
        seed=None,
        sample_count=len(cases),
        expected={"determinant_positive": True, "v_power_n": "identity", "rank_I_minus_v": 2},
        tolerances={"order_residual": 1.0e-10, "rank": 1.0e-10},
        observed={"cases": rows},
        interpretation="Plane rotations give deterministic witnesses; no random draw is required.",
    )


def check_rg_ray_kernel() -> dict[str, Any]:
    seed = 20260729
    rng = np.random.default_rng(seed)
    observed = []
    passed = True
    for n, k in [(5, 2), (6, 3), (7, 4), (5, 3), (6, 2)]:
        x = rng.uniform(0.2, 2.0, size=n)
        s = float(x.sum())
        m = random_spd(rng, k)
        spatial = s * np.diag(x) - np.outer(x, x)
        lap = np.kron(spatial, m)
        eig = np.linalg.eigvalsh(lap)
        tol = max(float(eig[-1]), 1.0) * 1.0e-10
        nullity = int(np.count_nonzero(np.abs(eig) <= tol))
        residual = float(np.linalg.norm(lap @ np.kron(np.ones((n, 1)), np.eye(k)), ord="fro"))
        observed.append({"N": n, "K": k, "nullity": nullity, "consensus_residual": residual})
        passed &= nullity == k and residual <= 1.0e-9
    n, k = 5, 3
    x = rng.uniform(0.2, 2.0, size=n)
    q, _ = np.linalg.qr(rng.standard_normal((k, k)))
    m = q @ np.diag([2.0, 1.0, 0.0]) @ q.T
    lap = np.kron(float(x.sum()) * np.diag(x) - np.outer(x, x), m)
    eig = np.linalg.eigvalsh(lap)
    tol = max(float(eig[-1]), 1.0) * 1.0e-10
    control_nullity = int(np.count_nonzero(np.abs(eig) <= tol))
    expected_control = k + (n - 1) * (k - 2)
    passed &= control_nullity == expected_control
    return result(
        "CHK-RG-RAY-KERNEL",
        "Kernel of the bi-additive matrix ray",
        ["NUM-RG-RAY-KERNEL"],
        status="PASS" if passed else "FAIL",
        seed=seed,
        sample_count="five full-rank draws and one rank-two control",
        expected={"full_rank_nullity": "K", "rank_two_control_nullity": expected_control},
        tolerances={"rank_relative": 1.0e-10, "consensus_absolute": 1.0e-9},
        observed={"full_rank_cases": observed, "rank_two_control_nullity": control_nullity},
        interpretation="The rank-deficient control checks the full kernel formula, not only the consensus subspace.",
    )


def check_rg_sector_split() -> dict[str, Any]:
    seed = 20260728
    rng = np.random.default_rng(seed)
    n, k = 8, 3
    assignments = [0, 0, 1, 1, 2, 2, 3, 3]
    s = incidence_map(assignments, k)
    weights = {(i, j): random_spd(rng, k, 0.1) for i in range(n) for j in range(i + 1, n)}
    self_terms = [random_spd(rng, k, 0.1) for _ in range(n)]
    base, _ = assemble_interaction(self_terms, weights)
    coarse_base = s.T @ base @ s

    changed_self = [a + random_spd(rng, k, 0.1) for a in self_terms]
    self_changed, _ = assemble_interaction(changed_self, weights)
    coarse_self_changed = s.T @ self_changed @ s
    offdiag_change = 0.0
    nc = 4
    for i in range(nc):
        for j in range(i + 1, nc):
            block = (
                coarse_self_changed[i * k : (i + 1) * k, j * k : (j + 1) * k]
                - coarse_base[i * k : (i + 1) * k, j * k : (j + 1) * k]
            )
            offdiag_change = max(offdiag_change, float(np.linalg.norm(block, ord="fro")))

    weights_changed = {key: value.copy() for key, value in weights.items()}
    delta = 1000.0 * np.eye(k)
    weights_changed[(0, 1)] += delta
    internal_changed, _ = assemble_interaction(self_terms, weights_changed)
    coarse_internal_changed = s.T @ internal_changed @ s
    diagonal_change = 0.0
    for i in range(nc):
        block = (
            coarse_internal_changed[i * k : (i + 1) * k, i * k : (i + 1) * k]
            - coarse_base[i * k : (i + 1) * k, i * k : (i + 1) * k]
        )
        diagonal_change = max(diagonal_change, float(np.linalg.norm(block, ord="fro")))
    passed = offdiag_change <= 1.0e-10 and diagonal_change <= 1.0e-9
    return result(
        "CHK-RG-SECTOR-SPLIT",
        "Independent self and coupling sectors under declared aggregation",
        ["NUM-RG-SECTOR-SPLIT"],
        status="PASS" if passed else "FAIL",
        seed=seed,
        sample_count="one system and two perturbation controls",
        expected={
            "self_to_coarse_coupling_residual": "<= declared tolerance",
            "internal_edge_to_coarse_self_residual": "<= declared tolerance",
        },
        tolerances={"absolute": 1.0e-9},
        observed={"maximum_coarse_offdiagonal_change_from_self": offdiag_change, "maximum_coarse_diagonal_change_from_internal_edge": diagonal_change},
        interpretation="The test isolates blocks of the exact parameter map; it does not assert attraction.",
    )


def aggregate_weights_pairwise(
    weights: dict[tuple[int, int], np.ndarray], n: int
) -> tuple[dict[tuple[int, int], np.ndarray], int]:
    assignments = [i // 2 for i in range(n)]
    nc = (n + 1) // 2
    out: dict[tuple[int, int], np.ndarray] = {}
    k = next(iter(weights.values())).shape[0]
    for ci in range(nc):
        for cj in range(ci + 1, nc):
            out[(ci, cj)] = sum(
                (
                    w
                    for (i, j), w in weights.items()
                    if {assignments[i], assignments[j]} == {ci, cj}
                ),
                np.zeros((k, k)),
            )
    return out, nc


def check_rg_invariant_faces() -> dict[str, Any]:
    seed = 20260729
    rng = np.random.default_rng(seed)
    n, k = 16, 3
    v = rng.standard_normal(k)
    rank_one = np.outer(v, v)
    common = {
        (i, j): rng.uniform(0.2, 2.0) * rank_one
        for i in range(n)
        for j in range(i + 1, n)
    }
    full = {
        (i, j): random_spd(rng, k, 0.2)
        for i in range(n)
        for j in range(i + 1, n)
    }
    rank_history = []
    full_rank_history = []
    current_n = n
    for _level in range(3):
        common, current_n = aggregate_weights_pairwise(common, current_n)
        full, _ = aggregate_weights_pairwise(full, current_n * 2)
        common_ranks = [int(np.linalg.matrix_rank(w, tol=1.0e-10)) for w in common.values()]
        full_ranks = [int(np.linalg.matrix_rank(w, tol=1.0e-10)) for w in full.values()]
        rank_history.append(sorted(set(common_ranks)))
        full_rank_history.append(sorted(set(full_ranks)))
    t_values = np.logspace(-2, 2, 21)
    distance_errors = []
    for t in t_values:
        mt = np.diag([t, 1.0, 1.0])
        eig = np.linalg.eigvalsh(mt)
        hilbert = math.log(float(eig.max() / eig.min()))
        distance_errors.append(abs(hilbert - abs(math.log(float(t)))))
    max_distance_error = max(distance_errors)
    passed = all(ranks == [1] for ranks in rank_history) and all(ranks == [3] for ranks in full_rank_history) and max_distance_error <= 1.0e-12
    return result(
        "CHK-RG-INVARIANT-FACES",
        "Common-range invariant face and unbounded projective diameter",
        ["NUM-RG-INVARIANT-FACES"],
        status="PASS" if passed else "FAIL",
        seed=seed,
        sample_count="three pair-aggregation levels and 21 t values over four decades",
        expected={"common_range_rank": 1, "full_range_rank": k, "hilbert_distance": "abs(log t)"},
        tolerances={"rank": 1.0e-10, "distance_absolute": 1.0e-12},
        observed={
            "common_range_rank_sets_by_level": rank_history,
            "full_range_rank_sets_by_level": full_rank_history,
            "maximum_projective_distance_error": max_distance_error,
        },
        interpretation="Persistent rank-one ranges exhibit an invariant proper face, while the distance family has no finite diameter bound.",
    )


def check_rg_homogeneous_gate() -> dict[str, Any]:
    k, b = 2, 2
    symmetric_basis = [
        sp.Matrix([[1, 0], [0, 0]]),
        sp.Matrix([[0, 0], [0, 1]]),
        sp.Matrix([[0, 1], [1, 0]]),
    ]

    def sym_coordinates(matrix: sp.Matrix) -> sp.Matrix:
        return sp.Matrix([matrix[0, 0], matrix[1, 1], matrix[0, 1]])

    columns = []
    for sector in ("coupling", "self"):
        for basis_matrix in symmetric_basis:
            if sector == "coupling":
                output_coupling = b**2 * basis_matrix
                output_self = sp.zeros(k)
            else:
                output_coupling = sp.zeros(k)
                output_self = b * basis_matrix
            columns.append(
                sym_coordinates(output_coupling).col_join(
                    sym_coordinates(output_self)
                )
            )
    endomorphism = sp.Matrix.hstack(*columns)
    characteristic_variable = sp.symbols("x")
    characteristic = sp.factor(
        endomorphism.charpoly(characteristic_variable).as_expr()
    )
    exact_eigenvalues = {
        str(eigenvalue): int(multiplicity)
        for eigenvalue, multiplicity in endomorphism.eigenvals().items()
    }
    numeric_eigenvalues = sorted(
        [float(value) for value in endomorphism.eigenvals().keys()],
        reverse=True,
    )
    expanded_eigenvalues = sorted(
        [
            float(value)
            for value, multiplicity in endomorphism.eigenvals().items()
            for _ in range(int(multiplicity))
        ],
        reverse=True,
    )
    distinct = sorted(set(expanded_eigenvalues), reverse=True)
    naive_ratio = expanded_eigenvalues[1] / expanded_eigenvalues[0]
    outside_dominant_ratio = distinct[1] / distinct[0]
    normalized_self_ratios = [(1.0 / b) ** level for level in range(9)]
    passed = (
        endomorphism.shape == (6, 6)
        and characteristic == (characteristic_variable - 4) ** 3
        * (characteristic_variable - 2) ** 3
        and exact_eigenvalues == {"4": 3, "2": 3}
        and naive_ratio == 1.0
        and outside_dominant_ratio == 0.5
        and all(a > bval for a, bval in zip(normalized_self_ratios, normalized_self_ratios[1:]))
    )
    return result(
        "CHK-RG-HOMOGENEOUS-GATE",
        "Exact homogeneous gate spectrum and sector ratio",
        ["RG-HOMOGENEOUS-EXACT"],
        status="PASS" if passed else "FAIL",
        seed=None,
        sample_count="one exact 6x6 Sym(2) coupling-plus-self endomorphism at b=2",
        expected={"spectrum": [4, 4, 4, 2, 2, 2], "naive_top_two_ratio": 1, "outside_dominant_ratio": 0.5},
        tolerances={"arithmetic": "exact integers"},
        observed={
            "symmetric_basis": [
                [[str(entry) for entry in row] for row in matrix.tolist()]
                for matrix in symmetric_basis
            ],
            "endomorphism_matrix": [
                [str(entry) for entry in row] for row in endomorphism.tolist()
            ],
            "characteristic_polynomial": str(characteristic),
            "eigenvalue_multiplicities": exact_eigenvalues,
            "distinct_numeric_eigenvalues": numeric_eigenvalues,
            "spectrum_with_multiplicity": expanded_eigenvalues,
            "naive_top_two_ratio": naive_ratio,
            "outside_dominant_ratio": outside_dominant_ratio,
            "normalized_self_sector_ratios_by_level": normalized_self_ratios,
        },
        evidence_kind="exact_algebraic_evaluation",
        interpretation="The actual endomorphism is built on an explicit Sym(2) basis and diagonalized exactly. It does not reproduce the heterogeneous matched-null table or establish a physical fixed law.",
    )


def graph_laplacian_matrix(rng: np.random.Generator, n: int, k: int) -> np.ndarray:
    weights = {
        (i, j): random_spd(rng, k, 0.2)
        for i in range(n)
        for j in range(i + 1, n)
        if rng.random() < 0.65
    }
    # Add a chain to guarantee connectivity.
    for i in range(n - 1):
        weights.setdefault((i, i + 1), random_spd(rng, k, 0.2))
    _, lap = assemble_interaction([np.zeros((k, k)) for _ in range(n)], weights)
    return lap


def positive_quotient_basis(lap: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    eig, vec = np.linalg.eigh(lap)
    tol = max(float(eig[-1]), 1.0) * 1.0e-10
    mask = eig > tol
    return vec[:, mask], eig[mask]


def check_rg_noncommuting_limits_symbolic() -> dict[str, Any]:
    d, eps = sp.symbols("d eps")
    scalar_lap = sp.Matrix([[1, -1], [-1, 1]])
    symbolic_det = sp.factor((scalar_lap - d * (scalar_lap + eps * sp.eye(2))).det())
    expected_det = sp.factor(d * eps * (d * eps + 2 * d - 2))
    symbolic_match = sp.simplify(symbolic_det - expected_det) == 0
    x1, x2, x3, fiber = sp.symbols("x1 x2 x3 m")
    spatial = sp.Matrix(
        [
            [x1 * (x2 + x3), -x1 * x2, -x1 * x3],
            [-x1 * x2, x2 * (x1 + x3), -x2 * x3],
            [-x1 * x3, -x2 * x3, x3 * (x1 + x2)],
        ]
    )
    ray_laplacian = fiber * spatial
    ray_det = sp.factor(ray_laplacian.det())
    ray_pencil_det = sp.factor(((1 - d) * ray_laplacian).det())
    a, spectral_lambda = sp.symbols("a lambda", positive=True)
    transfer = spectral_lambda / (spectral_lambda + a)
    mass_then_infrared = sp.limit(sp.limit(transfer, a, 0, dir="+"), spectral_lambda, 0, dir="+")
    infrared_then_mass = sp.limit(sp.limit(transfer, spectral_lambda, 0, dir="+"), a, 0, dir="+")
    passed = (
        symbolic_match
        and ray_det == 0
        and ray_pencil_det == 0
        and mass_then_infrared == 1
        and infrared_then_mass == 0
    )
    return result(
        "CHK-RG-NONCOMMUTING-LIMITS",
        "Exact symbolic singular pencils and noncommuting mass/spectral limits",
        ["NUM-RG-NONCOMMUTING"],
        status="PASS" if passed else "FAIL",
        seed=None,
        sample_count="one exact symbolic two-node pencil, one symbolic three-agent bi-additive ray, and two iterated limits",
        expected={
            "symbolic_determinant": "d*eps*(d*eps + 2*d - 2)",
            "three_agent_ray_determinant": 0,
            "three_agent_ray_pencil_determinant": 0,
            "a_to_zero_at_fixed_lambda": 1,
            "lambda_to_zero_at_fixed_a": 0,
        },
        tolerances={"symbolic": "exact"},
        observed={
            "two_node_symbolic_determinant": str(symbolic_det),
            "three_agent_ray_determinant": str(ray_det),
            "three_agent_ray_pencil_determinant": str(ray_pencil_det),
            "mass_then_infrared_limit": str(mass_then_infrared),
            "infrared_then_mass_limit": str(infrared_then_mass),
        },
        evidence_kind="exact_symbolic_witness",
        interpretation="Only this exact symbolic check supports the manuscript's keep-exact disposition for the noncommuting-limit numerical tag.",
    )


def check_rg_noncommuting_limits_floating() -> dict[str, Any]:
    seed = 20260729
    rng = np.random.default_rng(seed)
    lap = graph_laplacian_matrix(rng, 6, 2)
    q, positive = positive_quotient_basis(lap)
    bar = q.T @ lap @ q
    quotient_eigen = sla.eigvalsh(bar, bar)
    quotient_error = float(np.max(np.abs(quotient_eigen - 1.0)))
    tolerance = 1.0e-10
    passed = quotient_error <= tolerance
    return result(
        "CHK-RG-NONCOMMUTING-FLOATING",
        "Seeded six-agent floating quotient-pencil control",
        ["SUPPLEMENT-RG-NONCOMMUTING-FLOATING"],
        status="PASS" if passed else "FAIL",
        seed=seed,
        sample_count="one six-agent K=2 graph-Laplacian quotient pencil",
        expected={"quotient_generalized_eigenvalues": "within tolerance of one"},
        tolerances={"absolute_generalized_eigenvalue": tolerance},
        observed={
            "quotient_eigenvalues": quotient_eigen,
            "quotient_eigenvalue_max_error": quotient_error,
            "positive_quotient_dimension": len(positive),
        },
        evidence_kind="reproduced_output",
        interpretation="This separately seeded floating check is current corroboration only and is not classified as keep-exact evidence.",
    )


def check_rg_mass_pencil() -> dict[str, Any]:
    seed = 20260729
    rng = np.random.default_rng(seed)
    lap = graph_laplacian_matrix(rng, 6, 2)
    r = random_spd(rng, lap.shape[0], 1.0)
    generalized_lambda = sla.eigvalsh(lap, r)
    max_errors = {}
    for a in [0.5, 1.0, 3.0]:
        d_values = sla.eigvalsh(lap, lap + a * r)
        predicted = generalized_lambda / (generalized_lambda + a)
        max_errors[str(a)] = float(np.max(np.abs(np.sort(d_values) - np.sort(predicted))))
    r_identity = np.eye(lap.shape[0])
    smallest_nonzero = {}
    q, positive_lap = positive_quotient_basis(lap)
    for a in [1.0, 1.0e-2, 1.0e-4]:
        d_values = sla.eigvalsh(lap, lap + a * r_identity)
        positive_d = d_values[d_values > 1.0e-10]
        smallest_nonzero[str(a)] = float(positive_d.min())
    passed = max(max_errors.values()) <= 1.0e-10 and smallest_nonzero["0.0001"] > smallest_nonzero["1.0"]
    return result(
        "CHK-RG-MASS-PENCIL",
        "Mass-pencil eigenvalue transfer",
        ["NUM-RG-MASS-TRANSFER"],
        status="PASS" if passed else "FAIL",
        seed=seed,
        sample_count="one 12x12 pencil at three masses plus a three-mass identity control",
        expected={"d_k": "lambda_k/(lambda_k+a)", "smaller_mass_moves_nonzero_d_toward_one": True},
        tolerances={"eigenvalue_absolute": 1.0e-10},
        observed={
            "maximum_transfer_errors": max_errors,
            "smallest_nonzero_d_by_mass": smallest_nonzero,
            "positive_laplacian_eigenvalue_count": len(positive_lap),
        },
        interpretation="The check uses a regular positive-definite reference form and treats zero modes separately.",
    )


def star_precision(
    p0: np.ndarray, omegas: list[np.ndarray], covariances: list[np.ndarray]
) -> np.ndarray:
    k = p0.shape[0]
    n = len(omegas)
    out = np.zeros(((n + 1) * k, (n + 1) * k))
    out[:k, :k] = p0
    for idx, (omega, covariance) in enumerate(zip(omegas, covariances), start=1):
        rinv = np.linalg.inv(covariance)
        si = slice(idx * k, (idx + 1) * k)
        out[:k, :k] += omega.T @ rinv @ omega
        out[:k, si] -= omega.T @ rinv
        out[si, :k] -= rinv @ omega
        out[si, si] += rinv
    return out


def reciprocal_precision(
    omega_uv: np.ndarray,
    omega_vu: np.ndarray,
    r_uv: np.ndarray,
    r_vu: np.ndarray,
) -> np.ndarray:
    k = omega_uv.shape[0]
    e_uv = np.hstack([np.eye(k), -omega_uv])
    e_vu = np.hstack([-omega_vu, np.eye(k)])
    return e_uv.T @ np.linalg.solve(r_uv, e_uv) + e_vu.T @ np.linalg.solve(r_vu, e_vu)


def check_obs_star_fold_new_protocol() -> dict[str, Any]:
    seed = 20260728
    rng = np.random.default_rng(seed)
    draws, k, n = 300, 3, 4
    star_minima = []
    fold_nullities = []
    precision_block_errors = []
    for _ in range(draws):
        p0 = random_spd(rng, k, 0.5)
        omegas = [random_gl_plus(rng, k) for _i in range(n)]
        covariances = [random_spd(rng, k, 0.5) for _i in range(n)]
        star = star_precision(p0, omegas, covariances)
        star_minima.append(float(np.linalg.eigvalsh(star).min()))
        predicted_bb = p0 + sum(
            (omega.T @ np.linalg.solve(covariance, omega) for omega, covariance in zip(omegas, covariances)),
            np.zeros((k, k)),
        )
        precision_block_errors.append(float(np.linalg.norm(star[:k, :k] - predicted_bb, ord="fro")))

        omega_uv = random_gl_plus(rng, k)
        omega_vu = np.linalg.inv(omega_uv)
        fold = reciprocal_precision(
            omega_uv, omega_vu, random_spd(rng, k, 0.5), random_spd(rng, k, 0.5)
        )
        eig = np.linalg.eigvalsh(fold)
        tol = max(float(eig[-1]), 1.0) * 1.0e-9
        fold_nullities.append(int(np.count_nonzero(np.abs(eig) <= tol)))
    passed = min(star_minima) > 0 and set(fold_nullities) == {k} and max(precision_block_errors) <= 1.0e-10
    return result(
        "CHK-OBS-STAR-FOLD-NEW-PROTOCOL",
        "New declared-seed star-versus-reciprocal-fold protocol",
        ["NUM-OBS-STAR-FOLD"],
        status="PASS" if passed else "FAIL",
        seed=seed,
        sample_count=draws,
        expected={"all_stars_positive_definite": True, "cocycle_fold_nullity": k, "apex_precision_addition": True},
        tolerances={"fold_rank_relative": 1.0e-9, "precision_block_absolute": 1.0e-10},
        observed={
            "minimum_star_eigenvalue": min(star_minima),
            "fold_nullities_observed": sorted(set(fold_nullities)),
            "maximum_apex_precision_block_error": max(precision_block_errors),
        },
        interpretation="This is a replacement run. The manuscript's historical 300-draw extrema remain unrecoverable because their seed and matrices were lost.",
    )


def check_obs_holonomy_det_kernel() -> dict[str, Any]:
    seed = 20260728
    rng = np.random.default_rng(seed)
    logdet_errors = []
    usable_draws = 0
    for draw in range(1000):
        k = draw % 5 + 1
        omega_uv = random_gl_plus(rng, k, 0.20)
        q, _ = np.linalg.qr(rng.standard_normal((k, k)))
        h_eigenvalues = rng.choice([-1.0, 1.0], size=k) * rng.uniform(0.25, 0.65, size=k) + 1.0
        h = q @ np.diag(h_eigenvalues) @ q.T
        omega_vu = h @ np.linalg.inv(omega_uv)
        r_uv = random_spd(rng, k, 1.0)
        r_vu = random_spd(rng, k, 1.0)
        h = omega_vu @ omega_uv
        j = reciprocal_precision(omega_uv, omega_vu, r_uv, r_vu)
        sign_j, logdet_j = np.linalg.slogdet(j)
        sign_h, logdet_h = np.linalg.slogdet(np.eye(k) - h)
        sign_ruv, logdet_ruv = np.linalg.slogdet(r_uv)
        sign_rvu, logdet_rvu = np.linalg.slogdet(r_vu)
        if sign_j > 0 and sign_h != 0 and sign_ruv > 0 and sign_rvu > 0:
            predicted = 2.0 * logdet_h - logdet_ruv - logdet_rvu
            logdet_errors.append(abs(float(logdet_j - predicted)))
            usable_draws += 1

    cases = []
    kernel_match = True
    for k in range(2, 6):
        for multiplicity in range(k + 1):
            q, _ = np.linalg.qr(rng.standard_normal((k, k)))
            nonunit = [1.5 + 0.3 * idx for idx in range(k - multiplicity)]
            h = q @ np.diag([1.0] * multiplicity + nonunit) @ q.T
            omega_uv = np.eye(k)
            omega_vu = h
            j = reciprocal_precision(omega_uv, omega_vu, random_spd(rng, k, 1.0), random_spd(rng, k, 1.0))
            eig_j = np.linalg.eigvalsh(j)
            j_tol = max(float(eig_j[-1]), 1.0) * 1.0e-9
            observed_nullity = int(np.count_nonzero(np.abs(eig_j) <= j_tol))
            observed_fixed = k - np.linalg.matrix_rank(h - np.eye(k), tol=1.0e-9)
            kernel_match &= observed_nullity == multiplicity == observed_fixed
            cases.append(
                {
                    "K": k,
                    "prescribed_multiplicity": multiplicity,
                    "J_nullity": observed_nullity,
                    "fixed_space_dimension": int(observed_fixed),
                }
            )
    max_logdet_error = max(logdet_errors) if logdet_errors else math.inf
    passed = usable_draws >= 990 and max_logdet_error <= 1.0e-7 and kernel_match and len(cases) == 18
    return result(
        "CHK-OBS-HOLONOMY-DET-KERNEL",
        "Reciprocal-pair determinant and fixed-space kernel",
        ["NUM-OBS-HOLONOMY-DET-KERNEL"],
        status="PASS" if passed else "FAIL",
        seed=seed,
        sample_count={"determinant_draws": 1000, "prescribed_kernel_cases": len(cases)},
        expected={
            "logdet_J": "2 log|det(I-H)| - logdet(R_uv) - logdet(R_vu)",
            "J_nullity": "dim ker(H-I)",
        },
        tolerances={"logdet_absolute": 1.0e-7, "rank_relative": 1.0e-9},
        observed={
            "usable_determinant_draws": usable_draws,
            "maximum_logdet_identity_error": max_logdet_error,
            "all_kernel_cases_match": kernel_match,
            "kernel_cases": cases,
        },
        interpretation="Orthogonal similarities control rank conditioning in the prescribed-multiplicity cases.",
    )


def check_obs_normalizer_witness() -> dict[str, Any]:
    a, p0 = sp.symbols("a p0", nonzero=True)
    j = sp.Matrix(
        [[1 + a ** -2, -(a + a ** -1)], [-(a + a ** -1), 1 + a**2]]
    )
    determinant = sp.factor((j + p0 * sp.eye(2)).det())
    expected = sp.factor(p0**2 + p0 * (a + a**-1) ** 2)
    derivative = sp.factor(sp.diff(expected, a))
    matched = sp.simplify(determinant - expected) == 0
    numeric = {str(value): float(expected.subs({a: value, p0: 1})) for value in [1, 2, 3]}
    passed = matched and numeric["1"] < numeric["2"] < numeric["3"]
    return result(
        "CHK-OBS-NORMALIZER-WITNESS",
        "Exact scalar reciprocal-pair normalizer witness",
        ["NUM-OBS-HOLONOMY-DET-KERNEL"],
        status="PASS" if passed else "FAIL",
        seed=None,
        sample_count="one exact symbolic family and three evaluation points",
        expected={"determinant": "p0^2 + p0(a+a^-1)^2", "nonconstant": True},
        tolerances={"arithmetic": "exact symbolic"},
        observed={"determinant": str(determinant), "derivative": str(derivative), "p0_equals_1_values": numeric},
        evidence_kind="exact_symbolic_witness",
        interpretation="The determinant varies with transport. The sign of the induced log-normalizer force must be read from the chosen optimization objective, not inferred from determinant minimization alone.",
    )


CHECKS: list[Callable[[], dict[str, Any]]] = [
    check_gauss_projection,
    check_gauss_trivialization,
    check_gauss_conditioning,
    check_kron_exact_witness,
    check_kron_monte_carlo,
    check_restriction_schur,
    check_ig_expectation_metric,
    check_ig_pullback_pushforward,
    check_generalized_spectrum,
    check_cg_aggregation,
    check_graph_holonomy,
    check_cg_maximal_clusters,
    check_cg_lambda_continuum,
    check_cg_pair_merge,
    check_cg_biadditive,
    check_cg_epsilon_divergence,
    check_cg_factor_gap,
    check_cg_factor_gap_stress,
    check_cg_frame_cancellation,
    check_cg_equivariance,
    check_rg_ray_kernel,
    check_rg_sector_split,
    check_rg_invariant_faces,
    check_rg_homogeneous_gate,
    check_rg_noncommuting_limits_symbolic,
    check_rg_noncommuting_limits_floating,
    check_rg_mass_pencil,
    check_obs_star_fold_new_protocol,
    check_obs_holonomy_det_kernel,
    check_obs_normalizer_witness,
]


def scan_inventory(
    claims: list[dict[str, Any]],
) -> tuple[dict[str, Any], list[dict[str, Any]], dict[str, dict[str, Any]]]:
    grouped: dict[str, list[dict[str, Any]]] = {}
    for claim in claims:
        grouped.setdefault(claim["source_file"], []).append(claim)

    current_claims: list[dict[str, Any]] = []
    file_counts: dict[str, dict[str, int]] = {}
    source_manifest: dict[str, dict[str, Any]] = {}
    bare_table_status_entries: list[dict[str, Any]] = []
    failures: list[str] = []
    discovered_paths = sorted(
        TEX_ROOT.rglob("*.tex"),
        key=lambda path: path.relative_to(TEX_ROOT).as_posix(),
    )
    discovered_files = {
        path.relative_to(TEX_ROOT).as_posix(): path for path in discovered_paths
    }
    missing_declared_files = sorted(set(grouped) - set(discovered_files))
    for source_file in missing_declared_files:
        failures.append(f"{source_file}: declared source file was not discovered")

    for source_file, path in discovered_files.items():
        expected_claims = grouped.get(source_file, [])
        raw_source = path.read_bytes()
        text = raw_source.decode("utf-8")
        source_manifest[source_file] = manifest_entry(path, raw_source)
        matches = list(re.finditer(re.escape(NUMERICAL_TOKEN), text))
        bare_matches = list(re.finditer(r"&\s*NUMERICAL\s*&", text))
        for match in bare_matches:
            bare_table_status_entries.append(
                {
                    "source_file": source_file,
                    "source_line": text.count("\n", 0, match.start()) + 1,
                    "matched_text": match.group(0),
                }
            )
        if bare_matches:
            failures.append(
                f"{source_file}: found {len(bare_matches)} bare NUMERICAL status-table cells"
            )
        file_counts[source_file] = {"expected": len(expected_claims), "observed": len(matches)}
        if len(matches) != len(expected_claims):
            failures.append(
                f"{source_file}: expected {len(expected_claims)} NUMERICAL tokens, found {len(matches)}"
            )
        for claim in expected_claims:
            index = int(claim["occurrence_index"]) - 1
            item = dict(claim)
            if index < len(matches):
                item["current_source_line"] = text.count("\n", 0, matches[index].start()) + 1
                item["source_token_found"] = True
            else:
                item["current_source_line"] = None
                item["source_token_found"] = False
                failures.append(f"{claim['id']}: occurrence index not found")
            current_claims.append(item)

    for source_file in missing_declared_files:
        for claim in grouped[source_file]:
            item = dict(claim)
            item["current_source_line"] = None
            item["source_token_found"] = False
            current_claims.append(item)
            failures.append(f"{claim['id']}: source file not found")

    status = "PASS" if not failures else "FAIL"
    return (
        {
            "status": status,
            "scan_scope": {
                "source_root": TEX_ROOT.relative_to(REPO_ROOT).as_posix(),
                "recursive_glob": "**/*.tex",
                "discovered_tex_files": len(discovered_files),
            },
            "expected_total": len(claims),
            "observed_total": sum(value["observed"] for value in file_counts.values()),
            "bare_status_table_entries": {
                "count": len(bare_table_status_entries),
                "required_count": 0,
                "role": "forbidden unwrapped status cells; every semantic NUMERICAL status must use the macro and appear in the claim inventory",
                "entries": bare_table_status_entries,
            },
            "file_counts": file_counts,
            "failures": failures,
        },
        current_claims,
        source_manifest,
    )


def recommended_disposition(
    claim: dict[str, Any], completed_checks: dict[str, dict[str, Any]]
) -> dict[str, Any]:
    claim_id = claim["id"]
    mapped = claim.get("check_ids", [])
    mapped_results = [completed_checks[cid] for cid in mapped if cid in completed_checks]
    replacement_ids = [item["check_id"] for item in mapped_results if item["status"] == "PASS"]
    unknown_check_ids = [cid for cid in mapped if cid not in completed_checks]
    disposition = claim["recommended_disposition"]
    reproducible = claim.get("current_protocol_reproducible")
    if reproducible is None:
        current_status = "NOT_APPLICABLE"
    elif reproducible is False:
        current_status = "INCONCLUSIVE"
    elif (
        mapped
        and not unknown_check_ids
        and len(mapped_results) == len(mapped)
        and all(item["status"] == "PASS" for item in mapped_results)
    ):
        current_status = "PASS"
    else:
        current_status = "FAIL"
    endpoint_mapping_status = (
        "PASS"
        if (
            current_status in {"PASS", "NOT_APPLICABLE"}
            or (
                current_status == "INCONCLUSIVE"
                and disposition == "retain_as_inconclusive"
                and bool(claim.get("missing_obligation"))
            )
        )
        else "FAIL"
    )
    return {
        "claim_id": claim_id,
        "source_file": claim["source_file"],
        "current_source_line": claim["current_source_line"],
        "load_bearing": claim["load_bearing"],
        "role": claim["role"],
        "current_protocol_status": current_status,
        "endpoint_mapping_status": endpoint_mapping_status,
        "recommended_disposition": disposition,
        "replacement_check_ids": replacement_ids,
        "declared_check_ids": mapped,
        "unknown_check_ids": unknown_check_ids,
        "missing_obligation": claim.get("missing_obligation"),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help=f"JSON result path (default: {DEFAULT_OUTPUT})",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    claims_bytes = CLAIMS_PATH.read_bytes()
    claims_document = json.loads(claims_bytes.decode("utf-8"))
    inventory, current_claims, tex_source_manifest = scan_inventory(
        claims_document["claims"]
    )
    inventory_manifest = {
        "hash_algorithm": "SHA-256",
        "hash_domain": "raw file bytes",
        "path_semantics": "repository-relative POSIX paths",
        "binding_scope": "Every recursively discovered TeX file under source_root, including files with zero NUMERICAL occurrences, and the core verification protocol files; generated current-results.json is excluded.",
        "source_root": TEX_ROOT.relative_to(REPO_ROOT).as_posix(),
        "tex_sources": tex_source_manifest,
        "protocol_files": {
            "claims.json": manifest_entry(CLAIMS_PATH, claims_bytes),
            "run_checks.py": manifest_entry(RUNNER_PATH),
            "requirements.txt": manifest_entry(REQUIREMENTS_PATH),
            "VERIFICATION.md": manifest_entry(VERIFICATION_PATH),
        },
    }
    checks: list[dict[str, Any]] = []
    for check in CHECKS:
        try:
            checks.append(check())
        except Exception as exc:  # fail closed and preserve diagnostics in JSON
            checks.append(
                {
                    "check_id": f"EXCEPTION-{check.__name__}",
                    "title": check.__name__,
                    "claim_ids": [],
                    "status": "FAIL",
                    "seed": None,
                    "sample_count": 0,
                    "expected": {},
                    "tolerances": {},
                    "observed": {
                        "exception_type": type(exc).__name__,
                        "exception_message": str(exc),
                        "traceback": traceback.format_exc(),
                    },
                    "evidence_kind": "mechanical_failure",
                    "interpretation": "The check raised an exception and provides no supporting evidence.",
                }
            )
    completed = {item["check_id"]: item for item in checks}
    dispositions = [recommended_disposition(claim, completed) for claim in current_claims]
    substantive = [
        item
        for item in dispositions
        if item["role"] not in {"taxonomy", "duplicate_reference"}
    ]
    taxonomy = [item for item in dispositions if item["role"] == "taxonomy"]
    duplicate_references = [
        item for item in dispositions if item["role"] == "duplicate_reference"
    ]
    supplemental_ids = claims_document.get("supplemental_check_ids", [])
    supplemental_validation = {
        "declared_ids": supplemental_ids,
        "unknown_ids": [cid for cid in supplemental_ids if cid not in completed],
        "nonpassing_ids": [
            cid
            for cid in supplemental_ids
            if cid in completed and completed[cid]["status"] != "PASS"
        ],
    }
    mapping_failures = [
        item["claim_id"]
        for item in dispositions
        if item["endpoint_mapping_status"] != "PASS"
    ]
    check_counts = {
        state: sum(item["status"] == state for item in checks)
        for state in ["PASS", "FAIL", "INCONCLUSIVE"]
    }
    disposition_counts = {
        disposition: sum(item["recommended_disposition"] == disposition for item in substantive)
        for disposition in [
            "keep_exact",
            "rewrite_to_current_check",
            "remove",
            "retain_as_inconclusive",
        ]
    }
    overall = (
        "PASS"
        if (
            inventory["status"] == "PASS"
            and check_counts["FAIL"] == 0
            and not mapping_failures
            and not supplemental_validation["unknown_ids"]
            and not supplemental_validation["nonpassing_ids"]
        )
        else "FAIL"
    )
    document = _jsonable(
        {
            "schema_version": "2.1",
            "overall_status": overall,
            "interpretation": "PASS is numerical corroboration under the current declared protocol. It is not a proof of an analytic claim and does not retroactively reproduce omitted historical inputs.",
            "environment": {
                "python": sys.version,
                "python_executable": sys.executable,
                "platform": platform.platform(),
                "machine": platform.machine(),
                "numpy": np.__version__,
                "scipy": scipy.__version__,
                "sympy": sp.__version__,
                "float_info": {
                    "mantissa_bits": sys.float_info.mant_dig,
                    "epsilon": sys.float_info.epsilon,
                },
            },
            "inventory_manifest": inventory_manifest,
            "inventory": inventory,
            "checks": checks,
            "claim_dispositions": dispositions,
            "mapping_validation": {
                "status": "PASS" if not mapping_failures else "FAIL",
                "claim_failures": mapping_failures,
                "supplemental_checks": supplemental_validation,
            },
            "summary": {
                "total_NUMERICAL_occurrences": inventory["observed_total"],
                "literal_status_macro_occurrences": inventory["observed_total"],
                "bare_status_table_entries": inventory["bare_status_table_entries"][
                    "count"
                ],
                "substantive_claims": len(substantive),
                "taxonomy_entries": len(taxonomy),
                "duplicate_register_entries": len(duplicate_references),
                "checks": check_counts,
                "dispositions_for_substantive_claims": disposition_counts,
                "current_protocol_claims_inconclusive": sum(
                    item["current_protocol_status"] == "INCONCLUSIVE"
                    for item in substantive
                ),
                "current_protocol_claims_pass": sum(
                    item["current_protocol_status"] == "PASS"
                    for item in substantive
                ),
            },
        }
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(document, indent=2, sort_keys=False) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "overall_status": overall,
                "output": str(args.output.resolve()),
                "inventory": inventory["status"],
                "occurrences": inventory["observed_total"],
                "checks": check_counts,
                "dispositions": disposition_counts,
            },
            sort_keys=True,
        )
    )
    return 0 if overall == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
