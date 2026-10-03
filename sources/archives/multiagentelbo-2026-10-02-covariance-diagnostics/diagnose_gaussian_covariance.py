"""Diagnose local source conditioning during the first two archived source events."""
from __future__ import annotations

import os
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT/"docs/research/2026-10-02-renormalization-completion/continuous-budget-evidence"
TOLERANCE = 1e-8
MODE = "local_conditioning"
LOCAL_CONDITION_THRESHOLD = 1e12


class CapturedStop(Exception):
    """An observed diagnostic stop whose input/output state has been retained."""


def diagnose() -> int:
    """Replay saved observations once; preserve the first failure without repair."""
    from dataclasses import replace
    from datetime import datetime, timezone
    import json
    import shutil
    import time
    import traceback
    import zipfile
    import numpy as np
    import torch
    from multiagent_elbo.realizations.gaussian import source_gaussian
    from multiagent_elbo.realizations.gaussian.coupled_learning import CoupledModel, CoupledState
    from multiagent_elbo.realizations.gaussian.coupled_learning_experiment import build_coupled_case
    from multiagent_elbo.realizations.gaussian.gaussian_message import observe_gaussian, propagate_gaussian

    torch.set_num_threads(1)
    directory = ROOT/"artifacts/gaussian-covariance-diagnostic"/datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    directory.mkdir(parents=True, exist_ok=False)
    started = time.perf_counter()
    metadata = {"status": "running", "mode": MODE, "local_condition_threshold": LOCAL_CONDITION_THRESHOLD,
                "source_events": 0, "path_index": 1, "n_agents": 1024, "grid": "fine",
                "tolerance": TOLERANCE, "device": "cpu", "dtype": "float64", "cpu_threads": 1,
                "source_path": str(EVIDENCE/"N1024-path001.npz"),
                "activation_path": str(EVIDENCE/"inputs/N1024-learn_both-final.npz"),
                "base_head": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
                "python": sys.executable, "torch": torch.__version__, "completed_intervals": 0,
                "source_receivers_completed": 0, "source_probes_replayed": False, "repairs": False}
    context: dict = {"stage": "setup", "step": -1, "time": 0., "receiver": None}
    inputs: dict[str, torch.Tensor] = {}
    original_step = source_gaussian._source_step
    log = (directory/"diagnostic.jsonl").open("x", encoding="utf-8")

    def save_metadata() -> None:
        """Persist the attempt state, including elapsed time and terminal reason."""
        metadata["elapsed_seconds"] = time.perf_counter()-started
        (directory/"metadata.json").write_text(json.dumps(metadata, indent=2), encoding="utf-8")

    def record(values: dict) -> None:
        """Flush scalar observations as soon as they are available."""
        log.write(json.dumps(values)+"\n")
        log.flush()

    def stop(
        output:          dict[str, torch.Tensor] | None,
        reason:          str,
        status:          str = "observed_failure",
        exception_trace: str | None = None,
    ) -> None:
        """Capture full operation inputs and available outputs, then leave orderly."""
        arrays = {key: value.detach().cpu().numpy() for key, value in inputs.items()}
        if output is not None:
            arrays.update({"output_"+key: value.detach().cpu().numpy() for key, value in output.items()})
        with (directory/"capture.npz").open("xb") as stream:
            np.savez_compressed(stream, **arrays)
        metadata.update({"status": status, "reason": reason, "capture_context": context.copy()})
        if exception_trace is not None:
            metadata["traceback"] = exception_trace
        record({**context, "status": status, "reason": reason, "traceback": exception_trace})
        save_metadata()
        raise CapturedStop(reason)

    def residuals(mu: torch.Tensor, covariance: torch.Tensor) -> dict[str, float]:
        r"""Measure max absolute P Sigma and P mu-r without changing tensors."""
        observed = inputs["retained_endpoint"]
        projection = covariance.reshape(1, 64, 16, 2, 2048).mean(2)
        mean = mu.reshape(1, 64, 16, 2).mean(2).flatten(1)
        return {"covariance_fiber_max": float(projection.abs().max()),
                "mean_fiber_max": float((mean-observed).abs().max())}

    def check_output(mu: torch.Tensor, covariance: torch.Tensor) -> None:
        """Stop on the first post-update covariance-fiber threshold exceedance."""
        measured = residuals(mu, covariance)
        record({**context, "phase": "after", **measured})
        if not all(np.isfinite(value) for value in measured.values()):
            stop({"mean": mu, "covariance": covariance}, "nonfinite fiber diagnostic")
        if measured["covariance_fiber_max"] > TOLERANCE:
            stop({"mean": mu, "covariance": covariance}, "covariance-fiber residual exceeds 1e-8")

    def source_step(
        mu:         torch.Tensor,
        covariance: torch.Tensor,
        labels:     torch.Tensor,
        maps:       torch.Tensor,
        state:      CoupledState,
        model:      CoupledModel,
        receiver:   int,
        block_size: int,
    ) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
        """Instrument the unchanged receiver update without modifying its inputs."""
        context.update(stage="source_receiver", receiver=receiver)
        inputs.update(input_mean=mu, input_covariance=covariance, labels=labels, comparison_maps=maps)
        record({**context, "phase": "before", **residuals(mu, covariance)})
        # The frozen cycle/stride-17 profile has three distinct star nodes and
        # no complete sixteen-node block; all six coordinates are independent.
        nodes = sorted({receiver, *model.sources[receiver].tolist()})
        coordinates = torch.tensor([2*node+k for node in nodes for k in range(2)], dtype=torch.long)
        local = covariance[:, coordinates][:, :, coordinates]
        inputs.update(local_coordinates=coordinates, input_local_covariance=local)
        eigenvalues = torch.linalg.eigvalsh(local)
        low, high = float(eigenvalues.min()), float(eigenvalues.max())
        condition = high/low if low > 0 else None
        record({**context, "phase": "local_before", "local_eigen_min": low,
                "local_eigen_max": high, "local_condition": condition})
        if low <= 0 or condition > LOCAL_CONDITION_THRESHOLD:
            stop(None, "incoming local covariance is nonpositive or exceeds diagnostic condition threshold")
        try:
            result = original_step(mu, covariance, labels, maps, state, model, receiver, block_size)
        except Exception:
            stop(None, "source update raised", exception_trace=traceback.format_exc())
        check_output(result[1], result[2])
        local_after = result[2][:, coordinates][:, :, coordinates]
        eigenvalues_after = torch.linalg.eigvalsh(local_after)
        low_after, high_after = float(eigenvalues_after.min()), float(eigenvalues_after.max())
        condition_after = high_after/low_after if low_after > 0 else None
        record({**context, "phase": "local_after", "local_eigen_min": low_after,
                "local_eigen_max": high_after, "local_condition": condition_after})
        output = {"mean": result[1], "covariance": result[2], "local_covariance": local_after}
        if low_after <= 0 or condition_after > LOCAL_CONDITION_THRESHOLD:
            stop(output, "outgoing local covariance is nonpositive or exceeds diagnostic condition threshold")
        metadata["source_receivers_completed"] += 1
        if (receiver+1) % 128 == 0:
            print(f"step={context['step']} source receiver={receiver+1}/1024", flush=True)
        if metadata["source_events"] == 2 and receiver == 1023:
            compare_saved(result[1], result[2], saved_mean[context["step"]+1])
            stop(output, "second source event completed without local ill-conditioning", status="no_local_ill_conditioning")
        return result

    def observe(mu: torch.Tensor, covariance: torch.Tensor) -> tuple[torch.Tensor, torch.Tensor]:
        """Record observation inputs and inspect its returned conditional fiber."""
        inputs.update(input_mean=mu, input_covariance=covariance)
        record({**context, "phase": "before", **residuals(mu, covariance)})
        try:
            conditioned = observe_gaussian(mu, covariance, inputs["retained_endpoint"], 16)
        except Exception:
            stop(None, "Gaussian observation raised", exception_trace=traceback.format_exc())
        check_output(conditioned["mean"], conditioned["covariance"])
        return conditioned["mean"], conditioned["covariance"]

    def compare_saved(mu: torch.Tensor, covariance: torch.Tensor, saved: torch.Tensor) -> None:
        """Stop rather than interpret a replay that has drifted from the saved path."""
        mismatch = float((mu[0]-saved).abs().max())
        record({**context, "stage": "saved_mean_comparison", "max_absolute_error": mismatch})
        if not np.isfinite(mismatch) or mismatch > TOLERANCE:
            inputs["saved_mean"] = saved
            context["stage"] = "saved_mean_comparison"
            stop({"mean": mu, "covariance": covariance}, "replay mean differs from saved mean", status="mismatch")

    save_metadata()
    print(json.dumps({"run_dir": str(directory), "status": "running"}), flush=True)
    try:
        for source in (EVIDENCE/"N1024-path001.npz", EVIDENCE/"inputs/N1024-learn_both-final.npz", EVIDENCE/"metadata.json"):
            shutil.copyfile(source, directory/("origin-metadata.json" if source.name == "metadata.json" else source.name))
        modules = ("source_gaussian", "gaussian_message", "coupled_learning", "coupled_learning_experiment",
                   "switching_paths", "network", "network_experiment", "network_dynamics", "predictive_interfaces", "locality")
        sources = [ROOT/"src/multiagent_elbo/realizations/gaussian"/(name+".py") for name in modules]+[Path(__file__).resolve()]
        sources += list((ROOT/"docs/research/2026-10-02-renormalization-completion").glob("*covariance*CONTRACT*.md"))
        with zipfile.ZipFile(directory/"source.zip", "x", zipfile.ZIP_DEFLATED) as archive:
            for source in sources:
                archive.writestr(source.relative_to(ROOT).as_posix(), source.read_bytes())
        metadata["source_snapshot_paths"] = [source.relative_to(ROOT).as_posix() for source in sources]
        with np.load(directory/"N1024-learn_both-final.npz") as stored:
            initial = CoupledState(**{key: torch.from_numpy(stored[key].copy()) for key in ("mu", "Sigma", "pi", "Theta")})
        with np.load(directory/"N1024-path001.npz") as stored:
            native, saved_mean, assignments, times = [torch.from_numpy(stored["fine_"+key].copy())
                for key in ("native", "mean", "assignments", "times")]
        model, _ = build_coupled_case(1024, 2, 20261002, .2)
        model = replace(model, tau=.5)
        metadata.update(model_seed=20261002, link_scale=.2, tau=.5, block_size=16,
                        recorded_intervals=len(times)-1, source_snapshot_complete=True)
        source_gaussian._source_step = source_step
        with torch.no_grad():
            inputs.update(native_endpoint=native[0], retained_endpoint=native[0].reshape(1, 64, 16, 2).mean(2).flatten(1),
                          assignments_before=assignments[0], assignments_after=assignments[0])
            context.update(stage="initial_observation", time=float(times[0]))
            mu, cov = observe(initial.mu[None], torch.block_diag(*initial.Sigma)[None])
            compare_saved(mu, cov, saved_mean[0])
            for step in range(len(times)-1):
                context.update(stage="propagation", step=step, time=float(times[step+1]), receiver=None)
                inputs = {"input_mean": mu, "input_covariance": cov, "native_endpoint": native[step+1],
                          "retained_endpoint": native[step+1].reshape(1, 64, 16, 2).mean(2).flatten(1),
                          "assignments_before": assignments[step], "assignments_after": assignments[step+1]}
                forecast_mu, forecast_cov = propagate_gaussian(mu, cov, assignments[step:step+1],
                    initial.Sigma, initial, model, float(times[step+1]-times[step]))
                context["stage"] = "endpoint_observation"
                mu, cov = observe(forecast_mu, forecast_cov)
                if not torch.equal(assignments[step], assignments[step+1]):
                    metadata["source_events"] += 1
                    update = source_gaussian.sequential_source_message(mu, cov, assignments[step:step+1],
                        assignments[step+1:step+2], initial, model, 16, shortcut_mass=0.)
                    mu, cov = update["mean"], update["covariance"]
                compare_saved(mu, cov, saved_mean[step+1])
                metadata["completed_intervals"] = step+1
                save_metadata()
                print(f"completed interval={step+1}/{len(times)-1} time={float(times[step+1]):.9g}", flush=True)
        metadata["status"] = "no_failure_observed"
    except CapturedStop:
        pass
    except Exception:
        try:
            stop(None, "diagnostic operation raised", exception_trace=traceback.format_exc())
        except CapturedStop:
            pass
    finally:
        source_gaussian._source_step = original_step
        save_metadata()
        log.close()
        print(json.dumps({"run_dir": str(directory), "status": metadata["status"],
                          "elapsed_seconds": metadata["elapsed_seconds"]}), flush=True)
    return 0 if metadata["status"] in ("observed_failure", "no_local_ill_conditioning") else 1


def main() -> int:
    """Select isolated single-thread CPU execution before importing Torch."""
    sequential = os.environ.get("MKL_THREADING_LAYER") == "SEQUENTIAL"
    os.environ["MKL_THREADING_LAYER"] = "SEQUENTIAL"
    os.environ["OMP_NUM_THREADS"] = os.environ["MKL_NUM_THREADS"] = "1"
    interpreter = Path(os.environ.get("CUDA_PYTHON", "C:/anaconda/python.exe"))
    same = os.path.normcase(str(Path(sys.executable).resolve())) == os.path.normcase(str(interpreter.resolve()))
    if not same or not sys.flags.isolated or not sequential:
        return subprocess.run([str(interpreter), "-I", "-B", str(Path(__file__).resolve())],
                              env=os.environ.copy(), check=False).returncode
    sys.path.insert(0, str(ROOT/"src"))
    return diagnose()


if __name__ == "__main__":
    raise SystemExit(main())
