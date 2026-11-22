"""Independent check of C2 (conj_agy_synchronous.md).
(A) n=4 binary, multi-dimensional Gaussian slots and discrete slots: positive association of P_sync over all
    nontrivial monotone Boolean functions on {0,1}^4 (up-set indicators generate the monotone cone).
    Control: the same test applied to the group posterior P_C must FAIL when redundancy is present.
(B) Antitone log-odds step computed from first principles.
(C) Scope probe: with the null-policy LABEL of one member exchanged, a binary P_sync IS a redundant
    group posterior with product habits and gamma_C>0 (binary chain 0-1-2).
(D) C2(3): n=4 non-binary bipartite factorization; planted control (within-block redundancy).
"""
from itertools import product
import numpy as np

rng = np.random.default_rng(5)


def sync_T(G, E, gamma):
    shape = G.shape
    n = G.ndim
    lp = -gamma * G
    for i in range(n):
        sh = [1] * n
        sh[i] = shape[i]
        lp = lp + np.log(E[i]).reshape(sh)
    P = np.exp(lp - lp.max())
    P /= P.sum()
    K = [P / P.sum(axis=i, keepdims=True) for i in range(n)]
    states = list(product(*[range(m) for m in shape]))
    T = np.zeros((len(states),) * 2)
    for a, s in enumerate(states):
        for b, t in enumerate(states):
            pr = 1.0
            for i in range(n):
                u = list(s)
                u[i] = t[i]
                pr *= K[i][tuple(u)]
            T[a, b] = pr
    return T, P, K


def stat(T):
    N = T.shape[0]
    A = np.vstack([T.T - np.eye(N), np.ones(N)])
    b = np.zeros(N + 1)
    b[-1] = 1
    return np.linalg.lstsq(A, b, rcond=None)[0]


def gauss_G(Hs, shape, psi):
    d = [h for h in Hs[0] if h is not None][0].shape[1]
    G = np.zeros(shape)
    for s in product(*[range(m) for m in shape]):
        prec = np.eye(d)
        for i, a in enumerate(s):
            if a > 0:
                prec += Hs[i][a].T @ Hs[i][a]
        G[s] = -0.5 * np.linalg.slogdet(prec)[1] + sum(psi[i][a] for i, a in enumerate(s))
    return G


# monotone Boolean functions on {0,1}^4
pts = list(product([0, 1], repeat=4))
le = [[all(a <= b for a, b in zip(x, y)) for y in pts] for x in pts]
mono = []
for bits in range(1, 2 ** 16 - 1):
    f = [(bits >> k) & 1 for k in range(16)]
    ok = True
    for i in range(16):
        if f[i]:
            for j in range(16):
                if le[i][j] and not f[j]:
                    ok = False
                    break
        if not ok:
            break
    if ok:
        mono.append(np.array(f, float))
mono = np.array(mono)
print(f"(A) nontrivial monotone Boolean functions on {{0,1}}^4: {len(mono)} (Dedekind M(4)-2 = 166)")
assert len(mono) == 166


def min_cov(p):
    m = mono @ p
    C = (mono * p) @ mono.T - np.outer(m, m)
    return C.min()


min_sync, min_PC_red = 1e9, 1e9
viol_PC = 0
ntr = 40
for tr in range(ntr):
    d = int(rng.integers(1, 5))
    k = int(rng.integers(1, 3))  # slot dimension per member
    Hs = [[None, rng.normal(0, 1.5, size=(k, d))] for _ in range(4)]
    psi = [[0.0, float(rng.uniform(-1.5, 1.5))] for _ in range(4)]
    E = [np.array([e, 1 - e]) for e in rng.uniform(0.1, 0.9, size=4)]
    gamma = float(rng.uniform(0.2, 6.0))
    G = gauss_G(Hs, (2, 2, 2, 2), psi)
    T, P, K = sync_T(G, E, gamma)
    ps = stat(T)
    min_sync = min(min_sync, min_cov(ps))
    c = min_cov(P.ravel())
    min_PC_red = min(min_PC_red, c)
    viol_PC += (c < -1e-9)
print(f"  {ntr} random Gaussian n=4 binary models: min Cov_Psync(f,g) over 166^2 pairs = {min_sync:+.3e}")
print(f"  control: same test on P_C: min Cov = {min_PC_red:+.3e}; P_C violates positive association in {viol_PC}/{ntr} models")
assert min_sync > -1e-13 and viol_PC > ntr // 2

# (B) antitone conditional: K_i(1|y) <= K_i(1|x) for x<=y  (first principles from K)
worst = -1e9
for tr in range(20):
    d = int(rng.integers(1, 4))
    Hs = [[None, rng.normal(0, 1.5, size=(1, d))] for _ in range(4)]
    psi = [[0.0, float(rng.uniform(-1, 1))] for _ in range(4)]
    E = [np.array([e, 1 - e]) for e in rng.uniform(0.1, 0.9, size=4)]
    G = gauss_G(Hs, (2, 2, 2, 2), psi)
    T, P, K = sync_T(G, E, 1.7)
    for i in range(4):
        for x in pts:
            for y in pts:
                if all(a <= b for a, b in zip(x, y)):
                    xi = list(x); xi[i] = 1
                    yi = list(y); yi[i] = 1
                    worst = max(worst, K[i][tuple(yi)] - K[i][tuple(xi)])
print(f"(B) max over x<=y of K_i(1|y)-K_i(1|x) = {worst:+.2e}  (must be <= 0)")
assert worst < 1e-14

# (C) scope probe: binary chain 0-1-2. eta=(eta_a,eta_b); m0 reads eta_a, m2 reads eta_b, m1 reads both in
# two separate scalar slots. Pairwise redundancies I_01>0, I_12>0, I_02=0.
print("(C) scope probe: null label of member 0 exchanged")
h0, h1a, h1b, h2 = 1.3, 1.1, 0.9, 1.6
Hs = [[None, np.array([[h0, 0.0]])],
      [None, np.array([[h1a, 0.0], [0.0, h1b]])],
      [None, np.array([[0.0, h2]])]]
psi = [[0.0, 0.3], [0.0, -0.2], [0.0, 0.1]]
E = [np.array([0.4, 0.6]), np.array([0.5, 0.5]), np.array([0.35, 0.65])]
gamma = 2.0
G = gauss_G(Hs, (2, 2, 2), psi)
T, P, K = sync_T(G, E, gamma)
ps = stat(T).reshape(2, 2, 2)
L = np.log(ps)
J02_c0 = L[1, 0, 1] - L[1, 0, 0] - L[0, 0, 1] + L[0, 0, 0]
J02_c1 = L[1, 1, 1] - L[1, 1, 0] - L[0, 1, 1] + L[0, 1, 0]
J01 = L[1, 1, 0] - L[1, 0, 0] - L[0, 1, 0] + L[0, 0, 0]
J12 = L[0, 1, 1] - L[0, 1, 0] - L[0, 0, 1] + L[0, 0, 0]
print(f"  P_sync log odds ratios through the original nulls: (0,2|c=0)={J02_c0:+.6f} (0,2|c=1)={J02_c1:+.6f} (0,1)={J01:+.2e} (1,2)={J12:+.2e}")
# Any group model with the ORIGINAL nulls has all such log odds ratios <= 0 (prop:agy-performative-sign): excluded.
# Relabeled model: member 0's null policy is the original policy 1. New coordinate x0' = 1 - x0.
gC = 0.7
Jt = J02_c0                      # positive coupling between x0 and x2  ==  negative coupling -Jt between x0' and x2
Itil = Jt / gC                   # required redundancy
R = np.exp(2 * Itil)
s = (R - 1) + np.sqrt((R - 1) ** 2 + (R - 1))   # SNR with 0.5*ln((1+s)^2/(1+2s)) = Itil
Ht = [[None, np.array([[np.sqrt(s)]])],         # member 0 (relabeled): active policy reads eta~
      [None, np.array([[0.0]])],                # member 1: a slot carrying no information about eta~
      [None, np.array([[np.sqrt(s)]])]]         # member 2: policy 1 reads eta~
Gt = gauss_G(Ht, (2, 2, 2), [[0.0, 0.0]] * 3)   # in relabeled coordinates (x0', x1, x2)
red = Gt[1, 0, 1] - Gt[1, 0, 0] - Gt[0, 0, 1] + Gt[0, 0, 0]
ps_rel = ps[::-1, :, :]                          # P_sync in relabeled coordinates
# product habits: fit single-member terms exactly (closed form from marginals of the tilted law)
Q = ps_rel * np.exp(gC * Gt)                     # should be a product law if the claim holds
m = [Q.sum(axis=tuple(j for j in range(3) if j != i)) / Q.sum() for i in range(3)]
Et = [mi / mi.sum() for mi in m]
lp = -gC * Gt + np.log(Et[0])[:, None, None] + np.log(Et[1])[None, :, None] + np.log(Et[2])[None, None, :]
Pt = np.exp(lp); Pt /= Pt.sum()
print(f"  relabeled group model: gamma_C={gC}, redundancy I~(member0 active; member2 policy1)={red:.6f}>0, habits full support min={min(e.min() for e in Et):.3f}")
print(f"  TV(P_sync, relabeled redundant group posterior) = {0.5 * np.abs(Pt - ps_rel).sum():.2e}")
# control: without relabeling the same construction cannot fit
Q2 = ps * np.exp(gC * Gt)
m2 = [Q2.sum(axis=tuple(j for j in range(3) if j != i)) / Q2.sum() for i in range(3)]
lp2 = -gC * Gt + np.log(m2[0])[:, None, None] + np.log(m2[1])[None, :, None] + np.log(m2[2])[None, None, :]
P2 = np.exp(lp2); P2 /= P2.sum()
print(f"  control (original null labels, same slots): TV = {0.5 * np.abs(P2 - ps).sum():.2e}")

# (D) C2(3), n=4, shapes (3,2,3,2), U={0,1}, W={2,3}; coordinates eta_{uw}, u in U, w in W
print("(D) bipartite factorization, n=4 non-binary")
shape = (3, 2, 3, 2)
d = 4
cidx = {(0, 2): 0, (0, 3): 1, (1, 2): 2, (1, 3): 3}


def build(extra_within=False):
    Hs = []
    for i in range(4):
        pols = [None]
        for a in range(1, shape[i]):
            rows = []
            for (u, w), c in cidx.items():
                if i in (u, w):
                    r = np.zeros(d)
                    r[c] = rng.uniform(0.6, 2.0)
                    rows.append(r)          # separate scalar slot per coordinate => no collider
            if extra_within and i in (0, 1):
                r = np.zeros(d)
                r[0] = 1.0                  # members 0 and 1 (same block) both read coordinate 0 directly
                rows.append(r)
            pols.append(np.array(rows))
        Hs.append(pols)
    return Hs


psi = [[0.0] + list(rng.uniform(-0.5, 0.5, size=shape[i] - 1)) for i in range(4)]
E = [rng.dirichlet(np.ones(shape[i]) * 3) for i in range(4)]
for label, extra in [("bipartite (no within-block redundancy)", False), ("planted within-block redundancy", True)]:
    G = gauss_G(build(extra), shape, psi)
    T, P, K = sync_T(G, E, 1.5)
    ps = stat(T).reshape(shape)
    muU = ps.sum(axis=(2, 3))
    muW = ps.sum(axis=(0, 1))
    fact = np.einsum('ab,cd->abcd', muU, muW)
    full = np.einsum('a,b,c,d->abcd', ps.sum(axis=(1, 2, 3)), ps.sum(axis=(0, 2, 3)), ps.sum(axis=(0, 1, 3)), ps.sum(axis=(0, 1, 2)))
    print(f"  {label}: TV(P_sync, mu_U x mu_W)={0.5 * np.abs(ps - fact).sum():.2e}  TV(P_sync, full product)={0.5 * np.abs(ps - full).sum():.2e}  TV(P_sync,P_C)={0.5 * np.abs(ps - P).sum():.2e}")
print("done")
