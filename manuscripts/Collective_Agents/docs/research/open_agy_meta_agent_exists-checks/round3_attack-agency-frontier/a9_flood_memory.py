r"""Attack run a9: the candidate says precise slots (flooding lever, pi* = 1) 'conflict with the worst-path memory
reading' (single-round d_cl 0.20 at Rs = 1).  d_cl only bounds the Markov defect.  Compute the exact
I(y_{t+1}; y_{0:t-1} | y_t, input path) along the worst explored pairings, sustained, for Rs in {1, 2, 3, 5, 10}
(psi = g_max(Rs) + 0.06, m = 8).
Declared expectation: d_cl reproduces the candidate's 0.2017 / 0.1009 / 0.0596 / 0.0275 / 0.0091; exact MI is
one to two orders smaller.  NEGATIVE CONTROL: the stationary path returns MI = d_M = 4.37e-5 at Rs = 10."""
import time
import itertools
import numpy as np
from mylib import Par, steady, info_x
import a3_closure as A3
t0 = time.time()
stat = ((1, 0), (1, 0))
for Rs in (1.0, 2.0, 3.0, 5.0, 10.0):
    base = Par(Rs=Rs)
    g = max(info_x(base, steady(base, c, 0), cc, 1) - info_x(base, steady(base, c, 0), cc, 0)
            for c in (0, 1) for cc in (0, 1))
    par = base.w(psi=g + 0.06)
    worst_d, worst_mi, arg = 0.0, 0.0, None
    for p1 in itertools.product((0, 1), range(9)):
        for p2 in itertools.product((0, 1), range(9)):
            for L in (1, 4, 30):
                d, mi, _, _ = A3.run_path(par, [(p1, p2)] * L + [stat] * 30)
                if d > worst_d:
                    worst_d = d
                if mi > worst_mi:
                    worst_mi, arg = mi, (p1, p2, L)
    print(f"FLOOD Rs={Rs}: worst d_cl {worst_d:.4f}; worst exact MI {worst_mi:.2e} at {arg}  ({time.time()-t0:.1f}s)")
