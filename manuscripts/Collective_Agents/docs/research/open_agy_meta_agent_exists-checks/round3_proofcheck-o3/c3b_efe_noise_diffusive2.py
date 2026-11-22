r"""Refinement of c3b_efe_noise_diffusive.py: exclude near-inactive firms.
Restrict to EFE-consistent firm pairs with |a_k| >= 0.3 and |g_k| >= 0.02 (both firms act
non-trivially), a1 a2 < 0, prediction noise variance 10^U(-1, 1.3).
Declared expectation: exploratory; report the count of diffusive Pi^c and one example with the
cross entries, the largest off-diagonal entry and the smallest row sum.
"""
import os
os.environ.setdefault("OMP_NUM_THREADS", "1")
import numpy as np
exec(open("c3b_sign.py").read().split("# S1, S2, N1")[0])
nd = used = 0
ex = None
while used < 400:
    p = draw(efe=True)
    if p["a"][0] * p["a"][1] > 0 or np.min(np.abs(p["a"])) < 0.3 or np.min(np.abs(p["g"])) < 0.02:
        continue
    se2 = 10 ** rng.uniform(-1, 1.3)
    o1 = cross_and_V(p, se2)
    o0 = cross_and_V(p, 0.0)
    if o1 is None or o0 is None:
        continue
    used += 1
    Pi = o1[2]
    offd = Pi[~np.eye(Pi.shape[0], dtype=bool)]
    if np.max(offd) <= 0 and np.min(Pi.sum(1)) >= 0:
        nd += 1
        if ex is None:
            ex = (p, se2, Pi, o0[0])
print(f"EFE firms, a1 a2 < 0, |a_k| >= 0.3, |g_k| >= 0.02, prediction noise: Pi^c diffusive in {nd}/{used}")
if ex is not None:
    p, se2, Pi, cr0 = ex
    n1 = p["n"][0]
    offd = Pi[~np.eye(Pi.shape[0], dtype=bool)]
    print("  example:", {k: (np.round(v, 4).tolist() if hasattr(v, '__len__') else round(float(v), 4)) for k, v in p.items()}, f"se2={se2:.3f}")
    print(f"  with noise: cross entry {Pi[0, n1]:.4e}, largest off-diagonal {offd.max():.4e}, smallest row sum {Pi.sum(1).min():.4e}")
    print(f"  without noise: cross entry {cr0[0, 0]:.4e} (positive, non-diffusive)")
