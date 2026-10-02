"""Matched large-network controls for the coupled Gaussian recognition model."""
from __future__ import annotations

from dataclasses import asdict
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import platform
import shutil
import subprocess
import sys
import time
import traceback

import numpy as np
import torch

from .coupled_learning import CoupledModel, CoupledState, expected_costs, free_energy, natural_step
from .network_experiment import build_network_case


def build_coupled_case(
    n_agents:   int,
    dimension:  int,
    seed:       int,
    link_scale: float = .2,
    device:     str   = "cpu",
) -> tuple[CoupledModel, CoupledState]:
    """Reuse the sparse GL+ reference's seeded priors and independent maps."""
    if n_agents <= 34:
        raise ValueError("this study builder requires distinct cycle/stride-17 physical edges")
    case = build_network_case("independent_real_gl", n_agents, dimension, seed, link_scale)
    a, J_0, edges, Theta = [x.to(device) for x in (case.mu_0, case.J_0, case.edges, case.B_e)]
    sources = edges[:, 1].reshape(2, n_agents).T.contiguous()
    index = torch.arange(2*n_agents, device=device).reshape(2, n_agents).T.contiguous()
    model = CoupledModel(a, J_0, J_0.clone(), sources, edges, index,
                         torch.zeros_like(sources, dtype=torch.bool), tau=.5)
    perturbation = .3*torch.sin(torch.arange(n_agents*dimension, dtype=a.dtype, device=device)).reshape_as(a)
    state = CoupledState(a+perturbation, 1.2*torch.linalg.inv(J_0),
                         torch.full(sources.shape, .5, dtype=a.dtype, device=device), Theta)
    return model, state


def _snapshot(
    state:    CoupledState,
    initial:  CoupledState,
    model:    CoupledModel,
    clock:    float,
    previous: torch.Tensor | None = None,
) -> tuple[dict, torch.Tensor]:
    """Record law-level diagnostics; source preference is not a formation event."""
    with torch.no_grad():
        F, beta, cost = free_energy(state, model)
        _, mean_cost = expected_costs(state.mu, state.Sigma, state.Theta, model)
        choice = beta.argmax(-1)
        displacement = state.Theta-initial.Theta
        H_i = model.H[model.endpoints[:, 0]]
        H_j = model.H[model.endpoints[:, 1]]
        squared = torch.einsum("eij,eji->e", displacement.mT@H_i@displacement, torch.linalg.inv(H_j))
        L = torch.linalg.cholesky(model.H)
        whitened = L[model.endpoints[:, 0]].mT @ state.Theta @ torch.linalg.inv(L[model.endpoints[:, 1]].mT)
        singular = torch.linalg.svdvals(whitened)
        return {
            "inference_time": clock, "vfe": float(F), "vfe_per_agent": float(F/len(state.mu)),
            "expected_cost_per_row": float((beta*cost).sum(-1).mean()),
            "mean_cost_per_row": float((beta*mean_cost).sum(-1).mean()),
            "source_entropy": float(-(state.pi*state.pi.log()).sum(-1).mean()),
            "recognition_entropy": float(-torch.special.xlogy(beta, beta).sum(-1).mean()),
            "source_tv_from_initial": float(.5*(state.pi-initial.pi).abs().sum(-1).mean()),
            "link_metric_rms_change": float(squared.mean().sqrt()),
            "metric_link_condition_max": float((singular[:, 0]/singular[:, -1]).max()),
            "metric_link_singular_min": float(singular[:, -1].min()),
            "preferred_source_retained_fraction": None if previous is None else float((choice==previous).double().mean()),
            "min_covariance_eigenvalue": float(torch.linalg.eigvalsh(state.Sigma).min()),
            "min_link_determinant": float(torch.linalg.det(state.Theta).min()),
            "min_source_probability": float(state.pi.min()),
        }, choice


def run_coupled_learning(
    run:      dict,
    theory:   dict,
    numerics: dict,
    output:   dict,
) -> dict:
    """Run declared controls at common inference times and preserve failure records."""
    if numerics["dtype"] != "float64":
        raise ValueError("this study declares float64")
    device = str(numerics["device"])
    torch.set_num_threads(int(numerics["cpu_threads"]))
    directory = Path(output["root"])/datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    directory.mkdir(parents=True)
    root = Path(__file__).resolve().parents[4]
    source_paths = [
        "src/multiagent_elbo/realizations/gaussian/coupled_learning.py",
        "src/multiagent_elbo/realizations/gaussian/coupled_learning_experiment.py",
        "src/multiagent_elbo/realizations/gaussian/network_experiment.py",
        "experiments/gaussian_coupled_learning.py",
    ]
    (directory/"source").mkdir()
    hashes = {}
    for relative in source_paths:
        path = root/relative
        hashes[relative] = hashlib.sha256(path.read_bytes()).hexdigest()
        shutil.copyfile(path, directory/"source"/path.name)
    metadata = {
        "run": run, "theory": theory, "numerics": numerics, "output": output,
        "base_head": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip(),
        "working_status": subprocess.check_output(["git", "status", "--short"], cwd=root, text=True),
        "source_sha256_diagnostic": hashes, "python": sys.executable,
        "python_version": platform.python_version(), "torch": torch.__version__,
        "cuda_available": torch.cuda.is_available(), "device": device,
        "status": "running", "cases": [],
    }
    (directory/"metadata.json").write_text(json.dumps(metadata, indent=2), encoding="utf-8")
    arms = {"learn_both": (theory["source_rate"], theory["link_rate"]),
            "frozen_source": (0., theory["link_rate"]),
            "frozen_link": (theory["source_rate"], 0.),
            "frozen_both": (0., 0.)}
    started = time.perf_counter()
    try:
        for N in theory["n_agents"]:
            model, initial = build_coupled_case(N, theory["dimension"], run["seed"], theory["link_scale"], device)
            # Override the builder's declared default explicitly from this profile.
            from dataclasses import replace
            model = replace(model, tau=float(theory["tau"]))
            for arm, (source_rate, link_rate) in arms.items():
                state, clock = initial, 0.
                first, choice = _snapshot(state, initial, model, clock)
                snapshots, step_count, backtracks = [first], 0, 0
                max_increase, smallest_step = -float("inf"), float("inf")
                for target in theory["checkpoints"]:
                    if target <= clock:
                        raise ValueError("checkpoints must strictly increase after zero")
                    while clock < target-1e-12:
                        state, info = natural_step(
                            state, model, min(theory["dt"], target-clock),
                            belief_rate=theory["belief_rate"], source_rate=source_rate, link_rate=link_rate)
                        clock += info["accepted_dt"]
                        step_count += 1
                        backtracks += info["backtracks"]
                        smallest_step = min(smallest_step, info["accepted_dt"])
                        max_increase = max(max_increase, info["after"]-info["before"])
                    snap, choice = _snapshot(state, initial, model, clock, choice)
                    snapshots.append(snap)
                checks = {
                    "finite_and_descending": max_increase <= 0 and all(np.isfinite(s["vfe"]) for s in snapshots),
                    "positive_domains": all(s["min_covariance_eigenvalue"] > 0 and s["min_link_determinant"] > 0 and s["min_source_probability"] > 0 for s in snapshots),
                    "normalized_sources": bool(torch.allclose(state.pi.sum(-1), torch.ones(N, dtype=state.pi.dtype, device=device))),
                    "source_freeze_preserved": source_rate != 0 or torch.equal(state.pi, initial.pi),
                    "link_freeze_preserved": link_rate != 0 or torch.equal(state.Theta, initial.Theta),
                }
                result = {"n_agents": N, "arm": arm, "source_rate": source_rate, "link_rate": link_rate,
                          "steps": step_count, "backtracks": backtracks, "smallest_dt": smallest_step,
                          "max_vfe_increase": max_increase, "snapshots": snapshots, "checks": checks}
                metadata["cases"].append(result)
                (directory/f"N{N}-{arm}.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
                arrays = {name: value.detach().cpu().numpy() for name, value in asdict(state).items()}
                np.savez_compressed(directory/f"N{N}-{arm}-final.npz", **arrays)
                if not all(checks.values()):
                    raise RuntimeError(f"numerical/domain/control gate failed: N={N}, {arm}")
                print(f"N={N} {arm}: F/N {first['vfe_per_agent']:.6f} -> {snapshots[-1]['vfe_per_agent']:.6f}; steps={step_count}", flush=True)
        metadata["status"] = "pass"
    except Exception:
        metadata["status"] = "failed"
        metadata["traceback"] = traceback.format_exc()
        raise
    finally:
        if device.startswith("cuda"):
            torch.cuda.synchronize()
        metadata["elapsed_seconds"] = time.perf_counter()-started
        (directory/"metadata.json").write_text(json.dumps(metadata, indent=2), encoding="utf-8")
        print(json.dumps({"run_dir": str(directory), "status": metadata["status"],
                          "elapsed_seconds": metadata["elapsed_seconds"]}), flush=True)
    return {"run_dir": str(directory), **metadata}
