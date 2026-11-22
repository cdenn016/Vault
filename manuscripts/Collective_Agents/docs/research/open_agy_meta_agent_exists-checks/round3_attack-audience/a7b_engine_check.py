"""A7b: diagnose the 4.5-SE gap of engine 2 (amc2) on P0 against the exact value.
Prints Sigma^c entries from both engines (amc, amc2) at two seeds each.
Expectation: if both engines agree with exact entries within ~3 SE, the gap in r(A)
is estimator noise/bias of the ratio; otherwise engine 2 has a bug.
"""
import os, sys
for v in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS"):
    os.environ[v] = "1"
import itertools
import numpy as np
import amc, amc2
from alib import P0Model, contrast

ex = P0Model().sigma_c()
print("exact  sigma %.5e c %.5e var %.5e beta %.5e r(A) %.4f" % (ex[0, 0], ex[0, 1], ex[1, 1], ex[1, 2], contrast(np.linalg.inv(ex), [1, 2, 3, 4])))
Rsen = [0.01, 1.0, 1.0, 1.0, 1.0]
o = [[()]]
for i in range(1, 5):
    others = [0] + [j for j in range(1, 5) if j != i]
    o.append([()] + [(j,) for j in others])


def pr(lbl, S, Sb):
    se = Sb.std(axis=0, ddof=1) / np.sqrt(Sb.shape[0])
    mem = range(1, 5)
    c = np.mean(S[0, 1:]); cse = np.mean(se[0, 1:])
    v = np.mean(np.diag(S)[1:]); vse = np.mean(np.diag(se)[1:])
    b = np.mean([S[i, j] for i in mem for j in mem if i < j]); bse = np.mean([se[i, j] for i in mem for j in mem if i < j])
    print("%-12s sigma %.5e (%.1e) c %.5e (%.1e) var %.5e (%.1e) beta %.5e (%.1e) r(A) %.4f" %
          (lbl, S[0, 0], se[0, 0], c, cse, v, vse, b, bse, contrast(np.linalg.inv(S), [1, 2, 3, 4])))
    sys.stdout.flush()


for sd in (41, 42):
    S, Sb = amc.run("full", B=2000, T=900, burn=150, seed=sd)
    pr("amc s%d" % sd, S, Sb)
    S, Sb, _ = amc2.run(Rsen, o, mode="efe", gamma=40.0, B=2000, T=900, burn=150, seed=sd)
    pr("amc2 s%d" % sd, S, Sb)
