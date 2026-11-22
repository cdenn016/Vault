r"""Deciding script D4: partner-randomization test of prop:agy-tests(b) (05_agency.tex:367), run literally with
n_null = 999 independent null draws (N_pr redrawn every round), statistic = niche contrast r(A).
S_0 = r(A) of the full model (exact algebra, d1_<proto>.npz).
Declared expectations (before running): every null draw between 2.4 and 3.4, none >= S_0, so p = 1/1000 = 0.001
<= alpha_pr = 0.01.  NEGATIVE CONTROL: 199 draws of the FULL model through the same estimator put S_0 inside the bulk
of its own draws (p between 0.1 and 0.9), so the test is able to accept.
"""
import time
import numpy as np
from lib3 import compound
from mc3 import run
from instance3 import PAR, PROTO, N_NULL, ALPHA_PR

t0 = time.time()
S0 = float(np.load(f"d1_{PROTO}.npz")["r"])
o = run(PAR, K=N_NULL * 20, T=400, burn=80, seed=9301 if PROTO == "real" else 9302, mode="pr", nbatch=N_NULL)
S = np.array([1 + 4 * compound(s)[1] / compound(s)[0] for s in o.S_batches])
p = (1 + np.sum(S >= S0)) / (len(S) + 1)
print(f"[{PROTO}] N_pr, {len(S)} independent draws: min {S.min():.4f}, median {np.median(S):.4f}, max {S.max():.4f}; "
      f"#(S_l >= S0={S0:.4f}) = {int(np.sum(S >= S0))}; p = {p:.4f}; reject at alpha_pr={ALPHA_PR}: {p <= ALPHA_PR}; "
      f"margin S0 - max {S0 - S.max():.4f}  ({time.time()-t0:.0f}s)", flush=True)
np.save(f"d4_{PROTO}_null.npy", S)
of = run(PAR, K=199 * 20, T=400, burn=80, seed=9303 if PROTO == "real" else 9304, mode="full", nbatch=199)
Sf = np.array([1 + 4 * compound(s)[1] / compound(s)[0] for s in of.S_batches])
pf = (1 + np.sum(Sf >= S0)) / (len(Sf) + 1)
print(f"[{PROTO}] NEG full model, {len(Sf)} draws: min {Sf.min():.4f}, median {np.median(Sf):.4f}, max {Sf.max():.4f}; "
      f"p = {pf:.3f} (must lie in 0.1..0.9)  ({time.time()-t0:.0f}s)")
