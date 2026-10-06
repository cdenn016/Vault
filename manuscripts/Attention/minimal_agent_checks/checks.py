r"""Float64 checks for the minimal agent model (tied key and content, Bayesian receiver).

Declared model, reference coordinates, one receiver i, one layer, fixed input states:

.. math::
    X_i \sim \mathcal N(\xi_i, C_i),\quad X_j \sim \mathcal N(\xi_j, C_j)\ (j\in\mathcal N_i),
    \quad J^h \sim \pi^h_i,\quad
    o_h = S_{Q,h} X_i - T_h X_{J^h} + \varepsilon_h,\ \varepsilon_h\sim\mathcal N(0, N_h),

all independent, with the record observed at o = 0.  The source states are snapshots independent of
X_i (the random checks use four non-self sources).

Two independent computational paths are compared.  The brute-force path builds the full stacked joint
law of (X_i, every source state, every noise) for each label tuple, maps it linearly to (X_i, o),
and applies generic Gaussian conditioning; it never uses R_ij, G_ij, or the closed forms.  The closed
path evaluates the formulas of Proposition prop:minimal_agent.  A self-normalized importance-sampling
Monte Carlo estimate checks one configuration without any Gaussian conditioning formula.

Run:  C:/anaconda/python.exe checks.py > checks_output.txt
"""
from __future__ import annotations

import itertools

import numpy as np
from numpy.linalg import inv, matrix_rank, norm, slogdet, solve

rng = np.random.default_rng(20261005)
LOG2PI = np.log(2.0 * np.pi)
TOL = 1e-9
RESULTS: list[tuple[str, float, bool]] = []


def report(name: str, value: float, ok: bool | None = None, tol: float = TOL) -> None:
    """Record and print one residual; ``ok`` defaults to ``value < tol``."""
    if ok is None:
        ok = bool(value < tol)
    RESULTS.append((name, float(value), ok))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {value:.3e}")


def spd(n: int, lo: float = 0.3) -> np.ndarray:
    """Random SPD matrix with smallest eigenvalue at least ``lo``."""
    A = rng.standard_normal((n, n))
    return A @ A.T / n + lo * np.eye(n)


def logN(x: np.ndarray, m: np.ndarray, S: np.ndarray) -> float:
    r"""log N(x; m, S) for SPD S."""
    d = x - m
    sign, ld = slogdet(S)
    assert sign > 0
    return float(-0.5 * (d @ solve(S, d) + ld + len(x) * LOG2PI))


def lse(a: np.ndarray) -> float:
    m = np.max(a)
    return float(m + np.log(np.sum(np.exp(a - m))))


def softmax(a: np.ndarray) -> np.ndarray:
    a = np.asarray(a, dtype=float)
    e = np.exp(a - a.max())
    return e / e.sum()


def kl_gauss(m0: np.ndarray, S0: np.ndarray, m1: np.ndarray, S1: np.ndarray) -> float:
    r"""KL(N(m0,S0) || N(m1,S1))."""
    k = len(m0)
    d = m1 - m0
    return float(0.5 * (np.trace(solve(S1, S0)) + d @ solve(S1, d) - k
                        + slogdet(S1)[1] - slogdet(S0)[1]))


def c_orth_rows(SQ1: np.ndarray, C: np.ndarray, r2: int) -> np.ndarray:
    r"""Random r2 x K rows with SQ2 C SQ1^T = 0 (rows orthogonal to the columns of C SQ1^T)."""
    W = C @ SQ1.T
    P = np.eye(C.shape[0]) - W @ solve(W.T @ W, W.T)
    return rng.standard_normal((r2, C.shape[0])) @ P


# ----------------------------------------------------------------------------------------------
# Brute-force path: generic conditioning of the full stacked joint law.
# ----------------------------------------------------------------------------------------------
def brute(xi_i, C_i, xis, Cs, heads, logpi):
    """heads: list of dicts with 'SQ' (r_h x K), 'send' (list over sources of r_h x K), 'N'.

    Returns tuples, normalized tuple posterior, conditional means and covariances of X_i, and the
    mixture mean and covariance (law of total covariance)."""
    K = len(xi_i)
    n = len(xis)
    H = len(heads)
    rs = [hd["SQ"].shape[0] for hd in heads]
    rbar = sum(rs)
    dimZ = K + n * K + rbar
    mZ = np.concatenate([xi_i] + list(xis) + [np.zeros(rbar)])
    SZ = np.zeros((dimZ, dimZ))
    SZ[:K, :K] = C_i
    for k in range(n):
        SZ[K + k * K:K + (k + 1) * K, K + k * K:K + (k + 1) * K] = Cs[k]
    off = K + n * K
    for h, hd in enumerate(heads):
        o = off + sum(rs[:h])
        SZ[o:o + rs[h], o:o + rs[h]] = hd["N"]
    tuples = list(itertools.product(range(n), repeat=H))
    logw, means, covs = [], [], []
    for t in tuples:
        L = np.zeros((K + rbar, dimZ))
        L[:K, :K] = np.eye(K)
        for h, hd in enumerate(heads):
            ro = K + sum(rs[:h])
            rows = slice(ro, ro + rs[h])
            L[rows, :K] = hd["SQ"]
            j = t[h]
            L[rows, K + j * K:K + (j + 1) * K] -= hd["send"][j]
            eo = off + sum(rs[:h])
            L[rows, eo:eo + rs[h]] = np.eye(rs[h])
        m = L @ mZ
        S = L @ SZ @ L.T
        mx, mo = m[:K], m[K:]
        Sxx, Sxo, Soo = S[:K, :K], S[:K, K:], S[K:, K:]
        lp = logN(np.zeros(rbar), mo, Soo) + sum(logpi[h][t[h]] for h in range(H))
        logw.append(lp)
        means.append(mx + Sxo @ solve(Soo, -mo))
        covs.append(Sxx - Sxo @ solve(Soo, Sxo.T))
    logw = np.array(logw)
    w = np.exp(logw - lse(logw))
    means = np.array(means)
    covs = np.array(covs)
    mbar = w @ means
    D = means - mbar
    Cbar = np.einsum("t,tab->ab", w, covs) + np.einsum("t,ta,tb->ab", w, D, D)
    return tuples, w, means, covs, mbar, Cbar


def tied_head(SQ, T, N, n):
    return {"SQ": SQ, "send": [T] * n, "N": N}


# ----------------------------------------------------------------------------------------------
# Closed forms of the proposition.
# ----------------------------------------------------------------------------------------------
def closed_one_head(xi_i, C_i, xis, Cs, SQ, T, N, pi):
    n = len(xis)
    V = SQ @ C_i @ SQ.T
    R = [N + T @ Cj @ T.T for Cj in Cs]
    logw = np.array([np.log(pi[j]) + logN(T @ xis[j], SQ @ xi_i, V + R[j]) for j in range(n)])
    w = np.exp(logw - lse(logw))
    G = [C_i @ SQ.T @ inv(V + R[j]) for j in range(n)]
    m = np.array([xi_i + G[j] @ (T @ xis[j] - SQ @ xi_i) for j in range(n)])
    P = np.array([C_i - G[j] @ SQ @ C_i for j in range(n)])
    mbar = w @ m
    D = m - mbar
    Cbar = np.einsum("j,jab->ab", w, P) + np.einsum("j,ja,jb->ab", w, D, D)
    return dict(w=w, G=G, m=m, P=P, mbar=mbar, Cbar=Cbar, V=V, R=R)


def per_head_weights(xi_i, C_i, xis, Cs, SQ, T, N, pi):
    return closed_one_head(xi_i, C_i, xis, Cs, SQ, T, N, pi)["w"]


print("Minimal agent model checks (float64, NumPy %s), seed 20261005" % np.__version__)

# ==============================================================================================
print("\n(a) One head: label posterior, component posteriors, mixture moments")
K, r, n = 5, 3, 4
C_i = spd(K)
xi_i = rng.standard_normal(K)
xis = [rng.standard_normal(K) for _ in range(n)]
Cs = [spd(K) for _ in range(n)]
SQ = rng.standard_normal((r, K))
T = rng.standard_normal((r, K))
N = spd(r)
pi = softmax(rng.standard_normal(n))
_, wb, mb, Pb, mbarb, Cbarb = brute(xi_i, C_i, xis, Cs, [tied_head(SQ, T, N, n)], [np.log(pi)])
cf = closed_one_head(xi_i, C_i, xis, Cs, SQ, T, N, pi)
report("label posterior w_ij (closed vs brute), max abs", np.max(np.abs(cf["w"] - wb)))
report("component means m_ij, max abs", np.max(np.abs(cf["m"] - mb)))
report("component covariances C_i - G_ij S_Q C_i, max abs", np.max(np.abs(cf["P"] - Pb)))
report("posterior mean (mixture mean), max abs", np.max(np.abs(cf["mbar"] - mbarb)))
report("posterior covariance incl. between-source spread, max abs", np.max(np.abs(cf["Cbar"] - Cbarb)))
# Expected-likelihood identity: N(T xi_j; S_Q xi_i, V+R) = int N(y; S_Q xi_i, V) N(y; T xi_j, R) dy.
# For K=... checked by the closed product-of-Gaussians formula (independent algebra):
j = 1
V, Rj = cf["V"], cf["R"][j]
a, b = SQ @ xi_i, T @ xis[j]
Pp = inv(inv(V) + inv(Rj))
mp = Pp @ (solve(V, a) + solve(Rj, b))
log_int = (-0.5 * (a @ solve(V, a) + b @ solve(Rj, b) - mp @ solve(Pp, mp))
           - 0.5 * (slogdet(V)[1] + slogdet(Rj)[1] - slogdet(Pp)[1]) - 0.5 * r * LOG2PI)
report("expected-likelihood kernel = N(T xi_j; S_Q xi_i, V+R) (product integral)", abs(log_int - logN(b, a, V + Rj)))
# Expected-likelihood routing (Definition 2.1 of the note) with N = 0: weights = pi N(a_i; b_j, V_Q + V_K), S_K = T.
cf0 = closed_one_head(xi_i, C_i, xis, Cs, SQ, T, np.zeros((r, r)), pi)
nq = softmax([np.log(pi[k]) + logN(SQ @ xi_i, T @ xis[k], SQ @ C_i @ SQ.T + T @ Cs[k] @ T.T) for k in range(n)])
report("N=0: weights equal expected-likelihood routing with S_K = T", np.max(np.abs(cf0["w"] - nq)))
# Constant R: shared sender covariance.
Cshared = spd(K)
Cs_sh = [Cshared] * n
cf = closed_one_head(xi_i, C_i, xis, Cs_sh, SQ, T, N, pi)
_, wb, mb, Pb, mbarb, Cbarb = brute(xi_i, C_i, xis, Cs_sh, [tied_head(SQ, T, N, n)], [np.log(pi)])
G = cf["G"][0]
zbar = sum(cf["w"][k] * T @ xis[k] for k in range(n))
xi_plus = (np.eye(K) - G @ SQ) @ xi_i + G @ zbar
covz = sum(cf["w"][k] * np.outer(T @ xis[k] - zbar, T @ xis[k] - zbar) for k in range(n))
C_plus = (np.eye(K) - G @ SQ) @ C_i + G @ covz @ G.T
report("constant R: xi+ = (I - G S_Q) xi + G sum_j w_ij T xi_j (vs brute)", np.max(np.abs(xi_plus - mbarb)))
report("constant R: C+ = (I - G S_Q) C + G Cov_w(T xi) G^T (vs brute)", np.max(np.abs(C_plus - Cbarb)))
Pc = C_i - G @ SQ @ C_i
report("precision-weighted residual: I - G S_Q = P C_i^{-1}", np.max(np.abs((np.eye(K) - G @ SQ) - Pc @ inv(C_i))))
Rsh = cf["R"][0]
report("Woodbury: G = (C^-1 + S^T R^-1 S)^-1 S^T R^-1",
       np.max(np.abs(G - inv(inv(C_i) + SQ.T @ solve(Rsh, SQ)) @ SQ.T @ inv(Rsh))))

# ==============================================================================================
print("\n(a') Monte Carlo (self-normalized importance sampling, no Gaussian conditioning used)")
cf = closed_one_head(xi_i, C_i, xis, Cs, SQ, T, N, pi)
M_total, chunk = 1_000_000, 200_000
Lc = np.linalg.cholesky(C_i)
Ls = [np.linalg.cholesky(Cj) for Cj in Cs]
Ninv = inv(N)
sw = 0.0
swx = np.zeros(K)
swxx = np.zeros((K, K))
swJ = np.zeros(n)
logw_all, x_all = [], []
for _ in range(M_total // chunk):
    J = rng.choice(n, size=chunk, p=pi)
    X = xi_i + rng.standard_normal((chunk, K)) @ Lc.T
    XS = np.empty((chunk, K))
    for k in range(n):
        idx = J == k
        XS[idx] = xis[k] + rng.standard_normal((idx.sum(), K)) @ Ls[k].T
    o = X @ SQ.T - XS @ T.T
    lw = -0.5 * np.einsum("ta,ab,tb->t", o, Ninv, o)
    logw_all.append(lw)
    x_all.append((X, J))
lw = np.concatenate(logw_all)
X = np.concatenate([x for x, _ in x_all])
J = np.concatenate([jj for _, jj in x_all])
wt = np.exp(lw - lw.max())
wt /= wt.sum()
mc_mean = wt @ X
mc_se = np.sqrt(np.einsum("t,ta->a", wt ** 2, (X - mc_mean) ** 2))
ess = 1.0 / np.sum(wt ** 2)
mc_w = np.array([wt[J == k].sum() for k in range(n)])
mc_w_se = np.sqrt(np.array([np.sum(wt ** 2 * ((J == k) - mc_w[k]) ** 2) for k in range(n)]))
zmean = np.max(np.abs(mc_mean - cf["mbar"]) / mc_se)
zw = np.max(np.abs(mc_w - cf["w"]) / mc_w_se)
print(f"  draws = {M_total}, effective sample size = {ess:.0f}")
print(f"  exact mean  = {np.array2string(cf['mbar'], precision=4)}")
print(f"  MC mean     = {np.array2string(mc_mean, precision=4)}")
print(f"  MC std err  = {np.array2string(mc_se, precision=4)}")
print(f"  exact w     = {np.array2string(cf['w'], precision=4)}; MC w = {np.array2string(mc_w, precision=4)}")
report("MC posterior mean: max |MC - exact| / s.e. (pass if < 4)", zmean, ok=bool(zmean < 4))
report("MC label posterior: max |MC - exact| / s.e. (pass if < 4)", zw, ok=bool(zw < 4))

# ==============================================================================================
print("\n(b) Several heads: factorization under H1-H3, and its failure")
K, n = 6, 4
r1, r2 = 3, 2
C_i = spd(K)
xi_i = rng.standard_normal(K)
xis = [rng.standard_normal(K) for _ in range(n)]
Cshared = spd(K)
Cs = [Cshared] * n                                   # H1: R^h_ij independent of j
SQ1 = rng.standard_normal((r1, K))
SQ2 = c_orth_rows(SQ1, C_i, r2)                      # H3: S_Q1 C_i S_Q2^T = 0
T1 = rng.standard_normal((r1, K))
T2 = c_orth_rows(T1, Cshared, r2)                    # H2: T1 C_j T2^T = 0
N1, N2 = spd(r1), spd(r2)
pi1, pi2 = softmax(rng.standard_normal(n)), softmax(rng.standard_normal(n))
print(f"  |S_Q1 C_i S_Q2^T| = {norm(SQ1 @ C_i @ SQ2.T):.1e}, |T1 C_s T2^T| = {norm(T1 @ Cshared @ T2.T):.1e}")


def two_head_closed(SQs, Ts, Ns, pis, C_i, xi_i, xis, Cs):
    parts = [closed_one_head(xi_i, C_i, xis, Cs, SQs[h], Ts[h], Ns[h], pis[h]) for h in range(2)]
    return parts


heads = [tied_head(SQ1, T1, N1, n), tied_head(SQ2, T2, N2, n)]
tuples, wb, mb, Pb, mbarb, Cbarb = brute(xi_i, C_i, xis, Cs, heads, [np.log(pi1), np.log(pi2)])
parts = two_head_closed([SQ1, SQ2], [T1, T2], [N1, N2], [pi1, pi2], C_i, xi_i, xis, Cs)
wprod = np.array([parts[0]["w"][t[0]] * parts[1]["w"][t[1]] for t in tuples])
report("H1-H3: tuple posterior = product of per-head w^h, max abs", np.max(np.abs(wprod - wb)))
G1, G2 = parts[0]["G"][0], parts[1]["G"][0]
z1 = sum(parts[0]["w"][k] * T1 @ xis[k] for k in range(n))
z2 = sum(parts[1]["w"][k] * T2 @ xis[k] for k in range(n))
xi_plus = (np.eye(K) - G1 @ SQ1 - G2 @ SQ2) @ xi_i + G1 @ z1 + G2 @ z2
cz1 = sum(parts[0]["w"][k] * np.outer(T1 @ xis[k] - z1, T1 @ xis[k] - z1) for k in range(n))
cz2 = sum(parts[1]["w"][k] * np.outer(T2 @ xis[k] - z2, T2 @ xis[k] - z2) for k in range(n))
C_plus = (np.eye(K) - G1 @ SQ1 - G2 @ SQ2) @ C_i + G1 @ cz1 @ G1.T + G2 @ cz2 @ G2.T
report("H1-H3: xi+ = (I - sum_h G^h S_Qh) xi + sum_h G^h sum_j w^h T_h xi_j", np.max(np.abs(xi_plus - mbarb)))
report("H1-H3: C+ formula (per-head spread, no cross-head spread)", np.max(np.abs(C_plus - Cbarb)))

# H2 and H3 without H1 (source-dependent sender covariances, sending rows C_j-orthogonal for all j)
# Use point senders C_j = 0 except a common shared part to keep H2: R^h_ij depends on j through N only?
# Instead: sender covariances C_j = c_j * Cshared (scalar multiples keep T1 C_j T2^T = 0).
cj = rng.uniform(0.3, 2.0, size=n)
Cs_var = [cj[k] * Cshared for k in range(n)]
tuples, wb, mb, Pb, mbarb, Cbarb = brute(xi_i, C_i, xis, Cs_var, heads, [np.log(pi1), np.log(pi2)])
parts = two_head_closed([SQ1, SQ2], [T1, T2], [N1, N2], [pi1, pi2], C_i, xi_i, xis, Cs_var)
wprod = np.array([parts[0]["w"][t[0]] * parts[1]["w"][t[1]] for t in tuples])
report("H2,H3 without H1: tuple posterior still factorizes, max abs", np.max(np.abs(wprod - wb)))
xi_plus = xi_i + sum(sum(parts[h]["w"][k] * parts[h]["G"][k] @ ([T1, T2][h] @ xis[k] - [SQ1, SQ2][h] @ xi_i)
                         for k in range(n)) for h in range(2))
report("H2,H3 without H1: xi+ = xi + sum_h sum_j w^h G^h_ij (T_h xi_j - S_Qh xi)", np.max(np.abs(xi_plus - mbarb)))

# Failure of H3 (H1, H2 hold): random second query map.
SQ2b = rng.standard_normal((r2, K))
heads_b = [tied_head(SQ1, T1, N1, n), tied_head(SQ2b, T2, N2, n)]
tuples, wb, mb, Pb, mbarb, Cbarb = brute(xi_i, C_i, xis, Cs, heads_b, [np.log(pi1), np.log(pi2)])
parts = two_head_closed([SQ1, SQ2b], [T1, T2], [N1, N2], [pi1, pi2], C_i, xi_i, xis, Cs)
wprod = np.array([parts[0]["w"][t[0]] * parts[1]["w"][t[1]] for t in tuples])
dev = np.max(np.abs(wprod - wb))
report("H3 fails: tuple posterior differs from product of per-head w (expected > 0)", dev, ok=bool(dev > 1e-3))
# exact marginals and stacked gain reproduce the mean
wbar1 = np.array([sum(wb[t] for t in range(len(tuples)) if tuples[t][0] == k) for k in range(n)])
wbar2 = np.array([sum(wb[t] for t in range(len(tuples)) if tuples[t][1] == k) for k in range(n)])
S = np.vstack([SQ1, SQ2b])
Rblk = np.block([[parts[0]["R"][0], np.zeros((r1, r2))], [np.zeros((r2, r1)), parts[1]["R"][0]]])
Gs = C_i @ S.T @ inv(S @ C_i @ S.T + Rblk)
yb = np.concatenate([sum(wbar1[k] * T1 @ xis[k] for k in range(n)), sum(wbar2[k] * T2 @ xis[k] for k in range(n))])
xi_exact_formula = xi_i + Gs @ (yb - S @ xi_i)
report("H3 fails, H1,H2 hold: xi+ = xi + G_stack (sum_j wbar T xi_j - S xi) with exact marginals",
       np.max(np.abs(xi_exact_formula - mbarb)))
G1, G2 = parts[0]["G"][0], parts[1]["G"][0]
z1 = sum(parts[0]["w"][k] * T1 @ xis[k] for k in range(n))
z2 = sum(parts[1]["w"][k] * T2 @ xis[k] for k in range(n))
xi_perhead = (np.eye(K) - G1 @ SQ1 - G2 @ SQ2b) @ xi_i + G1 @ z1 + G2 @ z2
dev = np.max(np.abs(xi_perhead - mbarb))
report("H3 fails: per-head rows with per-head gains differ from exact mean (expected > 0)", dev, ok=bool(dev > 1e-3))
print(f"    max |w^1 - wbar^1| = {np.max(np.abs(parts[0]['w'] - wbar1)):.3e}, "
      f"max |G^1 - G_stack[:, head 1]| = {np.max(np.abs(G1 - Gs[:, :r1])):.3e}")

# Failure of H2 (H1, H3 hold): sending rows not C_s-orthogonal.
T2b = rng.standard_normal((r2, K))
heads_c = [tied_head(SQ1, T1, N1, n), tied_head(SQ2, T2b, N2, n)]
tuples, wb, mb, Pb, mbarb, Cbarb = brute(xi_i, C_i, xis, Cs, heads_c, [np.log(pi1), np.log(pi2)])
parts = two_head_closed([SQ1, SQ2], [T1, T2b], [N1, N2], [pi1, pi2], C_i, xi_i, xis, Cs)
wprod = np.array([parts[0]["w"][t[0]] * parts[1]["w"][t[1]] for t in tuples])
dev = np.max(np.abs(wprod - wb))
report("H2 fails (sender cross-head covariance): no factorization (expected > 0)", dev, ok=bool(dev > 1e-3))

# Minimal counterexample: K = 1, two heads querying the same coordinate, point senders.
print("  K=1 counterexample: S_Q1=S_Q2=T1=T2=1, C_i=1, N_h=1, C_j=0, xi_i=0, x_1=0, x_2=2, uniform prior")
one = np.ones((1, 1))
heads_k1 = [tied_head(one, one, one, 2), tied_head(one, one, one, 2)]
tuples, wb, mb, Pb, mbarb, Cbarb = brute(np.zeros(1), one, [np.zeros(1), 2 * np.ones(1)],
                                         [np.zeros((1, 1))] * 2, heads_k1, [np.log([0.5, 0.5])] * 2)
e = np.exp(-4.0 / 3.0)
analytic = np.array([1, e, e, e]) / (1 + 3 * e)
report("K=1: tuple posterior = (1, e^-4/3, e^-4/3, e^-4/3)/(1+3e^-4/3)", np.max(np.abs(wb - analytic)))
wbar = analytic[2] + analytic[3]
wph = np.exp(-1) / (1 + np.exp(-1))
print(f"    exact marginal P(J^h=2) = {wbar:.5f}; per-head weight from (a) = {wph:.5f}")
print(f"    P(J^1=2,J^2=2) = {analytic[3]:.5f} vs product of marginals {wbar ** 2:.5f}")
exact_mean = (1.0 / 3.0) * 2 * wbar * 2
report("K=1: exact posterior mean = (1/3) E[x_J1 + x_J2] = 4 wbar / 3", abs(mbarb[0] - exact_mean))
perhead_mean = 2 * 0.5 * wph * 2
print(f"    exact mean = {mbarb[0]:.5f}; per-head rows with per-head gains 1/2 give {perhead_mean:.5f}")

# ==============================================================================================
print("\n(c) Noise-free channel R = 0: gain, oblique projector, constraint, local form, passive law")
K, r, n = 6, 3, 4
C_i = spd(K)
xi_i = rng.standard_normal(K)
xis = [rng.standard_normal(K) for _ in range(n)]
C0s = [spd(K) for _ in range(n)]
SQ = rng.standard_normal((r, K))
T = rng.standard_normal((r, K))
N0 = spd(r)
pi = softmax(rng.standard_normal(n))
RQ = C_i @ SQ.T @ inv(SQ @ C_i @ SQ.T)
Pi = RQ @ SQ
cf0 = closed_one_head(xi_i, C_i, xis, [np.zeros((K, K))] * n, SQ, T, np.zeros((r, r)), pi)
for eps in [1e-1, 1e-2, 1e-4, 1e-6, 1e-8]:
    cfe = closed_one_head(xi_i, C_i, xis, [eps * C for C in C0s], SQ, T, eps * N0, pi)
    print(f"    eps={eps:.0e}: max|G_ij - R_Q| = {max(norm(Gj - RQ) for Gj in cfe['G']):.2e}, "
          f"|xi+(eps) - xi+(0)| = {norm(cfe['mbar'] - cf0['mbar']):.2e}, |w(eps) - w(0)| = {norm(cfe['w'] - cf0['w']):.2e}")
gerr = []
for eps in [1e-6, 1e-8]:
    cfe = closed_one_head(xi_i, C_i, xis, [eps * C for C in C0s], SQ, T, eps * N0, pi)
    gerr.append(max(norm(Gj - RQ) for Gj in cfe["G"]))
rate = np.log10(gerr[0] / gerr[1]) / 2.0
report("limit R -> 0: |G_ij - R_Q| = O(eps); |1 - fitted order| between eps=1e-6 and 1e-8", abs(rate - 1.0),
       ok=bool(abs(rate - 1.0) < 0.02))
_, wb, mb, Pb, mbarb, Cbarb = brute(xi_i, C_i, xis, [np.zeros((K, K))] * n,
                                    [tied_head(SQ, T, np.zeros((r, r)), n)], [np.log(pi)])
report("R = 0 exactly: closed form vs brute (mean)", np.max(np.abs(cf0["mbar"] - mbarb)))
report("R = 0 exactly: closed form vs brute (covariance)", np.max(np.abs(cf0["Cbar"] - Cbarb)))
report("S_Q R_Q = I_r", np.max(np.abs(SQ @ RQ - np.eye(r))))
report("Pi^2 = Pi", np.max(np.abs(Pi @ Pi - Pi)))
report("S_Q Pi = S_Q (so ker Pi = ker S_Q, by rank)", np.max(np.abs(SQ @ Pi - SQ)))
report("Pi C S_Q^T = C S_Q^T (im Pi = im C S_Q^T)", np.max(np.abs(Pi @ C_i @ SQ.T - C_i @ SQ.T)))
report("rank Pi = r", abs(matrix_rank(Pi) - r))
zbar = sum(cf0["w"][k] * T @ xis[k] for k in range(n))
xi_plus = (np.eye(K) - Pi) @ xi_i + RQ @ zbar
report("xi+ = (I - Pi) xi + R_Q sum_j w T xi_j (vs brute)", np.max(np.abs(xi_plus - mbarb)))
report("constraint S_Q xi+ = sum_j w_ij T xi_j", np.max(np.abs(SQ @ mbarb - zbar)))
report("unprobed component kept: (I - Pi)(xi+ - xi) = 0", np.max(np.abs((np.eye(K) - Pi) @ (mbarb - xi_i))))
# Minimal C^{-1}-norm change: solve the KKT system independently.
KKT = np.block([[inv(C_i), SQ.T], [SQ, np.zeros((r, r))]])
rhs = np.concatenate([np.zeros(K), zbar - SQ @ xi_i])
delta_kkt = solve(KKT, rhs)[:K]
report("xi+ - xi = argmin delta^T C^-1 delta s.t. S_Q delta = zbar - S_Q xi (KKT)", np.max(np.abs(delta_kkt - (mbarb - xi_i))))
covz = sum(cf0["w"][k] * np.outer(T @ xis[k] - zbar, T @ xis[k] - zbar) for k in range(n))
report("C+ = (I - Pi) C + R_Q Cov_w(T xi) R_Q^T", np.max(np.abs((np.eye(K) - Pi) @ C_i + RQ @ covz @ RQ.T - Cbarb)))
# Local coordinates, induced comparison link with S_K = T, passive law.
U = [rng.standard_normal((K, K)) + 2 * np.eye(K) for _ in range(n + 1)]   # U[0] receiver, U[1..n] senders
mu_i = U[0] @ xi_i
Sig_i = U[0] @ C_i @ U[0].T
mus = [U[k + 1] @ xis[k] for k in range(n)]


def local_brute(Ufr, mu_i, Sig_i, mus, Sigs, SQ, T, N, pi):
    head = {"SQ": SQ @ inv(Ufr[0]), "send": [T @ inv(Ufr[k + 1]) for k in range(len(mus))], "N": N}
    return brute(mu_i, Sig_i, mus, Sigs, [head], [np.log(pi)])


Zs = [np.zeros((K, K))] * n
_, wl, ml, Pl, mbl, Cbl = local_brute(U, mu_i, Sig_i, mus, Zs, SQ, T, np.zeros((r, r)), pi)
Mcmp = [U[0] @ RQ @ T @ inv(U[k + 1]) for k in range(n)]
mu_plus = U[0] @ (np.eye(K) - Pi) @ inv(U[0]) @ mu_i + sum(wl[k] * Mcmp[k] @ mus[k] for k in range(n))
report("local: mu+ = U_i(I-Pi)U_i^-1 mu_i + sum_j w M^cmp_ij mu_j (vs local brute)", np.max(np.abs(mu_plus - mbl)))
report("local weights equal reference weights", np.max(np.abs(wl - cf0["w"])))
g = [rng.standard_normal((K, K)) + 2 * np.eye(K) for _ in range(n + 1)]
Ug = [g[k] @ U[k] for k in range(n + 1)]
_, wg, mg, Pg, mbg, Cbg = local_brute(Ug, g[0] @ mu_i, g[0] @ Sig_i @ g[0].T,
                                      [g[k + 1] @ mus[k] for k in range(n)], Zs, SQ, T, np.zeros((r, r)), pi)
report("passive law: weights unchanged", np.max(np.abs(wg - wl)))
report("passive law: mu+ -> g_i mu+", np.max(np.abs(mbg - g[0] @ mbl)))
report("passive law: Sigma+ -> g_i Sigma+ g_i^T", np.max(np.abs(Cbg - g[0] @ Cbl @ g[0].T)))
Mcmp_g = [Ug[0] @ RQ @ T @ inv(Ug[k + 1]) for k in range(n)]
report("passive law: M^cmp_ij -> g_i M^cmp_ij g_j^-1",
       max(np.max(np.abs(Mcmp_g[k] - g[0] @ Mcmp[k] @ inv(g[k + 1]))) for k in range(n)))
# Noisy channel, sender covariances: local form of items 1-2 and the passive law.
Csn = [spd(K) for _ in range(n)]
Sigs = [U[k + 1] @ Csn[k] @ U[k + 1].T for k in range(n)]
_, wln, mln, Pln, mbln, Cbln = local_brute(U, mu_i, Sig_i, mus, Sigs, SQ, T, N0, pi)
cfn = closed_one_head(xi_i, C_i, xis, Csn, SQ, T, N0, pi)
Gbar = sum(cfn["w"][k] * cfn["G"][k] for k in range(n))
mu_plus_n = (U[0] @ (np.eye(K) - Gbar @ SQ) @ inv(U[0]) @ mu_i
             + sum(cfn["w"][k] * U[0] @ cfn["G"][k] @ T @ inv(U[k + 1]) @ mus[k] for k in range(n)))
report("noisy local: mu+ = U_i(I - sum_j w G_ij S_Q)U_i^-1 mu_i + sum_j w U_i G_ij T U_j^-1 mu_j", np.max(np.abs(mu_plus_n - mbln)))
_, wgn, mgn, Pgn, mbgn, Cbgn = local_brute(Ug, g[0] @ mu_i, g[0] @ Sig_i @ g[0].T, [g[k + 1] @ mus[k] for k in range(n)],
                                          [g[k + 1] @ Sigs[k] @ g[k + 1].T for k in range(n)], SQ, T, N0, pi)
report("noisy passive law: weights, mean, covariance (max abs)",
       max(np.max(np.abs(wgn - wln)), np.max(np.abs(mbgn - g[0] @ mbln)), np.max(np.abs(Cbgn - g[0] @ Cbln @ g[0].T))))
# Common reference change a (also with noise and sender covariances).
a_ = rng.standard_normal((K, K)) + 2 * np.eye(K)
Cs_n = [spd(K) for _ in range(n)]
cfA = closed_one_head(xi_i, C_i, xis, Cs_n, SQ, T, N0, pi)
cfB = closed_one_head(inv(a_) @ xi_i, inv(a_) @ C_i @ inv(a_).T, [inv(a_) @ x for x in xis],
                      [inv(a_) @ C @ inv(a_).T for C in Cs_n], SQ @ a_, T @ a_, N0, pi)
report("common reference change: weights unchanged", np.max(np.abs(cfA["w"] - cfB["w"])))
report("common reference change: xi+ -> a^-1 xi+", np.max(np.abs(cfB["mbar"] - inv(a_) @ cfA["mbar"])))
report("common reference change: G_ij -> a^-1 G_ij", max(np.max(np.abs(cfB["G"][k] - inv(a_) @ cfA["G"][k])) for k in range(n)))

# ==============================================================================================
print("\n(d) Full rank r = K: one comparison link weighs and transports")
K, n = 3, 4
C_i = spd(K)
xi_i = rng.standard_normal(K)
xis = [rng.standard_normal(K) for _ in range(n)]
Cs = [spd(K) for _ in range(n)]
SQ = rng.standard_normal((K, K)) + 1.5 * np.eye(K)
T = rng.standard_normal((K, K)) + 1.5 * np.eye(K)
pi = softmax(rng.standard_normal(n))
Th = inv(SQ) @ T                                        # mathring Theta = S_Q^{-1} T
cf = closed_one_head(xi_i, C_i, xis, Cs, SQ, T, np.zeros((K, K)), pi)
logel = np.array([logN(Th @ xis[k], xi_i, C_i + Th @ Cs[k] @ Th.T) for k in range(n)])
logl = np.array([logN(T @ xis[k], SQ @ xi_i, SQ @ C_i @ SQ.T + T @ Cs[k] @ T.T) for k in range(n)])
report("log N(T xi_j; S_Q xi_i, V+R) - log N(Th xi_j; xi_i, C_i + Th C_j Th^T) = -log|det S_Q|",
       np.max(np.abs(logl - logel + slogdet(SQ)[1])))
report("weights = pi * expected likelihood of q_i and Th_* q_j (normalized)",
       np.max(np.abs(cf["w"] - softmax(np.log(pi) + logel))))
for k in range(n):
    Ct = Th @ Cs[k] @ Th.T
    Pk = inv(inv(C_i) + inv(Ct))
    mk = Pk @ (solve(C_i, xi_i) + solve(Ct, Th @ xis[k]))
    if k == 0:
        dm = np.max(np.abs(mk - cf["m"][k]))
        dP = np.max(np.abs(Pk - cf["P"][k]))
    else:
        dm = max(dm, np.max(np.abs(mk - cf["m"][k])))
        dP = max(dP, np.max(np.abs(Pk - cf["P"][k])))
report("component posterior = normalized product q_i * Th_* q_j (mean)", dm)
report("component posterior = normalized product q_i * Th_* q_j (covariance)", dP)
_, wb, mb, Pb, mbarb, Cbarb = brute(xi_i, C_i, xis, Cs, [tied_head(SQ, T, np.zeros((K, K)), n)], [np.log(pi)])
report("full rank, N=0: closed vs brute (mean)", np.max(np.abs(cf["mbar"] - mbarb)))
# General N: C~_ij = Th C_j Th^T + S_Q^-1 N S_Q^-T.
Nf = spd(K)
cfN = closed_one_head(xi_i, C_i, xis, Cs, SQ, T, Nf, pi)
Ctil = [Th @ Cs[k] @ Th.T + inv(SQ) @ Nf @ inv(SQ).T for k in range(n)]
wN = softmax([np.log(pi[k]) + logN(Th @ xis[k], xi_i, C_i + Ctil[k]) for k in range(n)])
mN = [xi_i + C_i @ inv(C_i + Ctil[k]) @ (Th @ xis[k] - xi_i) for k in range(n)]
report("full rank, N>0: weights with C_i + C~_ij", np.max(np.abs(wN - cfN["w"])))
report("full rank, N>0: component means xi + C(C + C~)^-1 (Th xi_j - xi)", max(np.max(np.abs(mN[k] - cfN["m"][k])) for k in range(n)))
# Limit C~ -> 0: transport form.
for eps in [1e-2, 1e-4, 1e-6, 1e-8]:
    cfe = closed_one_head(xi_i, C_i, xis, [eps * C for C in Cs], SQ, T, np.zeros((K, K)), pi)
    transport = sum(cfe["w"][k] * Th @ xis[k] for k in range(n))
    w_lim = softmax([np.log(pi[k]) + logN(Th @ xis[k], xi_i, C_i) for k in range(n)])
    print(f"    C_j -> {eps:.0e} C_j: |xi+ - sum_j w Th xi_j| = {norm(cfe['mbar'] - transport):.2e}, "
          f"|w - pi N(Th xi_j; xi_i, C_i)| = {norm(cfe['w'] - w_lim):.2e}")
report("transport limit: |xi+ - sum_j w Th xi_j| at eps = 1e-8 (pass if < 1e-6; error is O(eps))", norm(cfe["mbar"] - transport), ok=bool(norm(cfe["mbar"] - transport) < 1e-6))
# Brief's mixed form (C_j in weights, pure transport in mean) is not exact at finite C_j:
mixed = sum(softmax(np.log(pi) + logel)[k] * Th @ xis[k] for k in range(n))
print(f"    at finite C_j: |exact xi+ - sum_j w(C_i + Th C_j Th^T) Th xi_j| = {norm(cf['mbar'] - mixed):.3e} (nonzero)")
# Transport in local coordinates at C_j = 0: mu+ = sum_j w Theta^cmp_ij mu_j.
U = [rng.standard_normal((K, K)) + 2 * np.eye(K) for _ in range(n + 1)]
mus = [U[k + 1] @ xis[k] for k in range(n)]
_, wl, ml, Pl, mbl, Cbl = local_brute(U, U[0] @ xi_i, U[0] @ C_i @ U[0].T, mus, [np.zeros((K, K))] * n,
                                      SQ, T, np.zeros((K, K)), pi)
Thcmp = [U[0] @ Th @ inv(U[k + 1]) for k in range(n)]
report("local, C_j = 0: mu+ = sum_j w_ij Theta^cmp_ij mu_j", np.max(np.abs(mbl - sum(wl[k] * Thcmp[k] @ mus[k] for k in range(n)))))
# KL identity of prop:comparison_link with S_K = T.
d_kl = max(abs(kl_gauss(SQ @ xi_i, SQ @ C_i @ SQ.T, T @ xis[k], T @ Cs[k] @ T.T)
               - kl_gauss(xi_i, C_i, Th @ xis[k], Th @ Cs[k] @ Th.T)) for k in range(n))
report("KL((S_Q)_* q_i || T_* q_j) = KL(q_i || Th_* q_j)", d_kl)
# Grid quadrature of the expected likelihood (overlap integral) in K = 2.
K2 = 2
C2 = spd(K2)
x2 = rng.standard_normal(K2) * 0.5
C2j = spd(K2)
x2j = rng.standard_normal(K2) * 0.5
SQ2_ = rng.standard_normal((K2, K2)) + 1.5 * np.eye(K2)
T2_ = rng.standard_normal((K2, K2)) + 1.5 * np.eye(K2)
Th2 = inv(SQ2_) @ T2_
m2 = Th2 @ x2j
S2 = Th2 @ C2j @ Th2.T
g1 = np.linspace(-12, 12, 1601)
XX, YY = np.meshgrid(g1, g1, indexing="ij")
P_ = np.stack([XX.ravel(), YY.ravel()], axis=1)


def dens(P, m, S):
    d = P - m
    Si = inv(S)
    return np.exp(-0.5 * np.einsum("ta,ab,tb->t", d, Si, d)) / np.sqrt(np.linalg.det(2 * np.pi * S))


h = g1[1] - g1[0]
quad = np.sum(dens(P_, x2, C2) * dens(P_, m2, S2)) * h * h
report("K=2 grid quadrature: int q_i Th_* q_j = N(Th xi_j; xi_i, C_i + Th C_j Th^T) (rel.)",
       abs(quad / np.exp(logN(m2, x2, C2 + S2)) - 1), tol=1e-6)

# ==============================================================================================
print("\n(e) Re-basing S_K = A T, and the rectangular case")
K, r, n = 5, 3, 4
C_i = spd(K)
xi_i = rng.standard_normal(K)
xis = [rng.standard_normal(K) for _ in range(n)]
Cs = [spd(K) for _ in range(n)]
SQ = rng.standard_normal((r, K))
T = rng.standard_normal((r, K))
N = spd(r)
pi = softmax(rng.standard_normal(n))
A = rng.standard_normal((r, r)) + 2 * np.eye(r)
Ai = inv(A)
untied = {"SQ": SQ, "send": [A @ T] * n, "N": N}
_, wu, mu_, Pu, mbu, Cbu = brute(xi_i, C_i, xis, Cs, [untied], [np.log(pi)])
_, wt_, mt, Pt, mbt, Cbt = brute(xi_i, C_i, xis, Cs, [tied_head(Ai @ SQ, T, Ai @ N @ Ai.T, n)], [np.log(pi)])
report("S_K = A T vs tied (A^-1 S_Q, T, A^-1 N A^-T): label posterior", np.max(np.abs(wu - wt_)))
report("S_K = A T vs tied: posterior mean", np.max(np.abs(mbu - mbt)))
report("S_K = A T vs tied: posterior covariance", np.max(np.abs(Cbu - Cbt)))
dD = max(abs(kl_gauss(SQ @ xi_i, SQ @ C_i @ SQ.T, A @ T @ xis[k], A @ T @ Cs[k] @ T.T @ A.T)
             - kl_gauss(Ai @ SQ @ xi_i, Ai @ SQ @ C_i @ SQ.T @ Ai.T, T @ xis[k], T @ Cs[k] @ T.T)) for k in range(n))
report("Gibbs costs D_ij with (S_Q, A T) equal those with (A^-1 S_Q, T)", dD)
# Common invertible map of the comparison space (A S_Q, A T, A N A^T) leaves the tied model unchanged.
_, wA, mA, PA, mbA, CbA = brute(xi_i, C_i, xis, Cs, [tied_head(A @ SQ, A @ T, A @ N @ A.T, n)], [np.log(pi)])
_, w0, m0, P0, mb0, Cb0 = brute(xi_i, C_i, xis, Cs, [tied_head(SQ, T, N, n)], [np.log(pi)])
report("tied model invariant under (A S_Q, A T, A N A^T)", max(np.max(np.abs(wA - w0)), np.max(np.abs(mbA - mb0)), np.max(np.abs(CbA - Cb0))))
# Rectangular A (r x s, r < s): key is a lower-dimensional readout of the content.
s, rr = 3, 2
Ts = rng.standard_normal((s, K))
Ar = rng.standard_normal((rr, s))
SQr = rng.standard_normal((rr, K))
Nr = spd(rr)
rect = {"SQ": SQr, "send": [Ar @ Ts] * n, "N": Nr}
_, w1, m1, P1, mb1, Cb1 = brute(xi_i, C_i, xis, Cs, [rect], [np.log(pi)])
v = np.linalg.svd(Ar)[2][rr:].T[:, 0]                # unit vector in ker A (content space)
delta = np.linalg.pinv(Ts) @ v                         # T delta = v, A T delta = 0
print(f"    |T delta| = {norm(Ts @ delta):.3f} (content changes), |A T delta| = {norm(Ar @ Ts @ delta):.1e}")
xis_p = [x + (delta if k == 1 else 0) for k, x in enumerate(xis)]
_, w2, m2_, P2, mb2, Cb2 = brute(xi_i, C_i, xis_p, Cs, [rect], [np.log(pi)])
report("rectangular A: content change in ker A does not reach the receiver", max(np.max(np.abs(w1 - w2)), np.max(np.abs(mb1 - mb2))))
changes = []
for _ in range(12):
    xis_q = [x + rng.standard_normal(K) for x in xis]
    _, _, _, _, mbq, _ = brute(xi_i, C_i, xis_q, Cs, [rect], [np.log(pi)])
    changes.append(mbq - xi_i)
changes = np.array(changes).T
W = C_i @ SQr.T
resid = changes - W @ np.linalg.lstsq(W, changes, rcond=None)[0]
report("rectangular A: every update xi+ - xi lies in im(C_i S_Q^T), dim r < s", np.max(np.abs(resid)))

# ==============================================================================================
print("\n(f) Shared covariance: constant gain, dot-product routing, tiled heads")
K, r, n = 5, 3, 4
C = spd(K)
Cs_sh = [spd(K)] * n
SQ = rng.standard_normal((r, K))
T = rng.standard_normal((r, K))
N = spd(r)
pi = softmax(rng.standard_normal(n))
xis = [rng.standard_normal(K) for _ in range(n)]
xa, xb = rng.standard_normal(K), rng.standard_normal(K)
cfa = closed_one_head(xa, C, xis, Cs_sh, SQ, T, N, pi)
cfb = closed_one_head(xb, C, xis, Cs_sh, SQ, T, N, pi)
report("shared C, common R: gain identical for two receivers", np.max(np.abs(cfa["G"][0] - cfb["G"][0])))
Sig = cfa["V"] + cfa["R"][0]
evals, evecs = np.linalg.eigh(Sig)
Wh = evecs @ np.diag(evals ** -0.5) @ evecs.T
q = Wh @ SQ @ xa
ks = [Wh @ T @ x for x in xis]
wdot = softmax([q @ k - 0.5 * k @ k + np.log(pi[j]) for j, k in enumerate(ks)])
report("w = softmax(q.k - |k|^2/2 + log pi), whitening by V_Q + V_K", np.max(np.abs(wdot - cfa["w"])))
weff = softmax([(solve(Sig, SQ @ xa)) @ (T @ x) - 0.5 * (T @ x) @ solve(Sig, T @ x) + np.log(pi[j]) for j, x in enumerate(xis)])
report("same with W_Q = Sigma^-1 S_Q and W_K = W_V = T (no key whitening)", np.max(np.abs(weff - cfa["w"])))
# Tiled noise-free heads, C-orthogonal query rows.
K, n = 4, 3
rs = (2, 2)
SQs = rng.standard_normal((K, K)) + 1.5 * np.eye(K)
D1, D2 = spd(2), spd(2)
Dblk = np.block([[D1, np.zeros((2, 2))], [np.zeros((2, 2)), D2]])
C = inv(SQs) @ Dblk @ inv(SQs).T                     # S_Q C S_Q^T block diagonal
Tst = rng.standard_normal((K, K)) + 1.5 * np.eye(K)
xis = [rng.standard_normal(K) for _ in range(n)]
xi0 = rng.standard_normal(K)
pis = [softmax(rng.standard_normal(n)) for _ in range(2)]
Z0 = [np.zeros((K, K))] * n
heads_t = [tied_head(SQs[:2], Tst[:2], np.zeros((2, 2)), n), tied_head(SQs[2:], Tst[2:], np.zeros((2, 2)), n)]
tuples, wb, mb, Pb, mbarb, Cbarb = brute(xi0, C, xis, Z0, heads_t, [np.log(pis[0]), np.log(pis[1])])
RQh = [C @ SQs[:2].T @ inv(SQs[:2] @ C @ SQs[:2].T), C @ SQs[2:].T @ inv(SQs[2:] @ C @ SQs[2:].T)]
report("tiled, C-orthogonal: sum_h R^h_Q S_Qh = I (residual vanishes)", np.max(np.abs(RQh[0] @ SQs[:2] + RQh[1] @ SQs[2:] - np.eye(K))))
report("tiled: R^h_Q = block columns of S_Q^-1", max(np.max(np.abs(RQh[0] - inv(SQs)[:, :2])), np.max(np.abs(RQh[1] - inv(SQs)[:, 2:]))))
wh = [per_head_weights(xi0, C, xis, Z0, SQs[:2], Tst[:2], np.zeros((2, 2)), pis[0]),
      per_head_weights(xi0, C, xis, Z0, SQs[2:], Tst[2:], np.zeros((2, 2)), pis[1])]
Th = inv(SQs) @ Tst


def Pi_of(wpair):
    bold = np.diag(np.concatenate([np.full(2, wpair[0]), np.full(2, wpair[1])]))
    return inv(Tst) @ bold @ Tst


xi_routed = sum(Th @ Pi_of((wh[0][k], wh[1][k])) @ xis[k] for k in range(n))
report("tiled: xi+ = sum_j Th Pi(w_ij) xi_j, Pi(w) = T^-1 bold(w) T (vs brute)", np.max(np.abs(xi_routed - mbarb)))
# Tiled without C-orthogonality: mean uses the exact joint marginals.
Cn = spd(K)
tuples, wb, mb, Pb, mbarb, Cbarb = brute(xi0, Cn, xis, Z0, heads_t, [np.log(pis[0]), np.log(pis[1])])
wbar = [np.array([sum(wb[t] for t in range(len(tuples)) if tuples[t][h] == k) for k in range(n)]) for h in range(2)]
xi_marg = sum(Th @ Pi_of((wbar[0][k], wbar[1][k])) @ xis[k] for k in range(n))
report("tiled, not C-orthogonal: xi+ = sum_j Th Pi(wbar_ij) xi_j with exact marginals", np.max(np.abs(xi_marg - mbarb)))
whn = [per_head_weights(xi0, Cn, xis, Z0, SQs[:2], Tst[:2], np.zeros((2, 2)), pis[0]),
       per_head_weights(xi0, Cn, xis, Z0, SQs[2:], Tst[2:], np.zeros((2, 2)), pis[1])]
dev = max(np.max(np.abs(whn[h] - wbar[h])) for h in range(2))
report("tiled, not C-orthogonal: per-head w^h differ from exact marginals (expected > 0)", dev, ok=bool(dev > 1e-3))

# ==============================================================================================
print("\n(g) Approximations: structured mean field and the power-posterior receiver")
K, r, n = 5, 3, 4
C_i = spd(K)
xi_i = rng.standard_normal(K)
xis = [rng.standard_normal(K) for _ in range(n)]
Cs = [spd(K) for _ in range(n)]
SQ = rng.standard_normal((r, K))
T = rng.standard_normal((r, K))
N = spd(r)
pi = softmax(rng.standard_normal(n))
V = SQ @ C_i @ SQ.T
R = [N + T @ Cs[k] @ T.T for k in range(n)]
# mean-field label cost c_j = -E_{q_i} log N(T xi_j; S_Q X, R_j); closed form and Monte Carlo
cost = np.array([0.5 * ((T @ xis[k] - SQ @ xi_i) @ solve(R[k], T @ xis[k] - SQ @ xi_i)
                        + np.trace(solve(R[k], V)) + slogdet(2 * np.pi * R[k])[1]) for k in range(n)])
Xs = xi_i + rng.standard_normal((400_000, K)) @ np.linalg.cholesky(C_i).T
k = 2
d = T @ xis[k] - Xs @ SQ.T
mc = 0.5 * (np.einsum("ta,ab,tb->t", d, inv(R[k]), d) + slogdet(2 * np.pi * R[k])[1])
z = abs(mc.mean() - cost[k]) / (mc.std() / np.sqrt(len(mc)))
report("mean-field label cost closed form vs MC (|z| < 4)", z, ok=bool(z < 4))
Dg = np.array([kl_gauss(SQ @ xi_i, V, T @ xis[k], R[k]) for k in range(n)])
report("label cost - KL((S_Q)_* q_i || N(T xi_j, R_ij)) is constant in j", np.ptp(cost - Dg))
Dg0 = np.array([kl_gauss(SQ @ xi_i, V, T @ xis[k], T @ Cs[k] @ T.T) for k in range(n)])
cost0 = np.array([0.5 * ((T @ xis[k] - SQ @ xi_i) @ solve(T @ Cs[k] @ T.T, T @ xis[k] - SQ @ xi_i)
                         + np.trace(solve(T @ Cs[k] @ T.T, V)) + slogdet(2 * np.pi * T @ Cs[k] @ T.T)[1]) for k in range(n)])
report("N=0: mean-field label step at the prior = Gibbs routing (tau=1, S_K=T)", np.max(np.abs(softmax(np.log(pi) - cost0) - softmax(np.log(pi) - Dg0))))
# power-posterior receiver (Proposition 4.1(ii)-(iii) of the note) with prior q_i, powers w_ij, constant R
Csh = spd(K)
cf = closed_one_head(xi_i, C_i, xis, [Csh] * n, SQ, T, N, pi)
Rc = cf["R"][0]
Lam = inv(C_i) + SQ.T @ (sum(cf["w"]) * inv(Rc)) @ SQ
eta = solve(C_i, xi_i) + SQ.T @ solve(Rc, sum(cf["w"][k] * T @ xis[k] for k in range(n)))
report("power-posterior receiver mean (powers w) = minimal agent posterior mean", np.max(np.abs(solve(Lam, eta) - cf["mbar"])))
G = cf["G"][0]
report("power-posterior receiver covariance = (I - G S_Q) C_i (omits between-source spread)",
       np.max(np.abs(inv(Lam) - (np.eye(K) - G @ SQ) @ C_i)))

# ==============================================================================================
nfail = sum(1 for _, _, ok in RESULTS if not ok)
print(f"\nSummary: {len(RESULTS)} checks, {len(RESULTS) - nfail} pass, {nfail} fail")
