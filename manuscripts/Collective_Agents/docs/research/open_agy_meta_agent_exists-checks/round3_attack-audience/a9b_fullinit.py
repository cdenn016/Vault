"""A9b: noise-only Markov defect of one member's prior-mean coordinate (same law as
the average) from three Gaussian initial laws: the noise-only stationary law, a
deterministic start, and the members' full stationary law (world tracking included),
i.e. 'the value without input for the same initial law' (05_agency.tex:20).
Declared expectation: 0.025717 for the noise-only law (A5); others unknown.
Negative control: the world block of the augmented covariance must equal the AR(1)
covariance [[Q/(1-F^2), F Q/(1-F^2)], [., Q/(1-F^2)]].
"""
import os
for v in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS"):
    os.environ[v] = "1"
import numpy as np
from scipy.linalg import solve_discrete_lyapunov
from alib import P0Model, AF

m = P0Model()
F, Q, qc, n = m.F, m.Q, m.qc, m.n
M = m.Mm
T0, W0 = m.system(include_world=True)
d0 = T0.shape[0]
A = AF(F)
dim = d0 + 2
T = np.zeros((dim, dim)); T[:d0, :d0] = T0; T[d0:, d0:] = A
g = np.zeros(dim); g[[2 * a for a in range(n + 1)]] = -1.0; g[d0] = 1.0
W = np.zeros((dim, dim))
W[:d0, :d0] = W0 - Q * np.outer(g[:d0], g[:d0])  # remove world part, re-add jointly
W += Q * np.outer(g, g)
S = solve_discrete_lyapunov(T, W)
ie, ix = [2, 3], [d0, d0 + 1]
Vx = Q / (1 - F ** 2)
print("NC world block:", np.round(S[np.ix_(ix, ix)].ravel(), 8), "expected", np.round([Vx, F * Vx, F * Vx, Vx], 8))
Cm = S[np.ix_(ie, ie)] + S[np.ix_(ix, ix)] + S[np.ix_(ie, ix)] + S[np.ix_(ix, ie)]
print("full stationary Cov(m^-_1):", np.round(Cm.ravel(), 6))


def defect_path(S0, tmax=40):
    Tn = tmax + 2
    covs = [S0]
    for _ in range(1, Tn):
        covs.append(M @ covs[-1] @ M.T + qc * np.eye(2))
    Y = np.zeros((Tn, Tn))
    for s in range(Tn):
        for t in range(s + 1):
            Y[s, t] = (np.linalg.matrix_power(M, s - t) @ covs[t])[0, 0]
            Y[t, s] = Y[s, t]
    out = []
    for t in range(1, tmax):
        a = t + 1
        def cv(idx):
            S12 = Y[a, idx]; S22 = Y[np.ix_(idx, idx)]
            return Y[a, a] - S12 @ np.linalg.solve(S22, S12)
        out.append(0.5 * np.log(cv([t]) / cv(list(range(0, t + 1)))))
    return np.array(out)


Sn = solve_discrete_lyapunov(M, qc * np.eye(2))
for name, S0 in (("noise-only stationary", Sn), ("deterministic start", 1e-14 * np.eye(2)),
                 ("members' full stationary law", Cm)):
    d = defect_path(S0)
    print("%-30s I_t (t=1..5) = %s  sup = %.6f at t=%d" % (name, np.round(d[:5], 6), d.max(), d.argmax() + 1))
