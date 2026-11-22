r"""a7: partner randomization drawn ONCE (quenched), which tab:agy-nulls also
permits ("once or every round"), for the CCP: exact enumeration of all 3^4 = 81
partner assignments (each member reads one of the three others), zero-gain and
kept-gain conventions.  Statistic: the largest contrast over all regions (and the
firm-pair contrasts), computed when the quenched precision is diffusive.

Declared expectations (before running):
 E1 zero-gain: every assignment is diffusive (block diagonal); the assignments in
    which some firm's two members read each other reproduce that firm's full-model
    block exactly, so S = S_0 = 4.3336 there; P(S >= S_0) = 1 - (8/9)^2 = 17/81 =
    0.210, so the test of prop:agy-tests(b) with 999 draws gives p near 0.21 > 0.01.
 E2 NEGATIVE CONTROL: the identity assignment (everyone reads its mate) gives S_0.
 E3 kept-gain: some assignments are non-diffusive; I report the fraction and
    P(S >= S_0) among the diffusive ones.
"""
import itertools
import numpy as np
from ccp_lib import *
import io, contextlib
with contextlib.redirect_stdout(io.StringIO()):
    import a2b_npr_kept as KG     # my 4-agent kept-gain system (its demo output suppressed)

p = default_params()
Phi, Qw, Gm = world_mats(p)
kap = p["kappa"]
filt_rel = member_filters(p)
filt_own = member_filters(p, relay=False)
role = ["b", "s", "b", "s"]; mate = [1, 0, 3, 2]; firm = [0, 0, 1, 1]
S0 = 4.33360016


def zero_gain_cov(assign):
    """Time-invariant 4-agent system; a member whose partner is its mate runs the
    full (relay) filter, otherwise the own-sensor-only filter (zero gain)."""
    NXa, NXIa = 20, 30
    A = np.zeros((NXa, NXa)); B = np.zeros((NXa, NXIa)); Cm = np.zeros((2, NXa)); Dm = np.zeros((2, NXIa))
    for j in range(4):
        reads_mate = assign[j] == mate[j]
        f = filt_rel[role[j]] if reads_mate else filt_own[role[j]]
        K, H = f["K"], f["H"]
        M = np.eye(4) - K @ H
        ZpS = np.zeros((4, NXa)); ZpS[:, 4 * j:4 * j + 4] = M
        ZpX = np.zeros((4, NXIa)); ZpX[:, j] += K[:, 0]
        if reads_mate:
            ZpS[:, 16 + mate[j]] += K[:, 1]
            ZpX[:, 4 + j] += K[:, 1]
        A[4 * j:4 * j + 4] = Phi @ ZpS
        B[4 * j:4 * j + 4] = Phi @ ZpX
        B[4 * j:4 * j + 4, 8 + 4 * j:12 + 4 * j] += np.eye(4)
        Cm[firm[j]] += -kap * D @ ZpS
        Dm[firm[j]] += -kap * D @ ZpX
        Dm[firm[j], 24 + j] += 1.0
    for j in range(4):
        B[16 + j, j] = 1.0
    Dm[0, 28] += 1.0; Dm[1, 29] += 1.0
    return A, B, Cm, Dm


def cond_cov_multi(A, B, Cm, Dm, qv, T, L=50):
    nx, nxi = B.shape
    S0c = solve_discrete_lyapunov(A, B @ np.diag(qv) @ B.T)
    nsteps = 2 * L + 1
    dimU = nx + nxi * nsteps
    coef = np.zeros((nx, dimU)); coef[:, :nx] = np.eye(nx)
    no = Cm.shape[0]
    O = np.zeros((no * nsteps, dimU)); tgt = None
    for k in range(nsteps):
        if k == L:
            tgt = T @ coef
        cx = np.zeros((nxi, dimU)); cx[:, nx + k * nxi:nx + (k + 1) * nxi] = np.eye(nxi)
        O[no * k:no * k + no] = Cm @ coef + Dm @ cx
        coef = A @ coef + B @ cx
    dg = np.tile(qv, nsteps)
    cov = lambda X, Y: X[:, :nx] @ S0c @ Y[:, :nx].T + (X[:, nx:] * dg) @ Y[:, nx:].T
    Soo = cov(O, O); Sto = cov(tgt, O); Stt = cov(tgt, tgt)
    return Stt - Sto @ np.linalg.solve(Soo, Sto.T)


def stat(Sig):
    Pi = np.linalg.inv(Sig)
    if not is_diffusive(Pi):
        return None, None
    rs = {C: rates(Pi, C)[2] for C in all_regions(4)}
    return max(rs.values()), (rs[(0, 1)], rs[(2, 3)])


qv, Tsel = KG.qv, KG.Tsel
others = [[q for q in range(4) if q != j] for j in range(4)]
res = {"zero": [], "kept": []}
for assign in itertools.product(*others):
    A, B, Cm, Dm = zero_gain_cov(assign)
    res["zero"].append((assign, stat(cond_cov_multi(A, B, Cm, Dm, qv, Tsel))))
    A2, B2, C2, D2_ = KG.step_mats(list(assign))
    res["kept"].append((assign, stat(cond_cov_multi(A2, B2, C2, D2_, qv, Tsel))))

ident = tuple(mate)
for conv in ("zero", "kept"):
    rows = res[conv]
    nd = [r for r in rows if r[1][0] is not None]
    ge = [r for r in nd if r[1][0] >= S0 - 1e-6]
    print("%s-gain quenched: %d/81 diffusive; #(S >= S_0) = %d among diffusive; P(S >= S_0) over all 81 = %.4f (non-diffusive counted as S < S_0)"
          % (conv, len(nd), len(ge), len(ge) / 81))
    print("   largest S among diffusive assignments: %.4f" % max(r[1][0] for r in nd))
    for r in rows:
        if r[0] == ident:
            print("   E2 identity assignment:", r[1])
    if conv == "zero":
        ex = [r for r in rows if r[0][0] == 1 and r[0][1] == 0 and r[0][2] != 3]
        print("   example (firm 1 mutual, firm 2 not):", ex[0])
