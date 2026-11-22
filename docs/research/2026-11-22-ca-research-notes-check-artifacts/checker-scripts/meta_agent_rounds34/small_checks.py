"""Small exact checks with planted-error controls: C16, C17b (static instances), C20(iii)."""
import itertools
import numpy as np
rng = np.random.default_rng(11)

# ---- C16: index of a deterministic joint policy
def index(G, E, k, gammas):
    def lse(g):
        a = np.log(E) - g * G; m = a.max(); return m + np.log(np.sum(np.exp(a - m)))
    f = np.array([np.log(E[k]) - g * G[k] - lse(g) for g in gammas])
    return 1 - (-f.max()) / (-np.log(E[k])), gammas[int(f.argmax())]
gam = np.concatenate([[0.0], np.logspace(-4, 6, 500)])
nb = viol_b = neg_pos = 0; amin = 1.0
for _ in range(400):
    m = rng.integers(3, 8); G = rng.normal(size=m); E = rng.dirichlet(np.ones(m))
    mean = E @ G
    for k in range(m):
        idx, g_at = index(G, E, k, gam)
        if G[k] >= mean:                 # case (b): index must be 0, attained at gamma = 0
            nb += 1; viol_b += (idx > 1e-12)
        else:                            # control: strict inequality the other way must give index > 0
            neg_pos += (idx > 1e-9)
    k = int(np.argmin(G)); amin = min(amin, index(G, E, k, gam)[0])   # case (a)
print("C16(b): %d cases, violations %d; control G(pi*)<E_E[G]: index>0 in %d cases; C16(a): min index at gamma<=1e6: %.6f"
      % (nb, viol_b, neg_pos, amin))

# ---- C17b on static instances: z_i = common + private, ytil = sum_r kappa_r^T z + noise
def contrast_block(Pi):
    n = Pi.shape[0]; phi = np.ones(n) / np.sqrt(n)
    Q, _ = np.linalg.qr(np.column_stack([np.ones(n), np.eye(n)[:, :n - 1]])); B = Q[:, 1:]
    return np.linalg.eigvalsh(B.T @ Pi @ B).min() / (phi @ Pi @ phi)
def diffusive(Pi):
    off = Pi - np.diag(np.diag(Pi)); return off.max() <= 1e-10 and Pi.sum(1).min() >= -1e-10
def trial(n, nload):
    a, b, v = rng.uniform(0.3, 2), rng.uniform(0, 2), rng.uniform(0.1, 2)
    Se = a * np.eye(n) + b * np.ones((n, n))
    Kp = rng.normal(size=(nload, n))                 # loading patterns kappa^(r)
    Sy = Kp @ Se @ Kp.T + v * np.eye(nload)
    Sc = Se - Se @ Kp.T @ np.linalg.solve(Sy, Kp @ Se)
    Pc, Pe = np.linalg.inv(Sc), np.linalg.inv(Se)
    if not (diffusive(Pc) and diffusive(Pe)): return None
    return contrast_block(Pc) / contrast_block(Pe) - 1
for n, nload, tag in ((3, 1, "dim W<=1<n-1 (hypotheses hold)"), (4, 2, "dim W<=2<n-1 (hypotheses hold)"),
                      (3, 2, "dim W=2=n-1 (O3 violated, control)"), (2, 1, "n=2, dim W=1=n-1 (O3 violated, control)")):
    res = [t for t in (trial(n, nload) for _ in range(6000)) if t is not None]
    print("C17b static n=%d loads=%d %-40s diffusive draws %4d, r>r_eff in %4d, max rel excess %.3e"
          % (n, nload, tag, len(res), sum(t > 1e-9 for t in res), max(res) if res else float('nan')))

# ---- C20(iii): substitute selector for a source and an exchangeable audience of four
def brute(Isa, Iaa):
    I = np.full((5, 5), Iaa); I[0, :] = I[:, 0] = Isa
    best = 0
    for blk in itertools.combinations(range(5), 2):
        oth = [k for k in range(5) if k not in blk]
        w = [I[blk]] + [I[i, j] for i, j in itertools.combinations(oth, 2)]
        bt = [I[i, j] for i in blk for j in oth]
        best = max(best, np.mean(w) / np.mean(bt))
    return best
err = wrong = mx = 0
for _ in range(2000):
    Isa, Iaa = rng.exponential(1.0, 2) * rng.choice([1e-3, 1, 30], 2)
    cf = max((Isa + 3 * Iaa) / (2 * (Isa + Iaa)), 3 * (Isa + Iaa) / (2 * Isa + 4 * Iaa))
    planted = max((Isa + 3 * Iaa) / (2 * (Isa + Iaa)), 3 * (Isa + Iaa) / (4 * Isa + 2 * Iaa))
    b = brute(Isa, Iaa)
    err = max(err, abs(cf - b)); wrong = max(wrong, abs(planted - b)); mx = max(mx, b)
print("C20(iii): max |closed form - enumeration| %.2e; planted-wrong formula error %.2f; max ratio %.6f (bound 1.5)" % (err, wrong, mx))
