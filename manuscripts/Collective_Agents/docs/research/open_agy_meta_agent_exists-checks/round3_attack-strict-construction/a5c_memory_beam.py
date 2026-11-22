r"""A5c (attack): deeper beam search (frozen-reachable sequences) for the exact Markov defect of the declared coarse
variable.  Per-member menu each round: sigma in {0,1}, attend 0 or all 3 mates, n_o in {0, all open mates attended}.
Objective: running max of the exact I_t.  Starting state: stationary base 0000 (the typical state).
Declared expectation: unknown; FALSIFIES the headline alpha_M = 0.02 (literal sup reading) if the max exceeds 0.02.
NEGATIVE CONTROL: I_t <= d_cl(t) at every evaluated step.
"""
import itertools, sys, time
import numpy as np
from mylib import Cfg
from memlib import Tracker, base_cfgs

t0 = time.time()
c = Cfg()
B = int(sys.argv[1]) if len(sys.argv) > 1 else 10
D = int(sys.argv[2]) if len(sys.argv) > 2 else 10
tr0 = Tracker(c)
for _ in range(400):
    tr0.step(base_cfgs((0, 0, 0, 0)))
def menu(sp, i):
    kopen = sum(sp[j] for j in range(4) if j != i)
    out = []
    for o in (0, 1):
        out.append((o, 0, 0))
        out.append((o, 3, kopen))
        if kopen > 0:
            out.append((o, 3, 0))
    return out
viol = 0
beam = [(0.0, 0.0, tr0, (0, 0, 0, 0), [])]
for depth in range(D):
    new = []
    for score, last, tr, sp, hist in beam:
        for cfg in itertools.product(*[menu(sp, i) for i in range(4)]):
            t2 = tr.copy()
            a, b = t2.step(list(cfg))
            if a > b + 1e-12:
                viol += 1
            new.append((max(score, a), a, t2, tuple(cc[0] for cc in cfg), hist + [cfg]))
    # keep the best by running max, plus diversity by last-step value
    new.sort(key=lambda z: -z[0])
    keep = new[:B // 2]
    new.sort(key=lambda z: -z[1])
    keep += new[:B - len(keep)]
    beam = keep
    print(f"depth {depth+1}: best running max {max(z[0] for z in beam):.4e}  ({time.time()-t0:.0f}s)", flush=True)
    if time.time() - t0 > 120:
        break
best = max(beam, key=lambda z: z[0])
print("worst sequence:")
for cfg in best[4]:
    print("   ", cfg)
print(f"WORST exact I {best[0]:.4e}; exceeds 0.02: {best[0] > 0.02}; NEG violations {viol} (expected 0)")
