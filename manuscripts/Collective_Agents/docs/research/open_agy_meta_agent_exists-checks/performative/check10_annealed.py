r"""Check 10: annealed habit null for PN (attention redrawn every round, acts from habits = no feedback,
habit act noise conditioned or absent) by Monte Carlo, and the mechanism baseline M1 by closed form.

(1) N_hab annealed: niche A of 4 agents among 8; each round each agent reads 3 of the other 7 uniformly;
    only niche-mates are informative; exact Kalman filters with time-varying gains.  With the world path
    fixed (exogenous under N_hab), E[Cov(e(T)|eta)] is estimated across replicas (private noises and
    attention vary), averaged over world paths.  Contrast of the niche block from Lemma E (compound
    symmetric part of the estimate).  Declared expectation: r_hab roughly 4-5 (rough fixed-gain estimate 4.5).
    Negative control: attention fixed to all niche-mates reproduces r_0 = 28.5 (no acts) within MC error.
(2) M1 baseline (exchangeable state of the attention mechanism: all 8 agents in one niche, 3 random partners
    per round, constant gains, all 8 act and read the total act): closed form with second-moment noise
    covariance; declared expectation about 2.7 (with collider, Gaussian approximation) and 2.78 without.
"""
import numpy as np
from pc import riccati_scalar

F, Q, R, Rc, b, g = 0.9, 0.05, 1.0, 0.2, 0.2, 0.15


def mc_niche(fixed_attention, reps=20000, T=80, paths=5, seed=3):
    rng = np.random.default_rng(seed)
    n = 4
    covs = []
    for p in range(paths):
        w = rng.standard_normal(T) * np.sqrt(Q)
        eta = np.zeros(T + 1)
        eta[0] = rng.standard_normal() * np.sqrt(Q / (1 - F * F))
        for t in range(T):
            eta[t + 1] = F * eta[t] + w[t]
        m = np.zeros((reps, n)) + eta[0] + rng.standard_normal((reps, n)) * np.sqrt(Q / (1 - F * F))
        Pm = np.full((reps, n), Q / (1 - F * F))
        others = np.array([[j for j in range(8) if j != i] for i in range(n)])  # (4,7)
        for t in range(T):
            v = rng.standard_normal((reps, n)) * np.sqrt(R)  # sensing noise of niche-A agents (only they matter)
            s = eta[t] + v
            if fixed_attention:
                useful = np.ones((reps, n, n), bool) & ~np.eye(n, dtype=bool)[None]
            else:
                # each agent picks 3 of its 7 others: random permutation, take first 3
                keys = rng.random((reps, n, 7))
                pick = np.argsort(keys, axis=2)[:, :, :3]
                chosen = np.take_along_axis(np.broadcast_to(others[None], (reps, n, 7)), pick, axis=2)  # (reps,n,3)
                useful = np.zeros((reps, n, n), bool)
                for c in range(3):
                    idx = chosen[:, :, c]
                    for j in range(n):
                        useful[:, :, j] |= (idx == j)
            k = useful.sum(axis=2)
            Pp = 1.0 / (1.0 / Pm + 1.0 / R + k / (R + Rc))
            Ks = Pp / R; Kc = Pp / (R + Rc)
            nu = rng.standard_normal((reps, n, n)) * np.sqrt(Rc)
            relay = (useful * (s[:, None, :] + nu - m[:, :, None])).sum(axis=2)
            mplus = m + Ks * (s - m) + Kc * relay
            m = F * mplus
            Pm = F * F * Pp + Q
        e = m - eta[T]
        covs.append(np.cov(e.T))
    S = np.mean(covs, axis=0)
    n = 4
    diag = np.mean(np.diag(S)); off = (S.sum() - np.trace(S)) / (n * (n - 1))
    alpha = diag - off; v = alpha + n * off
    return v / alpha, S


def m1_baseline():
    Pm, Pp = riccati_scalar(F, Q, 1 / R + 3 / (R + Rc))
    Ks, Kc = Pp / R, Pp / (R + Rc); c0 = Pp / Pm
    N = 8
    a = Ks ** 2 * R + 3 * Kc ** 2 * (R + Rc)
    c = 2 * Ks * Kc * R * (3 / 7) + Kc ** 2 * R * 6 * (3 / 7) ** 2
    sx, sp = a + (N - 1) * c, a - c
    phi = F - b * g * N; rho = c0 * phi; s = sx * b * b * g * g * N / Q
    v_coll = phi ** 2 * sx / np.sqrt((1 + rho ** 2 + s) ** 2 - 4 * rho ** 2)
    v_nocoll = phi ** 2 * sx / (1 - rho ** 2)
    alpha = F ** 2 * sp / (1 - F ** 2 * c0 ** 2)
    return v_coll / alpha, v_nocoll / alpha, sx / sp


if __name__ == "__main__":
    r_fix, S_fix = mc_niche(True)
    print("NEG control (attention fixed on niche-mates, no acts): MC r = %.3f (exact 28.5)" % r_fix)
    r_hab, S_hab = mc_niche(False)
    print("N_hab annealed (exact time-varying filters, no acts): MC r_hab = %.3f" % r_hab)
    print("   second-moment block:\n", np.array2string(S_hab, precision=5))
    rc, rn, r0h = m1_baseline()
    print("M1 mechanism baseline (Gaussian second-moment approx.): with collider %.4f, without %.4f, no-act %.4f" % (rc, rn, r0h))
