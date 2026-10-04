"""Sanity checks for the cross-model verification of ch:links (verify_V2).

Float64, CPU only, no randomness beyond a fixed seed. These computations do not
prove anything; they probe the explicit witnesses and closed forms of the
statements under review.
"""
from __future__ import annotations

import numpy as np
from numpy.polynomial.hermite_e import hermegauss
from scipy.linalg import expm, logm
from scipy.optimize import minimize

rng = np.random.default_rng(20261003)
np.set_printoptions(precision=6, suppress=True)


def frechet_L(B: np.ndarray, T: np.ndarray, n: int = 2000) -> np.ndarray:
    r"""L(B,T)=\int_0^1 e^{tB} T e^{(1-t)B} dt by composite midpoint rule."""
    ts = (np.arange(n) + 0.5) / n
    acc = np.zeros_like(B, dtype=float)
    for t in ts:
        acc += expm(t * B) @ T @ expm((1 - t) * B)
    return acc / n


print("=== lem:link-exp-derivative (a),(b): random 3x3 ===")
for trial in range(3):
    B = rng.normal(size=(3, 3))
    T = 1e-2 * rng.normal(size=(3, 3))
    S = rng.normal(size=(3, 3))
    L = frechet_L(B, T)
    lhs = np.linalg.norm(expm(B + T) - expm(B) - L, 2)
    rhs = 0.5 * np.linalg.norm(T, 2) ** 2 * np.exp(np.linalg.norm(B, 2) + np.linalg.norm(T, 2))
    adj = np.trace(S.T @ L) - np.trace(frechet_L(B.T, S).T @ T)
    print(f"  trial {trial}: remainder {lhs:.3e} <= bound {rhs:.3e} : {lhs <= rhs};  adjoint identity residual {adj:.2e}")


print("\n=== cor:link-prior-necessary (a)(iii): stationary generator at a fold (K=2) ===")
mu_i = np.array([1.0, 0.0])
mu_j = np.array([1.0, 0.0])
Sig_j = np.eye(2)
W = np.eye(2)
J = np.array([[0.0, -1.0], [1.0, 0.0]])
omega = -np.log(3.0) * np.eye(2) + 2 * np.pi * J
M_star = np.outer(mu_i, mu_j) @ np.linalg.inv(Sig_j + np.outer(mu_j, mu_j))
second = Sig_j + np.outer(mu_j, mu_j)


def ell(M: np.ndarray) -> float:
    r"""l(M)=E 1/2 (k_i-Mk_j)^T W (k_i-Mk_j) with Sigma_i free (dropped constant), Sigma_ij=0."""
    r = mu_i - M @ mu_j
    return 0.5 * float(r @ W @ r) + 0.5 * float(np.trace(W @ M @ Sig_j @ M.T))


def grad_ell(M: np.ndarray) -> np.ndarray:
    return -W @ (np.outer(mu_i, mu_j) - M @ second)


print("  exp(omega) =", expm(omega).round(6).tolist(), " M* =", M_star.round(6).tolist())
print("  grad l(exp omega) =", grad_ell(expm(omega)).round(6).tolist(), " (claimed (1/3)diag(-1,1))")
print("  L(omega^T, diag(-1,1)) =", frechet_L(omega.T, np.diag([-1.0, 1.0])).round(8).tolist())
# finite-difference gradient of omega -> l(exp omega)
h = 1e-6
fd = np.zeros((2, 2))
for a in range(2):
    for b in range(2):
        E = np.zeros((2, 2))
        E[a, b] = 1.0
        fd[a, b] = (ell(expm(omega + h * E)) - ell(expm(omega - h * E))) / (2 * h)
print("  finite-difference gradient of l(exp .) at omega:", fd.round(6).tolist())


print("\n=== cor:link-prior-necessary (a)(iv): K=2, negative case mu_j^T Sigma_j^{-1} mu_i < 0 ===")
mu_i = np.array([1.0, 0.0])
mu_j = np.array([-1.0, 0.0])
Sig_j = np.eye(2)
W = np.eye(2)
second = Sig_j + np.outer(mu_j, mu_j)
M_star = np.outer(mu_i, mu_j) @ np.linalg.inv(second)
print("  M* =", M_star.round(6).tolist(), " tr M* =", np.trace(M_star), " l(M*) =", ell(M_star))


def ell_chart(v: np.ndarray) -> float:
    return ell(expm(v.reshape(2, 2)))


best = None
for start in range(12):
    v0 = rng.normal(size=4) * 0.5
    res = minimize(ell_chart, v0, method="BFGS", options={"gtol": 1e-10, "maxiter": 2000})
    val, nrm = res.fun, np.linalg.norm(res.x)
    if best is None or val < best[0]:
        best = (val, nrm, res.x)
    print(f"  start {start:2d}: chart value {val:.8f}  |omega| {nrm:8.3f}  gap to l(M*) {val - ell(M_star):.6f}")
# analytic candidate from the review: M=[[-1/2,a],[b,0]] with ab=-1/16 (double eigenvalue, Jordan block, in the closure)
a = (2.0) ** 0.25 / 4.0
b = -1.0 / (16.0 * a)
Mc = np.array([[-0.5, a], [b, 0.0]])
print("  closure candidate [[-1/2,a],[b,0]], ab=-1/16: l =", ell(Mc), " eigenvalues", np.linalg.eigvals(Mc))
print("  (the chart infimum found numerically should be >= l(M*) + margin and approach the closure value with |omega| growing)")

print("\n=== cor:link-prior-necessary (a)(iv): K=2, positive case ===")
mu_j = np.array([1.0, 0.5])
second = Sig_j + np.outer(mu_j, mu_j)
M_star = np.outer(mu_i, mu_j) @ np.linalg.inv(second)
lam = np.trace(M_star)
w, S = np.linalg.eig(M_star)
S = np.real(S)
for c0 in [1e-1, 1e-3, 1e-6]:
    D = np.diag([np.log(lam) if abs(wi - lam) < 1e-9 else np.log(c0) for wi in np.real(w)])
    Mc = S @ expm(D) @ np.linalg.inv(S)
    print(f"  c0={c0:.0e}: |exp(omega)-M*| = {np.linalg.norm(Mc - M_star):.2e}, l - l(M*) = {ell(Mc) - ell(M_star):.2e}")


print("\n=== prop:link-law-level-energy (c): Gaussian orbit Fisher form (K=3) ===")
K = 3
A = rng.normal(size=(K, K))
Sigma = A @ A.T + K * np.eye(K)
mu = rng.normal(size=K)
xi = rng.normal(size=(K, K))
Sh = np.linalg.cholesky(Sigma)  # Sigma = Sh Sh^T
# symmetric square root
evals, evecs = np.linalg.eigh(Sigma)
Sig_half = evecs @ np.diag(np.sqrt(evals)) @ evecs.T
Sig_mhalf = evecs @ np.diag(1 / np.sqrt(evals)) @ evecs.T


def kl_gauss(mu0, S0, mu1, S1) -> float:
    S1i = np.linalg.inv(S1)
    d = mu1 - mu0
    return 0.5 * (np.trace(S1i @ S0) - K + np.log(np.linalg.det(S1) / np.linalg.det(S0)) + d @ S1i @ d)


def D_t(t: float) -> float:
    g = expm(t * xi)
    return kl_gauss(mu, Sigma, g @ mu, g @ Sigma @ g.T)


t = 1e-3
hess_num = (D_t(t) - 2 * D_t(0.0) + D_t(-t)) / t**2
Bm = Sig_mhalf @ xi @ Sig_half
k_formula = float(np.linalg.norm(Sig_mhalf @ xi @ mu) ** 2 + 0.5 * np.linalg.norm(Bm + Bm.T, "fro") ** 2)
print(f"  second derivative of KL along orbit: {hess_num:.6f}; formula k_q(xi,xi): {k_formula:.6f}")
# stabilizer direction: xi = Sigma^{1/2} A Sigma^{-1/2}, A skew with A v = 0, v = Sigma^{-1/2} mu
v = Sig_mhalf @ mu
u = np.cross(v, rng.normal(size=K))
Askew = np.outer(u, v) - np.outer(v, u)  # A v = u (v.v) - v (u.v) = |v|^2 u ... need A v = 0: use A = w v^perp form
# simpler: in K=3 skew matrices with A v = 0 are multiples of the cross-product map by v
Askew = np.array([[0, -v[2], v[1]], [v[2], 0, -v[0]], [-v[1], v[0], 0]])
xi_stab = Sig_half @ Askew @ Sig_mhalf
Bs = Sig_mhalf @ xi_stab @ Sig_half
print("  stabilizer direction: |xi mu| =", np.linalg.norm(xi_stab @ mu), " |B+B^T|_F =", np.linalg.norm(Bs + Bs.T))
g1 = expm(0.7 * xi_stab)
print("  exp(0.7 xi_stab) fixes q: |g mu - mu| =", np.linalg.norm(g1 @ mu - mu), " |g Sigma g^T - Sigma| =", np.linalg.norm(g1 @ Sigma @ g1.T - Sigma))


print("\n=== prop:link-law-level-energy (b): Mahalanobis criterion and transport ===")
A2 = rng.normal(size=(K, K))
Sig_i = A2 @ A2.T + np.eye(K)
ev_i, V_i = np.linalg.eigh(Sig_i)
Sig_i_half = V_i @ np.diag(np.sqrt(ev_i)) @ V_i.T
mu_i3 = rng.normal(size=K)
mah_i = np.sqrt(mu_i3 @ np.linalg.solve(Sig_i, mu_i3))
# pick mu_j with the same Mahalanobis norm under Sigma
vj = rng.normal(size=K)
vj = vj / np.linalg.norm(vj) * mah_i
mu_j3 = Sig_half @ vj
vi = Sig_mhalf @ Sig_i_half @ np.linalg.solve(Sig_i_half, mu_i3)  # placeholder
vi = np.linalg.solve(Sig_i_half, mu_i3)
# rotation O in SO(3) carrying vj -> vi (same norm): Rodrigues
a_ = vj / np.linalg.norm(vj)
b_ = vi / np.linalg.norm(vi)
vcross = np.cross(a_, b_)
c_ = a_ @ b_
vx = np.array([[0, -vcross[2], vcross[1]], [vcross[2], 0, -vcross[0]], [-vcross[1], vcross[0], 0]])
O = np.eye(K) + vx + vx @ vx * (1 / (1 + c_))
Theta0 = Sig_i_half @ O @ Sig_mhalf
print("  det O =", np.linalg.det(O), " |Theta0 mu_j - mu_i| =", np.linalg.norm(Theta0 @ mu_j3 - mu_i3),
      " |Theta0 Sigma_j Theta0^T - Sigma_i| =", np.linalg.norm(Theta0 @ Sigma @ Theta0.T - Sig_i), " det Theta0 > 0:", np.linalg.det(Theta0) > 0)


print("\n=== lem:link-gaussian-gradients: 1-D loop-defect-type h, Gauss-Hermite quadrature ===")
# h(w) = 1/2 (1 - e^{w})^2 : a loop defect for G=GL^+(1), one edge, dim V = 1
x, wts = hermegauss(80)
wts = wts / wts.sum()


def E_h(m: float, s2: float, f) -> float:
    return float(np.sum(wts * f(m + np.sqrt(s2) * x)))


hf = lambda w: 0.5 * (1 - np.exp(w)) ** 2
dh = lambda w: -(1 - np.exp(w)) * np.exp(w)
d2h = lambda w: -(1 - np.exp(w)) * np.exp(w) + np.exp(2 * w)
m0, s0 = 0.3, 0.4
eps = 1e-5
fd_m = (E_h(m0 + eps, s0, hf) - E_h(m0 - eps, s0, hf)) / (2 * eps)
fd_s = (E_h(m0, s0 + eps, hf) - E_h(m0, s0 - eps, hf)) / (2 * eps)
print(f"  d/dmu E h = {fd_m:.8f} vs E h' = {E_h(m0, s0, dh):.8f}")
print(f"  d/dSigma E h = {fd_s:.8f} vs 1/2 E h'' = {0.5 * E_h(m0, s0, d2h):.8f}")


print("\n=== prop:link-conditional-transfer (c): fourth moment witness ===")
# omega ~ N(0,1): E e^{2w} = e^2, E e^{4w} = e^8
E2 = E_h(0.0, 1.0, lambda w: np.exp(2 * w))
E4 = E_h(0.0, 1.0, lambda w: np.exp(4 * w))
Ek2 = 1 + E2
Ek4 = 3 * E_h(0.0, 1.0, lambda w: (1 + np.exp(2 * w)) ** 2)
print(f"  E e^(2w) = {E2:.6f} (e^2 = {np.exp(2):.6f}); E e^(4w) = {E4:.6f} (e^8 = {np.exp(8):.6f})")
print(f"  E k_i^4 = {Ek4:.4f}; 3(E k_i^2)^2 = {3 * Ek2**2:.4f}; claimed 3(1+2e^2+e^8) = {3 * (1 + 2 * np.exp(2) + np.exp(8)):.4f}")


print("\n=== lem:link-growth (a): d=1 exponential moment bound ===")
for (c, m, s2) in [(1.0, 0.5, 2.0), (3.0, -1.0, 0.5)]:
    exact = E_h(m, s2, lambda w: np.exp(c * np.abs(w)))
    bound = np.exp(c * abs(m)) * 2 * np.exp(c**2 * s2 / 2)
    print(f"  c={c}, mu={m}, Sigma={s2}: E e^(c|w|) = {exact:.6f} <= bound {bound:.6f}: {exact <= bound}")


print("\n=== prop:link-induced-action (b): GL+(1) witness normalizer ===")
for rho in [0.3, 0.9, 0.999]:
    Wm = np.array([[1.0, -rho], [-rho, 1.0]])
    print(f"  rho={rho}: (1-rho^2)^(-1/2) = {(1 - rho**2) ** -0.5:.6f}, det(W)^(-1/2) = {np.linalg.det(Wm) ** -0.5:.6f}")
print("  P(omega >= 0) under N(0,1) = 0.5 > 0, so the joint normalizer diverges.")
