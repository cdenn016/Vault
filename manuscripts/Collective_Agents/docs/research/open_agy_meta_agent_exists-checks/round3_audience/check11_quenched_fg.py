r"""Check 11 (supplementary, instance P0): (a) quenched partner randomization (each audience member's single partner
drawn once, uniformly among the four other agents; all 4^4 = 256 equally likely assignments enumerated exactly);
(b) the diagnostic N_fg (forgetting switched off: F = 1, random-walk world, same Q).

Declared expectations before running: (a) every assignment with a member reading a mate while another member reads
the source is non-diffusive (Corollary F-share: non-transitive sharing), so contrast is undefined for most draws; the
all-source assignment (probability 1/256) reproduces r(A) = 5.385; no diffusive assignment other than the all-source
one selects A at r0 = 4.5.  (b) r(A) stays above 1 at F = 1 (diagnostic only).
NEGATIVE CONTROL for (a): the all-source assignment must be diffusive with r(A) = 5.3849 (the enumeration can return
the full model).
"""
import itertools
import time
import numpy as np
from aud import Par, riccati_fixed, b_of, stationary_fixed, coords, diffusive, contrast, all_regions

t0 = time.time()
par = Par()
N, n = par.N, par.n
A = tuple(range(1, N))
Pm_S, _ = riccati_fixed(par, 1.0 / par.RS, 0.0)
Pm_readS, _ = riccati_fixed(par, 1.0 / par.R, b_of(par, 1, 0))
Pm_readM, _ = riccati_fixed(par, 1.0 / par.R, b_of(par, 0, 1))
counts = dict(total=0, diffusive=0, selectA=0, select_any=0)
rA_list = []
for assign in itertools.product(range(4), repeat=n):
    att = [tuple()]
    Pm = [Pm_S]
    for i in range(1, N):
        others = [j for j in range(N) if j != i]
        J = others[assign[i - 1]]
        att.append((J,))
        Pm.append(Pm_readS if J == 0 else Pm_readM)
    S, _, _ = stationary_fixed(par, att, np.array(Pm))
    Sc = coords(par, S)
    Pi = np.linalg.inv(Sc)
    counts["total"] += 1
    if not diffusive(Pi, tol=1e-12)[0]:
        continue
    counts["diffusive"] += 1
    tab = {C: contrast(Pi, C) for C in all_regions(N)}
    rA_list.append((tab[A], att))
    sel = [C for C, v in tab.items() if v >= 4.5]
    if sel:
        counts["select_any"] += 1
    if A in sel:
        counts["selectA"] += 1
print(f"(a) quenched N_pr over 256 assignments: {counts}")
for r, att in sorted(rA_list, key=lambda z: -z[0])[:6]:
    print(f"    diffusive assignment {att}: r(A) {r:.4f}")
# (b) N_fg
pf = par.with_(F=1.0)
Pm_S1, _ = riccati_fixed(pf, 1.0 / pf.RS, 0.0)
Pm_A1, _ = riccati_fixed(pf, 1.0 / pf.R, b_of(pf, 1, 0))
S, _, _ = stationary_fixed(pf, [tuple()] + [(0,)] * n, np.array([Pm_S1] + [Pm_A1] * n))
Pi = np.linalg.inv(coords(pf, S))
print(f"(b) N_fg (F = 1): diffusive {diffusive(Pi)[0]}; r(A) {contrast(Pi, A):.4f}; r(A u S) {contrast(Pi, tuple(range(N))):.4f}")
print(f"({time.time()-t0:.1f}s)")
