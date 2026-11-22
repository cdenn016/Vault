"""Falsification search for the pairwise-positivity conjecture (P+):
A >= 0 within components, no communication or common ancestor across C1, C2,
one-sign loadings b >= 0 on one scalar conditioned world coordinate
=> Pi^c_ij > 0 for every i in C1, j in C2 with b_i, b_j > 0.

EXPECTATION declared before running: unknown (exploratory); the proved part
(aggregated cross covariance < 0, Pi^c has some positive offdiag entry) must hold in every draw.
"""
import numpy as np
from scipy.linalg import solve_discrete_are, solve_discrete_lyapunov

rng = np.random.default_rng(99)


def sigma_c_rts(A, Q, b, q):
    N = A.shape[0]
    bb = b.reshape(N, 1)
    Pp = solve_discrete_are(A.T, bb, Q, np.array([[q]]))
    S = (bb.T @ Pp @ bb).item() + q
    Pf = Pp - Pp @ bb @ bb.T @ Pp / S
    J = Pf @ A.T @ np.linalg.inv(Pp)
    Ps = solve_discrete_lyapunov(J, Pf - J @ Pp @ J.T)
    return 0.5 * (Ps + Ps.T)


def comp(n, kind):
    if kind == "dense":
        X = rng.uniform(0, 1, (n, n))
    elif kind == "sparse":
        X = rng.uniform(0, 1, (n, n)) * (rng.uniform(size=(n, n)) < 0.4)
        X += np.diag(rng.uniform(0, 0.2, n))
    elif kind == "bipartite":   # near-bipartite: strong off-diagonal pairs, weak self weights
        X = np.zeros((n, n))
        for i in range(n):
            j = (i + 1) % n
            X[i, j] = rng.uniform(0.5, 1); X[j, i] = rng.uniform(0.5, 1)
        X += np.diag(rng.uniform(0, 0.05, n))
    elif kind == "chain":       # directed relay chain 0 -> 1 -> ... (listener reads previous)
        X = np.diag(rng.uniform(0, 0.5, n))
        for i in range(1, n):
            X[i, i - 1] = rng.uniform(0.3, 1)
    scale = max(np.abs(np.linalg.eigvals(X)).max(), 0.3 * np.linalg.norm(X, 2), 1e-3)
    A = X / scale * rng.uniform(0.3, 0.97)
    Qd = np.exp(rng.uniform(np.log(0.02), np.log(5.0), n))
    return A, Qd


stats = {}
worst = (np.inf, None)
for trial in range(3000):
    kinds = rng.choice(["dense", "sparse", "bipartite", "chain"], 3)
    n1, n2, n3 = rng.integers(1, 5), rng.integers(1, 5), rng.integers(0, 3)
    comps = [comp(n1, kinds[0]), comp(n2, kinds[1])] + ([comp(n3, kinds[2])] if n3 > 0 else [])
    N = sum(c[0].shape[0] for c in comps)
    A = np.zeros((N, N)); Qd = np.zeros(N); bl = []; i = 0
    for Ac, Qc in comps:
        k = Ac.shape[0]; A[i:i + k, i:i + k] = Ac; Qd[i:i + k] = Qc; bl.append(list(range(i, i + k))); i += k
    b = rng.uniform(0.01, 1.0, N) * (rng.uniform(size=N) < 0.75)
    if b[bl[0]].sum() == 0 or b[bl[1]].sum() == 0:
        continue
    q = np.exp(rng.uniform(np.log(0.01), np.log(10.0)))
    try:
        Sc = sigma_c_rts(A, np.diag(Qd), b, q)
        Pc = np.linalg.inv(Sc)
    except Exception:
        continue
    key = tuple(sorted(kinds[:2]))
    s = stats.setdefault(key, [0, 0, 0, 0, 0, 0])
    s[0] += 1
    agg = b[bl[0]] @ Sc[np.ix_(bl[0], bl[1])] @ b[bl[1]]
    s[1] += agg < 0
    off = Pc - np.diag(np.diag(Pc))
    s[2] += off.max() > 0
    cr = Pc[np.ix_(bl[0], bl[1])]
    act = np.outer(b[bl[0]] > 0, b[bl[1]] > 0)
    mn = cr[act].min() / np.sqrt(np.outer(np.diag(Pc)[bl[0]], np.diag(Pc)[bl[1]])[act]).max()
    if (cr[act] <= 0).any():
        s[3] += 1
    s[4] += cr.max() <= 0
    s[5] += (b[bl[0]] @ cr @ b[bl[1]]) <= 0
    if mn < worst[0]:
        worst = (mn, (A, Qd, b, q, bl, Pc))

tot = np.array([0, 0, 0, 0, 0, 0])
for k, v in sorted(stats.items()):
    print(f"kinds {k}: draws {v[0]}, agg<0 {v[1]}, Pi pos offdiag {v[2]}, acting cross Pi<=0 {v[3]}, cross block has no pos entry {v[4]}, b1^T Pi12 b2<=0 {v[5]}")
    tot += np.array(v)
print("TOTAL draws, agg<0, Pi pos offdiag, acting-cross-nonpositive, cross-block-no-pos, b-weighted-cross-Pi<=0:", tot.tolist())
print("proved part holds in every draw:", tot[1] == tot[0] and tot[2] == tot[0])
print(f"smallest normalized acting cross entry Pi_ij/sqrt(Pi_ii Pi_jj) (max-normalizer): {worst[0]:.3e}")
if worst[0] <= 0:
    A, Qd, b, q, bl, Pc = worst[1]
    np.set_printoptions(precision=4, suppress=True)
    print("counterexample to (P+):\nA=\n", A, "\nQ=", Qd, "\nb=", b, "\nq=", q, "\nblocks", bl, "\nPi^c=\n", Pc)
