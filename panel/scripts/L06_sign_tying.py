r"""L06 check of the belief-mean-sector claims at PIFB2.tex:1690 (sec:rg_status).

(a) In the belief-mean sector at fixed covariances, frames, and fixed beta, a five-term-type
    precision is D + (matrix-weighted Laplacian), with off-diagonal blocks -W_ij in the common
    (pulled-back) frame and -U_i^{-T} W_ij U_j^{-1} in agent frames; sign det = (-1)^K for GL^+.
(b) Integrating out within-cluster deviations at fixed barycenter (marginal precision of
    Y = W mu) can violate the sign condition on a sparse fine graph (scalar chain witness).
(c) Tying mu_i = mu_I (congruence S^T Lambda S) gives coarse off-diagonal blocks equal to
    minus the sum of cut-edge weights; within-cluster Laplacian terms cancel.
"""
import numpy as np

rng = np.random.default_rng(1)

def spd(K):
    M = rng.normal(size=(K, K))
    return M @ M.T + K * np.eye(K)

def glplus(K):
    while True:
        M = rng.normal(size=(K, K)) + 2 * np.eye(K)
        if np.linalg.det(M) > 0:
            return M

def build(K, N, edges):
    """Precision in agent-frame means for sum_i 1/2 mu_i^T D_i mu_i +
    sum_e 1/2 (nu_i - nu_j)^T W_e (nu_i - nu_j), nu_i = U_i^{-1} mu_i (pure-gauge transport)."""
    U = [glplus(K) for _ in range(N)]
    Lnu = np.zeros((N * K, N * K))
    W = {}
    for (i, j) in edges:
        We = spd(K) * rng.uniform(0.2, 2)
        W[(i, j)] = We
        for (p, q, s) in [(i, i, 1), (j, j, 1), (i, j, -1), (j, i, -1)]:
            Lnu[p*K:(p+1)*K, q*K:(q+1)*K] += s * We
    Uinv = np.zeros((N * K, N * K))
    for i in range(N):
        Uinv[i*K:(i+1)*K, i*K:(i+1)*K] = np.linalg.inv(U[i])
    Lmu = Uinv.T @ Lnu @ Uinv
    D = np.zeros_like(Lmu)
    for i in range(N):
        D[i*K:(i+1)*K, i*K:(i+1)*K] = spd(K) * 0.3
    return Lmu + D, U, W, Uinv

# (a)
for K in (1, 2, 3):
    N = 5
    edges = [(0, 1), (1, 2), (2, 3), (3, 4), (0, 2)]
    Lam, U, W, _ = build(K, N, edges)
    signs = [np.sign(np.linalg.det(Lam[i*K:(i+1)*K, j*K:(j+1)*K])) for (i, j) in edges]
    print("(a) K=%d off-diagonal block det signs:" % K, signs, "expected", (-1) ** K)

# (b) scalar chain of 6 nodes, clusters {0,1},{2,3},{4,5}, uniform barycenter weights
viol = 0
trials = 2000
worst = 0.0
for t in range(trials):
    N = 6
    w = rng.uniform(0.1, 3, size=N - 1)
    Lam = np.zeros((N, N))
    for e, we in enumerate(w):
        i, j = e, e + 1
        Lam[i, i] += we; Lam[j, j] += we; Lam[i, j] -= we; Lam[j, i] -= we
    Lam += np.diag(rng.uniform(0.01, 1, size=N))
    Wm = np.zeros((3, N))
    for I in range(3):
        Wm[I, 2*I] = Wm[I, 2*I + 1] = 0.5
    Cy = Wm @ np.linalg.inv(Lam) @ Wm.T
    Py = np.linalg.inv(Cy)
    if Py[0, 2] > 1e-12:
        viol += 1
        worst = max(worst, Py[0, 2] / np.sqrt(Py[0, 0] * Py[2, 2]))
print("(b) scalar chain: coarse precision (1,3) entry positive (sign det = +1 != (-1)^1) in %d/%d draws; max normalized = %.3e"
      % (viol, trials, worst))
# a specific deterministic witness
N = 6
Lam = np.zeros((N, N))
for i in range(N - 1):
    Lam[i, i] += 1; Lam[i+1, i+1] += 1; Lam[i, i+1] -= 1; Lam[i+1, i] -= 1
Lam += 0.1 * np.eye(N)
Wm = np.zeros((3, N))
for I in range(3):
    Wm[I, 2*I] = Wm[I, 2*I + 1] = 0.5
Py = np.linalg.inv(Wm @ np.linalg.inv(Lam) @ Wm.T)
print("(b) uniform chain (w=1, d=0.1) coarse precision:\n", np.round(Py, 6))

# (c) tying with pure-gauge transports: S maps mu_I (in parent frame U_I) to mu_i = U_i U_I^{-1} mu_I
K, N = 2, 6
edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (0, 3), (1, 4)]
Lam, U, W, Uinv = build(K, N, edges)
D = np.zeros_like(Lam)  # remove diagonal part to test Laplacian alone
Lam_L = Lam.copy()
for i in range(N):
    pass
clusters = [[0, 1], [2, 3], [4, 5]]
UI = [glplus(K) for _ in clusters]
S = np.zeros((N * K, len(clusters) * K))
for I, cl in enumerate(clusters):
    for i in cl:
        S[i*K:(i+1)*K, I*K:(I+1)*K] = U[i] @ np.linalg.inv(UI[I])
# Laplacian part only: rebuild without D
Lnu = np.zeros((N * K, N * K))
for (i, j), We in W.items():
    for (p, q, s) in [(i, i, 1), (j, j, 1), (i, j, -1), (j, i, -1)]:
        Lnu[p*K:(p+1)*K, q*K:(q+1)*K] += s * We
Lmu = Uinv.T @ Lnu @ Uinv
Lc = S.T @ Lmu @ S
# expected: coarse Laplacian in parent frames, W_IJ = sum of cut-edge weights
cid = {i: I for I, cl in enumerate(clusters) for i in cl}
Lexp_nu = np.zeros((3 * K, 3 * K))
for (i, j), We in W.items():
    I, J = cid[i], cid[j]
    if I == J:
        continue
    for (p, q, s) in [(I, I, 1), (J, J, 1), (I, J, -1), (J, I, -1)]:
        Lexp_nu[p*K:(p+1)*K, q*K:(q+1)*K] += s * We
UIinv = np.zeros((3 * K, 3 * K))
for I in range(3):
    UIinv[I*K:(I+1)*K, I*K:(I+1)*K] = np.linalg.inv(UI[I])
Lexp = UIinv.T @ Lexp_nu @ UIinv
print("(c) tying congruence vs cut-edge-sum Laplacian: max |diff| = %.2e" % np.max(np.abs(Lc - Lexp)))
