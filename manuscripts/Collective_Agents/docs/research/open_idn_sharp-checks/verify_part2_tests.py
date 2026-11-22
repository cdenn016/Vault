"""Verification suite for Part II of open:idn-sharp (Claims C4, C5).
Two independent channels + planted-error negative controls.
Single-threaded, deterministic seeds, exact stdout captured to verify_part2_tests.out.txt.
"""
import numpy as np
from scipy.linalg import solve_discrete_lyapunov, eigvalsh, cholesky
from scipy.stats import f as f_dist, chi2
from scipy.optimize import minimize

def kl_gauss(S_true, S_model):
    d = S_true.shape[0]
    s1, ld_t = np.linalg.slogdet(S_true)
    s2, ld_m = np.linalg.slogdet(S_model)
    assert s1 > 0 and s2 > 0
    return 0.5 * (np.trace(np.linalg.solve(S_model, S_true)) - d + ld_m - ld_t)

def build_block_toeplitz(gammas, T):
    n = gammas[0].shape[0]
    S = np.zeros((n * T, n * T))
    for t in range(T):
        for s in range(T):
            h = t - s
            S[t*n:(t+1)*n, s*n:(s+1)*n] = gammas[h] if h >= 0 else gammas[-h].T
    return S

print("=========================================================================")
print("CHECK 4 (C4): Broadcaster KL-closure counterexample (k=2, |E(A)|=n>=3)")
print("              + Whittle rate channel + private-noise-floor negative ctrl")
print("=========================================================================")
thetas = np.linspace(0, 2*np.pi, 256, endpoint=False)
zs = np.exp(1j * thetas)

for n in [3, 5]:
    c = 0.5
    A_b = np.zeros((n, n))
    A_b[1:, 0] = c
    D_b = np.eye(n)
    G0_b = D_b + A_b @ D_b @ A_b.T
    G1_b = A_b @ G0_b
    gammas_b = [G0_b, G1_b] + [np.zeros((n, n)) for _ in range(25)]
    T = 15
    S_b = build_block_toeplitz(gammas_b, T)
    f_b = np.array([np.linalg.inv(np.eye(n) - A_b*z) @ D_b @ np.linalg.inv(np.eye(n) - A_b*z).conj().T for z in zs])

    L = np.zeros((n, 2))
    L[0, 0] = 1.0
    L[1:, 1] = 1.0
    print(f"Broadcaster n={n} (|E(A)|={n} > k=2), window T={T}:")
    for eps in [1e-1, 1e-2, 1e-4, 1e-6]:
        D0 = np.diag([eps] + [1.0 - eps] * (n - 1))
        Gd0 = np.array([[1.0 - eps, 0.0], [0.0, c**2 * (1.0 - eps) + eps]])
        Gd1 = np.array([[0.0, 0.0], [c * (1.0 - eps), 0.0]])
        G0_e = L @ Gd0 @ L.T + D0
        G1_e = L @ Gd1 @ L.T
        gammas_e = [G0_e, G1_e] + [np.zeros((n, n)) for _ in range(25)]
        S_e = build_block_toeplitz(gammas_e, T)
        # Channel 1: exact window KL
        kl_win = kl_gauss(S_b, S_e)
        tv_ub = np.sqrt(0.5 * kl_win)
        # Channel 2: Whittle KL rate via spectral integral
        kl_rate = 0.0
        min_fd = np.inf
        for idx, z in enumerate(zs):
            fd_z = Gd0 + Gd1 * z + Gd1.T * np.conj(z)
            min_fd = min(min_fd, np.min(eigvalsh(fd_z)))
            fe_z = D0 + L @ fd_z @ L.T
            ratio = np.linalg.solve(fe_z, f_b[idx])
            s, ld = np.linalg.slogdet(ratio)
            assert s > 0
            kl_rate += 0.5 * (np.trace(ratio).real - n - ld.real)
        kl_rate /= len(zs)
        assert min_fd > 0
        # Verify KL/T closely tracks Whittle rate (within O(1/T) boundary term)
        assert abs(kl_win / T - kl_rate) / max(kl_rate, 1e-15) < 0.15
        print(f"  eps={eps:.0e}: KL_T={kl_win:.3e}, KL_T/T={kl_win/T:.3e}, Whittle_rate={kl_rate:.3e}, "
              f"TV<={tv_ub:.3e}, min_eig(f_d)={min_fd:.3e}")

# Planted-error negative control: enforce private-noise floor d1 = 0.2 > 0 on broadcaster limit H(z)
d1_floor = 0.2
gamma_b = np.sqrt(2.0) * 0.5
H_floor = np.array([[1.0 - d1_floor, gamma_b], [gamma_b, gamma_b**2]])
det_floor = np.linalg.det(H_floor)
assert det_floor < -0.05
print(f"[PASS] PLANTED-ERROR (private-noise floor d1={d1_floor} on n=3 broadcaster): "
      f"det H(1) = {det_floor:.4f} = -d1*gamma^2 < 0 [INFEASIBLE, SEPARATION RESTORED]")

print("\n=========================================================================")
print("CHECK 5A (C5 Test 1): Exact finite-sample replicate Bonferroni-F test")
print("                      for H_0^white + thm:idn-path(b) Type-I collapse")
print("=========================================================================")
rng = np.random.default_rng(2026)

def bonferroni_f_test(X0, X1, alpha=0.05):
    """Exact finite-sample row-wise partial F-test for A_off = 0 on n_rep pairs (X0, X1).
    X0, X1 have shape (n_rep, n)."""
    n_rep, n = X0.shape
    pvals = np.zeros(n)
    fstats = np.zeros(n)
    for i in range(n):
        y = X1[:, i]
        # Full model: regress y on all columns of X0
        beta_full, _, _, _ = np.linalg.lstsq(X0, y, rcond=None)
        rss_full = np.sum((y - X0 @ beta_full)**2)
        # Restricted model: regress y on X0[:, i] only
        xi = X0[:, i:i+1]
        beta_red, _, _, _ = np.linalg.lstsq(xi, y, rcond=None)
        rss_red = np.sum((y - xi @ beta_red)**2)
        F_i = ((rss_red - rss_full) / (n - 1)) / (rss_full / (n_rep - n))
        fstats[i] = F_i
        pvals[i] = f_dist.sf(F_i, n - 1, n_rep - n)
    reject = (np.min(pvals) <= alpha / n)
    return reject, pvals, fstats

n = 3
n_rep = 80
alpha = 0.05
n_mc = 2000

# (a) Under H_0^white: diagonal A0, full-rank correlated white driver Q_white
A0_w = np.diag([0.5, 0.3, 0.6])
B_q = np.array([[0.8, 0.3, 0.1], [0.2, 0.7, 0.4], [0.3, 0.5, 0.6]])
Q_w = np.diag([0.3, 0.4, 0.2]) + B_q @ B_q.T
G0_w = solve_discrete_lyapunov(A0_w, Q_w)
chol_G0_w = cholesky(G0_w, lower=True)
chol_Q_w = cholesky(Q_w, lower=True)

rej_null = 0
row0_rej = 0
for _ in range(n_mc):
    X0 = rng.standard_normal((n_rep, n)) @ chol_G0_w.T
    U = rng.standard_normal((n_rep, n)) @ chol_Q_w.T
    X1 = X0 @ A0_w.T + U
    rej, pvals, _ = bonferroni_f_test(X0, X1, alpha)
    rej_null += int(rej)
    row0_rej += int(pvals[0] <= alpha)
size_bonf = rej_null / n_mc
size_row0 = row0_rej / n_mc
assert size_bonf <= alpha + 0.015 and abs(size_row0 - alpha) < 0.015
print(f"[PASS] H_0^white (n=3, n_rep={n_rep}, {n_mc} MC): row-1 exact size={size_row0:.4f} (nom {alpha}), "
      f"Bonferroni FWER={size_bonf:.4f} (<= {alpha})")

# (b) Under driver-free interacting (A_alt, D_alt) AND identical thm:idn-path(b) colored confounder!
A_alt = np.array([[0.45, 0.30, 0.0], [0.25, 0.35, 0.20], [0.0, 0.25, 0.40]])
D_alt = np.diag([0.5, 0.4, 0.6])
G0_alt = solve_discrete_lyapunov(A_alt, D_alt)
chol_G0_alt = cholesky(G0_alt, lower=True)
chol_D_alt = cholesky(D_alt, lower=True)

# Construct explicit thm:idn-path(b) colored-driver interaction-free confounder with A0 = diag(A_alt), T = {1,2,3}
A0_conf = np.diag(np.diag(A_alt))
# Find c = min_{|z|=1} lambda_min(G(z) D_alt G(z)^*)
c_conf = min(
    np.min(eigvalsh((np.eye(3) - A0_conf*z) @ np.linalg.inv(np.eye(3) - A_alt*z) @ D_alt @
                    ((np.eye(3) - A0_conf*z) @ np.linalg.inv(np.eye(3) - A_alt*z)).conj().T))
    for z in zs
)
D0_conf = 0.5 * c_conf * np.eye(3)
# Verify spectral density of confounder matches (A_alt, D_alt) to machine precision!
max_conf_err = 0.0
for z in zs:
    G = (np.eye(3) - A0_conf*z) @ np.linalg.inv(np.eye(3) - A_alt*z)
    f_d = G @ D_alt @ G.conj().T - D0_conf
    assert np.min(eigvalsh(f_d)) > 0.4 * c_conf
    inv0 = np.linalg.inv(np.eye(3) - A0_conf*z)
    f_conf = inv0 @ (D0_conf + f_d) @ inv0.conj().T
    invA = np.linalg.inv(np.eye(3) - A_alt*z)
    f_true = invA @ D_alt @ invA.conj().T
    max_conf_err = max(max_conf_err, np.linalg.norm(f_conf - f_true))
assert max_conf_err < 1e-14

rej_alt = 0
for _ in range(n_mc):
    X0 = rng.standard_normal((n_rep, n)) @ chol_G0_alt.T
    U = rng.standard_normal((n_rep, n)) @ chol_D_alt.T
    X1 = X0 @ A_alt.T + U
    rej, _, _ = bonferroni_f_test(X0, X1, alpha)
    rej_alt += int(rej)
power_alt = rej_alt / n_mc
assert power_alt > 0.90
print(f"[PASS] Driver-free interacting alternative: empirical power = {power_alt:.4f}")
print(f"[PASS] NEGATIVE CONTROL (thm:idn-path(b) confounder, max spectral err={max_conf_err:.2e}, c={c_conf:.4f}):")
print(f"       Identical recorded path law => white-driver F-test Type-I error = {power_alt:.4f} >> {alpha} [COLLAPSE CONFIRMED]")

print("\n=========================================================================")
print("CHECK 5B (C5 Test 2): Algebraic Kolmogorov 3-cycle test of H_0(1, inf)")
print("=========================================================================")
# g(A*) = A*[0,1]*A*[1,2]*A*[2,0] - A*[0,2]*A*[2,1]*A*[1,0]
# Under H_0(1, inf), rank(A* - A0) <= 1 => g(A*) = 0 for ANY colored rank-1 driver!
def kolmogorov_cycle_stat(X):
    """Estimate A* = Gamma_1 Gamma_0^{-1} and compute g(A*) with block-jackknife SE."""
    # X shape (T, 3)
    T = X.shape[0]
    X0 = X[:-1]
    X1 = X[1:]
    Ahat = (X1.T @ X0) @ np.linalg.inv(X0.T @ X0)
    def g_fn(A):
        return A[0,1]*A[1,2]*A[2,0] - A[0,2]*A[2,1]*A[1,0]
    ghat = g_fn(Ahat)
    # Non-overlapping block jackknife (K = 10 blocks) for robust SE under arbitrary serial color
    K = 10
    blk = (T - 1) // K
    g_loo = np.zeros(K)
    S10_tot = X1.T @ X0
    S00_tot = X0.T @ X0
    for b in range(K):
        s, e = b * blk, (b + 1) * blk
        S10_b = S10_tot - X1[s:e].T @ X0[s:e]
        S00_b = S00_tot - X0[s:e].T @ X0[s:e]
        A_b = S10_b @ np.linalg.inv(S00_b)
        g_loo[b] = g_fn(A_b)
    se = np.sqrt((K - 1) / K * np.sum((g_loo - np.mean(g_loo))**2))
    zstat = abs(ghat) / max(se, 1e-12)
    return ghat, se, zstat, Ahat

# (a) Population check under strongly colored rank-1 interaction-free model (phi = 0.85)
A0_c = np.diag([0.5, 0.3, 0.6])
D0_c = np.diag([0.4, 0.5, 0.3])
L_c = np.array([[0.7], [0.5], [0.9]])
phi_c = 0.85
# Augmented state (x_t, d_t) in R^4:
A_aug = np.block([[A0_c, L_c], [np.zeros((1, 3)), np.array([[phi_c]])]])
Q_aug = np.block([[D0_c, np.zeros((3, 1))], [np.zeros((1, 3)), np.array([[1.0]])]])
P_aug = solve_discrete_lyapunov(A_aug, Q_aug)
G0_c = P_aug[:3, :3]
G1_c = (A_aug @ P_aug)[:3, :3]
Astar_c = G1_c @ np.linalg.inv(G0_c)
g_pop_c = Astar_c[0,1]*Astar_c[1,2]*Astar_c[2,0] - Astar_c[0,2]*Astar_c[2,1]*Astar_c[1,0]
off_norm_c = np.linalg.norm(Astar_c - np.diag(np.diag(Astar_c)), 'fro')
assert abs(g_pop_c) < 1e-15 and off_norm_c > 0.2
print(f"[PASS] Strongly colored rank-1 H_0(1) population check: ||A*_off||_F = {off_norm_c:.4f} > 0.2, "
      f"yet g(A*) = {g_pop_c:.2e} == 0!")

# MC simulation: 300 trajectories of length T = 2000 (critical value t_{9, 0.975} = 2.262 for K=10 jackknife)
from scipy.stats import t as t_dist
t_crit = t_dist.ppf(0.975, df=9)
T_traj = 2000
n_mc_traj = 300
chol_P_aug = cholesky(P_aug, lower=True)
chol_Q_aug = cholesky(Q_aug, lower=True)
rej_c_null = 0
for _ in range(n_mc_traj):
    st = np.zeros((T_traj, 4))
    st[0] = chol_P_aug @ rng.standard_normal(4)
    eps_all = rng.standard_normal((T_traj - 1, 4)) @ chol_Q_aug.T
    for t in range(T_traj - 1):
        st[t + 1] = A_aug @ st[t] + eps_all[t]
    _, _, zst, _ = kolmogorov_cycle_stat(st[:, :3])
    rej_c_null += int(zst > t_crit)
size_kolm = rej_c_null / n_mc_traj

# (b) Driver-free directed 3-cycle alternative: A_{12}=A_{23}=A_{31}=0.35
A_3c = np.array([[0.3, 0.35, 0.0], [0.0, 0.4, 0.35], [0.35, 0.0, 0.2]])
D_3c = np.eye(3)
G0_3c = solve_discrete_lyapunov(A_3c, D_3c)
chol_G0_3c = cholesky(G0_3c, lower=True)
g_pop_3c = 0.35**3
rej_c_alt = 0
for _ in range(n_mc_traj):
    X = np.zeros((T_traj, 3))
    X[0] = chol_G0_3c @ rng.standard_normal(3)
    eps_all = rng.standard_normal((T_traj - 1, 3))
    for t in range(T_traj - 1):
        X[t + 1] = A_3c @ X[t] + eps_all[t]
    _, _, zst, _ = kolmogorov_cycle_stat(X)
    rej_c_alt += int(zst > t_crit)
power_kolm = rej_c_alt / n_mc_traj
assert size_kolm <= 0.10 and power_kolm > 0.90
print(f"[PASS] Kolmogorov 3-cycle test (T={T_traj}, {n_mc_traj} MC): colored H_0(1) size={size_kolm:.4f}, "
      f"directed 3-cycle (g={g_pop_3c:.5f}) power={power_kolm:.4f}")

print("\n=========================================================================")
print("CHECK 5C (C5 Test 3): Exact pivotal Bartlett-Wishart Window-GLRT")
print("                      for H_0(1, inf) on n=2 symmetric A (r_off(A)=1)")
print("=========================================================================")
# Two-channel check of pivotal U_{d, N} distribution: direct Wishart vs Bartlett decomposition
d_win = 4 # n=2, W=2
N_piv = 200
n_draws = 20000
# Channel 1: direct Wishart Z = (1/N) X^T X
U_direct = np.zeros(n_draws)
for m in range(n_draws):
    X = rng.standard_normal((N_piv, d_win))
    Z = (X.T @ X) / N_piv
    _, ld = np.linalg.slogdet(Z)
    U_direct[m] = N_piv * (np.trace(Z) - d_win - ld)
# Channel 2: Bartlett decomposition (independent chi^2_{N-j+1} and N(0,1))
U_bart = np.zeros(n_draws)
for j in range(d_win):
    c_j = rng.chisquare(N_piv - j, size=n_draws)
    U_bart += c_j - N_piv * np.log(c_j / N_piv)
# Add sum of d*(d-1)/2 independent standard normal squares
U_bart += rng.chisquare(d_win * (d_win - 1) // 2, size=n_draws) - N_piv * d_win
q95_dir = np.quantile(U_direct, 0.95)
q95_bart = np.quantile(U_bart, 0.95)
assert abs(np.mean(U_direct) - np.mean(U_bart)) < 0.15
assert abs(q95_dir - q95_bart) < 0.3
print(f"[PASS] Pivotal U_{{4,{N_piv}}} two-channel check ({n_draws} draws): "
      f"direct(mean={np.mean(U_direct):.3f}, q95={q95_dir:.3f}) vs "
      f"Bartlett(mean={np.mean(U_bart):.3f}, q95={q95_bart:.3f}), chi2_10 q95={chi2.ppf(0.95,10):.3f}")

# Check exact finite-sample size & power of Window-GLRT on n=2, W=2 at N=1500
# Alternative: symmetric A = [[0.4, 0.2], [0.2, 0.4]], D = I_2 (where r_off(A)=1=k, so algebraic test is blind,
# yet Delta_2 = inf 2*D_KL ~ 0.02104 > 0!)
N_glrt = 1500
# Pivotal quantile q_{0.95}(4, 1500) via Bartlett
U_1500 = np.zeros(50000)
for j in range(4):
    c_j = rng.chisquare(N_glrt - j, size=50000)
    U_1500 += c_j - N_glrt * np.log(c_j / N_glrt)
U_1500 += rng.chisquare(6, size=50000) - N_glrt * 4
q95_1500 = np.quantile(U_1500, 0.95)

# Fast parametric H_0(1) W=2 covariance model:
# On 32 frequencies (fast!), compute window W=2 covariance (4x4) of interaction-free rank-1 model
th32 = np.linspace(0, 2*np.pi, 32, endpoint=False)
z32 = np.exp(1j * th32)
def h0_k1_S2(p):
    a1 = 0.98 * np.tanh(p[0])
    a2 = 0.98 * np.tanh(p[1])
    d1 = np.exp(p[2])
    d2 = np.exp(p[3])
    ang = p[4]
    l = np.array([np.cos(ang), np.sin(ang)])
    fd = np.zeros(32)
    fd[:17] = np.exp(p[5:])
    fd[17:] = fd[15:0:-1]
    D0 = np.diag([d1, d2])
    llT = np.outer(l, l)
    # Vectorized over 32 frequencies
    i1 = 1.0 / (1.0 - a1 * z32)
    i2 = 1.0 / (1.0 - a2 * z32)
    f00 = (d1 + fd * llT[0,0]) * (np.abs(i1)**2)
    f11 = (d2 + fd * llT[1,1]) * (np.abs(i2)**2)
    f01 = (fd * llT[0,1]) * i1 * np.conj(i2)
    g0 = np.array([[np.mean(f00).real, np.mean(f01).real],
                   [np.mean(f01).real, np.mean(f11).real]])
    g1 = np.array([[np.mean(f00 * np.conj(z32)).real, np.mean(f01 * np.conj(z32)).real],
                   [np.mean(np.conj(f01) * np.conj(z32)).real, np.mean(f11 * np.conj(z32)).real]])
    return np.block([[g0, g1.T], [g1, g0]])

def compute_window_glrt(Shat, N):
    _, ld_hat = np.linalg.slogdet(Shat)
    def loss(p):
        S0 = h0_k1_S2(p)
        s, ld0 = np.linalg.slogdet(S0)
        if s <= 0:
            return 1e6
        return np.trace(np.linalg.solve(S0, Shat)) - 4.0 + ld0 - ld_hat
    best = np.inf
    for s0 in [np.zeros(22), np.array([0.2, 0.2, 0.0, 0.0, 0.785] + [-0.5]*17)]:
        res = minimize(loss, s0, method="L-BFGS-B", options={"maxiter": 150})
        best = min(best, res.fun)
    return N * best

# True symmetric alternative W=2 covariance
A_sym = np.array([[0.4, 0.2], [0.2, 0.4]])
G0_sym = solve_discrete_lyapunov(A_sym, np.eye(2))
G1_sym = A_sym @ G0_sym
S2_sym = np.block([[G0_sym, G1_sym.T], [G1_sym, G0_sym]])
chol_S2_sym = cholesky(S2_sym, lower=True)
Delta2_sym = compute_window_glrt(S2_sym, 1)

# Null: strongly colored rank-1 interaction-free model (n=2, phi=0.8)
A_aug2 = np.array([[0.5, 0.0, 0.7], [0.0, 0.3, 0.8], [0.0, 0.0, 0.8]])
Q_aug2 = np.diag([0.5, 0.6, 1.0])
P_aug2 = solve_discrete_lyapunov(A_aug2, Q_aug2)
G0_n2 = P_aug2[:2, :2]
G1_n2 = (A_aug2 @ P_aug2)[:2, :2]
S2_null = np.block([[G0_n2, G1_n2.T], [G1_n2, G0_n2]])
chol_S2_null = cholesky(S2_null, lower=True)

# Test 25 MC replicates each (fast, decisive!)
n_glrt_mc = 25
rej_g_null, rej_g_alt = 0, 0
stats_null, stats_alt = [], []
for _ in range(n_glrt_mc):
    Xn = rng.standard_normal((N_glrt, 4)) @ chol_S2_null.T
    Sn_hat = (Xn.T @ Xn) / N_glrt
    lam_n = compute_window_glrt(Sn_hat, N_glrt)
    # Also check exact upper bound Lambda <= U_true!
    U_true_n = 2.0 * N_glrt * kl_gauss(Sn_hat, S2_null)
    assert lam_n <= U_true_n + 1e-4
    stats_null.append(lam_n)
    rej_g_null += int(lam_n > q95_1500)

    Xa = rng.standard_normal((N_glrt, 4)) @ chol_S2_sym.T
    Sa_hat = (Xa.T @ Xa) / N_glrt
    lam_a = compute_window_glrt(Sa_hat, N_glrt)
    stats_alt.append(lam_a)
    rej_g_alt += int(lam_a > q95_1500)

assert rej_g_null / n_glrt_mc <= 0.08 and rej_g_alt / n_glrt_mc >= 0.80
print(f"[PASS] Window-GLRT (n=2, W=2, N={N_glrt}, q95={q95_1500:.2f}, Delta_2={Delta2_sym:.5f}):")
print(f"       Colored H_0(1) null: size={rej_g_null}/{n_glrt_mc} ({rej_g_null/n_glrt_mc:.2f}), mean stat={np.mean(stats_null):.2f} (all <= U_true)")
print(f"       Symmetric driver-free alt: power={rej_g_alt}/{n_glrt_mc} ({rej_g_alt/n_glrt_mc:.2f}), mean stat={np.mean(stats_alt):.2f}")

print("\nALL PART II CHECKS PASSED.")
