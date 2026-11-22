"""(i) Symbolic check of the five C3(b) coefficients against my own derivation.
My derivation (Schwinger with v = 2 t sigma^2/(1+2 t sigma^2), phi_a := f_{K/2-1+a}):
  A = h g1/S, B = g1^2/S,
  E[A]  = lam*phi1,         E[A^2] = lam^2 (phi1-phi2) + (lam/2)(phi0-phi1),
  E[B]  = lam*phi2 + phi1/2,
  E[AB] = lam^2 (phi2-phi3) + (3 lam/2)(phi1-phi2),
  E[B^2]= lam^2 (phi3-phi4) + 3 lam (phi2-phi3) + (3/4)(phi1-phi2),
  c_R = E A^2, c_u = E(1-A)^2, c_par = E(1-B)^2, c_perp = E[B(1-B)]/(K-1), c_par_u = -E[(1-A)(1-B)],
  recurrence phi_{a+1} = (1 - (K/2-1+a) phi_a)/lam.
(ii) sigma_H^4 coefficient of C5(a) from the asymptotic series of f.
(iii) C4(2): sigma^2 E[(Hhat Hhat^T)^{-1}]_{11} at r_c=2,K=4,HH^T=s^2 I by my own route:
  condition on row 2; row 1 projected off row 2 is a noncentral chi^2_3, E[1/chi'^2_3(d)] = Dawson(sqrt(d/2))/sqrt(d/2)."""
import math, numpy as np, sympy as sp
from scipy import special

K, lam, phi0 = sp.symbols("K lam phi0", positive=True)
phi = [phi0]
for a in range(4):
    phi.append(sp.simplify((1 - (K / 2 - 1 + a) * phi[a]) / lam))
EA = lam * phi[1]; EA2 = lam**2 * (phi[1] - phi[2]) + lam / 2 * (phi[0] - phi[1])
EB = lam * phi[2] + phi[1] / 2
EAB = lam**2 * (phi[2] - phi[3]) + sp.Rational(3, 2) * lam * (phi[1] - phi[2])
EB2 = lam**2 * (phi[3] - phi[4]) + 3 * lam * (phi[2] - phi[3]) + sp.Rational(3, 4) * (phi[1] - phi[2])
mine = dict(cR=EA2, cu=1 - 2 * EA + EA2, cpar=1 - 2 * EB + EB2, cperp=(EB - EB2) / (K - 1), cpu=-(1 - EA - EB + EAB))
f0, f1, f2 = phi[0], phi[1], phi[2]
note = dict(cR=lam / 2 * ((K - 1) * f1 - (K - 3) * f0), cu=lam / 2 * ((K - 1) * f1 - (K - 3) * f0) - 2 * lam * f1 + 1,
            cpar=(K**2 - 1) / 4 * (f1 - f2), cperp=(K + 1) / 4 * f2 - (K - 1) / 4 * f1, cpu=(K - 1) * (K - 2) / 4 * (f1 - f0))
for k in mine:
    print(k, "mine - note =", sp.simplify(mine[k] - note[k]))

# (ii) asymptotic series f_alpha(lam) ~ sum_j (-1)^j (alpha-1)...(alpha-j) / lam^(j+1); e := 1/lam = 2 sigma^2/h^2
e = sp.symbols("e", positive=True)
al = K / 2 - 1
ser = sum((-1) ** j * sp.prod([al - i for i in range(1, j + 1)]) * e ** (j + 1) for j in range(6))
sub = {phi0: ser, lam: 1 / e}
Rc, u, Hm, h2, mp2, sg = sp.symbols("Rc u Hm h2 mp2 sigma", positive=True)
tot = (note["cR"] * Rc + note["cu"] * u**2 + note["cpar"] * Hm**2 + note["cperp"] * h2 * mp2 + 2 * note["cpu"] * Hm * u).subs(sub)
tot = sp.series(sp.expand(tot), e, 0, 3).removeO()
tot_s = sp.expand(tot.subs(e, 2 * sg**2 / h2))
c0_, c2_, c4_ = [sp.factor(tot_s.coeff(sg, n)) for n in (0, 2, 4)]
c4_note = ((K - 4) * (3 * K - 8) * Rc + (K - 4) ** 2 * u**2 + (K**2 - 1) * Hm**2 - (2 * K - 1) * h2 * mp2 - 2 * (K - 1) * (K - 2) * Hm * u) / h2**2
print("sigma^0:", c0_)
print("sigma^2:", sp.simplify(c2_))
print("sigma^4 mine - note:", sp.simplify(c4_ - c4_note))
# prop:lrn-understanding-expansion bracket at r_c=1, P=pI: ||mbar0||^2 + (5-2K) Rc/h2, mbar0 = m + H^T (u-Hm)/h2
brk = (mp2 + u**2 / h2) + (5 - 2 * K) * Rc / h2
print("sigma^2 mine - prop bracket:", sp.simplify(c2_ - brk))

# (iii) Shi formula
xs, ws = np.polynomial.hermite_e.hermegauss(120); ws = ws / math.sqrt(2 * math.pi)
xl, wl = np.polynomial.laguerre.laggauss(80)       # rho^2/2 ~ Exp(1) for chi_2
def half_f(delta_half):  # (1/2) f_{1/2}(delta/2) = Dawson(sqrt(x))/sqrt(x), x = delta/2
    x = np.maximum(delta_half, 1e-300)
    return np.where(delta_half > 1e-12, special.dawsn(np.sqrt(x)) / np.sqrt(x), 1.0)
for lamv in (0.3, 1.0, 1.7, 3.5):
    mu = math.sqrt(2 * lamv)
    a = xs[:, None, None]                 # component of row 2 along e1 (mean 0)
    b = mu + xs[None, :, None]            # component along e2 (mean mu)
    r2 = 2 * xl[None, None, :]            # squared norm of the other two components
    cos2 = a**2 / (a**2 + b**2 + r2)
    val = np.sum(ws[:, None, None] * ws[None, :, None] * wl[None, None, :] * half_f(lamv * (1 - cos2)))
    shi = special.shichi(lamv)[0]
    claim = (1 - math.exp(-2 * lamv)) / (4 * lamv) + (1 + lamv) / (2 * lamv) * math.exp(-lamv) * shi
    wrong = (1 - math.exp(-2 * lamv)) / (4 * lamv) + (1 + lamv) / (2 * lamv) * math.exp(-lamv) * math.sinh(lamv) / lamv
    print(f"lam={lamv}: my quadrature={val:.9f}  note Shi formula={claim:.9f}  diff={abs(val-claim):.1e}  planted sinh/lam diff={abs(val-wrong):.1e}")
