r"""D1 deciding run 2: the partner-randomization test of prop:agy-tests(b) (05_agency.tex:367) run literally,
n_null = 999 independent null draws (each: an independent estimate of the every-round null's Sigma^c from 20 world
paths x 2 replicas x 320 rounds; statistic = contrast of the niche), against S_0 = 4.3452 (exact) / 4.339 (MC).
Declared expectations: every S_l between 1.4 and 2.2, none >= S_0, p = 1/1000 <= alpha_pr = 0.01.
NEGATIVE CONTROL: the same estimator on 199 independent draws of the FULL model must put S_0 inside the bulk of its
own draws (p well above 0.01).
"""
import time
import numpy as np
from flib import mc, compound, r_ab
from design import D1

t0 = time.time()
S0 = 4.3452
o = mc(D1, "pr", K=999 * 20, T=400, burn=80, seed=2001, nbatch=999, r_att=1)
S = np.array([r_ab(2, *compound(s)) for s in o.S_batches])
p = (1 + np.sum(S >= S0)) / (len(S) + 1)
print(f"N_pr, {len(S)} draws: min {S.min():.3f}, median {np.median(S):.3f}, max {S.max():.3f}; "
      f"#(S_l >= S0) = {int(np.sum(S >= S0))}; p = {p:.4f}  ({time.time()-t0:.0f}s)")
of = mc(D1, "full", K=199 * 20, T=400, burn=80, seed=2002, nbatch=199)
Sf = np.array([r_ab(2, *compound(s)) for s in of.S_batches])
pf = (1 + np.sum(Sf >= S0)) / (len(Sf) + 1)
print(f"NEG full model, {len(Sf)} draws: min {Sf.min():.3f}, median {np.median(Sf):.3f}, max {Sf.max():.3f}; "
      f"p = {pf:.3f} (must be well above 0.01)  ({time.time()-t0:.0f}s)")
