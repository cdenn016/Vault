r"""Deciding script D6b: sampling error of the strict agency indices (5 independent stationary paths of 4000 rounds
per protocol, index per path, mean and standard error), and the strict full-policy G2 index at the two corners of
the 1% box (real protocol).  Declared expectations: per-path spread below 0.003 for the full-policy indices; corner
values within 0.01 of the centre.  NEGATIVE CONTROL: the index computed with the decision states of the FROZEN
protocol but the laws of the REAL protocol (mismatched protocol) differs from both correct values by more than 0.002
(the index is sensitive to the protocol).
"""
import time
import numpy as np
from lib3 import simulate_policy
from agency3 import state_summary, index_from_summaries
from instance3 import PAR

t0 = time.time()
for proto in ("real", "frozen"):
    par = PAR.with_(proto=proto)
    vals = {k: [] for k in ("fullG1", "fullG2", "slotG1", "slotG2")}
    for seed in range(6201, 6206):
        decs = simulate_policy(par, 4200, np.random.default_rng(seed), "full", record_dec=True).log["dec"][200:]
        S = [state_summary(par, d[1], d[2], proto) for d in decs]
        for fp in (True, False):
            for cls in ("G1", "G2"):
                vals[("full" if fp else "slot") + cls].append(index_from_summaries(par, S, cls=cls, full_policy=fp)["index"])
    for k, v in vals.items():
        v = np.array(v)
        print(f"[{proto}] strict {k}: mean {v.mean():.5f} SE {v.std(ddof=1)/np.sqrt(len(v)):.5f} (paths {np.round(v,5)})",
              flush=True)
    print(f"   ({time.time()-t0:.0f}s)", flush=True)
grad = np.load("d7a_grad.npy", allow_pickle=True).item()
for lab, sg in (("lower", -1), ("upper", +1)):
    kw = {nm: getattr(PAR, nm) * (1 + sg * 0.01 * np.sign(g)) for nm, g in grad.items()}
    par = PAR.with_(proto="real", **kw)
    decs = simulate_policy(par, 6200, np.random.default_rng(6301), "full", record_dec=True).log["dec"][200:]
    S = [state_summary(par, d[1], d[2], "real") for d in decs]
    r2 = index_from_summaries(par, S, cls="G2", full_policy=True)["index"]
    r1 = index_from_summaries(par, S, cls="G1", full_policy=True)["index"]
    print(f"{lab} corner (real): strict full G2 {r2:.5f}, G1 {r1:.5f}")
par = PAR.with_(proto="frozen")
decs = simulate_policy(par, 4200, np.random.default_rng(6401), "full", record_dec=True).log["dec"][200:]
S = [state_summary(PAR.with_(proto="real"), d[1], d[2], "real") for d in decs]
print(f"NEG mismatched protocol (frozen states, real laws): strict full G2 "
      f"{index_from_summaries(PAR, S, cls='G2', full_policy=True)['index']:.5f}")
print(f"total {time.time()-t0:.0f}s")
