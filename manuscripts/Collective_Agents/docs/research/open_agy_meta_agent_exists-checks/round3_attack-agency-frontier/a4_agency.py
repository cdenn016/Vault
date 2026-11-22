r"""Attack run a4: D1's agency index (def:agy-agency-index, 05_agency.tex:240-246) recomputed, and under the
LITERAL external states of 05_agency.tex:11 ("the world states that members sense and the active channels of
non-members that they hear").

In D1 the members of A can attend the relays of the non-members o1, o2 (support {}, {mate}, {o1}, {o2}).  Under
def:col-partition (04_collectives.tex:17-26) member i's channel y_{i,o} reads a non-collective variable (o's speech
channel), so it is a sensory state, o's channel is exterior, and it is part of eta_C; reading it is opening an
exterior-facing sensory channel, i.e. a slot of def:agy-group-model (05_agency.tex:157), with no pragmatic term (the
members' preferences put no cost on relays).  G_C then carries -I_{q_C}(eta_C; o) for those channels, which is
1/2 ln(1 + n_o V_o / R_c) for n_o members reading outsider o, V_o = q_C's variance of o's channel content.  Any q_C
that is a function of A's coarse state and is calibrated has V_o >= R = 1 (o's private sensing noise), prior value
Var(eta^B) + R = 1.263.  The candidate's class G2 (translate of the members' anticipated belief about eta^A) does not
say what V_o is.

Declared expectations:
  (a) R-outsider reading (candidate): index 0.800000 (KL_a 2 ln 4, KL_s|a 16 ln 2, slot misfit ~ 1e-16).
  (b) literal reading, calibrated V_o >= 1: the misfit is increasing in gamma_C from gamma_C = 0 (its derivative
      there is E_E[I] - 8 psi > 0), so the infimum is the habit-only model and the index is EXACTLY 0.
  (c) index -> 0.8 only as V_o -> 0 (q_C nearly certain of the non-members' messages).
NEGATIVE CONTROLS: V_o = 0 must reproduce (a); gamma_C = 0 must give misfit = KL(P||E) (index 0).
"""
import itertools
import time
import numpy as np
from scipy.optimize import minimize_scalar
from mylib import Par, steady, gains, efe, lbin

t0 = time.time()
par = Par()
m = par.m
Pm = steady(par, 1, 0)
_, _, _, _, Pp = gains(par, Pm, 1, 0)
vstar = Pp[0, 0]
lb = lbin(m)
sets = ["0", "mate", "o1", "o2"]
cset = {"0": 0, "mate": 1, "o1": 0, "o2": 0}
# member law over (set, k) with multiplicity C(m,k) per count
lw = np.array([[lb[k] - par.gamma * efe(par, Pm, cset[s], k) for k in range(m + 1)] for s in sets])
lw -= lw.max()
Pk = np.exp(lw); Pk /= Pk.sum()           # P(set, count k) (count k aggregates C(m,k) patterns)
pa = Pk.sum(1)
# KL to habits: uniform 1/4 on sets, 2^-m on patterns
KLa1 = sum(pa[i] * np.log(4 * pa[i]) for i in range(4) if pa[i] > 0)
KLs1 = 0.0
for i in range(4):
    pk = Pk[i] / pa[i]
    for k in range(m + 1):
        if pk[k] > 0:
            KLs1 += pa[i] * pk[k] * (np.log(pk[k]) - lb[k] + m * np.log(2.0))
KLa, KLs = 2 * KLa1, 2 * KLs1
den = KLa + KLs
print(f"P(mate) = 1 - {1 - pa[1]:.3e}; KL_a {KLa:.6f} (2 ln 4 = {2 * np.log(4):.6f}); KL_s|a {KLs:.6f} "
      f"(16 ln 2 = {16 * np.log(2):.6f}); v* {vstar:.5f}")
lb2 = lbin(2 * m)
Ks = np.arange(2 * m + 1)
# actual joint law of (k1+k2) and pattern log-probabilities, by attention pair
pairs = list(itertools.product(range(4), range(4)))


def slot_terms(gam, vC):
    GC = -0.5 * np.log1p(Ks * vC / par.Rs) + par.psi * Ks
    lZ = np.logaddexp.reduce(lb2 - 2 * m * np.log(2.0) - gam * GC)
    # E_P[ln P(s|a)] - E_P[ln Pg^slot(s)] summed over both members, given the attention pair
    out = {}
    for (i, j) in pairs:
        pk1 = Pk[i] / pa[i]; pk2 = Pk[j] / pa[j]
        val = 0.0
        for k1 in range(m + 1):
            for k2 in range(m + 1):
                w = pk1[k1] * pk2[k2]
                if w <= 0:
                    continue
                lp = np.log(pk1[k1]) - lb[k1] + np.log(pk2[k2]) - lb[k2]          # per pattern
                lg = -2 * m * np.log(2.0) - gam * GC[k1 + k2] - lZ
                val += w * (lp - lg)
        out[(i, j)] = val
    return out


def att_terms(gam, Vo):
    # Pg^att(a1,a2) propto (1/16) exp(gam * I_att(a1,a2)); I_att from outsider readings
    I = np.zeros((4, 4))
    for (i, j) in pairs:
        for o in ("o1", "o2"):
            no = (sets[i] == o) + (sets[j] == o)
            if no:
                I[i, j] += 0.5 * np.log1p(no * Vo / par.Rc)
    lg = np.log(1 / 16) + gam * I
    lg -= np.logaddexp.reduce(lg.ravel())
    return lg, I


def misfit(gam, Vo, vC):
    lg, _ = att_terms(gam, Vo)
    st = slot_terms(gam, vC)
    tot = 0.0
    for (i, j) in pairs:
        w = pa[i] * pa[j]
        if w <= 0:
            continue
        tot += w * (np.log(pa[i] * pa[j]) - lg[i, j]) + w * st[(i, j)]
    return tot


def inf_mis(Vo, vC=None, free_v=False):
    best = misfit(0.0, Vo, vstar)
    cand = [(0.0, vstar, best)]
    vgrid = [vstar] if not free_v else [1e-8, 1e-4, 0.01, vstar, 1.0]
    for vC in vgrid:
        r = minimize_scalar(lambda z: misfit(np.exp(z), Vo, vC), bounds=(-12, 8), method="bounded",
                            options=dict(xatol=1e-9))
        cand.append((float(np.exp(r.x)), vC, float(r.fun)))
    g, v, f = min(cand, key=lambda z: z[2])
    return f, g, v


f0, g0, _ = inf_mis(0.0)
print(f"(a) R-outsider / V_o = 0 (G2): inf misfit {f0:.6e} at gamma_C {g0:.1f}; index {1 - f0 / den:.6f}")
print(f"NEG gamma_C = 0: misfit {misfit(0.0, 1.0, vstar):.6f} vs KL(P||E) {den:.6f}")
_, I = att_terms(0.0, 1.0)
EI = I.mean()
print(f"E_E[I_att] at V_o = 1: {EI:.4f}; 8 psi = {8 * par.psi:.4f}; derivative of the misfit at gamma_C = 0 "
      f"(attention part + slot part) > 0 expected")
for Vo in (1e-6, 1e-4, 1e-3, 3e-3, 1e-2, 3e-2, 0.1, 0.136, 0.2, 0.5, 1.0, 1.263):
    f, g, v = inf_mis(Vo)
    f1, g1, v1 = inf_mis(Vo, free_v=True)
    print(f"(b/c) V_o = {Vo:<8g}: G2-lit index {1 - f / den:.5f} (gamma_C* {g:.3g}); "
          f"G1-lit (v_C free) index {1 - f1 / den:.5f} (gamma_C* {g1:.3g}, v_C* {v1:.2g})")
print(f"({time.time() - t0:.1f}s)")
