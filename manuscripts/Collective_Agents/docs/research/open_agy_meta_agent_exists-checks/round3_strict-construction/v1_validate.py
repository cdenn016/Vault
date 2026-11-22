r"""Check V1 (validation of the exact pair algebra and of the sampled Monte Carlo, before any deciding run).

Declared expectations (written before running):
  V1a  exact algebra, fixed policies (every mate attended, private sensors never open), qc = 0, Rc = 0.2: the model is
       then the round-1 A8 setting, so r = 7.425938 to 1e-5 (record C11 Evidence, round-2 attack run1).
       NEGATIVE CONTROL: same with the relayed private noises treated as fresh: Sigma^c diagonal, r = 1 to 1e-10.
  V1b  fixed asymmetric profile sigma = (1,0,1,0) every round (qc = 1e-4, Rc = 0.1): the per-realization covariance is
       NOT compound symmetric (largest deviation of an entry from the compound projection >> 1e-6); the sampled
       Monte Carlo (two replicas per world path) agrees with the exact algebra entrywise within 4 standard errors.
       NEGATIVE CONTROL: Monte Carlo with an independent world per replica gives a covariance larger than the exact
       world-conditional one by the common mode (mean off-diagonal at least 5x larger).
"""
import time
import numpy as np
from lib3 import Par, sigma_c, compound
from mc3 import run

t0 = time.time()
A8 = Par(Rc=0.2, qc=0.0)
res = sigma_c(A8, 1, 300, 150, 1, seed=1, mode="fixed", fixed_sig=[0, 0, 0, 0])
print(f"V1a A8 setting: alpha={res['alpha']:.8f} beta={res['beta']:.8f} r={res['r']:.6f} (expected 7.425938); "
      f"max |raw - compound| = {np.abs(res['S'] - (res['alpha'] * np.eye(4) + res['beta'])).max():.1e}")
neg = sigma_c(A8, 1, 300, 150, 1, seed=1, mode="fixed", fixed_sig=[0, 0, 0, 0], fresh_relays=True)
print(f"V1a NEG fresh relays: beta={neg['beta']:.3e} r={neg['r']:.10f} (expected 1)")

par = Par()
sig = [1, 0, 1, 0]
ex = sigma_c(par, 1, 300, 150, 1, seed=2, mode="fixed", fixed_sig=sig)
S = ex["S"]
al, be = compound(S)
print("V1b exact Sigma (fixed profile (1,0,1,0)):\n", np.array2string(S, precision=7))
print(f"    compound projection alpha={al:.6f} beta={be:.6f}; largest deviation from it {np.abs(S - (al*np.eye(4)+be)).max():.3e}")
mc = run(par, K=4000, T=260, burn=60, seed=3, mode="fixed", fixed_sig=sig, nbatch=40)
se = mc.S_batches.std(0, ddof=1) / np.sqrt(mc.S_batches.shape[0])
z = (mc.S - S) / se
print("    sampled MC Sigma:\n", np.array2string(mc.S, precision=7))
print(f"    max |z| over entries = {np.abs(z).max():.2f} (expected < 4)")
mci = run(par, K=4000, T=260, burn=60, seed=4, mode="fixed", fixed_sig=sig, shared_world=False, nbatch=40)
offd = lambda M: (M.sum() - np.trace(M)) / 12
print(f"V1b NEG independent worlds: mean off-diagonal {offd(mci.S):.5f} vs world-conditional {offd(S):.5f} "
      f"(ratio {offd(mci.S)/offd(S):.1f}, expected >= 5)")
print(f"total {time.time()-t0:.1f}s")
