"""L05: PIFB2 App. G, thm:self_consistent_source_equilibrium and the Banach mean sub-map bound.
(1) Eq. eq:equilibrium_row_kl_identity holds for ARBITRARY (q, beta), not only at a fixed point;
(2) geometric-pooling Euler equation: B_i minimizes a KL(r||p) + lam sum_j beta_j KL(r||T q_j) on the simplex;
(3) Banach claim: neighbor-operator norm of the frozen mean sub-map vs the stated bound
    lam_max(M)/(alpha lam_min(Lp) + lam_max(M)), M = sum_j beta_ij Lam_t,ij, orthogonal transports.
"""
import numpy as np
from scipy.optimize import minimize
rng = np.random.default_rng(13)
nX, nsrc = 5, 3
q = rng.dirichlet(np.ones(nX)); Tq = rng.dirichlet(np.ones(nX), size=nsrc)
beta = rng.dirichlet(np.ones(nsrc)); pi = rng.dirichlet(np.ones(nsrc))
Qm = beta[:, None]*q[None, :]; Pm = pi[:, None]*Tq
lhs = (Qm*np.log(Qm/Pm)).sum()
rhs = sum(beta[j]*(q*np.log(q/Tq[j])).sum() for j in range(nsrc)) + (beta*np.log(beta/pi)).sum()
print('(1) row KL chain-rule identity at a random non-equilibrium (q, beta): residual =', lhs - rhs)
# (2)
p = rng.dirichlet(np.ones(nX)); a, lam = 0.7, 1.9; A = a + lam
B = p**(a/A)*np.prod(Tq**(lam*beta[:, None]/A), axis=0); B /= B.sum()
def obj(z):
    r = np.exp(z - z.max()); r /= r.sum()
    return a*(r*np.log(r/p)).sum() + lam*sum(beta[j]*(r*np.log(r/Tq[j])).sum() for j in range(nsrc))
z = minimize(obj, rng.normal(size=nX), method='BFGS', options={'gtol':1e-12}).x
r = np.exp(z - z.max()); r /= r.sum()
print('(2) geometric pool vs numeric minimizer: max |diff| =', np.abs(r - B).max())
# (3) Banach bound. Full frozen mean map on N agents: mu_i <- (alpha Lp + M_i)^{-1}(alpha Lp mu_p + sum_j beta_ij Lt_ij Om_ij mu_j)
K, N = 2, 3
def rot(t): return np.array([[np.cos(t), -np.sin(t)], [np.sin(t), np.cos(t)]])
worst = 0.0; worst_rec = None
for trial in range(3000):
    alpha = 10**rng.uniform(-2, 0)
    Lp = np.diag(10**rng.uniform(-1, 1, K))
    Lt = {}; Om = {}; be = {}
    for i in range(N):
        b = rng.dirichlet(np.ones(N-1)); js = [j for j in range(N) if j != i]
        for bj, j in zip(b, js):
            d = 10**rng.uniform(-1, 2, K); U = rot(rng.uniform(0, np.pi))
            Lt[i, j] = U @ np.diag(d) @ U.T; Om[i, j] = rot(rng.uniform(0, 2*np.pi)); be[i, j] = bj
    Jac = np.zeros((N*K, N*K)); ratio_claim = 0.0
    for i in range(N):
        M = sum(be[i, j]*Lt[i, j] for j in range(N) if j != i)
        Ainv = np.linalg.inv(alpha*Lp + M)
        for j in range(N):
            if j != i: Jac[i*K:(i+1)*K, j*K:(j+1)*K] = Ainv @ (be[i, j]*Lt[i, j] @ Om[i, j])
        lm = np.linalg.eigvalsh(M).max()
        ratio_claim = max(ratio_claim, lm/(alpha*np.linalg.eigvalsh(Lp).min() + lm))
    nrm2 = np.linalg.norm(Jac, 2)
    blockinf = max(sum(np.linalg.norm(Jac[i*K:(i+1)*K, j*K:(j+1)*K], 2) for j in range(N)) for i in range(N))
    rho = np.abs(np.linalg.eigvals(Jac)).max()
    if nrm2 - ratio_claim > worst:
        worst = nrm2 - ratio_claim; worst_rec = (nrm2, blockinf, rho, ratio_claim)
print('(3) largest excess of ||Jacobian||_2 over the stated bound:', worst)
print('    at that instance: ||J||_2 = %.4f, block-inf norm = %.4f, spectral radius = %.4f, stated bound = %.4f' % worst_rec)

# (3b) reproduce: search for an instance with spectral radius > 1, then iterate the frozen mean map directly
rng = np.random.default_rng(99)
for trial in range(20000):
    alpha = 0.05; Lp = np.eye(K)
    Lt = {}; Om = {}; be = {}
    for i in range(N):
        b = rng.dirichlet(np.ones(N-1)); js = [j for j in range(N) if j != i]
        for bj, j in zip(b, js):
            d = 10**rng.uniform(-1, 2, K); U = rot(rng.uniform(0, np.pi))
            Lt[i, j] = U @ np.diag(d) @ U.T; Om[i, j] = rot(rng.uniform(0, 2*np.pi)); be[i, j] = bj
    Jac = np.zeros((N*K, N*K)); bound = 0.0
    for i in range(N):
        M = sum(be[i, j]*Lt[i, j] for j in range(N) if j != i); Ainv = np.linalg.inv(alpha*Lp + M)
        lm = np.linalg.eigvalsh(M).max(); bound = max(bound, lm/(alpha + lm))
        for j in range(N):
            if j != i: Jac[i*K:(i+1)*K, j*K:(j+1)*K] = Ainv @ (be[i, j]*Lt[i, j] @ Om[i, j])
    rho = np.abs(np.linalg.eigvals(Jac)).max()
    if rho > 1.05: break
mu_p = np.zeros(K); mu = rng.normal(size=N*K); n0 = np.linalg.norm(mu)
for it in range(60):
    new = np.zeros_like(mu)
    for i in range(N):
        M = sum(be[i, j]*Lt[i, j] for j in range(N) if j != i)
        rhs = alpha*Lp @ mu_p + sum(be[i, j]*Lt[i, j] @ Om[i, j] @ mu[j*K:(j+1)*K] for j in range(N) if j != i)
        new[i*K:(i+1)*K] = np.linalg.solve(alpha*Lp + M, rhs)
    mu = new
print('(3b) trial %d: stated bound max_i lam_max(M)/(alpha+lam_max(M)) = %.4f, spectral radius = %.4f, |mu_60|/|mu_0| = %.3e'
      % (trial, bound, rho, np.linalg.norm(mu)/n0))
