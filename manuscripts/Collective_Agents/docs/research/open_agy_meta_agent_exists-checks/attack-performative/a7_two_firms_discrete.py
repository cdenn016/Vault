r"""Attack A7: (i) independent recomputation of the C3 counterexample (check3 case E2) and of the sign rule of Prop S
in the investigator's two-firm setting; (ii) the discrete declared agency model at g = 0.05 (claimed pooled index
0.947 with class gamma_C in [0,6], gamma = 2, U = {-1,0,1}).

Two firms of 4 on one world variable: all-to-all raw relays inside each firm (receiver-specific Rc), no channel
between firms, steady-state Kalman gains (info 1/R + 3/(R+Rc)), acts u = -g_k m^+, members read their own firm's
total act and predict m' = F m^+ + b U_own (other firm's act ignored, mu = 0).

Declared expectations: E1 (g = 0.3, 0.3; Rc = 1): all cross entries of Pi^c equal and positive (~ +0.268), not
diffusive.  E2 (g = 1.5, 0.2; Rc = 0.02): cross entries negative (~ -0.956), Pi^c diffusive, r(C1) ~ 10.86,
r(C2) ~ 146.96.  NEG control: E2 with Rc = 1 is not diffusive (investigator: within-C1 positive entries 43.6).
Discrete agency: pooled index about 0.947 (if the investigator's number is the pooled one).
"""
import os
os.environ.setdefault("OMP_NUM_THREADS", "1")
import itertools
import numpy as np
from win import kalman_ss, contrast_block

F, Q, R, b = 0.9, 0.05, 1.0, 0.2


def two_firms(Rc: float, g1: float, g2: float, T: int = 90, ts: int = 50) -> np.ndarray:
    n = 4
    N = 2 * n
    firm = [0] * n + [1] * n
    gk = [g1, g2]
    pairs = [(i, j) for i in range(N) for j in range(N) if i != j and firm[i] == firm[j]]
    pidx = {p: q for q, p in enumerate(pairs)}
    per = 1 + N + len(pairs)
    NT = 1 + per * T
    Pm, Pp = kalman_ss(F, Q, 1 / R + (n - 1) / (R + Rc))
    Ks, Kc = Pp / R, Pp / (R + Rc)
    c0 = 1 - Ks - (n - 1) * Kc
    sig0 = np.sqrt(Q / (1 - F * F))
    eta = np.zeros((T + 1, NT)); eta[0, 0] = sig0
    m = np.zeros((N, NT))
    Erow = None
    for t in range(T):
        base = 1 + per * t
        if t == ts:
            Erow = m - eta[t][None, :]
        mp = np.zeros((N, NT))
        for i in range(N):
            row = c0 * m[i] + (Ks + (n - 1) * Kc) * eta[t]
            row = row.copy()
            row[base + 1 + i] += Ks * np.sqrt(R)
            for j in range(N):
                if j != i and firm[j] == firm[i]:
                    row[base + 1 + j] += Kc * np.sqrt(R)
                    row[base + 1 + N + pidx[(i, j)]] += Kc * np.sqrt(Rc)
            mp[i] = row
        U = [-gk[k] * mp[[i for i in range(N) if firm[i] == k]].sum(axis=0) for k in range(2)]
        eta[t + 1] = F * eta[t] + b * (U[0] + U[1])
        eta[t + 1][base] += np.sqrt(Q)
        for i in range(N):
            m[i] = F * mp[i] + b * U[firm[i]]
    Qh, _ = np.linalg.qr(eta.T)
    Ep = Erow - (Erow @ Qh) @ Qh.T
    S = Ep @ Ep.T
    return np.linalg.inv(0.5 * (S + S.T))


def contrast_region(Pi: np.ndarray, C: list) -> float:
    N = Pi.shape[0]
    a = -(Pi - np.diag(np.diag(Pi)))
    eps = Pi.sum(axis=1)
    out = [k for k in range(N) if k not in C]
    cut = a[np.ix_(C, out)].sum(axis=1)
    M = Pi[np.ix_(C, C)] - np.diag(cut)
    n = len(C)
    phi = np.ones(n) / np.sqrt(n)
    xout = float(phi @ Pi[np.ix_(C, C)] @ phi)
    Z = np.linalg.qr(np.column_stack([phi, np.eye(n)[:, :n - 1]]))[0][:, 1:]
    return float(np.linalg.eigvalsh(Z.T @ M @ Z).min()) / xout


if __name__ == "__main__":
    for lab, Rc, g1, g2 in [("E1", 1.0, 0.3, 0.3), ("E2", 0.02, 1.5, 0.2), ("NEG E2 Rc=1", 1.0, 1.5, 0.2)]:
        Pi = two_firms(Rc, g1, g2)
        cross = Pi[:4, 4:]
        off = Pi - np.diag(np.diag(Pi))
        dif = off.max() <= 0 and Pi.sum(axis=1).min() >= 0
        msg = "%-12s cross in [%+.4e, %+.4e]  max offdiag %+.4e  min rowsum %+.4e  diffusive=%s" % (
            lab, cross.min(), cross.max(), off.max(), Pi.sum(axis=1).min(), dif)
        if dif:
            msg += "  r(C1)=%.4f r(C2)=%.4f" % (contrast_region(Pi, [0, 1, 2, 3]), contrast_region(Pi, [4, 5, 6, 7]))
        print(msg)
    # (ii) discrete declared agency model
    n, Lam, gam, g = 4, 4.0, 2.0, 0.05
    alpha = 4.202606e-03
    rng = np.random.default_rng(1)
    Z = np.linalg.qr(np.column_stack([np.ones(n) / 2, rng.standard_normal((n, n - 1))]))[0][:, 1:]
    prof = np.array(list(itertools.product([-1.0, 0.0, 1.0], repeat=n)))
    num_by_g = np.zeros(601); den = 0.0; per_state = []
    grid = np.linspace(0, 6, 601)
    states = []
    for _ in range(200):
        mi = 0.3 + Z @ (np.sqrt(alpha) * rng.standard_normal(n - 1))
        states.append(mi)
    for mi in states:
        z = F * mi; zC = F * 0.3
        GC = 0.5 * Lam * (zC + b * prof.sum(axis=1)) ** 2
        tilt = (Lam * b * (z - zC)[None, :] * prof).sum(axis=1)
        lp = -gam * (GC + tilt); p = np.exp(lp - lp.max()); p /= p.sum()
        d = float(np.sum(p * np.log(p * len(prof))))
        den += d
        kls = []
        for k, gC in enumerate(grid):
            lq = -gC * GC; q = np.exp(lq - lq.max()); q /= q.sum()
            kk = float(np.sum(p * np.log(p / q)))
            num_by_g[k] += kk
            kls.append(kk)
        per_state.append(1 - min(kls) / d)
    k = int(np.argmin(num_by_g))
    print("discrete model g=0.05: pooled index %.5f at gamma_C=%.2f ; per-state median %.5f min %.5f" % (
        1 - num_by_g[k] / den, grid[k], np.median(per_state), np.min(per_state)))
