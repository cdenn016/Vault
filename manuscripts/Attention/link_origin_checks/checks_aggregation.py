r"""Float64 checks for the aggregation section of link_origin.tex (small dimensions; grounding only)."""
import numpy as np
from scipy.linalg import expm

rng = np.random.default_rng(1)
rel = lambda a, b: np.abs(a - b).max() / max(1.0, np.abs(b).max())

# (1) Complement split: exp(OT) = (I - P) + O e^{TO} (TO)^{-1} T, P = O (TO)^{-1} T.
K, r = 7, 4                                         # non-tiling channel: rank r < K
O = rng.standard_normal((K, r)); T = rng.standard_normal((r, K))
TO = T @ O; P = O @ np.linalg.solve(TO, T)
print("exp(OT) = (I-P) + O e^TO (TO)^-1 T   rel err",
      rel(expm(O @ T), np.eye(K) - P + O @ expm(TO) @ np.linalg.solve(TO, T)))
print("(I-P) fixes ker T, kills im O         err",
      max(np.abs((np.eye(K) - P) @ O).max(), np.abs(T @ (np.eye(K) - P)).max()))

# (2) Expected message under per-channel source labels, complement carried by the receiver.
H, d = 2, 2; K = 7; Hd = H * d                       # Hd < K: complement of dimension 3
O = rng.standard_normal((K, Hd)); T = rng.standard_normal((Hd, K))
TO = T @ O; P = O @ np.linalg.solve(TO, T); E = expm(TO) @ np.linalg.inv(TO)
N = 5; xi = rng.standard_normal((N, K)); i = N - 1
beta = rng.dirichlet(np.ones(N), size=H)             # beta[h, j], causal row i = N-1
# Exact enumeration over the head-label tuple (J^1, J^2): channel h carries T_h xi_{J^h}.
enum = np.zeros(K)
for j1 in range(N):
    for j2 in range(N):
        z = np.concatenate([T[:d] @ xi[j1], T[d:] @ xi[j2]])
        enum += beta[0, j1] * beta[1, j2] * ((np.eye(K) - P) @ xi[i] + O @ E @ z)
closed = (np.eye(K) - P) @ xi[i] + sum(O @ E[:, h*d:(h+1)*d] @ T[h*d:(h+1)*d] @ (beta[h] @ xi) for h in range(H))
print("label enumeration = closed form       rel err", rel(enum, closed))

# (3) Tiled heads (Hd = K): P = I, no complement, and the message is the current head sum
#     with reparameterized receiving maps O_h' = O E_{:,h}.
H, d = 3, 2; K = H * d
O = rng.standard_normal((K, K)); T = rng.standard_normal((K, K)); TO = T @ O
E = expm(TO) @ np.linalg.inv(TO)
P = O @ np.linalg.solve(TO, T)
print("tiled: P = I                          err", np.abs(P - np.eye(K)).max())
xi = rng.standard_normal((N, K)); beta = rng.dirichlet(np.ones(N), size=H)
optA = sum(O @ E[:, h*d:(h+1)*d] @ T[h*d:(h+1)*d] @ (beta[h] @ xi) for h in range(H))
Oprime = O @ E
current = sum(Oprime[:, h*d:(h+1)*d] @ T[h*d:(h+1)*d] @ (beta[h] @ xi) for h in range(H))
print("tiled: option A = head sum with O E   rel err", rel(optA, current))
print("tiled: det(E) > 0 (exp image in GL+)  ", np.linalg.det(expm(TO)) > 0)

# (4) Isotropic Gaussian fusion: posterior mean on the observed subspace is
#     (alpha xi_i + lambda m)/(alpha + lambda), and unobserved directions keep xi_i.
alpha, lam = 2.0, 6.0
K = 5; W = np.linalg.qr(rng.standard_normal((K, 2)))[0]       # observed subspace, orthonormal
Pw = W @ W.T; xi_i = rng.standard_normal(K); m = rng.standard_normal(K)
J = alpha * np.eye(K) + lam * Pw                                   # prior precision + evidence on W
post = np.linalg.solve(J, alpha * xi_i + lam * Pw @ m)
pred = (np.eye(K) - Pw) @ xi_i + Pw @ (alpha * xi_i + lam * m) / (alpha + lam)
print("fusion: partial residual alpha/(a+l)  rel err", rel(post, pred))

# (5) A positive diagonal gate is the exponential of its log: x*sigmoid(x) = exp(log sigmoid(x)) x.
x = rng.standard_normal(8)
silu = x / (1 + np.exp(-x))
print("SiLU = exp(diag(log sigma(x))) x      rel err", rel(expm(np.diag(np.log(1 / (1 + np.exp(-x))))) @ x, silu))
