r"""Check 0: validation of the exact pair-moment propagation against round 1.

Declared expectations (before running):
 (a) fixed attention on all three mates, no slots, qc = 0, F=0.9, Q=0.05, R=1, Rc=0.2: r(A) = 7.4259 (round-1
     attack A8, a8_out.txt "PN delay 1, no acts"), Sigma^c compound symmetric to rounding, mixture term 0
     (single deterministic policy path), Sigma^c from the pair formula equal to the private covariance.
 (b) NEGATIVE CONTROL: the same with Rc = 1.0 must give a different (smaller) contrast.
 (c) NEGATIVE CONTROL: dead relays (pure noise, dead_var = R+Rc) must give a diagonal Sigma^c (r = 1).
 (d) timing of one full-model pair path of 400 rounds.
"""
import time
import numpy as np
from lib import Par, sigma_c, compound, simulate_policy_path, pair_moments

par0 = Par(qc=0.0, Rs=2.0)
res = sigma_c(par0, "fixed", npairs=1, T=200, burn=150, every=10, seed=1, fixed_slots=0)
S = res["S"]
print("(a) fixed, no slots, qc=0: r =", round(res["r"], 6), " alpha, beta =", res["alpha"], res["beta"])
print("    max |S - compound| =", np.abs(S - (res["alpha"] * np.eye(4) + res["beta"])).max(),
      " max |S - Priv| =", np.abs(S - res["Priv"]).max())
res_b = sigma_c(par0.with_(Rc=1.0), "fixed", npairs=1, T=200, burn=150, every=10, seed=1, fixed_slots=0)
print("(b) NEG Rc=1.0: r =", round(res_b["r"], 6))
res_c = sigma_c(par0, "fixed", npairs=1, T=200, burn=150, every=10, seed=1, fixed_slots=0, dead_var=1.2)
print("(c) NEG dead relays: offdiag max |S_ij| =", np.abs(res_c["S"] - np.diag(np.diag(res_c["S"]))).max(),
      " r =", round(res_c["r"], 6))
par = Par()
rng = np.random.default_rng(0)
t0 = time.time()
pa = simulate_policy_path(par, 400, rng, "full")
pb = simulate_policy_path(par, 400, rng, "full")
t1 = time.time()
out = pair_moments(par, pa, pb, list(range(100, 400, 5)))
t2 = time.time()
print(f"(d) timing: 2 paths {t1-t0:.2f}s, pair moments {t2-t1:.2f}s; open rate {pa.slots[100:].mean():.3f}, "
      f"attention deviations {pa.att_dev + pb.att_dev}")
