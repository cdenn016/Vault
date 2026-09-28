"""Exact algebra and constant checks for the Stage 4 early-parent path coupling."""
import itertools, math
import sympy as sp
import mpmath as mp

def residual(edge, channel):
    a = sp.zeros(12, 1); a[channel + edge] = -1; a[channel + (edge + 1) % 4] = 1; a[8 + edge] = -1
    return a
ab = [residual(e, 0) for e in range(4)]; am = [residual(e, 4) for e in range(4)]
I12 = sp.eye(12); Dmat = sp.zeros(4, 12)
for i in range(4): Dmat[i, i] = 1; Dmat[i, 4 + i] = -1
Rev = 2 * Dmat.T * Dmat
def edge_of(i, j): return i if (i + 1) % 4 == j else j
def H_of(S):
    H = sp.zeros(12, 12)
    for i, j in enumerate(S):
        g = edge_of(i, j); H += ab[g] * ab[g].T + am[g] * am[g].T
    return H
def dot(u, v): return (u.T * v)[0]
xcirc = sp.Matrix([0] * 8 + [1] * 4); loop = sp.Matrix([0] * 8 + [1] * 4)
S0, S1 = (1, 0, 3, 2), (3, 2, 1, 0)
for M, (e, f), ext in [(S0, (0, 2), (1, 3)), (S1, (1, 3), (0, 2))]:
    H = H_of(M); Pe, Pf = ab[e] + am[e], ab[f] + am[f]
    nc, z1, z2, z3 = (Pe + Pf) / 4, (Pe - Pf) / 4, (ab[e] - am[e]) / 2, (ab[f] - am[f]) / 2
    rng = [nc, z1, z2, z3]
    assert sp.Matrix([[dot(u, v) for v in rng] for u in rng]) == sp.eye(4)
    for u, lam in zip(rng, [8, 8, 4, 4]): assert H * u == lam * u
    assert H.rank() == 4 and Rev * nc == sp.zeros(12, 1) and Rev * z1 == sp.zeros(12, 1)
    assert Rev * z2 == 4 * z2 and Rev * z3 == 4 * z3
    Prng = sum((u * u.T for u in rng), sp.zeros(12, 12)); Pker = I12 - Prng
    assert Pker * Rev * Prng == sp.zeros(12, 12)
    print("eigenvalues of Pker Rev Pker:", (Pker * Rev * Pker).eigenvals())
    for g in ext:
        c = (ab[g] + am[g]) / 2
        assert all(dot(c, u) == 0 for u in (z1, z2, z3)); print("c_g.n_c =", dot(c, nc))
    assert all(dot(loop, u) == 0 for u in (z1, z2, z3))
    print("(z+,z1,z2,z3)(xcirc) =", [dot(u, xcirc) for u in rng])
    v0 = xcirc + nc
    assert H * v0 == sp.zeros(12, 1) and Rev * v0 == sp.zeros(12, 1) and (Pe + Pf) / 4 == nc
    for g in ext:
        assert dot(ab[g], v0) == dot(am[g], v0) == sp.Rational(-3, 2)
        assert dot(ab[g], nc) == dot(am[g], nc) == sp.Rational(-1, 2)
    for g in (e, f): assert dot(ab[g], v0) == 0 and dot(ab[g], nc) == 1 and dot(am[g], nc) == 1
    X = sp.Matrix(sp.symbols("x0:12")); zp_, z1_, z2_, z3_ = [dot(u, X) for u in rng]
    De = (dot(ab[e], X) ** 2 + dot(am[e], X) ** 2) / 2; Df = (dot(ab[f], X) ** 2 + dot(am[f], X) ** 2) / 2
    assert sp.expand(De - (zp_ + z1_) ** 2 - z2_ ** 2) == 0 and sp.expand(Df - (zp_ - z1_) ** 2 - z3_ ** 2) == 0
    for g in ext:
        Dg = (dot(ab[g], X) ** 2 + dot(am[g], X) ** 2) / 2
        assert sp.expand(Dg - (dot(ab[g] + am[g], X) / 2) ** 2 - (dot(ab[g] - am[g], X) / 2) ** 2) == 0
mp.mp.dps = 60
Hn = {S: mp.matrix(H_of(S).tolist()) for S in itertools.product(*[((i + 1) % 4, (i - 1) % 4) for i in range(4)])}
Revn = mp.matrix(Rev.tolist())
logdet = lambda S, Tv: mp.log(mp.det(Hn[S] + Tv * (mp.eye(12) + Revn)))
for S in Hn:
    r1 = (logdet(S0, mp.mpf("1e-10")) - logdet(S, mp.mpf("1e-10"))) / 2
    r2 = (logdet(S0, mp.mpf("1e-20")) - logdet(S, mp.mpf("1e-20"))) / 2
    slope = (r2 - r1) / (mp.log(mp.mpf("1e-20")) - mp.log(mp.mpf("1e-10")))
    print(S, "w_S/w_M ~", float(mp.e ** r1 / mp.mpf("1e-10") ** slope), "* T^", float(slope))
def gap(th, x, R):
    c = math.exp(-x) * (1.5 - math.exp(-8 * th) / 2) - math.sqrt(2) * R
    return max(c, 0.0) ** 2 - 2 * (math.exp(-8 * th) + R) ** 2
d = 1e-4 / (8 * math.sqrt(3))
for R in (0.01 + 2 * d, 0.01 + d + 0.05):
    print(R, gap(0.25, 0.1, R), gap(2 * math.log(100), 0.1, R))
