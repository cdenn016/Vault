r"""L19: PIFB2 prop:meta_clock_slowdown (1856) against Theory c07 thm:hist-record-clock-contraction.

Uniform-weight mean-sector case, common precision Lambda, N constituents.
  delta mu_i = delta c + eps_i,  E eps_i = 0, eps_i uncorrelated.
(a) Z_I = E[Delta I_I]/E[Delta I_i] = f + (1-f)/N under the averaging convention Sigma_I = Sigma.
(b) The averaging-convention barycenter law N(mean mu_i, Sigma) is the image of the product law
    prod_i N(mu_i, Sigma) under the FIXED Markov kernel y = mean(x) + xi, xi ~ N(0, Sigma - Sigma/N),
    so Theory's contraction applies: meta Fisher speed^2 <= joint Fisher speed^2 = sum_i speeds^2.
(c) Precision pooling Lambda_I = N Lambda is the deterministic averaging image (also Markov):
    per-constituent ratio f N + (1-f) > 1 for coherent drift, but meta <= joint still holds.
"""
import numpy as np

rng = np.random.default_rng(1)
K, N, T = 3, 7, 400000
A = rng.normal(size=(K, K)); Sig = A @ A.T + np.eye(K); Lam = np.linalg.inv(Sig)
Lc = np.linalg.cholesky(Sig)
for f_target in [0.1, 0.5, 0.9]:
    # choose scales so that E||dc||^2_Lam : E||eps||^2_Lam = f : 1-f  (isotropic in Sigma-whitened coords)
    sc, se = np.sqrt(f_target), np.sqrt(1 - f_target)
    dc = sc * (Lc @ rng.normal(size=(K, T))).T / np.sqrt(K)
    eps = se * np.einsum('kl,tnl->tnk', Lc, rng.normal(size=(T, N, K))) / np.sqrt(K)
    dmu = dc[:, None, :] + eps
    nrm = lambda v: np.einsum('...k,kl,...l->...', v, Lam, v)
    Ei = nrm(dmu).mean()                      # E ||dmu_i||^2 (per constituent; KL = half of it)
    dbar = dmu.mean(axis=1)
    EI_avg = nrm(dbar).mean()                 # averaging convention: Lambda_I = Lambda
    EI_pp = N * nrm(dbar).mean()              # precision pooling: Lambda_I = N Lambda
    Ejoint = nrm(dmu).sum(axis=1).mean()      # product-law Fisher speed^2
    f = nrm(dc).mean() / (nrm(dc).mean() + nrm(eps[:, 0, :]).mean())
    print(f"f={f:.4f}  Z_avg={EI_avg/Ei:.4f}  f+(1-f)/N={f+(1-f)/N:.4f}  "
          f"Z_pp={EI_pp/Ei:.4f}  fN+(1-f)={f*N+(1-f):.4f}  "
          f"meta/joint avg={EI_avg/Ejoint:.4f}  pp={EI_pp/Ejoint:.4f}")

noise = Sig - Sig / N
print("(b) min eigenvalue of Markov-noise covariance Sigma - Sigma/N:", np.linalg.eigvalsh(noise).min())
# exact law check: image of prod N(mu_i, Sig) under y = mean(x) + xi has mean mean(mu), cov Sig/N + noise = Sig
print("(b) image covariance residual:", np.abs(Sig / N + noise - Sig).max())
