"""Numerical probes for verify_V3 (part 2): prop:link-map-inertia (b),(c) and
prop:link-linearized-equation (a),(b),(c). float64, CPU, seeded."""
import numpy as np
from scipy.linalg import expm, sqrtm
from scipy.optimize import minimize

rng = np.random.default_rng(11)
np.set_printoptions(precision=6, suppress=True)

def Lfre(B, T, n=400):  # L(B,T) = int_0^1 e^{tB} T e^{(1-t)B} dt by midpoint rule
    ts = (np.arange(n) + 0.5) / n
    return sum(expm(t * B) @ T @ expm((1 - t) * B) for t in ts) / n

K = 3
G = np.array([[2.0, 0.3, 0.0], [0.3, 1.0, 0.2], [0.0, 0.2, 1.5]])  # fiber metric
Ginv = np.linalg.inv(G)
def ipG(X, Y): return np.trace(Ginv @ X.T @ G @ Y)
def star(H): return Ginv @ H.T @ G
def Qdef(H): return 0.5 * ipG(H - np.eye(K), H - np.eye(K))

# ---- C: eq:link-timelike-gradients with g = gl(3) (pr = identity) ----
A = 0.4 * rng.standard_normal((K, K)); Ap = 0.4 * rng.standard_normal((K, K))  # earlier A, later A'
def U_of(Ap_, A_): return Qdef(expm(-Ap_) @ expm(A_))
Hol = expm(-Ap) @ expm(A)
grad_early = Lfre(star(A), star(expm(-Ap)) @ (Hol - np.eye(K)))
grad_late = -Lfre(-star(Ap), (Hol - np.eye(K)) @ star(expm(A)))
# finite differences w.r.t. the G-inner product: directional derivative along D equals ipG(grad, D)
h = 1e-6; err_e = 0.0; err_l = 0.0
for _ in range(6):
    D = rng.standard_normal((K, K))
    fd_e = (U_of(Ap, A + h * D) - U_of(Ap, A - h * D)) / (2 * h)
    fd_l = (U_of(Ap + h * D, A) - U_of(Ap - h * D, A)) / (2 * h)
    err_e = max(err_e, abs(fd_e - ipG(grad_early, D))); err_l = max(err_l, abs(fd_l - ipG(grad_late, D)))
print("C  timelike gradients vs finite differences (gl(3), G != I): early", err_e, " late", err_l)
# deviation from the Gaussian-increment gradients: small generators
s = 0.05; As = s * rng.standard_normal((K, K)); Aps = As + s * rng.standard_normal((K, K))
Hs = expm(-Aps) @ expm(As)
ge = Lfre(star(As), star(expm(-Aps)) @ (Hs - np.eye(K))); gl = -Lfre(-star(Aps), (Hs - np.eye(K)) @ star(expm(As)))
print("C  |grad_early - (A - A')|_G =", np.sqrt(ipG(ge - (As - Aps), ge - (As - Aps))), " |A-A'|_G =", np.sqrt(ipG(As - Aps, As - Aps)),
      " |grad_late - (A' - A)|_G =", np.sqrt(ipG(gl - (Aps - As), gl - (Aps - As))))
# quadratic form of the increment at a given A: U(A+dA, A) vs 1/2 |L(-A,dA) e^A|^2_G
dA = 1e-2 * rng.standard_normal((K, K))
lhs = U_of(A + dA, A); rhs = 0.5 * ipG(Lfre(-A, dA) @ expm(A), Lfre(-A, dA) @ expm(A))
print("C  U(A+dA,A) =", lhs, " 1/2|L(-A,dA)e^A|^2 =", rhs, " rel. diff =", abs(lhs - rhs) / rhs)
# so(3) with G = I: pr = projection onto skew matrices
def skew(X): return 0.5 * (X - X.T)
S1 = skew(rng.standard_normal((K, K))); S2 = skew(rng.standard_normal((K, K)))
H1 = expm(-S2) @ expm(S1)
ge3 = skew(Lfre(S1.T, expm(-S2).T @ (H1 - np.eye(K))))
err = 0.0
for _ in range(5):
    D = skew(rng.standard_normal((K, K)))
    fd = (0.5 * np.linalg.norm(expm(-S2) @ expm(S1 + h * D) - np.eye(K)) ** 2 - 0.5 * np.linalg.norm(expm(-S2) @ expm(S1 - h * D) - np.eye(K)) ** 2) / (2 * h)
    err = max(err, abs(fd - np.trace(ge3.T @ D)))
print("C  so(3), G=I: projected early gradient vs finite differences:", err)

# ---- D: prop:link-linearized-equation(a): expansion of E[E_a] (gl(3), Euclidean fiber) ----
W = np.array([[1.5, 0.2, 0], [0.2, 1.0, 0.1], [0, 0.1, 0.8]])
mu_i = rng.standard_normal(K); mu_j = rng.standard_normal(K)
Sj = np.eye(K) + 0.3 * np.ones((K, K)); Si = 0.5 * np.eye(K)
def EE(Om):
    M = expm(Om); d = mu_i - M @ mu_j
    return 0.5 * (d @ W @ d + np.trace(W @ Si) + np.trace(W @ M @ Sj @ M.T))
J = W @ (np.outer(mu_i - mu_j, mu_j) - Sj)
Ekk = Sj + np.outer(mu_j, mu_j)
errg = 0.0; errh = 0.0
for _ in range(5):
    D = rng.standard_normal((K, K))
    fd1 = (EE(h * D) - EE(-h * D)) / (2 * h)
    errg = max(errg, abs(fd1 - (-np.trace(J.T @ D))))
    hh = 1e-3
    fd2 = (EE(hh * D) - 2 * EE(np.zeros((K, K))) + EE(-hh * D)) / hh ** 2
    quad = np.trace(W @ D @ Ekk @ D.T) - np.trace(J.T @ D @ D)
    errh = max(errh, abs(fd2 - quad))
print("D  grad E[E_a](0) = -J_a:", errg, "  Hessian form = Tr(W D Ekk D^T) - Tr(J^T D^2):", errh)

# ---- D': small full instance: K-operator, linear solution, nonlinear critical point, error bound ----
# one edge e, two episodes (n1=1), g = gl(2) with G = I, zero anchor, no loops, Gaussian increment
K2 = 2
W2 = np.eye(K2); mui = np.array([0.3, -0.1]); muj = np.array([0.2, 0.25]); Sj2 = 0.2 * np.eye(K2); Si2 = 0.1 * np.eye(K2)
sig = 0.5  # prior covariance Sigma = sig*I  => c_Sigma = 1/sig
mm = 0.7
J2 = W2 @ (np.outer(mui - muj, muj) - Sj2)
def S_hist(x):  # x = (vec Om0, vec Om1)
    O0 = x[:4].reshape(2, 2); O1 = x[4:].reshape(2, 2)
    def EEa(Om):
        M = expm(Om); d = mui - M @ muj
        return 0.5 * (d @ W2 @ d + np.trace(W2 @ Si2) + np.trace(W2 @ M @ Sj2 @ M.T))
    return sum(0.5 * np.sum(O ** 2) / sig + EEa(O) for O in (O0, O1)) + 0.5 * mm * np.sum((O1 - O0) ** 2)
# K operator as 8x8 matrix: quadratic form <x, K x>
def Kform(x):
    O0 = x[:4].reshape(2, 2); O1 = x[4:].reshape(2, 2)
    Ekk2 = Sj2 + np.outer(muj, muj)
    val = sum(np.sum(O ** 2) / sig + np.trace(W2 @ O @ Ekk2 @ O.T) for O in (O0, O1))
    return val + mm * np.sum((O1 - O0) ** 2)
Kmat = np.zeros((8, 8))
for a in range(8):
    for b_ in range(8):
        ea = np.eye(8)[a]; eb = np.eye(8)[b_]
        Kmat[a, b_] = 0.25 * (Kform(ea + eb) - Kform(ea - eb))
jvec = np.concatenate([J2.ravel(), J2.ravel()])  # <j, x> = sum_n Tr(J^T Om_n)
x_lin = np.linalg.solve(Kmat, jvec)
# gradient check at 0: grad S_hist(0) = -j
g0 = np.array([(S_hist(h * np.eye(8)[k]) - S_hist(-h * np.eye(8)[k])) / (2 * h) for k in range(8)])
print("D' grad S_hist(0) + j :", np.abs(g0 + jvec).max())
res = minimize(S_hist, x_lin, method="BFGS", options={"gtol": 1e-12})
x_star = res.x
cSig = 1 / sig
print("D' |x_star| =", np.linalg.norm(x_star), " 2|j|/c_Sigma =", 2 * np.linalg.norm(jvec) / cSig,
      " min eig K - c_Sigma =", np.linalg.eigvalsh(Kmat).min() - cSig)
# N_0 and c_0, c_r (crude): c_0 = ||N_0||, N_0 form = -sum_n Tr(J^T Om_n^2)
def N0form(x):
    return -sum(np.trace(J2.T @ O @ O) for O in (x[:4].reshape(2, 2), x[4:].reshape(2, 2)))
Nmat = np.zeros((8, 8))
for a in range(8):
    for b_ in range(8):
        ea = np.eye(8)[a]; eb = np.eye(8)[b_]
        Nmat[a, b_] = 0.25 * (N0form(ea + eb) - N0form(ea - eb))
c0 = np.abs(np.linalg.eigvalsh(Nmat)).max()
# c_r: max over sampled points in the ball of radius r of ||D^3 S_hist|| (operator norm, crude estimate)
r = 0.6
def hess(x, hh=1e-3):
    Hh = np.zeros((8, 8))
    for a in range(8):
        for b_ in range(8):
            ea = hh * np.eye(8)[a]; eb = hh * np.eye(8)[b_]
            Hh[a, b_] = (S_hist(x + ea + eb) - S_hist(x + ea - eb) - S_hist(x - ea + eb) + S_hist(x - ea - eb)) / (4 * hh * hh)
    return Hh
cr = 0.0
H0 = hess(np.zeros(8))
for _ in range(12):
    p = rng.standard_normal(8); p = p / np.linalg.norm(p) * r * rng.uniform(0.2, 1.0)
    cr = max(cr, np.linalg.norm(hess(p) - H0, 2) / np.linalg.norm(p))  # lower bound on sup ||D^3||
cond_small = c0 + cr * r <= cSig / 2 and np.linalg.norm(jvec) <= cSig * r / 4
bound = 2 * np.linalg.norm(jvec) / cSig ** 2 * (c0 + cr * np.linalg.norm(jvec) / cSig)
print("D' c_0 =", c0, " c_r(est) =", cr, " conditions of (c) hold:", cond_small,
      " |x_star - x_lin| =", np.linalg.norm(x_star - x_lin), " bound =", bound)
print("D' cond(G)=1 bounds: c_0 <= max j =", c0 <= np.linalg.norm(J2, "fro"), " |j| <= sqrt(sum j^2) =", np.linalg.norm(jvec) <= np.sqrt(2) * np.linalg.norm(J2, "fro"))

# ---- E: prop:link-map-inertia(c): 1D double well, held ends, monotone kink ----
def Vdw(x): return (x ** 2 - 1) ** 2
a, bnd = -1.0, 1.0; n1 = 6
def E_hist(z, m):
    w = np.concatenate([[a], z, [bnd]])
    return 0.5 * m * np.sum(np.diff(w) ** 2) + np.sum(Vdw(z))
for m in (0.3, 1.0, 5.0):
    best = None
    for _ in range(60):
        z0 = rng.uniform(-1.6, 1.6, n1 - 1)
        res = minimize(E_hist, z0, args=(m,), method="BFGS", options={"gtol": 1e-10})
        if best is None or res.fun < best.fun - 1e-12: best = res
    w = np.concatenate([[a], best.x, [bnd]])
    print(f"E  m={m}: best history {np.round(w, 4)}  strictly increasing: {np.all(np.diff(w) > 1e-9)}")
# rearrangement inequality on random histories in [a,b]
viol = 0
for _ in range(2000):
    z = rng.uniform(a, bnd, n1 - 1); m = 1.0
    E1 = E_hist(z, m); E2 = E_hist(np.sort(z), m)
    if E2 > E1 + 1e-12: viol += 1
print("E  rearrangement raised the energy in", viol, "of 2000 random histories")
