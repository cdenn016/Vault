r"""X1 (exploration, not deciding): basic quantities of the niche class without slots and with slots.

Expectations (rough, before running): n=2 full pair r(A) between 3 and 8, above the N=4 medium (2.49);
canonical N_hab (mate read 1/4 of rounds) well below the medium; N_pr (1 of 3 channels) below the medium.
n=4: full 8.8-ish, medium N=8 c=3 somewhere 3-5.
"""
import time
import numpy as np
from flib import (Par, exact_sigma_c, compound, r_ab, mc, r_and_se, medium_exact, steady_prior, efe_grid,
                  canonical_types)

t0 = time.time()
for n, kmsg in ((2, 1), (4, 3)):
    N = 2 * n
    par = Par(Rc=0.1, qc=1e-4, n=n, n_zero=N - n, m=0, types=canonical_types(n - 1, N - n, kmsg))
    att = ~np.eye(n, dtype=bool)
    S, _, _ = exact_sigma_c(par, att, np.zeros(n, dtype=int))
    al, be = compound(S)
    rf = r_ab(n, al, be)
    alm, bem, rm = medium_exact(par, N=N, c=kmsg)
    Pm = steady_prior(par, n - 1, 0)
    G = efe_grid(par, Pm[0, 0], Pm[0, 1], Pm[1, 1], np.arange(n), np.arange(3))
    print(f"n={n} kmsg={kmsg}: types {par.types}; full r(A) {rf:.4f} (alpha {al:.5f} beta {be:.5f}); "
          f"medium N={N} c={kmsg}: {rm:.4f}; P^- {np.round(Pm, 5).tolist()}")
    print(f"   EFE G[c, k] (k=0..2): {np.round(G, 5).tolist()}")
    oh = mc(par, "hab", K=1500, T=400, burn=80, seed=100 + n)
    rh, seh, _, _ = r_and_se(oh, n)
    op = mc(par, "pr", K=1500, T=400, burn=80, seed=200 + n, r_att=kmsg)
    rp, sep, _, _ = r_and_se(op, n)
    print(f"   N_hab canonical: {rh:.4f} +- {seh:.4f} (mean reads {oh.mean_c:.3f}); N_pr: {rp:.4f} +- {sep:.4f} "
          f"(mean informative reads {op.mean_c:.3f})  ({time.time()-t0:.0f}s)")
    # habit family rho(pi): x* = all mates w.p. pi, zero-informative otherwise
    for pi in (0.25, 0.5, 0.75, 0.9, 1.0):
        tps = ((0, 1), (n - 1, 1))
        p2 = par.with_(types=tps)
        o = mc(p2, "hab", K=1000, T=400, burn=80, seed=300 + int(100 * pi), att_law=np.array([1 - pi, pi]))
        r, se, _, _ = r_and_se(o, n)
        print(f"   rho(pi={pi}) (no slots): {r:.4f} +- {se:.4f}")
    print(f"   ({time.time()-t0:.0f}s)")
print(f"total {time.time()-t0:.1f}s")
