"""Design exploration (not a deciding check): niche contrast vs baselines and habit/partner nulls."""
import itertools, math
import numpy as np
from core import *

n, N, kappa = 4, 8, 3


def att_full(i, p):
    return [(tuple(j for j in range(n) if j != i), 1.0)]


def att_random(i, p):  # uniform kappa-subset of the N-1 others, restricted to co-members
    others = [j for j in range(n) if j != i]
    out = []
    for r in range(0, min(kappa, n - 1) + 1):
        if kappa - r > N - n:
            continue
        pr = math.comb(N - n, kappa - r) / math.comb(N - 1, kappa)
        for U in itertools.combinations(others, r):
            out.append((U, pr))
    return out


if __name__ == "__main__": print("P0 s c gamma | r(A) rsub | rhom_mech | rhom_mean | r_hab | r_pr_ann")
if __name__ == "__main__":
  for P0, s, c, gam in [(1, 1, .1, 4), (1, 1, .1, 8), (1, 1, .05, 4), (4, 1, .1, 4), (4, 1, .1, 2), (1, 1, .2, 4)]:
      law, g = deliberation_law(n, n - 1, P0, s, c, gam)
      SA = sigma_c_enum(n, law, att_full, P0, s, c, 1e-3)
      Pi = np.linalg.inv(block_diag(SA, SA))
      rA = contrast(Pi, range(n))
      rsub = max(contrast(Pi, C) for C in itertools.combinations(range(n), n - 1))
      lawN, _ = deliberation_law(N, kappa, P0, s, c, gam)
      SH = sigma_c_capacity(N, lawN, kappa, P0, s, c, 1e-3)
      PiH = np.linalg.inv(SH)
      rhom = contrast(PiH, range(N))
      # (c)-mean coupling baseline from the population's own Pi
      a = -(Pi - np.diag(np.diag(Pi))); abar = a[np.triu_indices(N, 1)].mean(); ebar = Pi.sum(1).mean()
      rmean = 1 + N * abar / ebar
      Sh = sigma_c_enum(n, np.full(2 ** n, 2.0 ** -n), att_random, P0, s, c, 1e-3)
      rhab = contrast(np.linalg.inv(block_diag(Sh, Sh)), range(n))
      Sp = sigma_c_enum(n, law, att_random, P0, s, c, 1e-3)
      rpr = contrast(np.linalg.inv(block_diag(Sp, Sp)), range(n))
      print(P0, s, c, gam, "|", round(rA, 3), round(rsub, 3), "|", round(rhom, 3), "|", round(rmean, 3), "|",
            round(rhab, 3), "|", round(rpr, 3), "| P(S):", np.round([law[profiles(n).sum(1) == k].sum() for k in range(n + 1)], 3))
