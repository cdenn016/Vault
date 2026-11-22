r"""Check 1: the (P4) slot chain.
Declared expectations: (a) at a symmetric decision state the stationary law of the 16-profile chain equals the Gibbs
law P(pi) ∝ exp(-gamma Gt(|pi|)) to 1e-14 and detailed balance holds to 1e-15 (identical-interest potential);
(b) NEGATIVE CONTROL: with one member at a different covariance state the chain violates detailed balance by
more than 1e-6 (the slot game is then not an exact potential game); (c) the vectorized chain equals a direct
loop construction to 1e-15."""
import itertools
import numpy as np
from math import comb
from lib import Pminus, efe_table, softmin_att, attention_weights, p4_chain, profiles, posterior
from instance import PAR

w = attention_weights(PAR, 3, 4)
def Gt_at(p):
    return softmin_att(PAR, efe_table(PAR, Pminus(PAR, p), 3, 4), w)
g = Gt_at(0.088)
Gt = np.tile(g, (4, 1))
v, T = p4_chain(PAR.gamma, Gt)
P = profiles(4)
gib = np.exp(-PAR.gamma * (g[P.sum(1)] - g.min())); gib /= gib.sum()
F = v[:, None] * T
print(f"(a) symmetric: max|chain - Gibbs| = {np.abs(v - gib).max():.2e}; detailed-balance violation {np.abs(F - F.T).max():.2e}")
Gt2 = Gt.copy(); Gt2[0] = Gt_at(0.095)
v2, T2 = p4_chain(PAR.gamma, Gt2)
F2 = v2[:, None] * T2
print(f"(b) NEG asymmetric (member 0 at p=0.095): detailed-balance violation {np.abs(F2 - F2.T).max():.2e}")
# (c) direct loop construction
idx = {tuple(p): k for k, p in enumerate(P)}
T3 = np.zeros_like(T)
for k, p in enumerate(P):
    for i in range(4):
        Sm = p.sum() - p[i]
        lw = np.array([np.log(0.5) - PAR.gamma * Gt2[i, Sm], np.log(0.5) - PAR.gamma * Gt2[i, Sm + 1]])
        pr = np.exp(lw - lw.max()); pr /= pr.sum()
        for x in (0, 1):
            q = p.copy(); q[i] = x
            T3[k, idx[tuple(q)]] += pr[x] / 4
print(f"(c) vectorized vs loop transition matrices: {np.abs(T2 - T3).max():.2e}")
