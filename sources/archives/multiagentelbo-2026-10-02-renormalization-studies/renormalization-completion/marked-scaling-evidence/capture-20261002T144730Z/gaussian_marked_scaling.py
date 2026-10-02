"""Predeclared CPU study; execute only after the parent authorizes the large run."""
from __future__ import annotations
import os
for _name in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[_name] = "1"
os.environ["MKL_THREADING_LAYER"] = "SEQUENTIAL"

from datetime import datetime, timezone
import json
from pathlib import Path
import sys
from time import perf_counter
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

RUN = {"seed": 20261002, "name": "massive-marked-gaussian-diagonal"}
THEORY = {"n_agents": [512, 1024, 2048, 4096, 8192], "mass": 2.0,
          "kappa": 0.3, "gamma": 0.2, "eta": 0.4, "amplitude": 0.05}
NUMERICS = {"padding_cells": 64, "neumann_degree": 63, "upper": 5.5, "tolerance": 1e-10}
OBSERVABLE = {"fixed_depth_block_cells": 16, "covector": [1.0, -0.5, 0.25, 1.0, -0.75, 0.5]}
OUTPUT = {"root": "docs/research/2026-10-02-renormalization-completion/marked-scaling-evidence"}


def main() -> int:
    """Run one coupled-environment diagonal and retain its raw Gaussian/mark arrays."""
    import numpy as np
    import scipy
    from scipy import sparse
    from threadpoolctl import threadpool_info, threadpool_limits
    from multiagent_elbo.realizations.gaussian.marked_gaussian_scaling import (
        block_map, build_precision, cell_map, draw_environment, initial_marks,
        padded_covariance_bound, push_marks, solve_pair, susceptibility_reference,
    )
    repository = Path(__file__).resolve().parents[1]
    out = repository / OUTPUT["root"] / datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out.mkdir(parents=True, exist_ok=False)
    start = perf_counter()
    pad, maximum = NUMERICS["padding_cells"], max(THEORY["n_agents"])//2
    A, B = draw_environment(maximum+2*pad, RUN["seed"], THEORY["amplitude"])
    parameters = {k: THEORY[k] for k in ("mass", "kappa", "gamma", "eta")}
    results = []
    previous_fixed, previous_bound = None, None
    covector = np.asarray(OBSERVABLE["covector"])
    with threadpool_limits(limits=1):
        Hmax = build_precision(A, B, **parameters)
        chi, chi_tail = susceptibility_reference(Hmax, THEORY["mass"], NUMERICS["upper"], maximum, pad,
                                                  NUMERICS["neumann_degree"])
        characteristic_proxy = float(np.exp(-0.5*covector @ np.kron(np.eye(3), chi) @ covector))
        np.savez_compressed(out/"environment.npz", A=A, B=B, empirical_susceptibility=chi)
        for agents in THEORY["n_agents"]:
            cells = agents//2
            depth = int(np.log2(cells))//2
            ratio = 2**depth
            frames = np.tile(np.eye(2), (cells, 1, 1))
            H = build_precision(A[:cells+2*pad], B[:cells+2*pad], **parameters)
            initial = cell_map(cells, pad)
            direct = block_map(frames, ratio)
            staged = sparse.eye(2*cells, format="csr")
            marks = initial_marks(A[pad:pad+cells], B[pad:pad+cells], frames)
            staged_marks, current_frames = marks, frames
            for _ in range(depth):
                staged = block_map(current_frames, 2) @ staged
                staged_marks = push_marks(staged_marks, current_frames, 2)
                current_frames = current_frames[::2]
            direct_marks = push_marks(marks, frames, ratio)
            pair, residual = solve_pair(H, direct @ initial, np.zeros(H.shape[0]), THEORY["mass"])
            staged_pair, staged_residual = solve_pair(H, staged @ initial, np.zeros(H.shape[0]), THEORY["mass"])
            errors = [np.max(np.abs(pair.covariance-staged_pair.covariance)),
                      abs(pair.offset-staged_pair.offset), abs(pair.relative_offset-staged_pair.relative_offset),
                      np.max(np.abs(pair.reference_covariance-staged_pair.reference_covariance))]
            mark_error = max(float(np.max(np.abs(a-b))) for a, b in zip(direct_marks, staged_marks))
            first = pair.covariance[:6, :6]
            fixed_map = block_map(frames, OBSERVABLE["fixed_depth_block_cells"])[:6] @ initial
            fixed_pair, fixed_residual = solve_pair(H, fixed_map, np.zeros(H.shape[0]), THEORY["mass"])
            fixed_error = None if previous_fixed is None else float(np.max(np.abs(fixed_pair.covariance-previous_fixed)))
            characteristic = float(np.exp(-0.5*covector @ first @ covector))
            diagonal = [float(np.linalg.norm(first[2*i:2*i+2, 2*i:2*i+2]-chi, 2)) for i in range(3)]
            off = [float(np.linalg.norm(first[2*i:2*i+2, 2*j:2*j+2], 2)) for i, j in ((0, 1), (1, 2), (0, 2))]
            bound = padded_covariance_bound(THEORY["mass"], NUMERICS["upper"], pad)
            q = 1-THEORY["mass"]/NUMERICS["upper"]
            cross_bound = q/(THEORY["mass"]*(1-q)**2*ratio)+bound
            gates = {"solve_residual": max(residual, staged_residual, fixed_residual) < NUMERICS["tolerance"],
                     "direct_staged": max(errors) < NUMERICS["tolerance"],
                     "all_marks": mark_error < NUMERICS["tolerance"],
                     "positive": float(np.linalg.eigvalsh(pair.covariance).min()) > 0,
                     "cross_bound": max(off) <= cross_bound+NUMERICS["tolerance"]}
            fixed_bound = None if previous_bound is None else bound+previous_bound
            if fixed_error is not None:
                gates["fixed_depth_consistency"] = fixed_error <= fixed_bound+NUMERICS["tolerance"]
            np.savez_compressed(out/f"N{agents}.npz", mean=pair.mean, covariance=pair.covariance,
                reference_covariance=pair.reference_covariance, first_three_cells=first,
                fixed_depth_first_three_covariance=fixed_pair.covariance, observable_covector=covector,
                mark_source=direct_marks[0], mark_destination=direct_marks[1],
                mark_origin_id=np.arange(len(direct_marks[0])),
                mark_values_belief=direct_marks[2], mark_values_model=direct_marks[2])
            results.append({"n_agents": agents, "cells": cells, "depth": depth, "block_cells": ratio,
                "retained_cells": cells//ratio, "retained_marks_per_channel": len(direct_marks[0]),
                "both_channels": "independent identical Gaussian copies; identity cross morphisms",
                "padded_raw_log_mass_per_channel": pair.log_mass, "relative_offset": pair.relative_offset,
                "model_offset": pair.offset, "solve_residual": max(residual, staged_residual, fixed_residual),
                "fixed_depth_solve_residual": fixed_residual,
                "direct_staged_errors": [float(e) for e in errors], "mark_error": mark_error,
                "first_three_diagonal_errors_to_empirical_reference": diagonal,
                "first_three_cross_covariance_norms": off, "cross_covariance_bound": cross_bound,
                "fixed_depth_block_cells": OBSERVABLE["fixed_depth_block_cells"],
                "fixed_depth_adjacent_size_maxnorm": fixed_error, "fixed_depth_sum_padding_bounds": fixed_bound,
                "characteristic_observable": characteristic,
                "characteristic_error_to_empirical_proxy": abs(characteristic-characteristic_proxy),
                "exact_arithmetic_padding_bound": bound, "gates": gates})
            previous_fixed, previous_bound = fixed_pair.covariance, bound
        pools = threadpool_info()
    payload = {"run": RUN, "theory": THEORY, "numerics": NUMERICS, "observable": OBSERVABLE, "results": results,
        "reference": {"empirical_susceptibility": chi.tolist(), "deterministic_neumann_tail": chi_tail,
        "characteristic_empirical_proxy": characteristic_proxy,
        "scope": "one finite iid environment average; no confidence interval for infinite-environment expectation"},
        "environment": {"python": sys.version, "executable": sys.executable,
                        "numpy": np.__version__, "scipy": scipy.__version__, "threadpools": pools},
        "elapsed_seconds": perf_counter()-start, "passed": all(all(r["gates"].values()) for r in results)}
    (out/"summary.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(json.dumps({"output": str(out), "passed": payload["passed"], "elapsed_seconds": payload["elapsed_seconds"]}))
    return 0 if payload["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

