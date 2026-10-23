r"""Numerical checks for Item_1_communication_links.tex (float64, tiny sizes, single thread).

Each block prints a residual or a dimension. Agreement supports the identities at the tested
instances; the proofs are in the document.
"""
import numpy as np
from scipy.linalg import expm, null_space

rng = np.random.default_rng(20261022)


def spd(n):
    a = rng.standard_normal((n, n))
    return a @ a.T + n * np.eye(n)


def kl_gauss(m1, S1, m2, S2):
    r"""KL(N(m1,S1) || N(m2,S2))."""
    n = len(m1)
    S2i = np.linalg.inv(S2)
    d = m2 - m1
    return 0.5 * (np.trace(S2i @ S1) - n + d @ S2i @ d
                  + np.linalg.slogdet(S2)[1] - np.linalg.slogdet(S1)[1])


K, r = 5, 2
T = rng.standard_normal((r, K))
Sp, Sq = spd(K), spd(K)
m, a = rng.standard_normal(K), rng.standard_normal(K)

# (1) Noiseless reconstruction: gain, projector, law, loss identity.
G = Sp @ T.T @ np.linalg.inv(T @ Sp @ T.T)
P = G @ T
print("(1a) |T G - I|        =", np.abs(T @ G - np.eye(r)).max())
print("(1b) |P^2 - P|        =", np.abs(P @ P - P).max())
mh = (np.eye(K) - P) @ m + P @ a
Sh = (np.eye(K) - P) @ Sp @ (np.eye(K) - P).T + P @ Sq @ P.T
Sh_alt = Sp - G @ T @ Sp + G @ T @ Sq @ T.T @ G.T
print("(1c) covariance forms =", np.abs(Sh - Sh_alt).max())
print("(1d) T-marginal kept  =", np.abs(T @ mh - T @ a).max(), np.abs(T @ Sh @ T.T - T @ Sq @ T.T).max())
loss = kl_gauss(a, Sq, mh, Sh)
chain = kl_gauss(a, Sq, m, Sp) - kl_gauss(T @ a, T @ Sq @ T.T, T @ m, T @ Sp @ T.T)
print("(1e) KL(q||qhat) - [KL(q||p) - KL(Tq||Tp)] =", loss - chain)

# Fiber computation of E_h KL(q(.|h) || p(.|h)) in coordinates of ker T.
N = null_space(T)
Lq, Lp = N.T @ np.linalg.inv(Sq) @ N, N.T @ np.linalg.inv(Sp) @ N   # fiber precisions
# conditional means in fiber coordinates: z = (N^T N)^{-1} N^T (mean - particular solution);
# the difference of conditional means is affine in h; average over h ~ T#q analytically.
Gq = Sq @ T.T @ np.linalg.inv(T @ Sq @ T.T)
Ninv = np.linalg.pinv(N)
# mean_q(h) - mean_p(h) = (a - Gq T a) - (m - G T m) + (Gq - G) h ; project to fiber coords
c0 = Ninv @ ((a - Gq @ T @ a) - (m - G @ T @ m))
C1 = Ninv @ (Gq - G)
hbar, Hcov = T @ a, T @ Sq @ T.T
dmean = c0 + C1 @ hbar
quad = dmean @ Lp @ dmean + np.trace(Lp @ C1 @ Hcov @ C1.T)
kfib = 0.5 * (np.trace(Lp @ np.linalg.inv(Lq)) - (K - r) + quad
              + np.linalg.slogdet(Lq)[1] - np.linalg.slogdet(Lp)[1])
print("(1f) fiber average - KL(q||qhat) =", kfib - loss)

# (2) Noisy channel: Bayesian reconstruction and the bound.
R = spd(r) * 0.3
O = Sp @ T.T @ np.linalg.inv(T @ Sp @ T.T + R)
mh2 = m + O @ T @ (a - m)
Sh2 = Sp - O @ T @ Sp + O @ (T @ Sq @ T.T + R) @ O.T
loss2 = kl_gauss(a, Sq, mh2, Sh2)
bound2 = kl_gauss(a, Sq, m, Sp) - kl_gauss(T @ a, T @ Sq @ T.T + R, T @ m, T @ Sp @ T.T + R)
print("(2a) noisy loss, bound, slack =", loss2, bound2, bound2 - loss2)
Spost = Sp - O @ T @ Sp
print("(2b) posterior precision update =",
      np.abs(np.linalg.inv(Spost) - (np.linalg.inv(Sp) + T.T @ np.linalg.inv(R) @ T)).max())
mi1 = 0.5 * np.linalg.slogdet(np.eye(r) + np.linalg.inv(R) @ T @ Sp @ T.T)[1]
mi2 = 0.5 * (np.linalg.slogdet(Sp)[1] - np.linalg.slogdet(Spost)[1])
print("(2c) mutual information forms   =", mi1 - mi2)

# (3) Exponential of a low-rank generator.
phi1 = lambda Z: np.linalg.solve(Z, expm(Z) - np.eye(len(Z)))
Ot = rng.standard_normal((K, r))
print("(3)  |e^{OT} - I - O phi1(TO) T| =",
      np.abs(expm(Ot @ T) - np.eye(K) - Ot @ phi1(T @ Ot) @ T).max())

# (4) Identifiability of the link from coded messages: Fisher form on gl(K).
C = spd(K)
Rinv = np.linalg.inv(R)
basis = []
for i in range(K):
    for j in range(K):
        E = np.zeros((K, K)); E[i, j] = 1.0; basis.append(E)


def fisher(codes, noises):
    F = np.zeros((K * K, K * K))
    for Tc, Rc in zip(codes, noises):
        Ri = np.linalg.inv(Rc)
        for p, Ep in enumerate(basis):
            for q, Eq in enumerate(basis):
                F[p, q] += np.trace(Ri @ Tc @ Ep @ C @ Eq.T @ Tc.T)
    return F


F1 = fisher([T], [R])
print("(4a) rank F, K*r, K*K =", np.linalg.matrix_rank(F1, tol=1e-9), K * r, K * K)
delta = null_space(T) @ rng.standard_normal((K - r, K))   # T delta = 0
print("(4b) |T e^{-delta} - T| for delta in stabilizer algebra =", np.abs(T @ expm(-delta) - T).max())
vec = delta.reshape(-1)
print("(4c) F(delta,delta) =", vec @ F1 @ vec)

# (5) Several modalities with overlapping row spaces.
T2 = np.vstack([T[0] + 0.0, rng.standard_normal(K)])        # shares one row direction with T
R2 = spd(2) * 0.5
F12 = fisher([T, T2], [R, R2])
stack_rank = np.linalg.matrix_rank(np.vstack([T, T2]))
print("(5)  rank F12, K*rank(stack), stack rank, r1+r2 =",
      np.linalg.matrix_rank(F12, tol=1e-9), K * stack_rank, stack_rank, 4)

# (6) Consensus and holonomy: directed links, energy sum ||mu_i - theta_ij mu_j||^2.
def rot(t):
    return np.array([[np.cos(t), -np.sin(t)], [np.sin(t), np.cos(t)]])


def consensus_kernel(edges, n):
    rows = []
    for (i, j, Th) in edges:
        B = np.zeros((2, 2 * n)); B[:, 2 * i:2 * i + 2] = np.eye(2); B[:, 2 * j:2 * j + 2] = -Th
        rows.append(B)
    B = np.vstack(rows)
    L = B.T @ B
    ev = np.linalg.eigvalsh(L)
    return int((ev < 1e-10).sum()), ev.min()

for alpha in (0.0, 0.7):
    edges = [(0, 1, rot(0.3)), (1, 2, rot(0.5)), (2, 0, rot(-0.8 + alpha))]
    print("(6a) triangle, holonomy angle", alpha, ": kernel dim, lambda_min =", consensus_kernel(edges, 3))
edges = [(0, 1, rot(0.4)), (1, 0, rot(-0.4))]
print("(6b) two-cycle, inverse links : kernel dim, lambda_min =", consensus_kernel(edges, 2))
edges = [(0, 1, rot(0.4)), (1, 0, rot(-0.1))]
print("(6c) two-cycle, holonomy 0.3  : kernel dim, lambda_min =", consensus_kernel(edges, 2))

# (7) Routed modalities: information about theta_ij with routing weights.
# Receiver i, two senders (j=0 target, k=1 other), two heads. Head c hears sender 0 with
# probability b[c]. Complete-data information = sum_c b[c] F_c; with a latent label the
# observed-data information is smaller in the Loewner order (missing information).
K2, M2 = 3, 1
codes = [rng.standard_normal((M2, K2)) for _ in range(2)]          # sender 0 codes, one per head
codes_other = [rng.standard_normal((M2, K2)) for _ in range(2)]    # sender 1 codes
th0, th1 = expm(0.3 * rng.standard_normal((K2, K2))), expm(0.3 * rng.standard_normal((K2, K2)))
Rh = [np.array([[0.5]]), np.array([[0.8]])]
b = np.array([0.7, 0.2])
basis2 = []
for i in range(K2):
    for j in range(K2):
        E = np.zeros((K2, K2)); E[i, j] = 1.0; basis2.append(E)
nsamp = 200000
Y = rng.standard_normal((nsamp, K2)) @ np.linalg.cholesky(spd(K2)).T   # referents, i's coordinates
comp = np.zeros((K2 * K2, K2 * K2))
obs = np.zeros((K2 * K2, K2 * K2))
for c in range(2):
    A0 = codes[c] @ np.linalg.inv(th0)
    A1 = codes_other[c] @ np.linalg.inv(th1)
    lab = rng.random(nsamp) < b[c]
    mean0, mean1 = Y @ A0.T, Y @ A1.T
    noise = rng.standard_normal((nsamp, M2)) * np.sqrt(Rh[c][0, 0])
    msg = np.where(lab[:, None], mean0, mean1) + noise
    Rinv_c = 1.0 / Rh[c][0, 0]
    # score of the component-0 log density with respect to delta (theta0 -> theta0 e^delta)
    dmean = np.stack([-(Y @ (codes[c] @ E @ np.linalg.inv(th0)).T) for E in basis2], axis=2)  # n x M2 x K2^2
    resid = (msg - mean0) * Rinv_c                                                         # n x M2
    s0 = np.einsum('nm,nmp->np', resid, dmean)                                             # d log phi0
    l0 = np.exp(-0.5 * Rinv_c * ((msg - mean0) ** 2).sum(1))
    l1 = np.exp(-0.5 * Rinv_c * ((msg - mean1) ** 2).sum(1))
    w = b[c] * l0 / (b[c] * l0 + (1 - b[c]) * l1)                                         # responsibility
    comp += (s0 * lab[:, None]).T @ s0 / nsamp
    obs += (s0 * w[:, None]).T @ (s0 * w[:, None]) / nsamp
Fpred = np.zeros_like(comp)
Cmat = np.linalg.inv(th0) @ (Y.T @ Y / nsamp) @ np.linalg.inv(th0).T
for c in range(2):
    for p_, Ep in enumerate(basis2):
        for q_, Eq in enumerate(basis2):
            Fpred[p_, q_] += b[c] * np.trace(np.linalg.inv(Rh[c]) @ codes[c] @ Ep @ Cmat @ Eq.T @ codes[c].T)
print("(7a) complete-data info vs sum_c b_c F_c, relative error =",
      np.abs(comp - Fpred).max() / np.abs(Fpred).max())
print("(7b) min eigenvalue of (complete - observed) =", np.linalg.eigvalsh(comp - obs).min())
print("(7c) rank of complete info, K*rank(stacked codes) =",
      np.linalg.matrix_rank(Fpred, tol=1e-9), K2 * np.linalg.matrix_rank(np.vstack(codes)))

# (8) A receiver's reading S of a code T is T theta^{-1} for some theta, unique modulo Stab(T).
Tq, Sq_ = rng.standard_normal((2, 5)), rng.standard_normal((2, 5))
P_ = np.vstack([Tq, null_space(Tq).T]); Q_ = np.vstack([Sq_, null_space(Sq_).T])
theta0_inv = np.linalg.solve(P_, Q_)
print("(8a) |T theta0^{-1} - S| =", np.abs(Tq @ theta0_inv - Sq_).max())
st = np.eye(5) + null_space(Tq) @ rng.standard_normal((3, 5))   # element of Stab(T)
theta1_inv = np.linalg.inv(np.linalg.inv(theta0_inv) @ st)
print("(8b) |T (theta0 s)^{-1} - S| for s in Stab(T) =", np.abs(Tq @ theta1_inv - Sq_).max())

# (9) Dictionary learning with a loop prior: tangent model at the identity dictionaries.
# Edge e = (tail j -> head i) carries omega_e in gl(K), flattened row-major (length m = K^2).
# Tangent grounded model: h = T_e (I - omega_e) y + eps.  Anchor N(0, s2 I), loop energy
# (lam/2) |B omega|_W^2 with (B omega)_gamma = sum of omega_e along gamma.
from scipy.linalg import logm


def gl_fisher(code, Rc, Mc):
    return np.kron(code.T @ np.linalg.inv(Rc) @ code, Mc)


def blockdiag(blocks):
    n = sum(b.shape[0] for b in blocks)
    out = np.zeros((n, n)); k = 0
    for b in blocks:
        s = b.shape[0]; out[k:k + s, k:k + s] = b; k += s
    return out


def loop_matrix(loops, nE, Kd):
    mm = Kd * Kd
    B = np.zeros((len(loops) * mm, nE * mm))
    for g, gam in enumerate(loops):
        for e in gam:
            B[g * mm:(g + 1) * mm, e * mm:(e + 1) * mm] += np.eye(mm)
    return B


def sheaf_h0(edges, codes, nV, Kd):
    rows = []
    for (tail, head), Te in zip(edges, codes):
        Rw = np.zeros((Te.shape[0], nV * Kd))
        Rw[:, head * Kd:(head + 1) * Kd] += Te
        Rw[:, tail * Kd:(tail + 1) * Kd] -= Te
        rows.append(Rw)
    return nV * Kd - np.linalg.matrix_rank(np.vstack(rows), tol=1e-9)


def structure(edges, codes, loops, Kd):
    F = blockdiag([gl_fisher(Te, np.eye(Te.shape[0]), np.eye(Kd)) for Te in codes])
    Z = null_space(F)
    B = loop_matrix(loops, len(edges), Kd)
    rb = np.linalg.matrix_rank(B, tol=1e-9)
    filled = np.linalg.matrix_rank(B @ Z, tol=1e-9)
    return Z, B, dict(dimN=Z.shape[1], rankB=rb, filled=filled,
                      unreach=Z.shape[1] - filled, detect=rb - filled)


def limit_mean(Z, Lam0, w):
    S = Z.T @ Lam0 @ Z
    return w - Z @ np.linalg.solve(S, Z.T @ Lam0 @ w)


def dressed(Kd):
    Sg = spd(Kd)
    return np.kron(np.linalg.inv(Sg), Sg)


Kd = 3; mm = Kd * Kd
# (9a) Tangent Fisher in Kronecker form equals the trace form, kernel dimension K(K - r).
Tc, Rc, Mc = rng.standard_normal((2, Kd)), spd(2), spd(Kd)
dl = rng.standard_normal((Kd, Kd))
print("(9a) kron vs trace Fisher =", abs(dl.flatten() @ gl_fisher(Tc, Rc, Mc) @ dl.flatten()
                                         - np.trace(np.linalg.inv(Rc) @ Tc @ dl @ Mc @ dl.T @ Tc.T)),
      " kernel dim =", null_space(gl_fisher(Tc, Rc, Mc)).shape[1], "expected", Kd * (Kd - 2))

# Directed triangle 0 -> 1 -> 2 -> 0 (edge e carries the code of its tail).
tri_edges = [(0, 1), (1, 2), (2, 0)]
tri_loops = [[0, 1, 2]]

# (9b) Streaming tangent posterior: concentration on the coset and the conditioned-prior limit.
codes2 = [rng.standard_normal((2, Kd)) for _ in range(3)]
R2 = spd(2); Mref = spd(Kd); Lref = np.linalg.cholesky(Mref)
s2, lam = 0.5, 4.0
B = loop_matrix(tri_loops, 3, Kd)
Lam0 = np.eye(3 * mm) / s2 + lam * B.T @ B
Fbar = blockdiag([gl_fisher(Te, R2, Mref) for Te in codes2])
Z = null_space(Fbar); Y = null_space(Z.T)
w_true = 0.1 * rng.standard_normal(3 * mm)
w_inf = limit_mean(Z, Lam0, w_true)
cov_inf = Z @ np.linalg.inv(Z.T @ Lam0 @ Z) @ Z.T
R2i = np.linalg.inv(R2); R2c = np.linalg.cholesky(R2)
for n in (1000, 100000):
    Lam = Lam0.copy(); eta = np.zeros(3 * mm)
    for e, Te in enumerate(codes2):
        ys = rng.standard_normal((n, Kd)) @ Lref.T
        Om = w_true[e * mm:(e + 1) * mm].reshape(Kd, Kd)
        res = -(ys @ Om.T) @ Te.T + rng.standard_normal((n, 2)) @ R2c.T     # h - T y
        Lam[e * mm:(e + 1) * mm, e * mm:(e + 1) * mm] += np.kron(Te.T @ R2i @ Te, ys.T @ ys)
        eta[e * mm:(e + 1) * mm] += -(Te.T @ R2i @ res.T @ ys).flatten()
    cov_n = np.linalg.inv(Lam); mean_n = cov_n @ eta
    ident = n * (Y.T @ cov_n @ Y)
    print("(9b) n =", n, ": |mean - limit| =", np.abs(mean_n - w_inf).max(),
          " |cov - Z S^-1 Z^T| =", np.abs(cov_n - cov_inf).max(),
          " rel |n Y^T cov Y - (Y^T F Y)^-1| =",
          np.abs(ident - np.linalg.inv(Y.T @ Fbar @ Y)).max() / np.abs(ident).max())

# (9c) Without the loop term the limit on N is the prior: mean (I - Z Z^T) w*, covariance s2 Z Z^T.
L00 = np.eye(3 * mm) / s2
print("(9c) lam = 0: |mean - (I - ZZ^T)w*| =",
      np.abs(limit_mean(Z, L00, w_true) - (w_true - Z @ (Z.T @ w_true))).max(),
      " |cov - s2 ZZ^T| =", np.abs(Z @ np.linalg.inv(Z.T @ L00 @ Z) @ Z.T - s2 * Z @ Z.T).max())

# Complete exchange among three agents: six edges, three two-cycles and both directed triangles.
cx_edges = [(1, 0), (0, 1), (2, 1), (1, 2), (0, 2), (2, 0)]
cx_loops = [[0, 1], [2, 3], [4, 5], [1, 3, 5], [4, 2, 0]]   # 0->1->2->0 and 0->2->1->0
codes_sender = [rng.standard_normal((1, Kd)) for _ in range(3)]
cx_codes = [codes_sender[t] for (t, h) in cx_edges]

# (9d) Flat truth: shrinkage formula and exact recovery modulo N cap ker B as lam -> infinity.
Zc, Bc, info = structure(cx_edges, cx_codes, cx_loops, Kd)
Wc = blockdiag([dressed(Kd) for _ in cx_loops])
a_pot = 0.1 * rng.standard_normal((3, mm))
w_flat = np.concatenate([a_pot[h] - a_pot[t] for (t, h) in cx_edges])
print("(9d) flat truth: |B w*| =", np.abs(Bc @ w_flat).max())
Mc_ = Zc.T @ Bc.T @ Wc @ Bc @ Zc
z_true = Zc.T @ w_flat
for lam_ in (2.0, 1e7):
    L0_ = np.eye(len(w_flat)) / s2 + lam_ * Bc.T @ Wc @ Bc
    err = Zc.T @ (limit_mean(Zc, L0_, w_flat) - w_flat)
    pred = -np.linalg.solve(np.eye(Zc.shape[1]) + lam_ * s2 * Mc_, z_true)
    print("     lam =", lam_, ": |err - shrinkage formula| =", np.abs(err - pred).max(),
          " |err| =", np.abs(err).max())

# (9e) Dissonant truth, general W: bias, residual loop defect, detectable dissonance.
w_dis = 0.1 * rng.standard_normal(len(w_flat))
z_dis = Zc.T @ w_dis
Mp = np.linalg.pinv(Mc_, rcond=1e-10)
Pker = np.eye(Zc.shape[1]) - Mp @ Mc_
pred = -Pker @ z_dis - Mp @ Zc.T @ Bc.T @ Wc @ Bc @ w_dis
for lam_ in (1e6, 1e8):
    L0_ = np.eye(len(w_dis)) / s2 + lam_ * Bc.T @ Wc @ Bc
    w_lim = limit_mean(Zc, L0_, w_dis)
    print("(9e) lam =", lam_, ": |Z^T(w_lim - w*) - (-P_ker z* - M^+ Z^T B^T W B w*)| =",
          np.abs(Zc.T @ (w_lim - w_dis) - pred).max())
BZ = Bc @ Zc


def detectable(w):
    v = Bc @ w
    return v @ Wc @ v - v @ Wc @ BZ @ Mp @ BZ.T @ Wc @ v


nu = Zc @ rng.standard_normal(Zc.shape[1])
print("     D(w*) =", detectable(w_dis), " D(w* + nu) =", detectable(w_dis + nu),
      " |B w_lim|_W^2 =", (Bc @ w_lim) @ Wc @ (Bc @ w_lim),
      " |B w*|_W^2 =", (Bc @ w_dis) @ Wc @ (Bc @ w_dis))

# (9f) Dimension counts against the code-sheaf formula.
print("(9f) complete exchange, rank-1 codes:", info,
      " ker B dim =", 6 * mm - np.linalg.matrix_rank(Bc, tol=1e-9), "coboundary dim =", 2 * mm,
      " sheaf K(dim H0 - K) =", Kd * (sheaf_h0(cx_edges, cx_codes, 3, Kd) - Kd))
_, _, info2 = structure(cx_edges, cx_codes, cx_loops[:3], Kd)
pair_unreach = sum(Kd * null_space(np.vstack([codes_sender[i], codes_sender[j]])).shape[1]
                   for i, j in [(0, 1), (1, 2), (0, 2)])
print("     two-cycles only:", info2, " sum over pairs K dim(ker_i cap ker_j) =", pair_unreach)
kvec = rng.standard_normal(Kd)
shared = [rng.standard_normal((1, Kd)) for _ in range(3)]
shared = [c - (c @ kvec) / (kvec @ kvec) * kvec[None, :] for c in shared]   # common kernel vector
sh_codes = [shared[t] for (t, h) in cx_edges]
_, _, info3 = structure(cx_edges, sh_codes, cx_loops, Kd)
print("     common unread direction:", info3, " sheaf K(dim H0 - K) =",
      Kd * (sheaf_h0(cx_edges, sh_codes, 3, Kd) - Kd))
tri_codes = [codes_sender[t] for (t, h) in tri_edges]
_, _, info4 = structure(tri_edges, tri_codes, tri_loops, Kd)
print("     directed triangle, rank-1 codes:", info4, " sheaf K(dim H0 - K) =",
      Kd * (sheaf_h0(tri_edges, tri_codes, 3, Kd) - Kd))

# (9g) Reciprocal pair: three-way split and the detectable two-cycle defect.
pair_edges = [(1, 0), (0, 1)]
for rk in (2, 1):
    T0, T1 = rng.standard_normal((rk, Kd)), rng.standard_normal((rk, Kd))
    Zp, Bp, ip = structure(pair_edges, [T1, T0], [[0, 1]], Kd)
    k0, k1 = null_space(T0), null_space(T1)
    dsum = np.linalg.matrix_rank(np.hstack([k0, k1]), tol=1e-9)
    dcap = k0.shape[1] + k1.shape[1] - dsum
    print("(9g) rank", rk, ":", ip, " predicted filled, unreach, detect =",
          Kd * dsum, Kd * dcap, Kd * (Kd - dsum))
    if Kd - dsum > 0:
        U = null_space(np.hstack([k0, k1]).T)          # basis of row T0 cap row T1
        Pc = U @ U.T
        wp = rng.standard_normal(2 * mm)
        Mp_ = Zp.T @ Bp.T @ Bp @ Zp
        v = Bp @ wp
        Dp = v @ v - v @ Bp @ Zp @ np.linalg.pinv(Mp_, rcond=1e-10) @ Zp.T @ Bp.T @ v
        hol = (wp[:mm] + wp[mm:]).reshape(Kd, Kd)
        wq = wp + Zp @ rng.standard_normal(Zp.shape[1])
        vq = Bp @ wq
        Dq = vq @ vq - vq @ Bp @ Zp @ np.linalg.pinv(Mp_, rcond=1e-10) @ Zp.T @ Bp.T @ vq
        print("     D(w*) =", Dp, " D(w* + nu) =", Dq,
              " |P_(row cap row)(w01 + w10)|_F^2 =", np.sum((Pc @ hol) ** 2))

# (9h) Exact pair (no linearization): reciprocal residual set is Stab(T_1) cap Stab(T_0 theta*).
th = expm(0.6 * rng.standard_normal((Kd, Kd)))
for rk in (2, 1):
    T0, T1 = rng.standard_normal((rk, Kd)), rng.standard_normal((rk, Kd))
    kst = null_space(np.vstack([T1, T0 @ th]))
    print("(9h) rank", rk, ": dim of residual Lie algebra K dim ker(T1; T0 theta*) =", Kd * kst.shape[1])
    if kst.shape[1] > 0:
        s_el = np.eye(Kd) + 0.7 * kst @ rng.standard_normal((kst.shape[1], Kd))
        th01 = th @ s_el; th10 = np.linalg.inv(th01)
        print("     |T1 th01^-1 - T1 th*^-1| =", np.abs(T1 @ np.linalg.inv(th01) - T1 @ np.linalg.inv(th)).max(),
              " |T0 th10^-1 - T0 th*| =", np.abs(T0 @ np.linalg.inv(th10) - T0 @ th).max(),
              " |th01 th10 - I| =", np.abs(th01 @ th10 - np.eye(Kd)).max(),
              " |th01 - th*| =", np.abs(th01 - th).max())

# (9i) Exact flat constraint on the complete exchange with a common unread direction.
gs = [expm(0.5 * rng.standard_normal((Kd, Kd))) for _ in range(3)]
codes_ref = [shared[v] @ np.linalg.inv(gs[v]) for v in range(3)]          # T_j = T'_j g_j^-1
us = [np.eye(Kd) + np.outer(kvec, 0.4 * rng.standard_normal(Kd)) for _ in range(3)]
th_true = {(t, h): gs[h] @ np.linalg.inv(gs[t]) for (t, h) in cx_edges}
th_alt = {(t, h): gs[h] @ us[h] @ np.linalg.inv(us[t]) @ np.linalg.inv(gs[t]) for (t, h) in cx_edges}
msg = max(np.abs(codes_ref[t] @ np.linalg.inv(th_alt[(t, h)])
                 - codes_ref[t] @ np.linalg.inv(th_true[(t, h)])).max() for (t, h) in cx_edges)
hol = 0.0
for gam in cx_loops:
    H = np.eye(Kd)
    for e in gam:
        H = th_alt[cx_edges[e]] @ H
    hol = max(hol, np.abs(H - np.eye(Kd)).max())
dist = max(np.abs(th_alt[k] - th_true[k]).max() for k in cx_edges)
print("(9i) max message-law change =", msg, " max |H - I| =", hol, " max |theta - theta*| =", dist)

# (9j) Receiver-factorized recognition law: exact means, overconfident variances.
Fx = blockdiag([gl_fisher(Te, np.eye(1), Mref) for Te in cx_codes])
Lam_x = np.eye(6 * mm) / s2 + 3.0 * Bc.T @ Bc + 50.0 * Fx
eta_x = rng.standard_normal(6 * mm)
owner = [h for (t, h) in cx_edges]
blocks = [np.concatenate([np.arange(e * mm, (e + 1) * mm) for e in range(6) if owner[e] == i]) for i in range(3)]
mf = np.zeros(6 * mm)
for sweep in range(400):
    for idx in blocks:
        rest = np.setdiff1d(np.arange(6 * mm), idx)
        mf[idx] = np.linalg.solve(Lam_x[np.ix_(idx, idx)], eta_x[idx] - Lam_x[np.ix_(idx, rest)] @ mf[rest])
exact = np.linalg.solve(Lam_x, eta_x)
Cx = np.linalg.inv(Lam_x)
gaps = [np.linalg.eigvalsh(Cx[np.ix_(idx, idx)] - np.linalg.inv(Lam_x[np.ix_(idx, idx)])).min() for idx in blocks]
tr_ex = sum(np.trace(Cx[np.ix_(idx, idx)]) for idx in blocks)
tr_mf = sum(np.trace(np.linalg.inv(Lam_x[np.ix_(idx, idx)])) for idx in blocks)
print("(9j) |mean-field mean - exact mean| =", np.abs(mf - exact).max(),
      " min eig(exact block cov - MF cov) =", min(gaps), " trace exact, MF =", tr_ex, tr_mf)

# (9k) Linearized holonomy: |log H - sum omega| is second order.
dirs = [rng.standard_normal((Kd, Kd)) for _ in range(3)]
for eps in (1e-2, 1e-3):
    xs = [eps * d for d in dirs]
    H = expm(xs[2]) @ expm(xs[1]) @ expm(xs[0])
    print("(9k) eps =", eps, ": |log H - sum x| / eps^2 =", np.abs(logm(H).real - sum(xs)).max() / eps ** 2)

# (10) Location families beyond Gaussian noise: Student-t noise, Fisher form tr(J_f T delta C delta^T T^T).
nu, Kt, rt, ns = 5.0, 3, 2, 400000
Tt = rng.standard_normal((rt, Kt)); th_t = expm(0.3 * rng.standard_normal((Kt, Kt)))
Mt = spd(Kt) / Kt; Lt = np.linalg.cholesky(Mt)
Ct = np.linalg.inv(th_t) @ Mt @ np.linalg.inv(th_t).T
dl_t = rng.standard_normal((Kt, Kt))
ys_t = rng.standard_normal((ns, Kt)) @ Lt.T
eps_t = rng.standard_t(nu, size=(ns, rt))
grad_logf = -(nu + 1) * eps_t / (nu + eps_t ** 2)
dmu = ys_t @ np.linalg.inv(th_t).T @ dl_t.T @ Tt.T                      # rows: T delta theta^{-1} y
score = np.sum(grad_logf * dmu, axis=1)
Jf = (nu + 1) / (nu + 3) * np.eye(rt)
pred_t = np.trace(Jf @ Tt @ dl_t @ Ct @ dl_t.T @ Tt.T)
print("(10) Student-t location family: Monte Carlo Fisher", np.mean(score ** 2), " formula", pred_t,
      " relative difference", abs(np.mean(score ** 2) - pred_t) / pred_t)
