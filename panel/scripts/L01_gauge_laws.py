"""L01 gauge-law checks for PIFB2.tex (lines 142-504, 2637-2652). float64 NumPy/SciPy."""
import numpy as np
from scipy.linalg import expm, logm, polar
rng = np.random.default_rng(0)
K = 3
def rnd(k=K, s=0.5): return s * rng.standard_normal((k, k))
def curve(c, A0, A1, A2):
    return expm(A0 + c * A1 + c**2 * A2)
inv = np.linalg.inv
h = 1e-6
Ai = [rnd() for _ in range(3)]; Aj = [rnd() for _ in range(3)]
c0 = 0.3
Ui = lambda c: curve(c, *Ai); Uj = lambda c: curve(c, *Aj)
d = lambda f: (f(c0 + h) - f(c0 - h)) / (2 * h)
th_i = np.linalg.solve(Ui(c0), d(Ui)); th_j = np.linalg.solve(Uj(c0), d(Uj))
Om = lambda c: Ui(c) @ inv(Uj(c))
rhs = inv(Uj(c0)) @ (np.linalg.solve(Om(c0), d(Om))) @ Uj(c0) + th_j
print("(1a) eq:theta_overlap_relation residual:", np.abs(th_i - rhs).max())
hij = lambda c: inv(Uj(c)) @ Ui(c)
H = hij(c0)
std_right = inv(H) @ th_j @ H + np.linalg.solve(H, d(hij))
print("(1b) left-MC obeys standard law A_i = h^-1 A_j h + h^-1 dh with h=U_j^-1 U_i, residual:", np.abs(th_i - std_right).max())
vt_i = d(Ui) @ inv(Ui(c0)); vt_j = d(Uj) @ inv(Uj(c0))
A_i, A_j = -vt_i, -vt_j; O = Om(c0)
std_left = O @ A_j @ inv(O) - d(Om) @ inv(O)
print("(1c) A=-dU U^-1 obeys displayed law A_i = g A_j g^-1 - dg g^-1 with g=Omega_ij, residual:", np.abs(A_i - std_left).max())
print("     displayed law with A=theta (left MC) and g=Omega, residual:", np.abs(th_i - (O @ th_j @ inv(O) - d(Om) @ inv(O))).max())
B = [rnd() for _ in range(4)]
U2 = lambda x, y: expm(B[0] + x * B[1] + y * B[2] + x * y * B[3])
x0, y0 = 0.2, -0.1
Ax = lambda x, y: np.linalg.solve(U2(x, y), (U2(x + h, y) - U2(x - h, y)) / (2 * h))
Ay = lambda x, y: np.linalg.solve(U2(x, y), (U2(x, y + h) - U2(x, y - h)) / (2 * h))
hh = 1e-4
dxAy = (Ay(x0 + hh, y0) - Ay(x0 - hh, y0)) / (2 * hh); dyAx = (Ax(x0, y0 + hh) - Ax(x0, y0 - hh)) / (2 * hh)
F = dxAy - dyAx + Ax(x0, y0) @ Ay(x0, y0) - Ay(x0, y0) @ Ax(x0, y0)
print("(2) eq:field_strength for pure gauge, max|F|:", np.abs(F).max(), " scale of dA:", np.abs(dxAy).max())
N = 4
U = [expm(rnd()) for _ in range(N)]
Omega = lambda i, j: U[i] @ inv(U[j])
res = max(np.abs(Omega(i, j) @ Omega(j, k) - Omega(i, k)).max() for i in range(N) for j in range(N) for k in range(N))
print("(3a) cocycle residual:", res, " Omega_ii-I:", max(np.abs(Omega(i, i) - np.eye(K)).max() for i in range(N)))
D = {(i, j): rnd(s=0.3) for i in range(N) for j in range(N) if i != j}
def Ore(i, j, UU=U): return UU[i] @ expm(D[(i, j)]) @ inv(UU[j])
def Hol(i, j, k, UU=U): return Ore(i, j, UU) @ Ore(j, k, UU) @ Ore(k, i, UU)
H012 = Hol(0, 1, 2)
print("(3b) eq:discrete_holonomy residual:", np.abs(H012 - U[0] @ expm(D[(0, 1)]) @ expm(D[(1, 2)]) @ expm(D[(2, 0)]) @ inv(U[0])).max())
g = [expm(rnd()) for _ in range(N)]
Ug = [g[i] @ U[i] for i in range(N)]
print("(3c) H -> g0 H g0^-1 residual:", np.abs(Hol(0, 1, 2, Ug) - g[0] @ H012 @ inv(g[0])).max(), " W invariance:", abs(np.trace(Hol(0, 1, 2, Ug)) - np.trace(H012)))
print("(3d) free delta per ordered pair: |Omega_01 Omega_10 - I| =", np.abs(Ore(0, 1) @ Ore(1, 0) - np.eye(K)).max())
print("     |H_021 - inv(H_012)| =", np.abs(Hol(0, 2, 1) - inv(H012)).max(), " W_012, W_021 =", np.trace(H012), np.trace(Hol(0, 2, 1)))
Da = {}
for i in range(N):
    for j in range(i + 1, N):
        Da[(i, j)] = rnd(s=0.4); Da[(j, i)] = -Da[(i, j)]
def L(i, j): return U[i] @ expm(Da[(i, j)]) @ inv(U[j])
def P(a, b, c): return L(a, b) @ L(b, c) @ L(c, a)
bianchi = P(0, 1, 2) @ P(0, 2, 3) @ P(0, 3, 1) @ (L(0, 1) @ P(1, 3, 2) @ L(1, 0))
print("(3e) lattice Bianchi on boundary of 3-simplex |prod - I|:", np.abs(bianchi - np.eye(K)).max(), " single plaquette |P012 - I|:", np.abs(P(0, 1, 2) - np.eye(K)).max())
Ht = np.array([[1, 1.0], [0, 1.]])
a = 1e-3; gg = np.diag([a, 1 / a])
print("(4a) conj of unit shear by diag(a,1/a), a=1e-3: |g H g^-1 - I| =", np.abs(gg @ Ht @ inv(gg) - np.eye(2)).max())
print("(4b) 1 - tr(H)/2 for H=diag(10,0.1):", 1 - (10 + 0.1) / 2)
ok = 0
for _ in range(200):
    A = rng.standard_normal((K, K))
    if np.linalg.det(A) < 0: A[:, 0] *= -1
    R, Pm = polar(A)
    phi_i = np.real(logm(R)); phi_j = -np.real(logm(Pm))
    ok += np.abs(expm(phi_i) @ expm(-phi_j) - A).max() < 1e-8
print("(5a) polar pair reproduces random GL+(3) elements:", ok, "of 200")
Lg = logm(np.diag([-1., -2.])); print("(5b) logm(diag(-1,-2)) max imag part:", np.abs(np.imag(Lg)).max())
cnt = tot = 0
for _ in range(20000):
    A = rng.standard_normal((2, 2))
    if np.linalg.det(A) <= 0: continue
    tot += 1; ev = np.linalg.eigvals(A)
    cnt += bool(np.all(np.abs(np.imag(ev)) < 1e-14) and np.all(np.real(ev) < 0))
print("(5c) fraction of det>0 random 2x2 with two negative real eigenvalues:", cnt / tot)
def kl(m1, S1, m2, S2):
    k = len(m1); S2i = inv(S2); dm = m2 - m1
    return 0.5 * (np.log(np.linalg.det(S2) / np.linalg.det(S1)) + np.trace(S2i @ S1) + dm @ S2i @ dm - k)
def spd(k=K):
    X = rng.standard_normal((k, k)); return X @ X.T + k * np.eye(k)
m1, m2 = rng.standard_normal(K), rng.standard_normal(K); S1, S2 = spd(), spd()
Gm = rng.standard_normal((K, K))
print("(6a) thm:glk_invariance residual:", abs(kl(Gm @ m1, Gm @ S1 @ Gm.T, Gm @ m2, Gm @ S2 @ Gm.T) - kl(m1, S1, m2, S2)), " det(G)=", np.linalg.det(Gm))
def unpack(t):
    m = t[:K]; L_ = np.zeros((K, K)); L_[np.tril_indices(K)] = t[K:]; return m, L_ @ L_.T
def fisher(t0, Gmat, eps=1e-4):
    m0, S0 = unpack(t0); n = len(t0); Hs = np.zeros((n, n))
    def f(t):
        m, S = unpack(t)
        return kl(Gmat @ m0, Gmat @ S0 @ Gmat.T, Gmat @ m, Gmat @ S @ Gmat.T)
    for p in range(n):
        for q in range(n):
            ea = np.zeros(n); eb = np.zeros(n); ea[p] = eps; eb[q] = eps
            Hs[p, q] = (f(t0 + ea + eb) - f(t0 + ea - eb) - f(t0 - ea + eb) + f(t0 - ea - eb)) / (4 * eps**2)
    return Hs
Lc = np.linalg.cholesky(S1); t0 = np.concatenate([m1, Lc[np.tril_indices(K)]])
F0 = fisher(t0, np.eye(K)); Fg = fisher(t0, Gm)
print("(6b) Fisher metric (KL Hessian) through congruence vs original, max rel diff:", np.abs(F0 - Fg).max() / np.abs(F0).max())
for k in (2, 3, 4):
    basis = []
    for i in range(k):
        for j in range(k):
            E = np.zeros((k, k)); E[i, j] = 1; basis.append(E)
    Gtr = np.array([[np.trace(X @ Y) for Y in basis] for X in basis]); ev = np.linalg.eigvalsh(Gtr)
    print("(7) tr(XY) on gl(%d): (+,-,0) = %d %d %d ; expected %d %d" % (k, (ev > 1e-9).sum(), (ev < -1e-9).sum(), (abs(ev) < 1e-9).sum(), k * (k + 1) // 2, k * (k - 1) // 2))
Gx = np.array([[0, 0, 0], [0, 0, -1], [0, 1, 0.]]); Gy = np.array([[0, 0, 1], [0, 0, 0], [-1, 0, 0.]]); Gz = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 0.]])
print("(8a) [Gx,Gy]-Gz:", np.abs(Gx @ Gy - Gy @ Gx - Gz).max(), " [Gy,Gz]-Gx:", np.abs(Gy @ Gz - Gz @ Gy - Gx).max())
X0, Y0 = rnd(), rnd()
for t in (0.1, 0.05):
    X, Y = t * X0, t * Y0
    r1 = np.abs(expm(X + Y) - expm(X) @ expm(Y)).max()
    r2 = np.abs(expm(X + Y) - expm(X) @ expm(Y) @ expm(-0.5 * (X @ Y - Y @ X))).max()
    print("(8b) t=%.2f: |e^(X+Y)-e^X e^Y|=%.2e ; with factor e^(-[X,Y]/2): %.2e" % (t, r1, r2))
