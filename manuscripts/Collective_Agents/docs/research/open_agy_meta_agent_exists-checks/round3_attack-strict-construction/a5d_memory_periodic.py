r"""A5d (attack): periodic adversarial patterns for the exact Markov defect (all frozen-reachable).
(1) the beam's period-2 alternation run for 200 periods: periodic steady-state exact I;
(2) exhaustive period-2 patterns: every member alternates between two configurations X_i, Y_i drawn from the full
    per-member menu (sigma, n_s in 0..3, n_o feasible given the previous round's statuses), with members split into
    an in-phase group and an anti-phase group; random sample of 2500 patterns, 60 periods each;
(3) period-3 random patterns (1000), 40 periods.
Declared expectation: the periodic steady state of (1) lies between 0.011 and 0.02; FALSIFIES alpha_M = 0.02 under
the literal supremum if any reachable pattern exceeds 0.02. NEGATIVE CONTROL: I_t <= d_cl(t) everywhere.
"""
import time
import numpy as np
from mylib import Cfg
from memlib import Tracker, base_cfgs

t0 = time.time()
c = Cfg()
rng = np.random.default_rng(11)
viol = 0
def run_periodic(phases, nper, warm=400):
    global viol
    tr = Tracker(c)
    for _ in range(warm):
        tr.step(base_cfgs((0, 0, 0, 0)))
    Is = []
    sp = (0, 0, 0, 0)
    for k in range(nper):
        for sig, ns in phases:
            cfg = []
            for i in range(4):
                kopen = sum(sp[j] for j in range(4) if j != i)
                no = min(ns[i][1], kopen, ns[i][0])
                cfg.append((sig[i], ns[i][0], no))
            a, b = tr.step(cfg)
            if a > b + 1e-12:
                viol += 1
            Is.append(a)
            sp = sig
    return np.array(Is)
# (1) the beam's alternation: phase A = members 0-2 silent and closed, member 3 open attending all (n_o max);
#     phase B = members 0-2 open attending all (n_o max), member 3 silent and closed
ph = [((0, 0, 0, 1), [(0, 0), (0, 0), (0, 0), (3, 3)]), ((1, 1, 1, 0), [(3, 3), (3, 3), (3, 3), (0, 0)])]
Is = run_periodic(ph, 200)
print(f"(1) beam alternation, 200 periods: exact I max {Is.max():.4e}, last-period values {np.round(Is[-2:], 6)}  "
      f"({time.time()-t0:.0f}s)", flush=True)
# (2) random period-2 patterns with the full menu
best2 = (0.0, None)
for trial in range(2500):
    phases = []
    for _ in range(2):
        sig = tuple(int(x) for x in rng.integers(0, 2, 4))
        att = [(int(rng.integers(0, 4)), int(rng.integers(0, 4))) for _ in range(4)]
        phases.append((sig, att))
    Is = run_periodic(phases, 40, warm=150)
    m = Is[20:].max()
    if m > best2[0]:
        best2 = (m, phases)
    if time.time() - t0 > 80:
        break
print(f"(2) random period-2 patterns ({trial+1}): worst exact I {best2[0]:.4e} at {best2[1]}  ({time.time()-t0:.0f}s)",
      flush=True)
best3 = (0.0, None)
for trial in range(1000):
    phases = []
    for _ in range(3):
        sig = tuple(int(x) for x in rng.integers(0, 2, 4))
        att = [(int(rng.integers(0, 4)), int(rng.integers(0, 4))) for _ in range(4)]
        phases.append((sig, att))
    Is = run_periodic(phases, 25, warm=150)
    m = Is[20:].max()
    if m > best3[0]:
        best3 = (m, phases)
    if time.time() - t0 > 115:
        break
print(f"(3) random period-3 patterns ({trial+1}): worst exact I {best3[0]:.4e}  ({time.time()-t0:.0f}s)")
print(f"NEG violations {viol} (expected 0)")
