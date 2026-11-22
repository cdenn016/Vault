"""Independent check of C3 (conj_agy_synchronous.md).
(A) Peretto lemma: exact rational detailed balance for random symmetric pair factors, n=3,4; planted asymmetric control.
(B) delta->0 limit system F derived by sympy series from the exact Z(u,v) (not typed in), compared with the note's
    F1..F3; root (beta0,kappa0,mu0); det J0; positivity threshold.
(C) 50-digit solve of the exact three equations at eps=0.05, delta=0.1; exact comparison mu_P vs P_C(gamma_C).
(D) Krawczyk interval certificate: a true root exists in a small box around the computed point (upgrades the
    computed instance from "numerical" to "proved to exist", given correct interval arithmetic in mpmath.iv).
(E) Independent 12D first-principles rebuild (own code) and stationary-law comparison; planted control.
"""
from fractions import Fraction as Fr
from itertools import product
import random
import sympy as sp
import mpmath as mp
import numpy as np

# ---------------- (A) Peretto lemma, exact ----------------
random.seed(3)


def peretto_exact(shape, symmetric=True):
    n = len(shape)
    w = [[Fr(random.randint(1, 9), random.randint(1, 9)) for _ in range(shape[i])] for i in range(n)]
    # pair factor t_ij(a,b) = exp(-gamma V_ij(a,b)) > 0 rational, with t_ji(b,a) = t_ij(a,b) if symmetric
    t = {}
    for i in range(n):
        for j in range(i + 1, n):
            t[(i, j)] = [[Fr(random.randint(1, 9), random.randint(1, 9)) for _ in range(shape[j])] for _ in range(shape[i])]
            if symmetric:
                t[(j, i)] = [[t[(i, j)][a][b] for a in range(shape[i])] for b in range(shape[j])]
            else:
                t[(j, i)] = [[Fr(random.randint(1, 9), random.randint(1, 9)) for _ in range(shape[i])] for _ in range(shape[j])]
    states = list(product(*[range(m) for m in shape]))

    def kern(i, a, s):  # unnormalized conditional weight of member i choosing a given others in s
        v = w[i][a]
        for j in range(n):
            if j != i:
                v *= t[(i, j)][a][s[j]]
        return v

    def Z(i, s):
        return sum(kern(i, a, s) for a in range(shape[i]))

    def T(s, s2):
        v = Fr(1)
        for i in range(n):
            v *= kern(i, s2[i], s) / Z(i, s)
        return v

    def mu(s):
        v = Fr(1)
        for i in range(n):
            v *= w[i][s[i]] * Z(i, s)
        return v
    worst = Fr(0)
    for s in states:
        for s2 in states:
            worst = max(worst, abs(mu(s) * T(s, s2) - mu(s2) * T(s2, s)))
    return worst


print("(A) Peretto detailed balance, exact Fractions")
for shape in [(3, 3, 3), (2, 3, 2), (2, 2, 2, 2)]:
    print(f"  shape {shape}: symmetric V: max|mu T - (mu T)^T| = {peretto_exact(shape)} ; planted asymmetric V: {float(peretto_exact(shape, False)):.3e}")

# ---------------- (B) limit system from the exact Z ----------------
eps, d, be, ka, mu_ = sp.symbols('epsilon delta beta kappa mu', positive=True)
p = (1 - eps) / 2
a_, b_, c_ = d, be * d, ka * d
Bm = {(1, 1): a_, (1, 2): b_, (2, 1): c_, (2, 2): a_}


def Bf(u, v):
    return 0 if (u == 0 or v == 0) else Bm[(u, v)]


def Zs(u, v):  # member k's normalizer with successor at u and predecessor at v
    return eps + p * sp.exp(-(Bf(1, u) + Bf(v, 1))) + p * sp.exp(-(Bf(2, u) + Bf(v, 2)))


def lead(u, v, rhs):
    expr = -sp.log(Zs(u, v)) + sp.log(Zs(u, 0)) + sp.log(Zs(0, v)) - mu_ * d * rhs
    ser = sp.series(expr, d, 0, 3).removeO()
    return sp.simplify(ser.coeff(d, 0)), sp.simplify(ser.coeff(d, 1)), sp.simplify(ser.coeff(d, 2))


F_note = [p * (p * (1 + be) * (1 + ka) - (1 + be * ka)) - mu_,
          p * (p * (1 + ka) ** 2 - 2 * ka) - mu_ * be,
          p * (p * (1 + be) ** 2 - 2 * be) - mu_ * ka]
print("(B) series of the exact equations in delta: orders 0,1 vanish, order 2 equals the note's F_k ?")
F_der = []
for k, (u, v, rhs) in enumerate([(1, 1, a_), (1, 2, b_), (2, 1, c_)]):
    c0, c1, c2 = lead(u, v, rhs)
    F_der.append(c2)
    print(f"  eq {k + 1}: c0={c0}, c1={c1}, c2 - F_note = {sp.simplify(c2 - F_note[k])}")
# the (2,2) equation coincides with the (1,1) equation identically
print("  (2,2) vs (1,1) equation difference:", sp.simplify(sp.log(Zs(2, 2)) - sp.log(Zs(2, 0)) - sp.log(Zs(0, 2)) - sp.log(Zs(1, 1)) + sp.log(Zs(1, 0)) + sp.log(Zs(0, 1))))
b0 = (1 - eps + 2 * sp.sqrt(3 * eps)) / (1 + eps)
k0 = (1 - eps - 2 * sp.sqrt(3 * eps)) / (1 + eps)
m0 = 2 * eps * (1 - eps) / (1 + eps)
sub = {be: b0, ka: k0, mu_: m0}
print("  F_derived at (beta0,kappa0,mu0):", [sp.simplify(f.subs(sub)) for f in F_der])
J = sp.Matrix(F_der).jacobian([be, ka, mu_]).subs(sub)
detJ = sp.factor(sp.simplify(J.det()))
print("  det J0 =", detJ, "; minus note's formula:", sp.simplify(detJ + 24 * eps ** 2 * (1 - eps) ** 2 / (1 + eps) ** 2))
print("  planted control: F1 with the sign of mu flipped at the root:", sp.simplify((F_note[0] + 2 * mu_).subs(sub)))
print("  kappa0 at eps = 7-4sqrt3:", sp.simplify(k0.subs(eps, 7 - 4 * sp.sqrt(3))), "; kappa0(0.05)=%.6f kappa0(0.08)=%.6f" % (float(k0.subs(eps, 0.05)), float(k0.subs(eps, 0.08))))

# ---------------- (C) 50-digit solve ----------------
mp.mp.dps = 50
EPS = mp.mpf('0.05')
A = mp.mpf('0.1')
PP = (1 - EPS) / 2


def Zm(u, v, a, b, c):
    Bq = {(1, 1): a, (1, 2): b, (2, 1): c, (2, 2): a}
    f = lambda x, y: mp.mpf(0) if (x == 0 or y == 0) else Bq[(x, y)]
    return EPS + PP * mp.e ** (-(f(1, u) + f(v, 1))) + PP * mp.e ** (-(f(2, u) + f(v, 2)))


def Fm(b, c, g):
    a = A
    return [-mp.log(Zm(1, 1, a, b, c)) + mp.log(Zm(1, 0, a, b, c)) + mp.log(Zm(0, 1, a, b, c)) - g * a,
            -mp.log(Zm(1, 2, a, b, c)) + mp.log(Zm(1, 0, a, b, c)) + mp.log(Zm(0, 2, a, b, c)) - g * b,
            -mp.log(Zm(2, 1, a, b, c)) + mp.log(Zm(2, 0, a, b, c)) + mp.log(Zm(0, 1, a, b, c)) - g * c]


sol = mp.findroot(lambda b, c, g: Fm(b, c, g), (mp.mpf('0.1673'), mp.mpf('0.0106'), mp.mpf('0.0104')))
bS, cS, gS = sol
print("(C) 50-digit root at eps=0.05, delta=0.1:")
print("   b       =", mp.nstr(bS, 40))
print("   c       =", mp.nstr(cS, 40))
print("   gamma_C =", mp.nstr(gS, 40))
print("   residual max |F| =", mp.nstr(max(abs(x) for x in Fm(bS, cS, gS)), 5))
# exact comparison of Peretto law with P_C(gamma_C; E, G_C)
w = [EPS, PP, PP]
Bq = {(1, 1): A, (1, 2): bS, (2, 1): cS, (2, 2): A}
Bv = lambda x, y: mp.mpf(0) if (x == 0 or y == 0) else Bq[(x, y)]
gstar = mp.log(Zm(1, 0, A, bS, cS) * Zm(0, 1, A, bS, cS)) / (1 - gS)
gv = [mp.mpf(0), gstar, gstar]
Eun = [w[u] * mp.e ** gv[u] for u in range(3)]
E = [x / sum(Eun) for x in Eun]
states = list(product(range(3), repeat=3))


def GC(s):
    return sum(gv[x] for x in s) + sum(Bv(s[i], s[(i + 1) % 3]) for i in range(3))


def normalize(v):
    t = sum(v)
    return [x / t for x in v]


PgC = normalize([E[s[0]] * E[s[1]] * E[s[2]] * mp.e ** (-gS * GC(s)) for s in states])
P1 = normalize([E[s[0]] * E[s[1]] * E[s[2]] * mp.e ** (-GC(s)) for s in states])
idx = {s: k for k, s in enumerate(states)}


def Kc(i, a, s):  # conditional of P1 for member i choosing a given s_{-i}
    num = 0
    den = 0
    for x in range(3):
        t = list(s)
        t[i] = x
        val = P1[idx[tuple(t)]]
        den += val
        if x == a:
            num = val
    return num / den


Tm = mp.matrix(27, 27)
for s in states:
    for s2 in states:
        Tm[idx[s], idx[s2]] = Kc(0, s2[0], s) * Kc(1, s2[1], s) * Kc(2, s2[2], s)
vec = mp.matrix(1, 27)
for k in range(27):
    vec[0, k] = PgC[k]
res = vec * Tm - vec
print("   stationarity of P_C(gamma_C) under T_sync(gamma=1): ||P T - P||_1 =", mp.nstr(sum(abs(res[0, k]) for k in range(27)), 5))
res1 = mp.matrix(1, 27)
for k in range(27):
    res1[0, k] = P1[k]
res1 = res1 * Tm - res1
print("   control, P_C(gamma=1) under the same kernel: ||P T - P||_1 =", mp.nstr(sum(abs(res1[0, k]) for k in range(27)), 5))
print("   E =", [mp.nstr(x, 12) for x in E], " g* =", mp.nstr(gstar, 12), " R_s =", mp.nstr(mp.e ** (gstar / 2) / (2 * mp.pi * mp.e), 12))

# ---------------- (D) Krawczyk certificate ----------------
iv = mp.iv
iv.dps = 40
EPSi = iv.mpf('0.05')
Ai = iv.mpf('0.1')
PPi = (1 - EPSi) / 2


def Zparts(u, v, a, b, c):
    Bq = {(1, 1): a, (1, 2): b, (2, 1): c, (2, 2): a}
    f = lambda x, y: iv.mpf(0) if (x == 0 or y == 0) else Bq[(x, y)]
    e1 = PPi * iv.exp(-(f(1, u) + f(v, 1)))
    e2 = PPi * iv.exp(-(f(2, u) + f(v, 2)))
    return EPSi + e1 + e2, e1, e2


def dlogZ(u, v, a, b, c):
    """gradient of ln Z(u,v) wrt (b,c)"""
    Zv, e1, e2 = Zparts(u, v, a, b, c)
    # exponent of e1: B(1,u)+B(v,1); of e2: B(2,u)+B(v,2)
    def cnt(pairs, key):
        return sum(1 for q in pairs if q == key)
    p1 = [(1, u), (v, 1)]
    p2 = [(2, u), (v, 2)]
    p1 = [q for q in p1 if 0 not in q]
    p2 = [q for q in p2 if 0 not in q]
    db = -(e1 * cnt(p1, (1, 2)) + e2 * cnt(p2, (1, 2))) / Zv
    dc = -(e1 * cnt(p1, (2, 1)) + e2 * cnt(p2, (2, 1))) / Zv
    return db, dc


def F_iv(b, c, g):
    a = Ai
    L = lambda u, v: iv.log(Zparts(u, v, a, b, c)[0])
    return [-L(1, 1) + L(1, 0) + L(0, 1) - g * a,
            -L(1, 2) + L(1, 0) + L(0, 2) - g * b,
            -L(2, 1) + L(2, 0) + L(0, 1) - g * c]


def J_iv(b, c, g):
    a = Ai
    D = lambda u, v: dlogZ(u, v, a, b, c)
    rows = []
    for (u, v), lin in [((1, 1), None), ((1, 2), 'b'), ((2, 1), 'c')]:
        d_uv, d_u0, d_0v = D(u, v), D(u, 0), D(0, v)
        db = -d_uv[0] + d_u0[0] + d_0v[0] - (g if lin == 'b' else 0)
        dc = -d_uv[1] + d_u0[1] + d_0v[1] - (g if lin == 'c' else 0)
        dg = -(a if lin is None else (b if lin == 'b' else c))
        rows.append([db, dc, dg])
    return rows


y = [mp.mpf(mp.nstr(bS, 30)), mp.mpf(mp.nstr(cS, 30)), mp.mpf(mp.nstr(gS, 30))]
rad = mp.mpf('1e-12')
X = [iv.mpf([yy - rad, yy + rad]) for yy in y]
Y = [iv.mpf(yy) for yy in y]
Jmid = mp.matrix([[x.mid for x in row] for row in J_iv(*Y)])
Cm = mp.inverse(Jmid)
Ci = [[iv.mpf(Cm[i, j]) for j in range(3)] for i in range(3)]
Fy = F_iv(*Y)
JX = J_iv(*X)
Kbox = []
for i in range(3):
    acc = Y[i] - sum(Ci[i][j] * Fy[j] for j in range(3))
    for j in range(3):
        m_ij = (iv.mpf(1) if i == j else iv.mpf(0)) - sum(Ci[i][k] * JX[k][j] for k in range(3))
        acc = acc + m_ij * (X[j] - Y[j])
    Kbox.append(acc)
inside = all((Kbox[i].a > X[i].a) and (Kbox[i].b < X[i].b) for i in range(3))
print("(D) Krawczyk: K(X) strictly inside X (radius 1e-12) =", inside)
print("   widths of K(X):", [mp.nstr(k.delta, 3) for k in Kbox])
print("   box: b in", mp.nstr(X[0].a, 15), mp.nstr(X[0].b, 15), "; c in", mp.nstr(X[1].a, 15), mp.nstr(X[1].b, 15), "; gamma_C in", mp.nstr(X[2].a, 15), mp.nstr(X[2].b, 15))
# planted control: shift the center off the root by 1e-6 with the same radius -> must NOT certify
y2 = [y[0] + mp.mpf('1e-6'), y[1], y[2]]
X2 = [iv.mpf([yy - rad, yy + rad]) for yy in y2]
Y2 = [iv.mpf(yy) for yy in y2]
Fy2 = F_iv(*Y2)
JX2 = J_iv(*X2)
K2 = []
for i in range(3):
    acc = Y2[i] - sum(Ci[i][j] * Fy2[j] for j in range(3))
    for j in range(3):
        m_ij = (iv.mpf(1) if i == j else iv.mpf(0)) - sum(Ci[i][k] * JX2[k][j] for k in range(3))
        acc = acc + m_ij * (X2[j] - Y2[j])
    K2.append(acc)
print("   planted control (center displaced by 1e-6): certified =", all((K2[i].a > X2[i].a) and (K2[i].b < X2[i].b) for i in range(3)))
# check interval Jacobian against finite differences of F (guards the hand-coded derivative)
hh = mp.mpf('1e-20')
Jfd = mp.matrix(3, 3)
base = Fm(bS, cS, gS)
for j in range(3):
    arg = [bS, cS, gS]
    arg[j] += hh
    f2 = Fm(*arg)
    for i in range(3):
        Jfd[i, j] = (f2[i] - base[i]) / hh
print("   max |J_interval_mid - J_finite_difference| =", mp.nstr(max(abs(Jmid[i, j] - Jfd[i, j]) for i in range(3) for j in range(3)), 3))

# ---------------- (E) independent 12D rebuild ----------------
print("(E) independent 12D linear-Gaussian rebuild (float64)")
b, c, g = float(bS), float(cS), float(gS)
Bn = np.array([[0.1, b], [c, 0.1]])
Sn = (np.exp(2 * Bn) - 1) + np.sqrt((np.exp(2 * Bn) - 1) ** 2 + (np.exp(2 * Bn) - 1))
gst = float(gstar)
Rs = np.exp(gst / 2) / (2 * np.pi * np.e)
En = np.array([float(x) for x in E])
coord = {(e, u, v): 4 * e + 2 * (u - 1) + (v - 1) for e in range(3) for u in (1, 2) for v in (1, 2)}


def slots(i, u):
    """list of (coordinate, SNR) opened by member i's policy u"""
    out = [((i, u, v), Sn[u - 1, v - 1]) for v in (1, 2)]              # outgoing edge i -> i+1
    out += [(((i - 1) % 3, x, u), Sn[x - 1, u - 1]) for x in (1, 2)]    # incoming edge i-1 -> i
    return out


def G_first_principles(s, Bpert=None):
    Lam = np.eye(12)       # posterior precision of eta
    psi = 0.0
    for i, u in enumerate(s):
        if u == 0:
            continue
        for key, S in slots(i, u):
            h = np.zeros(12)
            h[coord[key]] = np.sqrt(Rs * S)
            Lam += np.outer(h, h) / Rs
            psi += 0.5 * np.log(2 * np.pi * np.e * Rs * (1 + S))   # cross-entropy of N(0,Rs(1+S)) with itself
    return -0.5 * np.linalg.slogdet(Lam)[1] + psi


G = np.zeros((3, 3, 3))
for s in states:
    G[s] = G_first_principles(s)
Gpair = np.zeros((3, 3, 3))
for s in states:
    Gpair[s] = sum(float(gv[x]) for x in s) + sum((Bn[s[i] - 1, s[(i + 1) % 3] - 1] if s[i] and s[(i + 1) % 3] else 0.0) for i in range(3))
print(f"   max |G_first_principles - (sum g + sum B)| = {np.abs(G - Gpair).max():.2e}")
red = G[1, 2, 0] - G[1, 0, 0] - G[0, 2, 0] + G[0, 0, 0]
print(f"   redundancy check I(o_B0(1); o_B1(2)) from G = {red:.12f}  vs B_12 = {b:.12f}")


def sync_stat(G, E3, gamma):
    lp = -gamma * G + np.log(E3)[:, None, None] + np.log(E3)[None, :, None] + np.log(E3)[None, None, :]
    P = np.exp(lp - lp.max())
    P /= P.sum()
    K = [P / P.sum(axis=i, keepdims=True) for i in range(3)]
    T = np.zeros((27, 27))
    for a_, s in enumerate(states):
        for b_, t in enumerate(states):
            pr = 1.0
            for i in range(3):
                u = list(s)
                u[i] = t[i]
                pr *= K[i][tuple(u)]
            T[a_, b_] = pr
    A_ = np.vstack([T.T - np.eye(27), np.ones(27)])
    rhs = np.zeros(28)
    rhs[-1] = 1
    return np.linalg.lstsq(A_, rhs, rcond=None)[0].reshape(3, 3, 3), P


def post(G, E3, gamma):
    lp = -gamma * G + np.log(E3)[:, None, None] + np.log(E3)[None, :, None] + np.log(E3)[None, None, :]
    P = np.exp(lp - lp.max())
    return P / P.sum()


ps, P1n = sync_stat(G, En, 1.0)
print(f"   TV(P_sync(1), P_C(gamma_C;E,G_C)) = {0.5 * np.abs(ps - post(G, En, g)).sum():.2e}")
print(f"   TV(P_sync(1), P_C(1;E,G_C))       = {0.5 * np.abs(ps - P1n).sum():.6e}")
# best gamma' scan as control that the match is specific
tvs = [(0.5 * np.abs(ps - post(G, En, gg)).sum(), gg) for gg in [0.0, 0.005, g, 0.02, 0.05, 0.5]]
print("   TV to P_C(gamma';E,G_C) for gamma' in [0,0.005,gamma_C,0.02,0.05,0.5]:", ["%.2e" % t for t, _ in tvs])
print("done")
