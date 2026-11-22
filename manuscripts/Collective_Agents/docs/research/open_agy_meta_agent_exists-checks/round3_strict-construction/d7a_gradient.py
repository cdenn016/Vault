r"""Deciding script D7a: sensitivities of r(A) to the eight continuous parameters at I** (real protocol), central
differences with relative step 2% and common random numbers (same seed for the policy paths), exact pair algebra,
24 pairs per evaluation.  Declared expectations: |d r / d ln(theta)| at most about 3 for gamma and psi (they set the
open rate through gamma*psi), at most about 3 for Rc, and the sum of |d r/d ln theta| below 12, so a box of relative
half-width 2% moves r(A) by at most about 0.25 < 0.53 = min(r(A) - r0, 9.05 - r(A)) at first order.
NEGATIVE CONTROL: the same differences with independent seeds for + and - are much noisier (spread reported) - shows
the common-random-number differences are not dominated by Monte Carlo noise.
"""
import time
import numpy as np
from lib3 import sigma_c
from instance3 import PAR, T, BURN, EVERY

t0 = time.time()
names = ["F", "Q", "R", "Rc", "Rs", "psi", "gamma", "qc"]
h = 0.02
grad = {}
for nm in names:
    v = getattr(PAR, nm)
    rp = sigma_c(PAR.with_(**{nm: v * (1 + h)}), 24, T, BURN, EVERY, seed=7001)["r"]
    rm = sigma_c(PAR.with_(**{nm: v * (1 - h)}), 24, T, BURN, EVERY, seed=7001)["r"]
    grad[nm] = (rp - rm) / (2 * h)
    print(f"d r / d ln {nm} = {grad[nm]:+.3f}   (r+ {rp:.4f}, r- {rm:.4f})  ({time.time()-t0:.0f}s)", flush=True)
c0 = sigma_c(PAR, 24, T, BURN, EVERY, seed=7001)["r"]
s = sum(abs(g) for g in grad.values())
print(f"center (same seed) r = {c0:.4f}; sum |d r/d ln theta| = {s:.3f}; first-order excursion on a box of relative "
      f"half-width 2%: {0.02*s:.3f}; 1%: {0.01*s:.3f}")
ra = sigma_c(PAR.with_(psi=PAR.psi * 1.02), 24, T, BURN, EVERY, seed=7002)["r"]
rb = sigma_c(PAR.with_(psi=PAR.psi * 0.98), 24, T, BURN, EVERY, seed=7003)["r"]
print(f"NEG independent seeds for psi: d r/d ln psi = {(ra-rb)/(2*h):+.3f} (vs {grad['psi']:+.3f} with common numbers)")
np.save("d7a_grad.npy", grad, allow_pickle=True)
print(f"total {time.time()-t0:.0f}s")
