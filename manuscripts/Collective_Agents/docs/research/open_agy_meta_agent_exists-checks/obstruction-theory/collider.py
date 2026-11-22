"""Part (2): collider lemma for performative populations.

Agents' states given the world path: x_{t+1} = A x_t + (known input) + xi_t, xi ~ N(0,Q).
World equation read as an observation of the agents: y_t = eta_{t+1} - F eta_t - (known)
= b^T x_t + omega_t, omega ~ N(0,q) (world innovation plus unstored act noise).
World-conditional one-time covariance Sigma^c = Cov(x_t | eta_Z).
"""
import numpy as np
from scipy.linalg import solve_discrete_are, solve_discrete_lyapunov
from common import is_diffusive

rng = np.random.default_rng(7)
ok_all = True


def report(name, expect, got):
    global ok_all
    flag = "PASS" if expect == got else "FAIL"
    if expect != got:
        ok_all = False
    print(f"[{flag}] {name}: expected {expect}, got {got}")


def sigma_c_spectral(A, Q, b, q, M=4096):
    N = A.shape[0]
    Qi = np.linalg.inv(Q)
    BB = np.outer(b, b) / q
    acc = np.zeros((N, N), dtype=complex)
    for th in 2 * np.pi * np.arange(M) / M:
        E = np.exp(1j * th) * np.eye(N) - A
        P = E.conj().T @ Qi @ E + BB
        acc += np.linalg.inv(P)
    return (acc / M).real


def sigma_c_rts(A, Q, b, q):
    """Steady-state fixed-interval smoother covariance for x_{t+1}=Ax_t+xi, y_t=b^T x_t+omega."""
    N = A.shape[0]
    bb = b.reshape(N, 1)
    Pp = solve_discrete_are(A.T, bb, Q, np.array([[q]]))
    S = (bb.T @ Pp @ bb).item() + q
    Pf = Pp - Pp @ bb @ bb.T @ Pp / S
    J = Pf @ A.T @ np.linalg.inv(Pp)
    Ps = solve_discrete_lyapunov(J, Pf - J @ Pp @ J.T)
    return 0.5 * (Ps + Ps.T)


def sigma_0(A, Q):
    return solve_discrete_lyapunov(A, Q)


def random_component(n, signed=False, reversible=False):
    if reversible:
        X = rng.uniform(0, 1, (n, n)) if not signed else rng.normal(size=(n, n))
        X = 0.5 * (X + X.T)
        if not signed:
            np.fill_diagonal(X, rng.uniform(0, 1, n))
        A = X / (np.abs(np.linalg.eigvals(X)).max() + 1e-9) * rng.uniform(0.3, 0.9)
        Qd = np.ones(n) * rng.uniform(0.2, 2.0)   # isotropic noise -> A Q = Q A^T
        return A, Qd
    if signed:
        X = rng.normal(size=(n, n))
    else:
        X = rng.uniform(0, 1, (n, n)) * (rng.uniform(size=(n, n)) < 0.8)
    # normalize by max(spectral radius, 0.3*operator norm) to avoid blowing up near-nilpotent draws
    scale = max(np.abs(np.linalg.eigvals(X)).max(), 0.3 * np.linalg.norm(X, 2), 1e-3)
    A = X / scale * rng.uniform(0.3, 0.92)
    Qd = rng.uniform(0.1, 2.0, n)
    return A, Qd


def assemble(comps):
    N = sum(c[0].shape[0] for c in comps)
    A = np.zeros((N, N)); Qd = np.zeros(N); blocks = []; i = 0
    for Ac, Qc in comps:
        k = Ac.shape[0]
        A[i:i + k, i:i + k] = Ac; Qd[i:i + k] = Qc; blocks.append(list(range(i, i + k))); i += k
    return A, np.diag(Qd), blocks


# ---------------- validation: spectral vs RTS ----------------
err = 0.0
for _ in range(20):
    A, Q, bl = assemble([random_component(2), random_component(2)])
    b = rng.uniform(0.1, 1.0, A.shape[0]); q = rng.uniform(0.1, 2.0)
    err = max(err, np.abs(sigma_c_spectral(A, Q, b, q, 2048) - sigma_c_rts(A, Q, b, q)).max())
report("spectral integral equals RTS smoother covariance (20 draws, err<1e-8)", True, err < 1e-8)
print(f"   max abs difference {err:.2e}")

# ---------------- ex:agy-collider instance (s05_agency.tex:240-242) ----------------
A = 0.4 * np.eye(3); Q = 0.25 * np.eye(3); b = np.array([0.30, 0.25, 0.0]); q = 1.0
Sc = sigma_c_rts(A, Q, b, q); Pc = np.linalg.inv(Sc)
print("   ex:agy-collider Pi^c =\n", np.round(Pc, 6))
report("ex:agy-collider: Pi^c_12 > 0 and Pi^c_13 = Pi^c_23 = 0", (True, True),
       (bool(Pc[0, 1] > 0), bool(abs(Pc[0, 2]) < 1e-10 and abs(Pc[1, 2]) < 1e-10)))
# window MI as in the example, conditioning on world path and initial state, T=6 rounds
def window_mi(T):
    # variables: p1(0..T-1), p2(0..T-1), w(0..T-1); initial state conditioned (set to 0)
    # mu_i(t) = sum_{s<t} 0.4^{t-1-s} 0.5 p_i(s); eta(t+1)-0.9 eta(t) = 0.3 mu1(t)+0.25 mu2(t)+w(t)
    nv = 3 * T
    L = np.zeros((2 * T + T, nv))   # rows: mu1(1..T), mu2(1..T), y(0..T-1)
    for t in range(1, T + 1):
        for s in range(t):
            L[t - 1, s] = 0.4 ** (t - 1 - s) * 0.5
            L[T + t - 1, T + s] = 0.4 ** (t - 1 - s) * 0.5
    for t in range(T):
        for s in range(t):
            L[2 * T + t, s] += 0.30 * 0.4 ** (t - 1 - s) * 0.5
            L[2 * T + t, T + s] += 0.25 * 0.4 ** (t - 1 - s) * 0.5
        L[2 * T + t, 2 * T + t] = 1.0
    C = L @ L.T
    i1, i2, iy = list(range(T)), list(range(T, 2 * T)), list(range(2 * T, 3 * T))
    def cond(idx):
        return C[np.ix_(idx, idx)] - C[np.ix_(idx, iy)] @ np.linalg.solve(C[np.ix_(iy, iy)], C[np.ix_(iy, idx)])
    S12 = cond(i1 + i2)
    return 0.5 * (np.linalg.slogdet(S12[:T, :T])[1] + np.linalg.slogdet(S12[T:, T:])[1] - np.linalg.slogdet(S12)[1])
print(f"   window MI given world path and X0, T=6: {window_mi(6):.3e} nats (manuscript: 1.39e-3)")

# ---------------- Theorem C (non-communicating scalar actors) ----------------
viol = 0
for _ in range(300):
    N = rng.integers(2, 7)
    c = rng.uniform(-0.9, 0.9, N); Qd = rng.uniform(0.1, 2.0, N)
    b = rng.uniform(0.05, 1.0, N); q = rng.uniform(0.05, 2.0)
    Sc = sigma_c_rts(np.diag(c), np.diag(Qd), b, q); Pc = np.linalg.inv(Sc)
    off = Pc[~np.eye(N, dtype=bool)]
    offS = Sc[~np.eye(N, dtype=bool)]
    if not (off.min() > 0 and offS.max() < 0):
        viol += 1
report("THM: non-communicating scalar actors, one-sign loadings: Sigma^c offdiag<0 and Pi^c offdiag>0 (violations/300)", 0, viol)

# ---------------- exact one-time decomposition Pi^c = Pi_0 + b b^T/q + I_other, I_other PSD ----------------
mineig = np.inf
for _ in range(200):
    A, Q, bl = assemble([random_component(rng.integers(1, 4), signed=True), random_component(rng.integers(1, 4), signed=True)])
    N = A.shape[0]
    b = rng.normal(size=N); q = rng.uniform(0.05, 2.0)
    Pc = np.linalg.inv(sigma_c_rts(A, Q, b, q)); P0 = np.linalg.inv(sigma_0(A, Q))
    Iother = Pc - P0 - np.outer(b, b) / q
    mineig = min(mineig, np.linalg.eigvalsh(0.5 * (Iother + Iother.T)).min())
report("exact decomposition: I_other = Pi^c - Pi_0 - bb^T/q is PSD (200 signed draws)", True, mineig > -1e-8)
print(f"   min eigenvalue of I_other over draws: {mineig:.3e}")

# ---------------- Theorem (collider obstruction): two components, no common ancestor ----------------
def run_two(signed, reversible, ndraw=400):
    stats = dict(agg_neg=0, sig_neg=0, pi_pos=0, cross_all_pos=0, cross_some_neg=0, posentry_cross=0, n=0)
    example = None
    for _ in range(ndraw):
        n1, n2 = rng.integers(1, 4), rng.integers(1, 4)
        A, Q, bl = assemble([random_component(n1, signed, reversible), random_component(n2, signed, reversible)])
        N = A.shape[0]
        b = rng.uniform(0.05, 1.0, N) * (rng.uniform(size=N) < 0.8)
        if b[bl[0]].sum() == 0 or b[bl[1]].sum() == 0:
            continue
        q = rng.uniform(0.05, 2.0)
        Sc = sigma_c_rts(A, Q, b, q); Pc = np.linalg.inv(Sc)
        stats["n"] += 1
        agg = b[bl[0]] @ Sc[np.ix_(bl[0], bl[1])] @ b[bl[1]]
        stats["agg_neg"] += agg < 0
        stats["sig_neg"] += Sc[np.ix_(bl[0], bl[1])].min() < 0
        off = Pc - np.diag(np.diag(Pc))
        stats["pi_pos"] += off.max() > 1e-12
        cr = Pc[np.ix_(bl[0], bl[1])]
        act = np.outer(b[bl[0]] > 0, b[bl[1]] > 0)
        stats["cross_all_pos"] += bool((cr[act] > 0).all())
        stats["cross_some_neg"] += bool((cr[act] < 0).any())
        stats["posentry_cross"] += cr.max() > 1e-12
        if (cr[act] < 0).any() and example is None:
            example = (A, Q, b, q, bl, Pc)
    return stats, example

for signed, rev, lab in [(False, False, "A>=0 nonreversible"), (False, True, "A>=0 reversible"), (True, False, "signed A")]:
    st, ex = run_two(signed, rev)
    n = st["n"]
    print(f"   [{lab}] draws={n}: agg<0 {st['agg_neg']}, Sigma cross<0 {st['sig_neg']}, Pi has pos offdiag {st['pi_pos']}, "
          f"pos entry in cross block {st['posentry_cross']}, all acting cross Pi>0 {st['cross_all_pos']}, some acting cross Pi<0 {st['cross_some_neg']}")
    report(f"THM collider [{lab}]: aggregated cross cov < 0 in every draw", n, st["agg_neg"])
    report(f"THM collider [{lab}]: Pi^c has a positive offdiag entry in every draw", n, st["pi_pos"])
    if ex is not None:
        A, Q, b, q, bl, Pc = ex
        print(f"      example with a negative acting cross entry: blocks {bl}\n      A=\n{np.round(A,3)}\n      Qdiag={np.round(np.diag(Q),3)} b={np.round(b,3)} q={q:.3f}\n      Pi^c=\n{np.round(Pc,4)}")

# ---------------- negative controls ----------------
# (a) opposite-sign loadings, two non-communicating scalar agents -> diffusive possible
A = np.diag([0.5, 0.5]); Q = np.eye(2); b = np.array([0.6, -0.6]); q = 1.0
Pc = np.linalg.inv(sigma_c_rts(A, Q, b, q)); d = is_diffusive(Pc)
report("NEG CONTROL opposite-sign loadings: Pi^c diffusive", (True, True), (bool(d[0]), bool(d[1])))
# (b) no acts -> block diagonal, diffusive for reversible A>=0 components
A, Q, bl = assemble([random_component(3, False, True), random_component(3, False, True)])
Pc = np.linalg.inv(sigma_0(A, Q)); d = is_diffusive(Pc, tol=1e-9)
report("NEG CONTROL no acts (reversible A>=0 components): Pi^c diffusive", (True, True), (bool(d[0]), bool(d[1])))
# (c) hypothesis (N) violated: common source k read by both collectives; search for a diffusive instance
found = None
for _ in range(4000):
    # agents: 0 (source, does not act), 1 in C1, 2 in C2; 1 and 2 read 0
    a1, a2 = rng.uniform(0.1, 0.9, 2); c0, c1, c2 = rng.uniform(0, 0.9, 3)
    A = np.array([[c0, 0, 0], [a1, c1, 0], [a2, 0, c2]])
    if np.abs(np.linalg.eigvals(A)).max() >= 0.95:
        continue
    Qd = rng.uniform(0.05, 2.0, 3); b = np.array([0.0, *rng.uniform(0.01, 1.0, 2)]); q = rng.uniform(0.05, 5.0)
    Pc = np.linalg.inv(sigma_c_rts(A, np.diag(Qd), b, q))
    d = is_diffusive(Pc)
    if d[0] and d[1]:
        found = (A, Qd, b, q, Pc); break
report("NEG CONTROL common source (hypothesis N violated): a diffusive instance exists", True, found is not None)
if found:
    A, Qd, b, q, Pc = found
    print(f"      A=\n{np.round(A,3)}\n      Qdiag={np.round(Qd,3)} b={np.round(b,3)} q={q:.3f}\n      Pi^c=\n{np.round(Pc,5)}")

print("ALL CHECKS AS EXPECTED" if ok_all else "SOME CHECK DIFFERED FROM EXPECTATION")
