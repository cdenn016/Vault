r"""Exploration 1 (design only, not deciding): exact full-model quantities for the pure audience (kmsg = 1, every
audience member reads exactly the source), over a small parameter scan.

Declared expectations before running:
  * at RS = 0.01, Rc = 0.002, R = 1: Pi^c diffusive, source weakly coupled (|Pi_{S,i}| << |Pi_{i,j}|),
    r(A) between 3 and 10, r(A u {S}) < r(A), mean-coupling baseline below r(A);
  * the EFE attention law puts probability >= 1 - 1e-6 on 'read the source' at gamma = 40;
  * NEGATIVE CONTROL: Rc = 1e6 gives r(A) within 1e-3 of 1 (audience decoupled);
  * NEGATIVE CONTROL: RS = 4 R makes the source a worse channel than a mate, so EFE does not pick it.
"""
import time
import numpy as np
from aud import Par, riccati_fixed, b_of, stationary_fixed, coords, diffusive, contrast, region_table, \
    mean_coupling_baseline, type_law

t0 = time.time()


def full_fixed(par: Par):
    Pm_S, _ = riccati_fixed(par, 1.0 / par.RS, 0.0)
    Pm_A, _ = riccati_fixed(par, 1.0 / par.R, b_of(par, 1, 0))
    Pm = np.array([Pm_S] + [Pm_A] * par.n)
    att = [tuple()] + [(0,)] * par.n
    S, A, Nz = stationary_fixed(par, att, Pm)
    Sc = coords(par, S)
    return Sc, Pm_A


def report(par: Par, label: str):
    Sc, Pm_A = full_fixed(par)
    Pi = np.linalg.inv(Sc)
    dif = diffusive(Pi)
    A = tuple(range(1, par.N))
    rA = contrast(Pi, A) if dif[0] else float("nan")
    rAS = contrast(Pi, tuple(range(par.N))) if dif[0] else float("nan")
    tab = region_table(Pi) if dif[0] else {}
    others = max((v for k, v in tab.items() if k != A), default=float("nan"))
    best_other = max(((v, k) for k, v in tab.items() if k != A), default=(float("nan"), None))
    mb = mean_coupling_baseline(Pi) if dif[0] else (float("nan"),) * 4
    ty, p, G, mult = type_law(par, Pm_A)
    pS = sum(pp for (s, m), pp in zip(ty, p) if s == 1)
    print(f"[{label}] RS={par.RS} Rc={par.Rc} R={par.R} n={par.n}: diffusive={dif[0]} (max off {dif[1]:.3e}, "
          f"min rowsum {dif[2]:.3e})")
    print(f"   Sigma^c: var S {Sc[0,0]:.4e}, cov(S,i) {Sc[0,1]:.4e}, var i {Sc[1,1]:.4e}, cov(i,j) {Sc[1,2]:.4e}")
    print(f"   Pi: Pi_SS {Pi[0,0]:.4e}, Pi_Si {Pi[0,1]:.4e}, Pi_ii {Pi[1,1]:.4e}, Pi_ij {Pi[1,2]:.4e}; "
          f"leak S {Pi.sum(1)[0]:.4e}, leak i {Pi.sum(1)[1]:.4e}")
    print(f"   r(A) {rA:.4f}; r(A+S) {rAS:.4f}; best other region {best_other[0]:.4f} {best_other[1]}; "
          f"mean-coupling baseline {mb[0]:.4f} (closed form {mb[3]:.4f})")
    print(f"   EFE law: P(read source) = {pS:.12f}; G by type {dict(zip(ty, np.round(G, 5)))}")


report(Par(), "base")
for RS, Rc in ((0.01, 0.001), (0.02, 0.002), (0.005, 0.001), (0.05, 0.005), (0.1, 0.01)):
    report(Par(RS=RS, Rc=Rc), "scan")
for R in (2.0, 4.0):
    report(Par(R=R), "scan R")
for n in (3, 6):
    report(Par(n=n), "scan n")
report(Par(Rc=1e6), "NEG Rc=1e6")
report(Par(RS=4.0), "NEG RS=4R")
print(f"({time.time() - t0:.1f}s)")
