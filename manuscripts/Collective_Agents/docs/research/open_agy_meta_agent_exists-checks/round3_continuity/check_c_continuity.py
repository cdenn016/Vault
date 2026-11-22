r"""O6 check C: numerical illustration of the continuity of r(A) (Theorem 2 and 3 of the O6 report) at I*, T-fast.

Sigma^c_A is estimated as in the constructor's run_main.py: exact two-replica Gaussian algebra (lib.pair_moments,
read-only import) per pair of independent policy paths, averaged over pairs and over rounds 60..296 step 4 of
300-round paths; r(A) = 1 + 4 beta/alpha from the compound projection.  Policy paths come from sim_core (validated
against lib in check B0).  Common random numbers: pair k uses the same uniform streams at every parameter value, which
couples the policy paths synchronously (check B1), so differences isolate the parameter effect.

DECLARED EXPECTATIONS (before running):
  C0 r(A)(theta*) from 32 pairs lies in 4.391 +/- 0.04 (constructor, T-fast: 4.3912 +/- 0.0044 with 160 pairs).
  C1 direction psi, relative steps h = 1e-2, 1e-3, 1e-4 with common random numbers: |Delta r(h)|/h is the same within
     a factor 3 across the three steps, and the pair-level SE of Delta r shrinks at least 10-fold from h = 1e-2 to 1e-4.
  C2 direction Rc (changes the Riccati maps, not only the policy kernel): same criteria.
  C3 open rate (a functional of the one-time stationary law mu_theta, Theorem 1): |Delta open|/h same within factor 3.
  NEGATIVE CONTROL (must fail the shrinkage criterion): the same difference at h = 1e-4 with INDEPENDENT uniform
     streams at the perturbed point has pair-level SE at least 20 times the common-random-number SE.
"""
import os
import sys
import time
for _v in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS"):
    os.environ[_v] = "1"
import numpy as np
from sim_core import Par, run_path
from lib import pair_moments, compound

PAR = Par(F=0.9, Q=0.05, R=1.0, Rc=0.1, Rs=2.0, Rsh=0.0, psi=0.024, gamma=400.0, qc=1e-4, n=4, n_zero=4, kmsg=3)
T, BURN, EVERY, NP = 300, 60, 4, 32
TEV = list(range(BURN, T, EVERY))


def evaluate(par, seed):
    r"""Per-pair (alpha, beta, open rate) with the uniform streams of pair k fixed by (seed, k)."""
    rows = []
    for k in range(NP):
        pa = run_path(par, T, np.random.default_rng([seed, k, 0]), "fast")
        pb = run_path(par, T, np.random.default_rng([seed, k, 1]), "fast")
        res = pair_moments(par, pa, pb, TEV)
        S = np.mean([r[0] for r in res], axis=0)
        al, be = compound(S)
        rows.append((al, be, 0.5 * (pa.slots[BURN:].mean() + pb.slots[BURN:].mean())))
    return np.array(rows)


def r_of(rows):
    return 1 + 4 * rows[:, 1].mean() / rows[:, 0].mean()


def r_pairs_delta(rows1, rows0):
    r"""Jackknife SE of r(rows1) - r(rows0) over pairs (pairs are matched)."""
    K = len(rows0)
    full = r_of(rows1) - r_of(rows0)
    loo = []
    for k in range(K):
        m = np.arange(K) != k
        loo.append(r_of(rows1[m]) - r_of(rows0[m]))
    loo = np.array(loo)
    return full, np.sqrt((K - 1) / K * np.sum((loo - loo.mean()) ** 2))


t0 = time.time()
base = evaluate(PAR, 777)
r0 = r_of(base)
K = NP
loo = np.array([r_of(base[np.arange(K) != k]) for k in range(K)])
se0 = np.sqrt((K - 1) / K * np.sum((loo - loo.mean()) ** 2))
print(f"C0 r(A)(theta*) = {r0:.4f} +/- {se0:.4f} (32 pairs); open rate {base[:, 2].mean():.4f} -> "
      f"{'PASS' if abs(r0 - 4.391) < 0.04 else 'FAIL'}  ({time.time()-t0:.1f}s)")

for name in ("psi", "Rc"):
    print(f"direction {name} (theta* value {getattr(PAR, name)})")
    slopes, ses, oslopes = [], [], []
    for h in (1e-2, 1e-3, 1e-4):
        par = PAR.with_(**{name: getattr(PAR, name) * (1 + h)})
        rows = evaluate(par, 777)
        d, se = r_pairs_delta(rows, base)
        do = rows[:, 2].mean() - base[:, 2].mean()
        slopes.append(abs(d) / h); ses.append(se); oslopes.append(abs(do) / h)
        print(f"  h={h:.0e}: Delta r = {d:+.3e} (pair SE {se:.1e}), Delta r/h = {d/h:+.3f}; "
              f"Delta open = {do:+.3e}, /h = {do/h:+.3f}  ({time.time()-t0:.1f}s)")
    ok_r = max(slopes) <= 3 * min(slopes) and ses[2] <= ses[0] / 10
    ok_o = max(oslopes) <= 3 * min(oslopes) if min(oslopes) > 0 else False
    print(f"  {name}: r(A) slope ratio max/min {max(slopes)/max(min(slopes),1e-300):.2f}, SE shrink "
          f"{ses[0]/max(ses[2],1e-300):.1f}x -> {'PASS' if ok_r else 'FAIL'}; open-rate slope ratio "
          f"{max(oslopes)/max(min(oslopes),1e-300):.2f} -> {'PASS' if ok_o else 'FAIL'}")
    if name == "psi":
        par = PAR.with_(psi=PAR.psi * (1 + 1e-4))
        rows = evaluate(par, 999)          # independent uniform streams
        d, se = r_pairs_delta(rows, base)
        print(f"  NEGATIVE CONTROL (independent streams, h=1e-4): Delta r = {d:+.3e} (pair SE {se:.1e}); "
              f"SE ratio to common-random-number SE {se/max(ses[2],1e-300):.0f}x -> "
              f"{'FAIL-as-expected (no shrinkage without coupling)' if se >= 20 * ses[2] else 'UNEXPECTED'} "
              f"({time.time()-t0:.1f}s)")
