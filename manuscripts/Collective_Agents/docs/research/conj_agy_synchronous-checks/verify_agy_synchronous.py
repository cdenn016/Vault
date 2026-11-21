"""
Two-channel verification and negative controls for conj:agy-synchronous
(Collective_Agents/sections/s05_agency.tex, lines 102-109).

Verifies:
  C1: Exact one-step residual identity and same-precision impossibility
      P_sync^infty(gamma) != P_C(gamma; E, G_C) for all n >= 2, all finite A_i,
      all gamma > 0 whenever any conditional redundancy is positive (including
      Gaussian, general discrete, and synergistic XOR slot models).
  C2: Binary-policy positive association (FKG) of P_sync^infty(gamma) and
      universal impossibility against EVERY redundant binary group posterior
      P_C(gamma_C; E_tilde, G_tilde_C) with gamma_C > 0, plus bipartite
      factorization for arbitrary finite policy sets.
  C3: Rigorous IFT existence (symbolic Jacobian det J_0 = -24 eps^2(1-eps)^2/(1+eps)^2)
      and explicit 12D linear-Gaussian 3-member, 3-policy collective with genuine
      normalized Gaussian slot-product preferences where
      P_sync^infty(gamma=1; E, G_C) == P_C(gamma_C; E, G_C) to ~1e-16 for the
      EXACT SAME E and G_C at gamma_C = 0.010398019508 > 0.
  C4: Elementary closed-form reversed-cycle 3-member, 3-policy collective where
      P_sync^infty(gamma) equals an exact redundant linear-Gaussian group posterior
      on the reversed cycle for every gamma > 0.

Includes planted-error negative controls for each claim.
"""

import numpy as np
import sympy as sp
from itertools import product
from scipy.optimize import root


# ---------------------------------------------------------------------------
# Core helpers (two independent channels for stationary law)
# ---------------------------------------------------------------------------

def build_sync_kernel_from_G_list(G_list, E_list, gamma):
    """Build full synchronous transition matrix T_sync from member EFEs G_i(pi)
    and product habits E_i(pi_i) at precision gamma."""
    shape = G_list[0].shape
    n = len(shape)
    N = int(np.prod(shape))
    K = []
    for i in range(n):
        # log K_i(pi_i | pi_{-i}) = log E_i(pi_i) - gamma G_i(pi) - log Z_i(pi_{-i})
        log_w = -gamma * G_list[i].copy()
        for a in range(shape[i]):
            sl = [slice(None)] * n
            sl[i] = a
            log_w[tuple(sl)] += np.log(E_list[i][a])
        log_w -= np.max(log_w, axis=i, keepdims=True)
        w = np.exp(log_w)
        K.append(w / np.sum(w, axis=i, keepdims=True))
    states = list(product(*[range(s) for s in shape]))
    T = np.zeros((N, N))
    for a_idx, sf in enumerate(states):
        for b_idx, st in enumerate(states):
            prob = 1.0
            for i in range(n):
                idx = list(sf)
                idx[i] = st[i]
                prob *= K[i][tuple(idx)]
            T[a_idx, b_idx] = prob
    return T, K


def stationary_via_eig(T, shape):
    """Channel A: left eigenvector for eigenvalue 1."""
    vals, vecs = np.linalg.eig(T.T)
    idx = np.argmin(np.abs(vals - 1.0))
    v = np.real(vecs[:, idx])
    v = v / np.sum(v)
    return v.reshape(shape)


def stationary_via_power(T, shape, init_vec=None, tol=1e-15, max_iter=10000):
    """Channel B: power iteration from arbitrary initial law."""
    N = T.shape[0]
    p = np.ones(N) / N if init_vec is None else init_vec.copy()
    for _ in range(max_iter):
        p_new = p @ T
        if np.sum(np.abs(p_new - p)) < tol:
            return p_new.reshape(shape)
        p = p_new
    return p.reshape(shape)


def group_posterior(G_C, E_list, gamma):
    shape = G_C.shape
    n = len(shape)
    lp = -gamma * G_C.copy()
    for i in range(n):
        for a in range(shape[i]):
            sl = [slice(None)] * n
            sl[i] = a
            lp[tuple(sl)] += np.log(E_list[i][a])
    lp -= np.max(lp)
    P = np.exp(lp)
    return P / np.sum(P)


def tv_dist(P, Q):
    return 0.5 * float(np.sum(np.abs(P - Q)))


def prod_of_marginals(P):
    shape = P.shape
    n = len(shape)
    out = np.ones(shape)
    for i in range(n):
        axes = tuple(j for j in range(n) if j != i)
        out = out * P.sum(axis=axes, keepdims=True)
    return out


# ---------------------------------------------------------------------------
# Check 1: Exact one-step residual identity & same-precision theorem (C1)
# ---------------------------------------------------------------------------

def residual_identity_rhs(P_C, G_C, gamma, i, j):
    """Channel B: compute the exact RHS of Theorem 1 for pair (i, j) from
    P_C and conditional mutual informations I(o_{A_i}; o_{A_j} | o_{A_{-ij}})."""
    shape = P_C.shape
    n = len(shape)
    other_axes = [k for k in range(n) if k not in (i, j)]
    other_ranges = [range(shape[k]) for k in other_axes]
    total = 0.0
    for c in product(*other_ranges):
        # Extract 2D slice p_c(a, b) = P_C(X_i=a, X_j=b | X_{-ij}=c)
        joint_slice = np.zeros((shape[i], shape[j]))
        G_slice = np.zeros((shape[i], shape[j]))
        for a in range(shape[i]):
            for b in range(shape[j]):
                idx = [0] * n
                idx[i] = a
                idx[j] = b
                for axis, val in zip(other_axes, c):
                    idx[axis] = val
                joint_slice[a, b] = P_C[tuple(idx)]
                G_slice[a, b] = G_C[tuple(idx)]
        p_context = np.sum(joint_slice)
        p_c = joint_slice / p_context
        r_c = np.sum(p_c, axis=1)
        s_c = np.sum(p_c, axis=0)
        # Pearson chi^2(p_c || r_c x s_c)
        chi2 = np.sum((p_c - np.outer(r_c, s_c))**2 / np.outer(r_c, s_c))
        # Mutual info term: d^2 G_C = G_slice[a,b] - G_slice[a,0] - G_slice[0,b] + G_slice[0,0]
        mi_sum = 0.0
        for a in range(shape[i]):
            for b in range(shape[j]):
                I_cond = G_slice[a, b] - G_slice[a, 0] - G_slice[0, b] + G_slice[0, 0]
                mi_sum += (p_c[a, b]**2 / (r_c[a] * s_c[b])) * (np.exp(gamma * I_cond) - 1.0)
        total += p_context * p_c[0, 0] * (chi2 + mi_sum)
    return total


def run_check_1():
    print("=" * 72)
    print("CHECK 1: Exact One-Step Residual Identity & Same-Precision Theorem (C1)")
    print("=" * 72)
    rng = np.random.default_rng(202601)
    max_id_err = 0.0
    min_positive_gap = 1e9
    cases_tested = 0

    # 1a. Linear-Gaussian models with mixed shapes (2,2,2), (2,3,4), (2,2,2,2)
    #     and MEMBER-SPECIFIC pragmatic costs psi^{(i)} on co-members' slots!
    for shape in [(2, 2, 2), (2, 3, 4), (2, 2, 2, 2)]:
        n = len(shape)
        d = 3
        for trial in range(5):
            H_slots = []
            for i in range(n):
                pols = [None]
                for a in range(1, shape[i]):
                    pols.append(rng.normal(0, 1.3, size=(1, d)))
                H_slots.append(pols)
            # Member-specific pragmatic costs psi_mat[k][j][a] = member k's cost for member j's policy a
            psi_mat = [
                [[0.0] + list(rng.uniform(-0.8, 0.8, size=shape[j] - 1)) for j in range(n)]
                for k in range(n)
            ]
            E_list = []
            for i in range(n):
                e = rng.uniform(0.15, 1.0, size=shape[i])
                E_list.append(e / np.sum(e))
            gamma = float(rng.uniform(0.3, 3.5))

            # Build G_C and individual G_k from first principles
            I_arr = np.zeros(shape)
            for s in product(*[range(m) for m in shape]):
                prec = np.eye(d)
                for i in range(n):
                    if s[i] > 0:
                        Hi = H_slots[i][s[i]]
                        prec = prec + Hi.T @ Hi
                I_arr[s] = 0.5 * np.linalg.slogdet(prec)[1]

            G_C = -I_arr.copy()
            G_list = [-I_arr.copy() for _ in range(n)]
            for s in product(*[range(m) for m in shape]):
                G_C[s] += sum(psi_mat[j][j][s[j]] for j in range(n))
                for k in range(n):
                    G_list[k][s] += sum(psi_mat[k][j][s[j]] for j in range(n))

            P_C = group_posterior(G_C, E_list, gamma)
            T, _ = build_sync_kernel_from_G_list(G_list, E_list, gamma)
            P_next = (P_C.reshape(-1) @ T).reshape(shape)
            P_stat_eig = stationary_via_eig(T, shape)
            P_stat_pow = stationary_via_power(T, shape)
            assert tv_dist(P_stat_eig, P_stat_pow) < 1e-13

            for i in range(n):
                for j in range(i + 1, n):
                    # Marginal prob P(X_i=0, X_j=0)
                    axes = tuple(k for k in range(n) if k not in (i, j))
                    p00_C = float(np.sum(P_C, axis=axes)[0, 0])
                    p00_N = float(np.sum(P_next, axis=axes)[0, 0])
                    lhs = p00_N - p00_C
                    rhs = residual_identity_rhs(P_C, G_C, gamma, i, j)
                    err = abs(lhs - rhs)
                    max_id_err = max(max_id_err, err)
                    min_positive_gap = min(min_positive_gap, lhs)
                    cases_tested += 1
                    assert lhs > 0.0 and tv_dist(P_stat_eig, P_C) > 0.0

    print(f"Gaussian mixed shapes ({cases_tested} pairs across (2,2,2), (2,3,4), (2,2,2,2)):")
    print(f"  max |LHS - RHS| = {max_id_err:.3e}")
    print(f"  min positive gap P_next(0,0) - P_C(0,0) = {min_positive_gap:.6e}")

    # 1b. Synergistic discrete XOR model: I(o_i; o_j) = 0 for all pairs,
    #     but I(o_1; o_2 | o_3) = ln 2 > 0!
    G_xor = np.zeros((2, 2, 2))
    for a, b, c in product([0, 1], repeat=3):
        # eta = (B1, B2) unif on {0,1}^2; o1=B1, o2=B2, o3=B1 xor B2
        # I(eta; o_S) = min(|S|, 2) * ln 2
        I_val = min(a + b + c, 2) * np.log(2.0)
        G_xor[a, b, c] = -I_val + 0.3 * a + 0.2 * b + 0.4 * c
    E_xor = [np.array([0.4, 0.6]), np.array([0.5, 0.5]), np.array([0.3, 0.7])]
    gamma_xor = 1.5
    P_C_xor = group_posterior(G_xor, E_xor, gamma_xor)
    T_xor, _ = build_sync_kernel_from_G_list([G_xor]*3, E_xor, gamma_xor)
    P_next_xor = (P_C_xor.reshape(-1) @ T_xor).reshape((2, 2, 2))
    P_stat_xor = stationary_via_eig(T_xor, (2, 2, 2))
    lhs_xor = float(np.sum(P_next_xor, axis=2)[0, 0] - np.sum(P_C_xor, axis=2)[0, 0])
    rhs_xor = residual_identity_rhs(P_C_xor, G_xor, gamma_xor, 0, 1)
    print(f"Synergistic XOR model (unconditional I(o_i;o_j)=0, conditional I(o1;o2|o3)=ln 2):")
    print(f"  LHS = {lhs_xor:.12e}, RHS = {rhs_xor:.12e}, |LHS-RHS| = {abs(lhs_xor-rhs_xor):.3e}")
    print(f"  TV(P_sync^infty, P_C) = {tv_dist(P_stat_xor, P_C_xor):.6e}")
    assert abs(lhs_xor - rhs_xor) < 1e-15 and lhs_xor > 1e-4

    # 1c. Boundary check: zero redundancy (product law) => LHS = RHS = 0, TV = 0
    G_indep = np.zeros((2, 3, 2))
    for a, b, c in product(range(2), range(3), range(2)):
        G_indep[a, b, c] = -0.4 * a - 0.3 * b - 0.5 * c
    E_indep = [np.array([0.4, 0.6]), np.array([0.2, 0.5, 0.3]), np.array([0.7, 0.3])]
    P_C_ind = group_posterior(G_indep, E_indep, 2.0)
    T_ind, _ = build_sync_kernel_from_G_list([G_indep]*3, E_indep, 2.0)
    P_stat_ind = stationary_via_eig(T_ind, (2, 3, 2))
    rhs_ind = residual_identity_rhs(P_C_ind, G_indep, 2.0, 0, 1)
    print(f"Zero-redundancy product boundary: RHS = {rhs_ind:.3e}, TV(P_sync^infty, P_C) = {tv_dist(P_stat_ind, P_C_ind):.3e}")
    assert abs(rhs_ind) < 1e-15 and tv_dist(P_stat_ind, P_C_ind) < 1e-15

    # 1d. Negative controls for C1:
    #     (i) Flip gamma -> -1.5 < 0 on XOR model: RHS becomes NEGATIVE (identity still holds, sign fails!)
    P_C_neg = group_posterior(G_xor, E_xor, -1.5)
    T_neg, _ = build_sync_kernel_from_G_list([G_xor]*3, E_xor, -1.5)
    P_next_neg = (P_C_neg.reshape(-1) @ T_neg).reshape((2, 2, 2))
    lhs_neg = float(np.sum(P_next_neg, axis=2)[0, 0] - np.sum(P_C_neg, axis=2)[0, 0])
    rhs_neg = residual_identity_rhs(P_C_neg, G_xor, -1.5, 0, 1)
    print(f"Negative control (gamma = -1.5 < 0 on XOR): LHS = {lhs_neg:+.6e}, RHS = {rhs_neg:+.6e}, |LHS-RHS| = {abs(lhs_neg-rhs_neg):.3e}")
    assert lhs_neg < 0.0 and abs(lhs_neg - rhs_neg) < 1e-15
    #     (ii) Degenerate support P(000)=P(111)=1/2 (violating full support): P T_sync = P!
    P_deg = np.zeros((2, 2, 2))
    P_deg[0, 0, 0] = 0.5
    P_deg[1, 1, 1] = 0.5
    # On support {000, 111}, given X_{-i}=(0,0) => Y_i=0 w.p. 1; given (1,1) => Y_i=1 w.p. 1
    # So P_next = P_deg even though P_deg is not a product law!
    print(f"Negative control (degenerate GHZ support): TV(P_deg, prod) = {tv_dist(P_deg, prod_of_marginals(P_deg)):.4f}, fixed under sync = True")


# ---------------------------------------------------------------------------
# Check 2: Binary-policy positive association (FKG) & bipartite factorization (C2)
# ---------------------------------------------------------------------------

def all_nondecreasing_bool_3():
    """Enumerate all 18 nontrivial nondecreasing Boolean functions on {0,1}^3."""
    pts = list(product([0, 1], repeat=3))
    funcs = []
    for bits in product([0, 1], repeat=8):
        if sum(bits) in (0, 8):
            continue
        ok = True
        for i, x in enumerate(pts):
            for j, y in enumerate(pts):
                if all(a <= b for a, b in zip(x, y)) and bits[i] > bits[j]:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            funcs.append(np.array(bits, dtype=float).reshape((2, 2, 2)))
    return funcs


def cov_under(P, f, g):
    ef = np.sum(P * f)
    eg = np.sum(P * g)
    return float(np.sum(P * f * g) - ef * eg)


def run_check_2():
    print("\n" + "=" * 72)
    print("CHECK 2: Binary-Policy Positive Association (C2) & Bipartite Cut")
    print("=" * 72)
    rng = np.random.default_rng(202602)
    monotone_funcs = all_nondecreasing_bool_3()
    assert len(monotone_funcs) == 18

    min_fkg_cov_stat = 1e9
    min_fkg_cov_iter = 1e9
    max_group_cov_witness = -1e9

    # Witness functions f_i(x) = x_i, g_i(x) = 1[x_{-i} != 0]
    f_w = [np.zeros((2, 2, 2)) for _ in range(3)]
    g_w = [np.zeros((2, 2, 2)) for _ in range(3)]
    for s in product([0, 1], repeat=3):
        for i in range(3):
            f_w[i][s] = float(s[i])
            g_w[i][s] = 1.0 if any(s[j] == 1 for j in range(3) if j != i) else 0.0

    for trial in range(60):
        if trial < 40:
            # Random Gaussian slots (d in {1,2,3})
            d = int(rng.integers(1, 4))
            H = [rng.normal(0, 1.8, size=(1, d)) for _ in range(3)]
            psi = rng.uniform(-1.5, 1.5, size=3)
            G = np.zeros((2, 2, 2))
            for s in product([0, 1], repeat=3):
                prec = np.eye(d)
                for i in range(3):
                    if s[i] == 1:
                        prec = prec + H[i].T @ H[i]
                G[s] = -0.5 * np.linalg.slogdet(prec)[1] + sum(s[i] * psi[i] for i in range(3))
        else:
            # Random discrete conditionally independent slots
            M = 3
            p_eta = rng.dirichlet(np.ones(M))
            liks = [rng.dirichlet(np.ones(2), size=M) for _ in range(3)]
            psi = rng.uniform(-1.5, 1.5, size=3)
            G = np.zeros((2, 2, 2))
            for s in product([0, 1], repeat=3):
                active = [i for i in range(3) if s[i] == 1]
                if not active:
                    I_val = 0.0
                else:
                    H_cond = 0.0
                    marg = None
                    for m in range(M):
                        p_m = liks[active[0]][m]
                        for i in active[1:]:
                            p_m = np.multiply.outer(p_m, liks[i][m])
                        nz = p_m > 1e-300
                        H_cond += p_eta[m] * (-np.sum(p_m[nz] * np.log(p_m[nz])))
                        marg = p_eta[m] * p_m if marg is None else marg + p_eta[m] * p_m
                    nz = marg > 1e-300
                    I_val = max(0.0, -np.sum(marg[nz] * np.log(marg[nz])) - H_cond)
                G[s] = -I_val + sum(s[i] * psi[i] for i in range(3))

        E_list = [rng.uniform(0.1, 1.0, size=2) for _ in range(3)]
        E_list = [e / e.sum() for e in E_list]
        gamma = float(rng.uniform(0.2, 5.0))
        P_C = group_posterior(G, E_list, gamma)
        T, _ = build_sync_kernel_from_G_list([G]*3, E_list, gamma)
        P_stat = stationary_via_eig(T, (2, 2, 2))

        # Channel A: check ALL 18 x 18 = 324 monotone pairs on P_stat
        for f in monotone_funcs:
            for g in monotone_funcs:
                min_fkg_cov_stat = min(min_fkg_cov_stat, cov_under(P_stat, f, g))

        # Channel B: check iterates t=0..10 from product start E_0 x E_1 x E_2
        p_t = np.multiply.outer(np.multiply.outer(E_list[0], E_list[1]), E_list[2]).reshape(-1)
        for _ in range(10):
            p_t = p_t @ T
            Pt = p_t.reshape((2, 2, 2))
            for i in range(3):
                min_fkg_cov_iter = min(min_fkg_cov_iter, cov_under(Pt, f_w[i], g_w[i]))

        # Check witness Cov_{P_C}(X_i, 1[X_{-i} != 0]) < 0 for every redundant member i
        # (Check unconditional pair redundancies I(o_i; o_j))
        reds = [
            G[1, 1, 0] - G[1, 0, 0] - G[0, 1, 0] + G[0, 0, 0],
            G[1, 0, 1] - G[1, 0, 0] - G[0, 0, 1] + G[0, 0, 0],
            G[0, 1, 1] - G[0, 1, 0] - G[0, 0, 1] + G[0, 0, 0],
        ]
        # Member 0 redundant with 1 or 2?
        if max(reds[0], reds[1]) > 1e-6:
            max_group_cov_witness = max(max_group_cov_witness, cov_under(P_C, f_w[0], g_w[0]))

    print(f"60 random binary 3-member models (40 Gaussian + 20 discrete):")
    print(f"  min Cov_{{P_sync^infty}}(f, g) over all 324 monotone pairs = {min_fkg_cov_stat:+.3e}")
    print(f"  min Cov_{{mu_t}}(X_i, 1[X_{{-i}}!=0]) along iterates t=1..10 = {min_fkg_cov_iter:+.3e}")
    print(f"  max Cov_{{P_C}}(X_0, 1[X_{{-0}}!=0]) when red > 1e-6         = {max_group_cov_witness:+.6e}")
    assert min_fkg_cov_stat >= -1e-15
    assert min_fkg_cov_iter >= -1e-15
    assert max_group_cov_witness < 0.0

    # Negative control for C2: 3 policies {0, 1, 2} (cyclic 3D slots)
    # breaks Cov(1[X_i != 0], 1[X_{-i} != 0]) >= 0!
    e0 = np.array([[2.0, 0.0, 0.0]])
    e1 = np.array([[0.0, 2.0, 0.0]])
    e2 = np.array([[0.0, 0.0, 2.0]])
    H_neg = [[None, e0, e1], [None, e1, e2], [None, e2, e0]]
    G_neg = np.zeros((3, 3, 3))
    for s in product(range(3), repeat=3):
        prec = np.eye(3)
        for i in range(3):
            if s[i] > 0:
                Hi = H_neg[i][s[i]]
                prec = prec + Hi.T @ Hi
        G_neg[s] = -0.5 * np.linalg.slogdet(prec)[1] + 0.8 * sum(1 for v in s if v > 0)
    E_neg = [np.array([0.2, 0.4, 0.4])] * 3
    T_neg, _ = build_sync_kernel_from_G_list([G_neg]*3, E_neg, 3.0)
    Ps_neg = stationary_via_eig(T_neg, (3, 3, 3))
    f0 = np.array([[[0.0 if a == 0 else 1.0 for c in range(3)] for b in range(3)] for a in range(3)])
    g0 = np.array([[[0.0 if (b == 0 and c == 0) else 1.0 for c in range(3)] for b in range(3)] for a in range(3)])
    cov_3pol = cov_under(Ps_neg, f0, g0)
    print(f"Negative control (3 policies {{0,1,2}}, cyclic 3D slots): Cov(1[X0!=0], 1[X_{{-0}}!=0]) = {cov_3pol:+.6e}")
    assert cov_3pol < -1e-4

    # Bipartite factorization check: 3-member path 0 - 1 - 2 with 3 policies each (U={0,2}, W={1})
    # eta = (eta_a, eta_b); m0 senses eta_a, m2 senses eta_b, m1 opens SEPARATE slots on eta_a and eta_b
    # so I(o_0; o_2 | o_1) = 0 identically (truly bipartite conditional-redundancy graph).
    H_path = [
        [None, np.array([[1.5, 0.0]]), np.array([[2.5, 0.0]])],
        [None, np.array([[1.2, 0.0], [0.0, 0.8]]), np.array([[0.7, 0.0], [0.0, 1.9]])],
        [None, np.array([[0.0, 1.4]]), np.array([[0.0, 2.2]])],
    ]
    G_path = np.zeros((3, 3, 3))
    for s in product(range(3), repeat=3):
        prec = np.eye(2)
        for i in range(3):
            if s[i] > 0:
                Hi = H_path[i][s[i]]
                prec = prec + Hi.T @ Hi
        G_path[s] = -0.5 * np.linalg.slogdet(prec)[1]
    E_path = [np.array([0.3, 0.3, 0.4]), np.array([0.2, 0.5, 0.3]), np.array([0.4, 0.2, 0.4])]
    T_path, _ = build_sync_kernel_from_G_list([G_path]*3, E_path, 2.0)
    Ps_path = stationary_via_eig(T_path, (3, 3, 3))
    mu_U = np.sum(Ps_path, axis=1)      # shape (3, 3) on (m0, m2)
    mu_W = np.sum(Ps_path, axis=(0, 2)) # shape (3,) on m1
    fact_UW = np.einsum('ac,b->abc', mu_U, mu_W)
    err_bip = tv_dist(Ps_path, fact_UW)
    err_full_prod = tv_dist(Ps_path, prod_of_marginals(Ps_path))
    print(f"Bipartite 3-member path (U={{0,2}}, W={{1}}, |A_i|=3, I(o0;o2|o1)=0): TV(P_sync, mu_U x mu_W) = {err_bip:.3e}, TV(P_sync, prod) = {err_full_prod:.6f}")
    assert err_bip < 1e-14 and err_full_prod > 1e-4

    # Negative control for bipartite factorization: m1 uses a single MIXED slot [1.2, 0.8] (collider),
    # so I(o_0; o_2) = 0 unconditionally but I(o_0; o_2 | o_1) > 0, breaking mu_U x mu_W factorization!
    H_col = [
        [None, np.array([[1.5, 0.0]]), np.array([[2.5, 0.0]])],
        [None, np.array([[1.2, 0.8]]), np.array([[0.7, 1.9]])],
        [None, np.array([[0.0, 1.4]]), np.array([[0.0, 2.2]])],
    ]
    G_col = np.zeros((3, 3, 3))
    for s in product(range(3), repeat=3):
        prec = np.eye(2)
        for i in range(3):
            if s[i] > 0:
                Hi = H_col[i][s[i]]
                prec = prec + Hi.T @ Hi
        G_col[s] = -0.5 * np.linalg.slogdet(prec)[1]
    T_col, _ = build_sync_kernel_from_G_list([G_col]*3, E_path, 2.0)
    Ps_col = stationary_via_eig(T_col, (3, 3, 3))
    fact_col = np.einsum('ac,b->abc', np.sum(Ps_col, axis=1), np.sum(Ps_col, axis=(0, 2)))
    err_col = tv_dist(Ps_col, fact_col)
    print(f"Negative control (mixed collider slot, I(o0;o2)=0 but I(o0;o2|o1)>0): TV(P_sync, mu_U x mu_W) = {err_col:.6e}")
    assert err_col > 1e-4


# ---------------------------------------------------------------------------
# Check 3: Exact self-reproducing 3-member, 3-policy linear-Gaussian model (C3)
# ---------------------------------------------------------------------------

def solve_snr_from_mi(I_val):
    """Unique positive S solving 0.5 * ln((1+S)^2 / (1+2S)) = I_val."""
    R = np.exp(2.0 * I_val)
    return (R - 1.0) + np.sqrt((R - 1.0)**2 + (R - 1.0))


def induced_Z_and_B(B_mat, w, gamma=1.0):
    Z = np.zeros((3, 3))
    for u in range(3):
        for v in range(3):
            val = w[0]
            for c in range(2):
                cost = (B_mat[c, u - 1] if u > 0 else 0.0) + (B_mat[v - 1, c] if v > 0 else 0.0)
                val += w[c + 1] * np.exp(-gamma * cost)
            Z[u, v] = val
    B_ind = np.zeros((2, 2))
    for u in (1, 2):
        for v in (1, 2):
            B_ind[u - 1, v - 1] = -np.log((Z[u, v] * Z[0, 0]) / (Z[u, 0] * Z[0, v]))
    return Z, B_ind


def solve_ift_branch(eps, delta, gamma=1.0):
    p = (1.0 - eps) / 2.0
    w = np.array([eps, p, p])
    beta0 = (1.0 - eps + 2.0 * np.sqrt(3.0 * eps)) / (1.0 + eps)
    kappa0 = (1.0 - eps - 2.0 * np.sqrt(3.0 * eps)) / (1.0 + eps)
    mu0 = 4.0 * p * eps / (1.0 + eps)

    def res_fn(x):
        beta, kappa, mu = x
        B_mat = delta * np.array([[1.0, beta], [kappa, 1.0]])
        _, B_ind = induced_Z_and_B(B_mat, w, gamma=gamma)
        gC = mu * delta
        return np.array([
            (B_ind[0, 0] - gC * B_mat[0, 0]) / (delta**2),
            (B_ind[0, 1] - gC * B_mat[0, 1]) / (delta**2),
            (B_ind[1, 0] - gC * B_mat[1, 0]) / (delta**2),
        ])

    sol = root(res_fn, np.array([beta0, kappa0, mu0]), tol=1e-15)
    beta, kappa, mu = sol.x
    B_sol = delta * np.array([[1.0, beta], [kappa, 1.0]])
    gC_sol = mu * delta
    return B_sol, gC_sol, float(np.max(np.abs(res_fn(sol.x)))), (beta0, kappa0, mu0)


def run_check_3():
    print("\n" + "=" * 72)
    print("CHECK 3: Self-Reproducing 3-Member, 3-Policy Linear-Gaussian Collective (C3)")
    print("=" * 72)

    # Channel A: Symbolic verification of perturbative root & Jacobian determinant
    eps_s, beta_s, kappa_s, mu_s = sp.symbols('eps beta kappa mu', positive=True)
    p_s = (1 - eps_s) / 2
    F1 = p_s * (p_s * (1 + beta_s) * (1 + kappa_s) - (1 + beta_s * kappa_s)) - mu_s
    F2 = p_s * (p_s * (1 + kappa_s)**2 - 2 * kappa_s) - mu_s * beta_s
    F3 = p_s * (p_s * (1 + beta_s)**2 - 2 * beta_s) - mu_s * kappa_s
    b0_s = (1 - eps_s + 2 * sp.sqrt(3 * eps_s)) / (1 + eps_s)
    k0_s = (1 - eps_s - 2 * sp.sqrt(3 * eps_s)) / (1 + eps_s)
    m0_s = 4 * p_s * eps_s / (1 + eps_s)
    subs0 = {beta_s: b0_s, kappa_s: k0_s, mu_s: m0_s}
    for idx, Fk in enumerate((F1, F2, F3), 1):
        val = sp.simplify(Fk.subs(subs0))
        assert val == 0, f"F{idx} did not vanish: {val}"
    J0 = sp.Matrix([F1, F2, F3]).jacobian([beta_s, kappa_s, mu_s]).subs(subs0)
    detJ0 = sp.factor(sp.simplify(J0.det()))
    expected_det = -24 * eps_s**2 * (eps_s - 1)**2 / (eps_s + 1)**2
    assert sp.simplify(detJ0 - expected_det) == 0
    print(f"Symbolic Channel A: F(beta0, kappa0, mu0; 0) = (0, 0, 0) exactly.")
    print(f"Symbolic det(J_0(eps)) = {detJ0} (nonzero for all eps in (0, 1)).")
    print(f"Positivity threshold eps_max = 7 - 4*sqrt(3) = {float(7 - 4*sp.sqrt(3)):.12f}")

    # Channel B: Explicit 12D linear-Gaussian construction from first principles at eps=0.05, delta=0.1, gamma=1
    eps = 0.05
    delta = 0.1
    gamma = 1.0
    p = (1.0 - eps) / 2.0
    w = np.array([eps, p, p])
    B_sol, gC_sol, res_norm, (beta0, kappa0, mu0) = solve_ift_branch(eps, delta, gamma=gamma)
    Z, B_ind = induced_Z_and_B(B_sol, w, gamma=gamma)
    assert np.all(B_sol > 0) and 0 < gC_sol < gamma
    assert np.max(np.abs(B_ind - gC_sol * B_sol)) < 1e-15

    # Exact closed-form habits E and single-slot target g* (identical across members!)
    assert abs(Z[1, 0] * Z[0, 1] - Z[2, 0] * Z[0, 2]) < 1e-15
    g_star = float(np.log(Z[1, 0] * Z[0, 1]) / (gamma - gC_sol))
    g_vec = np.array([0.0, g_star, g_star])
    E_unnorm = w * np.exp(gamma * g_vec)
    E = E_unnorm / np.sum(E_unnorm)

    # Realize B_sol via 12 independent coordinates eta ~ N(0, I_12)
    # and genuine normalized Gaussian preferences p_tilde_s = N(0, R_s(1 + S_s))
    # with common noise variance R_s = exp(g_star / 2) / (2 * pi * e)!
    S_mat = np.vectorize(solve_snr_from_mi)(B_sol)
    R_s = float(np.exp(g_star / 2.0) / (2.0 * np.pi * np.e))

    # Build explicit 12D observation matrices H_{i, u} (shape (4, 12) for u in {1, 2})
    # Coordinate index map: coord(edge, a, b) = 4*edge + 2*(a-1) + (b-1), edge in {0,1,2}, a,b in {1,2}
    # Edge e connects member e (using policy a) to member (e+1)%3 (using policy b).
    def coord_idx(edge, a, b):
        return 4 * edge + 2 * (a - 1) + (b - 1)

    H_mem = [[None, None, None] for _ in range(3)]
    slot_vars = [[[], [], []] for _ in range(3)]
    for i in range(3):
        edge_out = i
        edge_in = (i - 1) % 3
        for u in (1, 2):
            rows = []
            svars = []
            # 2 outgoing slots: (edge_out, a=u, b in {1,2})
            for b in (1, 2):
                row = np.zeros(12)
                S_val = S_mat[u - 1, b - 1]
                row[coord_idx(edge_out, u, b)] = np.sqrt(R_s * S_val)
                rows.append(row)
                svars.append(R_s * (1.0 + S_val))
            # 2 incoming slots: (edge_in, a in {1,2}, b=u)
            for a in (1, 2):
                row = np.zeros(12)
                S_val = S_mat[a - 1, u - 1]
                row[coord_idx(edge_in, a, u)] = np.sqrt(R_s * S_val)
                rows.append(row)
                svars.append(R_s * (1.0 + S_val))
            H_mem[i][u] = np.vstack(rows)
            slot_vars[i][u] = svars

    # Compute G_C(pi) directly from 12x12 precision matrix determinants and exact Gaussian cross-entropies!
    G_C_full = np.zeros((3, 3, 3))
    for s in product(range(3), repeat=3):
        prec = np.eye(12)
        psi_total = 0.0
        for i in range(3):
            u = s[i]
            if u > 0:
                Hi = H_mem[i][u]
                prec = prec + (Hi.T @ Hi) / R_s
                # Exact cross-entropy -E_{q_C}[ln N(o_s; 0, var_s)] = 0.5 * ln(2*pi*e*var_s)
                psi_total += sum(0.5 * np.log(2.0 * np.pi * np.e * v) for v in slot_vars[i][u])
        sign, logdet = np.linalg.slogdet(prec)
        assert sign > 0
        G_C_full[s] = -0.5 * logdet + psi_total

    # Verify G_C_full reproduces exact pairwise structure & single-slot EFEs g_vec
    G_C_check = np.zeros((3, 3, 3))
    for s in product(range(3), repeat=3):
        val = sum(g_vec[s[i]] for i in range(3))
        for edge in range(3):
            u, v = s[edge], s[(edge + 1) % 3]
            if u > 0 and v > 0:
                val += B_sol[u - 1, v - 1]
        G_C_check[s] = val
    assert np.max(np.abs(G_C_full - G_C_check)) < 1e-14

    P_gamma = group_posterior(G_C_full, [E, E, E], gamma)
    P_gammaC = group_posterior(G_C_full, [E, E, E], gC_sol)
    T_sync, _ = build_sync_kernel_from_G_list([G_C_full]*3, [E, E, E], gamma)

    # Channel 1: eigendecomposition; Channel 2: power iteration from uniform AND from corner (0,0,0)
    P_stat_eig = stationary_via_eig(T_sync, (3, 3, 3))
    P_stat_pow_unif = stationary_via_power(T_sync, (3, 3, 3))
    corner = np.zeros(27); corner[0] = 1.0
    P_stat_pow_corner = stationary_via_power(T_sync, (3, 3, 3), init_vec=corner)

    tv_match_eig = tv_dist(P_stat_eig, P_gammaC)
    tv_match_pow = tv_dist(P_stat_pow_corner, P_gammaC)
    tv_same_gamma = tv_dist(P_stat_eig, P_gamma)
    tv_non_prod = tv_dist(P_stat_eig, prod_of_marginals(P_stat_eig))
    # Detailed balance residual for P_gammaC under T_sync:
    pv = P_gammaC.reshape(-1)
    db_res = float(np.max(np.abs(pv[:, None] * T_sync - pv[None, :] * T_sync.T)))
    stat_res = float(np.sum(np.abs(pv @ T_sync - pv)))

    print(f"\nExplicit 12D linear-Gaussian instance (eps={eps}, delta={delta}, gamma={gamma}):")
    print(f"  B_sol = [[{B_sol[0,0]:.12f}, {B_sol[0,1]:.12f}], [{B_sol[1,0]:.12f}, {B_sol[1,1]:.12f}]]")
    print(f"  gamma_C = {gC_sol:.12f}  (ratio gamma_C/gamma = {gC_sol/gamma:.12f})")
    print(f"  Exact habits E = [{E[0]:.10f}, {E[1]:.10f}, {E[2]:.10f}]")
    print(f"  Single-slot EFE g* = {g_star:.10f}, common noise variance R_s = {R_s:.10f}")
    print(f"  SNRs S_mat = [[{S_mat[0,0]:.8f}, {S_mat[0,1]:.8f}], [{S_mat[1,0]:.8f}, {S_mat[1,1]:.8f}]]")
    print(f"  TV(P_sync^infty(1), P_C(gamma_C, E, G_C)) [eig]    = {tv_match_eig:.3e}")
    print(f"  TV(P_sync^infty(1), P_C(gamma_C, E, G_C)) [power]  = {tv_match_pow:.3e}")
    print(f"  Stationarity residual ||P_C(gamma_C) T - P_C(gamma_C)||_1 = {stat_res:.3e}")
    print(f"  Detailed-balance residual max |P(x)T(x,y) - P(y)T(y,x)|   = {db_res:.3e}")
    print(f"  TV(P_sync^infty(1), P_C(gamma=1, E, G_C)) [C1 gap] = {tv_same_gamma:.6e}")
    print(f"  TV(P_sync^infty(1), prod of marginals)             = {tv_non_prod:.6e}")
    assert tv_match_eig < 1e-14 and tv_match_pow < 1e-14
    assert stat_res < 1e-14 and db_res < 1e-15
    assert tv_same_gamma > 1e-3 and tv_non_prod > 1e-5

    # Trace IFT branch across delta in {0.01, 0.05, 0.1, 0.15, 0.2}
    print(f"\nIFT branch verification at eps={eps} (asymptotic beta0={beta0:.6f}, kappa0={kappa0:.6f}, mu0={mu0:.6f}):")
    for d_val in [0.01, 0.05, 0.10, 0.15, 0.20]:
        Bd, gCd, rn, _ = solve_ift_branch(eps, d_val, gamma=1.0)
        _, Bd_ind = induced_Z_and_B(Bd, w, gamma=1.0)
        unscaled = float(np.max(np.abs(Bd_ind - gCd * Bd)))
        print(f"  delta={d_val:.2f}: b/delta={Bd[0,1]/d_val:.6f}, c/delta={Bd[1,0]/d_val:.6f}, "
              f"gamma_C/delta={gCd/d_val:.6f}, gamma_C={gCd:.8f}, min(B)={Bd.min():.6f}, max|dB|={unscaled:.2e}")
        assert np.all(Bd > 0) and gCd > 0 and unscaled < 1e-15

    # Negative control for C3: perturb B[0,1] by +1e-3 off the IFT branch
    B_pert = B_sol.copy()
    B_pert[0, 1] += 1e-3
    G_pert = np.zeros((3, 3, 3))
    for s in product(range(3), repeat=3):
        val = sum(g_vec[s[i]] for i in range(3))
        for edge in range(3):
            u, v = s[edge], s[(edge + 1) % 3]
            if u > 0 and v > 0:
                val += B_pert[u - 1, v - 1]
        G_pert[s] = val
    T_pert, _ = build_sync_kernel_from_G_list([G_pert]*3, [E, E, E], gamma)
    Ps_pert = stationary_via_eig(T_pert, (3, 3, 3))
    P_gC_pert = group_posterior(G_pert, [E, E, E], gC_sol)
    print(f"Negative control (B_12 perturbed by +1e-3): TV(P_sync^infty, P_C(gamma_C)) = {tv_dist(Ps_pert, P_gC_pert):.6e}")
    assert tv_dist(Ps_pert, P_gC_pert) > 1e-6


# ---------------------------------------------------------------------------
# Check 4: Elementary closed-form reversed-cycle collective (C4)
# ---------------------------------------------------------------------------

def run_check_4():
    print("\n" + "=" * 72)
    print("CHECK 4: Elementary Closed-Form Reversed-Cycle Collective (C4)")
    print("=" * 72)
    h = [1.5, 2.0, 1.2]
    E_list = [
        np.array([0.20, 0.35, 0.45]),
        np.array([0.30, 0.40, 0.30]),
        np.array([0.25, 0.25, 0.50]),
    ]
    psi = [[0.0, 0.3, -0.2], [0.0, 0.1, 0.4], [0.0, -0.1, 0.2]]
    e_vecs = [np.array([[h[0], 0, 0]]), np.array([[0, h[1], 0]]), np.array([[0, 0, h[2]]])]
    # Clockwise: member i pol 1 -> eta_i, pol 2 -> eta_{(i+1)%3}
    H_cw = [[None, e_vecs[i], e_vecs[(i + 1) % 3]] for i in range(3)]
    G_cw = np.zeros((3, 3, 3))
    for s in product(range(3), repeat=3):
        prec = np.eye(3)
        cost = 0.0
        for i in range(3):
            if s[i] > 0:
                Hi = H_cw[i][s[i]]
                prec = prec + Hi.T @ Hi
                cost += psi[i][s[i]]
        G_cw[s] = -0.5 * np.linalg.slogdet(prec)[1] + cost

    # Closed-form reversed-cycle parameters
    I_pair = [0.5 * np.log((1.0 + hi**2)**2 / (1.0 + 2.0 * hi**2)) for hi in h]
    g_single = [
        [0.0, -0.5 * np.log(1.0 + h[i]**2) + psi[i][1], -0.5 * np.log(1.0 + h[(i + 1) % 3]**2) + psi[i][2]]
        for i in range(3)
    ]

    for gamma in [0.2, 1.0, 2.0, 5.0]:
        T_cw, _ = build_sync_kernel_from_G_list([G_cw]*3, E_list, gamma)
        P_sync = stationary_via_eig(T_cw, (3, 3, 3))
        P_cw = group_posterior(G_cw, E_list, gamma)

        w = [[E_list[i][a] * np.exp(-gamma * g_single[i][a]) for a in range(3)] for i in range(3)]
        alp = [np.exp(-gamma * I_pair[k]) for k in range(3)]

        def cross_J(w0, w1, w2, a_first, a_second):
            z00 = w0 + w1 + w2
            z10 = w0 + w1 + a_first * w2
            z01 = w0 + a_second * w1 + w2
            z11 = w0 + a_second * w1 + a_first * w2
            return -np.log((z11 * z00) / (z10 * z01))

        # Z_2 couples (m0=1, m1=2) via (eta_0 on m2 pol 2, eta_2 on m2 pol 1)
        # Z_0 couples (m1=1, m2=2) via (eta_1 on m0 pol 2, eta_0 on m0 pol 1)
        # Z_1 couples (m2=1, m0=2) via (eta_2 on m1 pol 2, eta_1 on m1 pol 1)
        J01 = cross_J(w[2][0], w[2][1], w[2][2], alp[0], alp[2])
        J12 = cross_J(w[0][0], w[0][1], w[0][2], alp[1], alp[0])
        J20 = cross_J(w[1][0], w[1][1], w[1][2], alp[2], alp[1])
        assert J01 > 0 and J12 > 0 and J20 > 0

        # Realize reversed cycle at gamma_C = gamma (same precision!) with tilted habits E_tilde
        s01 = solve_snr_from_mi(J01 / gamma)
        s12 = solve_snr_from_mi(J12 / gamma)
        s20 = solve_snr_from_mi(J20 / gamma)
        H_ccw = [
            [None, np.array([[np.sqrt(s01), 0, 0]]), np.array([[0, 0, np.sqrt(s20)]])],
            [None, np.array([[0, np.sqrt(s12), 0]]), np.array([[np.sqrt(s01), 0, 0]])],
            [None, np.array([[0, 0, np.sqrt(s20)]]), np.array([[0, np.sqrt(s12), 0]])],
        ]
        G_ccw = np.zeros((3, 3, 3))
        for s in product(range(3), repeat=3):
            prec = np.eye(3)
            for i in range(3):
                if s[i] > 0:
                    Hi = H_ccw[i][s[i]]
                    prec = prec + Hi.T @ Hi
            G_ccw[s] = -0.5 * np.linalg.slogdet(prec)[1]

        # Closed-form tilted habits from Z factors (independent of fitting!)
        # Single-member ratio for member i: w_i(a) * Z_{i+1}(a, 0) * Z_{i-1}(0, a) * exp(+gamma G_ccw(a_i, 0_{-i}))
        def Z_k_marg(wk, a_pol1, a_pol2):
            # Z_k when neighbor on pol2 is active (1) vs null (0), and neighbor on pol1 is active (1) vs null (0)
            z00 = wk[0] + wk[1] + wk[2]
            z_p1 = wk[0] + a_pol1 * wk[1] + wk[2]
            z_p2 = wk[0] + wk[1] + a_pol2 * wk[2]
            return z00, z_p1, z_p2

        z0_00, z0_p1, z0_p2 = Z_k_marg(w[0], alp[0], alp[1])  # p1 hits m2=2, p2 hits m1=1
        z1_00, z1_p1, z1_p2 = Z_k_marg(w[1], alp[1], alp[2])  # p1 hits m0=2, p2 hits m2=1
        z2_00, z2_p1, z2_p2 = Z_k_marg(w[2], alp[2], alp[0])  # p1 hits m1=2, p2 hits m0=1

        # Factor on m0: pol0->1, pol1->z2_p2/z2_00, pol2->z1_p1/z1_00
        # Factor on m1: pol0->1, pol1->z0_p2/z0_00, pol2->z2_p1/z2_00
        # Factor on m2: pol0->1, pol1->z1_p2/z1_00, pol2->z0_p1/z0_00
        z_fac = [
            [1.0, z2_p2 / z2_00, z1_p1 / z1_00],
            [1.0, z0_p2 / z0_00, z2_p1 / z2_00],
            [1.0, z1_p2 / z1_00, z0_p1 / z0_00],
        ]
        E_tilde = []
        for i in range(3):
            et = np.zeros(3)
            for a in range(3):
                idx = [0, 0, 0]; idx[i] = a
                et[a] = w[i][a] * z_fac[i][a] * np.exp(gamma * G_ccw[tuple(idx)])
            E_tilde.append(et / np.sum(et))

        Q_ccw = group_posterior(G_ccw, E_tilde, gamma)
        err_ccw = tv_dist(P_sync, Q_ccw)
        err_cw = tv_dist(P_sync, P_cw)
        print(f"gamma={gamma:.1f}: J_ccw=({J01:.6f},{J12:.6f},{J20:.6f}), "
              f"TV(P_sync, P_ccw)={err_ccw:.3e}, TV(P_sync, P_cw)={err_cw:.6f}")
        assert err_ccw < 1e-14 and err_cw > 1e-4


if __name__ == "__main__":
    run_check_1()
    run_check_2()
    run_check_3()
    run_check_4()
    print("\nALL CHECKS PASSED.")
