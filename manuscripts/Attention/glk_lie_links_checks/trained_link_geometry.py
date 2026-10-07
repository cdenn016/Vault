r"""Geometry of the trained content links of the October 3, 2026 chart runs (CPU, float64).

Reads the stored float32 factors (T, O) of every map snapshot (steps 0 to 15000) of the K=20 runs
from trained_links_K20.npz (written by extract_trained_links.py from the run folders
10-3-2026_Experiments/<run>/map_snapshots) and evaluates, per layer, the stacked transfer
M = O'T (K x K) of each run's chart: the reference operator of an edge on which every head selects
the same source with unit weight. Needs numpy and torch (CPU) only:

    python trained_link_geometry.py > trained_link_geometry_output.txt
"""
import os
import platform

import numpy as np
import torch

torch.set_num_threads(1)
print(f"python {platform.python_version()}, numpy {np.__version__}, torch {torch.__version__}, {platform.platform()}")
NPZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), "trained_links_K20.npz")
RUNS = [("affine", "affine", "121.77_wikitext-103_K20_affine", "affine"),
        ("first order", "first_order", "121.98_wikitext-103_K20_first-order", "first_order"),
        ("exponential", "exponential", "121.53_wikitext-103_K20_exponential", "exponential"),
        ("exponential, receiver", "exponential", "124.93_wikitext-103_K20_exponential_gradient",
         "exponential_receiver")]


def _phi1(A: torch.Tensor) -> torch.Tensor:
    r"""phi_1(A) = sum_{n>=1} A^{n-1}/n!, the upper-right block of exp([[A, I], [0, 0]])."""
    n = A.shape[-1]
    eye = torch.eye(n, dtype=A.dtype)
    augmented = torch.cat([torch.cat([A, eye], dim=-1), torch.zeros(n, 2 * n, dtype=A.dtype)], dim=-2)
    return torch.linalg.matrix_exp(augmented)[:n, n:]


def chart_receive_map(T: torch.Tensor, O: torch.Tensor, chart: str) -> torch.Tensor:
    r"""Effective receiving maps O' (H, K, d) of the tiled content link (same arithmetic as
    vfe3.model.relational_operators.chart_receive_map, one equal-head run):
    O'_affine = O, O'_first_order = T^{-1} + O, O'_exponential = T^{-1} + O phi_1(TO) = e^{OT} T^{-1},
    with T the (K, K) row stack of the sending maps and O the (K, K) column stack of the receiving factors."""
    if chart == "affine":
        return O
    H, d, K = T.shape
    T_stack = T.to(torch.float64).reshape(-1, K)                               # (K, K) rows by head
    O_stack = O.to(torch.float64).permute(1, 0, 2).reshape(K, -1)              # (K, K) columns by head
    inverse = torch.linalg.inv_ex(T_stack).inverse
    receive = inverse + O_stack if chart == "first_order" else inverse + O_stack @ _phi1(T_stack @ O_stack)
    return receive.reshape(K, H, d).permute(1, 0, 2)                           # (H, K, d)


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


data = np.load(NPZ)
for label, chart, run, tag in RUNS:
    steps = [int(s) for s in data[f"{tag}_steps"]]
    T_all, O_all = data[f"{tag}_T"], data[f"{tag}_O"]                      # (S, L, H, d, K), (S, L, H, K, d)
    print(f"== {label}: {run}")
    print("   snapshot steps:", steps)
    by_layer = {}
    for k, step in enumerate(steps):
        for layer in range(T_all.shape[1]):
            T, O = torch.from_numpy(T_all[k, layer]), torch.from_numpy(O_all[k, layer])
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
