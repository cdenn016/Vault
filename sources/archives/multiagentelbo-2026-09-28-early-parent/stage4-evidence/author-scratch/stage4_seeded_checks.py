r"""Scratch checks for the stage-4 seeded hidden-information derivation.

Exact (Fraction) linear algebra for the four-cycle carrier, symbolic checks of the
Gaussian identities, and float evaluation of the explicit constants.  Coordinates are
x = (kbar_0..3, mbar_0..3, omega_0..3), as in stage3-projection-check.py.
"""
from fractions import Fraction as F
import itertools
import math

import numpy as np
import sympy as sp


def residual(edge: int, channel: int) -> list[F]:
    a = [F(0)] * 12
    a[channel + edge] = F(-1)
    a[channel + (edge + 1) % 4] = F(1)
    a[8 + edge] = F(-1)
    return a


def dot(x, y):
    return sum((a * b for a, b in zip(x, y)), F(0))


x_circ = [F(0)] * 8 + [F(1)] * 4
out = {}

# (1) hidden components of +-x_circ vanish for both matchings; all residuals of x_circ are -1
for edges in [(0, 2), (1, 3)]:
    ab = [residual(e, 0) for e in edges]
    am = [residual(e, 4) for e in edges]
    plus = [[b + m for b, m in zip(ab[i], am[i])] for i in range(2)]      # 2 sqrt2 n^+
    minus = [[b - m for b, m in zip(ab[i], am[i])] for i in range(2)]     # 2 n^-
    Zcols = [[p - q for p, q in zip(plus[0], plus[1])], minus[0], minus[1]]
    for sgn in (1, -1):
        xs = [sgn * v for v in x_circ]
        assert all(dot(z, xs) == 0 for z in Zcols), edges
    for g in range(4):
        assert dot(residual(g, 0), x_circ) == -1 and dot(residual(g, 4), x_circ) == -1
        assert dot(residual(g, 0), residual(g, 0)) == 3
out["hidden_component_of_pm_xcirc"] = 0

# (2) operator norms: max eigenvalue of H_S over all 16 assignments, and of R_ev
Dm = np.zeros((4, 12))
for i in range(4):
    Dm[i, i] = 1.0
    Dm[i, 4 + i] = -1.0
R_ev = 2.0 * Dm.T @ Dm
out["norm_R_ev"] = float(np.linalg.eigvalsh(R_ev).max())
lam_max = 0.0
for S in itertools.product(*[((i - 1) % 4, (i + 1) % 4) for i in range(4)]):
    H = np.zeros((12, 12))
    for i, j in enumerate(S):
        e = i if j == (i + 1) % 4 else j   # edge e_i joins i and i+1
        for ch in (0, 4):
            a = np.array([float(v) for v in residual(e, ch)])
            H += np.outer(a, a)
    lam_max = max(lam_max, float(np.linalg.eigvalsh(H).max()))
out["max_eig_H_S_over_16_assignments"] = lam_max

# (3) held path residuals from x_circ under K_M (M = S^(0)), T small, compare to closed form
T = 1e-3
H0 = np.zeros((12, 12))
for i, j in enumerate((1, 0, 3, 2)):
    e = i if j == (i + 1) % 4 else j
    for ch in (0, 4):
        a = np.array([float(v) for v in residual(e, ch)])
        H0 += np.outer(a, a)
K = H0 + T * (np.eye(12) + R_ev)
w, V = np.linalg.eigh(K)
xc = np.array([float(v) for v in x_circ])
errs = []
for t in (0.25, 1.0, 3.0):
    xt = V @ np.diag(np.exp(-w * t)) @ V.T @ xc
    rint = np.array([float(v) for v in residual(0, 0)]) @ xt
    rext = np.array([float(v) for v in residual(1, 0)]) @ xt
    errs.append(abs(rint + math.exp(-(8 + T) * t)))
    errs.append(abs(rext - math.exp(-T * t) * (-1.5 + math.exp(-8 * t) / 2)))
out["held_path_formula_max_error"] = max(errs)

# (4) symbolic Gaussian identities
a_, lam, Tsym, z0, s = sp.symbols("a lambda T z0 s", positive=True)
# per-coordinate KL(N(e^{-lam t} z0, (T/lam)(1-a)) || N(0,T/lam)), a=e^{-2 lam t}
v = (Tsym / lam) * (1 - a_)
kl = sp.Rational(1, 2) * (v / (Tsym / lam) - 1 - sp.log(v / (Tsym / lam)) + a_ * z0**2 / (Tsym / lam))
target = sp.Rational(1, 2) * (-a_ - sp.log(1 - a_) + lam * a_ * z0**2 / Tsym)
out["per_coordinate_KL_identity"] = sp.simplify(kl - target) == 0
# tilt normalizer: two discrepancy coordinates change precision (4+T)/T -> (4+5T)/T
Ztilt = sp.sqrt((4 + Tsym) / (4 + 5 * Tsym)) ** 2
out["Z_tilt"] = str(sp.simplify(Ztilt))
# -a-log(1-a) <= a^2/(2(1-a)) on (0,1)
agrid = np.linspace(1e-6, 0.999, 20000)
out["series_bound_ok"] = bool(np.all(-agrid - np.log1p(-agrid) <= agrid**2 / (2 * (1 - agrid)) + 1e-15))
# DV constant: E_nu exp(s*lam z^2/(2T)) = (1-s)^{-1/2}
zz = sp.symbols("zz", real=True)
mgf = sp.integrate(sp.exp(s * lam * zz**2 / (2 * Tsym)) * sp.sqrt(lam / (2 * sp.pi * Tsym))
                   * sp.exp(-lam * zz**2 / (2 * Tsym)), (zz, -sp.oo, sp.oo), conds="none")
out["DV_mgf"] = str(sp.simplify(mgf))

# (5) constants
out["chebyshev_constant"] = 384 * 192          # 384 T t / delta^2 with delta^2 = eps^4/192, T = eps^8
out["subgaussian_constant"] = 2 * 96 * 192     # a^2 = delta^2/(96 T) = eps^{-4}/18432; a^2/(2t)
eps = 0.01
Tv = eps**8
t_eps = 2 * math.log(1 / eps)
t_star = t_eps + 1
rho, delta = 0.01, eps**2 / (8 * math.sqrt(3))
out["eps_t_star_at_0.01"] = eps * t_star
out["row_ratio_2e^{eps t*}-1"] = 2 * math.exp(eps * t_star) - 1
out["selected_margin_e^-2+sqrt3(rho+delta)"] = math.exp(-2) + math.sqrt(3) * (rho + delta)
out["exterior_Ttheta_threshold"] = -math.log((1.3 + math.sqrt(3) * (rho + delta)) / (1.5 - math.exp(-2) / 2))
# selected residual at t >= (1/2)log(1/eps): e^{-8t}+sqrt3 rho e^{-4t}+sqrt3 delta, as a multiple of eps^2
t1 = 0.5 * math.log(1 / eps)
out["selected_at_t1_over_eps2"] = (math.exp(-8 * t1) + math.sqrt(3) * rho * math.exp(-4 * t1) + math.sqrt(3) * delta) / eps**2


def hb(p):
    return 0.0 if p <= 0 else -p * math.log(p) - (1 - p) * math.log1p(-p)


def eta(theta):
    return 9 * rho**2 * math.exp(-8 * theta) / (2 * Tv) + 3 * math.exp(-16 * theta) / (4 * (1 - math.exp(-8 * theta)))


for theta, name in ((t_eps, "t_eps"), (t_star, "t_star")):
    dep = 4 * (2 * math.exp(eps * theta) - 1) * theta * math.exp(-1 / Tv)
    p_ch = 73728 * eps**4 * theta + dep
    log_p_sg = math.log(24) - eps**-4 / (36864 * theta)
    p_sg = math.exp(log_p_sg) + dep
    out[f"eta({name})"] = eta(theta)
    out[f"p_cheb({name})"] = p_ch
    out[f"kappa_cheb({name})"] = (eta(theta) + hb(p_ch)) / (1 - p_ch)
    out[f"log_p_subgauss({name})"] = log_p_sg
    # h_b(p) <= p log(e/p) for tiny p, computed in logs
    hb_sg = math.exp(log_p_sg) * (1 - log_p_sg) if log_p_sg > -700 else 0.0
    out[f"kappa_subgauss({name})"] = (eta(theta) + hb_sg) / (1 - p_sg)
    out[f"eta({name})/T"] = eta(theta) / Tv

# (6) uniform 12-ball: |z_perp|^2/rho^2 ~ Beta(1,6); tail at 1/4 and mean
rng = np.random.default_rng(0)
n = 400000
g = rng.standard_normal((n, 12))
u = rng.random(n) ** (1 / 12)
pts = g / np.linalg.norm(g, axis=1, keepdims=True) * u[:, None]
r2 = (pts[:, :2] ** 2).sum(axis=1)
out["MC_P(|z_perp|^2>=1/4)"] = float((r2 >= 0.25).mean())
out["exact_(3/4)^6"] = 0.75**6
out["MC_E|z_perp|^2"] = float(r2.mean())
out["exact_1/7"] = 1 / 7

for k, val in out.items():
    print(f"{k}: {val}")

# (7) held path: all selected and exterior residuals, both channels, both matchings
maxerr = 0.0
for S, sel in (((1, 0, 3, 2), (0, 2)), ((3, 2, 1, 0), (1, 3))):
    Hm = np.zeros((12, 12))
    for i, j in enumerate(S):
        e = i if j == (i + 1) % 4 else j
        for ch in (0, 4):
            a = np.array([float(v) for v in residual(e, ch)])
            Hm += np.outer(a, a)
    Km = Hm + T * (np.eye(12) + R_ev)
    wm, Vm = np.linalg.eigh(Km)
    for t in (0.1, 0.25, 2.0):
        for sgn in (1.0, -1.0):
            xt = Vm @ np.diag(np.exp(-wm * t)) @ Vm.T @ (sgn * xc)
            for g in range(4):
                for ch in (0, 4):
                    r = np.array([float(v) for v in residual(g, ch)]) @ xt
                    ref = -math.exp(-(8 + T) * t) if g in sel else math.exp(-T * t) * (-1.5 + math.exp(-8 * t) / 2)
                    maxerr = max(maxerr, abs(r - sgn * ref))
print("held_path_all_residuals_max_error:", maxerr)
print("exterior_margin_at_Ttheta=1/12:", math.exp(-1 / 12) * (1.5 - math.exp(-2) / 2) - math.sqrt(3) * (rho + delta))
print("exterior_margin_on_[0,1/4]:", (1.5 - 0.5) - math.sqrt(3) * (rho + delta))
print("entrance_KL_lower:", (1 - math.sqrt(3) * rho) ** 2 / 2)
print("ratio_bound_eps_tstar_via_row_formula:", 0.5511 / 0.4489)
print("x_circ+p/4 norm^2 check:")
pvec = np.zeros(12)
for g in (0, 2):
    pvec += np.array([float(v) for v in residual(g, 0)]) + np.array([float(v) for v in residual(g, 4)])
print(float(np.dot(xc + pvec / 4, xc + pvec / 4)))
