r"""Deciding script 4b: agency index under the real-time (P4) protocol (one deliberation event per round, no message
faster than one round), at decision states = symmetric covariance states binned by the members' posterior
variance p.  The actual conditional law P(pi(t+1) | X(t)) is estimated from long simulated policy paths (law of the
number of open slots; exchangeability within the niche checked).
Declared expectations: the empirical law at the median bin is close to, but not equal to, the Gibbs law at the
bin's p (feedback between profile and covariance); index in G1 and G2 above 0.99 at the median bin; departure from
habits positive; log odds ratio negative (not a product law).  NEGATIVE CONTROL: the same estimator applied to the
habit null (gamma = 0) gives a law within sampling error of the uniform habits (KL to habits below 5e-4).
"""
import time
import numpy as np
from math import comb
from scipy.optimize import minimize, minimize_scalar
from lib import (Pminus, posterior, efe_table, softmin_att, attention_weights, simulate_policy_path_real,
                 gibbs_law_sym)
from instance import PAR

t0 = time.time()
w = attention_weights(PAR, 3, 4)


def collect(mode, nrounds, seed, sym_only=True):
    rng = np.random.default_rng(seed)
    P, N, M0 = [], [], []
    per = 5000
    for k in range(nrounds // per):
        _, dec = simulate_policy_path_real(PAR, per, rng, mode, record_dec=True)
        for t, pv, prof in dec[100:]:
            if (not sym_only) or np.ptp(pv) < 1e-12:
                P.append(pv[0]); N.append(int(prof.sum())); M0.append(prof)
    return np.array(P), np.array(N), np.array(M0)


P, N, M0 = collect("full", 240000, 9101)
print(f"symmetric decision rounds: {len(P)}; P(open) by member {np.round(M0.mean(0), 4)}  ({time.time()-t0:.0f}s)")
qs = np.quantile(P, [0.05, 0.15, 0.45, 0.55, 0.85, 0.95])
bins = {"10%": (qs[0], qs[1]), "50%": (qs[2], qs[3]), "90%": (qs[4], qs[5])}
cnt_law, pmed = {}, {}
for b, (lo, hi) in bins.items():
    sel = (P >= lo) & (P <= hi)
    c = np.bincount(N[sel], minlength=5) / sel.sum()
    cnt_law[b] = c; pmed[b] = float(np.median(P[sel]))
    g = gibbs_law_sym(PAR.gamma, softmin_att(PAR, efe_table(PAR, Pminus(PAR, pmed[b]), 3, 4), w), 4)
    print(f"bin {b}: n={sel.sum()}, p median {pmed[b]:.5f}; law of open count {np.round(c, 4)}; "
          f"Gibbs at that p {np.round(g, 4)}")


def kl_counts(c, q):
    m = c > 0
    return float(np.sum(c[m] * np.log(c[m] / q[m])))


hab_c = np.array([comb(4, k) for k in range(5)]) / 16.0


def group_counts(vC, gC):
    n = np.arange(5)
    G = -0.5 * np.log1p(n * vC / (PAR.Rs + PAR.Rsh)) + PAR.psi * n
    lw = np.log([comb(4, k) for k in range(5)]) - gC * G
    lw -= lw.max(); q = np.exp(lw)
    return q / q.sum()


def index(laws, vfix=None):
    den = np.mean([kl_counts(c, hab_c) for c in laws])
    if vfix is None:
        obj = lambda z: np.mean([kl_counts(c, group_counts(np.exp(z[0]), np.exp(z[1]))) for c in laws])
        best = min((minimize(obj, [np.log(v0), np.log(g0)], method="Nelder-Mead",
                             options=dict(xatol=1e-10, fatol=1e-14, maxiter=20000))
                    for v0 in (0.05, 0.1, 0.15) for g0 in (100, 400, 1000)), key=lambda r: r.fun)
        num = min(best.fun, np.mean([kl_counts(c, hab_c) for c in laws]))
        fit = (float(np.exp(best.x[0])), float(np.exp(best.x[1])))
    else:
        obj = lambda g: np.mean([kl_counts(c, group_counts(v, g)) for c, v in zip(laws, vfix)])
        r = minimize_scalar(obj, bounds=(0, 5000), method="bounded", options=dict(xatol=1e-8))
        num, fit = min(r.fun, obj(0.0)), float(r.x)
    return 1 - num / den, num, den, fit


e2 = lambda p: posterior(Pminus(PAR, p), 1 / PAR.R, 3 / (PAR.R + PAR.Rc))[0, 0]
c = cnt_law["50%"]
# two-member log odds ratio from the exchangeable count law
pr = {k: c[k] / comb(4, k) for k in range(5)}
p11 = sum(c[k] * (k * (k - 1)) / 12 for k in range(5))
p10 = sum(c[k] * (k * (4 - k)) / 12 for k in range(5))
p00 = sum(c[k] * ((4 - k) * (3 - k)) / 12 for k in range(5))
lor = np.log(p11 * p00 / p10 ** 2)
print(f"median bin: KL(P||E) = {kl_counts(c, hab_c):.5f}; log odds ratio of two members' choices {lor:.4f}")
for name, kw in (("G1", {}), ("G2", {"vfix": [e2(pmed["50%"])]})):
    A_, num, den, fit = index([c], **kw)
    print(f"  index at the median bin, {name}: {A_:.5f} (min KL {num:.2e}, den {den:.5f}, fit {fit})")
L3 = [cnt_law[b] for b in ("10%", "50%", "90%")]
for name, kw in (("G1 one (v_C, gamma_C)", {}), ("G2 per-bin E2 variance", {"vfix": [e2(pmed[b]) for b in ("10%", "50%", "90%")]})):
    A_, num, den, fit = index(L3, **kw)
    print(f"  index on three bins, {name}: {A_:.5f} (min KL {num:.2e}, den {den:.5f})")
Ph, Nh, Mh = collect("hab", 60000, 9102, sym_only=False)
ch = np.bincount(Nh, minlength=5) / len(Nh)
print(f"NEG habit null through the same estimator: law {np.round(ch, 4)}, KL to habits {kl_counts(ch, hab_c):.2e} "
      f"(n={len(Nh)})")
print(f"total {time.time()-t0:.0f}s")
