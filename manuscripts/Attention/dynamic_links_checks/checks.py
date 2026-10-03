"""Float64 checks for dynamic_links.tex (latent link generators X_ij), October 3, 2026.

Small sizes only (K <= 4, a few tokens). Each block prints the quantity the note states and the
largest residual. Run: C:/anaconda/python.exe checks.py  (numpy, scipy).
"""
import numpy as np
from scipy.linalg import expm, expm_frechet, logm
from scipy.optimize import minimize

rng = np.random.default_rng(20261003)
np.set_printoptions(precision=4, suppress=True)


def header(title):
    print("\n" + "=" * 78 + "\n" + title + "\n" + "=" * 78)


def rand_orth(K):
    Q, R = np.linalg.qr(rng.standard_normal((K, K)))
    Q = Q * np.sign(np.diag(R))
    if np.linalg.det(Q) < 0:
        Q[:, 0] *= -1
    return Q


def spd(K, scale=1.0):
    A = rng.standard_normal((K, K))
    return scale * (A @ A.T / K + 0.5 * np.eye(K))


def frob_curv(W):
    return 0.5 * np.linalg.norm(W - np.eye(W.shape[0])) ** 2


# --------------------------------------------------------------------------------------------
header("1. Class functions are blind to unipotent holonomy; the Frobenius defect is not")
K = 3
N = np.eye(K); N[0, 1] = 1.0
lam = np.linalg.eigvals(N)
print("eigenvalues of I+E12:", lam)
print("sum_k |lambda_k - 1| =", np.sum(np.abs(lam - 1)))
print("rms |Log lambda_k|   =", np.sqrt(np.mean(np.abs(np.log(lam.astype(complex))) ** 2)))
print("Frobenius defect (1/2)||W - I||_F^2 =", frob_curv(N))
for t in (1.0, 1e-2, 1e-4):
    D = np.diag([t] + [1.0] * (K - 1))
    print(f"  conjugate by diag({t},1,1): ||D N D^-1 - I||_F = {np.linalg.norm(D @ N @ np.linalg.inv(D) - np.eye(K)):.1e}")

header("2. On O(K) the Frobenius defect equals the Wilson density K - tr W; small-field expansion")
err = 0.0
for _ in range(200):
    Q = rand_orth(K)
    err = max(err, abs(frob_curv(Q) - (K - np.trace(Q))))
print("max |(1/2)||Q-I||^2 - (K - tr Q)| over 200 orthogonal Q:", f"{err:.1e}")
base = [rng.standard_normal((K, K)) for _ in range(3)]
for s in (1e-1, 1e-2, 1e-3):
    Xik, Xij, Xjk = (s * B for B in base)
    F = expm(-Xik) @ expm(Xij) @ expm(Xjk)
    dX = Xij + Xjk - Xik
    print(f"  s={s:.0e}: Phi(F) = {frob_curv(F):.3e}, (1/2)||dX||^2 = {0.5*np.linalg.norm(dX)**2:.3e}, "
          f"rel diff = {abs(frob_curv(F) - 0.5*np.linalg.norm(dX)**2)/(0.5*np.linalg.norm(dX)**2):.1e}")

# --------------------------------------------------------------------------------------------
header("3. Transport term: E[-log N(z'; m, Q)] - H[q(z')] = KL(q' || N(mbar, Q)) + (1/2) tr(Q^-1 V)")
K, H, d, Nsrc = 4, 2, 2, 3
T = np.eye(K) + 0.3 * rng.standard_normal((K, K))
Tinv = np.linalg.inv(T)
P = []
for h in range(H):
    Dh = np.zeros((K, K)); Dh[h*d:(h+1)*d, h*d:(h+1)*d] = np.eye(d)
    P.append(Tinv @ Dh @ T)
print("sum_h P_h = I:", f"{np.abs(sum(P) - np.eye(K)).max():.1e}",
      "  P_h P_g = delta P_h:", f"{max(np.abs(P[0]@P[1]).max(), np.abs(P[0]@P[0]-P[0]).max()):.1e}")
G = [expm(0.4 * rng.standard_normal((K, K))) for _ in range(Nsrc)]
xi = [rng.standard_normal(K) for _ in range(Nsrc)]
C = [spd(K, 0.5) for _ in range(Nsrc)]
beta = rng.dirichlet(np.ones(Nsrc), size=H)                 # (H, Nsrc) independent head labels
Qn = spd(K, 0.7); A = np.linalg.inv(Qn)
xi_p = rng.standard_normal(K); C_p = spd(K, 0.4)

# Closed-form mean and covariance of m = sum_h G_{J^h} P_h zeta_{J^h}.
mbar = sum(beta[h, j] * G[j] @ P[h] @ xi[j] for h in range(H) for j in range(Nsrc))
V = np.zeros((K, K))
for h in range(H):
    mh = sum(beta[h, j] * G[j] @ P[h] @ xi[j] for j in range(Nsrc))
    for j in range(Nsrc):
        a = G[j] @ P[h] @ xi[j]
        V += beta[h, j] * np.outer(a - mh, a - mh)                       # between-source spread
for h in range(H):
    for g in range(H):
        for j in range(Nsrc):
            c = beta[h, j] if h == g else beta[h, j] * beta[g, j]
            V += c * G[j] @ P[h] @ C[j] @ P[g].T @ G[j].T               # transported source covariance

# Monte Carlo of the joint (labels, sources, receiver).
S = 400_000
labels = np.stack([rng.choice(Nsrc, size=S, p=beta[h]) for h in range(H)])     # (H, S)
Z = np.stack([rng.multivariate_normal(xi[j], C[j], size=S) for j in range(Nsrc)])  # (Nsrc, S, K)
m = np.zeros((S, K))
for h in range(H):
    for j in range(Nsrc):
        sel = labels[h] == j
        m[sel] += (G[j] @ P[h] @ Z[j][sel].T).T
zp = rng.multivariate_normal(xi_p, C_p, size=S)
r = zp - m
mc = 0.5 * np.einsum("si,ij,sj->s", r, A, r).mean() + 0.5 * np.linalg.slogdet(2*np.pi*Qn)[1] \
     - 0.5 * np.linalg.slogdet(2*np.pi*np.e*C_p)[1]
KL = 0.5 * (np.trace(A @ C_p) + (xi_p - mbar) @ A @ (xi_p - mbar) - K
            + np.linalg.slogdet(Qn)[1] - np.linalg.slogdet(C_p)[1])
closed = KL + 0.5 * np.trace(A @ V)
print(f"Monte Carlo {mc:.4f}   closed form {closed:.4f}   rel diff {abs(mc-closed)/abs(closed):.1e} (S={S})")
print("mean of m: MC vs closed", f"{np.abs(m.mean(0) - mbar).max():.1e}",
      "  cov of m: MC vs closed", f"{np.abs(np.cov(m.T) - V).max():.1e}")

header("4. One head: transport term = sum_j beta_j [KL(q'||N(G_j xi_j, Q)) + (1/2) tr(Q^-1 G_j C_j G_j^T)]")
b = rng.dirichlet(np.ones(Nsrc))
mb = sum(b[j] * G[j] @ xi[j] for j in range(Nsrc))
V1 = sum(b[j] * (G[j] @ C[j] @ G[j].T + np.outer(G[j] @ xi[j] - mb, G[j] @ xi[j] - mb)) for j in range(Nsrc))


def KLg(m1, S1, m2, S2):
    S2i = np.linalg.inv(S2)
    return 0.5 * (np.trace(S2i @ S1) + (m1 - m2) @ S2i @ (m1 - m2) - len(m1)
                  + np.linalg.slogdet(S2)[1] - np.linalg.slogdet(S1)[1])


lhs = KLg(xi_p, C_p, mb, Qn) + 0.5 * np.trace(A @ V1)
rhs = sum(b[j] * (KLg(xi_p, C_p, G[j] @ xi[j], Qn) + 0.5 * np.trace(A @ G[j] @ C[j] @ G[j].T)) for j in range(Nsrc))
print(f"lhs {lhs:.12f}  rhs {rhs:.12f}  diff {abs(lhs-rhs):.1e}")

# --------------------------------------------------------------------------------------------
header("5. Link gradient: dF/dX = L(X^T, dF/dG) with dF/dG = beta A (G S_j - xi' xi_j^T)")
K = 3
X = 0.5 * rng.standard_normal((K, K))
xj = rng.standard_normal(K); Cj = spd(K, 0.5); Sj = Cj + np.outer(xj, xj)
xr = rng.standard_normal(K); A3 = np.linalg.inv(spd(K, 0.8)); bij = 0.37


def edge_energy(Xm):
    Gm = expm(Xm)
    e = xr - Gm @ xj
    return bij * (0.5 * e @ A3 @ e + 0.5 * np.trace(A3 @ Gm @ Cj @ Gm.T))


Gx = expm(X)
dFdG = bij * A3 @ (Gx @ Sj - np.outer(xr, xj))
grad = expm_frechet(X.T, dFdG, compute_expm=False)
fd = np.zeros_like(X); h = 1e-6
for a in range(K):
    for c in range(K):
        Ep = np.zeros_like(X); Ep[a, c] = h
        fd[a, c] = (edge_energy(X + Ep) - edge_energy(X - Ep)) / (2 * h)
print("max |analytic - central FD| =", f"{np.abs(grad - fd).max():.1e}", " (|grad| ~", f"{np.abs(grad).max():.2f})")
G_star = np.outer(xr, xj) @ np.linalg.inv(Sj)
print("unregularized stationary G = xi' xi_j^T S_j^{-1} has rank", np.linalg.matrix_rank(G_star),
      "and det", f"{np.linalg.det(G_star):.1e}", "(not in the image of exp)")

# --------------------------------------------------------------------------------------------
header("6. Linearized field equation: screened discrete Maxwell (Proca) operator vs exact MAP")
# One transition (layer l -> l+1), N tokens, H = 1, cross-token edges j < i, trivial temporal links,
# so the elementary loops are the triangles F_ijk = G_ik^{-1} G_ij G_jk, k < j < i. Every receiver i
# has one mean xi'_i = u + eps r_i; every source has mean u and covariance eps C_j, so the whole
# source term beta A[(xi'_i - xi_j) xi_j^T - C_j] is O(eps) and the MAP links are O(eps).
K, Ntok = 2, 4
edges = [(i, j) for i in range(Ntok) for j in range(i)]
idx = {e: n for n, e in enumerate(edges)}
tris = [(i, j, k) for i in range(Ntok) for j in range(i) for k in range(j)]
pi = {e: 1.0 / e[0] for e in edges}                                 # uniform causal prior over j < i
w = {t: pi[(t[0], t[1])] * pi[(t[1], t[2])] for t in tris}
sigma2, lam_c, qn = 0.5, 0.8, 0.6
A_n = np.eye(K) / qn
u = rng.standard_normal(K)
r_recv = {i: rng.standard_normal(K) for i in range(Ntok)}
C_base = [spd(K, 0.3) for _ in range(Ntok)]
n = len(edges) * K * K


def unpack(v):
    return {e: v[idx[e]*K*K:(idx[e]+1)*K*K].reshape(K, K) for e in edges}


def setup(eps):
    xr = {i: u + eps * r_recv[i] for i in range(Ntok)}
    Cs = [eps * c for c in C_base]
    Ss = [Cs[j] + np.outer(u, u) for j in range(Ntok)]
    return xr, Cs, Ss


def free_energy(v, eps):
    xr, Cs, _ = setup(eps)
    Xd = unpack(v)
    total = 0.0
    for (i, j) in edges:
        Gm = expm(Xd[(i, j)])
        e = xr[i] - Gm @ u
        total += pi[(i, j)] * (0.5 * e @ A_n @ e + 0.5 * np.trace(A_n @ Gm @ Cs[j] @ Gm.T))
        total += 0.5 / sigma2 * np.sum(Xd[(i, j)] ** 2)
    for (i, j, k) in tris:
        F = expm(-Xd[(i, k)]) @ expm(Xd[(i, j)]) @ expm(Xd[(j, k)])
        total += lam_c * w[(i, j, k)] * frob_curv(F)
    return total


def linear_operator(Ss):
    def apply(v):
        Xd = unpack(v)
        out = {e: Xd[e] / sigma2 + pi[e] * A_n @ Xd[e] @ Ss[e[1]] for e in edges}
        for (i, j, k) in tris:
            dX = Xd[(i, j)] + Xd[(j, k)] - Xd[(i, k)]
            out[(i, j)] = out[(i, j)] + lam_c * w[(i, j, k)] * dX
            out[(j, k)] = out[(j, k)] + lam_c * w[(i, j, k)] * dX
            out[(i, k)] = out[(i, k)] - lam_c * w[(i, j, k)] * dX
        return np.concatenate([out[e].ravel() for e in edges])
    return np.stack([apply(col) for col in np.eye(n)], axis=1)


for eps in (1e-1, 3e-2, 1e-2):
    xr, Cs, Ss = setup(eps)
    Lmat = linear_operator(Ss)
    rhs = np.concatenate([(pi[e] * A_n @ (np.outer(xr[e[0]] - u, u) - Cs[e[1]])).ravel() for e in edges])
    x_lin = np.linalg.solve(Lmat, rhs)
    res = minimize(free_energy, np.zeros(n), args=(eps,), method="BFGS",
                   options={"gtol": 1e-12, "maxiter": 10000})
    rel = np.linalg.norm(res.x - x_lin) / np.linalg.norm(res.x)
    if eps == 1e-1:
        print("linear operator symmetric:", f"{np.abs(Lmat - Lmat.T).max():.1e}",
              " min eigenvalue:", f"{np.linalg.eigvalsh(0.5*(Lmat+Lmat.T)).min():.3f}",
              f"(>= 1/sigma^2 = {1/sigma2})")
    print(f"  eps={eps:.0e}: |X_map| = {np.linalg.norm(res.x):.2e}, |X_map - X_lin|/|X_map| = {rel:.2e}")

# --------------------------------------------------------------------------------------------
header("7. Electric (time-like) loop: W ~ I - [(X^{l+1}_ik - X^l_ik) - (X^{l+1}_ii - X^l_kk)]")
K = 3
base = [rng.standard_normal((K, K)) for _ in range(4)]
for s in (1e-1, 1e-2, 1e-3):
    Xl_ik, Xl1_ik, Xl1_ii, Xl_kk = (s * B for B in base)
    W = np.linalg.inv(expm(Xl1_ik) @ expm(Xl_kk)) @ expm(Xl1_ii) @ expm(Xl_ik)
    E = (Xl1_ik - Xl_ik) - (Xl1_ii - Xl_kk)
    print(f"  s={s:.0e}: ||W - (I - E)||_F / ||E||_F = {np.linalg.norm(W - np.eye(K) + E)/np.linalg.norm(E):.1e}")

# --------------------------------------------------------------------------------------------
header("8. Undirected Gaussian matter: induced action (1/2) log det J(X) and the hopping expansion")
K = 2
lam0, lamE = 3.0, 1.0                                    # site and edge precisions (isotropic)
tri_edges = [(1, 0), (2, 1), (2, 0)]                       # (receiver i, source j): G_10, G_21, G_20


def J_matrix(Gd, n_nodes=3):
    J = np.zeros((n_nodes*K, n_nodes*K))
    for v in range(n_nodes):
        J[v*K:(v+1)*K, v*K:(v+1)*K] += lam0 * np.eye(K)
    for (i, j) in Gd:
        Gm = Gd[(i, j)]
        Bi, Bj = slice(i*K, (i+1)*K), slice(j*K, (j+1)*K)
        J[Bi, Bi] += lamE * np.eye(K)
        J[Bj, Bj] += lamE * Gm.T @ Gm
        J[Bi, Bj] += -lamE * Gm
        J[Bj, Bi] += -lamE * Gm.T
    return J


def S_ind(Gd, n_nodes=3):
    return 0.5 * np.linalg.slogdet(J_matrix(Gd, n_nodes))[1]


# (a) orthogonal links: invariance under orthogonal reference gauge h_v and dependence on F only.
Gd = {e: rand_orth(K) for e in tri_edges}
h = [rand_orth(K) for _ in range(3)]
Gd_g = {(i, j): h[i] @ Gd[(i, j)] @ h[j].T for (i, j) in tri_edges}
F = Gd[(2, 0)].T @ Gd[(2, 1)] @ Gd[(1, 0)]                 # G_20^{-1} G_21 G_10 (orthogonal)
print("S_ind gauge-transformed - S_ind:", f"{abs(S_ind(Gd_g) - S_ind(Gd)):.1e}")
# (b) leading Wilson term: for orthogonal links D = (lam0 + deg*lamE) I, coupling c = lamE^3/d^3.
deg = 2
dd = lam0 + deg * lamE
c = lamE ** 3 / dd ** 3
flat = {e: np.eye(K) for e in tri_edges}
for th in (0.3, 1.0, 2.0):
    R = np.array([[np.cos(th), -np.sin(th)], [np.sin(th), np.cos(th)]])
    Gd_t = {(1, 0): np.eye(K), (2, 1): R, (2, 0): np.eye(K)}      # holonomy F = R
    exact = S_ind(Gd_t) - S_ind(flat)
    wilson = c * (K - np.trace(R))
    # full hopping series
    Jm = J_matrix(Gd_t); Dm = np.diag(np.diag(Jm)); Am = Dm - Jm
    M = np.linalg.solve(Dm, Am)
    series = 0.5 * np.linalg.slogdet(Dm)[1] - 0.5 * sum(np.trace(np.linalg.matrix_power(M, k)) / k for k in range(1, 200))
    print(f"  theta={th}: exact dS_ind = {exact:.6f}, leading Wilson c(K - tr F) = {wilson:.6f}, "
          f"hopping series vs exact S_ind: {abs(series - S_ind(Gd_t)):.1e}, rho(D^-1 A) = {max(abs(np.linalg.eigvals(M))):.3f}")
# Heavier matter (larger site precision) makes the leading term exact: ratio -> 1.
R1 = np.array([[np.cos(1.0), -np.sin(1.0)], [np.sin(1.0), np.cos(1.0)]])
for lam0_try in (3.0, 10.0, 30.0, 100.0):
    lam0_saved, lam0 = lam0, lam0_try
    d_try = lam0 + deg * lamE
    exact = S_ind({(1, 0): np.eye(K), (2, 1): R1, (2, 0): np.eye(K)}) - S_ind(flat)
    print(f"  lam0={lam0_try:>5}: exact / leading Wilson = {exact / ((lamE/d_try)**3 * (K - np.trace(R1))):.4f}")
    lam0 = lam0_saved
# (c) tree (single edge): orthogonal link has no induced action, a symmetric (non-compact) one does.
single = lambda Gm: S_ind({(1, 0): Gm}, n_nodes=2)
Hs = np.array([[0.7, 0.2], [0.2, -0.1]])
print("single edge: S_ind(orthogonal) - S_ind(I) =", f"{single(rand_orth(K)) - single(np.eye(K)):.1e}",
      "  S_ind(e^{sH_sym}) - S_ind(I) =", f"{single(expm(Hs)) - single(np.eye(K)):.4f}")
# (d) unipotent holonomy on the triangle is seen by S_ind (non-orthogonal link).
U = np.array([[1.0, 0.8], [0.0, 1.0]])
print("triangle with unipotent link: S_ind - S_ind(flat) =", f"{S_ind({(1,0): np.eye(K), (2,1): U, (2,0): np.eye(K)}) - S_ind(flat):.4f}",
      " (class-function curvature of its holonomy:", f"{np.sum(np.abs(np.linalg.eigvals(U) - 1)):.1e})")
# (e) bounded below: J >= lam0 I.
worst = min(S_ind({e: expm(2.0 * rng.standard_normal((K, K))) for e in tri_edges}) for _ in range(500))
print("min S_ind over 500 random large GL links:", f"{worst:.4f}", ">= (1/2) log det(lam0 I) =",
      f"{0.5 * 3 * K * np.log(lam0):.4f}")

# --------------------------------------------------------------------------------------------
header("9. Depth path MAP: increment precision is the inertial mass, Euclidean (inverted-potential) sign")
# Scalar path x_0..x_L with fixed ends, energy sum (m/2)(x_{l+1}-x_l)^2 + V(x_l), V = (x^2-1)^2/4.
Lp, mass = 40, 25.0
V = lambda x: 0.25 * (x ** 2 - 1) ** 2
dV = lambda x: x * (x ** 2 - 1)


def path_energy(inner):
    x = np.concatenate([[-1.0], inner, [1.0]])
    return 0.5 * mass * np.sum(np.diff(x) ** 2) + np.sum(V(x[1:-1]))


res = minimize(path_energy, np.linspace(-1, 1, Lp + 1)[1:-1], method="BFGS", options={"gtol": 1e-12})
x = np.concatenate([[-1.0], res.x, [1.0]])
el = mass * (2 * x[1:-1] - x[2:] - x[:-2]) + dV(x[1:-1])
print("max |m(2x_l - x_{l+1} - x_{l-1}) + V'(x_l)| at the MAP path:", f"{np.abs(el).max():.1e}")
print("MAP path is a monotone kink between the wells (no oscillation):", bool(np.all(np.diff(x) > 0)))

# --------------------------------------------------------------------------------------------
header("10. Static limit: shared generator recovers the exponential-chart message e^{OT} T^-1 B T xi")
K, H, d = 4, 2, 2
O = 0.4 * rng.standard_normal((K, K)); Tm = np.eye(K) + 0.3 * rng.standard_normal((K, K))
Xbar = O @ Tm
Ps = []
for hh in range(H):
    Dh = np.zeros((K, K)); Dh[hh*d:(hh+1)*d, hh*d:(hh+1)*d] = np.eye(d)
    Ps.append(np.linalg.inv(Tm) @ Dh @ Tm)
bet = rng.dirichlet(np.ones(3), size=H)
xis = [rng.standard_normal(K) for _ in range(3)]
model = sum(bet[hh, j] * expm(Xbar) @ Ps[hh] @ xis[j] for hh in range(H) for j in range(3))
Oprime = expm(O @ Tm) @ np.linalg.inv(Tm)
chart = sum(Oprime @ np.kron(np.diag(bet[:, j]), np.eye(d)) @ Tm @ xis[j] for j in range(3))
print("max |model mean - exponential-chart mean| =", f"{np.abs(model - chart).max():.1e}")
