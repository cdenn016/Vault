r"""(H2) vector-map check with roundoff control: per-step coordinatewise ratio and the
t-step ratio restricted to differences well above double-precision roundoff; plus the
Prop 4 coercivity bound at large gamma_C."""
from __future__ import annotations

import os
import sys

os.environ["OMP_NUM_THREADS"] = "1"
from math import comb

import numpy as np

LIB = r"C:\Users\chris and christine\Desktop\Research\manuscripts\Collective_Agents\docs\research\open_agy_meta_agent_exists-checks\round2_epistemic_persistent"
sys.path.insert(0, LIB)
import lib  # noqa: E402


def g_mob(F, Q, qc, a, b, p):
    Qp = Q + qc; K1 = F * F * qc + Qp
    return ((F * F + b * K1) * p + Qp * (1 + b * qc)) / ((a * F * F + b + a * b * K1) * p + (1 + a * Qp) * (1 + b * qc))


rng = np.random.default_rng(0)
worst_step = 0.0; worst_t = 0.0; worst_case = None
for trial in range(400):
    F = rng.uniform(0.1, 0.999); Q = rng.uniform(0.005, 1.0); R = rng.uniform(0.2, 3); Rc = rng.uniform(0.0, 1)
    Rs = rng.uniform(0.3, 4); qc = 10 ** rng.uniform(-5, -1)
    rho_bar = (F / (1 + (Q + qc) / R)) ** 2
    p = rng.uniform(0, 3, 4); pp = rng.uniform(0, 3, 4)
    d0 = np.abs(p - pp).max()
    for t in range(1, 41):
        if rho_bar ** t * d0 < 1e-8:
            break
        nvis = rng.integers(0, 5); a = 1 / R + nvis / Rs
        prev = np.abs(p - pp)
        for i in range(4):
            b = rng.integers(0, 4) / (R + Rc)
            p[i] = g_mob(F, Q, qc, a, b, p[i]); pp[i] = g_mob(F, Q, qc, a, b, pp[i])
        cur = np.abs(p - pp)
        mask = prev > 1e-9
        if mask.any():
            worst_step = max(worst_step, float((cur[mask] / prev[mask]).max() / rho_bar))
        r = cur.max() / (rho_bar ** t * d0)
        if r > worst_t:
            worst_t = r; worst_case = (F, Q, R, Rc, Rs, qc, t, cur.max(), rho_bar ** t * d0)
print("max per-step coordinate ratio / rho_bar   :", worst_step)
print("max t-step sup ratio / (rho_bar^t d0)     :", worst_t)
print("case attaining it (F,Q,R,Rc,Rs,qc,t,diff,bound):", worst_case)

# Same with lib.posterior (as cited), restricted the same way
worst_lib = 0.0
rng = np.random.default_rng(1)
for trial in range(100):
    F = rng.uniform(0.1, 0.999); Q = rng.uniform(0.005, 1.0); R = rng.uniform(0.2, 3); Rc = rng.uniform(0.0, 1)
    Rs = rng.uniform(0.3, 4); qc = 10 ** rng.uniform(-5, -1)
    par = lib.Par().with_(F=F, Q=Q, R=R, Rc=Rc, Rs=Rs, qc=qc)
    rho_bar = (F / (1 + (Q + qc) / R)) ** 2
    p = rng.uniform(0, 3, 4); pp = rng.uniform(0, 3, 4); d0 = np.abs(p - pp).max()
    for t in range(1, 41):
        if rho_bar ** t * d0 < 1e-8:
            break
        nvis = rng.integers(0, 5); a = 1 / R + nvis / Rs
        for i in range(4):
            b = rng.integers(0, 4) / (R + Rc)
            p[i] = lib.posterior(lib.Pminus(par, p[i]), a, b)[0, 0]
            pp[i] = lib.posterior(lib.Pminus(par, pp[i]), a, b)[0, 0]
        worst_lib = max(worst_lib, np.abs(p - pp).max() / (rho_bar ** t * d0))
print("lib.posterior: max t-step sup ratio       :", worst_lib)

# Prop 4 coercivity at large gamma_C (symmetric X = 0.09, slot component, vC = member variance)
par = lib.Par().with_(Rc=0.1)
w = lib.attention_weights(par, 3, par.n_zero); mmax = len(w) - 1
Gt = lib.softmin_att(par, lib.efe_table(par, lib.Pminus(par, 0.09), mmax, 4), w)
Pn = lib.gibbs_law_sym(par.gamma, Gt, 4)
binom = np.array([comb(4, k) for k in range(5)], float)
vC = lib.posterior(lib.Pminus(par, 0.09), 1 / par.R, mmax / (par.R + par.Rc))[0, 0]
n = np.arange(5); GC = -0.5 * np.log(1 + n * vC / par.Rs) + par.psi * n
amin = int(np.argmin(GC))
print("G_C(n) =", GC, " argmin n =", amin)
for off in [k for k in range(5) if k != amin][:2]:
    Delta = GC[off] - GC[amin]
    for gC in (1e3, 1e4, 1e5, 1e6):
        lw = np.log(binom) - gC * GC; lw -= lw.max(); q = np.exp(lw); q /= q.sum()
        kl = float(np.sum(Pn * np.log(Pn / q)))
        bound = (Pn[off] / binom[off]) * gC * Delta - np.log(16)
        print(f"  off n={off} Delta={Delta:.3e} gamma_C={gC:.0e}: KL={kl:.6e} bound={bound:.6e} holds={kl >= bound - 1e-9}")
