r"""L06 checks on the coarse-graining map R_s of App. I (PIFB2.tex ~3750-3815, 3866-3880).

(a) Equivariance of the SO(3) Karcher mean under left multiplication (thm:rg_covariance).
(b) Two-stage Karcher mean != one-stage Karcher mean with product weights (no blocking semigroup
    R_{b'} o R_b = R_{bb'} in the frame sector), while two-stage M-projection moment matching
    with a common final frame equals one-stage (mixture of mixtures).
(c) With pure-gauge transport Omega_ij = U_i U_j^{-1} (the appendix's state space), the
    parent-coordinate edges Theta_ij^{IJ} = Omega_Ii Omega_ij Omega_jJ all coincide, so H_IJ = 0.
(d) SO(3) sectional curvature bound and injectivity radius for d^2 = ||log(U^T V)||_F^2.
"""
import numpy as np
from scipy.linalg import expm

rng = np.random.default_rng(2)

def hat(v):
    return np.array([[0, -v[2], v[1]], [v[2], 0, -v[0]], [-v[1], v[0], 0]])

def so3log(R):
    c = np.clip((np.trace(R) - 1) / 2, -1, 1)
    th = np.arccos(c)
    if th < 1e-12:
        return 0.5 * (R - R.T)
    return th / (2 * np.sin(th)) * (R - R.T)

def logm(R):
    return so3log(R)

def rand_near(R0, s):
    return R0 @ expm(hat(rng.normal(size=3) * s))

def karcher(Rs, w, iters=200):
    M = Rs[0].copy()
    for _ in range(iters):
        X = sum(wi * np.real(logm(M.T @ R)) for wi, R in zip(w, Rs))
        M = M @ expm(X)
        if np.linalg.norm(X) < 1e-15:
            break
    return M

R0 = expm(hat(rng.normal(size=3)))
Rs = [rand_near(R0, 0.5) for _ in range(6)]
w = np.full(6, 1 / 6)

# (a)
h = expm(hat(rng.normal(size=3)))
M = karcher(Rs, w)
Mh = karcher([h @ R for R in Rs], w)
print("(a) ||Karcher(h R) - h Karcher(R)|| = %.2e" % np.linalg.norm(Mh - h @ M))

# (b) frames
groups = [[0, 1, 2], [3, 4, 5]]
M1 = [karcher([Rs[i] for i in g], np.full(3, 1 / 3)) for g in groups]
M2 = karcher(M1, np.array([0.5, 0.5]))
d = np.linalg.norm(np.real(logm(M2.T @ M)))
print("(b) geodesic distance between two-stage and one-stage Karcher means = %.3e (nonzero: no semigroup)" % d)

# (b) beliefs: given frames, two-stage moment matching vs one-stage
K = 3
mus = [rng.normal(size=K) for _ in range(6)]
Sig = []
for _ in range(6):
    A = rng.normal(size=(K, K)); Sig.append(A @ A.T + np.eye(K))
Uc = [expm(hat(rng.normal(size=3))) for _ in range(6)]  # child frames
UI = [expm(hat(rng.normal(size=3))) for _ in range(2)]
UII = expm(hat(rng.normal(size=3)))

def mproj(mus_t, Sig_t, ww):
    m = sum(wi * mi for wi, mi in zip(ww, mus_t))
    S = sum(wi * (Si + np.outer(mi - m, mi - m)) for wi, mi, Si in zip(ww, mus_t, Sig_t))
    return m, S

par = []
for gI, g in enumerate(groups):
    mt = [UI[gI] @ Uc[i].T @ mus[i] for i in g]
    St = [UI[gI] @ Uc[i].T @ Sig[i] @ Uc[i] @ UI[gI].T for i in g]
    par.append(mproj(mt, St, np.full(3, 1 / 3)))
mt2 = [UII @ UI[k].T @ par[k][0] for k in range(2)]
St2 = [UII @ UI[k].T @ par[k][1] @ UI[k] @ UII.T for k in range(2)]
m2, S2 = mproj(mt2, St2, [0.5, 0.5])
mt1 = [UII @ Uc[i].T @ mus[i] for i in range(6)]
St1 = [UII @ Uc[i].T @ Sig[i] @ Uc[i] @ UII.T for i in range(6)]
m1, S1 = mproj(mt1, St1, np.full(6, 1 / 6))
print("(b) belief moments, two-stage vs one-stage (common final frame): |dmu|=%.2e |dSigma|=%.2e"
      % (np.linalg.norm(m2 - m1), np.linalg.norm(S2 - S1)))

# (c)
U = [expm(hat(rng.normal(size=3))) @ np.diag([1, 1, 1]) for _ in range(6)]
UIc = [expm(hat(rng.normal(size=3))) for _ in range(2)]
Om = lambda A, B: A @ np.linalg.inv(B)
Thetas = [Om(UIc[0], U[i]) @ Om(U[i], U[j]) @ Om(U[j], UIc[1]) for i in groups[0] for j in groups[1]]
spread = max(np.linalg.norm(T - Thetas[0]) for T in Thetas)
print("(c) pure-gauge transport: max spread of Theta_ij^{IJ} = %.2e  => H_IJ = 0 identically" % spread)

# (d) sectional curvature of bi-invariant metric <X,Y> = tr(X^T Y) on so(3): K = 1/4 |[X,Y]|^2/(|X|^2|Y|^2 - <X,Y>^2)
ip = lambda X, Y: np.trace(X.T @ Y)
Kmax = 0
for _ in range(20000):
    X, Y = hat(rng.normal(size=3)), hat(rng.normal(size=3))
    br = X @ Y - Y @ X
    den = ip(X, X) * ip(Y, Y) - ip(X, Y) ** 2
    Kmax = max(Kmax, 0.25 * ip(br, br) / den)
print("(d) max sectional curvature (Frobenius bi-invariant metric on SO(3)) = %.6f (exact 1/8 = 0.125)" % Kmax)
print("(d) injectivity radius = ||log R||_F at angle pi = %.6f = sqrt(2) pi" % (np.sqrt(2) * np.pi))
rcx = 0.5 * min(np.sqrt(2) * np.pi, np.pi / np.sqrt(0.125))
print("(d) Afsari radius 1/2 min(inj, pi/sqrt(Delta)) = %.6f, i.e. rotation angle < %.6f rad (pi/2 = %.6f)"
      % (rcx, rcx / np.sqrt(2), np.pi / 2))
