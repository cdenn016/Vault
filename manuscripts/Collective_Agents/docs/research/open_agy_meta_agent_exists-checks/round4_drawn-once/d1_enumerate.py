r"""Drawn-once partner randomization for the audience instances P0 (one partner per
member) and P1 (two partners per member), by exact enumeration of the fixed patterns.

Declared expectations before running:
  E1 (validation) all-source P0 pattern gives r(A) = 5.384864 and 54/256 diffusive
     patterns (values of the round-3 rebuild); hundredfold Rc gives r(A) near 1.07.
  E2 (P0, contrast scoring) no diffusive pattern other than all-source reaches 5.3849,
     so P(S >= S0) = 1/256 if non-diffusive draws select nothing and 203/256 if they
     are counted as exceeding.
  E3 (MI-ratio selector) for a source plus an exchangeable audience the statistic is
     below 1.5 (two-block balanced bipartitions split the audience), so many patterns
     with isolated member pairs exceed it and the test does not reject.
  E4 (P1) fewer than half of the 6^4 patterns are diffusive.
"""
from __future__ import annotations

import itertools
import os
import sys
from collections import Counter

os.environ.setdefault("OMP_NUM_THREADS", "1")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from scipy.stats import binom

from fixedlib import sigma_fixed, is_diffusive, contrast, max_region, mi_ratio

n = 4
others = {i: [j for j in range(n + 1) if j != i] for i in range(1, n + 1)}
A = [1, 2, 3, 4]


def analyze(patterns: list[tuple], label: str, S0_contrast: float, S0_mi: float) -> dict:
    rows = []
    for pat in patterns:
        reads = [()] + [tuple(p) if isinstance(p, tuple) else (p,) for p in pat]
        Sig = sigma_fixed(reads)
        Pi = np.linalg.inv(Sig)
        dif, offmax, rsmin = is_diffusive(Pi)
        mr, marg = (max_region(Pi) if dif else (np.nan, None))
        rA = contrast(Pi, A) if dif else np.nan
        mi, miarg = mi_ratio(Sig)
        rows.append(dict(pat=pat, dif=dif, offmax=offmax, rsmin=rsmin, maxr=mr, arg=marg, rA=rA, mi=mi, miarg=miarg))
    K = len(rows)
    ndif = sum(r["dif"] for r in rows)
    ge_dif = sum(1 for r in rows if r["dif"] and r["maxr"] >= S0_contrast - 1e-9)
    near = sorted([r for r in rows if r["dif"]], key=lambda r: -r["maxr"])[:6]
    ge_mi = sum(1 for r in rows if r["mi"] >= S0_mi - 1e-12)
    inf_mi = sum(1 for r in rows if np.isinf(r["mi"]))
    print(f"\n=== {label}: {K} equally likely fixed patterns ===")
    print(f"diffusive: {ndif}/{K}")
    print(f"full-model statistics: largest regional contrast S0 = {S0_contrast:.6f}; MI ratio S0 = {S0_mi:.6f}")
    print("largest regional contrast among diffusive patterns (top 6):")
    for r in near:
        print(f"   {r['pat']}: max r = {r['maxr']:.4f} on {r['arg']}, r(A) = {r['rA']:.4f}")
    p_a = (ge_dif + (K - ndif)) / K
    p_b = ge_dif / K
    p_c = ge_mi / K
    print(f"(a) contrast, non-diffusive counted as exceeding: P(S>=S0) = {ge_dif + K - ndif}/{K} = {p_a:.6f}")
    print(f"(b) contrast, non-diffusive select nothing:       P(S>=S0) = {ge_dif}/{K} = {p_b:.6f}")
    print(f"(c) MI-ratio selector on every draw:               P(S>=S0) = {ge_mi}/{K} = {p_c:.6f} ({inf_mi} draws infinite)")
    for lab, p in (("a", p_a), ("b", p_b), ("c", p_c)):
        # n_null = 999 draws, p = (1 + #{S_l >= S0})/1000 <= 0.01  iff  # <= 9
        prej = binom.cdf(9, 999, p)
        Ep = (1 + 999 * p) / 1000
        print(f"   reading ({lab}): with n_null=999, E[p] = {Ep:.5f}, P(p <= 0.01) = {prej:.4f}")
    mis = np.array([r["mi"] for r in rows])
    fin = mis[np.isfinite(mis)]
    print(f"MI-ratio over draws: median {np.median(mis):.4f}, finite max {fin.max():.4f}, min {mis.min():.4f}")
    return dict(rows=rows, ndif=ndif)


# ---------------- E1 validation ----------------
Sig0 = sigma_fixed([(), (0,), (0,), (0,), (0,)])
Pi0 = np.linalg.inv(Sig0)
print("E1 all-source P0 pattern: r(A) =", f"{contrast(Pi0, A):.6f}", "(expect 5.384864);",
      "diffusive", is_diffusive(Pi0)[0], "; entries", f"sigma={Sig0[0,0]:.6e} c={Sig0[0,1]:.6e} var={Sig0[1,1]:.6e} beta={Sig0[1,2]:.6e}")
SigN = sigma_fixed([(), (0,), (0,), (0,), (0,)], Rc=0.2)
print("E1 negative control, Rc x100: r(A) =", f"{contrast(np.linalg.inv(SigN), A):.4f}", "(expect about 1.07)")
SigC = sigma_fixed([(), (0,), (0,), (0,), (0,)], cond_vS=True)
print("E1 control, source sensing noise conditioned: max |offdiag among members| =",
      f"{np.abs(SigC[1:,1:][~np.eye(4, dtype=bool)]).max():.2e}")
mi0, mi0arg = mi_ratio(Sig0)
print(f"MI ratio of the all-source pattern: {mi0:.6f} on {mi0arg}")

# ---------------- P0 drawn once: one fixed partner per member ----------------
pats0 = list(itertools.product(*[others[i] for i in A]))
res0 = analyze(pats0, "P0 drawn once (one partner)", S0_contrast=contrast(Pi0, A), S0_mi=mi0)

# ---------------- P1 drawn once: two fixed partners per member ----------------
pairs = {i: list(itertools.combinations(others[i], 2)) for i in A}
pats1 = list(itertools.product(*[pairs[i] for i in A]))
# Full P1 model statistic: r(A) from the two Monte Carlo estimates (5.3724, 5.3752 +- 0.007);
# take the lower one so that the count of exceeding draws is not understated.
res1 = analyze(pats1, "P1 drawn once (two partners)", S0_contrast=5.3724, S0_mi=1.5)
print("\nNote: for P1 the MI-ratio statistic of the full model is bounded by 1.5 for any source plus"
      " exchangeable audience (see the closed form in the record); 1.5 is used as an upper bound, so"
      " the count of exceeding draws in (c) is a lower bound.")
