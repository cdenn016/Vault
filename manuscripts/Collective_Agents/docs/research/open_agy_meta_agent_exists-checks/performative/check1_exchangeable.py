r"""Check 1: exchangeable performative niche, windowed exact conditioning vs closed form.

Declared expectations (before running):
 (E1) For one niche of n members (all-to-all raw relays, exact Kalman, members read the total act,
      deterministic acts u_j = -g m_j^+), the windowed world-conditional covariance equals
      alpha (I - J/n) + v J/n with (v, alpha) from exch_closed_form, to <= 1e-8 relative, for L >= 100,
      at g = 0 and at g > 0.
 (E2) Diffusive iff v >= alpha; contrast r = v/alpha.
 (E3) A point with strong control/collider (phi_cl near 0 or s large) gives v < alpha: non-diffusive,
      positive off-diagonal entries of Pi^c equal to (1/v - 1/alpha)/n.
 Negative controls (must FAIL to match): (N1) the unconditional covariance of the beliefs' errors
      (common mode included) does not match the closed form; (N2) a closed form with the collider
      switched off (s = 0) does not match the windowed result when g > 0.
"""
import numpy as np
from pc import build_population, world_conditional_cov, exch_closed_form, diffusivity, contrast, stationary_cov


def niche_spec(n, F, Q, R, Rc, b, g):
    return {"F": [F], "Qw": [Q], "comp": [0] * n, "R": [R] * n,
            "reads": [[j for j in range(n) if j != i] for i in range(n)], "Rc": Rc,
            "act_comp": [0] * n, "g": [g] * n, "b": b, "known": [set(range(n)) for _ in range(n)],
            "model_unknown": True}


def run(n, F, Q, R, Rc, b, g, Ls=(60, 100, 160)):
    spec = niche_spec(n, F, Q, R, Rc, b, g)
    mod = build_population(spec)
    cf = exch_closed_form(n, F, Q, R, Rc, b, g)
    J = np.ones((n, n))
    Sig_cf = cf["alpha"] * (np.eye(n) - J / n) + cf["v"] * J / n
    out = []
    for L in Ls:
        Sc = world_conditional_cov(mod["A"], mod["Qx"], mod["iw"], mod["ia"], L)
        out.append((L, np.max(np.abs(Sc - Sig_cf)) / np.max(np.abs(Sig_cf))))
    Pi = np.linalg.inv(Sc)
    dif = diffusivity(Pi)
    res = {"cf": cf, "relerr": out, "dif": dif, "Pi01": Pi[0, 1], "Pi01_cf": (1 / cf["v"] - 1 / cf["alpha"]) / n}
    if dif["diffusive"]:
        res["contrast"] = contrast(Pi, list(range(n)))["r"]
    # negative controls
    # N1: unconditional covariance of errors e = m - eta
    P = stationary_cov(mod["A"], mod["Qx"])
    D = np.zeros((n, 1 + n)); D[:, 0] = -1; D[:, 1:] = np.eye(n)
    Sig_unc = D @ P @ D.T
    res["N1_relerr"] = np.max(np.abs(Sig_unc - Sig_cf)) / np.max(np.abs(Sig_cf))
    # N2: closed form without the collider (s=0)
    c0, phi, sx = cf["c0"], cf["phi_cl"], cf["sx"]
    v_nocoll = phi ** 2 * sx / (1 - (c0 * phi) ** 2)
    Sig_n2 = cf["alpha"] * (np.eye(n) - J / n) + v_nocoll * J / n
    res["N2_relerr"] = np.max(np.abs(Sc - Sig_n2)) / np.max(np.abs(Sig_cf))
    return res


if __name__ == "__main__":
    np.set_printoptions(precision=6, suppress=False)
    pts = [
        dict(n=4, F=0.9, Q=0.05, R=1.0, Rc=1.0, b=0.2, g=0.0),
        dict(n=4, F=0.9, Q=0.05, R=1.0, Rc=1.0, b=0.2, g=0.15),
        dict(n=4, F=0.9, Q=0.05, R=1.0, Rc=0.2, b=0.2, g=0.3),
        dict(n=4, F=0.9, Q=0.01, R=1.0, Rc=1.0, b=0.2, g=1.0),   # phi_cl = 0.1: strong control
        dict(n=3, F=0.8, Q=0.2, R=0.5, Rc=2.0, b=0.5, g=0.4),
    ]
    for p in pts:
        r = run(**p)
        cf = r["cf"]
        print("params", p)
        print("  phi_cl=%.4f c0=%.4f s=%.4f  v=%.6g alpha=%.6g  r=v/alpha=%.6g" % (cf["phi_cl"], cf["c0"], cf["s"], cf["v"], cf["alpha"], cf["r"]))
        print("  window rel. err vs closed form:", [(L, "%.2e" % e) for L, e in r["relerr"]])
        print("  diffusive=%s max_offdiag=%.4e  Pi01=%.6e  Pi01_cf=%.6e" % (r["dif"]["diffusive"], r["dif"]["max_offdiag"], r["Pi01"], r["Pi01_cf"]))
        if "contrast" in r:
            print("  contrast from Pi (def:col-contrast) = %.6f" % r["contrast"])
        print("  NEG N1 (unconditional cov vs closed form) rel. err = %.3e" % r["N1_relerr"])
        print("  NEG N2 (closed form with collider off vs window) rel. err = %.3e" % r["N2_relerr"])
