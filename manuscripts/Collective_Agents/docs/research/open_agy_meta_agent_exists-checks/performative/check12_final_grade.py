r"""Check 12: remaining clause numbers for PN at the final act gain g = 0.05.

Declared expectations: (a) quenched N_pr draws (acts kept, g = 0.05) non-diffusive in (almost) all of 99 draws;
(b) N_inf contrast above r(A) (same partition at the fixed baseline); (c) continuous Gaussian agency index
close to 1 with habits fixed; (d) Omega_int(A | zeta_B) > 0, zero across niches; (e) windowed Pi^c at
g = 0.05 equals the closed form and the collectives at levels in (5.0754, 24.4989] are exactly A and B.
"""
import itertools
import numpy as np
from pc import world_conditional_cov, diffusivity, contrast, exch_closed_form
from pcg import build
from check8_nulls_pn import spec_reads, all_contrasts
from check5_candidate import pn_spec

F, Q, R, Rc, b, n, N, g = 0.9, 0.05, 1.0, 0.2, 0.2, 4, 8, 0.05
A_, B_ = list(range(4)), list(range(4, 8))

if __name__ == "__main__":
    # (e)
    m = build(pn_spec(g=g))
    Pi = np.linalg.inv(world_conditional_cov(m["A"], m["Qx"], m["iw"], m["ia"], 120))
    cf = exch_closed_form(n, F, Q, R, Rc, b, g)
    rs = all_contrasts(Pi)
    sel = [C for C, r, het in rs if r >= 5.0755 and 5.0755 > max(het, 5.0754)]
    print("(e) diffusive=%s r(A)=%.6f closed form %.6f; selected at r0=5.0755: %s; second-largest region contrast %.4f" % (
        diffusivity(Pi)["diffusive"], contrast(Pi, A_)["r"], cf["r"], sel, sorted([r for _, r, _ in rs])[-3]))
    # (a)
    rng = np.random.default_rng(7)
    nd = 0
    for draw in range(99):
        reads = [list(rng.choice([j for j in range(N) if j != i], size=3, replace=False)) for i in range(N)]
        mm = build(spec_reads(reads, g))
        P = np.linalg.inv(world_conditional_cov(mm["A"], mm["Qx"], mm["iw"], mm["ia"], 60))
        nd += diffusivity(P, tol=1e-10)["diffusive"]
    print("(a) N_pr quenched at g=%.2f: diffusive draws %d/99" % (g, nd))
    # (b)
    mi = build(pn_spec(g=g, known=False, mu=1.0))
    Pii = np.linalg.inv(world_conditional_cov(mi["A"], mi["Qx"], mi["iw"], mi["ia"], 120))
    print("(b) N_inf (others' acts modeled): diffusive=%s r(A)=%.4f" % (diffusivity(Pii)["diffusive"], contrast(Pii, A_)["r"]))
    # (c) continuous agency, act rule b g n = F n c/(1+n c)
    gam, Lam = 2.0, 4.0
    c = b * g * n / (F * n - b * g * n * n)
    sigE2 = c / (gam * Lam * b ** 2)
    alpha = cf["alpha"]
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
    best = min((sum(kl(mu, S, *gauss(gC, F * 0.3 * np.ones(n))) for mu, S in acts), gC) for gC in np.linspace(0, 6, 601))
    print("(c) continuous agency at g=%.2f (sigE2=%.5f): index %.5f at gamma_C=%.2f" % (g, sigE2, 1 - best[0] / den, best[1]))
    # (d) Omega_int over six rounds
    Am, Qx = m["A"], m["Qx"]; Qp = Qx.copy(); Qp[0, 0] -= Q; Qp[1, 1] -= Q
    T, d = 6, Am.shape[0]
    Phi = [np.linalg.matrix_power(Am, k) for k in range(T)]
    C = np.zeros((T * d, T * d))
    for t in range(1, T + 1):
        for s in range(1, T + 1):
            C[(t - 1) * d:t * d, (s - 1) * d:s * d] = sum(Phi[t - 1 - u] @ Qp @ Phi[s - 1 - u].T for u in range(min(t, s)))
    def mi_pair(i, j):
        ii = [t * d + 2 + i for t in range(T)]; jj = [t * d + 2 + j for t in range(T)]
        Sii, Sjj, Sij = C[np.ix_(ii, ii)], C[np.ix_(jj, jj)], C[np.ix_(ii, jj)]
        M = np.linalg.solve(Sii, Sij) @ np.linalg.solve(Sjj, Sij.T)
        return -0.5 * np.log(np.linalg.det(np.eye(T) - M))
    print("(d) Omega_int(A|zeta_B) = %.4f nats (pairs within A averaged); across niches %.2e" % (
        np.mean([mi_pair(i, j) for i, j in itertools.combinations(A_, 2)]), mi_pair(0, 4)))
