"""Validate the integrated factor backend once on the archived N1024 fine tape."""
from __future__ import annotations

import os
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
PHASE = ROOT/"docs/research/2026-10-02-renormalization-completion"
FIBER_TOLERANCE = 1e-8


def reconstruct(values: dict, tape: dict, coefficients: dict, source_records: list[dict]) -> dict:
    r"""Independently reconstruct .5 a^T Q_r^(-1) a and marked jump costs in NumPy."""
    import math
    import numpy as np

    errors: dict[str, float] = {}
    def compare(name: str, actual: np.ndarray, expected: np.ndarray) -> None:
        """Check the predeclared absolute-plus-relative arithmetic tolerance."""
        actual, expected = np.asarray(actual), np.asarray(expected)
        errors[name] = float(np.max(np.abs(actual-expected)))
        if not np.allclose(actual, expected, atol=1e-10, rtol=5e-11):
            raise ValueError(f"independent arithmetic differs: {name}, {errors[name]}")

    M, H, J_0 = [coefficients[key] for key in ("mobility", "H", "J_0")]
    sources, index, reverse = [coefficients[key] for key in ("sources", "link_index", "reverse")]
    maps = coefficients["Theta"][index].copy()
    maps[reverse] = np.linalg.inv(maps[reverse])
    tau, block = float(coefficients["tau"]), 16
    N, K = M.shape[:2]
    Qr = 2*M.reshape(N//block, block, K, K).sum(1)/block**2
    rates = []
    receiver = np.arange(N)
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
    compare("drift_rates", rates, values["drift_rates"])
    drift = rates@np.diff(values["times"])
    compare("drift_integral", drift, values["drift_integral"])
    native, candidate = values["probe_log_beta"], values["probe_log_candidate_rows"]
    mark = (np.exp(native)*(native-candidate)).sum(axis=(-1, -2))
    log_p, log_q = values["probe_log_self_native"], values["probe_log_self_candidate"]
    difference = log_p-log_q
    self_cost = np.exp(log_p)*difference-np.exp(log_p)+np.exp(log_q)
    near = np.abs(difference) < .01
    for j in np.flatnonzero(near):
        d = float(difference[j])
        self_cost[j] = np.exp(log_p[j])*math.fsum((-d)**k/math.factorial(k) for k in range(2, 15))
    if not np.allclose(self_cost, values["probe_self_psi"], atol=1e-300, rtol=1e-9):
        raise ValueError("tiny self-cost relative check failed")
    for name, value in (("mark", mark), ("self", self_cost), ("visible", mark-self_cost)):
        compare("probe_"+name, value, values["probe_"+{"mark": "mark_kl", "self": "self_psi", "visible": "visible_kl"}[name]])
        compare(name+"_integral", value.mean(), values[name+"_integral"])
    compare("total_integral", drift+(mark-self_cost).mean(), values["total_integral"])
    compare("augmented_integral", drift+mark.mean(), values["augmented_integral"])
    probe_steps = np.searchsorted(values["times"], tape["probe_times"], side="right")-1
    for probe, step in enumerate(probe_steps):
        X = values["native"][step]
        residual = X[:, None]-np.einsum("nsij,nsj->nsi", maps, X[sources])
        cost = .5*np.einsum("nsi,nij,nsj->ns", residual, H, residual)
        logits = np.log(coefficients["pi"])-cost/tau
        shifted = logits-logits.max(axis=-1, keepdims=True)
        rows = shifted-np.log(np.exp(shifted).sum(axis=-1, keepdims=True))
        compare(f"native_rows_{probe}", rows, native[probe])
        compare(f"native_self_{probe}", rows[receiver, values["assignments"][step]].sum(), log_p[probe])
        record, = [entry for entry in source_records if entry["log_rows"].shape[0] == 2 and entry["time"] == values["times"][step]]
        compare(f"candidate_self_{probe}", record["log_rows"][1, receiver, values["assignments"][step]].sum(), log_q[probe])
    return errors


def validate() -> int:
    """Execute one fixed-tape path and retain its first failure without a retry."""
    from dataclasses import replace
    from datetime import datetime, timezone
    import json
    import shutil
    import time
    import traceback
    import zipfile
    import numpy as np
    import torch
    from multiagent_elbo.realizations.gaussian import continuous_budget as budget
    from multiagent_elbo.realizations.gaussian.coupled_learning import CoupledState
    from multiagent_elbo.realizations.gaussian.coupled_learning_experiment import build_coupled_case

    torch.set_num_threads(1)
    out = ROOT/"artifacts/gaussian-square-root-path"/datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    out.mkdir(parents=True, exist_ok=False)
    started = time.perf_counter()
    metadata = {"status": "running", "scope": "one archived N1024 path001 fine tape",
        "source_backend": "square_root", "python": sys.executable, "torch": torch.__version__,
        "device": "cpu", "dtype": "float64", "cpu_threads": 1,
        "base_head": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
        "forecast_calls": 0, "observation_calls": 0, "source_batches": [],
        "maximum_mean_fiber": 0., "maximum_covariance_fiber": 0., "maximum_row_normalization_error": 0.,
        "native_resampling": False, "learning_rerun": False, "full_study_retry": False}
    context: dict = {"operation": "setup", "time": 0.}
    inputs: dict = {}
    output: dict = {}
    source_records: list[dict] = []
    records = (out/"operations.jsonl").open("x", encoding="utf-8")
    original = (budget.propagate_gaussian, budget.observe_gaussian, budget.square_root_source_rows)

    def save() -> None:
        """Persist a terminal or running receipt."""
        metadata["elapsed_seconds"] = time.perf_counter()-started
        (out/"metadata.json").write_text(json.dumps(metadata, indent=2), encoding="utf-8")

    def invoke(kind: str, function: object, args: tuple, names: tuple[str, ...]) -> object:
        """Capture each real operation's inputs and measure its returned state."""
        nonlocal context, inputs, output
        step = metadata["forecast_calls"]
        context = {"operation": kind, "step": step, "time": float(tape["fine_times"][step])}
        inputs = {name: value for name, value in zip(names, args) if isinstance(value, torch.Tensor)}
        output = {}
        records.write(json.dumps({**context, "status": "entered"})+"\n"); records.flush()
        if kind == "source":
            print(json.dumps({**context, "batch": args[0].shape[0], "status": "entered"}), flush=True)
        result = function(*args)
        output = {"mean": result[0], "covariance": result[1]} if kind == "forecast" else result
        if not all(bool(torch.isfinite(value).all()) for value in output.values()):
            raise FloatingPointError(f"nonfinite {kind} output")
        diagnostics = {}
        if kind != "forecast":
            B, N, K = output["mean"].shape
            expected = args[2] if kind == "observation" else args[0].reshape(B, 64, 16, 2).mean(2).flatten(1)
            mean_error = float((output["mean"].reshape(B, 64, 16, 2).mean(2).flatten(1)-expected).abs().max())
            cov_error = float(output["covariance"].reshape(B, 64, 16, 2, N*K).mean(2).abs().max())
            diagnostics.update(mean_fiber=mean_error, covariance_fiber=cov_error)
            metadata["maximum_mean_fiber"] = max(metadata["maximum_mean_fiber"], mean_error)
            metadata["maximum_covariance_fiber"] = max(metadata["maximum_covariance_fiber"], cov_error)
            if max(mean_error, cov_error) > FIBER_TOLERANCE:
                raise FloatingPointError(f"post-conditioning fiber residual exceeds {FIBER_TOLERANCE}")
        if kind == "source":
            metadata["source_batches"].append(int(args[0].shape[0]))
            row_error = float(torch.logsumexp(output["log_rows"], dim=-1).abs().max())
            metadata["maximum_row_normalization_error"] = max(metadata["maximum_row_normalization_error"], row_error)
            diagnostics["row_normalization_error"] = row_error
            if row_error > 1e-11:
                raise FloatingPointError("source-row normalization exceeds 1e-11")
            retained_rows = {"time": np.array(context["time"]), "log_rows": output["log_rows"].numpy(), "labels": args[2].numpy()}
            source_records.append(retained_rows)
            np.savez_compressed(out/f"source-call{len(source_records):02d}.npz", **retained_rows)
        else:
            metadata[kind+"_calls"] += 1
        records.write(json.dumps({**context, "status": "completed", **diagnostics})+"\n"); records.flush()
        if kind == "source" or (kind == "observation" and metadata["observation_calls"] % 16 == 0):
            save(); print(json.dumps({**context, "status": "completed", **diagnostics}), flush=True)
        return result

    def forecast(*args: object) -> tuple:
        """Observe the actual forecast entry without modifying its arithmetic."""
        return invoke("forecast", original[0], args, ("mean", "covariance", "assignments", "mobility"))

    def observe(*args: object) -> dict:
        """Observe initialization and every endpoint conditioning operation."""
        return invoke("observation", original[1], args, ("mean", "covariance", "retained"))

    def source(*args: object) -> dict:
        """Observe visible source updates and the two-branch hypothetical probes."""
        return invoke("source", original[2], args, ("mean", "covariance", "labels"))

    save(); print(json.dumps({"run_dir": str(out), "status": "running"}), flush=True)
    try:
        for name, path in {"path.npz": PHASE/"continuous-budget-evidence/N1024-path001.npz",
                           "activation.npz": PHASE/"continuous-budget-evidence/inputs/N1024-learn_both-final.npz"}.items():
            shutil.copyfile(path, out/name)
        modules = ("continuous_budget", "source_square_root", "source_gaussian", "gaussian_message", "coupled_learning",
                   "coupled_learning_experiment", "switching_paths", "network", "network_experiment", "network_dynamics", "predictive_interfaces", "locality")
        sources = [ROOT/"src/multiagent_elbo/realizations/gaussian"/(name+".py") for name in modules]
        sources += [Path(__file__), ROOT/"experiments/gaussian_continuous_square_root.py", PHASE/"covariance-square-root-integration-CONTRACT.md"]
        with zipfile.ZipFile(out/"source.zip", "x", zipfile.ZIP_DEFLATED) as archive:
            for path in sources: archive.writestr(path.relative_to(ROOT).as_posix(), path.read_bytes())
        with np.load(out/"activation.npz") as stored:
            initial = CoupledState(**{key: torch.from_numpy(stored[key].copy()) for key in ("mu", "Sigma", "pi", "Theta")})
        keys = ("initial_X", "initial_J", "fine_times", "fine_dW", "proposal_times", "proposal_uniforms", "probe_times", "probe_uniforms")
        with np.load(out/"path.npz") as stored:
            tape = {key: torch.from_numpy(stored[key].copy()) for key in keys}
            reference = {key: stored["fine_"+key].copy() for key in ("native", "mean", "assignments", "total_integral")}
        model, _ = build_coupled_case(1024, 2, 20261002, .2)
        model = replace(model, tau=.5)
        coefficients = {key: getattr(model, key).numpy() for key in ("a", "J_0", "H", "sources", "link_index", "reverse")}
        coefficients.update(mobility=initial.Sigma.numpy(), Theta=initial.Theta.numpy(), pi=initial.pi.numpy(), tau=np.array(model.tau))
        np.savez_compressed(out/"coefficients.npz", **coefficients)
        if len(tape["fine_times"])-1 != 130 or len(tape["probe_times"]) != 2 or len(tape["proposal_times"]) != 2:
            raise ValueError("archived tape differs from the declared operation counts")
        budget.propagate_gaussian, budget.observe_gaussian, budget.square_root_source_rows = forecast, observe, source
        with torch.no_grad():
            computed = budget._run_grid(initial.Sigma, initial, model, tape, torch.arange(len(tape["fine_times"])),
                                        1., 16, source_backend="square_root")
        values = {key: value.numpy() for key, value in computed.items()}
        np.savez_compressed(out/"path-output.npz", **values)
        context = {"operation": "post-run checks"}
        if not all(np.isfinite(value).all() for value in values.values()):
            raise FloatingPointError("nonfinite path output")
        native_error = float(np.max(np.abs(values["native"]-reference["native"])))
        if native_error > 1e-12 or not np.array_equal(values["assignments"], reference["assignments"]):
            raise ValueError("native path does not match its archived reference")
        if metadata["source_batches"].count(1) != 2 or metadata["source_batches"].count(2) != 2 or float(values["visible_changes"]) != 2:
            raise ValueError("both visible events and both probes must run the selected backend")
        arithmetic = reconstruct(values, {key: value.numpy() for key, value in tape.items()}, coefficients, source_records)
        metadata.update(status="pass", native_maximum_error=native_error, assignments_exact=True,
            candidate_mean_difference_from_dense=float(np.max(np.abs(values["mean"]-reference["mean"]))),
            candidate_total_difference_from_dense=float(values["total_integral"]-reference["total_integral"]),
            arithmetic_maximum_errors=arithmetic,
            integrals={key: float(value) for key, value in values.items() if key.endswith("_integral")})
        return 0
    except Exception:
        metadata.update(status="failed", failure_context=context, traceback=traceback.format_exc())
        arrays = {"input_"+key: value.detach().numpy() for key, value in inputs.items()}
        arrays.update({"output_"+key: value.detach().numpy() for key, value in output.items()})
        np.savez_compressed(out/"failure-capture.npz", **arrays)
        print(metadata["traceback"], flush=True)
        return 1
    finally:
        budget.propagate_gaussian, budget.observe_gaussian, budget.square_root_source_rows = original
        save(); records.close()
        print(json.dumps({"run_dir": str(out), **metadata}), flush=True)


def main() -> int:
    """Bootstrap the declared isolated CPU runtime before importing numerical libraries."""
    sequential = os.environ.get("MKL_THREADING_LAYER") == "SEQUENTIAL"
    os.environ["MKL_THREADING_LAYER"] = "SEQUENTIAL"
    os.environ["OMP_NUM_THREADS"] = os.environ["MKL_NUM_THREADS"] = "1"
    interpreter = Path(os.environ.get("CUDA_PYTHON", "C:/anaconda/python.exe"))
    same = os.path.normcase(str(Path(sys.executable).resolve())) == os.path.normcase(str(interpreter.resolve()))
    if not same or not sys.flags.isolated or not sequential:
        return subprocess.run([str(interpreter), "-I", "-B", str(Path(__file__).resolve())], env=os.environ.copy(), check=False).returncode
    sys.path.insert(0, str(ROOT/"src"))
    return validate()


if __name__ == "__main__":
    raise SystemExit(main())
