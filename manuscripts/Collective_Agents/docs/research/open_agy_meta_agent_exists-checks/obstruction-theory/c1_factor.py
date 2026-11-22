"""Part (1): claim C1 (exchangeable blocks) and the factor model Sigma = D + G V G^T.

Expected outcomes are declared before each check (EXPECT ...) and compared.
"""
import numpy as np
import sympy as sp
from common import is_diffusive, contrast, baseline_exchangeable_mean

rng = np.random.default_rng(20261121)
ok_all = True


def report(name, expect, got):
    global ok_all
    flag = "PASS" if expect == got else "FAIL"
    if expect != got:
        ok_all = False
    print(f"[{flag}] {name}: expected {expect}, got {got}")


# ---------------- C1 symbolic ----------------
a, b, n = sp.symbols("alpha beta n", positive=True)
N4 = 4
Sig = a * sp.eye(N4) + b * sp.ones(N4, N4)
Pi = sp.simplify(Sig.inv())
off = sp.simplify(Pi[0, 1])
rs = sp.simplify(sum(Pi[0, j] for j in range(N4)))
print("C1 symbolic (n=4): offdiag =", off, "; row sum =", rs)
report("C1 offdiag == -beta/(alpha(alpha+4beta))", True,
       sp.simplify(off + b / (a * (a + 4 * b))) == 0)
report("C1 row sum == 1/(alpha+4beta)", True, sp.simplify(rs - 1 / (a + 4 * b)) == 0)
# general n via Sherman-Morrison identity check: (aI+b11^T)(I/a - b/(a(a+nb)) 11^T) = I
nn = sp.Symbol("n", positive=True, integer=True)
# scalar check of the identity on the 1-direction and on 1^perp
lam1 = (a + nn * b) * (1 / a - nn * b / (a * (a + nn * b)))
report("Sherman-Morrison on 1-direction equals 1", True, sp.simplify(lam1 - 1) == 0)

# ---------------- C1 numeric: alpha=1, beta=0.5, n=4 ----------------
alpha, beta, n = 1.0, 0.5, 4
S1 = alpha * np.eye(n) + beta * np.ones((n, n))
# population: block C1 plus an independent block C2 (same law) -> block-diagonal
Sfull = np.zeros((2 * n, 2 * n))
Sfull[:n, :n] = S1
Sfull[n:, n:] = S1
Pfull = np.linalg.inv(Sfull)
d = is_diffusive(Pfull)
report("C1 numeric diffusive (offdiag<=0 and rowsum>=0)", (True, True), (bool(d[0]), bool(d[1])))
cpl = -Pfull[0, 1]
leak = Pfull[0].sum()
print(f"   coupling {cpl:.6f} (formula {beta/(alpha*(alpha+n*beta)):.6f}); leak {leak:.6f} (formula {1/(alpha+n*beta):.6f})")
r, xin, xout = contrast(Pfull, range(n))
report("C1 contrast r = 1 + n beta/alpha = 3", True, abs(r - 3.0) < 1e-10)
print(f"   r = {r:.12f}, xin = {xin:.6f} (1/alpha), xout = {xout:.6f} (1/(alpha+n beta))")
rb, rb_formula, abar, epsbar = baseline_exchangeable_mean(Pfull)
print(f"   clause (c) mean-coupling baseline = {rb:.6f} (formula {rb_formula:.6f}), significance {r/rb:.4f}")
report("each block is a collective under clause (c) mean coupling (r > baseline)", True, r > rb)

# negative control: beta<0 (still PD since alpha+n beta>0) -> positive offdiag
betan = -0.2
Sn = alpha * np.eye(n) + betan * np.ones((n, n))
Pn = np.linalg.inv(Sn)
dn = is_diffusive(Pn)
report("NEG CONTROL beta=-0.2: offdiag<=0 fails", False, bool(dn[0]))
print(f"   max offdiag = {dn[2]:.6f} (formula {-betan/(alpha*(alpha+n*betan)):.6f})")

# ---------------- factor model: exact formula ----------------
def factor_pi(Dd, G, V):
    Sig = np.diag(Dd) + G @ V @ G.T
    return Sig, np.linalg.inv(Sig)


def K_of(Dd, G, V):
    return np.linalg.inv(np.linalg.inv(V) + G.T @ np.diag(1 / Dd) @ G)


# identity Pi_ij = -g_i^T K g_j/(d_i d_j) and D Pi 1 = 1 - G K G^T D^{-1} 1 on random draws
maxerr = 0.0
for _ in range(200):
    N, m = rng.integers(3, 8), rng.integers(1, 4)
    Dd = rng.uniform(0.2, 2.0, N)
    G = rng.normal(size=(N, m))
    X = rng.normal(size=(m, m))
    V = X @ X.T + 0.1 * np.eye(m)
    Sig, P = factor_pi(Dd, G, V)
    K = K_of(Dd, G, V)
    Pform = np.diag(1 / Dd) - np.diag(1 / Dd) @ G @ K @ G.T @ np.diag(1 / Dd)
    maxerr = max(maxerr, np.abs(P - Pform).max())
    rs1 = np.diag(Dd) @ P @ np.ones(N)
    rs2 = np.ones(N) - G @ K @ G.T @ (np.ones(N) / Dd)
    maxerr = max(maxerr, np.abs(rs1 - rs2).max())
report("Woodbury formula for Pi and for row sums (200 draws, err<1e-9)", True, maxerr < 1e-9)
print(f"   max error {maxerr:.2e}")

# Theorem F(a): G>=0 and K^{-1} a Z-matrix => offdiag(Pi) <= 0
viol = 0
for _ in range(500):
    N, m = rng.integers(3, 9), rng.integers(1, 5)
    Dd = rng.uniform(0.2, 2.0, N)
    G = rng.uniform(0, 1, size=(N, m)) * (rng.uniform(size=(N, m)) < 0.7)
    T = G.T @ np.diag(1 / Dd) @ G
    E = rng.uniform(0, 0.5, size=(m, m))
    E = 0.5 * (E + E.T)
    np.fill_diagonal(E, 0)
    Toff = T - np.diag(np.diag(T))
    B = Toff + E                       # nonneg, symmetric
    c = B.sum(axis=1) + rng.uniform(0.05, 1.0, m)
    Vinv = np.diag(c) - B              # offdiag(Vinv + T) = -E <= 0
    V = np.linalg.inv(Vinv)
    if np.linalg.eigvalsh(V).min() <= 0:
        continue
    _, P = factor_pi(Dd, G, V)
    if is_diffusive(P)[2] > 1e-12:
        viol += 1
report("THM F(a): G>=0, K^{-1} Z-matrix => Pi offdiag <= 0 (violations in 500 draws)", 0, viol)

# Theorem F(c): unit block-indicator loadings + diffusive V^{-1} => Pi diffusive
viol = 0
for _ in range(500):
    m = rng.integers(2, 5)
    sizes = rng.integers(1, 4, m)
    N = sizes.sum()
    G = np.zeros((N, m))
    idx = 0
    for k, s in enumerate(sizes):
        G[idx: idx + s, k] = 1.0
        idx += s
    Dd = rng.uniform(0.2, 2.0, N)
    A = rng.uniform(0, 1, (m, m))
    A = 0.5 * (A + A.T)
    np.fill_diagonal(A, 0)
    Vinv = np.diag(A.sum(1) + rng.uniform(0.01, 1.0, m)) - A   # diffusive precision of factors
    V = np.linalg.inv(Vinv)
    _, P = factor_pi(Dd, G, V)
    dd = is_diffusive(P)
    if not (dd[0] and dd[1]):
        viol += 1
report("THM F(c): unit indicator loadings + diffusive V^{-1} => Pi diffusive (violations/500)", 0, viol)

# ---------------- counterexamples (G >= 0) ----------------
# CE1: single factor, heterogeneous loadings -> negative row sum
Dd = np.array([1.0, 1.0]); G = np.array([[1.0], [0.1]]); V = np.array([[20.0]])
_, P = factor_pi(Dd, G, V)
dd = is_diffusive(P)
report("CE1 single factor g=(1,0.1), v=20: offdiag ok, row sum fails", (True, False), (bool(dd[0]), bool(dd[1])))
S1_, S2_ = (G[:, 0] / Dd).sum(), (G[:, 0] ** 2 / Dd).sum()
print(f"   row sums {P.sum(1)}; criterion max g = {G.max():.3f} vs (1/v+S2)/S1 = {(1/V[0,0]+S2_)/S1_:.4f}")

# CE2: overlap collider, independent factors V=I: agent 3 loads on both factors
Dd = np.ones(3); G = np.array([[1.0, 0], [0, 1.0], [1.0, 1.0]]); V = np.eye(2)
_, P = factor_pi(Dd, G, V)
print("   CE2 Pi*8 =\n", np.round(8 * P, 10))
report("CE2 overlap collider: Pi_12 = +1/8 > 0", True, abs(P[0, 1] - 0.125) < 1e-12)
# negative control: drop the overlapping agent -> block diagonal, diffusive
_, P2 = factor_pi(np.ones(2), np.array([[1.0, 0], [0, 1.0]]), np.eye(2))
report("CE2 NEG CONTROL without agent 3: diffusive", True, bool(all(is_diffusive(P2)[:2])))

# CE3: disjoint supports, negatively correlated factors (not MTP2)
Dd = np.ones(4); G = np.array([[1.0, 0], [1.0, 0], [0, 1.0], [0, 1.0]]); V = np.array([[1.0, -0.5], [-0.5, 1.0]])
_, P = factor_pi(Dd, G, V)
report("CE3 disjoint supports, V12<0: positive cross entry", True, P[0, 2] > 0)
print(f"   Pi_13 = {P[0,2]:.6f}")
# CE4: disjoint supports, V >= 0 entrywise but V^{-1} not Z (chain of three), strong loadings
aa = 0.6
V = np.array([[1, aa, 0], [aa, 1, aa], [0, aa, 1.0]])
print(f"   CE4 V^-1_13 = {np.linalg.inv(V)[0,2]:.4f} (>0: not MTP2); min eig V = {np.linalg.eigvalsh(V).min():.4f}")
for s in [0.3, 1.0, 3.0]:
    Dd = np.ones(3); G = s * np.eye(3)
    _, P = factor_pi(Dd, G, V)
    print(f"   loading {s}: Pi_13 = {P[0,2]:+.6f}")
Dd = np.ones(3); G = 3.0 * np.eye(3)
_, P = factor_pi(Dd, G, V)
report("CE4 V>=0 entrywise, loading 3: Pi_13 > 0", True, P[0, 2] > 0)
# iff check for disjoint supports: MTP2 V (V^{-1} Z) -> K>=0 for all loading strengths
viol = 0
for _ in range(300):
    m = 3
    A = rng.uniform(0, 1, (m, m)); A = 0.5 * (A + A.T); np.fill_diagonal(A, 0)
    Vinv = np.diag(A.sum(1) + rng.uniform(0.01, 1, m)) - A
    V = np.linalg.inv(Vinv)
    for s in [0.1, 1.0, 10.0, 100.0]:
        _, P = factor_pi(np.ones(3), s * np.eye(3), V)
        if is_diffusive(P)[2] > 1e-12:
            viol += 1
report("MTP2 factors + disjoint supports: offdiag<=0 at all loading strengths (violations)", 0, viol)

print("ALL CHECKS AS EXPECTED" if ok_all else "SOME CHECK DIFFERED FROM EXPECTATION")
