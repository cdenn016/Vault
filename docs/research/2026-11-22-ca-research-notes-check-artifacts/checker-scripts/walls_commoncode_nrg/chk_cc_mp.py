# Independent multiprecision recomputation of conj_sca_common_code C3 and C4 (own code from the level-1 equations)
import mpmath as mp
mp.mp.dps = 40
I2 = mp.eye(2)
def B_of(H, Rc, P): return H.T * mp.inverse(Rc + H*P*H.T) * H
def step(Ps, Gs, Js, H, Rc):
    """one reception round: returns W^rec (4x4) and posterior covariances"""
    N = 2; Bs = [B_of(H, Rc, Ps[j]) for j in range(N)]
    W = mp.zeros(4, 4); post = []
    for i in range(N):
        Lam = mp.inverse(Ps[i]); Lp = Lam + Gs[i]
        for j in Js[i]: Lp = Lp + Bs[j]
        Pp = mp.inverse(Lp); post.append(Pp)
        blk = Pp*Lam
        for a in range(2):
            for b in range(2): W[2*i+a, 2*i+b] = blk[a, b]
        for j in Js[i]:
            blk = Pp*Bs[j]
            for a in range(2):
                for b in range(2): W[2*i+a, 2*j+b] = blk[a, b]
    return W, post
def orbit(profile, H, Rc, f, iters):
    Ps = [I2/(1-f*f), I2/(1-f*f)]
    for _ in range(iters):
        for (Gs, Js) in profile:
            _, post = step(Ps, Gs, Js, H, Rc); Ps = [f*f*p + I2 for p in post]
    P0 = [p.copy() for p in Ps]; Wp = mp.eye(4)
    for (Gs, Js) in profile:
        W, post = step(Ps, Gs, Js, H, Rc); Wp = (f*W)*Wp; Ps = [f*f*p + I2 for p in post]
    res = max(mp.norm(Ps[i]-P0[i], mp.inf) for i in range(2))
    ev = mp.eig(Wp, left=False, right=False)
    return max(abs(e) for e in ev), res
row = lambda a, b: mp.matrix([[a, b]])
outer = lambda g: g.T*g
print("C3 frozen, common rank-2 code H=diag(10,0.15), sensors (0.5,0.14),(15,4.6)")
H = mp.diag([10, mp.mpf('0.15')])
for f, it in ((mp.mpf('0.95'), 400), (mp.mpf('0.99'), 500), (mp.mpf('0.9999'), 600)):
    rho, res = orbit([([outer(row(mp.mpf('0.5'), mp.mpf('0.14'))), outer(row(15, mp.mpf('4.6')))], [[1], [0]])], H, I2, f, it)
    print("  f=%s rho(W)=%s rho/f-1=%s  fixed-point residual=%s" % (f, mp.nstr(rho, 18), mp.nstr(rho/f-1, 12), mp.nstr(res, 3)))
rho, res = orbit([([outer(row(mp.mpf('0.5'), mp.mpf('0.15'))), outer(row(15, mp.mpf('4.5')))], [[1], [0]])], H, I2, mp.mpf('0.95'), 400)
print("  control parallel sensors: rho/f-1=%s res=%s" % (mp.nstr(rho/mp.mpf('0.95')-1, 6), mp.nstr(res, 3)))
print("C4 period-2, common rank-1 code H=(100,0)")
H1 = row(100, 0); Rc1 = mp.matrix([[1]])
prof = [([outer(200*row(1, mp.mpf('0.3'))), outer(200*row(1, mp.mpf('-0.3')))], [[1], [0]]),
        ([outer(100*row(1, mp.mpf('0.35'))), outer(100*row(1, mp.mpf('-0.35')))], [[], []])]
for f in (mp.mpf('0.95'), mp.mpf('0.99'), mp.mpf('0.995')):
    rho, res = orbit(prof, H1, Rc1, f, 150)
    print("  f=%s rho(W2)=%s rho/f^2-1=%s per-round=%s residual=%s" % (f, mp.nstr(rho, 18), mp.nstr(rho/f**2-1, 12), mp.nstr(mp.sqrt(rho), 12), mp.nstr(res, 3)))
prof0 = [(prof[0][0], [[], []]), prof[1]]
rho, res = orbit(prof0, H1, Rc1, mp.mpf('0.995'), 150)
print("  control no listening: rho/f^2=%s" % mp.nstr(rho/mp.mpf('0.995')**2, 12))
# single-sensor variant of C4 (same Gamma_i in both rounds, i.e. inside the narrowed conjecture): should NOT amplify if conjecture is right
for g in (mp.mpf('0.3'), mp.mpf('0.35')):
    G = [outer(200*row(1, g)), outer(200*row(1, -g))]
    for prof1, name in (([(G, [[1],[0]]), (G, [[],[]])], "sense both rounds, listen round 0"),
                        ([(G, [[1],[0]]), ([mp.zeros(2), mp.zeros(2)], [[],[]])], "sense+listen round 0, idle round 1"),
                        ([([mp.zeros(2), mp.zeros(2)], [[1],[0]]), (G, [[],[]])], "listen round 0, sense round 1")):
        rho, res = orbit(prof1, H1, Rc1, mp.mpf('0.995'), 200)
        print("  narrowed-conjecture variant g=%s [%s]: rho/f^2-1=%s res=%s" % (g, name, mp.nstr(rho/mp.mpf('0.995')**2-1, 8), mp.nstr(res, 3)))
