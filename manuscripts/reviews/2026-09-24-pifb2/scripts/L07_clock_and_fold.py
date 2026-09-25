r"""L07: information clock (PIFB2.tex 1828-1866) and fast-manifold folds (929-1005).

 (1) clock-dissipation identity (dtau/dt)^2 = eta(-dF/dt) along an autonomous natural-gradient flow;
     total Fisher arc length tau(infinity) is finite (clock stops);
 (2) with time-dependent observations o(t) the identity fails (F can rise while tau ticks);
 (3) discrete step: Delta I = KL(new||old) vs (eta/2)|Delta F|;
 (4) consensus relaxation rate of disagreement: 2 eta lambda_2(L_sym) (Omega = I, equal precision);
 (5) fold of the fast critical manifold under softmax attention: reduced free energy
     F_red(mu; m) = alpha/2 (mu - m)^2 - tau log sum_j exp(-(mu - x_j)^2 / (2 tau))
     with slow prior mean m; count equilibria and locate F_red''=0 (loss of normal hyperbolicity).
"""
import numpy as np
from scipy.integrate import solve_ivp

eta = 1.0
# ---- (1) single Gaussian agent, mean + covariance (1D) with prior and observation
mp, sp2, o, so2 = 0.0, 1.0, 2.0, 0.5
def F(mu, s2, o=o):
    kl = 0.5 * (s2 / sp2 + (mu - mp) ** 2 / sp2 - 1 + np.log(sp2 / s2))
    return kl + 0.5 * ((o - mu) ** 2 + s2) / so2
def grad(mu, s2, o=o):
    return (mu - mp) / sp2 + (mu - o) / so2, 0.5 * (1 / sp2 - 1 / s2) + 0.5 / so2
def rhs(t, y, odep=None):
    mu, s2 = y
    oo = o if odep is None else odep(t)
    gm, gs = grad(mu, s2, oo)
    return [-eta * s2 * gm, -eta * 2 * s2 ** 2 * gs]   # Fisher: g_mm = 1/s2, g_ss = 1/(2 s2^2)
sol = solve_ivp(rhs, [0, 40], [-3.0, 4.0], dense_output=True, rtol=1e-11, atol=1e-13)
ts = np.linspace(0, 40, 40001); Y = sol.sol(ts)
dmu, ds2 = np.array([rhs(t, y) for t, y in zip(ts, Y.T)]).T
speed2 = dmu ** 2 / Y[1] + ds2 ** 2 / (2 * Y[1] ** 2)
gg = np.array([grad(m_, s_) for m_, s_ in Y.T]).T
dF = gg[0] * dmu + gg[1] * ds2   # exact chain rule dF/dt = grad F . xdot
print("(1) max |speed^2 - eta(-dF/dt)| (interior) =", np.abs(speed2 - eta * (-dF))[5:-5].max())
tau = np.concatenate([[0], np.cumsum(0.5 * (np.sqrt(speed2[1:]) + np.sqrt(speed2[:-1])) * np.diff(ts))])
print("    tau(10), tau(20), tau(40) =", tau[10000], tau[20000], tau[-1], " (saturates: finite total clock time)")
# ---- (2) driven observations
odep = lambda t: 2.0 + np.sin(t)
sol2 = solve_ivp(lambda t, y: rhs(t, y, odep), [0, 40], [-3.0, 4.0], dense_output=True, rtol=1e-11, atol=1e-13)
Y2 = sol2.sol(ts)
d2 = np.array([rhs(t, y, odep) for t, y in zip(ts, Y2.T)]).T
g2 = np.array([grad(m_, s_, odep(t)) for t, (m_, s_) in zip(ts, Y2.T)]).T
dodt = np.cos(ts)
dF2 = g2[0] * d2[0] + g2[1] * d2[1] + ((odep(ts) - Y2[0]) / so2) * dodt  # total dF/dt incl. explicit dF/do * do/dt
sp2d = d2[0] ** 2 / Y2[1] + d2[1] ** 2 / (2 * Y2[1] ** 2)
print("(2) driven: fraction of time with dF/dt > 0 while speed > 0:", np.mean((dF2 > 1e-9) & (sp2d > 1e-9)),
      " max |speed^2 - eta(-dF/dt)| =", np.abs(sp2d - eta * (-dF2))[5:-5].max())
# ---- (3) discrete step (mean only, fixed variance) : x+ = x - h G^{-1} grad
for h in [0.1, 0.01]:
    mu, s2 = -3.0, 0.4
    gm, _ = grad(mu, s2)
    mu1 = mu - h * s2 * gm
    KL = 0.5 * (mu1 - mu) ** 2 / s2
    dFv = F(mu1, s2) - F(mu, s2)
    print(f"(3) step h={h}: KL(new||old) = {KL:.6g}, (h/2)|dF| = {h/2*abs(dFv):.6g}, ratio = {KL/(h/2*abs(dFv)):.4f}")
# ---- (4) consensus relaxation rate
rng = np.random.default_rng(1); N = 5
beta = rng.random((N, N)); np.fill_diagonal(beta, 0); beta /= beta.sum(1, keepdims=True)
Ls = 0.5 * (np.diag((beta + beta.T).sum(1)) - (beta + beta.T))
# F_c = sum_ij beta_ij (1/2) lam |mu_i - mu_j|^2 = mu^T (Ls lam) mu ; nat grad (Sigma = 1/lam): mu' = -eta/lam * 2 lam Ls mu
Hc = np.zeros((N, N))
for i in range(N):
    for j in range(N):
        e = np.zeros(N); e[i] += 1; e[j] -= 1
        Hc += beta[i, j] * np.outer(e, e)
print("(4) Hessian of coupling == 2 Ls:", np.allclose(Hc, 2 * Ls), "; disagreement amplitude rate = eta*lambda_2(2Ls) =",
      np.sort(np.linalg.eigvalsh(2 * Ls))[1], "= 2 eta lambda_2(Ls) =", 2 * np.sort(np.linalg.eigvalsh(Ls))[1])
# ---- (5) fold of fast manifold
alpha, tt, xs = 0.2, 0.05, np.array([-1.0, 1.0])
def dFr(mu, m):
    mu = np.asarray(mu, dtype=float)[..., None]
    w = np.exp(-(mu - xs) ** 2 / (2 * tt)); w /= w.sum(-1, keepdims=True)
    return alpha * (mu[..., 0] - m) + np.sum(w * (mu - xs), -1)
def d2Fr(mu, m, h=1e-6):
    return (dFr(mu + h, m) - dFr(mu - h, m)) / (2 * h)
grid = np.linspace(-3.0, 3.0, 60001)
def eqs(m):
    g = dFr(grid, m)
    pos = g > 0
    return grid[:-1][pos[:-1] != pos[1:]]
for m in [0.3, 2.0, 3.0, 3.4, 3.6, 4.0]:
    r = eqs(m)
    print(f"(5) slow prior mean m={m:+.2f}: equilibria mu* = {np.round(r, 3)}, F_red'' = {np.round(d2Fr(r, m), 4)}")
lo, hi = 3.0, 6.0   # bisection on the equilibrium count 3 -> 1 (saddle-node)
for _ in range(40):
    mid = 0.5 * (lo + hi)
    lo, hi = (mid, hi) if len(eqs(mid)) == 3 else (lo, mid)
r = eqs(lo)
print(f"(5) saddle-node at m* = {lo:.6f}: equilibria {np.round(r, 4)}, F_red'' = {np.round(d2Fr(r, lo), 4)}  (-> 0 for the merging pair)")
