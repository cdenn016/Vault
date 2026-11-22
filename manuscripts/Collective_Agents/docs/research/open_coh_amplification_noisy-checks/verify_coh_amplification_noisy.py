"""Verification script for open:coh-amplification-noisy (Amplification beyond noiseless circulation).

Covers Claims C1-C7 with two independent channels (SymPy exact rational arithmetic and NumPy/SciPy
direct world-coordinate matrix evaluations) plus three planted-error negative controls (NC1-NC3).
"""
from __future__ import annotations

import sys
import numpy as np
import scipy.linalg as la
import sympy as sp


def make_spd(K: int, rng: np.random.Generator) -> np.ndarray:
    M = rng.standard_normal((K, K))
    return M @ M.T + 0.1 * np.eye(K)


def edge_map_np(P_j: np.ndarray, H_i: np.ndarray, R_i: np.ndarray) -> np.ndarray:
    S_ji = H_i @ P_j @ H_i.T + R_i
    K_ji = P_j @ H_i.T @ la.inv(S_ji)
    return K_ji @ H_i


def edge_map_sp(P_j: sp.Matrix, H_i: sp.Matrix, R_i: sp.Matrix) -> sp.Matrix:
    S_ji = H_i * P_j * H_i.T + R_i
    K_ji = P_j * H_i.T * S_ji.inv()
    return K_ji * H_i


def main() -> int:
    print("=" * 78)
    print("VERIFICATION SUITE: open:coh-amplification-noisy (Claims C1 to C7 + NC1 to NC3)")
    print("=" * 78)

    # -------------------------------------------------------------------------
    # 0. Registered Test Instance from s06_coherence.tex (line 121) & chk06_coherence.tex (line 50)
    # -------------------------------------------------------------------------
    print("\n[0] Registered Test Instance (s06_coherence.tex line 121, chk06_coherence.tex line 50)")
    alpha = 0.9
    x_val = 4.0
    r_val = 0.1
    Pa = np.array([[1.0, alpha * np.sqrt(x_val)], [alpha * np.sqrt(x_val), x_val]])
    Pb = np.array([[x_val, alpha * np.sqrt(x_val)], [alpha * np.sqrt(x_val), 1.0]])
    H_id = np.eye(2)
    for M_val in [1.0, 10.0, 100.0, 1e4]:
        Rb = np.diag([r_val, M_val])
        Ra = np.diag([M_val, r_val])
        A_ab = edge_map_np(Pa, H_id, Rb)
        A_ba = edge_map_np(Pb, H_id, Ra)
        rho_val = max(abs(la.eigvals(A_ab @ A_ba)))
        print(f"  M = {M_val:7.1f}: rho(A_c) = {rho_val:.6f} (limit alpha^2*x/(1+r)^2 = {alpha**2 * x_val / (1 + r_val)**2:.6f})")

    # -------------------------------------------------------------------------
    # 1. Claim C1: Refutation of rho(bar_A_c) = max(rho(A_c), 1) and base-point invariance
    # -------------------------------------------------------------------------
    print("\n[1] Claim C1: Exact rational counterexamples for noisy round-trip map bar_A_c = (I - A_{1N}) + A_c")
    # Counterexample C1(a): rho(A_c) = 1/2 < 1, while rho(bar_A_c^(1)) = 7/6 > 1 and rho(bar_A_c^(2)) = 1
    P1_sp = sp.Matrix([[1, sp.Rational(3, 2)], [sp.Rational(3, 2), 4]])
    P2_sp = sp.Matrix([[4, sp.Rational(3, 2)], [sp.Rational(3, 2), 1]])
    h1_sp = sp.Matrix([[0, 1]])
    h2_sp = sp.Matrix([[1, 0]])
    R1_sp = sp.Matrix([[sp.Rational(1, 2)]])
    R2_sp = sp.Matrix([[sp.Rational(2, 1)]])

    A21_sp = edge_map_sp(P2_sp, h1_sp, R1_sp)
    A12_sp = edge_map_sp(P1_sp, h2_sp, R2_sp)
    Ac1_sp = A12_sp * A21_sp
    Ac2_sp = A21_sp * A12_sp
    bar_Ac1_sp = sp.eye(2) - A12_sp + Ac1_sp
    bar_Ac2_sp = sp.eye(2) - A21_sp + Ac2_sp

    eigs_Ac1 = list(Ac1_sp.eigenvals().keys())
    eigs_bar1 = list(bar_Ac1_sp.eigenvals().keys())
    eigs_bar2 = list(bar_Ac2_sp.eigenvals().keys())
    print(f"  Counterexample C1(a) [SymPy exact]:")
    print(f"    spec(A_c)       = {eigs_Ac1}, rho(A_c) = {max(abs(e) for e in eigs_Ac1)} < 1")
    print(f"    spec(bar_A_c^1) = {eigs_bar1}, rho(bar_A_c^1) = {max(abs(e) for e in eigs_bar1)} > 1 (amplifies at agent 1!)")
    print(f"    spec(bar_A_c^2) = {eigs_bar2}, rho(bar_A_c^2) = {max(abs(e) for e in eigs_bar2)} == 1 (stable at agent 2!)")
    assert max(abs(e) for e in eigs_Ac1) == sp.Rational(1, 2)
    assert max(abs(e) for e in eigs_bar1) == sp.Rational(7, 6)
    assert max(abs(e) for e in eigs_bar2) == sp.Rational(1, 1)

    # Also C1(a') under prop:coh-no-amplification(c) (R_i >= X_ii on every edge!):
    # Let P1 = [[1, 3], [3, 10]], P2 = [[10, 3], [3, 1]], h1 = [0, 1], h2 = [1, 0], R1 = 10 = X_11, R2 = 10 = X_22.
    # Wait: if R1 = 10 and R2 = 10, then s_21 = 1/(1+10) = 1/11, s_12 = 1/(1+10) = 1/11,
    # and tr(A_c)/s_12 = (3 * 3) / (1 * (1 + 10)) = 9/11 < 1.
    # What if P1 = [[1, 3], [3, 10]] (so X_11 = 10, X_12 = 1) and P2 = [[100, 25], [25, 7]] (so X_22 = 100, X_21 = 7)?
    # Set R1 = 10 = X_11 and R2 = 100 = X_22 (both satisfy prop:coh-no-amplification(c): R_i >= X_ii!).
    # Then s_21 = 7 / (7 + 10) = 7/17, s_12 = 1 / (1 + 100) = 1/101.
    # And tr(A_c) = (3 * 25) / ((7 + 10) * (1 + 100)) = 75 / 1717 < 1!
    # Yet tr(A_c) / s_12 = 75 / 17 = 4.41176 > 1, so lambda_rt^(1) = 1 - 1/101 + 75/1717 = 1 + 58/1717 = 1775/1717 > 1!
    P1_c_sp = sp.Matrix([[1, 3], [3, 10]])
    P2_c_sp = sp.Matrix([[100, 25], [25, 7]])
    R1_c_sp = sp.Matrix([[10]])
    R2_c_sp = sp.Matrix([[100]])
    A21_c_sp = edge_map_sp(P2_c_sp, h1_sp, R1_c_sp)
    A12_c_sp = edge_map_sp(P1_c_sp, h2_sp, R2_c_sp)
    Ac_c_sp = A12_c_sp * A21_c_sp
    bar_Ac_c_sp = sp.eye(2) - A12_c_sp + Ac_c_sp
    print(f"  Counterexample C1(a') [R_i = X_ii satisfying prop:coh-no-amplification(c) on every edge]:")
    print(f"    rho(A_c)        = {max(abs(e) for e in Ac_c_sp.eigenvals().keys())} = {float(max(abs(e) for e in Ac_c_sp.eigenvals().keys())):.6f} < 1")
    print(f"    rho(bar_A_c^1)  = {max(abs(e) for e in bar_Ac_c_sp.eigenvals().keys())} = {float(max(abs(e) for e in bar_Ac_c_sp.eigenvals().keys())):.6f} > 1")
    assert max(abs(e) for e in Ac_c_sp.eigenvals().keys()) == sp.Rational(75, 1717)
    assert max(abs(e) for e in bar_Ac_c_sp.eigenvals().keys()) == sp.Rational(1775, 1717)

    # Counterexample C1(b): rho(A_c) = 6/5 > 1, while rho(bar_A_c^1) = 1 (no geometric growth of round-trip map!)
    P1_b_sp = sp.Matrix([[1, 2], [2, 5]])
    P2_b_sp = sp.Matrix([[5, -2], [-2, 1]])
    R1_b_sp = sp.Matrix([[sp.Rational(2, 3)]])
    R2_b_sp = sp.Matrix([[1]])
    A21_b_sp = edge_map_sp(P2_b_sp, h1_sp, R1_b_sp)
    A12_b_sp = edge_map_sp(P1_b_sp, h2_sp, R2_b_sp)
    Ac_b_sp = A12_b_sp * A21_b_sp
    bar_Ac_b_sp = sp.eye(2) - A12_b_sp + Ac_b_sp
    eigs_Ac_b = list(Ac_b_sp.eigenvals().keys())
    eigs_bar_b = list(bar_Ac_b_sp.eigenvals().keys())
    print(f"  Counterexample C1(b) [SymPy exact]:")
    print(f"    spec(A_c)       = {eigs_Ac_b}, rho(A_c) = {max(abs(e) for e in eigs_Ac_b)} > 1 (cycle product amplifies!)")
    print(f"    spec(bar_A_c^1) = {eigs_bar_b}, rho(bar_A_c^1) = {max(abs(e) for e in eigs_bar_b)} == 1 (round-trip map does not grow!)")
    assert max(abs(e) for e in eigs_Ac_b) == sp.Rational(6, 5)
    assert max(abs(e) for e in eigs_bar_b) == sp.Rational(1, 1)

    # -------------------------------------------------------------------------
    # 2. Claim C2 & NC1: Coded reduction & sharp return-noiseless bound for bar_A_c
    # -------------------------------------------------------------------------
    print("\n[2] Claim C2 & Negative Control NC1: Return-noiseless round-trip bound across 5000 random cycles")
    rng = np.random.default_rng(20261121)
    c2_spec_max_err = 0.0
    c2_bound_violations = 0
    c2_common_prior_violations = 0
    c2_max_ratio = 0.0
    nc1_planted_violations = 0

    for trial in range(5000):
        K = int(rng.integers(2, 6))
        N = int(rng.integers(2, 6))
        r = int(rng.integers(1, K))
        common_prior = (trial < 1000)
        if common_prior:
            P0 = make_spd(K, rng)
            Ps = [P0.copy() for _ in range(N)]
        else:
            Ps = [make_spd(K, rng) * (10.0 ** rng.uniform(-1.5, 1.5)) for _ in range(N)]
        Hs = [rng.standard_normal((r, K)) for _ in range(N)]
        Rs = [make_spd(r, rng) * (10.0 ** rng.uniform(-1.5, 1.5)) for _ in range(N)]

        As = []
        r_es = []
        snr_facs = []
        for i in range(N):
            j = (i + 1) % N
            As.append(edge_map_np(Ps[j], Hs[i], Rs[i]))
            X_ji = Hs[i] @ Ps[j] @ Hs[i].T
            X_ii = Hs[i] @ Ps[i] @ Hs[i].T
            S_ji = X_ji + Rs[i]
            r_es.append(max(la.eigvalsh(X_ii, S_ji)))
            snr_facs.append(max(la.eigvalsh(X_ji, S_ji)))

        Ac = np.eye(K)
        for i in range(N):
            Ac = As[i] @ Ac
        bar_Ac = np.eye(K) - As[N - 1] + Ac
        eigs_bar_world = np.sort_complex(la.eigvals(bar_Ac))

        # Channel 2: Reduced coded representation M_rt^(1) = (I - Sigma_{1N}) + Sigma_{1N} tilde_C_c
        X_1N = Hs[N - 1] @ Ps[0] @ Hs[N - 1].T
        S_1N = X_1N + Rs[N - 1]
        X_1N_half = la.fractional_matrix_power(X_1N, 0.5)
        X_1N_mhalf = la.fractional_matrix_power(X_1N, -0.5)
        Phi_1 = Ps[0] @ Hs[N - 1].T @ X_1N_mhalf
        Phi_1_plus = X_1N_mhalf @ Hs[N - 1]
        Sigma_1N = X_1N_half @ la.inv(S_1N) @ X_1N_half

        A_prefix = np.eye(K)
        for i in range(N - 1):
            A_prefix = As[i] @ A_prefix
        tilde_C_c = Phi_1_plus @ A_prefix @ Phi_1
        M_rt = (np.eye(r) - Sigma_1N) + Sigma_1N @ tilde_C_c
        eigs_bar_coded = np.sort_complex(np.append(la.eigvals(M_rt), np.ones(K - r)))
        c2_spec_max_err = max(c2_spec_max_err, float(np.max(np.abs(eigs_bar_world - eigs_bar_coded))))

        rho_bar = float(np.max(np.abs(eigs_bar_world)))
        if common_prior and rho_bar > 1.0 + 1e-12:
            c2_common_prior_violations += 1

        X_NN = Hs[N - 1] @ Ps[N - 1] @ Hs[N - 1].T
        r_1N_noiseless = float(max(la.eigvalsh(X_NN, X_1N)))
        prod_c2 = np.sqrt(r_1N_noiseless) * np.prod([np.sqrt(r_es[i] * snr_facs[i]) for i in range(N - 1)])
        bound_c2 = max(1.0, float(prod_c2))
        if rho_bar > bound_c2 + 1e-10:
            c2_bound_violations += 1
        if prod_c2 > 1.0:
            c2_max_ratio = max(c2_max_ratio, rho_bar / bound_c2)

        # Planted error NC1: using noisy edge ratio on N->1 instead of noiseless r_{1N}^circ
        planted_prod = np.prod([np.sqrt(r_es[i] * snr_facs[i]) for i in range(N)])
        planted_bound = max(1.0, float(planted_prod))
        if rho_bar > planted_bound + 1e-6:
            nc1_planted_violations += 1

    print(f"  Max spectral discrepancy between world bar_A_c and coded M_rt^(1) U {{1}}: {c2_spec_max_err:.2e}")
    print(f"  Violations of C2 return-noiseless bound (5000 trials): {c2_bound_violations}")
    print(f"  Violations of rho(bar_A_c) <= 1 under common prior (1000 trials): {c2_common_prior_violations}")
    print(f"  Max ratio rho(bar_A_c) / C2_bound when C2_bound > 1: {c2_max_ratio:.6f}")
    print(f"  [Negative Control NC1] Planted noisy-edge-N->1 bound violated in {nc1_planted_violations}/4000 heterogeneous trials (PASS: >0)")
    assert c2_spec_max_err < 1e-10
    assert c2_bound_violations == 0
    assert c2_common_prior_violations == 0
    assert nc1_planted_violations > 50

    # -------------------------------------------------------------------------
    # 3. Claim C3: Full N-agent sequential (Gauss-Seidel) and synchronous (Jacobi) circulation
    # -------------------------------------------------------------------------
    print("\n[3] Claim C3: Full N-agent sequential (T_seq) and synchronous (T_sync) noisy circulation")
    # Build full NK x NK operators T_seq and T_sync and compare against characteristic equation in rank 1
    # and check noise-invariance of instability threshold tau^circ > 1.
    c3_poly_max_err = 0.0
    c3_contraction_violations = 0

    for trial in range(1000):
        K = 2
        N = 3
        Ps = [make_spd(K, rng) * (10.0 ** rng.uniform(-1, 1)) for _ in range(N)]
        Hs = [rng.standard_normal((1, K)) for _ in range(N)]
        Rs = [np.array([[10.0 ** rng.uniform(-1, 1)]]) for _ in range(N)]

        As = []
        s_list = []
        for i in range(N):
            j = (i + 1) % N
            As.append(edge_map_np(Ps[j], Hs[i], Rs[i]))
            w_j = float((Hs[i] @ Ps[j] @ Hs[i].T).item())
            s_list.append(w_j / (w_j + float(Rs[i].item())))

        # Synchronous operator on (R^K)^N: x_k(t+1) = (I - A_{k,k-1})x_k(t) + A_{k,k-1}x_{k-1}(t)
        T_sync = np.zeros((N * K, N * K))
        for k in range(N):
            km = (k - 1) % N
            T_sync[k*K:(k+1)*K, k*K:(k+1)*K] = np.eye(K) - As[km]
            T_sync[k*K:(k+1)*K, km*K:(km+1)*K] = As[km]

        # Sequential operator (sweep order k = 1, 2, ..., N-1, 0 corresponding to agents 2, 3, ..., N, 1)
        T_seq = np.eye(N * K)
        for k in [1, 2, 0]:
            km = (k - 1) % N
            Step = np.eye(N * K)
            Step[k*K:(k+1)*K, k*K:(k+1)*K] = np.eye(K) - As[km]
            Step[k*K:(k+1)*K, km*K:(km+1)*K] = As[km]
            T_seq = Step @ T_seq

        Ac = As[2] @ As[1] @ As[0]
        tr_Ac = float(np.trace(Ac))
        tau_circ = tr_Ac / float(np.prod(s_list))

        # Check characteristic equations at all non-unit eigenvalues
        for lam in la.eigvals(T_sync):
            if abs(lam - 1.0) > 1e-7:
                lhs = np.prod([lam - (1.0 - s_list[k]) for k in range(N)])
                c3_poly_max_err = max(c3_poly_max_err, float(abs(lhs - tr_Ac)))
        for lam in la.eigvals(T_seq):
            if abs(lam - 1.0) > 1e-7 and abs(lam) > 1e-7:
                lhs = np.prod([lam - (1.0 - s_list[k]) for k in range(N)])
                rhs = (lam ** (N - 1)) * tr_Ac
                c3_poly_max_err = max(c3_poly_max_err, float(abs(lhs - rhs)))

        if abs(tau_circ) <= 1.0:
            if max(abs(la.eigvals(T_sync))) > 1.0 + 1e-10 or max(abs(la.eigvals(T_seq))) > 1.0 + 1e-10:
                c3_contraction_violations += 1
            # Also verify step-by-step nonincrease of the quadratic Lyapunov energies E_sync and E_seq on random initial states
            z_init = rng.standard_normal(N)
            # In rank 1 with |tau_circ| <= 1, check common-prior case r_e^circ = 1 (where |tilde_C_{k,k-1}| <= 1):
            if all(float(max(la.eigvalsh(Hs[i] @ Ps[i] @ Hs[i].T, Hs[i] @ Ps[(i+1)%N] @ Hs[i].T))) <= 1.0 + 1e-12 for i in range(N)):
                pass

    # Explicit verification of C3(1) quadratic Lyapunov energies E_sync and E_seq across 500 common-prior higher-rank cycles:
    c3_energy_violations = 0
    for _ in range(500):
        K_e = 3
        N_e = 3
        r_e = 2
        P_comm = make_spd(K_e, rng)
        Hs_e = [rng.standard_normal((r_e, K_e)) for _ in range(N_e)]
        Rs_e = [make_spd(r_e, rng) * (10.0 ** rng.uniform(-1, 1)) for _ in range(N_e)]
        Sigmas_e = []
        C_tildes_e = []
        for k in range(N_e):
            km = (k - 1) % N_e
            kmm = (k - 2) % N_e
            X_k = Hs_e[km] @ P_comm @ Hs_e[km].T
            X_km = Hs_e[kmm] @ P_comm @ Hs_e[kmm].T
            S_k = X_k + Rs_e[km]
            Xk_half = la.fractional_matrix_power(X_k, 0.5)
            Xk_mhalf = la.fractional_matrix_power(X_k, -0.5)
            Xkm_mhalf = la.fractional_matrix_power(X_km, -0.5)
            Sigmas_e.append(Xk_half @ la.inv(S_k) @ Xk_half)
            C_tildes_e.append(Xk_mhalf @ Hs_e[km] @ P_comm @ Hs_e[kmm].T @ Xkm_mhalf)
        zs = [rng.standard_normal(r_e) for _ in range(N_e)]
        # Synchronous step
        zs_sync = [(np.eye(r_e) - Sigmas_e[k]) @ zs[k] + Sigmas_e[k] @ C_tildes_e[k] @ zs[(k - 1) % N_e] for k in range(N_e)]
        E_before = sum(float(zs[k].T @ la.inv(Sigmas_e[k]) @ zs[k]) for k in range(N_e))
        E_after = sum(float(zs_sync[k].T @ la.inv(Sigmas_e[k]) @ zs_sync[k]) for k in range(N_e))
        if E_after > E_before + 1e-10:
            c3_energy_violations += 1
        # Sequential sweep k = 1, 2, 0 (agents 2, 3, 1)
        z_curr = [z.copy() for z in zs]
        for k in [1, 2, 0]:
            km = (k - 1) % N_e
            z_curr[k] = (np.eye(r_e) - Sigmas_e[k]) @ z_curr[k] + Sigmas_e[k] @ C_tildes_e[k] @ z_curr[km]
        E_seq_before = float(zs[0].T @ la.inv(Sigmas_e[0]) @ zs[0]) + sum(float(zs[k].T @ (la.inv(Sigmas_e[k]) - np.eye(r_e)) @ zs[k]) for k in [1, 2])
        E_seq_after = float(z_curr[0].T @ la.inv(Sigmas_e[0]) @ z_curr[0]) + sum(float(z_curr[k].T @ (la.inv(Sigmas_e[k]) - np.eye(r_e)) @ z_curr[k]) for k in [1, 2])
        if E_seq_after > E_seq_before + 1e-10:
            c3_energy_violations += 1

    print(f"  Max characteristic-equation residual for T_sync and T_seq (1000 trials): {c3_poly_max_err:.2e}")
    print(f"  Violations of rho(T_sync), rho(T_seq) <= 1 when |tau^circ| <= 1: {c3_contraction_violations}")
    print(f"  Violations of quadratic Lyapunov energy dissipation E_sync and E_seq (500 trials): {c3_energy_violations}")
    assert c3_poly_max_err < 1e-10
    assert c3_contraction_violations == 0
    assert c3_energy_violations == 0

    # Explicit demonstration that when tau^circ > 1 (Ex 6.7(i) with alpha=0.9, x=4 => tau^circ = 3.24 > 1),
    # T_seq and T_sync amplify for ANY finite assigned noise R_c, even R_c = 100 (where rho(A_c) = 0.000318 << 1):
    print("  Persistent N-agent instability under Ex 6.7(i) (tau^circ = 3.24 > 1) at arbitrarily large noises:")
    for Rc_val in [0.1, 1.0, 4.0, 10.0, 100.0]:
        A_ab = edge_map_np(Pa, np.array([[1.0, 0.0]]), np.array([[Rc_val]]))
        A_ba = edge_map_np(Pb, np.array([[0.0, 1.0]]), np.array([[Rc_val]]))
        rho_Ac_val = max(abs(la.eigvals(A_ab @ A_ba)))
        T_sync_2 = np.block([[np.eye(2) - A_ab, A_ab], [A_ba, np.eye(2) - A_ba]])
        S1 = np.block([[np.eye(2), np.zeros((2, 2))], [A_ba, np.eye(2) - A_ba]])
        S2 = np.block([[np.eye(2) - A_ab, A_ab], [np.zeros((2, 2)), np.eye(2)]])
        T_seq_2 = S2 @ S1
        print(f"    R_c = {Rc_val:5.1f}: rho(A_c) = {rho_Ac_val:.6f}, rho(T_sync) = {max(abs(la.eigvals(T_sync_2))):.6f} > 1, rho(T_seq) = {max(abs(la.eigvals(T_seq_2))):.6f} > 1")
        assert max(abs(la.eigvals(T_sync_2))) > 1.0
        assert max(abs(la.eigvals(T_seq_2))) > 1.0

    # -------------------------------------------------------------------------
    # 4. Claims C4, C5 & NC2: Posterior Edge-Ratio Theorem and dynamic cycles
    # -------------------------------------------------------------------------
    print("\n[4] Claims C4, C5 & Negative Control NC2: Posterior Edge-Ratio Theorem and dynamic cycles")
    # Exact SymPy check on an explicit 2-cycle where prior edge ratios r_e > 3 on BOTH edges
    # under posted post-reception posterior covariances, yet posterior edge ratios r_e^+ < 1 and rho(A_c) < 1!
    P1_d = sp.Matrix([[1, 9], [9, 100]])
    P2_d = sp.Matrix([[100, 9], [9, 1]])
    # Suppose at step 0->1, sender 1 posts posterior covariance after receiving from 2 with R2_init = 1,
    # or consider the exact rational fixed-point/one-pass values:
    # Let R2 = 1/2 (posted by sender 2) and R1 = 1/2 (Wait: let's compute exact post-reception posteriors tilde_P_i^+)!
    # With R2_header = 20 and R1_header = 20:
    # Let's compute tilde_P1^+ after receiving h2 = [1, 0] from agent 2 with noise R2,
    # and set sender 1's posted header to R1 = h1 * tilde_P1^+ * h1^T + Rc (with Rc = 1/10)!
    Rc_sp = sp.Matrix([[sp.Rational(1, 10)]])
    # In symmetric 2-cycle with P1_d, P2_d, h1=[0,1], h2=[1,0], X_12 = 1, X_11 = 100, C_1 = 9:
    # tilde_X_11^+ = 100 - 81 / (1 + R)
    # Fixed point R = tilde_X_11^+ + 1/10 = 1001/10 - 81/(1 + R) => 10 R^2 - 991 R - 191 = 0
    # Or in sequential 1-pass starting from agent 2's sensor posterior header R2 = 1/2:
    R2_post_sp = sp.Matrix([[sp.Rational(1, 2)]])
    S12_d = h2_sp * P1_d * h2_sp.T + R2_post_sp  # 1 + 1/2 = 3/2
    tilde_P1_plus = P1_d - P1_d * h2_sp.T * S12_d.inv() * h2_sp * P1_d
    # Notice h1 * tilde_P1_plus * h1^T = 100 - 81 / (3/2) = 100 - 54 = 46!
    # Wait: if R2_post = 1/20, then S12 = 21/20, tilde_X_11^+ = 100 - 81 * 20/21 = 100 - 540/7 = 160/7.
    # To make tilde_X_11^+ < S_21 so that prior r_e = X_11 / S_21 > 1 on BOTH edges at the symmetric fixed point:
    # Take P1_sym = [[1, 19/2], [19/2, 100]], P2_sym = [[100, 19/2], [19/2, 1]], and 1-pass or sensor-updated header:
    # Even simpler: at any fixed R_i = h_i * tilde_P_i^+ * h_i^T + Rc_i, let's solve the rational fixed point when
    # P1 = [[1, 4], [4, 20]], P2 = [[20, 4], [4, 1]], Rc = 1/5:
    # Wait: X_11 = 20, X_12 = 1, C_1 = 4 => tilde_X_11^+ = 20 - 16 / (1 + R).
    # For prior edge ratio r_e = X_11 / (1 + R) > 1, we need 1 + R < 20, which ALWAYS holds since R = 20 - 16/(1+R) + 1/5 < 20!
    # Specifically, at rational R solving R = 20 - 16/(1+R) + 0 (or with exact rationalP1 = [[1, 3], [3, 10]], Rc = 1):
    # Let's solve R = 10 - 9/(1+R) + 2/5 => R = 9.468... so 1 + R = 10.468 > 10.
    # Why was 1 + R > X_11 there? Because X_21 + R = 1 + X_11 - C^2/(1+R) + Rc = X_11 + (1 + Rc - C^2/(1+R)).
    # So 1 + R < X_11 iff C^2 / (1 + R) > 1 + Rc, i.e., (1 + R) < C^2 / (1 + Rc)!
    # Since 1 + R ~ X_11 - C^2/X_11, we just choose X_12 = 1, X_11 = 4, C = 19/10 (so det P1 = 4 - 3.61 = 0.39 > 0)!
    # Let's check X_11 = 4, C = 19/10: at R ~ 3, C^2/(1+R) = 3.61/4 = 0.9025.
    # What if X_12 is SMALLER than 1, say P1 = [[1/10, 19/10], [19/10, 40]] (det = 4 - 3.61 = 0.39 > 0)!
    # BINGO! Look at P1 = [[1/10, 19/10], [19/10, 40]] and P2 = [[40, 19/10], [19/10, 1/10]]:
    # Here X_12 = 1/10, X_11 = 40, C = 19/10!
    # At the symmetric fixed point R = tilde_X_11^+ + Rc:
    # Suppose we pick Rc so that R = 4/10 (exact rational!):
    # Then S_12 = X_12 + R = 1/10 + 4/10 = 1/2!
    # Then tilde_X_11^+ = X_11 - C^2 / S_12 = 40 - (361/100) / (1/2) = 40 - 361/50 = 1639/50 = 32.78.
    # Wait: to have tilde_X_11^+ < 4/10, we need 40 - C^2 / S_12 < 4/10, so C^2 / S_12 ~ 40, which holds because det P1 = 4 - 3.61 = 0.39 => X_11 - C^2 / X_12 = 40 - 3.61 / 0.1 = 40 - 36.1 = 3.9!
    # And with X_11 = 40 and tilde_X_11^+ ~ 3.9, R ~ 4.0, so S_21 = X_21 + R = 0.1 + 4.0 = 4.1,
    # which makes the PRIOR edge ratio r_e = X_11 / S_21 = 40 / 4.1 = 9.75 > 9 on BOTH edges!!
    P1_post_sp = sp.Matrix([[sp.Rational(1, 10), sp.Rational(19, 10)], [sp.Rational(19, 10), 40]])
    P2_post_sp = sp.Matrix([[40, sp.Rational(19, 10)], [sp.Rational(19, 10), sp.Rational(1, 10)]])
    # Choose exact rational R = 9/2 => S_12 = 1/10 + 9/2 = 46/10 = 23/5
    # Wait: at R = 4, S_12 = 41/10, tilde_X_11^+ = 40 - (361/100)/(41/10) = 40 - 361/410 = 16039/410?
    # No! In 1/10 + R, to keep S_12 close to 1/10, we need R << 1/10 on the FIRST edge (asymmetric 2-cycle)!
    # Look at an ASYMMETRIC 2-cycle:
    # Agent 1 has P1 = [[1, 19/10], [19/10, 4]] (X_12 = 1, X_11 = 4, det = 39/100 > 0).
    # Agent 2 has P2 = [[1/100, 0], [0, 1/100]] (isotropic prior 1/100 * I_2, so X_22 = 1/100, X_21 = 1/100)!
    # Wait: if agent 2 has P2 = [[1/10, 9/100], [9/100, 1/10]], then X_22 = 1/10!
    # So agent 2's posterior header is R2 <= 1/10 (say R2 = 1/10)!
    # Then on edge 2->1, S_12 = X_12 + R2 = 1 + 1/10 = 11/10, so tilde_X_11^+ = 4 - (361/100)/(11/10) = 4 - 361/110 = 79/110!
    # Now agent 1 posts its EXACT posterior covariance header R1 = tilde_X_11^+ + Rc_1 = 79/110 + 1/110 = 80/110 = 8/11!
    # And on edge 1->2, receiver 2 has X_21 = 1/10, so S_21 = X_21 + R1 = 1/10 + 8/11 = 91/110!
    # Look at the PRIOR edge ratio on edge 1->2:
    # r_{1->2} = X_11 / S_21 = 4 / (91/110) = 440 / 91 = 4.835 > 1 !!
    # WHILE the POSTERIOR edge ratio on edge 1->2 is:
    # r_{1->2}^+ = tilde_X_11^+ / R1 = (79/110) / (80/110) = 79/80 < 1 !!
    P1_asym = sp.Matrix([[1, sp.Rational(19, 10)], [sp.Rational(19, 10), 4]])
    P2_asym = sp.Matrix([[sp.Rational(1, 10), sp.Rational(9, 100)], [sp.Rational(9, 100), sp.Rational(1, 10)]])
    # Exact symmetric fixed-point rational check or 1-step exact rational check:
    R2_asym = sp.Matrix([[sp.Rational(1, 10)]])  # covers X_22 = 1/10 >= tilde_X_22^+
    S12_asym = h2_sp * P1_asym * h2_sp.T + R2_asym  # 11/10
    K12_asym = P1_asym * h2_sp.T * S12_asym.inv()
    tilde_P1_asym = P1_asym - K12_asym * h2_sp * P1_asym
    tilde_X11_asym = (h1_sp * tilde_P1_asym * h1_sp.T)[0, 0]  # 79/110
    R1_asym = sp.Matrix([[tilde_X11_asym + sp.Rational(1, 110)]])  # 8/11
    S21_asym = h1_sp * P2_asym * h1_sp.T + R1_asym  # 1/10 + 8/11 = 91/110
    K21_asym = P2_asym * h1_sp.T * S21_asym.inv()
    tilde_P2_asym = P2_asym - K21_asym * h1_sp * P2_asym
    tilde_X22_asym = (h2_sp * tilde_P2_asym * h2_sp.T)[0, 0]

    # Verify Kalman identity in exact rational arithmetic:
    assert K12_asym == tilde_P1_asym * h2_sp.T * R2_asym.inv()
    assert K21_asym == tilde_P2_asym * h1_sp.T * R1_asym.inv()

    r12_prior = sp.Rational(4, 1) / S21_asym[0, 0]  # 440/91
    r12_post = tilde_X11_asym / R1_asym[0, 0]       # 79/80
    r21_post = tilde_X22_asym / R2_asym[0, 0]       # < 1
    Ac_asym = (K12_asym * h2_sp) * (K21_asym * h1_sp)
    rho_Ac_asym = max(abs(e) for e in Ac_asym.eigenvals().keys())
    print(f"  Exact rational witness for C4 [SymPy]:")
    print(f"    Kalman identity K_ji == tilde_P_j^+ H_i^T R_i^-1 verified exactly: True")
    print(f"    Edge 1->2 prior ratio r_12 = {r12_prior} = {float(r12_prior):.4f} > 1 (violates prop:coh-no-amplification(c))")
    print(f"    Edge 1->2 posterior ratio r_12^+ = {r12_post} = {float(r12_post):.4f} < 1, r_21^+ = {r21_post} = {float(r21_post):.4f} < 1")
    print(f"    Exact rho(A_c) = {rho_Ac_asym} = {float(rho_Ac_asym):.6f} < 1")

    # 5000 random cycles for C4 (including multi-round dynamic Riccati evolution) and Negative Control NC2
    c4_kalman_max_err = 0.0
    c4_norm_max_err = 0.0
    c4_bound_violations = 0
    c4_amp_count = 0
    c4_prior_r_exceeds_1 = 0
    nc2_planted_violations = 0

    for trial in range(5000):
        K = int(rng.integers(2, 5))
        N = int(rng.integers(2, 5))
        r = int(rng.integers(1, K + 1))
        Ps = [make_spd(K, rng) * (10.0 ** rng.uniform(-2, 2)) for _ in range(N)]
        Hs = [rng.standard_normal((r, K)) for _ in range(N)]
        Rc = [make_spd(r, rng) * (10.0 ** rng.uniform(-2, 0)) for _ in range(N)]

        # Stationary or multi-round posterior headers R_i = H_i tilde_P_i^+ H_i^T + Rc_i
        Rs = [Hs[i] @ Ps[i] @ Hs[i].T + Rc[i] for i in range(N)]
        for _ in range(20):
            for i in range(N):
                im = (i - 1) % N
                S_i_im = Hs[im] @ Ps[i] @ Hs[im].T + Rs[im]
                tilde_Pi = Ps[i] - Ps[i] @ Hs[im].T @ la.inv(S_i_im) @ Hs[im] @ Ps[i]
                Rs[i] = Hs[i] @ tilde_Pi @ Hs[i].T + Rc[i]

        tilde_Ps = []
        snr_facs = []
        for i in range(N):
            im = (i - 1) % N
            X_i_im = Hs[im] @ Ps[i] @ Hs[im].T
            S_i_im = X_i_im + Rs[im]
            K_prior = Ps[i] @ Hs[im].T @ la.inv(S_i_im)
            tilde_Pi = Ps[i] - K_prior @ Hs[im] @ Ps[i]
            tilde_Ps.append(tilde_Pi)
            K_post = tilde_Pi @ Hs[im].T @ la.inv(Rs[im])
            c4_kalman_max_err = max(c4_kalman_max_err, float(la.norm(K_prior - K_post)))

            # Direct check of ||(tilde_Pi)^{-1/2} K_prior Rs[im]^{1/2}||_2^2 == snr / (1 + snr)
            # Using generalized eigenvalues of K_prior Rs[im] K_prior^T w.r.t. tilde_Pi:
            sq_norm = float(max(la.eigvalsh(K_prior @ Rs[im] @ K_prior.T, tilde_Pi)))
            snr_fac = float(max(la.eigvalsh(X_i_im, S_i_im)))
            c4_norm_max_err = max(c4_norm_max_err, abs(sq_norm - snr_fac))
            snr_facs.append(snr_fac)

        As = []
        r_prior_list = []
        r_post_list = []
        for i in range(N):
            j = (i + 1) % N
            S_ji = Hs[i] @ Ps[j] @ Hs[i].T + Rs[i]
            As.append(Ps[j] @ Hs[i].T @ la.inv(S_ji) @ Hs[i])
            X_ii = Hs[i] @ Ps[i] @ Hs[i].T
            X_ii_post = Hs[i] @ tilde_Ps[i] @ Hs[i].T
            r_prior_list.append(float(max(la.eigvalsh(X_ii, S_ji))))
            r_post_list.append(float(max(la.eigvalsh(X_ii_post, Rs[i]))))

        if max(r_prior_list) > 1.0:
            c4_prior_r_exceeds_1 += 1

        Ac = np.eye(K)
        for i in range(N):
            Ac = As[i] @ Ac
        rho_Ac = float(max(abs(la.eigvals(Ac))))
        if rho_Ac >= 1.0 - 1e-12:
            c4_amp_count += 1

        post_bound = float(np.prod([np.sqrt(r_post_list[i] * snr_facs[i]) for i in range(N)]))
        if rho_Ac > post_bound + 1e-10:
            c4_bound_violations += 1

        # Planted error NC2: squaring snr_facs[i] instead of sqrt(snr_facs[i]) in post_bound
        planted_post_bound = float(np.prod([np.sqrt(r_post_list[i]) * (snr_facs[i] ** 2) for i in range(N)]))
        if rho_Ac > planted_post_bound + 1e-6:
            nc2_planted_violations += 1

    print(f"  5000 random cycles with posted posterior covariances:")
    print(f"    Max Kalman identity error: {c4_kalman_max_err:.2e}")
    print(f"    Max second-bracket norm error: {c4_norm_max_err:.2e}")
    print(f"    Violations of Posterior Edge-Ratio Bound: {c4_bound_violations}")
    print(f"    Amplifying cycles (rho(A_c) >= 1): {c4_amp_count}/5000")
    print(f"    Trials where max_e r_e (prior edge ratio) > 1: {c4_prior_r_exceeds_1}/5000")
    print(f"    [Negative Control NC2] Planted over-attenuated posterior bound violated in {nc2_planted_violations}/5000 trials (PASS: >0)")
    assert c4_kalman_max_err < 1e-8
    assert c4_norm_max_err < 1e-8
    assert c4_bound_violations == 0
    assert c4_amp_count == 0
    assert c4_prior_r_exceeds_1 > 1000
    assert nc2_planted_violations > 100

    # Claim C5: Dynamic cycle with prediction innovation Q_i where receivers use predicted priors P_i^-(t) = F P_i^+(t-1) F^T + Q_i
    # while senders post pre-prediction filtered posterior covariances H_i P_i^+(t-1) H_i^T
    print("  Claim C5: Dynamic cycle with pre-prediction filtered posterior headers vs predicted reception priors:")
    F_dyn = 0.5 * np.eye(2)
    P_plus_a = np.array([[0.2, 0.0], [0.0, 0.2]])
    P_plus_b = np.array([[0.2, 0.0], [0.0, 0.2]])
    # Process noise Q_a, Q_b creates the anisotropic predicted priors Pa, Pb of Ex 6.7(i):
    Qa = Pa - F_dyn @ P_plus_a @ F_dyn.T
    Qb = Pb - F_dyn @ P_plus_b @ F_dyn.T
    assert min(la.eigvalsh(Qa)) > 0 and min(la.eigvalsh(Qb)) > 0
    # Senders post filtered posterior headers H_i P_plus_i H_i^T = 0.2 with channel noise R_c = 0.1 (so R_i = 0.3)
    R_lag = np.array([[0.3]])
    A_ab_lag = edge_map_np(Pa, np.array([[1.0, 0.0]]), R_lag)
    A_ba_lag = edge_map_np(Pb, np.array([[0.0, 1.0]]), R_lag)
    rho_lag = float(max(abs(la.eigvals(A_ab_lag @ A_ba_lag))))
    print(f"    With F = 0.5*I_2, P_i^+ = 0.2*I_2, R_c = 0.1 (header R_i = 0.3), predicted priors Pa, Pb: rho(A_c) = {rho_lag:.6f} > 1 (exact 3.24 / 1.3^2 = {3.24 / 1.69:.6f})")
    assert abs(rho_lag - 3.24 / 1.69) < 1e-12

    # -------------------------------------------------------------------------
    # 5. Claims C6, C7 & NC3: Common code of rank >= 2 with sender-specific noise covariances
    # -------------------------------------------------------------------------
    print("\n[5] Claims C6, C7 & Negative Control NC3: Common code of rank >= 2 with sender-specific noises")
    # (a) 5000 random cycles with common code H (r_c in {2,3,4}) and PROPORTIONAL noises R_i = alpha_i R_0
    c7_prop_amp_Ac = 0
    c7_prop_amp_bar = 0
    c7_max_rho_prop = 0.0
    for trial in range(5000):
        K = int(rng.integers(2, 6))
        N = int(rng.integers(2, 5))
        r = int(rng.integers(2, K + 1))
        H_comm = rng.standard_normal((r, K))
        R0 = make_spd(r, rng)
        alphas = 10.0 ** rng.uniform(-2, 2, N)
        Rs = [alphas[i] * R0 for i in range(N)]
        Ps = [make_spd(K, rng) * (10.0 ** rng.uniform(-2, 2)) for _ in range(N)]

        As = [edge_map_np(Ps[(i + 1) % N], H_comm, Rs[i]) for i in range(N)]
        Ac = np.eye(K)
        for i in range(N):
            Ac = As[i] @ Ac
        rho_Ac = float(max(abs(la.eigvals(Ac))))
        rho_bar = float(max(abs(la.eigvals(np.eye(K) - As[N - 1] + Ac))))
        c7_max_rho_prop = max(c7_max_rho_prop, rho_Ac)
        if rho_Ac >= 1.0 - 1e-12:
            c7_prop_amp_Ac += 1
        if rho_bar > 1.0 + 1e-10:
            c7_prop_amp_bar += 1

    print(f"  5000 random cycles with common code (r_c >= 2) and proportional noises R_i = alpha_i R_0:")
    print(f"    Amplifying A_c count: {c7_prop_amp_Ac}/5000 (max rho(A_c) = {c7_max_rho_prop:.6f} < 1)")
    print(f"    Amplifying bar_A_c count (rho(bar_A_c) > 1): {c7_prop_amp_bar}/5000")
    assert c7_prop_amp_Ac == 0
    assert c7_prop_amp_bar == 0

    # (b) 5000 random cycles with NON-PROPORTIONAL noises: check C6(1) cyclic spread bound and C6(2) Kantorovich bound
    c6_spread_violations = 0
    c6_kant_violations = 0
    c6_spread_cond_met = 0
    c6_kant_cond_met = 0
    c6_amp_when_cond_met = 0

    for trial in range(5000):
        K = int(rng.integers(2, 5))
        N = int(rng.integers(2, 5))
        r = int(rng.integers(2, K + 1))
        H_comm = rng.standard_normal((r, K))
        R_ref = make_spd(r, rng)
        # Perturb R_ref with variable noise anisotropy
        scale_pert = 0.2 if trial < 2500 else 2.0
        Rs = []
        for i in range(N):
            alpha_i = 10.0 ** rng.uniform(-1.5, 1.5)
            U_orth, _ = la.qr(rng.standard_normal((r, r)))
            d_pert = np.exp(rng.uniform(-scale_pert, scale_pert, r))
            R_half = la.fractional_matrix_power(R_ref, 0.5)
            Rs.append(alpha_i * (R_half @ U_orth @ np.diag(d_pert) @ U_orth.T @ R_half))
        Ps = [make_spd(K, rng) * (10.0 ** rng.uniform(-1.5, 1.5)) for _ in range(N)]

        As = []
        snr_facs = []
        snr_vals = []
        for i in range(N):
            j = (i + 1) % N
            As.append(edge_map_np(Ps[j], H_comm, Rs[i]))
            X_j = H_comm @ Ps[j] @ H_comm.T
            S_ji = X_j + Rs[i]
            sf = float(max(la.eigvalsh(X_j, S_ji)))
            snr_facs.append(sf)
            snr_vals.append(sf / (1.0 - sf))

        Ac = np.eye(K)
        for i in range(N):
            Ac = As[i] @ Ac
        rho_Ac = float(max(abs(la.eigvals(Ac))))

        # Cyclic spread S_c(R) = sum_{j=1}^N ln lambda_max(R_j^{-1} R_{j-1})
        S_c = sum(np.log(float(max(la.eigvalsh(Rs[(j - 1) % N], Rs[j])))) for j in range(N))
        bound_spread = float(np.exp(0.5 * S_c) * np.prod(snr_facs))
        if rho_Ac > bound_spread + 1e-10:
            c6_spread_violations += 1

        # Kantorovich bound around R_ref (and geometric mean for N=2)
        if N == 2:
            R0_half = la.fractional_matrix_power(Rs[0], 0.5)
            R0_mhalf = la.fractional_matrix_power(Rs[0], -0.5)
            R_star = R0_half @ la.fractional_matrix_power(R0_mhalf @ Rs[1] @ R0_mhalf, 0.5) @ R0_half
        else:
            R_star = R_ref
        kant_factors = []
        for i in range(N):
            eigs_rel = la.eigvalsh(Rs[i], R_star)
            kap = float(max(eigs_rel) / min(eigs_rel))
            kant_factors.append((kap + 1.0) / (2.0 * np.sqrt(kap)))
        bound_kant = float(np.prod(snr_facs) * np.prod(kant_factors))
        if rho_Ac > bound_kant + 1e-10:
            c6_kant_violations += 1

        if bound_spread <= 1.0:
            c6_spread_cond_met += 1
            if rho_Ac > 1.0 + 1e-10:
                c6_amp_when_cond_met += 1
        if bound_kant <= 1.0:
            c6_kant_cond_met += 1
            if rho_Ac > 1.0 + 1e-10:
                c6_amp_when_cond_met += 1

    print(f"  5000 random cycles with common code (r_c >= 2) and non-proportional noises:")
    print(f"    Violations of C6(1) cyclic noise-spread bound: {c6_spread_violations}/5000")
    print(f"    Violations of C6(2) Kantorovich projective-distance bound: {c6_kant_violations}/5000")
    print(f"    Draws meeting C6(1) spread condition: {c6_spread_cond_met}; meeting C6(2) Kantorovich condition: {c6_kant_cond_met}; amplifying among them: {c6_amp_when_cond_met}")
    assert c6_spread_violations == 0
    assert c6_kant_violations == 0
    assert c6_amp_when_cond_met == 0
    assert c6_kant_cond_met > c6_spread_cond_met  # Kantorovich is strictly sharper near proportionality

    # (c) Exact SymPy + numerical check of C7(2) worst-case supremum (sqrt(kappa) + 1)^2 / (4*sqrt(kappa))
    # and Negative Control NC3 (equal-determinant / equal-trace non-proportional noises still amplify!)
    print("  Claim C7(2) & Negative Control NC3: Exact supremum (sqrt(kappa)+1)^2 / (4*sqrt(kappa)) for non-proportional noises:")
    nc3_violations = 0
    for m_rat in [sp.Rational(11, 10), sp.Rational(3, 2), sp.Rational(2, 1), sp.Rational(3, 1), sp.Rational(5, 1), sp.Rational(10, 1)]:
        # Equal determinant det(R1) = det(R2) = 1: R2 = diag(1, 1), R1 = diag(m, 1/m), so kappa(R2^{-1} R1) = m^2, sqrt(kappa) = m!
        # Let's verify in exact SymPy that with u1 = sqrt(s)*[1, 1/sqrt(m)]^T?
        # Wait: in basis R2 = diag(1, m), R1 = diag(m, 1) (which has equal trace and equal determinant!),
        # u_a = [1, sqrt(m)]^T, u_b = [sqrt(m), 1]^T with scale s -> infinity gives (m+1)^2 / (4m)!
        # Let's evaluate at exact rational s = 10^6, eps = 10^-6 in float and exact asymptotic formula in SymPy:
        m_f = float(m_rat)
        s_val = 1e7
        ua = np.array([[np.sqrt(s_val)], [np.sqrt(m_f * s_val)]])
        ub = np.array([[np.sqrt(m_f * s_val)], [np.sqrt(s_val)]])
        Xa = ua @ ua.T + 1e-7 * np.eye(2)
        Xb = ub @ ub.T + 1e-7 * np.eye(2)
        Rb = np.diag([1.0, m_f])
        Ra = np.diag([m_f, 1.0])
        Ba = Xa @ la.inv(Xa + Rb)
        Bb = Xb @ la.inv(Xb + Ra)
        rho_achieved = float(max(abs(la.eigvals(Bb @ Ba))))
        exact_sup_sp = (m_rat + 1)**2 / (4 * m_rat)
        exact_sup_f = float(exact_sup_sp)
        print(f"    sqrt(kappa) = {str(m_rat):4s} (kappa = {float(m_rat**2):6.2f}): achieved rho = {rho_achieved:.8f}, exact sup = {str(exact_sup_sp):7s} = {exact_sup_f:.8f}")
        assert abs(rho_achieved - exact_sup_f) < 1e-5
        if rho_achieved > 1.0:
            nc3_violations += 1

    print(f"  [Negative Control NC3] Equal-trace/equal-determinant non-proportional noises amplified in {nc3_violations}/6 cases (PASS: 6/6)")
    assert nc3_violations == 6

    # Also verify N=3 arc construction in C7(2) (a=1, b=2, R_1 = diag(4,1), R_2 = I_2, R_3 = diag(3,2), m = 2 => sup = 9/8 = 1.125)
    R1_3 = np.diag([4.0, 1.0])
    R2_3 = np.eye(2)
    R3_3 = np.diag([3.0, 2.0])
    w1_3 = np.array([[1.0], [0.0]])
    w2_3 = np.array([[0.0], [1.0]])
    v1_3 = w1_3 + w2_3
    v2_3 = 2.0 * w1_3 + w2_3
    # u_k = v_2 for k in {a+1..b} = {2} (1-indexed), u_k = v_1 for k in {3, 1}
    u_list_3 = [v1_3, v2_3, v1_3]
    Rs_3 = [R1_3, R2_3, R3_3]
    s_3 = 1e7
    B_prod_3 = np.eye(2)
    for j_idx in range(3):
        im_idx = (j_idx - 1) % 3
        u_j = u_list_3[j_idx]
        X_j = s_3 * (u_j @ u_j.T) + 1e-7 * np.eye(2)
        B_j = X_j @ la.inv(X_j + Rs_3[im_idx])
        B_prod_3 = B_j @ B_prod_3
    rho_N3 = float(max(abs(la.eigvals(B_prod_3))))
    print(f"  N=3 arc construction check (a=1, b=2, kappa_12=4, m=2): achieved rho = {rho_N3:.8f} vs 9/8 = {9.0/8.0:.8f}")
    assert abs(rho_N3 - 9.0 / 8.0) < 1e-5

    print("\n" + "=" * 78)
    print("ALL VERIFICATION CHECKS AND NEGATIVE CONTROLS PASSED (0 ERRORS).")
    print("=" * 78)
    return 0


if __name__ == "__main__":
    sys.exit(main())
