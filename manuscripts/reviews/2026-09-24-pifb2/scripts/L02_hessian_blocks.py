r"""L02: frozen-beta Hessian blocks of PIFB2 Sec. 'Statistical Precision as Configuration-Space Stiffness'
(lines 1400-1532), two agents, K=2, general GL(2) transport, reciprocal consensus.
Also: coordinate (in)dependence of the coordinate Hessian at non-critical points (kinetic-metric postulate),
and the alpha* rank-one PD thresholds at line 1512.
"""
import numpy as np
from scipy.linalg import expm
rng = np.random.default_rng(3)
K = 2
def spd(): A = rng.standard_normal((K, K)); return A@A.T + 0.5*np.eye(K)
def sym(): A = rng.standard_normal((K, K)); return (A+A.T)/2
def kl(m1, S1, m2, S2):
    S2i = np.linalg.inv(S2); d = m2-m1
    return 0.5*(np.log(np.linalg.det(S2)/np.linalg.det(S1)) + np.trace(S2i@S1) + d@S2i@d - K)
U1 = expm(0.6*rng.standard_normal((K, K))); U2 = expm(0.6*rng.standard_normal((K, K)))
O12 = U1@np.linalg.inv(U2); O21 = np.linalg.inv(O12)
b12, b21 = 0.7, 0.4
m2 = rng.standard_normal(K); S2 = spd()
m1 = O12@m2; S1 = O12@S2@O12.T          # consensus
mp1, Sp1, mp2, Sp2 = rng.standard_normal(K), spd(), rng.standard_normal(K), spd()
Lo1, Lo2 = spd(), spd(); o1, o2 = rng.standard_normal(K), rng.standard_normal(K)
def F(m1, S1, m2, S2):
    val = kl(m1, S1, mp1, Sp1) + kl(m2, S2, mp2, Sp2)
    val += b12*kl(m1, S1, O12@m2, O12@S2@O12.T) + b21*kl(m2, S2, O21@m1, O21@S1@O21.T)
    val += 0.5*(o1-m1)@Lo1@(o1-m1) + 0.5*np.trace(Lo1@S1) + 0.5*(o2-m2)@Lo2@(o2-m2) + 0.5*np.trace(Lo2@S2)
    return val
x0 = [m1, S1, m2, S2]
def d2(dirA, dirB, h=1e-4):
    def ev(sa, sb):
        x = [x0[k] + sa*dirA[k] + sb*dirB[k] for k in range(4)]
        return F(*x)
    return (ev(h, h) - ev(h, -h) - ev(-h, h) + ev(-h, -h))/(4*h*h)
Z = lambda: [np.zeros(K), np.zeros((K, K)), np.zeros(K), np.zeros((K, K))]
L1, L2 = np.linalg.inv(S1), np.linalg.inv(S2); Lp1 = np.linalg.inv(Sp1)
Lt2 = np.linalg.inv(O12@S2@O12.T)
# mean diag block
M11 = Lp1 + b12*Lt2 + b21*L1 + Lo1
M12 = -b12*np.linalg.inv(O12).T@L2 - b21*L1@np.linalg.inv(O21)
num11 = np.zeros((K, K)); num12 = np.zeros((K, K))
for a in range(K):
    for b in range(K):
        da = Z(); da[0][a] = 1; db = Z(); db[0][b] = 1; num11[a, b] = d2(da, db)
        db2 = Z(); db2[2][b] = 1; num12[a, b] = d2(da, db2)
print(f"[M_mumu]_11 boxed vs FD: rel.err {np.linalg.norm(num11-M11)/np.linalg.norm(M11):.2e}")
print(f"[M_mumu]_12 boxed vs FD: rel.err {np.linalg.norm(num12-M12)/np.linalg.norm(M12):.2e}")
# covariance diag block at consensus
V, W = sym(), sym()
dV = Z(); dV[1] = V; dW = Z(); dW[1] = W
box = 0.5*(1+b12+b21)*np.trace(L1@V@L1@W)
fd = d2(dV, dW)
print(f"[M_SS]_11[V,W] at consensus: boxed {box:.6f}, FD {fd:.6f}, rel.err {abs(box-fd)/abs(box):.2e}")
# covariance off-diag block
dW2 = Z(); dW2[3] = W
A = np.linalg.inv(O12).T@L2; B = np.linalg.inv(O21).T@L1
box12 = -0.5*b12*np.trace(A@W@A.T@V) - 0.5*b21*np.trace(B@V@B.T@W)
fd12 = d2(dV, dW2)
vecbox = -0.5*b12*V.ravel(order='F')@np.kron(A, A)@W.ravel(order='F') - 0.5*b21*V.ravel(order='F')@np.kron(B, B).T@W.ravel(order='F')
print(f"[M_SS]_12[V,W]: bilinear {box12:.6f}, Kronecker form of Eq. (mass_sigma_offdiagonal) {vecbox:.6f}, FD {fd12:.6f}, rel.err {abs(box12-fd12)/abs(box12):.2e}")
# cross block at consensus
dm = Z(); dm[0] = rng.standard_normal(K)
print(f"[C^muSigma]_12 at consensus (FD): {d2(dm, dW2):.2e};  [C]_11: {d2(dm, dV):.2e}")

# Coordinate dependence of the coordinate Hessian away from critical points.
# single covariance variable, f(S) = KL(N(0,S)||N(0,Sp)) + 1/2 tr(Lo S); compare Hessian in S-coords with
# Hessian in Lambda = S^{-1} coords pushed back by the Jacobian.
Sp = spd(); Lo = spd()
f = lambda S: kl(np.zeros(K), S, np.zeros(K), Sp) + 0.5*np.trace(Lo@S)
Scrit = np.linalg.inv(np.linalg.inv(Sp) + Lo)
def compare(S0, h=1e-4):
    V, W = sym(), sym()
    HS = (f(S0+h*V+h*W) - f(S0+h*V-h*W) - f(S0-h*V+h*W) + f(S0-h*V-h*W))/(4*h*h)
    L0 = np.linalg.inv(S0)
    # tangent vectors in Lambda coords corresponding to V, W: dLambda = -L V L
    a, b = -L0@V@L0, -L0@W@L0
    g = lambda L: f(np.linalg.inv(L))
    HL = (g(L0+h*a+h*b) - g(L0+h*a-h*b) - g(L0-h*a+h*b) + g(L0-h*a-h*b))/(4*h*h)
    return HS, HL
for name, S0 in [("critical point", Scrit), ("non-critical point", spd())]:
    HS, HL = compare(S0)
    print(f"coordinate Hessian at {name}: Sigma-chart {HS:.6f}, Lambda-chart {HL:.6f}, rel.diff {abs(HS-HL)/abs(HS):.2e}")

# alpha* rank-one thresholds (line 1512): along Delta direction, D = 1/2 Delta^T Lp Delta
c0, b0 = 1.0, 0.8
for D in [0.2, b0/3, 0.5, b0, 1.0]:
    a = c0/(b0+D)
    # quadratic form along Delta, normalized by Delta^T Lp Delta = 2D: regularized (c0 log(b0+D)) and unregularized (alpha* D)
    reg = a - a*a/c0*2*D
    unreg = c0*b0/(b0+D)**2 - 2*c0*b0/(b0+D)**3*2*D
    print(f"D={D:.3f}: log-barrier curvature {reg:+.4f}, c0 D/(b0+D) curvature {unreg:+.4f}")
