"""Editable held-link network baseline; run this file directly without changing run_lab.py."""
from __future__ import annotations

import os
from pathlib import Path
import subprocess
import sys

RUN = {"name": "pointwise-held-gaussian-network", "seed": 20260930}

THEORY = {
    "experiment": "pointwise_gaussian_network",
    "n_agents": 512,
    "dimension": 2,  # Real dimension for GL(R); complex dimension for GL(C) and SU.
    "cases": ["flat_real_gl", "independent_real_gl", "matrix", "complex_gl", "su"],
    "link_scale": 0.2,
}

NUMERICS = {
    "device": "cpu",  # CUDA is opt-in; run it only while the device is idle.
    "dtype": "float64",
    "cpu_threads": 1,
    "atol": 1e-9,
    "rtol": 1e-9,
}

OUTPUT = {"root": "artifacts", "save_arrays": True}


def main() -> int:
    """Select the CUDA-capable interpreter before importing torch on either lane."""
    interpreter = Path(os.environ.get("CUDA_PYTHON", "C:/anaconda/python.exe"))
    if not interpreter.is_file():
        raise FileNotFoundError(f"Required torch interpreter does not exist: {interpreter}")
    if os.path.normcase(str(Path(sys.executable).resolve())) != os.path.normcase(str(interpreter.resolve())) or not sys.flags.isolated or not sys.flags.dont_write_bytecode:
        environment = os.environ.copy()
        for name in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
            environment[name] = "1"
        completed = subprocess.run(
            [str(interpreter), "-I", "-B", str(Path(__file__).resolve()), *sys.argv[1:]],
            env=environment,
            check=False,
        )
        return completed.returncode
    repository_root = Path(__file__).resolve().parents[1]
    sys.path.insert(0, str(repository_root / "src"))
    from multiagent_elbo.realizations.gaussian.network_experiment import run_gaussian_network_experiment

    run_gaussian_network_experiment(RUN, THEORY, NUMERICS, OUTPUT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
