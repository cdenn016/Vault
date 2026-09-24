r"""L10: frame-sector update of PIFB2 2497-2499 (zeta = G_pull^{-1} grad_phi F, xi = dexp^L(zeta)),
eq:pullback_metric (972-990), the telescoping claim xi = U^{-1} grad_U F, conditioning, and cost.

J(phi): gl(K) -> gl(K), J[H] = Dexp_phi[H] (K^2 x K^2 matrix). G_pull = J^T J (Frobenius pullback).
If grad_phi F = J^T grad_U F then zeta = G^{-1} J^T grad_U F = J^{-1} grad_U F and xi = U^{-1} J zeta = U^{-1} grad_U F.
"""
import numpy as np, time
from scipy.linalg import expm, expm_frechet
rng = np.random.default_rng(3)

def basis(K):
    out = []
    for a in range(K):
        for b in range(K):
            E = np.zeros((K, K)); E[a, b] = 1; out.append(E)
    return out
def Jmat(phi):
    K = phi.shape[0]; return np.column_stack([expm_frechet(phi, T, compute_expm=False).ravel() for T in basis(K)])
def Psi_R_ad(phi, Hm):  # Psi_R(ad_phi)(H), Psi_R(z) = (e^z - 1)/z, via block exponential of ad_phi
    K = phi.shape[0]; I = np.eye(K); ad = np.kron(phi, I) - np.kron(I, phi.T)  # row-major vec: vec(phi H - H phi)
    n = K * K; M = np.zeros((2 * n, 2 * n)); M[:n, :n] = ad; M[:n, n:] = np.eye(n)
    return (expm(M)[:n, n:] @ Hm.ravel()).reshape(K, K)

print("formula checks (K=3, 10 draws, |phi|_F ~ 2):")
m1 = m2 = m3 = 0
for _ in range(10):
    K = 3; phi = rng.standard_normal((K, K)) * 2 / 3; U = expm(phi)
    J = Jmat(phi); G = J.T @ J
    Gform = np.array([[np.trace(Psi_R_ad(phi, Ta).T @ Psi_R_ad(phi, Tb) @ U @ U.T) for Tb in basis(K)] for Ta in basis(K)])
    m1 = max(m1, np.linalg.norm(G - Gform) / np.linalg.norm(G))
    Hm = rng.standard_normal((K, K))
    m2 = max(m2, np.linalg.norm(Psi_R_ad(phi, Hm) @ U - expm_frechet(phi, Hm, compute_expm=False)) / np.linalg.norm(Hm))
    gU = rng.standard_normal((K, K)); gphi = J.T @ gU.ravel()
    zeta = np.linalg.solve(G, gphi); xi = np.linalg.solve(U, (J @ zeta).reshape(K, K))
    m3 = max(m3, np.linalg.norm(xi - np.linalg.solve(U, gU)) / np.linalg.norm(np.linalg.solve(U, gU)))
print(f"  eq:pullback_metric Psi_R form vs J^T J: {m1:.2e}\n  Dexp_phi[H] = Psi_R(ad_phi)(H) e^phi: {m2:.2e}\n  telescoping xi = U^-1 grad_U F: {m3:.2e}")

print("\nconditioning and fp32 accuracy of the two routes to xi (K=3, 30 draws per scale; float64 reference = U^{-1} grad_U):")
print(" |phi|_F  median cond(U)  median cond(J)  median cond(G_pull)  | fp32 rel err: G_pull route (median/max)  direct U^-1 grad_U (median/max)")
for sc in (0.3, 1.0, 2.0, 3.0, 4.0, 5.0):
    cu, cj, cg, e1, e2 = [], [], [], [], []
    for _ in range(30):
        K = 3; phi = rng.standard_normal((K, K)); phi *= sc / np.linalg.norm(phi); U = expm(phi)
        J = Jmat(phi); G = J.T @ J; gU = rng.standard_normal((K, K))
        ref = np.linalg.solve(U, gU)
        f = np.float32; J32, U32, g32 = J.astype(f), U.astype(f), gU.astype(f)
        gphi32 = J32.T @ g32.ravel(); G32 = J32.T @ J32
        zeta = np.linalg.solve(G32, gphi32); xi1 = np.linalg.solve(U32, (J32 @ zeta).reshape(K, K))
        xi2 = np.linalg.solve(U32, g32)
        cu.append(np.linalg.cond(U)); cj.append(np.linalg.cond(J)); cg.append(np.linalg.cond(G))
        e1.append(np.linalg.norm(xi1 - ref) / np.linalg.norm(ref)); e2.append(np.linalg.norm(xi2 - ref) / np.linalg.norm(ref))
    print(f"  {sc:4.1f}   {np.median(cu):11.3e}   {np.median(cj):12.3e}   {np.median(cg):16.3e}    |  {np.median(e1):.2e} / {np.max(e1):.2e}                    {np.median(e2):.2e} / {np.max(e2):.2e}")

print("\napproach to the dexp-singular locus (Prop. dexp_regularity): phi = theta * so(2) generator in gl(3)")
Gz = np.zeros((3, 3)); Gz[0, 1] = -1; Gz[1, 0] = 1
for th in (3.0, 3.1, np.pi - 1e-4, np.pi, 4.0, 6.28, 2 * np.pi - 1e-4):
    phi = th * Gz; U = expm(phi); J = Jmat(phi)
    print(f"  theta={th:.5f}: cond(J)={np.linalg.cond(J):.3e} cond(G_pull)={np.linalg.cond(J.T@J):.3e} cond(U)={np.linalg.cond(U):.3f}")

print("\ncost per agent (float64, wall time of forming+solving G_pull vs direct solve):")
for K in (4, 8, 12, 16):
    phi = rng.standard_normal((K, K)) * 0.3; gU = rng.standard_normal((K, K)); U = expm(phi)
    t0 = time.perf_counter(); J = Jmat(phi); G = J.T @ J; zeta = np.linalg.solve(G, J.T @ gU.ravel()); xi1 = np.linalg.solve(U, (J @ zeta).reshape(K, K)); t1 = time.perf_counter()
    xi2 = np.linalg.solve(U, gU); t2 = time.perf_counter()
    print(f"  K={K:2d}: G_pull route {t1-t0:.3e} s (G is {K*K}x{K*K}), direct {t2-t1:.3e} s, agree to {np.linalg.norm(xi1-xi2)/np.linalg.norm(xi2):.1e}")

print("\nchart update exp(phi - eta v) vs group retraction U exp(-eta dexp^L(v)) at large phi (2502 / 995):")
K = 3; phi = rng.standard_normal((K, K)); phi *= 3 / np.linalg.norm(phi); U = expm(phi); v = rng.standard_normal((K, K))
xiL = np.linalg.solve(U, expm_frechet(phi, v, compute_expm=False))
for eta in (1e-1, 1e-2, 1e-3):
    d = np.linalg.norm(expm(phi - eta * v) - U @ expm(-eta * xiL))
    print(f"  eta={eta:.0e}: |difference| = {d:.3e}, /eta^2 = {d/eta**2:.3f}")
