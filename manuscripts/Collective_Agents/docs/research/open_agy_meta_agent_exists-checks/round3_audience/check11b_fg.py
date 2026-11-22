r"""Check 11b: diagnostic N_fg for P0 (forgetting switched off: F = 1, random-walk world, same Q).
Declared expectation before running: diffusive, r(A) > 1 (diagnostic only, reported beside the verdict)."""
import numpy as np
from aud import Par, riccati_fixed, b_of, stationary_fixed, coords, diffusive, contrast
pf = Par(F=1.0)
Pm_S1, _ = riccati_fixed(pf, 1.0 / pf.RS, 0.0)
Pm_A1, _ = riccati_fixed(pf, 1.0 / pf.R, b_of(pf, 1, 0))
S, _, _ = stationary_fixed(pf, [tuple()] + [(0,)] * pf.n, np.array([Pm_S1] + [Pm_A1] * pf.n))
Pi = np.linalg.inv(coords(pf, S))
print(f"N_fg (F = 1): diffusive {diffusive(Pi)[0]}; r(A) {contrast(Pi, (1,2,3,4)):.4f}; r(A u S) {contrast(Pi, (0,1,2,3,4)):.4f}")
