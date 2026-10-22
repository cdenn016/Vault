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
