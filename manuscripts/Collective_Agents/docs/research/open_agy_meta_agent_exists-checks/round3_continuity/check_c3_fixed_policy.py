r"""O6 check C3 (diagnostic for the Rc failure of check C2, L1): smooth part of r(A) along FIXED policy paths.

Post hoc explanation to be tested: in check C2 the 32 pairs at Rc*(1 + 1e-4) contained no policy-flip event (pair SE
2.2e-7), so Delta r measured only the derivative along fixed policy paths, which differs from the h = 1e-2 slope
(-0.690) by the contribution of policy flips.

DECLARED EXPECTATIONS (before running; same seed 4242, same 32 pairs, policy paths frozen at their theta* realization,
Riccati covariances and gains recomputed at Rc*(1 + h)):
  F1 Delta r_fixed(h)/h is the same for h = 1e-2, 1e-3, 1e-4 within 2% (smooth in Rc along fixed paths);
  F2 Delta r_fixed(1e-4)/1e-4 equals the check C2 value -0.5241 within 1%.
  NEGATIVE CONTROL: the same computation with Rc perturbed only in the error recursion (lib.pair_moments) but NOT in
     the covariance recursion that sets the gains gives a different slope (|ratio - 1| > 5%), showing that F2 is not
     automatic.
"""
import os
import time
for _v in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS"):
    os.environ[_v] = "1"
import numpy as np
from sim_core import Par, run_path, Pminus, posterior
from lib import pair_moments, compound, Path

PAR = Par(F=0.9, Q=0.05, R=1.0, Rc=0.1, Rs=2.0, Rsh=0.0, psi=0.024, gamma=400.0, qc=1e-4, n=4, n_zero=4, kmsg=3)
T, BURN, EVERY, NP, SEED = 300, 60, 4, 32, 4242
TEV = list(range(BURN, T, EVERY))


def refit(par: Par, pth: Path) -> Path:
    r"""Recompute the prior covariances along the fixed policy path at parameters par (initial p = 0.09)."""
    n = par.n
    p = np.full(n, 0.09)
    Pm = np.zeros_like(pth.Pm)
    for t in range(len(pth.mates)):
        for i in range(n):
            Pm[t, i] = Pminus(par, p[i])
        for i in range(n):
            p[i] = posterior(Pm[t, i], 1.0 / par.R + pth.vis[t, i] / (par.Rs + par.Rsh),
                             len(pth.mates[t][i]) / (par.R + par.Rc))[0, 0]
    return Path(Pm, pth.mates, pth.slots, pth.vis, pth.att_dev)


t0 = time.time()
paths = [(run_path(PAR, T, np.random.default_rng([SEED, k, 0]), "fast"),
          run_path(PAR, T, np.random.default_rng([SEED, k, 1]), "fast")) for k in range(NP)]


def r_fixed(par_cov: Par, par_err: Par) -> float:
    A, B = [], []
    for pa, pb in paths:
        qa, qb = refit(par_cov, pa), refit(par_cov, pb)
        res = pair_moments(par_err, qa, qb, TEV)
        al, be = compound(np.mean([r[0] for r in res], axis=0))
        A.append(al); B.append(be)
    return 1 + 4 * np.mean(B) / np.mean(A)


r0 = r_fixed(PAR, PAR)
print(f"r_fixed(theta*) = {r0:.4f} (equals the check C2 base value 4.3878 by construction)")
check = []
for h in (1e-2, 1e-3, 1e-4):
    par = PAR.with_(Rc=PAR.Rc * (1 + h))
    d = r_fixed(par, par) - r0
    check.append(d / h)
    print(f"h={h:.0e}: Delta r_fixed = {d:+.4e}, /h = {d/h:+.5f}  ({time.time()-t0:.1f}s)")
F1 = (max(abs(c) for c in check) / min(abs(c) for c in check) - 1) <= 0.02 and np.ptp(np.sign(check)) == 0
F2 = abs(check[2] / (-0.5241) - 1) <= 0.01
print(f"F1 slopes {', '.join(f'{c:+.5f}' for c in check)} -> {'PASS' if F1 else 'FAIL'}; "
      f"F2 vs C2 value -0.5241 -> {'PASS' if F2 else 'FAIL'}")
par = PAR.with_(Rc=PAR.Rc * (1 + 1e-4))
dneg = (r_fixed(PAR, par) - r0) / 1e-4
print(f"NEG gains held at Rc*, error noise at Rc*(1+1e-4): slope {dneg:+.5f}, ratio to F2 slope {dneg/check[2]:.3f} -> "
      f"{'FAIL-as-expected' if abs(dneg/check[2] - 1) > 0.05 else 'UNEXPECTED'}  ({time.time()-t0:.1f}s)")
