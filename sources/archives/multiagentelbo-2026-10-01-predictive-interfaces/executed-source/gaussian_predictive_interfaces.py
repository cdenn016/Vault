"""Editable X2 profile: predictive hidden modes and reduced-state path loss."""
from __future__ import annotations

import os
from pathlib import Path
import subprocess
import sys

RUN = {"name": "gaussian-predictive-interfaces", "seed": 20261001}
THEORY = {
    "n_agents": [512, 1024],
    "cases": ["flat_real_gl", "independent_real_gl"],
    "dimension": 2, "link_scale": .2, "motion_strength": .1,
    "n_steps": 4, "dt": .15, "block": 16,
    "rank_fractions": [.25, .5, 1.],
}
NUMERICS = {"device": "cpu", "dtype": "float64", "cpu_threads": 12, "tolerance": 1e-8}
OUTPUT = {"root": str(Path(__file__).resolve().parents[1]/"artifacts/gaussian-predictive-interfaces")}


def main() -> int:
    """Select sequential MKL before native imports in the isolated CUDA-capable Python."""
    sequential_at_entry = os.environ.get("MKL_THREADING_LAYER") == "SEQUENTIAL"
    os.environ["MKL_THREADING_LAYER"] = "SEQUENTIAL"
    for name in ("OMP_NUM_THREADS", "MKL_NUM_THREADS"):
        os.environ[name] = str(NUMERICS["cpu_threads"])
    interpreter = Path(os.environ.get("CUDA_PYTHON", "C:/anaconda/python.exe"))
    same = os.path.normcase(str(Path(sys.executable).resolve())) == os.path.normcase(str(interpreter.resolve()))
    if not same or not sys.flags.isolated or not sequential_at_entry:
        return subprocess.run([str(interpreter), "-I", "-B", str(Path(__file__).resolve())],
                              env=os.environ.copy(), check=False).returncode
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"src"))
    from multiagent_elbo.realizations.gaussian.predictive_interfaces_experiment import run_predictive_interfaces

    run_predictive_interfaces(RUN, THEORY, NUMERICS, OUTPUT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
