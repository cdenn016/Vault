"""L04: finite-difference checks of PIFB2 Appendix A direct-KL gradients (float64).
 receiver: dKL/dmu_i, dKL/dSigma_i (2260, 2307); unconstrained dKL/dOmega (eq:kl_omega_unconstrained, 2382)
 sender:   dE_li/dmu_i, dE_li/dSigma_i (2435-2436)."""
import numpy as np
rng = np.random.default_rng(5); K = 3
def spd(): M = rng.normal(size=(K, K)); return M@M.T + 0.5*np.eye(K)
def kl(m0, S0, m1, S1):
    S1i = np.linalg.inv(S1); d = m1 - m0
    return 0.5*(np.trace(S1i@S0) + d@S1i@d - K + np.log(np.linalg.det(S1)/np.linalg.det(S0)))
mi, Si, mj, Sj = rng.normal(size=K), spd(), rng.normal(size=K), spd(); Om = rng.normal(size=(K, K)) + 2*np.eye(K)
h = 1e-6
def fdvec(f, x): return np.array([(f(x + h*e) - f(x - h*e))/(2*h) for e in np.eye(len(x))])
def fdmat(f, X):
    G = np.zeros_like(X)
    for a in range(X.shape[0]):
        for b in range(X.shape[1]):
            E = np.zeros_like(X); E[a, b] = h; G[a, b] = (f(X + E) - f(X - E))/(2*h)
    return G
A = Om@Sj@Om.T; Lam = np.linalg.inv(A); r = mi - Om@mj
print('recv dmu :', np.abs(fdvec(lambda m: kl(m, Si, Om@mj, A), mi) - Lam@r).max())
print('recv dSig:', np.abs(fdmat(lambda S: kl(mi, S, Om@mj, A), Si) - 0.5*(-np.linalg.inv(Si) + Lam)).max())
N = np.eye(K) - Lam@Si - np.outer(Lam@r, Om@mj) - np.outer(Lam@r, r)
OmiT = np.linalg.inv(Om).T
anal = N@OmiT
alt = OmiT - Lam@Si@OmiT - np.outer(Lam@r, mj) - np.outer(Lam@r, r)@Lam@Om@Sj
fd = fdmat(lambda O: kl(mi, Si, O@mj, O@Sj@O.T), Om)
print('dOmega N Om^-T:', np.abs(fd - anal).max(), '; expanded form:', np.abs(fd - alt).max())
# sender: E_li = KL(q_l || Om q_i)
ml, Sl = rng.normal(size=K), spd()
Ali = Om@Si@Om.T; Lt = np.linalg.inv(Ali); d = Om@mi - ml
print('send dmu :', np.abs(fdvec(lambda m: kl(ml, Sl, Om@m, Ali), mi) - np.linalg.inv(Si)@np.linalg.inv(Om)@(Om@mi - ml)).max())
print('send dSig:', np.abs(fdmat(lambda S: kl(ml, Sl, Om@mi, Om@S@Om.T), Si) - 0.5*Om.T@(Lt - Lt@(Sl + np.outer(d, d))@Lt)@Om).max())
