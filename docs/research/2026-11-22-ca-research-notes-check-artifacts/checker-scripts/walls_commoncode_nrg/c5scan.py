import pickle, sys, numpy as np, time, mpmath as mp
from c5lib import *
top = pickle.load(open("c5top_strict.pkl", "rb")); r0, inst = top[2]; N, K, p, T, th, f, Q, G, prof = inst
mp.mp.dps = 34; t0 = time.time()
print("T=%s theta=%.6g f=%.10g" % (T.tolist(), th[0], f)); [print(" G_%d=" % i, g.tolist()) for i, g in enumerate(G)]
print("prof:", prof)
for name, scales in (("base", (1, 1, 1)), ("G2 x10", (1, 1, 10)), ("G2 x100", (1, 1, 100)), ("G2 x1e4", (1, 1, 1e4)), ("G0 x100", (100, 1, 1)), ("G0 x0.01", (0.01, 1, 1)), ("G1 x1e-4", (1, 1e-4, 1)), ("G2 x100,G1 x1e-4", (1, 1e-4, 100))):
    inst2 = (N, K, p, T, th, f, Q, [G[i]*scales[i] for i in range(N)], prof)
    rho, res = rho_mp(inst2, 220)
    print("%-18s rho_rec-1 = %s   residual %s   [%.0fs]" % (name, mp.nstr(rho-1, 8), mp.nstr(res, 2), time.time()-t0))
    if time.time()-t0 > 48: break
