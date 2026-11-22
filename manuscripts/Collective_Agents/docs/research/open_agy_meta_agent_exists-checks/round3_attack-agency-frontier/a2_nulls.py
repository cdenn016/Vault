r"""Attack run a2: N_hab and N_pr (redrawn every round) for D1 by independent two-replica Monte Carlo.

Declared expectations (candidate): N_hab 1.346 +- 0.007; N_pr 1.761 +- 0.007; both below the lower edge 2.493.
Also Theorem A's step 3 for asymmetric habits (n = 2): r_hab(q1, q2) with member-specific mate-reading habit
masses.  The theorem's bound sum_i d(1 || q_i) >= 2 d(1 || pi*) (delta -> 0) is violated iff some (q1, q2) with
r_hab <= b has q1 q2 > pi*^2 (pi* = 0.577 at K = 2, so pi*^2 = 0.333).  Expectation: not violated (contrast grows
with the total reading volume), i.e. r_hab(0.999, q) > b for q >= 0.34.
NEGATIVE CONTROL: N_hab with attention pinned on the mate and no slots (m = 0) must reproduce the exact 4.345.
"""
import time
import numpy as np
from mylib import Par, mc

t0 = time.time()
par = Par()
o = mc(par, "hab", B=3000, T=600, burn=150, seed=21)
print(f"N_hab: r {o['r']:.4f} +- {o['se']:.4f}; open rate (slots/member) {o['open_rate']:.3f}; mate rate {o['c_rate']:.3f}"
      f"  ({time.time() - t0:.1f}s)")
o = mc(par, "pr", B=3000, T=600, burn=150, seed=22)
print(f"N_pr (every round): r {o['r']:.4f} +- {o['se']:.4f}; open {o['open_rate']:.2e}; mate rate {o['c_rate']:.3f}"
      f"  ({time.time() - t0:.1f}s)")
o = mc(par.w(m=0), "hab", B=2000, T=500, burn=150, seed=23, q_mate=(1.0, 1.0))
print(f"NEG N_hab pinned on mate, m=0: r {o['r']:.4f} +- {o['se']:.4f} (exact 4.3452)  ({time.time() - t0:.1f}s)")
for q in [(0.577, 0.577), (0.999, 0.34), (0.999, 0.2), (0.999, 0.1)]:
    o = mc(par, "hab", B=2000, T=500, burn=150, seed=24, q_mate=q)
    print(f"Theorem A asym: q = {q}: r_hab {o['r']:.4f} +- {o['se']:.4f}; q1 q2 = {q[0] * q[1]:.3f} "
          f"(violation needs r <= 2.493 with q1 q2 > 0.333)  ({time.time() - t0:.1f}s)")
