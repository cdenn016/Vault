"""(i) C7(3), D=1: exhaustive regions inside a window of 6 sites of Z x {A,Z} (12 nodes, 4083 regions), several leak pairs and
    coupling ratios; compare max contrast with the note's bound (constant 2^{2+2/D} = 16 at D=1) -- shows how far the bound is from binding.
(ii) C5(2): discrete witnesses W6a (K3) and W6b (path) recomputed in floating point with my own discrete Lyapunov solve."""
import itertools, numpy as np
from scipy.linalg import solve_discrete_lyapunov

def region_contrast(nodes, eA, eZ, ann, b):
    S = list(nodes); n = len(S); idx = {v: k for k, v in enumerate(S)}
    Min = np.zeros((n, n)); cut = 0.0
    for (t, x) in S:
        k = idx[(t, x)]
        Min[k, k] += eA if t == 'A' else eZ
        nbrs = [('A', x - 1, ann), ('A', x + 1, ann), ('Z', x, b)] if t == 'A' else [('A', x, b)]
        for (t2, x2, w) in nbrs:
            if (t2, x2) in idx:
                Min[k, k] += w; Min[k, idx[(t2, x2)]] -= w
            else:
                cut += w
    xout = (sum(eA if t == 'A' else eZ for t, _ in S) + cut) / n
    Q = np.linalg.qr(np.column_stack([np.ones(n), np.eye(n)[:, 1:]]))[0][:, 1:]
    return np.linalg.eigvalsh(Q.T @ Min @ Q).min() / xout

allnodes = [(t, x) for x in range(6) for t in 'AZ']
for (ann, b) in [(1.0, 0.5), (1.0, 5.0), (1.0, 0.05)]:
    Dmax = max(2 * ann + b, b); vs2 = 2 * ann
    bound = max(3.0, 6 * Dmax / b, 8 * Dmax / ann, 16 * vs2 / ann)
    best = (0, None, None)
    for (eA, eZ) in [(0, 0), (1e-3, 0), (0, 1e-3), (0.1, 0.1), (10, 0), (0, 10), (1e-3, 5)]:
        for k in range(2, 13):
            for S in itertools.combinations(allnodes, k):
                r = region_contrast(S, eA, eZ, ann, b)
                if r > best[0]: best = (r, (eA, eZ), S)
    print(f"a_nn={ann} a_AZ={b}: bound={bound:.1f}  max r over 7 leak pairs x 4083 regions = {best[0]:.4f} at leaks {best[1]}, region {best[2]}")

def disc(W, Qd):
    Sig = solve_discrete_lyapunov(W, np.diag(Qd)); return np.linalg.inv(Sig)
def diffusive(P, tol=1e-11):
    off = P - np.diag(np.diag(P)); return off.max() <= tol * abs(P).max() and P.sum(1).min() >= -tol * abs(P).max()
Wk3 = np.array([[.35, .2, .2, .2], [.2, .35, .2, .2], [.2, .2, .55, 0], [.05, .05, 0, .9]])
print("W6a discrete K3:", {r: (bool(diffusive(disc(Wk3, [1, 1, 1, r * .25]))), round(float(disc(Wk3, [1, 1, 1, r * .25])[2, 3]), 6)) for r in (0, 1, 1.01, 2)})
Wp4 = np.array([[.65, .1, .1, 0, .2], [.1, .75, 0, 0, .2], [.1, 0, .75, .1, 0], [0, 0, .1, .85, 0], [.05, .05, 0, 0, .88]])
print("W6b path: Pi_3z at q_rev, 1.01 q_rev:", disc(Wp4, [1, 1, 1, 1, .25])[3, 4], disc(Wp4, [1, 1, 1, 1, .2525])[3, 4])
