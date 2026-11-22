r"""Check 8: independent spot check of the open-neighborhood claim at four points of the +/-1% box (my own design:
all +, all -, two random sign vectors over (F, Q, R, Rc, Rs, psi, gamma, qc)), T-real, declared readings.
Declared expectations (before running): at every point r(A) in [4.1, 4.8], mechanism medium in [2.8, 3.1], so
r0 = 3.5 admissible; N_hab and N_pr below 2.0; eta_t-marginal inference (best constant) below 0.09 (constructor's
box max 0.0847); joint (eta_t, eta_{t-1}) inference above 0.15 at every point (the reading-dependent failure is not
an artifact of the center); coarse-state G2 agency above 0.9.
"""
import time
import numpy as np
from math import comb
from scipy.optimize import minimize_scalar
from core import Par, run, compound, r_ab

t0 = time.time()
names = ("F", "Q", "R", "Rc", "Rs", "psi", "gamma", "qc")
base = Par()
rng = np.random.default_rng(8101)
signs = [np.ones(8), -np.ones(8), rng.choice([-1, 1], 8), rng.choice([-1, 1], 8)]
habc = np.array([comb(4, k) for k in range(5)]) / 16.0


def kl(c, q):
    m = c > 0
    return float(np.sum(c[m] * np.log(c[m] / q[m])))


for sg in signs:
    kw = {nm: getattr(base, nm) * (1 + 0.01 * s) for nm, s in zip(names, sg)}
    P = base.with_(**kw)
    M = P.with_(n=8, n_inf=7, n_zero=0, nslots=8)
    o = run(P, 1500, 400, 80, 8102, mode="full", want_inf=True, want_agency=True)
    rA = r_ab(4, *compound(o.S))
    rM = r_ab(8, *compound(run(M, 800, 400, 80, 8103, mode="full").S))
    rH = r_ab(4, *compound(run(P, 1000, 400, 80, 8104, mode="hab").S))
    rP = r_ab(4, *compound(run(P, 1000, 400, 80, 8105, mode="pr").S))
    I = o.inf; N = I["n"]
    kl1 = 0.5 * (I["d0sq_over"] / N + I["ln00"] / N + np.log(I["inv00"] / N))
    Einv2 = np.array([[I["inv2_00"], I["inv2_01"]], [I["inv2_01"], I["inv2_11"]]]) / N
    kl2 = 0.5 * (I["q2"] / N + I["lndet"] / N + np.log(np.linalg.det(Einv2)))
    A = o.agency; sym = A["sym"].astype(bool)
    c = np.bincount(A["newcount"][sym], minlength=5) / sym.sum()
    pv = float(np.median(A["p"][sym]))
    Pm = np.array([[P.F ** 2 * pv + P.Q + P.qc, P.F * pv], [P.F * pv, pv + P.qc]])
    vC = np.linalg.inv(np.linalg.inv(Pm) + np.diag([1 / P.R, 3 / (P.R + P.Rc)]))[0, 0]

    def grp(g):
        k = np.arange(5)
        G = -0.5 * np.log1p(k * vC / P.Rs) + P.psi * k
        lw = np.log([comb(4, j) for j in range(5)]) - g * G
        q = np.exp(lw - lw.max()); return q / q.sum()
    den = kl(c, habc)
    num = min(minimize_scalar(lambda g: kl(c, grp(g)), bounds=(0, 5000), method="bounded").fun, den)
    print(f"signs {''.join('+' if s > 0 else '-' for s in sg)}: r(A) {rA:.3f}, medium {rM:.3f}, N_hab {rH:.3f}, N_pr {rP:.3f}; "
          f"r0=3.5 admissible {rM < 3.5 <= rA}; inference eta_t {kl1:.4f}, joint {kl2:.4f}; G2 agency {1-num/den:.4f}; "
          f"open rate {o.open_rate:.3f}  ({time.time()-t0:.0f}s)", flush=True)
print(f"total {time.time()-t0:.1f}s")
