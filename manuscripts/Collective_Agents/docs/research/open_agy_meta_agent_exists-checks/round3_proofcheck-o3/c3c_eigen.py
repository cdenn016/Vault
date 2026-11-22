r"""Fresh-context check of C3c (Theorem C3-pair, eigen-loading).

Claim: under C3a's hypotheses, if J_k(theta)^{-1} b_k = rho_k(theta) b_k (rho_k > 0), every cross
block of Pi^c is kappa_kl bhat_k bhat_l^T with kappa_kl > 0, kappa = [(diag(sigma) - C)^{-1}]_kl,
sigma_k = (1/2pi) int rho_k, C = (1/2pi) int omega omega^T / D, omega_k = rho_k |b_k|,
D = q + sum_k rho_k |b_k|^2.
Construction: bhat_k a positive unit vector that is a joint eigenvector of A_k, A_k^T and Q_k.
Declared expectations:
  E1 cross blocks of Pi^c (precision of the full state of U) have sigma_2/sigma_1 <= 1e-8 and
     equal kappa bhat_k bhat_l^T with kappa > 0 matching the spectral formula to <= 1e-8.
  E2 marginal precision on a coordinate set containing supp(b): same cross blocks.
Negative controls:
  N1 generic positive loadings (not eigenvectors): cross blocks of rank two in most draws.
  N2 (scope) a non-acting agent that reads one member of U1 and one of U2: the cross block
     U1-U2 of the POPULATION precision is not rank one (expected sigma_2/sigma_1 >> 1e-8),
     and with reads of opposite sign a cross entry can be negative.
"""
import os

os.environ.setdefault("OMP_NUM_THREADS", "1")
import numpy as np
from scipy.linalg import solve_discrete_lyapunov, toeplitz, null_space

rng = np.random.default_rng(11)


def direct_conditional(A, k, b, F, Q, q, L=110):
    n = A.shape[0]
    M = np.zeros((n + 1, n + 1))
    M[:n, :n], M[:n, n], M[n, :n], M[n, n] = A, k, b, F
    if np.max(np.abs(np.linalg.eigvals(M))) >= 0.99:
        return None
    N = np.zeros((n + 1, n + 1)); N[:n, :n] = Q; N[n, n] = q
    P = solve_discrete_lyapunov(M, N)
    MP = [P]
    for _ in range(2 * L + 2):
        MP.append(M @ MP[-1])
    r = np.array([MP[h][n, n] for h in range(2 * L + 2)])
    times = np.arange(-L, L + 1)
    Cee = toeplitz(r[:len(times)])
    Cxe = np.stack([MP[t][n, :n] if t >= 0 else MP[-t][:n, n] for t in times], axis=1)
    S = P[:n, :n] - Cxe @ np.linalg.solve(Cee, Cxe.T)
    return (S + S.T) / 2


def eigen_group(n, supp=None):
    u = np.zeros(n)
    supp = np.arange(n) if supp is None else supp
    u[supp] = rng.uniform(0.3, 1.0, len(supp))
    u /= np.linalg.norm(u)
    Pp = null_space(u[None])
    lam = rng.uniform(-0.6, 0.8)
    Mm = rng.standard_normal((n - 1, n - 1))
    Mm *= rng.uniform(0.2, 0.8) / max(np.max(np.abs(np.linalg.eigvals(Mm))), 1e-9)
    A = lam * np.outer(u, u) + Pp @ Mm @ Pp.T
    X = rng.standard_normal((n - 1, n - 1))
    Q = rng.exponential(0.5) * np.outer(u, u) + Pp @ (X @ X.T / n + 0.1 * np.eye(n - 1)) @ Pp.T + 0.0
    Q += 0.05 * np.outer(u, u)
    return A, Q, u


def blockdiag(*Ms):
    n = sum(M.shape[0] for M in Ms); out = np.zeros((n, n)); i = 0
    for M in Ms:
        k = M.shape[0]; out[i:i + k, i:i + k] = M; i += k
    return out


def ratio(blk):
    s = np.linalg.svd(blk, compute_uv=False)
    return s[1] / s[0] if len(s) > 1 else 0.0


e1_rank = e1_kappa = 0.0
e1_pos = e2 = 0
used = 0
while used < 40:
    ns = [3, 3, 2]
    groups = [eigen_group(n) for n in ns]
    A = blockdiag(*[g[0] for g in groups]); Q = blockdiag(*[g[1] for g in groups])
    mags = rng.exponential(0.6, 3) + 0.1
    b = np.concatenate([m * g[2] for m, g in zip(mags, groups)])
    idx = [np.arange(0, 3), np.arange(3, 6), np.arange(6, 8)]
    k = rng.standard_normal(8) * 0.3
    F, q = rng.uniform(-0.9, 0.9), rng.exponential(0.5) + 0.05
    S = direct_conditional(A, k, b, F, Q, q)
    if S is None:
        continue
    used += 1
    Pi = np.linalg.inv(S)
    # spectral kappa
    N = 2048; th = 2 * np.pi * np.arange(N) / N
    rho = np.zeros((3, N))
    for kk, g in enumerate(groups):
        Ak, Qk, u = g
        Mz = np.exp(1j * th)[:, None, None] * np.eye(len(u))[None] - Ak[None]
        J = np.conj(np.transpose(Mz, (0, 2, 1))) @ np.linalg.inv(Qk)[None] @ Mz
        rho[kk] = np.real(np.einsum("i,tij,j->t", u, np.linalg.inv(J), u))
    om = rho * mags[:, None]
    D = q + np.sum(rho * mags[:, None] ** 2, 0)
    sig = rho.mean(1)
    C = np.einsum("kt,lt->kl", om, om / D) / N
    kap = np.linalg.inv(np.diag(sig) - C)
    for a in range(3):
        for c in range(a + 1, 3):
            blk = Pi[np.ix_(idx[a], idx[c])]
            e1_rank = max(e1_rank, ratio(blk))
            pred = kap[a, c] * np.outer(groups[a][2], groups[c][2])
            e1_kappa = max(e1_kappa, np.max(np.abs(blk - pred)) / np.max(np.abs(blk)))
            e1_pos += int(kap[a, c] > 0 and np.min(blk) > 0)
print(f"E1: draws={used}; max sigma2/sigma1 of cross blocks = {e1_rank:.2e}; max rel |block - kappa bb'| = {e1_kappa:.2e}; positive blocks {e1_pos}/{3 * used}")

# E2: marginalization with an unloaded coordinate in each group
worst = 0.0; used = 0
while used < 20:
    g1 = eigen_group(3, supp=np.array([0, 1])); g2 = eigen_group(3, supp=np.array([0, 2]))
    A = blockdiag(g1[0], g2[0]); Q = blockdiag(g1[1], g2[1])
    mags = rng.exponential(0.6, 2) + 0.1
    b = np.concatenate([mags[0] * g1[2], mags[1] * g2[2]])
    k = rng.standard_normal(6) * 0.3
    F, q = rng.uniform(-0.9, 0.9), rng.exponential(0.5) + 0.05
    S = direct_conditional(A, k, b, F, Q, q)
    if S is None:
        continue
    used += 1
    full = np.linalg.inv(S)
    keep = np.array([0, 1, 3, 5])
    marg = np.linalg.inv(S[np.ix_(keep, keep)])
    worst = max(worst, np.max(np.abs(marg[:2, 2:] - full[np.ix_([0, 1], [3, 5])])) / np.max(np.abs(full[np.ix_([0, 1], [3, 5])])))
print(f"E2: max rel difference of cross block, marginal vs full: {worst:.2e}")

# N1: generic loadings
rank2 = negs = used = 0
while used < 200:
    A = blockdiag(rng.uniform(0, 0.4, (3, 3)), rng.uniform(0, 0.4, (3, 3)))
    if np.max(np.abs(np.linalg.eigvals(A))) >= 0.95:
        continue
    X = rng.standard_normal((6, 6)) * 0.3
    Q = blockdiag(np.diag(rng.exponential(0.5, 3) + 0.05), np.diag(rng.exponential(0.5, 3) + 0.05))
    b = rng.exponential(0.6, 6) + 0.05
    k = rng.standard_normal(6) * 0.3
    F, q = rng.uniform(-0.9, 0.9), rng.exponential(0.5) + 0.05
    S = direct_conditional(A, k, b, F, Q, q)
    if S is None:
        continue
    used += 1
    blk = np.linalg.inv(S)[:3, 3:]
    rank2 += int(ratio(blk) > 1e-6)
    negs += int(np.min(blk) <= 0)
print(f"N1 generic loadings: cross block rank two in {rank2}/{used}; some cross entry <= 0 in {negs}/{used}")

# N2: scope - common non-acting listener d reading member 0 (U1) and member 3 (U2)
r2 = neg = used = 0
while used < 100:
    g1 = eigen_group(3); g2 = eigen_group(3)
    A = np.zeros((7, 7)); A[:3, :3] = g1[0]; A[3:6, 3:6] = g2[0]
    A[6, 6] = rng.uniform(0, 0.8)
    wsign = 1 if used < 50 else -1
    A[6, 0] = rng.exponential(0.8); A[6, 3] = wsign * rng.exponential(0.8)
    Q = blockdiag(g1[1], g2[1], np.array([[rng.exponential(0.5) + 0.05]]))
    mags = rng.exponential(0.6, 2) + 0.1
    b = np.concatenate([mags[0] * g1[2], mags[1] * g2[2], [0.0]])
    k = rng.standard_normal(7) * 0.3
    F, q = rng.uniform(-0.9, 0.9), rng.exponential(0.5) + 0.05
    S = direct_conditional(A, k, b, F, Q, q)
    if S is None:
        continue
    used += 1
    Pi_pop = np.linalg.inv(S)
    blk = Pi_pop[:3, 3:6]
    r2 += int(ratio(blk) > 1e-6)
    neg += int(np.min(blk) < 0)
    # the actors' own marginal precision must still be rank one
    assert ratio(np.linalg.inv(S[:6, :6])[:3, 3:]) < 1e-7
print(f"N2 common non-acting listener: population cross block rank two in {r2}/{used}; negative cross entry in {neg}/{used} (half the draws use reads of opposite sign); actors' marginal precision stayed rank one in all")
