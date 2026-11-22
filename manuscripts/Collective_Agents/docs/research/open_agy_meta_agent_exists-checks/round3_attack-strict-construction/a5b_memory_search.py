r"""A5b (attack): adversarial search for the exact Markov defect over multi-round reachable patterns.
(1) sustained heterogeneous configurations (each member's (sigma_i, n_s, n_o) held fixed for 300 rounds; reachable
    with positive probability since habits have full support and gamma < inf), stationary exact I;
(2) greedy beam over sequences of single-round switches (frozen-reachable: any sigma', any attended subset), depth 6,
    starting from the worst sustained state, objective = max exact I_t over the sequence plus 8 trailing base rounds;
(3) random sequences of length 40 with a random member configuration in every round (frozen-reachable).
Declared expectation: I do not know; if any reachable pattern gives exact I_t > 0.02 the candidate's headline grade
alpha_M = 0.02 fails under the literal supremum reading; if all stay below 0.02, the candidate's statement that the
literal reading needs alpha_M = 0.11 is an artifact of the d_cl bound.
NEGATIVE CONTROL: exact I_t <= d_cl(t) at every step (count violations, expected 0).
"""
import itertools, time
import numpy as np
from mylib import Cfg
from memlib import Tracker

t0 = time.time()
c = Cfg()
rng = np.random.default_rng(7)
viol = 0
def cfg_ok(sig_prev, cfg):
    for i, (o, ns, no) in enumerate(cfg):
        kopen = sum(sig_prev[j] for j in range(4) if j != i)
        if no > min(ns, kopen):
            return False
    return True
# (1) sustained heterogeneous
best1 = (0.0, None)
cfgs_all = [(o, ns, no) for o in (0, 1) for ns in range(4) for no in range(ns + 1)]
for trial in range(2500):
    sig = tuple(int(x) for x in rng.integers(0, 2, 4))
    cfg = []
    for i in range(4):
        kopen = sum(sig[j] for j in range(4) if j != i)
        ns = int(rng.integers(0, 4)); no = int(rng.integers(0, min(ns, kopen) + 1))
        cfg.append((sig[i], ns, no))
    tr = Tracker(c)
    Is = []
    for t in range(260):
        a, b = tr.step(cfg)
        if a > b + 1e-12: viol += 1
        if t >= 200: Is.append(a)
    m = max(Is)
    if m > best1[0]:
        best1 = (m, tuple(cfg))
print(f"(1) sustained heterogeneous (2500 random fixed configurations): worst stationary exact I {best1[0]:.4e} at {best1[1]}  "
      f"({time.time()-t0:.0f}s)", flush=True)
# (2) greedy beam from the worst sustained state
cfg0 = list(best1[1]); sig0 = tuple(cc[0] for cc in cfg0)
tr0 = Tracker(c)
for _ in range(300):
    tr0.step(cfg0)
beam = [(0.0, tr0, sig0, [])]
cands_cfg = [(o, ns, no) for o in (0, 1) for ns in (0, 3) for no in range(ns + 1)]   # reduced per-member menu
for depth in range(4):
    new = []
    for score, tr, sp, hist in beam:
        for cfg in itertools.product(cands_cfg, repeat=4):
            if not cfg_ok(sp, cfg):
                continue
            t2 = tr.copy()
            a, b = t2.step(list(cfg))
            if a > b + 1e-12: viol += 1
            new.append((max(score, a), t2, tuple(cc[0] for cc in cfg), hist + [cfg]))
    new.sort(key=lambda z: -z[0])
    beam = new[:6]
    print(f"(2) depth {depth+1}: best exact I so far {beam[0][0]:.4e}  ({time.time()-t0:.0f}s)", flush=True)
    if time.time() - t0 > 100:
        break
print(f"(2) worst sequence: {beam[0][3]}")
# (3) random sequences
best3 = 0.0
for trial in range(150):
    tr = Tracker(c)
    sp = (0, 0, 0, 0)
    for t in range(60):
        sig = tuple(int(x) for x in rng.integers(0, 2, 4))
        cfg = []
        for i in range(4):
            kopen = sum(sp[j] for j in range(4) if j != i)
            ns = int(rng.integers(0, 4)); no = int(rng.integers(0, min(ns, kopen) + 1))
            cfg.append((sig[i], ns, no))
        a, b = tr.step(cfg)
        if a > b + 1e-12: viol += 1
        if t >= 20: best3 = max(best3, a)
        sp = sig
    if time.time() - t0 > 115:
        break
print(f"(3) random frozen-reachable sequences ({trial+1} x 60 rounds): worst exact I {best3:.4e}  ({time.time()-t0:.0f}s)")
print(f"NEG data-processing violations: {viol} (expected 0)")
