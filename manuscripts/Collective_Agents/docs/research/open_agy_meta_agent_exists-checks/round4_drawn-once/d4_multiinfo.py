r"""Drawn-once partner randomization scored by a statistic defined on every draw.

Statistic: the largest world-conditional multi-information (total correlation) over regions of
four agents, TC(C) = 1/2 [sum_{i in C} ln Sigma_ii - ln det Sigma_CC], which needs no diffusive
precision.  Also reported: TC(A) for the audience A = {1,2,3,4}.

Question: does any non-diffusive drawn-once draw carry coherence of the audience's size at the
full model's level?  If not, scoring non-diffusive draws as selecting nothing does not hide
A-like structure in these populations.

Declared expectations: only the all-source pattern (P0) reaches the full model's TC(A); in P1
no fixed pattern reaches the full model's TC(A), since the full model's routing mixture has
the larger common mode; every non-diffusive draw has TC well below.
Full P1 covariance from the round-4 blind recomputation (Monte Carlo): Var e_S 0.0060718414,
Cov(S,m) 6.537e-4, Var m 7.5173e-3, Cov(m,m') 4.0046e-3.
"""
from __future__ import annotations

import itertools
import os
import sys

os.environ.setdefault("OMP_NUM_THREADS", "1")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np

from fixedlib import sigma_fixed, is_diffusive

A = (1, 2, 3, 4)
others = {i: [j for j in range(5) if j != i] for i in A}
regions4 = [list(c) for c in itertools.combinations(range(5), 4)]


def tc(S: np.ndarray, C) -> float:
    sub = S[np.ix_(C, C)]
    return 0.5 * (np.sum(np.log(np.diag(sub))) - np.linalg.slogdet(sub)[1])


def run(pats, label, tc_full):
    rows = []
    for p in pats:
        reads = [()] + [tuple(q) if isinstance(q, tuple) else (q,) for q in p]
        S = sigma_fixed(reads)
        dif = is_diffusive(np.linalg.inv(S))[0]
        t4 = max(tc(S, C) for C in regions4)
        rows.append((p, dif, tc(S, list(A)), t4))
    K = len(rows)
    ge = [r for r in rows if r[3] >= tc_full - 1e-12]
    nd = [r for r in rows if not r[1]]
    print(f"\n=== {label}: {K} patterns; full model TC(A) = {tc_full:.6f}")
    print(f"patterns with largest 4-region TC >= full TC(A): {len(ge)}/{K}: {[r[0] for r in ge][:5]}")
    print(f"non-diffusive patterns: {len(nd)}; their largest 4-region TC: max {max(r[3] for r in nd):.6f}, median {np.median([r[3] for r in nd]):.6f}")
    dd = sorted([r for r in rows if r[1]], key=lambda r: -r[3])[:4]
    print("diffusive patterns with the largest 4-region TC:", [(r[0], round(r[3], 6)) for r in dd])
    print(f"P(S_l >= S_0) = {len(ge)}/{K} = {len(ge) / K:.6f}")


S0 = sigma_fixed([(), (0,), (0,), (0,), (0,)])
run(list(itertools.product(*[others[i] for i in A])), "P0 drawn once", tc(S0, list(A)))

v, c = 7.5173e-3, 4.0046e-3
S1A = (v - c) * np.eye(4) + c * np.ones((4, 4))
tc1 = 0.5 * (4 * np.log(v) - np.linalg.slogdet(S1A)[1])
pairs = {i: list(itertools.combinations(others[i], 2)) for i in A}
run(list(itertools.product(*[pairs[i] for i in A])), "P1 drawn once (two partners)", tc1)

# negative control: the statistic must rise with the common mode; R_c x 100 on the all-source pattern
Sn = sigma_fixed([(), (0,), (0,), (0,), (0,)], Rc=0.2)
print(f"\nnegative control, R_c x100 all-source: TC(A) = {tc(Sn, list(A)):.6f} (expect far below {tc(S0, list(A)):.6f})")
