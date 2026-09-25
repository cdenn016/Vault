"""G2 crosswalk checks for PIFB2 Appendix F (thm:representation_app) against Theory c05/c06/g04.

(1) Exact identity behind the geometric-mean target:
    KL(q||p) + sum_j b_j KL(q||r_j) = (1+B) KL(q||g) - (1+B) log Z_g,
    g = Z_g^{-1} p^{1/(1+B)} prod_j r_j^{b_j/(1+B)}.
    The exponents 1/(1+B) are the reciprocal of the entropy weight (1+B) of the composite
    functional. Checked in 1D by quadrature for random Gaussians and a non-optimal q.
(2) Normalized pairwise Gaussian joint (Theory g03 interaction family, g04
    thm:restrict-exact-block-optimum, c05 prop:elbo-exact-e-coordinate): the mean-field
    coordinate update is a product of experts with unit exponents (precision addition), and at
    the CAVI fixed point the gradient of the joint ELBO vanishes in every coordinate, so the
    "sender" appearance of each agent is included automatically. Contrast with the PIFB2
    geometric pool (exponents 1/2 for B=1) at the same data (L03-1's two-agent numbers).
(3) Units map between PIFB2 eq:rg_reduced_hessian (energy units) and Theory
    prop:obs-attention-reduced-hessian (dimensionless R_i): tau * Hess R_i equals the PIFB2 form.
"""
import numpy as np
from scipy import integrate

rng = np.random.default_rng(7)

def npdf(x, m, v):
    return np.exp(-0.5 * (x - m) ** 2 / v) / np.sqrt(2 * np.pi * v)

def kl_quad(fq, fp, lo=-30, hi=30):
    val, _ = integrate.quad(lambda x: fq(x) * (np.log(fq(x) + 1e-300) - np.log(fp(x) + 1e-300)), lo, hi, limit=400)
    return val

# ---------------- (1) KL-sum identity ----------------
print("(1) KL-sum / geometric-pool identity")
worst = 0.0
for trial in range(5):
    mp, vp = rng.normal(), rng.uniform(0.3, 2.0)
    J = 3
    mr = rng.normal(size=J) * 2
    vr = rng.uniform(0.3, 2.0, size=J)
    b = rng.uniform(0.1, 1.0, size=J)
    B = b.sum()
    mq, vq = rng.normal(), rng.uniform(0.3, 2.0)  # arbitrary, not optimal
    fq = lambda x: npdf(x, mq, vq)
    fp = lambda x: npdf(x, mp, vp)
    # unnormalized geometric pool
    def graw(x):
        out = npdf(x, mp, vp) ** (1 / (1 + B))
        for j in range(J):
            out = out * npdf(x, mr[j], vr[j]) ** (b[j] / (1 + B))
        return out
    Zg, _ = integrate.quad(graw, -40, 40, limit=400)
    fg = lambda x: graw(x) / Zg
    lhs = kl_quad(fq, fp) + sum(b[j] * kl_quad(fq, lambda x, j=j: npdf(x, mr[j], vr[j])) for j in range(J))
    rhs = (1 + B) * kl_quad(fq, fg) - (1 + B) * np.log(Zg)
    worst = max(worst, abs(lhs - rhs))
    # the pool is Gaussian with precision = weighted average of precisions
    prec_pool = (1 / vp + sum(b[j] / vr[j] for j in range(J))) / (1 + B)
    mean_pool = (mp / vp + sum(b[j] * mr[j] / vr[j] for j in range(J))) / (1 + B) / prec_pool
    m_num, _ = integrate.quad(lambda x: x * fg(x), -40, 40, limit=400)
    v_num, _ = integrate.quad(lambda x: (x - m_num) ** 2 * fg(x), -40, 40, limit=400)
    if trial == 0:
        print(f"   pool mean {m_num:.10f} vs closed form {mean_pool:.10f}; var {v_num:.10f} vs {1/prec_pool:.10f}")
print(f"   max |LHS-RHS| over 5 draws = {worst:.3e}")

# ---------------- (2) normalized pairwise joint, mean field ----------------
print("(2) normalized pairwise Gaussian joint vs PIFB2 geometric pool (L03-1 data)")
# prior factors p1=N(0,1), p2=N(3,0.25); pair factor exp(-w/2 (k1-k2)^2)
w = 1.0
A = np.array([1.0, 4.0]); h = np.array([0.0, 12.0])
Lam = np.array([[A[0] + w, -w], [-w, A[1] + w]])
mu_exact = np.linalg.solve(Lam, h)
# CAVI
m = np.zeros(2)
for it in range(200):
    m[0] = (h[0] + w * m[1]) / Lam[0, 0]
    m[1] = (h[1] + w * m[0]) / Lam[1, 1]
s = 1 / np.diag(Lam)
print(f"   CAVI means {m} exact posterior mean {mu_exact}, diff {np.abs(m-mu_exact).max():.2e}")
print(f"   CAVI variances {s} = 1/(A_i + w): unit exponents on prior and pair factor")

def neg_elbo(theta):
    m1, m2, ls1, ls2 = theta
    s1, s2 = np.exp(ls1), np.exp(ls2)
    E = 0.5 * A[0] * (m1**2 + s1) + 0.5 * A[1] * ((m2 - 3) ** 2 + s2) + 0.5 * w * ((m1 - m2) ** 2 + s1 + s2)
    H = 0.5 * np.log(2 * np.pi * np.e * s1) + 0.5 * np.log(2 * np.pi * np.e * s2)
    return E - H

th = np.array([m[0], m[1], np.log(s[0]), np.log(s[1])])
g = np.array([(neg_elbo(th + 1e-6 * e) - neg_elbo(th - 1e-6 * e)) / 2e-6 for e in np.eye(4)])
print(f"   joint negative-ELBO gradient at CAVI fixed point: {g} (norm {np.linalg.norm(g):.2e})")
# PIFB2 geometric pool (B=1) fixed point from L03-1: q1=N(2,0.5), q2=N(2.667,0.333)
th_pool = np.array([2.0, 8 / 3, np.log(0.5), np.log(1 / 3)])
g2 = np.array([(neg_elbo(th_pool + 1e-6 * e) - neg_elbo(th_pool - 1e-6 * e)) / 2e-6 for e in np.eye(4)])
print(f"   same joint ELBO gradient at PIFB2 pool point: norm {np.linalg.norm(g2):.3f} (not stationary for this joint)")

# ---------------- (3) reduced Hessian units map ----------------
print("(3) tau * Hess(R_Theory) vs PIFB2 eq:rg_reduced_hessian")
tau = 0.7
pi = np.array([0.2, 0.5, 0.3])
Mk = [rng.normal(size=(2, 2)) for _ in range(3)]
Mk = [M @ M.T + 0.5 * np.eye(2) for M in Mk]
ck = [rng.normal(size=2) for _ in range(3)]
E = lambda x: np.array([0.5 * (x - ck[j]) @ Mk[j] @ (x - ck[j]) for j in range(3)])
gE = lambda x: np.array([Mk[j] @ (x - ck[j]) for j in range(3)])
R = lambda x: -np.log(np.sum(pi * np.exp(-E(x) / tau)))
x0 = rng.normal(size=2)
eps = 1e-4
H_fd = np.zeros((2, 2))
for a in range(2):
    for c in range(2):
        ea, ec = np.eye(2)[a] * eps, np.eye(2)[c] * eps
        H_fd[a, c] = (R(x0 + ea + ec) - R(x0 + ea - ec) - R(x0 - ea + ec) + R(x0 - ea - ec)) / (4 * eps**2)
beta = pi * np.exp(-E(x0) / tau); beta /= beta.sum()
G = gE(x0); gbar = beta @ G
cov = sum(beta[j] * np.outer(G[j] - gbar, G[j] - gbar) for j in range(3))
H_pifb2 = sum(beta[j] * Mk[j] for j in range(3)) - cov / tau
print(f"   max |tau*H_Theory - H_PIFB2| = {np.abs(tau * H_fd - H_pifb2).max():.2e} (FD second differences)")
