r"""L02: Gaussian Fisher-Rao metric, the 1/2 covariance factor, and sectional curvature.

Checks PIFB2.tex lines 167-186, 429, 462, 2621-2635:
  (a) KL second-order jet equals (1/2) g with g = dmu^T Sigma^-1 dmu + (1/2) tr(S^-1 dS S^-1 dS);
  (b) K=1 curvature is -1/2 (hyperbolic);
  (c) K=2: pure-mean plane at Sigma=I has sectional curvature +1/4 (claim at line 429);
      covariance planes are <= 0; mixed sign overall.
"""
import sympy as sp
import numpy as np
import itertools

def fisher_metric(K):
    mu = sp.symbols(f"m1:{K+1}")
    sig = []
    idx = []
    for i in range(K):
        for j in range(i, K):
            s = sp.Symbol(f"s{i}{j}")
            sig.append(s); idx.append((i, j))
    S = sp.zeros(K, K)
    for s, (i, j) in zip(sig, idx):
        S[i, j] = s; S[j, i] = s
    coords = list(mu) + sig
    n = len(coords)
    Si = S.inv()
    g = sp.zeros(n, n)
    # mean block
    for a in range(K):
        for b in range(K):
            g[a, b] = Si[a, b]
    # covariance block: 1/2 tr(Si dS_a Si dS_b)
    E = []
    for (i, j) in idx:
        M = sp.zeros(K, K); M[i, j] = 1; M[j, i] = 1
        E.append(M)
    for a in range(len(sig)):
        for b in range(len(sig)):
            g[K+a, K+b] = sp.Rational(1, 2) * (Si*E[a]*Si*E[b]).trace()
    return coords, g, S, K

def riemann_sectional(coords, g, point, pairs):
    n = len(coords)
    ginv = g.inv()
    Gam = [[[sp.simplify(sum(ginv[a, e]*(sp.diff(g[e, b], coords[c]) + sp.diff(g[e, c], coords[b]) - sp.diff(g[b, c], coords[e])) for e in range(n))/2)
             for c in range(n)] for b in range(n)] for a in range(n)]
    subs = dict(zip(coords, point))
    Gn = np.array([[[float(Gam[a][b][c].subs(subs)) for c in range(n)] for b in range(n)] for a in range(n)])
    dG = np.array([[[[float(sp.diff(Gam[a][b][c], coords[d]).subs(subs)) for d in range(n)] for c in range(n)] for b in range(n)] for a in range(n)])
    gn = np.array(g.subs(subs), dtype=float)
    # R^a_{bcd} = d_c Gam^a_{db} - d_d Gam^a_{cb} + Gam^a_{ce} Gam^e_{db} - Gam^a_{de} Gam^e_{cb}
    R = np.zeros((n, n, n, n))
    for a, b, c, d in itertools.product(range(n), repeat=4):
        R[a, b, c, d] = dG[a, d, b, c] - dG[a, c, b, d] + sum(Gn[a, c, e]*Gn[e, d, b] - Gn[a, d, e]*Gn[e, c, b] for e in range(n))
    def sec(X, Y):
        num = np.einsum('abcd,b,c,d,ae,e->', R, Y, X, Y, gn, X)
        den = (X@gn@X)*(Y@gn@Y) - (X@gn@Y)**2
        return num/den
    return sec, gn, n

# (a) KL jet vs metric, K=2, random point
rng = np.random.default_rng(0)
def kl(m1, S1, m2, S2):
    K = len(m1); S2i = np.linalg.inv(S2); d = m2-m1
    return 0.5*(np.log(np.linalg.det(S2)/np.linalg.det(S1)) + np.trace(S2i@S1) + d@S2i@d - K)
K = 2
A = rng.standard_normal((K, K)); S0 = A@A.T + 0.5*np.eye(K); m0 = rng.standard_normal(K)
dm = rng.standard_normal(K); B = rng.standard_normal((K, K)); dS = (B+B.T)/2
S0i = np.linalg.inv(S0)
gval = dm@S0i@dm + 0.5*np.trace(S0i@dS@S0i@dS)
for h in [1e-2, 1e-3]:
    val = kl(m0, S0, m0+h*dm, S0+h*dS)
    print(f"(a) KL(theta||theta+h v)/h^2 = {val/h**2:.10f}   (1/2) g(v,v) = {0.5*gval:.10f}   rel.err = {abs(val/h**2-0.5*gval)/(0.5*gval):.2e}  (h={h})")
gval_wrong = dm@S0i@dm + 1.0*np.trace(S0i@dS@S0i@dS)
print(f"    same check with factor 1 on covariance block: rel.err = {abs(kl(m0,S0,m0+1e-3*dm,S0+1e-3*dS)/1e-6-0.5*gval_wrong)/(0.5*gval_wrong):.2e}")

# (b) K=1
coords, g, S, _ = fisher_metric(1)
sec, gn, n = riemann_sectional(coords, g, [0.3, 1.7], None)
print("(b) K=1 sectional curvature (mu, sigma^2 plane):", sec(np.array([1., 0.]), np.array([0., 1.])), " expected -0.5")

# (c) K=2 at Sigma = I and at a random SPD point
coords, g, S, _ = fisher_metric(2)
for label, pt in [("Sigma=I", [0.0, 0.0, 1.0, 0.0, 1.0]), ("Sigma=[[2,0.7],[0.7,1.3]]", [0.4, -1.1, 2.0, 0.7, 1.3])]:
    sec, gn, n = riemann_sectional(coords, g, pt, None)
    e = np.eye(n)
    print(f"(c) K=2 at {label}:")
    print("    K(mu1,mu2) =", round(sec(e[0], e[1]), 12))
    vals = []
    for i, j in itertools.combinations(range(n), 2):
        vals.append(((i, j), sec(e[i], e[j])))
    cov_planes = [v for (ij, v) in vals if ij[0] >= 2]
    print("    coordinate-plane curvatures:", [(ij, round(v, 6)) for ij, v in vals])
    print("    max over covariance-only coordinate planes:", round(max(cov_planes), 12))
    # random planes
    ks = []
    for _ in range(4000):
        X = rng.standard_normal(n); Y = rng.standard_normal(n)
        ks.append(sec(X, Y))
    ks = np.array(ks)
    print(f"    random planes: min {ks.min():.4f}, max {ks.max():.4f}")
    # random covariance-only planes
    kc = []
    for _ in range(2000):
        X = np.r_[0, 0, rng.standard_normal(3)]; Y = np.r_[0, 0, rng.standard_normal(3)]
        kc.append(sec(X, Y))
    print(f"    random covariance-only planes: max {max(kc):.3e} (should be <= 0)")
