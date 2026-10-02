"""Decompose existing particle scores; draw no native or filter trajectories."""
from __future__ import annotations

from dataclasses import replace
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import platform
import subprocess
import sys
import time

import numpy as np
import torch

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "src"))
from multiagent_elbo.realizations.gaussian.block_observation import BlockObservation
from multiagent_elbo.realizations.gaussian.coupled_learning import CoupledState
from multiagent_elbo.realizations.gaussian.coupled_learning_experiment import build_coupled_case
from multiagent_elbo.realizations.gaussian.switching_paths import (
    source_log_posterior, source_transition_log_prob,
)

HERE = Path(__file__).resolve().parent
FILTER = ROOT / "artifacts/gaussian-joint-filter/20261002T165113504304Z"
NATIVE = ROOT / "artifacts/gaussian-joint-parent/20261002T161127396348Z"


def estimate(values: np.ndarray) -> dict:
    """Report independent-path empirical uncertainty, not step uncertainty."""
    n = len(values)
    return {"n_paths": n, "mean": float(values.mean()) if n else None,
            "standard_error": float(values.std(ddof=1) / np.sqrt(n)) if n > 1 else None}


def summarize(source: np.ndarray, config: np.ndarray, changed: np.ndarray) -> dict:
    """Decompose each path's loss before computing paired means and errors."""
    components = {"source": source, "conditional_configuration": config,
                  "joint": source + config}
    masks = {"all_steps": np.ones_like(changed), "changed_steps": changed,
             "unchanged_steps": ~changed}
    strata = {name: {key: estimate((values * mask).sum(-1))
                    for key, values in components.items()}
              for name, mask in masks.items()}
    for name, selected in (("no_change_paths", ~changed.any(-1)),
                            ("at_least_one_change_paths", changed.any(-1))):
        strata[name] = {key: estimate(values.sum(-1)[selected])
                        for key, values in components.items()}
    return strata


def main() -> None:
    """Run one deterministic baseline-source evaluation and score decomposition."""
    started = time.perf_counter()
    torch.set_num_threads(1)
    saved = json.loads((FILTER / "metadata.json").read_text(encoding="utf-8"))
    native = json.loads((NATIVE / "metadata.json").read_text(encoding="utf-8"))
    if saved["status"] != "pass" or native["status"] != "pass":
        raise ValueError("The referenced inputs are not completed studies.")
    if saved["run"]["n_paths"] != 128 or saved["theory"]["block"] != 16:
        raise ValueError("This diagnostic is defined for the published first-128/block-16 data.")
    metadata = {
        "started_utc": datetime.now(timezone.utc).isoformat(),
        "python": sys.executable, "python_version": platform.python_version(),
        "torch": torch.__version__, "numpy": np.__version__,
        "cuda_available": torch.cuda.is_available(), "device": "cpu", "dtype": "float64",
        "cpu_threads": 1,
        "environment": {key: os.environ.get(key) for key in (
            "MKL_THREADING_LAYER", "OMP_NUM_THREADS", "MKL_NUM_THREADS")},
        "head": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
        "working_status": subprocess.check_output(["git", "status", "--short"], cwd=ROOT, text=True),
        "filter_run": str(FILTER.relative_to(ROOT)), "native_run": str(NATIVE.relative_to(ROOT)),
        "filter_run_base_head": saved["base_head"], "run": saved["run"],
        "theory": saved["theory"], "native_run_config": native["run"],
        "native_theory": native["theory"],
        "input_sha256_diagnostic": {}, "source_sha256_diagnostic": {},
        "new_native_paths": 0, "new_filter_paths": 0, "relearning": False,
        "comparison_tolerance": 1e-9,
    }
    def record_input(path: Path) -> None:
        metadata["input_sha256_diagnostic"][str(path.relative_to(ROOT))] = hashlib.sha256(path.read_bytes()).hexdigest()

    for path in (FILTER / "metadata.json", NATIVE / "metadata.json"):
        record_input(path)
    modules = ["block_observation", "coupled_learning", "coupled_learning_experiment",
               "switching_paths", "network", "network_experiment", "network_dynamics",
               "predictive_interfaces", "locality"]
    for module in modules:
        path = ROOT / "src/multiagent_elbo/realizations/gaussian" / (module + ".py")
        metadata["source_sha256_diagnostic"][str(path.relative_to(ROOT))] = hashlib.sha256(path.read_bytes()).hexdigest()
    metadata["source_sha256_diagnostic"][str(Path(__file__).relative_to(ROOT))] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()

    results = {}
    for N in (512, 1024):
        activation_file = ROOT / native["run"]["activation_root"] / f"N{N}-learn_both-final.npz"
        schedule_file = ROOT / native["run"]["schedule_root"] / f"N{N}-learn_both-schedule.npz"
        history_file = NATIVE / f"N{N}-joint-paths-and-scores.npz"
        score_file = FILTER / f"N{N}-filter-scores.npz"
        for path in (activation_file, schedule_file, history_file, score_file):
            record_input(path)
        with np.load(activation_file) as z:
            initial = CoupledState(**{key: torch.from_numpy(z[key].copy())
                                     for key in ("mu", "Sigma", "pi", "Theta")})
        with np.load(schedule_file) as z:
            coarse = tuple(CoupledState(**{key: torch.from_numpy(z[key][t].copy())
                                          for key in ("mu", "Sigma", "pi", "Theta")})
                           for t in range(native["theory"]["intervals"]))
        subdivision = native["run"]["substeps"]
        schedule = tuple(state for state in coarse for _ in range(subdivision))
        dt = native["theory"]["interval_dt"] / subdivision
        with np.load(history_file) as z:
            R = torch.from_numpy(z["block16_paths"][:128].copy())
            J = torch.from_numpy(z["assignments"][:128].astype(np.int64))
            native_source = z["log_source_kernel"][:128].copy()
            prior_lifted_contrast = z["block16_source_lifted"][:128].copy()
        with np.load(score_file) as z:
            scores = {key: z[key].copy() for key in z.files}
        model, _ = build_coupled_case(N, native["theory"]["dimension"],
            native["run"]["model_seed"], native["theory"]["link_scale"])
        model = replace(model, tau=native["theory"]["tau"])
        B, H, K = 128, len(schedule), initial.mu.shape[-1]
        observed = R.reshape(B, H + 1, N // 16, K)
        activation = BlockObservation.compile(initial.Sigma, 16)
        baseline_source = np.empty((B, H), dtype=np.float64)
        with torch.no_grad():
            for t, state in enumerate(schedule):
                X = activation.conditional_mean(initial.mu.expand(B, N, K), observed[:, t])
                baseline_source[:, t] = source_transition_log_prob(
                    source_log_posterior(X, state, model), J[:, t], J[:, t + 1],
                    dt, native["theory"]["refresh_rate"]).numpy()
        baseline_residual = float(np.max(np.abs(
            (native_source - baseline_source).sum(-1) - prior_lifted_contrast)))
        if baseline_residual > 1e-9:
            raise ArithmeticError(f"N={N}: old and new baseline source totals differ by {baseline_residual}")
        changed = (J[:, 1:] != J[:, :-1]).any(-1).numpy()
        case = {
            "n_agents": N, "n_paths": B, "microsteps": H, "dt": dt,
            "changed_step_count": int(changed.sum()),
            "unchanged_step_count": int((~changed).sum()),
            "no_change_path_count": int((~changed.any(-1)).sum()),
            "at_least_one_change_path_count": int(changed.any(-1).sum()),
            "change_count_histogram": {str(v): int((changed.sum(-1) == v).sum())
                                      for v in np.unique(changed.sum(-1))},
            "baseline_source_total_vs_predecessor_max_abs_residual": baseline_residual,
            "arms": {}, "pairwise": {},
        }
        arrays = {"baseline_log_source": baseline_source, "changed": changed}
        base_config = scores["baseline_log_joint"] - baseline_source
        for arm in ("filter16", "filter64", "reset64"):
            source = baseline_source - scores[arm + "_log_source"]
            config = base_config - (scores[arm + "_log_joint"] - scores[arm + "_log_source"])
            residual = float(np.max(np.abs((source + config).sum(-1) - scores[arm + "_minus_baseline"])))
            if residual > 1e-9:
                raise ArithmeticError("Source plus conditional configuration does not reproduce published joint loss.")
            case["arms"][arm] = summarize(source, config, changed)
            case["arms"][arm]["published_joint_max_abs_residual"] = residual
            arrays[arm + "_source_loss_minus_baseline"] = source
            arrays[arm + "_configuration_loss_minus_baseline"] = config
        for high, low in (("filter64", "reset64"), ("filter16", "reset64"), ("filter64", "filter16")):
            source = scores[low + "_log_source"] - scores[high + "_log_source"]
            config = ((scores[low + "_log_joint"] - scores[low + "_log_source"])
                      - (scores[high + "_log_joint"] - scores[high + "_log_source"]))
            case["pairwise"][high + "_minus_" + low] = summarize(source, config, changed)
        np.savez_compressed(HERE / f"N{N}-decomposed-scores.npz", **arrays)
        (HERE / f"N{N}.json").write_text(json.dumps(case, indent=2), encoding="utf-8")
        results[str(N)] = case
        print(json.dumps({"N": N, "counts": {key: case[key] for key in
              ("changed_step_count", "no_change_path_count", "at_least_one_change_path_count")},
              "arms": {key: value["all_steps"] for key, value in case["arms"].items()},
              "filter64_minus_reset64": case["pairwise"]["filter64_minus_reset64"]["all_steps"],
              "checks": {"baseline_residual": baseline_residual}}), flush=True)
    metadata["elapsed_seconds"] = time.perf_counter() - started
    metadata["status"] = "completed"
    (HERE / "metadata.json").write_text(json.dumps(metadata, indent=2), encoding="utf-8")
    print(json.dumps({"status": metadata["status"], "elapsed_seconds": metadata["elapsed_seconds"]}), flush=True)


if __name__ == "__main__":
    main()
