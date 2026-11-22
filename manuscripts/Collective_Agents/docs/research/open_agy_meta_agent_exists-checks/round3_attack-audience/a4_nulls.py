"""A4: annealed type-D nulls for P0 by two-replica Monte Carlo (own code).

Declared expectations (candidate): N_hab r(A)=1.456 +- 0.004, every region <= 1.456;
N_pr (every round) r(A)=1.541 +- 0.004, max region <= ~1.6. Both far below the
window's lower edge 3.930. If any region exceeds 3.930 under a null, the differ
clause fails at the low end of the window.
Negative control: the same code in mode 'full' reproduces r(A)~5.385 (A3).
"""
import os, sys, time
for v in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS"):
    os.environ[v] = "1"
import numpy as np
from amc import run
from alib import contrast, all_regions, diffusive_parts

regs = all_regions(5)
t0 = time.time()
for mode, seed in (("hab", 21), ("pr", 22)):
    S, Sb = run(mode, B=2000, T=1300, burn=150, seed=seed)
    Pi = np.linalg.inv(S)
    a, eps, mo, mr = diffusive_parts(Pi)
    rs = {tuple(C): contrast(Pi, C) for C in regs}
    best = max(rs.items(), key=lambda kv: kv[1])
    rb = [contrast(np.linalg.inv(Sb[k]), [1, 2, 3, 4]) for k in range(Sb.shape[0])]
    mb = []
    for k in range(Sb.shape[0]):
        Pk = np.linalg.inv(Sb[k])
        mb.append(max(contrast(Pk, C) for C in regs))
    print("%s: diffusive max offdiag %.3e min rowsum %.3f | r(A)=%.4f (batch se %.4f) | best region %s r=%.4f | max over 20 batches of max-region r = %.4f" %
          (mode, mo, mr, rs[(1, 2, 3, 4)], np.std(rb, ddof=1) / np.sqrt(len(rb)), best[0], best[1], max(mb)))
    print("   Sigma: sigma=%.5e c=%.5e Var_i=%.5e beta=%.5e" % (S[0, 0], np.mean(S[0, 1:]), np.mean(np.diag(S)[1:]),
          np.mean([S[i, j] for i in range(1, 5) for j in range(i + 1, 5)])))
    print("   a_AA mean %.3f a_SA mean %.3f leaks %s  (%.1fs)" % (np.mean([a[i, j] for i in range(1, 5) for j in range(i + 1, 5)]),
          np.mean(a[0, 1:]), np.round(eps, 2), time.time() - t0))
    sys.stdout.flush()
