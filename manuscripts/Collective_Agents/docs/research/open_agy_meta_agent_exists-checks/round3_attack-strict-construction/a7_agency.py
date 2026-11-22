r"""A7 (attack): agency index of niche A of I** (def:agy-agency-index, 05_agency.tex:240-246), recomputed with my own
policy laws (explicit enumeration of the 2 x 64 policies) and my own fit.
Decision states: (p after the round-t update, sigma(t)) sampled from 3 stationary paths x 3000 rounds (burn 200), equal
weights.  Actual law of pi(t+1): 'frozen' product of the members' posteriors; 'real' one uniformly chosen reviser
redraws sigma from its marginal, the others keep sigma(t), every member draws M | sigma.
Classes (habits fixed at the uniform product; gamma_C >= 0):
  K1 = the candidate's G1: P_g = prod U64(M_i) x P^s_g(sigma), P^s_g prop exp(-gC G_C(|sigma|)),
       G_C(k) = -1/2 ln(1 + k v/Rs) + psi k, v free constant, psi fixed at the members' 0.030;
  K2 = K1 with free psi_C (still a slot-product preference on the private sensors);
  K3 = K1 plus the other niche's channels counted as slots (exterior-facing sensory channels, def:agy-group-model,
       05_agency.tex:157) with a slot-product pragmatic cost: P_g(M_i) prop exp(-lam nB(M_i)), lam = gC psi_B >= 0 free.
Declared expectations: K1 strict full-policy index about 0.071-0.073 (real) and 0.0748 (frozen); slot-only K1 about
0.65 (real) and 0.998 (frozen).  K3: I expect about 0.5 (the attention part 4 ln 64 drops to about 4 ln 8).
NEGATIVE CONTROLS: habit-only model gives index 0 exactly; K3 at lam = 0 equals K1.
"""
import sys, time
import numpy as np
from scipy.optimize import minimize
from mylib import Cfg, Policies, simulate, prior_cov, logits_member, lse

t0 = time.time()
LN64 = np.log(64.0)
PROF = np.array([[(k >> i) & 1 for i in range(4)] for k in range(16)])
CNT = PROF.sum(1)


def member_laws(c, pol, nB, p, sig):
    """per member: q1 = P(sigma'=1); for s in {0,1}: H-terms of q(M|s) for KL to U64 and to the lam-family."""
    out = []
    for i in range(4):
        Pm = prior_cov(c, p[i])
        mates = [j for j in range(4) if j != i]
        lg = logits_member(c, pol, Pm, sig[mates].astype(float), c.gamma)       # (2, 64)
        lz = lse(lg, axis=1)
        q1 = 1.0 / (1.0 + np.exp(lz[0] - lz[1]))
        res = []
        for s in (0, 1):
            q = np.exp(lg[s] - lz[s])
            negH = float(np.sum(np.where(q > 0, q * np.log(np.where(q > 0, q, 1)), 0.0)))
            EnB = float(q @ nB)
            res.append((negH, EnB))
        out.append((q1, res))
    return out


def run(proto, npaths=3, T=3200, burn=200):
    c = Cfg(proto=proto)
    pol = Policies(3, 4, 3)
    nB = np.array([sum(1 for ch in cmb if ch >= 3) for cmb in pol.sets], float)
    rng = np.random.default_rng(81 if proto == "real" else 82)
    states = []
    for k in range(npaths):
        pth = simulate(c, T, rng, "full", keep_states=True)
        states += pth.states[burn:]
    PX, attH, attB = [], [], []
    for (t, p, sig) in states:
        L = member_laws(c, pol, nB, p, sig)
        q1 = np.array([l[0] for l in L])
        if proto == "frozen":
            Ps = np.prod(np.where(PROF == 1, q1[None, :], 1 - q1[None, :]), axis=1)
        else:
            Ps = np.zeros(16)
            cur = sum(int(sig[i]) << i for i in range(4))
            for r in range(4):
                base = cur & ~(1 << r)
                Ps[base] += 0.25 * (1 - q1[r]); Ps[base | (1 << r)] += 0.25 * q1[r]
        # attention terms, expected under the slot law: sum_i [negH_i(s_i)], sum_i E[nB](s_i)
        aH = np.array([sum(L[i][1][PROF[k, i]][0] for i in range(4)) for k in range(16)])
        aB = np.array([sum(L[i][1][PROF[k, i]][1] for i in range(4)) for k in range(16)])
        PX.append(Ps); attH.append(float(Ps @ aH)); attB.append(float(Ps @ aB))
    PX = np.array(PX); attH = np.array(attH); attB = np.array(attB)
    w = np.full(len(PX), 1.0 / len(PX))
    negHs = np.array([float(np.sum(np.where(P > 0, P * np.log(np.where(P > 0, P, 1)), 0))) for P in PX])
    slot_den = float(w @ (negHs + np.log(16)))
    att_U64 = float(w @ (attH + 4 * LN64))                    # sum_i KL(q(M|s)||U64)
    den = slot_den + att_U64
    Pbar = w @ PX
    nHbar = float(w @ negHs)
    def slot_kl(v, g, psiC):
        G = -0.5 * np.log1p(CNT * v / c.Rs) + psiC * CNT
        lp = -g * G - lse(-g * G)
        return nHbar - float(Pbar @ lp)
    def fit(free_psi):
        best = slot_kl(1.0, 0.0, c.psi)   # habit-only
        for v0 in (1e-3, 0.03, 0.1, 0.3, 1.0):
            for g0 in (3.0, 30.0, 300.0, 3000.0):
                for ps0 in ((c.psi,) if not free_psi else (0.0, 0.02, 0.03, 0.05)):
                    x0 = [np.log(v0), np.log(g0)] + ([ps0] if free_psi else [])
                    f = (lambda z: slot_kl(np.exp(z[0]), np.exp(z[1]), z[2])) if free_psi else \
                        (lambda z: slot_kl(np.exp(z[0]), np.exp(z[1]), c.psi))
                    r = minimize(f, x0, method="Nelder-Mead", options=dict(xatol=1e-10, fatol=1e-14, maxiter=6000))
                    best = min(best, r.fun)
        return best
    s1 = fit(False); s2 = fit(True)
    # K3 attention part: E sum_i KL(q(M|s)||P_lam) = attH + lam attB + 4 ln Z(lam)
    lZ = lambda lam: np.log(8 + 28 * np.exp(-lam) + 24 * np.exp(-2 * lam) + 4 * np.exp(-3 * lam))
    lams = np.concatenate([[0.0], np.logspace(-2, 3, 400)])
    attK3 = min(float(w @ (attH + lam * attB)) + 4 * lZ(lam) for lam in lams)
    attK3_0 = float(w @ attH) + 4 * lZ(0.0)
    idx = lambda num: 1 - num / den
    print(f"[{proto}] {len(PX)} decision states ({time.time()-t0:.0f}s); open law mean count {Pbar @ CNT / 4:.4f}; "
          f"den {den:.4f} (slot {slot_den:.4f}, attention {att_U64:.4f}; 4 ln 64 = {4*LN64:.4f})")
    print(f"   K1 (candidate G1) full {idx(s1 + att_U64):.5f}  slot-only {1 - s1/slot_den:.5f}  C12 cap {slot_den/den:.5f}")
    print(f"   K2 (free psi_C)   full {idx(s2 + att_U64):.5f}  slot-only {1 - s2/slot_den:.5f}")
    print(f"   K3 (other-niche channels as slots, free cost) full {idx(s1 + attK3):.5f}; attention part {attK3:.4f} "
          f"(4 ln 8 = {4*np.log(8):.4f}); NEG K3 at lam=0 equals K1: {abs(attK3_0 - att_U64) < 1e-9}")
    print(f"   NEG habit-only index {idx(slot_den + att_U64):.1e} (expected 0)", flush=True)


for proto in sys.argv[1:]:
    run(proto)
print(f"total {time.time()-t0:.0f}s")
