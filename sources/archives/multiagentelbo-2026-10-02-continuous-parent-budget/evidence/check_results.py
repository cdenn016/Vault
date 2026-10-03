"""Independently reconstruct a completed frozen-budget study from saved arrays.

This reads scientific outputs without changing them. The NumPy force calculation
includes receiver and sender terms; no production force or budget function runs.
It checks a discretized empirical calculation, not a continuous-law error bound.
"""
from __future__ import annotations

import os
os.environ["MKL_THREADING_LAYER"] = "SEQUENTIAL"
os.environ["OMP_NUM_THREADS"] = os.environ["MKL_NUM_THREADS"] = "1"

from dataclasses import replace
from datetime import datetime, timezone
import json
from pathlib import Path
import sys
import traceback

import numpy as np

_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_ROOT/"src"))
from multiagent_elbo.realizations.gaussian.coupled_learning_experiment import build_coupled_case
import torch

_METRICS = ("drift", "mark", "self", "visible", "total", "augmented")
_TOLERANCE = 1e-8


def _drift_rates(
    X:           np.ndarray,
    mean:        np.ndarray,
    assignments: np.ndarray,
    mobility:    np.ndarray,
    maps:        np.ndarray,
    sources:     np.ndarray,
    precision:   np.ndarray,
    H:           np.ndarray,
    tau:         float,
    block_size:  int,
) -> np.ndarray:
    r"""Return half the Q_r inverse norm squared of P M(g(X)-g(mean))."""
    difference = X[:-1]-mean[:-1]                       # (T,N,K).
    T, N, K = difference.shape
    sheet = assignments[:-1]
    receiver = np.arange(N)[None, :]
    selected_maps = maps[receiver, sheet]              # (T,N,K,K).
    selected_sources = sources[receiver, sheet]        # (T,N).
    source_difference = difference[np.arange(T)[:, None], selected_sources]
    residual = difference-np.einsum("tnij,tnj->tni", selected_maps, source_difference)
    record = np.einsum("nij,tnj->tni", H, residual)/tau
    force = np.einsum("nij,tnj->tni", precision, difference)+record
    sender = -np.einsum("tnji,tnj->tni", selected_maps, record)
    np.add.at(force, (np.arange(T)[:, None], selected_sources), sender)
    projected = np.einsum("nij,tnj->tni", mobility, force).reshape(T, N//block_size, block_size, K).mean(2)
    Qr = 2*mobility.reshape(N//block_size, block_size, K, K).sum(1)/block_size**2
    solved = np.linalg.solve(Qr[None], projected[..., None])[..., 0]
    return .5*(projected*solved).sum((1, 2))


def check_results(directory: Path) -> tuple[dict, Path]:
    """Write one fresh success or failure receipt without retrying a calculation."""
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    receipt_path = Path(__file__).with_name("result-check-"+stamp+".json")
    receipt = {"status": "running", "run_dir": str(directory), "utc": stamp,
               "absolute_tolerance": _TOLERANCE, "checks": {}, "cases": [],
               "scope": "Saved discrete budget, paired summaries and stochastic tapes; no continuous-time or confidence-bound claim.",
               "limits": "Candidate cubature rows and reported covariance-fiber residuals are retained inputs, not independently regenerated Gaussian messages."}

    def require(condition: bool, message: str) -> None:
        """Keep a clear failure reason in the receipt."""
        if not condition:
            raise AssertionError(message)

    def compare(name: str, actual: np.ndarray | float, expected: np.ndarray | float) -> None:
        """Accumulate absolute and relative residuals, gating only absolute error."""
        a, b = np.asarray(actual), np.asarray(expected)
        require(a.shape == b.shape, f"{name}: shape mismatch {a.shape} != {b.shape}")
        require(bool(np.isfinite(a).all() and np.isfinite(b).all()), f"{name}: nonfinite comparison")
        error = np.abs(a-b)
        absolute = float(error.max()) if error.size else 0.
        relative = float((error/np.maximum(np.maximum(np.abs(a), np.abs(b)), 1e-300)).max()) if error.size else 0.
        record = receipt["checks"].setdefault(name, {"comparisons": 0, "values": 0,
            "max_absolute_error": 0., "max_relative_error": 0.})
        record["comparisons"] += 1
        record["values"] += int(a.size)
        record["max_absolute_error"] = max(record["max_absolute_error"], absolute)
        record["max_relative_error"] = max(record["max_relative_error"], relative)
        require(absolute <= _TOLERANCE, f"{name}: absolute error {absolute}, relative error {relative}")

    try:
        torch.set_num_threads(1)
        metadata = json.loads((directory/"metadata.json").read_text(encoding="utf-8"))
        require(metadata["status"] == "pass", "study is not terminal with pass status; refusing analysis")
        run, theory = metadata["run"], metadata["theory"]
        block, K = theory["block_size"], theory["dimension"]
        horizon, n_probes = theory["horizon"], theory["n_probes"]
        n_paths = run["n_paths"]
        require(n_paths >= 2, "paired SE requires at least two paths")
        for size_index, N in enumerate(theory["n_agents"]):
            case = json.loads((directory/f"N{N}.json").read_text(encoding="utf-8"))
            require(case["status"] == "pass" and case["completed_paths"] == n_paths, f"N{N}: case incomplete")
            require({p.name for p in directory.glob(f"N{N}-path*.npz")} ==
                    {f"N{N}-path{index:03d}.npz" for index in range(n_paths)}, f"N{N}: unexpected completed path inventory")
            records = {entry["path_index"]: entry for entry in case["paths"]}
            require(len(case["paths"]) == n_paths and set(records) == set(range(n_paths)), f"N{N}: per-path records incomplete")
            with np.load(directory/"inputs"/f"N{N}-learn_both-final.npz") as inputs:
                mobility, Theta = inputs["Sigma"].copy(), inputs["Theta"].copy()
            model, _ = build_coupled_case(N, K, run["model_seed"], theory["link_scale"])
            model = replace(model, tau=theory["tau"])
            precision, H, sources, link_index, reverse = [value.numpy() for value in
                (model.J_0, model.H, model.sources, model.link_index, model.reverse)]
            maps = Theta[link_index].copy()
            maps[reverse] = np.linalg.inv(maps[reverse])
            scalar_rows = {grid: {key: [] for key in _METRICS} for grid in ("coarse", "fine")}
            counts = {"n_agents": N, "paths": 0, "coarse_steps": 0, "fine_steps": 0,
                      "proposals": 0, "coarse_visible_changes": 0, "fine_visible_changes": 0,
                      "probe_evaluations": 0}
            receipt["cases"].append(counts)
            for index in range(n_paths):
                require(records[index]["seed"] == run["path_seed"]+100000*size_index+10*index, f"N{N} path{index}: seed mismatch")
                with np.load(directory/f"N{N}-path{index:03d}.npz") as stored:
                    values = {key: stored[key].copy() for key in stored.files}
                require(all(np.isfinite(value).all() for value in values.values()), f"N{N} path{index}: nonfinite saved arrays")
                proposal_times = values["proposal_times"]
                require(proposal_times.ndim == 1 and np.all(np.diff(proposal_times) > 0) and
                        np.all((proposal_times > 0) & (proposal_times < horizon)), "invalid proposal times")
                require(values["proposal_uniforms"].shape == (len(proposal_times), N), "proposal uniform shape")
                require(values["probe_times"].shape == (n_probes,) and values["probe_uniforms"].shape == (n_probes, N), "probe tape shape")
                for name in ("proposal_uniforms", "probe_uniforms"):
                    require(bool(np.all((values[name] >= 0) & (values[name] < 1))), f"{name}: outside [0,1)")
                require(bool(np.all((values["probe_times"] >= 0) & (values["probe_times"] < horizon))), "probe time outside horizon")
                for grid in ("coarse", "fine"):
                    prefix = grid+"_"
                    times, X, mean, assignments = [values[prefix+name] for name in ("times", "native", "mean", "assignments")]
                    require(times[0] == 0 and times[-1] == horizon and np.all(np.diff(times) > 0), "invalid integration mesh")
                    require(bool(np.isin(proposal_times, times).all()), "proposal missing from mesh")
                    require(X.shape == mean.shape == (len(times), N, K) and assignments.shape == (len(times), N), "state history shape")
                    require(np.issubdtype(assignments.dtype, np.integer) and bool(np.all((assignments >= 0) & (assignments < sources.shape[1]))), "invalid assignments")
                    compare("initial_native", X[0], values["initial_X"])
                    compare("initial_assignment", assignments[0], values["initial_J"])
                    retained_X, retained_mean = [array.reshape(len(times), N//block, block, K).mean(2) for array in (X, mean)]
                    compare("retained_fiber", retained_mean, retained_X)
                    compare("reported_projection_max_error", values[prefix+"projection_max_error"],
                            float(np.abs(retained_mean[:-1]-retained_X[:-1]).max()))
                    require(0 <= float(values[prefix+"covariance_projection_max_error"]) <= _TOLERANCE, "reported covariance projection residual exceeds tolerance")
                    changed = np.any(assignments[1:] != assignments[:-1], axis=1)
                    require(bool(np.isin(times[1:][changed], proposal_times).all()), "assignment change outside proposal event")
                    compare("proposal_count", values[prefix+"proposal_count"], len(proposal_times))
                    compare("visible_change_count", values[prefix+"visible_changes"], int(changed.sum()))
                    for key in ("proposal_count", "visible_changes", "projection_max_error", "covariance_projection_max_error"):
                        compare("per_path_record_"+key, records[index][prefix+key], values[prefix+key])
                    rate = _drift_rates(X, mean, assignments, mobility, maps, sources, precision, H, model.tau, block)
                    compare("drift_rates", values[prefix+"drift_rates"], rate)
                    beta, candidate = values[prefix+"probe_log_beta"], values[prefix+"probe_log_candidate_rows"]
                    require(beta.shape == candidate.shape == (n_probes, N, sources.shape[1]), "source probe row shape")
                    compare("native_row_normalization", np.exp(beta).sum(-1), np.ones(beta.shape[:-1]))
                    compare("candidate_row_normalization", np.exp(candidate).sum(-1), np.ones(candidate.shape[:-1]))
                    mark = (np.exp(beta)*(beta-candidate)).sum((-1, -2))
                    native_log, candidate_log = values[prefix+"probe_log_self_native"], values[prefix+"probe_log_self_candidate"]
                    self_cost = np.exp(native_log)*(native_log-candidate_log)-np.exp(native_log)+np.exp(candidate_log)
                    visible = mark-self_cost
                    for key, actual in (("mark_kl", mark), ("self_psi", self_cost), ("visible_kl", visible)):
                        compare("probe_"+key, values[prefix+"probe_"+key], actual)
                    integrals = {"drift": float((rate*np.diff(times)).sum()), "mark": float(horizon*mark.mean()),
                                 "self": float(horizon*self_cost.mean()), "visible": float(horizon*visible.mean())}
                    integrals["total"] = integrals["drift"]+integrals["visible"]
                    integrals["augmented"] = integrals["drift"]+integrals["mark"]
                    for key, integral in integrals.items():
                        compare(key+"_integral", values[prefix+key+"_integral"], integral)
                        compare("per_path_record_"+key, records[index][prefix+key+"_integral"], integral)
                        scalar_rows[grid][key].append(integral)
                    counts[grid+"_steps"] += len(times)-1
                    counts[grid+"_visible_changes"] += int(changed.sum())
                    counts["probe_evaluations"] += n_probes
                coarse_times, fine_times = values["coarse_times"], values["fine_times"]
                boundaries = np.searchsorted(fine_times, coarse_times)
                require(bool(np.array_equal(fine_times[boundaries], coarse_times)), "coarse mesh not nested in fine mesh")
                coarse_noise = np.stack([values["fine_dW"][a:b].sum(0) for a, b in zip(boundaries[:-1], boundaries[1:])])
                compare("shared_brownian_increments", values["coarse_dW"], coarse_noise)
                counts["paths"] += 1
                counts["proposals"] += len(proposal_times)
            for metric in _METRICS:
                coarse, fine = [np.asarray(scalar_rows[grid][metric]) for grid in ("coarse", "fine")]
                for grid, samples in (("coarse", coarse), ("fine", fine), ("fine_minus_coarse", fine-coarse)):
                    estimates = case["estimates"][grid][metric+"_integral"]
                    compare("summary_mean", estimates["mean"], float(samples.mean()))
                    compare("summary_standard_error", estimates["standard_error"], float(samples.std(ddof=1)/np.sqrt(n_paths)))
        receipt["status"] = "pass"
    except Exception:
        receipt["status"] = "failed"
        receipt["traceback"] = traceback.format_exc()
    finally:
        with receipt_path.open("x", encoding="utf-8") as stream:
            json.dump(receipt, stream, indent=2, allow_nan=False)
    return receipt, receipt_path


def main() -> int:
    """Accept one completed run directory and retain one analysis receipt."""
    if len(sys.argv) != 2:
        raise SystemExit("usage: check_results.py RUN_DIR")
    receipt, path = check_results(Path(sys.argv[1]).resolve())
    print(json.dumps({"status": receipt["status"], "receipt": str(path), "cases": receipt["cases"]}), flush=True)
    if receipt["status"] != "pass":
        print(receipt["traceback"], file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
