"""Joint source-assignment/configuration parents on the saved learned schedule."""
from __future__ import annotations
import os
from pathlib import Path
import subprocess
import sys

RUN = {"model_seed":20261002,"path_seed":20261004,"n_paths":1024,"batch_size":128,"substeps":8,
    "activation_root":"docs/research/2026-10-02-renormalization-completion/evidence/activation",
    "schedule_root":"docs/research/2026-10-02-renormalization-completion/evidence/switching-schedules"}
THEORY = {"n_agents":[512,1024],"dimension":2,"link_scale":.2,"tau":.5,
    "interval_dt":.125,"intervals":8,"refresh_rate":1.,"blocks":[16,32,64]}
NUMERICS = {"device":"cpu","dtype":"float64","cpu_threads":1}
OUTPUT = {"root":str(Path(__file__).resolve().parents[1]/"artifacts/gaussian-joint-parent")}


def main() -> int:
    """Select the CUDA-capable installation while keeping this study on CPU."""
    sequential = os.environ.get("MKL_THREADING_LAYER") == "SEQUENTIAL"
    os.environ["MKL_THREADING_LAYER"] = "SEQUENTIAL"
    for key in ("OMP_NUM_THREADS","MKL_NUM_THREADS"):
        os.environ[key] = str(NUMERICS["cpu_threads"])
    interpreter = Path(os.environ.get("CUDA_PYTHON","C:/anaconda/python.exe"))
    same = os.path.normcase(str(Path(sys.executable).resolve())) == os.path.normcase(str(interpreter.resolve()))
    if not same or not sys.flags.isolated or not sequential:
        return subprocess.run([str(interpreter),"-I","-B",str(Path(__file__).resolve())],
                              env=os.environ.copy(),check=False).returncode
    sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"src"))
    from multiagent_elbo.realizations.gaussian.joint_parent_experiment import run_joint_parent_study
    run_joint_parent_study(RUN,THEORY,NUMERICS,OUTPUT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
