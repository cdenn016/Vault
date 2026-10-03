"""Measure the frozen-parent actual-law budget on paired discretizations."""
from __future__ import annotations

from concurrent.futures import ProcessPoolExecutor, as_completed
from dataclasses import replace
from datetime import datetime, timezone
import hashlib
import json
import multiprocessing
from pathlib import Path
import platform
import shutil
import subprocess
import sys
import time
import traceback
import zipfile

import numpy as np
import torch

from .continuous_budget import sample_frozen_budget
from .coupled_learning import CoupledState
from .coupled_learning_experiment import build_coupled_case
from .switching_paths import all_sheet_curvature_bound

_context: dict = {}
_INTEGRALS = ("drift_integral", "mark_integral", "self_integral",
              "visible_integral", "total_integral", "augmented_integral")
_DIAGNOSTICS = ("proposal_count", "visible_changes", "projection_max_error",
                "covariance_projection_max_error")


def _initialize_worker(context: dict) -> None:
    """Install the frozen case once per single-thread CPU worker."""
    global _context
    torch.set_num_threads(1)
    _context = context


def _sample_task(task: tuple[int, int]) -> dict:
    """Return one fresh path and its shared tape without an automatic retry."""
    path_index, seed = task
    c = _context
    with torch.no_grad():
        values = sample_frozen_budget(
            c["initial"].Sigma, c["initial"], c["model"], c["horizon"],
            c["block_size"], c["coarse_steps"], c["n_probes"], seed,
            source_backend=c.get("source_backend", "dense"))
    return {"path_index": path_index, "seed": seed,
            "values": {key: value.detach().cpu().numpy() for key, value in values.items()}}


def _estimate(values: np.ndarray) -> dict[str, float]:
    """Report an empirical path mean and its standard error, not a confidence bound."""
    scale = float(np.abs(values).max())
    standard_error = 0. if scale == 0. else scale*float((values/scale).std(ddof=1))/len(values)**.5
    return {"mean": float(values.mean()), "standard_error": standard_error}


def run_frozen_budget_study(
    run:      dict,
    theory:   dict,
    numerics: dict,
    output:   dict,
) -> dict:
    """Retain fresh frozen paths and descriptive paired-grid budget estimates.

    Finite negative Monte Carlo visible-rate estimates are retained. A finite
    simulated average does not establish an upper confidence bound or a
    continuous-time discretization limit.
    """
    if {key: value for key, value in numerics.items() if key != "source_backend"} != {
            "device": "cpu", "dtype": "float64", "cpu_threads": 1}:
        raise ValueError("the declared budget profile requires single-thread CPU float64 and supported numerics keys")
    source_backend = numerics.get("source_backend", "dense")
    if source_backend not in ("dense", "square_root"):
        raise ValueError("source_backend must be dense or square_root")
    if not 1 <= run["workers"] <= 4 or run["n_paths"] < 2:
        raise ValueError("use one to four workers and at least two independent paths")
    if theory["horizon"] <= 0 or theory["coarse_steps"] < 1 or theory["n_probes"] < 1:
        raise ValueError("horizon, integration steps, and probe count must be positive")
    torch.set_num_threads(1)
    root = Path(__file__).resolve().parents[4]
    directory = Path(output["root"])/datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    directory.mkdir(parents=True)
    started = time.perf_counter()
    metadata = {
        "run": run, "theory": theory, "numerics": numerics, "output": output,
        "status": "running", "cases": [], "retries": 0,
        "automatic_resume": False, "source_sha256_diagnostic": {},
        "input_sha256_diagnostic": {}, "python": sys.executable,
        "python_version": platform.python_version(), "torch": torch.__version__,
        "base_head": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=root, text=True).strip(),
        "working_status": subprocess.check_output(
            ["git", "status", "--short"], cwd=root, text=True),
        "estimate_scope": "Empirical path mean and SE, one frozen model per size; not a confidence upper bound.",
        "grid_scope": "Paired grids share initial draw, proposal times, uniforms, and Brownian tape; refinement alone is not a discretization-limit proof.",
        "probe_scope": "Independent uniform times select left endpoints of the fixed simulation mesh; probes do not change its grid.",
    }

    def save() -> None:
        """Keep completion and failure records after every received task."""
        metadata["elapsed_seconds"] = time.perf_counter()-started
        (directory/"metadata.json").write_text(json.dumps(metadata, indent=2), encoding="utf-8")

    save()
    print(json.dumps({"run_dir": str(directory), "status": "running"}), flush=True)
    try:
        modules = ("continuous_budget_experiment", "continuous_budget", "source_gaussian", "source_square_root",
                   "gaussian_message", "source_adapted_filter", "coupled_learning",
                   "coupled_learning_experiment", "switching_paths", "network",
                   "network_experiment", "network_dynamics", "predictive_interfaces", "locality")
        sources = ["src/multiagent_elbo/realizations/gaussian/"+name+".py" for name in modules]
        sources += ["experiments/gaussian_continuous_budget.py", "experiments/gaussian_continuous_square_root.py"]
        document_root = root/"docs/research/2026-10-02-renormalization-completion"
        sources += [p.relative_to(root).as_posix() for p in document_root.glob("continuous*.md")]
        sources += [p.relative_to(root).as_posix() for p in
                    (root/"tests").glob("test_gaussian_continuous_*.py")]
        with zipfile.ZipFile(directory/"source.zip", "w", zipfile.ZIP_DEFLATED) as archive:
            for relative in dict.fromkeys(sources):
                data = (root/relative).read_bytes()
                archive.writestr(relative, data)
                metadata["source_sha256_diagnostic"][relative] = hashlib.sha256(data).hexdigest()
        inputs = directory/"inputs"
        inputs.mkdir()
        for N in theory["n_agents"]:
            path = root/run["activation_root"]/f"N{N}-learn_both-final.npz"
            shutil.copyfile(path, inputs/path.name)
            metadata["input_sha256_diagnostic"][str(path)] = hashlib.sha256(path.read_bytes()).hexdigest()
        save()
        for size_index, N in enumerate(theory["n_agents"]):
            case_started = time.perf_counter()
            with np.load(inputs/f"N{N}-learn_both-final.npz") as z:
                initial = CoupledState(**{key: torch.from_numpy(z[key].copy())
                                         for key in ("mu", "Sigma", "pi", "Theta")})
            if initial.mu.shape != (N, theory["dimension"]) or any(
                    value.dtype != torch.float64 or not bool(torch.isfinite(value).all())
                    for value in (initial.mu, initial.Sigma, initial.pi, initial.Theta)):
                raise ValueError("activation must have the declared dimensions and finite float64 coefficients")
            model, _ = build_coupled_case(N, theory["dimension"], run["model_seed"], theory["link_scale"])
            model = replace(model, tau=theory["tau"])
            bound = all_sheet_curvature_bound(initial.Sigma, initial.Theta, model)
            dt = theory["horizon"]/theory["coarse_steps"]
            case = {"n_agents": N, "n_paths": run["n_paths"], "completed_paths": 0,
                    "coarse_dt": dt, "fine_dt": dt/2, "all_sheet_curvature_bound": bound,
                    "coarse_dt_times_bound": dt*bound, "status": "running", "paths": []}
            metadata["active_case"] = case
            save()
            if not np.isfinite(bound) or dt*bound > 1.:
                raise ValueError(f"coarse step violates declared curvature condition: dt*bound={dt*bound}")
            context = {"initial": initial, "model": model, "source_backend": source_backend, **{key: theory[key] for key in
                       ("horizon", "block_size", "coarse_steps", "n_probes")}}
            pool = ProcessPoolExecutor(max_workers=run["workers"],
                mp_context=multiprocessing.get_context("spawn"),
                initializer=_initialize_worker, initargs=(context,))
            futures = {}
            try:
                futures = {pool.submit(_sample_task, (index, run["path_seed"]+
                           100000*size_index+10*index)): index for index in range(run["n_paths"])}
                for future in as_completed(futures):
                    path_index = futures[future]
                    metadata["active_path"] = {"n_agents": N, "path_index": path_index,
                        "seed": run["path_seed"]+100000*size_index+10*path_index}
                    save()
                    result = future.result()
                    values = result["values"]
                    path_index = result["path_index"]
                    np.savez_compressed(directory/f"N{N}-path{path_index:03d}.npz", **values)
                    if any(not np.isfinite(value).all() for value in values.values()):
                        raise FloatingPointError(f"nonfinite output for N={N}, path={path_index}")
                    required = [grid+"_"+key for grid in ("coarse", "fine")
                                for key in _INTEGRALS+_DIAGNOSTICS]
                    if any(key not in values or values[key].size != 1 for key in required):
                        raise ValueError("budget output lacks a declared scalar metric")
                    record = {"path_index": path_index, "seed": result["seed"],
                              **{key: float(values[key]) for key in required}}
                    case["paths"].append(record)
                    case["paths"].sort(key=lambda item: item["path_index"])
                    case["completed_paths"] += 1
                    metadata.pop("active_path")
                    case["elapsed_seconds"] = time.perf_counter()-case_started
                    (directory/f"N{N}-progress.json").write_text(json.dumps(case, indent=2), encoding="utf-8")
                    save()
                    print(f"N={N} path={path_index+1}/{run['n_paths']}; "
                          f"completed={case['completed_paths']}; elapsed={case['elapsed_seconds']:.1f}s", flush=True)
            finally:
                for future in futures:
                    future.cancel()
                pool.shutdown(wait=True, cancel_futures=True)
            case["estimates"] = {grid: {} for grid in ("coarse", "fine", "fine_minus_coarse")}
            for metric in _INTEGRALS:
                coarse = np.array([path["coarse_"+metric] for path in case["paths"]])
                fine = np.array([path["fine_"+metric] for path in case["paths"]])
                for grid, values in (("coarse", coarse), ("fine", fine), ("fine_minus_coarse", fine-coarse)):
                    case["estimates"][grid][metric] = _estimate(values)
            case["status"] = "pass"
            case["elapsed_seconds"] = time.perf_counter()-case_started
            (directory/f"N{N}.json").write_text(json.dumps(case, indent=2), encoding="utf-8")
            metadata["cases"].append(case)
            metadata.pop("active_case")
            save()
        metadata["status"] = "pass"
    except Exception:
        metadata["status"] = "failed"
        metadata["traceback"] = traceback.format_exc()
        raise
    finally:
        save()
        print(json.dumps({"run_dir": str(directory), "status": metadata["status"],
                          "elapsed_seconds": metadata["elapsed_seconds"]}), flush=True)
    return metadata
