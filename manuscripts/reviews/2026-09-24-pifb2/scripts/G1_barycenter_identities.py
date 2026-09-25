r"""G1 verified-no-defect checks (PIFB2.tex 1542-1566, 1602, 1625, 1633).
 (1) prop:barycenter_existence: numerical minimization of sum_i w_i KL(Omega_Ii q_i || q) over Gaussians equals
     the closed form (eq:meta_agent_mu_barycenter, eq:meta_agent_sigma_barycenter), K=3, GL+ transports.
 (2) 1602: the shared-prior M-step max_{mu_I,Sigma_I} sum_i w_i E_{q_i}[log N(Omega_iI mu_I, Omega_iI Sigma_I Omega_iI^T)]
     has the same maximizer (transport cancels up to the constant log|det Omega|).
 (3) 1625: pairwise-difference identity for weighted spreads.
 (4) 1633: weight gauge invariance w_i(h.X) = w_i(X) under the base-local action with an equivariant parent frame.
"""
import numpy as np
from scipy.linalg import expm
from scipy.optimize import minimize
rng = np.random.default_rng(5); K = 3; n = 4

def kl(m1, S1, m2, S2):
    S2i = np.linalg.inv(S2); dd = m2 - m1
    return 0.5*(np.trace(S2i@S1) + dd@S2i@dd - K + np.log(np.linalg.det(S2)/np.linalg.det(S1)))
def spd(): A = rng.standard_normal((K, K)); return A@A.T + 0.3*np.eye(K)
mus = [rng.standard_normal(K) for _ in range(n)]; Ss = [spd() for _ in range(n)]
Om = [expm(0.5*rng.standard_normal((K, K))) for _ in range(n)]; w = rng.dirichlet(np.ones(n))
mt = [O@m for O, m in zip(Om, mus)]; St = [O@S@O.T for O, S in zip(Om, Ss)]
muI = sum(wi*m for wi, m in zip(w, mt)); SigI = sum(wi*(S + np.outer(m - muI, m - muI)) for wi, m, S in zip(w, mt, St))
def unpack(p):
    L = np.zeros((K, K)); L[np.tril_indices(K)] = p[K:]; return p[:K], L@L.T + 1e-9*np.eye(K)
obj = lambda p: sum(wi*kl(m, S, *unpack(p)) for wi, m, S in zip(w, mt, St))
L0 = np.linalg.cholesky(np.eye(K)); p0 = np.concatenate([np.zeros(K), L0[np.tril_indices(K)]])
r = minimize(obj, p0, method='BFGS', options=dict(gtol=1e-12, maxiter=5000)); m_, S_ = unpack(r.x)
print(f"(1) closed form vs numerical minimizer: |dmu| = {np.linalg.norm(m_ - muI):.2e}, |dSigma|_F = {np.linalg.norm(S_ - SigI):.2e} (|Sigma| = {np.linalg.norm(SigI):.2f})")
def ell(p):
    m, S = unpack(p); tot = 0.0
    for wi, O, mu, Sig in zip(w, Om, mus, Ss):
        Oi = np.linalg.inv(O); C = Oi@S@Oi.T; Ci = np.linalg.inv(C); dd = mu - Oi@m
        tot += wi*(-0.5*np.log(np.linalg.det(C)) - 0.5*np.trace(Ci@(Sig + np.outer(dd, dd))))
    return -tot
r2 = minimize(ell, p0, method='BFGS', options=dict(gtol=1e-12, maxiter=5000)); m2, S2 = unpack(r2.x)
print(f"(2) shared-prior M-step maximizer vs closed form: |dmu| = {np.linalg.norm(m2 - muI):.2e}, |dSigma|_F = {np.linalg.norm(S2 - SigI):.2e}")
lhs = sum(wi*np.outer(m - muI, m - muI) for wi, m in zip(w, mt))
rhs = 0.5*sum(w[i]*w[j]*np.outer(mt[i] - mt[j], mt[i] - mt[j]) for i in range(n) for j in range(n))
print(f"(3) pairwise-difference identity residual: {np.linalg.norm(lhs - rhs):.2e} (scale {np.linalg.norm(lhs):.2f})")
# (4) weights under base-local action: U_i -> h U_i, q_i -> h_# q_i, parent frame U_I -> h U_I
U = [expm(0.4*rng.standard_normal((K, K))) for _ in range(n)]; UI = expm(0.4*rng.standard_normal((K, K)))
h = expm(0.8*rng.standard_normal((K, K)))
def weights(U, UI, mus, Ss, qbar):
    out = []
    for Ui, m, S in zip(U, mus, Ss):
        O = UI@np.linalg.inv(Ui); out.append(np.exp(-kl(O@m, O@S@O.T, *qbar)))
    return np.array(out)
qbar = (rng.standard_normal(K), spd())
w0 = weights(U, UI, mus, Ss, qbar)
w1 = weights([h@Ui for Ui in U], h@UI, [h@m for m in mus], [h@S@h.T for S in Ss], (h@qbar[0], h@qbar[1]@h.T))
print(f"(4) weight gauge invariance residual (GL+(3), |log h| ~ {np.linalg.norm(0.8*np.ones(1)):.1f} scale): {np.max(abs(w1 - w0)):.2e} (weights ~ {w0.mean():.2e})")
