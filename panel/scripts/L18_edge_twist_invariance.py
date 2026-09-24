"""L18: per-edge twist invariance at one base point, and redundancy of Regime-I frames.

Checks, in float64:
 (1) Theory prop:geo-edge-twist-invariance: the twist U_i^{-1} Theta_e U_j is unchanged by
     arbitrary per-agent passive re-expressions (U_i -> g_i U_i, Theta_e -> g_i Theta_e g_j^{-1})
     and conjugated by g0 under a reference change; so PIFB2's edge twist exp(delta_ij . G) of
     eq:edge_relaxed_omega carries an invariant conjugacy class (trace, spectrum) per edge.
 (2) If frames are NOT retained as data (pure lattice gauge Theta_e -> g_i Theta_e g_j^{-1}),
     a single link's trace is not invariant: the per-edge invariant exists because frames are data.
 (3) PIFB2 Regime I: KL(q_i || (U_i U_j^{-1})_# q_j) = KL(qt_i || qt_j) with qt_i = (U_i^{-1})_# q_i,
     so the alignment sector depends on (q_i, U_i) only through qt_i (frames redundant there).
"""
import numpy as np

rng = np.random.default_rng(18)
K = 3


def rand_gl(k):
    while True:
        A = rng.normal(size=(k, k))
        if np.linalg.det(A) > 0.2:
            return A


def rand_spd(k):
    A = rng.normal(size=(k, k))
    return A @ A.T + k * np.eye(k)


def kl_gauss(m1, S1, m2, S2):
    k = len(m1)
    S2i = np.linalg.inv(S2)
    d = m2 - m1
    return 0.5 * (np.log(np.linalg.det(S2) / np.linalg.det(S1)) + np.trace(S2i @ S1) + d @ S2i @ d - k)


# (1) twist invariance
U = [rand_gl(K) for _ in range(3)]
Theta = {(0, 1): rand_gl(K), (1, 2): rand_gl(K), (2, 0): rand_gl(K)}  # edge j->i stored as (i,j)
tw = {e: np.linalg.inv(U[e[0]]) @ T @ U[e[1]] for e, T in Theta.items()}
g = [rand_gl(K) for _ in range(3)]
U2 = [g[i] @ U[i] for i in range(3)]
Theta2 = {e: g[e[0]] @ T @ np.linalg.inv(g[e[1]]) for e, T in Theta.items()}
tw2 = {e: np.linalg.inv(U2[e[0]]) @ T @ U2[e[1]] for e, T in Theta2.items()}
res1 = max(np.abs(tw[e] - tw2[e]).max() for e in tw)
print(f"(1a) max |twist - twist'| under per-agent re-expression: {res1:.3e}")
g0 = rand_gl(K)  # reference change sigma' = sigma g0; u_i = sigma U_i^{-1} = sigma' (U_i g0)^{-1} -> U_i' = U_i g0
U3 = [Ui @ g0 for Ui in U]
tw3 = {e: np.linalg.inv(U3[e[0]]) @ T @ U3[e[1]] for e, T in Theta.items()}
res1b = max(np.abs(tw3[e] - np.linalg.inv(g0) @ tw[e] @ g0).max() for e in tw)
print(f"(1b) max |twist'' - g0^-1 twist g0| under reference change: {res1b:.3e}")
# PIFB2 edge-relaxed form Omega_ij = U_i exp(delta.G) U_j^{-1}: twist equals exp(delta.G)
from scipy.linalg import expm
D = rng.normal(size=(K, K)) * 0.4
Om = U[0] @ expm(D) @ np.linalg.inv(U[1])
res1c = np.abs(np.linalg.inv(U[0]) @ Om @ U[1] - expm(D)).max()
print(f"(1c) PIFB2 edge-relaxed twist U_i^-1 Omega U_j - exp(delta.G): {res1c:.3e}; "
      f"tr exp(delta.G) = {np.trace(expm(D)):.6f} (per-edge invariant, not a closed-loop trace)")

# (2) without frames as data: lattice gauge changes a single link trace
T = Theta[(0, 1)]
Tg = g[0] @ T @ np.linalg.inv(g[1])
print(f"(2) single-link trace before/after vertex gauge without frames: {np.trace(T):.4f} -> {np.trace(Tg):.4f}")
hol = Theta[(0, 1)] @ Theta[(1, 2)] @ Theta[(2, 0)]
hol2 = Theta2[(0, 1)] @ Theta2[(1, 2)] @ Theta2[(2, 0)]
print(f"    loop trace before/after: {np.trace(hol):.6f} -> {np.trace(hol2):.6f} (invariant)")

# (3) Regime I redundancy
mus = [rng.normal(size=K) for _ in range(2)]
Ss = [rand_spd(K) for _ in range(2)]
Om01 = U[0] @ np.linalg.inv(U[1])
kl_a = kl_gauss(mus[0], Ss[0], Om01 @ mus[1], Om01 @ Ss[1] @ Om01.T)
Ui = [np.linalg.inv(U[0]), np.linalg.inv(U[1])]
kl_b = kl_gauss(Ui[0] @ mus[0], Ui[0] @ Ss[0] @ Ui[0].T, Ui[1] @ mus[1], Ui[1] @ Ss[1] @ Ui[1].T)
print(f"(3) KL(q_i||Omega q_j) = {kl_a:.12f}; KL(qt_i||qt_j) = {kl_b:.12f}; diff {abs(kl_a-kl_b):.2e}")
