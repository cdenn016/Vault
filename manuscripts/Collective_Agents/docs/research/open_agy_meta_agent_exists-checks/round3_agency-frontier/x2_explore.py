r"""X2 (exploration, not deciding): closure for n=2, slot flooding under N_hab, kappa lever, H_mon spot check.

Expectations (rough): closure d_M(n=2) of order 1e-4, d_cl of order 1e-3; inference defect 0.05-0.15;
slot flooding lowers N_hab; medium with c=2 (n=2, kmsg=2) above the pair's 4.35 or close to it;
H_mon: moving habit mass from zero-informative to partially informative sets raises N_hab's contrast.
"""
import time
import numpy as np
from flib import (Par, exact_sigma_c, compound, r_ab, mc, r_and_se, medium_exact, steady_prior, efe_grid,
                  canonical_types, closure_numbers)

t0 = time.time()
base = Par(Rc=0.1, qc=1e-4, n=2, n_zero=2, m=0, types=canonical_types(1, 2, 1))
dcl, dM, dMh = closure_numbers(base, c=1, k=0, n=2)
print(f"closure n=2 (reads mate, no slots): d_cl {dcl:.3e}, stationary d_M {dM:.3e} (half window {dMh:.3e})")
o = mc(base, "full", K=1500, T=400, burn=80, seed=21, want_inf=True)
I = o.inf
vstar = 1.0 / (I["invU"] / I["n"])
best = 0.5 * (vstar * I["invU"] / I["n"] - 1 - np.log(vstar) + I["lnU"] / I["n"] + I["q"] / I["n"])
print(f"inference n=2: best-constant {best:.4f}, claimed-variance {I['claim']/I['n']:.4f}, reverse {I['rev']/I['n']:.4f}"
      f"  ({time.time()-t0:.0f}s)")
for n in (3, 4):
    p = base.with_(n=n, n_zero=n)
    dcl, dM, dMh = closure_numbers(p, c=n - 1, k=0, n=n)
    o = mc(p.with_(types=((n - 1, 1),)), "full", K=800, T=400, burn=80, seed=22 + n, want_inf=True)
    I = o.inf
    vstar = 1.0 / (I["invU"] / I["n"])
    best = 0.5 * (vstar * I["invU"] / I["n"] - 1 - np.log(vstar) + I["lnU"] / I["n"] + I["q"] / I["n"])
    print(f"closure n={n}: d_cl {dcl:.3e}, d_M {dM:.3e}; inference best-constant {best:.4f}")
# slot flooding under N_hab, n=2 canonical support, m slots at Rs, psi irrelevant under N_hab
for m, Rs in ((8, 1.0), (8, 0.2), (18, 1.0), (18, 0.2)):
    p = base.with_(m=m, Rs=Rs)
    oh = mc(p, "hab", K=1000, T=400, burn=80, seed=31 + m)
    rh, seh, _, _ = r_and_se(oh, 2)
    pp = p.with_(types=((0, 1), (1, 1)))
    oh2 = mc(pp, "hab", K=1000, T=400, burn=80, seed=41 + m)
    rh2, seh2, _, _ = r_and_se(oh2, 2)
    oh3 = mc(pp, "hab", K=1000, T=400, burn=80, seed=51 + m, att_law=np.array([0.0, 1.0]))
    rh3, seh3, _, _ = r_and_se(oh3, 2)
    print(f"N_hab m={m} Rs={Rs}: canonical |S|=4 {rh:.4f}+-{seh:.4f}; |S|=2 {rh2:.4f}+-{seh2:.4f}; "
          f"attention fixed on mate (pi=1) {rh3:.4f}+-{seh3:.4f}; open rate {oh.open_rate:.3f}")
print(f"({time.time()-t0:.0f}s)")
# kappa lever: n=2, kmsg=2 -> medium N=4 c=2
for c in (1, 2):
    al, be, rm = medium_exact(base, N=4, c=c)
    print(f"medium N=4 c={c}: {rm:.4f}")
for K_ in (2, 3, 4):
    al, be, rm = medium_exact(base, N=2 * K_, c=1)
    al4, be4, rm4 = medium_exact(base, N=4 * K_, c=3)
    print(f"niches K={K_}: medium n=2 (N={2*K_}, c=1) {rm:.4f};  n=4 (N={4*K_}, c=3) {rm4:.4f}")
# H_mon spot check n=4: pi=0.5 on x*, rest on c=0 vs c=1 vs c=2
p4 = Par(Rc=0.1, qc=1e-4, n=4, n_zero=4, m=0, types=((0, 1), (1, 1), (2, 1), (3, 1)))
for lab, law in (("rest c=0", [0.5, 0, 0, 0.5]), ("rest c=1", [0, 0.5, 0, 0.5]), ("rest c=2", [0, 0, 0.5, 0.5])):
    o = mc(p4, "hab", K=800, T=400, burn=80, seed=61, att_law=np.array(law))
    r, se, _, _ = r_and_se(o, 4)
    print(f"H_mon n=4, pi=0.5, {lab}: {r:.4f} +- {se:.4f}")
print(f"total {time.time()-t0:.1f}s")
