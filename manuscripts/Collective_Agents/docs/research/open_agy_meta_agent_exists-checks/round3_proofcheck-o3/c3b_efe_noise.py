r"""Does the EFE corollary of C3b survive prediction (computation) noise?
Declared expectation (reconstruction): with eps = 0 cross entries are positive (corollary).  With
large prediction noise and a_1 a_2 < 0 (firms with opposite-sign world models, so phi1 phi2 < 0
while phi_k kappa_k > 0), sign(V_12) -> -sign(kappa1 kappa2) = +, so cross entries can turn
negative.  With a_1 a_2 > 0 no flip is expected at moderate noise.
"""
import os
os.environ.setdefault("OMP_NUM_THREADS", "1")
import numpy as np
src = open("c3b_sign.py").read().split("# S1, S2, N1")[0]
exec(src)
for label, same in [("a1 a2 < 0", False), ("a1 a2 > 0", True)]:
    flips = used = 0
    example = None
    while used < 150:
        p = draw(efe=True)
        if (p["a"][0] * p["a"][1] > 0) != same:
            continue
        o0 = cross_and_V(p, 0.0)
        se2 = 10 ** rng.uniform(-1, 1.3)
        o1 = cross_and_V(p, se2)
        if o0 is None or o1 is None:
            continue
        used += 1
        assert np.min(o0[0]) > 0
        if np.min(o1[0]) < 0:
            flips += 1
            if example is None:
                example = (p, se2, o0[0][0, 0], o1[0][0, 0], o1[2])
    print(f"EFE firms, {label}: cross entries turn negative under prediction noise in {flips}/{used}")
    if example is not None:
        p, se2, c0v, c1v, Pi = example
        offd = Pi[~np.eye(Pi.shape[0], dtype=bool)]
        diffusive = np.max(offd) <= 0 and np.min(Pi.sum(1)) >= 0
        print("  example:", {k: (np.round(v, 4).tolist() if hasattr(v, '__len__') else round(float(v), 4)) for k, v in p.items()},
              f"se2={se2:.3f}, cross without noise {c0v:.3e}, with noise {c1v:.3e}; Pi^c diffusive with noise: {diffusive}")
