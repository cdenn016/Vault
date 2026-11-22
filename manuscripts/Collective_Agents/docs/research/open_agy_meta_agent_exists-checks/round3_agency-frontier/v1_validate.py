r"""V1: validation of flib against round-2 numbers, with negative controls.

Declared expectations (before running):
 (a) exact Lyapunov, A8 setting (n=4, Rc=0.2, every member reads its 3 mates every round, no slots, qc=0):
     r(A) = 7.425938 (round-1 A8, reproduced by both round-2 codes).
 (b) MC (two replicas, shared w) at the A8 setting: within 3 SE of 7.4259.
 (c) NEGATIVE CONTROLS (must fail to reproduce 7.43): dead relays -> exact beta = 0, r = 1; MC with independent
     worlds per replica -> r far from 7.43 (round-2 attack: 42.6 at its own setting); MC dead relays -> r within
     3 SE of 1.
 (d) mechanism medium exact recursion vs MC (N=4, each agent reads 1 uniformly random other each round,
     Rc=0.1, qc=1e-4, no slots): agree within 3 SE.
 (e) no-slot I*-like niche (n=4, Rc=0.1, qc=0, all mates): r about 8.80 (round-2 attack's no-slot value).
"""
import time
import numpy as np
from flib import Par, exact_sigma_c, compound, r_ab, mc, r_and_se, medium_exact

t0 = time.time()
A8 = Par(Rc=0.2, qc=0.0, n=4, n_zero=4, m=0, types=((3, 1),))
att = ~np.eye(4, dtype=bool)
S, _, _ = exact_sigma_c(A8, att, np.zeros(4, dtype=int))
al, be = compound(S)
print(f"(a) exact A8: alpha {al:.7f} beta {be:.7f} r(A) {r_ab(4, al, be):.6f}   (expected 7.425938)")
Sd, _, _ = exact_sigma_c(A8, att, np.zeros(4, dtype=int), dead=True)
ald, bed = compound(Sd)
print(f"(c) NEG exact dead relays: beta {bed:.3e}, r {r_ab(4, ald, bed):.6f}   (must be 1)")
o = mc(A8, "full", K=1500, T=400, burn=80, seed=11)
r, se, _, _ = r_and_se(o, 4)
print(f"(b) MC A8: r {r:.4f} +- {se:.4f}   (z vs exact {(r-7.425938)/se:+.2f})  ({time.time()-t0:.0f}s)")
o = mc(A8, "full", K=1500, T=400, burn=80, seed=12, indep_world=True)
r2, se2, _, _ = r_and_se(o, 4)
print(f"(c) NEG MC independent worlds: r {r2:.3f} +- {se2:.3f}   (must be far from 7.43)")
o = mc(A8, "full", K=1500, T=400, burn=80, seed=13, dead=True)
r3, se3, _, _ = r_and_se(o, 4)
print(f"(c) NEG MC dead relays: r {r3:.4f} +- {se3:.4f}   (must be within 3 SE of 1)  ({time.time()-t0:.0f}s)")
# (d) medium
med = Par(Rc=0.1, qc=1e-4, n=4, n_zero=0, m=0, types=((1, 3),))
alm, bem, rm = medium_exact(med, N=4, c=1)
o = mc(med, "full", K=2000, T=400, burn=80, seed=14)
rmc, sem, _, _ = r_and_se(o, 4)
print(f"(d) medium N=4 c=1: exact alpha {alm:.6f} beta {bem:.6f} r_hom {rm:.4f}; MC {rmc:.4f} +- {sem:.4f} "
      f"(z {(rmc-rm)/sem:+.2f}); MC mean reads {o.mean_c:.3f}  ({time.time()-t0:.0f}s)")
# (e)
P0 = Par(Rc=0.1, qc=0.0, n=4, n_zero=4, m=0, types=((3, 1),))
S, _, _ = exact_sigma_c(P0, att, np.zeros(4, dtype=int))
print(f"(e) no-slot n=4 Rc=0.1 qc=0: r(A) {r_ab(4, *compound(S)):.4f}  (round-2 attack: 8.80)")
print(f"total {time.time()-t0:.1f}s")
