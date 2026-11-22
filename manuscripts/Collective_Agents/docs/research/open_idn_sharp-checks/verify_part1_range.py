"""Verification suite for Part I of open:idn-sharp (Claims C1, C2, C3).
Two independent channels + planted-error negative controls.
Single-threaded, deterministic seeds, exact stdout captured to verify_part1_range.out.txt.
"""
import numpy as np
from scipy.linalg import solve_discrete_lyapunov, eigvalsh
from scipy.optimize import minimize, brentq

# ---------------------------------------------------------------------------
# Channel 1 & Channel 2 implementations of Omega_int(A, D; tbar)
# ---------------------------------------------------------------------------
def omega_int_direct(A, d_vec, tbar):
    """Channel 1: Direct block covariance of (x_1, ..., x_tbar) from eq:agy-omega."""
    n = A.shape[0]
    d_vec = np.asarray(d_vec, dtype=float)
    assert np.all(d_vec > 0), f"Inadmissible non-positive D: {d_vec}"
    assert np.max(np.abs(np.linalg.eigvals(A))) < 1.0, "Inadmissible unstable A"
    D = np.diag(d_vec)
    dim = n * tbar
    Apows = [np.eye(n)]
    for _ in range(tbar - 1):
        Apows.append(Apows[-1] @ A)
    L = np.zeros((dim, dim))
    for t in range(tbar):
        for s in range(t + 1):
            L[t*n:(t+1)*n, s*n:(s+1)*n] = Apows[t - s]
    Sigma = L @ np.kron(np.eye(tbar), D) @ L.T
    total = 0.0
    pairs = 0
    for i in range(n):
        idx_i = [t*n + i for t in range(tbar)]
        s_i, ldi = np.linalg.slogdet(Sigma[np.ix_(idx_i, idx_i)])
        assert s_i > 0
        for j in range(i + 1, n):
            idx_j = [t*n + j for t in range(tbar)]
            s_j, ldj = np.linalg.slogdet(Sigma[np.ix_(idx_j, idx_j)])
            assert s_j > 0
            idx_ij = idx_i + idx_j
            s_ij, ldij = np.linalg.slogdet(Sigma[np.ix_(idx_ij, idx_ij)])
            assert s_ij > 0
            total += 0.5 * (ldi + ldj - ldij)
            pairs += 1
    return total / pairs

def omega_int_cholesky_sim(A, d_vec, tbar):
    """Channel 2: Diagonal similarity A_tilde = D^{-1/2} A D^{1/2} with unit noise,
    using agent-major ordering and Cholesky factors."""
    n = A.shape[0]
    sq = np.sqrt(np.asarray(d_vec, dtype=float))
    Atilde = (A / sq[:, None]) * sq[None, :]
    # Build agent-major impulse blocks L_{i, l} of size tbar x tbar
    Apows = [np.eye(n)]
    for _ in range(tbar - 1):
        Apows.append(Apows[-1] @ Atilde)
    # Marginals Sigma^(i) = sum_l L_{i,l} L_{i,l}^T
    Lblocks = [[np.zeros((tbar, tbar)) for _ in range(n)] for _ in range(n)]
    for t in range(tbar):
        for s in range(t + 1):
            M = Apows[t - s]
            for i in range(n):
                for l in range(n):
                    Lblocks[i][l][t, s] = M[i, l]
    Sigma_i = [sum(Lblocks[i][l] @ Lblocks[i][l].T for l in range(n)) for i in range(n)]
    logdet_i = [2.0 * np.sum(np.log(np.diag(np.linalg.cholesky(Si)))) for Si in Sigma_i]
    total = 0.0
    pairs = 0
    for i in range(n):
        for j in range(i + 1, n):
            Sij_off = sum(Lblocks[i][l] @ Lblocks[j][l].T for l in range(n))
            Sij = np.block([[Sigma_i[i], Sij_off], [Sij_off.T, Sigma_i[j]]])
            ldij = 2.0 * np.sum(np.log(np.diag(np.linalg.cholesky(Sij))))
            total += 0.5 * (logdet_i[i] + logdet_i[j] - ldij)
            pairs += 1
    return total / pairs

def omega_int_n2_spectral(A, d_vec, tbar):
    """Channel 2b (n=2): Exact eigenvalue formula 0.5 sum log(1+lam1*r) + 0.5 sum log(1+lam2/r)."""
    assert A.shape == (2, 2)
    Apows = [np.eye(2)]
    for _ in range(tbar - 1):
        Apows.append(Apows[-1] @ A)
    L11, L12, L21, L22 = [np.zeros((tbar, tbar)) for _ in range(4)]
    for t in range(tbar):
        for s in range(t + 1):
            M = Apows[t - s]
            L11[t, s], L12[t, s], L21[t, s], L22[t, s] = M[0, 0], M[0, 1], M[1, 0], M[1, 1]
    B1 = np.linalg.solve(L11, L12)
    B2 = np.linalg.solve(L22, L21)
    lam1 = np.maximum(0.0, eigvalsh(B1 @ B1.T))
    lam2 = np.maximum(0.0, eigvalsh(B2 @ B2.T))
    r = d_vec[1] / d_vec[0]
    val = 0.5 * np.sum(np.log1p(lam1 * r)) + 0.5 * np.sum(np.log1p(lam2 / r))
    return val, lam1, lam2

print("=========================================================================")
print("CHECK 1 (C1): Similarity invariance, n=2 spectral formula, DC & nonconvex")
print("=========================================================================")
rng = np.random.default_rng(2026)
# 1a. Generic asymmetric non-normal matrices: two channels agree to < 1e-13
max_diff_gen = 0.0
for n in [2, 3, 4]:
    for tbar in [2, 4]:
        A = rng.normal(0, 0.3, (n, n))
        sr = np.max(np.abs(np.linalg.eigvals(A)))
        if sr >= 0.85:
            A *= 0.8 / sr
        d = rng.uniform(0.1, 3.0, n)
        c1 = omega_int_direct(A, d, tbar)
        c2 = omega_int_cholesky_sim(A, d, tbar)
        c_scaled = omega_int_direct(A, 7.3 * d, tbar)
        max_diff_gen = max(max_diff_gen, abs(c1 - c2), abs(c1 - c_scaled))
print(f"[PASS] Generic n=2,3,4 two-channel & scale-invariance max diff = {max_diff_gen:.3e}")
assert max_diff_gen < 1e-13

# 1b. n=2 exact spectral formula (tbar=2,3,6) + planted-error negative control
A2 = np.array([[0.45, 0.35], [-0.25, 0.30]]) # asymmetric, non-symmetric, signed
d2 = np.array([0.4, 1.1])
for tbar in [2, 3, 6]:
    v_dir = omega_int_direct(A2, d2, tbar)
    v_spec, lam1, lam2 = omega_int_n2_spectral(A2, d2, tbar)
    assert abs(v_dir - v_spec) < 1e-14
    print(f"  n=2, tbar={tbar}: direct={v_dir:.12f}, spectral={v_spec:.12f}, diff={abs(v_dir-v_spec):.2e}")
# Closed form at tbar=2 + planted error (dropping A12^2 A21^2 cross term)
r2 = d2[1] / d2[0]
v_closed = 0.5 * np.log(1.0 + (A2[0,1]**2)*(A2[1,0]**2) + (A2[0,1]**2)*r2 + (A2[1,0]**2)/r2)
v_wrong = 0.5 * np.log(1.0 + (A2[0,1]**2)*r2 + (A2[1,0]**2)/r2)
v_true2 = omega_int_direct(A2, d2, 2)
assert abs(v_true2 - v_closed) < 1e-15
assert abs(v_true2 - v_wrong) > 2e-3
print(f"  n=2, tbar=2 closed-form err={abs(v_true2-v_closed):.2e}; "
      f"PLANTED-ERROR (drop cross term) err={abs(v_true2-v_wrong):.4e} > 2e-3 [DETECTED]")

# 1c. Analytic closed-form n=3, tbar=2 nonconvexity counterexample
A_nc = np.array([[0.0, 0.5, 0.5], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]])
w1_nc = np.array([0.0, 6.0, -2.0])
w2_nc = np.array([0.0, 6.0, 2.0])
wm_nc = 0.5 * (w1_nc + w2_nc)
f1_nc = omega_int_direct(A_nc, np.exp(w1_nc), 2)
f2_nc = omega_int_direct(A_nc, np.exp(w2_nc), 2)
fm_nc = omega_int_direct(A_nc, np.exp(wm_nc), 2)
# Channel 2 analytic formula for A_nc
def omega_nc_analytic(w):
    a = 0.25 * np.exp(w[1] - w[0])
    x = 0.25 * np.exp(w[2] - w[0])
    return (1.0 / 6.0) * np.log(((1.0 + a + x)**2) / ((1.0 + a) * (1.0 + x)))
assert abs(fm_nc - omega_nc_analytic(wm_nc)) < 1e-14
assert fm_nc > 0.5 * (f1_nc + f2_nc) + 1e-2
print(f"[PASS] n=3, tbar=2 analytic nonconvexity: f(w1)={f1_nc:.6f}, f(w2)={f2_nc:.6f}, "
      f"avg={0.5*(f1_nc+f2_nc):.6f} < f(wm)={fm_nc:.6f} (gap=+{fm_nc-0.5*(f1_nc+f2_nc):.6f})")

# 1d. Explicit n=3, tbar=4 non-quasiconvexity counterexample
rng_q = np.random.default_rng(42)
found_nqc = None
for _ in range(300):
    Aq = rng_q.normal(0, 0.35, (3, 3))
    sr = np.max(np.abs(np.linalg.eigvals(Aq)))
    if sr >= 0.9:
        Aq *= 0.85 / sr
    wa = rng_q.normal(0, 1.5, 3)
    wb = rng_q.normal(0, 1.5, 3)
    wm = 0.5 * (wa + wb)
    fa, fb, fm = [omega_int_direct(Aq, np.exp(w), 4) for w in [wa, wb, wm]]
    if fm > max(fa, fb) + 1e-4:
        # Verify with Channel 2
        fa2, fb2, fm2 = [omega_int_cholesky_sim(Aq, np.exp(w), 4) for w in [wa, wb, wm]]
        assert max(abs(fa-fa2), abs(fb-fb2), abs(fm-fm2)) < 1e-13
        found_nqc = (Aq, wa, wb, fa, fb, fm)
        break
assert found_nqc is not None
Aq, wa, wb, fa, fb, fm = found_nqc
print(f"[PASS] n=3, tbar=4 non-quasiconvexity (two-channel verified): "
      f"f(wa)={fa:.6f}, f(wb)={fb:.6f}, f(wm)={fm:.6f} > max={max(fa,fb):.6f} (gap=+{fm-max(fa,fb):.6f})")

print("\n=========================================================================")
print("CHECK 2 (C2): White-driver exact range, Ray-Projection Collapse,")
print("              n=2 closed form (V1/V2/V3), n=4 chk:idn-bounds, cycles")
print("=========================================================================")
# 2a. n=2 exact closed-form range vs numerical spectrahedron optimization (k=1 and k=2)
Q2 = np.array([[1.2, 0.4], [0.4, 0.9]]) # PD: det = 1.08 - 0.16 = 0.92 > 0
# Test V1 (entrywise v = (0.7, 0.5)), V2/V3 (trace/spectral v = 1.0)
def n2_exact_range(A, Q, tbar, mode, v):
    q1, q2, q12 = Q[0,0], Q[1,1], Q[0,1]
    assert q12 != 0
    if mode == "V1":
        v1, v2 = v
        u1_lo = max(q12**2 / q2, q12**2 / v2)
        u1_hi = min(q1, v1)
        open_lo = (v2 >= q2)
        open_hi = (v1 >= q1)
    elif mode in ("V2", "V3"):
        disc = v**2 - 4.0 * q12**2
        assert disc >= 0
        u1_lo = max(q12**2 / q2, 0.5 * (v - np.sqrt(disc)))
        u1_hi = min(q1, 0.5 * (v + np.sqrt(disc)))
        open_lo = (0.5 * (v - np.sqrt(disc)) <= q12**2 / q2)
        open_hi = (0.5 * (v + np.sqrt(disc)) >= q1)
    assert u1_lo <= u1_hi
    r_of_u = lambda u: (q2 - q12**2 / u) / (q1 - u)
    r_lo = 0.0 if open_lo else r_of_u(u1_lo)
    r_hi = np.inf if open_hi else r_of_u(u1_hi)
    _, lam1, lam2 = omega_int_n2_spectral(A, [1.0, 1.0], tbar)
    f_of_r = lambda r: 0.5 * np.sum(np.log1p(lam1 * r)) + 0.5 * np.sum(np.log1p(lam2 / r))
    # Derivative in u = log r: sum (lam1*r)/(1+lam1*r) - sum lam2/(r+lam2) = 0
    g_prime = lambda u: np.sum(lam1 * np.exp(u) / (1.0 + lam1 * np.exp(u))) - np.sum(lam2 / (np.exp(u) + lam2))
    u_star = brentq(g_prime, -30.0, 30.0)
    r_star = np.exp(u_star)
    r_min_pt = np.clip(r_star, r_lo, r_hi)
    omega_min = f_of_r(r_min_pt)
    omega_max = max(f_of_r(r_lo), f_of_r(r_hi))
    return omega_min, omega_max, r_lo, r_hi, r_star

# Choose A2 with r_star strictly inside (r_lo, r_hi) so interior min attainment is tested!
A2_int = np.array([[0.4, 0.3], [0.25, 0.35]]) # at tbar=2, r* = 0.25/0.3 = 0.8333
for mode, v in [("V1", (0.7, 0.5)), ("V2", 1.05), ("V3", 1.05)]:
    for tbar in [2, 4]:
        omin_th, omax_th, rlo, rhi, rstar = n2_exact_range(A2_int, Q2, tbar, mode, v)
        # Channel 2: direct constrained SLSQP over 2D spectrahedron D in R^2_{>0},
        # Q - D >= 0, var(Q-D) <= v (k=2, NO rank-1 restriction imposed!)
        def var_slack(d):
            M = Q2 - np.diag(d)
            if mode == "V1":
                return np.array([v[0] - M[0,0], v[1] - M[1,1]])
            elif mode == "V2":
                return np.array([v - np.trace(M)])
            else: # V3: lambda_max(M) <= v
                return np.array([v - np.max(eigvalsh(M))])
        cons = [
            {"type": "ineq", "fun": lambda d: np.min(eigvalsh(Q2 - np.diag(d)))},
            {"type": "ineq", "fun": var_slack},
        ]
        bnds = [(1e-6, Q2[0,0] - 1e-6), (1e-6, Q2[1,1] - 1e-6)]
        # Multi-start over feasible points inside k=2 spectrahedron
        starts = [np.array([0.6, 0.5]), np.array([0.8, 0.3]), np.array([0.95, 0.1]),
                  np.array([1.0, 0.05]), np.array([0.55, 0.65]), np.array([0.4, 0.7])]
        omin_num, omax_num = np.inf, -np.inf
        for s0 in starts:
            for sgn in [+1.0, -1.0]:
                res = minimize(lambda d: sgn * omega_int_direct(A2_int, d, tbar), s0,
                               method="SLSQP", bounds=bnds, constraints=cons, options={"ftol": 1e-12, "maxiter": 300})
                if res.success and np.min(eigvalsh(Q2 - np.diag(res.x))) >= -1e-7 and np.all(var_slack(res.x) >= -1e-7):
                    val = omega_int_direct(A2_int, res.x, tbar)
                    omin_num = min(omin_num, val)
                    omax_num = max(omax_num, val)
        assert abs(omin_th - omin_num) < 1e-5, f"{mode} tbar={tbar} min: {omin_th} vs {omin_num}"
        assert abs(omax_th - omax_num) < 1e-5, f"{mode} tbar={tbar} max: {omax_th} vs {omax_num}"
        interior_flag = (rlo < rstar < rhi)
        print(f"  n=2 {mode} tbar={tbar}: exact=[{omin_th:.6f}, {omax_th:.6f}], "
              f"k=2 spectrahedron=[{omin_num:.6f}, {omax_num:.6f}], "
              f"r*={rstar:.4f} in [{rlo:.4f},{rhi:.4f}] (interior_min={interior_flag})")

# 2b. Planted-error negative controls: naive box relaxation & Eckart-Young truncation
# On n=4 chk:idn-bounds model:
A4 = np.array([
    [0.5, 0.2, 0.1, 0.0],
    [0.15, 0.4, 0.25, 0.0],
    [0.0, 0.1, 0.5, 0.3],
    [0.0, 0.0, 0.2, 0.3]
])
d4_true = np.array([0.5, 0.4, 0.3, 0.6])
L4_true = np.array([0.7, 0.5, 0.9, 0.4])
Q4 = np.diag(d4_true) + np.outer(L4_true, L4_true)
v4 = 1.2 * L4_true**2
d4_lo = np.diag(Q4) - v4
# Naive Eckart-Young rank-1 truncation of Q4:
evals, evecs = np.linalg.eigh(Q4)
M_EY1 = evals[-1] * np.outer(evecs[:, -1], evecs[:, -1])
R_EY1 = Q4 - M_EY1
off_EY1 = np.linalg.norm(R_EY1 - np.diag(np.diag(R_EY1)), 'fro')
assert off_EY1 > 0.1
print(f"[PASS] PLANTED-ERROR (Eckart-Young rank-1 of Q4): ||(Q4 - M_EY1)_off||_F = {off_EY1:.4f} > 0.1 [NON-DIAGONAL, INFEASIBLE]")
# Naive box corner D = diag(Q4):
min_eig_box_corner = np.min(eigvalsh(Q4 - np.diag(np.diag(Q4))))
assert min_eig_box_corner < -0.5
print(f"[PASS] PLANTED-ERROR (box corner D=diag(Q4)): min eig(Q4 - D) = {min_eig_box_corner:.4f} < -0.5 [INFEASIBLE]")
# Triad identification for k=1: singleton D4_true!
d4_rec = np.zeros(4)
for i in range(4):
    others = [j for j in range(4) if j != i]
    j, l = others[0], others[1]
    d4_rec[i] = Q4[i,i] - Q4[i,j]*Q4[i,l]/Q4[j,l]
assert np.max(np.abs(d4_rec - d4_true)) < 1e-14
# Compare k=1 singleton vs k=3,4 spectrahedron vs box vs eq:idn-bound (tbar=2)
o_k1 = omega_int_direct(A4, d4_true, 2)
# Compute eq:idn-bound from prop:idn-white(c)
eq_bound_terms = []
for i in range(4):
    for j in range(i+1, 4):
        def rho2(a, b):
            num = (A4[a,b]**2) * d4_lo[b]
            den = num + sum((A4[a,l]**2) * Q4[l,l] for l in range(4) if l != b) + Q4[a,a]
            return num / den
        r2max = max(rho2(i, j), rho2(j, i))
        eq_bound_terms.append(-0.5 * np.log(1.0 - r2max))
o_eq_bound = np.mean(eq_bound_terms)
# Optimize over spectrahedron Q4 - D >= 0, D >= d4_lo (which gives exact k=3 and k=4 range!)
# Use interior point + barrier/SLSQP from multiple feasible starts
def opt_spectrahedron(sign):
    best = np.inf
    best_d = None
    # Feasible starts: d4_true and scaled convex combinations with d4_lo
    starts = [d4_true, 0.5*(d4_true + d4_lo), d4_lo + 0.01*(d4_true - d4_lo)]
    for _ in range(15):
        t = rng.uniform(0.0, 1.0, 4)
        cand = d4_lo + t * (d4_true - d4_lo)
        if np.min(eigvalsh(Q4 - np.diag(cand))) >= 0:
            starts.append(cand)
    cons = [{"type": "ineq", "fun": lambda d: np.min(eigvalsh(Q4 - np.diag(d)))}]
    bnds = [(d4_lo[i], Q4[i,i]) for i in range(4)]
    for s0 in starts:
        res = minimize(lambda d: sign * omega_int_direct(A4, d, 2), s0,
                       method="SLSQP", bounds=bnds, constraints=cons, options={"ftol": 1e-11})
        if res.success and np.min(eigvalsh(Q4 - np.diag(res.x))) >= -1e-8:
            if res.fun < best:
                best = res.fun
                best_d = res.x
    # Verify Ray-Projection Collapse: push best_d to k=3 boundary c_max * best_d
    sq = np.sqrt(best_d)
    cmax = np.min(eigvalsh((Q4 / sq[:, None]) / sq[None, :]))
    d_proj = cmax * best_d
    assert abs(np.min(eigvalsh(Q4 - np.diag(d_proj)))) < 1e-7
    assert np.all(d_proj >= d4_lo - 1e-7)
    assert abs(omega_int_direct(A4, d_proj, 2) - omega_int_direct(A4, best_d, 2)) < 1e-12
    return sign * best, best_d, d_proj

omin_sp, _, _ = opt_spectrahedron(+1.0)
omax_sp, _, _ = opt_spectrahedron(-1.0)
print(f"  n=4 chk:idn-bounds (tbar=2): eq:idn-bound={o_eq_bound:.6f}, "
      f"k=1 exact={o_k1:.6f} (singleton!), k=3,4 exact spectrahedron=[{omin_sp:.6f}, {omax_sp:.6f}]")
assert o_eq_bound < omin_sp <= o_k1 <= omax_sp

# 2c. Unconstrained Cycle Dichotomy + non-attainment on 1 <-> 2 -> 3
# DAG: strictly lower triangular
A_dag = np.array([[0.4, 0.0, 0.0], [0.5, 0.3, 0.0], [0.2, 0.6, 0.2]])
o_dag_small = omega_int_direct(A_dag, [1e-8, 1e-4, 1.0], 3)
assert o_dag_small < 1e-4
print(f"[PASS] Unconstrained DAG (3x3): Omega_int([1e-8, 1e-4, 1], tbar=3) = {o_dag_small:.3e} -> 0")
# 3-cycle: 1 -> 2 -> 3 -> 1 with weights 0.4, 0.5, 0.3 (c_gamma^{1/3} = 0.06^{1/3})
A_cyc = np.array([[0.2, 0.0, 0.3], [0.4, 0.1, 0.0], [0.0, 0.5, 0.3]])
c_gm = (0.4 * 0.5 * 0.3) ** (1.0 / 3.0)
diag_max2 = np.max(np.diag(A_cyc)**2)
lb_cyc = (1.0 / 3.0) * (-0.5 * np.log(1.0 - c_gm**2 / (2.0 * c_gm**2 + diag_max2 + 1.0)))
min_obs_cyc = np.inf
for _ in range(2000):
    w = rng.uniform(-12.0, 12.0, 3)
    min_obs_cyc = min(min_obs_cyc, omega_int_direct(A_cyc, np.exp(w), 2))
assert min_obs_cyc >= lb_cyc - 1e-12
print(f"[PASS] Unconstrained 3-cycle: analytical LB = {lb_cyc:.6f} <= min over 2000 random D (12 orders) = {min_obs_cyc:.6f}")
# Outgoing-tail 1 <-> 2 -> 3: infimum strictly positive yet unattained as D33 -> inf
A_tail = np.array([[0.3, 0.4, 0.0], [0.25, 0.2, 0.0], [0.0, 0.5, 0.1]])
# On {1,2} at tbar=2, exact min is log(1 + |A12 A21|) = log(1.1)
inf_tail_th = (1.0 / 3.0) * np.log(1.0 + 0.4 * 0.25)
r_opt_12 = 0.25 / 0.4
vals_tail = [omega_int_direct(A_tail, [1.0, r_opt_12, d3], 2) for d3 in [1.0, 10.0, 1e3, 1e6, 1e9]]
assert all(vals_tail[i] > vals_tail[i+1] > inf_tail_th for i in range(len(vals_tail)-1))
assert abs(vals_tail[-1] - inf_tail_th) < 1e-7
print(f"[PASS] Outgoing-tail 1<->2->3 (tbar=2): exact inf = {inf_tail_th:.8f}, "
      f"D33=1e9 gives {vals_tail[-1]:.8f} (strictly decreasing, unattained!)")

print("\n=========================================================================")
print("CHECK 3 (C3): Colored drivers — f(z)=I_2 rank-2, pure-source expansion,")
print("              and v_crit Jensen+Weierstrass lower bound")
print("=========================================================================")
thetas = np.linspace(0, 2*np.pi, 256, endpoint=False)
zs = np.exp(1j * thetas)
# 3a. Pure white-noise law f(z) = I_2 realized by interacting model with k=2 colored driver of trace 2*eps
eps = 0.15
delta = eps - eps**2
A_wn = np.array([[0.0, eps], [0.0, 0.0]])
D_wn = np.diag([1.0 - delta, 1.0 - eps**2 / (eps**2 + delta)])
max_spec_err = 0.0
min_fdrv_eig = np.inf
for z in zs:
    H = (np.eye(2) - A_wn * z) @ (np.eye(2) - A_wn * z).conj().T
    f_drv = H - D_wn
    min_fdrv_eig = min(min_fdrv_eig, np.min(eigvalsh(f_drv)))
    inv = np.linalg.inv(np.eye(2) - A_wn * z)
    f_rec = inv @ (D_wn + f_drv) @ inv.conj().T
    max_spec_err = max(max_spec_err, np.linalg.norm(f_rec - np.eye(2)))
tr_M = np.trace(np.eye(2) + A_wn @ A_wn.T - D_wn)
o_wn = omega_int_direct(A_wn, np.diag(D_wn), 2)
assert max_spec_err < 1e-14 and min_fdrv_eig >= -1e-14 and abs(tr_M - 2*eps) < 1e-14 and o_wn > 0
print(f"[PASS] f(z)=I_2 realized by interacting k=2 colored driver: tr(M)={tr_M:.4f}=2*eps, "
      f"min_eig(f_drv)={min_fdrv_eig:.2e}, max||f_rec-I_2||={max_spec_err:.2e}, Omega_int(2)={o_wn:.6f} > 0")

# 3b. Pure-source rank-1 colored expansion at tbar=3 (exceeds white rank-1 range!)
A_src = np.array([[0.5, 0.3], [0.0, 0.4]])
D_src = np.diag([0.5, 0.6])
# Colored rank-1 driver on pure source (agent 2): changes A22 from 0.4 -> 0.65 (or 0.7) with D22 = 0.1
A_col = np.array([[0.5, 0.3], [0.0, 0.65]])
D_col = np.diag([0.5, 0.1])
# Check spectral match on circle: f_drv(z) supported on e_2 and strictly positive!
min_f22 = np.inf
max_out = 0.0
for z in zs:
    G = (np.eye(2) - A_col * z) @ np.linalg.inv(np.eye(2) - A_src * z)
    M = G @ D_src @ G.conj().T - D_col
    max_out = max(max_out, abs(M[0,0]), abs(M[0,1]), abs(M[1,0]))
    min_f22 = min(min_f22, M[1,1].real)
# Driver variance on agent 2:
G0_src = solve_discrete_lyapunov(A_src, D_src)
G1_src = A_src @ G0_src
Q_ar_col = G0_src - A_col @ G1_src.T - G1_src @ A_col.T + A_col @ G0_src @ A_col.T
var_col = Q_ar_col[1,1] - D_col[1,1]
# Compare Omega_int(tbar=3) at the SAME ratio D22/D11 = 0.1/0.5 = 0.2:
o_white_t3 = omega_int_direct(A_src, [0.5, 0.1], 3)
o_col_t3 = omega_int_direct(A_col, [0.5, 0.1], 3)
# Also test A22 = 0.0 with D22 = 0.2 (reduces source persistence, strictly lowers Omega_int at tbar=3!)
A_col_zero = np.array([[0.5, 0.3], [0.0, 0.0]])
D_col_zero = np.diag([0.5, 0.2])
min_f22_zero = min(((np.eye(2) - A_col_zero*z) @ np.linalg.inv(np.eye(2) - A_src*z) @ D_src @
                   ((np.eye(2) - A_col_zero*z) @ np.linalg.inv(np.eye(2) - A_src*z)).conj().T - D_col_zero)[1,1].real
                   for z in zs)
o_col_zero_t3 = omega_int_direct(A_col_zero, [0.5, 0.2], 3)
o_white_zero_t3 = omega_int_direct(A_src, [0.5, 0.2], 3)
assert max_out < 1e-14 and min_f22 > 0.05 and abs(o_col_t3 - o_white_t3) > 1e-3
assert min_f22_zero > 0.05 and o_col_zero_t3 < o_white_zero_t3 - 1e-3
print(f"[PASS] Pure-source k=1 colored expansion: outside-(2,2) err={max_out:.2e}, min f_d(z)={min_f22:.4f}, "
      f"var_2={var_col:.4f}")
print(f"       Omega_int(tbar=3) at D=(0.5,0.1): white(A22=0.4)={o_white_t3:.6f} vs colored(A22=0.65)={o_col_t3:.6f}")
print(f"       Omega_int(tbar=3) at D=(0.5,0.2): white(A22=0.4)={o_white_zero_t3:.6f} vs colored(A22=0.0)={o_col_zero_t3:.6f} (min_f22={min_f22_zero:.4f})")

# 3c. v_crit_trace analytical Jensen+Weierstrass lower bound vs grid-exact optimum
for name, A, d_vec in [
    ("symmetric", np.array([[0.4, 0.25], [0.25, 0.4]]), np.array([0.5, 0.5])),
    ("asymmetric", np.array([[0.5, 0.3], [0.1, 0.3]]), np.array([0.4, 0.7])),
    ("unidirectional", np.array([[0.5, 0.35], [0.0, 0.4]]), np.array([0.5, 0.6])),
]:
    D = np.diag(d_vec)
    G0 = solve_discrete_lyapunov(A, D)
    A_off = A - np.diag(np.diag(A))
    eta = np.min(eigvalsh(G0)) * np.sum((A_off**2) / d_vec[:, None])
    lb = np.min(d_vec) * eta / (1.0 + eta)
    # Verify on a 15x15 A0 grid that EVERY interaction-free model has tr(M) > lb
    zs_half = np.exp(1j * np.linspace(0, np.pi, 129))
    min_trM = np.inf
    for a1 in np.linspace(-0.7, 0.85, 15):
        for a2 in np.linspace(-0.7, 0.85, 15):
            A0 = np.diag([a1, a2])
            Q_AR = D + (A0 - A) @ G0 @ (A0 - A).T
            h11, h22, h12sq = [], [], []
            for z in zs_half:
                G = (np.eye(2) - A0 * z) @ np.linalg.inv(np.eye(2) - A * z)
                H = G @ D @ G.conj().T
                h11.append(H[0,0].real); h22.append(H[1,1].real); h12sq.append(abs(H[0,1])**2)
            h11, h22, h12sq = np.array(h11), np.array(h22), np.array(h12sq)
            d1s = np.linspace(1e-5, np.min(h11) - 1e-5, 100)
            best_trD0 = max(d1 + np.min(h22 - h12sq / (h11 - d1)) for d1 in d1s)
            if best_trD0 > 0:
                min_trM = min(min_trM, np.trace(Q_AR) - best_trD0)
    assert min_trM > lb > 0
    print(f"[PASS] v_crit_trace ({name:14s}): grid_opt={min_trM:.6f} > Jensen+Weierstrass LB={lb:.6f} > 0")

print("\nALL PART I CHECKS PASSED.")
