"""Check D: lower bound for the inference clause when the encoded belief is ANY Gaussian function of the scalar y,
N(g(y), V(y)), at the declared instance (gamma = 4, top-kappa attention).

Pointwise optimum: V(y) = 1/E[1/P*|y], g(y) = E[m*/P*|y] / E[1/P*|y].
Expected: <= 0.02388 (identity mean); control: g(y)=y reproduces 0.02388, g(y)=y with V=Pbar(pi) gives 0.00765.
"""
import os
for k in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS"):
    os.environ[k] = "1"
import math
import numpy as np
from fx import *

n, N, kappa = 4, 8, 3
P0, Rs, Rc, gam, s2 = 1.0, 1.0, 0.1, 4.0, 1e-3
Gfull = lambda i, x, So: finfo(x / Rs + So / (Rs + Rc), P0)
profs, law, _ = stationary_chain(n, Gfull, gam)


def moments(p):
    S = p.sum()
    Lam = 1 / P0 + p / Rs + (S - p) / (Rs + Rc)
    Ps = 1 / (1 / P0 + S / Rs)
    nv = 1 + n + n * n + n
    cy = np.zeros(nv); cm = np.zeros(nv)
    var = np.concatenate([[P0], np.full(n, Rs), np.full(n * n, Rc), np.full(n, s2)])
    for i in range(n):
        if p[i]:
            cy[0] += 1 / (Lam[i] * Rs) / n; cy[1 + i] += 1 / (Lam[i] * Rs) / n
        for k in range(n):
            if k != i and p[k]:
                w = 1 / (Lam[i] * (Rs + Rc)) / n
                cy[0] += w; cy[1 + k] += w; cy[1 + n + i * n + k] += w
        cy[1 + n + n * n + i] += 1 / n
    for k in range(n):
        if p[k]:
            cm[0] += Ps / Rs; cm[1 + k] += Ps / Rs
    VY = np.sum(cy ** 2 * var); VM = np.sum(cm ** 2 * var); C = np.sum(cy * cm * var)
    return Ps, VY, VM, C, float(np.mean(1 / Lam))


M = np.array([(law[k],) + moments(p) for k, p in enumerate(profs) if law[k] > 0])
W, PS, VY, VM, CC, PB = M.T
beta = CC / VY
resid = VM - CC ** 2 / VY                      # Var(m* | y, pi)
ys = np.linspace(-8, 8, 160001); dy = ys[1] - ys[0]
dens = np.array([w * np.exp(-ys ** 2 / (2 * v)) / math.sqrt(2 * math.pi * v) for w, v in zip(W, VY)])
post = dens / dens.sum(0)
Einv = (post / PS[:, None]).sum(0)
V = 1 / Einv
g = (post * beta[:, None] / PS[:, None]).sum(0) * ys / Einv


def kl(gy, Vy):
    var_part = dens * 0.5 * (Vy[None, :] / PS[:, None] - 1 - np.log(Vy[None, :] / PS[:, None]))
    mean_part = dens * 0.5 * ((gy[None, :] - beta[:, None] * ys[None, :]) ** 2 + resid[:, None]) / PS[:, None]
    return float((var_part + mean_part).sum() * dy)


print("control g=y, V(y) optimal (expect 0.02388):", kl(ys, V))
Vpb = None
tot = 0.0
for w, ps, vy, vm, c, pb in M:
    tot += w * 0.5 * (pb / ps - 1 - math.log(pb / ps) + (vy - 2 * c + vm) / ps)
print("control g=y, V=Pbar(pi) (expect 0.00765):", tot)
print("optimal Gaussian encoding by y alone, N(g(y), V(y)):", kl(g, V), "| alpha_I declared 0.02")
print("irreducible mean part E[Var(m*|y,pi)/(2P*)]:", float(np.sum(W * 0.5 * resid / PS)))
