r"""Float64 checks for link_curvature.tex (small dimensions; grounding only, not evidence about large N)."""
import numpy as np
from scipy.linalg import expm, logm, sqrtm

rng = np.random.default_rng(7)
rel = lambda a, b: np.abs(a - b).max() / max(1.0, np.abs(b).max())
K = 4
inv = np.linalg.inv


def rand_gl(scale=0.4):
    return expm(scale * rng.standard_normal((K, K)))


print("== 1. Flat <=> recurrent; invertible flat <=> pure gauge; singular counterexample ==")
N = 6
A = [rand_gl() for _ in range(N)]                                  # adjacent links A_i, invertible


def prod(i, j):                                                    # Theta_ij = A_i ... A_{j+1}, i > j
    M = np.eye(K)
    for m in range(i, j, -1):
        M = M @ A[m]
    return M


Th = {(i, j): prod(i, j) for i in range(N) for j in range(i)}
F = lambda T, i, j, k: inv(T[(i, k)]) @ T[(i, j)] @ T[(j, k)]
worst = max(np.abs(F(Th, i, j, k) - np.eye(K)).max() for i in range(N) for j in range(i) for k in range(j))
print("recurrent links: max |F_ijk - I| over all triples          ", worst)
g = [np.eye(K)] + [prod(i, 0) for i in range(1, N)]                # g_i = Theta_i0, g_0 = I
print("pure gauge: Theta_ij = g_i g_j^-1, max err                  ",
      max(np.abs(Th[(i, j)] - g[i] @ inv(g[j])).max() for i in range(N) for j in range(i)))
P = np.zeros((K, K)); P[0, 0] = 1.0                                # shared projector, singular
print("singular shared projector is flat (Theta_ij Theta_jk = Theta_ik): err",
      max(np.abs(P @ P - P).max() for _ in range(1)), " rank", np.linalg.matrix_rank(P), "(cannot be g_i g_j^-1)")

print("\n== 2. Curvature of candidate generators ==")
Fr = [rand_gl(0.3) for _ in range(N)]                              # frames U_i
X = 0.3 * rng.standard_normal((K, K))
Tc = {(i, j): Fr[i] @ expm(X) @ inv(Fr[j]) for i in range(N) for j in range(i)}
print("constant generator: F_ijk = U_k e^X U_k^-1, max err         ",
      max(np.abs(F(Tc, i, j, k) - Fr[k] @ expm(X) @ inv(Fr[k])).max() for i in range(N) for j in range(i) for k in range(j)))
pos = np.arange(N, dtype=float)
Tp = {(i, j): Fr[i] @ expm((pos[i] - pos[j]) * X) @ inv(Fr[j]) for i in range(N) for j in range(i)}
print("positional generator (p_i-p_j) X: max |F - I|               ",
      max(np.abs(F(Tp, i, j, k) - np.eye(K)).max() for i in range(N) for j in range(i) for k in range(j)))
H, d = 2, 2
Oq, _ = np.linalg.qr(rng.standard_normal((K, K))); Tq = inv(Oq)    # T O = I
Bd = lambda b: np.kron(np.diag(b), np.eye(d))
bw = {(i, j): rng.uniform(0.05, 0.9, H) for i in range(N) for j in range(i)}
Tr = {e: Fr[e[0]] @ expm(Oq @ Bd(bw[e]) @ Tq) @ inv(Fr[e[1]]) for e in bw}
err = 0.0
for i in range(N):
    for j in range(i):
        for k in range(j):
            pred = Fr[k] @ Oq @ expm(Bd(bw[(i, j)] + bw[(j, k)] - bw[(i, k)])) @ Tq @ inv(Fr[k])
            err = max(err, np.abs(F(Tr, i, j, k) - pred).max())
print("routed exponent: F = U_k O exp(b_ij+b_jk-b_ik) T U_k^-1, err", err)
Tm = {e: Fr[e[0]] @ Oq @ Bd(bw[e]) @ Tq @ inv(Fr[e[1]]) for e in bw}
err = 0.0
for i in range(N):
    for j in range(i):
        for k in range(j):
            pred = Fr[k] @ Oq @ Bd(bw[(i, j)] * bw[(j, k)] / bw[(i, k)]) @ Tq @ inv(Fr[k])
            err = max(err, np.abs(F(Tm, i, j, k) - pred).max())
print("head-sum: F = U_k O diag(b_ij b_jk / b_ik) T U_k^-1, err    ", err)
com = lambda a, b: a @ b - b @ a
A0, B0, Z0 = (rng.standard_normal((K, K)) for _ in range(3))
for eps in (1e-1, 5e-2, 2.5e-2):
    Aa, Bb, Zz = eps * A0, eps * B0, eps * Z0
    lg = np.real(logm(expm(-Zz) @ expm(Aa) @ expm(Bb)))
    first = Aa + Bb - Zz
    second = first + 0.5 * (com(Aa, Bb) - com(Zz, Aa) - com(Zz, Bb))
    print(f"BCH eps={eps:g}: |logF-first order|={np.abs(lg-first).max():.2e}  |logF-second order|={np.abs(lg-second).max():.2e}")

print("\n== 3. Flat normalized head-sum routing: beta_ij = c_i / c_j on the strict past ==")
c = np.array([1.0, 0.5, 0.2, 0.05, 0.01])
Nb = len(c); Bm = np.zeros((Nb, Nb))
for i in range(Nb):
    for j in range(i):
        Bm[i, j] = c[i] / c[j]
    Bm[i, i] = 1 - Bm[i, :i].sum()
print("rows sum to 1:", np.allclose(Bm.sum(1), 1), " diagonal:", np.round(np.diag(Bm), 3), " all positive:", bool((Bm[np.tril_indices(Nb)] > 0).all()))
print("strict-triangle cocycle beta_ij beta_jk = beta_ik, max err:",
      max(abs(Bm[i, j] * Bm[j, k] - Bm[i, k]) for i in range(Nb) for j in range(i) for k in range(j)))
unif = np.tril(np.ones((Nb, Nb))); unif /= unif.sum(1, keepdims=True)
print("uniform causal attention: max |beta_ij beta_jk - beta_ik| over strict triangles:",
      max(abs(unif[i, j] * unif[j, k] - unif[i, k]) for i in range(Nb) for j in range(i) for k in range(j)))

print("\n== 4. Regression links of a joint Gaussian; Markov <=> flat ==")


def joint_generic(n_tokens):
    M = rng.standard_normal((n_tokens * K, n_tokens * K))
    return M @ M.T + 0.5 * np.eye(n_tokens * K)


def joint_chain(n_tokens):
    Aar = 0.5 * expm(0.3 * rng.standard_normal((K, K)))
    Aar = Aar / max(1.0, 1.2 * np.abs(np.linalg.eigvals(Aar)).max())
    Sii = [np.eye(K)]
    for i in range(1, n_tokens):
        Sii.append(Aar @ Sii[-1] @ Aar.T + np.eye(K))
    S = [[None] * n_tokens for _ in range(n_tokens)]
    for i in range(n_tokens):
        S[i][i] = Sii[i]
        for j in range(i):
            S[i][j] = np.linalg.matrix_power(Aar, i - j) @ Sii[j]
            S[j][i] = S[i][j].T
    return np.block(S), Aar


blk = lambda S, a, b: S[a * K:(a + 1) * K, b * K:(b + 1) * K]
Wlink = lambda S, a, b: blk(S, a, b) @ inv(blk(S, b, b))
S = joint_generic(3)
i_, j_, k_ = 2, 1, 0
Sik_j = blk(S, i_, k_) - blk(S, i_, j_) @ inv(blk(S, j_, j_)) @ blk(S, j_, k_)
lhs = Wlink(S, i_, j_) @ Wlink(S, j_, k_)
print("W_ij W_jk = W_ik - Sigma_ik|j Sigma_kk^-1  err:", rel(lhs, Wlink(S, i_, k_) - Sik_j @ inv(blk(S, k_, k_))))
Fm = inv(Wlink(S, i_, k_)) @ lhs
print("F = I - W_ik^-1 Sigma_ik|j Sigma_kk^-1      err:", rel(Fm, np.eye(K) - inv(Wlink(S, i_, k_)) @ Sik_j @ inv(blk(S, k_, k_))))
Sc, Aar = joint_chain(5)
print("AR(1) chain: max |F_ijk - I| over triples:",
      max(np.abs(inv(Wlink(Sc, i, k)) @ Wlink(Sc, i, j) @ Wlink(Sc, j, k) - np.eye(K)).max() for i in range(5) for j in range(i) for k in range(j)))
print("AR(1) chain: W_ij = A^(i-j), max err:", max(np.abs(Wlink(Sc, i, j) - np.linalg.matrix_power(Aar, i - j)).max() for i in range(5) for j in range(i)))
print("generic joint: |F - I| =", np.abs(Fm - np.eye(K)).max(), " (not Markov)")
gs_ = [rand_gl() for _ in range(3)]
Gbd = np.block([[gs_[a] if a == b else np.zeros((K, K)) for b in range(3)] for a in range(3)])
Sg = Gbd @ S @ Gbd.T
print("W_ab -> g_a W_ab g_b^-1 under distinct per-token frames, err:", rel(Wlink(Sg, 2, 1), gs_[2] @ Wlink(S, 2, 1) @ inv(gs_[1])))

print("\n-- reduced-rank regression: rank-d optimum of E||Sii^-1/2 (xi_i - W xi_j)||^2 --")
d_ = 2
Sii, Sjj, Sij = blk(S, 2, 2), blk(S, 1, 1), blk(S, 2, 1)
msqrt = lambda M: np.real(sqrtm(M))
Sii_h, Sjj_h = msqrt(Sii), msqrt(Sjj)
Uu, sv, Vt = np.linalg.svd(inv(Sii_h) @ Sij @ inv(Sjj_h))
Wd = Sii_h @ (Uu[:, :d_] * sv[:d_]) @ Vt[:d_] @ inv(Sjj_h)


def risk(W):
    R = inv(Sii_h) @ (Sii - W @ Sij.T - Sij @ W.T + W @ Sjj @ W.T) @ inv(Sii_h)
    return np.trace(R)


print("rank of reduced-rank predictor:", np.linalg.matrix_rank(Wd), " risk(full) =", round(risk(Sij @ inv(Sjj)), 4), " risk(rank-2) =", round(risk(Wd), 4))
Afac = Sii_h @ (Uu[:, :d_] * sv[:d_]); Bfac = Vt[:d_] @ inv(Sjj_h)
assert np.allclose(Afac @ Bfac, Wd)
base = risk(Wd)
worst_local = min(risk((Afac + 1e-2 * rng.standard_normal(Afac.shape)) @ (Bfac + 1e-2 * rng.standard_normal(Bfac.shape))) - base
                  for _ in range(4000))
print("min over 4000 factor perturbations (A+dA)(B+dB) of risk - risk(Wd):", worst_local, " (>= 0: local optimality within rank 2)")
print("risk(Wd) - risk(full) =", round(base - risk(Sij @ inv(Sjj)), 6), "  sum of squared discarded singular values =", round(float(np.sum(sv[d_:] ** 2)), 6))
print("no random rank-2 matrix beats it:", min(risk(rng.standard_normal((K, d_)) @ rng.standard_normal((d_, K))) for _ in range(4000)) >= base)

print("\n== 5. Fisher metric pulled back to the group link; barrier at the singular boundary ==")
mu = rng.standard_normal(K)
Lc = np.tril(rng.standard_normal((K, K)), -1) + np.diag(rng.uniform(0.7, 1.5, K)); Sg0 = Lc @ Lc.T


def kl(m0, S0, m1, S1):
    S1i = inv(S1); dm = m1 - m0
    return 0.5 * (np.trace(S1i @ S0) + dm @ S1i @ dm - K + np.linalg.slogdet(S1)[1] - np.linalg.slogdet(S0)[1])


g0 = rand_gl(0.3); Aal = rng.standard_normal((K, K))
m0, S0 = g0 @ mu, g0 @ Sg0 @ g0.T
Lp = np.linalg.cholesky(S0); Z = inv(Lp) @ Aal @ Lp; eta = inv(Lp) @ m0
ds2 = np.sum((Z @ eta) ** 2) + 2 * np.sum(((Z + Z.T) / 2) ** 2)
for t in (1e-2, 5e-3, 2.5e-3):
    g1 = expm(t * Aal) @ g0
    print(f"t={t:g}: 2 KL(q_g1 || q_g0) / (t^2 ds^2) = {2 * kl(g1 @ mu, g1 @ Sg0 @ g1.T, m0, S0) / (t ** 2 * ds2):.6f}  (-> 1)")
Xg = 0.3 * rng.standard_normal((K, K)); dX = rng.standard_normal((K, K)); h = 1e-6
fd = (expm(Xg + h * dX) - expm(Xg - h * dX)) / (2 * h)
ss = np.linspace(0, 1, 4001)
vals = np.array([expm(s * Xg) @ dX @ expm(-s * Xg) for s in ss])
Aint = np.trapezoid(vals, ss, axis=0)
print("dexp: (int_0^1 e^{sX} dX e^{-sX} ds) e^X = d e^X   rel err:", rel(Aint @ expm(Xg), fd))
for s in (1e-1, 1e-2, 1e-3, 1e-4):
    gs = np.diag([s] + [1.0] * (K - 1))
    print(f"sigma_min={s:g}: KL(q_t||q_0) = {kl(gs @ mu, gs @ gs.T, mu, np.eye(K)):8.3f}   -log sigma_min = {-np.log(s):7.3f}   "
          f"Fisher length of the path = {np.sqrt(mu[0] ** 2 + 2) * -np.log(s):7.3f}")
