"""Measure a frozen parent budget using square-root source conditioning."""
from __future__ import annotations

import os
from pathlib import Path
import subprocess
import sys

RUN = {
    "activation_root": "docs/research/2026-10-02-renormalization-completion/evidence/activation",
    "model_seed": 20261002, "path_seed": 20261007, "n_paths": 16, "workers": 4,
}
THEORY = {
    "n_agents": [512, 1024], "dimension": 2, "link_scale": .2, "tau": .5,
    "block_size": 16, "horizon": 1., "coarse_steps": 64, "n_probes": 2,
}
NUMERICS = {"device": "cpu", "dtype": "float64", "cpu_threads": 1, "source_backend": "square_root"}
OUTPUT = {"root": str(Path(__file__).resolve().parents[1]/"artifacts/gaussian-continuous-square-root")}


def main() -> int:
    """Bootstrap isolated sequential-MKL execution before any Torch import."""
    sequential = os.environ.get("MKL_THREADING_LAYER") == "SEQUENTIAL"
    os.environ["MKL_THREADING_LAYER"] = "SEQUENTIAL"
    os.environ["OMP_NUM_THREADS"] = os.environ["MKL_NUM_THREADS"] = "1"
    interpreter = Path(os.environ.get("CUDA_PYTHON", "C:/anaconda/python.exe"))
    same = os.path.normcase(str(Path(sys.executable).resolve())) == os.path.normcase(str(interpreter.resolve()))
    if not same or not sys.flags.isolated or not sequential:
        return subprocess.run([str(interpreter), "-I", "-B", str(Path(__file__).resolve())],
                              env=os.environ.copy(), check=False).returncode
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"src"))
    from multiagent_elbo.realizations.gaussian.continuous_budget_experiment import run_frozen_budget_study
    run_frozen_budget_study(RUN, THEORY, NUMERICS, OUTPUT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
