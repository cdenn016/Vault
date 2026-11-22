"""Deciding script 3: robustness on the box P0, s, c, gamma in [0.8, 1.2] x declared value (3^4 = 81 points),
plus a quenched partner-randomization test (199 draws) at the 16 corners.
Expected: at every point, diffusive with beta > 0; lower window end < r0 <= r(A) for the declared r0;
agency index >= 0.99; alpha_I <= 0.01; every type-D null contrast < r0."""
import itertools, math
import numpy as np
from core import *
n, N, kappa, s2 = 4, 8, 3, 1e-3


def att_full(i, p):
    return [(tuple(j for j in range(n) if j != i), 1.0)]


def att_random(i, p):
    lst = []
    for r in range(0, min(kappa, n - 1) + 1):
        if kappa - r > N - n: continue
        pr = math.comb(N - n, kappa - r) / math.comb(N - 1, kappa)
        lst += [(U, pr) for U in itertools.combinations([j for j in range(n) if j != i], r)]
    return lst
base = dict(P0=1.0, s=1.0, c=0.1, gam=4.0)
rows = []
rng = np.random.default_rng(11)
for fP, fs, fc, fg in itertools.product((0.8, 1.0, 1.2), repeat=4):
    P0, s, c, gam = base["P0"] * fP, base["s"] * fs, base["c"] * fc, base["gam"] * fg
    law, _ = deliberation_law(n, n - 1, P0, s, c, gam)
    SA = sigma_c_enum(n, law, att_full, P0, s, c, s2)
    Pi = np.linalg.inv(block_diag(SA, SA)); dif = diffusive(Pi)[0] and SA[0, 1] > 0
    rA = contrast(Pi, range(n)); rsub = contrast(Pi, range(n - 1))
    lawN, _ = deliberation_law(N, kappa, P0, s, c, gam)
    rmech = contrast(np.linalg.inv(sigma_c_capacity(N, lawN, kappa, P0, s, c, s2)), range(N))
    a = -(Pi - np.diag(np.diag(Pi))); rmean = 1 + N * a[np.triu_indices(N, 1)].mean() / Pi.sum(1).mean()
    Sh = sigma_c_enum(n, np.full(2 ** n, 2.0 ** -n), att_random, P0, s, c, s2)
    rhab = contrast(np.linalg.inv(block_diag(Sh, Sh)), range(n))
    Sp = sigma_c_enum(n, law, att_random, P0, s, c, s2)
    rpr = contrast(np.linalg.inv(block_diag(Sp, Sp)), range(n))
    ag = agency_index(law, n, P0, s)[0]
    aI = inference_kl(n, law, P0, s, c, s2)
    rows.append((fP, fs, fc, fg, dif, rA, rsub, rmech, rmean, rhab, rpr, ag, aI))
R = np.array([r[4:] for r in rows], float)
names = ["diffusive&beta>0", "r(A)", "r_sub", "rhom_mech", "rhom_mean", "r_hab", "r_pr_ann", "Agency", "alpha_I"]
for k, nm in enumerate(names):
    print(f"{nm:18s} min {R[:, k].min():.6g}  max {R[:, k].max():.6g}")
lo_mech = np.max(R[:, [2, 3, 5, 6]], axis=1); lo_mean = np.max(R[:, [2, 4, 5, 6]], axis=1)
for r0 in (36.0, 45.0, 50.0):
    print(f"r0={r0}: (c)-mechanism admissible+selected at {np.sum((lo_mech < r0) & (R[:, 1] >= r0))}/81;"
          f" (c)-mean at {np.sum((lo_mean < r0) & (R[:, 1] >= r0))}/81")
print("min margin r(A)-lo_mech", (R[:, 1] - lo_mech).min(), "| min margin r(A)-lo_mean", (R[:, 1] - lo_mean).min())

# quenched partner randomization at the corners
worst = 0.0; nd = 0; tot = 0
for fP, fs, fc, fg in itertools.product((0.8, 1.2), repeat=4):
    P0, s, c, gam = base["P0"] * fP, base["s"] * fs, base["c"] * fc, base["gam"] * fg
    law, _ = deliberation_law(n, n - 1, P0, s, c, gam)
    for l in range(199):
        T = [rng.choice([j for j in range(N) if j != i], size=kappa, replace=False) for i in range(N)]
        blocks = [sigma_c_enum(n, law, lambda i, p, U=[tuple(int(j) - b for j in T[b + i] if b <= j < b + n)
                  for i in range(n)]: [(U[i], 1.0)], P0, s, c, s2) for b in (0, n)]
        Pi = np.linalg.inv(block_diag(*blocks)); tot += 1
        if not diffusive(Pi)[0]:
            nd += 1; continue
        worst = max(worst, min(contrast(Pi, range(n)), contrast(Pi, range(n, N))))
print("corners quenched N_pr: draws", tot, "non-diffusive", nd, "| largest S_l among diffusive draws", worst)
