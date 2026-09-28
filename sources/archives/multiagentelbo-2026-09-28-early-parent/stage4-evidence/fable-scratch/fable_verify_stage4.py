"""Independent verifier checks (Claude Fable 5.1) for stage4-first-contrast-activation.md.

Exact rational arithmetic for the sheet geometry; floating point for the scalar constants.
Prints every number the report cites.
"""
from fractions import Fraction as Fr
import math
import numpy as np
from scipy.special import gamma
from scipy.integrate import quad

# ---------- exact sheet geometry (four-cycle, x=(kbar,mbar,omega) in R^12) ----------
def e(i):
    v = [Fr(0)] * 4
    v[i] = Fr(1)
    return v

def cov_b(i):  # r^b_i = kbar_{i+1}-kbar_i-omega_i
    j = (i + 1) % 4
    k = [a - b for a, b in zip(e(j), e(i))]
    return k + [Fr(0)] * 4 + [-x for x in e(i)]

def cov_m(i):
    j = (i + 1) % 4
    m = [a - b for a, b in zip(e(j), e(i))]
    return [Fr(0)] * 4 + m + [-x for x in e(i)]

def dot(a, b):
    return sum(x * y for x, y in zip(a, b))

def outer(a, b):
    return [[x * y for y in b] for x in a]

def madd(A, B, c=Fr(1)):
    return [[A[i][j] + c * B[i][j] for j in range(12)] for i in range(12)]

def mv(A, v):
    return [dot(row, v) for row in A]

Z = [[Fr(0)] * 12 for _ in range(12)]
I12 = [[Fr(int(i == j)) for j in range(12)] for i in range(12)]
H = Z
for g in (0, 2):
    for c in (cov_b(g), cov_m(g)):
        H = madd(H, outer(c, c), Fr(2))
# R_ev = 2 D^T D, D x = kbar - mbar
D = [e(i) + [-x for x in e(i)] + [Fr(0)] * 4 for i in range(4)]
R = Z
for row in D:
    R = madd(R, outer(row, row), Fr(2))

# n^+ and n^- are unit only up to the scalar factors; use unnormalized directions
def nplus(g):
    return [a + b for a, b in zip(cov_b(g), cov_m(g))]  # = 2 sqrt2 n^+

def nminus(g):
    return [a - b for a, b in zip(cov_b(g), cov_m(g))]  # = 2 n^-

for g in (0, 2):
    p, m = nplus(g), nminus(g)
    assert mv(H, p) == [8 * x for x in p], "H n+ = 8 n+"
    assert mv(H, m) == [4 * x for x in m], "H n- = 4 n-"
    assert mv(R, p) == [Fr(0)] * 12, "R_ev n+ = 0"
    assert mv(R, m) == [4 * x for x in m], "R_ev n- = 4 n-"
    assert dot(p, p) == 8 and dot(m, m) == 4
print("exact: H n+ = 8 n+, H n- = 4 n-, R_ev n+ = 0, R_ev n- = 4 n-   OK")
# hidden component of x_circ = (0,0,1_4)
xc = [Fr(0)] * 8 + [Fr(1)] * 4
z1dir = [a - b for a, b in zip(nplus(0), nplus(2))]
assert dot(z1dir, xc) == 0 and dot(nminus(0), xc) == 0 and dot(nminus(2), xc) == 0
zplus_dir = [a + b for a, b in zip(nplus(0), nplus(2))]  # = 2 sqrt2 * sqrt2 * z_+ direction = 4 z_+dir
print("exact: hidden projection of x_circ is 0; z_+(x_circ) =", dot(zplus_dir, xc) / 4, "(expect -1)")
# residual covector norms
print("exact: |a^b|^2 =", dot(cov_b(0), cov_b(0)), " (expect 3)")
# |D F z|^2 for n^- direction: |D n^-|^2
nm = [x / 2 for x in nminus(0)]  # unit n^-
Dn = mv(D, nm)
print("exact: |D n^-|^2 =", dot(Dn, Dn), "(expect 2)  |D n^+|^2 =", dot(mv(D, [x / (2 * Fr(2)) for x in nplus(0)]), mv(D, [x / (2 * Fr(2)) for x in nplus(0)])), "(expect 0)")

# ---------- ||P_m F|| where P_m reads the mbar block ----------
F = np.array([
    [float(x) / (2 * math.sqrt(2) * math.sqrt(2)) for x in z1dir],           # (n+_e - n+_f)/sqrt2
    [float(x) / 2 for x in nminus(0)],
    [float(x) / 2 for x in nminus(2)],
]).T
assert np.allclose(F.T @ F, np.eye(3))
PmF = F[4:8, :]
print("||P_m F|| =", np.linalg.norm(PmF, 2), " sqrt3/2 =", math.sqrt(3) / 2)

# ---------- uniform-ball constants ----------
c12 = gamma(7) / (math.sqrt(math.pi) * gamma(6.5))
print("c_12 =", c12, " 46080/(10395 pi) =", 46080 / (10395 * math.pi))
print("(15/16)^(13/2) =", (15 / 16) ** 6.5)
print("0.1427 check: 2*c12/13*(15/16)^6.5 =", 2 * c12 / 13 * (15 / 16) ** 6.5)
# exact integral version at a = rho/4 (no Taylor step): (c12/13) int_{-1/4}^{1/4} (1-x^2)^{13/2} dx / (a/rho)
val, _ = quad(lambda x: (1 - x * x) ** 6.5, -0.25, 0.25)
print("exact E[v3^2 1{|v2|<=rho/4}]/(rho a) at a=rho/4 =", c12 / 13 * val / 0.25)
# E v_k^2 = rho^2/14 and E min(v2^2,v3^2) (Monte Carlo, uniform 12-ball)
rng = np.random.default_rng(7)
N = 2_000_000
g = rng.standard_normal((N, 12))
g /= np.linalg.norm(g, axis=1, keepdims=True)
r = rng.random(N) ** (1 / 12)
v = g * r[:, None]
print("MC E v_k^2 =", v[:, 0].var() + v[:, 0].mean() ** 2, " 1/14 =", 1 / 14)
print("MC E min(v2^2,v3^2) =", np.minimum(v[:, 1] ** 2, v[:, 2] ** 2).mean(), " (author: 0.02596)")

# ---------- Phi and the numeric lower bound ----------
def Phi(m):
    return 0.0 if m < 3 else (m - 3) / 2 - 1.5 * math.log(m / 3)

eps = 1e-2
T = eps ** 8
L = math.log(1 / eps)
tstar = 2 * L + 1
rho = 1e-2
phat = 73728 * eps ** 4 * tstar + 18 * tstar * math.exp(-1 / T)
t1 = L / 2 - 0.25 * math.log(50)
lam2 = 4 + 5 * T
Mgen = 5000 * math.exp(-8) * rho ** 2 * math.exp(-10 * T * (t1 + 1)) * (math.exp(-2 * rho * rho) / 7 - phat) / eps ** 4 - 16 * (t1 + 1) - 2
print("eps=1/100: p_hat =", phat, " t_1+1 =", t1 + 1, " M_gen(0) =", Mgen, " Phi =", Phi(Mgen))
# M_rare at eps=1/100 with a = rho/4
a = min(eps, rho / 4)
sflat = L / 4 + 0.15
Mrare = 2 * math.exp(-9.2) * math.exp(-10 * T * (sflat + 1)) * (0.1427 * math.exp(-2 * rho * rho) * rho * a - rho ** 2 * phat) / eps ** 6 - 8 * (t1 + 1) - 1
print("eps=1/100: M_rare(0) =", Mrare)
print("asymptotic constant 2 e^{-9.2} 0.1427 rho =", 2 * math.exp(-9.2) * 0.1427 * rho)
print("H-phys correction 3.5*rho^2 =", 3.5 * rho ** 2)

# ---------- completion-time margins (deterministic envelope, tube noise eps^2/8) ----------
def envelope(t, vmin, eps):
    return (1 + math.sqrt(2) * rho) * math.exp(-8 * t) + vmin * math.exp(-4 * t) + eps ** 2 / 8

for eps in (1e-2, 1e-3, 1e-4):
    L = math.log(1 / eps)
    t1 = L / 2 - 0.25 * math.log(50)
    print(f"eps={eps}: envelope at t_1 / eps^2 (vmin=rho) =", envelope(t1, rho, eps) / eps ** 2,
          " ; at s=L/4+0.15 with vmin=eps:", envelope(L / 4 + 0.15, eps, eps) / eps ** 2,
          " ; at s=(1/4)log(rho/eps^2)+0.15, vmin=rho:", envelope(0.25 * math.log(rho / eps ** 2) + 0.15, rho, eps) / eps ** 2)
# smallest c with 1.01414 e^{-8c} + e^{-4c} <= 7/8
from scipy.optimize import brentq
c_up = brentq(lambda c: 1.01414 * math.exp(-8 * c) + math.exp(-4 * c) - 0.875, 0, 1)
print("upper tolerance c (both terms at threshold) =", c_up, " (author uses 0.15)")
print("lower tolerances: (1/8)log(1.33) =", math.log(1.33) / 8, " (1/4)log(1.28) =", math.log(1.28) / 4)
print("s <= t_1 check: (1/4)log(rho/eps^2)+0.15 - (L/2-0.978) =", 0.25 * math.log(rho) + 0.15 + 0.978)

# ---------- where the lower bound becomes vacuous (M_rare(h) < 3) ----------
c_rare = 2 * math.exp(-9.2) * 0.1427 * rho
print("M_rare(h) >= 3 needs e^{-8h} eps^{-5} >= ", 4 / c_rare, " i.e. h <= 5L/8 - ", math.log(4 / c_rare) / 8)
# Xi crossover: p_hat term vs eps^{-5} term
for eps in (1e-2, 2.5e-3, 1e-3):
    L = math.log(1 / eps); tstar = 2 * L + 1
    phat = 73728 * eps ** 4 * tstar
    lead = 0.04474 * rho * eps ** -5
    ph = 2.69e-3 * rho ** 2 * phat * eps ** -8
    print(f"eps={eps}: Xi leading term {lead:.3e}, p_hat term {ph:.3e}, ratio p_hat/lead = {ph/lead:.2f}")
