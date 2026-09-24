r"""L07: recompute PIFB2 Appendix D (covariance fixed point, stability) in small instances.

Receiver-only, frozen-attention surrogate (PIFB2.tex 2662-2891):
  dF_i/dSigma_i = 1/2 [ -2 Sigma_i^{-1} + A_i + sum_j beta_ij (Om_ij Sigma_j Om_ij^T)^{-1} ],
  A_i = Sigma_{p,i}^{-1} + Lambda_{o,i}.
In precision coordinates Lambda_i = Sigma_i^{-1} the stationarity condition is LINEAR:
  2 Lambda = A + L(Lambda),  L(Lambda)_i = sum_j beta_ij Om_ij^{-T} Lambda_j Om_ij^{-1}.
Natural-gradient flow dSigma/dt = -2 eta Sigma (dF/dSigma) Sigma  <=>  dLambda/dt = eta (A + L(Lambda) - 2 Lambda).
"""
import numpy as np

rng = np.random.default_rng(7)
K = 2
sym = lambda X: 0.5 * (X + X.T)


def spd(K, s=1.0):
    B = rng.normal(size=(K, K))
    return B @ B.T + s * np.eye(K)


def F_i(i, Sig, mu, Sp, mup, Lo, beta, Om):
    """Receiver free energy of agent i (Gaussian KLs, obs term), senders frozen."""
    def kl(m1, S1, m2, S2):
        S2i = np.linalg.inv(S2)
        d = m2 - m1
        return 0.5 * (np.trace(S2i @ S1) + d @ S2i @ d - K + np.log(np.linalg.det(S2) / np.linalg.det(S1)))
    val = kl(mu[i], Sig[i], mup[i], Sp[i])
    for j in range(len(Sig)):
        if j != i and beta[i, j] > 0:
            val += beta[i, j] * kl(mu[i], Sig[i], Om[i][j] @ mu[j], Om[i][j] @ Sig[j] @ Om[i][j].T)
    val += 0.5 * np.trace(Lo[i] @ Sig[i])
    return val


def grad_formula(i, Sig, Sp, Lo, beta, Om):
    G = -2 * np.linalg.inv(Sig[i]) + np.linalg.inv(Sp[i]) + Lo[i]
    for j in range(len(Sig)):
        if j != i:
            G += beta[i, j] * np.linalg.inv(Om[i][j] @ Sig[j] @ Om[i][j].T)
    return 0.5 * G


def Lmap(Lam, beta, Om):
    N = len(Lam)
    out = []
    for i in range(N):
        acc = np.zeros((K, K))
        for j in range(N):
            if j != i and beta[i, j] > 0:
                Oi = np.linalg.inv(Om[i][j])
                acc += beta[i, j] * Oi.T @ Lam[j] @ Oi
        out.append(acc)
    return out


def sym_basis(K):
    B = []
    for a in range(K):
        for b in range(a, K):
            E = np.zeros((K, K)); E[a, b] = 1; E[b, a] = 1
            B.append(E / (np.sqrt(2) if a != b else 1))
    return B


def op_matrix(fun, N):
    """Matrix of a linear map on (Sym_K)^N in an orthonormal basis."""
    B = sym_basis(K); nb = len(B)
    M = np.zeros((N * nb, N * nb))
    for i in range(N):
        for a, E in enumerate(B):
            X = [np.zeros((K, K)) for _ in range(N)]; X[i] = E
            Y = fun(X)
            for k in range(N):
                for b, Eb in enumerate(B):
                    M[k * nb + b, i * nb + a] = np.sum(Y[k] * Eb)
    return M


def rhoL(beta, Om, N):
    return max(abs(np.linalg.eigvals(op_matrix(lambda X: Lmap(X, beta, Om), N))))


def solve_linear(A, beta, Om, N):
    Lm = op_matrix(lambda X: Lmap(X, beta, Om), N)
    B = sym_basis(K); nb = len(B)
    a = np.concatenate([[np.sum(A[i] * E) for E in B] for i in range(N)])
    x = np.linalg.solve(2 * np.eye(N * nb) - Lm, a)
    return [sum(x[i * nb + b] * B[b] for b in range(nb)) for i in range(N)]


def picard(A, beta, Om, N, iters=400):
    Sig = [np.eye(K) for _ in range(N)]
    for _ in range(iters):
        Lam = [np.linalg.inv(S) for S in Sig]
        LL = Lmap(Lam, beta, Om)
        Sig = [2 * np.linalg.inv(A[i] + LL[i]) for i in range(N)]
    return Sig


print("== 1. covariance gradient formula vs finite differences (N=3, GL transports) ==")
N = 3
Sig = [spd(K) for _ in range(N)]; Sp = [spd(K) for _ in range(N)]; Lo = [0.3 * spd(K, 0.1) for _ in range(N)]
mu = [rng.normal(size=K) for _ in range(N)]; mup = [rng.normal(size=K) for _ in range(N)]
beta = rng.random((N, N)); np.fill_diagonal(beta, 0); beta /= beta.sum(1, keepdims=True)
Om = [[np.eye(K) + 0.15 * rng.normal(size=(K, K)) for _ in range(N)] for _ in range(N)]
i = 0; h = 1e-6; G = grad_formula(i, Sig, Sp, Lo, beta, Om); err = 0
for a in range(K):
    for b in range(K):
        E = np.zeros((K, K)); E[a, b] += 0.5; E[b, a] += 0.5
        Sp_ = [S.copy() for S in Sig]; Sm_ = [S.copy() for S in Sig]
        Sp_[i] = Sig[i] + h * E; Sm_[i] = Sig[i] - h * E
        fd = (F_i(i, Sp_, mu, Sp, mup, Lo, beta, Om) - F_i(i, Sm_, mu, Sp, mup, Lo, beta, Om)) / (2 * h)
        err = max(err, abs(fd - np.sum(G * E)))
print("max |FD - formula| =", err)

print("== 2. fixed point: Picard iteration of T vs exact linear solve in precision coords ==")
A = [np.linalg.inv(Sp[k]) + Lo[k] for k in range(N)]
r = rhoL(beta, Om, N)
Cmax = max(max(np.linalg.eigvalsh(sum(beta[k, j] * np.linalg.inv(Om[k][j] @ Om[k][j].T) for j in range(N) if j != k))) for k in range(N))
print("rho(L) =", r, " max_i lambda_max(C_i) =", Cmax)
Lam_lin = solve_linear(A, beta, Om, N)
Sig_pic = picard(A, beta, Om, N)
print("max |Sigma_picard - inv(Lambda_linear)| =", max(np.abs(Sig_pic[k] - np.linalg.inv(Lam_lin[k])).max() for k in range(N)))
print("stationarity residual:", max(np.abs(grad_formula(k, Sig_pic, Sp, Lo, beta, Om)).max() for k in range(N)))

print("== 3. homogeneous limit ==")
S0 = spd(K); Lo0 = 0.5 * spd(K, 0.1); Nh = 4
bh = np.ones((Nh, Nh)) - np.eye(Nh); bh /= bh.sum(1, keepdims=True)
Omh = [[np.eye(K) for _ in range(Nh)] for _ in range(Nh)]
Sh = picard([np.linalg.inv(S0)] * Nh, bh, Omh, Nh)
print("Lambda_o=0: |Sigma_inf - Sigma_0| =", np.abs(Sh[0] - S0).max())
Sh2 = picard([np.linalg.inv(S0) + Lo0] * Nh, bh, Omh, Nh)
print("Lambda_o>0: |Sigma_inf - (Sigma_0^-1+Lambda_o)^-1| =", np.abs(Sh2[0] - np.linalg.inv(np.linalg.inv(S0) + Lo0)).max())

print("== 4. own-block Hessian = Sigma^-1 X Sigma^-1 (FD) ==")
X = sym(rng.normal(size=(K, K))); Sg = [S.copy() for S in Sig]; Sg[i] = Sig[i] + h * X
Hfd = (grad_formula(i, Sg, Sp, Lo, beta, Om) - grad_formula(i, Sig, Sp, Lo, beta, Om)) / h
Li = np.linalg.inv(Sig[i]); print("max |FD - Lam X Lam| =", np.abs(Hfd - Li @ X @ Li).max())


def jacobians(Lam, beta, Om, N):
    """Joint receiver-only Jacobians at a fixed point: natural (Sigma coords) and Euclidean."""
    Lm = op_matrix(lambda X: Lmap(X, beta, Om), N)
    D = op_matrix(lambda X: [Lam[k] @ X[k] @ Lam[k] for k in range(N)], N)
    I = np.eye(Lm.shape[0])
    J_euc = -(I - 0.5 * Lm) @ D                        # eta = 1
    Dinv = op_matrix(lambda X: [np.linalg.inv(Lam[k]) @ X[k] @ np.linalg.inv(Lam[k]) for k in range(N)], N)
    J_nat = -2 * Dinv @ (I - 0.5 * Lm) @ D
    return np.linalg.eigvals(J_nat), np.linalg.eigvals(J_euc)


en, ee = jacobians(Lam_lin, beta, Om, N)
print("== 5. joint receiver-only Jacobian at the fixed point (random instance) ==")
print("natural: max Re =", en.real.max(), " predicted -2(1-rho/2) =", -2 * (1 - r / 2))
print("euclid : max Re =", ee.real.max())

print("== 6. flat GL connection: C_i condition fails, fixed point still exists ==")
U = [np.diag([10.0, 1.0]), np.eye(2), np.array([[1.0, 3.0], [0.0, 0.5]])]
Omf = [[U[a] @ np.linalg.inv(U[b]) for b in range(3)] for a in range(3)]
Cf = max(max(np.linalg.eigvalsh(sum(beta[k, j] * np.linalg.inv(Omf[k][j] @ Omf[k][j].T) for j in range(3) if j != k))) for k in range(3))
rf = rhoL(beta, Omf, 3)
Lf = solve_linear(A, beta, Omf, 3)
print("max lambda_max(C_i) =", Cf, " rho(L) =", rf, " min eig of Lambda* =", min(min(np.linalg.eigvalsh(l)) for l in Lf))
en, ee = jacobians(Lf, beta, Omf, 3)
print("natural max Re =", en.real.max(), " euclid max Re =", ee.real.max())

print("== 7. GL holonomy with rho(L) > 2: no SPD fixed point, precision runaway ==")
a = 0.6
Om2 = [[np.eye(2), np.diag([a, 1.0])], [np.diag([a, 1.0]), np.eye(2)]]
b2 = np.array([[0, 1.0], [1.0, 0]])
r2 = rhoL(b2, Om2, 2); print("holonomy diag(a^2,1), a=0.6: rho(L) = 1/a^2 =", r2)
A2 = [np.eye(2), np.eye(2)]
Lam = [np.eye(2), np.eye(2)]; dt = 0.01
for step in range(3000):
    LL = Lmap(Lam, b2, Om2)
    Lam = [Lam[k] + dt * (A2[k] + LL[k] - 2 * Lam[k]) for k in range(2)]
print("after t=30 natural-gradient flow: Lambda_1 diag =", np.diag(Lam[0]), "(runaway in e1; e2 converges to 1)")
Sp2 = picard(A2, b2, Om2, 2, iters=60)
print("Picard iterate Sigma_1 after 60 steps:", np.diag(Sp2[0]))

print("== 8. alignment-dominated limit (coupling A_c): (1+A_c) Lam = A + A_c L(Lam) ==")
for label, Omx, bx, Nx in [("orthogonal/flat (rho=1)", Omf, beta, 3), ("holonomy a=0.9 (rho>1)", [[np.eye(2), np.diag([0.9, 1.0])], [np.diag([0.9, 1.0]), np.eye(2)]], b2, 2),
                           ("holonomy a=1.2 (rho<1)", [[np.eye(2), np.diag([1.2, 1.0])], [np.diag([1.2, 1.0]), np.eye(2)]], b2, 2)]:
    rx = rhoL(bx, Omx, Nx); Ax = [np.eye(2)] * Nx
    Lm = op_matrix(lambda X: Lmap(X, bx, Omx), Nx); B = sym_basis(K); nb = len(B)
    ax = np.concatenate([[np.sum(Ax[k] * E) for E in B] for k in range(Nx)])
    out = []
    for Ac in [1, 10, 100, 1000]:
        Mx = (1 + Ac) * np.eye(Nx * nb) - Ac * Lm
        ev = np.linalg.eigvals(Mx)
        if ev.real.min() <= 0:
            out.append((Ac, "no SPD fixed point (1+A_c <= A_c rho)")); continue
        x = np.linalg.solve(Mx, ax)
        L0 = sum(x[b] * B[b] for b in range(nb))
        out.append((Ac, np.round(np.linalg.eigvalsh(L0), 4)))
    print(label, "rho(L)=%.4f" % rx, out)

print("== 9. search: rho(L)<2 but Euclidean receiver-only flow unstable? (K=2, N=2..3) ==")
worst = -np.inf; found = None
for trial in range(4000):
    Nn = rng.integers(2, 4)
    bb = rng.random((Nn, Nn)); np.fill_diagonal(bb, 0); bb /= bb.sum(1, keepdims=True)
    Oo = [[np.eye(K) + rng.normal(scale=rng.choice([0.3, 0.8, 1.5]), size=(K, K)) for _ in range(Nn)] for _ in range(Nn)]
    if any(np.linalg.det(Oo[p][q]) <= 0.05 for p in range(Nn) for q in range(Nn)):
        continue
    rr = rhoL(bb, Oo, Nn)
    if rr >= 1.95:
        continue
    Aa = [spd(K, 0.01) * rng.choice([0.01, 1, 100]) for _ in range(Nn)]
    Ll = solve_linear(Aa, bb, Oo, Nn)
    if min(min(np.linalg.eigvalsh(l)) for l in Ll) <= 0:
        continue
    en, ee = jacobians(Ll, bb, Oo, Nn)
    if ee.real.max() > worst:
        worst = ee.real.max(); found = (rr, en.real.max(), ee.real.max())
print("largest Euclidean max-Re eigenvalue found (rho, natural maxRe, euclid maxRe):", found)
