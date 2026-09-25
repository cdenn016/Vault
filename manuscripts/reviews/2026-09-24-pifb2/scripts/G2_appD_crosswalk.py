"""G2 crosswalk: PIFB2 Appendix D covariance fixed point versus Theory g03/g04 block optimum.

(1) For frozen neighbors, the receiver functional
      F_i(S) = KL(N(mu,S)||p_i) + sum_j b_ij KL(N(mu,S)||N(Om mu_j, Om S_j Om^T))  (+ obs term)
    has entropy weight (1+B_i) on -1/2 log det S, and its minimizer is S = (1+B_i) M_i^{-1},
    M_i = Sp^{-1} + sum_j b_ij (Om S_j Om^T)^{-1} + Lam_o. With B_i = 1 this is
    eq:sigma_fixed_point_beta.  Checked by numerical minimization over Cholesky factors.
(2) Theory: for a normalized Gaussian joint in the interaction family (g03 def:gauss-interaction-family),
    the block-diagonal (mean-field) optimum is S_b = (Lambda_bb)^{-1} (g04 thm:restrict-exact-block-optimum),
    independent of every other block's covariance: no fixed-point problem. Checked by direct
    minimization of KL(Q||P) over block-diagonal Gaussian Q (N=3, K=2).
(3) Homogeneous illustration: PIFB2 gives Sigma_inf = Sigma_0 (prior reproduced); a normalized joint
    with fixed coupling W = Sigma_0^{-1} per edge gives precision addition instead.
"""
import numpy as np
from scipy.optimize import minimize

rng = np.random.default_rng(3)
K = 2

def spd(scale=1.0):
    M = rng.normal(size=(K, K))
    return scale * (M @ M.T) + 0.5 * np.eye(K)

def kl(m0, S0, m1, S1):
    S1i = np.linalg.inv(S1)
    d = m1 - m0
    return 0.5 * (np.trace(S1i @ S0) + d @ S1i @ d - K + np.log(np.linalg.det(S1) / np.linalg.det(S0)))

def chol_to_S(v):
    L = np.array([[np.exp(v[0]), 0.0], [v[1], np.exp(v[2])]])
    return L @ L.T

# ---------------- (1) composite receiver functional ----------------
print("(1) PIFB2 receiver functional: minimizer (1+B) M^{-1}")
mu = rng.normal(size=K)
Sp = spd(); mp = rng.normal(size=K)
Lo = spd(0.3)
b = np.array([0.3, 0.45, 0.25])  # B = 1
Om = [np.eye(K) + 0.4 * rng.normal(size=(K, K)) for _ in b]
Sj = [spd() for _ in b]; mj = [rng.normal(size=K) for _ in b]
for B_scale in (1.0, 2.5):
    bb = b * B_scale
    B = bb.sum()
    def F(v):
        S = chol_to_S(v)
        val = kl(mu, S, mp, Sp) + 0.5 * np.trace(Lo @ S)
        for j in range(len(bb)):
            val += bb[j] * kl(mu, S, Om[j] @ mj[j], Om[j] @ Sj[j] @ Om[j].T)
        return val
    res = minimize(F, np.zeros(3), method="BFGS", options={"gtol": 1e-11})
    S_num = chol_to_S(res.x)
    M = np.linalg.inv(Sp) + Lo + sum(bb[j] * np.linalg.inv(Om[j] @ Sj[j] @ Om[j].T) for j in range(len(bb)))
    S_formula = (1 + B) * np.linalg.inv(M)
    print(f"   B={B:.2f}: max|S_num - (1+B)M^-1| = {np.abs(S_num - S_formula).max():.2e}")

# ---------------- (2) Theory block optimum ----------------
print("(2) normalized interaction-family joint: mean-field optimum = Lambda_bb^{-1}")
N = 3
A = [spd() for _ in range(N)]
W = {(0, 1): spd(0.5), (0, 2): spd(0.5), (1, 2): spd(0.5)}
Lam = np.zeros((N * K, N * K))
for i in range(N):
    Lam[i*K:(i+1)*K, i*K:(i+1)*K] += A[i]
for (i, j), Wij in W.items():
    Lam[i*K:(i+1)*K, i*K:(i+1)*K] += Wij
    Lam[j*K:(j+1)*K, j*K:(j+1)*K] += Wij
    Lam[i*K:(i+1)*K, j*K:(j+1)*K] -= Wij
    Lam[j*K:(j+1)*K, i*K:(i+1)*K] -= Wij
h = rng.normal(size=N * K)
mu_P = np.linalg.solve(Lam, h)
def KLQP(v):
    m = v[:N*K]
    Sq = np.zeros((N*K, N*K))
    for i in range(N):
        Sq[i*K:(i+1)*K, i*K:(i+1)*K] = chol_to_S(v[N*K+3*i:N*K+3*i+3])
    return 0.5 * (np.trace(Lam @ Sq) + (m - mu_P) @ Lam @ (m - mu_P) - N*K
                  - np.log(np.linalg.det(Lam)) - np.log(np.linalg.det(Sq)))
res = minimize(KLQP, np.zeros(N*K + 3*N), method="BFGS", options={"gtol": 1e-11, "maxiter": 5000})
worst = 0.0
for i in range(N):
    S_i = chol_to_S(res.x[N*K+3*i:N*K+3*i+3])
    worst = max(worst, np.abs(S_i - np.linalg.inv(Lam[i*K:(i+1)*K, i*K:(i+1)*K])).max())
print(f"   max|S_i - Lambda_ii^-1| = {worst:.2e};  mean error {np.abs(res.x[:N*K]-mu_P).max():.2e}")
print("   Lambda_ii = A_i + sum_j W_ij contains no neighbor covariance: one-step optimum")

# ---------------- (3) homogeneous illustration ----------------
print("(3) homogeneous, observation-free, identity transport")
S0 = spd()
# PIFB2 fixed point, B=1, one neighbor identical: Sigma^-1 = 1/2 (S0^-1 + Sigma^-1)
S = S0.copy() * 3
for _ in range(200):
    S = 2 * np.linalg.inv(np.linalg.inv(S0) + np.linalg.inv(S))
print(f"   PIFB2 iteration -> max|Sigma - Sigma0| = {np.abs(S - S0).max():.2e}")
# normalized joint: two agents, prior precision S0^-1 each, edge weight W = S0^-1
Lam2 = np.block([[2*np.linalg.inv(S0), -np.linalg.inv(S0)], [-np.linalg.inv(S0), 2*np.linalg.inv(S0)]])
print(f"   normalized joint mean-field covariance = Sigma0/2: max dev {np.abs(np.linalg.inv(Lam2[:K,:K]) - S0/2).max():.2e}")

# ---------------- (4) Appendix E versus Theory g05 prop:ig-fixed-covariance-kl ----------------
print("(4) fixed-W expected quadratic form = common-covariance KL + trace term (Monte Carlo)")
Wf = spd(); Om1 = np.eye(K) + 0.3 * rng.normal(size=(K, K))
mi, mj = rng.normal(size=K), rng.normal(size=K); Si, Sj = spd(), spd()
n = 400000
ki = rng.multivariate_normal(mi, Si, size=n); kj = rng.multivariate_normal(mj, Sj, size=n)
d = ki - kj @ Om1.T
mc = 0.5 * np.einsum('ni,ij,nj->n', d, Wf, d).mean()
Winv = np.linalg.inv(Wf)
closed = kl(mi, Winv, Om1 @ mj, Winv) + 0.5 * np.trace(Wf @ (Si + Om1 @ Sj @ Om1.T))
print(f"   MC {mc:.5f} vs closed {closed:.5f}; rel {abs(mc-closed)/closed:.1e}")
