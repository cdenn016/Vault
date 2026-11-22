r"""Exploration only (not deciding): agency index of I** at psi values, both protocols, strict and coarse states."""
import sys, time
import numpy as np
from lib3 import Par, simulate_policy
from agency3 import state_summary, index_from_summaries, mixture_summary, COUNTS

t0 = time.time()
for psi in [float(a) for a in sys.argv[1:]]:
    for proto in ("real", "frozen"):
        par = Par(psi=psi, proto=proto)
        rng = np.random.default_rng(41)
        path = simulate_policy(par, 6000, rng, "full", record_dec=True)
        decs = path.log["dec"][200:]
        S = [state_summary(par, d[1], d[2], proto) for d in decs]
        emp = np.bincount([int(d[3].sum()) for d in decs], minlength=5) / len(decs)
        avg = np.mean([s["cnt"] for s in S], 0)
        line = f"psi={psi} {proto}: open {np.mean([d[3].mean() for d in decs]):.3f}; count law emp {np.round(emp,3)} vs computed {np.round(avg,3)}"
        print(line, flush=True)
        for fp in (True, False):
            for cls in ("G1", "G2"):
                r = index_from_summaries(par, S, cls=cls, full_policy=fp)
                M = mixture_summary(S)
                rm = index_from_summaries(par, [M], cls=cls, full_policy=fp)
                print(f"   {'full' if fp else 'slot'} {cls}: strict {r['index']:.4f} (num {r['num']:.4f} den {r['den']:.4f} "
                      f"att {r['att']:.3f} slotKL {r['slot_den']:.4f} C12 {r['c12_bound']:.4f} fit {r['fit']}); "
                      f"coarse {rm['index']:.4f} (slotKL {rm['slot_den']:.4f})", flush=True)
        print(f"   ({time.time()-t0:.0f}s)", flush=True)
