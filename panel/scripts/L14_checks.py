"""L14 numerical checks of cited-fact content used in PIFB2.

(a) PIFB2:2328.  g_S(U,V) = a tr(S^-1 U S^-1 V) + b tr(S^-1 U) tr(S^-1 V) is invariant
    under S -> A S A^T, U -> A U A^T for every A in GL(K), and is positive definite
    iff a > 0 and a + K b > 0.
(b) PIFB2:1212.  For L(M) with M = A_Q A_K^T, gradient flow conserves
    A_Q^T A_Q - A_K^T A_K (Du-Hu-Lee 2018 balancedness in this index convention).
(c) PIFB2:633.  ALiBi slopes m_h = 2^(-8h/H), h = 1..H (Press et al. 2022, Sec. 3).
"""
import numpy as np
from scipy.integrate import solve_ivp

rng = np.random.default_rng(0)
K = 4


def sym(X: np.ndarray) -> np.ndarray:
    return 0.5 * (X + X.T)


def g(S: np.ndarray, U: np.ndarray, V: np.ndarray, a: float, b: float) -> float:
    Si = np.linalg.inv(S)
    return a * np.trace(Si @ U @ Si @ V) + b * np.trace(Si @ U) * np.trace(Si @ V)


B = rng.standard_normal((K, K)); S = B @ B.T + K * np.eye(K)
U = sym(rng.standard_normal((K, K))); V = sym(rng.standard_normal((K, K)))
A = rng.standard_normal((K, K))
a, b = 1.3, -0.2
inv_res = abs(g(A @ S @ A.T, A @ U @ A.T, A @ V @ A.T, a, b) - g(S, U, V, a, b))
print(f"(a) congruence-invariance residual: {inv_res:.2e}")


def min_eig_metric(a: float, b: float) -> float:
    # Gram matrix of g_I on a basis of Sym(K)
    basis = []
    for i in range(K):
        for j in range(i, K):
            E = np.zeros((K, K)); E[i, j] = E[j, i] = 1.0; basis.append(E)
    G = np.array([[g(np.eye(K), X, Y, a, b) for Y in basis] for X in basis])
    return float(np.linalg.eigvalsh(G).min())


for (aa, bb) in [(1.0, -1.0 / K + 1e-3), (1.0, -1.0 / K - 1e-3), (1.0, 5.0), (-0.1, 1.0)]:
    print(f"    a={aa}, b={bb:+.4f}, a+Kb={aa + K * bb:+.4f}: min eig of Gram = {min_eig_metric(aa, bb):+.3e}")

# (b)
d = 3
C = rng.standard_normal((d, d))
Aq0 = rng.standard_normal((d, d)); Ak0 = rng.standard_normal((d, d))


def rhs(t: float, y: np.ndarray) -> np.ndarray:
    Aq = y[: d * d].reshape(d, d); Ak = y[d * d:].reshape(d, d)
    M = Aq @ Ak.T
    G = M - C  # dL/dM for L = 0.5 ||M - C||_F^2
    return np.concatenate([(-G @ Ak).ravel(), (-G.T @ Aq).ravel()])


sol = solve_ivp(rhs, (0, 2.0), np.concatenate([Aq0.ravel(), Ak0.ravel()]), rtol=1e-11, atol=1e-12)
Aq1 = sol.y[: d * d, -1].reshape(d, d); Ak1 = sol.y[d * d:, -1].reshape(d, d)
c0 = Aq0.T @ Aq0 - Ak0.T @ Ak0; c1 = Aq1.T @ Aq1 - Ak1.T @ Ak1
o0 = Aq0 @ Aq0.T - Ak0 @ Ak0.T; o1 = Aq1 @ Aq1.T - Ak1 @ Ak1.T
print(f"(b) drift of A_Q^T A_Q - A_K^T A_K: {np.abs(c1 - c0).max():.2e}   (other ordering A A^T drift: {np.abs(o1 - o0).max():.2e})")
print(f"    loss change {0.5*np.linalg.norm(Aq0@Ak0.T-C)**2:.3f} -> {0.5*np.linalg.norm(Aq1@Ak1.T-C)**2:.3f}")

# (c)
H = 8
print("(c) ALiBi slopes H=8:", [2 ** (-8 * h / H) for h in range(1, H + 1)])
