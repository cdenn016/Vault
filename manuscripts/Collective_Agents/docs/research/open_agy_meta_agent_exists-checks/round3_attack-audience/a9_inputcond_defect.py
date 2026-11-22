r"""A9: the input-conditional Markov defect of def:agy-closure(i) (05_agency.tex:20),
d_M = sup_t I(y_{t+1}; y_{0:t-1} | y_t, x_{B,0:t}), evaluated literally on P0's
stationary joint process (world, source noise, members), with the blanket path
x_B = members' sensory inputs (own sensor and channel from S) on rounds 0..t, and
also with the blanket path extended back to round -P (P = 40) to approximate the
whole past.

Declared expectations: with the blanket path from -infinity the value is the
stationary noise-only defect 0.025717 (A5).  With the blanket path from 0 only the
initial state is not independent of the inputs, the hypothesis of the simplified form
fails, and the value is unknown (could exceed 0.03).
Negative control: the noise-only stationary computation (A5) must be recovered as P grows.
"""
import os
for v in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS"):
    os.environ[v] = "1"
import numpy as np
from scipy.linalg import solve_discrete_lyapunov
from alib import P0Model, AF

m = P0Model()
F, Q, R, RS, Rc, qc, n = m.F, m.Q, m.R, m.RS, m.Rc, m.qc, m.n
A = AF(F)
AK = A @ m.Km
M = m.Mm
dX = 3 + 2 * n
dxi = 2 + n + n + 2 * n  # w, vS, v_i, nu_i, frak n_i (2 each)
T = np.zeros((dX, dX)); G = np.zeros((dX, dxi))
H = np.zeros((2 * n, dX)); J = np.zeros((2 * n, dxi))
T[0, 0] = F; G[0, 0] = 1.0          # eta_{t+1}
T[1, 0] = 1.0                        # eta_t copy
G[2, 1] = 1.0                        # vS lag <- vS_t
qv = np.zeros(dxi); qv[0] = Q; qv[1] = RS; qv[2:2 + n] = R; qv[2 + n:2 + 2 * n] = Rc; qv[2 + 2 * n:] = qc
for i in range(n):
    s = 3 + 2 * i
    # z_i(t) = [eta_t + v_i(t), eta_{t-1} + vS_lag + nu_i(t)]
    H[2 * i, 0] = 1.0; J[2 * i, 2 + i] = 1.0
    H[2 * i + 1, 1] = 1.0; H[2 * i + 1, 2] = 1.0; J[2 * i + 1, 2 + n + i] = 1.0
    # m_i(t+1) = M m_i + AK z_i(t) + frak n_i
    T[s:s + 2, s:s + 2] = M
    T[s:s + 2, :] += AK @ H[2 * i:2 * i + 2, :]
    G[s:s + 2, :] += AK @ J[2 * i:2 * i + 2, :]
    G[s, 2 + 2 * n + 2 * i] += 1.0; G[s + 1, 2 + 2 * n + 2 * i + 1] += 1.0
SX = solve_discrete_lyapunov(T, G @ np.diag(qv) @ G.T)
c = np.zeros(dX)
for i in range(n):
    c[3 + 2 * i] = 1.0 / n


def defects(P, Tw):
    """window rounds -P..Tw; returns I_t for t = 1..Tw-1 (y index relative to round 0)."""
    rounds = list(range(-P, Tw + 1))
    nr = len(rounds)
    L0 = np.linalg.cholesky(SX + 1e-18 * np.eye(dX))
    ncols = dX + nr * dxi
    sq = np.concatenate([np.ones(dX), np.tile(np.sqrt(qv), nr)])
    Xmap = np.zeros((dX, ncols)); Xmap[:, :dX] = L0
    ymaps, zmaps = {}, {}
    for k, t in enumerate(rounds):
        ymaps[t] = c @ Xmap
        xi = np.zeros((dxi, ncols)); xi[:, dX + k * dxi: dX + (k + 1) * dxi] = np.eye(dxi)
        zmaps[t] = H @ Xmap + J @ xi
        Xmap = T @ Xmap + G @ xi
    ymaps[Tw + 1] = c @ Xmap
    def cov(rows):
        Mx = np.vstack(rows) * sq[None, :]
        return Mx @ Mx.T
    out = []
    for t in range(1, Tw):
        target = [ymaps[t + 1]]
        cond_base = [ymaps[t]] + [zmaps[u][j] for u in rounds if u <= t for j in range(2 * n)]
        past = [ymaps[u] for u in range(0, t)]
        def cvar(cond):
            S = cov(target + cond)
            S11 = S[0, 0]; S12 = S[0, 1:]; S22 = S[1:, 1:]
            return S11 - S12 @ np.linalg.lstsq(S22, S12, rcond=1e-13)[0]
        v1 = cvar(cond_base); v2 = cvar(cond_base + past)
        out.append(0.5 * np.log(v1 / v2))
    return np.array(out)


for P in (0, 5, 20, 40):
    d = defects(P, 10)
    print("blanket path from round %4d: I_t (t=1..9) =" % (-P), np.round(d, 6), " sup = %.6f" % d.max())
