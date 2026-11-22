"""Theorem (eigen-loading): if each null-independent component k has act loading b_k with
S_{0,k}(theta) b_k = rho_k(theta) b_k (e.g. b_k a joint eigenvector of A_k, A_k^T, Q_k), then the
cross blocks of Pi^c are kappa_kl b_k b_l^T/(|b_k||b_l|) with kappa_kl > 0.
EXPECTED: rank-one positive cross blocks in every draw (up to 1e-8); NEG CONTROL: generic loading
(not an eigenvector) gives cross blocks that are not rank one."""
import numpy as np
from scipy.linalg import solve_discrete_are, solve_discrete_lyapunov
rng = np.random.default_rng(11)
def sigma_c_rts(A, Q, b, q):
    N = A.shape[0]; bb = b.reshape(N, 1)
    Pp = solve_discrete_are(A.T, bb, Q, np.array([[q]]))
    S = (bb.T @ Pp @ bb).item() + q
    Pf = Pp - Pp @ bb @ bb.T @ Pp / S
    J = Pf @ A.T @ np.linalg.inv(Pp)
    Ps = solve_discrete_lyapunov(J, Pf - J @ Pp @ J.T)
    return 0.5 * (Ps + Ps.T)
def comp(n, eigen=True):
    bh = rng.uniform(0.2, 1.0, n); bh /= np.linalg.norm(bh)
    Pp = np.eye(n) - np.outer(bh, bh)
    M = rng.normal(size=(n, n)); M = M / max(np.abs(np.linalg.eigvals(Pp @ M @ Pp)).max(), 1e-3) * 0.8
    lam = rng.uniform(-0.9, 0.9)
    A = lam * np.outer(bh, bh) + Pp @ M @ Pp
    R = rng.normal(size=(n, n)); R = R @ R.T + 0.1 * np.eye(n)
    Q = rng.uniform(0.1, 2) * np.outer(bh, bh) + Pp @ R @ Pp + (0.0 if n > 1 else 0.5)
    if not eigen:
        bh = rng.uniform(0.2, 1.0, n); bh /= np.linalg.norm(bh)
    return A, Q, bh * rng.uniform(0.1, 1.5)
def run(eigen, ndraw=300):
    worst_rank, min_kappa, cnt = 0.0, np.inf, 0
    for _ in range(ndraw):
        m = rng.integers(2, 4); sizes = rng.integers(2, 4, m)
        comps = [comp(s, eigen) for s in sizes]
        N = sizes.sum(); A = np.zeros((N, N)); Q = np.zeros((N, N)); b = np.zeros(N); bl = []; i = 0
        for (Ak, Qk, bk), s in zip(comps, sizes):
            A[i:i+s, i:i+s] = Ak; Q[i:i+s, i:i+s] = Qk; b[i:i+s] = bk; bl.append(list(range(i, i+s))); i += s
        if np.abs(np.linalg.eigvals(A)).max() >= 0.97 or np.linalg.eigvalsh(Q).min() <= 1e-6: continue
        Pc = np.linalg.inv(sigma_c_rts(A, Q, b, rng.uniform(0.05, 2)))
        cnt += 1
        for k in range(m):
            for l in range(k + 1, m):
                X = Pc[np.ix_(bl[k], bl[l])]
                sv = np.linalg.svd(X, compute_uv=False)
                worst_rank = max(worst_rank, sv[1] / sv[0] if sv[0] > 0 else 0)
                bk, bl_ = b[bl[k]], b[bl[l]]
                kappa = bk @ X @ bl_ / (np.linalg.norm(bk) * np.linalg.norm(bl_))
                min_kappa = min(min_kappa, kappa)
    return cnt, worst_rank, min_kappa
cnt, wr, mk = run(True)
print(f"eigen-loaded: draws {cnt}, max sigma2/sigma1 of cross blocks {wr:.2e}, min kappa {mk:.3e}")
print("[PASS]" if (wr < 1e-8 and mk > 0) else "[FAIL]", "eigen-loading theorem: rank-one cross blocks with kappa>0")
cnt, wr, mk = run(False)
print(f"generic loading (NEG CONTROL): draws {cnt}, max sigma2/sigma1 {wr:.2e}")
print("[PASS]" if wr > 1e-4 else "[FAIL]", "negative control: cross blocks not rank one for generic loadings")
