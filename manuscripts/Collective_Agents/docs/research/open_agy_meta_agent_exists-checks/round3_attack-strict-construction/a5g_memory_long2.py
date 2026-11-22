r"""A5g (attack): continue the hill-climb from the period-8 optimum of A5f (0.01576), periods 8 and 16
(16 = the optimum twice, mutated independently).  Same scoring and reachability as A5f (frozen-reachable).
Declared expectation: unknown; FALSIFIES alpha_M = 0.02 under the literal supremum if > 0.02. NEG: I_t <= d_cl(t).
"""
import time, copy
import numpy as np
from mylib import Cfg
from memlib import Tracker, base_cfgs
t0 = time.time()
c = Cfg()
rng = np.random.default_rng(23)
viol = 0
def score(phases, warm=120):
    global viol
    L = len(phases); nper = max(5, 64 // L)
    tr = Tracker(c)
    for _ in range(warm):
        tr.step(base_cfgs((0, 0, 0, 0)))
    sp = (0, 0, 0, 0); best = 0.0
    for k in range(nper):
        for sig, att in phases:
            cfg = [(sig[i], att[i][0], min(att[i][1], sum(sp[j] for j in range(4) if j != i), att[i][0])) for i in range(4)]
            a, b = tr.step(cfg)
            if a > b + 1e-12: viol += 1
            if k >= nper // 2: best = max(best, a)
            sp = sig
    return best
def mutate(ph):
    ph = copy.deepcopy(ph)
    for _ in range(int(rng.integers(1, 3))):
        k = int(rng.integers(len(ph))); i = int(rng.integers(4))
        sig, att = list(ph[k][0]), [list(a) for a in ph[k][1]]
        r = rng.random()
        if r < 0.3: sig[i] = 1 - sig[i]
        elif r < 0.65: att[i][0] = int(rng.integers(0, 4))
        else: att[i][1] = int(rng.integers(0, 4))
        ph[k] = (tuple(sig), [tuple(a) for a in att])
    return ph
p8 = [((1, 1, 1, 0), [(0, 1), (0, 3), (0, 1), (3, 1)]), ((1, 1, 1, 0), [(3, 2), (3, 3), (3, 2), (0, 3)]),
      ((0, 0, 0, 1), [(0, 2), (0, 2), (0, 3), (3, 3)]), ((0, 0, 0, 0), [(0, 1), (0, 0), (0, 1), (0, 1)]),
      ((0, 0, 0, 0), [(0, 3), (0, 3), (0, 3), (0, 3)]), ((0, 0, 0, 0), [(0, 2), (0, 0), (0, 0), (0, 1)]),
      ((0, 0, 0, 0), [(0, 3), (0, 1), (0, 3), (3, 0)]), ((0, 0, 0, 0), [(3, 3), (3, 2), (3, 0), (0, 3)])]
best_all = 0.0
for label, init, budget in (("period 8 continued", p8, 55), ("period 16", p8 + p8, 55)):
    cur = init; cs = score(cur); t1 = time.time()
    while time.time() - t1 < budget:
        nw = mutate(cur); ns = score(nw)
        if ns >= cs:
            cur, cs = nw, ns
    best_all = max(best_all, cs)
    print(f"{label}: local optimum exact I {cs:.4e}  ({time.time()-t0:.0f}s)", flush=True)
    print("    ", cur)
print(f"WORST {best_all:.4e}; exceeds 0.02: {best_all > 0.02}; NEG violations {viol} (expected 0)")
