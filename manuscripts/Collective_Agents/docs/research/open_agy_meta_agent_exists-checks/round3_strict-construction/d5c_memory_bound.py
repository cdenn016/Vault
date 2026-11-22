r"""Deciding script D5c: upper bound on sup over all reachable paths of the per-step closure defect of the scalar
collective average, with members' configurations AND prior variances chosen independently.

Reduction (proved in the report): with Sigma = blockdiag(S_i) <= blockdiag(Sbar) (Sbar a common invariant bound) and
P1 = (1/4)(e1,e1,e1,e1), the monotonicity of Sigma -> Sigma_{x|y} gives
   d_cl <= 1/2 ln(1 + f),  f = [sum_i c_i - (sum_i b_i)^2 / (4 s)] / sum_i q_i,
   c_i = a_i^T Sbar a_i, b_i = e1^T Sbar a_i, s = Sbar_00, a_i = A_i^T e1, q_i = (Q_i)_00,
each member choosing (config, p_prev) from the option set independently.  max f by bisection on lam:
f* >= lam iff max_choices [sum_i (c_i - lam q_i) - (sum_i b_i)^2/(4s)] >= 0; the inner maximum is bounded above by a
max-plus convolution over bins of b (width res): the true sum B of a choice lies in [B_K, B_K + 4 res) for its bin
sum K, and the penalty is evaluated at the smallest |B| of that interval.
Sbar = c M with M - A M A^T > 0 on the whole option set (checked) and c = max lambda_max(Q relative to M - AMA^T).
Declared expectations: bound between the reachable worst 0.0266 (d5b) and the common-p bound 0.089 (d5b).
NEGATIVE CONTROL: the reduction formula with the actual sustained Sigma at the d5b worst pattern reproduces 0.0266.
"""
import time
import numpy as np
from lib3 import Pminus, A_F
from instance3 import PAR

t0 = time.time()
Af = A_F(PAR.F)


def member_mats(p_prev, own, ns, no, par=PAR):
    P00, P01, P11 = Pminus(par, p_prev)
    Pm = np.array([[P00, P01], [P01, P11]])
    Pp = np.linalg.inv(np.linalg.inv(Pm) + np.diag([1 / par.R + own / par.Rs,
                                                     ns / (par.R + par.Rc) + no / (par.Rs + par.Rc)]))
    Ai = Af @ Pp @ np.linalg.inv(Pm)
    krs = Pp[:, 1] / (par.R + par.Rc); kro = Pp[:, 1] / (par.Rs + par.Rc)
    Qi = Af @ (ns * par.Rc * np.outer(krs, krs) + no * par.Rc * np.outer(kro, kro)) @ Af.T + par.qc * np.eye(2)
    return Ai, Qi, Pp[0, 0]


def riccati(own, ns, no):
    p = PAR.p0
    for _ in range(3000):
        p = member_mats(p, own, ns, no)[2]
    return p


cfgs = [(o, ns, no) for o in (0, 1) for ns in range(4) for no in range(ns + 1)]
p_lo = riccati(1, 3, 3); p_hi = max(riccati(0, 0, 0), PAR.p0)
pgrid = np.linspace(p_lo, p_hi, 81)
OPT = [member_mats(pp, *c)[:2] for c in cfgs for pp in pgrid]
Aall = np.array([A for A, _ in OPT]); Qall = np.array([Q for _, Q in OPT])


def fbound(Sbar, nb=1500):
    s = Sbar[0, 0]
    a = Aall[:, 0, :]                                     # rows: a_i = A_i^T e1 = first row of A_i
    c = np.einsum("ki,ij,kj->k", a, Sbar, a)
    b = a @ Sbar[:, 0]
    q = Qall[:, 0, 0]
    bmin, bmax = b.min(), b.max() + 1e-15
    res = (bmax - bmin) / nb
    j = np.minimum(((b - bmin) / res).astype(int), nb - 1)

    def g(lam):
        w = c - lam * q
        W = np.full(nb, -np.inf)
        np.maximum.at(W, j, w)
        nz = np.nonzero(np.isfinite(W))[0]
        V = W.copy()
        for _ in range(3):
            Vn = np.full(len(V) + nb - 1, -np.inf)
            for jj in nz:
                np.maximum(Vn[jj:jj + len(V)], V + W[jj], out=Vn[jj:jj + len(V)])
            V = Vn
        K = np.arange(len(V))
        BK = 4 * bmin + K * res
        lo, hi = BK, BK + 4 * res
        Bc = np.where((lo <= 0) & (hi >= 0), 0.0, np.minimum(np.abs(lo), np.abs(hi)))
        return float(np.max(V - Bc ** 2 / (4 * s)))

    lo_l, hi_l = 0.0, 1.0
    while g(hi_l) >= 0:
        hi_l *= 2
    for _ in range(45):
        mid = 0.5 * (lo_l + hi_l)
        if g(mid) >= 0:
            lo_l = mid
        else:
            hi_l = mid
    return hi_l


def shape(pp, cf):
    A_w = member_mats(pp, *cf)[0]
    M = np.eye(2)
    for _ in range(3000):
        M = A_w @ M @ A_w.T + np.eye(2)
    return M


best = None
for pp, cf in ((p_hi, (0, 0, 0)), (p_lo, (1, 3, 3)), (0.5 * (p_lo + p_hi), (0, 3, 0)), (p_hi, (0, 3, 0))):
    M = shape(pp, cf)
    D = M[None] - np.einsum("kij,jl,kml->kim", Aall, M, Aall)
    ev = np.linalg.eigvalsh(D)
    if ev.min() <= 0:
        print(f"shape from {cf} at p={pp:.4f}: not a common Lyapunov bound (min eig {ev.min():.2e})")
        continue
    Ls = np.linalg.inv(np.linalg.cholesky(D))
    cmax = max(np.linalg.eigvalsh(L @ Q @ L.T).max() for L, Q in zip(Ls, Qall))
    fb = fbound(cmax * M)
    db = 0.5 * np.log1p(fb)
    print(f"shape from {cf} at p={pp:.4f}: c={cmax:.3e}, bound on sup d_cl {db:.4e}  ({time.time()-t0:.0f}s)", flush=True)
    if best is None or db < best:
        best = db
print(f"options: {len(cfgs)} configs x {len(pgrid)} p_prev values in [{p_lo:.4f}, {p_hi:.4f}], members independent")
print(f"UPPER BOUND on sup over reachable paths of d_cl(P1): {best:.4e}")
sb = (1, 1, 1, 0)
p = np.full(4, PAR.p0); Sb = [np.zeros((2, 2)) for _ in range(4)]
for _ in range(400):
    new = []
    for i in range(4):
        k1 = sum(sb[jj] for jj in range(4) if jj != i)
        Ai, Qi, ppp = member_mats(p[i], sb[i], 3, k1)
        Sb[i] = Ai @ Sb[i] @ Ai.T + Qi; new.append(ppp)
    p = np.array(new)
pat = [(0, 0, 0), (0, 0, 0), (0, 0, 0), (1, 3, 3)]
num = den = Bsum = Ssum = 0.0
for i, cf in enumerate(pat):
    A, Q, _ = member_mats(p[i], *cf)
    a = A[0, :]
    num += a @ Sb[i] @ a; Bsum += a @ Sb[i][:, 0]; Ssum += Sb[i][0, 0]; den += Q[0, 0]
print(f"NEG reduction check (base 1110, pattern {pat}): {0.5*np.log1p((num - Bsum**2/Ssum)/den):.4e} (d5b 2.6644e-02)")
print(f"total {time.time()-t0:.0f}s")
