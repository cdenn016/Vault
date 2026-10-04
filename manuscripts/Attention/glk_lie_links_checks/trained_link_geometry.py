r"""Geometry of the trained content links of the October 3, 2026 chart runs (CPU, float64).

Reads the stored factors (T, O) from the saved map snapshots and final weights of the K=20 runs in
VFE_3.0/vfe3_runs/10-3-2026_Experiments and evaluates, per layer, the stacked transfer
M = O'T (K x K) of each run's chart: the reference operator of an edge on which every head selects
the same source with unit weight. Run from the VFE_3.0 checkout with its package importable:

    PYTHONPATH=. python <this file> > trained_link_geometry_output.txt
"""
import glob
import os

import torch

from vfe3.model.relational_operators import chart_receive_map

torch.set_num_threads(1)
ROOT = os.path.join("vfe3_runs", "10-3-2026_Experiments")
RUNS = [("affine", "affine", "121.77_wikitext-103_K20_affine"),
        ("first order", "first_order", "121.98_wikitext-103_K20_first-order"),
        ("exponential", "exponential", "121.53_wikitext-103_K20_exponential"),
        ("exponential, receiver", "exponential", "124.93_wikitext-103_K20_exponential_gradient")]


def flat(d, pre=""):
    out = {}
    for k, v in d.items():
        out.update(flat(v, pre + k + ".") if isinstance(v, dict) else {pre + k: v})
    return out


def layers(state):
    found = [(state["relational_operators.T"], state["relational_operators.O"])]
    i = 0
    while f"relational_operators_extra.{i}.T" in state:
        found.append((state[f"relational_operators_extra.{i}.T"], state[f"relational_operators_extra.{i}.O"]))
        i += 1
    return found


def geometry(T, O, chart):
    H, d, K = T.shape
    Op = chart_receive_map(T.double(), O.double(), chart)                 # (H, K, d)
    T_s = T.double().reshape(H * d, K)
    O_s = O.double().permute(1, 0, 2).reshape(K, H * d)
    M = Op.permute(1, 0, 2).reshape(K, H * d) @ T_s                        # stacked transfer O'T
    sv = torch.linalg.svdvals(M)
    row = dict(sign=int(torch.linalg.slogdet(M)[0]), smin=float(sv.min()), kappa=float(sv.max() / sv.min()))
    if chart == "exponential":
        X = O_s @ T_s                                                       # shared generator X = OT
        I = torch.eye(K, dtype=X.dtype)
        eX = torch.linalg.matrix_exp(X)
        row.update(Xnorm=float(torch.linalg.matrix_norm(X, ord=2)),
                   chart_err=float(torch.linalg.matrix_norm(M - eX) / torch.linalg.matrix_norm(eX)),
                   trunc1=float(torch.linalg.matrix_norm(eX - (I + X), ord=2) / torch.linalg.matrix_norm(eX, ord=2)),
                   trunc2=float(torch.linalg.matrix_norm(eX - (I + X + X @ X / 2), ord=2) / torch.linalg.matrix_norm(eX, ord=2)))
    return row


for label, chart, run in RUNS:
    base = os.path.join(ROOT, run)
    entries = []
    for path in sorted(glob.glob(os.path.join(base, "map_snapshots", "step_*.pt"))):
        snap = torch.load(path, map_location="cpu", weights_only=False)
        entries.append((int(snap["step"]), flat(snap["state"])))
    if not entries or entries[-1][0] != 15000:                             # final weights unless snapshotted
        final = torch.load(os.path.join(base, "final_model.pt"), map_location="cpu", weights_only=False)
        entries.append((15000, final["model_state"]))
    print(f"== {label}: {run}")
    print("   snapshot steps:", [s for s, _ in entries])
    by_layer = {}
    for step, state in entries:
        for layer, (T, O) in enumerate(layers(state)):
            by_layer.setdefault(layer, []).append((step, geometry(T, O, chart)))
    for layer, rows in by_layer.items():
        signs = [r["sign"] for _, r in rows]
        changes = sum(a != b for a, b in zip(signs, signs[1:]))
        smin = min(r["smin"] for s, r in rows if s >= 1000)
        fin = rows[-1][1]
        line = (f"   layer {layer}: det signs {signs} ({changes} changes); min sigma_min(M), steps >= 1000: {smin:.3e}; "
                f"final sigma_min {fin['smin']:.3e}, kappa {fin['kappa']:.3g}")
        if chart == "exponential":
            line += (f"; final ||X||_2 {fin['Xnorm']:.3f}, rel|M - e^X| {fin['chart_err']:.1e}, "
                     f"rel||e^X - (I+X)||_2 {fin['trunc1']:.3f}, rel||e^X - (I+X+X^2/2)||_2 {fin['trunc2']:.3f}")
        print(line)
