"""L05: barycenter as M-step; I-projection barycenter as a second gauge-covariant variational minimizer;
mean-field parent (E-step) precision addition.  K = 2, float64.
"""
import numpy as np
from scipy.optimize import minimize
rng = np.random.default_rng(11)
K, n = 2, 4
def spd():
    A = rng.normal(size=(K, K)); return A @ A.T + 0.5*np.eye(K)
def gl():
    A = rng.normal(size=(K, K))
    if np.linalg.det(A) < 0: A[:, 0] *= -1
    return A + 0.2*np.eye(K)
mu = [rng.normal(size=K) for _ in range(n)]; Sig = [spd() for _ in range(n)]
OmIi = [gl() for _ in range(n)]            # Omega_{I,i}: child frame -> parent frame
w = rng.random(n); w /= w.sum()
def kl(m1, S1, m2, S2):
    S2i = np.linalg.inv(S2); d = m2 - m1
    return 0.5*(np.trace(S2i @ S1) + d @ S2i @ d - K + np.linalg.slogdet(S2)[1] - np.linalg.slogdet(S1)[1])
# transported moments
nu = [OmIi[i] @ mu[i] for i in range(n)]; S = [OmIi[i] @ Sig[i] @ OmIi[i].T for i in range(n)]
muB = sum(w[i]*nu[i] for i in range(n))
SB = sum(w[i]*(S[i] + np.outer(nu[i]-muB, nu[i]-muB)) for i in range(n))
# (1) M-step: maximize sum_i w_i E_{q_i} log N(k; Omega_{iI} mu_I, Omega_{iI} Sigma_I Omega_{iI}^T), Omega_{iI} = inv(Omega_{Ii})
def unpack(x):
    L = np.array([[np.exp(x[2]), 0], [x[3], np.exp(x[4])]]); return x[:2], L @ L.T
def negEll(x):
    mI, SI = unpack(x); v = 0.0
    for i in range(n):
        Oi = np.linalg.inv(OmIi[i]); P = Oi @ SI @ Oi.T; Pinv = np.linalg.inv(P); d = mu[i] - Oi @ mI
        v += w[i]*0.5*(np.trace(Pinv @ Sig[i]) + d @ Pinv @ d + np.linalg.slogdet(2*np.pi*P)[1])
    return v
best = min((minimize(negEll, rng.normal(size=5), method='BFGS', options={'gtol':1e-12}) for _ in range(6)), key=lambda z: z.fun)
mI, SI = unpack(best.x)
print('(1) M-step optimum vs barycenter-with-dispersion: |dmu| =', np.abs(mI-muB).max(), ' |dSigma| =', np.abs(SI-SB).max())
# same objective is sum_i w_i KL(Omega_{Ii} q_i || q_I) up to a q_I-independent constant
c = [negEll(np.r_[muB, np.log(np.linalg.cholesky(SB)[0,0]), np.linalg.cholesky(SB)[1,0], np.log(np.linalg.cholesky(SB)[1,1])])
     - sum(w[i]*kl(nu[i], S[i], muB, SB) for i in range(n))]
x2 = rng.normal(size=5); m2, S2_ = unpack(x2)
c.append(negEll(x2) - sum(w[i]*kl(nu[i], S[i], m2, S2_) for i in range(n)))
print('    [neg E log shadow] - [sum w KL(Omega_Ii q_i||q_I)] at two parent states:', c, '(equal => same argmin)')
# (2) I-projection (reverse-KL) barycenter: argmin_q sum w_i KL(q || Omega_{Ii} q_i)
Lam = sum(w[i]*np.linalg.inv(S[i]) for i in range(n)); SR = np.linalg.inv(Lam)
mR = SR @ sum(w[i]*np.linalg.solve(S[i], nu[i]) for i in range(n))
def negR(x):
    m, Sx = unpack(x); return sum(w[i]*kl(m, Sx, nu[i], S[i]) for i in range(n))
bR = min((minimize(negR, rng.normal(size=5), method='BFGS', options={'gtol':1e-12}) for _ in range(6)), key=lambda z: z.fun)
mr, Sr = unpack(bR.x)
print('(2) I-projection closed form vs numeric minimizer: |dmu| =', np.abs(mr-mR).max(), ' |dSigma| =', np.abs(Sr-SR).max())
A = gl()   # common gauge transformation in the parent frame
LamA = sum(w[i]*np.linalg.inv(A @ S[i] @ A.T) for i in range(n)); SRA = np.linalg.inv(LamA)
mRA = SRA @ sum(w[i]*np.linalg.solve(A @ S[i] @ A.T, A @ nu[i]) for i in range(n))
print('    equivariance residual |mu(A.)-A mu|, |Sigma(A.)-A Sigma A^T| =', np.abs(mRA - A @ mR).max(), np.abs(SRA - A @ SR @ A.T).max())
print('    I-projection differs from M-projection: |dmu| =', np.abs(mR-muB).max(), ' |dSigma| =', np.abs(SR-SB).max())
# (3) mean-field parent update in the augmented joint (E-step): precision = Lam_p + sum Omega^T Omega / s2, independent of Sigma_i
s2 = 0.2; Lp = spd()
def mf_parent_prec(Sigs):
    return Lp + sum(np.linalg.inv(OmIi[i]).T @ np.linalg.inv(OmIi[i]) for i in range(n))/s2
print('(3) MF parent precision change when constituent covariances are rescaled x10:', np.abs(mf_parent_prec(Sig) - mf_parent_prec([10*s for s in Sig])).max())
