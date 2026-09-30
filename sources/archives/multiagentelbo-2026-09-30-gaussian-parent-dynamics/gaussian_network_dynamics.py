"""Editable observed-link path reference; run directly without changing existing profiles."""
from __future__ import annotations

import os
from pathlib import Path
import subprocess
import sys

RUN = {"name": "pointwise-observed-gaussian-network-dynamics", "seed": 20260930}

THEORY = {
    "experiment": "pointwise_gaussian_network_dynamics",
    "n_agents": 512,
    "dimension": 2,
    "cases": ["flat_real_gl", "independent_real_gl", "matrix", "complex_gl", "su"],
    "link_scale": 0.2,
    "motion_strength": 0.1,
    "n_steps": 3,
    "dt": 0.2,
}

NUMERICS = {
    "device": "cpu",  # CUDA is opt-in and requires an idle device.
    "dtype": "float64",
    "cpu_threads": 1,
    "atol": 1e-8,
    "rtol": 1e-8,
}

OUTPUT = {"root": "artifacts", "save_arrays": True}


def main() -> int:
    """Choose the CUDA-capable interpreter before importing torch on either lane."""
    os.environ.setdefault("MKL_THREADING_LAYER", "SEQUENTIAL")
    for name in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
        os.environ[name] = "1"
    interpreter = Path(os.environ.get("CUDA_PYTHON", "C:/anaconda/python.exe"))
    if not interpreter.is_file():
        raise FileNotFoundError(f"Required torch interpreter does not exist: {interpreter}")
    matching_interpreter = os.path.normcase(str(Path(sys.executable).resolve())) == os.path.normcase(str(interpreter.resolve()))
    if not matching_interpreter or not sys.flags.isolated or not sys.flags.dont_write_bytecode:
        environment = os.environ.copy()

        completed = subprocess.run(
            [str(interpreter), "-I", "-B", str(Path(__file__).resolve()), *sys.argv[1:]],
            env=environment,
            check=False,
        )
        return completed.returncode
    sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
    from multiagent_elbo.realizations.gaussian.network_dynamics_experiment import run_gaussian_network_dynamics_experiment

    run_gaussian_network_dynamics_experiment(RUN, THEORY, NUMERICS, OUTPUT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
