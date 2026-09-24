r"""L10: discrete step-size stability at the frozen-attention covariance fixed point (Appendix D)
for three update rules named in PIFB2: affine-invariant retraction (2496), Euclidean step on Sigma
(Appendix D gradient flow, 2855), Euclidean step on the Cholesky factor L (shipped default, 2655-2660).
F(Sigma) = 1/2 [tr(M Sigma) - 2 logdet Sigma], M = anchor + beta-averaged transported precision (frozen);
fixed point Sigma* = 2 M^{-1}. Largest eta with spectral radius of the linearized map < 1 is reported.
"""
import numpy as np
from scipy.linalg import expm, sqrtm
rng = np.random.default_rng(2)
K = 3
def grad(S, M): return 0.5 * (M - 2 * np.linalg.inv(S))
def step_retr(S, M, eta):
    Sh = np.real(sqrtm(S)); Shi = np.linalg.inv(Sh); N = 2 * S @ grad(S, M) @ S
    return Sh @ expm(-eta * Shi @ N @ Shi) @ Sh
def step_euc(S, M, eta): return S - eta * grad(S, M)
def step_chol(S, M, eta):
    L = np.linalg.cholesky(S); L = L - eta * np.tril(2 * grad(S, M) @ L); return L @ L.T
def symbasis(K):
    out = []
    for a in range(K):
        for b in range(a, K):
            E = np.zeros((K, K)); E[a, b] = E[b, a] = 1; out.append(E)
    return out
def rho(step, S, M, eta, h=1e-6):
    B = symbasis(K); J = np.array([[np.sum((step(S + h * Eb, M, eta) - step(S - h * Eb, M, eta)) / (2 * h) * Ea) / np.sum(Ea * Ea) for Eb in B] for Ea in B])
    return np.abs(np.linalg.eigvals(J)).max()
def eta_max(step, S, M):
    lo, hi = 0.0, 1.0
    while rho(step, S, M, hi) < 1 and hi < 1e6: hi *= 2
    for _ in range(40):
        mid = 0.5 * (lo + hi); lo, hi = (mid, hi) if rho(step, S, M, mid) < 1 else (lo, mid)
    return lo
Q, _ = np.linalg.qr(rng.standard_normal((K, K)))
print(" kappa(Sigma*) lambda_min(Sigma*) | eta_max retraction | eta_max Euclidean Sigma | eta_max Euclidean Cholesky L")
for kap in (1.0, 1e1, 1e2, 1e3, 1e4):
    lam = np.logspace(0, -np.log10(kap), K); Sst = (Q * lam) @ Q.T; M = 2 * np.linalg.inv(Sst)
    assert np.linalg.norm(grad(Sst, M)) < 1e-8 * np.linalg.norm(M)
    print(f"  {kap:8.0e}   {lam.min():10.1e}        | {eta_max(step_retr, Sst, M):12.4f}       | {eta_max(step_euc, Sst, M):14.3e}          | {eta_max(step_chol, Sst, M):14.3e}")
