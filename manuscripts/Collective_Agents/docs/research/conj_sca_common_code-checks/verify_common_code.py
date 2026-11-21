import numpy as np
from scipy import linalg

def build_Wrec_general(Ps, Gammas, J_sets, H_list, Rc):
    """Build homogeneous level-1 reception map W^rec. H_list[j] is sender j's effective code."""
    N = len(Ps); K = Ps[0].shape[0]
    Bs = [H_list[j].T @ linalg.solve(Rc + H_list[j] @ Ps[j] @ H_list[j].T, H_list[j]) for j in range(N)]
    W = np.zeros((N * K, N * K))
    P_plus = []
    for i in range(N):
        Lam_i = linalg.inv(Ps[i])
        Lam_plus = Lam_i + Gammas[i]
        for j in J_sets[i]:
            Lam_plus = Lam_plus + Bs[j]
        Pi_plus = linalg.inv(Lam_plus)
        P_plus.append(Pi_plus)
        W[i*K:(i+1)*K, i*K:(i+1)*K] = Pi_plus @ Lam_i
        for j in J_sets[i]:
            W[i*K:(i+1)*K, j*K:(j+1)*K] = Pi_plus @ Bs[j]
    return W, P_plus

def solve_cov_orbit(Gammas_seq, J_seq, H, Rc, f, Q, max_iter=50000, tol=1e-14):
    p = len(Gammas_seq); N = len(Gammas_seq[0]); K = Q.shape[0]
    H_list = [H] * N
    Ps = [Q / (1.0 - f**2) for _ in range(N)]
    diff = np.inf
    for it in range(1, max_iter + 1):
        Ps_start = [P.copy() for P in Ps]
        Ps_orbit = []
        for t in range(p):
            Ps_orbit.append([P.copy() for P in Ps])
            _, P_plus = build_Wrec_general(Ps, Gammas_seq[t], J_seq[t], H_list, Rc)
            Ps = [f**2 * Pp + Q for Pp in P_plus]
        diff = max(np.max(np.abs(Ps[i] - Ps_start[i])) for i in range(N))
        if diff < tol:
            break
    # Independent check of fixed-point residual on the returned orbit
    Ps_check = [P.copy() for P in Ps_orbit[0]]
    W_prod = np.eye(N * K)
    W_steps = []
    for t in range(p):
        Wt, P_plus = build_Wrec_general(Ps_check, Gammas_seq[t], J_seq[t], H_list, Rc)
        W_steps.append(f * Wt)
        W_prod = (f * Wt) @ W_prod
        Ps_check = [f**2 * Pp + Q for Pp in P_plus]
    orbit_res = max(np.max(np.abs(Ps_check[i] - Ps_orbit[0][i])) for i in range(N))
    eigs = linalg.eigvals(W_prod)
    rho_W = float(np.max(np.abs(eigs)))
    return rho_W, rho_W / (f**p), eigs, W_steps, Ps_orbit, orbit_res, it

def time_domain_growth(W_steps, n_periods=300, seed=0):
    """Channel 2: Direct time-domain propagation of e(t+1) = F W^rec(t) e(t) without eigendecomposition."""
    rng = np.random.default_rng(seed)
    dim = W_steps[0].shape[0]
    e = rng.normal(size=dim)
    e /= np.linalg.norm(e)
    # Burn-in 200 periods, then measure growth over next n_periods
    for _ in range(200):
        for W in W_steps:
            e = W @ e
        e /= np.linalg.norm(e)
    log_sum = 0.0
    for _ in range(n_periods):
        for W in W_steps:
            e = W @ e
        nrm = np.linalg.norm(e)
        log_sum += np.log(nrm)
        e /= nrm
    return float(np.exp(log_sum / n_periods))

print("============================================================")
print("PART 1: Theorem 1 — Frozen Rank-1 Common Code on Directed Graphs")
print("============================================================")
rng = np.random.default_rng(20261121)
max_rho_r1 = 0.0
max_non1_mod = 0.0
n_tested = 0
for N in [2, 3, 4, 5]:
    for K in [2, 3, 4]:
        for _ in range(125):
            Tc = rng.normal(size=(1, K))
            thetas = rng.uniform(0.2, 5.0, size=N)
            H_list = [thetas[j] * Tc for j in range(N)]
            Ps = []
            for _ in range(N):
                A = rng.normal(size=(K, K))
                Ps.append(A @ A.T + 0.02 * np.eye(K))
            Gammas = []
            for _ in range(N):
                r = int(rng.integers(0, K + 1))
                if r == 0:
                    Gammas.append(np.zeros((K, K)))
                else:
                    M = rng.normal(scale=3.0, size=(r, K))
                    Gammas.append(M.T @ M)
            # Random directed listening graph (no self-loops)
            J_sets = [[j for j in range(N) if j != i and rng.random() < 0.5] for i in range(N)]
            W, _ = build_Wrec_general(Ps, Gammas, J_sets, H_list, np.array([[1.0]]))
            eigs = linalg.eigvals(W)
            rho = float(np.max(np.abs(eigs)))
            max_rho_r1 = max(max_rho_r1, rho)
            # Check no eigenvalue on {|lambda| >= 1} \ {1}
            non1 = [abs(z) for z in eigs if abs(z - 1.0) > 1e-9]
            if non1:
                max_non1_mod = max(max_non1_mod, max(non1))
            assert rho <= 1.0 + 1e-11, f"Theorem 1 violated: rho={rho}"
            n_tested += 1

print(f"Tested {n_tested} arbitrary directed rank-1 common-code instances (N=2..5, K=2..4):")
print(f"  max rho(W^rec)                         = {max_rho_r1:.15f} (<= 1)")
print(f"  max |lambda| among lambda != 1         = {max_non1_mod:.10f} (< 1 strictly)")
assert max_rho_r1 <= 1.0 + 1e-11 and max_non1_mod < 1.0

# Negative control for Theorem 1: two distinct rank-1 codes satisfying lem:min-disagreement criterion (P1_12*P2_12 = 9 > P1_22*P2_11 = 1)
P_nc = [np.array([[10.0, 3.0], [3.0, 1.0]]), np.array([[1.0, 3.0], [3.0, 10.0]])]
W_nc, _ = build_Wrec_general(P_nc, [np.zeros((2,2)), np.zeros((2,2))], [[1],[0]],
                             [np.array([[3.0, 0.0]]), np.array([[0.0, 3.0]])], np.array([[1.0]]))
rho_nc = float(np.max(np.abs(linalg.eigvals(W_nc))))
print(f"Negative control (two distinct rank-1 codes): rho(W^rec) = {rho_nc:.6f} (> 1, confirms common-code hypothesis needed)")
assert rho_nc > 1.1

print("\n============================================================")
print("PART 2: Counterexample 1 — Frozen Symmetric 2-Cycle, Common RANK-2 Code (1 fixed sensor/agent)")
print("============================================================")
# Clean round parameters: N=2, K=2, Q=I_2, Rc=I_2, symmetric listening [[1],[0]]
# Common rank-2 code H = diag(10, 0.15), fixed sensors H0^s = (0.5, 0.14), H1^s = (15, 4.6)
H_cex1 = np.diag([10.0, 0.15])
g0_cex1 = np.array([0.5, 0.14])
g1_cex1 = np.array([15.0, 4.6])
G_cex1 = [[np.outer(g0_cex1, g0_cex1), np.outer(g1_cex1, g1_cex1)]]
J_cex1 = [[[1], [0]]]

for f in [0.95, 0.99, 0.9999]:
    rho_W, rho_rec, eigs, W_steps, Ps_orb, res, it = solve_cov_orbit(G_cex1, J_cex1, H_cex1, np.eye(2), f, np.eye(2))
    td_rho = time_domain_growth(W_steps, n_periods=400, seed=1)
    assert res < 1e-13, f"Orbit did not converge: res={res}"
    assert abs(td_rho - rho_W) < 1e-10, f"Time-domain mismatch: {td_rho} vs {rho_W}"
    assert rho_rec > 1.0 + 1e-4, f"Expected rho_rec > 1, got {rho_rec}"
    status_M = "VIOLATES (M): rho(W) > 1!" if rho_W > 1.0 else "violates rho(W) <= f"
    print(f"  f={f:6.4f}: rho(W^rec)={rho_rec:.12f}, rho(W)={rho_W:.12f} (TD={td_rho:.12f}), res={res:.1e} (it={it}) -> {status_M}")

# Negative control on Counterexample 1: make g0, g1 parallel (g0=(0.5, 0.15), g1=(15, 4.5)) -> rho_rec = 1.000000
G_par = [[np.outer([0.5, 0.15], [0.5, 0.15]), np.outer([15.0, 4.5], [15.0, 4.5])]]
_, rho_par, _, _, _, res_par, _ = solve_cov_orbit(G_par, J_cex1, H_cex1, np.eye(2), 0.95, np.eye(2))
print(f"  Control (parallel sensors g0=(0.5,0.15), g1=(15,4.5)): rho(W^rec)={rho_par:.12f} (res={res_par:.1e})")
assert abs(rho_par - 1.0) < 1e-12

print("\n============================================================")
print("PART 3: Counterexample 2 — Period-2 Symmetric 2-Cycle, Common RANK-1 Code (2 world channels/agent)")
print("============================================================")
# Clean mirror-symmetric parameters: N=2, K=2, Q=I_2, Rc=1, common rank-1 code H = [100, 0]
# t=0: both listen [[1],[0]], sensors 200*(1, +0.3) and 200*(1, -0.3)
# t=1: neither listens [[],[]], sensors 100*(1, +0.35) and 100*(1, -0.35)
H_cex2 = np.array([[100.0, 0.0]])
G_cex2 = [
    [np.outer(200.0 * np.array([1.0, 0.3]), 200.0 * np.array([1.0, 0.3])),
     np.outer(200.0 * np.array([1.0, -0.3]), 200.0 * np.array([1.0, -0.3]))],
    [np.outer(100.0 * np.array([1.0, 0.35]), 100.0 * np.array([1.0, 0.35])),
     np.outer(100.0 * np.array([1.0, -0.35]), 100.0 * np.array([1.0, -0.35]))],
]
J_cex2 = [[[1], [0]], [[], []]]

for f in [0.95, 0.99, 0.995]:
    rho_W2, rho_rec2, eigs2, W_steps2, Ps_orb2, res2, it2 = solve_cov_orbit(G_cex2, J_cex2, H_cex2, np.array([[1.0]]), f, np.eye(2))
    td_rho2 = time_domain_growth(W_steps2, n_periods=300, seed=2)
    assert res2 < 1e-13
    assert abs(td_rho2 - rho_W2) < 1e-10
    assert rho_rec2 > 1.01
    status_M = "VIOLATES (M): rho(W^(2)) > 1!" if rho_W2 > 1.0 else "violates rho(W^(2)) <= f^2"
    print(f"  f={f:5.3f}: rho_rec={rho_rec2:.12f}, rho(W^(2))={rho_W2:.12f} (TD={td_rho2:.12f}), per-round={np.sqrt(rho_W2):.10f}, res={res2:.1e} (it={it2}) -> {status_M}")

# Negative control on Counterexample 2: switch off listening (J_seq = [[[],[]], [[],[]]]) -> single-agent Kalman contracts strictly below f^2!
rho_nolis, rho_rec_nolis, _, _, _, res_nl, _ = solve_cov_orbit(G_cex2, [[[],[]], [[],[]]], H_cex2, np.array([[1.0]]), 0.995, np.eye(2))
print(f"  Control (listening switched off, same sensors): rho_rec={rho_rec_nolis:.12f} (< 1, confirms level-1 listening causes amplification)")
assert rho_rec_nolis < 1.0

print("\nALL CHECKS PASSED.")
