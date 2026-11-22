"""Item 5 addendum: spread over blanket paths of the deterministic-start memory defect, including the
transient (the s2 run reported the spread only at late rounds). Expectation: the t=2 peak varies
across paths by a few percent of its mean, more than the late-round spread (std 3e-5)."""
import os
import sys
import json

for _k in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS"):
    os.environ[_k] = "4"
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import numpy as np  # noqa: E402
import p1lib as L  # noqa: E402

B = 6000
r = L.simulate(L.Model(L.BASE), B=B, T_burn=10, T_avg=30, seed=31337, G=20, do_memory=True)
I2 = r["I2"]
q = [0.0, 0.05, 0.5, 0.95, 1.0]
print("path-average by t:", np.round(I2.mean(0)[:8], 6))
for t in (2, 3, 39):
    print("t=%2d: mean %.6f  std over paths %.3g  quantiles %s" % (t, I2[:, t].mean(), I2[:, t].std(),
                                                                   np.round(np.quantile(I2[:, t], q), 6)))
ps = I2.max(1)
print("per-path sup over t=0..39: mean %.6f std %.3g quantiles %s; argmax t distribution %s" % (
    ps.mean(), ps.std(), np.round(np.quantile(ps, q), 6), np.bincount(I2.argmax(1))[:6]))
json.dump(dict(t2=dict(mean=float(I2[:, 2].mean()), std=float(I2[:, 2].std()),
                       q=np.quantile(I2[:, 2], q).tolist()),
               per_path_sup=dict(mean=float(ps.mean()), std=float(ps.std()), q=np.quantile(ps, q).tolist())),
          open(os.path.join(HERE, "s8_memory_spread_output.json"), "w"), indent=1)
