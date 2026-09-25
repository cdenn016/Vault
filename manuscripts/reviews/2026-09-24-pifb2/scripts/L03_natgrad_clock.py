r"""L03: natural gradient, clock-dissipation identity, frame pullback telescoping (PIFB2.tex l.946, 965-1004, 2621-2635, 1845-1852).
(a) vech-coordinate Fisher matrix inverse applied to the vech gradient equals vech(2 Sigma G Sigma), mean block Sigma grad_mu.
(b) Clock identity (d tau/dt)^2 = eta (-dF/dt) for x' = -eta G^{-1} grad F; failure when mean and covariance blocks
    carry different rates eta_mu != eta_Sigma (eq:gauge_natural_gradient uses separate rates) and the clock is the Fisher length.
(c) Pullback telescoping l.1004: v = G_pull^{-1} grad_phi F gives Dexp_phi[v] = grad_U F, so xi = U^{-1} grad_U F
    (the frame 'natural gradient' is the ambient Euclidean gradient of U); for a proper subalgebra (so(3)) it is only the projection.
"""
import numpy as np
from scipy.linalg import expm
rng = np.random.default_rng(7)
K = 3
A = rng.normal(size=(K, K)); Sig = A@A.T + 0.5*np.eye(K); Si = np.linalg.inv(Sig)
idx = [(i, j) for i in range(K) for j in range(i, K)]
def E(i, j):
    M = np.zeros((K, K)); M[i, j] = 1; M[j, i] = 1; return M
Es = [E(i, j) for (i, j) in idx]
Fv = np.array([[0.5*np.trace(Si@Ea@Si@Eb) for Eb in Es] for Ea in Es])
# a test objective F(Sigma) = tr(C Sigma) + log det Sigma with C symmetric; symmetric gradient G = C + Sigma^{-1}
C = rng.normal(size=(K, K)); C = C + C.T
G = C + Si
grad_vech = np.array([np.trace(G@Ea) for Ea in Es])   # dF/d(vech coord)
nat_vech = np.linalg.solve(Fv, grad_vech)
# reconstruct symmetric matrix from vech coordinates: Sigma = sum_c s_c E_c with E_c having both off-diagonal slots, diag counted once
M = np.zeros((K, K))
for c, (i, j) in zip(nat_vech, idx):
    M[i, j] = c; M[j, i] = c
print(f"(a) ||vech-Fisher natural gradient - 2 Sigma G Sigma|| = {np.linalg.norm(M - 2*Sig@G@Sig):.2e} (scale {np.linalg.norm(2*Sig@G@Sig):.2f})")

# (b) clock identity on a Gaussian KL objective F(mu,Sigma)=KL(N(mu,Sigma)||N(m0,S0))
m0 = rng.normal(size=K); B = rng.normal(size=(K, K)); S0 = B@B.T + 0.5*np.eye(K); S0i = np.linalg.inv(S0)
mu = rng.normal(size=K)
g_mu = S0i@(mu - m0); g_S = 0.5*(S0i - Si)
def fisher_sq(dmu, dS): return dmu@Si@dmu + 0.5*np.trace(Si@dS@Si@dS)
for (em, es) in [(0.3, 0.3), (0.3, 0.03)]:
    dmu = -em*Sig@g_mu; dS = -es*2*Sig@g_S@Sig
    speed2 = fisher_sq(dmu, dS)
    dFdt = g_mu@dmu + np.trace(g_S@dS)
    print(f"(b) eta_mu={em}, eta_Sigma={es}: Fisher speed^2 {speed2:.6f}; eta_mu*(-dF/dt) {em*(-dFdt):.6f}; eta_Sigma*(-dF/dt) {es*(-dFdt):.6f}")
    print(f"    blockwise: mu {dmu@Si@dmu:.6f} vs {em*(-(g_mu@dmu)):.6f};  Sigma {0.5*np.trace(Si@dS@Si@dS):.6f} vs {es*(-np.trace(g_S@dS)):.6f}")

# (c) pullback telescoping
def dexp(phi, H, n=40):
    # D exp_phi[H] via block matrix exponential
    Kd = phi.shape[0]; Z = np.zeros((2*Kd, 2*Kd)); Z[:Kd, :Kd] = phi; Z[Kd:, Kd:] = phi; Z[:Kd, Kd:] = H
    return expm(Z)[:Kd, Kd:]
phi = 0.6*rng.normal(size=(K, K)); U = expm(phi)
basis = []
for i in range(K):
    for j in range(K):
        T = np.zeros((K, K)); T[i, j] = 1; basis.append(T)
J = np.stack([dexp(phi, T).ravel() for T in basis], 1)   # K^2 x K^2
Wt = rng.normal(size=(K, K))
gradU = Wt  # F(U) = <W, U>_F  => grad_U F = W
grad_phi = J.T@gradU.ravel()
Gpull = J.T@J
v = np.linalg.solve(Gpull, grad_phi)
push = (J@v).reshape(K, K)
xi = np.linalg.solve(U, push)
print(f"(c) gl(3): ||Dexp[v] - grad_U F|| = {np.linalg.norm(push-gradU):.2e}; ||xi - U^-1 grad_U F|| = {np.linalg.norm(xi - np.linalg.solve(U, gradU)):.2e}")
# check Psi_R formula: Dexp_phi[H] = Psi_R(ad_phi)(H) exp(phi), Psi_R(z)=(e^z-1)/z
import math
H = rng.normal(size=(K, K))
acc = np.zeros((K, K)); term = H.copy()
for k in range(60):
    acc = acc + term/math.factorial(k+1)
    term = phi@term - term@phi
print(f"(c) ||Psi_R(ad_phi)(H) exp(phi) - Dexp_phi[H]|| = {np.linalg.norm(acc@U - dexp(phi, H)):.2e}")
# pullback formula tr(Psi(Ta)^T Psi(Tb) U U^T) vs <Dexp Ta, Dexp Tb>_F
Ta, Tb = basis[1], basis[5]
def Psi(X):
    acc = np.zeros((K, K)); term = X.copy()
    for k in range(60):
        acc = acc + term/math.factorial(k+1); term = phi@term - term@phi
    return acc
lhs = np.trace(Psi(Ta).T@Psi(Tb)@U@U.T); rhs = np.sum(dexp(phi, Ta)*dexp(phi, Tb))
print(f"(c) eq:pullback_metric entry: trace form {lhs:.12f} vs Frobenius <Dexp Ta, Dexp Tb> {rhs:.12f}, resid {abs(lhs-rhs):.2e}")
# so(3) subalgebra: D exp not surjective onto R^{3x3}; telescoping gives only the projection
w = rng.normal(size=3)
def hat(a): return np.array([[0, -a[2], a[1]], [a[2], 0, -a[0]], [-a[1], a[0], 0]])
phs = hat(0.8*w); Us = expm(phs)
Js = np.stack([dexp(phs, hat(e)).ravel() for e in np.eye(3)], 1)  # 9 x 3
vs = np.linalg.solve(Js.T@Js, Js.T@gradU.ravel())
pushs = (Js@vs).reshape(3, 3)
print(f"(c) so(3): ||Dexp[v] - grad_U F|| = {np.linalg.norm(pushs-gradU):.3f} (nonzero: only the tangent projection; ||grad_U F|| = {np.linalg.norm(gradU):.3f})")
