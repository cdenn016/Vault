r"""Check 2: independent recomputation at I* under the literal real-time protocol (T-real).

Computed with my own code (core.py): Sigma^c_A by two-replica Monte Carlo of the actual filters, r(A), the region
contrasts of the 8-agent population, the clause (c) mechanism medium (8 agents, one component, 8 slots read by all,
attention 3 of 7 mates, (P4) among 8) and the clause (c) mean-coupling medium; the inference clause in four
readings; the agency index at the coarse decision state, slot component only (constructor's reading) and with the
attention component included (the members' full policies).

Declared expectations (before running):
  r(A) = 4.43 +/- 0.05 (constructor 4.4319 +/- 0.0075); Sigma^c compound symmetric within MC error; open rate
  about 0.39; attention deviation rate about 1e-4; mechanism medium about 2.94; mean coupling 1 + (6/7)(r(A)-1).
  Inference, eta_t marginal, best constant encoding: about 0.081 (constructor 0.0812); claimed-variance encoding
  about 0.098.  Joint (eta_t, eta_{t-1}) belief against the union posterior on the same state, best constant
  encoding: about 0.17 by my estimate (above alpha_I = 0.09).
  Agency, slot component, coarse state: G2 about 0.97, G1 about 0.9999.  With the attention component included:
  far below 0.9 (attention departs from its uniform habits by about ln 64 per member; no group model with fixed
  habits reproduces it because G_C does not depend on internal attention).
  NEGATIVE CONTROL: Rc = 1e6 (relays carry nothing) must give r(A) within 0.05 of 1.
"""
import time
import itertools
import numpy as np
from math import comb
from scipy.optimize import minimize, minimize_scalar
from core import Par, run, compound, r_ab, contrast, is_diffusive

t0 = time.time()
PAR = Par()
MED = Par(n=8, n_inf=7, n_zero=0, nslots=8)
K, T, BURN = 3000, 400, 80


def summary(out, n):
    al, be = compound(out.S)
    ab = np.array([compound(s) for s in out.S_batches])
    nb = len(ab)
    loo = np.array([r_ab(n, (ab[:, 0].sum() - ab[k, 0]) / (nb - 1), (ab[:, 1].sum() - ab[k, 1]) / (nb - 1))
                    for k in range(nb)])
    se_r = np.sqrt((nb - 1) / nb * np.sum((loo - loo.mean()) ** 2))
    return al, be, r_ab(n, al, be), se_r


o = run(PAR, K=K, T=T, burn=BURN, seed=2101, mode="full", want_inf=True, want_agency=True)
al, be, rA, se = summary(o, 4)
S = o.S
print(f"[I*, T-real] K={K} worlds x 2 replicas, T={T}, burn={BURN}; open rate {o.open_rate:.4f}; "
      f"attention deviation rate {o.dev_rate:.2e}")
print("  Sigma^c_A (raw) =\n", np.array2string(S, precision=6))
print(f"  compound: alpha={al:.6f} beta={be:.6f}; max |raw - compound| {np.abs(S - (al*np.eye(4)+be)).max():.1e}")
print(f"  r(A) = {rA:.4f} +/- {se:.4f}   (constructor 4.4319 +/- 0.0075)")
SA = al * np.eye(4) + be
S8 = np.zeros((8, 8)); S8[:4, :4] = SA; S8[4:, 4:] = SA
Pi = np.linalg.inv(S8)
dif = is_diffusive(Pi, tol=1e-12)
rc = {C: contrast(Pi, C) for k in range(2, 9) for C in itertools.combinations(range(8), k)}
oth = max(v for C, v in rc.items() if C not in ((0, 1, 2, 3), (4, 5, 6, 7)))
both = max(v for C, v in rc.items() if any(i < 4 for i in C) and any(i >= 4 for i in C))
print(f"  Pi^c diffusive={dif[0]} (largest offdiag {dif[1]:.2e}, smallest row sum {dif[2]:.3f}); r(A) from Pi "
      f"{rc[(0,1,2,3)]:.4f}; largest other region {oth:.4f}; largest region meeting both niches {both:.4f}")
eps = Pi.sum(1); a = -Pi[0, 1]
abar = a * 12 / 28
r_mc = 1 + 8 * abar / eps[0]
print(f"  mean-coupling medium: abar={abar:.4f} eps={eps[0]:.4f} -> r_hom = {r_mc:.4f}")
print(f"  ({time.time()-t0:.0f}s)")

# ---------------- mechanism medium ----------------
om = run(MED, K=1500, T=T, burn=BURN, seed=2102, mode="full")
alm, bem, rM, seM = summary(om, 8)
Sm = om.S
print(f"[mechanism medium] open rate {om.open_rate:.4f}; deviation rate {om.dev_rate:.2e}; alpha={alm:.6f} "
      f"beta={bem:.6f}; max |raw - compound| {np.abs(Sm - (alm*np.eye(8)+bem)).max():.1e}")
PiM = np.linalg.inv(alm * np.eye(8) + bem)
rcM = max(contrast(PiM, C) for k in range(2, 9) for C in itertools.combinations(range(8), k))
print(f"  whole-medium contrast {rM:.4f} +/- {seM:.4f}; sup over regions {rcM:.4f}  (constructor 2.9417 +/- 0.0072)")
print(f"WINDOW mechanism ({rM:.4f}, {rA:.4f}];  WINDOW mean coupling ({r_mc:.4f}, {rA:.4f}]")
print(f"  ({time.time()-t0:.0f}s)")

# ---------------- inference clause ----------------
I = o.inf
N = I["n"]
E_q1 = I["d0sq_over"] / N
E_inv1 = I["inv00"] / N
E_ln1 = I["ln00"] / N
kl1_best = 0.5 * (E_q1 + E_ln1 + np.log(E_inv1))
kl1_claim = 0.5 * (I["claim1"] / N + E_q1)
E_q2 = I["q2"] / N
Einv2 = np.array([[I["inv2_00"], I["inv2_01"]], [I["inv2_01"], I["inv2_11"]]]) / N
E_lndet = I["lndet"] / N
kl2_best = 0.5 * (E_q2 + E_lndet + np.log(np.linalg.det(Einv2)))
kl2_claim = 0.5 * (I["claim2"] / N + E_q2)
rev1 = 0.5 * (np.log((I["rev1_P"] + I["rev1_dd"]) / N) - E_ln1)
C2 = np.array([[I["rev2_00"], I["rev2_01"]], [I["rev2_01"], I["rev2_11"]]]) / N
rev2 = 0.5 * (np.log(np.linalg.det(C2)) - E_lndet)
print(f"[inference] E(ybar0 - m*0)^2 = {I['d0sq']/N:.5f}; E[1/P*00]^-1 = {1/E_inv1:.5f}")
print(f"  eta_t marginal: best constant {kl1_best:.5f} (mean term {0.5*E_q1:.5f}); claimed-variance {kl1_claim:.5f}; "
      f"reverse best constant {rev1:.5f}   (constructor 0.0812 / 0.0979 / 0.075)")
print(f"  joint (eta_t, eta_(t-1)): best constant {kl2_best:.5f} (mean term {0.5*E_q2:.5f}); claimed-variance "
      f"{kl2_claim:.5f}; reverse best constant {rev2:.5f}")
print(f"  ({time.time()-t0:.0f}s)")

# ---------------- agency ----------------
A = o.agency
sym = A["sym"].astype(bool)
nc = A["newcount"][sym]
p = A["p"][sym]
c = np.bincount(nc, minlength=5) / len(nc)
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


pmed = float(np.median(p))
vs = vstar(pmed)
den = kl(c, hab)
r2 = minimize_scalar(lambda g: kl(c, group(vs, g)), bounds=(0, 5000), method="bounded", options=dict(xatol=1e-6))
num2 = min(r2.fun, den)
best1 = min((minimize(lambda z: kl(c, group(np.exp(z[0]), np.exp(z[1]))), [np.log(v0), np.log(g0)],
                      method="Nelder-Mead", options=dict(xatol=1e-10, fatol=1e-15, maxiter=20000))
             for v0 in (0.03, 0.1, 0.3) for g0 in (50, 400, 2000)), key=lambda z: z.fun)
num1 = min(best1.fun, den)
lor = None
p11 = sum(c[k] * k * (k - 1) / 12 for k in range(5)); p10 = sum(c[k] * k * (4 - k) / 12 for k in range(5))
p00 = sum(c[k] * (4 - k) * (3 - k) / 12 for k in range(5))
print(f"[agency] symmetric decision rounds {sym.sum()} of {len(sym)}; law of the new open count {np.round(c, 4)}; "
      f"median p {pmed:.5f}, v* {vs:.5f}; KL(P||E) {den:.5f}; log odds ratio {np.log(p11*p00/p10**2):.4f}")
print(f"  slot component, coarse state: G2 index {1 - num2/den:.4f} (gamma_C {r2.x:.1f}); G1 index {1 - num1/den:.5f}"
      f"   (constructor 0.971 / 0.99988)")
klatt_round = A["klatt"].mean()
qbar = A["qm_mean"].reshape(-1, 4, PAR.mmax + 1)
# per-member law of m averaged over all recorded rounds (a mixture): KL to the habit law of m (lower bound)
wv = PAR.w / PAR.w.sum()
qb = qbar.mean(0)
kl_mix = sum(float(np.sum(qb[i] * np.log(qb[i] / wv))) for i in range(4))
for name, att in (("per-round conditional laws (average)", klatt_round), ("mixture law (lower bound)", kl_mix)):
    print(f"  attention included, {name}: attention KL to habits {att:.4f} nats; "
          f"G2 index {1 - (num2 + att)/(den + att):.5f}; G1 index {1 - (num1 + att)/(den + att):.5f}")
print(f"  P(m = 3 informative relays) averaged {A['qm3'].mean():.6f}")

# ---------------- negative control ----------------
on = run(PAR.with_(Rc=1e6), K=600, T=300, burn=60, seed=2103, mode="full")
aln, ben, rn, sen = summary(on, 4)
print(f"NEG Rc=1e6: r(A) = {rn:.4f} +/- {sen:.4f} (must be within 0.05 of 1); deviation rate {on.dev_rate:.3f}")
print(f"total {time.time()-t0:.1f}s")
