"""Check E: blind recomputation of the investigator's 81-point box (P0, Rs, Rc, gamma at x0.8/1/1.2), adding the
inference tolerance under the y-only reading (optimal Gaussian encoding N(g(y), V(y)) of the scalar coarse variable).

Expected (investigator): r(A) in [36.66, 80.03]; mechanism <= 22.89; mean-coupling in [31.56, 68.74];
N_hab <= 4.62; N_pr annealed <= 4.49; Agency >= 0.99970; alpha_I (blanket-path variance) <= 0.0132.
Unknown: y-only alpha_I range.
"""
import os
for k in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS"):
    os.environ[k] = "1"
import itertools
import math
import numpy as np
from fx import *

n, N, kappa, s2 = 4, 8, 3, 1e-3
ys = np.linspace(-10, 10, 100001)
dy = ys[1] - ys[0]


def infer_both(law, profs, P0, Rs, Rc):
    rows = []
    for k, p in enumerate(profs):
        if law[k] <= 0:
            continue
        S = p.sum()
        Lam = 1 / P0 + p / Rs + (S - p) / (Rs + Rc)
        Ps = 1 / (1 / P0 + S / Rs)
        nv = 1 + n + n * n + n
        cy = np.zeros(nv); cm = np.zeros(nv)
        var = np.concatenate([[P0], np.full(n, Rs), np.full(n * n, Rc), np.full(n, s2)])
        for i in range(n):
            if p[i]:
                cy[0] += 1 / (Lam[i] * Rs) / n; cy[1 + i] += 1 / (Lam[i] * Rs) / n
            for j in range(n):
                if j != i and p[j]:
                    w = 1 / (Lam[i] * (Rs + Rc)) / n
                    cy[0] += w; cy[1 + j] += w; cy[1 + n + i * n + j] += w
            cy[1 + n + n * n + i] += 1 / n
        for j in range(n):
            if p[j]:
                cm[0] += Ps / Rs; cm[1 + j] += Ps / Rs
        rows.append((law[k], Ps, np.sum(cy ** 2 * var), np.sum(cm ** 2 * var), np.sum(cy * cm * var), np.mean(1 / Lam)))
    W, PS, VY, VM, CC, PB = np.array(rows).T
    a_pb = float(np.sum(W * 0.5 * (PB / PS - 1 - np.log(PB / PS) + (VY - 2 * CC + VM) / PS)))
    beta = CC / VY
    resid = VM - CC ** 2 / VY
    dens = W[:, None] * np.exp(-ys[None, :] ** 2 / (2 * VY[:, None])) / np.sqrt(2 * math.pi * VY[:, None])
    post = dens / dens.sum(0)
    Einv = (post / PS[:, None]).sum(0)
    V = 1 / Einv
    g = (post * beta[:, None] / PS[:, None]).sum(0) * ys / Einv
    vp = dens * 0.5 * (V[None, :] / PS[:, None] - 1 - np.log(V[None, :] / PS[:, None]))
    mp = dens * 0.5 * ((g[None, :] - beta[:, None] * ys[None, :]) ** 2 + resid[:, None]) / PS[:, None]
    return a_pb, float((vp + mp).sum() * dy)


rows = []
for fP, fs, fc, fg in itertools.product((0.8, 1.0, 1.2), repeat=4):
    P0, Rs, Rc, g1 = 1.0 * fP, 1.0 * fs, 0.1 * fc, 4.0 * fg
    Gf = lambda i, x, So: finfo(x / Rs + So / (Rs + Rc), P0)
    Gm = lambda i, x, So: finfo(x / Rs + min(kappa, So) / (Rs + Rc), P0)
    pr, lw, _ = stationary_chain(n, Gf, g1)
    SA = sigma_c(n, lw, N - 1, kappa, np.inf, P0, Rs, Rc, s2)
    Pi = np.linalg.inv(blockdiag(SA, SA))
    rA = contrast(Pi, range(n))
    prN, lwN, _ = stationary_chain(N, Gm, g1)
    PiH = np.linalg.inv(sigma_c(N, lwN, N - 1, kappa, np.inf, P0, Rs, Rc, s2))
    rmech = contrast(PiH, range(N))
    A_ = -(Pi - np.diag(np.diag(Pi)))
    rmean = 1 + N * A_[np.triu_indices(N, 1)].mean() / Pi.sum(1).mean()
    Sp = sigma_c(n, lw, N - 1, kappa, 0.0, P0, Rs, Rc, s2)
    rpr = contrast(np.linalg.inv(blockdiag(Sp, Sp)), range(n))
    Sh = sigma_c(n, np.full(2 ** n, 2.0 ** -n), N - 1, kappa, 0.0, P0, Rs, Rc, s2)
    rh = contrast(np.linalg.inv(blockdiag(Sh, Sh)), range(n))
    ag = agency(lw, pr, P0, Rs)[0]
    a_pb, a_y = infer_both(lw, pr, P0, Rs, Rc)
    rows.append((rA, rmech, rmean, rh, rpr, ag, a_pb, a_y))
R = np.array(rows)
for k, nm in enumerate(["r(A)", "mech", "mean", "N_hab", "N_pr ann", "Agency", "aI blanket-path", "aI y-only optimum"]):
    print(f"{nm:18s} min {R[:, k].min():.6g} max {R[:, k].max():.6g}")
print("points with y-only optimum > 0.02:", int(np.sum(R[:, 7] > 0.02)), "/81 | min margin r(A)-mech",
      float((R[:, 0] - np.maximum(R[:, 1], np.maximum(R[:, 3], R[:, 4]))).min()))
