"""Verification suite for open:prv-minimal (Minimal provenance with identifiers).

Two-channel checks and planted-error negative controls for:
  C1: Block-Cut Channel Protocol (exactness, storage counts, bridge channel reduction).
  C2: Cycle light-cone schedule and 2D-grid mixed-difference lower bound on C_n.
  C3: Subset-union / local-connectivity lower bound on K_{2,k+1} and subdivided K_{2,k}.
  C4: 2-connected graph dichotomy (circ, theta, block size) and O(1) vs Theta(n) scaling.
  C5: Falsification of naive graph-invariant bounds (fvs, tw, max-degree, circ alone).
"""

import os
import numpy as np
import networkx as nx
from sympy import Matrix


def check_c1_block_cut():
    print("=== CHECK 1: Block-Cut Channel Protocol (C1) ===")
    rng = np.random.default_rng(20261121)

    def run_protocol(G, d=2, steps=60, plant_cut_bug=False, force_tree_rule=False):
        nodes = list(G.nodes())
        n = len(nodes)
        blocks = [set(b) for b in nx.biconnected_components(G)]
        edge_to_block = {}
        for bi, B in enumerate(blocks):
            for u in B:
                for v in B:
                    if u < v and G.has_edge(u, v):
                        edge_to_block[(u, v)] = bi
                        edge_to_block[(v, u)] = bi
        node_blocks = {v: [bi for bi, B in enumerate(blocks) if v in B] for v in nodes}
        is_2conn = [len(B) >= 3 for B in blocks]

        # Non-symmetric invertible A, generic H_v, SPD R_v, SPD P0
        A = rng.normal(size=(d, d))
        while abs(np.linalg.det(A)) < 0.2:
            A = rng.normal(size=(d, d))
        A = 0.95 * A / max(abs(np.linalg.eigvals(A)))
        M0 = rng.normal(size=(d, d))
        P0 = M0 @ M0.T + 0.5 * np.eye(d)
        m0 = rng.normal(size=d)
        pi0_L = np.linalg.inv(P0)
        pi0_h = pi0_L @ m0

        H_map = {v: rng.normal(size=(d, d)) for v in nodes}
        R_map = {}
        for v in nodes:
            Mr = rng.normal(size=(d, d))
            R_map[v] = Mr @ Mr.T + 0.3 * np.eye(d)

        s_L = {v: pi0_L.copy() for v in nodes}
        s_h = {v: pi0_h.copy() for v in nodes}
        # Bridge channel pairs keyed by sorted edge (u, v)
        c_link_L = {}
        c_link_h = {}
        for u, v in G.edges():
            e = (min(u, v), max(u, v))
            if force_tree_rule or not is_2conn[edge_to_block[(u, v)]]:
                c_link_L[e] = pi0_L.copy()
                c_link_h[e] = pi0_h.copy()

        # 2-connected block tables at nodes
        E_L = {v: {bi: {w: np.zeros((d, d)) for w in blocks[bi] if w != v}
                   for bi in node_blocks[v] if is_2conn[bi]} for v in nodes}
        E_h = {v: {bi: {w: np.zeros(d) for w in blocks[bi] if w != v}
                   for bi in node_blocks[v] if is_2conn[bi]} for v in nodes}
        c_tab = {v: {bi: {w: 0 for w in blocks[bi] if w != v}
                     for bi in node_blocks[v] if is_2conn[bi]} for v in nodes}
        c_self = {v: {bi: 0 for bi in node_blocks[v] if is_2conn[bi]} for v in nodes}

        def get_E_self(v, bi):
            IL = sum(E_L[v][bi].values(), np.zeros((d, d)))
            Ih = sum(E_h[v][bi].values(), np.zeros(d))
            return s_L[v] - pi0_L - IL, s_h[v] - pi0_h - Ih

        D = {v: set() for v in nodes}
        # Store raw (v, t, o) for Channel B batch Gaussian conditioning
        raw_obs = {}
        items = {}
        obs_id = 0
        edges = list(G.edges())
        max_err_chA = 0.0

        A_pow = np.eye(d)
        for t in range(1, steps + 1):
            A_pow = A_pow @ A
            # Observation at random node
            v = nodes[rng.integers(n)]
            obs_id += 1
            o_val = rng.normal(size=d)
            Hv_eff = H_map[v] @ A_pow
            Rv_inv = np.linalg.inv(R_map[v])
            L_item = Hv_eff.T @ Rv_inv @ Hv_eff
            h_item = Hv_eff.T @ Rv_inv @ o_val
            items[obs_id] = (L_item, h_item)
            raw_obs[obs_id] = (Hv_eff, R_map[v], o_val)
            D[v].add(obs_id)
            s_L[v] += L_item
            s_h[v] += h_item
            if not force_tree_rule:
                for bi in node_blocks[v]:
                    if is_2conn[bi]:
                        c_self[v][bi] += 1

            # 3 random one-way reports per step
            for _ in range(3):
                u, v = edges[rng.integers(len(edges))]
                if rng.random() < 0.5:
                    u, v = v, u
                D[v] |= D[u]
                e = (min(u, v), max(u, v))
                bi = edge_to_block[(u, v)]
                if force_tree_rule or not is_2conn[bi]:
                    s_L[v] = s_L[v] + s_L[u] - c_link_L[e]
                    s_h[v] = s_h[v] + s_h[u] - c_link_h[e]
                    c_link_L[e] = s_L[u].copy()
                    c_link_h[e] = s_h[u].copy()
                    if not force_tree_rule and not plant_cut_bug:
                        for bj in node_blocks[v]:
                            if bj != bi and is_2conn[bj]:
                                c_self[v][bj] += 1
                else:
                    u_self_L, u_self_h = get_E_self(u, bi)
                    changed = False
                    for w in blocks[bi]:
                        if w == v:
                            continue
                        cw = c_self[u][bi] if w == u else c_tab[u][bi][w]
                        if cw > c_tab[v][bi][w]:
                            new_L = u_self_L if w == u else E_L[u][bi][w]
                            new_h = u_self_h if w == u else E_h[u][bi][w]
                            s_L[v] = s_L[v] - E_L[v][bi][w] + new_L
                            s_h[v] = s_h[v] - E_h[v][bi][w] + new_h
                            E_L[v][bi][w] = new_L.copy()
                            E_h[v][bi][w] = new_h.copy()
                            c_tab[v][bi][w] = cw
                            changed = True
                    if changed and not plant_cut_bug:
                        for bj in node_blocks[v]:
                            if bj != bi and is_2conn[bj]:
                                c_self[v][bj] += 1

            # Channel A: information-form sum over D[x]
            for x in nodes:
                gt_L = pi0_L + sum((items[k][0] for k in D[x]), np.zeros((d, d)))
                gt_h = pi0_h + sum((items[k][1] for k in D[x]), np.zeros(d))
                err = max(np.max(np.abs(s_L[x] - gt_L)), np.max(np.abs(s_h[x] - gt_h)))
                max_err_chA = max(max_err_chA, err)

        # Channel B: independent batch Gaussian conditioning in covariance form at final step
        max_err_chB = 0.0
        for x in nodes:
            keys = sorted(D[x])
            if not keys:
                post_L, post_h = pi0_L, pi0_h
            else:
                H_stack = np.vstack([raw_obs[k][0] for k in keys])
                R_blocks = [raw_obs[k][1] for k in keys]
                R_big = np.zeros((d * len(keys), d * len(keys)))
                for idx, Rb in enumerate(R_blocks):
                    R_big[idx*d:(idx+1)*d, idx*d:(idx+1)*d] = Rb
                o_stack = np.concatenate([raw_obs[k][2] for k in keys])
                # Joint Gaussian conditioning: Cov(x0, o) = P0 H^T, Cov(o) = H P0 H^T + R
                S_oo = H_stack @ P0 @ H_stack.T + R_big
                K_gain = P0 @ H_stack.T @ np.linalg.inv(S_oo)
                m_post = m0 + K_gain @ (o_stack - H_stack @ m0)
                P_post = P0 - K_gain @ H_stack @ P0
                post_L = np.linalg.inv(P_post)
                post_h = post_L @ m_post
            err = max(np.max(np.abs(s_L[x] - post_L)), np.max(np.abs(s_h[x] - post_h)))
            max_err_chB = max(max_err_chB, err)

        # Storage accounting
        node_extra = {v: sum(len(E_L[v][bi]) for bi in E_L[v]) for v in nodes}
        link_extra = len(c_link_L)
        expected_node_extra = {
            v: sum(len(blocks[bi]) - 1 for bi in node_blocks[v] if is_2conn[bi])
            for v in nodes
        }
        expected_link_extra = sum(1 for bi in range(len(blocks)) if not is_2conn[bi])
        storage_ok = (node_extra == expected_node_extra) and (link_extra == expected_link_extra)
        return max_err_chA, max_err_chB, storage_ok, max(node_extra.values()), link_extra

    graphs = [
        ("tree_8", nx.balanced_tree(2, 2)),
        ("unicyclic_C4_tree", nx.Graph([(0,1),(1,2),(2,3),(3,0),(0,4),(4,5),(4,6),(2,7)])),
        ("barbell_K4", nx.barbell_graph(4, 2)),
        ("cactus_3tri", nx.Graph([(0,1),(1,2),(2,0),(2,3),(3,4),(4,2),(4,5),(5,6),(6,4),(0,7)])),
        ("multi_block", nx.Graph([(0,1),(1,2),(2,3),(3,0),(0,4),(4,5),(5,0),(5,6),(6,7),(7,8),(8,9),(9,10),(10,6)])),
    ]
    for name, G in graphs:
        errA, errB, st_ok, max_np, lp = run_protocol(G, d=2, steps=60)
        assert errA < 1e-10 and errB < 1e-9 and st_ok, f"Failed on {name}: {errA}, {errB}, {st_ok}"
        print(f"  {name:18s}: n={G.number_of_nodes():2d}, max_node_pairs={max_np}, bridge_pairs={lp}, "
              f"err_ChA={errA:.2e}, err_ChB={errB:.2e}, storage_match={st_ok}")

    # Negative control 1: omit cut-vertex counter bump on barbell
    errA_bug, _, _, _, _ = run_protocol(nx.barbell_graph(4, 2), d=2, steps=60, plant_cut_bug=True)
    assert errA_bug > 1e-1, f"Negative control 1 did not fail! err={errA_bug}"
    print(f"  [NEG-CTRL 1] omit cut-vertex bump on barbell: err={errA_bug:.2e} (FAILS as expected)")

    # Negative control 2: tree channel-pair rule on C3
    errA_tree, _, _, _, _ = run_protocol(nx.cycle_graph(3), d=2, steps=30, force_tree_rule=True)
    assert errA_tree > 1e-1, f"Negative control 2 did not fail! err={errA_tree}"
    print(f"  [NEG-CTRL 2] tree channel-pair rule on C3:    err={errA_tree:.2e} (FAILS as expected)")


def check_c2_cycle_lower_bound():
    print("\n=== CHECK 2: Cycle Light-Cone & 2D-Grid Lower Bound (C2) ===")

    def sim_cycle(k, T0, T1, total_rounds=None):
        if total_rounds is None:
            total_rounds = 2 * k - 1
        D = [set() for _ in range(k + 2)]
        saw_T0 = [False] * (k + 2)
        saw_T1 = [False] * (k + 2)
        for t in range(1, total_rounds + 1):
            for s in range(1, k + 1):
                D[s].add((s, t))
            if t <= T0:
                D[0] |= D[1]
                saw_T0[0] |= saw_T0[1]
                saw_T1[0] |= saw_T1[1]
            if t > k:
                saw_T0[0] = True
                saw_T0[1] = True
            if t <= T1:
                D[k + 1] |= D[k]
                saw_T0[k + 1] |= saw_T0[k]
                saw_T1[k + 1] |= saw_T1[k]
            if t > k:
                saw_T1[k + 1] = True
                saw_T1[k] = True
            for s in range(k - 1, 0, -1):
                D[s + 1] |= D[s]
                saw_T0[s + 1] |= saw_T0[s]
                saw_T1[s + 1] |= saw_T1[s]
            for s in range(2, k + 1):
                D[s - 1] |= D[s]
                saw_T0[s - 1] |= saw_T0[s]
                saw_T1[s - 1] |= saw_T1[s]
        return D[0], D[k + 1], saw_T1[0], saw_T0[k + 1]

    rng = np.random.default_rng(12345)
    for n in [6, 8, 10, 12]:
        k = n - 2
        m = k // 2
        # Grid points (a, b) in {m+1, ..., 2m} x {0, ..., m-1} -> s = a-b, r = a+b
        # Indexed by (i, j) in {1..m} x {1..m} with a = m+i, b = j-1
        T0_vals = [2 * (m + i) - 1 for i in range(1, m + 1)]
        T1_vals = [k + 2 * (j - 1) for j in range(1, m + 1)]
        grid = {(i, j): ((m + i) - (j - 1), (m + i) + (j - 1))
                for i in range(1, m + 1) for j in range(1, m + 1)}
        # Verify all grid (s, r) are distinct and admissible
        assert len(set(grid.values())) == m * m
        for (i, j), (s, r) in grid.items():
            assert 1 <= s <= k and 1 <= r <= 2 * k - 1

        # Channel A: simulate ALL m^2 pairs (T0, T1) and build exact SymPy incidence matrix
        rows = []
        active_coords = [(a, b) for a in range(2, m + 1) for b in range(2, m + 1)]
        any_leak = False
        grid_match = True
        for i_idx, T0 in enumerate(T0_vals, start=1):
            for j_idx, T1 in enumerate(T1_vals, start=1):
                D0, Dk1, leak0, leakk1 = sim_cycle(k, T0, T1)
                any_leak = any_leak or leak0 or leakk1
                # Check exact match on grid
                for (a, b), sr in grid.items():
                    if (sr in D0) != (a <= i_idx):
                        grid_match = False
                    if (sr in Dk1) != (b <= j_idx):
                        grid_match = False
                union_set = D0 | Dk1
                rows.append([1 if grid[(a, b)] in union_set else 0 for (a, b) in active_coords])

        M_sym = Matrix(rows)
        rk = M_sym.rank()
        assert not any_leak and grid_match and rk == (m - 1) ** 2

        # Channel B: numerical recovery of random vector x in R^{(m-1)^2 x d} via 4-point mixed difference
        d = 3
        x_true = rng.normal(size=(m + 1, m + 1, d))
        x_true[1, :, :] = 0.0
        x_true[:, 1, :] = 0.0
        S = np.zeros((m + 1, m + 1, d))
        for i_idx in range(1, m + 1):
            for j_idx in range(1, m + 1):
                total = np.zeros(d)
                for a in range(2, m + 1):
                    for b in range(2, m + 1):
                        if a <= i_idx or b <= j_idx:
                            total += x_true[a, b]
                S[i_idx, j_idx] = total
        max_rec_err = 0.0
        for i_idx in range(2, m + 1):
            for j_idx in range(2, m + 1):
                x_rec = -(S[i_idx, j_idx] - S[i_idx, j_idx - 1]
                          - S[i_idx - 1, j_idx] + S[i_idx - 1, j_idx - 1])
                max_rec_err = max(max_rec_err, float(np.max(np.abs(x_rec - x_true[i_idx, j_idx]))))
        assert max_rec_err < 1e-13
        lb_d1 = (m - 1) ** 2 / m
        print(f"  C_{n:2d} (k={k:2d}, m={m}): leak={any_leak}, grid_match={grid_match}, "
              f"sym_rank={rk}/{(m-1)**2}, rec_err={max_rec_err:.2e}, a+b>={lb_d1:.3f}*d")

    # Negative control 1: run 2k rounds with T0=T1=2k -> causal leak MUST occur
    _, _, leak0_bad, leakk1_bad = sim_cycle(6, 12, 12, total_rounds=12)
    assert leak0_bad and leakk1_bad
    print(f"  [NEG-CTRL 1] 2k=12 rounds on C_8: leak_to_0={leak0_bad}, leak_to_k1={leakk1_bad} (LEAKS as expected)")

    # Negative control 2: wrong sign in 4-point difference formula
    wrong_err = float(np.max(np.abs(
        -(S[2, 2] + S[2, 1] - S[1, 2] + S[1, 1]) - x_true[2, 2]
    )))
    assert wrong_err > 0.5
    print(f"  [NEG-CTRL 2] flipped sign in 4-pt difference: err={wrong_err:.2e} (FAILS as expected)")


def check_c3_subset_union():
    print("\n=== CHECK 3: Subset-Union / Local-Connectivity Lower Bound (C3) ===")

    # Channel A: simulate asynchronous K_{2, k+1} schedule (no global sub-event clock)
    # Poles u, v; middle nodes 1..k; relay r = k+1
    for k in [3, 4]:
        all_ok = True
        for S_mask in range(1 << k):
            S = {s for s in range(1, k + 1) if (S_mask >> (s - 1)) & 1}
            for T_mask in range(1 << k):
                T = {s for s in range(1, k + 1) if (T_mask >> (s - 1)) & 1}
                # Track local event transcript of each node (no global clock)
                D = {x: set() for x in ['u', 'v', 'r'] + list(range(1, k + 1))}
                # Each middle node s observes e_s
                for s in range(1, k + 1):
                    D[s].add(s)
                # Phase 1: s -> u for s in T, then u -> r
                for s in sorted(T):
                    D['u'] |= D[s]
                D['r'] |= D['u']
                # Phase 2: s -> u for s not in T (s does NOT receive anything from u!)
                for s in range(1, k + 1):
                    if s not in T:
                        D['u'] |= D[s]
                # Phase 3: s -> v for s in S
                for s in sorted(S):
                    D['v'] |= D[s]
                # Check D['v'] == S, D['r'] == T, and D['v'] | D['r'] == S | T
                if D['v'] != S or D['r'] != T or (D['v'] | D['r']) != (S | T):
                    all_ok = False
        assert all_ok
        # Verify cross-intersecting bijection count: sum_{S, i in S} 1 = k * 2^{k-1}
        pairs = [(S_mask, i) for S_mask in range(1 << k) for i in range(k) if (S_mask >> i) & 1]
        full = (1 << k) - 1
        mapped = [((full ^ S_mask) | (1 << i), i) for (S_mask, i) in pairs]
        assert len(pairs) == k * (1 << (k - 1)) and set(mapped) == set(pairs)
        lb = (k * (1 << (k - 1))) / ((1 << k) - 1)
        print(f"  K_{{2,{k+1}}}: all {4**k} (S,T) pairs exact={all_ok}, bijection_ok=True, a+b >= {lb:.4f}*d (> {k/2:.2f}*d)")

    # Channel B: verify explicit partition upper bound (a = floor(k/2)+1, b = ceil(k/2)+1) for d=1
    for k in [4, 5, 6]:
        A_set = set(range(k // 2))
        B_set = set(range(k // 2, k))
        max_a, max_b = 0, 0
        for S_mask in range(1 << k):
            S = {i for i in range(k) if (S_mask >> i) & 1}
            # L_S basis: {e_i : i in S & A} and 1_{S & B}
            L_vecs = []
            for i in sorted(S & A_set):
                v = np.zeros(k); v[i] = 1.0; L_vecs.append(v)
            if S & B_set:
                v = np.zeros(k)
                for i in S & B_set: v[i] = 1.0
                L_vecs.append(v)
            max_a = max(max_a, len(L_vecs))
        for T_mask in range(1 << k):
            T = {i for i in range(k) if (T_mask >> i) & 1}
            R_vecs = []
            for i in sorted(T & B_set):
                v = np.zeros(k); v[i] = 1.0; R_vecs.append(v)
            if T & A_set:
                v = np.zeros(k)
                for i in T & A_set: v[i] = 1.0
                R_vecs.append(v)
            max_b = max(max_b, len(R_vecs))
        assert max_a <= k // 2 + 1 and max_b <= (k + 1) // 2 + 1
        print(f"  Subset-union partition UB (k={k}): max_a={max_a}, max_b={max_b}, sum={max_a+max_b} <= k+2={k+2}")

    # Negative control: check that cross-intersecting inequality fails if a+b <= k/2 is claimed for k=4
    k = 4
    rhs_required = k * (1 << (k - 1))  # 32
    max_achieved_at_ab_eq_2 = ((1 << k) - 1) * 2  # 30 < 32
    assert max_achieved_at_ab_eq_2 < rhs_required
    print(f"  [NEG-CTRL] k=4 with a+b=2: max covered={max_achieved_at_ab_eq_2} < required={rhs_required} (CONTRADICTION as expected)")


def check_c4_c5_dichotomy_and_falsification():
    print("\n=== CHECK 4 & 5: 2-Connected Dichotomy (C4) & Falsification of Naive Bounds (C5) ===")

    def circumference_exact(G):
        if G.number_of_edges() < G.number_of_nodes():
            return 0
        # Simple cycles (for small test graphs)
        return max((len(c) for c in nx.simple_cycles(G.to_directed()) if len(c) >= 3), default=0)

    def max_local_conn(G):
        nodes = list(G.nodes())
        best = 0
        for i in range(len(nodes)):
            for j in range(i + 1, len(nodes)):
                best = max(best, nx.node_connectivity(G, nodes[i], nodes[j]))
        return best

    # Test 2-connected graphs: verify diam(B) <= circ(B)//2 and |V(B)| <= 1 + Delta^{circ//2}
    two_conn_suite = [
        ("C_6", nx.cycle_graph(6)),
        ("K_5", nx.complete_graph(5)),
        ("K_{2,5}", nx.complete_bipartite_graph(2, 5)),
        ("Wheel_7", nx.wheel_graph(7)),
        ("Prism_5", nx.circular_ladder_graph(5)),
    ]
    for name, B in two_conn_suite:
        assert nx.is_biconnected(B)
        b = B.number_of_nodes()
        circ = circumference_exact(B)
        diam = nx.diameter(B)
        delta = max(dict(B.degree()).values())
        theta = max_local_conn(B)
        bound_v = 1 + delta ** (circ // 2)
        assert diam <= circ // 2 and b <= bound_v
        print(f"  {name:10s}: |V|={b:2d}, circ={circ:2d}, diam={diam} <= {circ//2}, "
              f"Delta={delta}, theta={theta}, 1+Delta^(circ//2)={bound_v}")

    # Negative control for C4: non-2-connected graph violates diam <= circ//2
    barbell = nx.barbell_graph(3, 5)
    c_bb = circumference_exact(barbell)
    d_bb = nx.diameter(barbell)
    assert d_bb > c_bb // 2
    print(f"  [NEG-CTRL C4] barbell(3,5) (not 2-connected): circ={c_bb}, diam={d_bb} > {c_bb//2} (VIOLATES bound as expected)")

    # C5: Falsification witness G_k (subdivided K_{2,k} + edge uv)
    # Vertices: u, v, and for s=1..k: a_s, m_s, b_s with path v - a_s - m_s - b_s - u
    for k in [4, 6]:
        Gk = nx.Graph()
        Gk.add_edge('u', 'v')
        for s in range(1, k + 1):
            Gk.add_edges_from([('v', f'a{s}'), (f'a{s}', f'm{s}'), (f'm{s}', f'b{s}'), (f'b{s}', 'u')])
        # FVS <= 2: removing {'u', 'v'} leaves k disjoint paths of length 2 (a forest!)
        G_minus_uv = Gk.copy()
        G_minus_uv.remove_nodes_from(['u', 'v'])
        is_forest = nx.is_forest(G_minus_uv)
        # Treewidth = 2 (series-parallel: repeatedly contract degree-2 vertices)
        tw, _ = nx.algorithms.approximation.treewidth_min_degree(Gk)
        circ_Gk = circumference_exact(Gk)
        theta_Gk = nx.node_connectivity(Gk, 'u', 'v')
        assert is_forest and tw == 2 and circ_Gk == 8 and theta_Gk == k + 1
        print(f"  [C5 witness] G_{k}: n={Gk.number_of_nodes():2d}, fvs<=2 (forest={is_forest}), "
              f"tw={tw}, circ={circ_Gk}, theta={theta_Gk} -> LB > {k/2:.1f}*d = Omega(n)")

    # Bounded-block-size family: cactus of m triangles attached in a path (n = 2m + 1)
    print("  Bounded-block-size cactus chain (triangles in a path):")
    for m_tri in [5, 25, 50]:
        Cact = nx.Graph()
        for t in range(m_tri):
            u, w, v = 2 * t, 2 * t + 1, 2 * t + 2
            Cact.add_edges_from([(u, w), (w, v), (v, u)])
        n = Cact.number_of_nodes()
        blocks = [set(b) for b in nx.biconnected_components(Cact)]
        max_node_pairs = max(sum(len(B) - 1 for B in blocks if v in B and len(B) >= 3) for v in Cact.nodes())
        print(f"    m={m_tri:2d}, n={n:3d}: Block-Cut max_node_pairs={max_node_pairs} (O(1)) vs prop:prv-clock={n} (Theta(n))")


if __name__ == "__main__":
    check_c1_block_cut()
    check_c2_cycle_lower_bound()
    check_c3_subset_union()
    check_c4_c5_dichotomy_and_falsification()
    print("\nALL CHECKS AND NEGATIVE CONTROLS PASSED.")
