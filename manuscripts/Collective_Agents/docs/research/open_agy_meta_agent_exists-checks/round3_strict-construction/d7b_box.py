r"""Deciding script D7b: the explicit neighborhood B_delta = prod_j [theta*_j (1-delta), theta*_j (1+delta)],
delta = 1%, over (F, Q, R, Rc, Rs, psi, gamma, qc), real protocol.  One r0 = 7.9 works on B_delta under the
mean-coupling baseline iff r(A) in [7.9, 9.05) there (baseline 1 + (6/7)(r(A)-1) < 7.9 <=> r(A) < 9.05), and under the
mechanism baseline iff r(A) >= 7.9 and the medium < 7.9.
Points: the two first-order extreme corners (r decreasing / increasing along -/+ sign(gradient)), 60 pairs each,
the medium (20 pairs) and N_hab, N_pr (20 pairs) at both corners; then (d7c) a 16-point fractional factorial.
Declared expectations (before running): r at the lower corner about 8.43 - 0.24 = 8.19 (>= 7.9), at the upper corner
about 8.67 (< 9.05); medium below 6.5 at both; N_hab, N_pr below 3.2 at both.
NEGATIVE CONTROL: at delta = 3% the lower corner must come within 0.1 of r0 or below it (shows the box size is
binding, i.e. the check can fail).
"""
import time
import numpy as np
from lib3 import sigma_c
from instance3 import PAR, MEDIUM, T, BURN, EVERY, R0

t0 = time.time()
grad = np.load("d7a_grad.npy", allow_pickle=True).item()


def corner(sign, delta):
    kw = {nm: getattr(PAR, nm) * (1 + sign * delta * np.sign(g)) for nm, g in grad.items()}
    return kw


for lab, sg in (("lower", -1), ("upper", +1)):
    kw = corner(sg, 0.01)
    par = PAR.with_(**kw)
    f = sigma_c(par, 60, T, BURN, EVERY, seed=7101)
    med = sigma_c(MEDIUM.with_(**kw), 20, T, BURN, EVERY, seed=7102)
    h = sigma_c(par, 20, T, BURN, EVERY, seed=7103, mode="hab")
    pr = sigma_c(par, 20, T, BURN, EVERY, seed=7104, mode="pr")
    mc = 1 + 6 / 7 * (f["r"] - 1)
    print(f"{lab} corner (delta 1%): r(A) {f['r']:.4f} +/- {f['se_r']:.4f}; mean-coupling baseline {mc:.4f}; "
          f"medium {med['r']:.4f}; N_hab {h['r']:.4f}; N_pr {pr['r']:.4f}; r0={R0} works (mean coupling): "
          f"{mc < R0 <= f['r']}; (mechanism): {med['r'] < R0 <= f['r']}; nulls below both lower edges: "
          f"{max(h['r'], pr['r']) < min(med['r'], mc)}  ({time.time()-t0:.0f}s)", flush=True)
kw = corner(-1, 0.03)
f3 = sigma_c(PAR.with_(**kw), 20, T, BURN, EVERY, seed=7105)
print(f"NEG lower corner at delta 3%: r(A) {f3['r']:.4f} (expected within 0.1 of r0={R0} or below)")
print(f"total {time.time()-t0:.0f}s")
