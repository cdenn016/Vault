"""A3: validate the two-replica Monte Carlo against the exact Lyapunov result (full
model), plus two negative controls.

Declared expectations:
  full: Sigma^c entries within ~3 SE of exact (sigma 6.0718e-3, c 6.589e-4,
        Var 7.5547e-3, beta 4.0304e-3); r(A) within ~3 SE of 5.3849.
  NC-a (independent worlds): member covariance far above exact (fails to match).
  NC-b (dead channels): member off-diagonals ~0 within SE (diagonal).
"""
import os, sys, time
for v in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS"):
    os.environ[v] = "1"
import numpy as np
from amc import run
from alib import P0Model, contrast

ex = P0Model().sigma_c()


def summ(S_all, S_b, label):
    nb = S_b.shape[0]
    se = S_b.std(axis=0, ddof=1) / np.sqrt(nb)
    mem = [1, 2, 3, 4]
    covs = [S_all[i, j] for i in mem for j in mem if i < j]
    covs_se = [se[i, j] for i in mem for j in mem if i < j]
    rA = contrast(np.linalg.inv(S_all), mem)
    rAb = []
    for k in range(nb):
        try:
            rAb.append(contrast(np.linalg.inv(S_b[k]), mem))
        except Exception:
            pass
    print("%s: sigma=%.5e (se %.1e) c=%.5e (se %.1e) Var_i=%.5e beta=%.5e (se %.1e) r(A)=%.4f (batch se %.4f)" %
          (label, S_all[0, 0], se[0, 0], np.mean(S_all[0, 1:]), np.mean(se[0, 1:]), np.mean(np.diag(S_all)[1:]),
           np.mean(covs), np.mean(covs_se), rA, np.std(rAb, ddof=1) / np.sqrt(len(rAb))))
    return S_all


t0 = time.time()
print("exact: sigma=%.5e c=%.5e Var_i=%.5e beta=%.5e" % (ex[0, 0], ex[0, 1], ex[1, 1], ex[1, 2]))
S, Sb = run("full", B=2000, T=1000, burn=150, seed=11)
summ(S, Sb, "MC full")
print("  time %.1fs" % (time.time() - t0)); sys.stdout.flush()
S, Sb = run("full", B=400, T=500, burn=150, seed=12, indep_world=True)
summ(S, Sb, "NC-a indep worlds")
S, Sb = run("dead", B=1000, T=500, burn=150, seed=13)
summ(S, Sb, "NC-b dead channels")
print("total time %.1fs" % (time.time() - t0))
