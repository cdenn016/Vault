r"""C8 consequence ("if N_eff is type D, no collective in setting P is a meta-agent") under the two
comparison-medium conventions.  Instance of setting P: two niches of n=4 on independent world components,
fixed identical gains (not Kalman), deterministic acts u_j = -g m_j^+, members read their niche's total act.
Full model: brute-force conditioning on the world path.  N_eff: the act's effect on eta is exogenous forcing,
members keep their update m' = F m^+ + b U, so given the (now exogenous) world path the members follow
m' = (F I - b g J)(c0 m + k1 eta + zeta): Lyapunov equation.
"""
import numpy as np
from scipy.linalg import solve_discrete_lyapunov

from chk2_settingP import build, closed_form, cond_cov, contrast

n, F, b, g, Q, R, Rc, Ks, Kc = 4, 0.9, 0.2, 0.125, 0.002, 1.0, 0.1, 0.2, 0.2
alpha, v, r0, Dfb, Dcoll, c0, phi, s = closed_form(n, Ks, Kc, F, b, g, Q, R, Rc)
A, Qx, firm = build([n], [Ks], [Kc], [F], [b], [g], b, F, Q, R, Rc)
S = cond_cov(A, Qx, L=120)
Pi_blk = np.linalg.inv(S)
r_full = contrast(Pi_blk, range(n))
# N_eff
J = np.ones((n, n))
zc = (Ks ** 2 * R + (n - 1) * Kc ** 2 * (R + Rc) - (2 * Ks * Kc * R + (n - 2) * Kc ** 2 * R))  # a = Var - Cov
cc = 2 * Ks * Kc * R + (n - 2) * Kc ** 2 * R
Cz = zc * np.eye(n) + cc * J
T = F * np.eye(n) - b * g * J
S_eff = solve_discrete_lyapunov(c0 * T, T @ Cz @ T.T)
Pi_eff_blk = np.linalg.inv(S_eff)
r_eff = contrast(Pi_eff_blk, range(n))
print(f"setting P instance: c0={c0:.3f} phi={phi:.3f} s={s:.4f}  r0={r0:.4f} D_fb={Dfb:.4f} D_coll={Dcoll:.4f}")
print(f" full model: r(A) brute force {r_full:.4f}, closed form {v / alpha:.4f}; N_eff: r_eff(A) brute force {r_eff:.4f}, closed form r0*D_fb {r0 * Dfb:.4f}")


def population(Pi_b):
    P = np.zeros((2 * n, 2 * n)); P[:n, :n] = Pi_b; P[n:, n:] = Pi_b
    return P


def mean_coupling_baseline(P):
    N = P.shape[0]
    eps = P.sum(1).mean(); a = -(P - np.diag(np.diag(P)))[np.triu_indices(N, 1)].mean()
    return max((eps + m * a) / (eps + (N - m) * a) for m in range(2, N + 1))


Pf, Pe = population(Pi_blk), population(Pi_eff_blk)
for nm, P in (("full", Pf), ("N_eff", Pe)):
    off = P - np.diag(np.diag(P))
    print(f" {nm}: diffusive={off.max() <= 1e-9 and P.sum(1).min() >= 0}, r(A)={contrast(P, range(n)):.4f}, r(3-subset)={contrast(P, range(3)):.4f}, "
          f"r(A u B)={contrast(P, range(2 * n)):.4f}, mean-coupling baseline of this precision={mean_coupling_baseline(P):.4f}")
bf, be = mean_coupling_baseline(Pf), mean_coupling_baseline(Pe)
print(f" convention 1 (baseline held at the full model's {bf:.4f} under the null): window ({bf:.4f}, {r_full:.4f}]; "
      f"N_eff selects A at every level of it (r_eff={r_eff:.4f} >= r0): same partition -> does not differ (C8 as stated)")
print(f" convention 2 (baseline recomputed from the null's precision, {be:.4f}): for every r0 in ({bf:.4f}, {r_full:.4f}] the null has "
      f"r0 <= {r_full:.4f} < {be:.4f}, so A is not a collective under N_eff at any admissible level -> differs at each constant: {r_full < be}")
print(f" sub-block caveat of Prop N: n-1 = {n - 1}; here r0 > {bf:.2f} >= n-1, so no sub-block is selected in either model")
# control: weak acts (PN-like), where the two conventions agree on 'does not differ' for r0 near the top of the window
g2, Q2 = 0.05, 0.05
al2, v2, r02, Dfb2, Dcoll2, *_ = closed_form(n, Ks, Kc, F, b, g2, Q2, R, Rc)
r2, re2 = v2 / al2, r02 * Dfb2
c = 2 * (n - 1) / (2 * n - 1)
print(f" control (g={g2}, Q={Q2}): r={r2:.4f}, r_eff={re2:.4f}, own baselines {1 + c * (r2 - 1):.4f} / {1 + c * (re2 - 1):.4f}: "
      f"null baseline < r, so at r0 in ({1 + c * (re2 - 1):.4f}, {r2:.4f}] both select A under either convention")
