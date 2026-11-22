# Re-examine in multiprecision the top candidates of the C5 random search (rho/f^p slightly above 1 in double precision)
import numpy as np, mpmath as mp, time, pickle
exec(open('chk_cc_rand.py').read().split("t0 = time.time(); worst")[0])   # reuse spd, Wrec, sinks
exec("def orbit_rho" + open('chk_cc_rand.py').read().split("def orbit_rho")[1].split("# positive control")[0])
rng = np.random.default_rng(424243)
def draw():
    N = int(rng.integers(2, 4)); K = int(rng.integers(2, 4)); p = int(rng.integers(2, 4))
    T = rng.normal(size=K); th = 10.0**rng.uniform(-1, 2.3, N); f = rng.uniform(0.8, 0.999)
    Q = np.eye(K) if rng.uniform() < 0.5 else spd(K, -1, 1)
    Gfix = []
    for i in range(N):
        r = int(rng.integers(1, K+1)); h = rng.normal(size=(r, K))*10.0**rng.uniform(-1, 2.5); Gfix.append(h.T @ h)
    prof = []
    for t in range(p):
        on = [rng.uniform() < 0.6 for i in range(N)]
        J = [[j for j in range(N) if j != i and rng.uniform() < 0.6] for i in range(N)]
        prof.append((on, J))
    return N, K, p, T, th, f, Q, Gfix, prof
t0 = time.time(); top = []
while time.time() - t0 < 25:
    inst = draw(); N, K, p, T, th, f, Q, Gfix, prof = inst
    r = orbit_rho([([Gfix[i] if on[i] else np.zeros((K, K)) for i in range(N)], J) for on, J in prof], T, th, f, Q, N, K)
    if r is None: continue
    top.append((r, inst)); top.sort(key=lambda x: -x[0]); top = top[:4]
print("double-precision top candidates:", ["%.12f" % t[0] for t in top])
mp.mp.dps = 60
def mpm(a): return mp.matrix(a.tolist())
def mp_rho(inst, iters):
    N, K, p, T, th, f, Q, Gfix, prof = inst
    Tm = mpm(T.reshape(1, -1)); TT = Tm.T*Tm; f = mp.mpf(float(f)); Qm = mpm(Q); G = [mpm(g) for g in Gfix]; th = [mp.mpf(float(x)) for x in th]
    Ps = [Qm/(1-f*f) for _ in range(N)]
    def rnd(Ps, on, J, build):
        al = [th[j]**2/(1 + th[j]**2*(Tm*Ps[j]*Tm.T)[0]) for j in range(N)]
        W = mp.zeros(N*K, N*K); post = []
        for i in range(N):
            Lam = mp.inverse(Ps[i]); Lp = Lam + (G[i] if on[i] else mp.zeros(K)) + sum(al[j] for j in J[i])*TT
            Pp = mp.inverse(Lp); post.append(Pp)
            if build:
                b = Pp*Lam
                for a in range(K):
                    for c in range(K): W[i*K+a, i*K+c] = b[a, c]
                for j in J[i]:
                    b = al[j]*Pp*TT
                    for a in range(K):
                        for c in range(K): W[i*K+a, j*K+c] = b[a, c]
        return W, [f*f*x + Qm for x in post]
    for _ in range(iters):
        P0 = Ps
        for on, J in prof: _, Ps = rnd(Ps, on, J, False)
    res = max(mp.norm(Ps[i]-P0[i], mp.inf)/mp.norm(P0[i], mp.inf) for i in range(N))
    Wp = mp.eye(N*K)
    for on, J in prof:
        W, Ps = rnd(Ps, on, J, True); Wp = W*Wp
    ev = mp.eig(Wp, left=False, right=False)
    return max(abs(e) for e in ev), res
for r, inst in top:
    rho, res = mp_rho(inst, 500)
    print("  double %.12f -> 60-digit rho_rec - 1 = %s  (orbit residual %s; N,K,p,f=%s)" % (r, mp.nstr(rho-1, 6), mp.nstr(res, 3), (inst[0], inst[1], inst[2], round(float(inst[5]), 4))))
