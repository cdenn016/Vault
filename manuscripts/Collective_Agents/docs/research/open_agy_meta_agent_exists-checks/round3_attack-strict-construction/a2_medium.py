r"""A2 (attack): clause (c) mechanism medium of I** (declared by the candidate: 8 agents on one world component, the
same mechanism, n_zero = 0; real protocol with 2 revisers per round), recomputed with mylib.py.
Declared expectations: whole-medium contrast 1 + 8 beta/alpha = 5.96 +/- 0.05 (real, nrev 2), 6.01 +/- 0.05 (frozen);
variant real with nrev 1 about 6.02. FALSIFIER of the candidate: medium contrast >= 7.9.
"""
import sys, time
from mylib import Cfg, sigma_c
proto = sys.argv[1]; nrev = int(sys.argv[2]) if len(sys.argv) > 2 else 2
t0 = time.time()
c = Cfg(proto=proto, n=8, nz=0, nrev=nrev)
o = sigma_c(c, npairs=50, T=400, burn=80, every=4, seed=51 if proto == "real" else 52)
print(f"[medium {proto} nrev {nrev}] 50 pairs: open {o['open']:.4f}; alpha {o['alpha']:.6f} beta {o['beta']:.6f}; "
      f"whole-medium contrast {o['r']:.4f} +/- {o['se_r']:.4f}  ({time.time()-t0:.0f}s)")
