"""Actual switching-history parent comparison on a learned activation."""
from __future__ import annotations

from dataclasses import replace
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

from .coupled_learning import CoupledState, free_energy, natural_step
from .coupled_learning_experiment import build_coupled_case
from .locality import block_mean_projector
from .predictive_interfaces import (
    predictive_reference, spectral_interface, compile_predictor,
    _predictor_path, _gaussian_kl,
)
from .switching_paths import (
    sample_switching_paths, reference_transition, gaussian_log_ratio,
    projected_row_bound,
)


def _estimate(values: torch.Tensor) -> dict[str, float]:
    """Return empirical mean and standard error over independent trajectories."""
    return {"mean": float(values.mean()), "standard_error": float(values.std(unbiased=True)/len(values)**.5)}


def run_switching_study(
    run:      dict,
    theory:   dict,
    numerics: dict,
    output:   dict,
) -> dict:
    """Execute the declared finite-step law once, retaining any failed case."""
    if numerics["dtype"] != "float64" or numerics["device"] != "cpu":
        raise ValueError("this profile declares a CPU float64 study")
    torch.set_num_threads(numerics["cpu_threads"])
    root = Path(__file__).resolve().parents[4]
    directory = Path(output["root"])/datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    directory.mkdir(parents=True)
    source_paths = [
        "src/multiagent_elbo/realizations/gaussian/"+name+".py"
        for name in ("switching_paths", "switching_experiment", "coupled_learning",
                     "coupled_learning_experiment", "network", "network_experiment",
                     "network_dynamics", "locality", "predictive_interfaces")
    ]+["experiments/gaussian_switching_paths.py"]
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
        "source_sha256_diagnostic": hashes, "activation_sha256_diagnostic": {},
        "python": sys.executable, "python_version": platform.python_version(),
        "torch": torch.__version__, "cuda_available": torch.cuda.is_available(),
        "status": "running", "cases": [],
    }
    def save() -> None:
        """Preserve progress and diagnostics without reclassifying failures."""
        (directory/"metadata.json").write_text(json.dumps(metadata, indent=2), encoding="utf-8")
    save()
    arms = {"learn_both": (theory["source_rate"], theory["link_rate"]),
            "frozen_source": (0., theory["link_rate"]),
            "frozen_link": (theory["source_rate"], 0.), "frozen_both": (0., 0.)}
    started = time.perf_counter()
    try:
        for N in theory["n_agents"]:
            activation = root/run["activation_root"]/f"N{N}-learn_both-final.npz"
            metadata["activation_sha256_diagnostic"][str(activation.relative_to(root))] = hashlib.sha256(activation.read_bytes()).hexdigest()
            with np.load(activation) as arrays:
                initial = CoupledState(**{name: torch.from_numpy(arrays[name].copy())
                                          for name in ("mu", "Sigma", "pi", "Theta")})
            model, _ = build_coupled_case(N, theory["dimension"], run["model_seed"], theory["link_scale"])
            model = replace(model, tau=theory["tau"])
            mobility = initial.Sigma.clone()
            projections = {block: block_mean_projector(N, theory["dimension"], block)
                           for block in theory["blocks"]}
            P_0 = projections[theory["blocks"][0]]
            composition = {}
            for block, P in projections.items():
                stage = block_mean_projector(N//theory["blocks"][0], theory["dimension"],
                                             block//theory["blocks"][0])
                composition[str(block)] = float((P-stage@P_0).abs().max())
                torch.testing.assert_close(P, stage@P_0, atol=1e-13, rtol=1e-13)
            for arm, (source_rate, link_rate) in arms.items():
                case_started = time.perf_counter()
                state, clock = initial, 0.
                schedule, steps, backtracks, increases = [], 0, 0, []
                for t in range(theory["horizon_steps"]):
                    schedule.append(state)
                    target = (t+1)*theory["dt"]
                    while clock < target-1e-12:
                        state, info = natural_step(
                            state, model, min(theory["optimizer_dt"], target-clock),
                            belief_rate=theory["belief_rate"], source_rate=source_rate, link_rate=link_rate)
                        clock += info["accepted_dt"]
                        steps += 1
                        backtracks += info["backtracks"]
                        increases.append(info["after"]-info["before"])
                freeze_source = source_rate != 0 or torch.equal(state.pi, initial.pi)
                freeze_link = link_rate != 0 or torch.equal(state.Theta, initial.Theta)
                if not freeze_source or not freeze_link:
                    raise ArithmeticError("a frozen parameter moved")
                with torch.no_grad():
                    paths, fine_costs, means = sample_switching_paths(
                        mobility, initial, schedule, model, theory["dt"], run["n_paths"],
                        run["path_seed"], theory["refresh_rate"])
                    transitions = tuple(reference_transition(mobility, s, model, theory["dt"]) for s in schedule)
                    case = {
                        "n_agents": N, "arm": arm, "source_rate": source_rate, "link_rate": link_rate,
                        "steps": steps, "backtracks": backtracks,
                        "max_vfe_increase": max(increases), "freeze_source_preserved": freeze_source,
                        "freeze_link_preserved": freeze_link, "composition_max_error": composition,
                        "fine_augmented_path_kl": _estimate(fine_costs),
                        "fine_augmented_path_kl_per_agent": _estimate(fine_costs/N),
                        "initial_vfe": float(free_energy(initial, model)[0]),
                        "final_vfe": float(free_energy(state, model)[0]), "levels": [],
                    }
                    saved_arrays = {"fine_costs": fine_costs.numpy()}
                    for block, P in projections.items():
                        reference = predictive_reference(initial.mu.flatten(), torch.block_diag(*initial.Sigma), P, transitions)
                        m = len(P)
                        spectral = spectral_interface(reference.Sigma_h, reference.C, reference.noise)
                        rows = {"rank_zero": P.new_empty((0, N*theory["dimension"]-m)),
                                "spectral": spectral.W[:m],
                                "coordinate": torch.eye(N*theory["dimension"]-m, dtype=P.dtype)[:m]}
                        R = paths.flatten(2)@P.T
                        scores, level = {}, {"block": block, "output_dimension": m, "parents": {}}
                        saved_arrays[f"block{block}_paths"] = R.numpy()
                        for name, W in rows.items():
                            parent = compile_predictor(W, reference)
                            candidate_mu, candidate_Sigma = _predictor_path(parent)
                            correction = gaussian_log_ratio(R.flatten(1), reference.path_mu, reference.path_Sigma,
                                                            candidate_mu, candidate_Sigma)
                            U = projected_row_bound(paths, means, P, mobility, theory["dt"], parent)
                            if not bool(torch.isfinite(U).all()) or not bool(torch.isfinite(correction).all()):
                                raise FloatingPointError("nonfinite parent score")
                            # Negative roundoff is reported rather than clamped.
                            if float(U.min()) < -1e-8:
                                raise ArithmeticError("materially negative conditional Gaussian KL")
                            scores[name] = U
                            level["parents"][name] = {
                                "hidden_rank": len(W), "online_hidden_mean_entries": len(W),
                                "online_hidden_covariance_entries": len(W)**2,
                                "deployed_kernel_entries": sum(k.F.numel()+k.Q.numel()+k.u.numel() for k in parent.kernels),
                                "offline_reference_covariance_entries": sum(x.numel() for x in reference.covariances),
                                "direct_row_upper_functional": _estimate(U),
                                "direct_row_upper_per_output_step": _estimate(U/(m*len(schedule))),
                                "reference_transfer_upper_functional": _estimate(fine_costs+correction),
                                "signed_density_correction": _estimate(correction),
                                "gaussian_reference_path_kl": float(_gaussian_kl(
                                    reference.path_mu, reference.path_Sigma, candidate_mu, candidate_Sigma)),
                            }
                            saved_arrays[f"block{block}_{name}_row_score"] = U.numpy()
                            saved_arrays[f"block{block}_{name}_density_correction"] = correction.numpy()
                        level["paired_spectral_minus_rank_zero"] = _estimate(scores["spectral"]-scores["rank_zero"])
                        level["paired_spectral_minus_coordinate"] = _estimate(scores["spectral"]-scores["coordinate"])
                        case["levels"].append(level)
                        print(f"N={N} {arm} block={block}: U0={scores['rank_zero'].mean():.6f}, "
                              f"Us={scores['spectral'].mean():.6f}; elapsed={time.perf_counter()-case_started:.1f}s", flush=True)
                        del reference, spectral, parent
                    np.savez_compressed(directory/f"N{N}-{arm}-scores.npz", **saved_arrays)
                    np.savez_compressed(directory/f"N{N}-{arm}-schedule.npz",
                                        **{name: torch.stack([getattr(s, name) for s in (*schedule, state)]).numpy()
                                           for name in ("mu", "Sigma", "pi", "Theta")})
                    case["elapsed_seconds"] = time.perf_counter()-case_started
                    metadata["cases"].append(case)
                    (directory/f"N{N}-{arm}.json").write_text(json.dumps(case, indent=2), encoding="utf-8")
                    del paths, means, transitions, saved_arrays, scores
                    save()
        metadata["status"] = "pass"
    except Exception:
        metadata["status"] = "failed"
        metadata["traceback"] = traceback.format_exc()
        raise
    finally:
        metadata["elapsed_seconds"] = time.perf_counter()-started
        save()
        print(json.dumps({"run_dir": str(directory), "status": metadata["status"],
                          "elapsed_seconds": metadata["elapsed_seconds"]}), flush=True)
    return {"run_dir": str(directory), **metadata}
