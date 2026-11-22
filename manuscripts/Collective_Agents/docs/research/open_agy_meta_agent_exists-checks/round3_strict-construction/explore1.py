r"""Exploration only (not deciding): I** at I*'s parameters and nearby (Rs, psi), both protocols.
Reports open rate, r(A), mechanism medium (8 agents, 2 revisers per round under 'real'), N_hab, N_pr."""
import sys, time
import numpy as np
from lib3 import Par, sigma_c

t0 = time.time()
cfgs = [dict(Rs=2.0, psi=0.024)]
if len(sys.argv) > 1:
    cfgs = [dict(Rs=float(a.split(",")[0]), psi=float(a.split(",")[1])) for a in sys.argv[1:]]
for cfg in cfgs:
    for proto in ("real", "frozen"):
        par = Par(proto=proto, **cfg)
        med = par.with_(n=8, n_zero=0, nrev=2)
        f = sigma_c(par, 24, 360, 80, 4, seed=11)
        m = sigma_c(med, 8, 360, 80, 4, seed=12)
        h = sigma_c(par, 12, 360, 80, 4, seed=13, mode="hab")
        pr = sigma_c(par, 12, 360, 80, 4, seed=14, mode="pr")
        print(f"{cfg} {proto}: open {f['open_rate']:.3f} r(A) {f['r']:.3f}+-{f['se_r']:.3f} "
              f"(alpha {f['alpha']:.5f} beta {f['beta']:.5f}, mixture beta {f['beta']-f['beta_priv']:.2e}); "
              f"medium {m['r']:.3f} (open {m['open_rate']:.3f}); meancoup {1+6/7*(f['r']-1):.3f}; "
              f"N_hab {h['r']:.3f}; N_pr {pr['r']:.3f}; dev {f['dev_rate']:.1e}  ({time.time()-t0:.0f}s)", flush=True)
