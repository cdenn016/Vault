"""Two-channel verification and planted-error negative controls for open:prv-aware.

Channel A: Analytic block-tridiagonal precision matrix J_D, Schur-complement operator Phi(U),
           exact rational SymPy ranks, and compressed linear encoder/decoder fusion.
Channel B: Independent brute-force batch covariance-form Gaussian conditioning built directly
           from forward unrolling of x_{t+1} = A x_t + w_t and o_{j,t} = H_j x_t + v_{j,t},
           without forming J_D, Phi(U), or Kalman recursions.

Deepest shared element: the linear-Gaussian model parameters (A, Q_x, P_0, m_0, H_j, R_j) and
standard linear algebra routines. Any sign, transposition, Schur-complement, indexing, encoding,
or reconstruction error in Channel A fails against Channel B.
"""
from __future__ import annotations

import numpy as np
import sympy as sp


# ============================================================================
# Channel A: Information-form precision J_D and Schur operator Phi(U)
# ============================================================================

def build_prior_precision(A: np.ndarray, Q: np.ndarray, P0: np.ndarray, T: int) -> np.ndarray:
    d = A.shape[0]
    Qinv = np.linalg.inv(Q)
    P1 = A @ P0 @ A.T + Q
    P1inv = np.linalg.inv(P1)
    J0 = np.zeros((T * d, T * d))
    J0[:d, :d] = P1inv
    AtQinvA = A.T @ Qinv @ A
    AtQinv = A.T @ Qinv
    QinvA = Qinv @ A
    for t in range(T - 1):
        i0, i1 = t * d, (t + 1) * d
        j0, j1 = (t + 1) * d, (t + 2) * d
        J0[i0:i1, i0:i1] += AtQinvA
        J0[i0:i1, j0:j1] -= AtQinv
        J0[j0:j1, i0:i1] -= QinvA
        J0[j0:j1, j0:j1] += Qinv
    return J0


def build_J(J0: np.ndarray, D_obs: list[tuple[int, int]], Lambdas: list[np.ndarray], d: int) -> np.ndarray:
    J = J0.copy()
    for (j, tau) in D_obs:
        s = (tau - 1) * d
        J[s:s + d, s:s + d] += Lambdas[j]
    return J


def build_j0(A: np.ndarray, Q: np.ndarray, P0: np.ndarray, m0: np.ndarray, T: int) -> np.ndarray:
    d = A.shape[0]
    P1 = A @ P0 @ A.T + Q
    j0 = np.zeros(T * d)
    j0[:d] = np.linalg.solve(P1, A @ m0)
    return j0


def phi_operator(
    A: np.ndarray,
    Q: np.ndarray,
    P0: np.ndarray,
    U_lt_b: list[tuple[int, int]],
    Lambdas: list[np.ndarray],
    b: int,
    W_i: list[int],
    basis_i: np.ndarray,
) -> np.ndarray:
    """Compute Phi(U_{<b})|_{R_i^k} of shape (d, k * r_i) via
    Phi(U) l_i = h_{i,b} + Q^{-1} A E_{b-1}^T K(U)^{-1} l_{i,<b}.
    """
    d = A.shape[0]
    k = len(W_i)
    r_i = basis_i.shape[1]
    Phi = np.zeros((d, k * r_i))
    if b in W_i:
        b_idx = W_i.index(b)
        Phi[:, b_idx * r_i:(b_idx + 1) * r_i] = basis_i
    if b > 1:
        Qinv = np.linalg.inv(Q)
        J0_prev = build_prior_precision(A, Q, P0, b - 1)
        K = build_J(J0_prev, U_lt_b, Lambdas, d)
        K[(b - 2) * d:(b - 1) * d, (b - 2) * d:(b - 1) * d] += A.T @ Qinv @ A
        Kinv = np.linalg.inv(K)
        QinvA = Qinv @ A
        for idx, tau in enumerate(W_i):
            if tau < b:
                blk = Kinv[(b - 2) * d:(b - 1) * d, (tau - 1) * d:tau * d]
                Phi[:, idx * r_i:(idx + 1) * r_i] = QinvA @ blk @ basis_i
    return Phi


def sensitivity_info_form(
    J0: np.ndarray,
    D_obs: list[tuple[int, int]],
    Lambdas: list[np.ndarray],
    d: int,
    t_query: int,
    W_i: list[int],
    basis_i: np.ndarray,
) -> np.ndarray:
    J = build_J(J0, D_obs, Lambdas, d)
    Jinv = np.linalg.inv(J)
    k = len(W_i)
    r_i = basis_i.shape[1]
    M = np.zeros((d, k * r_i))
    rs = slice((t_query - 1) * d, t_query * d)
    for idx, tau in enumerate(W_i):
        cs = slice((tau - 1) * d, tau * d)
        M[:, idx * r_i:(idx + 1) * r_i] = Jinv[rs, cs] @ basis_i
    return M


# ============================================================================
# Channel B: Brute-force batch covariance-form Gaussian conditioning
# ============================================================================

def forward_state_moments(A: np.ndarray, Q: np.ndarray, m0: np.ndarray, P0: np.ndarray, T: int):
    """Build prior mean mu_X and joint covariance Sigma_XX of X = (x_1, ..., x_T) by forward unrolling."""
    d = A.shape[0]
    means = []
    covs_diag = []
    m_cur = m0.copy()
    P_cur = P0.copy()
    for _ in range(T):
        m_cur = A @ m_cur
        P_cur = A @ P_cur @ A.T + Q
        means.append(m_cur.copy())
        covs_diag.append(P_cur.copy())
    mu_X = np.concatenate(means)
    Sigma_XX = np.zeros((T * d, T * d))
    for s in range(T):
        Sigma_XX[s * d:(s + 1) * d, s * d:(s + 1) * d] = covs_diag[s]
        A_pow = np.eye(d)
        for t in range(s + 1, T):
            A_pow = A @ A_pow
            cov_ts = A_pow @ covs_diag[s]
            Sigma_XX[t * d:(t + 1) * d, s * d:(s + 1) * d] = cov_ts
            Sigma_XX[s * d:(s + 1) * d, t * d:(t + 1) * d] = cov_ts.T
    return mu_X, Sigma_XX


def batch_cov_posterior(
    A: np.ndarray,
    Q: np.ndarray,
    m0: np.ndarray,
    P0: np.ndarray,
    Hs: list[np.ndarray],
    Rs: list[np.ndarray],
    D_obs: list[tuple[int, int]],
    obs_dict: dict[tuple[int, int], np.ndarray],
    t_query: int,
):
    """Exact posterior (mean, cov) of x_{t_query} given obs in D_obs via batch covariance conditioning."""
    d = A.shape[0]
    T = max([t_query] + [tau for (_, tau) in D_obs])
    mu_X, Sigma_XX = forward_state_moments(A, Q, m0, P0, T)
    mu_xt = mu_X[(t_query - 1) * d:t_query * d]
    Sigma_xt = Sigma_XX[(t_query - 1) * d:t_query * d, (t_query - 1) * d:t_query * d]
    if not D_obs:
        return mu_xt, Sigma_xt
    # Build linear map C_obs: X -> stacked noiseless observations, and block-diag R_obs
    row_blocks = []
    R_blocks = []
    y_blocks = []
    for (j, tau) in D_obs:
        Hj = Hs[j]
        p_j = Hj.shape[0]
        C_row = np.zeros((p_j, T * d))
        C_row[:, (tau - 1) * d:tau * d] = Hj
        row_blocks.append(C_row)
        R_blocks.append(Rs[j])
        y_blocks.append(obs_dict[(j, tau)])
    C_obs = np.vstack(row_blocks)
    m_tot = C_obs.shape[0]
    R_obs = np.zeros((m_tot, m_tot))
    off = 0
    for Rj in R_blocks:
        p = Rj.shape[0]
        R_obs[off:off + p, off:off + p] = Rj
        off += p
    y_vec = np.concatenate(y_blocks)
    mu_y = C_obs @ mu_X
    Sigma_yy = C_obs @ Sigma_XX @ C_obs.T + R_obs
    Sigma_xy = Sigma_XX[(t_query - 1) * d:t_query * d, :] @ C_obs.T
    gain = np.linalg.solve(Sigma_yy, Sigma_xy.T).T
    post_mean = mu_xt + gain @ (y_vec - mu_y)
    post_cov = Sigma_xt - gain @ Sigma_xy.T
    return post_mean, post_cov


def sensitivity_cov_form(
    A: np.ndarray,
    Q: np.ndarray,
    P0: np.ndarray,
    Hs: list[np.ndarray],
    Rs: list[np.ndarray],
    D_obs: list[tuple[int, int]],
    t_query: int,
    i_member: int,
    W_i: list[int],
) -> np.ndarray:
    """Compute d x (sum p_i) gain matrix from member i's raw window observations O_i to E[x_{t_query}|o_D]
    purely via Channel B (batch covariance form).
    """
    d = A.shape[0]
    T = max([t_query] + [tau for (_, tau) in D_obs])
    _, Sigma_XX = forward_state_moments(A, Q, np.zeros(d), P0, T)
    row_blocks = []
    R_blocks = []
    col_slices_W = {}
    off = 0
    for (j, tau) in D_obs:
        Hj = Hs[j]
        p_j = Hj.shape[0]
        C_row = np.zeros((p_j, T * d))
        C_row[:, (tau - 1) * d:tau * d] = Hj
        row_blocks.append(C_row)
        R_blocks.append(Rs[j])
        if j == i_member and tau in W_i:
            col_slices_W[tau] = slice(off, off + p_j)
        off += p_j
    C_obs = np.vstack(row_blocks)
    R_obs = np.zeros((off, off))
    cur = 0
    for Rj in R_blocks:
        p = Rj.shape[0]
        R_obs[cur:cur + p, cur:cur + p] = Rj
        cur += p
    Sigma_yy = C_obs @ Sigma_XX @ C_obs.T + R_obs
    Sigma_xy = Sigma_XX[(t_query - 1) * d:t_query * d, :] @ C_obs.T
    gain = np.linalg.solve(Sigma_yy, Sigma_xy.T).T
    return np.hstack([gain[:, col_slices_W[tau]] for tau in W_i])


# ============================================================================
# Utilities
# ============================================================================

def num_rank(M: np.ndarray, tol: float = 1e-10) -> int:
    s = np.linalg.svd(M, compute_uv=False)
    if len(s) == 0 or s[0] == 0:
        return 0
    return int(np.sum(s > tol * s[0]))


def row_basis(M: np.ndarray, tol: float = 1e-10) -> np.ndarray:
    """Orthonormal basis for row(M), shape (r, n_cols)."""
    _, s, Vt = np.linalg.svd(M, full_matrices=False)
    r = int(np.sum(s > tol * s[0])) if len(s) > 0 and s[0] > 0 else 0
    return Vt[:r, :]


def rand_spd(rng: np.random.Generator, d: int) -> np.ndarray:
    M = rng.normal(size=(d, d))
    return M @ M.T + 0.8 * np.eye(d)


def rand_sensing(rng: np.random.Generator, d: int, r: int, p: int | None = None):
    if p is None:
        p = r
    # Generic non-orthogonal rank-r matrix with controlled singular values in [0.8, 2.0]
    Q_left, _ = np.linalg.qr(rng.normal(size=(p, r)))
    Q_right, _ = np.linalg.qr(rng.normal(size=(d, r)))
    sv = rng.uniform(0.8, 2.0, size=r)
    H = (Q_left * sv) @ Q_right.T
    R = rand_spd(rng, p)
    Lam = H.T @ np.linalg.inv(R) @ H
    Uh, _, _ = np.linalg.svd(H.T)
    basis = Uh[:, :r]
    return H, R, Lam, basis


def exact_sympy_phi_block(A_sp, Q_sp, P0_sp, Lam_list_by_tau, k):
    """Exact rational SymPy matrix Phi(U) of shape (d, k*d) for W = {1..k}."""
    d = A_sp.rows
    Qinv = Q_sp.inv()
    m = k - 1
    P1 = A_sp * P0_sp * A_sp.T + Q_sp
    P1inv = P1.inv()
    K = sp.zeros(m * d, m * d)
    K[:d, :d] = P1inv
    AtQinvA = A_sp.T * Qinv * A_sp
    AtQinv = A_sp.T * Qinv
    QinvA = Qinv * A_sp
    for t in range(m - 1):
        i0, i1 = t * d, (t + 1) * d
        j0, j1 = (t + 1) * d, (t + 2) * d
        K[i0:i1, i0:i1] += AtQinvA
        K[i0:i1, j0:j1] -= AtQinv
        K[j0:j1, i0:i1] -= QinvA
        K[j0:j1, j0:j1] += Qinv
    for t in range(m):
        i0, i1 = t * d, (t + 1) * d
        K[i0:i1, i0:i1] += Lam_list_by_tau[t]
    K[(m - 1) * d:m * d, (m - 1) * d:m * d] += AtQinvA
    Kinv = K.inv()
    Phi = sp.zeros(d, k * d)
    for t in range(m):
        Phi[:, t * d:(t + 1) * d] = QinvA * Kinv[(m - 1) * d:m * d, t * d:(t + 1) * d]
    Phi[:, (k - 1) * d:k * d] = sp.eye(d)
    return Phi


# ============================================================================
# CHECK 1: C1 (Markov Factorization + End-to-End Compressed Fusion + Neg Controls)
# ============================================================================

def check_1_master_and_fusion():
    print("=" * 78)
    print("CHECK 1: C1 (Markov Factorization, End-to-End Exact Fusion, Negative Controls)")
    print("=" * 78)
    rng = np.random.default_rng(202601)
    # Generic non-symmetric A, non-diagonal Q, P0, heterogeneous partial/full sensing
    d = 3
    A = np.array([[0.8, 0.3, -0.2], [-0.4, 0.7, 0.5], [0.2, -0.3, 0.9]])
    Q = rand_spd(rng, d)
    P0 = rand_spd(rng, d)
    m0 = rng.normal(size=d)
    H0, R0, L0, B0 = rand_sensing(rng, d, 3, 4)
    H1, R1, L1, B1 = rand_sensing(rng, d, 2, 3)
    H2, R2, L2, B2 = rand_sensing(rng, d, 1, 2)
    Hs, Rs, Lambdas, bases = [H0, H1, H2], [R0, R1, R2], [L0, L1, L2], [B0, B1, B2]

    # 1A: Verify Markov Factorization M_{D,t} = Cov(x_t,x_b|D) Phi(D_{<b})
    T = 8
    b = 5
    W0 = [2, 3, 4, 5]
    D_lt_b = [(0, 2), (0, 3), (0, 4), (1, 1), (1, 3), (2, 2), (2, 4)]
    D_ge_b = [(0, 5), (1, 5), (2, 5), (0, 6), (1, 7), (2, 8)]
    D_full = D_lt_b + D_ge_b
    J0_T = build_prior_precision(A, Q, P0, T)
    J_full = build_J(J0_T, D_full, Lambdas, d)
    J_full_inv = np.linalg.inv(J_full)
    Phi = phi_operator(A, Q, P0, D_lt_b, Lambdas, b, W0, B0)
    max_fact_err = 0.0
    for t_q in [5, 6, 7, 8]:
        M_A = sensitivity_info_form(J0_T, D_full, Lambdas, d, t_q, W0, B0)
        Cov_tb = J_full_inv[(t_q - 1) * d:t_q * d, (b - 1) * d:b * d]
        err = np.max(np.abs(M_A - Cov_tb @ Phi))
        max_fact_err = max(max_fact_err, err)
        # Cross-check M_A against Channel B (covariance-form sensitivity)
        G_B = sensitivity_cov_form(A, Q, P0, Hs, Rs, D_full, t_q, 0, W0)
        # Convert M_A (in ledger coords B0^T H0^T R0^{-1} o) to raw observation coords:
        L_map = np.zeros((len(W0) * B0.shape[1], len(W0) * H0.shape[0]))
        T0 = B0.T @ H0.T @ np.linalg.inv(R0)
        for idx in range(len(W0)):
            L_map[idx * B0.shape[1]:(idx + 1) * B0.shape[1], idx * H0.shape[0]:(idx + 1) * H0.shape[0]] = T0
        err_AB = np.max(np.abs(M_A @ L_map - G_B))
        assert err_AB < 1e-12, f"Channel A vs B sensitivity mismatch: {err_AB}"
    print(f"  [PASS] Markov factorization max error (d=3, t=5..8): {max_fact_err:.3e}")
    print(f"  [PASS] Channel A vs Channel B sensitivity cross-check: < 1e-12")
    assert max_fact_err < 1e-13

    # 1B: End-to-end compressed multi-agent star fusion on deterministic staggered schedule
    # 3 members, horizon T=10; report schedules (asynchronous):
    # Member 0 reports at t=4 (W=[1..4]) and t=8 (W=[5..8])
    # Member 1 reports at t=5 (W=[1..5]) and t=9 (W=[6..9])
    # Member 2 reports at t=6 (W=[1..6]) and t=10 (W=[7..10])
    windows = [
        (0, [1, 2, 3, 4], 4),
        (1, [1, 2, 3, 4, 5], 5),
        (2, [1, 2, 3, 4, 5, 6], 6),
        (0, [5, 6, 7, 8], 8),
        (1, [6, 7, 8, 9], 9),
        (2, [7, 8, 9, 10], 10),
    ]
    T_sim = 10
    # Generate one random trajectory and observations
    x_true = np.zeros((T_sim + 1, d))
    x_true[0] = rng.multivariate_normal(m0, P0)
    obs_dict = {}
    for t in range(1, T_sim + 1):
        x_true[t] = A @ x_true[t - 1] + rng.multivariate_normal(np.zeros(d), Q)
        for j in range(3):
            obs_dict[(j, t)] = Hs[j] @ x_true[t] + rng.multivariate_normal(np.zeros(Rs[j].shape[0]), Rs[j])

    # Determine D_z(t) for each t = 1..10
    D_by_t = {}
    for t in range(1, T_sim + 1):
        D_t = []
        for (j, W, t_rep) in windows:
            if t_rep <= t:
                for tau in W:
                    D_t.append((j, tau))
        D_by_t[t] = D_t

    J0_sim = build_prior_precision(A, Q, P0, T_sim)
    j0_sim = build_j0(A, Q, P0, m0, T_sim)

    # Encode each window W using exact minimal row basis B_W of stacked M_{D_z(t), t} for t >= t_rep
    enc_bases = {}
    messages = {}
    dims = {}
    for w_idx, (j, W, t_rep) in enumerate(windows):
        rows = []
        for t in range(t_rep, T_sim + 1):
            rows.append(sensitivity_info_form(J0_sim, D_by_t[t], Lambdas, d, t, W, bases[j]))
        B_W = row_basis(np.vstack(rows))
        enc_bases[w_idx] = B_W
        dims[w_idx] = B_W.shape[0]
        # Compute window ledger coordinates tilde_l in R^{k * r_j}
        l_coords = np.concatenate([bases[j].T @ Hs[j].T @ np.linalg.solve(Rs[j], obs_dict[(j, tau)]) for tau in W])
        messages[w_idx] = B_W @ l_coords

    # Hub reconstruction at every step t = 1..10 vs Channel B batch covariance conditioning
    max_mean_err = 0.0
    max_cov_err = 0.0
    for t in range(1, T_sim + 1):
        D_t = D_by_t[t]
        J_t = build_J(J0_sim, D_t, Lambdas, d)
        J_t_inv = np.linalg.inv(J_t)
        rs = slice((t - 1) * d, t * d)
        mean_A = J_t_inv[rs, :] @ j0_sim
        for w_idx, (j, W, t_rep) in enumerate(windows):
            if t_rep <= t:
                M_W = sensitivity_info_form(J0_sim, D_t, Lambdas, d, t, W, bases[j])
                B_W = enc_bases[w_idx]
                # Since rows of B_W are orthonormal basis of row space, C = M_W @ B_W^T
                C_W = M_W @ B_W.T
                mean_A = mean_A + C_W @ messages[w_idx]
        cov_A = J_t_inv[rs, rs]
        mean_B, cov_B = batch_cov_posterior(A, Q, m0, P0, Hs, Rs, D_t, obs_dict, t)
        max_mean_err = max(max_mean_err, np.max(np.abs(mean_A - mean_B)))
        max_cov_err = max(max_cov_err, np.max(np.abs(cov_A - cov_B)))

    print(f"  Window exact dims vs blind k*r_j: " + ", ".join(
        f"W{idx}(j={j},k={len(W)}): {dims[idx]}/{len(W)*bases[j].shape[1]}"
        for idx, (j, W, _) in enumerate(windows)
    ))
    print(f"  [PASS] End-to-end hub fusion vs Channel B (t=1..10): max_mean_err={max_mean_err:.3e}, max_cov_err={max_cov_err:.3e}")
    assert max_mean_err < 1e-11 and max_cov_err < 1e-12

    # Negative Control 1a: Drop 1 dimension from window 2 (4->3) and window 0 (9->8)
    for w_drop, t_check, err_floor in [(2, 8, 1e-5), (0, 6, 1e-10)]:
        B_trunc = enc_bases[w_drop][:-1, :]
        m_trunc = messages[w_drop][:-1]
        D_t = D_by_t[t_check]
        J_t = build_J(J0_sim, D_t, Lambdas, d)
        J_t_inv = np.linalg.inv(J_t)
        rs = slice((t_check - 1) * d, t_check * d)
        mean_bad = J_t_inv[rs, :] @ j0_sim
        for w_idx, (j, W, t_rep) in enumerate(windows):
            if t_rep <= t_check:
                M_W = sensitivity_info_form(J0_sim, D_t, Lambdas, d, t_check, W, bases[j])
                if w_idx == w_drop:
                    mean_bad = mean_bad + (M_W @ B_trunc.T) @ m_trunc
                else:
                    mean_bad = mean_bad + (M_W @ enc_bases[w_idx].T) @ messages[w_idx]
        mean_B_chk, _ = batch_cov_posterior(A, Q, m0, P0, Hs, Rs, D_t, obs_dict, t_check)
        neg_err = np.max(np.abs(mean_bad - mean_B_chk))
        print(f"  [NEG-CTRL 1a PASS] Dropping 1 dim from W{w_drop} ({dims[w_drop]}->{dims[w_drop]-1}) fails at t={t_check} with error = {neg_err:.3e} (vs exact {max_mean_err:.3e})")
        assert neg_err > err_floor and neg_err > 1000.0 * max_mean_err

    # Negative Control 1b: Naive d-dim encoding (using only t=4 sensitivity for W0) fails at t=6
    t_check = 6
    D_t = D_by_t[t_check]
    J_t = build_J(J0_sim, D_t, Lambdas, d)
    J_t_inv = np.linalg.inv(J_t)
    rs = slice((t_check - 1) * d, t_check * d)
    mean_B6, _ = batch_cov_posterior(A, Q, m0, P0, Hs, Rs, D_t, obs_dict, t_check)
    M0_t4 = sensitivity_info_form(J0_sim, D_by_t[4], Lambdas, d, 4, windows[0][1], bases[0])
    B0_naive = row_basis(M0_t4)
    l0_coords = np.concatenate([bases[0].T @ Hs[0].T @ np.linalg.solve(Rs[0], obs_dict[(0, tau)]) for tau in windows[0][1]])
    m0_naive = B0_naive @ l0_coords
    M0_t6 = sensitivity_info_form(J0_sim, D_t, Lambdas, d, t_check, windows[0][1], bases[0])
    # Best possible linear reconstruction from m0_naive (orthogonal projection onto row(B0_naive))
    mean_naive = J_t_inv[rs, :] @ j0_sim + (M0_t6 @ B0_naive.T) @ m0_naive
    for w_idx in [1, 2]:
        j, W, _ = windows[w_idx]
        M_W = sensitivity_info_form(J0_sim, D_t, Lambdas, d, t_check, W, bases[j])
        mean_naive = mean_naive + (M_W @ enc_bases[w_idx].T) @ messages[w_idx]
    neg_err_1b = np.max(np.abs(mean_naive - mean_B6))
    print(f"  [NEG-CTRL 1b PASS] Naive d-dim encoder (dim={B0_naive.shape[0]} vs {dims[0]}) fails at t=6 with error = {neg_err_1b:.3e}")
    assert neg_err_1b > 1e-3


# ============================================================================
# CHECK 2: C3 (Exact Rational SymPy Counterexample Refuting d-dim Off Schedule)
# ============================================================================

def check_2_counterexample_c3():
    print("\n" + "=" * 78)
    print("CHECK 2: C3 (Exact Rational Counterexample Refuting d-dim Encoding Off Schedule)")
    print("=" * 78)
    # d=1, A=1, Q=1, P0=1, H1=H2=1, R1=R2=1; W1={1,2} reported at t=2, W2={1,2,3} at t=3
    # Channel A: exact rational precision matrix
    J_t2 = sp.Matrix([[sp.Rational(5, 2), -1], [-1, 2]])
    J_t2_inv = J_t2.inv()
    w_t2_A = [J_t2_inv[1, 0], J_t2_inv[1, 1]]
    var_t2_A = J_t2_inv[1, 1]

    J_t3 = sp.Matrix([[sp.Rational(7, 2), -1, 0], [-1, 4, -1], [0, -1, 2]])
    J_t3_inv = J_t3.inv()
    w_t3_A = [J_t3_inv[2, 0], J_t3_inv[2, 1]]
    var_t3_A = J_t3_inv[2, 2]

    # Channel B: exact rational covariance-form conditioning
    # Prior covariance of (x_1, x_2, x_3): Cov(x_s, x_t) = 1 + min(s, t)
    # Observations at t=2: (o_{1,1}, o_{1,2}) -> Sigma_yy = [[2,2],[2,3]] + I_2 = [[3,2],[2,4]]
    Sigma_yy_t2 = sp.Matrix([[3, 2], [2, 4]])
    Sigma_xy_t2 = sp.Matrix([[2, 3]])
    gain_t2_B = Sigma_xy_t2 * Sigma_yy_t2.inv()
    w_t2_B = [gain_t2_B[0, 0], gain_t2_B[0, 1]]
    var_t2_B = sp.Rational(3, 1) - (gain_t2_B * Sigma_xy_t2.T)[0, 0]

    # Observations at t=3: (o_{1,1}, o_{1,2}, o_{2,1}, o_{2,2}, o_{2,3})
    times = [1, 2, 1, 2, 3]
    Sigma_yy_t3 = sp.Matrix(5, 5, lambda r, c: (1 + min(times[r], times[c])) + (1 if r == c else 0))
    Sigma_xy_t3 = sp.Matrix(1, 5, lambda r, c: 1 + times[c])
    gain_t3_B = Sigma_xy_t3 * Sigma_yy_t3.inv()
    w_t3_B = [gain_t3_B[0, 0], gain_t3_B[0, 1]]
    var_t3_B = sp.Rational(4, 1) - (gain_t3_B * Sigma_xy_t3.T)[0, 0]

    assert w_t2_A == w_t2_B == [sp.Rational(1, 4), sp.Rational(5, 8)]
    assert var_t2_A == var_t2_B == sp.Rational(5, 8)
    assert w_t3_A == w_t3_B == [sp.Rational(2, 45), sp.Rational(7, 45)]
    assert var_t3_A == var_t3_B == sp.Rational(26, 45)
    M_ce = sp.Matrix([w_t2_A, w_t3_A])
    det_ce = M_ce.det()
    rk_ce = M_ce.rank()
    assert det_ce == sp.Rational(1, 90) and rk_ce == 2
    print(f"  [PASS] Channel A == Channel B at t=2: weights={w_t2_A} (ratio 2:5), var={var_t2_A}")
    print(f"  [PASS] Channel A == Channel B at t=3: weights={w_t3_A} (ratio 2:7), var={var_t3_A}")
    print(f"  [PASS] 2x2 stacked sensitivity det = {det_ce}, rank = {rk_ce} > d = 1")

    # Negative Control 2: Synchronized schedule (both report at t=2, then t=3 has only o_{2,3})
    # At t=2: D_{<2} = {(1,1),(2,1)}; at t=3: D_{<2} is STILL {(1,1),(2,1)}!
    J_sync_t2 = sp.Matrix([[sp.Rational(7, 2), -1], [-1, 3]])
    J_sync_t2_inv = J_sync_t2.inv()
    w_sync_t2 = [J_sync_t2_inv[1, 0], J_sync_t2_inv[1, 1]]
    # Compare with w_t3_A:
    M_sync = sp.Matrix([w_sync_t2, w_t3_A])
    print(f"  [NEG-CTRL 2 PASS] Synchronized t=2 weights={w_sync_t2} (ratio 2:7), det(sync)={M_sync.det()}, rank={M_sync.rank()} == d=1")
    assert M_sync.det() == 0 and M_sync.rank() == 1


# ============================================================================
# CHECK 3: C4 (Block-Krylov Theorem min(s,k)*d & Aligned-Window Random Delays)
# ============================================================================

def check_3_block_krylov_c4():
    print("\n" + "=" * 78)
    print("CHECK 3: C4 (Block-Krylov Exact Dimension min(s,k)*d & Aligned Random Delays)")
    print("=" * 78)
    # 3A: Exact SymPy d=1, k=5, s=1..6
    A1, Q1, P1, L1 = sp.Matrix([[1]]), sp.Matrix([[1]]), sp.Matrix([[1]]), sp.Matrix([[1]])
    phis_d1 = [exact_sympy_phi_block(A1, Q1, P1, [c * L1] * 4, 5) for c in range(1, 7)]
    for s in range(1, 7):
        rk = sp.Matrix.vstack(*phis_d1[:s]).rank()
        assert rk == min(s, 5)
    print("  [PASS] SymPy exact d=1, k=5, s=1..6: ranks = [1, 2, 3, 4, 5, 5] == min(s, 5)")

    # 3B: Aligned windows + random delivery delays (n=3, k=5, d=1): identical vs distinct subset sums
    # Identical alpha=(1,1,1): subsets of {1,2} give total c in {1, 2, 2, 3} -> 3 distinct -> rank 3
    M_id = sp.Matrix.vstack(*[exact_sympy_phi_block(A1, Q1, P1, [c * L1] * 4, 5) for c in [1, 2, 2, 3]])
    # Distinct alpha=(1,1,3): subsets give c in {1, 2, 4, 5} -> 4 distinct -> rank 4 = 2^{n-1}
    M_dist = sp.Matrix.vstack(*[exact_sympy_phi_block(A1, Q1, P1, [c * L1] * 4, 5) for c in [1, 2, 4, 5]])
    assert M_id.rank() == 3 and M_dist.rank() == 4
    print(f"  [PASS] SymPy aligned-window random delays (n=3, k=5, d=1): identical rank={M_id.rank()} (n=3), distinct rank={M_dist.rank()} (2^(n-1)=4)")

    # 3C: Exact SymPy d=2 with non-symmetric invertible A, non-diagonal Q, P0, Lam (k=3, s=1..4)
    A2 = sp.Matrix([[1, 1], [-1, 2]])
    Q2 = sp.Matrix([[2, 1], [1, 2]])
    P2 = sp.Matrix([[2, 1], [1, 3]])
    L2 = sp.Matrix([[3, 1], [1, 2]])
    phis_d2 = [exact_sympy_phi_block(A2, Q2, P2, [c * L2] * 2, 3) for c in [1, 2, 3, 4]]
    rks_d2 = [sp.Matrix.vstack(*phis_d2[:s]).rank() for s in range(1, 5)]
    assert rks_d2 == [2, 4, 6, 6]
    print(f"  [PASS] SymPy exact d=2 (non-sym A, non-diag Q,P0,Lam), k=3, s=1..4: ranks={rks_d2} == min(s,3)*2")

    # 3D: Channel B cross-check for d=3, k=4, s=1..4 (generic non-symmetric, well-conditioned A)
    rng = np.random.default_rng(202603)
    d = 3
    A3 = np.array([[1.1, 0.4, -0.3], [-0.2, 0.9, 0.5], [0.3, -0.4, 1.2]])
    Q3 = rand_spd(rng, d)
    P3 = rand_spd(rng, d)
    H3, R3, L3, B3 = rand_sensing(rng, d, d)
    k = 4
    W0 = [1, 2, 3, 4]
    rows_A, rows_B = [], []
    Hs = [H3] * 4
    Rs = [R3] * 4
    Ls = [L3] * 4
    min_svs_A, min_svs_B = [], []
    for s in range(1, 5):
        U = [(j, tau) for j in range(s) for tau in range(1, k)]
        D = U + [(0, k)]
        rows_A.append(phi_operator(A3, Q3, P3, U, Ls, k, W0, B3))
        rows_B.append(sensitivity_cov_form(A3, Q3, P3, Hs, Rs, D, k, 0, W0))
        svA = np.linalg.svd(np.vstack(rows_A), compute_uv=False)
        svB = np.linalg.svd(np.vstack(rows_B), compute_uv=False)
        rkA = num_rank(np.vstack(rows_A), tol=1e-12)
        rkB = num_rank(np.vstack(rows_B), tol=1e-12)
        assert rkA == rkB == min(s, k) * d, f"s={s}: rkA={rkA}, rkB={rkB}, min_svA={svA[-1]:.3e}, min_svB={svB[-1]:.3e}"
        min_svs_A.append(svA[min(s, k) * d - 1])
        min_svs_B.append(svB[min(s, k) * d - 1])
    print(f"  [PASS] Channel A & Channel B generic d=3, k=4, s=1..4: ranks=[3, 6, 9, 12] == min(s,4)*3 (min_svA={min_svs_A[-1]:.3e}, min_svB={min_svs_B[-1]:.3e})")

    # Negative Control 3: Planted A = 0 collapses rank to d for all s
    A_zero = sp.zeros(2, 2)
    phis_zero = [exact_sympy_phi_block(A_zero, Q2, P2, [c * L2] * 2, 3) for c in [1, 2, 3, 4]]
    rk_zero = sp.Matrix.vstack(*phis_zero).rank()
    assert rk_zero == 2
    print(f"  [NEG-CTRL 3 PASS] Planted A=0 (d=2, k=3, s=4) collapses rank to {rk_zero} == d (not 6)")


# ============================================================================
# CHECK 4: C6 (Steady-State Round-Robin Exact Dimension (p+1)*d)
# ============================================================================

def check_4_round_robin_c6():
    print("\n" + "=" * 78)
    print("CHECK 4: C6 (Steady-State Round-Robin Exact Dimension (p+1)*d)")
    print("=" * 78)
    # 4A: Exact SymPy d=2, heterogeneous full-rank sensing, k=4, n=4 (phases 1,2,3,4 -> p=2 -> rank=6=(k-1)*d)
    A2 = sp.Matrix([[1, 1], [-1, 2]])
    Q2 = sp.Matrix([[2, 1], [1, 2]])
    P2 = sp.Matrix([[2, 1], [1, 3]])
    Lams = [
        sp.Matrix([[2, 0], [0, 1]]),  # member 1 (phase 1)
        sp.Matrix([[1, 1], [1, 3]]),  # member 2 (phase 2)
        sp.Matrix([[3, -1], [-1, 2]]), # member 3 (phase 3 = k-1, zero pending!)
        sp.Matrix([[2, 1], [1, 2]]),  # member 4 (phase 4 = k, reporting now)
    ]
    # k=4, W_4 = {1,2,3,4}. At t=4:
    # tau=1: all 4 members present; tau=2: members 2,3,4 present; tau=3: members 3,4 present
    L_t4 = [Lams[0] + Lams[1] + Lams[2] + Lams[3], Lams[1] + Lams[2] + Lams[3], Lams[2] + Lams[3]]
    # At t=5 (member 1 reports {2,3}):
    L_t5 = [L_t4[0], L_t4[1] + Lams[0], L_t4[2] + Lams[0]]
    # At t=6 (member 2 reports {3}):
    L_t6 = [L_t5[0], L_t5[1], L_t5[2] + Lams[1]]
    M_rr = sp.Matrix.vstack(
        exact_sympy_phi_block(A2, Q2, P2, L_t4, 4),
        exact_sympy_phi_block(A2, Q2, P2, L_t5, 4),
        exact_sympy_phi_block(A2, Q2, P2, L_t6, 4),
    )
    rk_rr = M_rr.rank()
    assert rk_rr == 6
    print(f"  [PASS] SymPy exact round-robin d=2, k=4, n=4 (heterogeneous): rank = {rk_rr} == (k-1)*d = 6 (< kd = 8)")

    # 4B: General phases n=3, k=5: phases (1, 3, 5) -> p=2 -> rank=6; phases (2, 4, 5) -> p=1 -> rank=4
    # Phases (1, 3, 5): member 1 pending {2,3,4}, member 2 pending {4}
    L_base_13 = [Lams[0] + Lams[1] + Lams[3], Lams[1] + Lams[3], Lams[1] + Lams[3], Lams[3]]
    L_step1_13 = [L_base_13[0], L_base_13[1] + Lams[0], L_base_13[2] + Lams[0], L_base_13[3] + Lams[0]]
    L_step2_13 = [L_step1_13[0], L_step1_13[1], L_step1_13[2], L_step1_13[3] + Lams[1]]
    rk_13 = sp.Matrix.vstack(
        exact_sympy_phi_block(A2, Q2, P2, L_base_13, 5),
        exact_sympy_phi_block(A2, Q2, P2, L_step1_13, 5),
        exact_sympy_phi_block(A2, Q2, P2, L_step2_13, 5),
    ).rank()
    # Phases (2, 4, 5): member 1 pending {3,4}, member 2 (phase 4=k-1) pending {}! -> p=1 -> rank=4
    L_base_24 = [Lams[0] + Lams[1] + Lams[3], Lams[0] + Lams[1] + Lams[3], Lams[1] + Lams[3], Lams[1] + Lams[3]]
    L_step1_24 = [L_base_24[0], L_base_24[1], L_base_24[2] + Lams[0], L_base_24[3] + Lams[0]]
    rk_24 = sp.Matrix.vstack(
        exact_sympy_phi_block(A2, Q2, P2, L_base_24, 5),
        exact_sympy_phi_block(A2, Q2, P2, L_step1_24, 5),
    ).rank()
    assert rk_13 == 6 and rk_24 == 4
    print(f"  [PASS] SymPy exact phases d=2, k=5, n=3: phases (1,3,5) p=2 -> rank={rk_13}; phases (2,4,5) p=1 -> rank={rk_24}")

    # 4C: End-to-end fusion test on steady-state round-robin d=2, k=4, n=4 using 6 numbers (not 8)
    rng = np.random.default_rng(202604)
    d = 2
    A_np = np.array([[0.9, 0.3], [-0.2, 0.8]])
    Q_np = rand_spd(rng, d)
    P0_np = rand_spd(rng, d)
    m0_np = rng.normal(size=d)
    Hs, Rs, Ls, Bs = [], [], [], []
    for _ in range(4):
        Hj, Rj, Lj, Bj = rand_sensing(rng, d, d)
        Hs.append(Hj); Rs.append(Rj); Ls.append(Lj); Bs.append(Bj)
    # Build steady-state windows over T=8:
    # Warm-up initial segments at t=1,2,3 (members 0,1,2) and full period-4 windows thereafter
    rr_windows = [
        (0, [1], 1), (1, [1, 2], 2), (2, [1, 2, 3], 3), (3, [1, 2, 3, 4], 4),
        (0, [2, 3, 4, 5], 5), (1, [3, 4, 5, 6], 6), (2, [4, 5, 6, 7], 7), (3, [5, 6, 7, 8], 8),
    ]
    T_rr = 8
    x_tr = np.zeros((T_rr + 1, d))
    x_tr[0] = rng.multivariate_normal(m0_np, P0_np)
    obs_rr = {}
    for t in range(1, T_rr + 1):
        x_tr[t] = A_np @ x_tr[t - 1] + rng.multivariate_normal(np.zeros(d), Q_np)
        for j in range(4):
            obs_rr[(j, t)] = Hs[j] @ x_tr[t] + rng.multivariate_normal(np.zeros(d), Rs[j])
    D_rr = {t: [(j, tau) for (j, W, tr) in rr_windows if tr <= t for tau in W] for t in range(1, T_rr + 1)}
    J0_rr = build_prior_precision(A_np, Q_np, P0_np, T_rr)
    j0_rr = build_j0(A_np, Q_np, P0_np, m0_np, T_rr)
    # Check exact message dim of steady-state window 3 (member 3, W=[1,2,3,4], t_rep=4)
    rows_w3 = [sensitivity_info_form(J0_rr, D_rr[t], Ls, d, t, [1, 2, 3, 4], Bs[3]) for t in range(4, T_rr + 1)]
    B_w3 = row_basis(np.vstack(rows_w3))
    assert B_w3.shape[0] == 6
    # Reconstruct full hub posterior at t=4..8 using compressed windows for all windows
    enc_rr, msg_rr = {}, {}
    for idx, (j, W, tr) in enumerate(rr_windows):
        rows = [sensitivity_info_form(J0_rr, D_rr[t], Ls, d, t, W, Bs[j]) for t in range(tr, T_rr + 1)]
        Bw = row_basis(np.vstack(rows))
        enc_rr[idx] = Bw
        lc = np.concatenate([Bs[j].T @ Hs[j].T @ np.linalg.solve(Rs[j], obs_rr[(j, tau)]) for tau in W])
        msg_rr[idx] = Bw @ lc
    max_err_rr = 0.0
    for t in range(4, T_rr + 1):
        J_t = build_J(J0_rr, D_rr[t], Ls, d)
        J_t_inv = np.linalg.inv(J_t)
        rs = slice((t - 1) * d, t * d)
        mean_A = J_t_inv[rs, :] @ j0_rr
        for idx, (j, W, tr) in enumerate(rr_windows):
            if tr <= t:
                M_W = sensitivity_info_form(J0_rr, D_rr[t], Ls, d, t, W, Bs[j])
                mean_A = mean_A + (M_W @ enc_rr[idx].T) @ msg_rr[idx]
        mean_B, _ = batch_cov_posterior(A_np, Q_np, m0_np, P0_np, Hs, Rs, D_rr[t], obs_rr, t)
        max_err_rr = max(max_err_rr, np.max(np.abs(mean_A - mean_B)))
    print(f"  [PASS] End-to-end round-robin fusion (W3 dim={B_w3.shape[0]}/8): max_err vs Channel B = {max_err_rr:.3e}")
    assert max_err_rr < 1e-12


# ============================================================================
# CHECK 5: C2 & C5 (Random Schedules, Subspace-Coupled Formula, Bounded Delay,
#                   Causal Broadcast, Pre-Window rank(A), Decoupled Counterexample)
# ============================================================================

def check_5_random_and_subspace():
    print("\n" + "=" * 78)
    print("CHECK 5: C2 & C5 (Random Bernoulli, Subspace Coupling, Bounded Delay, Broadcast)")
    print("=" * 78)
    rng = np.random.default_rng(202605)

    # 5A: Random Bernoulli n=2 (decentralized, unknown u in 0..k-1), Channel A vs Channel B
    for d, r1, r2, k, expected in [
        (2, 2, 1, 4, 2 + 3 * 1),   # d + (k-1)*r2 = 5 < k*r1 = 8
        (3, 3, 1, 4, 3 + 3 * 1),   # d + (k-1)*r2 = 6 < k*r1 = 12
        (3, 3, 2, 4, 3 + 3 * 2),   # d + (k-1)*r2 = 9 < k*r1 = 12
        (3, 1, 3, 4, 4 * 1),       # full late coverage -> k*r1 = 4
        (3, 2, 3, 4, 4 * 2),       # full late coverage -> k*r1 = 8
    ]:
        A = rng.normal(size=(d, d)) * 0.5 + 0.6 * np.eye(d)
        Q = rand_spd(rng, d)
        P0 = rand_spd(rng, d)
        H1, R1, L1, B1 = rand_sensing(rng, d, r1)
        H2, R2, L2, B2 = rand_sensing(rng, d, r2)
        W1 = list(range(1, k + 1))
        rows_A, rows_B = [], []
        for u in range(k):
            U = [(0, tau) for tau in range(1, k)] + [(1, tau) for tau in range(1, u + 1)]
            D = U + [(0, k)]
            rows_A.append(phi_operator(A, Q, P0, U, [L1, L2], k, W1, B1))
            rows_B.append(sensitivity_cov_form(A, Q, P0, [H1, H2], [R1, R2], D, k, 0, W1))
        rkA = num_rank(np.vstack(rows_A))
        rkB = num_rank(np.vstack(rows_B))
        assert rkA == rkB == expected
        print(f"  [PASS] Bernoulli n=2 (d={d}, r1={r1}, r2={r2}, k={k}): rkA={rkA} == rkB={rkB} == {expected} (blind={k*r1})")

    # 5B: Multi-member collective full-rank coverage (d=3, r1=2, member 2 has r2=1, member 3 has r3=2, span=R^3)
    d, k = 3, 4
    A = rng.normal(size=(d, d)) * 0.5 + 0.6 * np.eye(d)
    Q = rand_spd(rng, d)
    P0 = rand_spd(rng, d)
    H1, R1, L1, B1 = rand_sensing(rng, d, 2)
    H2, R2, L2, B2 = rand_sensing(rng, d, 1)
    H3, R3, L3, B3 = rand_sensing(rng, d, 2)
    assert num_rank(np.vstack([H2, H3])) == 3
    W1 = [1, 2, 3, 4]
    # Realizable chain stepping (u2, u3): (0,0)->(1,0)->(1,1)->(2,1)->(2,2)->(3,2)->(3,3)
    chain = [(0, 0), (1, 0), (1, 1), (2, 1), (2, 2), (3, 2), (3, 3)]
    rows_A, rows_B = [], []
    for (u2, u3) in chain:
        U = [(0, tau) for tau in range(1, k)] + [(1, tau) for tau in range(1, u2 + 1)] + [(2, tau) for tau in range(1, u3 + 1)]
        rows_A.append(phi_operator(A, Q, P0, U, [L1, L2, L3], k, W1, B1))
        rows_B.append(sensitivity_cov_form(A, Q, P0, [H1, H2, H3], [R1, R2, R3], U + [(0, k)], k, 0, W1))
    rkA = num_rank(np.vstack(rows_A))
    rkB = num_rank(np.vstack(rows_B))
    assert rkA == rkB == 8  # k * r1 = 4 * 2 = 8
    print(f"  [PASS] Multi-member collective span=R^3 (d=3, r1=2, r2=1, r3=2, k=4): rkA={rkA} == rkB={rkB} == k*r1=8")

    # 5C: Bounded delivery delay Delta_max < k
    d, r1, r2, k, dmax = 2, 2, 1, 6, 2
    A = rng.normal(size=(d, d)) * 0.5 + 0.6 * np.eye(d)
    Q = rand_spd(rng, d)
    P0 = rand_spd(rng, d)
    H1, R1, L1, B1 = rand_sensing(rng, d, r1)
    H2, R2, L2, B2 = rand_sensing(rng, d, r2)
    W1 = list(range(1, k + 1))
    fixed_taus = list(range(1, k - dmax))
    unc_taus = list(range(k - dmax, k))
    rows_A, rows_B = [], []
    for mask in range(1 << len(unc_taus)):
        U = [(0, tau) for tau in range(1, k)] + [(1, tau) for tau in fixed_taus]
        for idx, tau in enumerate(unc_taus):
            if (mask >> idx) & 1:
                U.append((1, tau))
        rows_A.append(phi_operator(A, Q, P0, U, [L1, L2], k, W1, B1))
        rows_B.append(sensitivity_cov_form(A, Q, P0, [H1, H2], [R1, R2], U + [(0, k)], k, 0, W1))
    rkA, rkB = num_rank(np.vstack(rows_A)), num_rank(np.vstack(rows_B))
    assert rkA == rkB == d + dmax * r2 == 4
    print(f"  [PASS] Bounded delay (d=2, r1=2, r2=1, k=6, Delta_max=2): rkA={rkA} == rkB={rkB} == 4 (blind=12)")

    # 5D: Causal schedule broadcast (n=2, k=6, d=2, member 1 knows u2=1 at t=6, random future T2 > 6)
    # Only two <6 sets ever occur: U_1 (m2 has {1}) and U_2 (m2 has {1..5}) -> dim = 2d = 4 < kd = 12
    d, k = 2, 6
    A = rng.normal(size=(d, d)) * 0.5 + 0.6 * np.eye(d)
    Q = rand_spd(rng, d)
    P0 = rand_spd(rng, d)
    H1, R1, L1, B1 = rand_sensing(rng, d, 2)
    H2, R2, L2, B2 = rand_sensing(rng, d, 2)
    W1 = list(range(1, k + 1))
    U1 = [(0, tau) for tau in range(1, k)] + [(1, 1)]
    U2 = [(0, tau) for tau in range(1, k)] + [(1, tau) for tau in range(1, k)]
    rkA = num_rank(np.vstack([phi_operator(A, Q, P0, U1, [L1, L2], k, W1, B1),
                              phi_operator(A, Q, P0, U2, [L1, L2], k, W1, B1)]))
    rkB = num_rank(np.vstack([sensitivity_cov_form(A, Q, P0, [H1, H2], [R1, R2], U1 + [(0, k)], k, 0, W1),
                              sensitivity_cov_form(A, Q, P0, [H1, H2], [R1, R2], U2 + [(0, k), (1, k), (1, 7), (1, 8)], 8, 0, W1)]))
    assert rkA == rkB == 4
    print(f"  [PASS] Causal schedule broadcast (n=2, d=2, k=6, random future T2): rkA={rkA} == rkB={rkB} == 2d=4 (blind=12)")

    # 5E: Pre-window late observations only (T_late^pre != empty, T_late^in = empty) with rank(A) < d
    d, a, k, rankA = 3, 2, 5, 2
    A_sing = rng.normal(size=(d, rankA)) @ rng.normal(size=(rankA, d))
    Q = rand_spd(rng, d)
    P0 = rand_spd(rng, d)
    H1, R1, L1, B1 = rand_sensing(rng, d, d)
    H2, R2, L2, B2 = rand_sensing(rng, d, d)
    b = a + k
    W1 = list(range(a + 1, b + 1))
    rows_A = []
    for trial in range(25):
        U = [(0, tau) for tau in range(a + 1, b)]
        for tau in range(1, a + 1):
            for _ in range(int(rng.integers(0, 4))):
                U.append((1, tau))
        rows_A.append(phi_operator(A_sing, Q, P0, U, [L1, L2], b, W1, B1))
    rk_pre = num_rank(np.vstack(rows_A))
    assert rk_pre == d + rankA == 5
    print(f"  [PASS] Pre-window late obs only (d=3, a=2, k=5, rankA=2): rank={rk_pre} == d+rankA=5 (blind=15)")

    # 5F: Decoupled partial-sensing counterexample (refutes universal equality r* = min(d+(k-1)r2, k*r1) when r1 < d)
    A_dec = sp.eye(2)
    Q_dec = sp.eye(2)
    P_dec = sp.eye(2)
    L1_dec = sp.Matrix([[1, 0], [0, 0]])
    L2_dec = sp.Matrix([[0, 0], [0, 1]])
    B1_dec = sp.Matrix([[1], [0]])
    B1_block = sp.diag(B1_dec, B1_dec, B1_dec, B1_dec)
    rows_dec = []
    for u in range(4):
        lam_taus = [L1_dec + (L2_dec if tau <= u else sp.zeros(2, 2)) for tau in range(1, 4)]
        Phi_u = exact_sympy_phi_block(A_dec, Q_dec, P_dec, lam_taus, 4) * B1_block
        rows_dec.append(Phi_u)
    rk_dec = sp.Matrix.vstack(*rows_dec).rank()
    assert rk_dec == 1
    print(f"  [PASS] SymPy decoupled partial-sensing counterexample (d=2, r1=1, r2=1, k=4): rank={rk_dec} < min(2+3, 4)=4")


# ============================================================================
# CHECK 6: C7 (Degenerate Boundary Cases Q_x = 0 and A = 0 via Channel B)
# ============================================================================

def check_6_degenerate_c7():
    print("\n" + "=" * 78)
    print("CHECK 6: C7 (Boundary Collapse for Q_x = 0 and A = 0)")
    print("=" * 78)
    rng = np.random.default_rng(202606)
    d, k = 2, 5
    A = np.array([[0.9, 0.4], [-0.3, 1.1]])
    P0 = rand_spd(rng, d)
    H1, R1, L1, B1 = rand_sensing(rng, d, 2)
    H2, R2, L2, B2 = rand_sensing(rng, d, 2)
    W1 = list(range(1, k + 1))

    # 6A: Q_x = 0 (Channel B covariance-form sensitivity across all 2^{k-1} subsets!)
    Q_zero = np.zeros((d, d))
    rows_Q0 = []
    for mask in range(1 << (k - 1)):
        U = [(0, tau) for tau in range(1, k)] + [(1, tau) for tau in range(1, k) if (mask >> (tau - 1)) & 1]
        rows_Q0.append(sensitivity_cov_form(A, Q_zero, P0, [H1, H2], [R1, R2], U + [(0, k)], k, 0, W1))
    rk_Q0 = num_rank(np.vstack(rows_Q0))
    assert rk_Q0 == d
    print(f"  [PASS] Q_x = 0 (d=2, k=5, all 16 subsets): Channel B sensitivity rank = {rk_Q0} == d = 2")

    # 6B: A = 0, Q_x > 0, r1 = 2, d = 3
    d3, r1_3 = 3, 2
    A_zero = np.zeros((d3, d3))
    Q3 = rand_spd(rng, d3)
    P3 = rand_spd(rng, d3)
    H1_3, R1_3, L1_3, B1_3 = rand_sensing(rng, d3, r1_3)
    H2_3, R2_3, L2_3, B2_3 = rand_sensing(rng, d3, d3)
    rows_A0_A, rows_A0_B = [], []
    for mask in range(1 << (k - 1)):
        U = [(0, tau) for tau in range(1, k)] + [(1, tau) for tau in range(1, k) if (mask >> (tau - 1)) & 1]
        rows_A0_A.append(phi_operator(A_zero, Q3, P3, U, [L1_3, L2_3], k, W1, B1_3))
        rows_A0_B.append(sensitivity_cov_form(A_zero, Q3, P3, [H1_3, H2_3], [R1_3, R2_3], U + [(0, k)], k, 0, W1))
    rk_A0_A = num_rank(np.vstack(rows_A0_A))
    rk_A0_B = num_rank(np.vstack(rows_A0_B))
    assert rk_A0_A == rk_A0_B == r1_3
    print(f"  [PASS] A = 0, Q_x > 0 (d=3, r1=2, k=5, all 16 subsets): rkA={rk_A0_A} == rkB={rk_A0_B} == r1 = 2")


if __name__ == "__main__":
    check_1_master_and_fusion()
    check_2_counterexample_c3()
    check_3_block_krylov_c4()
    check_4_round_robin_c6()
    check_5_random_and_subspace()
    check_6_degenerate_c7()
    print("\n" + "=" * 78)
    print("ALL 6 CHECK SUITES + 3 PLANTED-ERROR NEGATIVE CONTROLS PASSED.")
    print("=" * 78)
