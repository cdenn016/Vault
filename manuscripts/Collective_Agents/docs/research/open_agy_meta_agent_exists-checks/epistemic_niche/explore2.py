"""Design exploration 2: window under clause (c)-mechanism as a function of gamma (not a deciding check)."""
import itertools, math
import numpy as np
from core import *
from explore import att_full, att_random, n, N, kappa
print("c gamma | r(A) | rhom_mech | rhom_mean | r_hab | r_pr | Agency | alphaI | P(S=4)")
for c in (0.05, 0.1):
    for gam in (8, 16, 24, 32, 48, 64, 1e9):
        P0, s = 1.0, 1.0
        law, g = deliberation_law(n, n - 1, P0, s, c, gam)
        SA = sigma_c_enum(n, law, att_full, P0, s, c, 1e-3)
        Pi = np.linalg.inv(block_diag(SA, SA)); rA = contrast(Pi, range(n))
        lawN, _ = deliberation_law(N, kappa, P0, s, c, gam)
        rhom = contrast(np.linalg.inv(sigma_c_capacity(N, lawN, kappa, P0, s, c, 1e-3)), range(N))
        a = -(Pi - np.diag(np.diag(Pi))); rmean = 1 + N * a[np.triu_indices(N, 1)].mean() / Pi.sum(1).mean()
        Sp = sigma_c_enum(n, law, att_random, P0, s, c, 1e-3)
        rpr = contrast(np.linalg.inv(block_diag(Sp, Sp)), range(n))
        ag = agency_index(law, n, P0, s)[0] if gam < 1e8 else float('nan')
        aI = inference_kl(n, law, P0, s, c, 1e-3)
        print(c, gam, "|", round(rA, 3), "|", round(rhom, 3), "|", round(rmean, 3), "|", round(rpr, 3), "|", round(ag, 6), "|", round(aI, 5), "|", round(law[-1], 4))
