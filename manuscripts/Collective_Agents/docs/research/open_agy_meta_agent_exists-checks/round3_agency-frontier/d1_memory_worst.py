r"""D1 deciding run 4: worst reachable per-step closure defect (bounds the pathwise Markov defect, since
I(y_{t+1}; y_{0:t-1} | y_t) <= I(y_{t+1}; x_t | y_t) = d_cl(t) by data processing) over single-round deviations
c in {0,1}^2, k in {0..m}^2 from the stationary state, and over two consecutive deviation rounds with k in {0,..,m}
for one member, for Rs in {1, 10}; with the probability of the worst pattern under the full model's policy law.
Declared expectations: the worst involves a member opening many slots (large asymmetric gain change); at Rs = 1 it is
above 0.02 (0.039 already at k = 2) and grows with k; at Rs = 10 it stays below 0.02.  The probability of any slot
opening per member-round is about 1e-11 (Rs = 1).
NEGATIVE CONTROL: the symmetric stationary step must reproduce d_cl = 8.906e-4 (Rs = 1).
"""
import time
import itertools
import numpy as np
from scipy.linalg import solve_discrete_lyapunov
from flib import dcl_step, steady_prior, member_mats, member_policy_law
from design import make_design

t0 = time.time()
for Rs in (1.0, 10.0):
    par, gmax = make_design(m=8, Rs=Rs)
    n = 2
    Pm = steady_prior(par, 1, 0)
    M, k_own, k_slot, k_rel, _ = member_mats(par, Pm, 1, 0)
    A = np.kron(np.eye(n), M)
    Qn = np.kron(np.eye(n), par.Rc * np.outer(k_rel, k_rel) + par.qc * np.eye(2))
    Sig = solve_discrete_lyapunov(A, Qn)
    base = dcl_step(par, [Pm, Pm], [1, 1], [0, 0], Sig, n)
    worst, arg = 0.0, None
    for cs in itertools.product((0, 1), repeat=n):
        for ks in itertools.product(range(par.m + 1), repeat=n):
            v = dcl_step(par, [Pm, Pm], cs, ks, Sig, n)
            if v > worst:
                worst, arg = v, (cs, ks)
    # two consecutive deviation rounds for member 0 (k slots each round, c = 0 or 1), member 1 stationary
    worst2, arg2 = 0.0, None
    for c0 in (0, 1):
        for k0 in range(par.m + 1):
            M0, _, _, kr0, Pp0 = member_mats(par, Pm, c0, k0)
            Ad = np.zeros((4, 4)); Ad[:2, :2] = M0; Ad[2:, 2:] = M
            Qd = np.zeros((4, 4)); Qd[:2, :2] = c0 * par.Rc * np.outer(kr0, kr0) + par.qc * np.eye(2)
            Qd[2:, 2:] = par.Rc * np.outer(k_rel, k_rel) + par.qc * np.eye(2)
            S2 = Ad @ Sig @ Ad.T + Qd
            Pm0 = np.array([[par.F ** 2 * Pp0[0, 0] + par.Q + par.qc, par.F * Pp0[0, 0]],
                            [par.F * Pp0[0, 0], Pp0[0, 0] + par.qc]])
            for c1 in (0, 1):
                for k1 in range(par.m + 1):
                    v = dcl_step(par, [Pm0, Pm], [c1, 1], [k1, 0], S2, n)
                    if v > worst2:
                        worst2, arg2 = v, ((c0, k0), (c1, k1))
    P, G = member_policy_law(par, Pm)
    p_open = 1 - P[:, 0].sum()
    print(f"Rs={Rs}: psi {par.psi:.4f} (g_max {gmax:.4f}); stationary step d_cl {base:.4e}; worst single-round "
          f"deviation {worst:.4e} at (c, k) = {arg}; worst two-round (member 0) {worst2:.4e} at {arg2}; "
          f"P(any slot open per member-round) {p_open:.2e}  ({time.time()-t0:.0f}s)")
