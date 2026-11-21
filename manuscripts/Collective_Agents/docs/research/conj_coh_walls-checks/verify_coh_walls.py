import numpy as np
from scipy import special, linalg

def brute_force_open(h, J):
    """Channel 2: Exhaustive search over all 2^N spin configurations on open chain."""
    N = len(h)
    assert N <= 14
    best_E = np.inf
    best_sig = None
    second_E = np.inf
    for mask in range(1 << N):
        sig = np.array([1 if (mask >> i) & 1 else -1 for i in range(N)], dtype=np.int8)
        walls = int(np.sum(sig[:-1] != sig[1:]))
        E = J * walls - float(np.dot(h, sig))
        if E < best_E:
            second_E = best_E
            best_E = E
            best_sig = sig
        elif E < second_E:
            second_E = E
    walls = int(np.sum(best_sig[:-1] != best_sig[1:]))
    return best_sig, walls, walls + 1, best_E, second_E - best_E

def brute_force_ring(h, J):
    """Channel 2: Exhaustive search over all 2^N spin configurations on ring (N >= 2)."""
    N = len(h)
    assert 2 <= N <= 14
    best_E = np.inf
    best_sig = None
    for mask in range(1 << N):
        sig = np.array([1 if (mask >> i) & 1 else -1 for i in range(N)], dtype=np.int8)
        walls = int(np.sum(sig != np.roll(sig, -1)))
        E = J * walls - float(np.dot(h, sig))
        if E < best_E:
            best_E = E
            best_sig = sig
    walls = int(np.sum(best_sig != np.roll(best_sig, -1)))
    return best_sig, walls, (walls if walls > 0 else 1), best_E

def viterbi_open(h, J):
    N = len(h)
    Vp = -h[0]; Vm = +h[0]
    pp = np.empty(N, dtype=np.int8); pm = np.empty(N, dtype=np.int8)
    for i in range(1, N):
        if Vp <= Vm + J: nVp = Vp - h[i]; pp[i] = 1
        else: nVp = Vm + J - h[i]; pp[i] = -1
        if Vm <= Vp + J: nVm = Vm + h[i]; pm[i] = -1
        else: nVm = Vp + J + h[i]; pm[i] = 1
        Vp, Vm = nVp, nVm
    sig = np.empty(N, dtype=np.int8)
    sig[N - 1] = 1 if Vp <= Vm else -1
    for i in range(N - 1, 0, -1):
        sig[i - 1] = pp[i] if sig[i] == 1 else pm[i]
    walls = int(np.sum(sig[:-1] != sig[1:]))
    return sig, walls, walls + 1, min(Vp, Vm)

def viterbi_ring(h, J):
    N = len(h)
    best_E = np.inf; best_sig = None
    for s0 in (1, -1):
        Vp = -h[0] if s0 == 1 else np.inf
        Vm = +h[0] if s0 == -1 else np.inf
        pp = np.empty(N, dtype=np.int8); pm = np.empty(N, dtype=np.int8)
        for i in range(1, N):
            if Vp <= Vm + J: nVp = Vp - h[i]; pp[i] = 1
            else: nVp = Vm + J - h[i]; pp[i] = -1
            if Vm <= Vp + J: nVm = Vm + h[i]; pm[i] = -1
            else: nVm = Vp + J + h[i]; pm[i] = 1
            Vp, Vm = nVp, nVm
        Ep = Vp + (0.0 if s0 == 1 else J)
        Em = Vm + (0.0 if s0 == -1 else J)
        E = min(Ep, Em); sl = 1 if Ep <= Em else -1
        if E < best_E:
            best_E = E
            sr = np.empty(N, dtype=np.int8); sr[N - 1] = sl
            for i in range(N - 1, 0, -1): sr[i - 1] = pp[i] if sr[i] == 1 else pm[i]
            best_sig = sr
    walls = int(np.sum(best_sig != np.roll(best_sig, -1)))
    return best_sig, walls, (walls if walls > 0 else 1), best_E

def greedy_hysteresis(h, J):
    N = len(h)
    X = np.zeros(N + 1); X[1:] = np.cumsum(h)
    run_max = 0.0; run_min = 0.0; phase = 0
    switches = []
    for i in range(1, N + 1):
        xi = X[i]
        if phase == 0:
            if xi > run_max:
                run_max = xi
                if run_max - run_min >= J:
                    switches.append((i, +1)); phase = +1; run_max = xi
            elif xi < run_min:
                run_min = xi
                if run_max - run_min >= J:
                    switches.append((i, -1)); phase = -1; run_min = xi
        elif phase == +1:
            if xi > run_max: run_max = xi
            elif run_max - xi >= J:
                switches.append((i, -1)); phase = -1; run_min = xi
        else:
            if xi < run_min: run_min = xi
            elif xi - run_min >= J:
                switches.append((i, +1)); phase = +1; run_max = xi
    return len(switches), switches, X

def predicted_open_domains(h, J, plant_error=None):
    N = len(h)
    halfJ = J if plant_error == "wrong_clip_J" else 0.5 * J
    D = np.empty(N)
    D[0] = h[0]
    for i in range(1, N):
        D[i] = np.clip(D[i - 1], -halfJ, halfJ) + h[i]
    hits = [(idx + 1, 1 if D[idx] > halfJ else -1) for idx in range(N - 1) if abs(D[idx]) > halfJ]
    alt = []
    for idx1, s in hits:
        if not alt or alt[-1][1] != s:
            alt.append((idx1, s))
    M_N = len(alt)
    s_first = alt[0][1] if M_N >= 1 else 0
    s_last = alt[-1][1] if M_N >= 1 else 0
    s_end = 1 if D[N - 1] >= 0 else -1
    psi, switches, X = greedy_hysteresis(h, J)
    if psi == 0:
        return 1 + (1 if (M_N == 1 and s_end == -s_first) else 0), psi, 0, (1 if (M_N == 1 and s_end == -s_first) else 0)
    g1_dir = switches[0][1]
    g_last = switches[-1][0]
    b1_s = s_first if M_N >= 1 else (1 if X[N] > 0 else -1)
    sig_flip = 0 if plant_error == "drop_flip" else (1 if g1_dir == -b1_s else 0)
    sig_end = 0 if plant_error == "drop_end" else (1 if (g_last < N and s_end == -s_last) else 0)
    return psi + sig_flip + sig_end, psi, sig_flip, sig_end

print("============================================================")
print("PART 1: Exact Counterexamples Refuting Literal conj:coh-walls")
print("============================================================")
# CEX 1: N=2, J=1, h=[0.6, -0.6]
h1 = np.array([0.6, -0.6])
s1, w1, d1, E1, gap1 = brute_force_open(h1, 1.0)
psi1, _, _ = greedy_hysteresis(h1, 1.0)
print(f"CEX 1 (N=2, J=1, h=[0.6,-0.6]): unique min={s1.tolist()} (gap={gap1:.2f}), domains={d1}, Psi={psi1}, domains-Psi={d1-psi1}")
assert d1 == 2 and psi1 == 0 and gap1 > 0.1

# CEX 2: N=5, J=1, Psi=1, domains=3 (unique minimizer verified by brute force over 32 states)
h2 = np.array([0.76, -1.13, -0.90, 0.89, -0.21])
s2, w2, d2, E2, gap2 = brute_force_open(h2, 1.0)
psi2, sw2, _ = greedy_hysteresis(h2, 1.0)
print(f"CEX 2 (N=5, J=1, h={h2.tolist()}): unique min={s2.tolist()} (gap={gap2:.3f}), domains={d2}, Psi={psi2}, domains-Psi={d2-psi2}")
assert d2 == 3 and psi2 == 1 and gap2 > 0.05

print("\n============================================================")
print("PART 2: Brute-Force vs Viterbi vs Theorem Bounds & Exact Identity")
print("============================================================")
rng = np.random.default_rng(20261121)
n_bf = 0
for N in [2, 3, 5, 8, 10]:
    for J in [0.7, 1.5]:
        for _ in range(300):
            h = rng.normal(0.0, 1.0, size=N)
            sb, wb, db, _, _ = brute_force_open(h, J)
            sv, wv, dv, _ = viterbi_open(h, J)
            assert wb == wv and db == dv, "Viterbi != brute force (open)!"
            pred_d, psi, sf, se = predicted_open_domains(h, J)
            assert db == pred_d, f"Open identity failed: {db} != {pred_d}"
            assert psi - 1 <= wb <= psi + 1, f"Open wall bound failed: {wb} vs {psi}"

            sbr, wbr, _, _ = brute_force_ring(h, J)
            svr, wvr, _, _ = viterbi_ring(h, J)
            assert wbr == wvr, "Viterbi != brute force (ring)!"
            assert psi - 1 <= wbr <= psi + 1, f"Ring wall bound failed: {wbr} vs {psi}"
            if psi % 2 == 0:
                assert wbr == psi, f"Even-Psi ring equality failed: {wbr} != {psi}"
            n_bf += 1
print(f"PASS Brute-force cross-check ({n_bf} instances, N in {{2,3,5,8,10}}): 0 violations on open chain & ring.")

# Large-N frequency check + negative controls
N_big, J_big, trials_big = 400, 4.0, 1000
counts_diff = {0: 0, 1: 0, 2: 0}
n_flip = 0; n_end = 0
fail_neg = {"wrong_clip_J": 0, "drop_flip": 0, "drop_end": 0}
for _ in range(trials_big):
    h = rng.normal(0.0, 1.0, size=N_big)
    _, _, d_o, _ = viterbi_open(h, J_big)
    pred_d, psi, sf, se = predicted_open_domains(h, J_big)
    assert d_o == pred_d
    counts_diff[d_o - psi] += 1
    n_flip += sf; n_end += se
    for pe in fail_neg:
        pd_bad, _, _, _ = predicted_open_domains(h, J_big, plant_error=pe)
        if pd_bad != d_o:
            fail_neg[pe] += 1

print(f"Large-N (N={N_big}, J={J_big}, {trials_big} trials): open (domains-Psi) = {counts_diff}")
print(f"  Empirical P(sigma_flip=1) = {n_flip/trials_big:.4f}, P(sigma_end=1) = {n_end/trials_big:.4f}, product = {(n_flip/trials_big)*(n_end/trials_big):.4f}")
print(f"  Negative controls (mismatches out of {trials_big}): {fail_neg}")
assert all(v > 100 for v in fail_neg.values()), "Negative control failed to trigger!"

print("\n============================================================")
print("PART 3: Sharp Drawdown Bound (J/h)^2 <= E[T_J] <= (J/h)^2 + ((pi+4)/sqrt(2pi))*(J/h) + 2")
print("============================================================")
# 3a. Verify submartingale drift Delta_alpha(b) >= 1 for alpha = sqrt(pi/8) and negative control
def delta_alpha(b, alpha):
    phi = np.exp(-0.5 * b**2) / np.sqrt(2 * np.pi)
    Phi_bar = 0.5 * special.erfc(b / np.sqrt(2))
    g1 = phi - b * Phi_bar
    g2 = (1 + b**2) * Phi_bar - b * phi
    return 1.0 + 2 * alpha * g1 - g2

alpha_star = np.sqrt(np.pi / 8.0)
b_grid = np.linspace(0.0, 10.0, 10001)
min_drift = float(np.min(delta_alpha(b_grid, alpha_star)))
bad_drift = float(delta_alpha(0.0, 0.9 * alpha_star))
print(f"Submartingale drift min over b in [0,10] at alpha=sqrt(pi/8): {min_drift:.15f} (>= 1)")
print(f"Negative control drift at b=0, alpha=0.9*sqrt(pi/8)         : {bad_drift:.6f} (< 1, violates submartingale)")
assert min_drift >= 1.0 - 1e-15 and bad_drift < 0.99

# 3b. Exact Fredholm integral equation for E[T_J] (h=1, threshold r = J/h)
# m(b) = 1 + Pr(b - Z <= 0) * m(0) + int_0^r m(y) * phi(b - y) dy   for b in [0, r]
# Discretize [0, r] with Gauss-Legendre nodes y_1..y_M plus point y_0 = 0!
def exact_ET_fredholm(r, M=120):
    nodes, weights = np.polynomial.legendre.leggauss(M)
    y = 0.5 * r * (nodes + 1.0)
    w = 0.5 * r * weights
    # Unknown vector u = [m(0), m(y_1), ..., m(y_M)]
    pts = np.concatenate([[0.0], y])
    K = np.zeros((M + 1, M + 1))
    for i, b in enumerate(pts):
        # Probability of reflecting to 0: Pr(Z >= b) = Phi_bar(b)
        K[i, 0] = 0.5 * special.erfc(b / np.sqrt(2.0))
        # Density to land at y_j in (0, r): phi(b - y_j) * w_j
        K[i, 1:] = (np.exp(-0.5 * (b - y)**2) / np.sqrt(2.0 * np.pi)) * w
    u = linalg.solve(np.eye(M + 1) - K, np.ones(M + 1))
    return float(u[0])

c_lin = (np.pi + 4.0) / np.sqrt(2.0 * np.pi)
print(f"\nLinear coefficient (pi+4)/sqrt(2pi) = {c_lin:.6f}")
print(f"{'r=J/h':>6s} | {'Lower r^2':>10s} | {'Exact E[T_J]':>14s} | {'New Upper':>12s} | {'Old Upper':>12s} | {'Quad err':>10s}")
for r in [0.5, 1.0, 2.0, 5.0, 10.0, 20.0]:
    et_120 = exact_ET_fredholm(r, M=120)
    et_200 = exact_ET_fredholm(r, M=200)
    qerr = abs(et_200 - et_120)
    low = r**2
    up_new = r**2 + c_lin * r + 2.0
    up_old = 13.0 * r**2 + 3.25
    print(f"{r:6.1f} | {low:10.4f} | {et_200:14.8f} | {up_new:12.4f} | {up_old:12.4f} | {qerr:10.2e}")
    assert low <= et_200 <= up_new, f"Bound failed at r={r}!"
    assert qerr / et_200 < 1e-11, f"Quadrature not converged at r={r}!"

# 3c. Independent Monte Carlo spot-check at r = 2.0 (20,000 samples)
r_mc = 2.0
rng_mc = np.random.default_rng(999)
ts = np.empty(20000)
for k in range(20000):
    b = 0.0; t = 0
    while b < r_mc:
        b = max(0.0, b - rng_mc.normal())
        t += 1
    ts[k] = t
et_exact_2 = exact_ET_fredholm(2.0, M=140)
mc_mean = float(np.mean(ts)); mc_se = float(np.std(ts) / np.sqrt(len(ts)))
print(f"\nIndependent MC spot check at r=2.0 (20k samples): MC = {mc_mean:.4f} +/- {mc_se:.4f}, Fredholm = {et_exact_2:.6f}, z = {(mc_mean - et_exact_2)/mc_se:+.2f}")
assert abs(mc_mean - et_exact_2) < 4.0 * mc_se

print("\nALL CHECKS PASSED.")
