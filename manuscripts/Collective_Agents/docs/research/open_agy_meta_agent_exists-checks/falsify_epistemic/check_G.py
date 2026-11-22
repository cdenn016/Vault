"""Check G: reverse-direction inference tolerance at single gamma = 40 (slots and attention), encoded N(y, V) with the
best constant V = E[P* + (m* - y)^2]: value 0.5 (ln V - E ln P*), an upper bound on the y-only optimum.
Control: at the declared instance (gamma 4, top-kappa) the same estimator must give a value >= 0.0258 (check F optimum)."""
import os
for k in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS"):
    os.environ[k] = "1"
import math
import numpy as np
from fx import *
n, N, kappa, s2 = 4, 8, 3, 1e-3

def rev_const(P0, Rs, Rc, g_slot, g_att, T, rng):
    Gf = lambda i, x, So: finfo(x / Rs + So / (Rs + Rc), P0)
    profs, law, _ = stationary_chain(n, Gf, g_slot)
    counts = rng.multinomial(T, law)
    A = []; L = []
    for k, p in enumerate(profs):
        m = counts[k]
        if m == 0: continue
        S = p.sum(); Ps = 1 / (1 / P0 + S / Rs)
        eta = rng.normal(0, math.sqrt(P0), m)
        s = eta[:, None] + rng.normal(0, math.sqrt(Rs), (m, n))
        mstar = Ps * (s * p).sum(1) / Rs
        ms = np.zeros((m, n))
        for i in range(n):
            co = [j for j in range(n) if j != i and p[j]]
            js, pj = j_law(p[i], len(co), N - 1, kappa, g_att, P0, Rs, Rc)
            ji = rng.choice(js, size=m, p=pj)
            order = np.argsort(rng.random((m, len(co))), axis=1) if co else None
            acc = p[i] * s[:, i] / Rs; nh = np.zeros(m)
            for r_, jj in enumerate(co):
                heard = np.argmax(order == r_, axis=1) < ji
                acc = acc + heard * (s[:, jj] + rng.normal(0, math.sqrt(Rc), m)) / (Rs + Rc); nh += heard
            Lam = 1 / P0 + p[i] / Rs + nh / (Rs + Rc)
            ms[:, i] = acc / Lam + rng.normal(0, math.sqrt(s2), m)
        y = ms.mean(1)
        A.append(Ps + (mstar - y) ** 2); L.append(np.full(m, math.log(Ps)))
    A = np.concatenate(A); L = np.concatenate(L)
    return 0.5 * (math.log(A.mean()) - L.mean())

rng = np.random.default_rng(77)
print("control gamma 4 top-kappa (expect >= 0.0258):", rev_const(1.0, 1.0, 0.1, 4.0, np.inf, 200000, rng))
print("single gamma 40 reverse, constant V:", rev_const(1.0, 1.0, 0.1, 40.0, 40.0, 200000, rng), "| alpha_I 0.02")
