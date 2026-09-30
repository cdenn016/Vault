"""Conditional Gaussian path study for deterministic observed link schedules."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
import json
from math import log, pi
import os
from pathlib import Path
import platform
import sys
import time
import traceback
from typing import Mapping, Sequence

import numpy as np
import torch

from .network import assemble_network, realify_map
from .network_dynamics import (
    GaussianTransition,
    initialize_filter,
    markov_projection,
    memory_information,
    ou_transition,
    propagate_moments,
)
from .network_experiment import GaussianNetworkCase, build_network_case


@dataclass(frozen=True)
class GaussianNetworkDynamicsResult:
    run_dir: Path
    status:  str


def _symmetric(Sigma: torch.Tensor) -> torch.Tensor:
    return (Sigma + Sigma.T) / 2


def _logdet(Sigma: torch.Tensor) -> torch.Tensor:
    return 2 * torch.linalg.cholesky(Sigma).diagonal().log().sum()


def _comparison(
    observed: torch.Tensor,
    expected: torch.Tensor,
    atol:     float,
    rtol:     float,
) -> dict[str, object]:
    return {
        "passed": bool(torch.allclose(observed, expected, atol=atol, rtol=rtol)),
        "max_abs_error": float((observed - expected).abs().max()),
    }


def _motion_generator(
    B_e:      torch.Tensor,
    strength: float,
    n_agents: int,
    dimension:int,
    seed:     int,
    kind:     str,
) -> torch.Tensor:
    """Construct seeded observed controls; SU controls lie in its Lie algebra."""
    generator = torch.Generator(device="cpu").manual_seed(seed + 1)
    count = n_agents if kind == "flat_real_gl" else len(B_e)
    G = torch.randn((count, dimension, dimension), dtype=torch.float64, generator=generator)
    if kind in ("complex_gl", "su"):
        imaginary = torch.randn(G.shape, dtype=torch.float64, generator=generator)
        G = G.to(torch.complex128) + 1j * imaginary
        if kind == "su":
            H = (G + G.mH) / 2
            trace = torch.diagonal(H, dim1=-2, dim2=-1).sum(-1)
            H = H - (trace / dimension)[:, None, None] * torch.eye(dimension, dtype=H.dtype)
            G = 1j * H
    return (strength * G).to(B_e.device)


def _moving_source_map(
    B_0:      torch.Tensor,
    G:        torch.Tensor,
    edges:    torch.Tensor,
    t:        float,
    dimension:int,
    kind:     str,
) -> torch.Tensor:
    r"""Return scheduled maps, including flat V_i B_0 V_j^-1 and L_0 exp(tG)."""
    flow = torch.linalg.matrix_exp(t * G)
    if kind == "flat_real_gl":
        return flow[edges[:, 0]] @ B_0 @ torch.linalg.inv(flow[edges[:, 1]])
    if kind == "matrix":
        return B_0 @ flow
    if kind in ("complex_gl", "su"):
        L_0 = B_0[:, :dimension, :dimension].to(torch.complex128) + 1j * B_0[:, dimension:, :dimension]
        return realify_map(flow @ L_0)
    return flow @ B_0


def retained_path_moments(
    mu_0:        torch.Tensor,
    Sigma_0:     torch.Tensor,
    retained:    torch.Tensor,
    transitions: Sequence[GaussianTransition],
) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor, list[GaussianTransition]]:
    r"""Construct actual and one-step Markov path moments without a fine path matrix.

    Cov(X_next,R_j)=F Cov(X,R_j). The Markov product instead propagates
    each earlier retained cross covariance through its actual-pair coarse F.
    """
    r, n_times = len(retained), len(transitions) + 1
    actual_mu = mu_0.new_empty(n_times * r)
    markov_mu = mu_0.new_empty(n_times * r)
    actual_Sigma = Sigma_0.new_zeros((n_times * r, n_times * r))
    markov_Sigma = torch.zeros_like(actual_Sigma)
    initial_covariance = Sigma_0[retained][:, retained]
    actual_mu[:r] = markov_mu[:r] = mu_0[retained]
    actual_Sigma[:r, :r] = markov_Sigma[:r, :r] = initial_covariance
    history_cross = [Sigma_0[:, retained]]  # (fine dimension,r) for each earlier R_j.
    kernels: list[GaussianTransition] = []
    mu, Sigma = mu_0, Sigma_0
    for step, transition in enumerate(transitions):
        kernel = markov_projection(mu, Sigma, transition, retained)
        kernels.append(kernel)
        mu, Sigma = propagate_moments(mu, Sigma, transition)
        history_cross = [transition.F @ cross for cross in history_cross]
        end, next_end = (step + 1) * r, (step + 2) * r
        next_slice = slice(end, next_end)
        current_slice = slice(end - r, end)
        actual_mu[next_slice] = mu[retained]
        actual_Sigma[next_slice, next_slice] = Sigma[retained][:, retained]
        actual_cross = torch.cat([cross[retained] for cross in history_cross], dim=1)
        actual_Sigma[next_slice, :end] = actual_cross
        actual_Sigma[:end, next_slice] = actual_cross.T
        markov_mu[next_slice] = kernel.F @ markov_mu[current_slice] + kernel.u
        markov_cross = kernel.F @ markov_Sigma[current_slice, :end]
        markov_Sigma[next_slice, :end] = markov_cross
        markov_Sigma[:end, next_slice] = markov_cross.T
        markov_Sigma[next_slice, next_slice] = _symmetric(
            kernel.F @ markov_Sigma[current_slice, current_slice] @ kernel.F.T + kernel.Q
        )
        history_cross.append(Sigma[:, retained])
    return actual_mu, _symmetric(actual_Sigma), markov_mu, _symmetric(markov_Sigma), kernels


def _path_kl(
    mu:         torch.Tensor,
    Sigma:      torch.Tensor,
    mu_markov:  torch.Tensor,
    Sigma_markov:torch.Tensor,
) -> torch.Tensor:
    r"""Direct D(N(mu,Sigma)||N(mu_M,Sigma_M)) on the complete retained path."""
    L = torch.linalg.cholesky(Sigma_markov)
    displacement = mu - mu_markov
    trace = torch.cholesky_solve(Sigma, L).diagonal().sum()
    quadratic = displacement @ torch.cholesky_solve(displacement[:, None], L)[:, 0]
    return (trace + quadratic - len(mu) + _logdet(Sigma_markov) - _logdet(Sigma)) / 2


def _full_history_forecast(
    path_mu:    torch.Tensor,
    path_Sigma: torch.Tensor,
    history:    torch.Tensor,
    step:       int,
    dimension:  int,
) -> tuple[torch.Tensor, torch.Tensor]:
    r"""Condition the independently assembled path Gaussian on its full prefix."""
    end = (step + 1) * dimension
    next_slice = slice(end, end + dimension)
    cross = path_Sigma[next_slice, :end]
    gain = torch.cholesky_solve(cross.T, torch.linalg.cholesky(path_Sigma[:end, :end])).T
    mu = path_mu[next_slice] + gain @ (history[:end] - path_mu[:end])
    Sigma = _symmetric(path_Sigma[next_slice, next_slice] - gain @ cross.T)
    return mu, Sigma


def measure_network_dynamics(
    case:            GaussianNetworkCase,
    dt:              float,
    motion_strength: float,
    atol:            float,
    rtol:            float,
    n_steps:         int,
    dimension:       int,
    seed:            int,
    kind:            str,
    device:          torch.device,
) -> tuple[dict[str, object], dict[str, np.ndarray]]:
    r"""Compare retained Gaussian paths, optimal one-step rows, and exact filtering."""
    inputs = {name: getattr(case, name).to(device) for name in ("J_0", "mu_0", "A_e", "B_e", "Gamma_inv", "o_e", "edges")}
    base_action = assemble_network(*(inputs[name] for name in ("J_0", "mu_0", "A_e", "B_e", "Gamma_inv", "o_e", "edges")))
    mu_base, Sigma_base = base_action.moments()
    # Declared actual preparation differs from the equilibrium of the initial action.
    mu_0 = mu_base + 0.03 * torch.cos(torch.arange(len(mu_base), dtype=mu_base.dtype, device=device))
    Sigma_0 = 1.2 * Sigma_base
    n_agents, node_dimension = inputs["mu_0"].shape
    nodes = torch.arange(0, n_agents, 4, device=device)
    retained = (nodes[:, None] * node_dimension + torch.arange(node_dimension, device=device)).reshape(-1)
    G = _motion_generator(inputs["B_e"], motion_strength, n_agents, dimension, seed, kind)
    mobility = torch.eye(len(mu_0), dtype=mu_0.dtype, device=device)
    transitions: list[GaussianTransition] = []
    for step in range(n_steps):
        B_e = _moving_source_map(inputs["B_e"], G, inputs["edges"], step * dt, dimension, kind)
        action = assemble_network(inputs["J_0"], inputs["mu_0"], inputs["A_e"], B_e, inputs["Gamma_inv"], inputs["o_e"], inputs["edges"])
        transitions.append(ou_transition(action.J, action.h, mobility, dt))
    path_mu, path_Sigma, markov_mu, markov_Sigma, kernels = retained_path_moments(mu_0, Sigma_0, retained, transitions)
    information = memory_information(mu_0, Sigma_0, retained, transitions)
    direct_kl = _path_kl(path_mu, path_Sigma, markov_mu, markov_Sigma)
    checks = {"direct_path_kl_vs_innovation_sum": _comparison(direct_kl, information.sum(), atol, rtol)}
    r = len(retained)
    history = path_mu.clone()
    # A declared observed retained prefix exercises nonzero conditional mean updates.
    for step in range(1, n_steps + 1):
        history[step * r:(step + 1) * r] += 0.01 * torch.sin(torch.arange(r, dtype=mu_0.dtype, device=device) + step)
    state = initialize_filter(mu_0, Sigma_0, retained, history[:r])
    forecasts: list[torch.Tensor] = []
    for step, transition in enumerate(transitions):
        end, next_end = (step + 1) * r, (step + 2) * r
        next_slice, pair_slice = slice(end, next_end), slice(end - r, next_end)
        checks[f"step_{step + 1}_one_time_mean"] = _comparison(markov_mu[next_slice], path_mu[next_slice], atol, rtol)
        checks[f"step_{step + 1}_one_time_covariance"] = _comparison(markov_Sigma[next_slice, next_slice], path_Sigma[next_slice, next_slice], atol, rtol)
        checks[f"step_{step + 1}_pair_covariance"] = _comparison(markov_Sigma[pair_slice, pair_slice], path_Sigma[pair_slice, pair_slice], atol, rtol)
        forecast = state.predict(transition, history[end - r:end])
        expected_mu, expected_Sigma = _full_history_forecast(path_mu, path_Sigma, history, step, r)
        checks[f"step_{step + 1}_history_forecast_mean"] = _comparison(forecast.mu_r, expected_mu, atol, rtol)
        checks[f"step_{step + 1}_history_forecast_covariance"] = _comparison(forecast.Sigma_r, expected_Sigma, atol, rtol)
        residual = history[next_slice] - expected_mu
        quadratic = residual @ torch.cholesky_solve(residual[:, None], torch.linalg.cholesky(expected_Sigma))[:, 0]
        expected_log_probability = -(r * log(2 * pi) + _logdet(expected_Sigma) + quadratic) / 2
        checks[f"step_{step + 1}_history_predictive_log_density"] = _comparison(forecast.log_prob(history[next_slice]), expected_log_probability, atol, rtol)
        forecasts.append(forecast.Sigma_r)
        state = state.condition(forecast, history[next_slice])
    motion_description = {
        "flat_real_gl": "V_i(t)=exp(tG_i); B_e(t)=V_i(t) B_e(0) V_j(t)^{-1}",
        "independent_real_gl": "B_e(t)=exp(tG_e) B_e(0)",
        "matrix": "B_e(t)=B_e(0) exp(tG_e), equivalent to fixed S_K and L_e(t)=L_e(0) exp(tG_e)",
        "complex_gl": "L_e(t)=exp(tG_e) L_e(0), explicitly realified",
        "su": "L_e(t)=exp(tG_e) L_e(0), G_e anti-Hermitian and traceless, explicitly realified",
    }[kind]
    result = {
        **case.metadata,
        "status": "pass" if all(row["passed"] for row in checks.values()) else "fail",
        "held_variables": ["graph", "source assignments", "node prior parameters", "receiver comparison maps", "record precisions", "observed records"],
        "observed_dynamic_variables": ["source comparison maps under the declared deterministic schedule"],
        "integrated_variables": "fine node coordinates along the retained path",
        "activation": "mu_0=initial-action mean+0.03 cos(arange(d)); Sigma_0=1.2 initial-action covariance",
        "kinetics": "identity-mobility reversible OU with the current action frozen over each interval",
        "motion": motion_description,
        "motion_strength": motion_strength,
        "interval_start_times": [step * dt for step in range(n_steps)],
        "dt": dt,
        "n_steps": n_steps,
        "fine_dimension": len(mu_0),
        "retained_agents": r // node_dimension,
        "retained_dimension": r,
        "direct_retained_path_kl_to_optimal_markov_product": float(direct_kl),
        "innovation_information_per_step": information.detach().cpu().tolist(),
        "innovation_information_total": float(information.sum()),
        "first_and_later_information": "observed values for this preparation and schedule; no positivity threshold is an acceptance gate",
        "checks": checks,
        "scope": "observed externally supplied link motion with fixed priors, comparison maps, source assignments and records; conditional reference, without endogenous learning or an autonomous small parent",
        "array_scope": "base record inputs, seeded motion generators, observed prefix, retained forecasts and final covariance; excludes a fine-state path matrix",
    }
    arrays = {
        **inputs, "motion_generator": G, "retained": retained,
        "actual_initial_mu": mu_0, "retained_path_mu": path_mu, "observed_retained_prefix": history,
        "final_retained_covariance": path_Sigma[-r:, -r:],
        "history_forecast_covariances": torch.stack(forecasts),
        "optimal_markov_noise_covariances": torch.stack([kernel.Q for kernel in kernels]),
        "innovation_information": information,
    }
    return result, {name: value.detach().cpu().numpy() for name, value in arrays.items()}


def _write_json(path: Path, value: Mapping[str, object]) -> None:
    path.write_text(json.dumps(value, indent=2, allow_nan=False) + "\n", encoding="utf-8")


def run_gaussian_network_dynamics_experiment(
    run:      Mapping[str, object],
    theory:   Mapping[str, object],
    numerics: Mapping[str, object],
    output:   Mapping[str, object],
) -> GaussianNetworkDynamicsResult:
    """Run a finite conditional path comparison and retain its actual errors/results."""
    if numerics["dtype"] != "float64" or int(numerics["cpu_threads"]) != 1:
        raise ValueError("This reference study requires float64 and one CPU thread")
    n_agents, dimension, n_steps = int(theory["n_agents"]), int(theory["dimension"]), int(theory["n_steps"])
    if n_agents < 4 or n_agents % 4 or dimension < 2 or n_steps < 1:
        raise ValueError("Require at least four agents divisible by four, dimension at least two, and a positive step count")
    device = torch.device(str(numerics["device"]))
    if device.type not in ("cpu", "cuda"):
        raise ValueError("Device must be cpu or cuda")
    if device.type == "cuda" and not torch.cuda.is_available():
        raise RuntimeError("The selected CUDA lane is unavailable in this interpreter")
    torch.set_num_threads(1)
    root = Path(str(output["root"])).expanduser()
    if not root.is_absolute():
        root = Path(__file__).resolve().parents[4] / root
    directory = root / "pointwise-gaussian-network-dynamics" / datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    directory.mkdir(parents=True)
    record: dict[str, object] = {
        "status": "running", "created_utc": datetime.now(timezone.utc).isoformat(),
        "command": [sys.executable, *sys.orig_argv[1:]],
        "runtime": {
            "interpreter": sys.executable, "python": sys.version, "torch": torch.__version__,
            "cuda_available": torch.cuda.is_available(), "device": str(device), "cpu_threads": torch.get_num_threads(),
            "platform": platform.platform(),
            "thread_environment": {name: os.environ.get(name) for name in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_THREADING_LAYER")},
        },
        "profile": {"RUN": dict(run), "THEORY": dict(theory), "NUMERICS": dict(numerics), "OUTPUT": dict(output)},
        "scope": "finite Gaussian reference at c_* under observed piecewise-frozen link control; no latent link prior, endogenous VFE learning, formation theorem, or thermodynamic limit",
        "cases": [],
    }
    _write_json(directory / "result.json", record)
    started = time.perf_counter()
    try:
        with torch.no_grad():
            for kind in theory["cases"]:
                print(f"Running dynamic {kind}: N={n_agents}, dimension={dimension}, steps={n_steps}, {device}", flush=True)
                case_start = time.perf_counter()
                case = build_network_case(str(kind), n_agents, dimension, int(run["seed"]), float(theory["link_scale"]))
                result, arrays = measure_network_dynamics(
                    case, float(theory["dt"]), float(theory["motion_strength"]),
                    float(numerics["atol"]), float(numerics["rtol"]), n_steps,
                    dimension, int(run["seed"]), str(kind), device,
                )
                result["elapsed_seconds"] = time.perf_counter() - case_start
                _write_json(directory / f"{kind}.json", result)
                if output["save_arrays"]:
                    np.savez_compressed(directory / f"{kind}.npz", **arrays)
                record["cases"].append(result)
                _write_json(directory / "result.json", record)
                if result["status"] != "pass":
                    raise ArithmeticError(f"Dynamic parity failed for {kind}; see {directory}")
                print(f"{kind}: pass, path KL={result['innovation_information_total']:.9g}, elapsed={result['elapsed_seconds']:.3f}s", flush=True)
        record["status"] = "pass"
    except Exception as error:
        record.update(status="failed", error=f"{type(error).__name__}: {error}", traceback=traceback.format_exc())
        raise
    finally:
        record["elapsed_seconds"] = time.perf_counter() - started
        _write_json(directory / "result.json", record)
    print(f"run_dir={directory}", flush=True)
    return GaussianNetworkDynamicsResult(directory, "pass")
