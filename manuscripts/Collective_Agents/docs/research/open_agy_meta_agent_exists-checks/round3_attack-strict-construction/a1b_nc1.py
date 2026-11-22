# A1b: rerun of negative control NC1 after fixing the control (block-diagonal fresh copies). Expected r within 0.01 of 1.
import time
from mylib import Cfg, sigma_c
t0 = time.time()
for proto in ("real", "frozen"):
    n1 = sigma_c(Cfg(proto=proto), npairs=20, T=400, burn=80, every=4, seed=41, fresh_relays=True)
    print(f"[{proto}] NC1 fresh relays (fixed control): r(A) = {n1['r']:.4f}, beta {n1['beta']:.3e} "
          f"(mixture part {n1['beta']-n1['beta_priv']:.2e})  ({time.time()-t0:.0f}s)", flush=True)
