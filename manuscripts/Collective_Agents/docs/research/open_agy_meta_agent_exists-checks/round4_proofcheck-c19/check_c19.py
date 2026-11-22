r"""Checks for claim C19: Riccati Moebius form, derivative bound, rank-one closed loop,
vector-map contraction, contrast formulas, Cramer system, Prop 4 coercivity, gamma->0 index limit.
Single-threaded, small. Imports lib.py read-only."""
from __future__ import annotations

import os
import sys

os.environ["OMP_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
import itertools
from math import comb

import numpy as np

LIB = r"C:\Users\chris and christine\Desktop\Research\manuscripts\Collective_Agents\docs\research\open_agy_meta_agent_exists-checks\round2_epistemic_persistent"
sys.path.insert(0, LIB)
import lib  # noqa: E402

np.set_printoptions(precision=6, suppress=False, linewidth=140)


def mobius(F, Q, qc, a, b):
    Qp = Q + qc
    K1 = F * F * qc + Qp
    c1 = F * F + b * K1
    c0 = Qp * (1 + b * qc)
    d1 = a * F * F + b + a * b * K1
    d0 = (1 + a * Qp) * (1 + b * qc)
    return c1, c0, d1, d0


def g_lib(par, p, a, b):
    return lib.posterior(lib.Pminus(par, p), a, b)[0, 0]


print("=== A-D: Moebius coefficients, determinant identity, derivative, rank-one closed loop ===")
pts = [
    dict(F=0.9, Q=0.05, R=1.0, Rc=0.1, Rs=2.0, qc=1e-4, p=0.09, nvis=2, nrel=3),
    dict(F=0.5, Q=0.2, R=0.7, Rc=0.3, Rs=1.5, qc=1e-2, p=0.0, nvis=0, nrel=0),
    dict(F=0.99, Q=0.01, R=2.0, Rc=0.05, Rs=3.0, qc=1e-3, p=1.7, nvis=4, nrel=1),
    dict(F=0.3, Q=1.0, R=0.5, Rc=0.5, Rs=0.8, qc=0.2, p=0.4, nvis=1, nrel=2),
]
for d in pts:
    par = lib.Par().with_(F=d["F"], Q=d["Q"], R=d["R"], Rc=d["Rc"], Rs=d["Rs"], qc=d["qc"])
    a = 1.0 / par.R + d["nvis"] / par.Rs
    b = d["nrel"] / (par.R + par.Rc)
    p = d["p"]
    c1, c0, d1, d0 = mobius(par.F, par.Q, par.qc, a, b)
    g_m = (c1 * p + c0) / (d1 * p + d0)
    g_l = g_lib(par, p, a, b)
    det_lhs = c1 * d0 - c0 * d1
    det_rhs = par.F ** 2 * (1 + b * par.qc) ** 2
    h = 1e-6
    gp_fd = (g_lib(par, p + h, a, b) - g_lib(par, max(p - h, 0.0), a, b)) / (p + h - max(p - h, 0.0))
    gp_formula = det_rhs / (d1 * p + d0) ** 2
    bound1 = par.F ** 2 / (1 + a * (par.Q + par.qc)) ** 2
    rho_bar = (par.F / (1 + (par.Q + par.qc) / par.R)) ** 2
    Pm = lib.Pminus(par, p)
    Mx, _, _, Pp, _ = lib.round_mats(par, Pm, d["nrel"], d["nvis"])
    sv = np.linalg.svd(Mx, compute_uv=False)
    u = np.array([par.F, 1.0])
    v = (Pp @ np.linalg.inv(Pm))[0, :]  # Mx = u v^T since A_F = u e_1^T
    lam = v @ u
    lam_formula = par.F * (1 + b * par.qc) / (d1 * p + d0)
    print(f"pt F={par.F} Q={par.Q} R={par.R} Rc={par.Rc} Rs={par.Rs} qc={par.qc} p={p} a={a:.4f} b={b:.4f}")
    print(f"  g: lib={g_l:.15e} mobius={g_m:.15e} diff={g_l - g_m:.2e}")
    print(f"  c1d0-c0d1={det_lhs:.15e} F^2(1+bqc)^2={det_rhs:.15e} diff={det_lhs - det_rhs:.2e}")
    print(f"  g'(fd)={gp_fd:.10e} g'(formula)={gp_formula:.10e} F^2/(1+aQ')^2={bound1:.6e} rho_bar={rho_bar:.6e}"
          f" ok={gp_formula <= bound1 + 1e-15 <= rho_bar + 1e-15}")
    print(f"  Mx singular values={sv}  |Mx - u v^T|={np.abs(Mx - np.outer(u, v)).max():.2e}")
    print(f"  lambda=v.u={lam:.15e} formula={lam_formula:.15e} lambda^2={lam ** 2:.12e} g'={gp_formula:.12e}")

print("\n=== (H1) monotonicity of g on a grid (increasing in p, decreasing in a, b) ===")
par = lib.Par().with_(Rc=0.1)
viol = 0
for p in np.linspace(0, 2, 21):
    for nv in range(5):
        for nr in range(4):
            a = 1 / par.R + nv / par.Rs
            b = nr / (par.R + par.Rc)
            g0 = g_lib(par, p, a, b)
            if g_lib(par, p + 0.01, a, b) < g0 - 1e-15: viol += 1
            if nv < 4 and g_lib(par, p, a + 1 / par.Rs, b) > g0 + 1e-15: viol += 1
            if nr < 3 and g_lib(par, p, a, b + 1 / (par.R + par.Rc)) > g0 + 1e-15: viol += 1
print("monotonicity violations:", viol)

print("\n=== E: (H2) vector map along random policy sequences, n=4, C1=1 ===")
rng = np.random.default_rng(0)
worst = 0.0
for trial in range(200):
    F = rng.uniform(0.1, 0.999); Q = rng.uniform(0.005, 1.0); R = rng.uniform(0.2, 3); Rc = rng.uniform(0.0, 1)
    Rs = rng.uniform(0.3, 4); qc = 10 ** rng.uniform(-5, -1)
    par = lib.Par().with_(F=F, Q=Q, R=R, Rc=Rc, Rs=Rs, qc=qc)
    rho_bar = (F / (1 + (Q + qc) / R)) ** 2
    p = rng.uniform(0, 3, 4); pp = rng.uniform(0, 3, 4)
    d0 = np.abs(p - pp).max()
    for t in range(1, 31):
        if rho_bar ** t * d0 < 1e-8:  # below this the computed difference is double-precision roundoff
            break
        nvis = rng.integers(0, 5)
        a = 1 / R + nvis / Rs
        for i in range(4):
            b = rng.integers(0, 4) / (R + Rc)
            p[i] = g_lib(par, p[i], a, b); pp[i] = g_lib(par, pp[i], a, b)
        ratio = np.abs(p - pp).max() / (rho_bar ** t * d0)
        worst = max(worst, ratio)
print("max over trials/t of |G^t p - G^t p'|_inf / (rho_bar^t |p-p'|_inf):", worst)

print("\n=== F: ||A_F^k|| = F^(k-1) sqrt(1+F^2) ===")
for F in (0.3, 0.9):
    AF = lib.A_F(F)
    errs = [abs(np.linalg.norm(np.linalg.matrix_power(AF, k), 2) - F ** (k - 1) * np.sqrt(1 + F * F)) for k in range(1, 8)]
    print(F, max(errs))

print("\n=== G: contrast formulas, alpha=1, beta=0.5 (x=0.5) and alpha=0.7, beta=0.13 ===")
for al, be in ((1.0, 0.5), (0.7, 0.13)):
    x = be / al
    SA = al * np.eye(4) + be * np.ones((4, 4))
    S = np.block([[SA, np.zeros((4, 4))], [np.zeros((4, 4)), SA]])
    Pi = np.linalg.inv(S)
    a_ = -Pi[0, 1]; eps = Pi.sum(1)[0]
    print(f" x={x}: a/eps={a_ / eps:.12f}  cross coupling max={np.abs(Pi[:4, 4:]).max():.1e}  diffusive={lib.diffusive(Pi)[0]}")
    rc = lib.region_contrasts(Pi)
    rA = rc[(0, 1, 2, 3)]
    r3 = rc[(0, 1, 2)]; r2 = rc[(0, 1)]
    mixed = max(v for C, v in rc.items() if any(c < 4 for c in C) and any(c >= 4 for c in C))
    print(f"  r(A)={rA:.12f} vs 1+4x={1 + 4 * x:.12f}; r3={r3:.12f} vs {(1 + 3 * x) / (1 + x):.12f}; r2={r2:.12f}; max mixed={mixed:.12f}")
    abar = 12 * a_ / 28
    Pih = -abar * np.ones((8, 8)); np.fill_diagonal(Pih, 0.0)
    Pih = Pih + np.diag(eps - Pih.sum(1))
    rch = lib.region_contrasts(Pih)
    print(f"  mean-coupling medium: abar/a={abar / a_:.12f} (3/7={3 / 7:.12f}); sup r={max(rch.values()):.12f} vs 1+24x/7={1 + 24 * x / 7:.12f}")

print("\n=== H: (P4) Cramer system at the base point (gamma=400) ===")
par = lib.Par().with_(Rc=0.1)
w = lib.attention_weights(par, 3, par.n_zero)
mmax = len(w) - 1
for pX in ([0.09] * 4, [0.08, 0.09, 0.10, 0.11], [0.05, 0.2, 0.3, 0.6]):
    Gt = np.array([lib.softmin_att(par, lib.efe_table(par, lib.Pminus(par, pi), mmax, 4), w) for pi in pX])
    law, T = lib.p4_chain(par.gamma, Gt)
    Aeq = T.T - np.eye(16); Aeq[-1, :] = 1.0
    # number of transitions that are mathematically positive (one-flip moves) but numerically zero
    P_, idx = lib._prof(4)
    zero_moves = 0
    for k in range(16):
        for i in range(4):
            kk = idx[tuple(np.where(np.arange(4) == i, 1 - P_[k], P_[k]))]
            if T[k, kk] == 0.0: zero_moves += 1
    dG = np.array([[Gt[i, s + 1] - Gt[i, s] for s in range(4)] for i in range(4)])
    print(f" pX={pX}: gamma*|dGt| range=[{par.gamma * np.abs(dG).min():.2f},{par.gamma * np.abs(dG).max():.2f}]"
          f" cond(Aeq)={np.linalg.cond(Aeq):.3e} min law={law.min():.3e} zero one-flip moves={zero_moves}/64")

print("\n=== I/J: Prop 4 coercivity bound and the gamma->0 limit of the index (symmetric X, slot component) ===")


def law_sym(gamma, Gt_row):
    return lib.gibbs_law_sym(gamma, Gt_row, 4)  # law of n = |sigma|; profile law is this / C(4,n)


binom = np.array([comb(4, k) for k in range(5)], float)
E_n = binom / 16.0  # habit law of n under uniform product habits


def kl_n(P, Qd):
    m = P > 0
    return float(np.sum(P[m] * np.log(P[m] / Qd[m])))  # KL on profiles = KL on n when both are exchangeable


def group_law(gC, GC):
    lw = np.log(binom) - gC * GC
    lw -= lw.max(); q = np.exp(lw)
    return q / q.sum()


def agency(gamma, pX, vC, par):
    Gt = lib.softmin_att(par.with_(gamma=gamma), lib.efe_table(par, lib.Pminus(par, pX), mmax, 4), w) if gamma > 0 else None
    if gamma == 0:
        return 1.0, None
    P = law_sym(gamma, Gt)
    den = kl_n(P, E_n)
    n = np.arange(5)
    GC = -0.5 * np.log(1 + n * vC / par.Rs) + par.psi * n
    lo, hi = 0.0, 1.0
    while kl_n(P, group_law(hi, GC)) < kl_n(P, group_law(hi / 2, GC)) or hi < 4 * gamma:
        hi *= 2
        if hi > 1e7: break
    for _ in range(200):  # ternary search, KL convex in gamma_C
        m1 = lo + (hi - lo) / 3; m2 = hi - (hi - lo) / 3
        if kl_n(P, group_law(m1, GC)) < kl_n(P, group_law(m2, GC)): hi = m2
        else: lo = m1
    gbest = 0.5 * (lo + hi)
    num = kl_n(P, group_law(gbest, GC))
    return 1 - num / den, (P, GC, gbest, num, den)


par = lib.Par().with_(Rc=0.1)
pX = 0.09
Pm = lib.Pminus(par, pX)
vC = lib.posterior(Pm, 1 / par.R, mmax / (par.R + par.Rc))[0, 0]  # member variance after own + all relays
print(f" declared vC (own + {mmax} relays at p_X={pX}) = {vC:.6f}")
# coercivity bound check at gamma=400
A400, (P, GC, gb, num, den) = agency(400.0, pX, vC, par)
off = int(np.argmax(GC)); amin = int(np.argmin(GC)); Delta = GC[off] - GC[amin]
for gC in (0.0, 10.0, 100.0, 1000.0, 5000.0):
    lhs = kl_n(P, group_law(gC, GC))
    Poff = P[off] / binom[off]  # profile probability of one profile with |sigma|=off
    rhs = Poff * (gC * Delta - 0.0) - np.log(16)
    print(f"  gamma_C={gC:7.1f}: KL={lhs:.6e} >= bound={rhs:.6e} : {lhs >= rhs - 1e-12}")
print(f"  gamma=400: Agency={A400:.10f} best gamma_C={gb:.4f} den={den:.4e}")
for vCc, lab in ((vC, "vC=member"), (0.5, "vC=0.5"), (par.Rs, "vC=Rs")):
    vals = []
    for g in (1e-1, 1e-2, 1e-3, 1e-4):
        Ag, _ = agency(g, pX, vCc, par)
        vals.append((g, Ag))
    print(f"  {lab}: " + "  ".join(f"A(gamma={g:g})={Ag:.10f}" for g, Ag in vals) + "  A(0)=1 by definition")
