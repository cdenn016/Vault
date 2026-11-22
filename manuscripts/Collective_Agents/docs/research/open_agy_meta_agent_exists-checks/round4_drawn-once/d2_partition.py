r"""Drawn-once partner randomization, scored by the selected partition itself.

Statistic (d): the selector's output at the declared level r0 (the set of regions that are
collectives, an agent in no collective left unassigned), compared with the full model's
output {A}.  A null draw "agrees" with the full model when its output is exactly {A}.
Non-diffusive draws have no collective (reading (b)) or are excluded (reported both ways).
The comparison medium (baseline) is held at the full model's value, so a region is a
collective at level r0 when the draw's precision is diffusive and r(C) >= r0 (> baseline).
Collectives here are taken as maximal regions at the level: a region at level r0 that
contains another region at level r0 is kept, and the output is the family of all regions
with r >= r0 (reported in full, so the reader can apply another convention).

Declared expectations before running:
  P0 (r0 = 4.5): only the all-source pattern outputs {A}: P = 1/256; pair patterns output
     pairs at 4.887.
  P1 (r0 = 4.45): every pattern in which all four members read the source and the draw is
     diffusive outputs {A} (r(A) = 5.3541): P = (number of such diffusive patterns)/1296,
     about 81/1296 = 0.0625 if all of them are diffusive.
"""
from __future__ import annotations

import itertools
import os
import sys
from collections import Counter

os.environ.setdefault("OMP_NUM_THREADS", "1")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np

from fixedlib import sigma_fixed, is_diffusive, contrast, regions

A = (1, 2, 3, 4)
others = {i: [j for j in range(5) if j != i] for i in A}


def output(pat, r0):
    reads = [()] + [tuple(p) if isinstance(p, tuple) else (p,) for p in pat]
    Sig = sigma_fixed(reads)
    Pi = np.linalg.inv(Sig)
    dif = is_diffusive(Pi)[0]
    if not dif:
        return None
    out = tuple(sorted(tuple(C) for C in regions(5) if contrast(Pi, C) >= r0))
    return out


def run(pats, r0, label):
    outs = [output(p, r0) for p in pats]
    K = len(pats)
    cnt = Counter(outs)
    nd = cnt.pop(None, 0)
    same = cnt.get(((1, 2, 3, 4),), 0)
    print(f"\n=== {label}, r0 = {r0}: {K} patterns, {nd} non-diffusive ===")
    print(f"output exactly {{A}}: {same}/{K} = {same / K:.6f}")
    print(f"output contains A: {sum(v for k, v in cnt.items() if (1, 2, 3, 4) in k)}/{K}")
    print(f"output empty (diffusive, no region at r0): {cnt.get((), 0)}/{K}")
    for k, v in sorted(cnt.items(), key=lambda kv: -kv[1])[:8]:
        print(f"   {v:5d} x output {k}")
    print(f"if non-diffusive draws are excluded and the rest renormalized: P(output = {{A}}) = {same / (K - nd):.6f}")
    allS = [p for p in pats if all((0 in (q if isinstance(q, tuple) else (q,))) for q in p)]
    print(f"patterns in which every member reads the source: {len(allS)}")
    return same / K


pats0 = list(itertools.product(*[others[i] for i in A]))
run(pats0, 4.5, "P0 drawn once")
pairs = {i: list(itertools.combinations(others[i], 2)) for i in A}
pats1 = list(itertools.product(*[pairs[i] for i in A]))
run(pats1, 4.45, "P1 drawn once")
