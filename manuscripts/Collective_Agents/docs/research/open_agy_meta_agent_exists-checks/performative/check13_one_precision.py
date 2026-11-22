r"""Check 13: one policy precision for attention and acts (def:fw-system, (P3)).

Attention: a member of niche A chooses 3 of its 7 others; EFE of a slot set = -I(eta_t; relays | own data),
computed at the steady-state prior P^- of the full-attention filter (one-step information).  Only niche-mates
carry information.  P(set) ~ exp(gamma * I(set)).  Report P(set = all 3 niche-mates) for gamma = 2, 20, 100, 300.
Acts: continuous Gaussian group posterior with c = sigE2 gamma Lam b^2 fixed at the value giving b g n = 0.04
(g = 0.05); agency index over 200 decision states as in check 12, for gamma = 2, 20, 100 (expected ~ invariant).
Declared expectation: attention is sharp only for gamma of order 100 or more; the act index is ~0.967 at every gamma.
"""
import itertools
import numpy as np
from pc import riccati_scalar, exch_closed_form

F, Q, R, Rc, b, n, g, Lam = 0.9, 0.05, 1.0, 0.2, 0.2, 4, 0.05, 4.0
Pm, Pp = riccati_scalar(F, Q, 1 / R + 3 / (R + Rc))
P_own = 1 / (1 / Pm + 1 / R)
others = list(range(1, 8))  # agent 0's others; niche-mates are 1,2,3
sets = list(itertools.combinations(others, 3))
def info(S):
    k = sum(1 for j in S if j in (1, 2, 3))
    return 0.5 * np.log(P_own * (1 / P_own + k / (R + Rc)))
I = np.array([info(S) for S in sets])
for gam in [2, 20, 100, 300]:
    w = np.exp(gam * (I - I.max())); w /= w.sum()
    best = [i for i, S in enumerate(sets) if set(S) == {1, 2, 3}][0]
    print("attention gamma=%4d: P(all three niche-mates) = %.4f ; info gain of best set %.4f nats, of a set with two mates %.4f" % (
        gam, w[best], I[best], info((1, 2, 4))))

c = b * g * n / (F * n - b * g * n * n)
alpha = exch_closed_form(n, F, Q, R, Rc, b, g)["alpha"]
for gam in [2.0, 20.0, 100.0]:
    sigE2 = c / (gam * Lam * b ** 2)
    rng = np.random.default_rng(1)
    Z = np.linalg.qr(np.column_stack([np.ones(n) / 2, rng.standard_normal((n, n - 1))]))[0][:, 1:]
    def gauss(gC, z):
        S = np.linalg.inv(np.eye(n) / sigE2 + gC * Lam * b ** 2 * np.ones((n, n)))
        return -gC * Lam * b * S @ z, S
    def kl(m1, S1, m0, S0):
        S0i = np.linalg.inv(S0); d = m0 - m1
        return 0.5 * (np.trace(S0i @ S1) - n + d @ S0i @ d + np.log(np.linalg.det(S0) / np.linalg.det(S1)))
    acts, den = [], 0.0
    for _ in range(200):
        z = F * (0.3 + Z @ (np.sqrt(alpha) * rng.standard_normal(n - 1)))
        mu, S = gauss(gam, z); acts.append((mu, S)); den += kl(mu, S, np.zeros(n), sigE2 * np.eye(n))
    grid = np.linspace(0, 3 * gam, 901)
    best = min((sum(kl(mu, S, *gauss(gC, F * 0.3 * np.ones(n))) for mu, S in acts), gC) for gC in grid)
    print("acts gamma=%5.0f sigE2=%.2e: continuous agency index %.5f at gamma_C=%.2f" % (gam, sigE2, 1 - best[0] / den, best[1]))
