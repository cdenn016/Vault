r"""Attack run a3b: sustained deviations that pair a slot-opening member with a mate that reads no relay (the
pairing that maximizes the single-round d_cl), for D1 and the frontier lever (m = 18, 50; Rs = 10 and scaled).
Declared expectation: d_cl may exceed 0.02 for m >= 18 at Rs = 10; exact MI stays near 1e-4 (far below 0.02).
NEGATIVE CONTROL: L = 0 (stationary path) must return d_cl 8.906e-4 and MI ~ 4.4e-5 or less."""
import time
import numpy as np
from mylib import Par
import a3_closure as A3   # re-uses run_path (module-level prints repeat a3; harmless)

t0 = time.time()
stat = ((1, 0), (1, 0))
for m, Rs in ((8, 10.0), (18, 10.0), (50, 10.0), (18, 22.5), (50, 62.5)):
    pm = Par().w(m=m, Rs=Rs)
    out = []
    for L in (0, 1, 3, 10, 40):
        path = [((1, m), (0, 0))] * L + [stat] * 40
        mx, mi, _, _ = A3.run_path(pm, path)
        out.append(f"L={L}: d_cl {mx:.4f} MI {mi:.2e}")
    print(f"PAIR (1,m)+(0,0) m={m} Rs={Rs}: " + "; ".join(out))
print(f"({time.time()-t0:.1f}s)")
