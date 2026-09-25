r"""G1 check (a): lem:weight_contraction (PIFB2.tex 1636-1641).

Map T(qbar) = implementation barycenter (eq:meta_agent_mu_impl, eq:meta_agent_sigma_impl, dispersion dropped)
with weights w_i = chi_i exp[-KL(N(mu_i,S_i) || N(mubar,Sbar))], (mu_i,S_i) already in the parent frame.
Coordinates x = (mu, Sigma) with the Euclidean/Frobenius norm. Lip measured as the spectral norm of the
finite-difference Jacobian (orthonormal basis of Sym under Frobenius).
Parts:
 (1) Lip on the convex hull H of constituents and on a fixed bounded ball, versus eps = max pairwise KL, K=2,3.
 (2) Exact 1D pitchfork family: two constituents at +-a, identity covariance: T(m) = a tanh(a m), eps = 2 a^2;
     uniqueness is lost at eps = 2 (so any valid eps_0 <= 2 in these units).
 (3) Detector pass band (mean KL < tau log 2, tau = 0.05) does NOT imply the lemma hypothesis:
     one-parameter family (m outliers at distance D, n-m at 0, identity covariances): smallest n with two
     stable fixed points of T inside the pass band.
"""
import numpy as np
from scipy.linalg import expm, sqrtm
rng = np.random.default_rng(1)

def kl(m1, S1, m2, S2):
    K = len(m1); S2i = np.linalg.inv(S2); d = m2 - m1
    return 0.5*(np.trace(S2i@S1) + d@S2i@d - K + np.log(np.linalg.det(S2)/np.linalg.det(S1)))

def sym_basis(K):
    B = []
    for i in range(K):
        for j in range(i, K):
            E = np.zeros((K, K))
            if i == j: E[i, i] = 1.0
            else: E[i, j] = E[j, i] = 1/np.sqrt(2)
            B.append(E)
    return B

def T(mb, Sb, mus, Ss, chi):
    k = np.array([kl(m, S, mb, Sb) for m, S in zip(mus, Ss)])
    w = chi*np.exp(-(k - k.min())); w = w/w.sum()
    return sum(wi*m for wi, m in zip(w, mus)), sum(wi*S for wi, S in zip(w, Ss)), w

def lip(mb, Sb, mus, Ss, chi, h=1e-6):
    K = len(mb); B = sym_basis(K); cols = []
    dirs = [(np.eye(K)[i], np.zeros((K, K))) for i in range(K)] + [(np.zeros(K), E) for E in B]
    for dm, dS in dirs:
        mp, Sp, _ = T(mb + h*dm, Sb + h*dS, mus, Ss, chi)
        mm, Sm, _ = T(mb - h*dm, Sb - h*dS, mus, Ss, chi)
        dmu = (mp - mm)/(2*h); dSig = (Sp - Sm)/(2*h)
        cols.append(np.concatenate([dmu, [np.sum(dSig*E) for E in B]]))
    J = np.array(cols).T
    return np.linalg.norm(J, 2), max(abs(np.linalg.eigvals(J)))

def make_cluster(K, n, eps, base_S):
    A = [rng.standard_normal((K, K)) for _ in range(n)]; A = [(a + a.T)/2 for a in A]
    b = [rng.standard_normal(K) for _ in range(n)]
    R = np.real(sqrtm(base_S))
    def build(s):
        mus = [s*bi for bi in b]; Ss = [R@expm(s*a)@R for a in A]
        return mus, Ss
    def maxkl(s):
        mus, Ss = build(s)
        return max(kl(mus[i], Ss[i], mus[j], Ss[j]) for i in range(n) for j in range(n) if i != j)
    lo, hi = 0.0, 1.0
    while maxkl(hi) < eps: hi *= 2
    for _ in range(60):
        mid = 0.5*(lo + hi)
        if maxkl(mid) < eps: lo = mid
        else: hi = mid
    return build(lo)

print("(1) Lipschitz constant of T versus eps = max pairwise KL")
for K in (2, 3):
    base_S = np.diag(np.linspace(0.5, 2.0, K))
    print(f" K={K}, n=4, base spectrum [0.5,2.0]; columns: eps, max Lip on hull, max Lip on ball(R=1), Lip/eps (hull), Lip/sqrt(eps) (hull)")
    for eps in (1e-4, 1e-3, 1e-2, 0.035, 0.1, 0.3, 1.0):
        worst_h = 0.0; worst_b = 0.0
        for trial in range(6):
            mus, Ss = make_cluster(K, 4, eps, base_S); chi = np.ones(4)
            for _ in range(8):
                c = rng.dirichlet(np.ones(4))
                mb = sum(ci*m for ci, m in zip(c, mus)); Sb = sum(ci*S for ci, S in zip(c, Ss))
                worst_h = max(worst_h, lip(mb, Sb, mus, Ss, chi)[0])
                # ball: mean within distance 1, covariance = base congruence with spectrum kept in [0.25, 4]
                u = rng.standard_normal(K); u /= np.linalg.norm(u)
                mb2 = u*rng.uniform(0, 1); Q = np.linalg.qr(rng.standard_normal((K, K)))[0]
                Sb2 = Q@np.diag(rng.uniform(0.25, 4.0, K))@Q.T
                worst_b = max(worst_b, lip(mb2, Sb2, mus, Ss, chi)[0])
        print(f"   {eps:8.4g}  {worst_h:10.3e}  {worst_b:10.3e}  {worst_h/eps:8.3f}  {worst_h/np.sqrt(eps):8.3f}")

print("\n(2) Exact pitchfork: T(m) = a tanh(a m), eps = 2a^2, Lip on hull = a^2 = eps/2")
for eps in (1.0, 1.9, 2.0, 2.1, 3.0):
    a = np.sqrt(eps/2)
    # nonzero fixed points of m = a tanh(a m)
    m = a; 
    for _ in range(20000): m = a*np.tanh(a*m)
    # numerical check with the full T in K=1 (identity covariance): start at +a and -a
    mus = [np.array([a]), np.array([-a])]; Ss = [np.eye(1), np.eye(1)]; chi = np.ones(2)
    fps = []
    for m0 in (a, -a, 1e-3):
        mb, Sb = np.array([m0]), np.eye(1)
        for _ in range(5000): mb, Sb, _ = T(mb, Sb, mus, Ss, chi)
        fps.append(mb[0])
    print(f"  eps={eps:4.2f}: slope at 0 = {a*a:5.3f}; fixed points reached from +a,-a,1e-3: {fps[0]:+.4f}, {fps[1]:+.4f}, {fps[2]:+.4f}")

print("\n(3) Detector pass band vs lemma hypothesis: m outliers at D, n-m at 0, K=1, identity covariances, tau=0.05")
tau = 0.05; band = tau*np.log(2)
def fixed_points(n, m, D):
    mus = [np.array([D])]*m + [np.array([0.0])]*(n - m); Ss = [np.eye(1)]*n; chi = np.ones(n)
    out = []
    for m0 in (0.0, D):
        mb, Sb = np.array([m0]), np.eye(1)
        for _ in range(4000): mb, Sb, w = T(mb, Sb, mus, Ss, chi)
        out.append((mb[0], w))
    return out
found = None
for n in range(50, 2001, 10):
    for m in range(1, 4):
        for D in np.linspace(2.0, 8.0, 61):
            mean_kl = 2*m*(n - m)*(0.5*D*D)/n**2
            if mean_kl >= band: continue
            a_ = m/(n); 
            # quick scalar test via closed form f(x) = D*sigmoid(D x - D^2/2 + log(m/(n-m)))
            f = lambda x: D/(1 + np.exp(-(D*x - D*D/2 + np.log(m/(n - m)))))
            lo = 0.0; hi = D
            for _ in range(3000): lo = f(lo); hi = f(hi)
            if hi - lo > 0.5:
                found = (n, m, D, mean_kl, lo, hi); break
        if found: break
    if found: break
n, m, D, mk, lo, hi = found
print(f"  smallest n in scan: n={n}, m={m}, D={D:.2f}; unweighted mean KL = {mk:.5f} < tau log2 = {band:.5f}; Gamma = exp(-mean/tau) = {np.exp(-mk/tau):.3f}")
print(f"  max pairwise KL = D^2/2 = {D*D/2:.2f} (lemma hypothesis eps is violated by a factor {D*D/2/band:.0f} over the band value)")
fps = fixed_points(n, m, D)
for (mb, w), lab in zip(fps, ("start 0", "start D")):
    ebar_w = sum(w[i]*w[j]*0.5*(D*(i < m) - D*(j < m))**2 for i in range(n) for j in range(n))
    print(f"  full-T fixed point from {lab}: mubar = {mb:.4f}, outlier total weight = {w[:m].sum():.4f}, eps_w = {ebar_w:.4f}")
    # stability: derivative of scalar map
    h = 1e-6; mus = [np.array([D])]*m + [np.array([0.0])]*(n - m); Ss = [np.eye(1)]*n; chi = np.ones(n)
    dp = (T(np.array([mb + h]), np.eye(1), mus, Ss, chi)[0][0] - T(np.array([mb - h]), np.eye(1), mus, Ss, chi)[0][0])/(2*h)
    print(f"     local slope dT/dmu at this fixed point = {dp:.4f} (|slope|<1: stable)")
