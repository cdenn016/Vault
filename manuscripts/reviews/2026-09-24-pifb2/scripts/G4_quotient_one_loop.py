r"""G4 check (a): one-loop quotient formula eq:beyond_mf_one_loop (PIFB2.tex:3546-3551).

Part A (compact SO(2)): two K=2 means a,b in R^2, diagonal rotation redundancy.
  Exact:   Z_phys = Z_full / vol(SO(2)) = \int r_a r_b e^{-F/T} dr_a dr_b dpsi  (polar change of variables)
  Quotient one loop:  -T log Z_phys = F0 + (T/2) log det(H_h/(2 pi T)) - (T/2) log Gram + O(T^2),
  Gram = |V|^2, V = (J a, J b) the orbit generator; H_h = Hessian on the g-orthogonal complement of V.
  Also: gauge-fixed slice a_2 = 0 with Faddeev-Popov factor |a_1|: FP^2/det H_slice = Gram/det H_h.
  Also: the manuscript's form with a fixed scale mu (mu=1) misses -(n_phys T/2) log(2 pi T).
Part B (noncompact GL+(2)): (mu, Sigma) in R^2 x SPD(2), action (h mu, h Sigma h^T), Fisher metric.
  Checks: det Gram of the 4 generators is constant along orbits (so Gamma_measure is finite);
  the Weil quotient density J(u) = sqrt(det Gram) sqrt(g_uu); Lebesgue (non-invariant) reference
  gives an orbit-dependent Gram; one-loop quotient formula vs exact 1D quotient integral.
Runs in a few seconds with bare python (numpy, scipy, sympy).
"""
import numpy as np
import sympy as sp
from scipy.optimize import minimize
from scipy.integrate import quad

np.set_printoptions(precision=6, suppress=False)

# ---------------- Part A: SO(2) -----------------
a1, a2, b1, b2 = sp.symbols('a1 a2 b1 b2', real=True)
A2 = a1**2 + a2**2
B2 = b1**2 + b2**2
dot = a1*b1 + a2*b2
crs = a1*b2 - a2*b1
Fs = (A2 - 1)**2 + sp.Rational(1, 2)*(B2 - 2)**2 + sp.Rational(4, 5)*(dot - sp.Rational(3, 5))**2 \
    + sp.Rational(3, 5)*(crs - sp.Rational(9, 10))**2
X = [a1, a2, b1, b2]
F_f = sp.lambdify(X, Fs, 'numpy')
G_f = sp.lambdify(X, [sp.diff(Fs, v) for v in X], 'numpy')
H_f = sp.lambdify(X, sp.hessian(Fs, X), 'numpy')

res = minimize(lambda x: F_f(*x), x0=[1.0, 0.0, 0.5, 1.2], jac=lambda x: np.array(G_f(*x)),
               method='BFGS', options={'gtol': 1e-13})
x0 = res.x
F0 = res.fun
Hm = np.array(H_f(*x0), dtype=float)
Jrot = np.array([[0.0, -1.0], [1.0, 0.0]])
V = np.concatenate([Jrot @ x0[:2], Jrot @ x0[2:]])
Gram = V @ V
# orthonormal complement of V (Euclidean metric)
Qfull, _ = np.linalg.qr(np.column_stack([V, np.eye(4)]))
Qh = Qfull[:, 1:4]
Hh = Qh.T @ Hm @ Qh
print('Part A (SO(2))')
print('  saddle x0 =', x0, ' F0 =', F0, ' |grad| =', np.linalg.norm(G_f(*x0)))
print('  full Hessian eigenvalues =', np.linalg.eigvalsh(Hm), ' |H V| =', np.linalg.norm(Hm @ V))
print('  horizontal Hessian eigenvalues =', np.linalg.eigvalsh(Hh), ' Gram =', Gram)

# gauge-fixed slice a2 = 0 (a1 > 0), FP determinant |d(a2)/d theta| = |a1|; rotate x0 onto the slice
th = np.arctan2(x0[1], x0[0])
R = np.array([[np.cos(-th), -np.sin(-th)], [np.sin(-th), np.cos(-th)]])
xs = np.concatenate([R @ x0[:2], R @ x0[2:]])
Hs_full = np.array(H_f(*xs), dtype=float)
idx = [0, 2, 3]
Hslice = Hs_full[np.ix_(idx, idx)]
FP = abs(xs[0])
lhs = FP**2 / np.linalg.det(Hslice)
rhs = Gram / np.linalg.det(Hh)
print('  FP identity  FP^2/det H_slice =', lhs, '  Gram/det H_h =', rhs, '  rel.resid =', abs(lhs - rhs) / rhs)
print('  double-counting error if FP and Gamma_measure are both kept: -T log|a1| per unit T =', -np.log(FP))

# exact quotient integral in (r_a, r_b, psi)
N = 221
ra = np.linspace(1e-3, 2.0, N)
rb = np.linspace(1e-3, 2.6, N)
ps = np.linspace(-np.pi, np.pi, N, endpoint=False)
RA, RB, PS = np.meshgrid(ra, rb, ps, indexing='ij')
Fg = F_f(RA, np.zeros_like(RA), RB*np.cos(PS), RB*np.sin(PS))
wts = RA*RB
dV = (ra[1]-ra[0])*(rb[1]-rb[0])*(ps[1]-ps[0])
n_phys = 3
print('  T, exact -T log Z_phys, one-loop pred (mu^2=2piT), resid, resid/T^2, fixed-mu(=1) resid/T')
for T in [0.2, 0.1, 0.05, 0.025, 0.0125]:
    Z = np.sum(np.exp(-(Fg - F0)/T)*wts)*dV
    exact = F0 - T*np.log(Z)
    pred = F0 + 0.5*T*np.log(np.linalg.det(Hh/(2*np.pi*T))) - 0.5*T*np.log(Gram)
    pred_mu1 = F0 + 0.5*T*np.log(np.linalg.det(Hh)) - 0.5*T*np.log(Gram)
    r = exact - pred
    print(f'  {T:7.4f} {exact: .8f} {pred: .8f} {r: .3e} {r/T**2: .4f}   {(exact-pred_mu1)/T: .4f}'
          f'  [-(3/2)log(2piT) = {-(n_phys/2)*np.log(2*np.pi*T): .4f}]')

# ---------------- Part B: GL+(2) on (mu, Sigma) -----------------
print('\nPart B (GL+(2) on Gaussian (mu,Sigma), Fisher metric)')


def sym(v):
    return np.array([[v[0], v[1]], [v[1], v[2]]])


def fisher(mu, S):
    """Fisher metric in coordinates (mu1, mu2, S11, S12, S22)."""
    Si = np.linalg.inv(S)
    E = [np.array([[1., 0], [0, 0]]), np.array([[0, 1.], [1., 0]]), np.array([[0, 0], [0, 1.]])]
    g = np.zeros((5, 5))
    g[:2, :2] = Si
    for i in range(3):
        for j in range(3):
            g[2+i, 2+j] = 0.5*np.trace(Si @ E[i] @ Si @ E[j])
    return g


gens = [np.array([[1., 0], [0, 0]]), np.array([[0, 1.], [0, 0]]), np.array([[0, 0], [1., 0]]),
        np.array([[0, 0], [0, 1.]])]


def gen_vecs(mu, S):
    out = []
    for T_ in gens:
        dmu = T_ @ mu
        dS = T_ @ S + S @ T_.T
        out.append(np.array([dmu[0], dmu[1], dS[0, 0], dS[0, 1], dS[1, 1]]))
    return np.array(out).T  # 5 x 4


def gram(mu, S, metric='fisher'):
    Vg = gen_vecs(mu, S)
    g = fisher(mu, S) if metric == 'fisher' else np.eye(5)
    return Vg.T @ g @ Vg


rng = np.random.default_rng(0)
mu0 = np.array([0.7, -0.4])
S0 = np.array([[1.3, 0.4], [0.4, 0.8]])
dG = np.linalg.det(gram(mu0, S0))
dE = np.linalg.det(gram(mu0, S0, 'euclid'))
print('  det Gram (Fisher) at x          =', dG, '   (Euclidean coords metric) =', dE)
for k in range(3):
    h = rng.normal(size=(2, 2))
    if np.linalg.det(h) < 0:
        h[:, 0] *= -1
    mu1, S1 = h @ mu0, h @ S0 @ h.T
    print(f'  h#{k}: det h={np.linalg.det(h): .3f}  det Gram Fisher={np.linalg.det(gram(mu1, S1)): .12f}'
          f'  det Gram Euclid={np.linalg.det(gram(mu1, S1, "euclid")): .5e}')


def u_of(mu, S):
    return np.sqrt(mu @ np.linalg.solve(S, mu))


def g_uu(u):
    mu = np.array([u, 0.0]); S = np.eye(2)
    eps = 1e-6
    x = np.array([mu[0], mu[1], 1.0, 0.0, 1.0])
    grad = np.zeros(5)
    for i in range(5):
        xp = x.copy(); xm = x.copy(); xp[i] += eps; xm[i] -= eps
        grad[i] = (u_of(xp[:2], sym(xp[2:])) - u_of(xm[:2], sym(xm[2:])))/(2*eps)
    return 1.0/(grad @ np.linalg.solve(fisher(mu, S), grad))


def weil_density(u):
    """Density of the quotient measure of nu = Fisher volume, Haar normalized to Lebesgue at identity.
    Slice (u e1, I); map (dh, du) -> (d mu, d Sigma) at h = I."""
    Jm = np.zeros((5, 5))
    mu = np.array([u, 0.0]); S = np.eye(2)
    Vg = gen_vecs(mu, S)
    Jm[:, :4] = Vg
    Jm[:, 4] = np.array([1.0, 0, 0, 0, 0])
    return abs(np.linalg.det(Jm))*np.sqrt(np.linalg.det(fisher(mu, S)))


for u in [0.5, 1.0, 1.5, 2.5]:
    mu = np.array([u, 0.0]); S = np.eye(2)
    pred = np.sqrt(np.linalg.det(gram(mu, S)))*np.sqrt(g_uu(u))
    print(f'  u={u}: Weil density J(u)={weil_density(u):.10f}  sqrt(detGram)*sqrt(g_uu)={pred:.10f}'
          f'  g_uu={g_uu(u):.8f}')

u0 = 1.5
f = lambda u: 2*(u-u0)**2 + 0.5*(u-u0)**3 + 0.8*(u-u0)**4
fpp = 4.0
print('  T, exact -T log Z_quot, one-loop quotient pred, resid, resid/T^2')
for T in [0.2, 0.1, 0.05, 0.025, 0.0125]:
    Z, _ = quad(lambda u: weil_density(u)*np.exp(-f(u)/T), 1e-9, u0+12*np.sqrt(T), points=[u0], limit=400,
                epsabs=0, epsrel=1e-13)
    exact = -T*np.log(Z)
    mu = np.array([u0, 0.0]); S = np.eye(2)
    pred = 0.5*T*np.log(fpp/(g_uu(u0)*2*np.pi*T)) - 0.5*T*np.log(np.linalg.det(gram(mu, S)))
    r = exact - pred
    print(f'  {T:7.4f} {exact: .10f} {pred: .10f} {r: .3e} {r/T**2: .5f}')
print('  Raw invariant integral: Weil formula gives Z_raw = vol_Haar(GL+(2)) * Z_quot = infinity (analytic).')
