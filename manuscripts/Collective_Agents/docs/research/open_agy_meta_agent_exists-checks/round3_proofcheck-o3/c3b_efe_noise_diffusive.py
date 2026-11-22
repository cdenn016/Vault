r"""Follow-up: among EFE-consistent firm pairs (correct effect sign) with prediction noise, is the
whole Pi^c ever diffusive?  The corollary (no prediction noise) says never.
Declared expectation: unknown (exploratory); a diffusive case would show that the corollary's
conclusion depends on the absence of prediction noise, not only that the sign argument does.
Search: a1 a2 < 0, prediction noise variance 10^U(-1, 1.3), 400 draws.
"""
import os
os.environ.setdefault("OMP_NUM_THREADS", "1")
import numpy as np
exec(open("c3b_sign.py").read().split("# S1, S2, N1")[0])
nd = used = 0
ex = None
while used < 400:
    p = draw(efe=True)
    if p["a"][0] * p["a"][1] > 0:
        continue
    se2 = 10 ** rng.uniform(-1, 1.3)
    o1 = cross_and_V(p, se2)
    if o1 is None:
        continue
    used += 1
    Pi = o1[2]
    offd = Pi[~np.eye(Pi.shape[0], dtype=bool)]
    if np.max(offd) <= 0 and np.min(Pi.sum(1)) >= 0:
        nd += 1
        if ex is None:
            ex = (p, se2, Pi)
print(f"EFE firms with a1 a2 < 0 and prediction noise: Pi^c diffusive in {nd}/{used}")
if ex is not None:
    p, se2, Pi = ex
    print("  example:", {k: (np.round(v, 4).tolist() if hasattr(v, '__len__') else round(float(v), 4)) for k, v in p.items()}, f"se2={se2:.3f}")
    print("  Pi^c =\n", np.round(Pi, 4))
    # same parameters without noise: cross entries
    o0 = cross_and_V(p, 0.0)
    print("  without prediction noise: min cross entry", o0[0].min())
