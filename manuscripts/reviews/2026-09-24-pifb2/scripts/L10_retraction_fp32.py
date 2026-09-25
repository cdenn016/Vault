r"""L10: SPD retraction (PIFB2 2330-2349, 2496, 2510), natural gradient (2317-2328, 2629-2635),
and the fp32 positive-definiteness / Cholesky claims of 2510.

R_Sigma(Delta) = Sigma^{1/2} expm(Sigma^{-1/2} Delta Sigma^{-1/2}) Sigma^{1/2}.
"""
import numpy as np
from scipy.linalg import expm, sqrtm, logm, lapack
rng = np.random.default_rng(11)

def spd(K, c=1.0):
    A = rng.standard_normal((K, K)); return A @ A.T + c * np.eye(K)
def sym(K):
    A = rng.standard_normal((K, K)); return 0.5 * (A + A.T)
def R(S, D):
    Sh = np.real(sqrtm(S)); Shi = np.linalg.inv(Sh); return Sh @ expm(Shi @ D @ Shi) @ Sh
def R_eig(S, D):  # 2346
    lam, V = np.linalg.eigh(S); X = V * np.sqrt(lam); Xi = (V / np.sqrt(lam)).T
    return X @ expm(Xi @ D @ Xi.T) @ X.T
def rel(a, b): return np.linalg.norm(a - b) / np.linalg.norm(b)

print("float64 identities, K in {2,3,5}, 20 draws each (max residual):")
res = {k: 0.0 for k in ["eig form (2346) = sqrtm form (2339)", "min eig of R(Sigma,Delta) > 0",
       "equivariance R_{A S A^T}(A D A^T) = A R_S(D) A^T (2342)", "R_S(0)=S", "DR_S(0)=id (FD, h=1e-6)",
       "R_S(Log_S(S1)) = S1 (Riemannian exp, 2349)", "natural grad: 1/2 tr(S^-1 N S^-1 H) = tr(G H) for N=2SGS (2629)",
       "gauge law grad -> g^-T grad g^-1 (2325)", "gauge law nat grad -> g nat g^T (2326)"]}
mins = []
for K in (2, 3, 5):
    for _ in range(20):
        S, S1, D, A = spd(K, 0.2), spd(K, 0.2), 3 * sym(K), rng.standard_normal((K, K))
        res["eig form (2346) = sqrtm form (2339)"] = max(res["eig form (2346) = sqrtm form (2339)"], rel(R_eig(S, D), R(S, D)))
        mins.append(np.linalg.eigvalsh(R(S, D)).min())
        res["equivariance R_{A S A^T}(A D A^T) = A R_S(D) A^T (2342)"] = max(res["equivariance R_{A S A^T}(A D A^T) = A R_S(D) A^T (2342)"], rel(R(A @ S @ A.T, A @ D @ A.T), A @ R(S, D) @ A.T))
        res["R_S(0)=S"] = max(res["R_S(0)=S"], rel(R(S, 0 * D), S))
        h = 1e-6
        res["DR_S(0)=id (FD, h=1e-6)"] = max(res["DR_S(0)=id (FD, h=1e-6)"], rel((R(S, h * D) - R(S, -h * D)) / (2 * h), D))
        Sh = np.real(sqrtm(S)); Shi = np.linalg.inv(Sh); Log = Sh @ np.real(logm(Shi @ S1 @ Shi)) @ Sh
        res["R_S(Log_S(S1)) = S1 (Riemannian exp, 2349)"] = max(res["R_S(Log_S(S1)) = S1 (Riemannian exp, 2349)"], rel(R(S, Log), S1))
        G, Hs = sym(K), sym(K); Nat = 2 * S @ G @ S; Si = np.linalg.inv(S)
        res["natural grad: 1/2 tr(S^-1 N S^-1 H) = tr(G H) for N=2SGS (2629)"] = max(res["natural grad: 1/2 tr(S^-1 N S^-1 H) = tr(G H) for N=2SGS (2629)"], abs(0.5 * np.trace(Si @ Nat @ Si @ Hs) - np.trace(G @ Hs)) / abs(np.trace(G @ Hs)))
        # gauge law: F(S) = KL(N(0,S)||N(0,P)); F'(S') with S'=gSg^T, P'=gPg^T
        P = spd(K); g = rng.standard_normal((K, K))
        gradF = lambda S_, P_: 0.5 * (-np.linalg.inv(S_) + np.linalg.inv(P_))
        G0 = gradF(S, P); G1 = gradF(g @ S @ g.T, g @ P @ g.T); gi = np.linalg.inv(g)
        res["gauge law grad -> g^-T grad g^-1 (2325)"] = max(res["gauge law grad -> g^-T grad g^-1 (2325)"], rel(G1, gi.T @ G0 @ gi))
        res["gauge law nat grad -> g nat g^T (2326)"] = max(res["gauge law nat grad -> g nat g^T (2326)"], rel(2 * (g @ S @ g.T) @ G1 @ (g @ S @ g.T), g @ (2 * S @ G0 @ S) @ g.T))
res["min eig of R(Sigma,Delta) > 0"] = min(mins)
for k, v in res.items(): print(f"  {v:.2e}  {k}")

# ---------------- fp32: storage vs compute, eigh vs Cholesky ----------------
print("\nfp32 positive-definiteness onset (2510). u32 = 2^-24 = %.3e, 1/u32 = %.4e" % (2.0**-24, 2.0**24))
def rot(K):
    Q, _ = np.linalg.qr(rng.standard_normal((K, K))); return Q
K = 8; trials = 200
print(f"K={K}, {trials} random rotations per kappa; spectrum logspaced in [1/kappa, 1]")
print("   kappa   | stored fp32 matrix indefinite | fp32 eigh min<=0 | fp32 Cholesky (spotrf) fails | diag Sigma: eigh / chol fail")
for kap in (1e5, 1e6, 3e6, 1e7, 3e7, 1e8, 1e9, 1e12):
    st = ei = ch = 0
    lam = np.logspace(0, -np.log10(kap), K)
    for _ in range(trials):
        Q = rot(K); S64 = (Q * lam) @ Q.T; S32 = S64.astype(np.float32); S32 = 0.5 * (S32 + S32.T)
        st += np.linalg.eigvalsh(S32.astype(np.float64)).min() <= 0          # storage: exact-ish eig of the rounded matrix
        ei += np.linalg.eigvalsh(S32).min() <= 0                             # compute: fp32 LAPACK ssyevd
        c, info = lapack.spotrf(S32, lower=1); ch += info != 0
    D32 = np.diag(lam).astype(np.float32)
    de = np.linalg.eigvalsh(D32).min() <= 0; c, info = lapack.spotrf(D32, lower=1)
    print(f"  {kap:8.0e} | {st/trials:28.3f} | {ei/trials:16.3f} | {ch/trials:28.3f} | {int(de)} / {int(info != 0)}")
# Higham Thm 10.7-style scaled criterion: kappa of H = D^-1 S D^-1 matters, not kappa(S)
lam = np.array([1.0, 1e-12]); c, info = lapack.spotrf(np.diag(lam).astype(np.float32), lower=1)
print(f"\ndiag(1,1e-12) in fp32: kappa(Sigma)=1e12 > 1/u32, spotrf info={info}, L diag = {np.diag(c)}")
# badly scaled but well-correlated: Sigma = D C D with C a correlation matrix of kappa ~ 10
C = np.array([[1, .5, .2], [.5, 1, .3], [.2, .3, 1.]]); Dg = np.diag([1, 1e-4, 1e-8]); S = Dg @ C @ Dg
c, info = lapack.spotrf(S.astype(np.float32), lower=1)
print(f"D C D with kappa(Sigma)={np.linalg.cond(S):.2e}, kappa(C)={np.linalg.cond(C):.2f}: fp32 spotrf info={info}; rel fwd err of L vs float64 = {np.linalg.norm(np.tril(c)-np.linalg.cholesky(S))/np.linalg.norm(np.linalg.cholesky(S)):.2e}")
# backward error of fp32 Cholesky is kappa-independent (Higham Thm 10.3); forward error is not
print("fp32 Cholesky normwise backward error ||S - L L^T||/||S|| vs kappa (rotated spectra, K=8):")
for kap in (1e1, 1e3, 1e5, 1e6):
    be = []
    for _ in range(50):
        Q = rot(K); lam = np.logspace(0, -np.log10(kap), K); S32 = ((Q * lam) @ Q.T).astype(np.float32); S32 = 0.5*(S32+S32.T)
        c, info = lapack.spotrf(S32, lower=1); L = np.tril(c).astype(np.float64)
        be.append(np.linalg.norm(S32.astype(np.float64) - L @ L.T) / np.linalg.norm(S32.astype(np.float64)))
    print(f"   kappa={kap:7.0e}: median backward error {np.median(be):.2e}, max {np.max(be):.2e}")
