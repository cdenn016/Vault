"""L15: check the clock-dissipation identity (PIFB2.tex:1840, eq:clock_dissipation) that the
report compares with thermodynamic-length / Fisher-speed prior art, and the discrete bit-count
relation Delta I = (eta/2)|Delta F| to leading order for a unit-step natural-gradient update."""
import numpy as np
rng = np.random.default_rng(1)
n = 4
A = rng.normal(size=(n, n)); G = A @ A.T + n*np.eye(n)      # SPD sector metric
B = rng.normal(size=(n, n)); H = B @ B.T + np.eye(n)        # quadratic F = 1/2 x^T H x + b^T x
b = rng.normal(size=n); x = rng.normal(size=n)
F = lambda x: 0.5*x @ H @ x + b @ x
g = H @ x + b
for eta in [1e-2, 1e-3, 1e-4]:
    xdot = -eta*np.linalg.solve(G, g)
    speed2 = xdot @ G @ xdot
    dFdt = g @ xdot
    x1 = x + xdot                                              # one discrete update, unit step
    dI = 0.5*(x1 - x) @ G @ (x1 - x)                           # KL = 1/2 ds^2 (pure mean step, G = precision)
    dF = F(x1) - F(x)
    print(f"eta={eta:g}  (dtau/dt)^2 - eta(-dF/dt) = {speed2 - eta*(-dFdt):.3e}   dI/((eta/2)|dF|) - 1 = {dI/(0.5*eta*abs(dF)) - 1:.3e}")
# exactness of KL = 1/2 dmu^T Lambda dmu for a pure mean step
S = G.copy(); L = np.linalg.inv(S); dmu = rng.normal(size=n)*0.3
kl = 0.5*(np.trace(L@S) - n + dmu @ L @ dmu + np.log(np.linalg.det(S)/np.linalg.det(S)))
print("Gaussian KL mean step minus 1/2 dmu^T Lambda dmu:", kl - 0.5*dmu @ L @ dmu)
