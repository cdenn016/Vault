r"""Agency index (def:agy-agency-index, 05_agency.tex:240-246) for I**, computed exactly at each decision state.

Decision state X (end of round t): the members' posterior variances p_i (after the round-t update; they fix
P^-_i(t+1)) and the current statuses sigma(t), which every member knows through the intention headers.
Actual law of the joint policy pi(t+1) = (sigma(t+1), M(t+1)):
  'frozen' (P4 at the frozen state): prod_i q_i(sigma_i) q_i(M_i | sigma_i), q_i prop. E_i exp(-gamma G_i);
  'real'   one uniformly chosen reviser r redraws sigma_r ~ q_r(sigma_r); the others keep sigma_i(t); every member
           draws M_i ~ q_i(M_i | sigma_i(t+1)).
Habits E: uniform over the 2 x 64 policies of each member.
Group models (admissible classes; all contain the habit-only model gamma_C = 0 with habits E):
  P_g(sigma, M) = prod_i U64(M_i) * P^s_g(sigma),  P^s_g(sigma) prop. exp(-gamma_C G_C(|sigma|)),
  G_C(k) = -1/2 ln(1 + k v_C / Rs) + psi k  (slots read eta_{t+1} with likelihood N(eta, Rs); slot-product
  preference psi per open sensor; habits held fixed at E; gamma_C in [0, inf)).
  G1: v_C a free positive constant;  G2: v_C(X) declared = mean over members of Var(eta_{t+1}) after own sensor,
  the three s-relays and the o-relays of the mates open at t (the members' anticipated belief before their sensor).
Full-policy reading: KL over (sigma, M); slot-only reading: KL over sigma only.
"""
from __future__ import annotations

import numpy as np
from math import comb
from scipy.optimize import minimize, minimize_scalar

from lib3 import Par, Pminus, efe_grid, log_att_weights, lse

LN64 = np.log(64.0)
PROFILES = np.array([[(k >> (3 - i)) & 1 for i in range(4)] for k in range(16)])   # member 0 = most significant
COUNTS = PROFILES.sum(1)


def member_laws(par: Par, p: np.ndarray, sig: np.ndarray):
    r"""For each member: slot-marginal open probability q1, attention KL to U64 given own status s (KLa[s]),
    the anticipated variance v_ant, and the grouped attention law (for checks)."""
    n = len(p)
    k1 = sig.sum() - sig
    P00, P01, P11 = Pminus(par, p)
    G = efe_grid(par, P00, P01, P11)                    # (n, 2, K+1, K+1)
    lw = log_att_weights(par, k1)                       # (n, K+1, K+1)
    X = lw[:, None] - par.gamma * G                      # (n, 2, K+1, K+1)
    Xf = X.reshape(n, 2, -1)
    lZ = lse(Xf, 2)                                      # (n, 2)
    q1 = 1.0 / (1.0 + np.exp(lZ[:, 0] - lZ[:, 1]))
    Qa = np.exp(Xf - lZ[:, :, None])                     # grouped attention law (n, 2, cells)
    lwf = np.broadcast_to(lw.reshape(n, 1, -1), Qa.shape)
    with np.errstate(invalid="ignore", divide="ignore"):
        term = np.where(Qa > 0, Qa * (np.log(Qa) - lwf), 0.0)
    KLa = term.sum(2) + LN64                             # (n, 2)
    # anticipated variance of eta_{t+1} after own sensor, 3 s-relays, k1 o-relays
    a = 1.0 / par.R
    b = 3.0 / (par.R + par.Rc) + k1 / (par.Rs + par.Rc)
    det = P00 * P11 - P01 ** 2
    i00, i01, i11 = P11 / det, -P01 / det, P00 / det
    L00, L11 = i00 + a, i11 + b
    v_ant = L11 / (L00 * L11 - i01 ** 2)
    return q1, KLa, v_ant, Qa


def state_summary(par: Par, p: np.ndarray, sig: np.ndarray, proto: str):
    r"""Per decision state: slot law over the 16 profiles, KL of the slot law to U16, attention KL (expected under
    the slot law), count law, declared G2 belief variance."""
    q1, KLa, v_ant, _ = member_laws(par, p, sig)
    if proto == "frozen":
        Ps = np.prod(np.where(PROFILES == 1, q1[None, :], 1 - q1[None, :]), axis=1)
    else:
        Ps = np.zeros(16)
        cur = int(sum(int(s) << (3 - i) for i, s in enumerate(sig)))
        for r in range(4):
            bit = 1 << (3 - r)
            base = cur & ~bit
            Ps[base] += 0.25 * (1 - q1[r])
            Ps[base | bit] += 0.25 * q1[r]
    att = float(np.sum(Ps * np.sum(np.where(PROFILES == 1, KLa[None, :, 1], KLa[None, :, 0]), axis=1)))
    m = Ps > 0
    negH = float(np.sum(Ps[m] * np.log(Ps[m])))
    kl_u16 = negH + np.log(16.0)
    cnt = np.array([Ps[COUNTS == k].sum() for k in range(5)])
    return dict(Ps=Ps, att=att, negH=negH, kl_u16=kl_u16, cnt=cnt, v2=float(np.mean(v_ant)), q1=q1)


def GC(par: Par, v, k=np.arange(5)):
    return -0.5 * np.log1p(np.asarray(k)[None, :] * np.asarray(v, float)[:, None] / par.Rs) + par.psi * np.asarray(k)[None, :]


LOGC = np.log([comb(4, k) for k in range(5)])


def kl_slot_to_group(par: Par, cnt: np.ndarray, negH: np.ndarray, v: np.ndarray, gC: float) -> np.ndarray:
    r"""KL(P_sigma || P^s_g) per state = negH + gamma_C E[G_C(K)] + ln Z_g, Z_g = sum_k C(4,k) exp(-gamma_C G_C(k))."""
    G = GC(par, v)                                        # (S, 5)
    lz = lse(LOGC[None, :] - gC * G, 1)
    return negH + gC * np.sum(cnt * G, 1) + lz


def index_from_summaries(par: Par, S: list, w=None, cls: str = "G1", full_policy: bool = True):
    r"""Agency index over the declared decision states S (list of state summaries) with weights w."""
    nS = len(S)
    w = np.full(nS, 1.0 / nS) if w is None else np.asarray(w, float) / np.sum(w)
    cnt = np.array([s["cnt"] for s in S]); negH = np.array([s["negH"] for s in S])
    att = np.array([s["att"] for s in S]) if full_policy else np.zeros(nS)
    klu = np.array([s["kl_u16"] for s in S])
    den = float(np.sum(w * (klu + att)))
    if cls == "G1":
        # P_g does not depend on X in G1, so the objective depends on the states only through the averaged count
        # law and the averaged negative entropy (exact reduction)
        cbar = np.sum(w[:, None] * cnt, 0)[None, :]
        nHbar = np.array([float(np.sum(w * negH))])

        def obj(z):
            return float(kl_slot_to_group(par, cbar, nHbar, np.array([np.exp(z[0])]), np.exp(z[1]))[0])
        best = None
        for v0 in (1e-3, 0.01, 0.05, 0.1, 0.3, 1.0, 3.0):
            for g0 in (1.0, 30.0, 300.0, 3000.0):
                r = minimize(obj, x0=[np.log(v0), np.log(g0)], method="Nelder-Mead",
                             options=dict(xatol=1e-9, fatol=1e-13, maxiter=4000))
                if best is None or r.fun < best.fun:
                    best = r
        slot_num = min(best.fun, float(np.sum(w * klu)))
        fit = (float(np.exp(best.x[0])), float(np.exp(best.x[1])))
    elif cls == "G2":
        v2 = np.array([s["v2"] for s in S])
        f = lambda g: float(np.sum(w * kl_slot_to_group(par, cnt, negH, v2, g)))
        cands = []
        for lo, hi in ((0.0, 50.0), (0.0, 500.0), (0.0, 5000.0), (0.0, 50000.0)):
            r = minimize_scalar(f, bounds=(lo, hi), method="bounded", options=dict(xatol=1e-8))
            cands.append((r.fun, r.x))
        cands.append((f(0.0), 0.0))
        slot_num, gbest = min(cands)
        fit = (None, float(gbest))
    else:
        raise ValueError(cls)
    num = slot_num + float(np.sum(w * att))
    c12 = float(np.sum(w * klu)) / den if den > 0 else 1.0     # C12 bound: slot KL / total KL
    return dict(index=1 - num / den if den > 0 else 1.0, num=num, den=den, slot_num=slot_num,
                slot_den=float(np.sum(w * klu)), att=float(np.sum(w * att)), fit=fit, c12_bound=c12)


def mixture_summary(S: list, w=None, full_policy_att: bool = True):
    r"""Coarse single decision state: the stationary mixture of the slot laws; attention part approximated by the
    mean attention KL (exact up to the total correlation of the members' attention given the profile, >= 0)."""
    nS = len(S)
    w = np.full(nS, 1.0 / nS) if w is None else np.asarray(w, float) / np.sum(w)
    Ps = np.sum(w[:, None] * np.array([s["Ps"] for s in S]), 0)
    m = Ps > 0
    negH = float(np.sum(Ps[m] * np.log(Ps[m])))
    cnt = np.array([Ps[COUNTS == k].sum() for k in range(5)])
    att = float(np.sum(w * np.array([s["att"] for s in S])))
    v2 = float(np.sum(w * np.array([s["v2"] for s in S])))
    return dict(Ps=Ps, att=att, negH=negH, kl_u16=negH + np.log(16.0), cnt=cnt, v2=v2)
