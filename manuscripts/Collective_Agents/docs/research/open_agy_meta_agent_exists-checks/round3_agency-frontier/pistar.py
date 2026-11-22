r"""Deciding run 6: the threshold pi* of the attention-surprise bound KL_a >= n d(1 - delta || pi*), over n, the
number of niches K and the channel-noise ratio Rc/R (kappa_msg = n - 1), and the flooding check.

rho(pi; n, Rc): N_hab contrast of a niche when each member's attention is drawn i.i.d. per round from
pi delta_{x*} + (1 - pi) delta_{zero-informative} (x* = all mates) and no slots (slot-neutral).  It does not depend on
K (reading another niche's channel carries zero gain).  b(n, K, Rc): exact mechanism medium (N = K n agents, each reads
n - 1 uniformly random others per round).  pi* solves rho(pi*) = b by linear interpolation on a grid of pi
(rho increasing; checked on the grid).  Flooding: rho_flood(1) = N_hab contrast with attention pinned on x* and the
private slots of D1 drawn from their habits (m = 8, Rs in {10, 1}).
Declared expectations (before running): pi*(n=2,K=2,Rc=0.1) about 0.57 and pi*(n=4,K=2,Rc=0.1) about 0.73 (x1);
pi* rises with K (b falls) and with Rc in a direction to be measured; for some large Rc the window closes
(r_full <= b, reported as 'empty').  rho_flood(1) below b at Rs = 1 (x2: 1.245 < 2.493); at Rs = 10 rho_flood(1) is
an open question (expect between 2 and 4 for n = 2).
NEGATIVE CONTROL: rho(1) must reproduce the exact full-model r(A) within 3 SE (the family's endpoint).
"""
import time
import numpy as np
from flib import Par, exact_sigma_c, compound, r_ab, mc, r_and_se, medium_exact

t0 = time.time()
pis = np.array([0.0, 0.3, 0.5, 0.7, 0.85, 1.0])
for n in (2, 3, 4):
    for Rc in (0.05, 0.1, 0.2, 0.4):
        par = Par(Rc=Rc, qc=1e-4, n=n, n_zero=n, m=0, types=((0, 1), (n - 1, 1)))
        att = ~np.eye(n, dtype=bool)
        rf = r_ab(n, *compound(exact_sigma_c(par, att, np.zeros(n, dtype=int))[0]))
        rho, se = [], []
        for pi in pis:
            if pi == 0.0:
                rho.append(1.0); se.append(0.0); continue
            o = mc(par, "hab", K=500, T=300, burn=60, seed=int(7000 + 100 * n + 1000 * Rc + 10 * pi),
                   att_law=np.array([1 - pi, pi]))
            r, s, _, _ = r_and_se(o, n)
            rho.append(r); se.append(s)
        rho = np.array(rho)
        mono = bool(np.all(np.diff(rho) > -3 * np.array(se)[1:]))
        out = []
        for K in (2, 3, 4):
            b = medium_exact(par, N=K * n, c=n - 1)[2]
            if rf <= b:
                out.append(f"K={K}: b {b:.3f} empty")
                continue
            j = int(np.searchsorted(rho, b))
            if j >= len(rho):
                ps = 1.0
            else:
                ps = pis[j - 1] + (pis[j] - pis[j - 1]) * (b - rho[j - 1]) / (rho[j] - rho[j - 1])
            out.append(f"K={K}: b {b:.3f} pi* {ps:.3f} ln(1/pi*) {np.log(1/ps):.3f}")
        print(f"n={n} Rc={Rc}: r_full {rf:.3f}; rho(pi) {np.round(rho, 3).tolist()} (SE <= {max(se):.3f}, "
              f"monotone {mono}; endpoint z {(rho[-1]-rf)/se[-1]:+.2f}); " + "; ".join(out) + f"  ({time.time()-t0:.0f}s)")
# flooding check (n = 2, D1 slots)
for Rs in (10.0, 1.0):
    par = Par(Rc=0.1, qc=1e-4, n=2, n_zero=2, m=8, Rs=Rs, types=((0, 1), (1, 1)))
    o = mc(par, "hab", K=800, T=400, burn=80, seed=7999, att_law=np.array([0.0, 1.0]))
    r, s, _, _ = r_and_se(o, 2)
    print(f"flooding n=2, m=8, Rs={Rs}: rho_flood(1) {r:.4f} +- {s:.4f} vs b(K=2) 2.4932 -> "
          f"{'pi* = 1 (no attention bound)' if r + 3 * s < 2.4932 else 'bound persists'}")
for Rs in (10.0, 1.0):
    par = Par(Rc=0.1, qc=1e-4, n=4, n_zero=4, m=8, Rs=Rs, types=((0, 1), (3, 1)))
    o = mc(par, "hab", K=600, T=400, burn=80, seed=7998, att_law=np.array([0.0, 1.0]))
    r, s, _, _ = r_and_se(o, 4)
    print(f"flooding n=4, m=8, Rs={Rs}: rho_flood(1) {r:.4f} +- {s:.4f} vs b(K=2) 4.7541")
print(f"total {time.time()-t0:.1f}s")
