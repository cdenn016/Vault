r"""Independent check of C3a (aggregate collider) and C3c (eigen-loading), own code.

Model: x_{t+1} = A x_t + c eta_t + xi_t (xi ~ N(0,Qx), block diagonal over U1,U2,U3; c eta_t is the
conditioning-measurable sensing input), eta_{t+1} = F eta_t + b^T x_t + omega_t (Var q).
Direct: Lyapunov + exact conditioning on eta_{-L..L}.  Formula: Cov(b1'x1, b2'x2 | eta)
 = -(1/2pi) int beta1 beta2/(q+beta1+beta2+beta3), beta_k = b_k' (e^{i th}-A_k)^{-1} Q_k (e^{i th}-A_k)^{-H} b_k.
"""
import numpy as np
from scipy.linalg import block_diag, solve_discrete_lyapunov

rng = np.random.default_rng(7)


def cond_cov(M, Nz, L):
    d = M.shape[0]
    P = solve_discrete_lyapunov(M, Nz)
    pw = [np.eye(d)]
    for _ in range(2 * L):
        pw.append(M @ pw[-1])
    T = 2 * L + 1
    c = np.array([(pw[k] @ P)[-1, -1] for k in range(T)])
    See = c[np.abs(np.subtract.outer(np.arange(T), np.arange(T)))]
    Cxe = np.empty((d - 1, T))
    for i in range(T):
        s = i - L
        Mx = pw[s] @ P if s >= 0 else P @ pw[-s].T  # Cov(z_s, z_0)
        Cxe[:, i] = Mx[-1, :-1]
    S = P[:-1, :-1] - Cxe @ np.linalg.solve(See, Cxe.T)
    return 0.5 * (S + S.T)


def spectral(Ab, Qb, bb, q, Mgrid=4096, qfac=1.0):
    th = 2 * np.pi * np.arange(Mgrid) / Mgrid
    betas = []
    for Ak, Qk, bk in zip(Ab, Qb, bb):
        bet = np.empty(Mgrid)
        for m, t in enumerate(th):
            y = np.linalg.solve((np.exp(1j * t) * np.eye(len(bk)) - Ak).conj().T, bk)  # (e^{it}-A)^{-H} b
            bet[m] = np.real(np.conj(y) @ Qk @ y)
        betas.append(bet)
    D = qfac * q + sum(betas)
    return -np.mean(betas[0] * betas[1] / D)


def draw(sizes, common_source=False, eigen=False, opposite=False):
    Ab, Qb, bb = [], [], []
    for k, n in enumerate(sizes):
        if eigen:
            Ak = rng.uniform(-0.7, 0.7) * np.eye(n); Qk = rng.uniform(0.3, 2) * np.eye(n)
        else:
            Ak = rng.normal(size=(n, n)); Ak *= rng.uniform(0.3, 0.7) / max(abs(np.linalg.eigvals(Ak)))
            G = rng.normal(size=(n, n)); Qk = G @ G.T / n + 0.2 * np.eye(n)
        bk = rng.uniform(0.2, 1.0, n) * (rng.random(n) < 0.8)
        if not bk.any():
            bk[0] = 0.5
        if opposite and k == 1:
            bk = -bk
        Ab.append(Ak); Qb.append(Qk); bb.append(bk)
    A = block_diag(*Ab); Qx = block_diag(*Qb); b = np.concatenate(bb)
    if common_source:  # last block is one non-acting source read by the first agent of U1 and of U2
        b[-1] = 0.0; bb[-1][:] = 0.0
        A[0, -1] = rng.uniform(0.3, 0.8); A[sizes[0], -1] = rng.uniform(0.3, 0.8)
        Qx[-1, -1] = rng.uniform(20, 60)
    n = A.shape[0]
    c = rng.uniform(-0.3, 0.3, n)  # sensing of eta (conditioning-measurable input)
    F = rng.uniform(0.2, 0.8); q = rng.uniform(0.05, 1.0)
    M = np.zeros((n + 1, n + 1)); M[:n, :n] = A; M[:n, n] = c; M[n, :n] = b; M[n, n] = F
    return A, Qx, b, c, F, q, M, Ab, Qb, bb


print("== C3a: aggregate collider, disjoint ancestries, generic (signed, non-normal) blocks, sensing feedback ==")
sizes = (3, 2, 2); i1 = slice(0, 3); i2 = slice(3, 5)
err = 0; neg = 0; negentry = 0; posoff = 0; planted = np.inf; tot = 0; conv = 0
while tot < 30:
    A, Qx, b, c, F, q, M, Ab, Qb, bb = draw(sizes)
    if max(abs(np.linalg.eigvals(M))) > 0.9:
        continue
    Nz = block_diag(Qx, q)
    S = cond_cov(M, Nz, 120); S2 = cond_cov(M, Nz, 90)
    conv = max(conv, abs(S - S2).max() / abs(S).max())
    direct = b[i1] @ S[i1, i2] @ b[i2]
    f = spectral(Ab, Qb, bb, q)
    err = max(err, abs(direct / f - 1))
    planted = min(planted, abs(direct / spectral(Ab, Qb, bb, q, qfac=2.0) - 1))
    neg += direct < 0
    negentry += S[i1, i2].min() < 0
    Pi = np.linalg.inv(S); posoff += (Pi - np.diag(np.diag(Pi))).max() > 0
    tot += 1
print(f" 30 draws: window convergence {conv:.1e}; max rel |direct - formula| = {err:.1e}; planted error (q -> 2q) min rel discrepancy {planted:.1e}")
print(f" contracted covariance < 0 in {neg}/30; some Sigma^c cross entry < 0 in {negentry}/30; Pi^c has a positive off-diagonal in {posoff}/30")

pos = 0; tot = 0; mism = np.inf
while tot < 100:
    A, Qx, b, c, F, q, M, Ab, Qb, bb = draw((3, 2, 1), common_source=True)
    if max(abs(np.linalg.eigvals(M))) > 0.9:
        continue
    S = cond_cov(M, block_diag(Qx, q), 90)
    d_ = b[i1] @ S[i1, i2] @ b[i2]
    pos += d_ > 0; tot += 1
    mism = min(mism, abs(d_ / spectral(Ab[:2], Qb[:2], bb[:2], q) - 1))
print(f" control, one common (non-acting) source read by both ancestries: contracted covariance > 0 in {pos}/100; min rel discrepancy from the disjoint-ancestry formula {mism:.1e}")

dif = 0; tot = 0
while tot < 100:
    A, Qx, b, c, F, q, M, Ab, Qb, bb = draw((1, 1), opposite=True)
    if max(abs(np.linalg.eigvals(M))) > 0.9:
        continue
    S = cond_cov(M, block_diag(Qx, q), 90); Pi = np.linalg.inv(S)
    dif += ((Pi - np.diag(np.diag(Pi))).max() <= 1e-10) and (Pi.sum(1).min() >= 0); tot += 1
print(f" control, two opposite-sign scalar actors: Pi^c diffusive in {dif}/100 (one sign is needed for the obstruction)")

print("== C3a timing scope: acts load on posterior means m+, contrast on prior means m (setting of C3/E2) ==")
print(" see chk2_settingP.py: E2 has one-signed loadings and negative precision cross entries (diffusive); the factor phi1*phi2<0 enters because the act coordinates are not the contrast coordinates.")

print("== C3c: eigen-loading (A_k = a_k I, Q_k = q_k I): cross blocks of the precision of U are kappa bhat bhat^T, kappa>0 ==")
rank1 = 0; kpos = 0; tot = 0; dev = 0
while tot < 40:
    A, Qx, b, c, F, q, M, Ab, Qb, bb = draw(sizes, eigen=True)
    if max(abs(np.linalg.eigvals(M))) > 0.9:
        continue
    S = cond_cov(M, block_diag(Qx, q), 90); Pi = np.linalg.inv(S)
    blk = Pi[i1, i2]
    sv = np.linalg.svd(blk, compute_uv=False)
    bh1 = bb[0] / np.linalg.norm(bb[0]); bh2 = bb[1] / np.linalg.norm(bb[1])
    kappa = bh1 @ blk @ bh2
    dev = max(dev, abs(blk - kappa * np.outer(bh1, bh2)).max() / abs(blk).max())
    rank1 += sv[1] / sv[0] < 1e-9; kpos += kappa > 0; tot += 1
print(f" 40 draws: rank one in {rank1}/40, kappa>0 in {kpos}/40, max rel |block - kappa bhat bhat^T| = {dev:.1e}")
r2 = 0; negc = 0; tot = 0
while tot < 40:
    A, Qx, b, c, F, q, M, Ab, Qb, bb = draw(sizes)
    if max(abs(np.linalg.eigvals(M))) > 0.9:
        continue
    S = cond_cov(M, block_diag(Qx, q), 90); Pi = np.linalg.inv(S)
    sv = np.linalg.svd(Pi[i1, i2], compute_uv=False)
    r2 += sv[1] / sv[0] > 1e-6; tot += 1
    bmask = np.outer(bb[0] > 0, bb[1] > 0)
    negc += (Pi[i1, i2][bmask] <= 0).any()
print(f" control, generic loadings: cross block not rank one in {r2}/40; an acting cross pair with Pi_ij <= 0 in {negc}/40 (the note reports 13/2531 for nonnegative A; rare)")
