r"""L19: PIFB2 apex moment pool (1716-1726) against Theory c12 prop:full-graph-aggregate-prior.

Within the Gaussian family, argmin_p KL(Qbar || p) for Qbar = sum_j w_j N(m_j, S_j) is the full moment
match m* = sum w_j m_j, S* = sum w_j S_j + sum w_j (m_j - m*)(m_j - m*)^T.
PIFB2's apex drops the dispersion term: S_apex = sum w_j S_j. The excess cross-entropy is
  CE(apex) - CE(opt) = KL(N(m*, S*) || N(m*, S_apex)) >= 0.
"""
import numpy as np
from scipy.stats import multivariate_normal as mvn

rng = np.random.default_rng(2)
K, J = 2, 4
w = rng.dirichlet(np.ones(J))
ms = [2.0 * rng.normal(size=K) for _ in range(J)]
Ss = [(lambda B: B @ B.T + 0.3 * np.eye(K))(rng.normal(size=(K, K))) for _ in range(J)]
mstar = sum(wj * mj for wj, mj in zip(w, ms))
Sapex = sum(wj * Sj for wj, Sj in zip(w, Ss))
Sstar = Sapex + sum(wj * np.outer(mj - mstar, mj - mstar) for wj, mj in zip(w, ms))

# Monte Carlo cross-entropy -E_Qbar log p
M = 400000
comp = rng.choice(J, size=M, p=w)
X = np.stack([rng.multivariate_normal(ms[c], Ss[c]) for c in comp[:40000]])  # 4e4 samples
def CE(m, S):
    return -mvn(m, S).logpdf(X).mean()
ce_opt, ce_apex = CE(mstar, Sstar), CE(mstar, Sapex)
def kl(m0, S0, m1, S1):
    S1i = np.linalg.inv(S1); d = m1 - m0
    return 0.5 * (np.trace(S1i @ S0) + d @ S1i @ d - K + np.log(np.linalg.det(S1) / np.linalg.det(S0)))
print("MC  CE(apex)-CE(opt):", ce_apex - ce_opt)
print("exact KL(N(m*,S*)||N(m*,S_apex)):", kl(mstar, Sstar, mstar, Sapex))
# local optimality of S*: perturbations increase CE
for t in [-0.05, 0.05]:
    print(f"CE(S*+{t} I) - CE(S*):", CE(mstar, Sstar + t * np.eye(K)) - ce_opt)
