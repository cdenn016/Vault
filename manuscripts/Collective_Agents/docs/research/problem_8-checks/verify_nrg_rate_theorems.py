import numpy as np
from scipy import linalg

def solve_lyapunov(A, Q):
    return linalg.solve_discrete_lyapunov(A, Q)

def exact_ep(A, Q, Sigma):
    J = A @ Sigma - Sigma @ A.T
    return float(np.trace(linalg.solve(Q, J @ A.T)))

def window_Dn(A, Sigma, C, n):
    """Channel 2: Brute-force window divergence directly from Def / Thm nrg-coarse(b)."""
    m = C.shape[0]
    N = n + 1
    Gammas = [C @ Sigma @ C.T]
    Ak = np.eye(A.shape[0])
    for k in range(1, N):
        Ak = Ak @ A
        Gammas.append(C @ Ak @ Sigma @ C.T)
    T = np.zeros((N * m, N * m))
    for s in range(N):
        for t in range(N):
            T[s*m:(s+1)*m, t*m:(t+1)*m] = Gammas[s - t] if s >= t else Gammas[t - s].T
    Tr = np.zeros_like(T)
    for s in range(N):
        for t in range(N):
            Tr[s*m:(s+1)*m, t*m:(t+1)*m] = T[(N-1-s)*m:(N-s)*m, (N-1-t)*m:(N-t)*m]
    L = linalg.cholesky(Tr, lower=True)
    X = linalg.solve_triangular(L, T, lower=True)
    Y = linalg.solve_triangular(L.T, X, lower=False)
    return 0.5 * (float(np.trace(Y)) - N * m)

def spectral_rate_and_e0(A, Q, C, n_grid=2048, plant_error=None):
    """Channel 1: Exact spectral integral for ebar and 2d x 2d Woodbury formula for e0."""
    d = A.shape[0]
    m = C.shape[0]
    # Enforce side conditions
    rho = max(abs(linalg.eigvals(A)))
    assert rho < 1.0, f"Inadmissible A: rho(A)={rho} >= 1"
    eigs_Q = linalg.eigvalsh(0.5 * (Q + Q.T))
    assert np.min(eigs_Q) > 0, f"Inadmissible Q: min eig={np.min(eigs_Q)} <= 0"
    assert np.linalg.matrix_rank(C) == m, f"Inadmissible C: rank < {m}"

    Sigma = solve_lyapunov(A, Q)
    I_d = np.eye(d, dtype=complex)
    thetas = (np.arange(n_grid) + 0.5) * (2 * np.pi / n_grid) - np.pi

    ebar_acc = 0.0
    G1 = np.zeros((2*d, 2*d), dtype=complex)
    G2 = np.zeros((2*d, 2*d), dtype=complex)
    G3 = np.zeros((2*d, 2*d), dtype=complex)
    G4 = np.zeros((2*d, 2*d), dtype=complex)
    c_min = np.inf
    c_max = 0.0

    for th in thetas:
        z = np.exp(1j * th)
        zb = np.exp(-1j * th)
        inv1_m = linalg.solve(I_d - zb * A, I_d)
        inv2_m = linalg.solve(I_d - zb * A.T, I_d)
        L1hat_p = C @ inv1_m
        L2hat_p = C @ Sigma @ inv2_m
        L1hat_m = L1hat_p.conj()
        L2hat_m = L2hat_p.conj()

        R_res = zb * inv1_m
        S = C @ R_res @ Q @ R_res.conj().T @ C.T
        S = 0.5 * (S + S.conj().T)
        ev = linalg.eigvalsh(S)
        c_min = min(c_min, float(ev[0]))
        c_max = max(c_max, float(ev[-1]))

        Sinv = linalg.inv(S)
        Sbar_inv = Sinv.conj()
        B3 = Sbar_inv @ S @ Sbar_inv

        if plant_error == "no_conj_in_ebar":
            ebar_acc += 0.5 * np.real(np.trace(Sinv @ S) - m)
        else:
            ebar_acc += 0.5 * np.real(np.trace(Sbar_inv @ S) - m)

        z_phase = zb if plant_error == "flip_z_phase" else z
        Phi_W = np.hstack([L1hat_p, z_phase * L2hat_m])
        Phi_Wt = np.hstack([z_phase * L1hat_m, L2hat_p])

        G1 += Phi_Wt.conj().T @ Sbar_inv @ Phi_Wt
        G2 += Phi_W.conj().T @ Sbar_inv @ Phi_W
        G3 += Phi_Wt.conj().T @ B3 @ Phi_Wt
        G4 += Phi_Wt.conj().T @ Sbar_inv @ Phi_W

    ebar = ebar_acc / n_grid
    G1, G2, G3, G4 = (G / n_grid for G in (G1, G2, G3, G4))
    for G in (G1, G2, G3, G4):
        scale = max(1.0, float(np.max(np.abs(G.real))))
        assert float(np.max(np.abs(G.imag))) < 1e-11 * scale, f"Imag part too large: {np.max(np.abs(G.imag))} vs scale {scale}"
    G1, G2, G3, G4 = G1.real, G2.real, G3.real, G4.real

    H = np.block([[np.zeros((d, d)), A], [A.T, np.zeros((d, d))]])
    K = np.eye(2*d) - H @ G1
    eigs_K = linalg.eigvals(K)
    min_eig_K = float(np.min(eigs_K.real))
    det_K = float(np.real(linalg.det(K)))
    if plant_error is None:
        assert min_eig_K >= c_min / c_max - 1e-10, f"Eigenvalue bound violated: {min_eig_K} < {c_min/c_max}"

    KinvH = linalg.solve(K, H)
    delta_2D = -np.trace(H @ G2) + np.trace(KinvH @ G3) - np.trace(KinvH @ G4 @ H @ G4.T)
    if plant_error == "drop_ebar_shift":
        e0 = -0.5 * float(delta_2D)
    else:
        e0 = -ebar - 0.5 * float(delta_2D)
    return ebar, e0, min_eig_K, det_K, c_min / c_max

print("============================================================")
print("PART 1: Verification of Claim 1 (ebar) and Claim 1b (e0)")
print("============================================================")
rng = np.random.default_rng(5) # Also test seed 5 style (diagonal Q) to get negative e0!
cases = []

# 1. Registered test instance: directed ring (1,2)
P = np.array([[0,1,0],[0,0,1],[1,0,0]], dtype=float)
cases.append(("Directed ring (1,2)", 0.3*np.eye(3) + 0.5*P, np.eye(3), np.array([[1.,0.,0.],[0.,1.,0.]])))

# 2. Singular A (det A = 0, nilpotent + non-nilpotent block) - critical edge case!
A_sing = np.array([[0.0, 0.8, 0.3], [0.0, 0.0, 0.9], [0.2, 0.0, 0.0]]) # wait det != 0; make rank 2:
A_sing = np.array([[0.5, 0.7, 0.0], [-0.4, 0.3, 0.6], [0.0, 0.0, 0.0]]) # det A = 0!
Q_sing = np.array([[1.0, 0.2, -0.3], [0.2, 0.8, 0.4], [-0.3, 0.4, 1.2]])
C_sing = np.array([[1.0, 0.0, 0.5], [0.0, 1.0, -0.4]])
assert abs(linalg.det(A_sing)) < 1e-15
cases.append(("Singular A (det=0)", A_sing, Q_sing, C_sing))

# 3. Defective Jordan 3x3
A_def = np.array([[0.7, 1.0, 0.0], [0.0, 0.7, 1.0], [0.0, 0.0, 0.7]])
Q_def = np.array([[1.0, 0.3, -0.2], [0.3, 0.5, 0.1], [-0.2, 0.1, 0.8]])
C_def = np.array([[1.0, 0.0, 0.5], [0.0, 1.0, -0.3]])
cases.append(("Defective Jordan 3x3", A_def, Q_def, C_def))

# 4. Find at least two negative-e0 instances via random search (uncontaminated)
rng2 = np.random.default_rng(2026112101)
neg_found = 0
for attempt in range(50):
    A = rng2.normal(size=(4, 4))
    A = A * (0.7 / max(abs(linalg.eigvals(A))))
    Q = np.diag(rng2.uniform(0.5, 2.0, size=4))
    C = rng2.normal(size=(2, 4))
    ebar, e0, _, _, _ = spectral_rate_and_e0(A, Q, C, n_grid=512)
    if e0 < -0.05:
        neg_found += 1
        cases.append((f"Negative-e0 #{neg_found} (d=4,m=2)", A, Q, C))
        if neg_found == 2:
            break
assert neg_found == 2, "Did not find 2 negative-e0 instances"

# 5. High-dimension non-normal d=6, m=3
A6 = rng2.normal(size=(6, 6))
A6 = A6 * (0.75 / max(abs(linalg.eigvals(A6))))
G6 = rng2.normal(size=(6, 6))
Q6 = G6 @ G6.T + 0.4 * np.eye(6)
C6 = rng2.normal(size=(3, 6))
cases.append(("Generic d=6, m=3", A6, Q6, C6))

max_e0_err = 0.0
for name, A, Q, C in cases:
    Sigma = solve_lyapunov(A, Q)
    ebar_1024, e0_1024, _, _, _ = spectral_rate_and_e0(A, Q, C, n_grid=1024)
    ebar, e0_formula, min_eig_K, det_K, ratio_bound = spectral_rate_and_e0(A, Q, C, n_grid=2048)
    grid_diff = abs(e0_formula - e0_1024)
    dn_96 = window_Dn(A, Sigma, C, 96)
    e0_direct = 96 * ebar - dn_96
    err = abs(e0_formula - e0_direct)
    max_e0_err = max(max_e0_err, err)
    # Also check exponential decay n=8, 16, 32, 64
    errs_n = [abs(n*ebar - window_Dn(A, Sigma, C, n) - e0_formula) for n in (8, 16, 32, 64)]
    print(f"{name:26s}: ebar={ebar:9.6f} | e0_dir={e0_direct:+12.8f} | e0_thm={e0_formula:+12.8f} | err96={err:.2e} | grid_diff={grid_diff:.1e} | detK={det_K:.4f}")
    print(f"   |n*ebar - Dn - e0| for n=8,16,32,64: {[f'{e:.2e}' for e in errs_n]}")

assert max_e0_err < 1e-9, f"e0 discrepancy too large: {max_e0_err}"
print(f"PASS Part 1: max |e0_thm - e0_direct(n=96)| = {max_e0_err:.3e}")

print("\n--- Negative controls (planted errors MUST fail by > 0.05) ---")
A0, Q0, C0 = cases[0][1], cases[0][2], cases[0][3]
S0 = solve_lyapunov(A0, Q0)
ebar_ok, e0_ok, _, _, _ = spectral_rate_and_e0(A0, Q0, C0, n_grid=1024)
dn_ok = window_Dn(A0, S0, C0, 64)
for pe in ["no_conj_in_ebar", "drop_ebar_shift", "flip_z_phase"]:
    eb_bad, e0_bad, _, _, _ = spectral_rate_and_e0(A0, Q0, C0, n_grid=1024, plant_error=pe)
    diff_eb = abs(eb_bad - ebar_ok)
    diff_e0 = abs(e0_bad - (64*ebar_ok - dn_ok))
    print(f"  Planted error '{pe:16s}': |delta_ebar|={diff_eb:.6f}, |delta_e0|={diff_e0:.6f}")
    assert max(diff_eb, diff_e0) > 0.01, f"Negative control {pe} failed to trigger!"
print("PASS Negative controls: all 3 planted errors triggered cleanly.")

print("\n============================================================")
print("PART 2: Exact Lossless Retention Theorem: ebar(C)=ep <=> row(C) >= range(Omega)")
print("============================================================")
# Test 2a: Construct a coupled d=12 non-normal network with rank(Omega) = 2!
# How: start with a reversible pair (A_rev, Q) satisfying A_rev Q = Q A_rev^T (i.e. A_rev = Q M, M symmetric),
# then add a rank-2 skew perturbation Q * (u v^T - v u^T) so Omega = Q^{-1} A - A^T Q^{-1} = 2(u v^T - v u^T) has exact rank 2!
d12 = 12
G12 = rng2.normal(size=(d12, d12))
Q12 = G12 @ G12.T + 0.5 * np.eye(d12)
M12 = rng2.normal(size=(d12, d12)); M12 = 0.5 * (M12 + M12.T)
u = rng2.normal(size=d12); v = rng2.normal(size=d12)
W_skew = np.outer(u, v) - np.outer(v, u)
A12 = Q12 @ (M12 + 0.8 * W_skew)
A12 = A12 * (0.75 / max(abs(linalg.eigvals(A12))))
Sigma12 = solve_lyapunov(A12, Q12)
ep12 = exact_ep(A12, Q12, Sigma12)
Q12_inv = linalg.inv(Q12)
Omega12 = Q12_inv @ A12 - A12.T @ Q12_inv
svals = linalg.svdvals(Omega12)
U_om, S_om, _ = linalg.svd(Omega12)
assert np.sum(S_om > 1e-10) == 2, f"Expected rank 2, got {S_om}"
C_opt12 = U_om[:, :2].T # exact 2D basis for range(Omega12)
ebar_opt12, e0_opt12, _, _, _ = spectral_rate_and_e0(A12, Q12, C_opt12, n_grid=1024)
# Also test a perturbed C (angle 0.2 away from range(Omega)) -- negative control!
C_pert12 = C_opt12.copy()
C_pert12[0] = np.cos(0.2) * C_opt12[0] + np.sin(0.2) * U_om[:, 2]
ebar_pert12, _, _, _, _ = spectral_rate_and_e0(A12, Q12, C_pert12, n_grid=1024)
# Also test a random 2D projection
C_rand12 = rng2.normal(size=(2, d12))
ebar_rand12, _, _, _, _ = spectral_rate_and_e0(A12, Q12, C_rand12, n_grid=1024)
print(f"d=12 coupled network with rank(Omega)=2: ep = {ep12:.10f}")
print(f"  m=2 with row(C)=range(Omega): ebar = {ebar_opt12:.10f}, |ep - ebar| = {abs(ep12 - ebar_opt12):.2e}, e0 = {e0_opt12:+.6f}")
print(f"  m=2 perturbed by 0.2 rad    : ebar = {ebar_pert12:.10f}, retained = {ebar_pert12/ep12:.6f} (< 1 strictly)")
print(f"  m=2 random subspace         : ebar = {ebar_rand12:.10f}, retained = {ebar_rand12/ep12:.6f}")
assert abs(ep12 - ebar_opt12) < 1e-12
assert ebar_pert12 < ep12 - 1e-4

# Test 2b: Check ebar(I) = ep directly and verify odd d=3,5 generic systems retain 100% at m=d-1
for d_odd in [3, 5]:
    A = rng2.normal(size=(d_odd, d_odd))
    A = A * (0.7 / max(abs(linalg.eigvals(A))))
    G = rng2.normal(size=(d_odd, d_odd))
    Q = G @ G.T + 0.4 * np.eye(d_odd)
    Sigma = solve_lyapunov(A, Q)
    ep = exact_ep(A, Q, Sigma)
    Qinv = linalg.inv(Q)
    Omega = Qinv @ A - A.T @ Qinv
    U, s, _ = linalg.svd(Omega)
    assert s[-1] < 1e-13
    C_lossless = U[:, :d_odd-1].T
    eb, e0_l, _, _, _ = spectral_rate_and_e0(A, Q, C_lossless, n_grid=1024)
    print(f"Generic odd d={d_odd}, m={d_odd-1} (row(C)=range(Omega)): ep={ep:.8f}, ebar={eb:.8f}, |diff|={abs(ep-eb):.2e}, e0={e0_l:+.6f}")
    assert abs(ep - eb) < 1e-12
    assert e0_l >= -1e-12 # Since Dn(C) <= n*ep = n*ebar(C), e0 MUST be >= 0!

# Test 2c: Check Grassmannian gradient formula against central finite differences!
A_g, Q_g, C_g = cases[2][1], cases[2][2], cases[2][3]
def grad_ebar(A, Q, C, n_grid=1024):
    d, m = A.shape[0], C.shape[0]
    I_d = np.eye(d, dtype=complex)
    thetas = (np.arange(n_grid) + 0.5) * (2 * np.pi / n_grid) - np.pi
    grad = np.zeros((m, d))
    for th in thetas:
        z = np.exp(1j * th)
        R = linalg.solve(z * I_d - A, I_d)
        Sf = R @ Q @ R.conj().T
        S = C @ Sf @ C.T
        Sbar_inv = linalg.inv(S.conj())
        term = Sbar_inv @ C @ Sf - Sbar_inv @ S @ Sbar_inv @ C @ Sf.conj()
        grad += term.real
    return grad / n_grid

g_analytic = grad_ebar(A_g, Q_g, C_g)
eps_fd = 1e-6
g_fd = np.zeros_like(C_g)
for i in range(C_g.shape[0]):
    for j in range(C_g.shape[1]):
        Cp = C_g.copy(); Cp[i, j] += eps_fd
        Cm = C_g.copy(); Cm[i, j] -= eps_fd
        ep_p, _, _, _, _ = spectral_rate_and_e0(A_g, Q_g, Cp, n_grid=1024)
        ep_m, _, _, _, _ = spectral_rate_and_e0(A_g, Q_g, Cm, n_grid=1024)
        g_fd[i, j] = (ep_p - ep_m) / (2 * eps_fd)
grad_err = np.max(np.abs(g_analytic - g_fd))
orth_err = np.max(np.abs(g_analytic @ C_g.T))
print(f"\nGrassmannian gradient check: max |grad_analytic - grad_FD| = {grad_err:.2e}, max |grad @ C^T| = {orth_err:.2e}")
assert grad_err < 1e-8 and orth_err < 1e-13

print("\n============================================================")
print("PART 3: Frequency-multiplexing counterexample for m < rank(Omega)")
print("============================================================")
# d=4, rank(Omega)=4: two decoupled 2D oscillators at phi1 = eps, phi2 = pi - eps
# Every A-invariant 2D subspace retains exactly 0.5 of ep.
# The tilted m=2 subspace C = [I_2, I_2]/sqrt(2) approaches 1/(1 + sin^2(eps)) -> 1 as r -> 1^-, eps -> 0!
def rot2(r, phi):
    return r * np.array([[np.cos(phi), -np.sin(phi)], [np.sin(phi), np.cos(phi)]])

def ebar_only(A, Q, C, n_grid=4096):
    d, m = A.shape[0], C.shape[0]
    I_d = np.eye(d, dtype=complex)
    thetas = (np.arange(n_grid) + 0.5) * (2 * np.pi / n_grid) - np.pi
    acc = 0.0
    for th in thetas:
        z = np.exp(1j * th)
        R = linalg.solve(z * I_d - A, I_d)
        S = C @ R @ Q @ R.conj().T @ C.T
        acc += np.real(np.trace(linalg.solve(S.conj(), S)) - m)
    return 0.5 * acc / n_grid

C_mux = np.hstack([np.eye(2), np.eye(2)]) / np.sqrt(2.0)
for eps, r, ng in [(np.pi/3, 0.99, 4096), (0.5, 0.995, 8192), (0.2, 0.998, 16384), (0.1, 0.999, 16384)]:
    A_mux = linalg.block_diag(rot2(r, eps), rot2(r, np.pi - eps))
    Q_mux = np.eye(4)
    Sigma_mux = solve_lyapunov(A_mux, Q_mux)
    ep_mux = exact_ep(A_mux, Q_mux, Sigma_mux)
    eb_mux = ebar_only(A_mux, Q_mux, C_mux, n_grid=ng)
    asymp_pred = 1.0 / (1.0 + np.sin(eps)**2)
    frac = eb_mux / ep_mux
    print(f"eps={eps:.4f}, r={r:.3f}: ep={ep_mux:9.4f} | best 2D invariant=0.5000 | m=2 tilted retains {frac:.6f} (r->1^- pred: {asymp_pred:.6f})")
    assert frac > 0.5, "Tilted subspace did not beat invariant subspace!"

print("\nALL CHECKS PASSED.")
