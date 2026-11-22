"""Verification suite for open:mis-dynamic-ratio (Dynamic ratios).

Two independent channels for every load-bearing claim:
  Channel 1 (Symbolic): Exact algebraic identities, factorizations, positivity proofs,
    correlation duality, and asymptotic expansions in SymPy.
  Channel 2 (Brute-force trajectory): Direct finite-horizon covariance recursion of the
    joint linear-Gaussian Kalman filtering process (eta_t, m_i(t), m_j(t)) (or
    (eta_t, e_i(t), e_j(t)) for |F| >= 1 to avoid cancellation) from t = 0 to t = T,
    computing I(eta_T; y_ij(T) | m_i(T)) directly from the 3K x 3K joint covariance
    without passing through the closed-form formulas.

Includes planted-error negative controls that must fail loudly and are caught and reported.
All side conditions (positive definiteness, detectability, stability) are asserted explicitly.
"""
from __future__ import annotations

import math
import numpy as np
import sympy as sp
from scipy.linalg import solve_discrete_are, solve_discrete_lyapunov


def steady_state_kf_scalar(F: float, Q: float, Rs: float):
    assert Q > 0 and Rs > 0
    b = Rs * (1.0 - F**2) - Q
    D = math.sqrt(b**2 + 4.0 * Q * Rs)
    Pm = 0.5 * (-b + D)
    ks = Pm / (Pm + Rs)
    a = 1.0 - ks
    Pp = a * Pm
    assert a * F**2 < 1.0 - 1e-15, f"Unstable filter factor a*F^2={a*F**2}"
    return Pm, ks, a, Pp, D


def closed_form_scalar(F: float, Q: float, Rsi: float, Rsj: float, g: float, Rc: float):
    assert Q > 0 and Rsi > 0 and Rsj > 0 and g != 0 and Rc >= 0
    _, ki, ai, Sii, _ = steady_state_kf_scalar(F, Q, Rsi)
    _, kj, aj, Sjj, _ = steady_state_kf_scalar(F, Q, Rsj)
    Sij = (ai * aj * Q) / (1.0 - ai * aj * F**2)
    rho = Sij / math.sqrt(Sii * Sjj)

    V1 = 0.5 * math.log1p((g**2 * Sii) / (g**2 * Sjj + Rc))
    V0 = math.inf if Rc == 0.0 else 0.5 * math.log1p((g**2 * Sii) / Rc)

    sig = Q * ai * (1.0 - aj)**2 / ((1.0 - ai * F**2) * (1.0 - ai * aj * F**2)**2)
    if abs(F) < 1.0:
        Rex0 = (
            Q * aj * (1.0 - aj)
            * (1.0 - 2.0 * ai * aj * F**2 + ai * aj * (ai + aj - 1.0) * F**4)
            / ((1.0 - aj * F**2)**2 * (1.0 - ai * aj * F**2)**2)
        )
    else:
        Rex0 = (
            Q * aj * (1.0 - ai * aj - ai * aj * (2.0 - ai - aj) * F**2)
            / ((1.0 - aj * F**2) * (1.0 - ai * aj * F**2)**2)
        )
    assert Rex0 > 0.0, f"Nonpositive Rex0={Rex0}"
    Vex = 0.5 * math.log1p((g**2 * sig) / (g**2 * Rex0 + Rc))

    K1 = (Sii * g) / (g**2 * (Sii + Sjj) + Rc)
    P_l1_cl = (1.0 - K1 * g) * Sii
    P_l1_act = P_l1_cl * (1.0 + (2.0 * g**2 * Sij) / (g**2 * (Sii + Sjj) + Rc))
    P_ex = Sii * math.exp(-2.0 * Vex)

    return dict(
        Sii=Sii, Sjj=Sjj, Sij=Sij, rho=rho, ki=ki, kj=kj, ai=ai, aj=aj,
        V0=V0, V1=V1, Vex=Vex, ratio_V1=V1 / Vex,
        P_l1_cl=P_l1_cl, P_l1_act=P_l1_act, P_ex=P_ex,
        ratio_P_act_cl=P_l1_act / P_l1_cl,
        ratio_P_ex_cl=P_ex / P_l1_cl,
        ratio_P_act_ex=P_l1_act / P_ex,
    )


def brute_force_scalar_error_basis(F: float, Q: float, Rsi: float, Rsj: float, g: float, Rc: float, T: int):
    """Exact finite-horizon KF recursion tracked in the [eta, e_i, e_j] basis.

    Tracking errors e_k = m_k - eta avoids catastrophic cancellation when |F| >= 1
    and Var(eta_T) grows large.
    """
    P_init = Q / (1.0 - F**2) if abs(F) < 1.0 else 1.0
    # State vector z_t = [eta_t, e_i(t), e_j(t)], where e_k = m_k - eta.
    # Before t=0 measurement: m_k(-1)=0 so e_k^- = -eta_0.
    C = np.array([
        [P_init, -P_init, -P_init],
        [-P_init, P_init, P_init],
        [-P_init, P_init, P_init],
    ], dtype=float)
    Pmi = P_init
    Pmj = P_init
    for t in range(T + 1):
        if t > 0:
            # eta_t = F eta_{t-1} + w, e_k^- = F e_k(t-1) - w
            A = np.diag([F, F, F])
            w_vec = np.array([1.0, -1.0, -1.0])
            C = A @ C @ A.T + Q * np.outer(w_vec, w_vec)
            Pmi = F**2 * Ppi + Q
            Pmj = F**2 * Ppj + Q
        ki = Pmi / (Pmi + Rsi)
        kj = Pmj / (Pmj + Rsj)
        Ppi = (1.0 - ki) * Pmi
        Ppj = (1.0 - kj) * Pmj
        # e_k(t) = (1 - k_k) e_k^- + k_k v_k
        M = np.diag([1.0, 1.0 - ki, 1.0 - kj])
        Qv = np.diag([0.0, ki**2 * Rsi, kj**2 * Rsj])
        C = M @ C @ M.T + Qv

    # Compute conditional covariance of (eta, y = g*(eta + e_j) + nu) given m_i = eta + e_i
    # using exact Schur complement in terms of P_eta = C[0,0], Sii = C[1,1], Sjj = C[2,2], Sij = C[1,2],
    # and checking orthogonality Cov(eta, e_k) = -S_kk directly from C!
    assert abs(C[0, 1] + C[1, 1]) < 1e-11 * max(1.0, C[0, 0]), f"Orthogonality failed: {C[0,1]} vs {-C[1,1]}"
    assert abs(C[0, 2] + C[2, 2]) < 1e-11 * max(1.0, C[0, 0]), f"Orthogonality failed: {C[0,2]} vs {-C[2,2]}"
    P_eta = C[0, 0]
    Sii = C[1, 1]
    Sjj = C[2, 2]
    Sij = C[1, 2]
    # Direct transformation to [eta, m_i, y] when P_eta < 1e8, or algebraically exact Schur when P_eta >= 1e8
    if P_eta < 1e8:
        T_mat = np.array([
            [1.0, 0.0, 0.0],
            [1.0, 1.0, 0.0],
            [g, 0.0, g],
        ])
        Cy = T_mat @ C @ T_mat.T
        Cy[2, 2] += Rc
        idx = [0, 2]
        Cc = Cy[np.ix_(idx, idx)] - np.outer(Cy[idx, 1], Cy[idx, 1]) / Cy[1, 1]
        V_bf = 0.5 * math.log((Cc[0, 0] * Cc[1, 1]) / (Cc[0, 0] * Cc[1, 1] - Cc[0, 1]**2))
    else:
        # Exact identity without subtracting O(P_eta) from O(P_eta):
        # Var(m_i) = P_eta + 2*C[0,1] + Sii = P_eta - Sii (exact from C)
        Mi = P_eta + 2.0 * C[0, 1] + Sii
        cov_eta_mj_cond = -(C[0, 1] + Sij) - (C[0, 1] + Sii) * (Sjj - Sij) / Mi  # exact from C
        # Compute directly from C entries (still independent of closed-form formula for Sii, Sjj, Sij)
        Str = g**2 * (Sii + Sjj - 2.0 * Sij) + Rc
        Rtr = g**2 * (Sjj - Sij**2 / Sii) + Rc
        Dpr = g**2 * (Sjj - Sij)**2 / Mi
        V_bf = 0.5 * math.log((Str - Dpr) / (Rtr - Dpr))

    # Direct level-1 actual MSE from error covariance block C[1:, 1:]
    K1 = (Sii * g) / (g**2 * (Sii + Sjj) + Rc)
    w = np.array([1.0 - K1 * g, K1 * g])
    P_l1_act_bf = float(w @ C[1:, 1:] @ w + K1**2 * Rc)
    return V_bf, P_l1_act_bf, Sii, Sjj, Sij


def vector_closed_form(F, Q, Hsi, Hsj, Rsi, Rsj, Hj, Rc):
    K = F.shape[0]
    assert np.max(np.abs(np.linalg.eigvals(F))) < 1.0, "F must be Schur stable"
    assert np.min(np.linalg.eigvalsh(Q)) > 0.0, "Q must be positive definite"
    assert np.min(np.linalg.eigvalsh(Rsi)) > 0.0 and np.min(np.linalg.eigvalsh(Rsj)) > 0.0
    Pmi = solve_discrete_are(F.T, Hsi.T, Q, Rsi)
    Pmj = solve_discrete_are(F.T, Hsj.T, Q, Rsj)
    Ki = Pmi @ Hsi.T @ np.linalg.inv(Hsi @ Pmi @ Hsi.T + Rsi)
    Kj = Pmj @ Hsj.T @ np.linalg.inv(Hsj @ Pmj @ Hsj.T + Rsj)
    Ai = np.eye(K) - Ki @ Hsi
    Aj = np.eye(K) - Kj @ Hsj
    assert np.max(np.abs(np.linalg.eigvals(Ai @ F))) < 1.0
    assert np.max(np.abs(np.linalg.eigvals(Aj @ F))) < 1.0
    Sii = Ai @ Pmi
    Sjj = Aj @ Pmj
    Sii = 0.5 * (Sii + Sii.T)
    Sjj = 0.5 * (Sjj + Sjj.T)
    P0 = solve_discrete_lyapunov(F, Q)
    P0 = 0.5 * (P0 + P0.T)
    M_kron = np.eye(K * K) - np.kron(Aj @ F, Ai @ F)
    Sij = np.linalg.solve(M_kron, (Ai @ Q @ Aj.T).ravel(order="F")).reshape((K, K), order="F")
    Sji = Sij.T

    Mi = P0 - Sii
    assert np.min(np.linalg.eigvalsh(Mi)) > 1e-12, "P0 - Sii must be positive definite"
    Dpr = (Sjj - Sji) @ np.linalg.solve(Mi, Sjj - Sij)
    Sex = Hj @ (Sii + Sjj - Sij - Sji - Dpr) @ Hj.T + Rc
    Rex = Hj @ (Sjj - Sji @ np.linalg.solve(Sii, Sij) - Dpr) @ Hj.T + Rc
    assert np.min(np.linalg.eigvalsh(Rex)) > 1e-13, "R^exact must be positive definite"

    r = Hj.shape[0]
    _, ldS = np.linalg.slogdet(Sex)
    _, ldR = np.linalg.slogdet(Rex)
    Vex = 0.5 * (ldS - ldR)

    S1 = Hj @ Sjj @ Hj.T + Rc
    _, ldV1 = np.linalg.slogdet(np.eye(r) + np.linalg.solve(S1, Hj @ Sii @ Hj.T))
    V1 = 0.5 * ldV1
    if np.min(np.linalg.eigvalsh(Rc)) > 0.0:
        _, ldV0 = np.linalg.slogdet(np.eye(r) + np.linalg.solve(Rc, Hj @ Sii @ Hj.T))
        V0 = 0.5 * ldV0
    else:
        V0 = math.inf
    return dict(V0=V0, V1=V1, Vex=Vex, Sii=Sii, Sjj=Sjj, Sij=Sij, P0=P0, Sex=Sex, Rex=Rex)


def vector_brute_force(F, Q, Hsi, Hsj, Rsi, Rsj, Hj, Rc, T=250):
    K = F.shape[0]
    r = Hj.shape[0]
    P0 = solve_discrete_lyapunov(F, Q)
    C = np.zeros((3 * K, 3 * K))
    C[:K, :K] = P0
    Pmi = P0.copy()
    Pmj = P0.copy()
    for t in range(T):
        if t > 0:
            A_big = np.kron(np.eye(3), F)
            Qw = np.zeros((3 * K, 3 * K))
            Qw[:K, :K] = Q
            C = A_big @ C @ A_big.T + Qw
            Pmi = F @ Ppi @ F.T + Q
            Pmj = F @ Ppj @ F.T + Q
        Ki = Pmi @ Hsi.T @ np.linalg.inv(Hsi @ Pmi @ Hsi.T + Rsi)
        Kj = Pmj @ Hsj.T @ np.linalg.inv(Hsj @ Pmj @ Hsj.T + Rsj)
        Ppi = (np.eye(K) - Ki @ Hsi) @ Pmi
        Ppj = (np.eye(K) - Kj @ Hsj) @ Pmj
        M = np.zeros((3 * K, 3 * K))
        M[:K, :K] = np.eye(K)
        M[K:2 * K, :K] = Ki @ Hsi
        M[K:2 * K, K:2 * K] = np.eye(K) - Ki @ Hsi
        M[2 * K:, :K] = Kj @ Hsj
        M[2 * K:, 2 * K:] = np.eye(K) - Kj @ Hsj
        Qv = np.zeros((3 * K, 3 * K))
        Qv[K:2 * K, K:2 * K] = Ki @ Rsi @ Ki.T
        Qv[2 * K:, 2 * K:] = Kj @ Rsj @ Kj.T
        C = M @ C @ M.T + Qv

    G = np.zeros((2 * K + r, 3 * K))
    G[:K, :K] = np.eye(K)
    G[K:2 * K, K:2 * K] = np.eye(K)
    G[2 * K:, 2 * K:] = Hj
    Cy = G @ C @ G.T
    Cy[2 * K:, 2 * K:] += Rc
    idx_ey = list(range(0, K)) + list(range(2 * K, 2 * K + r))
    idx_m = list(range(K, 2 * K))
    C_ey_m = Cy[np.ix_(idx_ey, idx_ey)] - Cy[np.ix_(idx_ey, idx_m)] @ np.linalg.solve(
        Cy[np.ix_(idx_m, idx_m)], Cy[np.ix_(idx_m, idx_ey)]
    )
    _, ld_j = np.linalg.slogdet(C_ey_m)
    _, ld_e = np.linalg.slogdet(C_ey_m[:K, :K])
    _, ld_y = np.linalg.slogdet(C_ey_m[K:, K:])
    return 0.5 * (ld_e + ld_y - ld_j)


def run_symbolic_channel():
    print("=================================================================")
    print("CHANNEL 1: SYMBOLIC IDENTITIES & PROOFS (SYMPY)")
    print("=================================================================")
    ai, aj, a, F2, Q, Rs, Rc, g = sp.symbols("a_i a_j a F2 Q R_s R_c g", positive=True)
    rhoc = sp.Symbol("varrho_c", nonnegative=True)

    # 1. Exact asymmetric scalar factorizations (|F| < 1)
    P0 = Q / (1 - F2)
    Sii = ai * Q / (1 - ai * F2)
    Sjj = aj * Q / (1 - aj * F2)
    Sij = ai * aj * Q / (1 - ai * aj * F2)
    sig = sp.simplify((Sii - Sij)**2 / Sii)
    Rex0 = sp.simplify(Sjj - Sij**2 / Sii - (Sjj - Sij)**2 / (P0 - Sii))
    Rtr0 = sp.simplify(Sjj - Sij**2 / Sii)

    sig_target = Q * ai * (1 - aj)**2 / ((1 - ai * F2) * (1 - ai * aj * F2)**2)
    Rex0_target = (
        Q * aj * (1 - aj) * (1 - 2 * ai * aj * F2 + ai * aj * (ai + aj - 1) * F2**2)
        / ((1 - aj * F2)**2 * (1 - ai * aj * F2)**2)
    )
    Rtr0_target = (
        Q * aj * (1 - ai * aj - ai * aj * (2 - ai - aj) * F2)
        / ((1 - aj * F2) * (1 - ai * aj * F2)**2)
    )
    assert sp.simplify(sig - sig_target) == 0
    assert sp.simplify(Rex0 - Rex0_target) == 0
    assert sp.simplify(Rtr0 - Rtr0_target) == 0
    print("[PASS] Asymmetric scalar closed forms for sig_ij, R_ex0 (|F|<1), R_tr0 (|F|>=1) exact.")

    # 2. Strict overvaluation (no inversion) for ALL asymmetric scalar worlds
    c_Rc = sp.simplify(Sii - sig)
    c_Rc_target = Q * ai * aj * ((1 - aj) + (1 - ai * aj * F2)) / (1 - ai * aj * F2)**2
    c_g2_stat = sp.simplify(Sii * Rex0 - sig * Sjj)
    c_g2_stat_target = (
        Q**2 * ai * aj**2 * (1 - aj) * ((1 - ai * F2) + F2 * (1 - aj))
        / ((1 - aj * F2)**2 * (1 - ai * aj * F2)**2)
    )
    c_g2_tr = sp.simplify(Sii * Rtr0 - sig * Sjj)
    c_g2_tr_target = Q**2 * ai * aj**2 * (2 - ai - aj) / ((1 - aj * F2) * (1 - ai * aj * F2)**2)
    assert sp.simplify(c_Rc - c_Rc_target) == 0
    assert sp.simplify(c_g2_stat - c_g2_stat_target) == 0
    assert sp.simplify(c_g2_tr - c_g2_tr_target) == 0
    print("[PASS] Strict non-inversion identities (SNR^1 - SNR* > 0) exact for both |F|<1 and |F|>=1.")

    # 3. Symmetric scalar exact closed forms
    rho = a * (1 - a * F2) / (1 - a**2 * F2)
    assert sp.simplify((1 - rho) - (1 - a) / (1 - a**2 * F2)) == 0
    assert sp.simplify(sig.subs({ai: a, aj: a}) / Sii.subs(ai, a) - (1 - rho)**2) == 0
    assert sp.simplify(
        Rex0.subs({ai: a, aj: a}) / Sii.subs(ai, a) - (1 - rho) * (1 + a * F2 * (1 - rho))
    ) == 0
    assert sp.simplify(Rtr0.subs({ai: a, aj: a}) / Sii.subs(ai, a) - (1 - rho**2)) == 0
    print("[PASS] Symmetric scalar formulas for 1-rho, signal/S, R_ex0/S, R_tr0/S exact.")

    # 4. Riccati closed form for rho, duality at fixed P0, and crossover
    delta = sp.Symbol("delta", real=True)  # 1 - F^2 (any real!)
    lam = sp.Symbol("lam", positive=True)  # Q / R^s
    Du = sp.sqrt((delta - lam)**2 + 4 * lam)
    u = (-(delta - lam) + Du) / 2
    a_ric = 1 / (1 + u)
    rho_ric = a_ric * (1 - a_ric * (1 - delta)) / (1 - a_ric**2 * (1 - delta))
    rho_closed = sp.Rational(1, 2) * (1 + (delta - lam) / Du)
    assert sp.simplify(rho_ric - rho_closed) == 0
    assert sp.simplify((1 - rho_closed) - u / Du) == 0
    # Derivative w.r.t. lam:
    drho_dlam = sp.simplify(sp.diff(rho_closed, lam))
    drho_dlam_target = -(delta + lam) / Du**3
    assert sp.simplify(drho_dlam - drho_dlam_target) == 0
    # Duality at fixed P0 = gamma_0 * R^s (delta > 0, lam = delta * gamma_0):
    g0 = sp.Symbol("gamma_0", positive=True)
    dpos = sp.Symbol("delta_pos", positive=True)
    rho_p0 = sp.simplify(rho_closed.subs({delta: dpos, lam: dpos * g0}))
    rho_p0_target = sp.Rational(1, 2) * (1 + (1 - g0) * sp.sqrt(dpos) / sp.sqrt(dpos * (1 - g0)**2 + 4 * g0))
    assert sp.simplify(rho_p0 - rho_p0_target) == 0
    assert sp.simplify(rho_p0 + rho_p0.subs(g0, 1 / g0) - 1) == 0
    assert sp.simplify(rho_p0.subs(g0, 1) - sp.Rational(1, 2)) == 0
    print("[PASS] Exact Riccati formula for rho, 1-rho = u/D_u, d(rho)/d(lam) = -(delta+lam)/D_u^3, and P0-duality exact.")

    # 5. Amplification vs damping thresholds at fixed (Q, Rs, Rc=0)
    snr_at_0 = lam / (lam + 1)
    # At F=1 (delta=0): rho = (1/2)*(1 - sqrt(lam)/sqrt(lam+4)), SNR*(1) = (1-rho)/(1+rho)
    rho_at_1 = sp.Rational(1, 2) * (1 - sp.sqrt(lam) / sp.sqrt(lam + 4))
    snr_at_1 = sp.simplify((1 - rho_at_1) / (1 + rho_at_1))
    lam_cross = 1 + sp.sqrt(2) / 2
    assert sp.simplify((snr_at_1 - snr_at_0).subs(lam, lam_cross)) == 0
    # Local slope at F=0 (delta=1):
    # SNR*(F) = (1 - rho) / (1 + a*F^2*(1-rho)), evaluate d/d(F^2) at F^2=0 (i.e. -d/ddelta at delta=1)
    snr_sym_0 = (1 - rho_closed) / (1 + a_ric * (1 - delta) * (1 - rho_closed))
    d_snr_dF2_0 = (-sp.diff(snr_sym_0, delta).subs(delta, 1)).subs(4 * lam + (1 - lam)**2, (lam + 1)**2)
    assert sp.simplify(d_snr_dF2_0 - lam * (2 - lam) / (lam + 1)**3) == 0
    print("[PASS] Amplification/damping thresholds exact: lambda_cross = 1 + 1/sqrt(2), local slope at F=0 = lam*(2-lam)/(lam+1)^3.")

    # 6. Level-1 overconfidence variance ratio identity
    S1, S2, S12 = sp.symbols("S_ii S_jj S_ij", positive=True)
    K1 = S1 * g / (g**2 * (S1 + S2) + Rc)
    P_cl = (1 - K1 * g) * S1
    P_act = (1 - K1 * g)**2 * S1 + (K1 * g)**2 * S2 + 2 * (1 - K1 * g) * (K1 * g) * S12 + K1**2 * Rc
    assert sp.simplify(P_act / P_cl - (1 + 2 * g**2 * S12 / (g**2 * (S1 + S2) + Rc))) == 0
    print("[PASS] Level-1 variance ratio P_act/P_cl = 1 + 2*g^2*S_ij / (g^2*(S_ii+S_jj)+R_c) exact.")


def run_numerical_channel():
    print("\n=================================================================")
    print("CHANNEL 2: BRUTE-FORCE FINITE-HORIZON KALMAN FILTERING & LIMITS")
    print("=================================================================")

    # A. Registered test instance + chk:mis-dynamic benchmark tuples
    print("\n--- A. Scalar benchmarks (including chk:mis-dynamic tuples and |F|>=1) ---")
    cases = [
        ("Static F=0", 0.0, 1.0, 1.0, 1.0, 1.0, 0.5, 50),
        ("Registered (chk:mis-dynamic #2)", 0.5, 0.75, 2.0, 2.0, 1.0, 0.0, 120),
        ("chk:mis-dynamic #1 (asym)", 0.9, 0.19, 1.0, 0.5, 1.5, 0.2, 200),
        ("chk:mis-dynamic #3 (asym)", 0.99, 0.0199, 0.3, 3.0, 0.7, 0.1, 600),
        ("Random walk F=1 (sym)", 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 4000),
        ("Random walk F=1 (asym, Rc>0)", 1.0, 0.5, 1.0, 2.0, 1.3, 0.3, 4000),
        ("Unstable F=1.2 (asym)", 1.2, 0.5, 1.0, 2.0, 1.0, 0.3, 120),
        ("Unstable F=2.0 (sym)", 2.0, 1.0, 1.0, 1.0, 1.0, 0.5, 80),
    ]
    max_err_stat = 0.0
    max_err_nonstat = 0.0
    for label, F, Q, Rsi, Rsj, g, Rc, T in cases:
        cf = closed_form_scalar(F, Q, Rsi, Rsj, g, Rc)
        V_bf, Pact_bf, Sii_bf, Sjj_bf, Sij_bf = brute_force_scalar_error_basis(F, Q, Rsi, Rsj, g, Rc, T=T)
        err_V = abs(cf["Vex"] - V_bf)
        err_P = abs(cf["P_l1_act"] - Pact_bf)
        if abs(F) < 1.0:
            max_err_stat = max(max_err_stat, err_V)
            assert err_V < 1e-13, f"Mismatch for {label}: {err_V}"
        elif abs(F) == 1.0:
            max_err_nonstat = max(max_err_nonstat, err_V)
            assert err_V < 5e-5, f"F=1 convergence mismatch for {label}: {err_V}"
        else:
            assert err_V < 1e-12, f"|F|>1 mismatch for {label}: {err_V}"
        assert err_P < 1e-12, f"P_act mismatch for {label}: {err_P}"
        print(
            f"  {label:32s}: Sij={cf['Sij']:.6f}, rho={cf['rho']:.6f}, "
            f"V1={cf['V1']:.8f}, Vex={cf['Vex']:.8f}, Vbf={V_bf:.8f}, |diff|={err_V:.2e}, "
            f"V1/Vex={cf['ratio_V1']:.6f}, Pact/Pcl={cf['ratio_P_act_cl']:.6f}"
        )
    print(f"[PASS] Stationary max |Vex - Vbf| = {max_err_stat:.2e}; F=1 (T=4000, O(1/T)) max diff = {max_err_nonstat:.2e}.")

    # B. Generic non-symmetric, non-diagonal vector K=2 and K=3 checks vs brute force
    print("\n--- B. Generic vector dynamic worlds (K=2, K=3) vs brute force ---")
    rng = np.random.default_rng(20261122)
    max_vec_err = 0.0
    for K, r, Rc_scale in [(2, 1, 0.15), (2, 2, 0.0), (3, 2, 0.2), (3, 3, 0.0)]:
        A = rng.normal(size=(K, K))
        F = A / (np.max(np.abs(np.linalg.eigvals(A))) + 0.35)
        Gq = rng.normal(size=(K, K)); Q = Gq @ Gq.T + 0.2 * np.eye(K)
        Hsi = rng.normal(size=(K, K)); Hsj = rng.normal(size=(K, K))
        Gi = rng.normal(size=(K, K)); Rsi = Gi @ Gi.T + 0.2 * np.eye(K)
        Gj = rng.normal(size=(K, K)); Rsj = Gj @ Gj.T + 0.2 * np.eye(K)
        Hj = rng.normal(size=(r, K))
        Gc = rng.normal(size=(r, r))
        Rc = Rc_scale * (Gc @ Gc.T + 0.2 * np.eye(r)) if Rc_scale > 0 else np.zeros((r, r))
        cf = vector_closed_form(F, Q, Hsi, Hsj, Rsi, Rsj, Hj, Rc)
        V_bf = vector_brute_force(F, Q, Hsi, Hsj, Rsi, Rsj, Hj, Rc, T=220)
        diff = abs(cf["Vex"] - V_bf)
        max_vec_err = max(max_vec_err, diff)
        assert diff < 1e-13, f"Vector mismatch K={K}, r={r}: {diff}"
        print(f"  K={K}, r={r}, Rc_scale={Rc_scale:4.2f}: V1={cf['V1']:.10f}, Vex={cf['Vex']:.10f}, |diff|={diff:.2e}, V1/Vex={cf['V1']/cf['Vex']:.6f}")
    print(f"[PASS] Generic vector max |Vex - Vbf| = {max_vec_err:.2e}.")

    # C. Aligned and Isotropic vector closed-form decomposition checks
    print("\n--- C. Aligned & isotropic vector exact decompositions ---")
    # Isotropic K=3 with arbitrary rank-2 code Hj and non-diagonal Rc
    f_iso, q_iso, ri_iso, rj_iso = 0.85, 0.6, 1.2, 0.7
    F_iso = f_iso * np.eye(3)
    Q_iso = q_iso * np.eye(3)
    Hj_iso = np.array([[1.2, -0.5, 0.7], [0.3, 1.4, -0.8]])
    Rc_iso = np.array([[0.4, 0.15], [0.15, 0.3]])
    cf_iso = vector_closed_form(F_iso, Q_iso, np.eye(3), np.eye(3), ri_iso * np.eye(3), rj_iso * np.eye(3), Hj_iso, Rc_iso)
    G_iso = Hj_iso @ Hj_iso.T
    evals_G, evecs_G = np.linalg.eigh(G_iso)
    G_inv_sqrt = evecs_G @ np.diag(1.0 / np.sqrt(evals_G)) @ evecs_G.T
    d_eigs = np.linalg.eigvalsh(G_inv_sqrt @ Rc_iso @ G_inv_sqrt)
    Vex_decomp = sum(closed_form_scalar(f_iso, q_iso, ri_iso, rj_iso, 1.0, float(d))["Vex"] for d in d_eigs)
    V1_decomp = sum(closed_form_scalar(f_iso, q_iso, ri_iso, rj_iso, 1.0, float(d))["V1"] for d in d_eigs)
    assert abs(cf_iso["Vex"] - Vex_decomp) < 1e-14
    assert abs(cf_iso["V1"] - V1_decomp) < 1e-14
    print(f"  Isotropic K=3, r=2: Vex_mat={cf_iso['Vex']:.12f}, sum_scalar={Vex_decomp:.12f}, diff={abs(cf_iso['Vex']-Vex_decomp):.2e}")
    print(f"                      V1_mat ={cf_iso['V1']:.12f}, sum_scalar={V1_decomp:.12f}, diff={abs(cf_iso['V1']-V1_decomp):.2e}")

    # Aligned K=3 in non-standard orthogonal basis U
    U, _ = np.linalg.qr(rng.normal(size=(3, 3)))
    f_modes = [0.2, 0.75, 0.95]
    q_modes = [1.0, 0.5, 0.2]
    ri_modes = [0.8, 1.5, 0.4]
    rj_modes = [1.2, 0.6, 2.0]
    g_modes = [1.3, 0.7]  # code reads modes 0 and 2
    rc_modes = [0.1, 0.25]
    F_al = U @ np.diag(f_modes) @ U.T
    Q_al = U @ np.diag(q_modes) @ U.T
    Rsi_al = U @ np.diag(ri_modes) @ U.T
    Rsj_al = U @ np.diag(rj_modes) @ U.T
    Hj_al = np.vstack([g_modes[0] * U[:, 0], g_modes[1] * U[:, 2]])
    Rc_al = np.diag(rc_modes)
    cf_al = vector_closed_form(F_al, Q_al, np.eye(3), np.eye(3), Rsi_al, Rsj_al, Hj_al, Rc_al)
    Vex_al_sum = (
        closed_form_scalar(f_modes[0], q_modes[0], ri_modes[0], rj_modes[0], g_modes[0], rc_modes[0])["Vex"]
        + closed_form_scalar(f_modes[2], q_modes[2], ri_modes[2], rj_modes[2], g_modes[1], rc_modes[1])["Vex"]
    )
    V1_al_sum = (
        closed_form_scalar(f_modes[0], q_modes[0], ri_modes[0], rj_modes[0], g_modes[0], rc_modes[0])["V1"]
        + closed_form_scalar(f_modes[2], q_modes[2], ri_modes[2], rj_modes[2], g_modes[1], rc_modes[1])["V1"]
    )
    assert abs(cf_al["Vex"] - Vex_al_sum) < 1e-14 and abs(cf_al["V1"] - V1_al_sum) < 1e-14
    print(f"  Aligned K=3, r=2:   Vex_mat={cf_al['Vex']:.12f}, sum_scalar={Vex_al_sum:.12f}, diff={abs(cf_al['Vex']-Vex_al_sum):.2e}")

    # D. Exact asymptotic limits & non-commutativity checks
    print("\n--- D. Asymptotic limits, non-commutativity, crossover & boundedness ---")
    # Crossover 1 - F^2 = c * sqrt(Q/Rs) at Q/Rs = 1e-8
    lam_small = 1e-8
    for c_val in [0.0, 0.5, 1.0, 2.0, 10.0]:
        F_c = math.sqrt(1.0 - c_val * math.sqrt(lam_small))
        cf_c = closed_form_scalar(F_c, lam_small, 1.0, 1.0, 1.0, 0.0)
        rho_lim = 0.5 * (1.0 + c_val / math.sqrt(c_val**2 + 4.0))
        assert abs(cf_c["rho"] - rho_lim) < 2e-4
        print(f"  Crossover c={c_val:4.1f}, Q/Rs=1e-8: rho={cf_c['rho']:.6f}, limit={rho_lim:.6f}, diff={abs(cf_c['rho']-rho_lim):.2e}")

    # Q -> 0+ at fixed F=0.5 (Rc=0 and fixed Rc=0.5)
    F_fix = 0.5
    delta_fix = 1.0 - F_fix**2
    for Q_val in [1e-4, 1e-6, 1e-8]:
        cf0 = closed_form_scalar(F_fix, Q_val, 1.0, 1.0, 1.0, 0.0)
        asymp0 = math.log(2.0) * delta_fix**2 / Q_val
        cf_rc = closed_form_scalar(F_fix, Q_val, 1.0, 1.0, 1.0, 0.5)
        asymp_rc = delta_fix**4 / Q_val**2
        print(f"  Q={Q_val:.0e}, F=0.5: Rc=0 ratio/asymp={cf0['ratio_V1']/asymp0:.8f}; Rc=0.5 ratio/asymp={cf_rc['ratio_V1']/asymp_rc:.8f}")
        if Q_val == 1e-8:
            assert abs(cf0["ratio_V1"] / asymp0 - 1.0) < 1e-4
            assert abs(cf_rc["ratio_V1"] / asymp_rc - 1.0) < 1e-4

    # F = 1 symmetric bound: Q -> 0+ with Rc = 0 (limit ln 2 / ln(4/3)) and fixed Rc = 1 (limit 4)
    cf_f1_0 = closed_form_scalar(1.0, 1e-10, 1.0, 1.0, 1.0, 0.0)
    cf_f1_rc = closed_form_scalar(1.0, 1e-10, 1.0, 1.0, 1.0, 1.0)
    lim_f1_0 = math.log(2.0) / math.log(4.0 / 3.0)
    assert abs(cf_f1_0["ratio_V1"] - lim_f1_0) < 1e-3 and cf_f1_0["ratio_V1"] < lim_f1_0
    assert abs(cf_f1_rc["ratio_V1"] - 4.0) < 1e-3 and cf_f1_rc["ratio_V1"] < 4.0
    print(f"  F=1, Q=1e-10, Rc=0:   V1/Vex={cf_f1_0['ratio_V1']:.8f} < ln(2)/ln(4/3)={lim_f1_0:.8f}")
    print(f"  F=1, Q=1e-10, Rc=1.0: V1/Vex={cf_f1_rc['ratio_V1']:.8f} < 4.00000000")

    # E. Constructive counterexamples to vector ratio non-inversion (C5)
    print("\n--- E. Vector ratio inversions (verified against brute-force KF) ---")
    # E1: K=2 rank-limited dynamic sender-side completion
    F2 = np.array([[0.8, 0.0], [0.5, 0.5]])
    Q2 = np.array([[1.0, 0.0], [0.0, 0.1]])
    Hsi2 = np.array([[0.0, 1.0]])
    Hsj2 = np.array([[1.0, 0.0]])
    Hj2 = np.array([[0.0, 1.0]])
    Rc2 = np.array([[0.01]])
    for rs_val in [0.01, 1e-4]:
        cf2 = vector_closed_form(F2, Q2, Hsi2, Hsj2, np.array([[rs_val]]), np.array([[rs_val]]), Hj2, Rc2)
        bf2 = vector_brute_force(F2, Q2, Hsi2, Hsj2, np.array([[rs_val]]), np.array([[rs_val]]), Hj2, Rc2, T=220)
        assert abs(cf2["Vex"] - bf2) < 1e-13
        assert cf2["V1"] < cf2["Vex"]
        print(
            f"  K=2 rank-1 (Rs={rs_val:6.4f}): V0={cf2['V0']:.8f}, V1={cf2['V1']:.8f}, "
            f"Vex={cf2['Vex']:.8f}, Vbf={bf2:.8f}, V1/Vex={cf2['V1']/cf2['Vex']:.6f}, V0/Vex={cf2['V0']/cf2['Vex']:.6f}"
        )

    # E2: K=3 invertible noiseless code (Hj=I_3, Rc=0) with full-rank sensors
    F3 = np.array([[0.1, 0.6, 0.3], [-0.1, 0.2, 0.1], [-0.5, -0.2, 0.2]])
    G3 = np.array([[0.3, 0.9, -2.4], [1.5, -1.9, 0.0], [0.2, -0.1, 0.2]])
    Q3 = G3 @ G3.T + 0.01 * np.eye(3)
    Hsi3 = np.array([[-0.6, -0.7, -0.1], [0.2, -0.7, 0.3], [-0.9, -0.6, -0.2]])
    Hsj3 = np.array([[2.1, -0.5, -0.8], [1.0, 0.4, 0.1], [-2.4, 0.4, -0.1]])
    Gi3 = np.array([[0.4, -0.3, 0.4], [1.6, -0.5, 1.3], [-1.3, 0.6, -0.2]])
    Gj3 = np.array([[0.1, -0.8, 1.3], [0.0, -0.3, -1.6], [-0.2, -1.1, 1.3]])
    Rsi3 = Gi3 @ Gi3.T + 0.01 * np.eye(3)
    Rsj3 = Gj3 @ Gj3.T + 0.01 * np.eye(3)
    cf3 = vector_closed_form(F3, Q3, Hsi3, Hsj3, Rsi3, Rsj3, np.eye(3), np.zeros((3, 3)))
    bf3 = vector_brute_force(F3, Q3, Hsi3, Hsj3, Rsi3, Rsj3, np.eye(3), np.zeros((3, 3)), T=200)
    assert abs(cf3["Vex"] - bf3) < 1e-11, f"diff={abs(cf3['Vex'] - bf3)}"
    assert cf3["V1"] < cf3["Vex"], "Expected V1 < Vex inversion"
    print(
        f"  K=3 full-rank sensors, Hj=I3, Rc=0: V1={cf3['V1']:.10f}, Vex={cf3['Vex']:.10f}, "
        f"Vbf={bf3:.10f}, |diff|={abs(cf3['Vex']-bf3):.2e}, V1/Vex={cf3['V1']/cf3['Vex']:.8f}"
    )

    # E3: K=3 rank-1 sensors, Hj=I_3, Rc=0 (stronger inversion, well-conditioned)
    F3b = np.array([[0.7, -0.5, 0.6], [0.3, 0.0, -0.5], [0.0, 0.2, 0.0]])
    G3b = np.array([[-0.6, -0.8, 0.7], [0.6, 1.0, -0.8], [1.3, 2.5, 0.1]])
    Q3b = G3b @ G3b.T + 0.05 * np.eye(3)
    Hsi3b = np.array([[1.2, -1.3, 2.4]])
    Hsj3b = np.array([[1.2, 0.3, -1.6]])
    Rsi3b = np.array([[1.62]])
    Rsj3b = np.array([[0.80]])
    cf3b = vector_closed_form(F3b, Q3b, Hsi3b, Hsj3b, Rsi3b, Rsj3b, np.eye(3), np.zeros((3, 3)))
    bf3b = vector_brute_force(F3b, Q3b, Hsi3b, Hsj3b, Rsi3b, Rsj3b, np.eye(3), np.zeros((3, 3)), T=200)
    assert abs(cf3b["Vex"] - bf3b) < 1e-13
    assert cf3b["V1"] < cf3b["Vex"]
    print(
        f"  K=3 rank-1 sensors,    Hj=I3, Rc=0: V1={cf3b['V1']:.10f}, Vex={cf3b['Vex']:.10f}, "
        f"Vbf={bf3b:.10f}, |diff|={abs(cf3b['Vex']-bf3b):.2e}, V1/Vex={cf3b['V1']/cf3b['Vex']:.8f}"
    )

    # F. Belief-only vs raw-history retention gap (demonstrating scope of (m_i, y_ij))
    print("\n--- F. Belief-only I(eta_T; y | m_i) vs raw-history I(eta_T; y | s_i(0..T)) ---")
    for F_s, Q_s in [(0.0, 1.0), (0.8, 0.36)]:
        T = 25
        P0_s = Q_s / (1.0 - F_s**2)
        n_in = 1 + T + 2 * (T + 1) + 1
        cov_in = np.zeros(n_in)
        cov_in[0] = P0_s
        cov_in[1:1 + T] = Q_s
        cov_in[1 + T:1 + 2 * T + 1] = 1.0
        cov_in[1 + 2 * T + 1:1 + 3 * T + 2] = 1.0
        eta_row = np.zeros(n_in); eta_row[0] = 1.0
        mi_row = np.zeros(n_in); mj_row = np.zeros(n_in)
        si_rows = []
        Pmi = P0_s; Pmj = P0_s
        for t in range(T + 1):
            if t > 0:
                eta_row = F_s * eta_row; eta_row[t] = 1.0
                mi_row = F_s * mi_row; mj_row = F_s * mj_row
                Pmi = F_s**2 * Ppi + Q_s; Pmj = F_s**2 * Ppj + Q_s
            ki = Pmi / (Pmi + 1.0); kj = Pmj / (Pmj + 1.0)
            Ppi = (1.0 - ki) * Pmi; Ppj = (1.0 - kj) * Pmj
            si_row = eta_row.copy(); si_row[1 + T + t] += 1.0
            sj_row = eta_row.copy(); sj_row[1 + 2 * T + 1 + t] += 1.0
            si_rows.append(si_row)
            mi_row = (1.0 - ki) * mi_row + ki * si_row
            mj_row = (1.0 - kj) * mj_row + kj * sj_row

        def cond_mi(r_e, r_y, cond_list):
            A = np.vstack([r_e, r_y] + cond_list)
            C_all = (A * cov_in) @ A.T
            Cc = C_all[:2, :2] - C_all[:2, 2:] @ np.linalg.solve(C_all[2:, 2:], C_all[2:, :2])
            return 0.5 * math.log((Cc[0, 0] * Cc[1, 1]) / (Cc[0, 0] * Cc[1, 1] - Cc[0, 1]**2))

        V_m = cond_mi(eta_row, mj_row, [mi_row])
        V_raw = cond_mi(eta_row, mj_row, si_rows)
        print(f"  F={F_s:3.1f}, Q={Q_s:4.2f}, Rs=1, Rc=0 (T=25): I(eta;y|m_i)={V_m:.10f}, I(eta;y|s_i(0..T))={V_raw:.10f}, gap={V_raw-V_m:.3e}")
        if F_s == 0.0:
            assert abs(V_raw - V_m) < 1e-14
        else:
            assert V_raw - V_m > 1e-2


def run_negative_controls():
    print("\n=================================================================")
    print("PLANTED-ERROR NEGATIVE CONTROLS (EACH MUST DETECT THE ERROR)")
    print("=================================================================")
    # Control 1: Drop proper-prior correction Dpr at registered instance (F=0.5, Q=0.75, Rs=2, Rc=0)
    cf = closed_form_scalar(0.5, 0.75, 2.0, 2.0, 1.0, 0.0)
    V_bf, Pact_bf, Sii, Sjj, Sij = brute_force_scalar_error_basis(0.5, 0.75, 2.0, 2.0, 1.0, 0.0, T=120)
    V_wrong_track = 0.5 * math.log((Sii + Sjj - 2.0 * Sij) / (Sjj - Sij**2 / Sii))
    err1 = abs(V_wrong_track - V_bf)
    assert err1 > 1e-2, "Negative control 1 failed to discriminate!"
    print(f"[PASS - NEG CONTROL 1] Dropping Delta^pr at F=0.5 gives V_track={V_wrong_track:.8f} vs V_bf={V_bf:.8f} (err={err1:.4e} > 1e-2).")

    # Control 2: Drop cross-covariance (set Sij=0 -> level 1) at registered instance
    err2 = abs(cf["V1"] - V_bf)
    assert err2 > 1e-1, "Negative control 2 failed to discriminate!"
    print(f"[PASS - NEG CONTROL 2] Setting S_ij=0 gives V1={cf['V1']:.8f} vs V_bf={V_bf:.8f} (err={err2:.4e} > 1e-1).")

    # Control 3: Flip sign of S_ij in level-1 variance ratio
    P_act_wrong = cf["P_l1_cl"] * (1.0 - (2.0 * Sij) / (Sii + Sjj))
    err3 = abs(P_act_wrong - Pact_bf)
    assert err3 > 1e-1, "Negative control 3 failed to discriminate!"
    print(f"[PASS - NEG CONTROL 3] Flipping sign of S_ij in P_act gives {P_act_wrong:.8f} vs P_bf={Pact_bf:.8f} (err={err3:.4e} > 1e-1).")

    # Control 4: Assert V1 >= Vex on K=3 invertible noiseless code counterexample (must fail!)
    F3b = np.array([[0.7, -0.5, 0.6], [0.3, 0.0, -0.5], [0.0, 0.2, 0.0]])
    G3b = np.array([[-0.6, -0.8, 0.7], [0.6, 1.0, -0.8], [1.3, 2.5, 0.1]])
    Q3b = G3b @ G3b.T + 0.05 * np.eye(3)
    cf3b = vector_closed_form(F3b, Q3b, np.array([[1.2, -1.3, 2.4]]), np.array([[1.2, 0.3, -1.6]]),
                              np.array([[1.62]]), np.array([[0.80]]), np.eye(3), np.zeros((3, 3)))
    gap4 = cf3b["Vex"] - cf3b["V1"]
    assert gap4 > 0.1, "Negative control 4 failed to discriminate!"
    print(f"[PASS - NEG CONTROL 4] Naive static-style claim V1 >= Vex for invertible noiseless code fails by Vex - V1 = {gap4:.6f} > 0.1.")


if __name__ == "__main__":
    run_symbolic_channel()
    run_numerical_channel()
    run_negative_controls()
    print("\nALL CHECKS AND NEGATIVE CONTROLS PASSED.")
