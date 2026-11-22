"""Part (3): singular consensus matrices and the kernel term of the precision."""
import numpy as np
from scipy.linalg import solve_discrete_lyapunov, null_space
from common import is_diffusive, contrast

rng = np.random.default_rng(31)
ok_all = True


def report(name, expect, got):
    global ok_all
    flag = "PASS" if expect == got else "FAIL"
    if expect != got:
        ok_all = False
    print(f"[{flag}] {name}: expected {expect}, got {got}")


def lazy_ring(n, w=0.25):
    W = (1 - 2 * w) * np.eye(n)
    for i in range(n):
        W[i, (i + 1) % n] += w
        W[i, (i - 1) % n] += w
    return W


def is_Z(P, tol=1e-12):
    return (P - np.diag(np.diag(P))).max() <= tol


# ---------- static decomposition Pi_Y = P_K/tau + R_tau ----------
maxerr, bound_ok = 0.0, True
for _ in range(200):
    n = rng.integers(3, 8)
    d = rng.integers(1, n)
    U = np.linalg.qr(rng.normal(size=(n, n)))[0]
    lam = rng.uniform(0.2, 1.0, n) * rng.choice([-1, 1], n)
    lam[:d] = 0.0                                    # kernel of dimension d
    Wm = U @ np.diag(lam) @ U.T
    X = rng.normal(size=(n, n)); SX = X @ X.T + 0.2 * np.eye(n)
    tau = 10 ** rng.uniform(-4, 0)
    PiY = np.linalg.inv(Wm @ SX @ Wm.T + tau * np.eye(n))
    K = U[:, :d]; PK = K @ K.T
    R = PiY - PK / tau
    # R lives on K^perp and is bounded by 1/(s_min^2 lambda_min(SX))
    maxerr = max(maxerr, np.abs(PK @ R).max() * tau)
    smin = np.abs(lam[d:]).min()
    bound_ok &= np.linalg.norm(R, 2) <= 1 / (smin ** 2 * np.linalg.eigvalsh(SX).min()) * (1 + 1e-9)
report("Pi_Y = P_K/tau + R_tau with R_tau supported on K^perp (relative err < 1e-8)", True, maxerr < 1e-8)
report("||R_tau|| <= 1/(s_min^2 lambda_min(Sigma_X)) in all draws", True, bool(bound_ok))

# ---------- characterization: P_K (K inside 1^perp) is Z iff K = sum of within-block zero-sum spaces ----------
# (a) block construction -> Z
viol = 0
for _ in range(300):
    n = rng.integers(3, 9)
    perm = rng.permutation(n)
    cuts = np.sort(rng.choice(np.arange(1, n), rng.integers(0, n - 1), replace=False))
    blocks = np.split(perm, cuts)
    cols = []
    for bl in blocks:
        if len(bl) >= 2:
            B = np.zeros((n, len(bl))); B[bl, np.arange(len(bl))] = 1.0
            Zb = null_space(np.ones((1, len(bl))))         # zero-sum vectors on the block
            cols.append(B @ Zb)
    if not cols:
        continue
    K = np.linalg.qr(np.column_stack(cols))[0]
    if not is_Z(K @ K.T, 1e-10):
        viol += 1
report("block zero-sum kernels give a Z-matrix projector (violations/300)", 0, viol)
# (b) one-dimensional kernel v perp 1 with >= 3 nonzero entries -> positive entry
viol = 0
for _ in range(300):
    n = rng.integers(3, 9)
    k = rng.integers(3, n + 1)
    v = np.zeros(n); idx = rng.choice(n, k, replace=False); v[idx] = rng.normal(size=k)
    v[idx] -= v[idx].mean()
    if np.count_nonzero(np.abs(v) > 1e-9) < 3:
        continue
    v /= np.linalg.norm(v)
    if is_Z(np.outer(v, v), 1e-12):
        viol += 1
report("1-dim kernel with >=3 nonzero entries (v perp 1) has a positive projector entry (violations)", 0, viol)

# ---------- lazy ring n=4 ----------
W4 = lazy_ring(4)
ev, evec = np.linalg.eigh(W4)
print("   lazy ring n=4 eigenvalues", np.round(ev, 12))
v = np.array([1, -1, 1, -1]) / 2.0
report("kernel of lazy ring n=4 is the alternating vector", True, np.allclose(W4 @ v, 0))
sig2 = 1.0
for tau in [1e-3, 0.1, 0.49, 0.51, 1.0]:
    PiY = np.linalg.inv(sig2 * W4 @ W4 + tau * np.eye(4))
    form = 0.25 * (1 / (sig2 + tau) - 2 / (sig2 / 4 + tau) + 1 / tau)
    print(f"   tau={tau:6.3f}: Pi_13 = {PiY[0,2]:+.6f} (closed form {form:+.6f}), Pi_12 = {PiY[0,1]:+.6f}, diffusive={all(is_diffusive(PiY)[:2])}")
PiY = np.linalg.inv(W4 @ W4 + 1e-3 * np.eye(4))
report("lazy ring n=4, sigma^2=1, tau=1e-3: Pi_13 > 0 (approx 1/(4 tau)=250)", True, PiY[0, 2] > 0)
report("lazy ring n=4 threshold: diffusive iff tau >= sigma^2/2 (checked at 0.49 and 0.51)", (False, True),
       (all(is_diffusive(np.linalg.inv(W4 @ W4 + 0.49 * np.eye(4)))[:2]),
        all(is_diffusive(np.linalg.inv(W4 @ W4 + 0.51 * np.eye(4)))[:2])))

# odd ring (invertible, near-singular): sign pattern at small tau
for n in [5, 7]:
    Wn = lazy_ring(n)
    PiY = np.linalg.inv(Wn @ Wn + 1e-3 * np.eye(n))
    print(f"   lazy ring n={n}: min |eig| = {np.abs(np.linalg.eigvalsh(Wn)).min():.4f}, max offdiag Pi = {is_diffusive(PiY)[2]:+.3f}, diffusive={all(is_diffusive(PiY)[:2])}")

# ---------- negative controls ----------
n = 4
for name, Wc in [("complete averaging 11^T/n", np.ones((n, n)) / n),
                 ("invertible exchangeable (1-w)I+w11^T/n, w=0.7", 0.3 * np.eye(n) + 0.7 * np.ones((n, n)) / n),
                 ("pair 11^T/2 (kernel (1,-1))", np.ones((2, 2)) / 2)]:
    m = Wc.shape[0]
    good = all(all(is_diffusive(np.linalg.inv(Wc @ Wc + t * np.eye(m)))[:2]) for t in [1e-6, 1e-3, 0.1, 1.0])
    report(f"NEG CONTROL {name}: diffusive at all tau in {{1e-6,1e-3,0.1,1}}", True, good)
t = 1e-3
PiC = np.linalg.inv(np.ones((n, n)) / n + t * np.eye(n))
r, _, _ = contrast(PiC, range(n))
print(f"   complete averaging, tau=1e-3: contrast of the block = {r:.3f} (C1: 1 + sigma^2/tau = {1 + 1/t:.3f})")

# ---------- dynamic embedding: one firm, consensus on information contributions ----------
# e(t+1) = a e(t) + c W D_r^{-1} v(t) + delta(t), a = f(1-k), c = f k n / Lambda^s  (given the world path)
f, k, n = 0.9, 0.3, 4
r_i = np.array([0.5, 1.0, 2.0, 4.0]); Ls = (1 / r_i).sum()
a, c = f * (1 - k), f * k * n / Ls
tau = 1e-3
for name, Wc in [("lazy ring", lazy_ring(4)), ("complete averaging", np.ones((4, 4)) / 4)]:
    Qxi = c ** 2 * Wc @ np.diag(1 / r_i) @ Wc.T + tau * np.eye(4)
    Sc = solve_discrete_lyapunov(a * np.eye(4), Qxi)
    Pc = np.linalg.inv(Sc)
    dd = is_diffusive(Pc)
    print(f"   dynamic firm [{name}], tau=1e-3: Pi^c=\n{np.round(Pc, 3)}\n   diffusive={dd[0] and dd[1]}")
    if name == "lazy ring":
        pred = (1 - a ** 2) / (4 * tau)
        report("dynamic lazy ring: Pi^c_13 > 0, kernel term (1-a^2)/(4 tau) dominates", True, bool(Pc[0, 2] > 0))
        print(f"   Pi^c_13 = {Pc[0,2]:.2f}; kernel-term prediction (1-a^2)/(4 tau) = {pred:.2f}; remainder {Pc[0,2]-pred:+.3f}")
    else:
        report("NEG CONTROL dynamic complete averaging: diffusive", True, bool(dd[0] and dd[1]))

print("ALL CHECKS AS EXPECTED" if ok_all else "SOME CHECK DIFFERED FROM EXPECTATION")
