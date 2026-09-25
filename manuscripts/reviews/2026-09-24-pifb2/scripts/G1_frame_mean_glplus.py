r"""G1 check (c): the frame mean eq:meta_agent_frame_barycenter on GL+(K) with d(U,V) = ||log(U^{-1}V)||_F.

 (1) d is not a metric on GL+(2): domain gaps (no real principal log) and triangle-inequality violations.
 (2) d is not the Riemannian distance of the left-invariant Frobenius metric: discrete-path upper bound on
     d_Riem(I, exp X) is strictly below ||X||_F for non-normal X.
 (3) Afsari hypotheses for GL+(2) with the left-invariant Frobenius metric: sectional-curvature upper bound
     Delta computed from the left-invariant Levi-Civita connection (formula validated on so(3): K = 1/8).
 (4) Two-minimizer counterexample for sum_i w_i d(U,U_i)^2 on GL+(2) (and three for the cyclic triple).
 (5) Convexity of t -> d(exp(tZ), V)^2 at t=0 along one-parameter subgroups: radius where it fails.
 (6) The fixed-point iteration M <- M exp(sum_i w_i log(M^{-1}U_i)) (the Karcher Gauss-Newton step):
     convergence, and whether its fixed point (the exponential barycenter of Pennec-Arsigny) is a stationary
     point of the Frechet objective built from d; left/right equivariance of both objects.
"""
import warnings; warnings.filterwarnings("ignore")
import numpy as np
from scipy.linalg import expm, logm
from scipy.optimize import minimize
rng = np.random.default_rng(3)

def rlog(A):
    ev = np.linalg.eigvals(A)
    if np.any((abs(ev.imag) < 1e-12) & (ev.real <= 0)): return None
    L = logm(A)
    if np.max(abs(np.imag(L))) > 1e-9: return None
    return np.real(L)

def d(U, V):
    L = rlog(np.linalg.solve(U, V)); return np.inf if L is None else np.linalg.norm(L)

# (1) domain gaps and triangle inequality
Ms = [rng.standard_normal((2, 2)) for _ in range(20000)]; Ms = [M for M in Ms if np.linalg.det(M) > 0]
gaps = sum(rlog(M) is None for M in Ms)
viol = []; tested = 0
for _ in range(20000):
    s = rng.uniform(0.2, 2.0)
    X, Y = rng.standard_normal((2, 2))*s, rng.standard_normal((2, 2))*s
    A = np.eye(2); Bm = expm(X); C = expm(X)@expm(Y)
    dAB, dBC, dAC = d(A, Bm), d(Bm, C), d(A, C)
    if np.isfinite(dAB + dBC + dAC):
        tested += 1
        if dAC > dAB + dBC + 1e-9: viol.append((dAC - dAB - dBC, dAC, dAB, dBC, np.linalg.norm(X), np.linalg.norm(Y)))
viol.sort(reverse=True)
print(f"(1) det>0 random 2x2 matrices with no real principal log: {gaps} of {len(Ms)}")
print(f"    triangle inequality d(A,C) <= d(A,B)+d(B,C): {len(viol)} violations in {tested} finite triples")
if viol:
    v = viol[0]; print(f"    worst: excess {v[0]:.4f}; d(A,C)={v[1]:.4f}, d(A,B)={v[2]:.4f}, d(B,C)={v[3]:.4f}")
    small = [v for v in viol if max(v[2], v[3]) < 1.0]
    if small: s = max(small); print(f"    largest violation with both legs < 1: excess {s[0]:.4f} (d(A,C)={s[1]:.3f}, d(A,B)={s[2]:.3f}, d(B,C)={s[3]:.3f})")

# (2) discrete-path upper bound on the left-invariant Riemannian distance
def path_len(params, V, N, LV):
    Us = [np.eye(2)]
    for k in range(1, N):
        Us.append(expm((k/N)*LV)@expm(params[4*(k - 1):4*k].reshape(2, 2)))
    Us.append(V); tot = 0.0
    for a, b in zip(Us[:-1], Us[1:]):
        L = rlog(np.linalg.solve(a, b)); tot += 1e6 if L is None else np.linalg.norm(L)
    return tot
for X in (np.array([[0.0, 2.0], [0.0, 0.0]]), np.array([[0.5, 3.0], [0.0, -0.5]]), np.array([[0.0, -1.0], [1.0, 0.0]])):
    V = expm(X); N = 12
    res = minimize(path_len, np.zeros(4*(N - 1)), args=(V, N, X), method='BFGS', options=dict(maxiter=300))
    normal = np.allclose(X@X.T, X.T@X)
    print(f"(2) X={X.tolist()} (normal={normal}): ||X||_F = {np.linalg.norm(X):.4f}; discrete-path upper bound on d_Riem = {res.fun:.4f}")

# (3) sectional curvature of the left-invariant Frobenius metric
def br(A, B): return A@B - B@A
def nabla(X, Y): return 0.5*(br(X, Y) - br(X.T, Y) - br(Y.T, X))
def sec(X, Y):
    Rm = nabla(X, nabla(Y, Y)) - nabla(Y, nabla(X, Y)) - nabla(br(X, Y), Y)
    return np.sum(Rm*X)/(np.sum(X*X)*np.sum(Y*Y) - np.sum(X*Y)**2)
Ex = np.zeros((3, 3)); Ex[1, 2], Ex[2, 1] = -1, 1; Ey = np.zeros((3, 3)); Ey[0, 2], Ey[2, 0] = 1, -1
Ex /= np.linalg.norm(Ex); Ey /= np.linalg.norm(Ey)
print(f"(3) validation: so(3) Frobenius-orthonormal plane, K = {sec(Ex, Ey):.6f} (expected 0.125)")
best = -np.inf; worst = np.inf
for _ in range(20000):
    X, Y = rng.standard_normal((2, 2)), rng.standard_normal((2, 2))
    k = sec(X, Y); best = max(best, k); worst = min(worst, k)
f = lambda p: -sec(p[:4].reshape(2, 2), p[4:].reshape(2, 2))
bestopt = max(-minimize(f, rng.standard_normal(8), method='Nelder-Mead', options=dict(maxiter=4000)).fun for _ in range(20))
Delta = max(best, bestopt)
print(f"    gl(2) left-invariant Frobenius: sampled K in [{worst:.4f}, {best:.4f}]; optimized max K = {bestopt:.6f}")
inj_ub = np.sqrt(2)*np.pi
print(f"    SO(2) loop exp(tJ) is a geodesic of length {2*inj_ub:.4f}, so inj <= {inj_ub:.4f}")
print(f"    Afsari r_cx = 0.5 min(inj, pi/sqrt(Delta)) <= 0.5 min({inj_ub:.4f}, {np.pi/np.sqrt(Delta):.4f})")

# (4) multiple minimizers of the Frechet objective built from d
def frechet(M, Us, w): return sum(wi*d(M, U)**2 for wi, U in zip(w, Us))
def Rot(a): return np.array([[np.cos(a), -np.sin(a)], [np.sin(a), np.cos(a)]])
cases = [("pair R(+-pi/2)", [Rot(np.pi/2), Rot(-np.pi/2)]), ("cyclic triple R(2pi j/3)", [Rot(2*np.pi*j/3) for j in range(3)])]
for label, Us in cases:
    w = np.ones(len(Us))/len(Us); sols = []
    def g(p):
        v = frechet(expm(p.reshape(2, 2)), Us, w)
        return v if np.isfinite(v) else 1e6
    for _ in range(40):
        r = minimize(g, rng.standard_normal(4)*0.8, method='Nelder-Mead', options=dict(maxiter=3000, xatol=1e-10, fatol=1e-12))
        sols.append((r.fun, expm(r.x.reshape(2, 2))))
    fmin = min(s[0] for s in sols); mins = []
    for fv, M in sols:
        if fv < fmin + 1e-6 and not any(np.linalg.norm(M - M2) < 1e-3 for M2 in mins): mins.append(M)
    print(f"(4) {label}: global min value {fmin:.6f}; distinct global minimizers found: {len(mins)}")
    for M in mins: print("       ", np.round(M, 4).tolist())

# (5) convexity along one-parameter subgroups
def g2(Z, V, h=1e-4):
    gp = d(expm(h*Z), V)**2; g0 = d(np.eye(2), V)**2; gm = d(expm(-h*Z), V)**2
    return (gp - 2*g0 + gm)/h**2
for r in (0.25, 0.5, 1.0, 1.5, 2.0, 3.0):
    worst = np.inf
    for _ in range(3000):
        L = rng.standard_normal((2, 2)); L *= r/np.linalg.norm(L); Z = rng.standard_normal((2, 2)); Z /= np.linalg.norm(Z)
        val = g2(Z, expm(L))
        if np.isfinite(val): worst = min(worst, val)
    print(f"(5) norm of log V = {r:4.2f}: min over 3000 (L,Z) of second derivative of d^2 along exp(tZ) = {worst:+.4f} (flat value 2)")

# (6) exponential-barycenter iteration vs Frechet stationarity; equivariance
def expbar(Us, w, M0=None, iters=300):
    M = np.eye(2) if M0 is None else M0
    for it in range(iters):
        Ls = [rlog(np.linalg.solve(M, U)) for U in Us]
        if any(L is None for L in Ls): return None, it
        S = sum(wi*L for wi, L in zip(w, Ls)); M = M@expm(S)
        if np.linalg.norm(S) < 1e-14: return M, it
    return M, iters
def grad_fd(M, Us, w, h=1e-6):
    G = np.zeros((2, 2))
    for a in range(2):
        for b in range(2):
            E = np.zeros((2, 2)); E[a, b] = 1
            G[a, b] = (frechet(M@expm(h*E), Us, w) - frechet(M@expm(-h*E), Us, w))/(2*h)
    return G
def argmin_from(M0, Us, w):
    obj = lambda p: frechet(M0@expm(p.reshape(2, 2)), Us, w)
    r = minimize(obj, np.zeros(4), method='BFGS', options=dict(gtol=1e-11))
    return M0@expm(r.x.reshape(2, 2))
for spread in (0.1, 0.5, 1.0, 1.5):
    Us = [expm(spread*rng.standard_normal((2, 2))/2) for _ in range(4)]; w = rng.dirichlet(np.ones(4))
    Mb, it = expbar(Us, w)
    if Mb is None:
        print(f"(6) spread {spread}: iteration left the log domain at step {it}"); continue
    add = expm(sum(wi*rlog(U) for wi, U in zip(w, Us)))
    Mf = argmin_from(Mb, Us, w)
    h = expm(rng.standard_normal((2, 2))*0.7); gg = expm(rng.standard_normal((2, 2))*0.7)
    MbL, _ = expbar([h@U for U in Us], w, M0=h@Mb); MbR, _ = expbar([U@gg for U in Us], w, M0=Mb@gg)
    MfL = argmin_from(h@Mf, [h@U for U in Us], w); MfR = argmin_from(Mf@gg, [U@gg for U in Us], w)
    print(f"(6) spread {spread}: exp-barycenter converged in {it} steps; grad norm of Frechet(d) there = {np.linalg.norm(grad_fd(Mb, Us, w)):.2e}; "
          f"d(expbar, Frechet min) = {d(Mb, Mf):.2e}; d(additive average, expbar) = {d(add, Mb):.2e}")
    print(f"      equivariance residuals: expbar left {np.linalg.norm(MbL - h@Mb):.1e}, right {np.linalg.norm(MbR - Mb@gg):.1e}; "
          f"Frechet-min left {np.linalg.norm(MfL - h@Mf):.1e}, right {np.linalg.norm(MfR - Mf@gg):.1e}")
