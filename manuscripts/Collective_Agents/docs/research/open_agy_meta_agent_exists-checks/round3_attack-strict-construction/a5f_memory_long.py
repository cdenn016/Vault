r"""A5f (attack): hill-climbing over longer periodic patterns (period 6 and 8), two restarts each (one from the
period-4 optimum of A5e repeated, one random), full per-member menu (frozen-reachable).
Declared expectation: unknown; FALSIFIES alpha_M = 0.02 (literal sup) if > 0.02. NEGATIVE CONTROL: I_t <= d_cl(t).
"""
import sys, time, copy
import numpy as np
from mylib import Cfg
from memlib import Tracker, base_cfgs

t0 = time.time()
c = Cfg()
rng = np.random.default_rng(int(sys.argv[1]) if len(sys.argv) > 1 else 17)
viol = 0
def score(phases, nper=None, warm=120):
    global viol
    L = len(phases)
    nper = nper or max(6, 60 // L)
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
p4 = [((1, 1, 1, 0), [(0, 0), (0, 1), (0, 2), (3, 1)]), ((1, 1, 1, 0), [(3, 2), (3, 2), (3, 3), (0, 3)]),
      ((0, 0, 0, 1), [(0, 1), (0, 0), (0, 1), (3, 3)]), ((0, 0, 0, 0), [(3, 0), (3, 0), (3, 0), (0, 0)])]
def rand_phase():
    return (tuple(int(x) for x in rng.integers(0, 2, 4)), [(int(rng.integers(0, 4)), int(rng.integers(0, 4))) for _ in range(4)])
best_all = 0.0
for label, init in (("period 8 from p4 x2", p4 + p4), ("period 6 random", [rand_phase() for _ in range(6)]),
                    ("period 8 random", [rand_phase() for _ in range(8)])):
    cur = init; cs = score(cur); t1 = time.time()
    while time.time() - t1 < 36:
        nw = mutate(cur); ns = score(nw)
        if ns >= cs:
            cur, cs = nw, ns
    best_all = max(best_all, cs)
    print(f"{label}: local optimum exact I {cs:.4e}  ({time.time()-t0:.0f}s)", flush=True)
    print("    ", cur)
print(f"WORST {best_all:.4e}; exceeds 0.02: {best_all > 0.02}; NEG violations {viol} (expected 0)")
