r"""A1 (attack): collective clause of niche A of I**, recomputed with independent code (mylib.py).
Declared expectations (before running), from the candidate's report:
  r(A) = 8.431 +/- 0.03 (real) and 8.421 +/- 0.03 (frozen); open rate about 0.117;
  mixture part of beta (E[Cov(e|eta)] - E[Cov(e|eta,pi)]) of order 1e-5;
  mean-coupling baseline 1 + (6/7)(r(A) - 1) about 7.37.
  FALSIFIER of the candidate: r(A) < 7.9 or a mean-coupling baseline >= 7.9.
NEGATIVE CONTROLS (must fail to produce a collective):
  NC1 fresh relays (relayed own-sensor and private-sensor noise replaced by independent copies): r(A) within 0.01 of 1;
  NC2 Rc = 1e6 (messages carry no information): r(A) within 0.01 of 1.
"""
import sys, time
import numpy as np
from mylib import Cfg, sigma_c
proto = sys.argv[1]
t0 = time.time()
c = Cfg(proto=proto)
o = sigma_c(c, npairs=160, T=400, burn=80, every=4, seed=31 if proto == "real" else 32)
r = o["r"]; b = o["beta"] / o["alpha"]
print(f"[{proto}] pairs 160: open {o['open']:.4f}; alpha {o['alpha']:.8f} (SE {o['se_alpha']:.1e}) beta {o['beta']:.8f} "
      f"(SE {o['se_beta']:.1e}); r(A) = {r:.4f} +/- {o['se_r']:.4f}; mixture part of beta {o['beta']-o['beta_priv']:.2e}")
S = o["S"]
print("   raw Sigma^c_A:\n", np.array2string(S, precision=7))
print(f"   max |raw - compound| {np.max(np.abs(S - (o['alpha']*np.eye(4) + o['beta']))):.2e}")
mc = 1 + 24.0 / 7.0 * b
print(f"   mean-coupling baseline {mc:.4f}; window ({mc:.4f}, {r:.4f}]; r0 = 7.9 inside: {mc < 7.9 <= r}; "
      f"sub-region (3 of 4) contrast {(1+3*b)/(1+b):.4f}  ({time.time()-t0:.0f}s)", flush=True)
n1 = sigma_c(c, npairs=20, T=400, burn=80, every=4, seed=41, fresh_relays=True)
print(f"   NC1 fresh relays: r(A) = {n1['r']:.4f} (expected within 0.01 of 1)  ({time.time()-t0:.0f}s)", flush=True)
n2 = sigma_c(c.w(Rc=1e6), npairs=10, T=400, burn=80, every=4, seed=42)
print(f"   NC2 Rc = 1e6: r(A) = {n2['r']:.4f} (expected within 0.01 of 1)  ({time.time()-t0:.0f}s)", flush=True)
