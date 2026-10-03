"""Posthoc upper-functional estimates from saved native/candidate scores.

Run only after the source-adapted study passes. No simulation or model import.
"""
from __future__ import annotations

import json
import math
import os
import platform
import sys
from datetime import datetime, timezone
from pathlib import Path

os.environ["OMP_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["MKL_THREADING_LAYER"] = "SEQUENTIAL"

import numpy as np

ARMS = ("gaussian", "reset_gaussian", "baseline", "filter64", "reset64")


def path_sums(rows: np.ndarray) -> np.ndarray:
    """Accumulate complete paths with compensated summation."""
    return np.asarray([math.fsum(map(float, row)) for row in rows], dtype=np.float64)


def estimate(values: np.ndarray) -> dict[str, float | int]:
    """Return descriptive path mean and sample standard error, not a CI."""
    count = len(values)
    mean = math.fsum(map(float, values))/count
    variance = math.fsum((float(value)-mean)**2 for value in values)/(count-1)
    return {"n_paths": count, "mean": mean, "standard_error": math.sqrt(variance/count)}


def write_json(path: Path, value: dict) -> None:
    """Create one new postprocessing artifact, preserving existing files."""
    with path.open("x", encoding="utf-8") as handle:
        json.dump(value, handle, indent=2, allow_nan=False)


def main() -> None:
    """Read matched scores, compute entropy once, and save posthoc estimates."""
    root = Path(__file__).resolve().parents[2]
    run = root/(sys.argv[1] if len(sys.argv)>1 else
                "artifacts/gaussian-source-adapted/20261002T175407133253Z")
    metadata = json.loads((run/"metadata.json").read_text(encoding="utf-8"))
    if metadata["status"] != "pass":
        raise RuntimeError("postprocessing requires completed study status pass")
    native_dir = root/metadata["run"]["input_root"]
    native = json.loads((native_dir/"metadata.json").read_text(encoding="utf-8"))
    if native["status"] != "pass":
        raise RuntimeError("native input study is not a pass")
    count = metadata["run"]["n_paths"]
    block = metadata["theory"]["block"]
    dimension = native["theory"]["dimension"]
    steps = native["theory"]["intervals"]*native["run"]["substeps"]
    dt = native["theory"]["interval_dt"]/native["run"]["substeps"]
    sizes = metadata["theory"]["n_agents"]
    if count != 32 or block != 16 or steps != 64:
        raise ValueError("this postprocessor is scoped to the declared matched replay")
    targets = [run/"upper-functional.py", run/"upper-functional-metadata.json"]
    targets += [run/f"upper-functional-{n}{suffix}" for n in sizes
                for suffix in (".json", ".npz")]
    if any(path.exists() for path in targets):
        raise FileExistsError("postprocessing output already exists; preserve it")
    results = []
    for n_agents in sizes:
        activation = root/native["run"]["activation_root"]/f"N{n_agents}-learn_both-final.npz"
        history_file = native_dir/f"N{n_agents}-joint-paths-and-scores.npz"
        scores_file = run/f"N{n_agents}-source-adapted-scores.npz"
        with np.load(activation, allow_pickle=False) as saved:
            mobility = np.asarray(saved["Sigma"], dtype=np.float64).copy()
        if mobility.shape != (n_agents, dimension, dimension):
            raise ValueError("unexpected activation mobility shape")
        innovation = (2*dt/block**2)*mobility.reshape(
            n_agents//block, block, dimension, dimension).sum(axis=1)
        chol = np.linalg.cholesky(innovation)
        logdet = 2*math.fsum(map(float, np.log(np.diagonal(
            chol, axis1=-2, axis2=-1)).ravel()))
        retained_dimension = n_agents//block*dimension
        noise_entropy = .5*(retained_dimension*math.log(2*math.pi*math.e)+logdet)
        with np.load(history_file, allow_pickle=False) as saved:
            native_log_source = np.asarray(
                saved["log_source_kernel"][:count], dtype=np.float64).copy()
        if native_log_source.shape != (count, steps):
            raise ValueError("native source history shape mismatch")
        arrays = {"native_log_source": native_log_source,
                  "noise_entropy_per_step": np.asarray(noise_entropy),
                  "path_indices": np.arange(count)}
        report = {"n_agents": n_agents, "n_paths": count, "microsteps": steps,
                  "dt": dt, "block": block, "retained_dimension": retained_dimension,
                  "noise_logdet": logdet, "noise_entropy_per_step": noise_entropy,
                  "units": "nats per complete path", "posthoc": True,
                  "arms": {}, "paired_loss_differences": {},
                  "inputs": [str(path.relative_to(root)) for path in
                             (activation, history_file, scores_file)]}
        with np.load(scores_file, allow_pickle=False) as saved:
            scores = {}
            for arm in ARMS:
                joint = np.asarray(saved[arm+"_log_joint"], dtype=np.float64)
                source = np.asarray(saved[arm+"_log_source"], dtype=np.float64)
                if joint.shape != (count, steps) or source.shape != joint.shape:
                    raise ValueError(f"unmatched score arrays: {arm}")
                if not np.isfinite(joint).all() or not np.isfinite(source).all():
                    raise ValueError(f"nonfinite candidate score: {arm}")
                scores[arm] = joint.copy()
                rows = {"joint": native_log_source-joint-noise_entropy,
                        "source": native_log_source-source,
                        "configuration": -(joint-source)-noise_entropy}
                summary = {}
                for term, values in rows.items():
                    totals = path_sums(values)
                    if not np.isfinite(totals).all():
                        raise ValueError(f"nonfinite upper-functional statistic: {arm}")
                    arrays[f"{arm}_{term}_rows"] = values
                    arrays[f"{arm}_{term}_paths"] = totals
                    summary[term] = estimate(totals)
                joint_paths = arrays[f"{arm}_joint_paths"]
                separated = path_sums(native_log_source)-path_sums(joint)-steps*noise_entropy
                summary["max_accumulation_order_difference"] = float(
                    np.max(np.abs(joint_paths-separated)))
                summary["max_decomposition_residual"] = float(np.max(np.abs(
                    joint_paths-arrays[f"{arm}_source_paths"]-
                    arrays[f"{arm}_configuration_paths"])))
                summary["risk"] = ("tape-conditioned risk plus information gap"
                                   if arm in ("filter64", "reset64")
                                   else "deterministic-parent risk plus information gap")
                report["arms"][arm] = summary
            for first, second in (("gaussian", "reset_gaussian"),
                                  ("gaussian", "baseline"),
                                  ("reset_gaussian", "baseline"),
                                  ("filter64", "baseline"), ("reset64", "baseline")):
                key = first+"_minus_"+second
                paired = path_sums(scores[second]-scores[first])
                arrays[key+"_paths"] = paired
                report["paired_loss_differences"][key] = estimate(paired)
        with (run/f"upper-functional-{n_agents}.npz").open("xb") as handle:
            np.savez_compressed(handle, **arrays)
        write_json(run/f"upper-functional-{n_agents}.json", report)
        results.append(report)
        print(json.dumps({"n_agents": n_agents, "arms": report["arms"]}), flush=True)
    post = {"status": "pass", "posthoc": True,
            "created_utc": datetime.now(timezone.utc).isoformat(),
            "python": sys.executable, "python_version": platform.python_version(),
            "numpy": np.__version__, "study_metadata_changed": False,
            "native_paths_generated": False, "gpu_used": False,
            "scope": "Sample estimates of the existing augmented upper functional; "
                     "not retained-path KL estimates or confidence upper bounds. "
                     "Particle arms retain their independent tape-conditioned risk.",
            "cases": results}
    with (run/"upper-functional.py").open("xb") as handle:
        handle.write(Path(__file__).read_bytes())
    write_json(run/"upper-functional-metadata.json", post)


if __name__ == "__main__":
    main()
