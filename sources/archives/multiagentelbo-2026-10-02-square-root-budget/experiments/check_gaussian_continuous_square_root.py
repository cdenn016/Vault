"""Independently check the completed frozen square-root budget study in NumPy."""
from __future__ import annotations

import math
import os
from pathlib import Path
import subprocess
import sys
from typing import Callable

ROOT = Path(__file__).resolve().parents[1]
METRICS = ("drift", "mark", "self", "visible", "total", "augmented")
ATOL, RTOL = 1e-10, 5e-11
FIBER_TOLERANCE, ROW_TOLERANCE = 1e-8, 1e-11


def _reconstruct(
    values:       dict,
    tape:         dict,
    coefficients: dict,
    horizon:      float,
    block:        int,
    compare:      Callable[..., None],
) -> dict[str, float]:
    r"""Rebuild .5 (P M delta g)^T Q_r^(-1)(P M delta g) and marked costs."""
    import numpy as np

    M, H, J_0 = [coefficients[key] for key in ("Sigma", "H", "J_0")]
    sources, index, reverse = [coefficients[key] for key in ("sources", "link_index", "reverse")]
    maps = coefficients["Theta"][index].copy()
    maps[reverse] = np.linalg.inv(maps[reverse])
    N, K = M.shape[:2]
    tau = coefficients["tau"]
    Qr = 2*M.reshape(N//block, block, K, K).sum(1)/block**2
    receiver = np.arange(N)
    rates = []
    for delta, labels in zip(values["native"][:-1]-values["mean"][:-1], values["assignments"][:-1]):
        source, links = sources[receiver, labels], maps[receiver, labels]
        residual = delta-np.einsum("nij,nj->ni", links, delta[source])
        record = np.einsum("nij,nj->ni", H, residual)/tau
        force = np.einsum("nij,nj->ni", J_0, delta)+record
        np.add.at(force, source, -np.einsum("nji,nj->ni", links, record))
        projected = np.einsum("nij,nj->ni", M, force).reshape(N//block, block, K).mean(1)
        solved = np.linalg.solve(Qr, projected[..., None])[..., 0]
        rates.append(.5*np.sum(projected*solved))
    rates = np.asarray(rates)
    compare("drift_rates", values["drift_rates"], rates)
    probe_steps = np.searchsorted(values["times"], tape["probe_times"], side="right")-1
    native_rows, native_self = [], []
    for probe, step in enumerate(probe_steps):
        X = values["native"][step]
        residual = X[:, None]-np.einsum("nsij,nsj->nsi", maps, X[sources])
        cost = .5*np.einsum("nsi,nij,nsj->ns", residual, H, residual)
        logits = np.log(coefficients["pi"])-cost/tau
        rows = logits-np.logaddexp.reduce(logits, axis=-1, keepdims=True)
        native_rows.append(rows)
        native_self.append(rows[receiver, values["assignments"][step]].sum())
        drawn = (tape["probe_uniforms"][probe, :, None] > np.exp(rows).cumsum(-1)).sum(-1)
        drawn = np.minimum(drawn, rows.shape[-1]-1)
        compare("probe_labels", values["probe_labels"][probe], drawn, atol=0., rtol=0.)
    native = np.stack(native_rows)
    compare("native_source_rows", values["probe_log_beta"], native)
    compare("native_self_logs", values["probe_log_self_native"], np.asarray(native_self))
    # Check arithmetic from retained logs separately from their native-row derivation.
    retained_native = values["probe_log_beta"]
    candidate = values["probe_log_candidate_rows"]
    mark = (np.exp(retained_native)*(retained_native-candidate)).sum(axis=(-1, -2))
    log_p, log_q = values["probe_log_self_native"], values["probe_log_self_candidate"]
    difference = log_p-log_q
    self_cost = np.exp(log_p)*difference-np.exp(log_p)+np.exp(log_q)
    for probe in np.flatnonzero(np.abs(difference) < .01):
        d = float(difference[probe])
        self_cost[probe] = np.exp(log_p[probe])*math.fsum(
            (-d)**order/math.factorial(order) for order in range(2, 15))
    compare("tiny_self_cost", values["probe_self_psi"], self_cost, atol=1e-300, rtol=1e-9)
    visible = mark-self_cost
    for key, expected in (("mark_kl", mark), ("self_psi", self_cost), ("visible_kl", visible)):
        compare("probe_"+key, values["probe_"+key], expected)
    integrals = {"drift": float(rates@np.diff(values["times"])),
                 "mark": float(horizon*mark.mean()), "self": float(horizon*self_cost.mean()),
                 "visible": float(horizon*visible.mean())}
    integrals["total"] = integrals["drift"]+integrals["visible"]
    integrals["augmented"] = integrals["drift"]+integrals["mark"]
    for key, expected in integrals.items():
        compare(key+"_integral", values[key+"_integral"], expected)
    compare("tiny_self_integral", values["self_integral"], integrals["self"], atol=1e-300, rtol=1e-9)
    return integrals


def check(directory: Path) -> int:
    """Write one source archive and one terminal receipt without rerunning science."""
    from datetime import datetime, timezone
    import json
    import traceback
    import zipfile
    import numpy as np

    receipt_path = directory/"result-consistency.json"
    if receipt_path.exists():
        raise FileExistsError(f"preserving existing result receipt: {receipt_path}")
    receipt = {"status": "running", "run_dir": str(directory), "python": sys.executable,
        "utc": datetime.now(timezone.utc).isoformat(), "atol": ATOL, "rtol": RTOL,
        "fiber_tolerance": FIBER_TOLERANCE, "row_tolerance": ROW_TOLERANCE,
        "tiny_self_atol": 1e-300, "tiny_self_rtol": 1e-9,
        "scope": "All 32 saved paired paths, 64 grids and 36 aggregate estimates; independent NumPy arithmetic, not a continuous-time or confidence bound.",
        "limitations": ["Candidate self-prefix log probabilities are retained inputs; their prefix rows are not archived by this study.",
                        "Candidate Gaussian messages and reported covariance-fiber maxima are not independently regenerated.",
                        "Sixteen paths and one model realization per size give descriptive empirical standard errors."],
        "paths_checked": 0, "grids_checked": 0, "aggregate_estimates_checked": 0,
        "checks": {}, "cases": [], "context": "source archive"}

    def require(condition: bool, message: str) -> None:
        """Reject an unmet declared mathematical or completion condition."""
        if not condition:
            raise ValueError(message)

    def compare(
        name:     str,
        actual:   object,
        expected: object,
        atol:     float = ATOL,
        rtol:     float = RTOL,
    ) -> None:
        """Record discrepancies before applying the declared per-value tolerance."""
        a, b = np.asarray(actual), np.asarray(expected)
        require(a.shape == b.shape, f"{name}: shape {a.shape} != {b.shape}")
        require(bool(np.isfinite(a).all() and np.isfinite(b).all()), f"{name}: nonfinite values")
        error = np.abs(a-b)
        absolute = float(error.max()) if error.size else 0.
        record = receipt["checks"].setdefault(name, {"comparisons": 0, "values": 0,
            "max_absolute_error": 0., "atol": atol, "rtol": rtol})
        record["comparisons"] += 1
        record["values"] += int(a.size)
        record["max_absolute_error"] = max(record["max_absolute_error"], absolute)
        require(bool(np.all(error <= atol+rtol*np.abs(b))),
                f"{name}: maximum absolute discrepancy {absolute}; tolerance {atol}+{rtol}*abs(reference)")

    try:
        helper_names = ("coupled_learning_experiment", "coupled_learning", "network_experiment", "network")
        sources = [Path(__file__).resolve()]+[
            ROOT/"src/multiagent_elbo/realizations/gaussian"/(name+".py") for name in helper_names]
        with zipfile.ZipFile(directory/"checker-source.zip", "x", zipfile.ZIP_DEFLATED) as archive:
            for source in sources:
                archive.writestr(source.relative_to(ROOT).as_posix(), source.read_bytes())
        receipt["checker_sources"] = [source.relative_to(ROOT).as_posix() for source in sources]
        receipt["context"] = "producer completion"
        metadata = json.loads((directory/"metadata.json").read_text(encoding="utf-8"))
        require(metadata["status"] == "pass", "producer is incomplete or failed; refusing result analysis")
        run, theory, numerics = metadata["run"], metadata["theory"], metadata["numerics"]
        require(run["n_paths"] == 16 and theory["n_agents"] == [512, 1024], "study size/path contract differs")
        require(run["model_seed"] == 20261002 and run["path_seed"] == 20261007, "declared seeds differ")
        require(all(theory[key] == value for key, value in {
            "dimension": 2, "block_size": 16, "horizon": 1., "coarse_steps": 64,
            "n_probes": 2, "link_scale": .2, "tau": .5}.items()), "declared theory profile differs")
        require(numerics == {"device": "cpu", "dtype": "float64", "cpu_threads": 1,
                              "source_backend": "square_root"}, "declared numerical backend differs")
        n_paths, block, K, n_probes = 16, theory["block_size"], theory["dimension"], theory["n_probes"]
        horizon = theory["horizon"]
        expected_files = {f"N{N}-path{index:03d}.npz" for N in theory["n_agents"] for index in range(n_paths)}
        require({path.name for path in directory.glob("N*-path*.npz")} == expected_files,
                "complete study requires exactly the 32 declared path files")
        require(len(metadata["cases"]) == 2 and [case["n_agents"] for case in metadata["cases"]] == [512, 1024],
                "metadata case inventory differs")
        # Torch is used only by the declared coefficient builder, never for checks below.
        import torch
        from multiagent_elbo.realizations.gaussian.coupled_learning_experiment import build_coupled_case
        torch.set_num_threads(1)
        for size_index, N in enumerate(theory["n_agents"]):
            receipt["context"] = f"N{N} case"
            case = json.loads((directory/f"N{N}.json").read_text(encoding="utf-8"))
            meta_case = metadata["cases"][size_index]
            for entry in (case, meta_case):
                require(entry["status"] == "pass" and entry["completed_paths"] == n_paths and
                        entry["n_paths"] == n_paths and entry["n_agents"] == N, "case is incomplete")
                require(len(entry["paths"]) == n_paths and {p["path_index"] for p in entry["paths"]} == set(range(n_paths)),
                        "per-path index inventory differs")
            records = {entry["path_index"]: entry for entry in case["paths"]}
            meta_records = {entry["path_index"]: entry for entry in meta_case["paths"]}
            with np.load(directory/"inputs"/f"N{N}-learn_both-final.npz") as saved:
                coefficients = {key: saved[key].copy() for key in ("Sigma", "Theta", "pi")}
            model, _ = build_coupled_case(N, K, run["model_seed"], theory["link_scale"])
            coefficients.update({key: getattr(model, key).numpy().copy() for key in
                                 ("J_0", "H", "sources", "link_index", "reverse")})
            coefficients["tau"] = theory["tau"]
            require(all(np.isfinite(value).all() for value in coefficients.values()), "nonfinite model coefficients")
            require(coefficients["Sigma"].shape == (N, K, K), "activation mobility shape differs")
            rows = {grid: {metric: [] for metric in METRICS} for grid in ("coarse", "fine")}
            summary = {"n_agents": N, "paths": 0, "grids": 0, "estimates": {}}
            receipt["cases"].append(summary)
            for index in range(n_paths):
                receipt["context"] = f"N{N} path{index:03d}"
                seed = run["path_seed"]+100000*size_index+10*index
                require(records[index]["seed"] == meta_records[index]["seed"] == seed, "path/seed mapping differs")
                with np.load(directory/f"N{N}-path{index:03d}.npz") as saved:
                    tape = {key: saved[key].copy() for key in saved.files}
                require(all(np.isfinite(value).all() for value in tape.values()), "nonfinite path arrays")
                proposals = tape["proposal_times"]
                require(proposals.ndim == 1 and bool(np.all(np.diff(proposals) > 0)) and
                        bool(np.all((proposals > 0) & (proposals < horizon))), "invalid proposal times")
                require(tape["proposal_uniforms"].shape == (len(proposals), N) and
                        tape["probe_uniforms"].shape == (n_probes, N) and
                        tape["probe_times"].shape == (n_probes,), "stochastic tape shape differs")
                require(bool(np.all((tape["probe_times"] >= 0) & (tape["probe_times"] < horizon))), "invalid probe times")
                for key in ("probe_uniforms", "proposal_uniforms"):
                    require(bool(np.all((tape[key] >= 0) & (tape[key] < 1))), "uniform outside [0,1)")
                for grid in ("coarse", "fine"):
                    receipt["context"] = f"N{N} path{index:03d} {grid}"
                    prefix = grid+"_"
                    values = {key[len(prefix):]: value for key, value in tape.items() if key.startswith(prefix)}
                    times, X, mean, labels = [values[key] for key in ("times", "native", "mean", "assignments")]
                    require(times.ndim == 1 and len(times) > 1 and times[0] == 0 and times[-1] == horizon and
                            bool(np.all(np.diff(times) > 0)), "invalid temporal mesh")
                    require(bool(np.isin(proposals, times).all()), "proposal absent from mesh")
                    require(X.shape == mean.shape == (len(times), N, K) and labels.shape == (len(times), N), "history shape differs")
                    require(np.issubdtype(labels.dtype, np.integer) and
                            bool(np.all((labels >= 0) & (labels < coefficients["sources"].shape[1]))), "invalid assignments")
                    compare("initial_native", X[0], tape["initial_X"], atol=0., rtol=0.)
                    compare("initial_assignment", labels[0], tape["initial_J"], atol=0., rtol=0.)
                    retained_X, retained_mean = [value.reshape(len(times), N//block, block, K).mean(2) for value in (X, mean)]
                    compare("mean_fiber", retained_mean, retained_X, atol=FIBER_TOLERANCE, rtol=0.)
                    compare("reported_mean_fiber", values["projection_max_error"],
                            float(np.abs(retained_mean[:-1]-retained_X[:-1]).max()))
                    for key in ("projection_max_error", "covariance_projection_max_error"):
                        require(values[key].shape == () and 0 <= float(values[key]) <= FIBER_TOLERANCE,
                                f"{key} exceeds declared fiber tolerance")
                    changed = np.any(labels[1:] != labels[:-1], axis=1)
                    require(bool(np.isin(times[1:][changed], proposals).all()), "assignment changes outside proposals")
                    compare("proposal_count", values["proposal_count"], len(proposals), atol=0., rtol=0.)
                    compare("visible_changes", values["visible_changes"], int(changed.sum()), atol=0., rtol=0.)
                    for key in ("proposal_count", "visible_changes", "projection_max_error", "covariance_projection_max_error"):
                        for record in (records[index], meta_records[index]):
                            compare("path_record_"+key, record[prefix+key], values[key])
                    for key in ("log_beta", "log_candidate_rows"):
                        require(values["probe_"+key].shape == (n_probes, N, coefficients["sources"].shape[1]), "probe row shape differs")
                        compare("normalization_"+key, np.logaddexp.reduce(values["probe_"+key], axis=-1),
                                np.zeros((n_probes, N)), atol=ROW_TOLERANCE, rtol=0.)
                    for key in ("log_self_native", "log_self_candidate", "mark_kl", "self_psi", "visible_kl"):
                        require(values["probe_"+key].shape == (n_probes,), "probe scalar shape differs")
                    require(values["probe_labels"].shape == (n_probes, N), "probe label shape differs")
                    integrals = _reconstruct(values, tape, coefficients, horizon, block, compare)
                    for metric, expected in integrals.items():
                        rows[grid][metric].append(expected)
                        for record in (records[index], meta_records[index]):
                            compare("path_record_"+metric, record[prefix+metric+"_integral"], expected)
                    receipt["grids_checked"] += 1
                    summary["grids"] += 1
                boundaries = np.searchsorted(tape["fine_times"], tape["coarse_times"])
                require(bool(np.array_equal(tape["fine_times"][boundaries], tape["coarse_times"])), "paired meshes are not nested")
                aggregated = np.stack([tape["fine_dW"][left:right].sum(0) for left, right in zip(boundaries[:-1], boundaries[1:])])
                compare("shared_brownian_tape", tape["coarse_dW"], aggregated)
                receipt["paths_checked"] += 1
                summary["paths"] += 1
            for metric in METRICS:
                coarse, fine = [np.asarray(rows[grid][metric]) for grid in ("coarse", "fine")]
                for grid, samples in (("coarse", coarse), ("fine", fine), ("fine_minus_coarse", fine-coarse)):
                    receipt["context"] = f"N{N} {grid} {metric} summary"
                    center = math.fsum(float(value) for value in samples)/n_paths
                    scale = float(np.abs(samples).max())
                    variance_sum = 0. if scale == 0. else math.fsum((float(value)/scale-center/scale)**2 for value in samples)
                    estimates = {"mean": center,
                                 "standard_error": scale*math.sqrt(variance_sum/(n_paths*(n_paths-1)))}
                    summary["estimates"].setdefault(grid, {})[metric+"_integral"] = estimates
                    for case_record in (case, meta_case):
                        for key, expected in estimates.items():
                            compare("aggregate_"+key, case_record["estimates"][grid][metric+"_integral"][key], expected)
                    receipt["aggregate_estimates_checked"] += 1
        require((receipt["paths_checked"], receipt["grids_checked"], receipt["aggregate_estimates_checked"]) == (32, 64, 36),
                "declared coverage is incomplete")
        receipt["status"] = "pass"
        receipt["context"] = "completed"
    except Exception:
        receipt["status"] = "failed"
        receipt["traceback"] = traceback.format_exc()
    finally:
        with receipt_path.open("x", encoding="utf-8") as stream:
            json.dump(receipt, stream, indent=2, allow_nan=False)
    print(json.dumps({"status": receipt["status"], "receipt": str(receipt_path),
                     "paths": receipt["paths_checked"], "grids": receipt["grids_checked"],
                     "aggregate_estimates": receipt["aggregate_estimates_checked"]}), flush=True)
    if receipt["status"] != "pass":
        print(receipt["traceback"], file=sys.stderr)
        return 1
    return 0


def main() -> int:
    """Bootstrap isolated sequential-MKL CPU execution, retaining the directory argument."""
    if len(sys.argv) != 2:
        raise SystemExit("usage: check_gaussian_continuous_square_root.py RUN_DIR")
    directory = Path(sys.argv[1]).resolve()
    sequential = os.environ.get("MKL_THREADING_LAYER") == "SEQUENTIAL"
    os.environ["MKL_THREADING_LAYER"] = "SEQUENTIAL"
    os.environ["OMP_NUM_THREADS"] = os.environ["MKL_NUM_THREADS"] = "1"
    interpreter = Path(os.environ.get("CUDA_PYTHON", "C:/anaconda/python.exe"))
    same = os.path.normcase(str(Path(sys.executable).resolve())) == os.path.normcase(str(interpreter.resolve()))
    if not same or not sys.flags.isolated or not sequential:
        return subprocess.run([str(interpreter), "-I", "-B", str(Path(__file__).resolve()), str(directory)],
                              env=os.environ.copy(), check=False).returncode
    sys.path.insert(0, str(ROOT/"src"))
    return check(directory)


if __name__ == "__main__":
    raise SystemExit(main())
