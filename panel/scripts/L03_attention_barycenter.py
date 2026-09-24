r"""L03: attention row, -tau log Z, surrogate differential, mixture bound, M-projection barycenter, quadratic-form identity.
PIFB2.tex l.556-590 (eq:mixture_free_energy, eq:softmax_attention_general), l.715-731 (eq:attention_full_equals_reduced,
eq:attention_envelope_differential, dS_i), l.1543-1560 (eq:meta_agent_barycenter, mu/sigma barycenter), l.2918-2927 (quadratic form ~ KL).
"""
import numpy as np
from scipy.optimize import minimize
rng = np.random.default_rng(11)
def kl(m1, S1, m2, S2):
    K = len(m1); S2i = np.linalg.inv(S2); d = m2-m1
    return 0.5*(np.log(np.linalg.det(S2)/np.linalg.det(S1)) + np.trace(S2i@S1) + d@S2i@d - K)
def spd(K, s=0.4):
    A = rng.normal(size=(K, K)); return A@A.T + s*np.eye(K)
K, N, tau = 2, 5, 0.7
pi = rng.dirichlet(np.ones(N))
mq, Sq = rng.normal(size=K), spd(K)
ms = [rng.normal(size=K) for _ in range(N)]; Ss = [spd(K) for _ in range(N)]
Om = [np.eye(K) + 0.3*rng.normal(size=(K, K)) for _ in range(N)]
Ej = np.array([kl(mq, Sq, O@m, O@S@O.T) for O, m, S in zip(Om, ms, Ss)])
Z = np.sum(pi*np.exp(-Ej/tau)); bstar = pi*np.exp(-Ej/tau)/Z
Ffull = lambda b: np.sum(b*Ej) + tau*np.sum(b*np.log(b/pi))
# (1) optimality on simplex vs numeric
res = minimize(lambda z: Ffull(np.exp(z)/np.exp(z).sum()), np.zeros(N), method="BFGS", options={"gtol": 1e-12})
bnum = np.exp(res.x)/np.exp(res.x).sum()
print(f"(1) ||beta* - numeric argmin|| = {np.linalg.norm(bstar-bnum):.2e}; F_full(beta*) + tau log Z = {Ffull(bstar)+tau*np.log(Z):.2e}")
# (2) surrogate differential: dS = sum b dE - tau^{-1} Cov_b(E, dE), directional check
dE = rng.normal(size=N); h = 1e-6
def S_of(E):
    b = pi*np.exp(-E/tau); b /= b.sum(); return np.sum(b*E)
def Fred(E): return -tau*np.log(np.sum(pi*np.exp(-E/tau)))
num_dS = (S_of(Ej+h*dE)-S_of(Ej-h*dE))/(2*h)
cov = np.sum(bstar*Ej*dE) - np.sum(bstar*Ej)*np.sum(bstar*dE)
pred = np.sum(bstar*dE) - cov/tau
num_dF = (Fred(Ej+h*dE)-Fred(Ej-h*dE))/(2*h)
print(f"(2) dS numeric {num_dS:.10f} formula {pred:.10f} resid {abs(num_dS-pred):.1e}; dF_red numeric {num_dF:.10f} envelope {np.sum(bstar*dE):.10f} resid {abs(num_dF-np.sum(bstar*dE)):.1e}")
# (3) tau=1: min_beta F_align = -log sum pi exp(-KL(q||p_j)) >= KL(q || sum_j pi_j p_j) (mixture); MC estimate
Z1 = np.sum(pi*np.exp(-Ej)); Fmin1 = -np.log(Z1)
M = 400000; L = np.linalg.cholesky(Sq); x = mq + rng.normal(size=(M, K))@L.T
def lpdf(x, m, S):
    d = x-m; Si = np.linalg.inv(S); return -0.5*np.einsum('ni,ij,nj->n', d, Si, d) - 0.5*np.log((2*np.pi)**K*np.linalg.det(S))
lq = lpdf(x, mq, Sq)
lmix = np.logaddexp.reduce(np.stack([np.log(pi[j]) + lpdf(x, Om[j]@ms[j], Om[j]@Ss[j]@Om[j].T) for j in range(N)]), axis=0)
kl_mix = np.mean(lq - lmix); se = np.std(lq-lmix)/np.sqrt(M)
print(f"(3) tau=1: -log Z = {Fmin1:.5f} >= KL(q||mixture) = {kl_mix:.5f} +/- {se:.5f}  (gap {Fmin1-kl_mix:.4f})")
# (4) M-projection barycenter: argmin_q sum_i w_i KL(p_i || q) over Gaussians vs moment-matching closed form
w = rng.dirichlet(np.ones(4)); mus = [rng.normal(size=K) for _ in range(4)]; Sis = [spd(K) for _ in range(4)]
mu_s = sum(wi*m for wi, m in zip(w, mus))
Sig_s = sum(wi*(S + np.outer(mu_s-m, mu_s-m)) for wi, m, S in zip(w, mus, Sis))
def obj(z):
    m = z[:K]; Lc = np.array([[np.exp(z[2]), 0], [z[3], np.exp(z[4])]]); S = Lc@Lc.T
    return sum(wi*kl(mi, Si_, m, S) for wi, mi, Si_ in zip(w, mus, Sis))
r = minimize(obj, np.zeros(5), method="BFGS", options={"gtol": 1e-12})
Lc = np.array([[np.exp(r.x[2]), 0], [r.x[3], np.exp(r.x[4])]])
print(f"(4) M-projection: ||mu - closed|| {np.linalg.norm(r.x[:K]-mu_s):.1e}, ||Sigma - closed|| {np.linalg.norm(Lc@Lc.T-Sig_s):.1e}")
# reverse direction for contrast: argmin_q sum w KL(q || p_i) is the precision-weighted (geometric) pool
def objr(z):
    m = z[:K]; Lc = np.array([[np.exp(z[2]), 0], [z[3], np.exp(z[4])]]); S = Lc@Lc.T
    return sum(wi*kl(m, S, mi, Si_) for wi, mi, Si_ in zip(w, mus, Sis))
rr = minimize(objr, np.zeros(5), method="BFGS", options={"gtol": 1e-12})
Lam = sum(wi*np.linalg.inv(S) for wi, S in zip(w, Sis)); Sg = np.linalg.inv(Lam); mg = Sg@sum(wi*np.linalg.inv(S)@m for wi, m, S in zip(w, mus, Sis))
Lr = np.array([[np.exp(rr.x[2]), 0], [rr.x[3], np.exp(rr.x[4])]])
print(f"    I-projection (reverse) = geometric pool: ||mu-mg|| {np.linalg.norm(rr.x[:K]-mg):.1e}, ||Sigma-Sg|| {np.linalg.norm(Lr@Lr.T-Sg):.1e}")
# (5) quadratic form identity: (1/4) E[(ki - O kj)^T Lam (ki - O kj)] with Lam = t (O Sj O^T)^{-1}
t = 1.7; O = Om[0]; mi, Sii = mq, Sq; mj, Sj = ms[0], Ss[0]
St = O@Sj@O.T; Lamq = t*np.linalg.inv(St)
Eq = np.trace(Lamq@(Sii + St)) + (mi - O@mj)@Lamq@(mi - O@mj)
rhs = t/2*kl(mi, Sii, O@mj, St) + t*K/2 + t/4*np.log(np.linalg.det(np.linalg.solve(St, Sii)))
print(f"(5) (1/4)E = {Eq/4:.12f};  (t/2)KL + tK/2 + (t/4)logdet(St^-1 Si) = {rhs:.12f}; resid {abs(Eq/4-rhs):.1e}")
