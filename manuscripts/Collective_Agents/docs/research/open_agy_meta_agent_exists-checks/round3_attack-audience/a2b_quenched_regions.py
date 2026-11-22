"""A2b: which regions reach r >= 4.5 in diffusive quenched N_pr draws, and with what
probability (draws uniform over 4^4).  Expectation: unknown (A2 found max 4.887)."""
import os
for v in ("OMP_NUM_THREADS","MKL_NUM_THREADS","OPENBLAS_NUM_THREADS"): os.environ[v]="1"
import itertools, numpy as np
from alib import fixed_schedule_sigma, contrast, all_regions, diffusive_parts
regs = all_regions(5)
hits = {}; ndraw_hit = 0
for draw in itertools.product(range(4), repeat=4):
    reads = []
    for i, d in enumerate(draw, start=1):
        others = [0] + [j for j in range(1, 5) if j != i]
        reads.append(others[d])
    Sc, _ = fixed_schedule_sigma(reads)
    Pi = np.linalg.inv(Sc)
    _, _, mo, mr = diffusive_parts(Pi)
    if mo <= 1e-12 and mr >= -1e-12:
        sel = [(tuple(C), contrast(Pi, C)) for C in regs if contrast(Pi, C) >= 4.5]
        if sel:
            ndraw_hit += 1
            for C, r in sel:
                hits.setdefault((tuple(reads), C), r)
print("diffusive quenched draws with some region at r >= 4.5: %d / 256" % ndraw_hit)
for (reads, C), r in sorted(hits.items(), key=lambda kv: -kv[1])[:12]:
    print("  reads (member1..4 -> source)", reads, " region", C, " r=%.4f" % r)
