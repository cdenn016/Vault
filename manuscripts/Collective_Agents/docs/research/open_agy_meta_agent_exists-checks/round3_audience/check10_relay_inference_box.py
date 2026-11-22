r"""Check 10: inference clause of the relay variant P1 on the +-5% box of checks 6 and 9 (sampled simulation of
check 8, 2000 systems x 220 rounds per point).  Declared expectation before running: best-constant KL <= 0.03 at
every point (P0's box maximum was 0.0291).  NEGATIVE CONTROL: as in check 8 (union model without the source)."""
import itertools, time
import numpy as np
import importlib.util
spec = importlib.util.spec_from_file_location("c8", "check8_inference_mc.py")
src = open("check8_inference_mc.py").read().split("for par, lab in")[0]
ns = {}
exec(compile(src, "check8_inference_mc.py", "exec"), ns)
run = ns["run"]
from aud import Par
t0 = time.time()
base = Par(kmsg=2)
center = np.array([base.F, base.Q, base.R, base.RS, base.Rc, base.qc, base.gamma])
pts = [np.zeros(7)]
for a, b, c, d in itertools.product((-1, 1), repeat=4):
    pts.append(np.array([a, b, c, d, a * b * c, b * c * d, a * c * d], float))
worst = 0.0
for k, pt in enumerate(pts):
    x = center * (1 + 0.05 * pt)
    par = Par(F=x[0], Q=x[1], R=x[2], RS=x[3], Rc=x[4], qc=x[5], gamma=x[6], kmsg=2)
    D, PU, Pc = run(par, K=2000, T=220, burn=70, seed=1100 + k)
    kl = D / (2 * PU); worst = max(worst, kl)
    print(f"pt {k:2d}: best-constant KL {kl:.5f}; claimed-variance KL {0.5*(Pc/PU + D/PU - 1 - np.log(Pc/PU)):.5f}", flush=True)
print(f"max over the box {worst:.5f}  ({time.time()-t0:.0f}s)")
