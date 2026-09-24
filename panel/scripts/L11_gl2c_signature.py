"""L11: recompute the GL(2,C) worked example and the signature propositions of PIFB2 1901-1960.

Checks
 1. General (non-separable) complex frame phi = (i psi_t + psi_x) T: complex form rank one, det 0;
    Re(G) = tr(T^2) (d psi_x (x) d psi_x - d psi_t (x) d psi_t) with NO separability assumption.
 2. Signature of Re(G) is (1,1) iff d psi_t, d psi_x independent; Re(G_tt) alone is chart-dependent.
 3. Compact T (skew J, tr J^2 = -2): signature is still (1,1), the timelike role moves to x.
    Nilpotent T (tr T^2 = 0): G = 0.
 4. Regime I is automatic for an abelian frame: A = U^{-1} dU = d phi, F = dA + A^A = 0.
 5. SO+(1,1) preserves eta = diag(-1,1).
 6. Rank obstruction (single generator, 4D): eigenvalues of Re(G) carry the factor tr(T^2) = 2.
 7. All-real 4D construction: K=6 as stated; also K=5 with traceless commuting symmetric generators
    and K=4 without tracelessness (the stated minima K>=6 / K>=5 are not sharp).
 8. Combined tensor tr(AA) + Fisher pullback can be Riemannian: signature is not fixed by the
    horizontal block alone.
"""
import sympy as sp

t, x, y, z = sp.symbols('tau x y z', real=True)
I = sp.I

print("== 1-2. general complex 2D frame (no separability) ==")
# jet of the two real frame functions at a point: d psi_t = (p1, p2), d psi_x = (p3, p4)
p1, p2, p3, p4 = sp.symbols('p1 p2 p3 p4', real=True)
T = sp.diag(1, -1)
A = [(I * p1 + p3) * T, (I * p2 + p4) * T]  # A_mu = d_mu phi, phi = (i psi_t + psi_x) T
G = sp.Matrix(2, 2, lambda m, n: sp.expand((A[m] * A[n]).trace()))
print("det G (complex) =", sp.simplify(G.det()), "; rank generic =", G.subs({p1: 1, p2: 2, p3: 3, p4: 5}).rank())
ReG = G.applyfunc(lambda e: sp.re(e))
dpt, dpx = sp.Matrix([p1, p2]), sp.Matrix([p3, p4])
print("Re G - 2(dpx dpx^T - dpt dpt^T) =", sp.simplify(ReG - 2 * (dpx * dpx.T - dpt * dpt.T)))
print("det Re G + 4 Jac^2 =", sp.simplify(ReG.det() + 4 * (p1 * p4 - p2 * p3) ** 2))
M = ReG.subs({p1: 1, p2: sp.Rational(3, 10), p3: 2, p4: 1})
print("non-separable example: Re G_tt =", M[0, 0], "(positive), eigenvalues =", [sp.N(e, 6) for e in M.eigenvals()])

print("== 3. compact and nilpotent generators ==")
a, b = sp.symbols('a b', positive=True)  # a = d_tau psi_tau, b = d_x psi_x (separable)
for name, Tg in [("diag(1,-1)", sp.diag(1, -1)), ("skew J", sp.Matrix([[0, -1], [1, 0]])),
                 ("nilpotent", sp.Matrix([[0, 1], [0, 0]]))]:
    At, Ax = I * a * Tg, b * Tg
    Gc = sp.Matrix([[(At * At).trace(), (At * Ax).trace()], [(Ax * At).trace(), (Ax * Ax).trace()]])
    R = Gc.applyfunc(lambda e: sp.re(sp.expand(e)))
    print(f"T={name}: tr T^2={Tg.__pow__(2).trace()}, Re G = {R.tolist()}")

print("== 4. Regime I automatic for abelian frame ==")
s1, s2 = sp.Function('s1')(t, x), sp.Function('s2')(t, x)
Tn = sp.diag(1, -1)
U = sp.diag(sp.exp(I * s1 + s2), sp.exp(-(I * s1 + s2)))  # = exp((i s1 + s2) T)
Uinv = U.inv()
At_ = sp.simplify(Uinv * U.diff(t)); Ax_ = sp.simplify(Uinv * U.diff(x))
F = sp.simplify(Ax_.diff(t) - At_.diff(x) + At_ * Ax_ - Ax_ * At_)
print("A_tau - d_tau phi =", sp.simplify(At_ - (I * s1.diff(t) + s2.diff(t)) * Tn), " F =", F)

print("== 5. SO+(1,1) ==")
r = sp.symbols('r', real=True)
L = sp.Matrix([[sp.cosh(r), sp.sinh(r)], [sp.sinh(r), sp.cosh(r)]])
eta = sp.diag(-1, 1)
print("L^T eta L - eta =", sp.simplify(L.T * eta * L - eta))

print("== 6. rank obstruction, single generator in 4D ==")
bx, by, bz = sp.symbols('b_x b_y b_z', positive=True)
v = sp.Matrix([I * a, bx, by, bz])
G4 = 2 * v * v.T
R4 = G4.applyfunc(lambda e: sp.re(sp.expand(e)))
print("eigenvalues Re G4 =", R4.eigenvals())

print("== 7. all-real four-generator construction, minimal K ==")
def check(gens, label):
    S, Ts = gens[0], gens[1:]
    comm = max(abs(float(sp.Matrix(g1 * g2 - g2 * g1).norm())) for g1 in gens for g2 in gens)
    gram = sp.Matrix(4, 4, lambda i, j: (gens[i] * gens[j]).trace())
    traces = [g.trace() for g in Ts]
    ev = gram.eigenvals()
    print(f"{label}: max|[g,g']|={comm}, Gram(tr g g')={gram.tolist()}, spatial traces={traces}")
def blk(*ms):
    return sp.diag(*ms)
J = sp.Matrix([[0, -1], [1, 0]])
# K = 6 (paper): S on coords 1-2, traceless diagonal T's on coords 3-6
K6 = [blk(J, sp.zeros(4)), blk(sp.zeros(2), sp.diag(1, -1, 0, 0)), blk(sp.zeros(2), sp.diag(0, 0, 1, -1)),
      blk(sp.zeros(2), sp.diag(1, 1, -1, -1) / sp.sqrt(2))]
check(K6, "K=6")
# K = 5, traceless: a*I2 (+) diag(c,d,e) with 2a+c+d+e=0 is 3-dimensional; commutes with J (+) 0
e1 = blk(sp.eye(2), sp.diag(-2, 0, 0)) ; e2 = blk(sp.zeros(2), sp.diag(0, 1, -1)); e3 = blk(sp.eye(2), sp.diag(0, -1, -1))
# Gram-Schmidt w.r.t. tr(AB)
basis = []
for e in [e1, e2, e3]:
    w = e
    for u in basis:
        w = w - (w * u).trace() / (u * u).trace() * u
    basis.append(sp.simplify(w * sp.sqrt(2 / (w * w).trace())))
K5 = [blk(J, sp.zeros(3))] + basis
check(K5, "K=5 traceless")
K4 = [blk(J, sp.zeros(2)), blk(sp.eye(2), sp.zeros(2)), blk(sp.zeros(2), sp.diag(sp.sqrt(2), 0)),
      blk(sp.zeros(2), sp.diag(0, sp.sqrt(2)))]
check(K4, "K=4 non-traceless")

print("== 8. combined tensor tr(AA) + Fisher can be Riemannian ==")
kap, sig = sp.symbols('kappa sigma', positive=True)
# 4D real construction in coordinates psi: horizontal = diag(-2,2,2,2); add a Gaussian-mean Fisher term
# mu = kappa * psi_tau, Sigma = sigma^2  ->  sigma^-2 kappa^2 dpsi_tau^2
Gtot = sp.diag(-2 + kap ** 2 / sig ** 2, 2, 2, 2)
print("G_total =", Gtot.tolist(), "; Riemannian iff kappa^2/sigma^2 > 2")

print("== 9. Regime-I frame-twist form is pure gauge; relative-frame form is invariant ==")
import numpy as np
from scipy.linalg import expm
rng = np.random.default_rng(3)
Kd = 3
C0, C1 = rng.normal(size=(Kd, Kd)) * 0.4, rng.normal(size=(Kd, Kd)) * 0.4
D0, D1 = rng.normal(size=(Kd, Kd)) * 0.4, rng.normal(size=(Kd, Kd)) * 0.4
H0, H1 = rng.normal(size=(Kd, Kd)) * 0.4, rng.normal(size=(Kd, Kd)) * 0.4
Ui = lambda c: expm(C0 + c * C1)          # agent i frame along a base curve
Uj = lambda c: expm(D0 + c * D1 + c**2 * C1 @ D1)
gg = lambda c: expm(H0 + c * H1 + c**2 * H0 @ H1)  # local gauge transformation U -> U g
def A_of(U, c, h=1e-5):
    return np.linalg.solve(U(c), (U(c + h) - U(c - h)) / (2 * h))
c0 = 0.3
ftw = lambda U: np.trace(A_of(U, c0) @ A_of(U, c0))
print("agent frame-twist tr(A A):", ftw(Ui), " after U_i -> U_i g:", ftw(lambda c: Ui(c) @ gg(c)))
print("after gauge g = U_i^{-1} (Omega_ij unchanged):", ftw(lambda c: Ui(c) @ np.linalg.inv(Ui(c))))
Om = lambda c: Ui(c) @ np.linalg.inv(Uj(c))
Omg = lambda c: (Ui(c) @ gg(c)) @ np.linalg.inv(Uj(c) @ gg(c))
print("relative-frame tr((Om^-1 dOm)^2):", ftw(Om), " gauge-transformed:", ftw(Omg))
dA = A_of(Ui, c0) - A_of(Uj, c0)
print("equals tr((A_i-A_j)^2):", np.trace(dA @ dA))
