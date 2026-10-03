"""Evaluate one published source operation with the hidden-factor candidate."""
from __future__ import annotations

import os
from pathlib import Path
import sys

os.environ["MKL_THREADING_LAYER"] = "SEQUENTIAL"
os.environ["OMP_NUM_THREADS"] = os.environ["MKL_NUM_THREADS"] = "1"
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/"src"))


def main() -> None:
    """Run the declared single-operation comparison; preserve failures."""
    from datetime import datetime, timezone
    from math import sqrt
    import json
    import time
    import traceback
    import zipfile
    import numpy as np
    import torch
    from multiagent_elbo.realizations.gaussian.source_square_root import condition_hidden_factor

    torch.set_num_threads(1)
    phase = ROOT/"docs/research/2026-10-02-renormalization-completion"
    source = phase/"covariance-diagnostic-evidence/20261003T025107540279Z"
    out = ROOT/"artifacts/gaussian-square-root-capture"/datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    out.mkdir(parents=True, exist_ok=False)
    start = time.perf_counter()
    result = {"status": "running", "scope": "one captured receiver293 operation, no trajectory", "source": str(source),
              "python": sys.executable, "torch": torch.__version__, "device": "cpu", "dtype": "float64", "cpu_threads": 1}
    sources = [Path(__file__), ROOT/"src/multiagent_elbo/realizations/gaussian/source_square_root.py",
               phase/"covariance-square-root-CONTRACT.md"]
    with zipfile.ZipFile(out/"source.zip", "x", zipfile.ZIP_DEFLATED) as archive:
        for path in sources:
            archive.writestr(path.relative_to(ROOT).as_posix(), path.read_bytes())
    try:
        with np.load(source/"capture.npz") as data:
            mu, covariance, expected_mu, expected_covariance = [torch.from_numpy(data[key].copy()) for key in
                ("input_mean", "input_covariance", "output_mean", "output_covariance")]
        with np.load(source/"local-moments.npz") as data:
            L, weights, coordinates = [torch.from_numpy(data[key].copy()) for key in ("L", "weights", "coordinates")]
        independent = torch.arange(2048).reshape(64, 16, 2)[:, :15].flatten()
        local_rows = torch.zeros((6, 1920), dtype=torch.float64)
        for row, coordinate in enumerate(coordinates):
            where = (independent == coordinate).nonzero(as_tuple=True)[0]
            if len(where) != 1:
                raise ValueError("this capture requires six directly retained independent coordinates")
            local_rows[row, where[0]] = 1.
        factor = torch.linalg.cholesky(covariance[:, independent][:, :, independent])
        offsets = sqrt(6)*torch.cat((L.mT, -L.mT), dim=1)
        shift = torch.einsum("bq,bqr->br", weights, offsets)
        centered = offsets-shift[:, None]
        weighted = centered*weights.sqrt()[..., None]
        _, upper = torch.linalg.qr(weighted, mode="reduced")
        signs = upper.diagonal(dim1=-2, dim2=-1).sign()
        tilted_factor = (signs[..., None]*upper).mT
        def lift(value: torch.Tensor) -> torch.Tensor:
            """Lift h-dimensional factors into the arithmetic observed fiber."""
            blocks = value.reshape(1, 64, 15, 2, -1)
            return torch.cat((blocks, -blocks.sum(2, keepdim=True)), dim=2).reshape(1, 2048, -1)
        with torch.no_grad():
            initial_physical_factor = lift(factor)
            result["incoming_covariance_reconstruction_error"] = float((initial_physical_factor@initial_physical_factor.mT-covariance).abs().max())
            displacement, updated = condition_hidden_factor(factor, local_rows, shift, tilted_factor)
            physical_factor = lift(updated)
            actual_covariance = physical_factor@physical_factor.mT
            actual_mu = mu+lift(displacement[..., None]).reshape_as(mu)
            local_factor = physical_factor[:, coordinates]
            singular = torch.linalg.svdvals(local_factor)[0]
            result.update(status="comparison_completed", mean_error=float((actual_mu-expected_mu).abs().max()),
                covariance_error=float((actual_covariance-expected_covariance).abs().max()),
                covariance_fiber_max=float(actual_covariance.reshape(1, 64, 16, 2, 2048).mean(2).abs().max()),
                local_factor_minimum_squared=float(singular[-1]**2), local_factor_maximum_squared=float(singular[0]**2),
                local_covariance_error=float((actual_covariance[:, coordinates][:, :, coordinates]-expected_covariance[:, coordinates][:, :, coordinates]).abs().max()))
            np.savez_compressed(out/"updated-factor.npz", factor=updated.numpy(), mean=actual_mu.numpy(), local_factor=local_factor.numpy())
    except Exception:
        result.update(status="failed", traceback=traceback.format_exc())
        raise
    finally:
        result["elapsed_seconds"] = time.perf_counter()-start
        (out/"result.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
        print(json.dumps({"run_directory": str(out), **result}), flush=True)


if __name__ == "__main__":
    main()
