r"""A5h (attack): simulated annealing over aperiodic frozen-reachable sequences of 24 rounds (after a 120-round warm-up
at the typical base 0000), objective = max exact I_t over the 24 rounds and 6 trailing base rounds.  Two chains, one
started from the period-16 optimum of A5g (first 16 rounds + 8 base rounds), one from random.
Declared expectation: unknown; FALSIFIES alpha_M = 0.02 under the literal supremum if > 0.02. NEG: I_t <= d_cl(t).
"""
import time, copy
import numpy as np
from mylib import Cfg
from memlib import Tracker, base_cfgs
t0 = time.time()
c = Cfg()
rng = np.random.default_rng(29)
viol = 0
warm = Tracker(c)
for _ in range(120):
    warm.step(base_cfgs((0, 0, 0, 0)))
def score(seq):
    global viol
    tr = warm.copy(); sp = (0, 0, 0, 0); best = 0.0
    for sig, att in seq + [((0, 0, 0, 0), [(3, 0)] * 4)] * 6:
        cfg = [(sig[i], att[i][0], min(att[i][1], sum(sp[j] for j in range(4) if j != i), att[i][0])) for i in range(4)]
        a, b = tr.step(cfg)
        if a > b + 1e-12: viol += 1
        best = max(best, a); sp = sig
    return best
def mutate(seq):
    s = copy.deepcopy(seq)
    for _ in range(int(rng.integers(1, 4))):
        k = int(rng.integers(len(s))); i = int(rng.integers(4))
        sig, att = list(s[k][0]), [list(a) for a in s[k][1]]
        r = rng.random()
        if r < 0.3: sig[i] = 1 - sig[i]
        elif r < 0.65: att[i][0] = int(rng.integers(0, 4))
        else: att[i][1] = int(rng.integers(0, 4))
        s[k] = (tuple(sig), [tuple(a) for a in att])
    return s
p16 = [((0, 0, 0, 0), [(0, 1), (0, 0), (0, 2), (0, 2)]), ((0, 0, 0, 0), [(0, 2), (0, 0), (0, 2), (0, 2)]),
       ((0, 0, 0, 0), [(0, 3), (0, 1), (0, 3), (0, 1)]), ((0, 0, 0, 0), [(0, 0), (0, 2), (0, 3), (0, 3)]),
       ((0, 0, 0, 0), [(0, 0), (0, 3), (0, 2), (0, 2)]), ((0, 0, 0, 0), [(0, 3), (0, 1), (0, 2), (0, 1)]),
       ((0, 0, 0, 0), [(0, 3), (0, 2), (0, 0), (3, 2)]), ((0, 0, 0, 0), [(3, 1), (3, 2), (3, 3), (0, 0)]),
       ((1, 1, 1, 0), [(0, 3), (0, 3), (0, 0), (3, 0)]), ((1, 1, 1, 0), [(3, 2), (3, 2), (3, 2), (0, 1)]),
       ((0, 0, 0, 1), [(0, 2), (0, 0), (0, 3), (3, 3)]), ((0, 0, 0, 0), [(0, 3), (0, 1), (0, 1), (0, 1)])]
base = ((0, 0, 0, 0), [(3, 0)] * 4)
starts = [(p16 + p16)[:24], [(tuple(int(x) for x in rng.integers(0, 2, 4)), [(int(rng.integers(0, 4)), int(rng.integers(0, 4))) for _ in range(4)]) for _ in range(24)]]
best_all = 0.0
for ci, init in enumerate(starts):
    cur = init; cs = score(cur); best = cs; T0 = 2e-3; t1 = time.time(); it = 0
    while time.time() - t1 < 52:
        it += 1
        temp = T0 * (1 - (time.time() - t1) / 52) + 1e-6
        nw = mutate(cur); ns = score(nw)
        if ns >= cs or rng.random() < np.exp((ns - cs) / temp):
            cur, cs = nw, ns
            best = max(best, cs)
    best_all = max(best_all, best)
    print(f"chain {ci}: {it} iterations, best exact I {best:.4e}  ({time.time()-t0:.0f}s)", flush=True)
print(f"WORST {best_all:.4e}; exceeds 0.02: {best_all > 0.02}; NEG violations {viol} (expected 0)")
