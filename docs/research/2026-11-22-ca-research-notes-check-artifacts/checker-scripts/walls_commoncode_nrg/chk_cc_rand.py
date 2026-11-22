# (1) adversarial random test of C2 (frozen rank-one common code, directed graphs) at extreme scales + iff criterion
# (2) random search against the narrowed conjecture (C5): periodic rank-one common code, Gamma_i(t) in {0, Gamma_i}
import numpy as np, time
rng = np.random.default_rng(424242)
def spd(K, lo=-3, hi=3):
    Q, _ = np.linalg.qr(rng.normal(size=(K, K))); return Q @ np.diag(10.0**rng.uniform(lo, hi, K)) @ Q.T
def Wrec(Lam, Gam, J, T, alpha):
    N = len(Lam); K = Lam[0].shape[0]; W = np.zeros((N*K, N*K)); TT = np.outer(T, T); post = []
    for i in range(N):
        Lp = Lam[i] + Gam[i] + sum(alpha[j] for j in J[i])*TT
        Pp = np.linalg.inv(Lp); post.append(Pp)
        W[i*K:(i+1)*K, i*K:(i+1)*K] = Pp @ Lam[i]
        for j in J[i]: W[i*K:(i+1)*K, j*K:(j+1)*K] = alpha[j]*Pp @ TT
    return W, post
def sinks(N, J):
    R = np.eye(N, dtype=bool)
    for i in range(N):
        for j in J[i]: R[i, j] = True
    for k in range(N): R = R | (R[:, [k]] & R[[k], :])
    out = []
    for i in range(N):
        C = frozenset(np.where(R[i] & R[:, i])[0])
        if frozenset(np.where(R[i])[0]) == C and C not in out: out.append(C)
    return out
t0 = time.time(); worst = 0.0; nviol = 0; ncrit = [0, 0]; mism = 0; n = 0
while n < 4000:
    N = int(rng.integers(1, 6)); K = int(rng.integers(1, 5)); T = rng.normal(size=K)*10.0**rng.uniform(-2, 2)
    dens = rng.uniform(); J = [[j for j in range(N) if j != i and rng.uniform() < dens] for i in range(N)]
    P = [spd(K) for _ in range(N)]; Lam = [np.linalg.inv(p) for p in P]
    th = 10.0**rng.uniform(-2, 2, N); alpha = [th[j]**2/(1 + th[j]**2*(T @ P[j] @ T)) for j in range(N)]
    Hs = []
    for i in range(N):
        r = int(rng.integers(0, K+1)); Hs.append(rng.normal(size=(r, K))*10.0**rng.uniform(-2, 2))
    Gam = [h.T @ h for h in Hs]
    W, _ = Wrec(Lam, Gam, J, T, alpha); ev = np.linalg.eigvals(W); n += 1
    out = np.abs(ev)[(np.abs(ev - 1) > 1e-5)]
    if out.size: worst = max(worst, out.max())
    if out.size and out.max() > 1 - 1e-12 and np.any((np.abs(ev) >= 1-1e-12) & (np.abs(ev-1) > 1e-5)): nviol += 1
    crit = all(np.linalg.matrix_rank(np.vstack([Hs[i], T[None, :]])) == K for i in range(N)) and \
           all(any(Hs[i].shape[0] >= K and np.linalg.matrix_rank(Hs[i]) == K for i in C) for C in sinks(N, J))
    ncrit[int(crit)] += 1
    has1 = np.linalg.svd(W - np.eye(N*K), compute_uv=False)[-1] < 1e-11*max(1, np.linalg.norm(W, 2))
    if crit == has1: mism += 1
print("C2 extreme-scale test: %d instances, eigenvalues with |l|>=1 other than 1: %d; max |l| among l!=1: %.12f; criterion true/false=%s; criterion-vs-(1 in spectrum) mismatches=%d  [%.1fs]" % (n, nviol, worst, ncrit[::-1], mism, time.time()-t0))
# negative control: distinct codes
best = 0
for _ in range(500):
    K = 2; Lam = [np.linalg.inv(spd(K, -1, 1)) for _ in range(2)]; P = [np.linalg.inv(l) for l in Lam]
    Ts = [rng.normal(size=K), rng.normal(size=K)]
    W = np.zeros((4, 4))
    for i, j in ((0, 1), (1, 0)):
        a = 1/(1 + Ts[j] @ P[j] @ Ts[j]); B = a*np.outer(Ts[j], Ts[j]); Pp = np.linalg.inv(Lam[i] + B)
        W[2*i:2*i+2, 2*i:2*i+2] = Pp @ Lam[i]; W[2*i:2*i+2, 2*j:2*j+2] = Pp @ B
    best = max(best, np.abs(np.linalg.eigvals(W)).max())
print("  negative control (two distinct codes): max rho = %.4f (>1 => test can fail)" % best)

def orbit_rho(prof, T, th, f, Q, N, K, iters=3000, tol=1e-13):
    Ps = [Q/(1-f*f) for _ in range(N)]
    for it in range(iters):
        P0 = [p.copy() for p in Ps]
        for (Gam, J) in prof:
            alpha = [th[j]**2/(1 + th[j]**2*(T @ Ps[j] @ T)) for j in range(N)]
            _, post = Wrec([np.linalg.inv(p) for p in Ps], Gam, J, T, alpha); Ps = [f*f*p + Q for p in post]
        if max(np.abs(Ps[i]-P0[i]).max()/np.abs(P0[i]).max() for i in range(N)) < tol: break
    else: return None
    Wp = np.eye(N*K)
    for (Gam, J) in prof:
        alpha = [th[j]**2/(1 + th[j]**2*(T @ Ps[j] @ T)) for j in range(N)]
        W, post = Wrec([np.linalg.inv(p) for p in Ps], Gam, J, T, alpha); Wp = W @ Wp; Ps = [f*f*p + Q for p in post]
    return np.abs(np.linalg.eigvals(Wp)).max()
# positive control: C4 (two sensors per agent) must be detected by this code
T = np.array([1.0, 0.0]); th = np.array([100.0, 100.0])
G0 = [np.outer(200*np.array([1, .3]), 200*np.array([1, .3])), np.outer(200*np.array([1, -.3]), 200*np.array([1, -.3]))]
G1 = [np.outer(100*np.array([1, .35]), 100*np.array([1, .35])), np.outer(100*np.array([1, -.35]), 100*np.array([1, -.35]))]
print("  positive control C4 via this code: rho_rec = %.9f (note: 1.017037886)" % orbit_rho([(G0, [[1], [0]]), (G1, [[], []])], T, th, 0.995, np.eye(2), 2, 2))
t0 = time.time(); mx = 0.0; cnt = 0; nonconv = 0; arg = None
while time.time() - t0 < 38:
    N = int(rng.integers(2, 4)); K = int(rng.integers(2, 4)); p = int(rng.integers(2, 4))
    T = rng.normal(size=K); th = 10.0**rng.uniform(-1, 2.3, N); f = rng.uniform(0.8, 0.999)
    Q = np.eye(K) if rng.uniform() < 0.5 else spd(K, -1, 1)
    Gfix = []
    for i in range(N):
        r = int(rng.integers(1, K+1)); h = rng.normal(size=(r, K))*10.0**rng.uniform(-1, 2.5); Gfix.append(h.T @ h)
    prof = []
    for t in range(p):
        Gam = [Gfix[i] if rng.uniform() < 0.6 else np.zeros((K, K)) for i in range(N)]
        J = [[j for j in range(N) if j != i and rng.uniform() < 0.6] for i in range(N)]
        prof.append((Gam, J))
    r = orbit_rho(prof, T, th, f, Q, N, K)
    if r is None: nonconv += 1; continue
    cnt += 1
    if r > mx: mx = r; arg = (N, K, p, f)
print("C5 random search: %d converged periodic single-sensor profiles (%d not converged, skipped); max rho(W^(p))/f^p = %.12f at (N,K,p,f)=%s" % (cnt, nonconv, mx, arg))
