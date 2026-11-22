r"""Check 11: grade of PN as a function of the act gain g, against the mechanism baseline M1.

For g in {0.05, 0.10, 0.15}: r(A) (closed form), r_sub = (3r+1)/(r+3) (n=4), M1 baseline (Gaussian
second-moment approximation, with collider), mean-coupling baseline, r_eff (N_eff), annealed N_hab
contrast (MC, g-independent: no acts), annealed N_pr contrast (MC with exact time-varying filters and the
act feedback of members reading their niche's realized total act, world path exogenous: collider
ignored, which can only overstate the null's collective-mode variance in the exchangeable approximation).
Declared expectations: for small g the M1 baseline exceeds both annealed null contrasts, so that at every
admissible level of the window (max(r_sub, M1), r(A)] neither annealed null selects {A,B}.
"""
import numpy as np
from pc import exch_closed_form, riccati_scalar
from check10_annealed import m1_baseline as _m1

F, Q, R, Rc, b, n = 0.9, 0.05, 1.0, 0.2, 0.2, 4


def m1(g):
    Pm, Pp = riccati_scalar(F, Q, 1 / R + 3 / (R + Rc))
    Ks, Kc = Pp / R, Pp / (R + Rc); c0 = Pp / Pm
    N = 8
    a = Ks ** 2 * R + 3 * Kc ** 2 * (R + Rc)
    c = 2 * Ks * Kc * R * (3 / 7) + Kc ** 2 * R * 6 * (3 / 7) ** 2
    sx, sp = a + (N - 1) * c, a - c
    phi = F - b * g * N; rho = c0 * phi; s = sx * b * b * g * g * N / Q
    v = phi ** 2 * sx / np.sqrt((1 + rho ** 2 + s) ** 2 - 4 * rho ** 2)
    return v / (F ** 2 * sp / (1 - F ** 2 * c0 ** 2))


def mc_pr(g, reps=20000, T=80, paths=5, seed=11):
    rng = np.random.default_rng(seed)
    covs = []
    others = np.array([[j for j in range(8) if j != i] for i in range(n)])
    for p in range(paths):
        w = rng.standard_normal(T) * np.sqrt(Q)
        eta = np.zeros(T + 1); eta[0] = rng.standard_normal() * np.sqrt(Q / (1 - F * F))
        for t in range(T):
            eta[t + 1] = F * eta[t] + w[t]   # exogenous world path (collider ignored)
        m = eta[0] + rng.standard_normal((reps, n)) * np.sqrt(Q / (1 - F * F))
        Pm = np.full((reps, n), Q / (1 - F * F))
        for t in range(T):
            s = eta[t] + rng.standard_normal((reps, n)) * np.sqrt(R)
            keys = rng.random((reps, n, 7))
            chosen = np.take_along_axis(np.broadcast_to(others[None], (reps, n, 7)), np.argsort(keys, axis=2)[:, :, :3], axis=2)
            useful = np.zeros((reps, n, n), bool)
            for cc in range(3):
                for j in range(n):
                    useful[:, :, j] |= (chosen[:, :, cc] == j)
            k = useful.sum(axis=2)
            Pp = 1.0 / (1.0 / Pm + 1.0 / R + k / (R + Rc))
            Ks = Pp / R; Kc = Pp / (R + Rc)
            nu = rng.standard_normal((reps, n, n)) * np.sqrt(Rc)
            mplus = m + Ks * (s - m) + Kc * (useful * (s[:, None, :] + nu - m[:, :, None])).sum(axis=2)
            U = -g * mplus.sum(axis=1, keepdims=True)  # realized niche total act, read by all members
            m = F * mplus + b * U
            Pm = F * F * Pp + Q
        covs.append(np.cov((m - (eta[T] if False else 0.0)).T))
    S = np.mean(covs, axis=0)
    diag = np.mean(np.diag(S)); off = (S.sum() - np.trace(S)) / (n * (n - 1))
    al = diag - off
    return (al + n * off) / al


if __name__ == "__main__":
    r_hab = 4.409  # check 10 (MC, g-independent)
    for g in [0.05, 0.10, 0.15]:
        cf = exch_closed_form(n, F, Q, R, Rc, b, g)
        r = cf["r"]; rsub = (3 * r + 1) / (r + 3)
        rbar_mc = 1 + 2 * (n - 1) * (r - 1) / (2 * n - 1)
        rM1 = m1(g)
        phi, c0, sx = cf["phi_cl"], cf["c0"], cf["sx"]
        r_eff = (phi ** 2 * sx / (1 - (c0 * phi) ** 2)) / cf["alpha"]
        r_pr = mc_pr(g)
        lo = max(rsub, rM1)
        print("g=%.2f r(A)=%.4f r_sub=%.4f M1=%.4f meancoupling=%.4f window=(%.4f, %.4f]  r_eff=%.4f  r_hab(annealed)=%.3f  r_pr(annealed, no collider)=%.3f  every-constant vs N_hab: %s, vs N_pr: %s" % (
            g, r, rsub, rM1, rbar_mc, lo, r, r_eff, r_hab, r_pr, "pass" if r_hab <= lo else "fail on (%.3f, %.3f]" % (lo, min(r_hab, r)),
            "pass" if r_pr <= lo else "fail on (%.3f, %.3f]" % (lo, min(r_pr, r))))
