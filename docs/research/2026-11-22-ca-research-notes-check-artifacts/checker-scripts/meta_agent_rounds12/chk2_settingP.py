r"""Independent brute-force check of C7 (Prop P), C8 (Prop N), C3 (counterexample E2), C3b (sign rule,
EFE corollary, prediction-noise formula).  Own code: joint stationary covariance by Lyapunov, then exact
conditioning on the world path over a window of 2L+1 rounds.

State z = (eta, m_1..m_N), prior means m_i; firm k has n_k members, gains Ks_k, Kc_k (any fixed values),
m^+_i = c0 m_i + (Ks+(n-1)Kc) eta + Ks v_i + Kc sum_{j != i in firm} v_j + Kc nu_i,  Var nu_i = (n-1) Rc
u_i = -g_k m^+_i,  eta' = F eta + b sum_i u_i + w,  m_i' = a_k m^+_i + bhat_k U_k + eps_i (Var se2).
"""
import numpy as np
from scipy.linalg import solve_discrete_lyapunov

rng = np.random.default_rng(20261122)


def build(ns, Ks, Kc, a, bh, g, b, F, Q, R, Rc, se2=0.0):
    N = sum(ns)
    firm = np.repeat(np.arange(len(ns)), ns)
    nx = 1 + 3 * N  # w, v, nu, eps
    Cm = np.zeros((N, N)); Ce = np.zeros(N); D = np.zeros((N, nx))
    for i in range(N):
        k = firm[i]; n = ns[k]
        Cm[i, i] = 1 - Ks[k] - (n - 1) * Kc[k]
        Ce[i] = Ks[k] + (n - 1) * Kc[k]
        D[i, 1 + i] = Ks[k] * np.sqrt(R)
        for j in range(N):
            if firm[j] == k and j != i:
                D[i, 1 + j] = Kc[k] * np.sqrt(R)
        D[i, 1 + N + i] = Kc[k] * np.sqrt((n - 1) * Rc)
    gv = np.array([g[firm[i]] for i in range(N)])
    A = np.zeros((1 + N, 1 + N)); G = np.zeros((1 + N, nx))
    A[0, 0] = F - b * gv @ Ce; A[0, 1:] = -b * gv @ Cm
    G[0, 0] = np.sqrt(Q); G[0] += -b * gv @ D
    for i in range(N):
        k = firm[i]; own = np.where(firm == k)[0]
        A[1 + i, 1:] = a[k] * Cm[i] - bh[k] * (gv[own] @ Cm[own])
        A[1 + i, 0] = a[k] * Ce[i] - bh[k] * (gv[own] @ Ce[own])
        G[1 + i] = a[k] * D[i] - bh[k] * (gv[own] @ D[own])
        G[1 + i, 1 + 2 * N + i] += np.sqrt(se2)
    return A, G @ G.T, firm


def cond_cov(A, Qx, L=80):
    rho = max(abs(np.linalg.eigvals(A)))
    assert rho < 1, rho
    P = solve_discrete_lyapunov(A, Qx)
    d = A.shape[0]
    pw = [np.eye(d)]
    for _ in range(2 * L):
        pw.append(A @ pw[-1])
    T = 2 * L + 1
    See = np.empty((T, T)); Cxe = np.empty((d - 1, T))
    c = np.array([(pw[k] @ P)[0, 0] for k in range(T)])  # Cov(eta_{s+k}, eta_s)
    for i in range(T):
        for j in range(T):
            See[i, j] = c[abs(i - j)]
    for i in range(T):
        s = i - L  # eta at time s, m at time 0
        M = pw[s] @ P if s >= 0 else P @ pw[-s].T  # Cov(z_s, z_0) or Cov(z_s,z_0)= P A^{-s T}
        Cxe[:, i] = M[0, 1:]
    S = P[1:, 1:] - Cxe @ np.linalg.solve(See, Cxe.T)
    return 0.5 * (S + S.T)


def contrast(Pi, C):
    N = Pi.shape[0]; C = list(C); n = len(C)
    out = [k for k in range(N) if k not in C]
    cut_i = -Pi[np.ix_(C, out)].sum(axis=1) if out else np.zeros(n)
    M = Pi[np.ix_(C, C)] - np.diag(cut_i)
    phi = np.ones(n) / np.sqrt(n)
    Pr = np.eye(n) - np.outer(phi, phi)
    ev = np.linalg.eigvalsh(Pr @ M @ Pr + 1e6 * np.outer(phi, phi))
    return ev.min() / (phi @ Pi[np.ix_(C, C)] @ phi)


def closed_form(n, Ks, Kc, F, b, g, Q, R, Rc):
    c0 = 1 - Ks - (n - 1) * Kc
    sx = (Ks + (n - 1) * Kc) ** 2 * R + (n - 1) * Kc ** 2 * Rc
    sp_ = (Ks - Kc) ** 2 * R + (n - 1) * Kc ** 2 * Rc
    phi = F - b * g * n; rho = c0 * phi; s = n * b * b * g * g * sx / Q
    alpha = F * F * sp_ / (1 - F * F * c0 * c0)
    v = phi * phi * sx / np.sqrt((1 + rho ** 2 + s) ** 2 - 4 * rho ** 2)
    Dfb = (phi ** 2 / F ** 2) * (1 - F ** 2 * c0 ** 2) / (1 - phi ** 2 * c0 ** 2)
    Dcoll = (1 - rho ** 2) / np.sqrt((1 + rho ** 2 + s) ** 2 - 4 * rho ** 2)
    return alpha, v, sx / sp_, Dfb, Dcoll, c0, phi, s


print("== C7: single exchangeable collective, arbitrary fixed gains (not only Kalman) ==")
worst = 0.0; worst_planted = np.inf; ndraw = 0; iff_ok = 0
while ndraw < 40:
    n = int(rng.integers(2, 6)); F = rng.uniform(0.3, 0.95) * rng.choice([1, -1]); Q = rng.uniform(0.02, 0.5)
    R = rng.uniform(0.3, 2); Rc = rng.uniform(0.02, 2); b = rng.uniform(0.1, 0.6); g = rng.uniform(-0.3, 0.6)
    Ks = rng.uniform(0.02, 0.5); Kc = rng.uniform(0.01, 0.9 * (1 - Ks) / max(n - 1, 1))
    alpha, v, r0, Dfb, Dcoll, c0, phi, s = closed_form(n, Ks, Kc, F, b, g, Q, R, Rc)
    if abs(F * c0) >= 0.97 or abs(phi) >= 0.97 or abs(phi) < 0.05:
        continue
    A, Qx, firm = build([n], [Ks], [Kc], [F], [b], [g], b, F, Q, R, Rc)
    S = cond_cov(A, Qx, L=90)
    one = np.ones(n) / np.sqrt(n)
    v_num = one @ S @ one; alpha_num = (np.trace(S) - v_num) / (n - 1)
    comp = np.abs(S - (alpha_num * (np.eye(n) - np.outer(one, one)) + v_num * np.outer(one, one))).max()
    worst = max(worst, abs(v_num / v - 1), abs(alpha_num / alpha - 1), comp / S.max())
    # planted error: drop the collider term s
    v_wrong = phi * phi * ((Ks + (n - 1) * Kc) ** 2 * R + (n - 1) * Kc ** 2 * Rc) / (1 - (c0 * phi) ** 2)
    if abs(g) > 0.1:
        worst_planted = min(worst_planted, abs(v_num / v_wrong - 1))
    Pi = np.linalg.inv(S); off = Pi - np.diag(np.diag(Pi))
    diffusive = off.max() <= 1e-9 * Pi.max() and Pi.sum(1).min() >= 0
    r = v / alpha
    iff_ok += (diffusive == (r >= 1))
    assert abs(r - r0 * Dfb * Dcoll) < 1e-10 * r
    if diffusive:
        assert abs(contrast(Pi, range(n)) / r - 1) < 1e-7
    ndraw += 1
print(f" 40 draws: max rel error of (alpha, v, compound symmetry) vs closed form = {worst:.2e}")
print(f" planted error (collider term s dropped), min rel discrepancy over draws with |g|>0.1 = {worst_planted:.2e}")
print(f" 'diffusive iff r>=1' agreed in {iff_ok}/40 draws; r = r0*D_fb*D_coll identity asserted in all")

print("== C8: D_coll<=1 always; D_fb<1 for EFE-consistent gains (bgn = F nc/(1+nc), c>0) ==")
bad = 0; over = 0
for _ in range(20000):
    n = int(rng.integers(2, 8)); F = rng.uniform(-0.99, 0.99); c0 = rng.uniform(-0.99, 0.99)
    c = rng.uniform(1e-4, 5); phi = F / (1 + n * c); s = rng.uniform(0, 3); rho = c0 * phi
    Dfb = (phi ** 2 / F ** 2) * (1 - F ** 2 * c0 ** 2) / (1 - phi ** 2 * c0 ** 2)
    Dcoll = (1 - rho ** 2) / np.sqrt((1 + rho ** 2 + s) ** 2 - 4 * rho ** 2)
    bad += (Dfb >= 1) or (Dcoll > 1 + 1e-12)
    phi2 = rng.uniform(-0.99, 0.99)  # arbitrary (non-EFE) closed loop
    over += (phi2 ** 2 / F ** 2) * (1 - F ** 2 * c0 ** 2) / (1 - phi2 ** 2 * c0 ** 2) > 1
print(f" violations among 20000 EFE-consistent draws: {bad}; control: arbitrary phi gives D_fb>1 in {over}/20000 (exactly when phi^2>F^2)")

print("== C3 counterexample E2 (F=.9,Q=.05,R=1,Rc=.02,b=.2,n=4+4,g=(1.5,.2), exact Kalman gains, each ignores the other) ==")


def kalman(F, Q, info):
    Pm = Q
    for _ in range(200000):
        Pp = 1 / (1 / Pm + info); new = F * F * Pp + Q
        if abs(new - Pm) < 1e-16:
            break
        Pm = new
    return Pm, 1 / (1 / Pm + info)


def two_firm(Rc, g1, g2, F=0.9, Q=0.05, R=1.0, b=0.2, n=4):
    Pm, Pp = kalman(F, Q, 1 / R + (n - 1) / (R + Rc))
    Ks, Kc = Pp / R, Pp / (R + Rc)
    A, Qx, firm = build([n, n], [Ks, Ks], [Kc, Kc], [F, F], [b, b], [g1, g2], b, F, Q, R, Rc)
    S = cond_cov(A, Qx, L=120)
    return np.linalg.inv(S)


for lab, Rc, g1, g2 in [("E2 Rc=0.02", 0.02, 1.5, 0.2), ("E2 Rc=1 (control)", 1.0, 1.5, 0.2), ("E1 Rc=1 g=(.3,.3)", 1.0, 0.3, 0.3)]:
    Pi = two_firm(Rc, g1, g2)
    cross = Pi[:4, 4:]; off = Pi - np.diag(np.diag(Pi))
    dif = off.max() <= 1e-9 * Pi.max() and Pi.sum(1).min() >= 0
    msg = f" {lab}: cross in [{cross.min():+.5f}, {cross.max():+.5f}], max offdiag {off.max():+.4e}, min row sum {Pi.sum(1).min():+.4f}, diffusive={dif}"
    if dif:
        msg += f", r(C1)={contrast(Pi, range(4)):.4f}, r(C2)={contrast(Pi, range(4, 8)):.4f}"
    print(msg)

print("== C3b: sign rule sign(Pi_ij) = sign(phi1 kappa1 phi2 kappa2), no prediction noise ==")
agree = 0; naive_wrong = 0; tot = 0; relerr = 0
while tot < 120:
    ns = [int(rng.integers(2, 5)), int(rng.integers(2, 5))]
    F = rng.uniform(-0.8, 0.8); Q = rng.uniform(0.1, 1); R = rng.uniform(0.5, 2); Rc = rng.uniform(0.2, 2); b = rng.uniform(0.2, 1) * rng.choice([1, -1])
    Ks = rng.uniform(0.05, 0.45, 2); Kc = np.array([rng.uniform(0.02, 0.9 * (1 - Ks[k]) / (ns[k] - 1)) for k in range(2)])
    a = rng.uniform(-0.8, 0.8, 2); bh = rng.uniform(0.2, 1.2, 2) * rng.choice([1, -1], 2); g = rng.uniform(-0.4, 0.4, 2)
    phi = a - bh * g * np.array(ns); kap = b * g * np.sqrt(ns)
    if min(abs(phi)) < 0.05 or min(abs(g)) < 0.03:
        continue
    A, Qx, firm = build(ns, Ks, Kc, a, bh, g, b, F, Q, R, Rc)
    if max(abs(np.linalg.eigvals(A))) > 0.95:
        continue
    S = cond_cov(A, Qx, L=70); Pi = np.linalg.inv(S)
    cross = Pi[:ns[0], ns[0]:]
    if abs(cross).max() < 1e-9 * abs(Pi).max():
        continue
    tot += 1
    pred = np.sign(np.prod(phi) * np.prod(kap))
    agree += np.all(np.sign(cross) == pred)
    naive_wrong += np.any(np.sign(cross) != np.sign(np.prod(kap)))
    # constant cross block = (V^-1)_12 / sqrt(n1 n2)
    P1 = np.zeros((2, sum(ns))); P1[0, :ns[0]] = 1 / np.sqrt(ns[0]); P1[1, ns[0]:] = 1 / np.sqrt(ns[1])
    V = P1 @ S @ P1.T
    relerr = max(relerr, abs(cross - np.linalg.inv(V)[0, 1] / np.sqrt(ns[0] * ns[1])).max() / abs(Pi).max())
print(f" sign rule agrees in {agree}/{tot}; cross block == (V^-1)_12/sqrt(n1 n2) to {relerr:.1e} (rel. to max|Pi|); planted naive rule sign(kappa1 kappa2) wrong in {naive_wrong}/{tot}")

print("== C3b corollary: EFE-consistent gains g = a c/(bhat(1+nc)); sign(phi kappa) = sign(b bhat) ==")
pos = 0; neg = 0; tot = 0
while tot < 60:
    ns = [int(rng.integers(2, 5)), int(rng.integers(2, 5))]
    F = rng.uniform(0.2, 0.8); Q = rng.uniform(0.1, 1); R = rng.uniform(0.5, 2); Rc = rng.uniform(0.2, 2); b = rng.uniform(0.2, 1)
    Ks = rng.uniform(0.05, 0.45, 2); Kc = np.array([rng.uniform(0.02, 0.9 * (1 - Ks[k]) / (ns[k] - 1)) for k in range(2)])
    a = rng.uniform(0.2, 0.8, 2) * rng.choice([1, -1], 2); c = rng.uniform(0.02, 1.0, 2)
    res = []
    for flip in (1, -1):
        bh = np.array([flip * b * rng.uniform(0.5, 1.5), b * rng.uniform(0.5, 1.5)])
        g = a * c / (bh * (1 + np.array(ns) * c))
        A, Qx, firm = build(ns, Ks, Kc, a, bh, g, b, F, Q, R, Rc)
        if max(abs(np.linalg.eigvals(A))) > 0.95:
            break
        Pi = np.linalg.inv(cond_cov(A, Qx, L=70)); cross = Pi[:ns[0], ns[0]:]
        res.append(np.all(cross > 0) if flip == 1 else np.all(cross < 0))
    if len(res) == 2:
        tot += 1; pos += res[0]; neg += res[1]
print(f" both firms know the sign of their effect: cross entries all > 0 in {pos}/{tot}; firm 1 misjudges the sign: all < 0 in {neg}/{tot}")

print("== C3b with prediction noise: V_12 formula and the condition c0>0, phi1 phi2>0 ==")


def v12_formula(ns, Ks, Kc, a, bh, g, b, Q, R, Rc, se2, M=8192):
    ns = np.array(ns); c0 = 1 - Ks - (ns - 1) * Kc
    phi = a - bh * g * ns; kap = b * g * np.sqrt(ns)
    s = (Ks + (ns - 1) * Kc) ** 2 * R + (ns - 1) * Kc ** 2 * Rc
    om = 2 * np.pi * np.arange(M) / M; e = np.exp(-1j * om)
    h = [1 / (1 - c0[k] * phi[k] * e) for k in range(2)]
    So = sum(kap[k] ** 2 * abs(h[k]) ** 2 * (c0[k] ** 2 * se2 + s[k]) for k in range(2)) + Q
    num = np.real((c0[0] * se2 + phi[0] * s[0] * e) * (c0[1] * se2 + phi[1] * s[1] * np.conj(e)))
    return -kap[0] * kap[1] * np.mean(abs(h[0] * h[1]) ** 2 * num / So), c0, phi, kap


err = 0; hold_cond = 0; n_cond = 0; fail_other = 0; n_other = 0; planted = np.inf; tot = 0
while tot < 150:
    ns = [int(rng.integers(2, 5)), int(rng.integers(2, 5))]
    F = rng.uniform(-0.8, 0.8); Q = rng.uniform(0.1, 1); R = rng.uniform(0.5, 2); Rc = rng.uniform(0.2, 2); b = rng.uniform(0.2, 1)
    Ks = rng.uniform(0.05, 0.45, 2); Kc = np.array([rng.uniform(0.02, 0.9 * (1 - Ks[k]) / (ns[k] - 1)) for k in range(2)])
    a = rng.uniform(-0.8, 0.8, 2); bh = rng.uniform(0.2, 1.2, 2); g = rng.uniform(-0.4, 0.4, 2); se2 = rng.uniform(0.1, 6)
    A, Qx, firm = build(ns, Ks, Kc, a, bh, g, b, F, Q, R, Rc, se2)
    if max(abs(np.linalg.eigvals(A))) > 0.9:
        continue
    f, c0, phi, kap = v12_formula(ns, Ks, Kc, a, bh, g, b, Q, R, Rc, se2)
    if min(abs(phi)) < 0.05 or min(abs(g)) < 0.03:
        continue
    S = cond_cov(A, Qx, L=70)
    P1 = np.zeros((2, sum(ns))); P1[0, :ns[0]] = 1 / np.sqrt(ns[0]); P1[1, ns[0]:] = 1 / np.sqrt(ns[1])
    V = P1 @ S @ P1.T
    err = max(err, abs(V[0, 1] - f) / abs(V).max())
    f0, *_ = v12_formula(ns, Ks, Kc, a, bh, g, b, Q, R, Rc, 0.0)  # planted: noise ignored in V_12
    planted = min(planted, abs(V[0, 1] - f0) / abs(V).max())
    rule = np.sign(-V[0, 1]) == np.sign(np.prod(phi) * np.prod(kap))
    if np.all(c0 > 0) and phi[0] * phi[1] > 0:
        n_cond += 1; hold_cond += rule
    else:
        n_other += 1; fail_other += (not rule)
    tot += 1
print(f" formula vs direct V_12: max error {err:.1e} (rel. to max|V|); planted 'noise does not change V_12': min discrepancy {planted:.1e}")
print(f" rule holds in {hold_cond}/{n_cond} draws with c0>0 and phi1 phi2>0; fails in {fail_other}/{n_other} draws outside that condition")
