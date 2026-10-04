"""Numerical probes for verify_V3 (part 1): prop:link-recognition-flow, rem:link-rates(iv),
prop:link-history-prior witness, prop:link-anchor-m-coordinate witness.
float64, CPU, seeded. These support derivations; no verdict rests on them."""
import numpy as np
from numpy.polynomial.hermite_e import hermegauss
from scipy.linalg import sqrtm, eigh

rng = np.random.default_rng(3)
np.set_printoptions(precision=6, suppress=True)

# ---------- Gauss-Hermite expectation under N(mu, Sigma) in d=2 ----------
xg, wg = hermegauss(40)
wg = wg / wg.sum()
X1, X2 = np.meshgrid(xg, xg, indexing="ij")
W2 = np.outer(wg, wg)
Zpts = np.stack([X1.ravel(), X2.ravel()], 1)  # standard normal nodes
Wts = W2.ravel()

def expect(f, mu, Sigma):
    L = np.linalg.cholesky(Sigma)
    pts = mu[None, :] + Zpts @ L.T
    return np.sum(Wts * f(pts))

# nonquadratic integrand i(w) = 1/2 w^T Q w - b^T w + eps*sum cosh(w_k)
Q = np.array([[2.0, 0.4], [0.4, 1.5]]); b = np.array([0.3, -0.7]); eps = 0.15
def i_fun(w):  # vectorized over rows
    return 0.5 * np.einsum("ni,ij,nj->n", w, Q, w) - w @ b + eps * np.cosh(w).sum(1)
def grad_i(w):
    return w @ Q - b[None, :] + eps * np.sinh(w)
def hess_i_quad(w, D):  # <D, hess i(w)> for symmetric D, vectorized
    return np.einsum("ij,ij->", Q, D) + eps * (np.cosh(w) * np.diag(D)[None, :]).sum(1)

def F_of(mu, Lam):
    Sigma = np.linalg.inv(Lam)
    return expect(i_fun, mu, Sigma) + 0.5 * np.log(np.linalg.det(Lam))

# ---- A: Euler step in the natural chart equals eq:link-blr ----
mu0 = np.array([0.4, -0.2]); Lam0 = np.array([[1.8, 0.3], [0.3, 1.2]])
Sig0 = np.linalg.inv(Lam0)
# expectation coordinates (varpi1, varpi2) with varpi2 = Sigma + mu mu^T (full case: pr = id)
def F_exp(v1, v2):
    Sigma = v2 - np.outer(v1, v1); Lam = np.linalg.inv(Sigma)
    return F_of(v1, Lam)
v1 = mu0.copy(); v2 = Sig0 + np.outer(mu0, mu0)
h = 1e-5
g1 = np.zeros(2)
for k in range(2):
    e = np.zeros(2); e[k] = h
    g1[k] = (F_exp(v1 + e, v2) - F_exp(v1 - e, v2)) / (2 * h)
g2 = np.zeros((2, 2))
for k in range(2):
    for l in range(2):
        E = np.zeros((2, 2)); E[k, l] += h / 2; E[l, k] += h / 2  # symmetric direction
        if k == l: E = np.zeros((2, 2)); E[k, k] = h
        g2[k, l] = (F_exp(v1, v2 + E) - F_exp(v1, v2 - E)) / (2 * h)
# g2 as gradient w.r.t. trace pairing of symmetric matrices: off-diagonal entries of the
# gradient are half the directional derivative along (E_kl + E_lk)/2 scaled... handle directly:
# directional derivative along symmetric D equals <Grad, D>. Solve for Grad from 3 directions.
def dirder(D):
    return (F_exp(v1, v2 + h * D) - F_exp(v1, v2 - h * D)) / (2 * h)
D11 = np.array([[1.0, 0], [0, 0]]); D22 = np.array([[0, 0], [0, 1.0]]); D12 = np.array([[0, 1.0], [1.0, 0]])
G2 = np.zeros((2, 2)); G2[0, 0] = dirder(D11); G2[1, 1] = dirder(D22); G2[0, 1] = G2[1, 0] = dirder(D12) / 2
dt = 0.3
th1 = Lam0 @ mu0; th2 = -0.5 * Lam0
th1p = th1 - dt * g1; th2p = th2 - dt * G2
Lam_euler = -2 * th2p; mu_euler = np.linalg.solve(Lam_euler, th1p)
# eq:link-blr
EG = expect(lambda w: grad_i(w)[:, 0], mu0, Sig0), expect(lambda w: grad_i(w)[:, 1], mu0, Sig0)
EG = np.array(EG)
EH = np.zeros((2, 2))
for k in range(2):
    for l in range(2):
        D = np.zeros((2, 2)); D[k, l] = 1.0
        EH[k, l] = expect(lambda w: hess_i_quad(w, D) * np.ones(len(w)), mu0, Sig0)
Lam_blr = (1 - dt) * Lam0 + dt * EH
mu_blr = mu0 - dt * np.linalg.solve(Lam_blr, EG)
print("A  Euler(natural chart) vs eq:link-blr:  |dLam| =", np.abs(Lam_euler - Lam_blr).max(),
      " |dmu| =", np.abs(mu_euler - mu_blr).max())

# ---- A': diagonal-precision family: pr keeps the diagonal ----
Lam0d = np.diag([1.8, 1.2]); Sig0d = np.linalg.inv(Lam0d)
def F_exp_d(v1, s):  # s = diagonal of varpi2 = diag(Sigma) + v1^2
    Sigma = np.diag(s - v1 ** 2); return F_of(v1, np.linalg.inv(Sigma))
v1d = mu0.copy(); sd = np.diag(Sig0d) + mu0 ** 2
g1d = np.array([(F_exp_d(v1d + h * np.eye(2)[k], sd) - F_exp_d(v1d - h * np.eye(2)[k], sd)) / (2 * h) for k in range(2)])
g2d = np.array([(F_exp_d(v1d, sd + h * np.eye(2)[k]) - F_exp_d(v1d, sd - h * np.eye(2)[k])) / (2 * h) for k in range(2)])
th1d = Lam0d @ mu0; th2d = -0.5 * np.diag(Lam0d)
lam_e = -2 * (th2d - dt * g2d); mu_e = (th1d - dt * g1d) / lam_e
EGd = np.array([expect(lambda w: grad_i(w)[:, k], mu0, Sig0d) for k in range(2)])
EHd = np.array([expect(lambda w: hess_i_quad(w, np.diag(np.eye(2)[k])) * np.ones(len(w)), mu0, Sig0d) for k in range(2)])
lam_b = (1 - dt) * np.diag(Lam0d) + dt * EHd; mu_b = mu0 - dt * EGd / lam_b
print("A' diagonal family Euler vs eq:link-blr: |dlam| =", np.abs(lam_e - lam_b).max(), " |dmu| =", np.abs(mu_e - mu_b).max())

# ---- B: descent bound eq:link-blr-descent (full family) ----
def KL_gauss(mu_a, Lam_a, mu_b, Lam_b):  # KL(N(mu_a,Lam_a^-1) || N(mu_b,Lam_b^-1))
    Sa = np.linalg.inv(Lam_a); d = mu_b - mu_a
    return 0.5 * (np.trace(Lam_b @ Sa) + d @ Lam_b @ d - 2 + np.log(np.linalg.det(Lam_a) / np.linalg.det(Lam_b)))
def gamma_star_hess_ratio(v1, v2, direction):
    # second directional derivative of F~ and of Gamma* along 'direction' = (d1, D2) at (v1,v2)
    d1, D2 = direction
    def Ft(t): return F_exp(v1 + t * d1, v2 + t * D2)
    def Gs(t):  # Gamma*(varpi) = E_R log r = -entropy
        Sigma = (v2 + t * D2) - np.outer(v1 + t * d1, v1 + t * d1)
        return -0.5 * np.log(np.linalg.det(2 * np.pi * np.e * Sigma))
    hh = 1e-3
    f2 = (Ft(hh) - 2 * Ft(0) + Ft(-hh)) / hh ** 2
    g2 = (Gs(hh) - 2 * Gs(0) + Gs(-hh)) / hh ** 2
    return f2, g2
v1p = mu_blr; v2p = np.linalg.inv(Lam_blr) + np.outer(mu_blr, mu_blr)
dv1 = v1p - v1; dV2 = v2p - v2
cmax = 0.0
for t in np.linspace(0, 1, 11):
    f2, g2 = gamma_star_hess_ratio(v1 + t * dv1, v2 + t * dV2, (dv1, dV2))
    cmax = max(cmax, f2 / g2)
lhs = F_of(mu_blr, Lam_blr) - F_of(mu0, Lam0)
rhs = -KL_gauss(mu0, Lam0, mu_blr, Lam_blr) / dt - (1 / dt - cmax) * KL_gauss(mu_blr, Lam_blr, mu0, Lam0)
print("B  descent bound: F(R')-F(R) =", lhs, " bound =", rhs, " c_G(along segment, direction) =", cmax, " holds:", lhs <= rhs + 1e-9)

# ---- I: Fisher metric eq:link-gaussian-fisher by score covariance ----
def score(w, dmu, dLam):  # score of N(mu0, Lam0^-1) in direction (dmu, dLam)
    z = w - mu0[None, :]
    return (z @ Lam0) @ dmu - 0.5 * (np.einsum("ni,ij,nj->n", z, dLam, z) - np.trace(Sig0 @ dLam))
dmu = np.array([0.7, -0.3]); dLam = np.array([[0.5, 0.2], [0.2, -0.4]])
var = expect(lambda w: score(w, dmu, dLam) ** 2, mu0, Sig0)
formula = dmu @ Lam0 @ dmu + 0.5 * np.trace(Sig0 @ dLam @ Sig0 @ dLam)
print("I  Fisher metric: score variance =", var, " formula =", formula)

# ---- F: rem:link-rates(iv) invariant slice on the four-cycle ----
T = 0.37
def hessU(T):
    # x = (kbar_0..3, mbar_0..3, omega_0..3); held S^(0) selects e_0,e_2 from both ends
    H = np.zeros((12, 12))
    for i in (0, 2):
        for ch in (0, 4):  # belief block offset 0, model block offset 4
            r = np.zeros(12); r[ch + (i + 1) % 4] = 1; r[ch + i] = -1; r[8 + i] = -1
            H += 2 * np.outer(r, r)  # V = sum (r^b)^2 + (r^m)^2 -> Hessian 2 r r^T
    H += T * np.eye(12)
    Dm = np.zeros((4, 12)); Dm[:, 0:4] = np.eye(4); Dm[:, 4:8] = -np.eye(4)
    H += T * 2 * Dm.T @ Dm  # (T/2) x^T R_ev x with R_ev = 2 D^T D -> Hessian 2 T D^T D
    return H
H = hessU(T)
print("F  min eig(hess U) - T =", eigh(H, eigvals_only=True).min() - T)
Sig_slice = T * np.linalg.inv(H)
mu = rng.standard_normal(12)
mudot = -Sig_slice @ (H @ mu) / T
Sigdot = Sig_slice - Sig_slice @ H @ Sig_slice / T
print("F  on the slice: |mudot + mu| =", np.abs(mudot + mu).max(), " |Sigdot| =", np.abs(Sigdot).max())
# check the held-sheet blocks of eq:obs-cycle-held-blocks in the rotated coordinates for i=0
k_minus = np.zeros(12); k_minus[1] = 1 / np.sqrt(2); k_minus[0] = -1 / np.sqrt(2)
m_minus = np.zeros(12); m_minus[5] = 1 / np.sqrt(2); m_minus[4] = -1 / np.sqrt(2)
om0 = np.zeros(12); om0[8] = 1
B = np.stack([k_minus, m_minus, om0])
print("F  selected-edge block of hess U (expected [[4+3T,-2T,-2sqrt2],[-2T,4+3T,-2sqrt2],[-2sqrt2,-2sqrt2,4+T]]):\n", B @ H @ B.T)

# ---- G: prop:link-history-prior scalar witness ----
m_mass = 0.8
from scipy.integrate import quad
def Z0(w):
    return quad(lambda wp: np.exp(-0.5 * m_mass * (wp - w) ** 2) * np.exp(-0.5 * wp ** 2) / np.sqrt(2 * np.pi), -12, 12)[0]
for w in (0.0, 1.0, 2.5):
    print(f"G  Z0({w}) quad = {Z0(w):.8f}  formula = {(1 + m_mass) ** -0.5 * np.exp(-m_mass * w ** 2 / (2 * (1 + m_mass))):.8f}")
P = np.array([[1 + m_mass, -m_mass], [-m_mass, 1 + m_mass]])
print("G  first-marginal precision =", 1 / np.linalg.inv(P)[0, 0], " formula (1+2m)/(1+m) =", (1 + 2 * m_mass) / (1 + m_mass))

# ---- H: prop:link-anchor-m-coordinate(d) witness ----
c = 2.0; v = 0.6  # v >= 1/c
def obj(alpha, s):
    sp = s / (1 + c * s); mp = alpha / (1 + c * s)
    return -0.5 * np.log(2 * np.pi * sp) - (v + (0.3 - mp) ** 2) / (2 * sp)  # R = N(0.3, v)
vals = [max(obj((1 + c * s) * 0.3, s), obj(0.0, s)) for s in (0.5, 1, 5, 50, 500, 5000)]
print("H  sup_alpha objective at s=0.5,1,5,50,500,5000:", np.round(vals, 6), " increasing:", np.all(np.diff(vals) > 0))
