r"""L10: conditioning of the transported covariance A = Omega Sigma_j Omega^T, Omega = e^{phi_i} e^{-phi_j},
as a function of the frame norm, and fp32 accuracy of the transported KL (PIFB2 2375, 2510, 2613).
KL computed in fp32 by the textbook route (form A, Cholesky solve, logdet) against a float64 reference.
"""
import numpy as np
from scipy.linalg import expm, cho_factor, cho_solve
rng = np.random.default_rng(12)
def kl(mi, Si, mj, A, dt):
    Si, A, mi, mj = Si.astype(dt), A.astype(dt), mi.astype(dt), mj.astype(dt)
    try:
        c = cho_factor(A, lower=True)
    except np.linalg.LinAlgError:
        return np.nan
    d = mi - mj; K = len(mi)
    ld_A = 2 * np.sum(np.log(np.diag(c[0]))); ld_S = 2 * np.sum(np.log(np.diag(np.linalg.cholesky(Si))))
    return 0.5 * (np.trace(cho_solve(c, Si)) + d @ cho_solve(c, d) - K + ld_A - ld_S)
K = 5
print(f"K={K}, 200 draws per frame scale; Sigma_i, Sigma_j well conditioned (kappa ~ 10); mu offsets O(1)")
print(" |phi|_F each | median kappa(Omega) | median kappa(A) | fp32 KL rel err median / 90th pct | fp32 Cholesky failures")
for s in (0.5, 1.0, 2.0, 3.0, 4.0, 5.0):
    kO, kA, errs, fails = [], [], [], 0
    for _ in range(200):
        pi, pj = rng.standard_normal((K, K)), rng.standard_normal((K, K)); pi *= s / np.linalg.norm(pi); pj *= s / np.linalg.norm(pj)
        O = expm(pi) @ expm(-pj)
        B = rng.standard_normal((K, K)); Si = B @ B.T + np.eye(K); B = rng.standard_normal((K, K)); Sj = B @ B.T + np.eye(K)
        mi, mjt = rng.standard_normal(K), O @ rng.standard_normal(K)
        A = O @ Sj @ O.T; A = 0.5 * (A + A.T)
        ref = kl(mi, Si, mjt, A, np.float64); v = kl(mi, Si, mjt, A, np.float32)
        kO.append(np.linalg.cond(O)); kA.append(np.linalg.cond(A))
        if np.isnan(v): fails += 1
        else: errs.append(abs(v - ref) / abs(ref))
    e = np.array(errs)
    print(f"   {s:4.1f}        | {np.median(kO):12.3e}       | {np.median(kA):12.3e}  |  {np.median(e):.2e} / {np.percentile(e, 90):.2e}          | {fails}/200")
