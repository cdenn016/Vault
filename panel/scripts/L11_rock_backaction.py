"""L11: recompute Appendix B (PIFB2 2547-2587) rock derivations and test the back-action claim
in the framework's own Fisher geometry.

F_R = KL(q_R || p_R) + beta KL(q_R || r),  q_R = N(mu, v), p_R = N(mu_p, eps), r = N(mu_r, v_r)  (1D per axis)
"""
import sympy as sp

mu, mup, mur = sp.symbols('mu mu_p mu_r', real=True)
v, eps, vr, beta, eta = sp.symbols('v epsilon v_r beta eta', positive=True)

def kl(m1, s1, m2, s2):
    """KL(N(m1,s1) || N(m2,s2)) for scalar variances s1, s2."""
    return sp.Rational(1, 2) * (s1 / s2 + (m1 - m2) ** 2 / s2 - 1 + sp.log(s2 / s1))

F = kl(mu, v, mup, eps) + beta * kl(mu, v, mur, vr)

print("== manuscript formulas ==")
gmu = sp.diff(F, mu)
print("grad_mu F - [Lp(mu-mup)+beta Lr(mu-mur)] =", sp.simplify(gmu - ((mu - mup) / eps + beta * (mu - mur) / vr)))
mudot = -eta * v * gmu
print("mu_dot at v=eps:", sp.expand(mudot.subs(v, eps)))
gS_coup = sp.diff(beta * kl(mu, v, mur, vr), v)
print("coupling dF/dSigma - beta/2 (1/v_r - 1/v) =", sp.simplify(gS_coup - beta / 2 * (1 / vr - 1 / v)))
Sdot_back = -2 * eta * v * gS_coup * v
print("Sigma_dot^back at v=eps:", sp.expand(Sdot_back.subs(v, eps)), " -> O(eps) absolute: manuscript eq. rock_back_sigma reproduced")

print("== relative / Fisher size of the covariance back-action ==")
rel = sp.simplify(Sdot_back.subs(v, eps) / eps)
print("Sigma_dot^back / Sigma =", rel, "; limit eps->0:", sp.limit(rel, eps, 0))
# Fisher speed of variance change: ds/dt = |v_dot| / (sqrt(2) v)
print("Fisher speed of covariance back-action (eps->0):", sp.limit(sp.Abs(rel) / sp.sqrt(2), eps, 0))

print("== stationary rock state with coupling ==")
vstar = sp.solve(sp.Eq(sp.diff(F, v), 0), v)[0]
print("v* =", sp.simplify(vstar), "; precision 1/v* =", sp.simplify(1 / vstar))
ratio = sp.simplify(vstar / eps)
print("v*/eps =", ratio, "; limit eps->0:", sp.limit(ratio, eps, 0))
fisher_dist = sp.log(sp.limit(ratio, eps, 0)) / sp.sqrt(2)
print("Fisher-Rao distance between uncoupled (v=eps) and coupled rock variance, eps->0:", sp.simplify(fisher_dist))
for bval in [sp.Rational(1, 10), sp.Rational(1, 2), 1]:
    print(f"  beta={bval}: distance = {sp.N(fisher_dist.subs(beta, bval), 6)} nats^(1/2)")
mustar = sp.solve(sp.Eq(gmu, 0), mu)[0]
shift = sp.simplify(mustar - mup)
print("mean shift mu* - mu_p =", shift, "; Fisher length sqrt(shift^2/v*) ~", sp.simplify(sp.series(sp.sqrt(shift ** 2 / vstar), eps, 0, 2).removeO()))

print("== consensus stationary point and cocycle ==")
import numpy as np
rng = np.random.default_rng(0)
K = 3
phis = [rng.normal(size=(K, K)) * 0.3 for _ in range(3)]
from scipy.linalg import expm
E = [expm(p) for p in phis]
Om = lambda i, j: E[i] @ np.linalg.inv(E[j])
print("||Omega_hg Omega_gR - Omega_hR|| =", np.linalg.norm(Om(0, 1) @ Om(1, 2) - Om(0, 2)))
