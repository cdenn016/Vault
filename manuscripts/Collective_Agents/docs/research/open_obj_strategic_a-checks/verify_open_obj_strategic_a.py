"""Two-channel verification script for open:obj-strategic(a).

Channel A: Exact symbolic algebra (SymPy) and exact linear-algebra spectral operators.
Channel B: Direct forward heat-bath Markov-chain simulation from def:obj-quadratic
           and independent Monte Carlo Lyapunov/backward-mixture estimation.
Includes planted-error negative controls verifying every check can fail.
Single-threaded, fixed seeds, double precision + exact rational arithmetic.
"""
from __future__ import annotations

import math
import numpy as np
from numpy.linalg import eigvals, norm, inv
import sympy as sp


def make_A_np(K: np.ndarray, dims: list[int]) -> list[np.ndarray]:
    d = sum(dims)
    offsets = np.cumsum([0] + dims)
    As = []
    for i in range(len(dims)):
        s, e = int(offsets[i]), int(offsets[i + 1])
        Kii = K[s:e, s:e]
        assert np.allclose(Kii, Kii.T, atol=1e-12), f"K_{i}{i} not symmetric"
        assert np.min(np.linalg.eigvalsh(Kii)) > 0, f"K_{i}{i} not SPD"
        Ai = np.eye(d)
        Ai[s:e, :] = -inv(Kii) @ K[s:e, :]
        Ai[s:e, s:e] = 0.0
        As.append(Ai)
    return As


def rho_T_np(As: list[np.ndarray]) -> float:
    n = len(As)
    op = sum(np.kron(A, A) for A in As) / n
    return float(np.max(np.abs(eigvals(op))))


def rho_barA_np(As: list[np.ndarray]) -> float:
    barA = sum(As) / len(As)
    return float(np.max(np.abs(eigvals(barA))))


def lyapunov_mc(As: list[np.ndarray], steps: int = 120000, seed: int = 1) -> float:
    rng = np.random.default_rng(seed)
    n = len(As)
    d = As[0].shape[0]
    v = rng.normal(size=d)
    v /= norm(v)
    acc = 0.0
    for _ in range(steps):
        w = As[int(rng.integers(0, n))] @ v
        nw = norm(w)
        if nw == 0.0:
            return -math.inf
        acc += math.log(nw)
        v = w / nw
    return acc / steps


def simulate_heatbath(
    K: np.ndarray,
    dims: list[int],
    h: np.ndarray,
    gamma: float,
    steps: int,
    burn: int,
    seed: int,
) -> np.ndarray:
    """Direct forward Markov chain from def:obj-quadratic (Channel B)."""
    rng = np.random.default_rng(seed)
    n = len(dims)
    d = sum(dims)
    offsets = np.cumsum([0] + dims)
    Kii_inv = []
    chols = []
    for i in range(n):
        s, e = int(offsets[i]), int(offsets[i + 1])
        Ki_inv = inv(K[s:e, s:e])
        Kii_inv.append(Ki_inv)
        chols.append(np.linalg.cholesky(Ki_inv / gamma))
    u = np.zeros(d)
    out = np.empty((steps, d))
    total = burn + steps
    for t in range(total):
        i = int(rng.integers(0, n))
        s, e = int(offsets[i]), int(offsets[i + 1])
        # Conditional mean: -K_{ii}^{-1} (sum_{j != i} K_{ij} u_j + h_i)
        rhs = K[s:e, :] @ u - K[s:e, s:e] @ u[s:e] + h[s:e]
        mean_i = -Kii_inv[i] @ rhs
        u[s:e] = mean_i + chols[i] @ rng.normal(size=e - s)
        if t >= burn:
            out[t - burn] = u
    return out


def main() -> None:
    print("=================================================================")
    print("VERIFICATION SUITE FOR open:obj-strategic(a)")
    print("=================================================================")

    # -----------------------------------------------------------------
    # 0. Convention lock & registered test instance (prop:obj-protocol(a))
    # -----------------------------------------------------------------
    print("\n[0] Convention lock & registered test instance (n=2 scalar rotation c=0.5, gamma=2)")
    c0, gam0 = 0.5, 2.0
    K0 = np.array([[1.0, c0], [-c0, 1.0]])
    As0 = make_A_np(K0, [1, 1])
    for i, A in enumerate(As0):
        assert norm(A @ A - A) < 1e-14, "A_i not idempotent"
        ei = np.zeros((2, 1)); ei[i, 0] = 1.0
        assert norm(A @ ei) < 1e-14, "A_i E_i != 0"
    rA0 = rho_barA_np(As0)
    rT0 = rho_T_np(As0)
    lam0_exact = 0.25 * math.log(c0**2)
    lam0_mc = lyapunov_mc(As0, steps=150000, seed=10)
    assert abs(rA0 - math.sqrt(1 + c0**2) / 2) < 1e-14
    assert abs(rT0 - (1 + c0**2) / 2) < 1e-14
    assert abs(lam0_mc - lam0_exact) < 3e-3
    print(f"  rho(barA)={rA0:.6f} (exact {math.sqrt(1+c0**2)/2:.6f})")
    print(f"  rho(T)   ={rT0:.6f} (exact {(1+c0**2)/2:.6f})")
    print(f"  lam1_mc  ={lam0_mc:+.6f} vs (1/4)*ln(c^2)={lam0_exact:+.6f}")

    # -----------------------------------------------------------------
    # 1. C3: n=2 vector acts (generic d=(2,3) + counterexample K_{(2,2)})
    # -----------------------------------------------------------------
    print("\n[1] C3: n=2 vector acts (generic d=(2,3) & counterexample K_{(2,2)})")
    rng = np.random.default_rng(2026)
    X1 = rng.normal(size=(2, 2)); K11_g = X1 @ X1.T + 0.5 * np.eye(2)
    X2 = rng.normal(size=(3, 3)); K22_g = X2 @ X2.T + 0.5 * np.eye(3)
    K12_g = rng.normal(size=(2, 3)) * 0.45
    K21_g = rng.normal(size=(3, 2)) * 0.45
    K_g = np.block([[K11_g, K12_g], [K21_g, K22_g]])
    h_g = np.array([0.3, -0.5, 0.2, 0.7, -0.4])
    gam_g = 1.5
    As_g = make_A_np(K_g, [2, 3])
    A12_g = -inv(K11_g) @ K12_g
    A21_g = -inv(K22_g) @ K21_g
    M_g = A12_g @ A21_g
    rM_g = float(np.max(np.abs(eigvals(M_g))))
    rT_g = rho_T_np(As_g)
    lam_g_exact = 0.25 * math.log(rM_g)
    lam_g_mc = lyapunov_mc(As_g, steps=200000, seed=11)
    assert abs(rT_g - (1 + rM_g) / 2) < 1e-13, "rho(T) != (1+rho(M))/2"
    assert abs(lam_g_mc - lam_g_exact) < 5e-3, "lam1_mc mismatch on n=2 vec"
    # Solve discrete Lyapunov for S1, S2:
    Q1_g = (inv(K11_g) + A12_g @ inv(K22_g) @ A12_g.T) / gam_g
    S1_g = inv(np.eye(4) - np.kron(M_g, M_g)) @ Q1_g.reshape(-1)
    S1_g = S1_g.reshape(2, 2)
    S2_g = A21_g @ S1_g @ A21_g.T + inv(K22_g) / gam_g
    Sig1_g = np.block([[S1_g, A12_g @ S2_g], [S2_g @ A12_g.T, S2_g]])
    Sig2_g = np.block([[S1_g, S1_g @ A21_g.T], [A21_g @ S1_g, S2_g]])
    S_mix_g = 0.5 * (Sig1_g + Sig2_g)
    # Check S_mix_g solves S = T(S) + (1/(2*gamma)) K_d^{-1}
    Kd_inv_g = np.block([[inv(K11_g), np.zeros((2, 3))], [np.zeros((3, 2)), inv(K22_g)]])
    T_Smix = 0.5 * (As_g[0] @ S_mix_g @ As_g[0].T + As_g[1] @ S_mix_g @ As_g[1].T) + Kd_inv_g / (2 * gam_g)
    assert norm(S_mix_g - T_Smix) < 1e-13
    # Channel B: forward chain simulation for generic n=2 vector
    uN_g = -inv(K_g) @ h_g
    samp_g = simulate_heatbath(K_g, [2, 3], h_g, gam_g, steps=200000, burn=5000, seed=12)
    emp_mean_g = np.mean(samp_g, axis=0)
    emp_cov_g = np.cov((samp_g - uN_g).T, bias=True)
    # Non-Gaussian 4th moment along direction v = (1, 1, 1, 1, 1)
    v_g = np.ones(5)
    v1_g = float(v_g @ Sig1_g @ v_g)
    v2_g = float(v_g @ Sig2_g @ v_g)
    m4_mix_g = 1.5 * (v1_g**2 + v2_g**2)
    m4_gauss_g = 3.0 * (0.5 * (v1_g + v2_g)) ** 2
    m4_emp_g = float(np.mean(((samp_g - uN_g) @ v_g) ** 4))
    assert norm(emp_mean_g - uN_g) < 0.02
    assert norm(emp_cov_g - S_mix_g) / norm(S_mix_g) < 0.02
    assert abs(m4_emp_g - m4_mix_g) / m4_mix_g < 0.03
    print(f"  generic d=(2,3): rho(M)={rM_g:.6f}, rho(T)={rT_g:.6f}, (1+rho(M))/2={(1+rM_g)/2:.6f}, diff={abs(rT_g-(1+rM_g)/2):.2e}")
    print(f"  generic d=(2,3): lam1_mc={lam_g_mc:+.6f}, exact (1/4)ln rho(M)={lam_g_exact:+.6f}")
    print(f"  generic d=(2,3): Channel B rel cov err={norm(emp_cov_g-S_mix_g)/norm(S_mix_g):.4f}, E[(v.(u-uN))^4] emp={m4_emp_g:.4f} vs mix={m4_mix_g:.4f} (gauss={m4_gauss_g:.4f})")

    # Exact rational SymPy check of K_{(2,2)} (C3(3))
    lam = sp.Symbol("lam")
    z = sp.Symbol("z")
    K4_sym = sp.Matrix([
        [10, 0, 10, 10],
        [0, 1, sp.Rational(1, 2), 1],
        [-sp.Rational(1, 2), -1, 1, 0],
        [10, 10, 0, 10],
    ])
    K11_4, K12_4 = K4_sym[:2, :2], K4_sym[:2, 2:]
    K21_4, K22_4 = K4_sym[2:, :2], K4_sym[2:, 2:]
    M4_sym = K11_4.inv() * K12_4 * K22_4.inv() * K21_4
    assert M4_sym == sp.Matrix([[sp.Rational(1, 2), 0], [sp.Rational(3, 4), sp.Rational(1, 2)]])
    assert M4_sym.eigenvals() == {sp.Rational(1, 2): 2}
    cp4_neg = sp.expand(((-z) * sp.eye(4) - K4_sym).det())
    assert cp4_neg == z**4 + 22 * z**3 + sp.Rational(73, 2) * z**2 - 25 * z + 25
    eigs_K4 = sorted(eigvals(np.array(K4_sym.tolist(), dtype=float)), key=lambda x: x.real)
    assert eigs_K4[0].real < -0.34
    K4_np = np.array(K4_sym.tolist(), dtype=float)
    As4 = make_A_np(K4_np, [2, 2])
    # Exact SymPy spectral radius of T for K_{(2,2)} (Jordan block of size 3 in M4 x M4 has O(eps^{1/3}) fp conditioning)
    A1_4s = sp.eye(4); A1_4s[:2, :] = -K11_4.inv() * K4_sym[:2, :]; A1_4s[:2, :2] = sp.zeros(2, 2)
    A2_4s = sp.eye(4); A2_4s[2:, :] = -K22_4.inv() * K4_sym[2:, :]; A2_4s[2:, 2:] = sp.zeros(2, 2)
    op4_sym = (sp.kronecker_product(A1_4s, A1_4s) + sp.kronecker_product(A2_4s, A2_4s)) / 2
    eigs_T4_sym = op4_sym.eigenvals()
    assert max(abs(ev) for ev in eigs_T4_sym) == sp.Rational(3, 4), f"unexpected eigs {eigs_T4_sym}"
    rT4 = rho_T_np(As4)
    assert abs(rT4 - 0.75) < 1e-4, f"fp Jordan perturbation too large: {rT4}"
    # Channel B check on K_{(2,2)}
    A12_4 = -inv(K4_np[:2, :2]) @ K4_np[:2, 2:]
    A21_4 = -inv(K4_np[2:, 2:]) @ K4_np[2:, :2]
    M4_np = A12_4 @ A21_4
    Q1_4 = inv(K4_np[:2, :2]) + A12_4 @ inv(K4_np[2:, 2:]) @ A12_4.T
    S1_4 = (inv(np.eye(4) - np.kron(M4_np, M4_np)) @ Q1_4.reshape(-1)).reshape(2, 2)
    S2_4 = A21_4 @ S1_4 @ A21_4.T + inv(K4_np[2:, 2:])
    Sig1_4 = np.block([[S1_4, A12_4 @ S2_4], [S2_4 @ A12_4.T, S2_4]])
    Sig2_4 = np.block([[S1_4, S1_4 @ A21_4.T], [A21_4 @ S1_4, S2_4]])
    Smix_4 = 0.5 * (Sig1_4 + Sig2_4)
    samp4 = simulate_heatbath(K4_np, [2, 2], np.zeros(4), 1.0, steps=200000, burn=5000, seed=13)
    emp_cov4 = np.cov(samp4.T, bias=True)
    rel4 = norm(emp_cov4 - Smix_4) / norm(Smix_4)
    assert rel4 < 0.02
    v4 = np.array([1.0, 1.0, 1.0, 1.0])
    m4_4_mix = 1.5 * ((v4 @ Sig1_4 @ v4) ** 2 + (v4 @ Sig2_4 @ v4) ** 2)
    m4_4_gauss = 3.0 * (v4 @ Smix_4 @ v4) ** 2
    m4_4_emp = float(np.mean((samp4 @ v4) ** 4))
    assert abs(m4_4_emp - m4_4_mix) / m4_4_mix < 0.03
    print(f"  K_(2,2): M4 = [[1/2,0],[3/4,1/2]], rho(M4)=1/2, rho(T)={rT4:.6f} (exact 3/4)")
    print(f"  K_(2,2): det((-z)I - K4) = {cp4_neg}, minRe(K4)={eigs_K4[0].real:+.6f}")
    print(f"  K_(2,2): Channel B rel cov err={rel4:.4f}, E[(1.u)^4] emp={m4_4_emp:.2f} vs mix={m4_4_mix:.2f} (gauss={m4_4_gauss:.2f})")

    # -----------------------------------------------------------------
    # 2. C5: n=3 scalar family K(c) = [[1,-c,c],[-1,1,0],[-1,0,1]]
    # -----------------------------------------------------------------
    print("\n[2] C5: Exact symbolic & Channel B analysis of K(c)")
    c = sp.Symbol("c", real=True)
    Kc_sym = sp.Matrix([[1, -c, c], [-1, 1, 0], [-1, 0, 1]])
    assert sp.factor(Kc_sym.charpoly(lam).as_expr()) == (lam - 1) ** 3
    A1_s = sp.Matrix([[0, c, -c], [0, 1, 0], [0, 0, 1]])
    A2_s = sp.Matrix([[1, 0, 0], [1, 0, 0], [0, 0, 1]])
    A3_s = sp.Matrix([[1, 0, 0], [0, 1, 0], [1, 0, 0]])
    assert A2_s * A3_s * A1_s * A2_s * A3_s == sp.zeros(3, 3)
    assert A3_s * A2_s * A1_s * A3_s * A2_s == sp.zeros(3, 3)
    # Verify (A1*A2)^m * e1 = (c^m, c^{m-1}, 0)^T for m = 1..6
    e1_s = sp.Matrix([1, 0, 0])
    for m in range(1, 7):
        vec_m = (A1_s * A2_s) ** m * e1_s
        assert vec_m == sp.Matrix([c**m, c ** (m - 1), 0]), f"mismatch at m={m}"
    # Exact 6x6 matrix of T on Sym_3
    basis = [
        sp.Matrix([[1, 0, 0], [0, 0, 0], [0, 0, 0]]),
        sp.Matrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]]),
        sp.Matrix([[0, 0, 0], [0, 0, 0], [0, 0, 1]]),
        sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]]),
        sp.Matrix([[0, 0, 1], [0, 0, 0], [1, 0, 0]]),
        sp.Matrix([[0, 0, 0], [0, 0, 1], [0, 1, 0]]),
    ]
    def to_vec(M):
        return sp.Matrix([M[0, 0], M[1, 1], M[2, 2], M[0, 1], M[0, 2], M[1, 2]])
    T_sym = sp.zeros(6, 6)
    for j, B in enumerate(basis):
        T_sym[:, j] = to_vec((A1_s * B * A1_s.T + A2_s * B * A2_s.T + A3_s * B * A3_s.T) / 3)
    cp_T = sp.factor(T_sym.charpoly(lam).as_expr())
    assert sp.simplify(cp_T.subs(lam, 1) - sp.Rational(8, 729) * (1 - c**2)) == 0
    rhs_s = sp.Matrix([sp.Rational(1, 3), sp.Rational(1, 3), sp.Rational(1, 3), 0, 0, 0])
    sol_s = sp.simplify((sp.eye(6) - T_sym).LUsolve(rhs_s))
    Sinf_s = sp.Matrix([
        [sol_s[0], sol_s[3], sol_s[4]],
        [sol_s[3], sol_s[1], sol_s[5]],
        [sol_s[4], sol_s[5], sol_s[2]],
    ])
    M1_s = sp.factor(Sinf_s[0, 0])
    M2_s = sp.factor(Sinf_s[:2, :2].det())
    M3_s = sp.factor(Sinf_s.det())
    # Verify numerator of M2 is strictly positive for all real c (completing the square)
    num_M2 = 16 * c**4 - 24 * c**3 + 55 * c**2 - 12 * c + 28
    assert sp.expand(num_M2 - ((4 * c**2 - 3 * c) ** 2 + 46 * (c - sp.Rational(3, 23)) ** 2 + (28 - sp.Rational(18, 23)))) == 0
    print(f"  charpoly(T) at lam=1: {sp.factor(cp_T.subs(lam, 1))}")
    print(f"  Leading principal minors of gamma*S_infty(c):")
    print(f"    M1 = {M1_s}")
    print(f"    M2 = {M2_s}")
    print(f"    M3 = {M3_s}")
    # Check c=0.5 (finite variance) via Channel B
    Kc_half = np.array([[1.0, -0.5, 0.5], [-1.0, 1.0, 0.0], [-1.0, 0.0, 1.0]])
    Sinf_half = np.array(Sinf_s.subs(c, sp.Rational(1, 2)).tolist(), dtype=float)
    samp_half = simulate_heatbath(Kc_half, [1, 1, 1], np.zeros(3), 1.0, steps=250000, burn=5000, seed=14)
    emp_cov_half = np.cov(samp_half.T, bias=True)
    rel_half = norm(emp_cov_half - Sinf_half) / norm(Sinf_half)
    kurt_half = float(np.mean(samp_half[:, 0] ** 4) / (np.mean(samp_half[:, 0] ** 2) ** 2))
    assert rel_half < 0.025
    assert kurt_half > 3.2, f"expected non-Gaussian excess kurtosis, got {kurt_half}"
    print(f"  c=0.5: Channel B rel cov err={rel_half:.4f}, u1 kurtosis={kurt_half:.4f} (Gaussian=3.0)")

    # Check c=2.0 (infinite variance, finite-time coalescence, stationary law exists!)
    Kc_two = np.array([[1.0, -2.0, 2.0], [-1.0, 1.0, 0.0], [-1.0, 0.0, 1.0]])
    As_two = make_A_np(Kc_two, [1, 1, 1])
    rT_two = rho_T_np(As_two)
    assert rT_two > 1.37
    # Backward coalescence time & exact backward-mixture draws over 5000 independent schedules
    rng_b = np.random.default_rng(15)
    coal_times = []
    back_u1 = []
    for _ in range(5000):
        P = np.eye(3)
        S_w = np.zeros((3, 3))
        for k in range(1, 5000):
            idx = int(rng_b.integers(0, 3))
            e = np.zeros((3, 1)); e[idx, 0] = 1.0
            v = P @ e
            S_w += v @ v.T
            P = P @ As_two[idx]
            if norm(P) == 0.0:
                coal_times.append(k)
                back_u1.append(math.sqrt(S_w[0, 0]) * float(rng_b.normal()))
                break
    assert len(coal_times) == 5000
    back_u1_arr = np.array(back_u1)
    q50_back = float(np.quantile(np.abs(back_u1_arr), 0.50))
    q75_back = float(np.quantile(np.abs(back_u1_arr), 0.75))
    # Forward simulation of K(2) to compare against exact backward-mixture quantiles
    samp_two = simulate_heatbath(Kc_two, [1, 1, 1], np.zeros(3), 1.0, steps=150000, burn=2000, seed=16)
    q50 = float(np.quantile(np.abs(samp_two[:, 0]), 0.50))
    q75 = float(np.quantile(np.abs(samp_two[:, 0]), 0.75))
    emp_var_two = float(np.mean(samp_two[:, 0] ** 2))
    assert abs(q50 - q50_back) / q50_back < 0.08, f"q50 mismatch: fwd={q50}, back={q50_back}"
    assert abs(q75 - q75_back) / q75_back < 0.10, f"q75 mismatch: fwd={q75}, back={q75_back}"
    print(f"  c=2.0: rho(T)={rT_two:.6f} > 1, 5000/5000 backward schedules coalesced (mean tau={np.mean(coal_times):.2f}, max tau={np.max(coal_times)})")
    print(f"  c=2.0: Forward vs exact backward mixture quantiles: q50|u1|={q50:.4f} vs {q50_back:.4f}; q75|u1|={q75:.4f} vs {q75_back:.4f}; emp E[u1^2]={emp_var_two:.2f}")

    # Open-set persistence around K(2) with generic full perturbation
    rng_p = np.random.default_rng(17)
    delta_mat = rng_p.normal(size=(3, 3)) * 1e-2
    K_open = Kc_two + delta_mat
    As_open = make_A_np(K_open, [1, 1, 1])
    rT_open = rho_T_np(As_open)
    lam_open = lyapunov_mc(As_open, steps=150000, seed=18)
    assert rT_open > 1.3 and lam_open < -0.1
    print(f"  Open-set generic perturbation of K(2) (scale 1e-2): rho(T)={rT_open:.6f} > 1, lam1_mc={lam_open:+.6f} < 0")

    # -----------------------------------------------------------------
    # 3. C6: Directed n-cycle (n=3, n=4) & infinite Gaussian mixture
    # -----------------------------------------------------------------
    print("\n[3] C6: Directed n-cycle (n=3, n=4)")
    for n_cyc, a_vals in [(3, [0.5, -0.8, 0.6]), (4, [0.6, 0.7, -0.5, 0.9])]:
        K_cyc = np.eye(n_cyc)
        for i in range(n_cyc):
            K_cyc[i, (i + 1) % n_cyc] = -a_vals[i]
        chi_cyc = 1.0
        for a in a_vals:
            chi_cyc *= a
        As_cyc = make_A_np(K_cyc, [1] * n_cyc)
        rT_cyc = rho_T_np(As_cyc)
        rT_pred = (n_cyc - 1 + abs(chi_cyc) ** (2.0 / n_cyc)) / n_cyc
        lam_pred = math.log(abs(chi_cyc)) / (n_cyc**2)
        lam_mc_c = lyapunov_mc(As_cyc, steps=200000, seed=20 + n_cyc)
        assert abs(rT_cyc - rT_pred) < 1e-13
        assert abs(lam_mc_c - lam_pred) < 2e-3
        # Check hierarchy C4: 2*lam1 <= ln(rho(T)) and rho(barA)^2 <= rho(T)
        rA_cyc = rho_barA_np(As_cyc)
        assert 2 * lam_pred <= math.log(rT_cyc) + 1e-12
        assert rA_cyc**2 <= rT_cyc + 1e-12
        print(f"  n={n_cyc} cycle (chi={chi_cyc:+.4f}): rho(T)={rT_cyc:.6f} (pred {rT_pred:.6f}), lam1_mc={lam_mc_c:+.6f} (pred {lam_pred:+.6f})")

    # Exact cylinder-word check for n=3 directed cycle (a1=a2=a3=-1/2, K_{ii}=1, gamma=1)
    K_c3 = np.array([[1.0, 0.5, 0.0], [0.0, 1.0, 0.5], [0.5, 0.0, 1.0]])
    As_c3 = make_A_np(K_c3, [1, 1, 1])
    s_marg = 4.0 / 3.0
    chi_c3 = (-0.5) ** 3
    for m in range(6):
        word = [1, 0, 2, 1, 0, 2] * m + [0] + [1, 2, 0] * 40
        P = np.eye(3); S = np.zeros((3, 3))
        for idx in word:
            e = np.zeros((3, 1)); e[idx, 0] = 1.0
            v = P @ e; S += v @ v.T; P = P @ As_c3[idx]
        pred_12 = (chi_c3 ** (2 * m)) * (-0.5) * s_marg
        assert abs(S[0, 0] - s_marg) < 1e-12
        assert abs(S[0, 1] - pred_12) < 1e-12
    # Channel B check on n=3 directed cycle: Gaussian 1D marginal kurtosis = 3, non-Gaussian joint (u1+u2)
    samp_c3 = simulate_heatbath(K_c3, [1, 1, 1], np.zeros(3), 1.0, steps=250000, burn=5000, seed=25)
    emp_var1 = float(np.mean(samp_c3[:, 0] ** 2))
    kurt_u1 = float(np.mean(samp_c3[:, 0] ** 4) / (emp_var1**2))
    sum12 = samp_c3[:, 0] + samp_c3[:, 1]
    kurt_sum12 = float(np.mean(sum12**4) / (np.mean(sum12**2) ** 2))
    assert abs(emp_var1 - s_marg) < 0.02
    assert abs(kurt_u1 - 3.0) < 0.05
    assert kurt_sum12 > 3.12, f"expected non-Gaussian joint kurtosis > 3.12, got {kurt_sum12}"
    print(f"  n=3 cycle cylinder Sigma_12 = chi^(2m)*a1*s2 verified to <1e-12 for m=0..5")
    print(f"  n=3 cycle Channel B: Var(u1)={emp_var1:.4f} (exact 4/3={s_marg:.4f}), kurt(u1)={kurt_u1:.4f} (~3.0), kurt(u1+u2)={kurt_sum12:.4f} (>3)")

    # -----------------------------------------------------------------
    # 4. C7: n=3 scalar protocol incomparability K_{(3)} = D_{(3)} M_{(3)}
    # -----------------------------------------------------------------
    print("\n[4] C7: n=3 scalar HB-stable & Langevin-unstable K_{(3)}")
    M3_s = sp.Matrix([
        [1, sp.Rational(11, 10), -sp.Rational(1, 4)],
        [sp.Rational(11, 10), 1, sp.Rational(1, 4)],
        [sp.Rational(1, 2), -sp.Rational(1, 2), 1],
    ])
    D3_s = sp.diag(1, 1, sp.Rational(1, 100))
    K3_s = D3_s * M3_s
    cp3 = sp.expand(K3_s.charpoly(lam).as_expr())
    assert sp.simplify(cp3 - (lam - sp.Rational(21, 10)) * (lam**2 + sp.Rational(9, 100) * lam + sp.Rational(3, 2000))) == 0
    assert cp3.subs(lam, 0) == -sp.Rational(63, 20000) < 0
    assert cp3.subs(lam, -sp.Rational(1, 20)) == sp.Rational(43, 40000) > 0
    assert cp3.subs(lam, -sp.Rational(1, 5)) == -sp.Rational(1081, 20000) < 0
    A_M3_s = []
    for i in range(3):
        Ai = sp.eye(3)
        for j in range(3):
            Ai[i, j] = -M3_s[i, j] if j != i else 0
        A_M3_s.append(Ai)
    T3_s = sp.zeros(6, 6)
    for j, B in enumerate(basis):
        TB = sp.zeros(3, 3)
        for Ai in A_M3_s:
            TB += Ai * B * Ai.T
        T3_s[:, j] = to_vec(TB / 3)
    sol3_s = (sp.eye(6) - T3_s).LUsolve(rhs_s)
    S3_s = sp.Matrix([
        [sol3_s[0], sol3_s[3], sol3_s[4]],
        [sol3_s[3], sol3_s[1], sol3_s[5]],
        [sol3_s[4], sol3_s[5], sol3_s[2]],
    ])
    S3_expected = sp.Matrix([
        [sp.Rational(2125, 294), sp.Rational(-645, 98), sp.Rational(-115, 21)],
        [sp.Rational(-645, 98), sp.Rational(2125, 294), sp.Rational(115, 21)],
        [sp.Rational(-115, 21), sp.Rational(115, 21), sp.Rational(166, 21)],
    ])
    assert S3_s == S3_expected
    m1_3, m2_3, m3_3 = S3_s[0, 0], S3_s[:2, :2].det(), S3_s.det()
    assert m1_3 == sp.Rational(2125, 294) > 0
    assert m2_3 == sp.Rational(27550, 3087) > 0
    assert m3_3 == sp.Rational(228950, 7203) > 0
    K3_np = np.array(K3_s.tolist(), dtype=float)
    As3_np = make_A_np(K3_np, [1, 1, 1])
    rT3 = rho_T_np(As3_np)
    eigs_K3 = np.sort(np.real(eigvals(K3_np)))
    assert rT3 < 0.91 and eigs_K3[0] < -0.06
    # Channel B: forward simulation of K_{(3)} (exact S_infty solves (I - T) S = (1/(3*gamma)) D3^{-1})
    rhs3_K = sp.Matrix([sp.Rational(1, 3), sp.Rational(1, 3), sp.Rational(100, 3), 0, 0, 0])
    sol3_K = (sp.eye(6) - T3_s).LUsolve(rhs3_K)
    S3_K_np = np.array([
        [float(sol3_K[0]), float(sol3_K[3]), float(sol3_K[4])],
        [float(sol3_K[3]), float(sol3_K[1]), float(sol3_K[5])],
        [float(sol3_K[4]), float(sol3_K[5]), float(sol3_K[2])],
    ])
    samp3 = simulate_heatbath(K3_np, [1, 1, 1], np.zeros(3), 1.0, steps=300000, burn=10000, seed=26)
    emp_cov3 = np.cov(samp3.T, bias=True)
    rel3 = norm(emp_cov3 - S3_K_np) / norm(S3_K_np)
    assert rel3 < 0.03
    print(f"  K_(3): exact S_infty(M3) leading minors = ({m1_3}, {m2_3}, {m3_3}) > 0")
    print(f"  K_(3): exact charpoly(K3) = (lam - 21/10)*(lam^2 + 9/100*lam + 3/2000)")
    print(f"  K_(3): rho(T)={rT3:.6f} < 1, eigs(K3)={np.round(eigs_K3, 6)} (2 negative real eigs)")
    print(f"  K_(3): Channel B forward chain rel cov err={rel3:.4f}")

    # -----------------------------------------------------------------
    # 5. Planted-error negative controls (every control MUST fail!)
    # -----------------------------------------------------------------
    print("\n[5] Planted-error negative controls")
    # Control 1: Wrong n=2 Lyapunov factor (1/2 instead of 1/4)
    wrong_lam_n2 = 0.5 * math.log(rM_g)
    err_c1 = abs(lam_g_mc - wrong_lam_n2)
    assert err_c1 > 0.1, "Control 1 failed to discriminate"
    print(f"  Control 1 (wrong 1/2 factor in n=2 lam1): |mc - wrong| = {err_c1:.4f} > 0.1 [REJECTED AS EXPECTED]")

    # Control 2: Wrong directed 3-cycle Lyapunov factor (1/n instead of 1/n^2)
    wrong_lam_c3 = math.log(abs(chi_c3)) / 3.0
    lam_c3_mc = lyapunov_mc(As_c3, steps=100000, seed=30)
    err_c2 = abs(lam_c3_mc - wrong_lam_c3)
    assert err_c2 > 0.4, "Control 2 failed to discriminate"
    print(f"  Control 2 (wrong 1/n factor in 3-cycle lam1): |mc - wrong| = {err_c2:.4f} > 0.4 [REJECTED AS EXPECTED]")

    # Control 3: Wrong Gaussian 4th-moment prediction on K_{(2,2)}
    rel_err_c3 = abs(m4_4_emp - m4_4_gauss) / m4_4_gauss
    assert rel_err_c3 > 0.05, "Control 3 failed to discriminate"
    print(f"  Control 3 (Gaussian 4th moment on K_(2,2)): rel err = {rel_err_c3:.4f} > 0.05 [REJECTED AS EXPECTED]")

    # Control 4: Flip sign K_{13} from +2 to -2 in K(2) -> destroys nilpotent reset & flips lam1 > 0
    Kc_broken = np.array([[1.0, -2.0, -2.0], [-1.0, 1.0, 0.0], [-1.0, 0.0, 1.0]])
    As_broken = make_A_np(Kc_broken, [1, 1, 1])
    prod_broken = As_broken[1] @ As_broken[2] @ As_broken[0] @ As_broken[1] @ As_broken[2]
    lam_broken = lyapunov_mc(As_broken, steps=80000, seed=31)
    assert norm(prod_broken) > 1.0 and lam_broken > 0.2, "Control 4 failed to break"
    print(f"  Control 4 (sign flip K_13=-2 in K(2)): ||A2A3A1A2A3||={norm(prod_broken):.4f}, lam1={lam_broken:+.4f} > 0 [BROKEN AS EXPECTED]")

    # Control 5: Remove diagonal scaling in K_{(3)} (set D3 = I) -> Langevin becomes stable
    min_re_M3 = float(np.min(np.real(eigvals(np.array(M3_s.tolist(), dtype=float)))))
    assert min_re_M3 > 0.05, "Control 5 failed to flip Langevin stability"
    print(f"  Control 5 (D3=I in K_(3)): minRe(M3)={min_re_M3:+.6f} > 0 [LANGEVIN RESTORED AS EXPECTED]")

    print("\nALL CHECKS AND NEGATIVE CONTROLS PASSED.")


if __name__ == "__main__":
    main()
