r"""O6 check C2 (new seed, declared after check C failed its criteria; check C's output is kept unchanged).

Why check C's criteria were ill-posed: with common random numbers the perturbed and unperturbed policy paths differ
only after a uniform falls into an O(h) gap between the two inverse CDFs; each such event changes a pair's estimate by
an O(1) amount for a few rounds (coupling time ~ 4 to 10 rounds, check B1).  So E[Delta] ~ s h while the pair-level SE
scales like sqrt(h), and at h = 1e-4 the signal s h is below one SE.  The linear-response test below is the
statistically correct form of "no discontinuity at scale h".

DECLARED EXPECTATIONS (before running; seed 4242, 32 pairs, same estimator as check C):
  L1 for psi and for Rc: with s = Delta r(1e-2)/1e-2, the CRN differences at h = 1e-3 and 1e-4 satisfy
     |Delta r(h) - s h| <= 3 SE(h)  (linear response, no jump);
  L2 for psi: the CRN pair-level SE falls by a factor between 2 and 6.3 per decade of h (sqrt(h) law of rare
     policy-flip events; factor sqrt(10) = 3.16 expected);
  L3 bound: |Delta r(1e-4)| <= 3e-3 in both directions (no jump of r(A) larger than 3e-3 within relative 1e-4).
  NEGATIVE CONTROL (must FAIL the L2 shrinkage law): with independent uniform streams at the perturbed point, the
     pair-level SE at h = 1e-2 and at h = 1e-4 agree within a factor 1.5 (no shrinkage without coupling).
"""
import os
import time
for _v in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS"):
    os.environ[_v] = "1"
import numpy as np
from sim_core import Par, run_path
from lib import pair_moments, compound

# estimator identical to check_c_continuity.py (copied, so that importing does not rerun check C)
PAR = Par(F=0.9, Q=0.05, R=1.0, Rc=0.1, Rs=2.0, Rsh=0.0, psi=0.024, gamma=400.0, qc=1e-4, n=4, n_zero=4, kmsg=3)
T, BURN, EVERY, NP = 300, 60, 4, 32
TEV = list(range(BURN, T, EVERY))


def evaluate(par, seed):
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
    K = len(rows0)
    full = r_of(rows1) - r_of(rows0)
    loo = np.array([r_of(rows1[np.arange(K) != k]) - r_of(rows0[np.arange(K) != k]) for k in range(K)])
    return full, np.sqrt((K - 1) / K * np.sum((loo - loo.mean()) ** 2))


SEED = 4242
t0 = time.time()
base = evaluate(PAR, SEED)
print(f"base r(A) = {r_of(base):.4f} ({time.time()-t0:.1f}s)")
for name in ("psi", "Rc"):
    res = {}
    for h in (1e-2, 1e-3, 1e-4):
        rows = evaluate(PAR.with_(**{name: getattr(PAR, name) * (1 + h)}), SEED)
        res[h] = r_pairs_delta(rows, base)
        print(f"  {name} h={h:.0e}: Delta r = {res[h][0]:+.3e} (SE {res[h][1]:.1e})  ({time.time()-t0:.1f}s)")
    s = res[1e-2][0] / 1e-2
    L1 = all(abs(res[h][0] - s * h) <= 3 * res[h][1] for h in (1e-3, 1e-4))
    L3 = abs(res[1e-4][0]) <= 3e-3
    zs = ", ".join(f"h={h:.0e}: z={(res[h][0]-s*h)/res[h][1]:+.2f}" for h in (1e-3, 1e-4))
    print(f"  {name}: slope s = {s:+.3f}; {zs} -> L1 {'PASS' if L1 else 'FAIL'}; |Delta r(1e-4)| = "
          f"{abs(res[1e-4][0]):.1e} -> L3 {'PASS' if L3 else 'FAIL'}")
    if name == "psi":
        f1, f2 = res[1e-2][1] / res[1e-3][1], res[1e-3][1] / res[1e-4][1]
        L2 = 2 <= f1 <= 6.3 and 2 <= f2 <= 6.3
        print(f"  psi: SE factors per decade {f1:.2f}, {f2:.2f} -> L2 {'PASS' if L2 else 'FAIL'}")
        ind = {}
        for h in (1e-2, 1e-4):
            rows = evaluate(PAR.with_(psi=PAR.psi * (1 + h)), SEED + 1)     # independent streams
            ind[h] = r_pairs_delta(rows, base)
            print(f"  NEG independent streams h={h:.0e}: Delta r = {ind[h][0]:+.3e} (SE {ind[h][1]:.1e}) "
                  f"({time.time()-t0:.1f}s)")
        fneg = ind[1e-2][1] / ind[1e-4][1]
        print(f"  NEG SE factor over two decades {fneg:.2f} -> "
              f"{'FAIL-as-expected (no shrinkage without coupling)' if 1/1.5 <= fneg <= 1.5 else 'UNEXPECTED'}")
