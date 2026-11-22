r"""Check 9: the partner-randomization test of prop:agy-tests(b) (05_agency.tex:367) run literally with n_null = 999
independent null draws (each draw: an independent estimate of the every-round null's Sigma^c from 20 world paths x
2 replicas x 320 rounds; statistic S_l = contrast of the niche, the declared selector's statistic at the selected
block), against S_0 = 4.4185 (check 2).
Declared expectations (before running): every S_l between 1.5 and 2.4, none >= S_0, so p = 1/1000 <= alpha_pr = 0.01.
NEGATIVE CONTROL: the same estimator on 199 independent draws of the FULL model must put S_0 inside the bulk of its
own draws (p well above 0.01), so the test is able to accept.
"""
import time
import numpy as np
from core import Par, run, compound, r_ab

t0 = time.time()
PAR = Par()
S0 = 4.4185
o = run(PAR, K=999 * 20, T=400, burn=80, seed=9101, mode="pr", nbatch=999)
S = np.array([r_ab(4, *compound(s)) for s in o.S_batches])
p = (1 + np.sum(S >= S0)) / (len(S) + 1)
print(f"N_pr, {len(S)} draws: min {S.min():.3f}, median {np.median(S):.3f}, max {S.max():.3f}; #(S_l >= S0) = "
      f"{int(np.sum(S >= S0))}; p = {p:.4f}  ({time.time()-t0:.0f}s)")
of = run(PAR, K=199 * 20, T=400, burn=80, seed=9102, mode="full", nbatch=199)
Sf = np.array([r_ab(4, *compound(s)) for s in of.S_batches])
pf = (1 + np.sum(Sf >= S0)) / (len(Sf) + 1)
print(f"NEG full model, {len(Sf)} draws: min {Sf.min():.3f}, median {np.median(Sf):.3f}, max {Sf.max():.3f}; p = {pf:.3f} "
      f"(must be well above 0.01)  ({time.time()-t0:.0f}s)")
