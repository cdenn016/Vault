r"""Check 1: validate my Monte Carlo estimator of Sigma^c against an exact Lyapunov solve that I derive here, and
against the round-1 A8 value.

Declared expectations (before running):
 (a) fixed attention (all 3 mates), no slots, qc = 0, Rc = 0.2 (the A8 setting): my exact Lyapunov gives r = 7.425938 (round-1 A8 value,
     attack-performative/a8_delay.py), and my Monte Carlo agrees within 3 SE.
 (b) fixed attention, 2 slots open every round, qc = 1e-4: exact and Monte Carlo agree within 3 SE (no reference).
 NEGATIVE CONTROL (c): replicas on INDEPENDENT world paths: the two-replica statistic then estimates the
     unconditional covariance, which carries the world-driven common mode; beta must rise far above (a)'s value
     (contrast far above 7.4). If it does not, the estimator is not conditioning on the world.
 NEGATIVE CONTROL (d): dead relays (pure noise of the assigned variance) with fixed attention and no slots: beta
     must be 0 within 3 SE (r within 3 SE of 1).
"""
import time
import numpy as np
from scipy.linalg import solve_discrete_lyapunov
from core import Par, run, compound, r_ab

t0 = time.time()


def exact_fixed(par: Par, k_open: int):
    r"""Exact world-conditional covariance of the prior errors e_{i,0} for the fixed policy: every member reads its
    own sensor, all n-1 mates' relays and k_open slots every round.  State z = (e^-_1..e^-_n (2D), v_1(t-1)..v_n(t-1))."""
    n = par.n
    F, Q, R, Rc, Rs, qc = par.F, par.Q, par.R, par.Rc, par.Rs, par.qc
    AF = np.array([[F, 0.0], [1.0, 0.0]])
    D = np.diag([1 / R + k_open / Rs, (n - 1) / (R + Rc)])
    Pm = np.diag([0.3, 0.3])
    for _ in range(5000):
        Pp = np.linalg.inv(np.linalg.inv(Pm) + D)
        Pm = AF @ Pp @ AF.T + np.diag([Q, 0.0]) + qc * np.eye(2)
    Pp = np.linalg.inv(np.linalg.inv(Pm) + D)
    Kown = Pp[:, 0] / R
    Krel = Pp[:, 1] / (R + Rc)
    Kslot = Pp[:, 0] / Rs
    Mx = AF @ Pp @ np.linalg.inv(Pm)
    dz = 2 * n + n
    A = np.zeros((dz, dz))
    for i in range(n):
        A[2 * i:2 * i + 2, 2 * i:2 * i + 2] = Mx
        for j in range(n):
            if j != i:
                A[2 * i:2 * i + 2, 2 * n + j] = AF @ Krel
    # fresh noise covariance
    Nz = np.zeros((dz, dz))
    for i in range(n):
        ei = slice(2 * i, 2 * i + 2)
        vi = 2 * n + i
        g_own = AF @ Kown
        Nz[ei, ei] += R * np.outer(g_own, g_own) + (n - 1) * Rc * np.outer(AF @ Krel, AF @ Krel) \
            + k_open * Rs * np.outer(AF @ Kslot, AF @ Kslot) + qc * np.eye(2)
        Nz[ei, vi] += R * g_own
        Nz[vi, ei] += R * g_own
        Nz[vi, vi] += R
    Sz = solve_discrete_lyapunov(A, Nz)
    idx = [2 * i for i in range(n)]
    return Sz[np.ix_(idx, idx)]


def mc_summary(out, n):
    al, be = compound(out.S)
    ab = np.array([compound(s) for s in out.S_batches])
    nb = len(ab)
    loo = np.array([r_ab(n, (ab[:, 0].sum() - ab[k, 0]) / (nb - 1), (ab[:, 1].sum() - ab[k, 1]) / (nb - 1))
                    for k in range(nb)])
    se_r = np.sqrt((nb - 1) / nb * np.sum((loo - loo.mean()) ** 2))
    se_b = ab[:, 1].std(ddof=1) / np.sqrt(nb)
    return al, be, r_ab(n, al, be), se_r, se_b


# (a)
pa = Par(qc=0.0, Rc=0.2)   # A8 reference parameters (Rc = 0.2)
Sx = exact_fixed(pa, 0)
al, be = compound(Sx)
print(f"(a) exact fixed, no slots, qc=0: alpha={al:.9f} beta={be:.9f} r={r_ab(4, al, be):.6f} "
      f"(max |S - compound| {np.abs(Sx - (al*np.eye(4)+be)).max():.1e}); A8 reference 7.425938")
o = run(pa, K=1000, T=260, burn=60, seed=11, mode="fixed", fixed_slots=0)
alm, bem, rm, ser, seb = mc_summary(o, 4)
print(f"    MC: alpha={alm:.6f} beta={bem:.6f} (SE {seb:.1e}) r={rm:.4f} +/- {ser:.4f}; z(r) = {(rm - r_ab(4, al, be))/ser:.2f}"
      f"  ({time.time()-t0:.0f}s)")
# (b)
pb = Par()
Sx = exact_fixed(pb, 2)
al, be = compound(Sx)
o = run(pb, K=1000, T=260, burn=60, seed=12, mode="fixed", fixed_slots=2)
alm, bem, rm, ser, seb = mc_summary(o, 4)
print(f"(b) exact fixed, 2 slots, qc=1e-4: alpha={al:.7f} beta={be:.7f} r={r_ab(4, al, be):.5f};  "
      f"MC alpha={alm:.6f} beta={bem:.6f} r={rm:.4f} +/- {ser:.4f}; z(r) = {(rm - r_ab(4, al, be))/ser:.2f}  ({time.time()-t0:.0f}s)")
# (c) NEGATIVE CONTROL: independent worlds
o = run(pa, K=500, T=260, burn=60, seed=13, mode="fixed", fixed_slots=0, shared_world=False)
alm, bem, rm, ser, seb = mc_summary(o, 4)
print(f"(c) NEG independent worlds: alpha={alm:.6f} beta={bem:.6f} r={rm:.3f} (must be far above 7.43)")
# (d) NEGATIVE CONTROL: dead relays
o = run(pa, K=500, T=260, burn=60, seed=14, mode="fixed", fixed_slots=0, dead_relays=True)
alm, bem, rm, ser, seb = mc_summary(o, 4)
print(f"(d) NEG dead relays: beta={bem:.2e} (SE {seb:.1e}), z(beta) = {bem/seb:.2f}; r={rm:.4f} +/- {ser:.4f}")
print(f"total {time.time()-t0:.1f}s")
