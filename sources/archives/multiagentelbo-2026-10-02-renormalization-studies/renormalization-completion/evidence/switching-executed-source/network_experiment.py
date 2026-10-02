"""Finite held-link Gaussian network study at one base point."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import platform
import sys
import time
import traceback
from typing import Mapping

import numpy as np
import torch

from .network import assemble_network, marginalize, realify_map


@dataclass(frozen=True)
class GaussianNetworkCase:
    J_0:       torch.Tensor
    mu_0:      torch.Tensor
    A_e:       torch.Tensor
    B_e:       torch.Tensor
    Gamma_inv: torch.Tensor
    o_e:       torch.Tensor
    edges:     torch.Tensor
    metadata:  Mapping[str, object]


@dataclass(frozen=True)
class GaussianNetworkExperimentResult:
    run_dir: Path
    status:  str


def _normal(shape: tuple[int, ...], generator: torch.Generator) -> torch.Tensor:
    """Draw float64 CPU values so device lanes receive identical seeded inputs."""
    return torch.randn(shape, generator=generator, dtype=torch.float64)


def build_network_case(
    kind:       str,
    n_agents:   int,
    dimension:  int,
    seed:       int,
    link_scale: float = 0.2,
) -> GaussianNetworkCase:
    r"""Build normalized records with residuals A_e x_i - B_e x_j - o_e."""
    generator = torch.Generator(device="cpu").manual_seed(seed)
    nodes = torch.arange(n_agents, dtype=torch.long)
    # Two directed records per receiver; this is a declared finite graph family.
    edges = torch.cat(
        [torch.stack((nodes, (nodes + stride) % n_agents), dim=1) for stride in (1, 17)]
    )
    n_edges = edges.shape[0]
    complex_case = kind in ("complex_gl", "su")
    node_dimension = 2 * dimension if complex_case else dimension
    identity = torch.eye(node_dimension, dtype=torch.float64)
    if complex_case:
        Z = _normal((n_agents, dimension, dimension), generator).to(torch.complex128)
        Z = Z + 1j * _normal((n_agents, dimension, dimension), generator)
        H_0 = Z.mH @ Z + torch.eye(dimension, dtype=torch.complex128)
        # Circular complex exp[-(z-mu)^* H (z-mu)] has real precision 2 R(H).
        J_0 = 2 * realify_map(H_0)
    else:
        Z = _normal((n_agents, dimension, dimension), generator)
        J_0 = Z.mT @ Z + identity
    mu_0 = 0.1 * _normal((n_agents, node_dimension), generator)
    observed = 0.1 * _normal((n_edges, node_dimension), generator)
    A_e = identity.expand(n_edges, -1, -1).clone()
    map_specs: dict[str, object]
    if kind == "flat_real_gl":
        U = torch.linalg.matrix_exp(link_scale * _normal((n_agents, dimension, dimension), generator))
        L = U[edges[:, 0]] @ torch.linalg.inv(U[edges[:, 1]])
        B_e = L
        map_specs = {"group": f"GL+({dimension},R)", "map": "B_e=U_i U_j^{-1}; A_e=I"}
    elif kind == "independent_real_gl":
        L = torch.linalg.matrix_exp(link_scale * _normal((n_edges, dimension, dimension), generator))
        B_e = L
        map_specs = {"group": f"GL+({dimension},R)", "map": "independent B_e=exp(G_e); A_e=I"}
    elif kind == "matrix":
        # Rank-one communication with distinct rectangular query and key maps.
        P = _normal((n_edges, dimension, 1), generator)
        Q = _normal((n_edges, 1, dimension), generator)
        L = link_scale * (P @ Q)
        A_e = _normal((n_edges, 1, dimension), generator)
        S_K = _normal((n_edges, 1, dimension), generator)
        B_e = S_K @ L
        map_specs = {
            "group": "matrix communication",
            "map": "L_e=scale P_e Q_e; A_e=S_Q_e; B_e=S_K_e L_e",
            "communication_rank": 1,
            "comparison_dimension": 1,
        }
    elif complex_case:
        G = _normal((n_edges, dimension, dimension), generator).to(torch.complex128)
        G = G + 1j * _normal((n_edges, dimension, dimension), generator)
        if kind == "su":
            H = (G + G.mH) / 2
            trace = torch.diagonal(H, dim1=-2, dim2=-1).sum(-1)
            H = H - (trace / dimension)[:, None, None] * torch.eye(dimension, dtype=torch.complex128)
            L = torch.linalg.matrix_exp(1j * link_scale * H)
            group = f"SU({dimension})"
        else:
            L = torch.linalg.matrix_exp(link_scale * G)
            group = f"GL({dimension},C)"
        B_e = realify_map(L)
        map_specs = {
            "group": group,
            "map": "A_e=I; B_e=R(L_e), R(L)=[[Re L,-Im L],[Im L,Re L]]",
            "coordinate_order": "Re coordinates, then Im coordinates, within each node",
            "complex_precision_conversion": "J_0=2 R(H_0) for exp[-(z-mu)^* H_0 (z-mu)]",
            "record_convention": "normalized real Gaussian; Gamma_inv is its real precision",
        }
    else:
        raise ValueError(f"Unknown held-link case {kind!r}")
    record_dimension = A_e.shape[1]
    Gamma_inv = 0.25 * torch.eye(record_dimension, dtype=torch.float64).expand(n_edges, -1, -1).clone()
    o_e = observed[:, :record_dimension]
    map_specs["first_two_map_commutator_norm"] = float(torch.linalg.vector_norm(L[0] @ L[1] - L[1] @ L[0]))
    metadata = {
        "case": kind,
        "n_agents": n_agents,
        "group_dimension": dimension,
        "real_node_dimension": node_dimension,
        "n_records": n_edges,
        "record_dimension": record_dimension,
        "graph": "directed sparse cycle plus stride-17 chords, fixed across cases",
        "held_variables": ["graph", "source assignments", "frames/structural maps", "comparison maps", "record precisions", "observed records"],
        "integrated_variables": "real node coordinates only",
        "latent_link_prior": None,
        "normalization": "proper independent node priors and normalized real Gaussian record likelihoods",
        **map_specs,
    }
    return GaussianNetworkCase(J_0, mu_0, A_e, B_e, Gamma_inv, o_e, edges, metadata)


def _comparison(
    observed: torch.Tensor,
    expected: torch.Tensor,
    atol:     float,
    rtol:     float,
) -> dict[str, object]:
    """Record numerical equality and its largest absolute residual."""
    return {
        "passed": bool(torch.allclose(observed, expected, atol=atol, rtol=rtol)),
        "max_abs_error": float((observed - expected).abs().max()),
    }


def _coordinates(n_agents: int, dimension: int, stride: int, device: torch.device) -> torch.Tensor:
    """Retain all coordinates of every stride-th node in ascending node order."""
    nodes = torch.arange(0, n_agents, stride, device=device)
    return (nodes[:, None] * dimension + torch.arange(dimension, device=device)).reshape(-1)


def measure_network_case(
    case:   GaussianNetworkCase,
    atol:   float,
    rtol:   float,
    device: torch.device,
) -> tuple[dict[str, object], dict[str, np.ndarray]]:
    r"""Compare complete Schur laws and reverse conditionals to the fine Gaussian."""
    tensors = [getattr(case, name).to(device) for name in ("J_0", "mu_0", "A_e", "B_e", "Gamma_inv", "o_e", "edges")]
    action = assemble_network(*tensors)
    mu, Sigma = action.moments()
    n_agents, dimension = tensors[1].shape
    retained = _coordinates(n_agents, dimension, 4, device)
    first_retained = _coordinates(n_agents, dimension, 2, device)
    parent = marginalize(retained, action)
    first_parent = marginalize(first_retained, action)
    second_retained = _coordinates(first_retained.numel() // dimension, dimension, 2, device)
    staged = marginalize(second_retained, first_parent.action)
    mu_c, Sigma_c = parent.action.moments()
    selected_Sigma = Sigma.index_select(0, retained).index_select(1, retained)
    lifted_mu, lifted_Sigma = parent.lift_moments(mu_c, Sigma_c)
    fine_mass, parent_mass, staged_mass = action.log_mass(), parent.action.log_mass(), staged.action.log_mass()
    checks = {
        "fine_parent_log_mass": _comparison(parent_mass, fine_mass, atol, rtol),
        "fine_staged_log_mass": _comparison(staged_mass, fine_mass, atol, rtol),
        "retained_mean_selector": _comparison(mu_c, mu[retained], atol, rtol),
        "retained_covariance_selector": _comparison(Sigma_c, selected_Sigma, atol, rtol),
        "direct_staged_precision": _comparison(staged.action.J, parent.action.J, atol, rtol),
        "direct_staged_information": _comparison(staged.action.h, parent.action.h, atol, rtol),
        "direct_staged_energy_offset": _comparison(staged.action.c, parent.action.c, atol, rtol),
        "reverse_conditional_mean_recovery": _comparison(lifted_mu, mu, atol, rtol),
        "reverse_conditional_covariance_recovery": _comparison(lifted_Sigma, Sigma, atol, rtol),
    }
    defect = parent.markov_defect()
    result = {
        **case.metadata,
        "status": "pass" if all(row["passed"] for row in checks.values()) else "fail",
        "fine_dimension": action.h.numel(),
        "retained_agents": retained.numel() // dimension,
        "retained_dimension": retained.numel(),
        "fine_log_evidence": float(fine_mass),
        "parent_log_evidence": float(parent_mass),
        "staged_log_evidence": float(staged_mass),
        "checks": checks,
        "held_ou": {
            "kinetics": "dx=-(J x-h)dt+sqrt(2)dW, identity mobility",
            "markov_defect_frobenius_norm": float(torch.linalg.vector_norm(defect)),
            "markov_defect_trace": float(torch.trace(defect)),
            "scope": "generator discrepancy for this declared held OU; no autonomous parent dynamics or formation claim",
        },
    }
    arrays = {
        "J_0": tensors[0], "mu_0": tensors[1], "A_e": tensors[2], "B_e": tensors[3],
        "Gamma_inv": tensors[4], "o_e": tensors[5], "edges": tensors[6],
        "fine_J": action.J, "fine_h": action.h, "fine_c": action.c,
        "retained": retained, "parent_J": parent.action.J, "parent_h": parent.action.h,
        "parent_c": parent.action.c, "parent_mu": mu_c, "parent_Sigma": Sigma_c,
    }
    return result, {name: value.detach().cpu().numpy() for name, value in arrays.items()}


def _write_json(path: Path, value: Mapping[str, object]) -> None:
    path.write_text(json.dumps(value, indent=2, allow_nan=False) + "\n", encoding="utf-8")


def run_gaussian_network_experiment(
    run:      Mapping[str, object],
    theory:   Mapping[str, object],
    numerics: Mapping[str, object],
    output:   Mapping[str, object],
) -> GaussianNetworkExperimentResult:
    """Execute one seeded finite-network baseline, retaining every comparison/error."""
    if numerics["dtype"] != "float64" or int(numerics["cpu_threads"]) != 1:
        raise ValueError("This baseline requires float64 and one CPU thread")
    n_agents, dimension = int(theory["n_agents"]), int(theory["dimension"])
    if n_agents < 4 or n_agents % 4 or dimension < 2:
        raise ValueError("Use a positive agent count divisible by four and dimension at least two")
    device = torch.device(str(numerics["device"]))
    if device.type not in ("cpu", "cuda"):
        raise ValueError("Device must be cpu or cuda")
    if device.type == "cuda" and not torch.cuda.is_available():
        raise RuntimeError("The selected CUDA lane is unavailable in this interpreter")
    torch.set_num_threads(1)
    root = Path(str(output["root"])).expanduser()
    if not root.is_absolute():
        root = Path(__file__).resolve().parents[4] / root
    directory = root / "pointwise-gaussian-network" / datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    directory.mkdir(parents=True)
    record: dict[str, object] = {
        "status": "running",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "command": [sys.executable, *sys.orig_argv[1:]],
        "runtime": {
            "interpreter": sys.executable, "python": sys.version, "torch": torch.__version__,
            "cuda_available": torch.cuda.is_available(), "device": str(device),
            "cpu_threads": torch.get_num_threads(), "platform": platform.platform(),
            "thread_environment": {name: os.environ.get(name) for name in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS")},
        },
        "profile": {"RUN": dict(run), "THEORY": dict(theory), "NUMERICS": dict(numerics), "OUTPUT": dict(output)},
        "scope": "finite conditional Gaussian coarse-graining at c_* with observed/held links; no mixture closure, link dynamics, formation, or thermodynamic limit established",
        "cases": [],
    }
    _write_json(directory / "result.json", record)
    started = time.perf_counter()
    try:
        with torch.no_grad():
            for kind in theory["cases"]:
                print(f"Running {kind}: N={n_agents}, group dimension={dimension}, {device}", flush=True)
                case_start = time.perf_counter()
                case = build_network_case(str(kind), n_agents, dimension, int(run["seed"]), float(theory["link_scale"]))
                result, arrays = measure_network_case(case, float(numerics["atol"]), float(numerics["rtol"]), device)
                result["elapsed_seconds"] = time.perf_counter() - case_start
                _write_json(directory / f"{kind}.json", result)
                if output["save_arrays"]:
                    np.savez_compressed(directory / f"{kind}.npz", **arrays)
                record["cases"].append(result)
                _write_json(directory / "result.json", record)
                if result["status"] != "pass":
                    raise ArithmeticError(f"Numerical parity failed for {kind}; see {directory}")
                print(f"{kind}: pass in {result['elapsed_seconds']:.3f}s", flush=True)
        record["status"] = "pass"
    except Exception as error:
        record.update(status="failed", error=f"{type(error).__name__}: {error}", traceback=traceback.format_exc())
        raise
    finally:
        record["elapsed_seconds"] = time.perf_counter() - started
        _write_json(directory / "result.json", record)
    print(f"run_dir={directory}", flush=True)
    return GaussianNetworkExperimentResult(directory, "pass")
