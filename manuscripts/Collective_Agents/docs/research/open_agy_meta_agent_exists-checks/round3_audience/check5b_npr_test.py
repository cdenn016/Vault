r"""Check 5: the partner-randomization test of prop:agy-tests(b) (05_agency.tex:367) for instance P0, run literally
with n_null = 999 independent null draws under N_pr redrawn every round (each draw: an independent estimate of the
null's Sigma^c from 80 world paths x 2 replicas x 300 rounds, burn-in 80, symmetrized over the audience), statistic
S_l = r(A), the contrast of the selected block, and also the largest contrast over all regions.
S_0 = r(A) of the full model, estimated by the same estimator with 200 world paths (and the exact value 5.3849).

Declared expectations before running (rerun of check 5 with 80 world paths per draw, so that no estimate is non-diffusive; undefined draws, if any, are scored conservatively as S_l >= S_0): every S_l below 2.2; p = 1/1000 <= alpha_pr = 0.01 for both statistics.
NEGATIVE CONTROL: 199 draws of the FULL model with the same estimator must put the exact S_0 in their bulk
(p between 0.05 and 0.95), so that the test can accept.
"""
import time
import numpy as np
import sim
from aud import Par, symmetrize_audience, contrast, diffusive, all_regions

t0 = time.time()
par = Par()
A = tuple(range(1, par.N))
args = (par.F, par.Q, par.R, par.RS, par.Rc, par.qc, par.n, par.kmsg, par.gamma)


def stats(Sb):
    rA, rmax, nd = [], [], 0
    for S in Sb:
        Ss = symmetrize_audience(S)
        Pi = np.linalg.inv(Ss)
        if not diffusive(Pi, tol=0.0)[0]:
            nd += 1
            rA.append(np.nan); rmax.append(np.nan)
            continue
        rA.append(contrast(Pi, A))
        rmax.append(max(contrast(Pi, C) for C in all_regions(par.N)))
    return np.array(rA), np.array(rmax), nd


S0_exact = 5.384864
o0 = sim.run(*args, K=200, T=300, burn=80, seed=5001, mode="full", nbatch=1)
S0 = stats(o0["S_b"])[0][0]
print(f"S_0 (same estimator, 200 world paths) = {S0:.4f}; exact {S0_exact:.4f}  ({time.time()-t0:.0f}s)")
o = sim.run(*args, K=999 * 80, T=300, burn=80, seed=5002, mode="pr", nbatch=999)
rA, rmax, nd = stats(o["S_b"])
p1 = (1 + np.sum(rA >= S0_exact) + np.sum(np.isnan(rA))) / (len(rA) + 1)
p2 = (1 + np.sum(rmax >= S0_exact) + np.sum(np.isnan(rmax))) / (len(rmax) + 1)
print(f"N_pr, 999 draws: non-diffusive estimates {nd}; r(A): min {np.nanmin(rA):.3f}, median {np.nanmedian(rA):.3f}, "
      f"max {np.nanmax(rA):.3f}; p = {p1:.4f}; largest region contrast: max {np.nanmax(rmax):.3f}, p = {p2:.4f}  "
      f"({time.time()-t0:.0f}s)")
of = sim.run(*args, K=199 * 80, T=300, burn=80, seed=5003, mode="full", nbatch=199)
rf, _, ndf = stats(of["S_b"])
pf = (1 + np.sum(rf >= S0_exact)) / (len(rf) + 1)
print(f"NEG full model, 199 draws: min {np.nanmin(rf):.3f}, median {np.nanmedian(rf):.3f}, max {np.nanmax(rf):.3f}; "
      f"p = {pf:.3f} (must lie in (0.05, 0.95))  ({time.time()-t0:.0f}s)")
