"""Deciding script 5 (sensitivity): (a) second moment read as E[Cov(e|eta,policies)] (mean-variation term dropped);
(b) finite attention precision gamma_att (softmax over the 35 kappa-subsets of the 7 others), slot law fixed at P^inf.
Expected: window stays nonempty in (a); r(A) -> 54.086 as gamma_att grows in (b)."""
import itertools, math
import numpy as np
from core import *
n, N, kappa, P0, s, c, gam, s2 = 4, 8, 3, 1.0, 1.0, 0.1, 4.0, 1e-3
law, _ = deliberation_law(n, n - 1, P0, s, c, gam); lawN, _ = deliberation_law(N, kappa, P0, s, c, gam)
att_full = lambda i, p: [(tuple(j for j in range(n) if j != i), 1.0)]
for mv in (True, False):
    SA = sigma_c_enum(n, law, att_full, P0, s, c, s2, mean_var=mv)
    rA = contrast(np.linalg.inv(block_diag(SA, SA)), range(n))
    PiH = np.linalg.inv(sigma_c_capacity(N, lawN, kappa, P0, s, c, s2, mean_var=mv))
    print("(a) mean-variation term", mv, "| r(A)", round(rA, 4), "| (c)-mechanism baseline", round(max(region_contrasts(PiH).values()), 4),
          "| medium diffusive", diffusive(PiH)[0])
def att_soft(gatt):
    def f(i, p):
        co = [j for j in range(n) if j != i]; slots = co + ["B"] * (N - n)
        acc = {}
        for J in itertools.combinations(range(N - 1), kappa):
            U = tuple(sorted(slots[k] for k in J if slots[k] != "B"))
            V = -f_info(p[i] / s + sum(p[j] for j in U) / (s + c), P0)
            acc.setdefault(U, []).append(V)
        lw = {U: [gatt * v for v in Vs] for U, Vs in acc.items()}
        mx = max(max(v) for v in lw.values())
        w = {U: sum(math.exp(v - mx) for v in vs) for U, vs in lw.items()}; Z = sum(w.values())
        return [(U, wu / Z) for U, wu in w.items()]
    return f
for gatt in (5.0, 10.0, 20.0, 40.0):
    SA = sigma_c_enum(n, law, att_soft(gatt), P0, s, c, s2)
    Pi = np.linalg.inv(block_diag(SA, SA))
    print("(b) gamma_att", gatt, "| diffusive", diffusive(Pi)[0], "| r(A)", round(contrast(Pi, range(n)), 4))
