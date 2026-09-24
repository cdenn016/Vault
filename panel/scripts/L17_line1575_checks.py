"""L17: numeric checks of the two "findings recorded in 2026" at PIFB2.tex:1575.

(a) Parent-frame non-identifiability: the shadow N(U_i U_I^{-1} mu_I, U_i U_I^{-1} Sigma_I U_I^{-T} U_i^T)
    depends on (U_I, mu_I, Sigma_I) only through m = U_I^{-1} mu_I and S = U_I^{-1} Sigma_I U_I^{-T}.
    Check: replace (U_I, mu_I, Sigma_I) by (U_I g, U_I g m', ...) along the orbit with fixed (m, S).
(b) No left-equivariant permutation-symmetric map GL+(K)^n -> GL+(K): witness U_j = v^{j-1}, v a rotation
    of order n embedded in a 2x2 block. Check that left multiplication by v permutes the tuple cyclically
    and that ker(v - I) has dimension K - 2 < K, so (v - I) M = 0 forces rank M <= K - 2.
"""
from __future__ import annotations

import numpy as np
from scipy.linalg import expm

rng = np.random.default_rng(0)
K = 3
# (a)
U_i = expm(0.3 * rng.standard_normal((K, K)))
U_I = expm(0.3 * rng.standard_normal((K, K)))
mu_I = rng.standard_normal(K)
A = rng.standard_normal((K, K)); Sig_I = A @ A.T + K * np.eye(K)


def shadow(U_i, U_I, mu_I, Sig_I):
    Om = U_i @ np.linalg.inv(U_I)
    return Om @ mu_I, Om @ Sig_I @ Om.T


m0, S0 = shadow(U_i, U_I, mu_I, Sig_I)
g = expm(0.7 * rng.standard_normal((K, K)))  # move the parent frame along its orbit
U_I2 = U_I @ g
m = np.linalg.solve(U_I, mu_I); S = np.linalg.solve(U_I, np.linalg.solve(U_I, Sig_I).T).T
mu_I2 = U_I2 @ m; Sig_I2 = U_I2 @ S @ U_I2.T  # same (m, S), different U_I
m1, S1 = shadow(U_i, U_I2, mu_I2, Sig_I2)
print("(a) max |shadow mean diff| =", np.abs(m0 - m1).max(), " max |shadow cov diff| =", np.abs(S0 - S1).max())

# (b)
for K, n in [(2, 2), (2, 3), (3, 2), (4, 5)]:
    th = 2 * np.pi / n
    v = np.eye(K); v[:2, :2] = [[np.cos(th), -np.sin(th)], [np.sin(th), np.cos(th)]]
    tup = [np.linalg.matrix_power(v, j) for j in range(n)]
    moved = [v @ U for U in tup]
    perm_ok = all(any(np.allclose(M, U) for U in tup) for M in moved) and np.allclose(np.linalg.matrix_power(v, n), np.eye(K))
    kdim = K - np.linalg.matrix_rank(v - np.eye(K))
    print(f"(b) K={K} n={n}: v in GL+ (det={np.linalg.det(v):.3f}), left-mult permutes tuple={perm_ok}, dim ker(v-I)={kdim} (< K: {kdim < K})")
