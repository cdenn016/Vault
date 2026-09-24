r"""L19: gauge behavior of the three candidate base tensors of PIFB2 eq:induced_metric_full (1874),
against Theory b02 thm:pb-pullback-gauge-invariance. Left-action convention:
  mu' = g mu, Sigma' = g Sigma g^T, A' = g A g^{-1} - dg g^{-1},
  D mu = d mu + A mu, D Sigma = d Sigma + A Sigma + Sigma A^T.
Tensors on base R^2 at a point c:
  h_cov   = Fisher(D mu, D Sigma)          (covariant score block)
  h_ord   = Fisher(d mu, d Sigma)          (fixed-gauge ordinary pullback, PIFB2's implemented default)
  t_twist = tr(A_mu A_nu)                  (frame-twist block)
Also: with pure-gauge A = -dU U^{-1} (Regime I), h_cov equals the ordinary pullback of U^{-1} q.
Also (sympy): contact form A = dz - x dy has A ^ dA != 0 (Theory prop:pb-contact-null-counterexample),
while an exact (flat, abelian) A = d lambda has A ^ dA = 0.
"""
import numpy as np
from scipy.linalg import expm
import sympy as sp

rng = np.random.default_rng(3)
K = 2
C1, C2, C3 = [rng.normal(size=(K, K)) for _ in range(3)]
a1, a2 = rng.normal(size=K), rng.normal(size=K)
B1, B2 = rng.normal(size=(K, K)), rng.normal(size=(K, K))
P1, P2 = [rng.normal(size=(K, K)) * 0.3 for _ in range(2)]

def mu(c): return a1 * np.sin(c[0]) + a2 * c[1] ** 2 + 0.2 * c[0] * c[1]
def Sig(c):
    L = np.eye(K) + 0.3 * (B1 * np.cos(c[0]) + B2 * c[1])
    return L @ L.T + 0.2 * np.eye(K)
def U(c): return expm(0.4 * (C1 * c[0] + C2 * c[1] + C3 * c[0] * c[1]))   # frame field (Regime I)
def g(c): return expm(0.5 * (P1 * np.cos(c[1]) + P2 * c[0]))               # local gauge transformation

h = 1e-5
def d(fun, c, k):
    e = np.zeros(2); e[k] = h
    return (fun(c + e) - fun(c - e)) / (2 * h)

def A_pure(c, k):                       # A_k = -(d_k U) U^{-1}
    return -d(U, c, k) @ np.linalg.inv(U(c))

def fisher(Si, dm, dS):
    Sinv = np.linalg.inv(Si)
    return np.array([[dm[a] @ Sinv @ dm[b] + 0.5 * np.trace(Sinv @ dS[a] @ Sinv @ dS[b]) for b in range(2)] for a in range(2)])

def tensors(mu_f, Sig_f, A_f, c):
    m, S = mu_f(c), Sig_f(c)
    dm = [d(mu_f, c, k) for k in range(2)]; dS = [d(Sig_f, c, k) for k in range(2)]
    A = [A_f(c, k) for k in range(2)]
    Dm = [dm[k] + A[k] @ m for k in range(2)]
    DS = [dS[k] + A[k] @ S + S @ A[k].T for k in range(2)]
    return fisher(S, Dm, DS), fisher(S, dm, dS), np.array([[np.trace(A[a] @ A[b]) for b in range(2)] for a in range(2)])

c = np.array([0.37, -0.52])
hc, ho, tt = tensors(mu, Sig, A_pure, c)
mu2 = lambda c: g(c) @ mu(c)
Sig2 = lambda c: g(c) @ Sig(c) @ g(c).T
def A2(c, k):
    gi = np.linalg.inv(g(c))
    return g(c) @ A_pure(c, k) @ gi - d(g, c, k) @ gi
hc2, ho2, tt2 = tensors(mu2, Sig2, A2, c)
print("covariant Fisher block change  :", np.abs(hc2 - hc).max())
print("ordinary (fixed-gauge) change  :", np.abs(ho2 - ho).max())
print("frame-twist tr(A A) change     :", np.abs(tt2 - tt).max())
# Regime I: h_cov = ordinary pullback of untwisted section q~ = U^{-1} q
mut = lambda c: np.linalg.solve(U(c), mu(c))
Sigt = lambda c: np.linalg.solve(U(c), np.linalg.solve(U(c), Sig(c)).T).T
_, hot, _ = tensors(mut, Sigt, lambda c, k: np.zeros((K, K)), c)
print("Regime I: h_cov - h_ord(U^{-1} q):", np.abs(hc - hot).max())
print("eigenvalues h_cov:", np.linalg.eigvalsh(hc), " eigenvalues tr(AA):", np.linalg.eigvalsh(tt))

x, y, z = sp.symbols('x y z')
def wedge_AdA(Ax, Ay, Az):
    # A = Ax dx + Ay dy + Az dz; coefficient of dx^dy^dz in A ^ dA
    curl = [sp.diff(Az, y) - sp.diff(Ay, z), sp.diff(Ax, z) - sp.diff(Az, x), sp.diff(Ay, x) - sp.diff(Ax, y)]
    return sp.simplify(Ax * curl[0] + Ay * curl[1] + Az * curl[2])
print("contact A = dz - x dy: A^dA coefficient =", wedge_AdA(0, -x, 1))
lam = sp.sin(x) * y + z ** 2
print("exact A = d lambda: A^dA coefficient =", wedge_AdA(sp.diff(lam, x), sp.diff(lam, y), sp.diff(lam, z)))
