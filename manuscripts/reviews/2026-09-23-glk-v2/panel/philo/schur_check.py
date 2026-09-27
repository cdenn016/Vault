"""Dimension of GL(K)-equivariant interface maps without dressing (Schur-type check).
(1) S in R^{r x K} with S g = S for all g (trivial action on comparison space): solution space dim.
(2) X in R^{K x K} with X g = g X for all g (defining action on both sides): solution space dim.
(3) Same for the block group prod GL(d_b) acting on R^K with full-input S: dim of {S : S g = S}."""
import numpy as np
from scipy.linalg import null_space, block_diag
rng = np.random.default_rng(1)
K, r = 4, 2
gs = [rng.standard_normal((K, K)) + 2 * np.eye(K) for _ in range(6)]
# vec(S g) = (g^T kron I_r) vec(S) for column-major vec
A1 = np.vstack([np.kron(g.T, np.eye(r)) - np.eye(r * K) for g in gs])
A2 = np.vstack([np.kron(g.T, np.eye(K)) - np.kron(np.eye(K), g) for g in gs])
gb = [block_diag(rng.standard_normal((2, 2)) + 2 * np.eye(2), rng.standard_normal((2, 2)) + 2 * np.eye(2)) for _ in range(6)]
A3 = np.vstack([np.kron(g.T, np.eye(r)) - np.eye(r * K) for g in gb])
print("dim{S: Sg=S, g in GL(4)}          =", null_space(A1).shape[1])
print("dim{X: Xg=gX, g in GL(4)}         =", null_space(A2).shape[1], "(scalars)")
print("dim{S: Sg=S, g in GL(2)xGL(2)}    =", null_space(A3).shape[1])
