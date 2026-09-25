r"""L12 (Wheeler lens) checks for PIFB2.tex, 2026-09-24.

(1) KL(N(mu+d,S)||N(mu,S)) = 1/2 d^T S^{-1} d exactly (eq:kl_arclength), symbolic 2x2.
(2) Refinement non-additivity of the KL "bit count" versus additivity of Fisher arc length.
(3) Clock-dissipation identity (eq:clock_dissipation) and Delta I ~ (eta/2)|Delta F| per step.
(4) Elementary yes-no registration: E_o KL(q(.|o) || q) = I(X;O) <= ln 2 (one bit), while a
    single surprising outcome can move the belief by more than one bit.
(5) Regime I cocycle Omega_ij Omega_jk Omega_ki = I (coboundary of a coboundary) versus
    independent links with nontrivial holonomy.
"""
import numpy as np
import sympy as sp

rng = np.random.default_rng(0)

# (1) symbolic
d1, d2, a, b, c = sp.symbols('d1 d2 a b c', real=True)
S = sp.Matrix([[a, b], [b, c]])
d = sp.Matrix([d1, d2])
Si = S.inv()
# KL(N(m1,S1)||N(m0,S0)) = 1/2[tr(S0^-1 S1) + (m0-m1)^T S0^-1 (m0-m1) - k + ln det S0/det S1]
kl = sp.Rational(1, 2) * ((Si * S).trace() + (d.T * Si * d)[0] - 2 + sp.log(S.det() / S.det()))
res1 = sp.simplify(kl - sp.Rational(1, 2) * (d.T * Si * d)[0])
print("(1) KL - 1/2 d^T S^-1 d =", res1)

# (2) refinement
s = 1.0
for n in [1, 2, 10, 100]:
    kl_sum = n * 0.5 * (s / n) ** 2
    arc_sum = n * (s / n)
    print(f"(2) n={n:4d} substeps: summed KL bits = {kl_sum/np.log(2):.6f}, summed arc length = {arc_sum:.6f}")

# (3) clock-dissipation on a Gaussian mean sector: F(mu) = 1/2 (mu-m)^T H (mu-m), metric G = Lambda
K = 3
A = rng.normal(size=(K, K)); H = A @ A.T + K * np.eye(K)
B = rng.normal(size=(K, K)); Lam = B @ B.T + K * np.eye(K)
m = rng.normal(size=K); mu = rng.normal(size=K)
g = H @ (mu - m)
xdot = -np.linalg.solve(Lam, g)  # eta = 1 continuous-time
speed2 = xdot @ Lam @ xdot
dFdt = g @ xdot
print("(3a) (dtau/dt)^2 - eta(-dF/dt) =", speed2 - (-dFdt))
for eta in [1e-1, 1e-2, 1e-3]:
    dmu = -eta * np.linalg.solve(Lam, g)
    klstep = 0.5 * dmu @ Lam @ dmu
    F0 = 0.5 * (mu - m) @ H @ (mu - m); mu1 = mu + dmu; F1 = 0.5 * (mu1 - m) @ H @ (mu1 - m)
    print(f"(3b) eta={eta:g}: KL step / ((eta/2)|dF|) = {klstep/((eta/2)*abs(F1-F0)):.6f}")

# (4) binary registration with Gaussian prior and logistic likelihood
x = np.linspace(-12, 12, 20001); dx = x[1] - x[0]
prior = np.exp(-0.5 * x**2); prior /= prior.sum() * dx
def run(slope, bias):
    p1 = 1 / (1 + np.exp(-(slope * x + bias)))
    P1 = (prior * p1).sum() * dx; P0 = 1 - P1
    post1 = prior * p1 / P1; post0 = prior * (1 - p1) / P0
    def KL(p, q):
        mask = p > 1e-300
        return (p[mask] * np.log(p[mask] / q[mask])).sum() * dx
    k1, k0 = KL(post1, prior), KL(post0, prior)
    return P1, k1, k0, P1 * k1 + P0 * k0
for slope, bias in [(1.0, 0.0), (50.0, 0.0), (50.0, -3.0 * 50)]:
    P1, k1, k0, EK = run(slope, bias)
    print(f"(4) slope={slope:5.1f} bias={bias:7.1f}: P(o=1)={P1:.4g}, KL|o=1={k1/np.log(2):.4f} bits, "
          f"KL|o=0={k0/np.log(2):.4f} bits, E_o KL = I(X;O) = {EK/np.log(2):.4f} bits (<= 1)")

# (5) cocycle
def expm(X):
    w, V = np.linalg.eig(X); return (V @ np.diag(np.exp(w)) @ np.linalg.inv(V)).real
Kq = 4
phis = [0.4 * rng.normal(size=(Kq, Kq)) for _ in range(3)]
U = [expm(p) for p in phis]
Om = lambda i, j: U[i] @ np.linalg.inv(U[j])
hol = Om(0, 1) @ Om(1, 2) @ Om(2, 0)
print("(5a) Regime I holonomy ||Om01 Om12 Om20 - I|| =", np.linalg.norm(hol - np.eye(Kq)))
L = [expm(0.4 * rng.normal(size=(Kq, Kq))) for _ in range(3)]
print("(5b) independent links ||L01 L12 L20 - I|| =", np.linalg.norm(L[0] @ L[1] @ L[2] - np.eye(Kq)))

# (6) Wootters (1981) link cited by Wheeler 1990: Fisher metric on the simplex under p_k = y_k^2
#     equals 4x the round metric on the unit sphere, so Fisher-Rao distance = 2 arccos(sum sqrt(p q)).
y = sp.symbols('y1:4', positive=True); dy = sp.symbols('dy1:4', real=True)
p = [yi**2 for yi in y]; dp = [2 * yi * dyi for yi, dyi in zip(y, dy)]
gF = sum(dpi**2 / pi for dpi, pi in zip(dp, p))
print("(6a) Fisher(dp,dp) - 4 sum dy^2 =", sp.simplify(gF - 4 * sum(d_**2 for d_ in dy)))
# numerical: integrate Fisher line element along the great-circle path between two categorical laws
P = np.array([0.7, 0.2, 0.1]); Q = np.array([0.1, 0.3, 0.6])
yP, yQ = np.sqrt(P), np.sqrt(Q); th = np.arccos(yP @ yQ)
ts = np.linspace(0, 1, 20001)
path = np.array([(np.sin((1 - t) * th) * yP + np.sin(t * th) * yQ) / np.sin(th) for t in ts]) ** 2
dpath = np.diff(path, axis=0); mid = 0.5 * (path[1:] + path[:-1])
length = np.sum(np.sqrt(np.sum(dpath**2 / mid, axis=1)))
print(f"(6b) Fisher length along path = {length:.8f}, 2 arccos(sum sqrt(pq)) = {2*th:.8f}")
