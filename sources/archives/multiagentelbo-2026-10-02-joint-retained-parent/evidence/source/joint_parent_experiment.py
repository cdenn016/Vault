"""One finite-grid study of joint retained switching paths."""
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

from .coupled_learning import CoupledState
from .coupled_learning_experiment import build_coupled_case
from .joint_parent import joint_row_scores
from .locality import block_mean_projector
from .switching_paths import all_sheet_curvature_bound, sample_switching_history


def _estimate(values: np.ndarray) -> dict[str, float]:
    """Report a sample mean and empirical standard error, not a confidence bound."""
    return {"mean": float(values.mean()), "standard_error": float(values.std(ddof=1)/len(values)**.5)}


def run_joint_parent_study(run: dict, theory: dict, numerics: dict, output: dict) -> dict:
    """Execute the fixed profile and preserve failed results without a retry."""
    if numerics["device"] != "cpu" or numerics["dtype"] != "float64":
        raise ValueError("the declared study uses CPU float64")
    torch.set_num_threads(numerics["cpu_threads"])
    root = Path(__file__).resolve().parents[4]
    directory = Path(output["root"])/datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    directory.mkdir(parents=True)
    (directory/"source").mkdir()
    sources = ["src/multiagent_elbo/realizations/gaussian/"+name+".py" for name in (
        "joint_parent", "joint_parent_experiment", "switching_paths", "coupled_learning",
        "coupled_learning_experiment", "network", "network_experiment", "network_dynamics",
        "locality", "predictive_interfaces")]+["experiments/gaussian_joint_parent.py"]
    hashes = {}
    for relative in sources:
        hashes[relative] = hashlib.sha256((root/relative).read_bytes()).hexdigest()
        shutil.copyfile(root/relative, directory/"source"/Path(relative).name)
    metadata = {"run": run, "theory": theory, "numerics": numerics,
        "status": "running", "cases": [], "python": sys.executable,
        "python_version": platform.python_version(), "torch": torch.__version__,
        "cuda_available": torch.cuda.is_available(), "source_sha256_diagnostic": hashes,
        "input_sha256_diagnostic": {},
        "base_head": subprocess.check_output(["git","rev-parse","HEAD"],cwd=root,text=True).strip(),
        "working_status": subprocess.check_output(["git","status","--short"],cwd=root,text=True)}
    def save() -> None:
        """Retain completed cases and any failure diagnostic."""
        (directory/"metadata.json").write_text(json.dumps(metadata,indent=2),encoding="utf-8")
    save()
    started = time.perf_counter()
    try:
        for N in theory["n_agents"]:
            case_started = time.perf_counter()
            input_paths = [root/run["activation_root"]/f"N{N}-learn_both-final.npz",
                           root/run["schedule_root"]/f"N{N}-learn_both-schedule.npz"]
            for path in input_paths:
                metadata["input_sha256_diagnostic"][str(path.relative_to(root))] = hashlib.sha256(path.read_bytes()).hexdigest()
            with np.load(input_paths[0]) as arrays:
                initial = CoupledState(**{name: torch.from_numpy(arrays[name].copy())
                    for name in ("mu","Sigma","pi","Theta")})
            with np.load(input_paths[1]) as arrays:
                schedule = tuple(CoupledState(**{name: torch.from_numpy(arrays[name][t].copy())
                    for name in ("mu","Sigma","pi","Theta")}) for t in range(theory["intervals"]))
            for name in ("mu","Sigma","pi","Theta"):
                torch.testing.assert_close(getattr(initial,name),getattr(schedule[0],name),atol=0.,rtol=0.)
            model, _ = build_coupled_case(N,theory["dimension"],run["model_seed"],theory["link_scale"])
            model = replace(model,tau=theory["tau"])
            mobility = initial.Sigma
            dt = theory["interval_dt"]/run["substeps"]
            curvature = max(all_sheet_curvature_bound(mobility,s.Theta,model) for s in schedule)
            if dt*curvature > 1:
                raise ArithmeticError("microstep fails the all-assignment curvature condition")
            fine_schedule = tuple(s for s in schedule for _ in range(run["substeps"]))
            projections = {b: block_mean_projector(N,theory["dimension"],b) for b in theory["blocks"]}
            first = theory["blocks"][0]
            composition = {str(b): float((P-block_mean_projector(N//first,theory["dimension"],b//first)@projections[first]).abs().max())
                           for b,P in projections.items()}
            if max(composition.values()) > 1e-13:
                raise ArithmeticError("nested projections do not compose")
            chunks = {}
            def retain(name: str, values: np.ndarray) -> None:
                """Append independent trajectory batches in their declared order."""
                chunks.setdefault(name,[]).append(values)
            seeds = []
            with torch.no_grad():
                for batch,start in enumerate(range(0,run["n_paths"],run["batch_size"])):
                    count = min(run["batch_size"],run["n_paths"]-start)
                    seed = run["path_seed"]+batch
                    seeds.append(seed)
                    history = sample_switching_history(mobility,initial,fine_schedule,model,dt,count,seed,
                                                       refresh_rate=theory["refresh_rate"])
                    retain("assignments",history.assignments.numpy().astype(np.int16))
                    retain("log_source_kernel",history.log_source_kernel.numpy())
                    retain("fine_costs",history.fine_costs.numpy())
                    for block,P in projections.items():
                        retain(f"block{block}_paths",(history.paths.flatten(2)@P.T).numpy())
                        scores = joint_row_scores(history,P,mobility,initial,fine_schedule,model,dt,
                                                  refresh_rate=theory["refresh_rate"])
                        for name,values in scores.items():
                            if not bool(torch.isfinite(values).all()):
                                raise FloatingPointError("nonfinite joint parent score")
                            retain(f"block{block}_{name}",values.numpy())
                    del history
                    print(f"N={N}: retained and scored {start+count}/{run['n_paths']} paths; {time.perf_counter()-case_started:.1f}s",flush=True)
            arrays = {name: np.concatenate(values) for name,values in chunks.items()}
            case = {"n_agents":N,"microsteps":len(fine_schedule),"micro_dt":dt,
                "all_sheet_curvature_upper":curvature,"microstep_curvature_product":dt*curvature,
                "batch_seeds":seeds,"composition_max_error":composition,"levels":[]}
            for block,P in projections.items():
                parts = {name:arrays[f"block{block}_{name}"] for name in (
                    "source_reference","source_lifted","drift_reference","drift_assignment")}
                level = {"block":block,"configuration_dimension":len(P),"retained_assignments":N,
                         "components":{name:_estimate(value) for name,value in parts.items()},"parents":{}}
                for source in ("reference","lifted"):
                    for drift in ("reference","assignment"):
                        values = parts["source_"+source]+parts["drift_"+drift]
                        name = source+"_source_"+drift+"_drift"
                        arrays[f"block{block}_{name}"] = values
                        level["parents"][name] = _estimate(values)
                source_delta = parts["source_lifted"]-parts["source_reference"]
                drift_delta = parts["drift_assignment"]-parts["drift_reference"]
                level["paired_lifted_minus_reference_source"] = _estimate(source_delta)
                level["paired_assignment_minus_reference_drift"] = _estimate(drift_delta)
                level["paired_both_minus_neither"] = _estimate(source_delta+drift_delta)
                case["levels"].append(level)
            np.savez_compressed(directory/f"N{N}-joint-paths-and-scores.npz",**arrays)
            case["elapsed_seconds"] = time.perf_counter()-case_started
            metadata["cases"].append(case)
            (directory/f"N{N}.json").write_text(json.dumps(case,indent=2),encoding="utf-8")
            save()
            del arrays,chunks
        metadata["status"] = "pass"
    except Exception:
        metadata["status"] = "failed"
        metadata["traceback"] = traceback.format_exc()
        raise
    finally:
        metadata["elapsed_seconds"] = time.perf_counter()-started
        save()
        print(json.dumps({"run_dir":str(directory),"status":metadata["status"],
                          "elapsed_seconds":metadata["elapsed_seconds"]}),flush=True)
    return metadata
