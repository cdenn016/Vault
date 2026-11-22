r"""Check 5: agency index under T-real with my own code, for several declarations of decision states.

Decision states (def:agy-agency-index, 05_agency.tex:240-246):
  coarse: every symmetric decision round (constructor's declaration);
  p-bins: the members' common posterior variance p at the decision, in quantile bins (10%, 50%, 90%, width 10%);
  p-bin + current open count.
Classes: G2 = belief variance v*(p) of eta_{t+1} after own sensor and 3 relays, slot likelihood N(eta, Rs), psi,
uniform product habits fixed, gamma_C in [0, inf) (one gamma_C for all states); G1 = v_C free as well.
Full-policy reading: the members' joint policy includes attention; G2's habits are fixed and uniform over the 64
message sets, so the attention part of KL is added to numerator and denominator.  The attention habit mass
epsilon off the mates set that would still allow Agency0 = 0.9 is computed.
Declared expectations (before running): coarse G2 about 0.97; median bin G2 about 0.69, three bins G2 about 0.1
(constructor 0.971 / 0.69 / 0.11); habit-null negative control KL to habits below 5e-4 (must be near 0);
full-policy G2 about 0.008; allowed epsilon about 3e-3 per member.
"""
import time
import numpy as np
from math import comb
from scipy.optimize import minimize, minimize_scalar
from core import Par, run

t0 = time.time()
PAR = Par()
hab = np.array([comb(4, k) for k in range(5)]) / 16.0


def kl(c, q):
    m = c > 0
    return float(np.sum(c[m] * np.log(c[m] / q[m])))


def group(vC, gC):
    k = np.arange(5)
    G = -0.5 * np.log1p(k * vC / PAR.Rs) + PAR.psi * k
    lw = np.log([comb(4, j) for j in range(5)]) - gC * G
    lw -= lw.max()
    q = np.exp(lw)
    return q / q.sum()


def vstar(pv):
    F, Q, qc = PAR.F, PAR.Q, PAR.qc
    Pm = np.array([[F * F * pv + Q + qc, F * pv], [F * pv, pv + qc]])
    return np.linalg.inv(np.linalg.inv(Pm) + np.diag([1 / PAR.R, 3 / (PAR.R + PAR.Rc)]))[0, 0]


def index(laws, wts, vfix=None):
    den = sum(wt * kl(c, hab) for c, wt in zip(laws, wts))
    if vfix is None:
        obj = lambda z: sum(wt * kl(c, group(np.exp(z[0]), np.exp(z[1]))) for c, wt in zip(laws, wts))
        best = min((minimize(obj, [np.log(v0), np.log(g0)], method="Nelder-Mead",
                             options=dict(xatol=1e-10, fatol=1e-15, maxiter=20000))
                    for v0 in (0.03, 0.1, 0.3) for g0 in (50, 400, 2000)), key=lambda z: z.fun)
        num = min(best.fun, den)
    else:
        obj = lambda g: sum(wt * kl(c, group(v, g)) for c, wt, v in zip(laws, wts, vfix))
        rr = minimize_scalar(obj, bounds=(0, 5000), method="bounded", options=dict(xatol=1e-6))
        num = min(rr.fun, den)
    return 1 - num / den, num, den


o = run(PAR, K=2000, T=400, burn=80, seed=5101, mode="full", want_agency=True)
A = o.agency
sym = A["sym"].astype(bool)
nc, cc, p = A["newcount"][sym], A["curcount"][sym], A["p"][sym]
c_all = np.bincount(nc, minlength=5) / len(nc)
pm = float(np.median(p))
i2, num2, den2 = index([c_all], [1.0], [vstar(pm)])
i1, num1, den1 = index([c_all], [1.0])
print(f"coarse state: law {np.round(c_all, 4)}; G2 {i2:.4f}; G1 {i1:.5f}; KL(P||E) {den2:.4f}  ({time.time()-t0:.0f}s)")
qs = np.quantile(p, [0.05, 0.15, 0.45, 0.55, 0.85, 0.95])
bins = [(qs[0], qs[1]), (qs[2], qs[3]), (qs[4], qs[5])]
laws, vs = [], []
for lo, hi in bins:
    sel = (p >= lo) & (p <= hi)
    laws.append(np.bincount(nc[sel], minlength=5) / sel.sum()); vs.append(vstar(float(np.median(p[sel]))))
for lab, c in zip(("10%", "50%", "90%"), laws):
    print(f"  p-bin {lab}: law {np.round(c, 4)}")
im2 = index([laws[1]], [1.0], [vs[1]])[0]; im1 = index([laws[1]], [1.0])[0]
i32 = index(laws, [1, 1, 1], vs)[0]; i31 = index(laws, [1, 1, 1])[0]
print(f"median p-bin: G2 {im2:.4f}, G1 {im1:.4f};  three p-bins: G2 (per-bin v*) {i32:.4f}, G1 (one v_C) {i31:.4f}"
      f"   (constructor 0.69 / 0.978; 0.11 / 0.30)")
lo, hi = np.quantile(p, [0.4, 0.6])
for n0 in range(5):
    sel = (p >= lo) & (p <= hi) & (cc == n0)
    if sel.sum() < 500:
        continue
    cnt = np.bincount(nc[sel], minlength=5) / sel.sum()
    print(f"  state (median p-bin, current count {n0}), n={sel.sum()}: law {np.round(cnt, 3)}; G1 {index([cnt], [1.0])[0]:.4f}; "
          f"G2 {index([cnt], [1.0], [vstar(float(np.median(p[sel])))])[0]:.4f}")
# full-policy reading
att = A["klatt"].mean()
print(f"full policy (attention included), coarse state: attention KL to habits {att:.3f}; G2 {1-(num2+att)/(den2+att):.5f}")
# largest total attention KL x compatible with Agency0 = 0.9 in a fixed-habit class: (num+x)/(den+x) <= 0.1
x = (0.1 * den2 - num2) / 0.9
print(f"  Agency0 = 0.9 with fixed attention habits needs total attention KL <= {x:.4f} nats, i.e. habit mass off the "
      f"mates set epsilon <= about {x/4:.4f} per member")
# negative control: habit null through the same estimator
oh = run(PAR, K=500, T=300, burn=60, seed=5102, mode="hab", want_agency=True)
ch = np.bincount(oh.agency["newcount"], minlength=5) / len(oh.agency["newcount"])
print(f"NEG habit null: law {np.round(ch, 4)}; KL to habits {kl(ch, hab):.2e} (must be near 0)")
print(f"total {time.time()-t0:.1f}s")
