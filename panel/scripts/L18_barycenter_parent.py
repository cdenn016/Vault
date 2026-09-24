"""L18: meta-agent state, apex pooling, and the meta-clock versus the Theory's exact parents.

 (a) Full forward-KL (M-projection) barycenter = moment match of the mixture, dispersion included
     (Supplement G prop:cg-gaussian-forward-kl-barycenter); the PIFB2 implementation/apex form
     without dispersion has a strictly larger objective (numerical optimum check).
 (b) Theory prop:full-graph-aggregate-prior: over a Gaussian prior family, the optimal top prior
     for recognition laws q_n minimizes KL(Qbar||p) -> the same moment match (dispersion kept).
 (c) Mean-map pushforward of a product law (an exact Markov coarse channel) has covariance Sigma/N,
     the precision-pooled form PIFB2 declines; bit-production ratios for the two conventions, and
     the Theory's same-path contraction relative to the JOINT history (thm:hist-record-clock-contraction).
"""
import numpy as np
from scipy.optimize import minimize

rng = np.random.default_rng(7)
K, N = 2, 4


def kl(m1, S1, m2, S2):
    S2i = np.linalg.inv(S2)
    d = m2 - m1
    return 0.5 * (np.log(np.linalg.det(S2) / np.linalg.det(S1)) + np.trace(S2i @ S1) + d @ S2i @ d - len(m1))


mus = [rng.normal(size=K) * 1.5 for _ in range(N)]
Ss = []
for _ in range(N):
    A = rng.normal(size=(K, K))
    Ss.append(A @ A.T + np.eye(K))
w = np.ones(N) / N
mbar = sum(wi * m for wi, m in zip(w, mus))
Sbar_full = sum(wi * (S + np.outer(m - mbar, m - mbar)) for wi, S, m in zip(w, Ss, mus))
Sbar_nodisp = sum(wi * S for wi, S in zip(w, Ss))


def obj(m, S):
    return sum(wi * kl(mi, Si, m, S) for wi, mi, Si in zip(w, mus, Ss))


def unpack(x):
    L = np.array([[np.exp(x[2]), 0.0], [x[3], np.exp(x[4])]])
    return x[:2], L @ L.T


x0 = np.zeros(5)
r = minimize(lambda x: obj(*unpack(x)), x0, method="BFGS", options={"gtol": 1e-12, "maxiter": 5000})
mopt, Sopt = unpack(r.x)
print(f"(a) |m_opt - mbar| = {np.abs(mopt-mbar).max():.2e}, |S_opt - Sbar_full| = {np.abs(Sopt-Sbar_full).max():.2e}")
print(f"    objective full = {obj(mbar, Sbar_full):.10f}, no-dispersion = {obj(mbar, Sbar_nodisp):.10f}, "
      f"gap = {obj(mbar, Sbar_nodisp)-obj(mbar, Sbar_full):.4e} > 0")
score = 0.5 * (np.log(np.linalg.det(Sbar_full)) - sum(wi * np.log(np.linalg.det(S)) for wi, S in zip(w, Ss)))
print(f"    G eq:cg-gaussian-barycenter-score = {score:.10f} (matches full objective: diff {abs(score-obj(mbar,Sbar_full)):.1e})")

# (b) aggregate prior: Monte Carlo cross-entropy of mixture against candidate Gaussians
M = 400000
comp = rng.integers(0, N, size=M)
samples = np.empty((M, K))
for c in range(N):
    idx = comp == c
    samples[idx] = rng.multivariate_normal(mus[c], Ss[c], size=idx.sum())


def xent(m, S):
    Si = np.linalg.inv(S)
    d = samples - m
    return 0.5 * np.mean(np.einsum("ni,ij,nj->n", d, Si, d)) + 0.5 * np.log(np.linalg.det(2 * np.pi * S))


print(f"(b) E_Qbar[-log p]: full moment match {xent(mbar, Sbar_full):.5f} < no-dispersion {xent(mbar, Sbar_nodisp):.5f}")

# (c) meta clock conventions (identity transport, common Sigma)
Sig = np.array([[1.0, 0.3], [0.3, 0.5]])
Lam = np.linalg.inv(Sig)
Cc, Ee = 0.7, 1.3  # E||dc||^2_Lam, E||eps||^2_Lam per agent
fcoh = Cc / (Cc + Ee)
for Nn in (2, 4, 16):
    const = Cc + Ee
    avg_conv = (Cc + Ee / Nn) / const  # meta precision Lam (averaging convention)
    push_conv = Nn * (Cc + Ee / Nn) / const  # meta precision N Lam (mean-map pushforward)
    joint = Nn * const
    push_speed2 = Nn * (Cc + Ee / Nn)
    print(f"(c) N={Nn:2d}: f_coh+(1-f_coh)/N = {fcoh+(1-fcoh)/Nn:.4f}; averaging ratio {avg_conv:.4f}; "
          f"pushforward ratio {push_conv:.4f}; pushforward/joint speed^2 {push_speed2/joint:.4f} <= 1")
# check pushforward covariance by sampling
Nn = 4
Y = rng.multivariate_normal(np.zeros(K), Sig, size=(200000, Nn))
Ybar = Y.mean(axis=1)
print(f"    sampled cov of mean-map image vs Sigma/N: max diff {np.abs(np.cov(Ybar.T) - Sig/Nn).max():.3e}")

# same-path defect for deterministic velocities (Theory eq:hist-record-conditional-variance-defect)
V = rng.normal(size=(Nn, K))
joint2 = sum(v @ Lam @ v for v in V)
vbar = V.mean(0)
rec2 = Nn * vbar @ Lam @ vbar
defect = sum((v - vbar) @ Lam @ (v - vbar) for v in V)
print(f"    joint speed^2 {joint2:.10f} - image speed^2 {rec2:.10f} = {joint2-rec2:.10f}; sum (v_i-vbar)^T Lam (v_i-vbar) = {defect:.10f}")
