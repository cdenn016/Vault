# smoke test: timing and ballpark (not deciding)
import time, numpy as np
from mylib import Cfg, sigma_c
t0 = time.time()
c = Cfg(proto="real")
o = sigma_c(c, npairs=8, T=400, burn=80, every=4, seed=1)
print("real 8 pairs:", {k: (round(v, 6) if isinstance(v, float) else v) for k, v in o.items() if k != "S"}, f"{time.time()-t0:.1f}s")
