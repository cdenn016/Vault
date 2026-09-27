"""Framing checks for L1/L2 (Kretschmann/dressing) on a tiny numpy model of Algorithm 1.

Reported stack (Main Alg. 1): xi=U^{-1}mu, C=U^{-1}Sigma U^{-T}; Gaussian-KL routing with causal ALiBi;
m=U sum_h O_h sum_j beta T_h xi_j; mu_att=mu+m; u=LN(mu_att); mu_next=u+W2 GELU(W1 u+b1)+b2; Sigma_next=Sigma;
z=W_out mu^(L)+b_out.  Frames U_i=expm(X_{x_i}) expm(Y_i) (block diagonal).
"""
import numpy as np
from scipy.linalg import expm, block_diag
rng = np.random.default_rng(20260923)
N, K, H, r, s, L, Vv = 6, 4, 2, 2, 2, 2, 5
blocks = [2, 2]
tau = np.sqrt(r)

def blockdiag_rand(scale):
    return block_diag(*[scale * rng.standard_normal((d, d)) for d in blocks])

tokens = rng.integers(0, Vv, N)
Xtok = [blockdiag_rand(0.4) for _ in range(Vv)]
Ypos = [blockdiag_rand(0.3) for _ in range(N)]
mu_p = rng.standard_normal((Vv, K))
sig_p = np.exp(0.3 * rng.standard_normal((Vv, K)))
SQ = [rng.standard_normal((r, K)) for _ in range(H)]
SK = [rng.standard_normal((r, K)) for _ in range(H)]
T = [rng.standard_normal((s, K)) for _ in range(H)]
O = [rng.standard_normal((K, s)) for _ in range(H)]
W1, b1 = rng.standard_normal((3 * K, K)), rng.standard_normal(3 * K)
W2, b2 = rng.standard_normal((K, 3 * K)) / 3, rng.standard_normal(K)
gam, bet = 1 + 0.1 * rng.standard_normal(K), 0.1 * rng.standard_normal(K)
Wout, bout = rng.standard_normal((Vv, K)), rng.standard_normal(Vv)
slopes = [2.0 ** -(h + 1) for h in range(H)]

def gelu(x): return 0.5 * x * (1 + np.tanh(np.sqrt(2 / np.pi) * (x + 0.044715 * x ** 3)))
def LN(x):
    c = x - x.mean(); return gam * c / np.sqrt((c ** 2).mean() + 1e-5) + bet
def G(x):
    u = LN(x); return u + W2 @ gelu(W1 @ u + b1) + b2

def kl(m1, S1, m2, S2):
    P = np.linalg.inv(S2); d = m2 - m1; k = len(m1)
    return 0.5 * (np.trace(P @ S1) + d @ P @ d - k + np.linalg.slogdet(S2)[1] - np.linalg.slogdet(S1)[1])

def route_gauss(xi, C, h):
    beta = np.zeros((N, N))
    for i in range(N):
        lg = np.full(N, -np.inf)
        for j in range(i + 1):
            D = kl(SQ[h] @ xi[i], SQ[h] @ C[i] @ SQ[h].T, SK[h] @ xi[j], SK[h] @ C[j] @ SK[h].T)
            lg[j] = -slopes[h] * (i - j) - D / tau
        e = np.exp(lg - lg.max()); beta[i] = e / e.sum()
    return beta

def route_dot(xi, C, h):
    beta = np.zeros((N, N))
    for i in range(N):
        lg = np.full(N, -np.inf)
        for j in range(i + 1):
            lg[j] = -slopes[h] * (i - j) + (SQ[h] @ xi[i]) @ (SK[h] @ xi[j]) / tau
        e = np.exp(lg - lg.max()); beta[i] = e / e.sum()
    return beta

def attention(mu, Sig, U, router=route_gauss):
    Ui = [np.linalg.inv(u) for u in U]
    xi = [Ui[i] @ mu[i] for i in range(N)]
    C = [Ui[i] @ Sig[i] @ Ui[i].T for i in range(N)]
    betas = [router(xi, C, h) for h in range(H)]
    m = []
    for i in range(N):
        acc = np.zeros(K)
        for h in range(H):
            acc += O[h] @ sum(betas[h][i, j] * (T[h] @ xi[j]) for j in range(i + 1))
        m.append(U[i] @ acc)
    return m, betas

def stack(mu0, Sig0, U, dressed=False, router=route_gauss):
    mu = [x.copy() for x in mu0]
    for _ in range(L):
        m, _ = attention(mu, Sig0, U, router)
        att = [mu[i] + m[i] for i in range(N)]
        if dressed:
            mu = [U[i] @ G(np.linalg.solve(U[i], att[i])) for i in range(N)]
        else:
            mu = [G(att[i]) for i in range(N)]
    if dressed:
        return np.array([Wout @ np.linalg.solve(U[i], mu[i]) + bout for i in range(N)])
    return np.array([Wout @ mu[i] + bout for i in range(N)])

U = [expm(Xtok[tokens[i]]) @ expm(Ypos[i]) for i in range(N)]
mu0 = [mu_p[tokens[i]] for i in range(N)]
Sig0 = [np.diag(sig_p[tokens[i]]) for i in range(N)]
g = [blockdiag_rand(0.6) + np.eye(K) for _ in range(N)]
mu0g = [g[i] @ mu0[i] for i in range(N)]
Sig0g = [g[i] @ Sig0[i] @ g[i].T for i in range(N)]
Ug = [g[i] @ U[i] for i in range(N)]

out = {}
for name, router in [("gaussKL", route_gauss), ("dotprod", route_dot)]:
    m, b = attention(mu0, Sig0, U, router); mg, bg = attention(mu0g, Sig0g, Ug, router)
    out["passive_cov_" + name + "_beta"] = max(np.abs(b[h] - bg[h]).max() for h in range(H))
    out["passive_cov_" + name + "_msg"] = max(np.abs(g[i] @ m[i] - mg[i]).max() for i in range(N))
F = lambda x: np.tanh(W1[:K] @ x) * x
mF = [U[i] @ F(np.linalg.solve(U[i], mu0[i])) for i in range(N)]
mFg = [Ug[i] @ F(np.linalg.solve(Ug[i], mu0g[i])) for i in range(N)]
out["passive_cov_arbitrary_nonlinear_F"] = max(np.abs(g[i] @ mF[i] - mFg[i]).max() for i in range(N))
z, zg = stack(mu0, Sig0, U), stack(mu0g, Sig0g, Ug)
out["reported_stack_logit_change_under_passive"] = np.abs(z - zg).max()
zd, zdg = stack(mu0, Sig0, U, dressed=True), stack(mu0g, Sig0g, Ug, dressed=True)
out["dressed_stack_logit_change_under_passive"] = np.abs(zd - zdg).max()
Ui = [np.linalg.inv(u) for u in U]
xi0 = [Ui[i] @ mu0[i] for i in range(N)]; C0 = [Ui[i] @ Sig0[i] @ Ui[i].T for i in range(N)]
I = [np.eye(K)] * N
zref = stack(xi0, C0, I, dressed=False)
out["dressed_minus_frame_free_reference_stack"] = np.abs(zd - zref).max()
a = blockdiag_rand(0.5) + np.eye(K); ai = np.linalg.inv(a)
SQ0, SK0, T0, O0 = [x.copy() for x in SQ], [x.copy() for x in SK], [x.copy() for x in T], [x.copy() for x in O]
SQ[:] = [x @ a for x in SQ0]; SK[:] = [x @ a for x in SK0]; T[:] = [x @ a for x in T0]; O[:] = [ai @ x for x in O0]
za = stack(mu0, Sig0, [u @ a for u in U])
out["reported_stack_global_rebasing_redundancy"] = np.abs(z - za).max()
SQ[:], SK[:], T[:], O[:] = SQ0, SK0, T0, O0
hloc = [blockdiag_rand(0.5) + np.eye(K) for _ in range(N)]
zh = stack(mu0, Sig0, [U[i] @ hloc[i] for i in range(N)])
out["reported_stack_local_right_action_change"] = np.abs(z - zh).max()
A = rng.standard_normal((r, r)) + 2 * np.eye(r)
m0, b0 = attention(mu0, Sig0, U, route_gauss)
m0d, b0d = attention(mu0, Sig0, U, route_dot)
SQ[:] = [A @ x for x in SQ0]; SK[:] = [A @ x for x in SK0]
m1, b1g = attention(mu0, Sig0, U, route_gauss); m1d, b1d = attention(mu0, Sig0, U, route_dot)
SQ[:] = [A @ x for x in SQ0]; SK[:] = [np.linalg.inv(A).T @ x for x in SK0]
m2d, b2d = attention(mu0, Sig0, U, route_dot)
m2g, b2g = attention(mu0, Sig0, U, route_gauss)
SQ[:], SK[:] = SQ0, SK0
out["gauss_routing_cogredient_A_change"] = max(np.abs(b0[h] - b1g[h]).max() for h in range(H))
out["gauss_routing_contragredient_A_change"] = max(np.abs(b0[h] - b2g[h]).max() for h in range(H))
out["dot_routing_cogredient_A_change"] = max(np.abs(b0d[h] - b1d[h]).max() for h in range(H))
out["dot_routing_contragredient_A_change"] = max(np.abs(b0d[h] - b2d[h]).max() for h in range(H))
for k, v in out.items():
    print(f"{k:48s} {v:.3e}")
