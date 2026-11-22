"""
Two-channel verification script with planted-error negative controls for open:agy-uniform-bound.
Covers Claims C1, C2, C3, C4 of docs/research/open_agy_uniform_bound.md.
"""
import math
from decimal import Decimal, getcontext
from itertools import product
import numpy as np
from scipy.optimize import minimize

getcontext().prec = 80


# =============================================================================
# Helper functions: Linear-Gaussian slot model primitives (def:agy-group-model)
# =============================================================================

def I_red(v):
    """Redundancy I(o_1; o_2) = 0.5 * ln((1+v)^2 / (1+2v)) for two unit-SNR slots on eta ~ N(0, v)."""
    return 0.5 * math.log(((1.0 + v) ** 2) / (1.0 + 2.0 * v))


def v_from_I(I_val):
    """Exact inverse of I_red(v): v = (K-1) + sqrt(K*(K-1)) with K = exp(2*I_val)."""
    K = math.exp(2.0 * I_val)
    return (K - 1.0) + math.sqrt(K * (K - 1.0))


def build_geartrain_3top(m):
    """
    m >= 2 gears on n = 8*m - 9 binary members:
      gear 0: closed 4-cycle (4 members, harmonic motor)
      gears 1..m-2: closed 8-cycles (8 members each)
      gear m-1: open 3-path 0-1-2 (3 members)
    """
    assert m >= 2
    gear_nodes = []
    cur = 0
    for g in range(m):
        sz = 4 if g == 0 else (3 if g == m - 1 else 8)
        gear_nodes.append(list(range(cur, cur + sz)))
        cur += sz
    n = cur

    adj_edges, wall_edges, motor_edges = [], [], []
    for g in range(m):
        nodes = gear_nodes[g]
        sz = len(nodes)
        is_cycle = (g < m - 1)
        for i in range(sz):
            for j in range(i + 1, sz):
                is_adj = (j == i + 1) or (is_cycle and i == 0 and j == sz - 1)
                if is_adj:
                    adj_edges.append((nodes[i], nodes[j]))
                else:
                    wall_edges.append((nodes[i], nodes[j]))
        if g == 0:
            for i in range(4):
                motor_edges.append((nodes[i], nodes[(i + 1) % 4]))

    for g in range(m - 1):
        fast = gear_nodes[g]
        slow = gear_nodes[g + 1]
        fsz, ssz = len(fast), len(slow)
        a_lo, a_hi = (0, 2) if g == 0 else (1, 5)
        arc1 = set((a_lo + t) % fsz for t in range(fsz // 2 + 1))
        arc2 = set((a_hi + t) % fsz for t in range(fsz // 2 + 1))
        for r in range(ssz):
            if r in (0, 4):
                allowed = arc1
            elif r in (1, 5):
                allowed = {a_hi}
            elif r in (2, 6):
                allowed = arc2
            elif r in (3, 7):
                allowed = {a_lo}
            for s in range(fsz):
                if s not in allowed:
                    wall_edges.append((fast[s], slow[r]))

    return n, gear_nodes, adj_edges, wall_edges, motor_edges


def analyze_path_topology(m, drop_wall_idx=None):
    n, gear_nodes, adj_edges, wall_edges, motor_edges = build_geartrain_3top(m)
    if drop_wall_idx is not None:
        wall_edges = wall_edges[:drop_wall_idx] + wall_edges[drop_wall_idx + 1:]
    wall_set = set(wall_edges) | {(v, u) for (u, v) in wall_edges}
    adj_set = set(adj_edges) | {(v, u) for (u, v) in adj_edges}

    valid = []
    for tup in product(*gear_nodes):
        ok = True
        for a in range(m):
            for b in range(a + 1, m):
                if (tup[a], tup[b]) in wall_set:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            valid.append(tup)
    valid_set = set(valid)
    nbrs = {s: [] for s in valid}
    for s in valid:
        for g in range(m):
            u = s[g]
            for v in gear_nodes[g]:
                if (u, v) in adj_set:
                    s2 = list(s)
                    s2[g] = v
                    s2 = tuple(s2)
                    if s2 in valid_set:
                        nbrs[s].append(s2)

    endpoints = [s for s in valid if len(nbrs[s]) == 1]
    max_deg = max(len(nbrs[s]) for s in valid)
    min_deg = min(len(nbrs[s]) for s in valid)
    if len(endpoints) != 2 or max_deg > 2 or min_deg < 1:
        return False, (len(valid), len(endpoints), min_deg, max_deg), None

    path = [endpoints[0]]
    prev, cur = None, endpoints[0]
    motor_dir = set(motor_edges)
    s_steps = [0]
    while True:
        nxts = [x for x in nbrs[cur] if x != prev]
        if not nxts:
            break
        nxt = nxts[0]
        ds = 0
        if nxt[0] != cur[0]:
            ds = 1 if (cur[0], nxt[0]) in motor_dir else -1
        path.append(nxt)
        s_steps.append(s_steps[-1] + ds)
        prev, cur = cur, nxt
    if s_steps[-1] < 0:
        path.reverse()
        s_steps = [s_steps[-1] - x for x in reversed(s_steps)]
    if len(path) != len(valid):
        return False, (len(valid), len(path)), None
    return True, (n, gear_nodes, adj_edges, wall_edges, motor_edges), (path, s_steps)


def build_explicit_lg_model(n, adj_edges, wall_edges, motor_edges, I_adj, I_wall, delta, c_target, potential_control=False):
    """
    Channel 1: Build the FULL explicit linear-Gaussian slot model (def:agy-group-model):
      - One independent coordinate eta_e per edge e in E = adj_edges + wall_edges.
      - Slot o_{u,e} = lam * (eta_e + nu_{u,e}), nu_{u,e} ~ N(0, 1), for each edge e incident to u.
      - Declared belief q_C = N(0, diag(v_{C,e})), member beliefs q_u = N(0, diag(v_{u,e})).
      - Gaussian slot preferences N(mu_star_{u,e}, tau_{u,e}^2) achieving exact c_u = -I_{q_u}(eta; o_u) + psi_u(q_u).
    """
    edges = list(adj_edges) + list(wall_edges)
    E_cnt = len(edges)
    v_adj = v_from_I(I_adj)
    v_wall = v_from_I(I_wall)
    v_plus = v_from_I(I_adj + delta)
    v_minus = v_from_I(I_adj - delta)

    v_C = np.array([v_adj] * len(adj_edges) + [v_wall] * len(wall_edges), dtype=np.float64)
    v_mem = np.tile(v_C, (n, 1))

    motor_map = {}
    for idx_e, (u, v) in enumerate(adj_edges):
        if (u, v) in motor_edges:
            motor_map[idx_e] = (u, v)
        elif (v, u) in motor_edges:
            motor_map[idx_e] = (v, u)

    for idx_e, (u_out, v_in) in motor_map.items():
        if not potential_control:
            # Harmonic motor: u_out perceives I_adj + delta, v_in perceives I_adj - delta
            v_mem[u_out, idx_e] = v_plus
            v_mem[v_in, idx_e] = v_minus
        else:
            # Planted-error control: potential perturbation (both perceive I_adj + delta)
            v_mem[u_out, idx_e] = v_plus
            v_mem[v_in, idx_e] = v_plus

    # Incident edges per member
    inc = [[] for _ in range(n)]
    for idx_e, (u, v) in enumerate(edges):
        inc[u].append(idx_e)
        inc[v].append(idx_e)

    # Uniform observation scale lam so that 0.5*ln(2*pi*e*lam^2*(v+1)) <= 0 for all slots
    v_max = max(v_wall, v_plus)
    lam = 1.0 / math.sqrt(2.0 * math.pi * math.e * (v_max + 1.0))

    # Construct explicit Gaussian slot preferences (mu_star_{u,e}, tau_{u,e}^2)
    tau2 = {}
    mu_star = {}
    psi_own = np.zeros(n)
    I_own = np.zeros(n)
    for u in range(n):
        I_u = sum(0.5 * math.log(1.0 + v_mem[u, idx_e]) for idx_e in inc[u])
        I_own[u] = I_u
        psi_needed = c_target[u] + I_u
        assert psi_needed > 0.0, f"Member {u} needs psi={psi_needed} <= 0"
        base_psi = 0.0
        for idx_e in inc[u]:
            t2 = (lam ** 2) * (v_mem[u, idx_e] + 1.0)
            tau2[(u, idx_e)] = t2
            base_psi += 0.5 * math.log(2.0 * math.pi * math.e * t2)
        extra = psi_needed - base_psi
        assert extra >= 0.0, f"Extra pragmatic term negative: {extra}"
        # Split extra evenly across incident slots via (mu_star)^2 / (2*tau^2)
        per_slot = extra / len(inc[u])
        psi_check = 0.0
        for idx_e in inc[u]:
            t2 = tau2[(u, idx_e)]
            m_s = math.sqrt(2.0 * t2 * per_slot)
            mu_star[(u, idx_e)] = m_s
            var_o = (lam ** 2) * (v_mem[u, idx_e] + 1.0)
            psi_check += 0.5 * math.log(2.0 * math.pi * t2) + (var_o + m_s ** 2) / (2.0 * t2)
        psi_own[u] = psi_check
        assert abs((psi_check - I_u) - c_target[u]) < 1e-13

    return edges, inc, v_C, v_mem, lam, tau2, mu_star, psi_own, I_own


def compute_exact_G_from_lg(n, edges, inc, v_C, v_mem, lam, tau2, mu_star):
    """
    Evaluate G_u(pi), G_C(pi), T_u(pi_u), Phi(pi), R_u(pi) directly from def:agy-group-model
    on ALL 2^n states pi in {0,1}^n.
    """
    N = 1 << n
    E_cnt = len(edges)
    # Build edge-active count k_e(pi) in {0, 1, 2} for every state pi and edge e
    s_idx = np.arange(N, dtype=np.int32)
    bits = ((s_idx[:, None] >> np.arange(n)[None, :]) & 1)  # (N, n)
    u_arr = np.array([e[0] for e in edges])
    v_arr = np.array([e[1] for e in edges])
    k_e = bits[:, u_arr] + bits[:, v_arr]  # (N, E_cnt), entries in {0,1,2}

    # Information gains I_{q_C}(eta; o_B(pi)) and I_{q_u}(eta; o_B(pi))
    I_C_all = 0.5 * np.sum(np.log(1.0 + k_e * v_C[None, :]), axis=1)  # (N,)
    I_mem_all = np.zeros((n, N))
    for u in range(n):
        I_mem_all[u] = 0.5 * np.sum(np.log(1.0 + k_e * v_mem[u][None, :]), axis=1)

    # Pragmatic terms: psi^{(u)}_{B_j(1)}(q_u) and psi^{(j)}_{B_j(1)}(q_C)
    # Under (P1), member u's own pragmatic term on co-member j's slots depends only on pi_j;
    # for definiteness give member u the same slot preferences on every slot (or its own).
    psi_j_under_C = np.zeros(n)
    psi_j_under_j = np.zeros(n)
    for j in range(n):
        pC, pj = 0.0, 0.0
        for idx_e in inc[j]:
            t2 = tau2[(j, idx_e)]
            m_s = mu_star[(j, idx_e)]
            pC += 0.5 * math.log(2.0 * math.pi * t2) + ((lam ** 2) * (v_C[idx_e] + 1.0) + m_s ** 2) / (2.0 * t2)
            pj += 0.5 * math.log(2.0 * math.pi * t2) + ((lam ** 2) * (v_mem[j, idx_e] + 1.0) + m_s ** 2) / (2.0 * t2)
        psi_j_under_C[j] = pC
        psi_j_under_j[j] = pj

    # G_C(pi) = -I_{q_C}(eta; o_B(pi)) + sum_j pi_j * psi_j_under_C[j]
    G_C = -I_C_all + bits @ psi_j_under_C

    # Own tilts T_j(1) = -[I_{q_j} - I_{q_C}](eta; o_{B_j(1)}) + psi_j(q_j) - psi_j(q_C)
    T_tilt = np.zeros(n)
    for j in range(n):
        I_j_own = sum(0.5 * math.log(1.0 + v_mem[j, idx_e]) for idx_e in inc[j])
        I_C_own = sum(0.5 * math.log(1.0 + v_C[idx_e]) for idx_e in inc[j])
        T_tilt[j] = -(I_j_own - I_C_own) + (psi_j_under_j[j] - psi_j_under_C[j])
    Phi = G_C + bits @ T_tilt

    # Member u's EFE G_u(pi) (using member j's slot preferences for j's slots under q_u):
    G_mem = np.zeros((n, N))
    R_mem = np.zeros((n, N))
    for u in range(n):
        # Pragmatic term of all opened slots under q_u
        psi_u_on_j = np.zeros(n)
        for j in range(n):
            val = 0.0
            for idx_e in inc[j]:
                t2 = tau2[(j, idx_e)]
                m_s = mu_star[(j, idx_e)]
                val += 0.5 * math.log(2.0 * math.pi * t2) + ((lam ** 2) * (v_mem[u, idx_e] + 1.0) + m_s ** 2) / (2.0 * t2)
            psi_u_on_j[j] = val
        G_mem[u] = -I_mem_all[u] + bits @ psi_u_on_j

        # Direct definition of R_u(pi) = [I_{q_u} - I_{q_C}](o_{B_u(pi_u)}; o_{A_{-u}})
        # By chain rule: I(o_A; o_{A_{-u}}) = I(eta; o_A) + I(eta; o_{A_{-u}}) - I(eta; o_{A \cup A_{-u}})
        s_without_u = s_idx & (~(1 << u))
        I_u_own_vec = bits[:, u] * sum(0.5 * math.log(1.0 + v_mem[u, idx_e]) for idx_e in inc[u])
        I_C_own_vec = bits[:, u] * sum(0.5 * math.log(1.0 + v_C[idx_e]) for idx_e in inc[u])
        red_u = I_u_own_vec + I_mem_all[u, s_without_u] - I_mem_all[u]
        red_C = I_C_own_vec + I_C_all[s_without_u] - I_C_all
        R_mem[u] = red_u - red_C

    return G_mem, G_C, Phi, R_mem, bits


def build_T_from_G(n, G_mem, gamma):
    """Build exact 2^n x 2^n transition matrix T from G_mem(u, pi) with uniform habits."""
    N = 1 << n
    T = np.zeros((N, N))
    for s in range(N):
        for i in range(n):
            s0 = s & (~(1 << i))
            s1 = s | (1 << i)
            dG = G_mem[i, s1] - G_mem[i, s0]
            lr = -gamma * dG
            if lr >= 0:
                p1 = 1.0 / (1.0 + math.exp(-min(lr, 500.0)))
                p0 = 1.0 - p1
            else:
                e = math.exp(max(lr, -500.0))
                p1 = e / (1.0 + e)
                p0 = 1.0 / (1.0 + e)
            T[s, s0] += p0 / n
            T[s, s1] += p1 / n
    return T


def solve_dense_stationary(T):
    N = T.shape[0]
    A = T.T - np.eye(N)
    A[-1, :] = 1.0
    b = np.zeros(N)
    b[-1] = 1.0
    p = np.linalg.solve(A, b)
    res = np.max(np.abs(p @ T - p))
    cond = np.linalg.cond(A)
    return p, res, cond


def power_iter_stationary(T, tol=1e-13, max_sq=45):
    """Channel 2 independent solver: repeated squaring T^(2^k) with row renormalization (no LU)."""
    M = T.copy()
    for k in range(max_sq):
        M_next = M @ M
        M_next /= M_next.sum(axis=1, keepdims=True)
        diff = np.max(np.abs(M_next - M_next[0:1, :]))
        M = M_next
        if diff < tol:
            p = M.mean(axis=0)
            p /= p.sum()
            return p, k + 1, np.max(np.abs(p @ T - p))
    p = M.mean(axis=0)
    p /= p.sum()
    return p, max_sq, np.max(np.abs(p @ T - p))


def min_tv_to_rank1_2x2(pA, pB, pC, pD):
    Sp = pA + pB + pC + pD
    def obj(params):
        x, y, S = params
        qa, qb, qc, qd = S*x*y, S*(1-x)*y, S*x*(1-y), S*(1-x)*(1-y)
        return 0.5 * (abs(pA - qa) + abs(pB - qb) + abs(pC - qc) + abs(pD - qd) + abs((1 - Sp) - (1 - S)))
    best = 1.0
    best_p = (0.5, 0.5, Sp)
    for x0 in np.linspace(0.0, 1.0, 25):
        for y0 in np.linspace(0.0, 1.0, 25):
            for S0 in [Sp, 1.0]:
                v = obj((x0, y0, S0))
                if v < best:
                    best = v
                    best_p = (x0, y0, S0)
    res = minimize(obj, best_p, method='Nelder-Mead', options={'xatol': 1e-13, 'fatol': 1e-13})
    x, y, S = np.clip(res.x, 0.0, 1.0)
    return min(best, obj((x, y, S)))


# =============================================================================
# SECTION 0: Convention lock test values
# =============================================================================
print("=== SECTION 0: CONVENTION LOCK TEST VALUES ===")
v_test = 1.0
I_test = I_red(v_test)
I_exact = 0.5 * math.log(4.0 / 3.0)
v_back = v_from_I(I_test)
assert abs(I_test - I_exact) < 1e-15
assert abs(v_back - 1.0) < 1e-15
print(f"I_red(1) = {I_test:.15f} (exact 0.5*ln(4/3) = {I_exact:.15f}), v_from_I(I_red(1)) = {v_back:.15f}")

# TV test value: TV((0.8, 0.2), (0.3, 0.7)) = 0.5
tv_test = 0.5 * (abs(0.8 - 0.3) + abs(0.2 - 0.7))
assert abs(tv_test - 0.5) < 1e-15
print(f"TV((0.8,0.2),(0.3,0.7)) = {tv_test:.15f}")


# =============================================================================
# SECTION 1: Claim C1 (n = 2 binary non-uniformity in gamma, 2 channels + negative control)
# =============================================================================
print("\n=== SECTION 1: CLAIM C1 (n=2, pure non-potential vs Hodge projection, two channels) ===")

def n2_exact_decimal(I_C, delta, h, eps, gamma):
    """Channel 2: Exact 4-spanning-tree formula in 80-digit Decimal arithmetic."""
    g = Decimal(str(gamma))
    c1 = Decimal(str(-h - eps))
    c2 = Decimal(str(-h))
    I1 = Decimal(str(I_C + delta))
    I2 = Decimal(str(I_C - delta))

    def sig(x):
        # 1 / (1 + exp(-x))
        if x >= 0:
            return Decimal(1) / (Decimal(1) + (-x).exp())
        ex = x.exp()
        return ex / (Decimal(1) + ex)

    # Transition probabilities (factor 1/2 omitted since it cancels across all 3-edge trees)
    p10_0 = sig(-g * c1)          # 00 -> 10
    p00_10 = sig(g * c1)          # 10 -> 00
    p01_0 = sig(-g * c2)          # 00 -> 01
    p00_01 = sig(g * c2)          # 01 -> 00
    p11_10 = sig(-g * (c2 + I2))  # 10 -> 11
    p10_11 = sig(g * (c2 + I2))   # 11 -> 10
    p11_01 = sig(-g * (c1 + I1))  # 01 -> 11
    p01_11 = sig(g * (c1 + I1))   # 11 -> 01

    # All 4 spanning trees for each root on the 4-cycle 00 - 10 - 11 - 01 - 00:
    W01 = (p11_10 * p01_11 * p01_0
           + p00_10 * p01_0 * p01_11
           + p10_11 * p00_10 * p01_0
           + p10_0 * p11_10 * p01_11)
    W10 = (p11_01 * p10_11 * p10_0
           + p00_01 * p10_0 * p10_11
           + p01_11 * p00_01 * p10_0
           + p01_0 * p11_01 * p10_11)
    W00 = (p00_10 * p10_11 * p00_01
           + p00_10 * p01_11 * p00_01
           + p11_10 * p01_11 * p00_01
           + p11_01 * p10_11 * p00_10)
    W11 = (p10_0 * p11_10 * p11_01
           + p01_0 * p11_01 * p11_10
           + p00_10 * p01_0 * p11_01
           + p00_01 * p10_0 * p11_10)
    Z = W00 + W10 + W01 + W11
    p_inf = [W00 / Z, W10 / Z, W01 / Z, W11 / Z]

    # Exact Gibbs law for Phi and for Phi_Hodge = Phi + (delta/2)*(pi_1 - pi_2)
    def gibbs(energies):
        mE = min(energies)
        ws = [(-g * (e - mE)).exp() for e in energies]
        s = sum(ws)
        return [w / s for w in ws]

    E_Phi = [Decimal(0), c1, c2, c1 + c2 + Decimal(str(I_C))]
    d2 = Decimal(str(delta)) / Decimal(2)
    E_Hodge = [Decimal(0), c1 + d2, c2 - d2, c1 + c2 + Decimal(str(I_C))]
    p_Phi = gibbs(E_Phi)
    p_Hodge = gibbs(E_Hodge)

    tv_Phi = sum(abs(a - b) for a, b in zip(p_inf, p_Phi)) / Decimal(2)
    tv_Hodge = sum(abs(a - b) for a, b in zip(p_inf, p_Hodge)) / Decimal(2)
    return p_inf, p_Phi, p_Hodge, tv_Phi, tv_Hodge


I_C_2, delta_2, h_2, eps_2 = 0.5, 0.01, 0.4, 0.015  # delta < eps < 2*delta
# Channel 1: Full linear-Gaussian slot model for n=2
edges_2 = [(0, 1)]
_, inc_2, v_C_2, v_mem_2, lam_2, tau2_2, mu_2, _, _ = build_explicit_lg_model(
    2, edges_2, [], [(0, 1)], I_C_2, 1.0, delta_2, np.array([-h_2 - eps_2, -h_2])
)
G_mem_2, G_C_2, Phi_2, R_mem_2, bits_2 = compute_exact_G_from_lg(
    2, edges_2, inc_2, v_C_2, v_mem_2, lam_2, tau2_2, mu_2
)
# Check decomposition lem:agy-decomposition on n=2
for i in range(2):
    # G_i(1, pi_{-i}) - G_i(0, pi_{-i}) == (Phi + R_i)(1, pi_{-i}) - (Phi + R_i)(0, pi_{-i})
    for s in range(4):
        s0 = s & (~(1 << i))
        s1 = s | (1 << i)
        lhs = G_mem_2[i, s1] - G_mem_2[i, s0]
        rhs = (Phi_2[s1] + R_mem_2[i, s1]) - (Phi_2[s0] + R_mem_2[i, s0])
        assert abs(lhs - rhs) < 1e-14
print(f"n=2 parameters: I_C={I_C_2}, delta={delta_2}, h={h_2}, eps={eps_2} (delta < eps < 2*delta)")
print(f"  lem:agy-decomposition verified to <1e-14; Thompson distances: Th_1={abs(math.log(v_mem_2[0,0]/v_C_2[0])):.6f}, Th_2={abs(math.log(v_mem_2[1,0]/v_C_2[0])):.6f}")

for gamma in [1, 10, 50, 100, 200, 500, 2000]:
    p_inf_d, p_Phi_d, p_Hodge_d, tv_Phi_d, tv_Hodge_d = n2_exact_decimal(I_C_2, delta_2, h_2, eps_2, gamma)
    ch_diff_str = "N/A (float64 underflow)"
    if gamma <= 200:
        T2 = build_T_from_G(2, G_mem_2, gamma)
        p_inf_f, res_f, cond_f = solve_dense_stationary(T2)
        # Map bit order: s=0:(0,0), s=1:(1,0), s=2:(0,1), s=3:(1,1)
        ch_diff = max(abs(p_inf_f[k] - float(p_inf_d[k])) for k in range(4))
        tol_f = 1e-11 if gamma <= 100 else 1e-6
        assert ch_diff < tol_f and res_f < 1e-13, f"gamma={gamma}: ch_diff={ch_diff}, res={res_f}, cond={cond_f}"
        ch_diff_str = f"{ch_diff:.2e} (cond={cond_f:.1e})"
    print(f"  gamma={gamma:4d}: P_inf(0,1)={float(p_inf_d[2]):.8f}, TV(Phi)={float(tv_Phi_d):.8f}, TV(Phi_Hodge)={float(tv_Hodge_d):.8f}, |Ch1-Ch2|={ch_diff_str}")

# Planted-error negative control for C1: eps = 0.025 > 2*delta = 0.020
p_ctrl, _, _, tv_ctrl, tv_hodge_ctrl = n2_exact_decimal(I_C_2, delta_2, h_2, 0.025, 2000)
print(f"  [NEGATIVE CONTROL eps=0.025 > 2*delta] gamma=2000: P_inf(0,1)={float(p_ctrl[2]):.4e}, TV(Phi)={float(tv_ctrl):.4e} (blowup VANISHES as predicted)")
assert float(tv_ctrl) < 1e-3


# =============================================================================
# SECTION 2: Claim C2 (Gear-train topology, exact harmonicity, LG realization, energy landscape)
# =============================================================================
print("\n=== SECTION 2: CLAIM C2 (Gear-train topology, harmonicity, LG model, landscape) ===")

# 2a. Exact Hodge harmonicity (delta^* R)(pi) = 0 and sum_u R_u(pi) = 0 on ALL 2^4=16 gear-0 states
delta_sym = 0.01
max_div = 0.0
max_sum = 0.0
for bits4 in product([0, 1], repeat=4):
    # R_i(pi) = delta * pi_i * (pi_{i+1} - pi_{i-1}) for i in {0,1,2,3} mod 4
    R_vals = [delta_sym * bits4[i] * (bits4[(i + 1) % 4] - bits4[(i - 1) % 4]) for i in range(4)]
    div_val = sum((1 - 2 * bits4[i]) * delta_sym * (bits4[(i + 1) % 4] - bits4[(i - 1) % 4]) for i in range(4))
    max_div = max(max_div, abs(div_val))
    max_sum = max(max_sum, abs(sum(R_vals)))
assert max_div == 0.0 and max_sum == 0.0
print(f"Exact Hodge harmonicity on all 16 gear-0 states (hence all 2^n profiles): max|delta^* R|={max_div:.1e}, max|sum R_i|={max_sum:.1e}")

# 2b. Topology & checkpoint step counts for m = 2, 3, 4, 5, 6
for m in [2, 3, 4, 5, 6]:
    ok, geom, pinfo = analyze_path_topology(m)
    assert ok, f"Topology failed for m={m}"
    n, gear_nodes, adj_edges, wall_edges, motor_edges = geom
    path, s_steps = pinfo
    E_tot = len(adj_edges) + len(wall_edges)
    E_formula = 14 if m == 2 else 68 * m - 138
    assert n == 8 * m - 9
    assert len(path) == 3 * (1 << m) - 5
    assert s_steps[-1] == (1 << m)
    assert E_tot == E_formula
    hi_nodes = {gear_nodes[m - 1][0], gear_nodes[m - 1][2]}
    lo_nodes = {gear_nodes[m - 2][0], gear_nodes[m - 2][2]} if m == 2 else {gear_nodes[m - 2][1], gear_nodes[m - 2][5]}
    cps = [s_steps[k] for k in range(len(path)) if path[k][m - 1] in hi_nodes and path[k][m - 2] in lo_nodes]
    assert cps == [0, 1 << (m - 1), 1 << (m - 1), 1 << m]
    n_top = sum(1 for x in s_steps if x == (1 << m))
    assert n_top == m - 1
    print(f"  m={m}, n={n:2d}, dim(eta)={E_tot:3d}: |P_m|={len(path):3d} (3*2^m-5), motor_steps={s_steps[-1]:2d} (2^m), cp_steps={cps}, n_top={n_top}")

# 2c. Planted-error negative control on topology: drop ONE inter-gear wall edge in m=2
ok_bad, info_bad, _ = analyze_path_topology(2, drop_wall_idx=5)  # drop an inter-gear wall edge
print(f"  [NEGATIVE CONTROL dropped 1 wall edge on m=2] is_1D_path={ok_bad}, stats=(valid,endpts,min_deg,max_deg)={info_bad}")
assert not ok_bad

# 2d. Exhaustive energy landscape check on ALL 2^7=128 (m=2) and ALL 2^15=32768 (m=3) states
I_adj, I_wall, h_g = 1.0, 5.0, 0.90
Delta_g = I_adj - h_g  # 0.10
b_g = 0.01             # Delta_g / 10
for m in [2, 3]:
    ok, (n, gear_nodes, adj_edges, wall_edges, motor_edges), (path, s_steps) = analyze_path_topology(m)
    N = 1 << n
    I_C_mat = np.zeros((n, n))
    for u, v in adj_edges:
        I_C_mat[u, v] = I_C_mat[v, u] = I_adj
    for u, v in wall_edges:
        I_C_mat[u, v] = I_C_mat[v, u] = I_wall
    s_idx = np.arange(N, dtype=np.int32)
    bits = ((s_idx[:, None] >> np.arange(n)[None, :]) & 1).astype(np.float64)
    c_u = np.full(n, -h_g)
    Phi_u = bits @ c_u + 0.5 * np.sum((bits @ I_C_mat) * bits, axis=1)
    E0 = -m * h_g
    p_masks = {sum(1 << u for u in st) for st in path}
    b_masks = {sum(1 << u for u in (set(path[k]) | set(path[k + 1]))) for k in range(len(path) - 1)}
    V0 = p_masks | b_masks
    mP = np.array([k in p_masks for k in range(N)])
    mB = np.array([k in b_masks for k in range(N)])
    mV1 = ~(mP | mB)
    assert np.max(np.abs(Phi_u[mP] - E0)) < 1e-13
    assert np.max(np.abs(Phi_u[mB] - (E0 + Delta_g))) < 1e-13
    v1_gap = Phi_u[mV1].min() - E0
    assert v1_gap >= 2 * Delta_g - 1e-12

    # 4-checkpoint landscape
    c_cp = np.full(n, -h_g)
    lo_vals = (0, 2) if m == 2 else (1, 5)
    for u in [gear_nodes[m - 2][r] for r in lo_vals] + [gear_nodes[m - 1][0], gear_nodes[m - 1][2]]:
        c_cp[u] -= b_g
    Phi_cp = bits @ c_cp + 0.5 * np.sum((bits @ I_C_mat) * bits, axis=1)
    min_P_V1 = min(Phi_cp[st ^ (1 << i)] - Phi_cp[st] for st in p_masks for i in range(n) if (st ^ (1 << i)) not in V0)
    min_B_V1 = min(Phi_cp[st ^ (1 << i)] - Phi_cp[st] for st in b_masks for i in range(n) if (st ^ (1 << i)) not in V0)
    assert min_P_V1 >= h_g - 1e-12 and min_B_V1 >= Delta_g - b_g - 1e-12
    print(f"  Landscape m={m} (all {N} states): unif V1_gap={v1_gap:.4f} (>=2*Delta={2*Delta_g:.2f}), cp min_dPhi(P->V1)={min_P_V1:.4f}, min_dPhi(B->V1)={min_B_V1:.4f} (>=Delta-b={Delta_g-b_g:.2f})")


# =============================================================================
# SECTION 3: Claims C3 & C4 (Full 2^7=128 exact linear-Gaussian chain, 2 channels + controls)
# =============================================================================
print("\n=== SECTION 3: CLAIMS C3 & C4 (m=2, n=7, N=128 full explicit LG model, two channels) ===")
ok, (n2, gnodes2, adj2, wall2, mot2), (path2, s2) = analyze_path_topology(2)
st_start = sum(1 << u for u in path2[0])
st_end = sum(1 << u for u in path2[-1])
st_A = (1 << gnodes2[0][0]) | (1 << gnodes2[1][0])
st_B = (1 << gnodes2[0][2]) | (1 << gnodes2[1][0])
st_D = (1 << gnodes2[0][2]) | (1 << gnodes2[1][2])
st_C = (1 << gnodes2[0][0]) | (1 << gnodes2[1][2])
p_masks2 = [sum(1 << u for u in st) for st in path2]

# --- 3a. Claim C3: Uniform-cost model, fixed lambda = 2^2 * gamma * sigma_max ---
print("\n--- 3a. Claim C3 (Uniform-cost, fixed lambda = 4*gamma*sigma_max as gamma grows) ---")
for lam_target in [1.0, 2.0, 4.0]:
    # Limiting theoretical distribution mu_lambda on P_2
    w_lim = np.array([math.exp(2.0 * lam_target * sk / 4.0) for sk in s2])
    mu_lim = w_lim / w_lim.sum()
    unif_P = np.full(len(path2), 1.0 / len(path2))
    tv_lim = 0.5 * np.sum(np.abs(mu_lim - unif_P))
    print(f"  lambda={lam_target:.1f} (limiting ln(p_end/p_start)={2*lam_target:.4f}, limiting TV={tv_lim:.6f}):")
    for gamma in [40, 80, 120]:
        delta = lam_target / (4.0 * gamma)
        c_unif = np.full(n2, -h_g)
        edges_m, inc_m, vC_m, vmem_m, lam_m, tau2_m, mu_m, _, _ = build_explicit_lg_model(
            n2, adj2, wall2, mot2, I_adj, I_wall, delta, c_unif, potential_control=False
        )
        G_mem, G_C, Phi, R_mem, bits = compute_exact_G_from_lg(
            n2, edges_m, inc_m, vC_m, vmem_m, lam_m, tau2_m, mu_m
        )
        # Verify lem:agy-decomposition & sigma_max directly from explicit LG model
        max_decomp = 0.0
        sigmas = np.zeros(n2)
        for i in range(n2):
            for s in range(1 << n2):
                s0 = s & (~(1 << i))
                s1 = s | (1 << i)
                err = abs((G_mem[i, s1] - G_mem[i, s0]) - ((Phi[s1] + R_mem[i, s1]) - (Phi[s0] + R_mem[i, s0])))
                if err > max_decomp:
                    max_decomp = err
                if abs(R_mem[i, s1] - R_mem[i, s0]) > sigmas[i]:
                    sigmas[i] = abs(R_mem[i, s1] - R_mem[i, s0])
        assert max_decomp < 1e-12, f"max_decomp={max_decomp}"
        assert abs(sigmas.max() - delta) < 1e-12, f"sigmas={sigmas}, delta={delta}, diff={abs(sigmas.max()-delta)}"
        assert np.max(sigmas[4:]) < 1e-13, f"sigmas[4:]={sigmas[4:]}"

        # Channel 1: Dense LU linear solve
        T = build_T_from_G(n2, G_mem, gamma)
        p_ch1, res1, cond1 = solve_dense_stationary(T)
        # Channel 2: Repeated squaring T^(2^k) (completely independent of LU)
        p_ch2, k_sq, res2 = power_iter_stationary(T)
        ch_diff = np.max(np.abs(p_ch1 - p_ch2))
        assert ch_diff < 1e-8 and res1 < 1e-13 and res2 < 1e-13, f"gamma={gamma}: ch_diff={ch_diff}, res1={res1}, res2={res2}, cond1={cond1}"

        p_Phi = np.exp(-gamma * (Phi - Phi.min()))
        p_Phi /= p_Phi.sum()
        tv_Phi = 0.5 * np.sum(np.abs(p_ch1 - p_Phi))
        lr_end_start = math.log((p_ch1[st_end] / p_Phi[st_end]) / (p_ch1[st_start] / p_Phi[st_start]))
        mass_P = sum(p_ch1[idx] for idx in p_masks2)
        print(f"    gamma={gamma:3d}, sigma_max={delta:.6f}: mass(P_2)={mass_P:.6f}, ln_ratio={lr_end_start:.6f}, TV_Phi={tv_Phi:.6f}, |Ch1-Ch2|={ch_diff:.2e}")

# --- 3b. Claim C4: 4-checkpoint model, Class 2 lower bound & correlated q_C trade-off ---
print("\n--- 3b. Claim C4 (4-checkpoint model, b=0.01=Delta/10, Class 2 TV lower bound) ---")
for lam_target in [1.0, 2.0, 4.0]:
    p_lim = math.exp(lam_target) / (2.0 * (1.0 + math.exp(lam_target)))
    lb_lim = 2.0 * math.sqrt(p_lim) - 1.0
    print(f"  lambda={lam_target:.1f} (limiting p_B=p_C={p_lim:.6f}, analytic LB 2*sqrt(p)-1={lb_lim:.6f}):")
    for gamma in [100, 140, 180]:
        delta = lam_target / (4.0 * gamma)
        c_cp = np.full(n2, -h_g)
        for u in [gnodes2[0][0], gnodes2[0][2], gnodes2[1][0], gnodes2[1][2]]:
            c_cp[u] -= b_g
        c_cp[gnodes2[1][2]] += 4.0 * delta  # tilt +2^m * delta = lam / gamma

        edges_m, inc_m, vC_m, vmem_m, lam_m, tau2_m, mu_m, _, _ = build_explicit_lg_model(
            n2, adj2, wall2, mot2, I_adj, I_wall, delta, c_cp, potential_control=False
        )
        G_mem, G_C, Phi, R_mem, bits = compute_exact_G_from_lg(
            n2, edges_m, inc_m, vC_m, vmem_m, lam_m, tau2_m, mu_m
        )
        T = build_T_from_G(n2, G_mem, gamma)
        p_ch1, res1, cond1 = solve_dense_stationary(T)
        p_ch2, k_sq, res2 = power_iter_stationary(T)
        ch_diff = np.max(np.abs(p_ch1 - p_ch2))
        assert ch_diff < 5e-6 and res1 < 1e-13 and res2 < 1e-13, f"gamma={gamma}: ch_diff={ch_diff}, res1={res1}, res2={res2}, cond1={cond1}"

        pA, pB, pC, pD = p_ch1[st_A], p_ch1[st_B], p_ch1[st_C], p_ch1[st_D]
        lb_analytic = max(0.0, 2.0 * math.sqrt(min(pB, pC)) - 1.0)
        lb_num = min_tv_to_rank1_2x2(pA, pB, pC, pD)
        assert lb_num >= lb_analytic - 1e-9
        print(f"    gamma={gamma:3d}, sigma_max={delta:.6f}: cond={cond1:.1e}, p(A,B,C,D)=({pA:.4f},{pB:.4f},{pC:.4f},{pD:.4f}), sum={pA+pB+pC+pD:.4f}, 2sqrt(p)-1={lb_analytic:.5f}, num_LB={lb_num:.5f}, |Ch1-Ch2|={ch_diff:.2e}")

# Correlated-q_C trade-off bound R*(2*sqrt(p_lambda) - R) for m=3,4,5,6 at lambda=4.0
print("\n  Correlated-q_C trade-off bound R*(2*sqrt(p_lam)-R) at q_C=q_C^* (lambda=4.0, p_lam=0.491007):")
p_lam4 = math.exp(4.0) / (2.0 * (1.0 + math.exp(4.0)))
for m_tr in [3, 4, 5, 6]:
    gs = 4.0 / (1 << m_tr)
    R_tr = math.exp(0.5 * gs)
    lb_tr = R_tr * (2.0 * math.sqrt(p_lam4) - R_tr)
    assert lb_tr > 0.1
    print(f"    m={m_tr} (n={8*m_tr-9:2d}): gamma*sigma_max={gs:.5f}, R={R_tr:.5f}, R*(2*sqrt(p)-R)={lb_tr:.5f}")

# --- 3c. Planted-error negative controls for C3 & C4 ---
print("\n--- 3c. Planted-error negative controls ---")
# Control A: Potential perturbation (+delta, +delta) instead of harmonic (+delta, -delta)
gamma_ctrl, lam_ctrl = 100, 4.0
delta_ctrl = lam_ctrl / (4.0 * gamma_ctrl)
c_unif = np.full(n2, -h_g)
edges_p, inc_p, vC_p, vmem_p, lam_p, tau2_p, mu_p, _, _ = build_explicit_lg_model(
    n2, adj2, wall2, mot2, I_adj, I_wall, delta_ctrl, c_unif, potential_control=True
)
G_mem_p, _, Phi_p, R_mem_p, bits_p = compute_exact_G_from_lg(
    n2, edges_p, inc_p, vC_p, vmem_p, lam_p, tau2_p, mu_p
)
# Check Hodge divergence is NONZERO for potential perturbation
div_p = max(
    abs(sum(R_mem_p[i, s ^ (1 << i)] - R_mem_p[i, s] for i in range(n2)))
    for s in range(1 << n2)
)
T_p = build_T_from_G(n2, G_mem_p, gamma_ctrl)
p_pot, res_p, _ = solve_dense_stationary(T_p)
db_res = np.max(np.abs(p_pot[:, None] * T_p - p_pot[None, :] * T_p.T))
lr_pot = math.log(p_pot[st_end] / p_pot[st_start])
print(f"  [NEGATIVE CONTROL potential (+delta,+delta)] max|delta^* R|={div_p:.4f} (!=0), DB_res={db_res:.2e}, ln(p_end/p_start)={lr_pot:.2e} (0 instead of {2*lam_ctrl:.1f})")
assert div_p > 0.01 and db_res < 1e-14 and abs(lr_pot) < 1e-10

# Control B: Planted wrong lower bound (2*sqrt(p) - 0.5 instead of 2*sqrt(p) - 1) fails against an explicit rank-1 Q
p_test = 0.45
# Best rank-1 Q has x = sqrt(p), y = 1 - sqrt(p), S = 1 -> qB = x*(1-y) = p? Wait: qA = x*y, qB = (1-x)*y, qC = x*(1-y), qD = (1-x)*(1-y)
# Choose x = sqrt(p), 1-y = sqrt(p) -> y = 1 - sqrt(p):
# qC = p, qB = (1-sqrt(p))^2, qA = qD = sqrt(p)*(1-sqrt(p))
x_opt = math.sqrt(p_test)
y_opt = 1.0 - math.sqrt(p_test)
qA = x_opt * y_opt
qB = (1.0 - x_opt) * y_opt
qC = x_opt * (1.0 - y_opt)
qD = (1.0 - x_opt) * (1.0 - y_opt)
assert abs(qA * qD - qB * qC) < 1e-15
tv_exact_opt = 0.5 * (abs((0.5 - p_test) - qA) + abs(p_test - qB) + abs(p_test - qC) + abs((0.5 - p_test) - qD))
true_lb = 2.0 * math.sqrt(p_test) - 1.0
wrong_lb = 2.0 * math.sqrt(p_test) - 0.5
print(f"  [NEGATIVE CONTROL wrong TV LB at p={p_test}] actual TV(P, Q_rank1)={tv_exact_opt:.6f}, true_LB={true_lb:.6f} (holds), wrong_LB={wrong_lb:.6f} (VIOLATED!)")
assert tv_exact_opt >= true_lb - 1e-14 and tv_exact_opt < wrong_lb - 0.1

print("\nALL CHECKS AND NEGATIVE CONTROLS PASSED.")
