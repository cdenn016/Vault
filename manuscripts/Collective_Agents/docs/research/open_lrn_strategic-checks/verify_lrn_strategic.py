"""
Independent two-channel verification + planted-error negative controls
for open:lrn-strategic (Claims C1-C6).

Channel A: Exact closed-form formulas and symbolic rational identities (SymPy).
Channel B: Direct numerical optimization, Monte Carlo / raw-definition
           expectations, empirical OLS grounded learning, and explicit
           perturbation/gradient checks that never pass through Channel A.
"""

import sys
import numpy as np
import sympy as sp
from scipy.optimize import minimize

rng = np.random.default_rng(20261122)


def rand_spd(n, scale=1.0):
    M = rng.normal(size=(n, n))
    return scale * (M @ M.T + 0.4 * np.eye(n))


def mat_sqrt(M):
    w, V = np.linalg.eigh(M)
    assert np.all(w > 0), "Matrix not SPD"
    return V @ np.diag(np.sqrt(w)) @ V.T


def mat_inv_sqrt(M):
    w, V = np.linalg.eigh(M)
    assert np.all(w > 0), "Matrix not SPD"
    return V @ np.diag(1.0 / np.sqrt(w)) @ V.T


def raw_expected_sender_loss(A, d, Sz, H_hat, d_hat, K_hat, P, m_i, R, M_S, W, b):
    """Channel B: exact quadratic expectation directly from y = A eta + d + zeta + nu."""
    # m_hat - (W eta + b) = mu_e + (K_hat A - W)(eta - m_i) + K_hat(zeta + nu)
    mu_e = (np.eye(P.shape[0]) - W) @ m_i - b + K_hat @ (A @ m_i + d - d_hat - H_hat @ m_i)
    cov_e = (K_hat @ A - W) @ P @ (K_hat @ A - W).T + K_hat @ (Sz + R) @ K_hat.T
    return float(mu_e @ M_S @ mu_e + np.trace(M_S @ cov_e))


def main():
    print("=================================================================")
    print("VERIFICATION SUITE FOR open:lrn-strategic (Claims C1 - C6)")
    print("=================================================================")

    # -----------------------------------------------------------------
    # 0. Convention lock test values (exact rational SymPy)
    # -----------------------------------------------------------------
    print("\n[0] Convention lock test values (SymPy exact rational)")
    H_sym, D_sym, P_sym, R_sym, w_sym, b_sym, m_sym = sp.symbols(
        "H D P R w b m_i", real=True
    )
    # Registered test instance: K=rc=1, P=2, R=1, H=1, M_S=1, m_i=0, b=1
    # Evaluate Gamma_S = 1 - 2w, Sigma_mhat(A=1, Sz=0) = 2/3, J_sil(w=1) = 3, J_S(A=1,w=1) = 7/3
    val_Sigma = sp.Rational(2, 1) * 1**2 / (1**2 * 2 + 1) * sp.Rational(2, 1)  # P^2 A^2 / (A^2 P + R)
    # Wait: P=2, A=1, R=1 => Sigma_mhat = P^2 A^2 / (A^2 P + R) = 4 / 3!
    P0, R0, H0, b0 = sp.Rational(2), sp.Rational(1), sp.Rational(1), sp.Rational(1)
    Sig0 = P0**2 * H0**2 / (H0**2 * P0 + R0)
    J_sil_w1 = b0**2 + 1**2 * P0  # 1 + 2 = 3
    J_honest_w1 = J_sil_w1 + (1 - 2 * 1) * Sig0  # 3 - 4/3 = 5/3
    assert Sig0 == sp.Rational(4, 3), f"Unexpected Sig0={Sig0}"
    assert J_honest_w1 == sp.Rational(5, 3), f"Unexpected J_honest_w1={J_honest_w1}"
    # Check against direct expansion: (K* A - 1)^2 P + K*^2 R + b^2
    K0 = H0 * P0 / (H0**2 * P0 + R0)  # 2/3
    J_direct_w1 = (K0 * H0 - 1)**2 * P0 + K0**2 * R0 + b0**2
    assert sp.simplify(J_direct_w1 - J_honest_w1) == 0
    # Check Nash equilibrium at w=1/2, b=0, m_i=0: A* = sqrt((1/2)/(1/2) * R/P) = sqrt(1/2)
    A_nash_half = sp.sqrt(sp.Rational(1, 2))
    K_nash_half = A_nash_half * P0 / (A_nash_half**2 * P0 + R0)
    assert sp.simplify(K_nash_half * A_nash_half - sp.Rational(1, 2)) == 0
    # Check scalar KL test value at D=1, d=1, Sz=1, P=2, R=1, m_bar=0:
    # 1/2 * (1*2/1 + 1/1 + 1 - ln(2)) = 2 - (1/2) ln 2
    kl_test = sp.Rational(1, 2) * (1**2 * P0 / R0 + 1**2 / R0 + 1 / R0 - sp.log(1 + 1 / R0))
    assert sp.simplify(kl_test - (2 - sp.Rational(1, 2) * sp.log(2))) == 0
    print(f"  Registered scalar test: P=2, R=1, H=1, b=1, m_i=0, w=1 -> Sigma_mhat={Sig0}, J_S(D=0)={J_honest_w1}")
    print(f"  Nash test (w=1/2, b=0): A*=sqrt(1/2), K*A*={sp.simplify(K_nash_half*A_nash_half)}")
    print(f"  KL test (D=1, d=1, Sz=1, m_bar=0): D_KL = {kl_test} = {float(kl_test):.10f}")

    # -----------------------------------------------------------------
    # 1. CLAIM C1: Unconstrained Stackelberg with intercept absorption
    # -----------------------------------------------------------------
    print("\n[1] Claim C1: Stackelberg loss identity, Ky Fan infimum, gradient at D=0")
    max_id_err = 0.0
    max_grad_err = 0.0
    for (K, rc) in [(1, 1), (3, 2), (2, 3), (4, 3), (3, 3)]:
        P = rand_spd(K)
        R = rand_spd(rc, 0.4)
        M_S = rand_spd(K)
        W = rng.normal(size=(K, K))
        b = rng.normal(size=K)
        m_i = rng.normal(size=K)
        H = rng.normal(size=(rc, K))
        D = rng.normal(size=(rc, K))
        d = rng.normal(size=rc)
        Sz = rand_spd(rc, 0.25)
        A = H + D

        # Channel B: raw expectation + Monte Carlo spot check on first case
        S = A @ P @ A.T + R + Sz
        K_A = P @ A.T @ np.linalg.inv(S)
        J_raw = raw_expected_sender_loss(A, d, Sz, A, d, K_A, P, m_i, R, M_S, W, b)

        # Channel A: closed-form C1 identity
        mu_sil = (np.eye(K) - W) @ m_i - b
        J_sil = float(mu_sil @ M_S @ mu_sil + np.trace(M_S @ W @ P @ W.T))
        Gamma_S = M_S - M_S @ W - W.T @ M_S
        P_half = mat_sqrt(P)
        P_mhalf = mat_inv_sqrt(P)
        Gamma_tilde = P_half @ Gamma_S @ P_half
        Sig_mhat = P @ A.T @ np.linalg.inv(S) @ A @ P
        X = P_mhalf @ Sig_mhat @ P_mhalf
        J_form = J_sil + float(np.trace(Gamma_tilde @ X))
        err = abs(J_raw - J_form)
        max_id_err = max(max_id_err, err)
        assert err < 1e-12, f"C1 identity error {err}"

        # Check independence of d
        d_alt = d + rng.normal(size=rc) * 10.0
        J_raw_alt = raw_expected_sender_loss(A, d_alt, Sz, A, d_alt, K_A, P, m_i, R, M_S, W, b)
        assert abs(J_raw - J_raw_alt) < 1e-12, "C1 should be independent of d"

        # Check gradient at D=0, Sz=0 via finite differences (Channel B) vs 2 R^{-1} H P+ Gamma_S P+ (Channel A)
        S0 = H @ P @ H.T + R
        K0_m = P @ H.T @ np.linalg.inv(S0)
        P_plus = P - K0_m @ H @ P
        grad_A = 2.0 * np.linalg.inv(R) @ H @ P_plus @ Gamma_S @ P_plus
        grad_FD = np.zeros_like(H)
        eps = 1e-6
        for i in range(rc):
            for j in range(K):
                E = np.zeros_like(H)
                E[i, j] = eps
                Ap, Am = H + E, H - E
                Kp = P @ Ap.T @ np.linalg.inv(Ap @ P @ Ap.T + R)
                Km = P @ Am.T @ np.linalg.inv(Am @ P @ Am.T + R)
                Jp = raw_expected_sender_loss(Ap, d, np.zeros((rc, rc)), Ap, d, Kp, P, m_i, R, M_S, W, b)
                Jm = raw_expected_sender_loss(Am, d, np.zeros((rc, rc)), Am, d, Km, P, m_i, R, M_S, W, b)
                grad_FD[i, j] = (Jp - Jm) / (2.0 * eps)
        g_err = np.linalg.norm(grad_A - grad_FD) / max(1.0, np.linalg.norm(grad_A))
        max_grad_err = max(max_grad_err, g_err)
        assert g_err < 1e-8, f"C1 relative gradient mismatch {g_err}"

    # Verify Ky Fan infimum & selective disclosure on indefinite Gamma_tilde (K=4, rc=3, n_-=2)
    K, rc = 4, 3
    P = rand_spd(K)
    R = rand_spd(rc, 0.3)
    M_S = rand_spd(K)
    # Construct W so Gamma_tilde has eigenvalues (-2.5, -0.8, +0.6, +1.9) -> n_- = 2 < r = 3
    Q_orth, _ = np.linalg.qr(rng.normal(size=(K, K)))
    target_evals = np.array([-2.5, -0.8, 0.6, 1.9])
    Gamma_tilde_t = Q_orth @ np.diag(target_evals) @ Q_orth.T
    P_half, P_mhalf = mat_sqrt(P), mat_inv_sqrt(P)
    Gamma_S_t = P_mhalf @ Gamma_tilde_t @ P_mhalf
    # Need M_S - M_S W - W^T M_S = Gamma_S_t => W = 0.5*(I - M_S^{-1} Gamma_S_t) + M_S^{-1} Skew
    Skew_raw = rng.normal(size=(K, K))
    Skew = 0.5 * (Skew_raw - Skew_raw.T)
    W_indef = 0.5 * (np.eye(K) - np.linalg.inv(M_S) @ Gamma_S_t) + np.linalg.inv(M_S) @ Skew
    # Verify Gamma_S matches
    assert np.linalg.norm((M_S - M_S @ W_indef - W_indef.T @ M_S) - Gamma_S_t) < 1e-12
    b_t, m_t = rng.normal(size=K), rng.normal(size=K)
    mu_t = (np.eye(K) - W_indef) @ m_t - b_t
    J_sil_t = float(mu_t @ M_S @ mu_t + np.trace(M_S @ W_indef @ P @ W_indef.T))
    inf_C1 = J_sil_t + (-2.5 + -0.8)  # sum of min(r, n_-) = 2 negative eigenvalues
    # Approach infimum with rank-2 singular A_a = a * [u1, u2] @ [v1, v2]^T P^{-1/2}
    R_half = mat_sqrt(R)
    for a in [10.0, 100.0, 1000.0]:
        A_a = a * R_half[:, :2] @ Q_orth[:, :2].T @ P_mhalf
        K_a = P @ A_a.T @ np.linalg.inv(A_a @ P @ A_a.T + R)
        J_a = raw_expected_sender_loss(A_a, np.zeros(rc), np.zeros((rc, rc)), A_a, np.zeros(rc), K_a, P, m_t, R, M_S, W_indef, b_t)
        assert J_a > inf_C1, "Finite A cannot beat or equal open infimum when n_- >= 1"
    gap_1000 = J_a - inf_C1
    assert gap_1000 < 1e-4, f"Rank-2 singular sequence should approach infimum, gap={gap_1000}"
    # Check 500 random A never beat inf_C1
    for _ in range(500):
        A_r = rng.normal(size=(rc, K)) * (10 ** rng.uniform(-1, 2))
        K_r = P @ A_r.T @ np.linalg.inv(A_r @ P @ A_r.T + R)
        J_r = raw_expected_sender_loss(A_r, np.zeros(rc), np.zeros((rc, rc)), A_r, np.zeros(rc), K_r, P, m_t, R, M_S, W_indef, b_t)
        assert J_r >= inf_C1 - 1e-11, f"Random A beat Ky Fan infimum: {J_r} < {inf_C1}"
    # Check Monte Carlo validation of raw formula (50,000 draws)
    N_mc = 50000
    eta_mc = rng.multivariate_normal(m_t, P, size=N_mc)
    nu_mc = rng.multivariate_normal(np.zeros(rc), R, size=N_mc)
    A_mc = rng.normal(size=(rc, K))
    d_mc = rng.normal(size=rc)
    y_mc = eta_mc @ A_mc.T + d_mc + nu_mc
    K_mc = P @ A_mc.T @ np.linalg.inv(A_mc @ P @ A_mc.T + R)
    mhat_mc = m_t + (y_mc - d_mc - m_t @ A_mc.T) @ K_mc.T
    err_mc = mhat_mc - (eta_mc @ W_indef.T + b_t)
    J_mc = float(np.mean(np.sum((err_mc @ M_S) * err_mc, axis=1)))
    J_mc_se = float(np.std(np.sum((err_mc @ M_S) * err_mc, axis=1)) / np.sqrt(N_mc))
    Sig_mc = P @ A_mc.T @ np.linalg.inv(A_mc @ P @ A_mc.T + R) @ A_mc @ P
    J_th_mc = J_sil_t + float(np.trace(Gamma_S_t @ Sig_mc))
    z_mc = abs(J_mc - J_th_mc) / J_mc_se
    assert z_mc < 3.5, f"MC disagreement z={z_mc}"

    print(f"  Max identity residual across 5 (K,rc) dims: {max_id_err:.3e}")
    print(f"  Max gradient residual at D=0 (FD vs closed form): {max_grad_err:.3e}")
    print(f"  Indefinite Gamma_tilde (n_-=2 < r=3): rank-2 A(a=1000) gap to Ky Fan inf = {gap_1000:.3e}; 500 random A all > inf")
    print(f"  Monte Carlo (N={N_mc}): J_mc={J_mc:.4f} +/- {J_mc_se:.4f} vs J_th={J_th_mc:.4f} (z={z_mc:.2f})")

    # Planted-error negative control for C1: drop factor of 2 in Gamma_S = M_S - M_S W (missing W^T M_S)
    Gamma_wrong = M_S - M_S @ W_indef
    J_wrong = J_sil_t + float(np.trace(Gamma_wrong @ Sig_mc))
    c1_planted_err = abs(J_wrong - J_th_mc)
    assert c1_planted_err > 1.0, "Planted error C1 failed to separate"
    print(f"  [NEG-CTRL C1] Dropping W^T M_S shifts J_S by {c1_planted_err:.4f} (> 1.0, detected!)")

    # -----------------------------------------------------------------
    # 2. CLAIM C2: Power-penalized Stackelberg water-filling
    # -----------------------------------------------------------------
    print("\n[2] Claim C2: Multivariate water-filling exact closed form")
    max_wf_gap = 0.0
    for (K, rc, lam, label) in [
        (3, 2, 0.2, "full-rank active"),
        (4, 3, 1.5, "partial-rank singular"),
        (3, 3, 500.0, "complete silencing"),
        (2, 3, 0.1, "rc > K"),
    ]:
        P = rand_spd(K)
        R = rand_spd(rc, 0.4)
        M_S = rand_spd(K)
        W = 0.9 * np.eye(K) + 0.5 * rng.normal(size=(K, K))
        b = rng.normal(size=K)
        m_i = rng.normal(size=K)
        mu_sil = (np.eye(K) - W) @ m_i - b
        J_sil = float(mu_sil @ M_S @ mu_sil + np.trace(M_S @ W @ P @ W.T))
        Gamma_S = M_S - M_S @ W - W.T @ M_S
        P_half, P_mhalf = mat_sqrt(P), mat_inv_sqrt(P)
        Gamma_tilde = P_half @ Gamma_S @ P_half
        evals_G, V_G = np.linalg.eigh(Gamma_tilde)  # ascending
        evals_R, U_R = np.linalg.eigh(R)            # ascending
        r = min(rc, K)

        # Channel A: water-filling formula
        s2_opt = np.array([max(0.0, np.sqrt(max(-evals_G[j], 0.0) / (lam * evals_R[j])) - 1.0) for j in range(r)])
        A_wf = np.zeros((rc, K))
        for j in range(r):
            A_wf += np.sqrt(evals_R[j] * s2_opt[j]) * np.outer(U_R[:, j], V_G[:, j] @ P_mhalf)
        J_wf_formula = J_sil - sum(max(0.0, np.sqrt(max(-evals_G[j], 0.0)) - np.sqrt(lam * evals_R[j]))**2 for j in range(r))

        # Channel B: direct numerical BFGS over raw (A, L_zeta) with Sigma_zeta = L_zeta L_zeta^T
        def obj_raw(vec):
            Am = vec[:rc * K].reshape(rc, K)
            Lm = vec[rc * K:].reshape(rc, rc)
            Szm = Lm @ Lm.T
            Km = P @ Am.T @ np.linalg.inv(Am @ P @ Am.T + R + Szm)
            return raw_expected_sender_loss(Am, np.zeros(rc), Szm, Am, np.zeros(rc), Km, P, m_i, R, M_S, W, b) + lam * float(np.trace(Am @ P @ Am.T + Szm))

        J_wf_eval = obj_raw(np.concatenate([A_wf.ravel(), np.zeros(rc * rc)]))
        assert abs(J_wf_eval - J_wf_formula) < 1e-12
        best_bfgs = np.inf
        for _ in range(12):
            x0 = rng.normal(size=rc * K + rc * rc) * 0.4
            res = minimize(obj_raw, x0, method="BFGS", options={"gtol": 1e-10, "maxiter": 600})
            if res.fun < best_bfgs:
                best_bfgs = res.fun
        gap = abs(J_wf_formula - best_bfgs)
        max_wf_gap = max(max_wf_gap, gap)
        assert J_wf_formula <= best_bfgs + 1e-9, f"BFGS beat water-filling! {best_bfgs} < {J_wf_formula}"
        assert gap < 1e-8, f"Water-filling vs BFGS gap {gap}"
        rank_active = int(np.sum(s2_opt > 0))
        print(f"  Case ({label}, K={K}, rc={rc}, lam={lam}): rank={rank_active}, J_wf={J_wf_formula:.8f}, J_bfgs={best_bfgs:.8f}, gap={gap:.2e}")

    # Planted-error negative control for C2: wrong eigenvector pairing (pair smallest -lambda_j with largest rho_j reversed!)
    K, rc, lam = 3, 3, 0.05
    P = np.diag([1.0, 2.0, 3.0])
    R = np.diag([0.1, 0.5, 2.5])
    M_S = np.eye(K)
    W = np.diag([1.5, 1.0, 0.7])
    Gamma_tilde = P @ (M_S - 2 * W)
    evals_G, V_G = np.linalg.eigh(Gamma_tilde)
    evals_R, U_R = np.linalg.eigh(R)
    val_right = -sum(max(0.0, np.sqrt(max(-evals_G[j], 0.0)) - np.sqrt(lam * evals_R[j]))**2 for j in range(3))
    val_wrong_order = -sum(max(0.0, np.sqrt(max(-evals_G[j], 0.0)) - np.sqrt(lam * evals_R[2 - j]))**2 for j in range(3))
    assert val_wrong_order - val_right > 0.1, "Planted error C2 failed"
    print(f"  [NEG-CTRL C2] Reversing R-eigenvalue pairing worsens objective by +{val_wrong_order - val_right:.6f} (detected!)")

    # -----------------------------------------------------------------
    # 3. CLAIM C3: One-shot BR & simultaneous-move Nash equilibria
    # -----------------------------------------------------------------
    print("\n[3] Claim C3: One-shot BR & vector Nash equilibrium (including null-channel Sigma_zeta)")
    # 3a. One-shot BR vs BFGS
    K, rc = 3, 2
    P = rand_spd(K)
    R = rand_spd(rc, 0.3)
    M_S = rand_spd(K)
    W = rng.normal(size=(K, K))
    b = rng.normal(size=K)
    m_i = rng.normal(size=K)
    H_hat = rng.normal(size=(rc, K))
    d_hat = rng.normal(size=rc)
    K_hat = P @ H_hat.T @ np.linalg.inv(H_hat @ P @ H_hat.T + R)
    # Channel A: closed form
    KM_inv = np.linalg.inv(K_hat.T @ M_S @ K_hat)
    A_br = KM_inv @ K_hat.T @ M_S @ W
    d_br = d_hat + KM_inv @ K_hat.T @ M_S @ ((W - np.eye(K)) @ m_i + b - K_hat @ (A_br - H_hat) @ m_i)
    J_br_A = raw_expected_sender_loss(A_br, d_br, np.zeros((rc, rc)), H_hat, d_hat, K_hat, P, m_i, R, M_S, W, b)
    # Channel B: BFGS over (A, d, L_z)
    def obj_br(vec):
        Am = vec[:rc * K].reshape(rc, K)
        dm = vec[rc * K:rc * K + rc]
        Lm = vec[rc * K + rc:].reshape(rc, rc)
        return raw_expected_sender_loss(Am, dm, Lm @ Lm.T, H_hat, d_hat, K_hat, P, m_i, R, M_S, W, b)
    res_br = minimize(obj_br, rng.normal(size=rc * K + rc + rc * rc) * 0.2, method="BFGS", options={"gtol": 1e-10})
    assert abs(J_br_A - res_br.fun) < 1e-10, f"One-shot BR mismatch {abs(J_br_A - res_br.fun)}"
    print(f"  One-shot BR (K=3, rc=2): J_br_closed={J_br_A:.8f} vs BFGS={res_br.fun:.8f}, diff={abs(J_br_A-res_br.fun):.2e}")

    # 3b. Vector rank-deficient Nash equilibrium with nonzero b off M_S U AND nonzero Sigma_zeta in R ker(A^T)
    K, rc, r_prime = 4, 3, 2
    P = rand_spd(K)
    R = rand_spd(rc, 0.3)
    M_S = rand_spd(K)
    P_half, P_mhalf = mat_sqrt(P), mat_inv_sqrt(P)
    V1, _ = np.linalg.qr(rng.normal(size=(K, r_prime)))
    U_b = P_half @ V1  # U_b^T P^{-1} U_b = I_2
    _, _, Vt_u = np.linalg.svd(U_b.T)
    U_perp = Vt_u[r_prime:, :].T  # K x 2, U_b^T U_perp = 0
    Omega = np.array([[0.72, -0.18], [-0.18, 0.38]])  # symmetric, evals in (0,1)
    t_vals, Q_R = np.linalg.eigh(Omega)
    assert np.all((t_vals > 0) & (t_vals < 1))
    Sig_target = U_b @ Omega @ U_b.T
    # Build W so U_b^T M_S (Sig_target P^{-1} - W) = 0
    W_n = Sig_target @ np.linalg.inv(P) + np.linalg.inv(M_S) @ U_perp @ rng.normal(size=(K - r_prime, K))
    m_i = rng.normal(size=K)
    # Nonzero bias b such that M_S((I-W)m_i - b) lies in U_perp
    b_n = (np.eye(K) - W_n) @ m_i + np.linalg.inv(M_S) @ U_perp @ np.array([2.3, -1.1])
    # Construct A* with rank r_prime = 2 < rc = 3
    Q_full, _ = np.linalg.qr(rng.normal(size=(rc, rc)))
    Q_L = Q_full[:, :r_prime]
    s_vals = np.sqrt(t_vals / (1.0 - t_vals))
    A_star = mat_sqrt(R) @ Q_L @ np.diag(s_vals) @ Q_R.T @ U_b.T @ np.linalg.inv(P)
    d_star = rng.normal(size=rc)
    # Construct nonzero Sigma_zeta* in R ker(A*^T)
    _, _, Vt_a = np.linalg.svd(A_star.T)
    ker_AT = Vt_a[r_prime:, :].T  # rc x 1
    assert np.linalg.norm(A_star.T @ ker_AT) < 1e-13
    Rv = R @ ker_AT
    Sz_star = 3.5 * (Rv @ Rv.T)
    # Verify K* and Sigma_mhat are IDENTICAL with Sz=0 and Sz=Sz_star
    K_star_0 = P @ A_star.T @ np.linalg.inv(A_star @ P @ A_star.T + R)
    K_star_z = P @ A_star.T @ np.linalg.inv(A_star @ P @ A_star.T + R + Sz_star)
    assert np.linalg.norm(K_star_0 - K_star_z) < 1e-13, "Null-channel Sz changed K*"
    assert np.linalg.norm(K_star_z @ Sz_star) < 1e-13, "K* Sz* != 0"
    # Verify Nash global optimality against 500 random deviations + BFGS
    J_nash = raw_expected_sender_loss(A_star, d_star, Sz_star, A_star, d_star, K_star_z, P, m_i, R, M_S, W_n, b_n)
    def obj_dev(vec):
        Am = vec[:rc * K].reshape(rc, K)
        dm = vec[rc * K:rc * K + rc]
        Lm = vec[rc * K + rc:].reshape(rc, rc)
        return raw_expected_sender_loss(Am, dm, Lm @ Lm.T, A_star, d_star, K_star_z, P, m_i, R, M_S, W_n, b_n)
    res_dev = minimize(obj_dev, rng.normal(size=rc * K + rc + rc * rc) * 0.2, method="BFGS", options={"gtol": 1e-10})
    assert abs(J_nash - res_dev.fun) < 1e-9, f"Nash not global BR: {J_nash} vs {res_dev.fun}"
    print(f"  Rank-2 partial Nash (K=4, rc=3, b!=0, Sz*!=0): ||K*(Sz=0)-K*(Sz*)||={np.linalg.norm(K_star_0-K_star_z):.2e}, J_nash={J_nash:.8f} vs BR_min={res_dev.fun:.8f}")

    # 3c. Scalar Nash vs Stackelberg divergence at w=0.25 (0 < w < 1/2)
    P_s, R_s, w_s = 2.0, 1.0, 0.25
    A_ns = np.sqrt(w_s / (1.0 - w_s) * R_s / P_s)
    K_ns = A_ns * P_s / (A_ns**2 * P_s + R_s)
    J_ns = (K_ns * A_ns - w_s)**2 * P_s + K_ns**2 * R_s
    J_sil_s = w_s**2 * P_s
    assert abs((J_ns - J_sil_s) - w_s * (1.0 - 2.0 * w_s) * P_s) < 1e-14
    assert J_ns > J_sil_s
    print(f"  Scalar Nash vs Stackelberg (w=0.25): J_Nash={J_ns:.6f} > J_Stackelberg(silence)={J_sil_s:.6f}, diff={J_ns-J_sil_s:.6f} == w(1-2w)P")

    # Planted-error negative control for C3: break symmetry of Omega (non-symmetric rotational W in 2D)
    theta = 0.7
    W_rot = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
    # Try to satisfy K* A* = W_rot on full rank 2x2: impossible because K* A* = P^{1/2} X P^{-1/2} has real positive evals < 1!
    evals_rot = np.linalg.eigvals(W_rot)
    assert np.all(np.abs(evals_rot.imag) > 0.5), "Rotation eigenvalues must be non-real"
    # Planted wrong Sz NOT in R ker(A*^T): must strictly increase J_S^fix
    Sz_bad = 0.5 * np.eye(rc)
    J_bad_sz = raw_expected_sender_loss(A_star, d_star, Sz_bad, A_star, d_star, K_star_z, P, m_i, R, M_S, W_n, b_n)
    assert J_bad_sz - J_nash > 0.05, "Planted error C3 (bad Sz) failed"
    print(f"  [NEG-CTRL C3] Non-null Sz=0.5I strictly worsens J_fix by +{J_bad_sz - J_nash:.6f} (detected!)")

    # -----------------------------------------------------------------
    # 4. CLAIM C4: Iterated best-response phase portrait
    # -----------------------------------------------------------------
    print("\n[4] Claim C4: Scalar iterated best-response dynamics (all regimes)")
    P_d, R_d, m_d = 1.7, 0.4, 0.8
    # (i) w in (0, 1): global convergence + strict Lyapunov decrease + exact bias treadmill
    for w_d, b_d in [(0.7, (1 - 0.7) * m_d), (0.5, (1 - 0.5) * m_d), (0.2, (1 - 0.2) * m_d), (0.7, 1.5)]:
        A = 0.15
        d = 0.2
        A_st = np.sqrt(w_d / (1 - w_d) * R_d / P_d)
        K_st = A_st * P_d / (A_st**2 * P_d + R_d)
        delta_b = (w_d - 1.0) * m_d + b_d
        prev_lyap = abs(np.log(A / A_st))
        sum_invK = 0.0
        for step in range(80):
            Kn = A * P_d / (A * A * P_d + R_d)
            sum_invK += 1.0 / Kn
            A_new = w_d / Kn
            d_new = d + delta_b / Kn - (A_new - A) * m_d
            cur_lyap = abs(np.log(A_new / A_st))
            if prev_lyap > 1e-13:
                assert cur_lyap < prev_lyap, f"Lyapunov did not decrease at w={w_d}, step={step}"
            # Verify exact telescoping identity for d_n
            d_tele = 0.2 - (A_new - 0.15) * m_d + delta_b * sum_invK
            assert abs(d_new - d_tele) < 1e-10
            prev_lyap = cur_lyap
            A, d = A_new, d_new
        assert abs(A - A_st) < 1e-10
        if abs(delta_b) > 0:
            # Check constant velocity delta_b / K_st
            Kn = A * P_d / (A * A * P_d + R_d)
            vel = delta_b / Kn
            assert abs(vel - delta_b / K_st) < 1e-9
    # (ii) -1 < w < 0: 2-cycle
    w_d = -0.35
    A = 0.9
    A_sh = np.sqrt(abs(w_d) / (1 - abs(w_d)) * R_d / P_d)
    for _ in range(100):
        A = w_d * (A + R_d / (A * P_d))
    A_prev = A
    A_next = w_d * (A + R_d / (A * P_d))
    assert abs(A_prev + A_next) < 1e-11 and abs(abs(A_prev) - A_sh) < 1e-11
    # (iii) w = 1: A_n ~ sqrt(2Rn/P), d_n ~ (2/3) b sqrt(2R/P) n^{3/2}
    A, d, b_d = 0.5, 0.0, 0.6
    N_it = 2000
    for _ in range(N_it):
        Kn = A * P_d / (A * A * P_d + R_d)
        A_new = 1.0 / Kn
        d = d + b_d / Kn - (A_new - A) * m_d
        A = A_new
    A_asymp = np.sqrt(2.0 * R_d / P_d * N_it)
    d_asymp = (2.0 / 3.0) * b_d * np.sqrt(2.0 * R_d / P_d) * (N_it ** 1.5)
    assert abs(A / A_asymp - 1.0) < 0.005
    assert abs(d / d_asymp - 1.0) < 0.005
    print(f"  w in (0,1): global Lyapunov convergence + telescoping d_n verified to <1e-10")
    print(f"  w=-0.35: 2-cycle converged to +/-{abs(A_prev):.8f} vs A#={A_sh:.8f}")
    print(f"  w=1 (N={N_it}): A_N/sqrt(2RN/P)={A/A_asymp:.6f}, d_N/((2/3)b sqrt(2R/P) N^3/2)={d/d_asymp:.6f}")

    # Planted-error negative control for C4: wrong asymptotic coefficient sqrt(R/P * n) (missing factor 2)
    A_wrong_asymp = np.sqrt(R_d / P_d * N_it)
    assert abs(A / A_wrong_asymp - 1.0) > 0.35, "Planted error C4 failed"
    print(f"  [NEG-CTRL C4] Dropping factor 2 in sqrt(2Rn/P) gives ratio {A/A_wrong_asymp:.4f} (far from 1, detected!)")

    # -----------------------------------------------------------------
    # 5. CLAIM C5: No-intercept absorption breakdown & empirical-R half-sigma cap
    # -----------------------------------------------------------------
    print("\n[5] Claim C5: No-intercept absorption breakdown (known R vs empirical R)")
    # 5a. Empirical OLS simulation (Channel B) confirming prop:lrn-absorption(b) + residual second moment alpha_0 d d^T + R + Sz
    K, rc = 2, 2
    C_phi = rand_spd(K, 0.9)
    m_bar = np.array([0.8, -0.5])
    M2 = C_phi + np.outer(m_bar, m_bar)
    M2_inv = np.linalg.inv(M2)
    alpha0 = float(1.0 - m_bar @ M2_inv @ m_bar)
    alpha0_sm = float(1.0 / (1.0 + m_bar @ np.linalg.inv(C_phi) @ m_bar))
    assert abs(alpha0 - alpha0_sm) < 1e-15
    A_e = rng.normal(size=(rc, K))
    d_e = np.array([1.2, -0.9])
    R_e = rand_spd(rc, 0.3)
    Sz_e = rand_spd(rc, 0.15)
    T_sim = 80000
    phi_sim = rng.multivariate_normal(m_bar, C_phi, size=T_sim)
    eps_sim = rng.multivariate_normal(np.zeros(rc), R_e + Sz_e, size=T_sim)
    y_sim = phi_sim @ A_e.T + d_e + eps_sim
    # No-intercept OLS: H_hat = (Y^T Phi)(Phi^T Phi)^{-1}
    H_ols = (y_sim.T @ phi_sim) @ np.linalg.inv(phi_sim.T @ phi_sim)
    H_th = A_e + np.outer(d_e, m_bar @ M2_inv)
    res_sim = y_sim - phi_sim @ H_ols.T
    R_ols = (res_sim.T @ res_sim) / T_sim
    R_th = R_e + Sz_e + alpha0 * np.outer(d_e, d_e)
    mean_res_ols = np.mean(res_sim, axis=0)
    mean_res_th = alpha0 * d_e
    assert np.linalg.norm(H_ols - H_th) < 0.02
    assert np.linalg.norm(R_ols - R_th) < 0.03
    assert np.linalg.norm(mean_res_ols - mean_res_th) < 0.02
    print(f"  No-intercept OLS (T={T_sim}): ||H_ols-H_th||={np.linalg.norm(H_ols-H_th):.4f}, ||R_ols-R_th||={np.linalg.norm(R_ols-R_th):.4f}, ||mean_res-alpha0*d||={np.linalg.norm(mean_res_ols-mean_res_th):.4f}")

    # 5b. Scalar no-intercept Nash with known R at m_bar = m_i = 0, b != 0
    P_s, R_s, w_s, b_s = 2.0, 1.0, 0.4, 1.2  # b^2 = 1.44 > w P = 0.8 -> receiver worse than silence!
    A_ni = np.sqrt(w_s / (1.0 - w_s) * R_s / P_s)
    d_ni = b_s * A_ni / w_s
    K_ni = A_ni * P_s / (A_ni**2 * P_s + R_s)
    # Check Nash optimality for sender
    assert abs(K_ni * d_ni - b_s) < 1e-14
    assert abs(K_ni * A_ni - w_s) < 1e-14
    # Receiver risk vs silence risk P_s
    rec_mse = (K_ni * A_ni - 1.0)**2 * P_s + K_ni**2 * R_s + (K_ni * d_ni)**2
    rec_mse_th = (1.0 - w_s) * P_s + b_s**2
    assert abs(rec_mse - rec_mse_th) < 1e-14 and rec_mse > P_s
    print(f"  No-intercept known-R Nash (w=0.4, b=1.2, P=2): receiver MSE={rec_mse:.4f} > silence risk P={P_s:.4f} (b^2={b_s**2:.2f} > wP={w_s*P_s:.2f})")

    # 5c. Universal empirical-R half-sigma cap + sharpness across 1000 random trials
    max_cap_ratio = 0.0
    for _ in range(1000):
        Kk = int(rng.integers(1, 5))
        rck = int(rng.integers(1, 5))
        Pk = rand_spd(Kk)
        Cpk = rand_spd(Kk)
        mbk = rng.normal(size=Kk)
        mik = rng.normal(size=Kk)
        M2k = Cpk + np.outer(mbk, mbk)
        M2kinv = np.linalg.inv(M2k)
        a0k = float(1.0 - mbk @ M2kinv @ mbk)
        bik = float(1.0 - mbk @ M2kinv @ mik)
        Rk = rand_spd(rck, 0.1)
        Szk = rand_spd(rck, 0.05)
        sc = 10.0 ** rng.uniform(-1, 3)
        Ak = rng.normal(size=(rck, Kk)) * sc
        dk = rng.normal(size=rck) * sc
        Hnik = Ak + np.outer(dk, mbk @ M2kinv)
        Rnik = Rk + Szk + a0k * np.outer(dk, dk)
        Knik = Pk @ Hnik.T @ np.linalg.inv(Hnik @ Pk @ Hnik.T + Rnik)
        bias_k = bik * (Knik @ dk)
        pnorm = float(np.sqrt(bias_k @ np.linalg.inv(Pk) @ bias_k))
        cap = abs(bik) / (2.0 * np.sqrt(a0k))
        if cap > 1e-12:
            max_cap_ratio = max(max_cap_ratio, pnorm / cap)
    assert max_cap_ratio < 1.0, f"Cap violated: {max_cap_ratio}"
    # Sharpness check
    P_sh = rand_spd(3)
    C_sh = rand_spd(3)
    mb_sh = np.array([0.4, -0.3, 0.2])
    mi_sh = mb_sh.copy()
    M2_sh = C_sh + np.outer(mb_sh, mb_sh)
    a0_sh = float(1.0 - mb_sh @ np.linalg.inv(M2_sh) @ mb_sh)
    R_sh = rand_spd(2, 0.2)
    Pm_sh = mat_inv_sqrt(P_sh)
    u_sh = np.array([0.6, 0.8])
    v_sh = np.array([1.0, 0.0, 0.0])
    a_big = 2000.0
    H_big = a_big * np.outer(u_sh, v_sh) @ Pm_sh
    d_big = (a_big / np.sqrt(a0_sh)) * u_sh
    K_big = P_sh @ H_big.T @ np.linalg.inv(H_big @ P_sh @ H_big.T + R_sh + a0_sh * np.outer(d_big, d_big))
    pnorm_big = float(np.sqrt((a0_sh * K_big @ d_big) @ np.linalg.inv(P_sh) @ (a0_sh * K_big @ d_big)))
    cap_sh = np.sqrt(a0_sh) / 2.0
    assert pnorm_big < cap_sh and pnorm_big / cap_sh > 0.99999
    print(f"  Universal empirical-R cap: max ratio over 1000 random trials = {max_cap_ratio:.8f} (< 1); sharpness at a=2000: {pnorm_big/cap_sh:.10f}")

    # Planted-error negative control for C5: replace cap |beta_i|/(2 sqrt(alpha0)) by |beta_i|/(3 sqrt(alpha0))
    assert pnorm_big > (np.sqrt(a0_sh) / 3.0), "Planted error C5 failed"
    print(f"  [NEG-CTRL C5] Tightening cap constant 1/2 -> 1/3 is violated by sharpness witness ({pnorm_big:.6f} > {np.sqrt(a0_sh)/3.0:.6f}, detected!)")

    # -----------------------------------------------------------------
    # 6. CLAIM C6: Detection reference, KL divergence, & stealthy tradeoff
    # -----------------------------------------------------------------
    print("\n[6] Claim C6: Identifiability, exact KL formula, & stealthy jamming/attenuation tradeoff")
    # 6a. Exact KL formula (Channel A) vs joint Gaussian KL on (phi, y) (Channel B) across non-symmetric instances & singular C_phi
    max_kl_err = 0.0
    for (K, rc) in [(1, 1), (3, 2), (2, 3), (4, 4)]:
        H = rng.normal(size=(rc, K))
        D = rng.normal(size=(rc, K)) * 0.5
        d = rng.normal(size=rc) * 0.4
        R = rand_spd(rc, 0.5)
        Sz = rand_spd(rc, 0.25)
        C_phi = rand_spd(K, 0.7)
        m_bar = rng.normal(size=K)
        R_inv = np.linalg.inv(R)
        kl_A = 0.5 * (
            float(np.trace(R_inv @ D @ C_phi @ D.T))
            + float((D @ m_bar + d) @ R_inv @ (D @ m_bar + d))
            + float(np.trace(R_inv @ Sz))
            - float(np.linalg.slogdet(np.eye(rc) + R_inv @ Sz)[1])
        )
        mu1 = np.concatenate([m_bar, (H + D) @ m_bar + d])
        mu0 = np.concatenate([m_bar, H @ m_bar])
        S1 = np.block([[C_phi, C_phi @ (H + D).T], [(H + D) @ C_phi, (H + D) @ C_phi @ (H + D).T + R + Sz]])
        S0 = np.block([[C_phi, C_phi @ H.T], [H @ C_phi, H @ C_phi @ H.T + R]])
        S0_inv = np.linalg.inv(S0)
        kl_B = 0.5 * (
            float(np.trace(S0_inv @ S1))
            - (K + rc)
            - float(np.linalg.slogdet(S1)[1] - np.linalg.slogdet(S0)[1])
            + float((mu1 - mu0) @ S0_inv @ (mu1 - mu0))
        )
        max_kl_err = max(max_kl_err, abs(kl_A - kl_B))
        assert abs(kl_A - kl_B) < 1e-12
    # Check rank-deficient C_phi: deviation D supported on ker(M_2) gives KL = 0 identically!
    K, rc = 3, 2
    v1 = np.array([1.0, 0.0, 0.0])
    v2 = np.array([0.0, 1.0, 0.0])
    C_sing = np.outer(v1, v1)  # rank 1
    m_bar_s = v2               # orthogonal to col(C_sing)
    # ker(M_2) = span(e_3)
    D_invis = np.array([[0.0, 0.0, 5.0], [0.0, 0.0, -3.0]])
    R_s2 = rand_spd(rc, 0.4)
    kl_invis = 0.5 * (
        float(np.trace(np.linalg.inv(R_s2) @ D_invis @ C_sing @ D_invis.T))
        + float((D_invis @ m_bar_s) @ np.linalg.inv(R_s2) @ (D_invis @ m_bar_s))
    )
    assert kl_invis == 0.0, "D on ker(M_2) must have KL = 0"
    # Check confounding on span((I-P_C) m_bar): D_conf @ m_bar + d_conf = 0 with D_conf != 0, d_conf != 0 gives KL = 0!
    D_conf = np.array([[0.0, 2.0, 0.0], [0.0, -1.5, 0.0]])
    d_conf = -(D_conf @ m_bar_s)
    kl_conf = 0.5 * (
        float(np.trace(np.linalg.inv(R_s2) @ D_conf @ C_sing @ D_conf.T))
        + float((D_conf @ m_bar_s + d_conf) @ np.linalg.inv(R_s2) @ (D_conf @ m_bar_s + d_conf))
    )
    assert kl_conf == 0.0, "Confounded (D, d) off col(C_phi) must have KL = 0"

    # 6b. Stealthy jamming vs attenuation tradeoff at w < 1/2 (small delta) & exact amplification at w > 1/2 (all delta)
    H_s, P_s, R_s = 1.5, 2.0, 0.5
    snr0 = H_s**2 * P_s / R_s  # = 9.0
    # Case w < 1/2:
    w_low = 0.1
    sig_hon = H_s**2 * P_s**2 / (H_s**2 * P_s + R_s)
    delta_sm = 1e-7
    def obj_kl_low(x):
        Dv, szv = x
        Av = H_s + Dv
        return (1.0 - 2.0 * w_low) * (Av**2 * P_s**2) / (Av**2 * P_s + R_s + szv)
    def con_kl_low(x):
        Dv, szv = x
        return delta_sm - 0.5 * (Dv**2 * P_s / R_s + szv / R_s - np.log(1.0 + szv / R_s))
    res_low = minimize(
        obj_kl_low,
        [-np.sqrt(delta_sm * R_s / P_s), R_s * np.sqrt(delta_sm)],
        bounds=[(-5.0, 5.0), (0.0, 50.0)],
        constraints={"type": "ineq", "fun": con_kl_low},
        method="SLSQP",
        options={"ftol": 1e-15, "maxiter": 500},
    )
    assert res_low.success
    D_opt, sz_opt = res_low.x
    red_num = (1.0 - 2.0 * w_low) * sig_hon - res_low.fun
    red_th = (1.0 - 2.0 * w_low) * 2.0 * P_s * np.sqrt(snr0 * (2.0 + snr0)) / ((1.0 + snr0)**2) * np.sqrt(delta_sm)
    rel_ratio = (sz_opt / R_s) / (-D_opt / abs(H_s))
    kl_D = 0.5 * D_opt**2 * P_s / R_s
    kl_sz = 0.5 * (sz_opt / R_s - np.log(1.0 + sz_opt / R_s))
    kl_share_ratio = kl_sz / kl_D
    assert abs(red_num / red_th - 1.0) < 1e-3
    assert abs(rel_ratio - snr0) / snr0 < 5e-3
    assert abs(kl_share_ratio - snr0 / 2.0) / (snr0 / 2.0) < 1e-2

    # Case w > 1/2 (exact for finite delta = 0.5!):
    w_hi = 0.8
    delta_fin = 0.5
    D_hi_exact = np.sign(H_s) * np.sqrt(2.0 * R_s * delta_fin / P_s)
    A_hi_exact = H_s + D_hi_exact
    J_hi_exact = (1.0 - 2.0 * w_hi) * (A_hi_exact**2 * P_s**2) / (A_hi_exact**2 * P_s + R_s)
    def obj_kl_hi(x):
        Dv, szv = x
        Av = H_s + Dv
        return (1.0 - 2.0 * w_hi) * (Av**2 * P_s**2) / (Av**2 * P_s + R_s + szv)
    def con_kl_hi(x):
        Dv, szv = x
        return delta_fin - 0.5 * (Dv**2 * P_s / R_s + szv / R_s - np.log(1.0 + szv / R_s))
    res_hi = minimize(
        obj_kl_hi, [0.1, 0.1], bounds=[(-5.0, 5.0), (0.0, 50.0)],
        constraints={"type": "ineq", "fun": con_kl_hi},
        method="SLSQP", options={"ftol": 1e-14},
    )
    assert res_hi.success and abs(res_hi.fun - J_hi_exact) < 1e-11 and abs(res_hi.x[0] - D_hi_exact) < 1e-6 and res_hi.x[1] < 1e-6

    print(f"  Max KL residual (closed form vs joint Gaussian, 4 dims): {max_kl_err:.3e}")
    print(f"  Singular C_phi: ker(M_2) invisible KL={kl_invis:.1f}, confounded (D,d) KL={kl_conf:.1f}")
    print(f"  Stealthy tradeoff (w=0.1, snr0=9, delta=1e-7): red_num/red_th={red_num/red_th:.6f}, rel_ratio={rel_ratio:.4f} (vs {snr0:.1f}), kl_share={kl_share_ratio:.4f} (vs {snr0/2:.1f})")
    print(f"  Exact KL-constrained amplification (w=0.8, delta=0.5): D_opt={res_hi.x[0]:.8f} vs exact {D_hi_exact:.8f}, Sz_opt={res_hi.x[1]:.2e}")

    # Planted-error negative control for C6: drop log-det term in KL formula -> differs from joint Gaussian KL!
    kl_wrong_A = kl_A + 0.5 * float(np.linalg.slogdet(np.eye(Sz.shape[0]) + R_inv @ Sz)[1])
    assert abs(kl_wrong_A - kl_B) > 0.1, "Planted error C6 failed"
    print(f"  [NEG-CTRL C6] Dropping -ln det(I + R^-1 Sz) shifts KL by +{abs(kl_wrong_A - kl_B):.6f} (detected!)")

    print("\n=================================================================")
    print("ALL CHECKS AND PLANTED-ERROR NEGATIVE CONTROLS PASSED (EXIT 0).")
    print("=================================================================")


if __name__ == "__main__":
    main()
