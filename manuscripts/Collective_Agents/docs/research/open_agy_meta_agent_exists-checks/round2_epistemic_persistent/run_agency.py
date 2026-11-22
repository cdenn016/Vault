r"""Deciding script 4: agency index (def:agy-agency-index, 05_agency.tex:240-246) of C = A on the slot component.

Decision states: covariance states at which the members deliberate.  X* = the symmetric state at the median of the
stationary law of the members' posterior variance p (from simulated paths); X_q = {10%, 50%, 90% quantiles}.
Actual law: stationary law of the (P4) chain whose member i resamples its slot with its marginal policy posterior
(soft-min of its full EFE over its attention sets) -- by the declared protocol and by the lumping argument, the
slot marginal of the joint (P4) chain over (attention, slot).
Admissible classes (all contain the habit-only model gamma_C = 0, habits fixed at the uniform product, slot
likelihood N(eta_{t+1}, Rs) per open slot, slot preference psi per open slot):
  G1: v_C = Var_{q_C}(eta_{t+1}) free in (0, inf), gamma_C in [0, inf);
  G2: v_C = the members' anticipated variance of eta_{t+1} after own sensor and three relays at X (E2 belief);
  G3: v_C = the members' current predictive variance of eta_{t+1} at X (E1 belief), gamma_C free.
Declared expectations: at X*, index >= 0.999 in G1 and G2, KL(P||E) > 0, log odds ratio of two members' choices
about -0.3 (law not a product law); NEGATIVE CONTROL: a member whose slot choices ignore the others (product law with
the same marginals) has index well below 1 in G2 at X* only if the class cannot represent independence -- reported;
second NEGATIVE CONTROL: at an asymmetric state the chain is not reversible (detailed-balance violation > 0).
"""
import numpy as np
from math import comb
from scipy.optimize import minimize, minimize_scalar
from lib import (Pminus, posterior, efe_table, softmin_att, attention_weights, p4_chain, profiles,
                 simulate_policy_path, info_ab)
from instance import PAR, T, BURN

w = attention_weights(PAR, 3, 4)
P = profiles(4)
NP = P.sum(1)
E = np.full(16, 1 / 16)


def actual_law(ps):
    Gt = np.array([softmin_att(PAR, efe_table(PAR, Pminus(PAR, p), 3, 4), w) for p in ps])
    v, Tm = p4_chain(PAR.gamma, Gt)
    F = v[:, None] * Tm
    return v, float(np.abs(F - F.T).max())


def group_law(vC, gC):
    G = -0.5 * np.log1p(NP * vC / (PAR.Rs + PAR.Rsh)) + PAR.psi * NP
    lw = -gC * G
    lw -= lw.max()
    q = np.exp(lw)
    return q / q.sum()


def kl(p, q):
    return float(np.sum(p * (np.log(p) - np.log(q))))


def index(laws, weights, vC_fixed=None):
    den = sum(wt * kl(L, E) for L, wt in zip(laws, weights))
    if vC_fixed is None:
        def obj(z):
            vC, gC = np.exp(z[0]), np.exp(z[1])
            return sum(wt * kl(L, group_law(vC, gC)) for L, wt in zip(laws, weights))
        best = min((minimize(obj, x0=[np.log(v0), np.log(g0)], method="Nelder-Mead",
                             options=dict(xatol=1e-10, fatol=1e-16, maxiter=20000))
                    for v0 in (0.03, 0.06, 0.1) for g0 in (100, 400, 1000)), key=lambda r: r.fun)
        num, par_ = best.fun, (float(np.exp(best.x[0])), float(np.exp(best.x[1])))
    else:
        vs = vC_fixed if isinstance(vC_fixed, (list, tuple)) else [vC_fixed] * len(laws)
        def obj1(g):
            return sum(wt * kl(L, group_law(v, g)) for L, wt, v in zip(laws, weights, vs))
        r = minimize_scalar(obj1, bounds=(0.0, 5000.0), method="bounded", options=dict(xatol=1e-9))
        num, par_ = min(r.fun, obj1(0.0)), (vs, float(r.x))
    return 1 - num / den, num, den, par_


def e2_var(p):
    Pm = Pminus(PAR, p)
    return posterior(Pm, 1 / PAR.R, 3 / (PAR.R + PAR.Rc))[0, 0]


# stationary law of the members' posterior variance p on symmetric rounds
rng = np.random.default_rng(9001)
pv = []
for k in range(30):
    pth = simulate_policy_path(PAR, T, rng, "full")
    for t in range(BURN, T):
        Pm = pth.Pm[t]
        if np.allclose(Pm, Pm[0], atol=1e-12, rtol=0):
            # posterior variance of eta_{t-1} at round t (p of the previous round) equals P^-_{11} - qc
            pv.append(Pm[0, 1, 1] - PAR.qc)
pv = np.array(pv)
q10, q50, q90 = np.quantile(pv, [0.1, 0.5, 0.9])
print(f"stationary p on symmetric rounds: n={len(pv)}, mean {pv.mean():.5f}, quantiles 10/50/90% = "
      f"{q10:.5f}/{q50:.5f}/{q90:.5f}, range {pv.min():.5f}..{pv.max():.5f}")

L50, db50 = actual_law([q50] * 4)
lawn = np.array([L50[NP == k].sum() for k in range(5)])
gib = np.exp(-PAR.gamma * softmin_att(PAR, efe_table(PAR, Pminus(PAR, q50), 3, 4), w)[NP])
gib /= gib.sum()
print(f"X*: p={q50:.5f}; P(n open) = {np.round(lawn, 5)}; P(open) = {(L50 @ P)[0]:.4f}; "
      f"detailed-balance violation {db50:.1e}; max|chain - Gibbs| {np.abs(L50 - gib).max():.1e}")
m2 = np.zeros((2, 2))
for k, pr in enumerate(P):
    m2[pr[0], pr[1]] += L50[k]
lor = np.log(m2[1, 1] * m2[0, 0] / (m2[1, 0] * m2[0, 1]))
marg = L50 @ P
prod = np.array([np.prod([marg[i] if pr[i] else 1 - marg[i] for i in range(4)]) for pr in P])
print(f"X*: KL(P||E) = {kl(L50, E):.6f} (departure from habits); KL(P||product of marginals) = {kl(L50, prod):.6f}; "
      f"log odds ratio of two members' choices {lor:.4f}")
for name, kw in (("G1 (v_C, gamma_C free)", dict()), ("G2 (v_C = E2 belief)", dict(vC_fixed=e2_var(q50))),
                 ("G3 (v_C = E1 belief)", dict(vC_fixed=Pminus(PAR, q50)[0, 0]))):
    A_, num, den, pr_ = index([L50], [1.0], **kw)
    print(f"  index at X*, {name}: {A_:.7f} (min KL {num:.3e}, denominator {den:.5f}, fitted {pr_})")
# product-law control
A_p, num_p, den_p, pr_p = index([prod], [1.0])
print(f"  control: product law with the same marginals, G1: index {A_p:.5f} (min KL {num_p:.2e}, den {den_p:.5f})")
# three declared decision states, one group model
Ls = [actual_law([q] * 4)[0] for q in (q10, q50, q90)]
for name, kw in (("G1", dict()), ("G2 (per-state E2 variance)", dict(vC_fixed=[e2_var(q) for q in (q10, q50, q90)])),
                 ("G3 strict (one v_C = E1 variance at X*)", dict(vC_fixed=Pminus(PAR, q50)[0, 0]))):
    A_, num, den, pr_ = index(Ls, [1 / 3] * 3, **kw)
    print(f"  index on X_q (10/50/90%), {name}: {A_:.7f} (min KL {num:.3e}, den {den:.5f})")
# asymmetric decision state (negative control for reversibility; index reported)
La, dba = actual_law([q50 + 0.004, q50, q50, q50])
A_, num, den, pr_ = index([La], [1.0])
print(f"asymmetric X (member 0 at p+0.004): detailed-balance violation {dba:.2e}; index G1 {A_:.6f}")
A_p2, num_p2, den_p2, _ = index([prod], [1.0], vC_fixed=e2_var(q50))
print(f"NEG control: product law with the same marginals in G2 (v_C fixed at the E2 belief): index {A_p2:.5f} "
      f"(min KL {num_p2:.3e}, den {den_p2:.5f})")
