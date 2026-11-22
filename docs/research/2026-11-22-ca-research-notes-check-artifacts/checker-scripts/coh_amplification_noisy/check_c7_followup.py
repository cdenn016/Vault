"""Follow-up to check_bc.py: (i) size of the N=2 'exceedance', (ii) N=3 supremum vs best two-sender value, in world coordinates."""
import numpy as np, scipy.linalg as la
from scipy.optimize import minimize
rng = np.random.default_rng(11)
def spd(k, rng, scale=1.0):
    M = rng.standard_normal((k, k)); return scale * (M @ M.T + 0.2 * np.eye(k))
rho = lambda M: float(max(abs(la.eigvals(M))))
kap = lambda A, B: float(max(la.eigvalsh(A, B)) / min(la.eigvalsh(A, B)))
def edge(Pj, Hi, Ri):
    S = Hi @ Pj @ Hi.T + Ri
    return Pj @ Hi.T @ la.solve(S, Hi)
# (i) N=2: well-conditioned evaluation (finite s, eps) of the claimed optimizer and random + local search with bounded scale
worst = 0
for t in range(200):
    r = int(rng.integers(2, 4)); R1 = spd(r, rng); R2 = spd(r, rng, 10**rng.uniform(-1, 1))
    m = np.sqrt(kap(R1, R2)); target = (m+1)**2/(4*m)
    best = 0
    for q in range(300):
        L1 = rng.standard_normal((r, int(rng.integers(1, r+1)))) * 10**rng.uniform(-1, 4)
        L2 = rng.standard_normal((r, int(rng.integers(1, r+1)))) * 10**rng.uniform(-1, 4)
        X1 = L1 @ L1.T + 1e-6*np.eye(r); X2 = L2 @ L2.T + 1e-6*np.eye(r)
        best = max(best, rho(X1 @ la.inv(X1 + R2) @ X2 @ la.inv(X2 + R1)))
    worst = max(worst, best/target)
print(f"(i) N=2, 200 noise pairs x 300 random well-conditioned priors: max rho/closed-form sup = {worst:.6f} (must stay < 1)")
# (ii) N=3
def trace_limit(us, Rs):
    N = len(us); val = 1.0
    for i in range(N):
        un = us[(i+1) % N]; Ri = la.inv(Rs[i]); val *= (un @ Ri @ us[i]) / (un @ Ri @ un)
    return val
R = [np.diag([4.0, 1.0]), np.eye(2), np.diag([3.0, 2.0])]     # the note's own N=3 instance
pairs = {(i, j): (np.sqrt(kap(R[i], R[j])) + 1)**2/(4*np.sqrt(kap(R[i], R[j]))) for i in range(3) for j in range(i+1, 3)}
def g(th): return -abs(trace_limit([np.array([np.cos(x), np.sin(x)]) for x in th], R))
best = None
for q in range(200):
    res = minimize(g, rng.uniform(0, np.pi, 3), method='Nelder-Mead', options={'xatol': 1e-12, 'fatol': 1e-14})
    if best is None or res.fun < best.fun: best = res
us = [np.array([np.cos(x), np.sin(x)]) for x in best.x]
H = np.eye(2); s_, eps = 1e8, 1e-8
Ps = [s_*np.outer(u, u) + eps*np.eye(2) for u in us]
As = [edge(Ps[k], H, R[(k-1) % 3]) for k in range(3)]
Ac = As[0] @ As[2] @ As[1]
# Kantorovich upper bound of C6(2), minimized over the reference R_* (2x2 spd, 3 parameters), with s_j -> 1
def ub(p):
    L = np.array([[np.exp(p[0]), 0], [p[1], np.exp(p[2])]]); Rs_ = L @ L.T
    return np.prod([(kap(Ri, Rs_) + 1)/(2*np.sqrt(kap(Ri, Rs_))) for Ri in R])
ubest = min(minimize(ub, rng.standard_normal(3), method='Nelder-Mead', options={'xatol': 1e-10, 'fatol': 1e-12}).fun for q in range(40))
print(f"(ii) note's N=3 instance R=diag(4,1), I, diag(3,2): two-sender values {{(a,b): value}} = { {k: round(v, 6) for k, v in pairs.items()} }")
print(f"     best rank-one-limit trace found = {-best.fun:.6f}; world-coordinate rho(A_c) at s=1e8, eps=1e-8 with those directions = {rho(Ac):.6f}")
print(f"     C6(2) upper bound minimized over the reference (snr factors -> 1) = {ubest:.6f}")
