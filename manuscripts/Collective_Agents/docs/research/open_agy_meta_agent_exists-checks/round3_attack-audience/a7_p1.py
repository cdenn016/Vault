"""A7: relay variant P1 (kappa_msg = 2) with my own general engine.

Declared expectations (candidate): member law {S}: 0.2154, each {S,m_j}: 0.2615;
r(A) = 5.3724 +- 1e-4 (diffusive); mean-coupling baseline 3.8128;
E[Cov(e_i,e_j | X_sh, zeta_S)] = 3.8e-5 against Var 3.55e-3 (corr 0.011) > 0.
My additional claim to test: the member-member channels LOWER r(A) relative to P0
(5.3849), i.e. the contrast is not produced by member interaction.
Validation (must pass): the same engine on P0 (kappa=1) gives r(A) within 3 SE of 5.3849.
Negative control (must fail to show member dependence): P0 with zeta_S shared gives
member off-diagonal conditional covariance ~0 within SE.
"""
import os, sys, time
for v in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS"):
    os.environ[v] = "1"
import itertools
import numpy as np
from amc2 import run
from alib import contrast, all_regions, diffusive_parts, mean_coupling_baseline

Rsen = [0.01, 1.0, 1.0, 1.0, 1.0]
regs = all_regions(5)


def opts_for(kappa):
    o = [[()]]
    for i in range(1, 5):
        others = [0] + [j for j in range(1, 5) if j != i]
        L = []
        for k in range(kappa + 1):
            L += list(itertools.combinations(others, k))
        o.append(L)
    return o


def report(label, S, Sb):
    Pi = np.linalg.inv(S)
    a, eps, mo, mr = diffusive_parts(Pi)
    rA = contrast(Pi, [1, 2, 3, 4])
    rb = [contrast(np.linalg.inv(Sb[k]), [1, 2, 3, 4]) for k in range(Sb.shape[0])]
    best_other = max((contrast(Pi, C), C) for C in regs if C != [1, 2, 3, 4])
    print("%s: max offdiag %.3e min rowsum %.3f | r(A)=%.4f (se %.4f) | best other %s %.4f | mean-coupling baseline %.4f" %
          (label, mo, mr, rA, np.std(rb, ddof=1) / np.sqrt(len(rb)), best_other[1], best_other[0], mean_coupling_baseline(Pi)))
    sys.stdout.flush()


t0 = time.time()
S, Sb, fr = run(Rsen, opts_for(1), mode="efe", gamma=40.0, B=2000, T=900, seed=31)
report("P0 via engine", S, Sb)
S, Sb, fr = run(Rsen, opts_for(1), mode="efe", gamma=40.0, B=2000, T=700, seed=32, share_S=True)
off = [S[i, j] for i in range(1, 5) for j in range(i + 1, 5)]
offb = [np.mean([Sb[k][i, j] for i in range(1, 5) for j in range(i + 1, 5)]) for k in range(Sb.shape[0])]
print("NC P0 zeta_S shared: member offdiag mean %.3e (se %.1e), var %.3e  (%.0fs)" %
      (np.mean(off), np.std(offb, ddof=1) / np.sqrt(len(offb)), np.mean(np.diag(S)[1:]), time.time() - t0))
sys.stdout.flush()

o2 = opts_for(2)
S, Sb, fr = run(Rsen, o2, mode="efe", gamma=40.0, B=2000, T=1300, seed=33)
report("P1", S, Sb)
names = [str(s) for s in o2[1]]
print("  member 1 option frequencies:", {n_: round(float(f), 4) for n_, f in zip(names, fr[1]) if f > 1e-4})
print("  time %.0fs" % (time.time() - t0)); sys.stdout.flush()
S, Sb, fr = run(Rsen, o2, mode="efe", gamma=40.0, B=2000, T=1000, seed=34, share_S=True)
off = [S[i, j] for i in range(1, 5) for j in range(i + 1, 5)]
offb = [np.mean([Sb[k][i, j] for i in range(1, 5) for j in range(i + 1, 5)]) for k in range(Sb.shape[0])]
print("P1 zeta_S shared: member offdiag mean %.3e (se %.1e), var %.3e, corr %.4f  (%.0fs)" %
      (np.mean(off), np.std(offb, ddof=1) / np.sqrt(len(offb)), np.mean(np.diag(S)[1:]),
       np.mean(off) / np.mean(np.diag(S)[1:]), time.time() - t0))
