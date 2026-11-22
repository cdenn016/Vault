r"""Deciding run 8: soft attention (design D4) and the D3 Monte Carlo recheck.

D4: D2 (n=2, two niches, support {{mate},{o1}}, uniform habits, m private slots at Rs=10) with one smaller policy
precision gamma chosen so that the stationary probability of reading the mate is about 0.8, and the slot cost raised to
psi = g_max + 20/gamma so that slots stay closed with gamma*(psi - gain) >= 20 at the same gamma.
Agency at fine decision states (each member's claimed posterior variance at the decision; members decide
independently, so the joint law at a state is the product of the members' posteriors):
   Agency = 1 - sum_t [KL_a(t) + mis(t)] / sum_t [KL_a(t) + KL_s(t)], mis ~ 0 (checked at the median state).
Declared expectations (before running): gamma about 29 gives P(mate) about 0.8; full r(A) about 3.2-3.4 (between
rho(0.7)=2.94 and rho(0.85)=3.54); b = 2.4932 unchanged (closure of the support = all 1-sets, every medium agent reads
exactly one informative relay); N_hab about 1.76 (as D2); N_pr 1.75 / 2.20; KL_a per member about d(0.8||0.5)=0.193;
index about 0.78 (m=1) and 0.966 (m=8).
NEGATIVE CONTROL: at gamma = 400 the same pipeline must return the D2 index 0.5 (m=1) and 0.8889 (m=8).
D3 recheck: MC r(A) with K = 1500 and a fresh seed must be within 3 SE of the exact 8.6279.
"""
import time
import numpy as np
from flib import Par, exact_sigma_c, compound, r_ab, mc, r_and_se, medium_exact, steady_prior, efe_grid, post, log_binom
from d1_agency import design as mkdesign

t0 = time.time()


def d4(gamma: float, m: int) -> Par:
    base = Par(F=0.9, Q=0.05, R=1.0, Rc=0.1, Rs=10.0, psi=0.0, gamma=gamma, qc=1e-4, n=2, n_zero=2, m=m,
               types=((0, 1), (1, 1)))
    gmax = 0.0
    for c in (0, 1):
        Pm = steady_prior(base, c, 0)
        for cc in (0, 1):
            G = efe_grid(base, Pm[0, 0], Pm[0, 1], Pm[1, 1], np.array([cc]), np.array([0, 1]))
            gmax = max(gmax, float(G[0, 0] - G[0, 1]))
    return base.with_(psi=gmax + 20.0 / gamma)


def claimed_process(par: Par, T: int, nmem: int, seed: int):
    r"""Claimed-covariance process of independent members under the full policy: returns per member-round
    (P(mate | state), KL_a, KL_s) at the decision."""
    rng = np.random.default_rng(seed)
    Pp00 = np.full(nmem, 0.1)
    out = []
    lb = log_binom(par.m)
    ks = np.arange(par.m + 1)
    for t in range(T):
        P00 = par.F ** 2 * Pp00 + par.Q + par.qc
        P01 = par.F * Pp00
        P11 = Pp00 + par.qc
        G = efe_grid(par, P00, P01, P11, np.array([0, 1]), ks)            # (nmem, 2, m+1)
        lw = lb[None, None, :] - par.gamma * G
        lw = lw - lw.max(axis=(1, 2), keepdims=True)
        w = np.exp(lw)
        w /= w.sum(axis=(1, 2), keepdims=True)
        pa = w.sum(2)                                                       # (nmem, 2): types c=0 (o1), c=1 (mate)
        with np.errstate(divide="ignore", invalid="ignore"):
            KLa = np.sum(np.where(pa > 0, pa * np.log(pa * 2.0), 0.0), axis=1)
            pk = w / pa[:, :, None]
            KLs = np.sum(pa * np.sum(np.where(pk > 0, pk * (np.log(pk) - lb[None, None, :] + par.m * np.log(2)), 0.0),
                                     axis=2), axis=1)
        if t >= 100:
            out.append(np.stack([pa[:, 1], KLa, KLs], 1))
        c = (rng.random(nmem) < pa[:, 1]).astype(int)
        Pm = np.stack([np.stack([P00, P01], 1), np.stack([P01, P11], 1)], 1)
        newp = np.empty(nmem)
        for i in range(nmem):
            newp[i] = post(Pm[i], 1.0 / par.R, c[i] / (par.R + par.Rc))[0, 0]
        Pp00 = newp
    return np.concatenate(out, 0)


for gamma in (29.0, 400.0):
    for m in (1, 8):
        par = d4(gamma, m)
        rec = claimed_process(par, T=1100, nmem=200, seed=int(gamma) + m)
        pm, KLa, KLs = rec[:, 0].mean(), rec[:, 1].sum(), rec[:, 2].sum()
        idx = 1 - KLa / (KLa + KLs)
        print(f"gamma={gamma:g} m={m}: psi {par.psi:.4f}; mean P(mate) {pm:.4f} (range {rec[:,0].min():.4f}-"
              f"{rec[:,0].max():.4f}); KL_a/member-round {KLa/len(rec):.5f}; KL_s {KLs/len(rec):.5f}; "
              f"index (mis = 0) {idx:.4f}  ({time.time()-t0:.0f}s)")
par = d4(29.0, 8)
of = mc(par, "full", K=2000, T=400, burn=80, seed=9001, want_inf=True)
rf, sf, _, _ = r_and_se(of, 2)
b = medium_exact(par, N=4, c=1)[2]
oh = mc(par, "hab", K=1500, T=400, burn=80, seed=9002)
rh, sh, _, _ = r_and_se(oh, 2)
op = mc(par, "pr", K=1500, T=400, burn=80, seed=9003, r_att=1)
rp, sp, _, _ = r_and_se(op, 2)
op2 = mc(par.with_(n_zero=1), "pr", K=1500, T=400, burn=80, seed=9004, r_att=1)
rp2, sp2, _, _ = r_and_se(op2, 2)
I = of.inf
vst = 1.0 / (I["invU"] / I["n"])
best = 0.5 * (vst * I["invU"] / I["n"] - 1 - np.log(vst) + I["lnU"] / I["n"] + I["q"] / I["n"])
rmc = 1 + (2.0 / 3.0) * (rf - 1)
print(f"D4 (gamma=29, m=8): full r(A) {rf:.4f}+-{sf:.4f}; mean relays read {of.mean_c:.4f}; open-slot rate "
      f"{of.open_rate:.1e}; mechanism b {b:.4f}; mean-coupling baseline {rmc:.4f}; N_hab {rh:.4f}+-{sh:.4f}; "
      f"N_pr(all) {rp:.4f}+-{sp:.4f}; N_pr(potential) {rp2:.4f}+-{sp2:.4f}; inference best-constant {best:.4f}  "
      f"({time.time()-t0:.0f}s)")
D3 = mkdesign(4, ((0, 1), (3, 1)), 8)
o3 = mc(D3, "full", K=1500, T=400, burn=80, seed=9101)
r3, s3, _, _ = r_and_se(o3, 4)
print(f"D3 recheck: MC r(A) {r3:.4f}+-{s3:.4f} vs exact 8.6279 (z {(r3-8.6279)/s3:+.2f})  ({time.time()-t0:.0f}s)")
