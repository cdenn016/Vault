r"""Extract the stored content-link factors (T, O) of the K=20 chart runs into trained_links_K20.npz.

One-time provenance step for trained_link_geometry.py (which reads only the .npz). It reads every
map snapshot ``map_snapshots/step_*.pt`` of the four October 3, 2026 runs (2 layers, H=2 heads of
d=10, K=20) and stores, per run tag, the snapshot steps and the float32 factors exactly as saved:

    <tag>_steps  (S,)              int64
    <tag>_T      (S, L, H, d, K)   float32   stored sending maps
    <tag>_O      (S, L, H, K, d)   float32   stored receiving factors

Layer 0 is ``relational_operators``, layer l >= 1 is ``relational_operators_extra.{l-1}``. Usage:

    python extract_trained_links.py [RUNS_ROOT]

with RUNS_ROOT the folder holding the run directories (default D:/DATA_KEEP/10-3-2026_Experiments,
originally VFE_3.0/vfe3_runs/10-3-2026_Experiments). Needs torch only to read the snapshots.
"""
import glob
import os
import sys

import numpy as np
import torch

ROOT = sys.argv[1] if len(sys.argv) > 1 else "D:/DATA_KEEP/10-3-2026_Experiments"
RUNS = [("affine", "121.77_wikitext-103_K20_affine"),
        ("first_order", "121.98_wikitext-103_K20_first-order"),
        ("exponential", "121.53_wikitext-103_K20_exponential"),
        ("exponential_receiver", "124.93_wikitext-103_K20_exponential_gradient")]


def flat(d: dict, pre: str = "") -> dict:
    out = {}
    for k, v in d.items():
        out.update(flat(v, pre + k + ".") if isinstance(v, dict) else {pre + k: v})
    return out


def layers(state: dict) -> list:
    found = [(state["relational_operators.T"], state["relational_operators.O"])]
    i = 0
    while f"relational_operators_extra.{i}.T" in state:
        found.append((state[f"relational_operators_extra.{i}.T"], state[f"relational_operators_extra.{i}.O"]))
        i += 1
    return found


arrays = {}
for tag, run in RUNS:
    steps, Ts, Os = [], [], []
    for path in sorted(glob.glob(os.path.join(ROOT, run, "map_snapshots", "step_*.pt"))):
        snap = torch.load(path, map_location="cpu", weights_only=True)
        found = layers(flat(snap["state"]))
        steps.append(int(snap["step"]))
        Ts.append(np.stack([T.numpy() for T, _ in found]))
        Os.append(np.stack([O.numpy() for _, O in found]))
    if not steps or steps[-1] != 15000:
        raise SystemExit(f"{run}: expected snapshots through step 15000, found {steps}")
    arrays[f"{tag}_steps"] = np.array(steps, dtype=np.int64)
    arrays[f"{tag}_T"] = np.stack(Ts)
    arrays[f"{tag}_O"] = np.stack(Os)
    print(tag, run, arrays[f"{tag}_T"].shape, arrays[f"{tag}_O"].shape, arrays[f"{tag}_T"].dtype)

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "trained_links_K20.npz")
np.savez_compressed(out, **arrays)
print("wrote", out)
