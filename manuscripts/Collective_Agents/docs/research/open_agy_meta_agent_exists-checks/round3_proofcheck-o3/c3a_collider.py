r"""Fresh-context check of C3a (Lemma C3-a/C3-b, Theorem C3) by an independent method.

Model (setting LG-act, scalar world, sensing feedback included so that the reduction
sigma(eta) = sigma(y~) is exercised):
    x_{t+1} = A x_t + k eta_t + xi_t,        xi ~ N(0, Q),  A, Q block diagonal over U1, U2, U3,
    eta_{t+1} = F eta_t + b^T x_t + omega_t,  omega ~ N(0, q).
Direct method: stationary joint covariance of (x, eta) by Lyapunov, then exact Gaussian
conditioning of x_0 on the window eta_{-L..L}.  This uses neither the reduction nor the
spectral formula.
Claims checked:
  T1  Sigma^c = (1/2pi) int (J(theta) + b b^T/q)^{-1} dtheta, J = (e^{i th}-A)^H Q^{-1} (e^{i th}-A).
  T2  b1^T Sigma^c_12 b2 = -(1/2pi) int beta1 beta2/(q+beta1+beta2+beta3) < 0.
  T3  b >= 0 on U1 u U2  =>  some Sigma^c_ij < 0 (i in U1, j in U2, b_i b_j > 0).
  T4  (Lemma C3-b) Pi^c - Pi_0 - b b^T/q  is PSD, Pi_0 = Cov(x~_0)^{-1}.
Declared expectations:
  T1, T2 agree to <= 1e-8 relative on every admissible draw; T2 value < 0 in every draw;
  T3 holds in every draw; T4 min eigenvalue >= -1e-9 (relative) in every draw.
Negative controls (each expected to FAIL the corresponding conclusion in some draws):
  NC1  filtering (condition on eta_{-L..0} only): Pi_f - Pi_0 - b b^T/q is NOT PSD
       (the b b^T/q term needs eta_1).
  NC2  common source: one agent read by an actor of U1 and an actor of U2 (null
       independence violated): the formula of T2 no longer matches and b1^T Sigma_12 b2 > 0
       in some draws.
  NC3  opposite signs (b1 >= 0, b2 <= 0), single scalar actors: Pi^c is diffusive in some draws.
"""
import os

os.environ.setdefault("OMP_NUM_THREADS", "1")
import numpy as np
from scipy.linalg import solve_discrete_lyapunov

rng = np.random.default_rng(31)


def rand_stable(n: int, rho: float, nonneg: bool) -> np.ndarray:
    A = rng.exponential(1, (n, n)) if nonneg else rng.standard_normal((n, n))
    A *= rng.random((n, n)) < 0.7
    r = np.max(np.abs(np.linalg.eigvals(A))) if n > 0 else 1
    return A * (rho / max(r, 1e-9)) * rng.uniform(0.3, 1.0)


def rand_pd(n: int) -> np.ndarray:
    X = rng.standard_normal((n, n))
    return X @ X.T / n + 0.2 * np.eye(n)


def blockdiag(*Ms):
    n = sum(M.shape[0] for M in Ms)
    out = np.zeros((n, n))
    i = 0
    for M in Ms:
        k = M.shape[0]
        out[i:i + k, i:i + k] = M
        i += k
    return out


def direct_conditional(A, k, b, F, Q, q, L, causal=False):
    from scipy.linalg import toeplitz
    n = A.shape[0]
    M = np.zeros((n + 1, n + 1))
    M[:n, :n] = A
    M[:n, n] = k
    M[n, :n] = b
    M[n, n] = F
    if np.max(np.abs(np.linalg.eigvals(M))) >= 0.995:
        return None
    N = blockdiag(Q, np.array([[q]]))
    P = solve_discrete_lyapunov(M, N)
    MP = [P]
    for _ in range(2 * L + 2):
        MP.append(M @ MP[-1])
    r = np.array([MP[h][n, n] for h in range(2 * L + 2)])
    times = np.arange(-L, 1 if causal else L + 1)
    T = len(times)
    Cee = toeplitz(r[:T])
    Cxe = np.empty((n, T))
    for a, ta in enumerate(times):
        Cxe[:, a] = MP[ta][n, :n] if ta >= 0 else MP[-ta][:n, n]
    S = P[:n, :n] - Cxe @ np.linalg.solve(Cee, Cxe.T)
    return (S + S.T) / 2


def spectral(A, b, Q, q, idx, N=2048):
    n = A.shape[0]
    Qi = np.linalg.inv(Q)
    th = 2 * np.pi * np.arange(N) / N
    Mz = np.exp(1j * th)[:, None, None] * np.eye(n)[None] - A[None]
    J = np.conj(np.transpose(Mz, (0, 2, 1))) @ Qi[None] @ Mz
    Sig = np.real(np.linalg.inv(J + (np.outer(b, b) / q)[None])).mean(0)
    Jinv = np.linalg.inv(J)
    beta = [np.real(np.einsum("i,tij,j->t", b[ix], Jinv[:, ix][:, :, ix], b[ix])) if len(ix) else np.zeros(N) for ix in idx]
    T2 = np.mean(-beta[0] * beta[1] / (q + beta[0] + beta[1] + beta[2]))
    return Sig, T2


ndraw, L = 60, 110
stats = dict(t1=0.0, t2=0.0, t2neg=0, t3=0, t4min=np.inf, nc1_fail=0, used=0, conv=0.0)
while stats["used"] < ndraw:
    n1, n2, n3 = rng.integers(1, 4), rng.integers(1, 4), rng.integers(0, 3)
    nonneg = rng.random() < 0.5
    A = blockdiag(rand_stable(n1, 0.85, nonneg), rand_stable(n2, 0.85, nonneg), rand_stable(n3, 0.85, nonneg))
    Q = blockdiag(rand_pd(n1), rand_pd(n2), rand_pd(n3))
    n = n1 + n2 + n3
    idx = [np.arange(n1), np.arange(n1, n1 + n2), np.arange(n1 + n2, n)]
    b = np.concatenate([rng.exponential(0.6, n1), rng.exponential(0.6, n2), rng.standard_normal(n3) * 0.5])
    k = rng.standard_normal(n) * 0.4
    F, q = rng.uniform(-0.9, 0.9), rng.exponential(0.5) + 0.05
    Sd = direct_conditional(A, k, b, F, Q, q, L)
    if Sd is None:
        continue
    Sd2 = direct_conditional(A, k, b, F, Q, q, L - 30)
    stats["conv"] = max(stats["conv"], np.max(np.abs(Sd - Sd2)) / np.max(np.abs(Sd)))
    Ss, T2 = spectral(A, b, Q, q, idx)
    stats["used"] += 1
    stats["t1"] = max(stats["t1"], np.max(np.abs(Sd - Ss)) / np.max(np.abs(Sd)))
    c12 = b[idx[0]] @ Sd[np.ix_(idx[0], idx[1])] @ b[idx[1]]
    stats["t2"] = max(stats["t2"], abs(c12 - T2) / abs(T2))
    stats["t2neg"] += int(c12 < 0)
    blk = Sd[np.ix_(idx[0], idx[1])]
    stats["t3"] += int(np.min(blk) < 0)
    Pi_c = np.linalg.inv(Sd)
    Pi_0 = np.linalg.inv(solve_discrete_lyapunov(A, Q))
    I_other = Pi_c - Pi_0 - np.outer(b, b) / q
    stats["t4min"] = min(stats["t4min"], np.min(np.linalg.eigvalsh(I_other)) / np.max(np.abs(Pi_c)))
    Sf = direct_conditional(A, k, b, F, Q, q, L, causal=True)
    If = np.linalg.inv(Sf) - Pi_0 - np.outer(b, b) / q
    stats["nc1_fail"] += int(np.min(np.linalg.eigvalsh(If)) < -1e-9 * np.max(np.abs(Pi_c)))
print(f"draws={stats['used']}  window convergence (L vs L-30) max rel diff = {stats['conv']:.2e}")
print(f"T1 max rel |Sigma_direct - Sigma_spectral| = {stats['t1']:.2e}")
print(f"T2 max rel |b1'S12 b2 - formula| = {stats['t2']:.2e};  b1'S12 b2 < 0 in {stats['t2neg']}/{stats['used']}")
print(f"T3 some cross entry < 0 in {stats['t3']}/{stats['used']}")
print(f"T4 min over draws of lambda_min(I_other)/max|Pi^c| = {stats['t4min']:.2e}")
print(f"NC1 filtering bound fails (expected in many draws): {stats['nc1_fail']}/{stats['used']}")

# NC2: common source agent s read by one actor of U1 and one actor of U2 (null independence violated)
pos = used = 0
while used < 200:
    a1, a2, a3 = rng.uniform(0.0, 0.8, 3)
    w1, w2 = rng.exponential(1.0, 2)
    A = np.array([[a1, 0, w1], [0, a2, w2], [0, 0, a3]])
    Q = np.diag([rng.exponential(0.3) + 0.02, rng.exponential(0.3) + 0.02, rng.exponential(2) + 0.1])
    b = np.array([rng.exponential(0.6) + 0.05, rng.exponential(0.6) + 0.05, 0.0])
    k = rng.standard_normal(3) * 0.3
    F, q = rng.uniform(-0.9, 0.9), rng.exponential(0.5) + 0.05
    Sd = direct_conditional(A, k, b, F, Q, q, L)
    if Sd is None:
        continue
    used += 1
    pos += int(b[0] * Sd[0, 1] * b[1] > 0)
print(f"NC2 common source: b1 S12 b2 > 0 in {pos}/{used}")

# NC3: opposite signs, two scalar actors
diff = used = 0
while used < 100:
    A = np.diag(rng.uniform(-0.8, 0.8, 2))
    Q = np.diag(rng.exponential(0.5, 2) + 0.05)
    b = np.array([rng.exponential(0.6) + 0.05, -(rng.exponential(0.6) + 0.05)])
    k = rng.standard_normal(2) * 0.3
    F, q = rng.uniform(-0.9, 0.9), rng.exponential(0.5) + 0.05
    Sd = direct_conditional(A, k, b, F, Q, q, L)
    if Sd is None:
        continue
    used += 1
    Pi = np.linalg.inv(Sd)
    diff += int(Pi[0, 1] <= 0 and np.min(Pi.sum(1)) >= 0)
print(f"NC3 opposite signs, scalar actors: Pi^c diffusive in {diff}/{used}")
