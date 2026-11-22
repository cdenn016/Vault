r"""V2: diagnose the D3 MC-vs-exact gap (z about -2 to -3 at n = 4).

Hypotheses declared before running: (H1) burn-in too short for the slowest error mode (then the gap shrinks with
burn = 300 and the spectral radius of the exact state matrix is close to 1); (H2) slots in the full mode are not
closed (then open_rate > 0 and m = 0 removes the gap); (H3) ratio-estimator bias or SE underestimate (then neither
burn nor m changes the gap and repeated seeds scatter around the exact value).
NEGATIVE CONTROL: the A8 setting (validated, z = +1.1 at burn 80) must stay within 3 SE at burn 300.
"""
import time
import numpy as np
from flib import Par, exact_sigma_c, compound, r_ab, mc, r_and_se
from d1_agency import design as mkdesign

t0 = time.time()
D3 = mkdesign(4, ((0, 1), (3, 1)), 8)
att = ~np.eye(4, dtype=bool)
S, Sz, A = exact_sigma_c(D3, att, np.zeros(4, dtype=int))
rex = r_ab(4, *compound(S))
print(f"exact r(A) {rex:.5f}; spectral radius of the exact state matrix {max(abs(np.linalg.eigvals(A))):.5f}")
for lab, par, burn, T, seed in (("D3 m=8 burn80", D3, 80, 400, 11), ("D3 m=8 burn300", D3, 300, 620, 12),
                                 ("D3 m=0 burn300", D3.with_(m=0), 300, 620, 13),
                                 ("D3 m=8 burn300 seed2", D3, 300, 620, 14)):
    o = mc(par, "full", K=1500, T=T, burn=burn, seed=seed)
    r, s, _, _ = r_and_se(o, 4)
    print(f"{lab}: {r:.4f} +- {s:.4f} (z {(r-rex)/s:+.2f}); open rate {o.open_rate:.1e}; mean relays {o.mean_c:.4f}"
          f"  ({time.time()-t0:.0f}s)")
A8 = Par(Rc=0.2, qc=0.0, n=4, n_zero=4, m=0, types=((3, 1),))
o = mc(A8, "full", K=1500, T=620, burn=300, seed=15)
r, s, _, _ = r_and_se(o, 4)
print(f"NEG A8 burn300: {r:.4f} +- {s:.4f} (z vs 7.425938 {(r-7.425938)/s:+.2f})  ({time.time()-t0:.0f}s)")
