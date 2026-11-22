"""Check F: direction of the relative entropy in the inference clause (declared instance).

Forward (precedent of ex:met-two-firms, 'from the members' law to the exact one'): KL(encoded || union posterior).
Reverse: KL(union posterior || encoded).  For each direction: (i) encoded N(y, Pbar(pi)); (ii) best belief that is a
function of y alone (reverse optimum by moment matching: g = E[m*|y], V = E[P*|y] + Var(m*|y)).
Expected: forward values 0.007655 and 0.023620 (check D); reverse values unknown.
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
rows = []
for k, p in enumerate(profs):
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
D2 = VY - 2 * CC + VM
fwd_pb = np.sum(W * 0.5 * (PB / PS - 1 - np.log(PB / PS) + D2 / PS))
rev_pb = np.sum(W * 0.5 * (PS / PB - 1 - np.log(PS / PB) + D2 / PB))
beta = CC / VY; resid = VM - CC ** 2 / VY
ys = np.linspace(-10, 10, 200001); dy = ys[1] - ys[0]
dens = W[:, None] * np.exp(-ys[None, :] ** 2 / (2 * VY[:, None])) / np.sqrt(2 * math.pi * VY[:, None])
post = dens / dens.sum(0)
Em = (post * beta[:, None]).sum(0) * ys
Em2 = (post * (beta[:, None] ** 2 * ys[None, :] ** 2 + resid[:, None])).sum(0)
V = (post * PS[:, None]).sum(0) + Em2 - Em ** 2
rev_opt = float((dens.sum(0) * 0.5 * (np.log(V) - (post * np.log(PS)[:, None]).sum(0))).sum() * dy)
print("forward  N(y,Pbar(pi))", fwd_pb, "| reverse N(y,Pbar(pi))", rev_pb)
print("reverse, best belief that is a function of y alone:", rev_opt, "| alpha_I 0.02")
