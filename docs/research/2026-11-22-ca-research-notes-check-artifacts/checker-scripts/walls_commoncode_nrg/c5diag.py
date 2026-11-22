# Diagnose: frozen round-1 profile of the candidate (PROVED rho_rec<=1). Is mp.eig's "1+4e-11" real or an artifact?
import pickle, numpy as np, mpmath as mp
from c5lib import *
top = pickle.load(open("c5top_strict.pkl", "rb")); r0, inst = top[2]; N, K, p, T, th, f, Q, G, prof = inst
for dps in (40, 80):
    mp.mp.dps = dps
    rho, res, W, ev = rho_mp((N, K, 1, T, th, f, Q, G, [prof[1]]), 500, True)
    evs = sorted(ev, key=lambda z: -abs(z))
    print("dps=%d residual=%s  top eig-1: %s" % (dps, mp.nstr(res, 2), [mp.nstr(e-1, 6) for e in evs[:6]]))
    I = mp.eye(N*K)
    print("   det(W-(1+d)I) for d=-1e-10,1e-11,2e-11,5e-11,1e-10,1e-9:", [mp.nstr(mp.det(W-(1+mp.mpf(d))*I), 4) for d in ('-1e-10','1e-11','2e-11','5e-11','1e-10','1e-9')])
    for k in (1, 2, 3):
        s = mp.svd_r((W-I)**k, compute_uv=False); s = sorted([s[i] for i in range(len(s))])
        print("   singular values of (W-I)^%d (smallest 6): %s" % (k, [mp.nstr(x, 3) for x in s[:6]]))
