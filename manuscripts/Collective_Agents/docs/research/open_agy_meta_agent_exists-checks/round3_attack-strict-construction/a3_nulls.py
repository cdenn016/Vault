r"""A3 (attack): type-D nulls N_hab (gamma = 0) and N_pr (partners redrawn uniformly every round among all 7 channels,
|M| = 3; sigma' by EFE given the drawn partners), recomputed with mylib.py.
Declared expectations: N_hab r(A) about 2.38, N_pr about 2.84 in both protocols; both far below the full model's
mean-coupling baseline (about 7.37). FALSIFIER of the candidate: either null's largest region contrast >= 7.37
(then some admissible r0 would select the same partition under the null).
"""
import sys, time
from mylib import Cfg, sigma_c
proto = sys.argv[1]
t0 = time.time()
c = Cfg(proto=proto)
for mode, seed in (("hab", 61), ("pr", 62)):
    o = sigma_c(c, npairs=60, T=400, burn=80, every=4, seed=seed, mode=mode)
    b = o["beta"] / o["alpha"]
    print(f"[{proto}] N_{mode}: open {o['open']:.3f}; alpha {o['alpha']:.6f} beta {o['beta']:.6f}; r(A) {o['r']:.4f} +/- "
          f"{o['se_r']:.4f}; 3-subset {(1+3*b)/(1+b):.4f}  ({time.time()-t0:.0f}s)", flush=True)
