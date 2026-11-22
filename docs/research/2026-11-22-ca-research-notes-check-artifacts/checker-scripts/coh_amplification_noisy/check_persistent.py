"""Persistent circulation (the note's T_sync / T_seq, i.e. W of def:fw-level0 with F=I, no sensing) under the
exclusion conditions that the note and the manuscript state for the cycle product A_c."""
import numpy as np, scipy.linalg as la
rng = np.random.default_rng(3)
def spd(k, rng, scale=1.0):
    M = rng.standard_normal((k, k)); return scale * (M @ M.T + 0.2 * np.eye(k))
def edge(Pj, Hi, Ri):
    S = Hi @ Pj @ Hi.T + Ri
    return Pj @ Hi.T @ la.solve(S, Hi)
rho = lambda M: float(max(abs(la.eigvals(M))))
def build_T(As, K, order=None):
    N = len(As)
    if order is None:
        T = np.zeros((N*K, N*K))
        for k in range(N):
            km = (k-1) % N
            T[k*K:(k+1)*K, k*K:(k+1)*K] = np.eye(K) - As[k]; T[k*K:(k+1)*K, km*K:(km+1)*K] += As[k]
        return T
    T = np.eye(N*K)
    for k in order:
        km = (k-1) % N; St = np.eye(N*K)
        St[k*K:(k+1)*K, k*K:(k+1)*K] = np.eye(K) - As[k]; St[k*K:(k+1)*K, km*K:(km+1)*K] += As[k]
        T = St @ T
    return T
def restricted(T, Ps, Hs, N, K):
    rs = [Hs[(k-1) % N].shape[0] for k in range(N)]
    B = np.zeros((N*K, sum(rs))); c = 0
    for k in range(N):
        B[k*K:(k+1)*K, c:c+rs[k]] = Ps[k] @ Hs[(k-1) % N].T; c += rs[k]
    return la.pinv(B) @ T @ B

# (1) the note's own C4 witness (posterior headers, rho(A_c) = 171/910 < 1)
P1 = np.array([[1, 1.9], [1.9, 4.0]]); P2 = np.array([[0.1, 0.09], [0.09, 0.1]])
h1 = np.array([[0., 1.]]); h2 = np.array([[1., 0.]]); R2 = np.array([[0.1]]); R1 = np.array([[8/11]])
A12 = edge(P1, h2, R2); A21 = edge(P2, h1, R1)
tau = np.trace(A12 @ A21) / ((1/(1+0.1)) * (0.1/(0.1+8/11)))
print(f"(1) C4 witness: rho(A_c)={rho(A12@A21):.6f}, tau_circ={tau:.4f}, rho(T_sync)={rho(build_T([A12, A21], 2)):.6f}, rho(T_seq)={rho(build_T([A12, A21], 2, [1, 0])):.6f}")

# (2) level-1 reading of posted PRIOR covariances, R_i = H_i P_i H_i^T + R_c (prop:coh-no-amplification(c)): rank-one random cycles
cnt = unst = 0; worst = 0
for t in range(4000):
    K = int(rng.integers(2, 4)); N = int(rng.integers(2, 5))
    Ps = [spd(K, rng, 10**rng.uniform(-1, 1)) for _ in range(N)]
    hs = [rng.standard_normal((1, K)) for _ in range(N)]
    Rs = [hs[i] @ Ps[i] @ hs[i].T + 10**rng.uniform(-2, 0) for i in range(N)]
    As = [edge(Ps[k], hs[(k-1) % N], Rs[(k-1) % N]) for k in range(N)]
    Ac = np.eye(K)
    for k in list(range(1, N)) + [0]: Ac = As[k] @ Ac
    assert rho(Ac) < 1
    cnt += 1
    TV = restricted(build_T(As, K), Ps, hs, N, K); r_ = rho(TV)
    unst += r_ > 1 + 1e-9; worst = max(worst, r_)
print(f"(2) level-1 posted-prior headers, rank-one codes: rho(A_c)<1 in all {cnt}; rho(T_sync restricted) > 1 in {unst}; largest {worst:.4f}")

# (3) posterior headers at the header fixed point (C4 setting), rank-one codes
cnt = unst = 0; worst = 0
for t in range(3000):
    K = int(rng.integers(2, 4)); N = int(rng.integers(2, 5))
    Ps = [spd(K, rng, 10**rng.uniform(-1, 1)) for _ in range(N)]
    hs = [rng.standard_normal((1, K)) for _ in range(N)]
    Rc = [10**rng.uniform(-2, 0) for _ in range(N)]
    Rs = [hs[i] @ Ps[i] @ hs[i].T + Rc[i] for i in range(N)]
    for it in range(200):
        for i in range(N):
            im = (i-1) % N; S = hs[im] @ Ps[i] @ hs[im].T + Rs[im]
            Pt = Ps[i] - Ps[i] @ hs[im].T @ la.solve(S, hs[im] @ Ps[i]); Rs[i] = hs[i] @ Pt @ hs[i].T + Rc[i]
    As = [edge(Ps[k], hs[(k-1) % N], Rs[(k-1) % N]) for k in range(N)]
    Ac = np.eye(K)
    for k in list(range(1, N)) + [0]: Ac = As[k] @ Ac
    assert rho(Ac) < 1
    cnt += 1; r_ = rho(restricted(build_T(As, K), Ps, hs, N, K)); unst += r_ > 1 + 1e-9; worst = max(worst, r_)
print(f"(3) posterior headers at the header fixed point: rho(A_c)<1 in all {cnt}; rho(T_sync restricted) > 1 in {unst}; largest {worst:.4f}")

# (4) common code of rank 2 with COMMON noise (prop (d)) and with proportional noises (C7(1)); coded dynamics z_k = H x_k
for label, prop in (("common noise", False), ("proportional noises", True)):
    cnt = unst = 0; worst = 0
    for t in range(4000):
        r = 2; N = int(rng.integers(2, 5))
        R0 = spd(r, rng, 10**rng.uniform(-1, 1)); al = 10**rng.uniform(-1, 1, N) if prop else np.ones(N)
        Xs = [spd(r, rng, 10**rng.uniform(-1.5, 1.5)) for _ in range(N)]
        Bs = [Xs[k] @ la.inv(Xs[k] + al[(k-1) % N]*R0) for k in range(N)]      # H A_{k,k-1} = B_k H
        T = np.zeros((N*r, N*r))
        for k in range(N):
            km = (k-1) % N; T[k*r:(k+1)*r, k*r:(k+1)*r] = np.eye(r) - Bs[k]; T[k*r:(k+1)*r, km*r:(km+1)*r] += Bs[k]
        ev = la.eigvals(T); cnt += 1; m_ = max(abs(ev)); unst += m_ > 1 + 1e-7; worst = max(worst, m_)
    print(f"(4) common code rank 2, {label}: coded synchronous circulation has rho > 1 in {unst}/{cnt}; largest {worst:.6f}")

# (5) higher-rank extension of the tau>1 criterion: det(I - T|V) = prod det(Sigma_k) * det(I - noiseless coded cycle product)
maxrel = 0; odd = odd_unst = 0
for t in range(2000):
    N = int(rng.integers(2, 4)); r = 2; K = int(rng.integers(3, 5))
    Ps = [spd(K, rng, 10**rng.uniform(-1, 1)) for _ in range(N)]
    Hs = [rng.standard_normal((r, K)) for _ in range(N)]
    Rs = [spd(r, rng, 10**rng.uniform(-1, 1)) for _ in range(N)]
    As = [edge(Ps[k], Hs[(k-1) % N], Rs[(k-1) % N]) for k in range(N)]
    A0 = [edge(Ps[k], Hs[(k-1) % N], np.zeros((r, r))) for k in range(N)]
    Ac0 = np.eye(K)
    for k in list(range(1, N)) + [0]: Ac0 = A0[k] @ Ac0
    sig = 1.0
    for k in range(N):
        X = Hs[(k-1) % N] @ Ps[k] @ Hs[(k-1) % N].T; sig *= la.det(X) / la.det(X + Rs[(k-1) % N])
    pred = sig * la.det(np.eye(K) - Ac0)
    for order in (None, list(range(1, N)) + [0]):
        TV = restricted(build_T(As, K, order), Ps, Hs, N, K)
        d = la.det(np.eye(N*r) - TV); maxrel = max(maxrel, abs(d - pred) / (abs(pred) + 1e-12))
        if pred < -1e-9:
            odd += 1; odd_unst += rho(TV) > 1
print(f"(5) rank-2 codes: max relative error of det(I - T|V) = prod det(Sigma_k) det(I - A_c^noiseless): {maxrel:.2e}; negative determinant in {odd} operator draws, of which unstable: {odd_unst}")
