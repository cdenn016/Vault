"""Independent checks for open_prv_minimal (reviewer script). Exact integer / combinatorial only.

B1  Block-cut channel protocol re-implemented from the note's specification with exact integer
    "pairs" (multiplicity vectors over [prior, item_1, item_2, ...]); random schedules; planted errors.
B2  C2 light-cone schedule: causal independence checked on full local views (hash-consed histories,
    sender-side updates and global timestamps included), plus the D-set formulas and grid membership.
B3  C3 schedules: view independence for r != u; failure of the written async schedule when r = u;
    clock variant with gate vertices.
B4  C3 linear-algebra lemma on admissible subspace families, with an inadmissible control.
B5  C4 graph inequalities on every 2-connected graph with at most 7 vertices (graph atlas).
"""
import itertools
import random
import numpy as np
import networkx as nx
from sympy import Matrix

random.seed(20261122)

# ----------------------------------------------------------------------------- B1
print("=== B1: block-cut channel protocol, exact integer simulation ===")


def run_block_cut(G, n_events, max_obs, bug=None, seed=0):
    rnd = random.Random(seed)
    nodes = list(G.nodes())
    blocks = [frozenset(b) for b in nx.biconnected_components(G)]
    big = [B for B in blocks if len(B) >= 3]
    blk_of_edge = {}
    for B in blocks:
        for u, v in itertools.combinations(B, 2):
            if G.has_edge(u, v):
                blk_of_edge[frozenset((u, v))] = B
    N = max_obs + 1
    pi0 = np.zeros(N, dtype=np.int64); pi0[0] = 1
    s = {v: pi0.copy() for v in nodes}
    link = {e: pi0.copy() for e, B in blk_of_edge.items() if len(B) == 2}
    E = {(B, v, w): np.zeros(N, dtype=np.int64) for B in big for v in B for w in B if w != v}
    c = {(B, v, w): 0 for B in big for v in B for w in B}
    D = {v: set() for v in nodes}
    nobs = 0
    edges = list(G.edges())

    def e_self(B, v):
        return s[v] - pi0 - sum((E[(B, v, w)] for w in B if w != v), np.zeros(N, dtype=np.int64))

    for _ in range(n_events):
        if nobs < max_obs and rnd.random() < 0.3:
            v = rnd.choice(nodes)
            nobs += 1
            D[v].add(nobs)
            s[v][nobs] += 1
            for B in big:
                if v in B:
                    c[(B, v, v)] += 1
        else:
            u, v = rnd.choice(edges)
            if rnd.random() < 0.5:
                u, v = v, u
            B = blk_of_edge[frozenset((u, v))]
            D[v] |= D[u]
            if len(B) == 2:
                e = frozenset((u, v))
                s[v] = s[v] + s[u] - link[e]
                link[e] = s[u].copy()
                if bug != "no_bridge_bump":
                    for B2 in big:
                        if v in B2:
                            c[(B2, v, v)] += 1
            else:
                msg = {w: (c[(B, u, w)], e_self(B, u) if w == u else E[(B, u, w)].copy()) for w in B}
                changed = False
                for w in B:
                    if w == v:
                        continue
                    cw, Ew = msg[w]
                    if cw > c[(B, v, w)]:
                        s[v] = s[v] - E[(B, v, w)] + Ew
                        E[(B, v, w)] = Ew
                        c[(B, v, w)] = cw
                        changed = True
                if changed and bug != "no_cut_bump":
                    for B2 in big:
                        if v in B2 and B2 != B:
                            c[(B2, v, v)] += 1
        for x in nodes:
            want = pi0.copy()
            for it in D[x]:
                want[it] = 1
            if not np.array_equal(s[x], want):
                return False
    return True


def windmill(m):
    G = nx.Graph()
    for i in range(m):
        G.add_edges_from([(0, 2 * i + 1), (0, 2 * i + 2), (2 * i + 1, 2 * i + 2)])
    return G


def two_k4_bridge_c5():
    G = nx.complete_graph(4)
    G.add_edges_from([(3, 4), (3, 5), (3, 6), (4, 5), (4, 6), (5, 6)])       # second K4 sharing vertex 3
    G.add_edge(6, 7)                                                       # bridge
    G.add_edges_from([(7, 8), (8, 9), (9, 10), (10, 11), (11, 7)])         # C5
    G.add_edges_from([(9, 12), (12, 13)])                                  # pendant path
    return G


def theta_with_tail():
    G = nx.Graph([(0, 1), (1, 2), (2, 5), (0, 3), (3, 5), (0, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 6)])
    return G


suite = [("path_5", nx.path_graph(5)), ("C_6", nx.cycle_graph(6)), ("K_5", nx.complete_graph(5)),
         ("windmill_4", windmill(4)), ("two_K4+bridge+C5+tail", two_k4_bridge_c5()),
         ("theta+tail+triangle", theta_with_tail()), ("petersen", nx.petersen_graph()),
         ("K_{2,4}", nx.complete_bipartite_graph(2, 4))]
for name, G in suite:
    ok = all(run_block_cut(G, 1500, 250, seed=sd) for sd in range(4))
    print(f"  {name:24s} n={G.number_of_nodes():2d} exact after every event (4 schedules x 1500 events): {ok}")
    assert ok
b1 = any(not run_block_cut(two_k4_bridge_c5(), 1500, 250, bug="no_cut_bump", seed=sd) for sd in range(4))
b2 = any(not run_block_cut(two_k4_bridge_c5(), 1500, 250, bug="no_bridge_bump", seed=sd) for sd in range(4))
b3 = any(not run_block_cut(windmill(4), 1500, 250, bug="no_cut_bump", seed=sd) for sd in range(4))
print(f"  planted errors detected: no_cut_bump={b1}, no_bridge_bump={b2}, no_cut_bump on windmill={b3}")
assert b1 and b2 and b3

# ----------------------------------------------------------------------------- views
_intern = {}


def iv(t):
    """Hash-cons a nested tuple to an int id (structural equality == id equality)."""
    if t not in _intern:
        _intern[t] = len(_intern)
    return _intern[t]


class Net:
    def __init__(self, nodes, clock):
        self.view = {v: iv(("init", v)) for v in nodes}   # identifiers allowed
        self.D = {v: frozenset() for v in nodes}
        self.clock = clock
        self.time = None

    def stamp(self):
        return self.time if self.clock else None

    def obs(self, v, key):
        self.view[v] = iv(("obs", self.view[v], key, self.stamp()))
        self.D[v] = self.D[v] | {key}

    def report(self, u, v):
        vu = self.view[u]
        self.view[v] = iv(("recv", self.view[v], u, vu, self.stamp()))
        self.view[u] = iv(("sent", vu, v, self.stamp()))     # sender may update its state
        self.D[v] = self.D[v] | self.D[u]


# ----------------------------------------------------------------------------- B2
print("=== B2: C2 light-cone schedule, full-view causal independence (global clock on) ===")


def light_cone(k, T0, T1, rounds):
    net = Net(range(k + 2), clock=True)
    for t in range(1, rounds + 1):
        net.time = (t, 1)
        for s in range(1, k + 1):
            net.obs(s, (s, t))
        net.time = (t, 2)
        if t <= T0:
            net.report(1, 0)
        if t <= T1:
            net.report(k, k + 1)
        net.time = (t, 3)
        for s in range(k - 1, 0, -1):
            net.report(s, s + 1)
        net.time = (t, 4)
        for s in range(2, k + 1):
            net.report(s, s - 1)
    return net


for ell in [6, 7, 8, 9, 10, 12]:
    k = ell - 2
    m = k // 2
    T0s = [2 * (m + i) - 1 for i in range(1, m + 1)]
    T1s = [k + 2 * (j - 1) for j in range(1, m + 1)]
    assert all(k <= T <= 2 * k - 1 for T in T0s + T1s)
    v0, vk1, sets_ok, grid_ok = {}, {}, True, True
    for i, T0 in enumerate(T0s, 1):
        for j, T1 in enumerate(T1s, 1):
            net = light_cone(k, T0, T1, 2 * k - 1)
            v0.setdefault(T0, set()).add(net.view[0])
            vk1.setdefault(T1, set()).add(net.view[k + 1])
            want0 = frozenset((s, r) for s in range(1, k + 1) for r in range(1, T0 - s + 2) if r >= 1)
            wantk = frozenset((s, r) for s in range(1, k + 1) for r in range(1, T1 - k + s + 1) if r >= 1)
            sets_ok &= (net.D[0] == want0 and net.D[k + 1] == wantk)
            for a in range(1, m + 1):
                for b in range(1, m + 1):
                    key = (m + a - b + 1, m + a + b - 1)
                    grid_ok &= ((key in net.D[0]) == (a <= i)) and ((key in net.D[k + 1]) == (b <= j))
    indep = all(len(x) == 1 for x in v0.values()) and all(len(x) == 1 for x in vk1.values())
    print(f"  cycle length {ell:2d} (k={k}, m={m}): views independent={indep}, D formulas={sets_ok}, grid={grid_ok},"
          f" bound a_0+a_(k+1) >= d*{(m - 1) ** 2}/{m}")
    assert indep and sets_ok and grid_ok
# control: one extra round lets the T0-dependence reach vertex k+1
k = 6
views = {light_cone(k, T0, 2 * k, 2 * k).view[k + 1] for T0 in (k, k + 1)}
print(f"  control (2k rounds, T1=2k): view of vertex k+1 depends on T0: {len(views) > 1}")
assert len(views) > 1

# ----------------------------------------------------------------------------- B3
print("=== B3: C3 schedules ===")


def async_sched(k, S, T, r_is_u, step2=True, clock=False):
    """Paths of length 2: u - w_s - v. P_{k+1} is u - r - v (r_is_u False) or the edge uv (True)."""
    nodes = ["u", "v", "r"] + list(range(k))
    net = Net(nodes, clock)
    tick = itertools.count()
    def rep(a, b):
        net.time = next(tick); net.report(a, b)
    for s in range(k):
        net.time = next(tick); net.obs(s, s)
    for s in sorted(T):
        rep(s, "u")
    if not r_is_u:
        rep("u", "r")
    if step2:
        for s in range(k):
            if s not in T:
                rep(s, "u")
    for s in sorted(S):
        rep(s, "v")
    R = "u" if r_is_u else "r"
    return net.view["v"], net.view[R], net.D["v"], net.D[R]


k = 4
subsets = [frozenset(c) for n_ in range(k + 1) for c in itertools.combinations(range(k), n_)]


def audit(**kw):
    phi, psi, dv_ok, dr_ok = {}, {}, True, True
    for S in subsets:
        for T in subsets:
            a, b, Dv, Dr = async_sched(k, S, T, **kw)
            phi.setdefault(S, set()).add(a)
            psi.setdefault(T, set()).add(b)
            dv_ok &= (Dv == S)
            dr_ok &= (Dr == T)
    return (all(len(x) == 1 for x in phi.values()), all(len(x) == 1 for x in psi.values()), dv_ok, dr_ok)


res = audit(r_is_u=False)
print(f"  r != u, steps 1-4, no clock : Phi_S indep of T={res[0]}, Psi_T indep of S={res[1]}, D_v=S={res[2]}, D_r=T={res[3]}")
assert all(res)
res = audit(r_is_u=True)
print(f"  r == u, steps 1-4, no clock : Phi_S indep of T={res[0]}, Psi_T indep of S={res[1]}, D_v=S={res[2]}, D_r=T={res[3]}   <-- D_u = [k], not T")
assert not res[3]
res = audit(r_is_u=True, step2=False)
print(f"  r == u, step 2 dropped      : Phi_S indep of T={res[0]}, Psi_T indep of S={res[1]}, D_v=S={res[2]}, D_r=T={res[3]}   <-- Phi_S depends on T")
assert not res[0] and res[3]
res = audit(r_is_u=False, clock=True)
print(f"  r != u, steps 1-4, CLOCK on : Phi_S indep of T={res[0]}  (the no-clock hypothesis is needed for length-2 paths)")
assert not res[0]


def gate_sched(k, S, T):
    """Clock variant: v - a_s - w_s - b_s - u, edge uv, global clock."""
    nodes = ["u", "v"] + [("a", s) for s in range(k)] + [("w", s) for s in range(k)] + [("b", s) for s in range(k)]
    net = Net(nodes, clock=True)
    net.time = 1
    for s in range(k):
        net.obs(("w", s), s)
    for s in range(k):
        net.report(("w", s), ("a", s)); net.report(("w", s), ("b", s))
    net.time = 2
    for s in range(k):
        if s in S:
            net.report(("a", s), "v")
        if s in T:
            net.report(("b", s), "u")
    return net.view["v"], net.view["u"], net.D["v"], net.D["u"]


phi, psi, ok = {}, {}, True
for S in subsets:
    for T in subsets:
        a, b, Dv, Du = gate_sched(k, S, T)
        phi.setdefault(S, set()).add(a); psi.setdefault(T, set()).add(b)
        ok &= (Dv == S and Du == T)
print(f"  gate vertices, edge uv, CLOCK on: Phi_S indep of T={all(len(x) == 1 for x in phi.values())},"
      f" Psi_T indep of S={all(len(x) == 1 for x in psi.values())}, sets={ok}")
assert ok and all(len(x) == 1 for x in phi.values()) and all(len(x) == 1 for x in psi.values())

# ----------------------------------------------------------------------------- B4
print("=== B4: C3 lemma dim U_L(S,i)+dim U_R(T,i) >= d on admissible families ===")
rng = np.random.default_rng(7)


def rank(M):
    M = np.atleast_2d(np.array(M, dtype=float))
    return 0 if M.size == 0 else int(np.linalg.matrix_rank(M, tol=1e-9))


def vec(k, d, S, y):
    v = np.zeros((k, d))
    for s in S:
        v[s] = y
    return v.ravel()


def fam_partition(k, d, extra):
    Aset = set(range(k // 2)); Bset = set(range(k // 2, k)); I = np.eye(d)
    L, R = {}, {}
    for S in subsets_k(k):
        rowsL = [vec(k, d, [i], I[a]) for i in S & Aset for a in range(d)] + [vec(k, d, S & Bset, I[a]) for a in range(d)]
        rowsR = [vec(k, d, [i], I[a]) for i in S & Bset for a in range(d)] + [vec(k, d, S & Aset, I[a]) for a in range(d)]
        for _ in range(extra):                      # random enlargement inside (R^d)^S keeps admissibility
            if S:
                rowsL.append(sum(vec(k, d, [i], rng.normal(size=d)) for i in S))
        L[S] = np.array(rowsL).reshape(-1, k * d); R[S] = np.array(rowsR).reshape(-1, k * d)
    return L, R


def fam_bad(k, d):
    I = np.eye(d)
    L = {S: np.array([vec(k, d, S, I[a]) for a in range(d)]) for S in subsets_k(k)}
    return L, dict(L)


def subsets_k(k):
    return [frozenset(c) for n_ in range(k + 1) for c in itertools.combinations(range(k), n_)]


def audit_family(k, d, L, R):
    I = np.eye(d)
    admissible, lemma = True, True
    total = 0
    for S in subsets_k(k):
        for T in subsets_k(k):
            both = np.vstack([L[S], R[T]])
            for a in range(d):
                admissible &= rank(np.vstack([both, vec(k, d, S | T, I[a])])) == rank(both)
    def dimU(X, i):
        blk = np.array([vec(k, d, [i], I[a]) for a in range(d)])
        return rank(X) + d - rank(np.vstack([X, blk]))
    for S in subsets_k(k):
        for i in S:
            T = (frozenset(range(k)) - S) | {i}
            val = dimU(L[S], i) + dimU(R[T], i)
            total += val
            lemma &= val >= d
    a_v = max(rank(L[S]) for S in L); a_r = max(rank(R[T]) for T in R)
    return admissible, lemma, total, a_v, a_r


for k_, d_, extra in [(3, 1, 0), (4, 1, 0), (4, 2, 0), (4, 2, 2), (5, 1, 1)]:
    L, R = fam_partition(k_, d_, extra)
    adm, lem, tot, av, ar = audit_family(k_, d_, L, R)
    lb = d_ * k_ * 2 ** (k_ - 1) / (2 ** k_ - 1)
    print(f"  partition family k={k_}, d={d_}, extra={extra}: admissible={adm}, lemma holds={lem},"
          f" a_v+a_r={av + ar} >= {lb:.3f}: {av + ar >= lb}")
    assert adm and lem and av + ar >= lb
L, R = fam_bad(4, 1)
adm, lem, tot, av, ar = audit_family(4, 1, L, R)
print(f"  control family L_S=span(1_S), R_T=span(1_T), k=4: admissible={adm}, lemma holds={lem}, a_v+a_r={av + ar}"
      f" < {4 * 8 / 15:.3f}")
assert (not adm) and (not lem)
L, R = fam_bad(2, 1)
adm, lem, tot, av, ar = audit_family(2, 1, L, R)
print(f"  same family at k=2: admissible={adm}, lemma holds={lem}, a_v+a_r={av + ar} = ceil(4/3)=2 (bound attained in the relaxation)")
assert adm and lem and av + ar == 2

# ----------------------------------------------------------------------------- B5
print("=== B5: C4 inequalities on all 2-connected graphs with <= 7 vertices ===")
from networkx.generators.atlas import graph_atlas_g


def circumference(G):
    best = 0
    nodes = list(G.nodes())
    adj = {v: set(G[v]) for v in nodes}
    order = {v: i for i, v in enumerate(nodes)}
    def dfs(start, v, visited, length):
        nonlocal best
        for w in adj[v]:
            if w == start and length >= 3:
                best = max(best, length)
            elif w not in visited and order[w] > order[start]:
                visited.add(w)
                dfs(start, w, visited, length + 1)
                visited.remove(w)
    for s in nodes:
        dfs(s, s, {s}, 1)
    return best


def theta(G):
    best = 0
    for u, v in itertools.combinations(G.nodes(), 2):
        if G.has_edge(u, v):
            H = G.copy(); H.remove_edge(u, v)
            kap = 1 + (nx.node_connectivity(H, u, v) if nx.has_path(H, u, v) else 0)
        else:
            kap = nx.node_connectivity(G, u, v)
        best = max(best, kap)
    return best


count, viol = 0, 0
tight_diam = 0
for G in graph_atlas_g():
    if G.number_of_nodes() < 3 or not nx.is_biconnected(G):
        continue
    count += 1
    C = circumference(G); Dm = nx.diameter(G); Delta = max(dict(G.degree()).values()); th = theta(G)
    b = G.number_of_nodes()
    i1 = Dm <= C // 2
    i2 = Delta <= 1 + th ** ((C + 1) // 2 - 1)
    i3 = b <= 1 + Delta ** (C // 2)
    viol += not (i1 and i2 and i3)
    tight_diam += (Dm == C // 2)
print(f"  2-connected graphs checked: {count}, violations of (diam, Delta, |V|) inequalities: {viol},"
      f" diam bound tight on {tight_diam}")
assert viol == 0
G = nx.barbell_graph(3, 5)
print(f"  control (not 2-connected) barbell(3,5): diam={nx.diameter(G)} > circ//2={circumference(G) // 2}")
assert nx.diameter(G) > circumference(G) // 2
print("ALL REVIEWER CHECKS FOR prv_minimal COMPLETED.")
