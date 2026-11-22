r"""Exploration only (not deciding): EFE structure of instance I* (record C11) for designing the O6 checks.

Prints the covariance fixed points p_lo, p_hi, the marginal information gain of an extra slot at those points,
the best-response threshold count at gamma = infinity, and which slot counts k are self-consistent equilibria
(n_hat(p*(k)) = k), i.e. candidates for absorbing profiles of the gamma = infinity real-time chain.
"""
import os
import sys
for _v in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS"):
    os.environ[_v] = "1"
LIB = r"C:/Users/chris and christine/Desktop/Research/manuscripts/Collective_Agents/docs/research/open_agy_meta_agent_exists-checks/round2_epistemic_persistent"
sys.path.insert(0, LIB)
import numpy as np
from lib import Par, Pminus, posterior, efe_table, softmin_att, attention_weights

PAR = Par(F=0.9, Q=0.05, R=1.0, Rc=0.1, Rs=2.0, Rsh=0.0, psi=0.024, gamma=400.0, qc=1e-4, n=4, n_zero=4, kmsg=3)


def g(par, p, a, b):
    return posterior(Pminus(par, p), a, b)[0, 0]


def fixed_point(par, a, b, p=0.05):
    for _ in range(2000):
        p = g(par, p, a, b)
    return p


par = PAR
a_min, b_min = 1 / par.R, 0.0
a_max, b_max = 1 / par.R + par.n / par.Rs, par.kmsg / (par.R + par.Rc)
p_hi = fixed_point(par, a_min, b_min)
p_lo = fixed_point(par, a_max, b_max)
print(f"p_hi (own sensor only) = {p_hi:.6f}; p_lo (all slots, 3 relays) = {p_lo:.6f}")
w = attention_weights(par, 3, 4)
for k in range(5):
    pk = fixed_point(par, 1 / par.R + k / par.Rs, 3 / (par.R + par.Rc))
    G = efe_table(par, Pminus(par, pk), 3, 4)
    Gt = softmin_att(par, G, w)
    Gmin = G.min(axis=0)
    dI = [-(G[3, j + 1] - par.psi * (j + 1)) + (G[3, j] - par.psi * j) for j in range(4)]
    # best response (gamma = inf): reviser with n_other others open opens iff Gmin[n_other+1] < Gmin[n_other]
    opens = [bool(Gmin[j + 1] < Gmin[j]) for j in range(4)]
    stable = (k == 0 or opens[k - 1]) and (k == 4 or not opens[k])
    lw = np.log([1, 4, 6, 4, 1]) - par.gamma * Gt
    lw -= lw.max()
    law = np.exp(lw) / np.exp(lw).sum()
    print(f"k={k}: p*(k)={pk:.6f}  marginal info gain of slot j->j+1 (3 relays): "
          + " ".join(f"{d:.5f}" for d in dI) + f"  psi={par.psi}  BR opens at n_other=0..3: {opens}  "
          f"k self-consistent: {stable}; gamma=400 Gibbs count law at p*(k): {np.round(law, 4)}")
