r"""A5e (attack): hill-climbing over periodic patterns (period 2 and 4) with the full per-member menu, from the
beam's alternation; plus the same with statuses held fixed (attention-only alternation, reachable under the
real-time protocol, where at most one status changes per round).
Declared expectation: the local optimum stays below 0.02 (unknown). NEGATIVE CONTROL: I_t <= d_cl(t).
"""
import time, copy
import numpy as np
from mylib import Cfg
from memlib import Tracker, base_cfgs

t0 = time.time()
c = Cfg()
rng = np.random.default_rng(13)
viol = 0
def score(phases, nper=30, warm=150):
    global viol
    tr = Tracker(c)
    for _ in range(warm):
        tr.step(base_cfgs((0, 0, 0, 0)))
    sp = (0, 0, 0, 0); best = 0.0
    for k in range(nper):
        for sig, att in phases:
            cfg = []
            for i in range(4):
                kopen = sum(sp[j] for j in range(4) if j != i)
                cfg.append((sig[i], att[i][0], min(att[i][1], kopen, att[i][0])))
            a, b = tr.step(cfg)
            if a > b + 1e-12: viol += 1
            if k >= nper // 2: best = max(best, a)
            sp = sig
    return best
def mutate(phases, fix_sig):
    ph = copy.deepcopy(phases)
    k = int(rng.integers(len(ph))); i = int(rng.integers(4))
    sig, att = list(ph[k][0]), [list(a) for a in ph[k][1]]
    r = rng.random()
    if r < 0.3 and not fix_sig:
        sig[i] = 1 - sig[i]
    elif r < 0.65:
        att[i][0] = int(rng.integers(0, 4))
    else:
        att[i][1] = int(rng.integers(0, 4))
    ph[k] = (tuple(sig), [tuple(a) for a in att])
    return ph
start = [((0, 0, 0, 1), [(0, 0), (0, 0), (0, 0), (3, 3)]), ((1, 1, 1, 0), [(3, 3), (3, 3), (3, 3), (0, 0)])]
for label, fix_sig, init in (("period 2 free", False, start), ("period 4 free", False, start + start),
                             ("period 2 sigma fixed 0000", True,
                              [((0, 0, 0, 0), [(0, 0), (0, 0), (0, 0), (3, 0)]), ((0, 0, 0, 0), [(3, 0), (3, 0), (3, 0), (0, 0)])]),
                             ("period 2 sigma fixed 1111", True,
                              [((1, 1, 1, 1), [(0, 0), (0, 0), (0, 0), (3, 3)]), ((1, 1, 1, 1), [(3, 3), (3, 3), (3, 3), (0, 0)])])):
    cur = init; cs = score(cur)
    t1 = time.time()
    while time.time() - t1 < 25:
        nw = mutate(cur, fix_sig); ns = score(nw)
        if ns >= cs:
            cur, cs = nw, ns
    print(f"{label}: local optimum exact I {cs:.4e} at {cur}  ({time.time()-t0:.0f}s)", flush=True)
print(f"NEG violations {viol} (expected 0)")
