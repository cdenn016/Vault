r"""Check 7: full-policy agency (reading R-pol) against the differ clause for N_hab, as the attention habits vary.

Attention habits: mass 1 - eps on the set of all three mates, eps spread uniformly over the other 63 message sets
(eps = 63/64 is the declared uniform habit).  For each eps: the full model's r(A), N_hab's r(A) (gamma = 0: slots at
1/2, attention from the habits), and the agency index at the coarse decision state in the declared class G2 with the
members' joint policy including attention (habits fixed, so the attention part of the KL cannot be fitted).
Declared expectations (before running): r(A) of the full model about 4.42 at every eps; N_hab's r(A) falls from
about 3.99 (eps -> 0) to 1.73 (eps = 63/64); the full-policy G2 index rises from 0.008 (uniform) to the slot-only
value 0.974 (eps -> 0).  Prediction: no eps gives both N_hab below the lower edge (about 2.95-2.97) and index >= 0.9;
at eps = 0.0028 the index is about 0.90 and N_hab about 3.98.
NEGATIVE CONTROL: at eps = 63/64 the script must reproduce check 2 and check 4 (index 0.008, N_hab 1.73).
"""
import time
import numpy as np
from math import comb
from scipy.optimize import minimize_scalar
from core import Par, run, compound, r_ab

t0 = time.time()
PAR = Par()
habc = np.array([comb(4, k) for k in range(5)]) / 16.0
w0 = PAR.w                       # [15, 33, 15, 1]


def kl(c, q):
    m = c > 0
    return float(np.sum(c[m] * np.log(c[m] / q[m])))


def group(vC, gC):
    k = np.arange(5)
    G = -0.5 * np.log1p(k * vC / PAR.Rs) + PAR.psi * k
    lw = np.log([comb(4, j) for j in range(5)]) - gC * G
    lw -= lw.max(); q = np.exp(lw)
    return q / q.sum()


def vstar(pv):
    F, Q, qc = PAR.F, PAR.Q, PAR.qc
    Pm = np.array([[F * F * pv + Q + qc, F * pv], [F * pv, pv + qc]])
    return np.linalg.inv(np.linalg.inv(Pm) + np.diag([1 / PAR.R, 3 / (PAR.R + PAR.Rc)]))[0, 0]


def rA(out):
    al, be = compound(out.S)
    return r_ab(4, al, be)


for eps in (63 / 64, 0.3, 0.05, 0.01, 0.0028, 0.0005):
    h = np.array([eps * w0[0] / 63, eps * w0[1] / 63, eps * w0[2] / 63, 1 - eps])
    of = run(PAR, K=1500, T=400, burn=80, seed=7101, mode="full", want_agency=True, hab_m=h)
    oh = run(PAR, K=1500, T=400, burn=80, seed=7102, mode="hab", hab_m=h)
    A = of.agency
    sym = A["sym"].astype(bool)
    c = np.bincount(A["newcount"][sym], minlength=5) / sym.sum()
    v = vstar(float(np.median(A["p"][sym])))
    den = kl(c, habc)
    num = min(minimize_scalar(lambda g: kl(c, group(v, g)), bounds=(0, 5000), method="bounded").fun, den)
    att = A["klatt"].mean()
    print(f"eps={eps:.4g}: full r(A) {rA(of):.3f}; N_hab r(A) {rA(oh):.3f}; attention KL to habits {att:.4f}; "
          f"G2 index slot-only {1 - num/den:.4f}, full policy {1 - (num + att)/(den + att):.4f}  ({time.time()-t0:.0f}s)",
          flush=True)
print(f"total {time.time()-t0:.1f}s")
