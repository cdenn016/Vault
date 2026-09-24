r"""L19: clock identities of PIFB2 (1841-1852) against Theory c07 thm:hist-fisher-clock-invariance.

Checks, for a natural-gradient flow xdot = -eta G^{-1} grad F on a Gaussian (mu, log sigma) chart:
  (1) (d tau/dt)^2 = eta (-dF/dt)                                   [PIFB2 eq:clock_dissipation]
  (2) dF/d tau = -||grad^G F||_G, d tau/dt = eta ||grad^G F||_G       [Theory eq:hist-vfe-clock-rate,
                                                                      eq:hist-vfe-dissipation-per-length, a = eta]
  (3) one discrete step: KL(new||old) = (eta/2)|Delta F| + O(eta^2)   [PIFB2 1850]
  (4) finite total duration for an analytic F with a limit point       [Theory prop:hist-analytic-finite-duration]
"""
import numpy as np
from scipy.integrate import solve_ivp

rng = np.random.default_rng(0)
K = 3
A = rng.normal(size=(K, K)); Lam0 = A @ A.T + K * np.eye(K)    # target precision
m0 = rng.normal(size=K)

def F(x):
    """F(mu, s) = KL(N(mu, diag e^{2s}) || N(m0, Lam0^{-1})), analytic in (mu, s)."""
    mu, s = x[:K], x[K:]
    Sig = np.diag(np.exp(2 * s))
    d = mu - m0
    return 0.5 * (np.trace(Lam0 @ Sig) + d @ Lam0 @ d - K - np.log(np.linalg.det(Lam0 @ Sig)))

def grad(x, h=1e-6):
    g = np.zeros_like(x)
    for k in range(len(x)):
        e = np.zeros_like(x); e[k] = h
        g[k] = (F(x + e) - F(x - e)) / (2 * h)
    return g

def G(x):
    """Fisher metric of N(mu, diag e^{2s}) in (mu, s): diag(e^{-2s}, 2)."""
    s = x[K:]
    return np.diag(np.concatenate([np.exp(-2 * s), 2 * np.ones(K)]))

eta = 0.7
x0 = np.concatenate([rng.normal(size=K), 0.3 * rng.normal(size=K)])
g = grad(x0); Gm = G(x0)
xdot = -eta * np.linalg.solve(Gm, g)
speed2 = xdot @ Gm @ xdot
dFdt = g @ xdot
print("(1) residual (dtau/dt)^2 - eta(-dF/dt):", speed2 - eta * (-dFdt))
natnorm = np.sqrt(g @ np.linalg.solve(Gm, g))
print("(2) residual dtau/dt - eta||grad||_G:", np.sqrt(speed2) - eta * natnorm,
      " dF/dtau + ||grad||_G:", dFdt / np.sqrt(speed2) + natnorm)

def KLdiag(x1, x0):
    mu1, s1, mu0, s0 = x1[:K], x1[K:], x0[:K], x0[K:]
    v1, v0 = np.exp(2 * s1), np.exp(2 * s0)
    return 0.5 * np.sum(v1 / v0 + (mu1 - mu0) ** 2 / v0 - 1 - np.log(v1 / v0))

for step in [1e-1, 1e-2, 1e-3]:
    x1 = x0 - step * np.linalg.solve(Gm, g)
    dF = F(x1) - F(x0)
    print(f"(3) step {step:g}: KL/(|dF| step/2) = {KLdiag(x1, x0) / (abs(dF) * step / 2):.6f}")

sol = solve_ivp(lambda t, x: np.concatenate([-np.linalg.solve(G(x), grad(x))]), [0, 60], x0,
                dense_output=True, rtol=1e-9, atol=1e-11, max_step=0.05)
ts = sol.t; xs = sol.y.T
sp = np.array([np.sqrt(v @ G(x) @ v) for x, v in zip(xs, [-np.linalg.solve(G(x), grad(x)) for x in xs])])
L = np.concatenate([[0], np.cumsum(0.5 * (sp[1:] + sp[:-1]) * np.diff(ts))])
for T in [10, 20, 40, 60]:
    print(f"(4) Fisher length on [0,{T}]: {np.interp(T, ts, L):.8f}")
print("(4) F at end:", F(xs[-1]))
