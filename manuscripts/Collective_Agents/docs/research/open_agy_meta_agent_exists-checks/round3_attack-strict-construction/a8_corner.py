r"""A8 (attack): the lower corner of the candidate's +/-1% box (F, R, Rs, psi, gamma down; Q, Rc, qc up: the signs that
lower r(A) by the candidate's gradients), real protocol, recomputed with mylib.py.
Declared expectations: r(A) about 8.198 (candidate 8.1976); mean-coupling baseline about 7.169; medium about 6.0;
r0 = 7.9 admissible. FALSIFIER: r(A) < 7.9 or a baseline >= 7.9 at this corner.
"""
import time
from mylib import Cfg, sigma_c
t0 = time.time()
d = 0.01
c = Cfg(F=0.9 * (1 - d), Q=0.05 * (1 + d), R=1.0 * (1 - d), Rc=0.1 * (1 + d), Rs=2.0 * (1 - d), psi=0.030 * (1 - d),
        gamma=400.0 * (1 - d), qc=1e-4 * (1 + d), proto="real")
o = sigma_c(c, npairs=100, T=400, burn=80, every=4, seed=91)
b = o["beta"] / o["alpha"]
print(f"lower corner: r(A) {o['r']:.4f} +/- {o['se_r']:.4f}; mean-coupling baseline {1 + 24/7*b:.4f}; open {o['open']:.4f}  "
      f"({time.time()-t0:.0f}s)", flush=True)
m = sigma_c(c.w(n=8, nz=0, nrev=2), npairs=40, T=400, burn=80, every=4, seed=92)
print(f"lower corner medium (8 on one component, 2 revisers): {m['r']:.4f} +/- {m['se_r']:.4f}; r0 = 7.9 admissible under "
      f"both: {max(1 + 24/7*b, m['r']) < 7.9 <= o['r']}  ({time.time()-t0:.0f}s)")
