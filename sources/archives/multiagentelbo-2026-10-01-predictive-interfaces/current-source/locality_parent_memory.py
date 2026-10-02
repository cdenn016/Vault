"""Editable X3 profile: block-parent memory across source-prior locality; run directly."""
from __future__ import annotations

import os
from pathlib import Path
import subprocess
import sys

RUN = {"name": "locality-parent-memory", "seed": 20260930}

_GL2, _ID = "gl2", "identity"
THEORY = {
    "n_agents": [64, 128, 256, 512, 1024, 2048],
    "dimension": 2,          # fiber dimension K
    "link_sigma": 0.2,       # Omega_ij = exp(0.2 G_ij), independent GL+(2,R)
    "a": 0.05,               # on-site prior precision
    "kappa": 1.0,            # record precision scale; record i<-j has kappa pi_ij I
    "dt": 0.5,               # sampling interval of the held OU
    "block": 16,             # contiguous block-mean parent
    "horizon": 50,           # sampled times Z_0..Z_{H-1}
    "k_max": 5,
    "cases": [
        {"name": "window_R4", "family": "window", "prior": {"radius": 4}, "links": _GL2, "dynamics": "joint_descent"},
        {"name": "exponential_m0.5", "family": "exponential", "prior": {"decay": 0.5}, "links": _GL2, "dynamics": "joint_descent"},
        {"name": "power_a1", "family": "power", "prior": {"alpha": 1.0}, "links": _GL2, "dynamics": "joint_descent"},
        {"name": "power_a2", "family": "power", "prior": {"alpha": 2.0}, "links": _GL2, "dynamics": "joint_descent"},
        {"name": "complete", "family": "complete", "links": _GL2, "dynamics": "joint_descent"},
        {"name": "directed_R4_joint", "family": "directed_window", "prior": {"radius": 4}, "links": _GL2, "dynamics": "joint_descent"},
        {"name": "directed_R4_row_only", "family": "directed_window", "prior": {"radius": 4}, "links": _GL2, "dynamics": "row_only"},
        {"name": "id_window_R4", "family": "window", "prior": {"radius": 4}, "links": _ID, "dynamics": "joint_descent"},
        {"name": "id_power_a1", "family": "power", "prior": {"alpha": 1.0}, "links": _ID, "dynamics": "joint_descent"},
        {"name": "id_complete", "family": "complete", "links": _ID, "dynamics": "joint_descent"},
    ],
}

NUMERICS = {"device": "cpu", "dtype": "float64", "cpu_threads": 12, "identity_gate_max_N": 256, "filter_check_max_N": 64,
            "stable_kl_max_N": 1024, "analytic_zero_floor": 1e-12}

OUTPUT = {"root": str(Path(__file__).resolve().parents[1] / "docs/research/2026-09-30-locality-parent-memory/evidence/study")}


def main() -> int:
    """Re-launch under the torch interpreter, isolated, with sequential MKL selected before native imports."""
    sequential_at_entry = os.environ.get("MKL_THREADING_LAYER") == "SEQUENTIAL"
    os.environ["MKL_THREADING_LAYER"] = "SEQUENTIAL"
    for name in ("OMP_NUM_THREADS", "MKL_NUM_THREADS"):
        os.environ[name] = str(NUMERICS["cpu_threads"])
    interpreter = Path(os.environ.get("CUDA_PYTHON", "C:/anaconda/python.exe"))
    same = os.path.normcase(str(Path(sys.executable).resolve())) == os.path.normcase(str(interpreter.resolve()))
    if not same or not sys.flags.isolated or not sequential_at_entry:
        return subprocess.run([str(interpreter), "-I", "-B", str(Path(__file__).resolve()), *sys.argv[1:]],
                              env=os.environ.copy(), check=False).returncode
    sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
    from multiagent_elbo.realizations.gaussian.locality_experiment import run_locality_parent_memory

    run_locality_parent_memory(RUN, THEORY, NUMERICS, OUTPUT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
