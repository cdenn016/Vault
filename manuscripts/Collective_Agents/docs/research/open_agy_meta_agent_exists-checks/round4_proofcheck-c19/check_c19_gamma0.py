r"""Agency index near gamma = 0 at the symmetric decision state p_X = 0.09 (slot component), class
G_C(n) = -1/2 ln(1 + n v_C/R_s) + psi n with habits fixed at uniform E.
KL(P || P_{gamma_C}) is convex in gamma_C with derivative E_P[G_C] - E_{P_{gamma_C}}[G_C]; if the derivative
at gamma_C = 0 is >= 0, the infimum over gamma_C >= 0 is attained at 0, the numerator equals the
denominator, and Agency = 0 exactly, while Agency(gamma = 0) = 1 by the convention of def:agy-agency-index."""
from __future__ import annotations

import os
import sys

os.environ["OMP_NUM_THREADS"] = "1"
from math import comb

import numpy as np

LIB = r"C:\Users\chris and christine\Desktop\Research\manuscripts\Collective_Agents\docs\research\open_agy_meta_agent_exists-checks\round2_epistemic_persistent"
sys.path.insert(0, LIB)
import lib  # noqa: E402

par = lib.Par().with_(Rc=0.1)
w = lib.attention_weights(par, 3, par.n_zero); mmax = len(w) - 1
binom = np.array([comb(4, k) for k in range(5)], float)
E_n = binom / 16
n = np.arange(5)
for vC in (par.Rs, 0.5, 0.097991):
    GC = -0.5 * np.log(1 + n * vC / par.Rs) + par.psi * n
    row = []
    for g in (1e-3, 1e-2, 1e-1, 1.0, 10.0, 400.0):
        Gt = lib.softmin_att(par.with_(gamma=g), lib.efe_table(par, lib.Pminus(par, 0.09), mmax, 4), w)
        P = lib.gibbs_law_sym(g, Gt, 4)
        deriv0 = float(P @ GC - E_n @ GC)
        den = float(np.sum(P * np.log(P / E_n)))
        row.append(f"g={g:g}: dKL/dgC(0)={deriv0:+.3e} den={den:.3e} -> {'Agency=0 exactly' if deriv0 >= 0 else 'interior min'}")
    print(f"vC={vC}:\n  " + "\n  ".join(row))
