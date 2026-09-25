r"""L06 checks: Laplace anharmonic coefficients (thm:rg_residual_explicit), Hermite thresholds,
detector-retention theorem (thm:rg_detector_retention), conductance pooling (eq:rg_inter_cluster).

(1) -T log(Z/Z0) for F = m x^2/2 + t3 x^3/6 + t4 x^4/24 equals T^2 (t4/(8 m^2) - 5 t3^2/(24 m^3)) + O(T^3).
(2) |He_4| exceeds He_4(0)=3 beyond sqrt(3-sqrt3); |He_6| exceeds 15 beyond ~0.973.
(3) Random stress of the retention theorem's implication.
(4) Identical-children identity of the row-convex column-summed pooling with and without the
    self-cluster term L = I.
"""
import numpy as np
import sympy as sp
from scipy import integrate, optimize

# (1) symbolic Wick expansion
x, T, m, t3, t4, eps = sp.symbols("x T m t3 t4 epsilon", positive=True)
# expand exp(-(t3 x^3/6 + t4 x^4/24)/T) in eps-scaled couplings to 2nd order in t3, 1st in t4
pert = -(eps * t3 * x**3 / 6 + eps**2 * t4 * x**4 / 24) / T
series = sp.series(sp.exp(pert), eps, 0, 3).removeO()
def gauss_moment(k):
    # <x^k> under exp(-m x^2/(2T)), normalized
    if k % 2:
        return 0
    return sp.factorial2(k - 1) * (T / m) ** (k // 2)
poly = sp.Poly(sp.expand(series), x)
avg = sum(coef * gauss_moment(mon[0]) for mon, coef in zip(poly.monoms(), poly.coeffs()))
dF = sp.series(-T * sp.log(avg), eps, 0, 3).removeO().subs(eps, 1)
target = T**2 * (t4 / (8 * m**2) - sp.Rational(5, 24) * t3**2 / m**3)
print("(1) -T log(Z/Z0) - T^2(t4/(8m^2) - 5 t3^2/(24 m^3)) =", sp.simplify(dF - target))
# numerical sanity
mm, a3, a4, TT = 1.3, 0.4, 0.9, 1e-3
Zf = integrate.quad(lambda z: np.exp(-(mm*z*z/2 + a3*z**3/6 + a4*z**4/24)/TT), -2, 2, points=[0], limit=400)[0]
Z0 = np.sqrt(2*np.pi*TT/mm)
num = -TT*np.log(Zf/Z0)/TT**2
print("(1) numeric T=1e-3: %.6f vs predicted %.6f" % (num, a4/(8*mm**2) - 5*a3**2/(24*mm**3)))

# (2)
He4 = lambda z: z**4 - 6*z**2 + 3
He6 = lambda z: z**6 - 15*z**4 + 45*z**2 - 15
r4 = optimize.brentq(lambda z: He4(z) + 3, 0.5, 1.5)
r6 = optimize.brentq(lambda z: He6(z) - 15, 0.5, 1.5)
print("(2) R4 = %.6f (sqrt(3-sqrt3) = %.6f); R6 = %.6f" % (r4, np.sqrt(3-np.sqrt(3)), r6))

# (3)
rng = np.random.default_rng(3)
bad = 0; tested = 0
for _ in range(200000):
    Lq, Lp, tq, tp = rng.uniform(0, 5, 4)
    Gmin = rng.uniform(0.01, 0.99)
    d0, CI = rng.uniform(0, 1, 2)
    A = max(Lq*tq, Lp*tp)*np.log(1/Gmin) + d0 + CI + rng.uniform(1e-9, 1)
    Vq, Vp = rng.exponential(1, 2)
    P = rng.uniform(0, 1)
    Gam = P*np.exp(-Vq/tq)*np.exp(-Vp/tp)
    if Gam <= Gmin:
        continue
    tested += 1
    Fmicro = rng.normal()
    Fpar = Fmicro - A + Lq*Vq + Lp*Vp + d0 - rng.uniform(0, 1)  # satisfies hypothesis
    Delta = (Fmicro) - (Fpar + CI)  # C_micro set to 0, C_parent = C_I
    if not Delta > 0:
        bad += 1
print("(3) retention theorem: %d violations among %d detector-accepted draws" % (bad, tested))

# (4) identical children: kappa_ij independent of i in I
tau = 0.7
nI, nJ, nK = 3, 4, 2
kap_row = rng.uniform(0.1, 2, size=nI + nJ + nK)  # child's conductances to all agents (own cluster first)
w = rng.dirichlet(np.ones(nI))
F_child = -tau*np.log(kap_row.sum())
kIJ = {"I": sum(w)*kap_row[:nI].sum(), "J": sum(w)*kap_row[nI:nI+nJ].sum(), "K": sum(w)*kap_row[nI+nJ:].sum()}
F_with_self = -tau*np.log(kIJ["I"] + kIJ["J"] + kIJ["K"])
F_no_self = -tau*np.log(kIJ["J"] + kIJ["K"])
print("(4) F_child = %.6f; F_parent incl. self-cluster L=I: %.6f; excluding L=I: %.6f"
      % (F_child, F_with_self, F_no_self))
