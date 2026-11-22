import pickle, sys, numpy as np, time, mpmath as mp
from c5lib import *
top = pickle.load(open("c5top_strict.pkl", "rb")); r0, inst = top[2]; N, K, p, T, th, f, Q, G, prof = inst
mp.mp.dps = 40; t0 = time.time()
def run(name, sc=(1, 1, 1), thf=1.0, ff=None, Tn=None, iters=260, prof2=None):
    inst2 = (N, K, p, T if Tn is None else Tn, th*thf, f if ff is None else ff, Q, [G[i]*sc[i] for i in range(N)], prof if prof2 is None else prof2)
    rho, res = rho_mp(inst2, iters)
    print("%-28s rho_rec-1 = %s   residual %s   [%.0fs]" % (name, mp.nstr(rho-1, 8), mp.nstr(res, 2), time.time()-t0))
run("G1 x1e2", (1, 1e2, 1)); run("G1 x1e4", (1, 1e4, 1)); run("G1 x1e-2", (1, 1e-2, 1))
run("theta x10", thf=10); run("theta x0.1", thf=0.1); run("theta x100", thf=100)
run("f=0.5", ff=0.5); run("f=0.8", ff=0.8); run("f=0.999", ff=0.999, iters=900)
run("theta x0.1, G1 x1e-2", (1, 1e-2, 1), thf=0.1)
run("theta x0.01, G1 x1e-4", (1, 1e-4, 1), thf=0.01)
# frozen controls: each single round frozen must have rho_rec <= 1 (prop (d))
for t in range(3):
    inst2 = (N, K, 1, T, th, f, Q, G, [prof[t]]); rho, res = rho_mp(inst2, 400)
    print("frozen control round %d only: rho_rec-1 = %s residual %s" % (t, mp.nstr(rho-1, 8), mp.nstr(res, 2)))
# no-sensing control (prop (c)): rho_rec = 1 exactly
inst2 = (N, K, p, T, th, f, Q, G, [([False]*N, J) for on, J in prof]); rho, res = rho_mp(inst2, 400)
print("no-sensing periodic control: rho_rec-1 = %s residual %s" % (mp.nstr(rho-1, 8), mp.nstr(res, 2)))
