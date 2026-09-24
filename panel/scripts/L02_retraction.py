r"""L02: SPD retraction / exponential map, natural gradient, BCH, and the frame pullback metric.

PIFB2.tex 2322-2349 (SPD retraction), 2629-2635 (natural gradient), 2651 (BCH), 981-1004 (G_pull).
"""
import numpy as np
from scipy.linalg import expm, logm, sqrtm, eigh
rng = np.random.default_rng(2)
K = 4
eps = np.finfo(float).eps

def spd(K, cond=30.0):
    Q, _ = np.linalg.qr(rng.standard_normal((K, K)))
    return Q@np.diag(np.geomspace(1, cond, K))@Q.T
def sym(K):
    A = rng.standard_normal((K, K)); return (A+A.T)/2
def msqrt(S):
    w, V = eigh(S); return V@np.diag(np.sqrt(w))@V.T
def minvsqrt(S):
    w, V = eigh(S); return V@np.diag(1/np.sqrt(w))@V.T
def R(S, D):
    Sh = msqrt(S); Si = minvsqrt(S)
    M = Si@D@Si; M = (M+M.T)/2
    return Sh@expm(M)@Sh
def R_eig(S, D):
    w, V = eigh(S); sL = np.diag(np.sqrt(w)); isL = np.diag(1/np.sqrt(w))
    M = isL@V.T@D@V@isL; M = (M+M.T)/2
    return V@sL@expm(M)@sL@V.T
def Log(S, P):
    Sh = msqrt(S); Si = minvsqrt(S)
    M = Si@P@Si; M = (M+M.T)/2
    return Sh@np.real(logm(M))@Sh
def dist(A, B):
    w = eigh(B, A, eigvals_only=True)
    return np.sqrt(np.sum(np.log(w)**2))
def normS(S, D):  # AIRM norm without the 1/2
    Si = np.linalg.inv(S); return np.sqrt(np.trace(Si@D@Si@D))

S = spd(K); D = sym(K)
print("(1) SPD preservation for large steps: min eigenvalue of R_S(t D)")
for t in [1, 10, 50]:
    print(f"    t={t:3d}: lambda_min = {np.linalg.eigvalsh(R(S, t*D)).min():.3e}")
print(f"    additive step S + 50 D: lambda_min = {np.linalg.eigvalsh(S+50*D).min():.3e}  (contrast)")
print(f"(2) R_S(0) = S: {np.linalg.norm(R(S, 0*D)-S)/np.linalg.norm(S):.2e}")
h = 1e-6
dR = (R(S, h*D)-R(S, -h*D))/(2*h)
print(f"    dR_S(0)[D] = D: rel.err {np.linalg.norm(dR-D)/np.linalg.norm(D):.2e} (central FD, h=1e-6)")
print(f"(3) eigen form vs sqrt form: {np.linalg.norm(R(S,D)-R_eig(S,D))/np.linalg.norm(R(S,D)):.2e}")
A = rng.standard_normal((K, K))
lhs = R(A@S@A.T, A@D@A.T); rhs = A@R(S, D)@A.T
print(f"(4) congruence equivariance R_(ASA^T)(ADA^T) = A R_S(D) A^T: rel.err {np.linalg.norm(lhs-rhs)/np.linalg.norm(rhs):.2e}")
print("(5) geodesic property: d(S, R_S(tD)) / (t ||D||_S) for AIRM tr(S^-1 D S^-1 D):")
for t in [0.3, 1.0, 3.0]:
    print(f"    t={t}: ratio = {dist(S, R(S, t*D))/(t*normS(S, D)):.12f}")
P = R(S, D)
print(f"(6) log round trip ||Log_S(Exp_S(D)) - D||/||D|| = {np.linalg.norm(Log(S, P)-D)/np.linalg.norm(D):.2e}  (eps={eps:.1e}, cond(S)=30)")
# congruence isometry of AIRM distance
B = spd(K, 10); G = rng.standard_normal((K, K))
print(f"(7) AIRM congruence isometry |d(GSG^T,GBG^T)-d(S,B)|/d = {abs(dist(G@S@G.T, G@B@G.T)-dist(S, B))/dist(S, B):.2e}")

# (8) natural gradient: for f(S), Riemannian gradient under (1/2)tr metric is 2 S grad S
Lam = spd(K, 5); f = lambda X: np.trace(Lam@X) - np.log(np.linalg.det(X))
egrad = Lam - np.linalg.inv(S)  # symmetric Euclidean gradient
V = sym(K); df = (f(S+h*V)-f(S-h*V))/(2*h)
Si = np.linalg.inv(S)
for c, name in [(2.0, "2 S grad S with g=(1/2)tr"), (1.0, "1 S grad S with g=(1/2)tr")]:
    rg = c*S@egrad@S
    val = 0.5*np.trace(Si@rg@Si@V)
    print(f"(8) {name}: g(rgrad,V) - df[V] = {val-df:+.2e} (df={df:.3f})")
rg1 = S@egrad@S
print(f"    S grad S with g=tr (no 1/2): g(rgrad,V) - df[V] = {np.trace(Si@rg1@Si@V)-df:+.2e}")

# (9) BCH first correction
for s in [0.1, 0.03, 0.01]:
    X = s*rng.standard_normal((K, K)); Y = s*rng.standard_normal((K, K))
    exact = np.real(logm(expm(X)@expm(-Y)))
    first = X - Y; second = X - Y - 0.5*(X@Y-Y@X)
    print(f"(9) |phi|~{s}: ||log(e^X e^-Y) - (X-Y)|| = {np.linalg.norm(exact-first):.2e}, with -1/2[X,Y]: {np.linalg.norm(exact-second):.2e}")

# (10) G_pull: pullback of flat Frobenius metric through exp; invariance under right translation U -> U g
basis = []
for i in range(3):
    for j in range(3):
        E = np.zeros((3, 3)); E[i, j] = 1; basis.append(E)
def Dexp(phi, H, h=1e-6):
    return (expm(phi+h*H)-expm(phi-h*H))/(2*h)
phi = 0.4*rng.standard_normal((3, 3)); phidot = rng.standard_normal((3, 3))
U = expm(phi); Udot = Dexp(phi, phidot)
g = rng.standard_normal((3, 3)) + 2*np.eye(3)
kin = np.sum(Udot**2); kin_g = np.sum((Udot@g)**2)
print(f"(10) ambient Frobenius kinetic ||Udot||^2 = {kin:.4f}; after right translation U->Ug: ||Udot g||^2 = {kin_g:.4f} (ratio {kin_g/kin:.3f})")
Qo, _ = np.linalg.qr(rng.standard_normal((3, 3)))
print(f"     orthogonal g: ratio {np.sum((Udot@Qo)**2)/kin:.12f}")
# (11) G_pull positive definite away from 2 pi i Z locus; singular on it
J = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 0.]])
for th in [1.0, 2*np.pi - 1e-3, 2*np.pi]:
    ph = th*J
    M = np.array([Dexp(ph, E).ravel() for E in basis])
    Gp = M@M.T
    print(f"(11) phi = {th:.4f} J: min eig G_pull = {np.linalg.eigvalsh(Gp).min():.3e}")
