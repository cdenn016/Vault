r"""A6: agency index of P0 (def:agy-agency-index, 05_agency.tex:240-246), own code.

Joint policy = full attention profile (5^4 profiles).  Actual law: product of the
members' EFE policy posteriors at the stationary decision state (weight 1).
Class G2: habits fixed at uniform, G_C(pi) = -1/2 ln(1 + k V_u / R_c), k = number of
members reading S, V_u = P^-_{11} + R_S, gamma_C in [0, inf).  Class W: eta_C = world
only.  Group posterior P_g(pi) = e^{-gamma_C G(k)} / sum_k N_k e^{-gamma_C G(k)},
N_k = C(n,k) 4^{n-k}, so KL(P||P_g) = -H(P) + gamma_C E_P[G] + ln sum_k N_k e^{-gamma_C G(k)}.
Declared expectations (candidate): KL(P||E) = 4 ln 5 = 6.4378; index 1 - O(1e-13)
at gamma = 40; at member precision 4: G2 0.9857, W 0.9345.
Negative control: a law in which every member reads mate 1 w.p. 0.999 -> index ~0.
"""
import os
for v in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS"):
    os.environ[v] = "1"
from math import comb
import mpmath as mp
from alib import P0Model

mp.mp.dps = 60
m = P0Model()
R, RS, Rc, n = m.R, m.RS, m.Rc, m.n
Vu = mp.mpf(m.Pm[1, 1]) + mp.mpf(RS)
Veta = mp.mpf(m.Pm[1, 1])


def member_law(gamma):
    G = m.efe_options()
    Gv = [G["none"], G["S"], G["mate"], G["mate"], G["mate"]]
    w = [mp.e ** (-mp.mpf(gamma) * mp.mpf(g)) for g in Gv]
    Z = mp.fsum(w)
    return [x / Z for x in w]


def G2(k):
    return -mp.mpf(0.5) * mp.log(1 + k * Vu / mp.mpf(Rc))


def GW(k):
    if k == 0:
        return mp.mpf(0)
    return -mp.mpf(0.5) * mp.log(1 + Veta / (mp.mpf(RS) + mp.mpf(Rc) / k))


def index_for(p, Gfun):
    """p: member law over 5 options (index 1 = S). Product law over members."""
    pS = p[1]
    # entropy of the product law
    H1 = -mp.fsum(x * mp.log(x) for x in p if x > 0)
    H = n * H1
    Pk = [comb(n, k) * pS ** k * (1 - pS) ** (n - k) for k in range(n + 1)]
    Gk = [Gfun(k) for k in range(n + 1)]
    EG = mp.fsum(Pk[k] * Gk[k] for k in range(n + 1))
    Nk = [comb(n, k) * 4 ** (n - k) for k in range(n + 1)]
    KLPE = -H + n * mp.log(5)

    def KL(gc):
        lw = [mp.log(Nk[k]) - gc * Gk[k] for k in range(n + 1)]
        mx = max(lw)
        lse = mx + mp.log(mp.fsum(mp.e ** (l - mx) for l in lw))
        return -H + gc * EG + lse
    # KL is convex in gc (log-partition); minimize by derivative root: E_P[G] = E_Pg[G]
    def dKL(gc):
        lw = [mp.log(Nk[k]) - gc * Gk[k] for k in range(n + 1)]
        mx = max(lw)
        ws = [mp.e ** (l - mx) for l in lw]
        Z = mp.fsum(ws)
        EgG = mp.fsum(ws[k] * Gk[k] for k in range(n + 1)) / Z
        return EG - EgG
    if dKL(mp.mpf(0)) >= 0:
        gbest = mp.mpf(0)
    else:
        lo, hi = mp.mpf(0), mp.mpf(1)
        while dKL(hi) < 0:
            hi *= 2
            if hi > mp.mpf(10) ** 8:
                break
        for _ in range(400):
            mid = (lo + hi) / 2
            if dKL(mid) < 0:
                lo = mid
            else:
                hi = mid
        gbest = (lo + hi) / 2
    kb = KL(gbest)
    return KLPE, kb, 1 - kb / KLPE, gbest


for gamma in (40.0, 10.0, 4.0, 2.0):
    p = member_law(gamma)
    KLPE, kb, idx2, g2 = index_for(p, G2)
    _, kw, idxW, gw = index_for(p, GW)
    print("member gamma=%5.1f p(S)=%s p(each mate)=%s KL(P||E)=%s | G2 infKL=%s index=%s gamma_C*=%s | W index=%s" %
          (gamma, mp.nstr(p[1], 15), mp.nstr(p[2], 4), mp.nstr(KLPE, 8), mp.nstr(kb, 4), mp.nstr(idx2, 16), mp.nstr(g2, 5), mp.nstr(idxW, 8)))

q = [mp.mpf("0.00025"), mp.mpf("0.00025"), mp.mpf("0.999"), mp.mpf("0.00025"), mp.mpf("0.00025")]
# for the NC the law is not exchangeable within k (mate 1 favoured); compute KL directly over profiles
import itertools
profiles = list(itertools.product(range(5), repeat=n))
Pj = [mp.fprod(q[c] for c in pr) for pr in profiles]
ks = [sum(1 for c in pr if c == 1) for pr in profiles]
Gk = [G2(k) for k in range(n + 1)]
KLPE = mp.fsum(P * mp.log(P * 625) for P in Pj)
best = None
for gc in [mp.mpf(0)] + [mp.mpf(10) ** (x / 10) for x in range(-40, 41)]:
    lw = [-gc * Gk[k] for k in ks]
    mx = max(lw)
    lZ = mx + mp.log(mp.fsum(mp.e ** (l - mx) for l in lw))
    kl = mp.fsum(P * (mp.log(P) - (l - lZ)) for P, l in zip(Pj, lw))
    best = kl if best is None else min(best, kl)
print("NC (each member reads mate 1 w.p. .999): KL(P||E)=%s index G2=%s (expect ~0)" % (mp.nstr(KLPE, 6), mp.nstr(1 - best / KLPE, 6)))
