import pickle, sys, mpmath as mp, numpy as np, time
from c5lib import *
top = pickle.load(open("c5top_%s.pkl" % sys.argv[1], "rb"))
t0 = time.time()
for r, inst in top[:3]:
    N, K, p, T, th, f, Q, G, prof = inst
    out = []
    for dps, iters in ((40, 300), (90, 700)):
        mp.mp.dps = dps
        rho, res, Wp, ev = rho_mp(inst, iters, True)
        out.append((dps, mp.nstr(rho-1, 8), mp.nstr(res, 3)))
        if dps == 90:
            evs = sorted([complex(e) for e in ev], key=lambda z: -abs(z))
            # geometric multiplicity of eigenvalue ~1 and det test
            I = mp.eye(N*K)
            c = rho-1
            d_lo = mp.det(Wp-(1+c/2)*I); d_hi = mp.det(Wp-(1+2*c)*I); d_1 = mp.det(Wp - I)
    print("double rho-1=%.3e  N,K,p=%d,%d,%d f=%.4f theta=%.3g sensing-on=%s J=%s" % (r-1, N, K, p, f, th[0], [pr[0] for pr in prof], [pr[1] for pr in prof]))
    print("   mp:", out, " top |eig|-1:", ["%.3e" % (abs(z)-1) for z in evs[:4]], " imag:", ["%.2e" % z.imag for z in evs[:4]])
    print("   det(W-I)=%s det(W-(1+c/2)I)=%s det(W-(1+2c)I)=%s  [%.0fs]" % (mp.nstr(d_1, 5), mp.nstr(d_lo, 5), mp.nstr(d_hi, 5), time.time()-t0))
