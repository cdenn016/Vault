"""Posthoc fixed-activation-mean source control; reuses saved joint histories.

Invoke with C:/anaconda/python.exe -I -B fixed-mean-control.py RUN_DIRECTORY.
This analysis does not sample trajectories or rerun structural learning.
"""
from __future__ import annotations

import argparse
from dataclasses import replace
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import sys

os.environ["MKL_THREADING_LAYER"] = "SEQUENTIAL"
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"

import numpy as np
import torch

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT/"src"))

from multiagent_elbo.realizations.gaussian.coupled_learning import CoupledState
from multiagent_elbo.realizations.gaussian.coupled_learning_experiment import build_coupled_case
from multiagent_elbo.realizations.gaussian.switching_paths import (
    source_log_posterior, source_transition_log_prob,
)


def estimate(values: np.ndarray) -> dict[str, float]:
    """Report the sample mean and empirical SE across independent trajectories."""
    return {"mean": float(values.mean()),
            "standard_error": float(values.std(ddof=1)/len(values)**.5)}


def diagnostic(path: Path) -> dict[str, str]:
    """Record source/input references as diagnostic metadata."""
    return {"path": str(path.resolve()),
            "sha256_diagnostic": hashlib.sha256(path.read_bytes()).hexdigest()}


def analyze(directory: Path) -> dict:
    r"""Score sum_t log K_P(J_(t+1)|X_t,J_t)-log K_fixed(J_(t+1)|J_t).

    K_fixed uses beta^P_t(initial.mu). The activation mean stays fixed while
    the saved source priors and links follow their original eight intervals.
    Its normalized global refresh mixture includes refresh to the old labels.
    """
    torch.set_num_threads(1)
    directory = directory.resolve()
    metadata_path = directory/"metadata.json"
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    if metadata["status"] != "pass":
        raise ValueError("analyze only the completed passing joint-history run")
    run, theory = metadata["run"], metadata["theory"]
    result = {
        "status": "running",
        "classification": "posthoc control prompted by the first N512 source-score comparison",
        "scope": "fixed-activation-mean source kernel on existing actual assignment histories",
        "construction": "beta^P_t(initial.mu), with saved pi_t and Theta_t and fixed initial.mu",
        "estimator": "per-path native source log density minus candidate source log density",
        "uncertainty": "empirical standard errors across independent paths; no confidence certificate",
        "resampling": False, "relearning": False,
        "python": sys.executable, "torch": torch.__version__, "numpy": np.__version__,
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "run_metadata": diagnostic(metadata_path),
        "sources": [diagnostic(Path(__file__)),
                    diagnostic(ROOT/"src/multiagent_elbo/realizations/gaussian/switching_paths.py"),
                    diagnostic(ROOT/"src/multiagent_elbo/realizations/gaussian/coupled_learning.py"),
                    diagnostic(ROOT/"src/multiagent_elbo/realizations/gaussian/coupled_learning_experiment.py")],
        "cases": [],
    }
    saved = {}
    dt = theory["interval_dt"]/run["substeps"]
    with torch.no_grad():
        for N in theory["n_agents"]:
            activation_path = ROOT/run["activation_root"]/f"N{N}-learn_both-final.npz"
            schedule_path = ROOT/run["schedule_root"]/f"N{N}-learn_both-schedule.npz"
            history_path = directory/f"N{N}-joint-paths-and-scores.npz"
            with np.load(activation_path) as values:
                initial = CoupledState(**{
                    key: torch.from_numpy(values[key].copy()) for key in ("mu", "Sigma", "pi", "Theta")})
            with np.load(schedule_path) as values:
                schedule = tuple(CoupledState(**{
                    key: torch.from_numpy(values[key][t].copy()) for key in ("mu", "Sigma", "pi", "Theta")})
                    for t in range(theory["intervals"]))
            model, _ = build_coupled_case(N, theory["dimension"], run["model_seed"], theory["link_scale"])
            model = replace(model, tau=theory["tau"])
            fixed_logits = tuple(source_log_posterior(initial.mu[None], state, model)
                                 for state in schedule)
            with np.load(history_path) as history:
                assignments = history["assignments"]
                native_log = history["log_source_kernel"]
                n_paths, n_times, _ = assignments.shape
                if n_times-1 != theory["intervals"]*run["substeps"]:
                    raise ValueError("saved assignment history does not match the fine schedule")
                candidate_log = torch.zeros(n_paths, dtype=initial.mu.dtype)
                for t in range(n_times-1):
                    old = torch.from_numpy(assignments[:, t].astype(np.int64))
                    new = torch.from_numpy(assignments[:, t+1].astype(np.int64))
                    log_beta = fixed_logits[t//run["substeps"]].expand(n_paths, -1, -1)
                    candidate_log += source_transition_log_prob(
                        log_beta, old, new, dt, theory["refresh_rate"])
                fixed_score = native_log.sum(1)-candidate_log.numpy()
                if not np.isfinite(fixed_score).all():
                    raise FloatingPointError("nonfinite fixed-mean source score")
                saved[f"N{N}_source_fixed_mean"] = fixed_score
                saved[f"N{N}_fixed_mean_log_source_path"] = candidate_log.numpy()
                case = {
                    "n_agents": N, "n_paths": n_paths, "microsteps": n_times-1, "micro_dt": dt,
                    "source_fixed_mean": estimate(fixed_score),
                    "inputs": [diagnostic(activation_path), diagnostic(schedule_path), diagnostic(history_path)],
                    "levels": [],
                }
                for block in theory["blocks"]:
                    lifted = history[f"block{block}_source_lifted"]
                    reference = history[f"block{block}_source_reference"]
                    lifted_minus_fixed = lifted-fixed_score
                    fixed_minus_reference = fixed_score-reference
                    saved[f"N{N}_block{block}_lifted_minus_fixed_mean"] = lifted_minus_fixed
                    saved[f"N{N}_block{block}_fixed_mean_minus_reference"] = fixed_minus_reference
                    case["levels"].append({
                        "block": block,
                        "paired_lifted_minus_fixed_mean": estimate(lifted_minus_fixed),
                        "paired_fixed_mean_minus_reference": estimate(fixed_minus_reference),
                    })
            result["cases"].append(case)
    result["status"] = "pass"
    output = Path(__file__).resolve().parent
    np.savez_compressed(output/"fixed-mean-control.npz", **saved)
    (output/"fixed-mean-control.json").write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
    return result


def main() -> int:
    """Read one completed run and write the declared posthoc control beside this script."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("run_directory", type=Path)
    args = parser.parse_args()
    result = analyze(args.run_directory)
    print(json.dumps({"status": result["status"], "cases": [
        {key: value for key, value in case.items() if key != "inputs"}
        for case in result["cases"]]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
