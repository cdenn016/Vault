r"""Check 9: (i) EFE-consistent act rules and the sign rule; (ii) aggregate and continuous agency for PN.

(i) Two exchangeable firms on one price (all-to-all raw relays inside each firm, Rc), firm k predicts with
its own model (Fhat_k, bhat_k), models the other firm's act as mu_k*(-g_o n_o m_i^+) (with bhat_k), reads
its own realized total act, and acts by the group-posterior mean of a one-step quadratic EFE with Gaussian
habits: bhat_k g_k n_k = Fe_k n c_k/(1 + n c_k), c_k = sigE2 gam Lam bhat_k^2, Fe_k = Fhat_k - mu_k bhat_k g_o n_o
(solved jointly when mu = (1,1)).  True world: eta' = F eta + b (U_1 + U_2) + w.
Prediction coefficient phi_k = Fe_k - bhat_k g_k n_k = Fe_k/(1 + n c_k); loading kappa_k = b g_k sqrt(n).
Declared expectations: cross entries of Pi^c have the sign of phi_1 kappa_1 phi_2 kappa_2:
  (a) correct models: +;  (b) firm 1 believes Fhat_1 = -0.5: + (both signs flip together);
  (c) firm 1 believes bhat_1 = -b (wrong sign of its effect): -;  (d) mu = (1,1), correct: +.
(ii) PN agency: aggregate index over 200 equally weighted decision states (discrete declared model), and
the continuous Gaussian version with the dynamics' own act rule (gam=2, Lam=4, sigE2 such that b g n = 0.12).
"""
import itertools
import numpy as np
from pc import world_conditional_cov, diffusivity, riccati_scalar


def build_model_firms(n, F, Q, R, Rc, b, models, mus, sigE2=0.12, gam=2.0, Lam=4.0):
    # models: [(Fhat, bhat), (Fhat, bhat)]
    N = 2 * n
    firm = [0] * n + [1] * n
    c = [sigE2 * gam * Lam * models[k][1] ** 2 for k in range(2)]
    # solve for g_k (fixed point when mu=1)
    g = [0.0, 0.0]
    for _ in range(2000):
        gn = []
        for k in range(2):
            o = 1 - k
            Fh, bh = models[k]
            Fe = Fh - mus[k] * bh * g[o] * n
            gn.append(Fe * n * c[k] / (1 + n * c[k]) / (bh * n))
        if max(abs(gn[0] - g[0]), abs(gn[1] - g[1])) < 1e-15:
            g = gn; break
        g = gn
    gains, phis = [], []
    for k in range(2):
        o = 1 - k
        Fh, bh = models[k]
        Fe = Fh - mus[k] * bh * g[o] * n
        Pm, Pp = riccati_scalar(Fe, Q, 1 / R + (n - 1) / (R + Rc))
        gains.append((Pp / R, Pp / (R + Rc), Fe, bh))
        phis.append(Fe - bh * g[k] * n)
    nxi = 1 + N + N
    Cm = np.zeros((N, N)); Ceta = np.zeros(N); D = np.zeros((N, nxi))
    for i in range(N):
        k = firm[i]; ks, kc = gains[k][0], gains[k][1]
        mates = [j for j in range(N) if firm[j] == k and j != i]
        Cm[i, i] = 1 - ks - len(mates) * kc; Ceta[i] = ks + len(mates) * kc
        D[i, 1 + i] = ks * np.sqrt(R)
        for j in mates:
            D[i, 1 + j] = kc * np.sqrt(R)
        D[i, 1 + N + i] = kc * np.sqrt(len(mates) * Rc)
    gv = np.array([g[firm[i]] for i in range(N)])
    A = np.zeros((1 + N, 1 + N)); G = np.zeros((1 + N, nxi))
    A[0, 0] = F - b * gv @ Ceta; A[0, 1:] = -b * (gv @ Cm); G[0, 0] = np.sqrt(Q); G[0] += -b * (gv @ D)
    for i in range(N):
        k = firm[i]; Fe, bh = gains[k][2], gains[k][3]
        own = [j for j in range(N) if firm[j] == k]
        A[1 + i, 1:] = Fe * Cm[i] - bh * sum(gv[j] * Cm[j] for j in own)
        A[1 + i, 0] = Fe * Ceta[i] - bh * sum(gv[j] * Ceta[j] for j in own)
        G[1 + i] = Fe * D[i] - bh * sum(gv[j] * D[j] for j in own)
    return A, G @ G.T, g, phis


if __name__ == "__main__":
    F, Q, R, Rc, b, n = 0.9, 0.05, 1.0, 0.2, 0.2, 4
    cases = [("(a) correct models, mu=(0,0)", [(F, b), (F, b)], (0, 0)),
             ("(b) firm1 Fhat=-0.5, mu=(0,0)", [(-0.5, b), (F, b)], (0, 0)),
             ("(c) firm1 bhat=-b, mu=(0,0)", [(F, -b), (F, b)], (0, 0)),
             ("(d) correct models, mu=(1,1)", [(F, b), (F, b)], (1, 1))]
    for label, models, mus in cases:
        A, Qx, g, phis = build_model_firms(n, F, Q, R, Rc, b, models, mus)
        Pi = np.linalg.inv(world_conditional_cov(A, Qx, [0], list(range(1, 2 * n + 1)), 120))
        cross = Pi[:n, n:]
        kap = [b * g[k] * np.sqrt(n) for k in range(2)]
        pred = np.sign(phis[0] * kap[0] * phis[1] * kap[1])
        print("%-32s g=(%+.4f,%+.4f) phi=(%+.4f,%+.4f) kappa=(%+.4f,%+.4f) predicted sign %+d | cross in [%+.4e, %+.4e] diffusive=%s rho(A)=%.3f" % (
            label, g[0], g[1], phis[0], phis[1], kap[0], kap[1], pred, cross.min(), cross.max(),
            diffusivity(Pi)["diffusive"], max(abs(np.linalg.eigvals(A)))))

    # (ii) agency for PN
    from pc import exch_closed_form
    cf = exch_closed_form(n, F, Q, R, Rc, b, 0.15)
    alpha = cf["alpha"]
    rng = np.random.default_rng(1)
    Z = np.linalg.qr(np.column_stack([np.ones(n) / 2, rng.standard_normal((n, n - 1))]))[0][:, 1:]
    U = [-1.0, 0.0, 1.0]; prof = np.array(list(itertools.product(U, repeat=n)))
    Lam, gam = 4.0, 2.0
    nums, dens, devs = [], [], []
    for _ in range(200):
        dev = Z @ (np.sqrt(alpha) * rng.standard_normal(n - 1)); devs.append(dev)
        z = F * (0.3 + dev); zC = F * 0.3
        GC = 0.5 * Lam * (zC + b * prof.sum(axis=1)) ** 2
        tilt = (Lam * b * (z - zC)[None, :] * prof).sum(axis=1)
        lp = -gam * (GC + tilt); p = np.exp(lp - lp.max()); p /= p.sum()
        dens.append(np.sum(p * np.log(p * len(prof))))
        nums.append(p)
    # one gamma_C over all decision states (declared class: one precision over the declared states)
    best = (np.inf, None)
    for gC in np.linspace(0, 6, 1201):
        tot = 0.0
        for p, dev in zip(nums, devs):
            GC = 0.5 * Lam * (F * 0.3 + b * prof.sum(axis=1)) ** 2
            lq = -gC * GC; q = np.exp(lq - lq.max()); q /= q.sum()
            tot += np.sum(p * np.log(p / q))
        if tot < best[0]:
            best = (tot, gC)
    print("PN agency (discrete declared model, uniform habits fixed, one gamma_C over 200 equally weighted states): index = %.4f at gamma_C = %.3f" % (
        1 - best[0] / np.sum(dens), best[1]))
    # continuous Gaussian version with the dynamics' act rule: b g n = 0.12 = F n c/(1+n c) -> c
    c = 0.12 / (F * n - 0.12 * n)
    sigE2 = c / (gam * Lam * b ** 2)
    def gauss(gC, zvec):
        Prec = np.eye(n) / sigE2 + gC * Lam * b ** 2 * np.ones((n, n))
        S = np.linalg.inv(Prec)
        mu = -gC * Lam * b * S @ zvec
        return mu, S
    def kl(m1, S1, m0, S0):
        S0i = np.linalg.inv(S0); d = m0 - m1
        return 0.5 * (np.trace(S0i @ S1) - n + d @ S0i @ d + np.log(np.linalg.det(S0) / np.linalg.det(S1)))
    num_c, den_c = [], []
    for dev in devs:
        zvec = F * (0.3 + dev); zC = F * 0.3
        mu_a, S_a = gauss(gam, zvec)  # actual: tilted group posterior = Gaussian with members' own z_j
        den_c.append(kl(mu_a, S_a, np.zeros(n), sigE2 * np.eye(n)))
        num_c.append((mu_a, S_a))
    bestc = (np.inf, None)
    for gC in np.linspace(0, 6, 1201):
        tot = sum(kl(m, S, *gauss(gC, F * 0.3 * np.ones(n))) for m, S in num_c)
        if tot < bestc[0]:
            bestc = (tot, gC)
    print("PN agency (continuous Gaussian acts, sigE2=%.4f, habits fixed, one gamma_C): index = %.5f at gamma_C = %.3f" % (
        sigE2, 1 - bestc[0] / np.sum(den_c), bestc[1]))
