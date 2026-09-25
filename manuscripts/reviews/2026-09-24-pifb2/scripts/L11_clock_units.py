"""L11: (a) clock-dissipation identity eq:clock_dissipation (PIFB2 1843-1847) and the discrete bit count;
(b) dimensional scaling of the Gaussian Fisher pullback (PIFB2 1885-1888): invariant under a change of
fiber units, scales as L^-2 under base-coordinate rescaling, so ds^2 = G dc dc is a pure number (nats)."""
import numpy as np
import sympy as sp

rng = np.random.default_rng(1)
n = 5
B = rng.normal(size=(n, n)); Gm = B @ B.T + n * np.eye(n)
g = rng.normal(size=n); eta = 0.37
xdot = -eta * np.linalg.solve(Gm, g)
lhs = xdot @ Gm @ xdot
rhs = eta * (-(g @ xdot))
print("(dtau/dt)^2 - eta(-dF/dt) =", lhs - rhs)
# discrete step of size eta on a quadratic F = 1/2 x^T H x: Delta I = 1/2 ds^2 vs (eta/2)|Delta F|
H = rng.normal(size=(n, n)); H = H @ H.T + np.eye(n); x0 = rng.normal(size=n)
for h in [1e-2, 1e-3]:
    dx = -h * np.linalg.solve(Gm, H @ x0)
    dI = 0.5 * dx @ Gm @ dx
    dF = 0.5 * (x0 + dx) @ H @ (x0 + dx) - 0.5 * x0 @ H @ x0
    print(f"step h={h}: Delta I / ((h/2)|Delta F|) = {dI / (h / 2 * abs(dF)):.6f}  (-> 1 as h -> 0)")

c, lam, L, s = sp.symbols('c lambda L sigma', positive=True)
m = sp.Function('m')(c)
G = sp.diff(m, c) ** 2 / s ** 2  # 1D base, 1D fiber, constant variance
G_fiber_units = (sp.diff(lam * m, c) ** 2 / (lam * s) ** 2)
print("fiber-unit change mu->lam mu, sigma->lam sigma: G ratio =", sp.simplify(G_fiber_units / G))
cp = sp.symbols('cp', positive=True)  # c = L * cp
G_rescaled = sp.diff(m.subs(c, L * cp), cp) ** 2 / s ** 2
print("base rescaling c = L c': G'/G =", sp.simplify(G_rescaled / G.subs(c, L * cp)), "(so G dc^2 invariant, dimensionless)")
