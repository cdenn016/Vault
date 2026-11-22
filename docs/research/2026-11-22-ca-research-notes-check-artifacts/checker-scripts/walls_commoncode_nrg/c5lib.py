import numpy as np, mpmath as mp
def spd(rng, K, lo=-1, hi=1):
    Q, _ = np.linalg.qr(rng.normal(size=(K, K))); return Q @ np.diag(10.0**rng.uniform(lo, hi, K)) @ Q.T
def rnd_np(Ps, on, J, T, th, G, f, Q, build=True):
    N = len(Ps); K = len(T); TT = np.outer(T, T)
    al = [th[j]**2/(1 + th[j]**2*(T @ Ps[j] @ T)) for j in range(N)]
    W = np.zeros((N*K, N*K)); post = []
    for i in range(N):
        Lam = np.linalg.inv(Ps[i]); Lp = Lam + (G[i] if on[i] else 0) + sum(al[j] for j in J[i])*TT
        Pp = np.linalg.inv(Lp); post.append(f*f*Pp + Q)
        W[i*K:(i+1)*K, i*K:(i+1)*K] = Pp @ Lam
        for j in J[i]: W[i*K:(i+1)*K, j*K:(j+1)*K] = al[j]*Pp @ TT
    return W, post
def rho_np(inst, iters=4000, tol=1e-14):
    N, K, p, T, th, f, Q, G, prof = inst
    Ps = [Q/(1-f*f) for _ in range(N)]
    for it in range(iters):
        P0 = Ps
        for on, J in prof: _, Ps = rnd_np(Ps, on, J, T, th, G, f, Q)
        if max(np.abs(Ps[i]-P0[i]).max()/np.abs(P0[i]).max() for i in range(N)) < tol: break
    else: return None
    Wp = np.eye(N*K)
    for on, J in prof:
        W, Ps = rnd_np(Ps, on, J, T, th, G, f, Q); Wp = W @ Wp
    return np.abs(np.linalg.eigvals(Wp)).max()
def mpm(a): return mp.matrix(np.asarray(a).tolist())
def rho_mp(inst, iters=400, want_matrix=False):
    N, K, p, T, th, f, Q, G, prof = inst
    Tm = mpm(np.asarray(T).reshape(1, -1)); TT = Tm.T*Tm; f = mp.mpf(float(f)); Qm = mpm(Q); Gm = [mpm(g) for g in G]; thm = [mp.mpf(float(x)) for x in th]
    Ps = [Qm/(1-f*f) for _ in range(N)]
    def rnd(Ps, on, J):
        al = [thm[j]**2/(1 + thm[j]**2*(Tm*Ps[j]*Tm.T)[0]) for j in range(N)]
        W = mp.zeros(N*K, N*K); post = []
        for i in range(N):
            Lam = mp.inverse(Ps[i]); Lp = Lam + (Gm[i] if on[i] else mp.zeros(K)) + sum(al[j] for j in J[i])*TT
            Pp = mp.inverse(Lp); post.append(f*f*Pp + Qm)
            b = Pp*Lam
            for a in range(K):
                for c in range(K): W[i*K+a, i*K+c] = b[a, c]
            for j in J[i]:
                b = al[j]*Pp*TT
                for a in range(K):
                    for c in range(K): W[i*K+a, j*K+c] = b[a, c]
        return W, post
    for _ in range(iters):
        P0 = Ps
        for on, J in prof: _, Ps = rnd(Ps, on, J)
    res = max(mp.norm(Ps[i]-P0[i], mp.inf)/mp.norm(P0[i], mp.inf) for i in range(N))
    Wp = mp.eye(N*K)
    for on, J in prof:
        W, Ps = rnd(Ps, on, J); Wp = W*Wp
    ev = mp.eig(Wp, left=False, right=False)
    if want_matrix: return max(abs(e) for e in ev), res, Wp, ev
    return max(abs(e) for e in ev), res
