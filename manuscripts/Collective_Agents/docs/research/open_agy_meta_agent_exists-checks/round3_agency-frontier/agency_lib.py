r"""Agency-index functions extracted verbatim from d1_agency.py (no module-level runs)."""
import itertools
import numpy as np
from scipy.optimize import minimize_scalar, minimize
from flib import Par, canonical_types, steady_prior, efe_grid, kl_terms_member, member_policy_law, log_binom, post


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


