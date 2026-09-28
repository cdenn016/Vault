"""Exact algebra and constant checks for the Stage 4 early-parent path coupling.

Scope: algebraic identities of the four-cycle matching sector (exact rationals) and the
numerical values of explicit constants in stage4-early-parent-dynamics.md. No simulation;
these checks do not prove the theorem.
"""
import itertools
import math
import sympy as sp
import mpmath as mp


def residual(edge: int, channel: int) -> sp.Matrix:
    """Covector of r^b_edge (channel 0) or r^m_edge (channel 4); x=(k0..3, m0..3, w0..3)."""
    a = sp.zeros(12, 1)
    a[channel + edge] = -1
    a[channel + (edge + 1) % 4] = 1
    a[8 + edge] = -1
    return a


ab = [residual(e, 0) for e in range(4)]
am = [residual(e, 4) for e in range(4)]
I12 = sp.eye(12)
Dmat = sp.zeros(4, 12)
for i in range(4):
    Dmat[i, i] = 1
    Dmat[i, 4 + i] = -1
Rev = 2 * Dmat.T * Dmat


def edge_of(i: int, j: int) -> int:
    return i if (i + 1) % 4 == j else j


def H_of(S: tuple) -> sp.Matrix:
    H = sp.zeros(12, 12)
    for i, j in enumerate(S):
        g = edge_of(i, j)
        H += ab[g] * ab[g].T + am[g] * am[g].T
    return H


def dot(u: sp.Matrix, v: sp.Matrix):
    return (u.T * v)[0]


xcirc = sp.Matrix([0] * 8 + [1] * 4)
loop = sp.Matrix([0] * 8 + [1] * 4)
out = {}
out["|a^b|^2, a^b.a^m (same edge), |(a^b+a^m)/2|^2"] = (
    dot(ab[0], ab[0]), dot(ab[0], am[0]), dot((ab[1] + am[1]) / 2, (ab[1] + am[1]) / 2))

S0 = (1, 0, 3, 2)
S1 = (3, 2, 1, 0)
for name, M, (e, f), ext in [("S0", S0, (0, 2), (1, 3)), ("S1", S1, (1, 3), (0, 2))]:
    H = H_of(M)
    Pe, Pf = ab[e] + am[e], ab[f] + am[f]
    nc = (Pe + Pf) / 4                   # (n+_e + n+_f)/sqrt2
    z1 = (Pe - Pf) / 4                   # (n+_e - n+_f)/sqrt2
    z2 = (ab[e] - am[e]) / 2             # n-_e
    z3 = (ab[f] - am[f]) / 2             # n-_f
    rng = [nc, z1, z2, z3]
    assert sp.Matrix([[dot(u, v) for v in rng] for u in rng]) == sp.eye(4)
    for u, lam in zip(rng, [8, 8, 4, 4]):
        assert H * u == lam * u
    assert H.rank() == 4
    assert Rev * nc == sp.zeros(12, 1) and Rev * z1 == sp.zeros(12, 1)
    assert Rev * z2 == 4 * z2 and Rev * z3 == 4 * z3
    Prng = sum((u * u.T for u in rng), sp.zeros(12, 12))
    Pker = I12 - Prng
    assert Pker * Rev * Prng == sp.zeros(12, 12)
    RK = Pker * Rev * Pker
    out[f"{name}: eigenvalues of R_ev on ker H_M (with multiplicity, 8 dims + 4 zero from range)"] = RK.eigenvals()
    for g in ext:
        c = (ab[g] + am[g]) / 2
        assert all(dot(c, u) == 0 for u in (z1, z2, z3))
        out[f"{name}: c_{g}.n_c"] = dot(c, nc)
    assert all(dot(loop, u) == 0 for u in (z1, z2, z3))
    out[f"{name}: (z_+,z_1,z_2,z_3)(x_circ)"] = [dot(u, xcirc) for u in rng]
    v0 = xcirc + nc
    assert H * v0 == sp.zeros(12, 1) and Rev * v0 == sp.zeros(12, 1)   # K_M v0 = T v0
    assert Rev * nc == sp.zeros(12, 1)                                  # K_M nc = (8+T) nc
    assert (Pe + Pf) / 4 == nc                                            # p/4 = n_c
    out[f"{name}: |x_circ + n_c|^2"] = dot(v0, v0)
    for g in ext:
        assert dot(ab[g], v0) == sp.Rational(-3, 2) and dot(am[g], v0) == sp.Rational(-3, 2)
        assert dot(ab[g], nc) == sp.Rational(-1, 2) and dot(am[g], nc) == sp.Rational(-1, 2)
    for g in (e, f):
        assert dot(ab[g], v0) == 0 and dot(ab[g], nc) == 1 and dot(am[g], nc) == 1
    assert Prng * v0 == sp.zeros(12, 1)
    X = sp.Matrix(sp.symbols("x0:12"))
    zp_, z1_, z2_, z3_ = [dot(u, X) for u in rng]
    De = (dot(ab[e], X) ** 2 + dot(am[e], X) ** 2) / 2
    Df = (dot(ab[f], X) ** 2 + dot(am[f], X) ** 2) / 2
    assert sp.expand(De - (zp_ + z1_) ** 2 - z2_ ** 2) == 0
    assert sp.expand(Df - (zp_ - z1_) ** 2 - z3_ ** 2) == 0
    for g in ext:
        Dg = (dot(ab[g], X) ** 2 + dot(am[g], X) ** 2) / 2
        cgX = dot(ab[g] + am[g], X) / 2
        dgX = dot(ab[g] - am[g], X) / 2
        assert sp.expand(Dg - cgX ** 2 - dgX ** 2) == 0
    out[f"{name}: exact checks"] = "passed"

# sheet weights w_S proportional to det(K_S)^(-1/2); small-T exponents by high precision numerics
mp.mp.dps = 60
Hn = {S: mp.matrix(H_of(S).tolist()) for S in itertools.product(*[((i + 1) % 4, (i - 1) % 4) for i in range(4)])}
Revn = mp.matrix(Rev.tolist())


def logdet(S, Tv):
    K = Hn[S] + Tv * (mp.eye(12) + Revn)
    return mp.log(mp.det(K))


rows = {}
for S in Hn:
    r1 = 0.5 * (logdet(S0, mp.mpf("1e-10")) - logdet(S, mp.mpf("1e-10")))
    r2 = 0.5 * (logdet(S0, mp.mpf("1e-20")) - logdet(S, mp.mpf("1e-20")))
    slope = (r2 - r1) / (mp.log(mp.mpf("1e-20")) - mp.log(mp.mpf("1e-10")))
    rows[str(S)] = (float(slope), float(mp.e ** r1 / mp.mpf("1e-10") ** slope))
out["log(w_S/w_M) ~ slope*log T + log const: (slope, const)"] = rows

num = {}
num["row upper at eps t*<=(1+4ln10)/100"] = 0.5 + (1 + 4 * math.log(10)) / 200
num["row ratio 0.5511/0.4489"] = 0.5511 / 0.4489
num["1.23^4"] = 1.23 ** 4
num["mu(M) upper = 1.23^4/(1+1.23^4)"] = 1.23 ** 4 / (1 + 1.23 ** 4)
num["(1-mu)/mu lower = 1.23^-4"] = 1.23 ** -4
num["4(1+sqrt(8/3))"] = 4 * (1 + math.sqrt(8 / 3))
num["384*192"] = 384 * 192
num["192*400"] = 192 * 400
rho, eps = 0.01, 0.01
delta_eps = eps ** 2 / (8 * math.sqrt(3))
num["delta_eps at eps=1/100"] = delta_eps
R0 = rho + delta_eps
num["stationary slow-ball mass bound 2*(2pi)^-4*5^2*pi^4 R0^8/24"] = 2 * (2 * math.pi) ** -4 * 25 * math.pi ** 4 * R0 ** 8 / 24


def gap(theta_lo: float, x: float, R: float) -> float:
    c = math.exp(-x) * (1.5 - math.exp(-8 * theta_lo) / 2) - math.sqrt(2) * R
    return max(c, 0.0) ** 2 - 2 * (math.exp(-8 * theta_lo) + R) ** 2


for lab, R in [("Chebyshev tube R=rho+2delta", rho + 2 * delta_eps), ("O(1) tube R=rho+delta+1/20", rho + delta_eps + 0.05)]:
    num[f"g[{lab}] theta>=1/4, x<=1/10"] = gap(0.25, 0.1, R)
    num[f"g[{lab}] theta>=t_eps, x<=1/10"] = gap(2 * math.log(100), 0.1, R)
    lo, hi = 0.0, 2.0
    for _ in range(200):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if gap(0.25, mid, R) >= 1 else (lo, mid)
    num[f"max x=T(theta+h) with g>=1 [{lab}] theta>=1/4"] = lo
out["numerics"] = num

import scipy.integrate as si

Tv, a = 1e-3, 0.004
for rate in (8 + Tv, 4 + 5 * Tv):
    s2 = Tv / rate
    fz = lambda z: math.exp(-z * z / (2 * s2) + (a + z) ** 2 / Tv) / math.sqrt(2 * math.pi * s2)
    val = si.quad(fz, -1, 1, limit=400)[0]
    closed = (1 - 2 * s2 / Tv) ** -0.5 * math.exp(a * a / (Tv * (1 - 2 * s2 / Tv)))
    out[f"Gaussian identity, rate {rate}: quadrature vs closed form"] = (val, closed)

for kk, v in out.items():
    print(kk, ":", v)
