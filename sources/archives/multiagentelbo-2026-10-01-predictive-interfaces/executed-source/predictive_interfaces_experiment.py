"""Finite X2 study with matched interfaces and actual reduced-state path risk."""
from __future__ import annotations

from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import platform
import subprocess
import sys
import time
from typing import Mapping
import numpy as np
import torch

from .locality import block_mean_projector
from .network import assemble_network
from .network_dynamics import ou_transition
from .network_experiment import build_network_case
from .network_dynamics_experiment import _motion_generator, _moving_source_map
from .predictive_interfaces import (
    compile_predictor, discarded_information, path_budget, predictive_reference, spectral_interface,
)


def run_predictive_interfaces(
    run:      Mapping[str, object],
    theory:   Mapping[str, object],
    numerics: Mapping[str, object],
    output:   Mapping[str, object],
) -> Path:
    """Execute the declared finite study once, preserving a failed run's evidence."""
    started = datetime.now(timezone.utc)
    directory = Path(str(output["root"])) / started.strftime("%Y%m%dT%H%M%S%fZ")
    directory.mkdir(parents=True, exist_ok=False)
    root = Path(__file__).resolve().parents[4]
    source_dir = directory / "source"
    source_dir.mkdir()
    sources = [
        Path(__file__), Path(__file__).with_name("predictive_interfaces.py"),
        Path(__file__).with_name("network_dynamics.py"), Path(__file__).with_name("network_experiment.py"),
        Path(__file__).with_name("network_dynamics_experiment.py"),
        Path(__file__).with_name("network.py"), Path(__file__).with_name("locality.py"),
        root / "experiments/gaussian_predictive_interfaces.py",
    ]
    source_metadata = {}
    for source in sources:
        raw = source.read_bytes()
        (source_dir / source.name).write_bytes(raw)
        source_metadata[str(source.relative_to(root))] = hashlib.sha256(raw).hexdigest()
    metadata = {
        "status": "running", "run": dict(run), "theory": dict(theory), "numerics": dict(numerics),
        "started_utc": started.isoformat(), "python": sys.version, "executable": sys.executable,
        "torch": torch.__version__, "cuda_available": torch.cuda.is_available(), "device_used": "cpu",
        "platform": platform.platform(), "source_sha256_diagnostic": source_metadata,
        "git_head": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip(),
        "working_tree": subprocess.check_output(["git", "status", "--porcelain=v1"], cwd=root, text=True).splitlines(),
        "environment": {k: os.environ.get(k) for k in ("MKL_THREADING_LAYER", "MKL_NUM_THREADS", "OMP_NUM_THREADS")},
    }
    (directory/"result.json").write_text(json.dumps(metadata, indent=2), encoding="utf-8")
    torch.set_num_threads(int(numerics["cpu_threads"]))
    tolerance = float(numerics["tolerance"])
    start = time.perf_counter()
    try:
        for N_value in theory["n_agents"]:
            N = int(N_value)
            for kind_value in theory["cases"]:
                case_start = time.perf_counter()
                kind = str(kind_value)
                print(f"X2 {kind} N={N}", flush=True)
                K, seed = int(theory["dimension"]), int(run["seed"])
                case = build_network_case(kind, N, K, seed, float(theory["link_scale"]))
                action = assemble_network(case.J_0, case.mu_0, case.A_e, case.B_e,
                                          case.Gamma_inv, case.o_e, case.edges)
                mu, Sigma = action.moments()
                mu = mu + .03*torch.cos(torch.arange(len(mu), dtype=mu.dtype))
                Sigma = 1.2*Sigma
                mobility = torch.eye(len(mu), dtype=mu.dtype)
                G = _motion_generator(case.B_e, float(theory["motion_strength"]), N, K, seed, kind)
                kernels = []
                for t in range(int(theory["n_steps"])):
                    B_e = _moving_source_map(case.B_e, G, case.edges, t*float(theory["dt"]), K, kind)
                    held = assemble_network(case.J_0, case.mu_0, case.A_e, B_e,
                                            case.Gamma_inv, case.o_e, case.edges)
                    kernels.append(ou_transition(held.J, held.h, mobility, float(theory["dt"])))
                block = int(theory["block"])
                P = block_mean_projector(N, K, block)
                reference = predictive_reference(mu, Sigma, P, kernels)
                interface = spectral_interface(reference.Sigma_h, reference.C, reference.noise)
                m, hidden = reference.output_dimension, len(reference.Sigma_h)
                finer = block_mean_projector(N, K, block//2).reshape(N//block, 2, K, len(mu))
                contrasts = (finer[:, 0]-finer[:, 1]).reshape(m, len(mu)) @ reference.inverse[:, m:]
                ranks = sorted(set([0]+[max(1, round(float(f)*m)) for f in theory["rank_fractions"]]))
                case_result = {
                    "N": N, "case": kind, "fine_dimension": len(mu), "output_dimension": m,
                    "fine_hidden_dimension": hidden, "nu": interface.nu.tolist(),
                    "activation_information": float(torch.log1p(interface.nu).sum()/2),
                    "rows": [], "map_type": "Gaussian comparison records; edge-copy inverse interpretation is separate",
                }
                arrays = {
                    "P": P.numpy(), "Sigma_h": reference.Sigma_h.numpy(), "C": reference.C.numpy(),
                    "record_noise": reference.noise.numpy(), "nu": interface.nu.numpy(),
                    "actual_path_mu": reference.path_mu.numpy(), "actual_path_Sigma": reference.path_Sigma.numpy(),
                }
                for rank in ranks:
                    spectral_loss = float(torch.log1p(interface.nu[rank:]).sum()/2)
                    controls = {"spectral": interface.W[:rank]}
                    if rank:
                        controls["coordinate"] = torch.eye(hidden, dtype=Sigma.dtype)[:rank]
                        controls["block_contrast"] = contrasts[:rank]
                    for name, W in controls.items():
                        row_start = time.perf_counter()
                        loss = float(discarded_information(reference.Sigma_h, reference.C, reference.noise, W))
                        parent = compile_predictor(reference, W)
                        budget = path_budget(reference.path_mu, reference.path_Sigma, parent)
                        direct = float(budget.direct_kl)
                        memory, risk = float(budget.memory.sum()), float(budget.row_risk.sum())
                        gap = abs(direct-memory-risk)
                        checks = {
                            "spectral_tail": name != "spectral" or abs(loss-spectral_loss) <= tolerance*max(1., abs(loss)),
                            "matched_information": loss + tolerance*max(1., abs(loss)) >= spectral_loss,
                            "path_identity": gap <= tolerance*max(1., abs(direct)),
                            "nonnegative_budget": min(float(budget.memory.min()), float(budget.row_risk.min()), direct) >= -tolerance,
                            "deployed_dimension": parent.initialize(parent.mu_0[:m]).mu_h.numel() == rank,
                        }
                        row = {
                            "rank": rank, "control": name, "discarded_activation_information": loss,
                            "spectral_minimum": spectral_loss, "path_kl": direct, "memory": memory, "row_risk": risk,
                            "memory_by_step": budget.memory.tolist(), "row_risk_by_step": budget.row_risk.tolist(),
                            "path_identity_abs_error": gap, "hidden_mean_coordinates": rank,
                            "hidden_covariance_entries": rank*rank, "compiled_state_dimension": m+rank,
                            "checks": checks, "seconds": time.perf_counter()-row_start,
                        }
                        case_result["rows"].append(row)
                        key = f"{name}_r{rank}"
                        arrays[key+"_W"] = W.numpy()
                        arrays[key+"_mu0"] = parent.mu_0.numpy()
                        arrays[key+"_Sigma0"] = parent.Sigma_0.numpy()
                        for t, kernel in enumerate(parent.kernels):
                            for field in ("F", "u", "Q"):
                                arrays[f"{key}_{field}_{t}"] = getattr(kernel, field).numpy()
                        if not all(checks.values()):
                            (directory/f"{kind}-N{N}.json").write_text(json.dumps(case_result, indent=2), encoding="utf-8")
                            raise ArithmeticError(f"X2 comparison failed at {kind} N={N} {name} r={rank}")
                        print(f"  {name} r={rank} info_tail={loss:.6g} path={direct:.6g} memory={memory:.6g} row={risk:.6g}", flush=True)
                case_result["seconds"] = time.perf_counter()-case_start
                (directory/f"{kind}-N{N}.json").write_text(json.dumps(case_result, indent=2), encoding="utf-8")
                np.savez_compressed(directory/f"{kind}-N{N}.npz", **arrays)
        metadata["status"] = "pass"
    except Exception as exc:
        metadata["status"], metadata["error"] = "failed", repr(exc)
        raise
    finally:
        metadata["total_seconds"] = time.perf_counter()-start
        metadata["finished_utc"] = datetime.now(timezone.utc).isoformat()
        (directory/"result.json").write_text(json.dumps(metadata, indent=2), encoding="utf-8")
        print(f"Evidence: {directory}", flush=True)
    return directory
