"""Standalone study of block-parent memory across source-prior locality families (X3)."""
from __future__ import annotations

import csv
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import platform
import subprocess
import sys
import time
from typing import Mapping

import torch

from .locality import (
    block_basis,
    block_mean_projector,
    fitted_decay_ratio,
    held_prior_action,
    independent_links,
    lyapunov_stationary,
    parent_memory,
    row_only_drift,
    source_prior,
)
from .network_dynamics import memory_information, ou_transition


def _fine_process(
    pi:       torch.Tensor,
    Omega:    torch.Tensor,
    dynamics: str,
    a:        float,
    kappa:    float,
    dt:       float,
) -> tuple[torch.Tensor, torch.Tensor, float, float, torch.Tensor | None]:
    r"""Return (F, Sigma, fine gap, Lyapunov residual, J) of the stationary fine law."""
    if dynamics == "joint_descent":
        J = held_prior_action(pi, Omega, a, kappa).J
        n = len(J)
        F = ou_transition(J, torch.zeros(n, dtype=J.dtype), torch.eye(n, dtype=J.dtype), dt).F
        Sigma = torch.cholesky_inverse(torch.linalg.cholesky(J))
        return F, (Sigma + Sigma.T) / 2, float(torch.linalg.eigvalsh(J)[0]), 0.0, J
    if dynamics == "row_only":
        K = row_only_drift(pi, Omega, a, kappa)
        Sigma = lyapunov_stationary(K)
        residual = K @ Sigma + Sigma @ K.T - 2 * torch.eye(len(K), dtype=K.dtype)
        gap = float(torch.linalg.eigvals(K).real.min())
        return torch.linalg.matrix_exp(-dt * K), Sigma, gap, float(residual.abs().max()), None
    raise ValueError(f"unknown dynamics {dynamics!r}")


def _filter_cross_check(
    J:  torch.Tensor,
    N:  int,
    K:  int,
    b:  int,
    dt: float,
    H:  int,
) -> float:
    r"""D_{H,1} through the existing hidden filter after the block-mean change of basis."""
    T, retained = block_basis(N, K, b)
    T_inv = torch.linalg.inv(T)
    J_new = T_inv.T @ J @ T_inv
    J_new = (J_new + J_new.T) / 2
    M_new = T @ T.T
    kernel = ou_transition(J_new, torch.zeros(len(J), dtype=J.dtype), (M_new + M_new.T) / 2, dt)
    Sigma = torch.cholesky_inverse(torch.linalg.cholesky(J_new))
    return float(memory_information(torch.zeros(len(J), dtype=J.dtype), (Sigma + Sigma.T) / 2,
                                    retained, [kernel] * (H - 1)).sum())


def measure_case(
    N:        int,
    case:     Mapping[str, object],
    Omega:    torch.Tensor,
    theory:   Mapping[str, object],
    numerics: Mapping[str, object],
) -> dict[str, object]:
    """Measure one (N, prior family, link setting, dynamics) instance."""
    start = time.perf_counter()
    a, kappa, dt = float(theory["a"]), float(theory["kappa"]), float(theory["dt"])
    b, H, k_max, K = int(theory["block"]), int(theory["horizon"]), int(theory["k_max"]), int(theory["dimension"])
    pi = source_prior(N, str(case["family"]), **dict(case.get("prior", {})))
    F, Sigma, gap, lyapunov_residual, J = _fine_process(pi, Omega, str(case["dynamics"]), a, kappa, dt)
    P = block_mean_projector(N, K, b)
    stable = N <= int(numerics["stable_kl_max_N"])
    gated = N <= int(numerics["identity_gate_max_N"])
    memory = parent_memory(Sigma, P, dt, H, k_max, F, path_kl=True, stable_kl=stable, direct_D=gated, fine_gap=gap)
    n_blocks = N // b
    D, delta, risk = memory.D, memory.delta, memory.row_risk
    D_check = memory.D_direct if gated else D
    naive = float(memory.path_kl_naive)
    kl = float(memory.path_kl) if stable else naive
    zero_floor = float(numerics["analytic_zero_floor"])
    analytic_zero = (case["family"] == "complete" and case["links"] == "identity"
                     and case["dynamics"] == "joint_descent"
                     and bool((Omega == torch.eye(K, dtype=Omega.dtype, device=Omega.device)).all()))

    def errors(reference: float) -> tuple[list[float], list[float | None]]:
        # Analytical Markov controls have no relative error, irrespective of numerical size.
        absolute = [abs(float(D_check[k] + risk[k]) - reference) for k in range(1, k_max + 1)]
        return absolute, [e / abs(reference) if not analytic_zero and abs(reference) > zero_floor else None for e in absolute]

    identity_abs, identity = errors(kl)
    record: dict[str, object] = {
        "N": N, "case": case["name"], "family": case["family"], "links": case["links"],
        "dynamics": case["dynamics"], "prior": case.get("prior", {}),
        "retained_dimension": len(P), "fine_dimension": N * K,
        "fine_gap": gap, "mass_gap_ratio_ceiling": float(torch.exp(torch.tensor(-gap * dt))),
        "lyapunov_residual_max_abs": lyapunov_residual,
        "D_per_block": [float(x) / n_blocks for x in D],
        "delta_per_block": [float(x) / n_blocks for x in delta],
        "row_risk_per_block": [None] + [float(x) / n_blocks for x in risk[1:]],
        "activation_b0": 0.0,
        "path_kl_total": kl,
        "path_kl_per_block": kl / n_blocks,
        "analytic_zero": analytic_zero,
        "numerical_near_zero": abs(kl) <= zero_floor,
        "path_kl_method": "eigen_log1p" if stable else "trace_logdet",
        "path_kl_naive_per_block": naive / n_blocks,
        "identity_D_route": "direct_log1p" if gated else "toeplitz_logdet",
        "identity_abs_error": identity_abs,  # historical field, total nats
        "identity_abs_error_total_nats": identity_abs,
        "identity_abs_error_per_block_nats": [e / n_blocks for e in identity_abs],
        "identity_relative_error": identity,
        "identity_relative_error_naive_kl": errors(naive)[1],
        "identity_gated": gated,
        "D_direct_per_block": [float(x) / n_blocks for x in memory.D_direct] if gated else None,
        "D_toeplitz_vs_direct_abs_error": (max(abs(float(x - y)) for x, y in zip(D, memory.D_direct))
                                           if gated else None),
        "D_nonincreasing": bool(all(float(D[k + 1]) <= float(D[k]) + 1e-12 * max(1.0, abs(float(D[0])))
                                    for k in range(k_max))),
        "ratio_delta_fit_k1_5": fitted_decay_ratio(delta, range(1, k_max + 1)),
        "ratio_D_fit_k1_5": fitted_decay_ratio(D, range(1, k_max + 1)),
        "ratio_D_successive": [float(D[k + 1] / D[k]) if float(D[k]) > 0 else None for k in range(k_max)],
        "logdets": [float(x) for x in memory.logdets],
    }
    if J is not None and N <= int(numerics["filter_check_max_N"]):
        filtered = _filter_cross_check(J, N, K, b, dt, H)
        record["filter_D1_abs_error"] = abs(filtered - float(D_check[1]))
        record["filter_D1_relative_error"] = (record["filter_D1_abs_error"] / abs(float(D_check[1]))
                                              if not analytic_zero and abs(float(D_check[1])) > zero_floor else None)
    record["seconds"] = time.perf_counter() - start
    return record


def _max(values: list[float | None]) -> float | None:
    """Maximum over the defined entries, None when none is defined."""
    defined = [v for v in values if v is not None]
    return max(defined) if defined else None


def _git_revision(root: Path) -> str:
    try:
        return subprocess.run(["git", "rev-parse", "HEAD"], cwd=root, capture_output=True, text=True, check=True).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return "unknown"


def run_locality_parent_memory(
    run:      Mapping[str, object],
    theory:   Mapping[str, object],
    numerics: Mapping[str, object],
    output:   Mapping[str, object],
) -> Path:
    """Run every declared case, writing per-case JSON lines, a CSV summary and checks."""
    torch.set_num_threads(int(numerics["cpu_threads"]))
    directory = Path(str(output["root"]))
    directory.mkdir(parents=True, exist_ok=True)
    root = Path(__file__).resolve().parents[4]
    meta = {
        "run": dict(run), "theory": dict(theory), "numerics": dict(numerics),
        "started_utc": datetime.now(timezone.utc).isoformat(),
        "python": sys.version, "executable": sys.executable, "torch": torch.__version__,
        "cuda_available": torch.cuda.is_available(), "device_used": "cpu",
        "torch_threads": torch.get_num_threads(), "platform": platform.platform(),
        "processor": platform.processor(), "git_head": _git_revision(root),
        "env": {k: os.environ.get(k) for k in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "MKL_THREADING_LAYER")},
    }
    records: list[dict[str, object]] = []
    total = time.perf_counter()
    with open(directory / "cases.jsonl", "w", encoding="utf-8") as stream:
        for N in theory["n_agents"]:
            links = {"gl2": independent_links(N, int(theory["dimension"]), float(theory["link_sigma"]), int(run["seed"]) + N),
                     "identity": independent_links(N, int(theory["dimension"]), 0.0, 0)}
            for case in theory["cases"]:
                record = measure_case(N, case, links[str(case["links"])], theory, numerics)
                records.append(record)
                stream.write(json.dumps(record) + "\n")
                stream.flush()
                print(f"N={N:5d} {case['name']:28s} D1/blk={record['D_per_block'][1]:.3e} "
                      f"rho_delta={record['ratio_delta_fit_k1_5']} id_rel={_max(record['identity_relative_error'])} "
                      f"id_abs={max(record['identity_abs_error']):.1e} "
                      f"{record['seconds']:.1f}s", flush=True)
    columns = ["N", "case", "fine_gap", "mass_gap_ratio_ceiling", "path_kl_per_block",
               *[f"D{k}_per_block" for k in range(int(theory["k_max"]) + 1)],
               *[f"delta{k}_per_block" for k in range(int(theory["k_max"]) + 1)],
               *[f"row_risk{k}_per_block" for k in range(1, int(theory["k_max"]) + 1)],
               "ratio_delta_fit_k1_5", "ratio_D_fit_k1_5", "max_identity_relative_error", "D_nonincreasing", "seconds"]
    with open(directory / "summary.csv", "w", newline="", encoding="utf-8") as stream:
        writer = csv.writer(stream)
        writer.writerow(columns)
        for r in records:
            writer.writerow([r["N"], r["case"], r["fine_gap"], r["mass_gap_ratio_ceiling"], r["path_kl_per_block"],
                             *r["D_per_block"], *r["delta_per_block"], *r["row_risk_per_block"][1:],
                             r["ratio_delta_fit_k1_5"], r["ratio_D_fit_k1_5"], _max(r["identity_relative_error"]),
                             r["D_nonincreasing"], r["seconds"]])
    gated = [r for r in records if r["identity_gated"]]
    relative = [r for r in gated if r["identity_relative_error"][0] is not None]
    checks = {
        "identity_gate_passed": all(_max(r["identity_relative_error"]) <= 1e-9 for r in relative),
        "identity_gate_cases_relative": len(relative),
        "identity_gate_cases_analytic_zero": [(r["N"], r["case"], max(r["identity_abs_error_total_nats"]))
                                             for r in gated if r["analytic_zero"]],
        "identity_cases_analytic_zero": [(r["N"], r["case"], max(r["identity_abs_error_total_nats"]),
                                         max(r["identity_abs_error_per_block_nats"]))
                                        for r in records if r["analytic_zero"]],
        "identity_cases_numerical_near_zero": [(r["N"], r["case"]) for r in records
                                               if r["numerical_near_zero"] and not r["analytic_zero"]],
        "identity_absolute_error_units": {"identity_gate_cases_analytic_zero": "total nats",
                                          "identity_cases_analytic_zero": ["total nats", "nats per retained block"]},
        "identity_max_relative_error_gated": max((_max(r["identity_relative_error"]) for r in relative), default=None),
        "identity_max_relative_error_ungated": max((_max(r["identity_relative_error"]) for r in records
                                                    if not r["identity_gated"] and r["identity_relative_error"][0] is not None), default=None),
        "D_toeplitz_vs_direct_max_abs_error": max(r["D_toeplitz_vs_direct_abs_error"] for r in gated),
        "D_nonincreasing_all": all(r["D_nonincreasing"] for r in records),
        "filter_cross_check": [(r["case"], r["filter_D1_abs_error"], r["filter_D1_relative_error"])
                               for r in records if "filter_D1_abs_error" in r],
        "lyapunov_residual_max_abs": max(r["lyapunov_residual_max_abs"] for r in records),
    }
    meta.update({"finished_utc": datetime.now(timezone.utc).isoformat(),
                 "total_seconds": time.perf_counter() - total, "checks": checks})
    (directory / "result.json").write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(checks, indent=2))
    return directory
