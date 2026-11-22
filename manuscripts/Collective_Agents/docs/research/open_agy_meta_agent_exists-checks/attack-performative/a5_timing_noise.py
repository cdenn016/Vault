r"""Attack A5 (robustness of PN to two literal readings of the framework).

(i) Channel latency.  def:fw-system (02_framework.tex:15) writes y_ij(t+1) = u_j(t) + nu_ij(t+1): a relay of a
    raw observation s_j(t) can be read at round t+1 only.  PN fuses s_j(t) at round t (contemporaneous relay), the
    within-world-step convention of prop:agy-consensus(b) / ex:met-two-firms.  We recompute r(A) with one-round
    stale relays, members running the exact Kalman filter for that observation model with U as known input.
(ii) Internal noise.  def:agy-closure (05_agency.tex:16) requires Q^n > 0 for the internal variables; PN's beliefs
    are noiseless in the channel-level description.  Add private computation noise q_int to each prediction.

Declared expectations: (V) the batch known-input filter with delay 0 reproduces 24.4989 (validation; NEG: the same
builder at delay 1 must give a different value, so the validation can fail); (i) at delay 1 the block stays
diffusive (exchangeability) and r(A) stays above 5.075; (ii) r(A) decreases continuously in q_int, with a change
below 1e-3 at q_int = 1e-6.
"""
import os
os.environ.setdefault("OMP_NUM_THREADS", "1")
import numpy as np
from win import build, world_conditional, contrast_block, closed_form
from win2 import build_kf

F, Q, R, Rc, b, n = 0.9, 0.05, 1.0, 0.2, 0.2, 4
T, TS = 70, 40

if __name__ == "__main__":
    for delay in [0, 1]:
        for g in [0.05, 0.0]:
            mod = build_kf(F, Q, R, Rc, b, g, T, delay=delay)
            c = contrast_block(np.linalg.inv(world_conditional(mod, TS)))
            print("delay=%d g=%.2f: r(A)=%.6f diffusive=%s max_off=%.3e min_row=%.3f cs_dev=%.1e" % (
                delay, g, c["r"], c["diffusive"], c["max_off"], c["min_row"], c["cs_dev"]))
    print("closed form (delay 0): g=0.05 %.6f, g=0 %.6f" % (closed_form(n, F, Q, R, Rc, b, 0.05), closed_form(n, F, Q, R, Rc, b, 0.0)))
    for q in [1e-6, 1e-4, 1e-3]:
        mod = build(F, Q, R, Rc, b, 0.05, T, mode="base", q_int=q)
        c = contrast_block(np.linalg.inv(world_conditional(mod, TS)))
        print("internal noise q_int=%.0e: r(A)=%.6f diffusive=%s" % (q, c["r"], c["diffusive"]))
