"""A2: quenched partner randomization (drawn once) for P0, all 4^4 draws, exact.

Also cross-checks the general fixed-schedule builder against A1 (all read S).
Declared expectations (candidate, check 11): 54/256 diffusive; only the all-source
draw (prob 1/256) selects A at r0 in (3.930, 5.385].
Negative control: the all-source draw must reproduce r(A)=5.384864 exactly.
Also reports the participation ratio of a P0 member's partner distribution in the
full model and under the every-round null.
"""
import os
for v in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS"):
    os.environ[v] = "1"
import itertools
import numpy as np
from alib import fixed_schedule_sigma, contrast, all_regions, diffusive_parts, P0Model

regs = all_regions(5)
Sc, _ = fixed_schedule_sigma([0, 0, 0, 0])
print("all-source draw: r(A) = %.6f (expect 5.384864)" % contrast(np.linalg.inv(Sc), [1, 2, 3, 4]))

ndiff = 0
nselA = 0
rows = []
for draw in itertools.product(range(4), repeat=4):
    reads = []
    for i, d in enumerate(draw, start=1):
        others = [0] + [j for j in range(1, 5) if j != i]
        reads.append(others[d])
    Sc, _ = fixed_schedule_sigma(reads)
    Pi = np.linalg.inv(Sc)
    _, _, mo, mr = diffusive_parts(Pi)
    dif = (mo <= 1e-12) and (mr >= -1e-12)
    if dif:
        ndiff += 1
        rA = contrast(Pi, [1, 2, 3, 4])
        rmax = max(contrast(Pi, C) for C in regs)
        if rA >= 3.930115:
            nselA += 1
        rows.append((tuple(reads), rA, rmax))
print("quenched draws: diffusive %d / 256 ; draws with r(A) >= 3.930115: %d" % (ndiff, nselA))
top = sorted(rows, key=lambda x: -x[2])[:6]
for t in top:
    print("  reads", t[0], "r(A)=%.4f max region r=%.4f" % (t[1], t[2]))

# participation ratio of a member's partner distribution
m = P0Model()
p, _ = m.policy_probs()
part = np.array([p["S"], p["m1"], p["m2"], p["m3"]])
part = part / part.sum()
print("\nP0 member partner distribution:", part, " PR = 1/sum p^2 = %.6f" % (1 / np.sum(part ** 2)))
u = np.ones(4) / 4
print("every-round uniform redraw: long-run partner distribution", u, " PR = %.3f" % (1 / np.sum(u ** 2)))
