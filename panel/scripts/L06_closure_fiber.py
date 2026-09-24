r"""L06 check of thm:rg_exact_closure (PIFB2.tex ~3820-3850) and Assumption (A6).

(1) Gaussian fiber integral: -T log \int exp[-(Q + 1/2 xi^T A xi)/T] d^r xi
    = Q + (T/2) log det A - (r T/2) log(2 pi T).
(2) Non-closure under iteration: V(Y) = (T/2) log det A(Y) is not quadratic, so the
    next-scale fiber density is not Gaussian and (A6) generically fails at s+1.
(3) Fiber of the manuscript's M-projection barycenter map (dispersion retained) is bounded:
    K_q = 1, |I| = 2, w = 1/2: fixing (mu_I, Sigma_I) forces xi^2 < Sigma_I.
(4) Any smooth positive fiber density on an interval is mapped to an exact Gaussian by the
    monotone (Knothe-Rosenblatt) chart Phi^{-1}(G(xi)); hence (A6) read with arbitrary charts
    is satisfiable by every pushforward, with Q + (T/2)log det A absorbing -T log(fiber mass).
"""
import numpy as np
import sympy as sp
from scipy import integrate, stats

# (1)
T, Q = sp.symbols("T Q", positive=True)
x1, x2 = sp.symbols("x1 x2", real=True)
a, b, c = sp.symbols("a b c", positive=True)
A = sp.Matrix([[a, c], [c, b]])
# integrate 2D Gaussian with a*b > c^2 assumed via substitution check numerically
vals = {a: 2.3, b: 1.7, c: 0.4, T: 0.37, Q: 1.1}
f = lambda u, v: np.exp(-(1.1 + 0.5 * (2.3 * u * u + 2 * 0.4 * u * v + 1.7 * v * v)) / 0.37)
I2, _ = integrate.dblquad(f, -12, 12, -12, 12)
lhs = -0.37 * np.log(I2)
rhs = 1.1 + 0.37 / 2 * np.log(2.3 * 1.7 - 0.16) - 2 * 0.37 / 2 * np.log(2 * np.pi * 0.37)
print("(1) r=2 Gaussian fiber formula: lhs=%.15f rhs=%.15f resid=%.2e" % (lhs, rhs, abs(lhs - rhs)))

# (2)
y = sp.symbols("y", real=True)
a0, a1 = sp.symbols("a0 a1", positive=True)
V = T / 2 * sp.log(a0 + a1 * y**2)
d4 = sp.simplify(sp.diff(V, y, 4))
print("(2) d^4 V/dy^4 =", d4, " (nonzero => V not quadratic => next-scale fiber not Gaussian)")
# explicit next-stage: two parents y1,y2 with F = 1/2(y1^2+y2^2)+V(y1)+V(y2); fiber over Y'=(y1+y2)/2
Tn, a0n, a1n = 0.5, 1.0, 3.0
def Fs1(yv):
    return 0.5 * yv**2 + Tn / 2 * np.log(a0n + a1n * yv**2)
def Fnext(Yp):
    g = lambda eta: np.exp(-(Fs1(Yp + eta) + Fs1(Yp - eta)) / Tn)
    val, _ = integrate.quad(g, -30, 30, limit=400)
    return -Tn * np.log(val)
Ys = np.linspace(-2, 2, 41)
Fn = np.array([Fnext(v) for v in Ys])
coef = np.polyfit(Ys, Fn, 2)
res = Fn - np.polyval(coef, Ys)
print("(2) next-scale F vs best quadratic: max |residual| = %.4e (A6-type closure at s+2 fails)" % np.max(np.abs(res)))

# (3)
rng = np.random.default_rng(0)
muI, SigI = 0.3, 1.0
maxxi = 0.0
for _ in range(200000):
    xi = rng.uniform(-3, 3)
    s1 = rng.uniform(0, 3)
    s2 = 2 * (SigI - xi**2) - s1  # enforce 1/2(s1+s2) + xi^2 = Sigma_I
    if s1 > 0 and s2 > 0:
        maxxi = max(maxxi, abs(xi))
print("(3) barycenter fiber over (mu_I, Sigma_I=1): sup|xi| found = %.4f <= sqrt(Sigma_I)=1 (fiber bounded, not R^r)" % maxxi)

# (4)
aint = 1.0
g = lambda z: (1 + 0.8 * np.sin(3 * z)) * np.exp(-z**4)  # arbitrary positive density on (-1,1)
mass, _ = integrate.quad(g, -aint, aint)
Gcdf = lambda z: integrate.quad(g, -aint, z)[0] / mass
zs = np.linspace(-0.999, 0.999, 2001)
u = np.array([stats.norm.ppf(np.clip(Gcdf(z), 1e-15, 1 - 1e-15)) for z in zs[::100]])
# pushforward check: P(u <= u0) equals Phi(u0) by construction; check mass identity for (A6):
Tfix = 0.7
Fnext_true = -Tfix * np.log(mass)
# (A6) representation with A=1, Q = -T log mass + (r T/2)log(2 pi T)... chosen to match
Q_rep = Fnext_true + Tfix / 2 * np.log(2 * np.pi * Tfix) - Tfix / 2 * np.log(1.0)
print("(4) chart makes fiber density exactly Gaussian; -T log mass = %.12f ; Q_rep + (T/2)log det A - (T/2)log(2piT) = %.12f"
      % (Fnext_true, Q_rep + 0 - Tfix / 2 * np.log(2 * np.pi * Tfix)))
print("(4) monotone chart values sample:", np.round(u[:5], 4), "... strictly increasing:", bool(np.all(np.diff(u) > 0)))
