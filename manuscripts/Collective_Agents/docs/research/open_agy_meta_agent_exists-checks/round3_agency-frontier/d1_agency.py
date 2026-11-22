r"""D1 deciding run 5: agency index under the full-policy reading (O2(e) yes) at the stationary decision state X*,
and the frontier in the slot-array size m and the attention support size |S|.

Index (def:agy-agency-index, 05_agency.tex:240-246) with habits held fixed (uniform on the attention support and on
{0,1}^m), so every model of the class is P_g = E^a (x) P^s_g and (C12)
   Agency = 1 - [KL_a + E_{P_a} KL(P_{s|a} || P^s_g*)] / [KL_a + KL_{s|a}].
P^s_g over the collective's n m slots: propto exp(-gamma_C G_C(K)), G_C(K) = -1/2 ln(1 + K v_C/Rs) + psi K,
K = total open slots; class G2: v_C = v* (member's anticipated variance of eta_{t+1} after own sensor and its
relays), G1: v_C free; gamma_C in [0, inf).  Both laws are uniform over slot patterns given the count vector, so the
KL reduces to count vectors (exact Vandermonde normalization of the group law).
Declared expectations (before running): D1 (n=2, |S|=4, m=8): KL_a = 2 ln 4 = 2.773, KL_{s|a} = 16 ln 2 = 11.09,
slot misfit < 1e-8, index = 0.8 to 4 digits (formula m/(m + log2|S|)).  Frontier follows
m ln2 / (m ln2 + ln(|S|/|S*|)) within 1e-4 for every row.
NEGATIVE CONTROLS: (a) the I*-like attention support (n=4, |S|=64) with one costly slot per member must give about
1/7 = 0.143; (b) a class whose belief makes the group open slots (v_C = 1e4, G2 frozen at that v_C) must fit the slot
law no better than the habit-only model, index about 0 (the class matters); (c) the habit-null law has KL(P||E)=0.
"""
import time
import itertools
import numpy as np
from scipy.optimize import minimize_scalar, minimize
from flib import Par, canonical_types, steady_prior, efe_grid, kl_terms_member, member_policy_law, log_binom, post
from design import make_design

t0 = time.time()


def design(n: int, types, m: int, Rs: float = 10.0, margin: float = 0.06) -> Par:
    base = Par(F=0.9, Q=0.05, R=1.0, Rc=0.1, Rs=Rs, psi=0.0, gamma=400.0, qc=1e-4, n=n, n_zero=n, m=m, types=types)
    gmax = 0.0
    for c in range(n):
        Pm = steady_prior(base, c, 0)
        for cc in range(n):
            G = efe_grid(base, Pm[0, 0], Pm[0, 1], Pm[1, 1], np.array([cc]), np.array([0, 1]))
            gmax = max(gmax, float(G[0, 0] - G[0, 1]))
    return base.with_(psi=gmax + margin)


def index(par: Par, kmax: int = 2, vfix: float | None = None, free_v: bool = False):
    n, m = par.n, par.m
    cstar = max(c for c, _ in par.types)
    Pm = steady_prior(par, cstar, 0)
    KLa1, KLs1, P, G = kl_terms_member(par, Pm)
    KLa, KLs = n * KLa1, n * KLs1
    pa = P.sum(1)
    pk_given = [P[t] / pa[t] for t in range(len(pa))]
    vstar = post(Pm, 1.0 / par.R, cstar / (par.R + par.Rc))[0, 0] * par.F ** 2 + par.Q   # anticipated var of eta_{t+1}
    # exact: v* = variance of eta_{t+1} under the member's prior after own sensor and relays of round t+1
    Pp = np.linalg.inv(np.linalg.inv(Pm) + np.diag([1.0 / par.R, cstar / (par.R + par.Rc)]))
    vstar = Pp[0, 0]
    lb = log_binom(m)
    kk = np.arange(min(kmax, m) + 1)
    vecs = np.array(list(itertools.product(kk, repeat=n)))
    Ktot = vecs.sum(1)
    Kall = np.arange(n * m + 1)
    lbN = log_binom(n * m)
    # actual count-vector laws for each attention-type vector, weighted
    tvecs = list(itertools.product(range(len(pa)), repeat=n))
    acts, wts = [], []
    for tv in tvecs:
        wt = float(np.prod([pa[t] for t in tv]))
        if wt < 1e-300:
            continue
        lp = np.sum([np.log(np.maximum(pk_given[tv[i]][vecs[:, i]], 1e-300)) for i in range(n)], axis=0)
        acts.append(lp); wts.append(wt)
    acts = np.array(acts); wts = np.array(wts)
    tail = 1 - np.exp(acts).sum(1)                     # truncated mass per type vector

    def misfit(gC, vC):
        GC = -0.5 * np.log1p(Kall * vC / par.Rs) + par.psi * Kall
        lZ = np.logaddexp.reduce(lbN - gC * GC)
        lg = np.sum(lb[vecs], axis=1) - gC * GC[Ktot] - lZ
        return float(np.sum(wts * np.sum(np.exp(acts) * (acts - lg[None, :]), axis=1)))
    if free_v:
        f = lambda z: misfit(np.exp(z[0]), np.exp(z[1]))
        best = min((minimize(f, [np.log(g0), np.log(v0)], method="Nelder-Mead",
                             options=dict(xatol=1e-10, fatol=1e-16, maxiter=20000))
                    for g0 in (100.0, 400.0, 2000.0) for v0 in (0.01, vstar, 1.0)), key=lambda z: z.fun)
        mis, gbest, vbest = best.fun, float(np.exp(best.x[0])), float(np.exp(best.x[1]))
    else:
        vC = vstar if vfix is None else vfix
        rr = minimize_scalar(lambda z: misfit(np.exp(z), vC), bounds=(-10, 12), method="bounded",
                             options=dict(xatol=1e-10))
        mis, gbest, vbest = rr.fun, float(np.exp(rr.x)), vC
        mis = min(mis, misfit(0.0, vC))                 # gamma_C = 0 (habit-only model) is in the class
    mis = max(mis, 0.0)
    mis = min(mis, KLs)
    idx = 1 - (KLa + mis) / (KLa + KLs)
    return dict(idx=idx, slot_only=1 - mis / KLs if KLs > 0 else 1.0, KLa=KLa, KLs=KLs, mis=mis, gC=gbest, vC=vbest,
                vstar=vstar, tail=float(np.max(tail)), Ssize=sum(mu for _, mu in par.types),
                Sstar=sum(mu for c, mu in par.types if c == cstar))


D1, _ = make_design()
res = index(D1)
res1 = index(D1, free_v=True)
print(f"D1 (n=2, |S|=4, m=8, Rs=10): KL_a {res['KL_a' if False else 'KLa']:.6f}, KL_s|a {res['KLs']:.6f}, "
      f"slot misfit G2 {res['mis']:.3e} (gamma_C {res['gC']:.1f}, v* {res['vstar']:.5f}); "
      f"index G2 {res['idx']:.6f}; G1 {res1['idx']:.6f}; slot-only G2 {res['slot_only']:.8f}; truncation tail {res['tail']:.1e}")
print(f"   formula m ln2/(m ln2 + ln|S|) = {8*np.log(2)/(8*np.log(2)+np.log(4)):.6f}   ({time.time()-t0:.0f}s)")
# frontier
rows = [("n=2 |S|=4 canonical", 2, canonical_types(1, 2, 1)),
        ("n=2 |S|=3 {mate,o1,o2}", 2, ((0, 2), (1, 1))),
        ("n=2 |S|=2 {mate,o1}", 2, ((0, 1), (1, 1))),
        ("n=4 |S|=64 canonical", 4, canonical_types(3, 4, 3)),
        ("n=4 |S|=2 {mates,z}", 4, ((0, 1), (3, 1)))]
print("frontier: index (G2) by m; formula in brackets")
for lab, n, tps in rows:
    line = []
    for m in (1, 2, 3, 4, 8, 18, 50):
        p = design(n, tps, m)
        r = index(p, kmax=2 if n == 2 else 1)
        S = r["Ssize"] / r["Sstar"]
        fo = m * np.log(2) / (m * np.log(2) + np.log(S))
        line.append(f"m={m}: {r['idx']:.4f} [{fo:.4f}]")
    print(f"  {lab}: " + "; ".join(line) + f"  ({time.time()-t0:.0f}s)")
# negative controls
pa_ = design(4, canonical_types(3, 4, 3), 1)
ra = index(pa_, kmax=1)
print(f"NEG (a) I*-like support n=4 |S|=64, one costly slot: index {ra['idx']:.4f} (expected about 0.143)")
rb = index(D1, vfix=1e4)
print(f"NEG (b) class frozen at v_C = 1e4 (group would open slots): slot misfit {rb['mis']:.4f} of KL_s {rb['KLs']:.4f}; "
      f"index {rb['idx']:.4f} (expected about 0)")
ph = D1.with_(gamma=0.0)
KLa_h, KLs_h, _, _ = kl_terms_member(ph, steady_prior(ph, 1, 0))
print(f"NEG (c) habit-null law: KL_a {KLa_h:.2e}, KL_s|a {KLs_h:.2e} (must be 0)")
print(f"total {time.time()-t0:.1f}s")
