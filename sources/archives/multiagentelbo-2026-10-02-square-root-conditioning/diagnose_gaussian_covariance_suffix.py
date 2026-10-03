"""Continue one captured Gaussian message over only its remaining saved path."""
from __future__ import annotations

import os
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
PHASE = ROOT/"docs/research/2026-10-02-renormalization-completion"
EVIDENCE = PHASE/"continuous-budget-evidence"
PARENT = PHASE/"covariance-diagnostic-evidence/20261003T025107540279Z"
SEGMENT = PARENT/"remaining-source-segment"
EARLIER = PHASE/"covariance-diagnostic-evidence/20261003T024319027686Z"
TOLERANCE = 1e-8


class CapturedStop(Exception):
    """An observed failure whose complete operation state is already saved."""


def diagnose() -> int:
    """Continue the captured suffix once without resampling, repair, or restart."""
    from dataclasses import replace
    from datetime import datetime, timezone
    import json
    import shutil
    import time
    import traceback
    import zipfile
    import numpy as np
    import torch
    from multiagent_elbo.realizations.gaussian.coupled_learning import CoupledState
    from multiagent_elbo.realizations.gaussian.coupled_learning_experiment import build_coupled_case
    from multiagent_elbo.realizations.gaussian.gaussian_message import observe_gaussian, propagate_gaussian

    torch.set_num_threads(1)
    directory = ROOT/"artifacts/gaussian-covariance-suffix"/datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    directory.mkdir(parents=True, exist_ok=False)
    started = time.perf_counter()
    metadata = {"status": "running", "mode": "captured_state_suffix", "path_index": 1,
                "device": "cpu", "dtype": "float64", "cpu_threads": 1, "tolerance": TOLERANCE,
                "start_capture": str(SEGMENT/"capture.npz"), "parent_metadata": str(PARENT/"metadata.json"),
                "earlier_mismatch_capture": str(EARLIER/"capture.npz"),
                "saved_path": str(EVIDENCE/"N1024-path001.npz"),
                "base_head": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
                "python": sys.executable, "torch": torch.__version__, "repairs": False,
                "native_resampling": False, "prior_interval_replay": False, "source_probes": False,
                "mean_mismatch_scope": "reporting only; previous mismatch remains preserved",
                "completed_suffix_intervals": 0, "maximum_archived_mean_error": 0., "future_source_changes": 0}
    context: dict = {"stage": "setup", "step": None, "time": None, "receiver": None}
    inputs: dict[str, torch.Tensor] = {}
    log = (directory/"diagnostic.jsonl").open("x", encoding="utf-8")

    def save_metadata() -> None:
        """Persist the current diagnosis without modifying source artifacts."""
        metadata["elapsed_seconds"] = time.perf_counter()-started
        (directory/"metadata.json").write_text(json.dumps(metadata, indent=2), encoding="utf-8")

    def record(values: dict) -> None:
        """Flush one scalar diagnostic record."""
        log.write(json.dumps(values)+"\n")
        log.flush()

    def stop(output: dict[str, torch.Tensor] | None, reason: str, trace: str | None = None) -> None:
        """Save incoming and available outgoing states at the first failure."""
        arrays = {key: value.detach().cpu().numpy() for key, value in inputs.items()}
        if output is not None:
            arrays.update({"output_"+key: value.detach().cpu().numpy() for key, value in output.items()})
        with (directory/"capture.npz").open("xb") as stream:
            np.savez_compressed(stream, **arrays)
        metadata.update(status="observed_failure", reason=reason, capture_context=context.copy())
        if trace is not None:
            metadata["traceback"] = trace
        record({**context, "status": "observed_failure", "reason": reason, "traceback": trace})
        save_metadata()
        raise CapturedStop(reason)

    def finite_output(mu: torch.Tensor, covariance: torch.Tensor) -> None:
        """Stop if an operation returns nonfinite state."""
        if not bool(torch.isfinite(mu).all() and torch.isfinite(covariance).all()):
            stop({"mean": mu, "covariance": covariance}, "nonfinite operation output")

    def fiber(mu: torch.Tensor, covariance: torch.Tensor) -> None:
        r"""Record max absolute P Sigma and P mu-r after a conditioning update."""
        finite_output(mu, covariance)
        covariance_error = float(covariance.reshape(1, 64, 16, 2, 2048).mean(2).abs().max())
        mean_error = float((mu.reshape(1, 64, 16, 2).mean(2).flatten(1)-inputs["retained_endpoint"]).abs().max())
        record({**context, "covariance_fiber_max": covariance_error, "mean_fiber_max": mean_error})
        if covariance_error > TOLERANCE:
            stop({"mean": mu, "covariance": covariance}, "covariance-fiber residual exceeds 1e-8")

    def difference(actual: torch.Tensor, reference: torch.Tensor) -> dict[str, float]:
        """Report comparison residuals without changing execution flow."""
        error = (actual-reference).abs()
        scale = torch.maximum(actual.abs(), reference.abs()).clamp_min(1e-300)
        return {"maximum_absolute_error": float(error.max()), "maximum_relative_error": float((error/scale).max())}

    save_metadata()
    print(json.dumps({"run_dir": str(directory), "status": "running"}), flush=True)
    try:
        copies = {SEGMENT/"capture.npz": "starting-capture.npz", SEGMENT/"metadata.json": "segment-metadata.json",
                  PARENT/"metadata.json": "parent-metadata.json", EARLIER/"capture.npz": "earlier-mismatch-capture.npz",
                  EVIDENCE/"N1024-path001.npz": "N1024-path001.npz",
                  EVIDENCE/"inputs/N1024-learn_both-final.npz": "N1024-learn_both-final.npz"}
        for source, name in copies.items():
            shutil.copyfile(source, directory/name)
        modules = ("source_gaussian", "gaussian_message", "coupled_learning", "coupled_learning_experiment",
                   "switching_paths", "network", "network_experiment", "network_dynamics", "predictive_interfaces", "locality")
        sources = [ROOT/"src/multiagent_elbo/realizations/gaussian"/(name+".py") for name in modules]+[Path(__file__).resolve()]
        sources += list(PHASE.glob("*covariance*CONTRACT*.md"))
        with zipfile.ZipFile(directory/"source.zip", "x", zipfile.ZIP_DEFLATED) as archive:
            for source in sources:
                archive.writestr(source.relative_to(ROOT).as_posix(), source.read_bytes())
        metadata["source_snapshot_paths"] = [source.relative_to(ROOT).as_posix() for source in sources]
        parent = json.loads((directory/"parent-metadata.json").read_text(encoding="utf-8"))
        segment = json.loads((directory/"segment-metadata.json").read_text(encoding="utf-8"))
        if segment["status"] != "segment_completed" or segment["last_receiver"] != 1023:
            raise ValueError("starting capture does not finish the source event")
        with np.load(directory/"N1024-learn_both-final.npz") as stored:
            initial = CoupledState(**{key: torch.from_numpy(stored[key].copy()) for key in ("mu", "Sigma", "pi", "Theta")})
        with np.load(directory/"N1024-path001.npz") as stored:
            native, saved_mean, assignments, times = [torch.from_numpy(stored["fine_"+key].copy()) for key in ("native", "mean", "assignments", "times")]
        with np.load(directory/"starting-capture.npz") as stored:
            mu, cov = [torch.from_numpy(stored["output_"+key].copy()) for key in ("mean", "covariance")]
            captured_assignment = torch.from_numpy(stored["assignments_after"].copy())
        with np.load(directory/"earlier-mismatch-capture.npz") as stored:
            earlier = {key: torch.from_numpy(stored[key].copy()) for key in ("input_mean", "input_covariance", "output_mean", "output_covariance")}
        start_time = parent["capture_context"]["time"]
        matches = (times == start_time).nonzero(as_tuple=True)[0]
        if len(matches) != 1:
            raise ValueError("capture time does not uniquely match the saved fine mesh")
        start = int(matches[0])
        if not torch.equal(captured_assignment, assignments[start]):
            raise ValueError("captured assignment differs from the suffix's starting sheet")
        if start != 44 or len(times)-1-start != 86 or not bool((assignments[start:] == assignments[start]).all()):
            raise ValueError("this bounded suffix requires index44, eighty-six intervals, and no later source changes")
        model, _ = build_coupled_case(1024, 2, 20261002, .2)
        model = replace(model, tau=.5)
        metadata.update(start_index=start, start_time=start_time, planned_suffix_intervals=len(times)-1-start,
                        model_seed=20261002, link_scale=.2, tau=.5, block_size=16)
        with torch.no_grad():
            inputs = {"input_mean": mu, "input_covariance": cov, "native_endpoint": native[start],
                      "retained_endpoint": native[start].reshape(1, 64, 16, 2).mean(2).flatten(1),
                      "assignments_before": assignments[start], "assignments_after": assignments[start]}
            context.update(stage="starting_capture", step=start-1, time=start_time)
            fiber(mu, cov)
            record({**context, "archived_mean_comparison": difference(mu[0], saved_mean[start])})
            for step in range(start, len(times)-1):
                context.update(stage="propagation", step=step, time=float(times[step+1]), receiver=None)
                inputs = {"input_mean": mu, "input_covariance": cov, "native_endpoint": native[step+1],
                          "retained_endpoint": native[step+1].reshape(1, 64, 16, 2).mean(2).flatten(1),
                          "assignments_before": assignments[step], "assignments_after": assignments[step+1]}
                forecast_mu, forecast_cov = propagate_gaussian(mu, cov, assignments[step:step+1],
                    initial.Sigma, initial, model, float(times[step+1]-times[step]))
                finite_output(forecast_mu, forecast_cov)
                if step == start:
                    metadata["first_forecast_comparison"] = {key: difference(value, earlier["input_"+key])
                        for key, value in (("mean", forecast_mu), ("covariance", forecast_cov))}
                    record({**context, "earlier_mismatch_comparison": metadata["first_forecast_comparison"]})
                context["stage"] = "endpoint_observation"
                inputs.update(input_mean=forecast_mu, input_covariance=forecast_cov)
                cross = forecast_cov.reshape(1, 2048, 64, 16, 2).mean(3).reshape(1, 2048, 128)
                projected = cross.reshape(1, 64, 16, 2, 128).mean(2).reshape(1, 128, 128)
                eigenvalues = torch.linalg.eigvalsh((projected+projected.mT)/2)
                record({**context, "phase": "before", "projected_eigen_min": float(eigenvalues.min()), "projected_eigen_max": float(eigenvalues.max())})
                conditioned = observe_gaussian(forecast_mu, forecast_cov, inputs["retained_endpoint"], 16)
                mu, cov = conditioned["mean"], conditioned["covariance"]
                if step == start:
                    metadata["first_observation_comparison"] = {key: difference(value, earlier["output_"+key])
                        for key, value in (("mean", mu), ("covariance", cov))}
                    record({**context, "earlier_mismatch_comparison": metadata["first_observation_comparison"]})
                fiber(mu, cov)
                comparison = difference(mu[0], saved_mean[step+1])
                record({**context, "stage": "archived_mean_comparison", **comparison})
                metadata["maximum_archived_mean_error"] = max(metadata["maximum_archived_mean_error"], comparison["maximum_absolute_error"])
                metadata["completed_suffix_intervals"] += 1
                save_metadata()
                print(f"suffix interval={metadata['completed_suffix_intervals']}/{metadata['planned_suffix_intervals']} time={float(times[step+1]):.9g}", flush=True)
            with (directory/"final-state.npz").open("xb") as stream:
                np.savez_compressed(stream, mean=mu.numpy(), covariance=cov.numpy(), assignments=assignments[-1].numpy(), native=native[-1].numpy())
            metadata["status"] = "suffix_completed"
    except CapturedStop:
        pass
    except Exception:
        try:
            stop(None, "suffix operation raised", traceback.format_exc())
        except CapturedStop:
            pass
    finally:
        save_metadata()
        log.close()
        print(json.dumps({"run_dir": str(directory), "status": metadata["status"], "elapsed_seconds": metadata["elapsed_seconds"]}), flush=True)
    return 0 if metadata["status"] in ("suffix_completed", "observed_failure") else 1


def main() -> int:
    """Select isolated single-thread CPU execution before importing Torch."""
    sequential = os.environ.get("MKL_THREADING_LAYER") == "SEQUENTIAL"
    os.environ["MKL_THREADING_LAYER"] = "SEQUENTIAL"
    os.environ["OMP_NUM_THREADS"] = os.environ["MKL_NUM_THREADS"] = "1"
    interpreter = Path(os.environ.get("CUDA_PYTHON", "C:/anaconda/python.exe"))
    same = os.path.normcase(str(Path(sys.executable).resolve())) == os.path.normcase(str(interpreter.resolve()))
    if not same or not sys.flags.isolated or not sequential:
        return subprocess.run([str(interpreter), "-I", "-B", str(Path(__file__).resolve())], env=os.environ.copy(), check=False).returncode
    sys.path.insert(0, str(ROOT/"src"))
    return diagnose()


if __name__ == "__main__":
    raise SystemExit(main())
