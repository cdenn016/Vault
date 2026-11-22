r"""check9: (i) +-5% box for the pure-collider pair; (ii) Proposition D on the TDF deletion null.

(i) Box over (F, Q, R, qc, kappa, s2, QZ) with a 2^(7-3) design plus centre (17 points); per point the local window
    (rbar, r(pair)], whether N_eff/N_hab select nothing, and the common-level intersection.
    Declared expectation BEFORE running: every local window nonempty and a common level exists at +-5%.
(ii) Proposition D: under N_lp the two members of a department are uncorrelated and interchangeable in the private law
    and the path carries information about them, so their world-conditional covariance equals -|K_i|^2 < 0.
    Declared expectation BEFORE running: Sigma_lp[0,1] < 0 and equals -(Sigma_eff,lp - Sigma_lp)[0,1]... i.e. the
    covariance correction between members 0 and 1 equals the correction's diagonal entry (K_0 = K_1); NEG: under the
    full model (relays present) Sigma[0,1] > 0.
"""
import numpy as np
import lgx
from tdf import tdf_spec, groups

c0 = dict(F=0.9, Q=0.05, R=1.0, qc=1e-4, kappa=0.68, s2=0.01, QZ=0.05)
keys = list(c0)
G1 = groups(1, 2)


def design(hw):
    pts = [dict(c0)]
    for a in (-1, 1):
        for b in (-1, 1):
            for c in (-1, 1):
                for d in (-1, 1):
                    lv = [a, b, c, d, a * b * c, b * c * d, a * c * d]
                    pts.append({k: c0[k] * (1 + hw * s) for k, s in zip(keys, lv)})
    return pts


if __name__ == "__main__":
    los, his, ok = [], [], 0
    for idx, p in enumerate(design(0.05)):
        sp = tdf_spec(1, 2, F=p["F"], Q=p["Q"], R=p["R"], qc=p["qc"], kappa=p["kappa"], sa2=p["s2"], QZ=p["QZ"])
        Pf = np.linalg.inv(lgx.sigma_c(sp, "full", 40))
        Pe = np.linalg.inv(lgx.sigma_private(sp, "eff"))
        Ph = np.linalg.inv(lgx.sigma_c(sp, "hab", 40))
        rb = lgx.baseline_mean_coupling(Pf)
        rP = lgx.contrast(Pf, G1["C0"])["r"]
        bo = max(r for r, C, _ in lgx.all_regions(Pf, top=0) if C not in (G1["C0"], G1["C1"]))
        lo = max(rb, bo)
        los.append(lo); his.append(rP)
        mid = 0.5 * (lo + rP)
        good = (lgx.diffusivity(Pf)["diffusive"] and rP > lo
                and set(lgx.selected(Pf, mid, rb)) == {G1["C0"], G1["C1"]}
                and lgx.selected(Pe, mid, rb) == [] and lgx.selected(Ph, mid, rb) == [])
        ok += good
        print(f"pt{idx:2d}: window ({lo:.4f}, {rP:.4f}] full/N_eff/N_hab verdict at local midpoint ok={good}")
    print(f"pair box +-5%: {ok}/17 points ok; intersection ({max(los):.4f}, {min(his):.4f}] "
          f"nonempty={min(his) > max(los)}")
    # (ii) Proposition D on the TDF instance
    sp = tdf_spec(2, 2, kappa=0.68)
    S_lp = lgx.sigma_c(sp, "lp", 60)
    S_lp_priv = lgx.sigma_private(sp, "lp")
    corr = S_lp_priv - S_lp
    S_full = lgx.sigma_c(sp, "full", 60)
    print(f"Prop D: N_lp private law Cov(0,1) = {S_lp_priv[0, 1]:.2e} (expect 0); correction diag {corr[0, 0]:.6e}, "
          f"correction (0,1) {corr[0, 1]:.6e}; Sigma_lp(0,1) = {S_lp[0, 1]:.6e} (expect < 0)")
    print(f"NEG: full model Sigma(0,1) = {S_full[0, 1]:.6e} (expect > 0)")
