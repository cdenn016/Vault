"""2.6 local mixture: product-restricted row (Gibbs, clamped query law) vs unrestricted I-projection with the
y-marginal clamped to the query law (Jeffrey update). Discrete y for exactness, then the paper's 1-D example."""
import json, math
import numpy as np
from scipy import integrate, optimize, special, stats
rng = np.random.default_rng(7)
out = {}
ny, nj = 7, 3
pK = rng.dirichlet(np.ones(ny), size=nj); qQ = rng.dirichlet(np.ones(ny)); pi = rng.dirichlet(np.ones(nj))
P = pi[:, None] * pK                                   # P(J=j, y)
Dj = np.array([np.sum(qQ * np.log(qQ / pK[j])) for j in range(nj)])
gibbs = np.exp(np.log(pi) - Dj - special.logsumexp(np.log(pi) - Dj))
KL_prod = np.sum((gibbs[:, None] * qQ[None, :]) * np.log(gibbs[:, None] * qQ[None, :] / P))
postJ_y = P / P.sum(axis=0, keepdims=True)             # P(J|y)
Qj = postJ_y * qQ[None, :]                             # Jeffrey joint q(y) P(J|y)
KL_jeff = np.sum(Qj * np.log(Qj / P))
PY = P.sum(axis=0)
out["KL_prod_opt(Gibbs row)"] = KL_prod
out["KL_unrestricted_Jeffrey"] = KL_jeff
out["KL_Jeffrey_minus_KL(qQ||P_Y)"] = KL_jeff - np.sum(qQ * np.log(qQ / PY))
# numerically minimize KL over all Q(J,y) with fixed y-marginal: parametrize conditional rows
def kl_cond(theta):
    T = theta.reshape(nj, ny); C = np.exp(T - special.logsumexp(T, axis=0, keepdims=True)); Q = C * qQ[None, :]
    return np.sum(Q * np.log(Q / P))
res = optimize.minimize(kl_cond, np.zeros(nj * ny), method="BFGS", options={"gtol": 1e-12})
T = res.x.reshape(nj, ny); C = np.exp(T - special.logsumexp(T, axis=0, keepdims=True))
out["numeric_unrestricted_opt_minus_Jeffrey_KL"] = res.fun - KL_jeff
out["J_marginal_Jeffrey"] = list(Qj.sum(axis=1)); out["Gibbs_row"] = list(gibbs)
out["TV(Gibbs,Jeffrey)"] = 0.5 * float(np.abs(gibbs - Qj.sum(axis=1)).sum())
# paper example: q_Q=N(0,4), keys N(0,1), N(2,1), uniform prior
D0 = 0.5 * (4 + 0 - 1 - math.log(4)); D1 = 0.5 * (4 + 4 - 1 - math.log(4))
g1 = 1 / (1 + math.exp(D1 - D0))
jeff1 = integrate.quad(lambda y: stats.norm.pdf(y, 0, 2) / (1 + math.exp(2 - 2 * y)), -40, 40, epsabs=1e-14)[0]
out["paper_example_routing_Gibbs_rho1"] = g1; out["paper_example_routing_Jeffrey"] = jeff1
print(json.dumps(out, indent=1, default=float))
