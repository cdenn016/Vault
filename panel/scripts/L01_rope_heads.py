"""L01: RoPE relative-position identity as flat abelian transport; one-parameter subgroups of GL(d);
stabilizer of a learned bilinear M (residual symmetry of route R3); multi-head block structure. PIFB2.tex 1086-1133, 1210, 1266-1280."""
import numpy as np
from scipy.linalg import expm, null_space
rng = np.random.default_rng(2)
inv = np.linalg.inv
d = 4
def R(m, thetas):
    B = np.zeros((d, d))
    for n, th in enumerate(thetas):
        c, s = np.cos(m * th), np.sin(m * th); B[2*n:2*n+2, 2*n:2*n+2] = [[c, -s], [s, c]]
    return B
th = [1.0, 10000 ** (-2 / d)]
print("(P1) R(m)^T R(n) - R(n-m), m=3,n=7:", np.abs(R(3, th).T @ R(7, th) - R(4, th)).max())
X = rng.standard_normal((d, d))  # generic non-normal, non-skew generator
Um = lambda m: expm(m * X)
print("(P2) generic X in gl(4): U_m^-1 U_n - U_(n-m), m=2,n=5:", np.abs(inv(Um(2)) @ Um(5) - Um(3)).max(), " ; |[X,X^T]|:", np.abs(X @ X.T - X.T @ X).max())
print("     and for (m,n)=(0,3) vs (4,7) the kernels agree:", np.abs(inv(Um(0)) @ Um(3) - inv(Um(4)) @ Um(7)).max())
phi = lambda m: np.sqrt(m + 1.0)  # abelian SO(2) but nonlinear in position
Rn = lambda m: np.array([[np.cos(phi(m)), -np.sin(phi(m))], [np.sin(phi(m)), np.cos(phi(m))]])
print("(P3) abelian SO(2) with nonlinear phase: kernel(0,3) vs kernel(4,7):", np.abs(Rn(0).T @ Rn(3) - Rn(4).T @ Rn(7)).max())
Y, Z = rng.standard_normal((d, d)), rng.standard_normal((d, d))
U2d = lambda a, b: expm(a * Y + b * Z)
print("(P4) 2D positions with noncommuting generators: kernel((0,0),(1,1)) vs ((2,1),(3,2)):", np.abs(inv(U2d(0, 0)) @ U2d(1, 1) - inv(U2d(2, 1)) @ U2d(3, 2)).max())
for k in (2, 3, 4, 6):
    M = rng.standard_normal((k, k))
    rows = []
    for a in range(k):
        for b in range(k):
            E = np.zeros((k, k)); E[a, b] = 1; rows.append((E.T @ M + M @ E).ravel())
    A = np.array(rows).T
    ns = null_space(A).shape[1]
    S = M + M.T; rowsS = []
    for a in range(k):
        for b in range(k):
            E = np.zeros((k, k)); E[a, b] = 1; rowsS.append((E.T @ S + S @ E).ravel())
    nsS = null_space(np.array(rowsS).T).shape[1]
    print("(P5) k=%d: dim gl(k)=%d ; dim stab of generic M (X^T M + M X = 0) = %d ; dim stab of sym part = %d ; so(k) dim = %d" % (k, k*k, ns, nsS, k*(k-1)//2))
dm, H, dh = 6, 2, 3
WQ = rng.standard_normal((dm, dh)); WK = rng.standard_normal((dm, dh))
print("(P6) Vaswani per-head W_Q (d_model x d_head) row-support: nonzero rows =", int((np.abs(WQ).sum(1) > 0).sum()), "of", dm, "(reads all embedding coordinates, no block partition)")
