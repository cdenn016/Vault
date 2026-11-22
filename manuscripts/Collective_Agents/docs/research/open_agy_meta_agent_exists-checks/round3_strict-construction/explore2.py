r"""Exploration only (not deciding): relay-only structure (private sensors never open, psi = 10) over (R, Rc, F),
niche (all mates every round, exact) against the one-component mechanism medium (8 agents, 3 of 7 by EFE)."""
import sys, time
import numpy as np
from lib3 import Par, sigma_c

t0 = time.time()
grid = [(1.0, 0.1, 0.9), (1.0, 0.5, 0.9), (1.0, 1.0, 0.9), (0.5, 0.5, 0.9), (0.25, 0.25, 0.9), (0.25, 0.5, 0.9),
        (1.0, 0.3, 0.5), (0.5, 0.3, 0.7)]
for R, Rc, F in grid:
    par = Par(R=R, Rc=Rc, F=F, psi=10.0)
    med = par.with_(n=8, n_zero=0, nrev=2)
    f = sigma_c(par, 2, 300, 80, 4, seed=21)
    m = sigma_c(med, 6, 300, 80, 4, seed=22)
    h = sigma_c(par, 6, 300, 80, 4, seed=23, mode="hab")
    pr = sigma_c(par, 6, 300, 80, 4, seed=24, mode="pr")
    print(f"R={R} Rc={Rc} F={F}: r(A) {f['r']:.3f}; medium {m['r']:.3f}; meancoup {1+6/7*(f['r']-1):.3f}; "
          f"N_hab {h['r']:.3f}; N_pr {pr['r']:.3f}; alpha {f['alpha']:.4f} beta {f['beta']:.4f}  ({time.time()-t0:.0f}s)",
          flush=True)
