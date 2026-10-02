"""Editable finite-temperature coupled source/link learning profile."""
from __future__ import annotations

import os
from pathlib import Path
import subprocess
import sys

RUN = {"name": "gaussian-coupled-learning", "seed": 20261002}
THEORY = {
    "n_agents": [512, 1024], "dimension": 2, "link_scale": .2, "tau": .5,
    "dt": .05, "checkpoints": [1., 2., 3., 4., 5.],
    "belief_rate": 1., "source_rate": .2, "link_rate": .05,
}
NUMERICS = {"device": "cpu", "dtype": "float64", "cpu_threads": 1}
OUTPUT = {"root": str(Path(__file__).resolve().parents[1]/"artifacts/gaussian-coupled-learning")}


def main() -> int:
    """Establish sequential MKL before native imports in the CUDA-capable runtime."""
    sequential = os.environ.get("MKL_THREADING_LAYER") == "SEQUENTIAL"
    os.environ["MKL_THREADING_LAYER"] = "SEQUENTIAL"
    for key in ("OMP_NUM_THREADS", "MKL_NUM_THREADS"):
        os.environ[key] = str(NUMERICS["cpu_threads"])
    interpreter = Path(os.environ.get("CUDA_PYTHON", "C:/anaconda/python.exe"))
    same = os.path.normcase(str(Path(sys.executable).resolve())) == os.path.normcase(str(interpreter.resolve()))
    if not same or not sys.flags.isolated or not sequential:
        return subprocess.run([str(interpreter), "-I", "-B", str(Path(__file__).resolve())],
                              env=os.environ.copy(), check=False).returncode
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"src"))
    from multiagent_elbo.realizations.gaussian.coupled_learning_experiment import run_coupled_learning
    run_coupled_learning(RUN, THEORY, NUMERICS, OUTPUT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
