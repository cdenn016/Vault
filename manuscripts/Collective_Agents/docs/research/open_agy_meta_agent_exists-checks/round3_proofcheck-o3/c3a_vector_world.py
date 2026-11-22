r"""C3a with a two-dimensional world and one acted-on direction e (B = e b^T, correlated Q_w).

Claim: Sigma^c = (1/2pi) int (J + b b^T/q)^{-1}, q = 1/(e^T Q_w^{-1} e); the theorem's sign
conclusions then follow as in the scalar case.
Declared expectation: direct conditioning on the 2-d world window equals the spectral formula
to <= 1e-8 relative; b1^T S12 b2 < 0 in every draw.
Negative control (must fail): using q' = e^T Q_w e (the marginal variance along e instead of
the conditional one) mismatches whenever Q_w is not diagonal in a basis containing e.
"""
import os

os.environ.setdefault("OMP_NUM_THREADS", "1")
import numpy as np
from scipy.linalg import solve_discrete_lyapunov

rng = np.random.default_rng(5)


def cond_direct(A, Kx, Bm, Fw, Q, Qw, L):
    n, K = A.shape[0], Fw.shape[0]
    M = np.zeros((n + K, n + K))
    M[:n, :n] = A
    M[:n, n:] = Kx
    M[n:, :n] = Bm
    M[n:, n:] = Fw
    if np.max(np.abs(np.linalg.eigvals(M))) >= 0.99:
        return None
    N = np.zeros((n + K, n + K))
    N[:n, :n] = Q
    N[n:, n:] = Qw
    P = solve_discrete_lyapunov(M, N)
    MP = [P]
    for _ in range(2 * L + 2):
        MP.append(M @ MP[-1])
    times = np.arange(-L, L + 1)
    T = len(times)
    Cee = np.empty((T * K, T * K))
    Cxe = np.empty((n, T * K))
    for a, ta in enumerate(times):
        for c, tc in enumerate(times):
            h = ta - tc
            blk = MP[h][n:, n:] if h >= 0 else MP[-h][n:, n:].T
            Cee[a * K:(a + 1) * K, c * K:(c + 1) * K] = blk
        Cxe[:, a * K:(a + 1) * K] = MP[ta][n:, :n].T if ta >= 0 else MP[-ta][:n, n:]
    S = P[:n, :n] - Cxe @ np.linalg.solve(Cee, Cxe.T)
    return (S + S.T) / 2


def spectral(A, b, Q, q, N=2048):
    n = A.shape[0]
    th = 2 * np.pi * np.arange(N) / N
    Mz = np.exp(1j * th)[:, None, None] * np.eye(n)[None] - A[None]
    J = np.conj(np.transpose(Mz, (0, 2, 1))) @ np.linalg.inv(Q)[None] @ Mz
    return np.real(np.linalg.inv(J + (np.outer(b, b) / q)[None])).mean(0)


worst, worst_nc, neg, used = 0.0, np.inf, 0, 0
while used < 30:
    n1, n2 = 2, 2
    A = np.zeros((4, 4))
    A[:2, :2] = rng.uniform(0, 0.4, (2, 2))
    A[2:, 2:] = rng.uniform(0, 0.4, (2, 2))
    Q = np.diag(rng.exponential(0.5, 4) + 0.05)
    b = rng.exponential(0.5, 4) + 0.05
    e = rng.standard_normal(2)
    X = rng.standard_normal((2, 2))
    Qw = X @ X.T + 0.1 * np.eye(2)
    Fw = rng.uniform(-0.5, 0.5, (2, 2))
    Kx = rng.standard_normal((4, 2)) * 0.3
    Sd = cond_direct(A, Kx, np.outer(e, b), Fw, Q, Qw, 70)
    if Sd is None:
        continue
    used += 1
    q = 1 / (e @ np.linalg.solve(Qw, e))
    Ss = spectral(A, b, Q, q)
    worst = max(worst, np.max(np.abs(Sd - Ss)) / np.max(np.abs(Sd)))
    Ssw = spectral(A, b, Q, e @ Qw @ e)
    worst_nc = min(worst_nc, np.max(np.abs(Sd - Ssw)) / np.max(np.abs(Sd)))
    neg += int(b[:2] @ Sd[:2, 2:] @ b[2:] < 0)
print(f"2-d world: max rel error with q = 1/(e'Qw^-1 e): {worst:.2e}; b1'S12 b2 < 0 in {neg}/{used}")
print(f"negative control q' = e'Qw e: min rel error over draws {worst_nc:.2e} (expected >> 1e-8)")
