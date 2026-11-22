"""(a) high-precision resolution of rho(x)-1 = W(x)/(C_out w_path(x)) - 1 at m=2;
(b) path-tree ratio identity in the LG model for m=3,4,5 (path from one-hot tuple enumeration);
(c) m=3 truncated chain (V0 plus all hypercube neighbours of V0) stationary law, float64 GTH. Own code."""
import time
import numpy as np
import mpmath as mp
from gear import Model, gth, tree_weight, build_graph

t0 = time.time()
m, n = 2, 7
h, Delta = mp.mpf("0.9"), mp.mpf("0.1")


def onehot_path(mm):
    nn, sizes, offs, edges, motor = build_graph(mm)
    walls = {frozenset(e) for e, k in edges.items() if k == "wall"}
    adjs = {frozenset(e) for e, k in edges.items() if k == "adj"}
    tuples = []

    def rec(g, cur):
        if g == mm:
            tuples.append(tuple(cur))
            return
        for r in range(sizes[g]):
            x = offs[g] + r
            if not cur or frozenset((cur[-1], x)) not in walls:
                rec(g + 1, cur + [x])

    rec(0, [])
    tset = set(tuples)
    nb = {t: [] for t in tuples}
    for t in tuples:
        for g in range(mm):
            for r in range(sizes[g]):
                x = offs[g] + r
                if frozenset((t[g], x)) in adjs:
                    t2 = t[:g] + (x,) + t[g + 1:]
                    if t2 in tset:
                        nb[t].append(t2)
    ends = [t for t in tuples if len(nb[t]) == 1]
    assert len(ends) == 2 and max(len(v) for v in nb.values()) == 2
    path = [ends[0]]
    prev = None
    while True:
        nx = [u for u in nb[path[-1]] if u != prev]
        if not nx:
            break
        prev = path[-1]
        path.append(nx[0])
    assert len(path) == len(tuples)
    mot = set(motor)

    def steps(pp):
        sc = [0]
        for a, c in zip(pp[:-1], pp[1:]):
            g = [i for i in range(mm) if a[i] != c[i]][0]
            sc.append(sc[-1] + (1 if (a[g], c[g]) in mot else (-1 if (c[g], a[g]) in mot else 0)))
        return sc

    if steps(path)[-1] < 0:
        path = path[::-1]
    return nn, path, steps(path)


print("== (a) rho(x)-1 at m=2 with enough digits to resolve it ==")
for lam, gamma, dps in [(1, 40, 60), (1, 120, 140), (4, 120, 140), (4, 600, 520), (1, 2000, 1500)]:
    mp.mp.dps = dps
    delta = mp.mpf(lam) / (4 * mp.mpf(gamma))
    M = Model(m, delta, [-h] * n)
    nn, tpath, sc = onehot_path(m)
    Pst = [sum(1 << x for x in t) for t in tpath]
    path = []
    for k, a in enumerate(Pst):
        path.append(a)
        if k + 1 < len(Pst):
            path.append(a | Pst[k + 1])
    q = M.rates(gamma)
    V1 = [s for s in range(M.N) if s not in set(path)]
    _, piv, red = gth(q, path + V1, n_keep=len(path))
    rho = []
    for k in range(0, len(path), 2):
        wt = tree_weight(red, list(range(len(path))), k)
        w = mp.mpf(1)
        for j, a in enumerate(path):
            if j != k:
                w *= q[a][path[j + 1] if j < k else path[j - 1]]
        rho.append(wt / w - 1)
    bound = (2 * n) ** len(path) * mp.exp(-mp.mpf(gamma) * (Delta - (6 * 2 ** m - 8) * delta))
    print(f" lam={lam} gamma={gamma}: rho-1 in [{mp.nstr(min(rho), 4)}, {mp.nstr(max(rho), 4)}]  all>0: {min(rho) > 0}  "
          f"proved bound {mp.nstr(bound, 4)}  holds: {max(rho) <= bound}  -ln(max(rho-1))/gamma={mp.nstr(-mp.log(max(rho)) / gamma, 4)}  [{time.time() - t0:.1f}s]")

print("\n== (b) path-tree ratio identity ln[w(v_L)/w(v_0)] = 2*lam for m=3,4,5 (exact LG transition probabilities) ==")
mp.mp.dps = 40
for mm in [3, 4, 5]:
    nn, tpath, sc = onehot_path(mm)
    lam, gamma = mp.mpf(3), mp.mpf(200)
    delta = lam / (2 ** mm * gamma)
    M = Model(mm, delta, [-h] * nn)

    def T(a, bb):
        u = (a ^ bb).bit_length() - 1
        d = M.dG(u, a)
        return 1 / (nn * (1 + mp.exp(gamma * d))) if not (a >> u) & 1 else 1 / (nn * (1 + mp.exp(-gamma * d)))

    Pst = [sum(1 << x for x in t) for t in tpath]
    lr = mp.mpf(0)
    worst = mp.mpf(0)
    for k in range(len(Pst) - 1):
        a, c = Pst[k], Pst[k + 1]
        u = a | c
        lr += mp.log(T(a, u) * T(u, c) / (T(c, u) * T(u, a)))
        worst = max(worst, abs(lr - 2 * lam * sc[k + 1] / 2 ** mm))
    # Phi constant on P_m and R-based sigma on the motor only
    PhiP = [M.Phi(a) for a in Pst]
    print(f" m={mm} n={nn} |P|={len(Pst)} s(v_L)={sc[-1]} (2^m={2 ** mm}) gamma*sigma_max={mp.nstr(gamma * delta, 5)}: "
          f"ln[w(v_L)/w(v_0)]={mp.nstr(lr, 15)} (2 lam={mp.nstr(2 * lam, 3)}, = 2^(m+1)*gamma*sigma_max)  max dev along path={mp.nstr(worst, 3)}  "
          f"osc Phi on P_m={mp.nstr(max(PhiP) - min(PhiP), 3)}  [{time.time() - t0:.1f}s]")

print("\n== (c) m=3 truncated chain: V0 and all hypercube neighbours of V0 (float64, subtraction-free) ==")
mm = 3
nn, tpath, sc = onehot_path(mm)
Pst = [sum(1 << x for x in t) for t in tpath]
V0 = []
for k, a in enumerate(Pst):
    V0.append(a)
    if k + 1 < len(Pst):
        V0.append(a | Pst[k + 1])
states = list(V0)
seen = set(V0)
for a in V0:
    for i in range(nn):
        bb = a ^ (1 << i)
        if bb not in seen:
            seen.add(bb)
            states.append(bb)
idx = {s: k for k, s in enumerate(states)}
for lam, gamma in [(1.0, 60.0), (4.0, 60.0), (4.0, 100.0)]:
    delta = lam / (2 ** mm * gamma)
    mp.mp.dps = 20
    M = Model(mm, delta, [-h] * nn)
    N = len(states)
    Q = np.zeros((N, N))
    for s in states:
        for i in range(nn):
            t = s ^ (1 << i)
            if t in idx:
                d = float(M.dG(i, s))
                x = gamma * d if not (s >> i) & 1 else -gamma * d
                Q[idx[s], idx[t]] = 1.0 / (nn * (1.0 + np.exp(min(x, 700.0))))
    A = Q.copy()
    for k in range(N - 1, 0, -1):
        sk = A[k, :k].sum()
        A[:k, k] /= sk
        A[:k, :k] += np.outer(A[:k, k], A[k, :k])
    p = np.zeros(N)
    p[0] = 1.0
    for k in range(1, N):
        p[k] = p[:k] @ A[:k, k]
    p /= p.sum()
    pP = np.array([p[idx[a]] for a in Pst])
    mu = np.exp(2 * lam * np.array(sc) / 2 ** mm)
    mu /= mu.sum()
    print(f" lam={lam} gamma={gamma} gamma*sigma_max={lam / 2 ** mm:.4f} states={N}: mass(P_3)={pP.sum():.6f}  ln[P(v_L)/P(v_0)]={np.log(pP[-1] / pP[0]):.6f} (2 lam={2 * lam})  "
          f"TV(P|P_3, mu_lam)={0.5 * np.abs(pP / pP.sum() - mu).sum():.2e}  TV(mu_lam, Unif)={0.5 * np.abs(mu - 1 / len(mu)).sum():.4f}  [{time.time() - t0:.1f}s]")
