r"""A5 (attack): exact Markov defect d_M of the declared scalar coarse variable along reachable policy patterns.
Declared expectations (before running):
  (i) reproduction: my d_cl at the candidate's worst pattern (base 1110 sustained, then
      ((0,0,0),(0,0,0),(0,0,0),(1,3,3))) equals 2.6644e-02 (candidate d5b) to 1e-6;
  (ii) the exact I_t at that switch round is below d_cl (d_M <= d_cl); I do not know whether it exceeds 0.02;
  (iii) stationary symmetric bases give exact d_M of order 1e-4 (candidate: 7.1e-5 to 1.3e-4).
NEGATIVE CONTROL: with qc = 0 and all members in one identical configuration (base 0000) the coarse variable is an
exact linear function of a 2-dim average state ... (not used); instead: an R^2 coarse variable is not tested here.
Negative control used: the exact I_t must never exceed d_cl(t) (data processing); any violation means a bug.
"""
import itertools, time
import numpy as np
from mylib import Cfg
from memlib import Tracker, base_cfgs

t0 = time.time()
c = Cfg()
bases = {"0000": (0, 0, 0, 0), "1000": (1, 0, 0, 0), "1100": (1, 1, 0, 0), "1110": (1, 1, 1, 0), "1111": (1, 1, 1, 1)}
viol = 0
# (i)-(ii) the candidate's worst pattern
tr = Tracker(c)
for _ in range(400):
    tr.step(base_cfgs(bases["1110"]))
I0 = [tr.step(base_cfgs(bases["1110"]))[0] for _ in range(3)]
Isw, dsw = tr.step([(0, 0, 0), (0, 0, 0), (0, 0, 0), (1, 3, 3)])
after = []
sig_sw = (0, 0, 0, 1)
cf1 = [(1, 3, int(sum(sig_sw[j] for j in range(4) if j != i))) if bases["1110"][i] else
       (0, 3, int(sum(sig_sw[j] for j in range(4) if j != i))) for i in range(4)]
after.append(tr.step(cf1))
for _ in range(20):
    after.append(tr.step(base_cfgs(bases["1110"])))
print(f"(i) candidate worst pattern: d_cl {dsw:.6e} (candidate 2.6644e-02); exact I_t at switch {Isw:.4e}; "
      f"stationary I before {np.max(I0):.3e}; max exact I_t over the 21 rounds after {max(a[0] for a in after):.4e}")
# (iii) + exhaustive single-round switches from each base (frozen-reachable superset), exact I over switch + 21 rounds
for name, sb in bases.items():
    tr = Tracker(c)
    for _ in range(400):
        tr.step(base_cfgs(sb))
    Ist = max(tr.copy().step(base_cfgs(sb))[0] for _ in range(1))
    per = []
    for i in range(4):
        kopen = sum(sb[j] for j in range(4) if j != i)
        per.append([(o, ns, no) for o in (0, 1) for ns in range(4) for no in range(min(ns, kopen) + 1)])
    # exploit exchangeability of members with equal base status: canonical multisets per status class
    cls = {}
    for i in range(4):
        cls.setdefault(sb[i], []).append(i)
    groups = list(cls.values())
    def combos():
        lists = [list(itertools.combinations_with_replacement(per[g[0]], len(g))) for g in groups]
        for pick in itertools.product(*lists):
            cfg = [None] * 4
            for g, chosen in zip(groups, pick):
                for i, cc in zip(g, chosen):
                    cfg[i] = cc
            yield cfg
    best = (0.0, None, None); bestd = (0.0, None); ncomb = 0
    for cfg in combos():
        ncomb += 1
        t2 = tr.copy()
        I1, d1 = t2.step(cfg)
        sig_sw = tuple(cc[0] for cc in cfg)
        nxt = [(sb[i], 3, int(sum(sig_sw[j] for j in range(4) if j != i))) for i in range(4)]
        I2, d2 = t2.step(nxt)
        Is = [I1, I2]; ds = [d1, d2]
        for _ in range(8):
            a, b = t2.step(base_cfgs(sb)); Is.append(a); ds.append(b)
        viol += sum(1 for a, b in zip(Is, ds) if a > b + 1e-12)
        m = max(Is)
        if m > best[0]:
            nflip = sum(1 for i in range(4) if sig_sw[i] != sb[i])
            best = (m, cfg, nflip)
        if max(ds) > bestd[0]:
            bestd = (max(ds), cfg)
    print(f"(iii) base {name}: stationary exact I {Ist:.3e}; {ncomb} switch patterns; worst exact sup_t I_t {best[0]:.4e} "
          f"at {best[1]} (sigma flips vs base: {best[2]}); worst d_cl {bestd[0]:.4e}  ({time.time()-t0:.0f}s)", flush=True)
print(f"NEG data-processing violations (I_t > d_cl): {viol} (expected 0)")
