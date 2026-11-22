r"""V3: calibration of the batch standard error of r(A) against independent replicates (deterministic-policy designs,
where the exact value is known).

Declared expectation: if the batch SE is calibrated, the empirical SD of 12 independent replicates (K = 400 each) is
within a factor 1.5 of the mean reported SE, and the replicate mean is within 3 empirical SE of the exact value.
If the ratio exceeds 1.5, every MC margin in the report is restated with SEs inflated by that ratio.
NEGATIVE CONTROL: with nbatch = 2 the reported SE must be visibly noisier across replicates (coefficient of variation
of the SE estimates larger than with nbatch = 20).
"""
import time
import numpy as np
from flib import Par, exact_sigma_c, compound, r_ab, mc, r_and_se
from design import D1
from d1_agency import design as mkdesign

t0 = time.time()
for lab, par, n in (("D1 (n=2)", D1, 2), ("D3 (n=4)", mkdesign(4, ((0, 1), (3, 1)), 8), 4)):
    att = ~np.eye(n, dtype=bool)
    rex = r_ab(n, *compound(exact_sigma_c(par, att, np.zeros(n, dtype=int))[0]))
    rs, ses, ses2 = [], [], []
    for rep in range(12):
        o = mc(par, "full", K=400, T=400, burn=80, seed=50000 + 100 * n + rep, nbatch=20)
        r, s, _, _ = r_and_se(o, n)
        rs.append(r); ses.append(s)
        rb = np.array([r_ab(n, *compound(S)) for S in [o.S_batches[0::2].mean(0), o.S_batches[1::2].mean(0)]])
        ses2.append(rb.std(ddof=1) / np.sqrt(2))
    rs, ses, ses2 = np.array(rs), np.array(ses), np.array(ses2)
    sd = rs.std(ddof=1)
    print(f"{lab}: exact {rex:.4f}; replicate mean {rs.mean():.4f} (z {(rs.mean()-rex)/(sd/np.sqrt(12)):+.2f}); "
          f"empirical SD {sd:.4f}; mean batch SE {ses.mean():.4f}; ratio {sd/ses.mean():.2f}; "
          f"CV of SE (nbatch 20) {ses.std()/ses.mean():.2f}, (nbatch 2) {ses2.std()/ses2.mean():.2f}  ({time.time()-t0:.0f}s)")
