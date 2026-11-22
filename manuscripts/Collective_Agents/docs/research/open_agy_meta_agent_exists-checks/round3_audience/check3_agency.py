r"""Check 3: agency index (def:agy-agency-index, 05_agency.tex:240-246) under the FULL-POLICY reading, instance P0.

Members' joint policy: each audience member's whole policy, i.e. its attention set J (the only chosen active
component; its broadcast is fixed and it has no records or acts).  Policy set of member i: {empty, S, m_1, m_2, m_3}
(kmsg = 1), habits E_i uniform (1/5 each), product over members (625 profiles).
Decision state: the stationary covariance state of the full model (all members read the source); members decide
independently (no data or intention sharing), so the actual law P(.|X*) is the product of the members' policy
posteriors.  No deliberation chain is involved, so real-time and frozen-state readings coincide.

Group models (def:agy-group-model, 05_agency.tex:156-161):
  eta_C = (eta_{t+1}, u_S(t))  (world state the members sense and the active channel of the non-member they hear,
  05_agency.tex:11); slots: member i's reading of the source channel, o_i = u_S(t) + nu_i, conditionally independent
  across slots given eta_C, likelihood shared by every belief; reading a mate opens no slot (internal channel).
  G_C(pi) = -I_{q_C}(eta_C; o_{B(pi)}) = -1/2 ln(1 + k(pi) V_u / Rc),  k = number of members reading the source,
  V_u = Var_{q_C}(u_S(t)).  No pragmatic terms.  Habits fixed at prod_i E_i.  gamma_C in [0, inf).
  Class G2: q_C = the members' anticipated belief, V_u = P^-_{11}(X*) + RS.  Class G1: V_u free.
  Reading variant W (not the definition): eta_C = eta only, o_i = eta_t + v_S + nu_i (common noise), so
  G_C(k) = -1/2 ln(1 + P11/(RS + Rc/k)).

Declared expectations before running:
  at gamma = 40: KL(P||E) = 4 ln 5 = 6.4378 nats to 1e-9; index >= 1 - 1e-9 under G2, G1 and W;
  across gamma in {2, 4, 10, 40}: index >= 0.9 under G2 for gamma >= 10;
  NEGATIVE CONTROLS: (i) a law in which every member reads a mate deterministically (departure from habits
  explained by no slot) must give index <= 0.05; (ii) a law in which members read the source with probability 0.9
  but positively associated (all-or-none) must give an index clearly below the product law's.
"""
import itertools
import time
import numpy as np
from scipy.optimize import minimize_scalar
from aud import Par, riccati_fixed, b_of, type_law, info

t0 = time.time()
par = Par()
n = par.n
opts = ["0", "S", "m1", "m2", "m3"]            # policy set of a member (kmsg = 1)
E1 = np.full(5, 0.2)
profiles = list(itertools.product(range(5), repeat=n))
kS = np.array([sum(1 for x in pr if x == 1) for pr in profiles])
lnE = np.array([np.sum(np.log(E1[list(pr)])) for pr in profiles])


def member_law(par, Pm, gamma):
    r"""Policy posterior of one member over {0, S, m1, m2, m3}."""
    G0 = -info(Pm, 1.0 / par.R, 0.0)
    GS = -info(Pm, 1.0 / par.R, b_of(par, 1, 0))
    Gm = -info(Pm, 1.0 / par.R, b_of(par, 0, 1))
    G = np.array([G0, GS, Gm, Gm, Gm])
    lw = np.log(E1) - gamma * G
    lw -= lw.max()
    p = np.exp(lw)
    return p / p.sum()


def lnP_product(q):
    lq = np.log(q)
    return np.array([np.sum(lq[list(pr)]) for pr in profiles])


def kl(lnP, lnQ):
    P = np.exp(lnP)
    m = P > 0
    return float(np.sum(P[m] * (lnP[m] - lnQ[m])))


def lnPg(GC_k, gC):
    lw = lnE - gC * GC_k[kS]
    mx = lw.max()
    return lw - (mx + np.log(np.exp(lw - mx).sum()))


def best_gC(lnP, GC_k):
    obj = lambda z: kl(lnP, lnPg(GC_k, np.exp(z)))
    r = minimize_scalar(obj, bounds=(-10, 12), method="bounded", options=dict(xatol=1e-10))
    v0 = kl(lnP, lnPg(GC_k, 0.0))
    return (r.fun, float(np.exp(r.x))) if r.fun < v0 else (v0, 0.0)


def index(lnP, GC_list):
    den = kl(lnP, lnE)
    best = min(best_gC(lnP, g) for g in GC_list)
    return 1 - best[0] / den, best, den


ks = np.arange(n + 1)


def GC_G2(Pm):
    Vu = Pm[1, 1] + par.RS
    return -0.5 * np.log1p(ks * Vu / par.Rc)


def GC_G1_list():
    return [-0.5 * np.log1p(ks * Vu / par.Rc) for Vu in np.geomspace(1e-5, 1e3, 161)]


def GC_W(Pm):
    out = np.zeros(n + 1)
    for k in range(1, n + 1):
        out[k] = -0.5 * np.log1p(Pm[1, 1] / (par.RS + par.Rc / k))
    return out


for gamma in (2.0, 4.0, 10.0, 40.0):
    p = par.with_(gamma=gamma)
    # stationary decision state under this gamma: the full model's covariance when the members follow their law;
    # for gamma >= 10 the law is all-source to < 1e-3 and the all-source covariance is used; for smaller gamma
    # the all-source covariance is still used as the declared decision state (it is reported, not re-solved).
    Pm_A, _ = riccati_fixed(p, 1.0 / p.R, b_of(p, 1, 0))
    q = member_law(p, Pm_A, gamma)
    lnP = lnP_product(q)
    i2, b2, den = index(lnP, [GC_G2(Pm_A)])
    i1, b1, _ = index(lnP, GC_G1_list())
    iw, bw, _ = index(lnP, [GC_W(Pm_A)])
    print(f"gamma={gamma:5.1f}: member law {np.round(q, 6)}; KL(P||E) {den:.6f}; index G2 {i2:.10f} "
          f"(num {b2[0]:.3e}, gamma_C {b2[1]:.4g}); G1 {i1:.10f}; W {iw:.10f}")

# negative controls at the gamma = 40 decision state
Pm_A, _ = riccati_fixed(par, 1.0 / par.R, b_of(par, 1, 0))
qm = np.array([1e-12, 1e-12, 1 - 2e-12 - 2e-12, 1e-12, 1e-12])
qm /= qm.sum()
lnP = lnP_product(qm)
i2, b2, den = index(lnP, [GC_G2(Pm_A)])
i1, _, _ = index(lnP, GC_G1_list())
print(f"NEG (i) every member reads mate m1: KL(P||E) {den:.4f}; index G2 {i2:.6f}, G1 {i1:.6f}")
# all-or-none association: P(all S) = 0.9, P(all choose 0) = 0.1
lnP = np.full(len(profiles), -np.inf)
lnP[[k for k, pr in enumerate(profiles) if all(x == 1 for x in pr)][0]] = np.log(0.9)
lnP[[k for k, pr in enumerate(profiles) if all(x == 0 for x in pr)][0]] = np.log(0.1)
den = kl(lnP, lnE)
i2 = 1 - best_gC(lnP, GC_G2(Pm_A))[0] / den
q9 = np.array([0.1, 0.9, 0, 0, 0]) + 1e-300
lnPp = lnP_product(q9 / q9.sum())
i2p = 1 - best_gC(lnPp, GC_G2(Pm_A))[0] / kl(lnPp, lnE)
print(f"NEG (ii) all-or-none law (0.9 / 0.1): index G2 {i2:.4f}; product law with the same marginals: {i2p:.4f}")
print(f"({time.time() - t0:.0f}s)")
