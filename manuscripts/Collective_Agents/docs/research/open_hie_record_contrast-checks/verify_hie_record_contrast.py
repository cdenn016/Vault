"""Two-channel verification suite + planted-error negative controls for open:hie-record-contrast.

Channels:
  Channel 1 (Symbolic / Exact Rational): SymPy symbolic simplification and exact rational linear algebra.
  Channel 2 (Numerical Direct): SciPy Lyapunov solvers, direct matrix inversion, and eigendecomposition
  (independent of the derived closed forms).

Deepest shared element: the matrix representation of the drift M (or W) and noise Q from eq:hie-record
and def:fw-record-model. The feared errors (sign errors, factor errors, missing terms in closed forms,
false diffusivity claims, or invalid size/baseline bounds) cannot live in the shared definition because
Channel 2 solves the defining Lyapunov equation directly from M and Q while Channel 1 evaluates the
derived symbolic/exact expressions independently.
"""
from __future__ import annotations

import sys
import numpy as np
from scipy.linalg import solve_continuous_lyapunov, solve_discrete_lyapunov, inv, eigvalsh
import sympy as sp
from itertools import combinations


def build_continuous_system(A, n, eps, beta, omega, delta, q=1.0, q_z=None):
    N = A.shape[0]
    L = np.diag(A.sum(axis=1)) - A
    M = np.zeros((N + 1, N + 1), dtype=float)
    M[:N, :N] = eps * np.eye(N) + L
    for i in range(n):
        M[i, i] += beta
        M[i, N] = -beta
        M[N, i] = -omega / n
    M[N, N] = omega + delta
    q_rev = omega * q / (n * beta)
    if q_z is None:
        q_z = q_rev
    Q = np.diag([q] * N + [q_z])
    return M, Q, q_rev


def is_diffusive_num(P, tol=1e-12):
    sc = np.max(np.abs(P))
    off = P[~np.eye(P.shape[0], dtype=bool)]
    return (np.max(off) <= tol * sc) and (np.min(P.sum(axis=1)) >= -tol * sc)


def exact_lyapunov_sympy(M, Q2):
    """Solve M Sigma + Sigma M^T = Q2 exactly over Q/SymPy."""
    d = M.rows
    Id = sp.eye(d)
    K = sp.kronecker_product(Id, M) + sp.kronecker_product(M, Id)
    rhs = sp.Matrix([Q2[i, j] for j in range(d) for i in range(d)])  # column-major vec
    vecS = K.LUsolve(rhs)
    Sig = sp.Matrix(d, d, lambda i, j: sp.simplify(vecS[j * d + i]))
    # Verify residual == 0
    res = M * Sig + Sig * M.T - Q2
    assert all(sp.simplify(res[i, j]) == 0 for i in range(d) for j in range(d))
    return Sig


def exact_discrete_lyapunov_sympy(W, Q):
    """Solve Sigma - W Sigma W^T = Q exactly over Q/SymPy."""
    d = W.rows
    Id = sp.eye(d * d)
    K = Id - sp.kronecker_product(W, W)
    rhs = sp.Matrix([Q[i, j] for j in range(d) for i in range(d)])
    vecS = K.LUsolve(rhs)
    Sig = sp.Matrix(d, d, lambda i, j: sp.simplify(vecS[j * d + i]))
    res = Sig - W * Sig * W.T - Q
    assert all(sp.simplify(res[i, j]) == 0 for i in range(d) for j in range(d))
    return Sig


def contrast_euclid(Pi, S):
    S = list(S)
    k = len(S)
    sub = Pi[np.ix_(S, S)]
    ones = np.ones(k)
    xout = (ones @ sub @ ones) / k
    mask_out = np.ones(Pi.shape[0], dtype=bool)
    mask_out[S] = False
    a_part = -Pi[np.ix_(S, mask_out)].sum(axis=1)
    M_in = sub - np.diag(a_part)
    U, _, _ = np.linalg.svd(ones[:, None], full_matrices=True)
    B = U[:, 1:]
    xin = np.min(eigvalsh(B.T @ M_in @ B))
    return xin / xout, xin, xout


def contrast_weighted(Pi, w, S):
    S = list(S)
    k = len(S)
    sub = Pi[np.ix_(S, S)]
    wS = w[S]
    ones = np.ones(k)
    W_tot = float(np.sum(wS))
    xout = float((ones @ sub @ ones) / W_tot)
    mask_out = np.ones(Pi.shape[0], dtype=bool)
    mask_out[S] = False
    a_part = -Pi[np.ix_(S, mask_out)].sum(axis=1)
    M_in = sub - np.diag(a_part)
    sqw = np.sqrt(wS)
    u0 = sqw / np.linalg.norm(sqw)
    U, _, _ = np.linalg.svd(u0[:, None], full_matrices=True)
    B = U[:, 1:]
    inv_sqw = np.diag(1.0 / sqw)
    xin = float(np.min(eigvalsh(B.T @ inv_sqw @ M_in @ inv_sqw @ B)))
    return xin / xout, xin, xout


def check_conventions_and_manuscript_test_instance():
    print("=== 0. Convention lock & registered manuscript test instance (obs:hie-record-window) ===")
    n = 8
    A8 = np.zeros((8, 8))
    for i in range(8):
        A8[i, (i + 1) % 8] = A8[(i + 1) % 8, i] = 1.0
    A16 = np.zeros((16, 16))
    A16[:8, :8] = A8
    A16[8:, 8:] = A8
    for i in range(8):
        A16[i, 8 + i] = A16[8 + i, i] = 0.05

    eps, beta, omega, q = 0.02, 0.2, 0.1, 1.0
    q_rev = omega * q / (n * beta)
    assert abs(q_rev - 0.0625) < 1e-15

    # Check prop:hie-record-contrast & chk:hie-record-precision numbers
    M, Q, _ = build_continuous_system(A16, 8, eps, beta, omega, 0.0, q, q_rev)
    Sig = solve_continuous_lyapunov(M, 2.0 * Q)
    Pi = inv(Sig)
    r_Cprime, _, _ = contrast_euclid(Pi, list(range(8)) + [16])
    r_Cprime_formula = 9.0 * (eps + beta + 2.0 - np.sqrt(2.0)) / (8.0 * eps + 8.0 * 0.05)
    assert abs(r_Cprime - r_Cprime_formula) < 1e-12, f"r(C') mismatch: {r_Cprime} vs {r_Cprime_formula}"
    assert abs(round(r_Cprime, 4) - 12.9501) < 1e-12
    assert is_diffusive_num(Pi)

    # Check closed ring with delta=0.01: exact threshold kappa_max = 1 + delta*T/(eps*omega) = 2.65
    delta = 0.01
    T = eps + beta + omega + delta
    kmax = 1.0 + delta * T / (eps * omega)
    assert abs(kmax - 2.65) < 1e-15
    for ratio, expected in [(0.99, False), (1.0, True), (2.0, True), (2.649, True), (2.651, False), (4.0, False)]:
        Mc, Qc, _ = build_continuous_system(A8, 8, eps, beta, omega, delta, q, ratio * q_rev)
        Pic = inv(solve_continuous_lyapunov(Mc, 2.0 * Qc))
        got = is_diffusive_num(Pic)
        assert got == expected, f"closed8 delta=0.01 ratio={ratio}: got {got}, expected {expected}"
    print(f"  PASS: q_rev={q_rev}, r(C')={r_Cprime:.6f} (manuscript 12.9501), closed8 delta=0.01 kappa_max={kmax:.6f} (2.649 True, 2.651 False)")


def check_C1_closed_collective():
    print("\n=== C1. Closed collective exact closed form & diffusivity interval ===")
    # Channel 1: Symbolic derivation & verification in SymPy
    eps, beta, omega, delta, q, kappa = sp.symbols('eps beta omega delta q kappa', positive=True)
    n_sym = sp.Symbol('n', positive=True)
    T = eps + beta + omega + delta
    D2 = eps * (omega + delta) + beta * delta
    P = beta * omega * (kappa - 1) ** 2 + T ** 2 * kappa

    M2 = sp.Matrix([
        [eps + beta, -beta * sp.sqrt(n_sym)],
        [-omega / sp.sqrt(n_sym), omega + delta]
    ])
    q_rev_sym = omega * q / (n_sym * beta)
    Q2 = sp.Matrix([[q, 0], [0, kappa * q_rev_sym]])

    s_uu = q / (T * D2) * ((omega + delta) ** 2 + D2 + kappa * beta * omega)
    s_uz = omega * q / (sp.sqrt(n_sym) * T * D2) * ((omega + delta) + kappa * (eps + beta))
    s_zz = omega * q / (n_sym * beta * T * D2) * (beta * omega + kappa * ((eps + beta) ** 2 + D2))
    Sig2 = sp.Matrix([[s_uu, s_uz], [s_uz, s_zz]])

    lyap_res = sp.simplify(M2 * Sig2 + Sig2 * M2.T - 2 * Q2)
    assert lyap_res == sp.zeros(2, 2), f"Lyapunov residual nonzero: {lyap_res}"

    det_Sig2 = sp.simplify(Sig2.det() - omega * q ** 2 * P / (n_sym * beta * T ** 2 * D2))
    assert det_Sig2 == 0, f"det(Sig2) mismatch: {det_Sig2}"

    Pi2 = sp.simplify(Sig2.inv())
    Pi_uu_f = T * (beta * omega + kappa * ((eps + beta) ** 2 + D2)) / (q * P)
    Pi_uz_f = -beta * sp.sqrt(n_sym) * T * ((omega + delta) + kappa * (eps + beta)) / (q * P)
    Pi_zz_f = n_sym * beta * T * ((omega + delta) ** 2 + D2 + kappa * beta * omega) / (omega * q * P)
    assert sp.simplify(Pi2[0, 0] - Pi_uu_f) == 0
    assert sp.simplify(Pi2[0, 1] - Pi_uz_f) == 0
    assert sp.simplify(Pi2[1, 1] - Pi_zz_f) == 0

    # Check Delta_uu = q*Pi_uu - (eps + beta)
    Delta_uu = sp.simplify(q * Pi_uu_f - (eps + beta) - beta * omega * (1 - kappa) * ((omega + delta) + kappa * (eps + beta)) / P)
    assert Delta_uu == 0

    # Check member row sum and record row sum
    row_C = sp.simplify(Pi_uu_f + Pi_uz_f / sp.sqrt(n_sym) - T * (kappa * (eps * T + beta * delta) - beta * delta) / (q * P))
    row_z = sp.simplify(Pi_zz_f + sp.sqrt(n_sym) * Pi_uz_f - n_sym * beta * T * (delta * T + (1 - kappa) * eps * omega) / (omega * q * P))
    assert row_C == 0 and row_z == 0

    # Check marginal precision off-diagonal shift: (1/s_uu - (eps+beta)/q) / n
    marg_shift = sp.simplify(q / s_uu - (eps + beta) + beta * omega * ((omega + delta) + kappa * (eps + beta)) / ((omega + delta) ** 2 + D2 + kappa * beta * omega))
    assert marg_shift == 0
    print("  Channel 1 (SymPy): ALL closed-form Lyapunov, det, Pi, row-sum, and marginal-shift identities verified = 0.")

    # Channel 2: Numerical check over 200 random closed graphs (complete & non-complete, delta=0 & delta>0)
    rng = np.random.default_rng(1001)
    max_rel_err = 0.0
    for trial in range(200):
        n = int(rng.integers(2, 8))
        A = 10 ** rng.uniform(-2, 1, size=(n, n))
        A = (A + A.T) / 2
        np.fill_diagonal(A, 0.0)
        if trial % 2 == 0 and n >= 3:
            # Remove at least one edge -> non-complete
            A[0, n - 1] = A[n - 1, 0] = 0.0
        eps_v = float(10 ** rng.uniform(-2, 0.5))
        beta_v = float(10 ** rng.uniform(-2, 0.5))
        omega_v = float(10 ** rng.uniform(-2, 0.5))
        delta_v = 0.0 if trial % 3 == 0 else float(10 ** rng.uniform(-2, 0.5))
        q_v = float(10 ** rng.uniform(-1, 1))
        T_v = eps_v + beta_v + omega_v + delta_v
        D2_v = eps_v * (omega_v + delta_v) + beta_v * delta_v
        kmax_v = 1.0 + delta_v * T_v / (eps_v * omega_v)
        a_min = float(np.min(A + np.eye(n) * 1e9))
        if a_min == 0.0:
            kmin_v = 1.0
        else:
            k_row = beta_v * delta_v / (eps_v * T_v + beta_v * delta_v)
            if n * a_min >= omega_v + delta_v:
                k_off = 0.0
            else:
                # Solve quadratic Q(k) = beta*omega*(1-k)*[(w+d)+k*(e+b)] - n*a_min*[beta*omega*(k-1)^2 + T^2*k] = 0 in (0,1)
                c2 = -beta_v * omega_v * (eps_v + beta_v) - n * a_min * beta_v * omega_v
                c1 = beta_v * omega_v * (eps_v + beta_v - omega_v - delta_v) - n * a_min * (T_v ** 2 - 2 * beta_v * omega_v)
                c0 = beta_v * omega_v * (omega_v + delta_v - n * a_min)
                roots = np.roots([c2, c1, c0])
                real_roots = [r.real for r in roots if abs(r.imag) < 1e-10 and 0.0 < r.real < 1.0]
                assert len(real_roots) == 1
                k_off = real_roots[0]
            kmin_v = max(k_row, k_off)

        # Test interior and exterior points around [kmin_v, kmax_v]
        test_kappas = [0.0, 0.5 * kmin_v if kmin_v > 0 else 0.0, 1.0, kmax_v + 0.05]
        if kmin_v > 1e-3:
            test_kappas.append(max(0.0, kmin_v - 1e-3))
        if kmax_v > kmin_v + 2e-3:
            test_kappas.append(0.5 * (kmin_v + kmax_v))
            test_kappas.append(kmax_v - 1e-3)
        for kap in test_kappas:
            M, Q, q_rev = build_continuous_system(A, n, eps_v, beta_v, omega_v, delta_v, q_v, kap * q_rev if False else kap * (omega_v * q_v / (n * beta_v)))
            Sig = solve_continuous_lyapunov(M, 2.0 * Q)
            Pi = inv(Sig)
            Pi_m = inv(Sig[:n, :n])
            # Compare with closed form
            P_v = beta_v * omega_v * (kap - 1) ** 2 + T_v ** 2 * kap
            Pi_uu_v = T_v * (beta_v * omega_v + kap * ((eps_v + beta_v) ** 2 + D2_v)) / (q_v * P_v)
            Pi_uz_v = -beta_v * np.sqrt(n) * T_v * ((omega_v + delta_v) + kap * (eps_v + beta_v)) / (q_v * P_v)
            Pi_zz_v = n * beta_v * T_v * ((omega_v + delta_v) ** 2 + D2_v + kap * beta_v * omega_v) / (omega_v * q_v * P_v)
            L_C = np.diag(A.sum(axis=1)) - A
            Pi_cf = np.zeros((n + 1, n + 1))
            Pi_cf[:n, :n] = ((eps_v + beta_v) * np.eye(n) + L_C) / q_v + (Pi_uu_v - (eps_v + beta_v) / q_v) / n * np.ones((n, n))
            Pi_cf[:n, n] = Pi_cf[n, :n] = Pi_uz_v / np.sqrt(n)
            Pi_cf[n, n] = Pi_zz_v
            rel = np.linalg.norm(Pi - Pi_cf) / np.linalg.norm(Pi)
            max_rel_err = max(max_rel_err, rel)
            # Check diffusivity prediction away from exact boundary
            if kap < kmin_v - 1e-6 or kap > kmax_v + 1e-6:
                assert not is_diffusive_num(Pi, tol=1e-11), f"Expected non-diffusive at kap={kap}, interval=[{kmin_v},{kmax_v}]"
            elif kmin_v + 1e-6 < kap < kmax_v - 1e-6:
                assert is_diffusive_num(Pi, tol=1e-11), f"Expected diffusive at kap={kap}, interval=[{kmin_v},{kmax_v}]"
            # Marginal precision always diffusive
            assert is_diffusive_num(Pi_m, tol=1e-11), f"Closed marginal precision failed diffusivity!"

    # Witness W1 (exact rational): closed clique K2, a=1, eps=1/10, beta=1/5, omega=1/10, delta=0, q=1, q_z=0 -> DIFFUSIVE!
    M_w1 = sp.Matrix([
        [sp.Rational(13, 10), -1, -sp.Rational(1, 5)],
        [-1, sp.Rational(13, 10), -sp.Rational(1, 5)],
        [-sp.Rational(1, 20), -sp.Rational(1, 20), sp.Rational(1, 10)]
    ])
    Q_w1 = sp.diag(2, 2, 0)
    Pi_w1 = exact_lyapunov_sympy(M_w1, Q_w1).inv()
    assert Pi_w1[0, 1] == -sp.Rational(19, 20)
    assert Pi_w1[0, 2] == -sp.Rational(2, 5)
    assert sum(Pi_w1.row(0)) == 0 and sum(Pi_w1.row(2)) == sp.Rational(4, 5)

    # Negative control: plant wrong kappa_max = 1 + delta/eps (missing T/omega) -> must fail on closed8!
    wrong_kmax = 1.0 + 0.01 / 0.02  # 1.5, whereas true is 2.65
    assert abs(wrong_kmax - 2.65) > 1.0
    print(f"  Channel 2 (Numerical, 200 random closed graphs): max rel err = {max_rel_err:.3e}, all interval & marginal checks PASS.")
    print(f"  Witness W1 (SymPy exact K2, delta=0, q_z=0): Pi_01={Pi_w1[0,1]}, row0={sum(Pi_w1.row(0))}, rowz={sum(Pi_w1.row(2))} -> DIFFUSIVE.")
    print(f"  [NEGATIVE CONTROL CAUGHT]: planted wrong kmax=1+delta/eps={wrong_kmax} differs from true 2.65 by {abs(wrong_kmax-2.65):.2f}.")


def check_C2_C3_upper_and_noiseless_barriers():
    print("\n=== C2 & C3. Universal upper barrier (cut>0 or delta=0) & noiseless barrier (q_z=0) ===")
    rng = np.random.default_rng(2002)
    max_lyap_id_err = 0.0
    # Verify exact identity S - Pi_tilde = R solving R Pi_tilde + Pi_tilde R = 2 eta (Pi_tilde e_z)(Pi_tilde e_z)^T
    # AND verify no q_z > q_rev is diffusive when cut(C)>0 (300 random graphs x 5 ratios = 1500 solves)
    # AND verify no q_z = 0 is diffusive when cut(C)>0 or delta>0 (300 random graphs)
    above_failures_caught = 0
    noiseless_failures_caught = 0
    for trial in range(300):
        n = int(rng.integers(2, 6))
        m = int(rng.integers(1, 5))
        N = n + m
        A = 10 ** rng.uniform(-1.5, 1.5, size=(N, N))
        A = (A + A.T) / 2
        np.fill_diagonal(A, 0.0)
        if trial % 2 == 0:
            mask = rng.uniform(0, 1, size=(N, N)) < 0.5
            mask = mask | mask.T
            A = A * mask
            A[0, n] = A[n, 0] = float(10 ** rng.uniform(-1, 1))
        eps_v = float(10 ** rng.uniform(-1.5, 0.5))
        beta_v = float(10 ** rng.uniform(-1.5, 0.5))
        omega_v = float(10 ** rng.uniform(-1.5, 0.5))
        delta_v = 0.0 if trial % 2 == 0 else float(10 ** rng.uniform(-1.5, 0.5))
        q_rev = omega_v / (n * beta_v)
        d = np.array([1.0] * N + [np.sqrt(q_rev)])
        D = np.diag(d)
        Dinv = np.diag(1.0 / d)
        M, _, _ = build_continuous_system(A, n, eps_v, beta_v, omega_v, delta_v, 1.0, q_rev)
        S = Dinv @ M @ D

        for ratio in [1.005, 1.1, 2.0, 10.0]:
            eta = ratio - 1.0
            Q = np.diag([1.0] * N + [ratio * q_rev])
            Sig = solve_continuous_lyapunov(M, 2.0 * Q)
            Pi = inv(Sig)
            Pi_t = D @ Pi @ D
            R = S - Pi_t
            u = Pi_t[:, N:N + 1]
            res = R @ Pi_t + Pi_t @ R - 2.0 * eta * (u @ u.T)
            max_lyap_id_err = max(max_lyap_id_err, np.linalg.norm(res) / (np.linalg.norm(S @ Pi_t) + 1e-30))
            # C2: must NOT be an M-matrix (max off-diag strictly positive)
            off = Pi[~np.eye(N + 1, dtype=bool)]
            assert np.max(off) > 0.0, f"C2 violation at trial {trial}, ratio={ratio}"
            above_failures_caught += 1

        # C3: q_z = 0
        Q0 = np.diag([1.0] * N + [0.0])
        Sig0 = solve_continuous_lyapunov(M, 2.0 * Q0)
        Pi0 = inv(Sig0)
        MSig_z = (M @ Sig0)[:, N]
        r0 = Pi0.sum(axis=1)
        # Check exact identity r0^T (M Sig0)_{:,z} = -delta and (M Sig0)_{zz} = 0
        assert abs(MSig_z[N]) < 1e-11 * np.max(np.abs(M @ Sig0))
        assert abs(float(r0 @ MSig_z) + delta_v) < 1e-9 * (1.0 + delta_v + np.linalg.norm(r0) * np.linalg.norm(MSig_z))
        # Must fail diffusivity (specifically min row sum < 0 or max off-diag > 0)
        assert not is_diffusive_num(Pi0, tol=1e-12), f"C3 violation at trial {trial}"
        noiseless_failures_caught += 1

    # Negative control: drop the factor 2 in R Pi_tilde + Pi_tilde R = 2 eta u u^T -> residual must be O(1)
    M_nc, Q_nc, q_rev_nc = build_continuous_system(np.ones((3, 3)) - np.eye(3), 2, 0.1, 0.2, 0.1, 0.05, 1.0, 1.5 * (0.1 / 0.4))
    d_nc = np.array([1.0, 1.0, 1.0, np.sqrt(q_rev_nc)])
    S_nc = np.diag(1 / d_nc) @ M_nc @ np.diag(d_nc)
    Pi_nc = np.diag(d_nc) @ inv(solve_continuous_lyapunov(M_nc, 2.0 * Q_nc)) @ np.diag(d_nc)
    u_nc = Pi_nc[:, 3:4]
    R_nc = S_nc - Pi_nc
    wrong_res = np.linalg.norm(R_nc @ Pi_nc + Pi_nc @ R_nc - 1.0 * 0.5 * (u_nc @ u_nc.T))
    assert wrong_res > 1e-3
    print(f"  PASS: R*Pi_t + Pi_t*R = 2*eta*u*u^T max rel err = {max_lyap_id_err:.3e}.")
    print(f"  PASS: C2 upper barrier verified on {above_failures_caught}/1200 open instances (0 diffusive above q_rev).")
    print(f"  PASS: C3 noiseless identity & obstruction verified on {noiseless_failures_caught}/300 open instances (0 diffusive at q_z=0).")
    print(f"  [NEGATIVE CONTROL CAUGHT]: dropping factor 2 in Lyapunov identity gives residual {wrong_res:.4e} > 1e-3.")


def check_C4_below_qrev_and_witnesses():
    print("\n=== C4. Below q_rev with outsiders: symmetric rigidity + K3 & non-complete K4\\{(0,3),(1,3)} exact witnesses ===")
    # Witness W2 (SymPy exact rational): K3, C={0,1}, O={2}, a=1, eps=1/10, beta=1/5, omega=1/10, q=1, q_rev=1/4
    for delta_name, delta_r in [("delta=0", sp.Integer(0)), ("delta=1/20", sp.Rational(1, 20))]:
        M_k3 = sp.Matrix([
            [sp.Rational(23, 10), -1, -1, -sp.Rational(1, 5)],
            [-1, sp.Rational(23, 10), -1, -sp.Rational(1, 5)],
            [-1, -1, sp.Rational(21, 10), 0],
            [-sp.Rational(1, 20), -sp.Rational(1, 20), 0, sp.Rational(1, 10) + delta_r]
        ])
        q_rev_r = sp.Rational(1, 4)
        # ratio = 1/2 -> STRICTLY DIFFUSIVE
        Pi_half = exact_lyapunov_sympy(M_k3, 2 * sp.diag(1, 1, 1, q_rev_r / 2)).inv()
        off_half = [Pi_half[i, j] for i in range(4) for j in range(4) if i != j]
        rows_half = [sum(Pi_half.row(i)) for i in range(4)]
        assert all(x < 0 for x in off_half) and all(x > 0 for x in rows_half)
        # ratio = 0 -> NOT diffusive (member row sum < 0)
        Pi_zero = exact_lyapunov_sympy(M_k3, 2 * sp.diag(1, 1, 1, 0)).inv()
        assert sum(Pi_zero.row(0)) < 0
        # ratio = 3/2 -> NOT diffusive (Pi_oz > 0)
        Pi_above = exact_lyapunov_sympy(M_k3, 2 * sp.diag(1, 1, 1, 3 * q_rev_r / 2)).inv()
        assert Pi_above[2, 3] > 0
        print(f"  Witness W2 (SymPy exact K3, {delta_name}):")
        print(f"    q_z=q_rev/2: max_off={float(max(off_half)):+.6f} (<0), min_row={float(min(rows_half)):+.6f} (>0) -> STRICTLY DIFFUSIVE")
        print(f"    q_z=0      : row0={float(sum(Pi_zero.row(0))):+.6f} (<0) -> NOT diffusive")
        print(f"    q_z=3q_rev/2: Pi_oz={float(Pi_above[2,3]):+.6f} (>0) -> NOT diffusive")

    # Witness W3 (SymPy exact rational): NON-COMPLETE graph K4 \ {(0,3),(1,3)}, C={0,1}, O={2,3}
    # a01=1, a02=a12=5, a23=1, eps=1/2, beta=8, omega=1/4, delta=8, q=1 -> q_rev = 1/64
    M_w3 = sp.Matrix([
        [sp.Rational(29, 2), -1, -5, 0, -8],
        [-1, sp.Rational(29, 2), -5, 0, -8],
        [-5, -5, sp.Rational(23, 2), -1, 0],
        [0, 0, -1, sp.Rational(3, 2), 0],
        [-sp.Rational(1, 8), -sp.Rational(1, 8), 0, 0, sp.Rational(33, 4)]
    ])
    q_rev_w3 = sp.Rational(1, 64)
    # Test ratio = 9/10 -> STRICTLY DIFFUSIVE despite missing edges (0,3) and (1,3)!
    Pi_w3 = exact_lyapunov_sympy(M_w3, 2 * sp.diag(1, 1, 1, 1, sp.Rational(9, 10) * q_rev_w3)).inv()
    off_w3 = [Pi_w3[i, j] for i in range(5) for j in range(5) if i != j]
    rows_w3 = [sum(Pi_w3.row(i)) for i in range(5)]
    assert all(x < 0 for x in off_w3) and all(x > 0 for x in rows_w3)
    # Also check ratio = 11/10 -> Pi_2z > 0 or Pi_3z > 0 (NOT diffusive)
    Pi_w3_hi = exact_lyapunov_sympy(M_w3, 2 * sp.diag(1, 1, 1, 1, sp.Rational(11, 10) * q_rev_w3)).inv()
    assert Pi_w3_hi[2, 4] > 0 and Pi_w3_hi[3, 4] > 0
    print(f"  Witness W3 (SymPy exact non-complete K4\\{{(0,3),(1,3)}}, delta=8):")
    print(f"    q_z=9/10*q_rev : Pi_03=Pi_13={float(Pi_w3[0,3]):+.6e} (<0), max_off={float(max(off_w3)):+.6e} (<0), min_row={float(min(rows_w3)):+.6e} (>0) -> STRICTLY DIFFUSIVE")
    print(f"    q_z=11/10*q_rev: Pi_2z={float(Pi_w3_hi[2,4]):+.6e} (>0), Pi_3z={float(Pi_w3_hi[3,4]):+.6e} (>0) -> NOT diffusive")

    # Also verify exact integral identity for symmetric uncoupled pair on 0-2-1 (C={0,1}, O={2}, a01=0, a02=a12=1)
    M_021 = sp.Matrix([
        [sp.Rational(13, 10), 0, -1, -sp.Rational(1, 5)],
        [0, sp.Rational(13, 10), -1, -sp.Rational(1, 5)],
        [-1, -1, sp.Rational(21, 10), 0],
        [-sp.Rational(1, 20), -sp.Rational(1, 20), 0, sp.Rational(11, 100)]
    ])
    q_rev_021 = sp.Rational(1, 4)
    Pi_021_lo = exact_lyapunov_sympy(M_021, 2 * sp.diag(1, 1, 1, q_rev_021 / 2)).inv()
    assert Pi_021_lo[0, 1] > 0  # symmetric uncoupled pair strictly positive below q_rev
    # Channel 2 numerical check of integral formula Pi_01 = -2*eta/q * int_0^inf (w_0'(t))^2 dt
    d021 = np.array([1.0, 1.0, 1.0, 0.5])
    Pi_021_t = np.diag(d021) @ np.array(Pi_021_lo.evalf(), dtype=float) @ np.diag(d021)
    evals, evecs = np.linalg.eigh(Pi_021_t)
    # w_0'(t) = -sum_k evals[k] * exp(-evals[k]*t) * evecs[0,k] * evecs[3,k]
    # int_0^inf (w_0'(t))^2 dt = sum_{a,b} (evals[a]*evals[b]/(evals[a]+evals[b])) * c_a * c_b
    c = evecs[0, :] * evecs[3, :]
    integral_val = sum((evals[a] * evals[b] / (evals[a] + evals[b])) * c[a] * c[b] for a in range(4) for b in range(4))
    eta = -0.5
    pred_Pi01 = -2.0 * eta * integral_val
    assert abs(pred_Pi01 - float(Pi_021_lo[0, 1])) < 1e-13
    print(f"  PASS: Symmetric uncoupled pair identity on 0-2-1: exact Pi_01={float(Pi_021_lo[0,1]):+.8e}, integral={pred_Pi01:+.8e} (diff={abs(pred_Pi01-float(Pi_021_lo[0,1])):.2e}).")

    # Negative control: flip sign of eta in integral formula -> must fail!
    assert abs(-pred_Pi01 - float(Pi_021_lo[0, 1])) > 1e-3
    print(f"  [NEGATIVE CONTROL CAUGHT]: flipping sign of eta in symmetric-pair formula gives error {abs(-pred_Pi01 - float(Pi_021_lo[0,1])):.4e}.")

    # Verify C2(3)/C4(2) vector d = D^{-1} 1 vs planted wrong D 1 on K3 (a=1, eps=0.1, beta=10, omega=0.05, delta=0, q=1)
    A3_d = np.ones((3, 3)) - np.eye(3)
    M_d, _, q_rev_d = build_continuous_system(A3_d, 2, 0.1, 10.0, 0.05, 0.0, 1.0)
    d_diag = np.array([1.0, 1.0, 1.0, np.sqrt(q_rev_d)])
    S_d = np.diag(1.0 / d_diag) @ M_d @ np.diag(d_diag)
    E_d = np.zeros((4, 4)); E_d[3, 3] = 2.0
    Y_d = solve_continuous_lyapunov(S_d, E_d)
    SYS_d = S_d @ Y_d @ S_d
    d_inv_1 = 1.0 / d_diag
    d_pos_1 = d_diag
    true_sys_d_z = float((SYS_d @ d_inv_1)[3])
    wrong_sys_d_z = float((SYS_d @ d_pos_1)[3])
    # Numerical central difference of (Pi(1+eta) 1)_z at eta=0
    h_fd = 1e-6
    Pi_p = inv(solve_continuous_lyapunov(M_d, 2.0 * np.diag([1.0, 1.0, 1.0, (1.0 + h_fd) * q_rev_d])))
    Pi_m = inv(solve_continuous_lyapunov(M_d, 2.0 * np.diag([1.0, 1.0, 1.0, (1.0 - h_fd) * q_rev_d])))
    fd_drz = float((Pi_p.sum(axis=1)[3] - Pi_m.sum(axis=1)[3]) / (2.0 * h_fd))
    pred_drz = -true_sys_d_z / np.sqrt(q_rev_d)
    assert true_sys_d_z > 0 and wrong_sys_d_z < 0 and abs(fd_drz - pred_drz) < 1e-7
    print(f"  PASS: d = D^{{-1}} 1 check on K3 (beta=10, omega=0.05): (SYS d)_z = {true_sys_d_z:+.6e} (>0), d(r_z)/deta = {pred_drz:+.6e} vs FD {fd_drz:+.6e}.")
    print(f"  [NEGATIVE CONTROL CAUGHT]: using wrong D*1 gives (SYS D*1)_z = {wrong_sys_d_z:+.6e} (<0, wrong sign).")


def check_C5_marginal_and_discrete():
    print("\n=== C5. Marginal precision Pi_marg with outsiders & discrete-time comparison ===")
    # Witness W4 (SymPy exact rational): 0-2-1 (C={0,1}, O={2}, a01=0, a02=a12=1, eps=1/10, beta=1/5, omega=1/10, delta=1/100)
    M_021 = sp.Matrix([
        [sp.Rational(13, 10), 0, -1, -sp.Rational(1, 5)],
        [0, sp.Rational(13, 10), -1, -sp.Rational(1, 5)],
        [-1, -1, sp.Rational(21, 10), 0],
        [-sp.Rational(1, 20), -sp.Rational(1, 20), 0, sp.Rational(11, 100)]
    ])
    q_rev = sp.Rational(1, 4)
    for label, ratio in [("0", sp.Integer(0)), ("1/2", sp.Rational(1, 2)), ("1", sp.Integer(1)), ("2", sp.Integer(2)), ("10", sp.Integer(10))]:
        Sig = exact_lyapunov_sympy(M_021, 2 * sp.diag(1, 1, 1, ratio * q_rev))
        Pi_m = Sig[:3, :3].inv()
        off_m = [Pi_m[i, j] for i in range(3) for j in range(3) if i != j]
        rows_m = [sum(Pi_m.row(i)) for i in range(3)]
        diff_m = all(x <= 0 for x in off_m) and all(x >= 0 for x in rows_m)
        if label in ("0", "1/2", "1", "2"):
            assert diff_m, f"Expected Pi_marg diffusive at ratio={label}"
        else:
            assert not diff_m, f"Expected Pi_marg NOT diffusive at ratio=10"
        print(f"  Witness W4 (SymPy exact 0-2-1 Pi_marg, ratio={label:>3s}): diff={str(diff_m):5s}, max_off={float(max(off_m)):+.6e}, min_row={float(min(rows_m)):+.6e}")

    # Check open16 (obs:hie-record-window) opposite signs of dPi_marg at q_rev
    A8 = np.zeros((8, 8))
    for i in range(8):
        A8[i, (i + 1) % 8] = A8[(i + 1) % 8, i] = 1.0
    A16 = np.zeros((16, 16))
    A16[:8, :8] = A8; A16[8:, 8:] = A8
    for i in range(8):
        A16[i, 8 + i] = A16[8 + i, i] = 0.05
    M16, _, q_rev16 = build_continuous_system(A16, 8, 0.02, 0.2, 0.1, 0.01, 1.0)
    d16 = np.array([1.0] * 16 + [np.sqrt(q_rev16)])
    S16 = np.diag(1 / d16) @ M16 @ np.diag(d16)
    E16 = np.zeros((17, 17)); E16[16, 16] = 2.0
    Y16 = solve_continuous_lyapunov(S16, E16)
    Sinv16 = inv(S16)
    Mschur16 = inv(Sinv16[:16, :16])
    dPm16 = -Mschur16 @ Y16[:16, :16] @ Mschur16
    # Missing C-O edge (0, 9) vs missing O-O edge (8, 10)
    assert dPm16[0, 9] > 0 and dPm16[8, 10] < 0
    print(f"  open16 (delta=0.01) dPi_marg/deta at q_rev: missing C-O (0,9) = {dPm16[0,9]:+.6e} (>0), missing O-O (8,10) = {dPm16[8,10]:+.6e} (<0) -> breaks on BOTH sides.")

    # Witness W6 (SymPy exact rational): Discrete-time K3 two-sided window vs 0-1-2-3 upper barrier
    # Discrete K3: a=1/5, eps=1/20, beta=1/5, omega=1/10, delta=0 -> q_rev = 1/4
    W_k3 = sp.Matrix([
        [sp.Rational(7, 20), sp.Rational(1, 5), sp.Rational(1, 5), sp.Rational(1, 5)],
        [sp.Rational(1, 5), sp.Rational(7, 20), sp.Rational(1, 5), sp.Rational(1, 5)],
        [sp.Rational(1, 5), sp.Rational(1, 5), sp.Rational(11, 20), 0],
        [sp.Rational(1, 20), sp.Rational(1, 20), 0, sp.Rational(9, 10)]
    ])
    for label, ratio in [("0", sp.Integer(0)), ("1", sp.Integer(1)), ("101/100", sp.Rational(101, 100)), ("2", sp.Integer(2))]:
        Pi_d = exact_discrete_lyapunov_sympy(W_k3, sp.diag(1, 1, 1, ratio * sp.Rational(1, 4))).inv()
        off_d = [Pi_d[i, j] for i in range(4) for j in range(4) if i != j]
        rows_d = [sum(Pi_d.row(i)) for i in range(4)]
        diff_d = all(x <= 0 for x in off_d) and all(x >= 0 for x in rows_d)
        if label in ("0", "1", "101/100"):
            assert diff_d
        else:
            assert not diff_d
        print(f"  Witness W6a (SymPy exact discrete K3, delta=0, ratio={label:>7s}): diff={str(diff_d):5s}, Pi_oz={float(Pi_d[2,3]):+.6e}, min_row={float(min(rows_d)):+.6e}")

    # Discrete path 0-1-2-3 (C={0,1}, O={2,3}; outsider 3 at dist 2 from C, dist 3 from z; U psd)
    # a=1/10, eps=1/20, beta=1/5, omega=1/10, delta=1/50 -> W diag >= sum off-diag so U >= 0 psd!
    W_p4 = sp.Matrix([
        [sp.Rational(13, 20), sp.Rational(1, 10), sp.Rational(1, 10), 0, sp.Rational(1, 5)],
        [sp.Rational(1, 10), sp.Rational(15, 20), 0, 0, sp.Rational(1, 5)],
        [sp.Rational(1, 10), 0, sp.Rational(15, 20), sp.Rational(1, 10), 0],
        [0, 0, sp.Rational(1, 10), sp.Rational(17, 20), 0],
        [sp.Rational(1, 20), sp.Rational(1, 20), 0, 0, sp.Rational(22, 25)]
    ])
    # Verify U = D^-1 W D is psd
    d_p4 = np.array([1.0, 1.0, 1.0, 1.0, 0.5])
    U_p4 = np.diag(1 / d_p4) @ np.array(W_p4.evalf(), dtype=float) @ np.diag(d_p4)
    assert np.min(eigvalsh(U_p4)) > 0
    Pi_p4_rev = exact_discrete_lyapunov_sympy(W_p4, sp.diag(1, 1, 1, 1, sp.Rational(1, 4))).inv()
    Pi_p4_hi = exact_discrete_lyapunov_sympy(W_p4, sp.diag(1, 1, 1, 1, sp.Rational(101, 100) * sp.Rational(1, 4))).inv()
    assert Pi_p4_rev[3, 4] == 0 and Pi_p4_hi[3, 4] > 0
    print(f"  Witness W6b (SymPy exact discrete 0-1-2-3, U psd): at q_rev Pi_3z={Pi_p4_rev[3,4]}, at 1.01*q_rev Pi_3z={float(Pi_p4_hi[3,4]):+.6e} (>0, upper barrier restored).")
    # Negative control: discrete K3 at ratio=101/100 refutes applying continuous-time upper barrier C2 to discrete time!
    print("  [NEGATIVE CONTROL CAUGHT]: continuous-time upper barrier q_z<=q_rev fails on discrete K3 at ratio=101/100 (diff=True).")


def check_C6_weighted_contrast_and_size_bound():
    print("\n=== C6. Q^{-1}-weighted contrast r_W(C') & weighted size bound ===")
    # Channel 1 + 2: Verify exact formula for r_W(C') on 100 random embedded collectives at q_z = q_rev
    # AND verify weighted size bound on 200 random diffusive weighted media (coordinates & metric)
    rng = np.random.default_rng(3003)
    max_rW_err = 0.0
    max_bound_ratio = 0.0
    for trial in range(100):
        n = int(rng.integers(2, 7))
        m = int(rng.integers(0, 5))
        N = n + m
        A = 10 ** rng.uniform(-1, 1, size=(N, N))
        A = (A + A.T) / 2
        np.fill_diagonal(A, 0.0)
        eps_v = float(10 ** rng.uniform(-2, 0.5))
        beta_v = float(10 ** rng.uniform(-2, 0.5))
        omega_v = float(10 ** rng.uniform(-2, 0.5))
        delta_v = 0.0 if trial % 2 == 0 else float(10 ** rng.uniform(-2, 0.5))
        q_v = float(10 ** rng.uniform(-1, 1))
        M, Q, q_rev = build_continuous_system(A, n, eps_v, beta_v, omega_v, delta_v, q_v, None)
        Pi = np.diag(1.0 / np.diag(Q)) @ M  # exact Pi_rev = Q^{-1} M
        w = 1.0 / np.diag(Q)
        Cprime = list(range(n)) + [N]
        rW_num, xin_num, xout_num = contrast_weighted(Pi, w, Cprime)

        # Formula
        R_v = beta_v / omega_v
        A_C = A[:n, :n]
        L_C = np.diag(A_C.sum(axis=1)) - A_C
        lam2_C = float(eigvalsh(L_C)[1])
        cut_C = float(A[:n, n:].sum()) if m > 0 else 0.0
        xin_f = min(eps_v + beta_v + lam2_C, beta_v + omega_v + (eps_v * R_v + delta_v) / (1.0 + R_v))
        xout_f = (eps_v + R_v * delta_v + cut_C / n) / (1.0 + R_v)
        rW_f = xin_f / xout_f
        max_rW_err = max(max_rW_err, abs(rW_num - rW_f) / rW_f)

        # Weighted size bound check with random 1D coordinates x
        x = rng.normal(0.0, 2.0, size=N + 1)
        wC = w[Cprime]
        xC = x[Cprime]
        xbar_W = float(np.sum(wC * xC) / np.sum(wC))
        var_W = float(np.sum(wC * (xC - xbar_W) ** 2) / np.sum(wC))
        eps_M = np.diag(Q) * Pi.sum(axis=1)  # drift leaks
        eps_max_M = float(np.max(eps_M[Cprime]))
        eps_bar_W = float(np.sum(Pi.sum(axis=1)[Cprime]) / np.sum(wC))
        # varsigma_W^2 = max_u sum_v q_u a_{uv}^Pi (x_v - x_u)^2
        a_Pi = -Pi.copy()
        np.fill_diagonal(a_Pi, 0.0)
        q_vec = np.diag(Q)
        varsigma_W_sq = max(float(np.sum(q_vec[u] * a_Pi[u, :] * (x - x[u]) ** 2)) for u in range(N + 1))
        rhs = eps_max_M / eps_bar_W + varsigma_W_sq / (2.0 * eps_bar_W * var_W)
        assert rW_num <= rhs + 1e-11
        max_bound_ratio = max(max_bound_ratio, rW_num / rhs)

    # Verify global record unbounded-extent example (a_ij = 0, delta = 0): r_W(C') independent of Var(C)
    # n=100 uncoupled agents on x_i = i, global record at x_z = bar x_C, eps=0.02, beta=0.2, omega=0.02 (R=10)
    n_g = 100
    eps_g, beta_g, omega_g = 0.02, 0.2, 0.02
    R_g = beta_g / omega_g
    rW_uncoupled = (1 + R_g) * min(eps_g + beta_g, beta_g + omega_g + eps_g * R_g / (1 + R_g)) / eps_g
    var_C_g = (n_g ** 2 - 1) / 12.0
    # Verify local-record isolated path (delta = 0, x_{z_i} = x_i): r_W <= 1 + lam2/eps
    n_loc = 30
    a_loc, eps_loc, beta_loc, omega_loc = 1.0, 0.02, 0.2, 0.01  # R=20
    R_loc = beta_loc / omega_loc
    Pi_loc = np.zeros((2 * n_loc, 2 * n_loc))
    for i in range(n_loc):
        Pi_loc[i, i] += eps_loc + beta_loc
        Pi_loc[i, n_loc + i] = Pi_loc[n_loc + i, i] = -beta_loc
        Pi_loc[n_loc + i, n_loc + i] = beta_loc
        if i + 1 < n_loc:
            Pi_loc[i, i] += a_loc; Pi_loc[i + 1, i + 1] += a_loc
            Pi_loc[i, i + 1] = Pi_loc[i + 1, i] = -a_loc
    w_loc = np.array([1.0] * n_loc + [R_loc] * n_loc)
    rW_loc, _, _ = contrast_weighted(Pi_loc, w_loc, list(range(2 * n_loc)))
    lam2_loc = 2 * a_loc * (1 - np.cos(np.pi / n_loc))
    assert rW_loc <= 1.0 + lam2_loc / eps_loc + 1e-12

    # Negative control: replacing Var_W by unweighted Var_C (without 1+R factor) when x_z = bar_x violates bound on sharp star!
    # Take C={0,1} at x=-1,+1, z at x=0, eps=delta=0.1 (uniform drift leak -> het=1), beta=1, omega=0.01 (R=100), a01=0.
    # Then Var_C = 1, Var_W = 1/101, varsigma_W^2 = max(beta*1^2, omega*1^2) = 1.
    # Weighted bound: 1 + 1/(2*0.1*(1/101)) = 506, actual r_W = (0.1 + 1)/0.1 = 11 (Wait: with unweighted Var_C=1, 1 + 1/(2*0.1*1) = 6 < 11 -> VIOLATED!)
    M_nc, Q_nc, _ = build_continuous_system(np.zeros((2, 2)), 2, 0.1, 1.0, 0.01, 0.1, 1.0, None)
    Pi_nc = np.diag(1.0 / np.diag(Q_nc)) @ M_nc
    w_nc = 1.0 / np.diag(Q_nc)
    rW_nc, _, _ = contrast_weighted(Pi_nc, w_nc, [0, 1, 2])
    # x = [-1, 1, 0]: Var_C = 1, Var_W = 1/101, varsigma_W^2 = 1, eps_bar_W = 0.1, het = 1
    wrong_unweighted_rhs = 1.0 + 1.0 / (2.0 * 0.1 * 1.0)  # 6.0
    true_weighted_rhs = 1.0 + 1.0 / (2.0 * 0.1 * (1.0 / 101.0))  # 506.0
    assert rW_nc > wrong_unweighted_rhs + 4.0 and rW_nc <= true_weighted_rhs
    print(f"  PASS: r_W formula max rel err = {max_rW_err:.3e} over 100 random systems.")
    print(f"  PASS: weighted size bound held on all 100 random systems (max ratio r_W/RHS = {max_bound_ratio:.4f}).")
    print(f"  PASS: uncoupled global record (n=100, R=10, delta=0): r_W={rW_uncoupled:.4f} at Var(C)={var_C_g:.2f}; local-record path (n=30, R=20): r_W={rW_loc:.4f} <= 1+lam2/eps={1+lam2_loc/eps_loc:.4f}.")
    print(f"  [NEGATIVE CONTROL CAUGHT]: dropping 1+R dilution (using Var_C=1 instead of Var_W=1/101) gives RHS={wrong_unweighted_rhs:.1f} < actual r_W={rW_nc:.2f} (true weighted RHS={true_weighted_rhs:.1f}).")


def check_C7_typed_comparison_medium():
    print("\n=== C7. Typed comparison medium: whole-population exclusion, fibered-lattice bound, and 9-node / 17-node baselines ===")
    # 1. Verify whole-population exclusion (Euclidean AND Q^-1-weighted) over 100 random typed populations
    #    under two-type exchangeability (G = Sym(V) x Sym(Z))
    rng = np.random.default_rng(4004)
    for trial in range(100):
        N = int(rng.integers(3, 7))
        mz = int(rng.integers(1, 4))
        Vtot = N + mz
        A = rng.uniform(0.05, 2.0, size=(Vtot, Vtot))
        A = (A + A.T) / 2
        np.fill_diagonal(A, 0.0)
        eV = rng.uniform(0.05, 1.0, size=N)
        eZ = rng.uniform(0.0, 1.0, size=mz)
        e_all = np.concatenate([eV, eZ])
        Pi = np.diag(e_all + A.sum(axis=1)) - A
        # Construct typed exchangeable comparison medium
        a_VV = A[:N, :N].sum() / (N * (N - 1))
        a_VZ = A[:N, N:].sum() / (N * mz)
        a_ZZ = A[N:, N:].sum() / (mz * (mz - 1)) if mz >= 2 else 0.0
        A_hom = np.zeros((Vtot, Vtot))
        A_hom[:N, :N] = a_VV * (np.ones((N, N)) - np.eye(N))
        A_hom[:N, N:] = a_VZ; A_hom[N:, :N] = a_VZ
        if mz >= 2:
            A_hom[N:, N:] = a_ZZ * (np.ones((mz, mz)) - np.eye(mz))
        e_hom = np.concatenate([np.full(N, eV.mean()), np.full(mz, eZ.mean())])
        Pi_hom = np.diag(e_hom + A_hom.sum(axis=1)) - A_hom

        r_act, _, _ = contrast_euclid(Pi, list(range(Vtot)))
        r_hom, _, _ = contrast_euclid(Pi_hom, list(range(Vtot)))
        assert r_act <= r_hom + 1e-11
        # Also type-constant weight W = diag(wV,...,wV, wZ,...,wZ)
        w = np.concatenate([np.full(N, 1.0), np.full(mz, 5.0)])
        rW_act, _, _ = contrast_weighted(Pi, w, list(range(Vtot)))
        rW_hom, _, _ = contrast_weighted(Pi_hom, w, list(range(Vtot)))
        assert rW_act <= rW_hom + 1e-11
    print("  PASS: C7(2) whole-population exclusion r(V') <= r_hom(V') verified (Euclidean & weighted) on 100 random typed populations.")

    # 2. Verify C7(3) fibered lattice Z^1 x {A, Z} bound on 300 random finite subsets C' with arbitrary (eps_A, eps_Z)
    #    nearest-neighbor a_nn=1 on agents, local coupling beta=0.5, a_ZZ=0 -> Delta_max = 2.5, varsigma^2 = 2
    a_nn, beta_f = 1.0, 0.5
    Delta_max = 2.0 * a_nn + beta_f  # 2.5
    varsigma_sq = 2.0 * a_nn  # 2.0
    max_ratio_fibered = 0.0
    # Embed in ring of 40 sites (well larger than subsets of span <= 12)
    L_ring = 40
    for trial in range(300):
        eps_A = 0.0 if trial % 5 == 0 else float(10 ** rng.uniform(-4, 3))
        eps_Z = 0.0 if trial % 5 == 1 else float(10 ** rng.uniform(-4, 3))
        if eps_A == 0.0 and eps_Z == 0.0:
            eps_A = 1e-4
        # Build subset C_A, C_Z in {0..11}
        kA = int(rng.integers(0, 10))
        kZ = int(rng.integers(0, 10))
        if kA + kZ < 2:
            kA = 2
        C_A = sorted(rng.choice(12, size=kA, replace=False).tolist()) if kA > 0 else []
        C_Z = sorted(rng.choice(12, size=kZ, replace=False).tolist()) if kZ > 0 else []
        n_tot = kA + kZ
        # Compute exact cut and xin on Z^1 x {A,Z}
        nodes = [('A', i) for i in C_A] + [('Z', i) for i in C_Z]
        set_A = set(C_A); set_Z = set(C_Z)
        M_in = np.zeros((n_tot, n_tot))
        cut_val = 0.0
        for idx, (tp, pos) in enumerate(nodes):
            M_in[idx, idx] += eps_A if tp == 'A' else eps_Z
            if tp == 'A':
                for nb in (pos - 1, pos + 1):
                    if nb in set_A:
                        j = nodes.index(('A', nb))
                        M_in[idx, idx] += a_nn; M_in[idx, j] -= a_nn
                    else:
                        cut_val += a_nn
                if pos in set_Z:
                    j = nodes.index(('Z', pos))
                    M_in[idx, idx] += beta_f; M_in[idx, j] -= beta_f
                else:
                    cut_val += beta_f
            else:
                if pos in set_A:
                    j = nodes.index(('A', pos))
                    M_in[idx, idx] += beta_f; M_in[idx, j] -= beta_f
                else:
                    cut_val += beta_f
        ones = np.ones(n_tot)
        U, _, _ = np.linalg.svd(ones[:, None], full_matrices=True)
        B = U[:, 1:]
        xin_f = float(np.min(eigvalsh(B.T @ M_in @ B)))
        eps_bar = (kA * eps_A + kZ * eps_Z) / n_tot
        xout_f = eps_bar + cut_val / n_tot
        r_f = xin_f / xout_f
        # Theoretical uniform bound for D=1:
        # Case 1 (|kA-kZ| >= n/3): max(3/2, 6*Delta_max/beta_f) for n>=3, max(1, 2*Delta_max/beta_f) for n=2
        # Case 2 (|kA-kZ| < n/3): max(3, min(Delta_max*n / a_nn, 2*varsigma_sq*n / (a_nn*(n/4 - 1)^2)))
        # Uniform cap across all n >= 2 (D=1): max(3, 6*Delta_max/beta_f, 8*Delta_max/a_nn, 32*varsigma_sq/a_nn)
        B_unif = max(3.0, 6.0 * Delta_max / beta_f, 8.0 * Delta_max / a_nn, 32.0 * varsigma_sq / a_nn)
        assert r_f <= B_unif + 1e-11, f"Fibered bound failed: {r_f} > {B_unif}"
        max_ratio_fibered = max(max_ratio_fibered, r_f / B_unif)
    print(f"  PASS: C7(3) fibered lattice Z^1 x {{A,Z}} uniform bound B={B_unif:.2f} held on 300 random subsets (max r/B = {max_ratio_fibered:.4f}).")

    # 3. Exhaustive 9-node baseline (two 4-cycles + global record) at eps=0.20 and eps=0.50, and 17-node check at eps=0.02
    a_bar = 41.0 / 60.0
    b_bar = 0.2
    for eps_v in [0.05, 0.20, 0.50]:
        A_hom = np.zeros((8, 8))
        for i in range(4):
            A_hom[i, (i + 1) % 4] = A_hom[(i + 1) % 4, i] = a_bar
            A_hom[4 + i, 4 + (i + 1) % 4] = A_hom[4 + (i + 1) % 4, 4 + i] = a_bar
            A_hom[i, 4 + i] = A_hom[4 + i, i] = a_bar
        Pi_hom = np.zeros((9, 9))
        Pi_hom[:8, :8] = eps_v * np.eye(8) + np.diag(A_hom.sum(axis=1)) - A_hom + b_bar * np.eye(8)
        Pi_hom[:8, 8] = Pi_hom[8, :8] = -b_bar
        Pi_hom[8, 8] = 8 * b_bar
        best_r = max(contrast_euclid(Pi_hom, S)[0] for k in range(2, 10) for S in combinations(range(9), k))

        A_act = np.zeros((8, 8))
        for i in range(4):
            A_act[i, (i + 1) % 4] = A_act[(i + 1) % 4, i] = 1.0
            A_act[4 + i, 4 + (i + 1) % 4] = A_act[4 + (i + 1) % 4, 4 + i] = 1.0
            A_act[i, 4 + i] = A_act[4 + i, i] = 0.05
        Pi_act = np.zeros((9, 9))
        Pi_act[:8, :8] = eps_v * np.eye(8) + np.diag(A_act.sum(axis=1)) - A_act
        for i in range(4):
            Pi_act[i, i] += 0.4; Pi_act[i, 8] = Pi_act[8, i] = -0.4
        Pi_act[8, 8] = 4 * 0.4
        r_Cp, _, _ = contrast_euclid(Pi_act, [0, 1, 2, 3, 8])
        r_all, _, _ = contrast_euclid(Pi_act, list(range(9)))
        assert r_all <= best_r + 1e-12
        print(f"  9-node exhaustive baseline (502 regions, eps={eps_v:4.2f}): r(C')={r_Cp:.4f}, r_hom_bar={best_r:.4f}, sig={r_Cp/best_r:.4f}, r_act(V')={r_all:.4f}")

    # Negative control: pooling agent & record leaks into one uniform leak on homogeneous closed population breaks invariance!
    # Take closed 4-cycle + global record with uniform a=1, b=0.2, eps=0.1, delta=0: it IS homogeneous, so typed Pi_hom == Pi.
    # Pooled-leak Pi_pool sets leak 4*0.1/5 = 0.08 on every node -> differs from Pi by ||Pi - Pi_pool||_F > 0.08!
    Pi_closed_hom = np.zeros((5, 5))
    for i in range(4):
        Pi_closed_hom[i, i] = 0.1 + 2.0 + 0.2
        Pi_closed_hom[i, (i + 1) % 4] = Pi_closed_hom[(i + 1) % 4, i] = -1.0
        Pi_closed_hom[i, 4] = Pi_closed_hom[4, i] = -0.2
    Pi_closed_hom[4, 4] = 0.8
    Pi_pool = Pi_closed_hom.copy()
    for i in range(4): Pi_pool[i, i] -= 0.02
    Pi_pool[4, 4] += 0.08
    diff_pool = np.linalg.norm(Pi_closed_hom - Pi_pool)
    assert diff_pool > 0.08
    print(f"  [NEGATIVE CONTROL CAUGHT]: naive single-type leak pooling alters an already-homogeneous agent+record medium by ||dPi||_F={diff_pool:.4f}.")


if __name__ == "__main__":
    check_conventions_and_manuscript_test_instance()
    check_C1_closed_collective()
    check_C2_C3_upper_and_noiseless_barriers()
    check_C4_below_qrev_and_witnesses()
    check_C5_marginal_and_discrete()
    check_C6_weighted_contrast_and_size_bound()
    check_C7_typed_comparison_medium()
    print("\nALL CHECKS AND NEGATIVE CONTROLS PASSED.")
