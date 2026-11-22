r"""Deciding script D6: agency index of niche A of I** under each reading combination (def:agy-agency-index,
05_agency.tex:240-246), one protocol per run (PROTO env).

Decision states (declared): strict = the exact covariance states X = (p_0..p_3 after the round-t update, sigma(t)),
sampled from 3 independent stationary policy paths of 6000 rounds (burn 200), equal weights (empirical stationary
law); coarse alternatives: one state (the stationary mixture) and five states (binned by the current open count).
Readings: full policy (attention and private-sensor status) or slot only; classes G1 (v_C free constant) and G2
(v_C declared, the members' anticipated variance); habits held fixed at the uniform product; gamma_C in [0, inf).
Declared expectations (before running), from the exploration:
  strict full-policy index: 0.06-0.075 (real), 0.07-0.08 (frozen); slot-only strict: 0.55-0.7 (real), > 0.99 (frozen);
  coarse full-policy about 0.074; every full-policy index below its C12 bound (slot KL / total KL);
  attention KL to the uniform habit about 16.6 nats (4 x ln 64 = 16.636 minus the entropy of rare deficits);
  sigma(t) is a function of the p-vector on the sampled states (no two states with equal p-vectors differ in sigma).
NEGATIVE CONTROLS: (a) habit-only model alone (gamma_C = 0): index exactly 0; (b) a class that may also tilt the
attention habits to the actual attention law exceeds the C12 bound (index > bound); (c) the empirical count law of
the sampled sigma(t+1) matches the computed law (chi-square p > 0.001).
"""
import time
import numpy as np
from scipy.stats import chi2
from lib3 import simulate_policy
from agency3 import state_summary, index_from_summaries, mixture_summary
from instance3 import PAR, PROTO

t0 = time.time()
decs = []
for seed in (6101, 6102, 6103):
    path = simulate_policy(PAR, 6200, np.random.default_rng(seed), "full", record_dec=True)
    decs += path.log["dec"][200:]
S = [state_summary(PAR, d[1], d[2], PROTO) for d in decs]
print(f"[{PROTO}] decision states: {len(S)} (3 paths x 6000 rounds)  ({time.time()-t0:.0f}s)", flush=True)
# sigma(t) determined by the p-vector?
keys = {}
clash = 0
for d in decs:
    k = tuple(np.round(d[1], 12))
    s = tuple(d[2])
    if k in keys and keys[k] != s:
        clash += 1
    keys[k] = s
print(f"distinct p-vectors {len(keys)}; p-vectors shared by states with different sigma(t): {clash} (expected 0)")
# NEG (c): empirical vs computed count law of sigma(t+1)
emp = np.bincount([int(d[3].sum()) for d in decs], minlength=5).astype(float)
exp_ = np.sum([s["cnt"] for s in S], 0)
m = exp_ > 5
stat = float(np.sum((emp[m] - exp_[m]) ** 2 / exp_[m])); dfree = int(m.sum()) - 1
print(f"NEG(c) count law emp {np.round(emp/emp.sum(),4)} vs computed {np.round(exp_/exp_.sum(),4)}; chi2 {stat:.2f} on "
      f"{dfree} df, p = {chi2.sf(stat, dfree):.3f} (correlated samples; must exceed 0.001)")
att = np.array([s["att"] for s in S])
print(f"attention KL to the uniform habit: mean {att.mean():.4f} nats (4 ln 64 = {4*np.log(64):.4f}); "
      f"open rate {np.mean([d[3].mean() for d in decs]):.4f}")
results = {}
for fp in (True, False):
    for cls in ("G1", "G2"):
        r = index_from_summaries(PAR, S, cls=cls, full_policy=fp)
        results[("strict", fp, cls)] = r
        Mx = mixture_summary(S)
        rc = index_from_summaries(PAR, [Mx], cls=cls, full_policy=fp)
        results[("coarse1", fp, cls)] = rc
        bins = []
        cur = np.array([int(d[2].sum()) for d in decs])
        wts = []
        for k in range(5):
            idx = np.nonzero(cur == k)[0]
            if len(idx) == 0:
                continue
            bins.append(mixture_summary([S[i] for i in idx])); wts.append(len(idx))
        rb = index_from_summaries(PAR, bins, w=wts, cls=cls, full_policy=fp)
        results[("count5", fp, cls)] = rb
        print(f"  {'full' if fp else 'slot'} {cls}: strict {r['index']:.5f} (num {r['num']:.4f}, den {r['den']:.4f}, "
              f"slot KL {r['slot_den']:.4f}, attention {r['att']:.4f}, C12 bound {r['c12_bound']:.5f}, fit {r['fit']}); "
              f"five count states {rb['index']:.5f}; one coarse state {rc['index']:.5f}", flush=True)
# NEG (a): habit-only model alone
r = results[("strict", True, "G2")]
print(f"NEG(a) habit-only model alone: index = 1 - den/den = {1 - r['den']/r['den']:.1f} (expected 0)")
# NEG (b): attention habits may be tilted to the actual attention law (outside the declared class)
r = results[("strict", True, "G2")]
idx_free = 1 - (r["slot_num"] + 0.0) / r["den"]
print(f"NEG(b) class with free attention habits: index {idx_free:.4f} > C12 bound {r['c12_bound']:.4f}: "
      f"{idx_free > r['c12_bound']} (expected True)")
np.save(f"d6_{PROTO}.npy", {str(k): v["index"] for k, v in results.items()}, allow_pickle=True)
print(f"total {time.time()-t0:.0f}s")
