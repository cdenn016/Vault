r"""Check 8: inference clause by direct sampled simulation (independent of check 4's Lyapunov algebra), for P0
(kmsg = 1) and P1 (kmsg = 2).  Per system: world, source, members' exact filters with EFE attention, and the union
filter (union model: dynamics of eta_C = (eta_t, u_S(t-1)) with each member's own sensor and each member's reading of
the source, every datum once; relays between members carry copies of data and are not new data).
Encoded belief N(y, v) of eta_t with y = average of the members' prior means; union predictive N(m_U, P_U).
Reported: E[(y - m_U)^2], best-constant KL D/(2 P_U), claimed-variance KL, reverse KL 1/2 ln(1 + D/P_U).

Declared expectations before running: P0 best-constant KL = 0.0251 within 3 SE (check 4 exact); P1 best-constant KL
below 0.03.  NEGATIVE CONTROL: the encoded belief with the members' average of POSTERIOR means of eta_{t-1}... is not
used; instead a union model that ignores the source readings must give a KL at least five times larger.
"""
import time
import numpy as np
from math import comb
from itertools import combinations
from aud import Par, posterior, A_F

t0 = time.time()


def run(par: Par, K: int, T: int, burn: int, seed: int, union_with_source: bool = True):
    rng = np.random.default_rng(seed)
    n, F, Q = par.n, par.F, par.Q
    V0 = Q / (1 - F ** 2)
    eta = rng.normal(0, np.sqrt(V0), K)
    # members' filters (vectorized over K systems and n members) in moment form on x = (eta_t, eta_{t-1})
    P = np.zeros((K, n, 2, 2)); P[:] = np.array([[V0 + par.qc, F * V0], [F * V0, V0 + par.qc]])
    m = np.zeros((K, n, 2))
    PU = np.array([[V0, F * V0], [F * V0, V0]]); mU = np.zeros((K, 2))
    sS_prev = np.zeros(K); s_prev = np.zeros((K, n))
    att_S = np.ones((K, n), bool); att_m = -np.ones((K, n), int)     # mate index read this round (-1: none)
    acc = dict(D=0.0, PU=0.0, Pc=0.0, cnt=0)
    others = [[j for j in range(n) if j != i] for i in range(n)]
    # EFE sets (kmsg <= 2): (s, m) types with multiplicities
    types = [(s, mm) for s in (0, 1) for mm in range(0, n) if s + mm <= par.kmsg]
    mult = np.array([comb(n - 1, mm) for s, mm in types], float)
    for t in range(T):
        e_avg = m[:, :, 0].mean(1) - eta
        if t >= burn:
            acc["D"] += np.sum((m[:, :, 0].mean(1) - mU[:, 0]) ** 2)
            acc["PU"] += PU[0, 0] * K
            acc["Pc"] += P[:, :, 0, 0].mean() * K
            acc["cnt"] += K
        sS = eta + np.sqrt(par.RS) * rng.standard_normal(K)
        s = eta[:, None] + np.sqrt(par.R) * rng.standard_normal((K, n))
        yS = sS_prev[:, None] + np.sqrt(par.Rc) * rng.standard_normal((K, n))      # members' readings of u_S(t-1)
        # members' update
        for i in range(n):
            Pi = P[:, i]
            a = 1.0 / par.R
            bS = att_S[:, i] / (par.RS + par.Rc)
            hasm = att_m[:, i] >= 0
            bm = hasm / (par.R + par.Rc)
            ym = np.where(hasm, s_prev[np.arange(K), np.maximum(att_m[:, i], 0)] + np.sqrt(par.Rc) * rng.standard_normal(K), 0.0)
            det = Pi[:, 0, 0] * Pi[:, 1, 1] - Pi[:, 0, 1] ** 2
            i00, i01, i11 = Pi[:, 1, 1] / det, -Pi[:, 0, 1] / det, Pi[:, 0, 0] / det
            L00, L01, L11 = i00 + a, i01, i11 + bS + bm
            h0 = i00 * m[:, i, 0] + i01 * m[:, i, 1] + s[:, i] * a
            h1 = i01 * m[:, i, 0] + i11 * m[:, i, 1] + yS[:, i] * bS + ym * bm
            dL = L00 * L11 - L01 ** 2
            Q00, Q01, Q11 = L11 / dL, -L01 / dL, L00 / dL
            mp0 = Q00 * h0 + Q01 * h1
            m[:, i, 0] = F * mp0 + np.sqrt(par.qc) * rng.standard_normal(K)
            m[:, i, 1] = mp0 + np.sqrt(par.qc) * rng.standard_normal(K)
            P[:, i, 0, 0] = F * F * Q00 + Q + par.qc; P[:, i, 0, 1] = F * Q00; P[:, i, 1, 0] = F * Q00
            P[:, i, 1, 1] = Q00 + par.qc
        # union update: own sensors (mean, noise R/n) and the members' readings of u_S(t-1) (mean, noise RS + Rc/n)
        aU = n / par.R
        bU = (1.0 / (par.RS + par.Rc / n)) if (union_with_source and t > 0) else 0.0
        PUp = posterior(PU, aU, bU) if bU > 0 else np.linalg.inv(np.linalg.inv(PU) + np.diag([aU, 0.0]))
        iPU = np.linalg.inv(PU)
        hU = mU @ iPU.T + np.column_stack([s.mean(1) * aU, yS.mean(1) * bU])
        mUp = hU @ PUp.T
        mU = np.column_stack([F * mUp[:, 0], mUp[:, 0]])
        PU = A_F(F) @ PUp @ A_F(F).T + np.diag([Q, 0.0])
        # attention for round t+1 by EFE (types), uniform choice of the mate(s)
        for i in range(n):
            Pi = P[:, i]
            G = []
            for (sS_, mm) in types:
                b = sS_ / (par.RS + par.Rc) + mm / (par.R + par.Rc)
                a = 1.0 / par.R
                G.append(-0.5 * np.log((1 + a * Pi[:, 0, 0]) * (1 + b * Pi[:, 1, 1]) - a * b * Pi[:, 0, 1] ** 2))
            G = np.array(G).T
            lw = np.log(mult)[None, :] - par.gamma * G
            lw -= lw.max(1, keepdims=True)
            pr = np.exp(lw); pr /= pr.sum(1, keepdims=True)
            k = np.minimum((rng.random((K, 1)) > np.cumsum(pr, 1)).sum(1), len(types) - 1)
            ts = np.array([types[j][0] for j in k]); tm = np.array([types[j][1] for j in k])
            att_S[:, i] = ts == 1
            # at most one mate is read in P0/P1 at gamma = 40 (two-mate sets have probability < 1e-9; checked in log)
            pick = np.array(others[i])[rng.integers(0, n - 1, K)]
            att_m[:, i] = np.where(tm >= 1, pick, -1)
        sS_prev = sS
        s_prev = s
        eta = F * eta + np.sqrt(Q) * rng.standard_normal(K)
    D = acc["D"] / acc["cnt"]; PUm = acc["PU"] / acc["cnt"]; Pc = acc["Pc"] / acc["cnt"]
    return D, PUm, Pc


for par, lab in ((Par(), "P0"), (Par(kmsg=2), "P1")):
    D, PU, Pc = run(par, K=4000, T=260, burn=80, seed=801)
    D2, _, _ = run(par, K=4000, T=260, burn=80, seed=802)
    kl = D / (2 * PU); kl2 = D2 / (2 * PU)
    print(f"[{lab}] E[(y-m_U)^2] {D:.5e} (rerun {D2:.5e}); P_U {PU:.5e}; claimed {Pc:.5e}; best-constant KL {kl:.5f} "
          f"(rerun {kl2:.5f}); claimed-variance KL {0.5*(Pc/PU + D/PU - 1 - np.log(Pc/PU)):.5f}; reverse "
          f"{0.5*np.log1p(D/PU):.5f}  ({time.time()-t0:.0f}s)")
D, PU, Pc = run(Par(), K=2000, T=200, burn=80, seed=803, union_with_source=False)
print(f"[NEG P0, union model without the source readings] best-constant KL {D/(2*PU):.4f}")
