r"""Precision of S1 in c3b_sign.py: is the 1.3e-8 relative discrepancy round-off?
Declared expectation: error normalized by max|Pi^c| is <= 1e-10, and the worst cross-normalized
error occurs where |cross|/max|Pi^c| is small; doubling the window does not change the cross entries
by more than round-off.
"""
import os
os.environ.setdefault("OMP_NUM_THREADS", "1")
import numpy as np
exec(open("c3b_sign.py").read().split("# S1, S2, N1")[0])
worst_rel, worst_abs, ratio_at_worst, used = 0.0, 0.0, None, 0
while used < 150:
    p = draw()
    out = cross_and_V(p, 0.0)
    if out is None:
        continue
    cr, V, Pi = out
    if np.max(np.abs(cr)) < 1e-9 * np.max(np.abs(Pi)):
        continue
    used += 1
    n1, n2 = p["n"]
    err = np.max(np.abs(cr - np.linalg.inv(V)[0, 1] / np.sqrt(n1 * n2)))
    rel = err / np.max(np.abs(cr))
    if rel > worst_rel:
        worst_rel, ratio_at_worst = rel, np.max(np.abs(cr)) / np.max(np.abs(Pi))
    worst_abs = max(worst_abs, err / np.max(np.abs(Pi)))
print(f"S1 worst relative-to-cross error {worst_rel:.2e} at |cross|/max|Pi| = {ratio_at_worst:.2e}; worst error / max|Pi| = {worst_abs:.2e}")
