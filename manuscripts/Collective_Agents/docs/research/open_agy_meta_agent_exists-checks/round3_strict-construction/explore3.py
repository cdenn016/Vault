r"""Exploration only (not deciding): window against the mechanism medium over (Rs, psi), T-real, R=1, Rc=0.1, F=0.9."""
import sys, time
import numpy as np
from lib3 import Par, sigma_c

t0 = time.time()
grid = [tuple(float(x) for x in a.split(",")) for a in sys.argv[1:]]
for Rs, psi in grid:
    par = Par(Rs=Rs, psi=psi)
    med = par.with_(n=8, n_zero=0, nrev=2)
    f = sigma_c(par, 10, 300, 80, 4, seed=31)
    m = sigma_c(med, 5, 300, 80, 4, seed=32)
    print(f"Rs={Rs} psi={psi}: open {f['open_rate']:.3f} r(A) {f['r']:.3f}; medium {m['r']:.3f} (open {m['open_rate']:.3f}); "
          f"meancoup {1+6/7*(f['r']-1):.3f}  ({time.time()-t0:.0f}s)", flush=True)
