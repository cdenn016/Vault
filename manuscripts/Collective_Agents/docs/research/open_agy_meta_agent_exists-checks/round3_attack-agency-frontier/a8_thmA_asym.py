r"""Attack run a8: Theorem A step 3 assumes one habit mass E(X*) for all members.  Test asymmetric habits against
D1's own slot-inclusive threshold pi*_D1 = 0.880 (a5): the bound sum_i d(1||q_i) >= 2 d(1||pi*) fails iff some
(q1, q2) with r_hab <= b = 2.4932 has q1 q2 > pi*^2 = 0.774.
Declared expectation: r_hab(0.999, 0.775) > b (no violation).  NEGATIVE CONTROL: the symmetric point
(0.88, 0.88) must sit at b within about 3 SE."""
import time
from mylib import Par, mc
t0 = time.time()
for q in [(0.88, 0.88), (0.999, 0.775), (0.999, 0.70), (0.95, 0.815)]:
    o = mc(Par(), "hab", B=3000, T=500, burn=150, seed=81, q_mate=q)
    print(f"q = {q}: r_hab {o['r']:.4f} +- {o['se']:.4f}; q1 q2 = {q[0]*q[1]:.3f}; b = 2.4932  ({time.time()-t0:.1f}s)")
