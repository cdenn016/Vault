r"""Deciding script D8: sensitivity to two declarations, and the psi family (real protocol).
 (1) mechanism medium with one reviser among 8 per round (per-agent rate 1/8) instead of two (rate 1/4);
 (2) N_pr with the deciders ignorant of their drawn partners' current statuses ('pr0');
 (3) psi in {0.035, 0.045}: open rate, r(A), medium, mean-coupling baseline, N_hab, N_pr, strict full-policy agency
     (G1, G2) and its C12 bound.
Declared expectations (before running): (1) medium within 0.3 of 5.96, window unchanged in kind; (2) r(A) under
pr0 below 3.2; (3) as psi grows the open rate falls, r(A) rises toward the relay-only 8.63, the medium falls toward
4.75, and the strict full-policy index rises toward the C12 cap 4 ln2 / (16.64 + 4 ln2) = 0.143.
NEGATIVE CONTROL: psi = 0.024 (I*'s value) reproduces an empty mechanism window (medium > r(A)).
"""
import time
import numpy as np
from lib3 import sigma_c, simulate_policy
from agency3 import state_summary, index_from_summaries
from instance3 import PAR, MEDIUM, T, BURN, EVERY

t0 = time.time()
m1 = sigma_c(MEDIUM.with_(nrev=1), 30, T, BURN, EVERY, seed=8101)
print(f"(1) medium with one reviser among 8 per round: {m1['r']:.4f} +/- {m1['se_r']:.4f} (two revisers: 5.9589)  "
      f"({time.time()-t0:.0f}s)", flush=True)
p0 = sigma_c(PAR, 30, T, BURN, EVERY, seed=8102, mode="pr0")
print(f"(2) N_pr with ignorant deciders: r(A) {p0['r']:.4f}, open rate {p0['open_rate']:.3f}  ({time.time()-t0:.0f}s)",
      flush=True)
for psi in (0.035, 0.045, 0.024):
    par = PAR.with_(psi=psi)
    f = sigma_c(par, 24, T, BURN, EVERY, seed=8201)
    med = sigma_c(MEDIUM.with_(psi=psi), 8, T, BURN, EVERY, seed=8202)
    if psi == 0.024:
        print(f"NEG psi=0.024: r(A) {f['r']:.4f}, medium {med['r']:.4f}; mechanism window empty: {med['r'] >= f['r']}")
        break
    h = sigma_c(par, 12, T, BURN, EVERY, seed=8203, mode="hab")
    pr = sigma_c(par, 12, T, BURN, EVERY, seed=8204, mode="pr")
    decs = simulate_policy(par, 6200, np.random.default_rng(8205), "full", record_dec=True).log["dec"][200:]
    S = [state_summary(par, d[1], d[2], "real") for d in decs]
    g2 = index_from_summaries(par, S, cls="G2", full_policy=True)
    g1 = index_from_summaries(par, S, cls="G1", full_policy=True)
    print(f"(3) psi={psi}: open {f['open_rate']:.4f}; r(A) {f['r']:.4f}; medium {med['r']:.4f}; mean coupling "
          f"{1+6/7*(f['r']-1):.4f}; N_hab {h['r']:.4f}; N_pr {pr['r']:.4f}; strict full agency G2 {g2['index']:.4f}, "
          f"G1 {g1['index']:.4f}; C12 bound {g2['c12_bound']:.4f}  ({time.time()-t0:.0f}s)", flush=True)
print(f"total {time.time()-t0:.0f}s")
