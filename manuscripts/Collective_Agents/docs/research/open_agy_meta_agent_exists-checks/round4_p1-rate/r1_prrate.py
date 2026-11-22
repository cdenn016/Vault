r"""Variant P1: partner randomization redrawn every round at the members' attention rate.

Each member, in every round, reads one partner with probability q1 = 0.21537925553 and two otherwise
(mean 1.785 channels, the variant's attention rate), the partners drawn uniformly among the four other
agents. Engine: the round-4 blind implementation (p1lib.py), with this attention mode added.
Declared expectation: r(A) between the one-partner value of the audience (1.54) and the two-partner
value of the variant (1.76), diffusive, A the region of largest contrast, all far below 4.45.
Control: the same engine in its two-partner mode must reproduce 1.7641 +- 0.0008.
"""
import os, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import p1lib as L
t0 = time.time()
p = dict(L.BASE); p["q1"] = 0.21537925553
regs = L.regions(5)
def rep(name, res):
    Sg = L.group_sigmas(res)
    S, Sse = L.jackknife(lambda X: X, Sg)
    an = L.analyze_sigma(S)
    rall, rse = L.jackknife(lambda X: np.array([L.analyze_sigma(X)["r_all"][C] for C in regs]), Sg)
    iA = regs.index((1, 2, 3, 4)); im = int(np.argmax(rall))
    oth = [i for i in range(len(regs)) if i != iA]; io = oth[int(np.argmax(rall[oth]))]
    print(f"=== {name}: diffusive {an['diffusive']}; r(A) = {rall[iA]:.4f} +- {rse[iA]:.4f}; largest region {regs[im]} {rall[im]:.4f}; largest other {regs[io]} {rall[io]:.4f} +- {rse[io]:.4f}")
    print("attention law (members avg):", np.round(res["att_prob"].mean(0), 5))
B, TB, TA, G = 3000, 100, 300, 20
rep("N_pr at the attention rate", L.simulate(L.Model(p, att="prrate"), B=B, T_burn=TB, T_avg=TA, seed=301, G=G))
print(f"[{time.time()-t0:.1f}s]")
rep("control: N_pr at two partners", L.simulate(L.Model(p, att="pr"), B=B, T_burn=TB, T_avg=TA, seed=102, G=G))
print(f"[{time.time()-t0:.1f}s]")
