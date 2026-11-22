r"""Check 13: where the pure-audience window exists (exact full-model quantities; nulls not recomputed here).
Scan over the source noise RS and the channel noise Rc at R = 1, n = 4, other parameters as P0.  For each point:
diffusive?, r(A), r(A u S) and the best region containing S, the mean-coupling and M-perm baselines, and the closed
form r(A) = 1 - c/sigma + n beta'/alpha (Proposition A) as a check of the enumeration.

Declared expectations before running: the closed form matches the enumerated r(A) to 1e-9 at every diffusive point;
the source never joins (the best region containing S stays below r(A)); the mean-coupling window closes as RS grows
toward Q (RS >= 0.05 at Rc = RS/10, from exploration 1).
NEGATIVE CONTROL: RS = 2R (source worse than a mate) must leave the audience unselected (EFE does not pick S).
"""
import numpy as np
from aud import Par, riccati_fixed, b_of, stationary_fixed, coords, diffusive, contrast, all_regions, \
    mean_coupling_baseline, type_law

A = (1, 2, 3, 4)
print(f"{'RS':>7} {'Rc':>7} {'diff':>5} {'r(A)':>8} {'closed':>8} {'best w/ S':>9} {'mc base':>8} {'perm':>7} {'P(read S)':>10}")
for RS in (0.002, 0.005, 0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 2.0):
    for Rc in (RS / 10, RS / 5, 0.002):
        par = Par(RS=RS, Rc=Rc)
        Pm_S, _ = riccati_fixed(par, 1.0 / par.RS, 0.0)
        Pm_A, _ = riccati_fixed(par, 1.0 / par.R, b_of(par, 1, 0))
        S, _, _ = stationary_fixed(par, [tuple()] + [(0,)] * par.n, np.array([Pm_S] + [Pm_A] * par.n))
        Sc = coords(par, S)
        Pi = np.linalg.inv(Sc)
        d = diffusive(Pi)[0]
        sig, c = Sc[0, 0], Sc[0, 1]
        al, be = Sc[1, 1] - Sc[1, 2], Sc[1, 2]
        closed = 1 - c / sig + par.n * (be - c * c / sig) / al
        rA = contrast(Pi, A)
        bestS = max(contrast(Pi, C) for C in all_regions(5) if 0 in C)
        mc = mean_coupling_baseline(Pi)[0]
        N = 5
        dd = np.trace(Sc) / N; oo = (Sc.sum() - np.trace(Sc)) / (N * (N - 1))
        perm = 1 + N * oo / (dd - oo)
        ty, p, G, mult = type_law(par, Pm_A)
        pS = sum(pp for (s, m), pp in zip(ty, p) if s == 1)
        print(f"{RS:7.3f} {Rc:7.4f} {str(d):>5} {rA:8.4f} {closed:8.4f} {bestS:9.4f} {mc:8.4f} {perm:7.4f} {pS:10.6f}")
