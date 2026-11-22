r"""Fresh-context check of C5 (Theorem F and Corollary F-share).

Sigma = D + G V G^T, D = diag(d) > 0, V > 0, K = (V^{-1} + G^T D^{-1} G)^{-1}.
 (a) Pi_ij = -g_i^T K g_j/(d_i d_j) (i != j), D Pi 1 = 1 - G K G^T D^{-1} 1.
 (b) G >= 0 and K^{-1} a Z-matrix => offdiag(Pi) <= 0.
 (c) disjoint supports, positive loadings: offdiag(Pi) <= 0 at every scale s iff V^{-1} is Z.
 (d) G c = 1 => D Pi 1 = G K V^{-1} c; unit indicator loadings + diffusive V^{-1} => diffusive Pi.
 (e) m = 1, G >= 0: leaks >= 0 iff max g_i <= (1/v + S2)/S1.
 F-share: V diagonal, G >= 0 => diffusivity needs "share a source" transitive.

Declared expectations:
  1. (a),(d) identities hold to ~1e-12 relative on random draws (any signs).
  2. (b): 0 violations among accepted draws; (d): 0 non-diffusive among indicator draws.
  3. (e): leak formula matches; CE1 leak = -0.0377; CE2 Pi = (1/8)[[5,1,-2],[1,5,-2],[-2,-2,4]].
  4. F-share: every non-transitive G >= 0 draw is non-diffusive (0 exceptions).
  5. Negative control (must FAIL the F-share conclusion): a mixed-sign G with
     non-transitive sharing gives a diffusive Pi.  Shows G >= 0 is load-bearing.
  6. Defect probe for (c) "iff": V with an unloaded factor 3, V_12 > 0 and (V^{-1})_23 > 0:
     offdiag(Pi) <= 0 at every scale on a grid although V^{-1} is not Z.  Expected: the
     "iff" fails as literally stated; with every factor loaded, the necessity direction
     holds (positive control: Pi_ij > 0 at large s).
"""
import itertools
import os

os.environ.setdefault("OMP_NUM_THREADS", "1")
import numpy as np

rng = np.random.default_rng(7)


def is_diffusive(Pi: np.ndarray, tol: float = 1e-12) -> bool:
    off = Pi - np.diag(np.diag(Pi))
    sc = np.max(np.abs(Pi))
    return bool(np.max(off) <= tol * sc and np.min(Pi.sum(1)) >= -tol * sc)


def pi_formula(d, G, V):
    D = np.diag(d)
    Kinv = np.linalg.inv(V) + G.T @ np.diag(1 / d) @ G
    K = np.linalg.inv(Kinv)
    Pi = np.diag(1 / d) - np.diag(1 / d) @ G @ K @ G.T @ np.diag(1 / d)
    rowsum_D = np.ones(len(d)) - G @ K @ G.T @ (1 / d)
    return Pi, rowsum_D, K


# 1. (a) identities
err_a = 0.0
for _ in range(200):
    n, m = rng.integers(3, 8), rng.integers(1, 4)
    d = rng.exponential(1, n) + 0.1
    G = rng.standard_normal((n, m))
    X = rng.standard_normal((m, m))
    V = X @ X.T + 0.2 * np.eye(m)
    Pi_f, rs, _ = pi_formula(d, G, V)
    Pi = np.linalg.inv(np.diag(d) + G @ V @ G.T)
    err_a = max(err_a, np.max(np.abs(Pi_f - Pi)) / np.max(np.abs(Pi)),
                np.max(np.abs(np.diag(d) @ Pi @ np.ones(n) - rs)))
print(f"(a) max relative error of Woodbury formulas over 200 draws: {err_a:.2e}")

# 2. (b) G >= 0 and K^{-1} Z-matrix
acc = viol_b = 0
while acc < 300:
    n, m = rng.integers(3, 8), rng.integers(2, 5)
    d = rng.exponential(1, n) + 0.1
    G = rng.exponential(1, (n, m)) * (rng.random((n, m)) < 0.5)
    B = rng.exponential(1, (m, m))
    B = (B + B.T) / 2
    np.fill_diagonal(B, 0)
    Vinv = np.diag(B.sum(1) + rng.exponential(1, m) + 0.1) - B  # diffusive M-matrix
    Kinv = Vinv + G.T @ np.diag(1 / d) @ G
    off = Kinv - np.diag(np.diag(Kinv))
    if np.max(off) > 0:
        continue
    acc += 1
    Pi = np.linalg.inv(np.diag(d) + G @ np.linalg.inv(Vinv) @ G.T)
    offP = Pi - np.diag(np.diag(Pi))
    if np.max(offP) > 1e-12 * np.max(np.abs(Pi)):
        viol_b += 1
print(f"(b) accepted draws with K^-1 Z: {acc}, violations of offdiag(Pi) <= 0: {viol_b}")

# 3. (d) identity and indicator loadings
err_d = 0.0
nondiff_d = 0
for _ in range(300):
    n, m = rng.integers(3, 9), rng.integers(1, 4)
    d = rng.exponential(1, n) + 0.1
    lab = rng.integers(0, m, n)
    G = np.zeros((n, m))
    G[np.arange(n), lab] = 1.0
    B = rng.exponential(1, (m, m))
    B = (B + B.T) / 2
    np.fill_diagonal(B, 0)
    Vinv = np.diag(B.sum(1) + rng.exponential(0.5, m) * (rng.random(m) < 0.7) + 1e-3) - B
    V = np.linalg.inv(Vinv)
    Pi_f, rs, K = pi_formula(d, G, V)
    c = np.ones(m)
    err_d = max(err_d, np.max(np.abs(rs - G @ K @ Vinv @ c)))
    if not is_diffusive(Pi_f, 1e-10):
        nondiff_d += 1
print(f"(d) max error of D Pi 1 = G K V^-1 c: {err_d:.2e}; non-diffusive indicator draws: {nondiff_d}/300")

# 4. (e) single factor and counterexamples
d = np.array([1.0, 1.0]); g = np.array([[1.0], [0.1]]); v = np.array([[20.0]])
Pi = np.linalg.inv(np.diag(d) + g @ v @ g.T)
S1 = np.sum(g[:, 0] / d); S2 = np.sum(g[:, 0] ** 2 / d)
print(f"(e) CE1 leaks = {Pi.sum(1)}, threshold (1/v+S2)/S1 = {(1/20 + S2)/S1:.4f}, max g = 1")
err_e = 0.0
for _ in range(300):
    n = rng.integers(2, 7)
    d = rng.exponential(1, n) + 0.1
    g = rng.exponential(1, n)
    vv = rng.exponential(3) + 0.1
    Pi = np.linalg.inv(np.diag(d) + vv * np.outer(g, g))
    S1 = np.sum(g / d); S2 = np.sum(g ** 2 / d)
    pred = (1 - g * S1 / (1 / vv + S2)) / d
    err_e = max(err_e, np.max(np.abs(Pi.sum(1) - pred)))
print(f"(e) leak formula max error: {err_e:.2e}")
G2 = np.array([[1, 0], [0, 1], [1, 1]], float)
Pi2 = np.linalg.inv(np.eye(3) + G2 @ G2.T)
print("CE2 8*Pi =\n", np.round(8 * Pi2, 12))

# 5. F-share on random G >= 0, V diagonal
nontrans = exc = trans_diff = trans = 0
for _ in range(2000):
    n, m = rng.integers(3, 7), rng.integers(2, 6)
    d = rng.exponential(1, n) + 0.05
    mask = rng.random((n, m)) < 0.35
    G = rng.exponential(1, (n, m)) * mask
    V = np.diag(rng.exponential(1, m) + 0.05)
    share = (mask.astype(int) @ mask.T.astype(int)) > 0
    np.fill_diagonal(share, True)
    transitive = all(not (share[i, j] and share[j, k]) or share[i, k]
                     for i, j, k in itertools.permutations(range(n), 3))
    Pi = np.linalg.inv(np.diag(d) + G @ V @ G.T)
    if not transitive:
        nontrans += 1
        if is_diffusive(Pi, 1e-10):
            exc += 1
    else:
        trans += 1
        trans_diff += int(is_diffusive(Pi, 1e-10))
print(f"F-share: non-transitive draws {nontrans}, diffusive among them {exc}; transitive draws {trans}, diffusive {trans_diff}")

# 6. negative control: mixed-sign loadings with non-transitive sharing
Gm = np.array([[1, 1, 0], [1, -1, 1], [0, 0, 1]], float)  # i-j share {a,b}, j-k share {c}, i-k none
Pim = np.linalg.inv(np.eye(3) + Gm @ Gm.T)
print("mixed-sign control: Sigma =\n", np.eye(3) + Gm @ Gm.T, "\nPi =\n", np.round(Pim, 6),
      "\n diffusive:", is_diffusive(Pim))

# 7. (c) "iff" probe: factor 3 unloaded
V = np.array([[1.0, 0.5, 0.6], [0.5, 1.0, 0.0], [0.6, 0.0, 1.0]])
Vinv = np.linalg.inv(V)
print("V^-1 =\n", np.round(Vinv, 4), "\n V^-1 is Z:", np.max(Vinv - np.diag(np.diag(Vinv))) <= 0)
G0 = np.array([[1.0, 0, 0], [0.7, 0, 0], [0, 1.3, 0], [0, 0.4, 0]])  # nobody loads on factor 3
dd = np.array([1.0, 0.5, 2.0, 1.0])
maxoff = -np.inf
for s in np.geomspace(1e-3, 1e3, 121):
    Pi = np.linalg.inv(np.diag(dd) + (s * G0) @ V @ (s * G0).T)
    maxoff = max(maxoff, np.max(Pi[~np.eye(4, dtype=bool)]))
print(f"(c) unloaded factor: max offdiag(Pi) over scales 1e-3..1e3 = {maxoff:.3e} (<= 0 means the 'iff' fails)")
# positive control: every factor loaded, (V^{-1})_23 > 0 => positive entry at large s
G1 = np.array([[1.0, 0, 0], [0, 1.0, 0], [0, 0, 1.0], [0, 0.5, 0]])
Pi = np.linalg.inv(np.diag(dd) + (30 * G1) @ V @ (30 * G1).T)
print(f"(c) all factors loaded, s=30: Pi[agent on f2, agent on f3] = {Pi[1, 2]:.3e} (expected > 0)")
