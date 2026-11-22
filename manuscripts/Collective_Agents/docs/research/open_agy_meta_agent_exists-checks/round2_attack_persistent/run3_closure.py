r"""Check 3: memory clause for the two candidate coarse variables, computed with my own code.

  P2: y = average of the members' prior-mean vectors (R^2), the constructor's declaration;
  P1: y = average of the members' first components (the scalar collective average of def:col-contrast).

Internal variables x = (m^-_{i,0}, m^-_{i,1})_{i in A} (R^8); given the blanket path (own sensors, slot readings,
the members' own sensings carried by the relays) and the policy path,
  x_{t+1} = A(t) x_t + (input) + n_t,  A(t) = blockdiag_i A_F P^+_i (P^-_i)^{-1},
  n_t: relay read noise A_F K_rel sum_j nu_ij and computation noise xi_i, Q^n(t) > 0.
Per-step closure defect (eq:agy-closure-defect, 05_agency.tex:55) with Sigma = Cov(x_t | blanket path):
  d_cl = 1/2 ln det(I + (P Q^n P^T)^{-1} P A Sigma_{x|y} A^T P^T),  d_M <= d_cl.
Exact stationary Markov defect of P1 at fixed symmetric policies from the autocovariance of y (Toeplitz conditioning).

Declared expectations (before running):
  P2 on deviation-free stretches: d_cl = 0 to rounding (A preserves ker P2).  NEGATIVE CONTROL (must not be 0):
  P2 with one member permanently reading 2 mates: d_cl bounded away from 0.
  P1: d_cl about 3e-3 per step on symmetric stretches (my hand estimate 2.7e-3 at two open slots); exact
  stationary d_M of P1 below 1e-3; worst single-round relay pattern below 0.02.
  If all P1 values stay below alpha_M = 0.02, the scalar collective average repairs the declaration clause with
  the grade's alpha_M.
"""
import time
import itertools
import numpy as np
from core import Par, efe, _lse

t0 = time.time()
PAR = Par()
n = PAR.n
F = PAR.F
AF = np.array([[F, 0.0], [1.0, 0.0]])
P1 = np.zeros((1, 2 * n)); P1[0, 0::2] = 1.0 / n
P2 = np.kron(np.ones((1, n)) / n, np.eye(2))


def member(Pm, nopen, m):
    D = np.diag([1 / PAR.R + nopen / PAR.Rs, m / (PAR.R + PAR.Rc)])
    Pp = np.linalg.inv(np.linalg.inv(Pm) + D)
    Ai = AF @ Pp @ np.linalg.inv(Pm)
    krel = Pp[:, 1] / (PAR.R + PAR.Rc)
    Qi = AF @ (m * PAR.Rc * np.outer(krel, krel)) @ AF.T + PAR.qc * np.eye(2)
    return Ai, Qi, Pp


def Pminus(pp):
    return np.array([[F * F * pp + PAR.Q + PAR.qc, F * pp], [F * pp, pp + PAR.qc]])


def dcl(P, A, Qn, Sig):
    PS = P @ Sig
    Sxy = Sig - PS.T @ np.linalg.solve(PS @ P.T, PS)
    M = P @ A @ Sxy @ A.T @ P.T
    return 0.5 * np.log(np.linalg.det(np.eye(P.shape[0]) + np.linalg.solve(P @ Qn @ P.T, M)))


def step_mats(Pms, nopen, ms):
    A = np.zeros((2 * n, 2 * n)); Qn = np.zeros((2 * n, 2 * n)); Pps = []
    for i in range(n):
        Ai, Qi, Pp = member(Pms[i], nopen, ms[i])
        A[2 * i:2 * i + 2, 2 * i:2 * i + 2] = Ai
        Qn[2 * i:2 * i + 2, 2 * i:2 * i + 2] = Qi
        Pps.append(Pp)
    return A, Qn, Pps


def simulate_policy(T, rng):
    r"""T-real policy path for one niche (same rules as core.run), returning per round (nopen, m_i, P^-_i)."""
    w = PAR.w
    Pms = [Pminus(PAR.p0) for _ in range(n)]
    slots = np.zeros(n, dtype=int)
    ms = np.zeros(n, dtype=int)
    rec = []
    for t in range(T):
        nopen = int(slots.sum())
        rec.append((nopen, ms.copy(), [P.copy() for P in Pms]))
        Pps = [member(Pms[i], nopen, ms[i])[2] for i in range(n)]
        Pms = [AF @ Pp @ AF.T + np.diag([PAR.Q, 0.0]) + PAR.qc * np.eye(2) for Pp in Pps]
        G = np.array([efe(PAR, P[0, 0], P[0, 1], P[1, 1]) for P in Pms])         # (n, M, NS)
        Gt = -_lse(np.log(w)[None, :, None] - PAR.gamma * G, axis=1) / PAR.gamma
        r = rng.integers(n)
        cur = int(slots.sum())
        no = cur - slots[r]
        pr = 0.5 * (1 + np.tanh(0.5 * PAR.gamma * (Gt[r, no] - Gt[r, no + 1])))
        new = slots.copy(); new[r] = int(rng.random() < pr)
        newc = int(new.sum())
        for i in range(n):
            nk = newc if i == r else cur
            lq = np.log(w) - PAR.gamma * G[i, :, nk]
            q = np.exp(lq - lq.max()); q /= q.sum()
            ms[i] = rng.choice(len(q), p=q)
        slots = new
    return rec


# (1) sampled T-real paths
rng = np.random.default_rng(3101)
res1, res2 = [], []
for k in range(30):
    rec = simulate_policy(360, rng)
    Sig = np.zeros((2 * n, 2 * n))
    for t, (nopen, ms, Pms) in enumerate(rec):
        A, Qn, _ = step_mats(Pms, nopen, ms)
        if t >= 60:
            res1.append(dcl(P1, A, Qn, Sig)); res2.append(dcl(P2, A, Qn, Sig))
        Sig = A @ Sig @ A.T + Qn
res1, res2 = np.array(res1), np.array(res2)
print(f"(1) 30 sampled T-real paths x 300 steps: P2 d_cl max {res2.max():.2e}, mean {res2.mean():.2e}; "
      f"P1 d_cl max {res1.max():.3e}, mean {res1.mean():.3e}, 99.9% quantile {np.quantile(res1, 0.999):.3e}  "
      f"({time.time()-t0:.0f}s)")

# stationary symmetric covariance at a given open count (all members read 3 mates)
def stationary(nopen, ms=(3, 3, 3, 3)):
    Pm = Pminus(PAR.p0)
    for _ in range(2000):
        Pp = member(Pm, nopen, 3)[2]
        Pm = AF @ Pp @ AF.T + np.diag([PAR.Q, 0.0]) + PAR.qc * np.eye(2)
    return Pm


# (2) NEGATIVE CONTROL for P2 and worst single-round patterns for P1
for nopen in (0, 2, 4):
    Pm = stationary(nopen)
    A, Qn, _ = step_mats([Pm] * n, nopen, [3] * n)
    Sig = np.zeros((2 * n, 2 * n))
    for _ in range(400):
        Sig = A @ Sig @ A.T + Qn
    sym1, sym2 = dcl(P1, A, Qn, Sig), dcl(P2, A, Qn, Sig)
    worst1, worst2, arg1 = 0.0, 0.0, None
    for ms in itertools.product(range(4), repeat=n):
        Ad, Qd, _ = step_mats([Pm] * n, nopen, list(ms))
        v1, v2 = dcl(P1, Ad, Qd, Sig), dcl(P2, Ad, Qd, Sig)
        if v1 > worst1:
            worst1, arg1 = v1, ms
        worst2 = max(worst2, v2)
    # negative control: member 0 permanently reads 2 mates (sustained asymmetric gains)
    ms_neg = [2, 3, 3, 3]
    Pm0 = Pm.copy(); Pm_others = Pm.copy()
    for _ in range(2000):
        Pm0 = AF @ member(Pm0, nopen, 2)[2] @ AF.T + np.diag([PAR.Q, 0.0]) + PAR.qc * np.eye(2)
    An, Qnn, _ = step_mats([Pm0, Pm, Pm, Pm], nopen, ms_neg)
    Sn = np.zeros((2 * n, 2 * n))
    for _ in range(400):
        Sn = An @ Sn @ An.T + Qnn
    neg2 = dcl(P2, An, Qnn, Sn)
    # exact stationary Markov defect of P1 (no input) at the symmetric policy
    Sx = Sig
    L = 40
    gam = [float((P1 @ np.linalg.matrix_power(A, k) @ Sx @ P1.T)[0, 0]) for k in range(L + 2)]
    Tm = np.array([[gam[abs(i - j)] for j in range(L + 2)] for i in range(L + 2)])
    def cvar(hist):
        idx = list(range(L + 2 - 1 - hist, L + 1))
        S11 = Tm[np.ix_(idx, idx)]; s12 = Tm[np.ix_(idx, [L + 1])]
        return Tm[L + 1, L + 1] - float((s12.T @ np.linalg.solve(S11, s12))[0, 0])
    dM = 0.5 * np.log(cvar(1) / cvar(L))
    print(f"(2) nopen={nopen}: symmetric step d_cl P2 {sym2:.1e} (expected 0), P1 {sym1:.3e}; exact stationary "
          f"d_M(P1) {dM:.3e}; worst single-round relay pattern: P1 {worst1:.3e} at {arg1}, P2 {worst2:.3e}; "
          f"NEG P2 with member 0 at 2 mates permanently: {neg2:.3e} (must be > 0)")
print(f"total {time.time()-t0:.1f}s")
