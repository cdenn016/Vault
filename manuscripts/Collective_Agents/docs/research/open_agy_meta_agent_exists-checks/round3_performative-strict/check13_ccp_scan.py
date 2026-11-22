r"""check13: validation of lgx2 and scan of the correlated-component pair (CCP).

CCP population: two firms; firm f has b_f sensing eta^{3f} ('revenue') and s_f sensing eta^{3f+1} ('cost'), the two
AR(1) components having innovation correlation rho; each member models both components jointly and reads the other's
raw reading (literal latency, Rc).  Both regulate the renewed outcome eta^{3f+2} = h(eta^{3f} - eta^{3f+1})
+ beta (u_b + u_s) + w^Z with a COMMON preference (target 0), D2 act rule u_j = -kappa (m^+_{j,3f} - m^+_{j,3f+1}) + a_j.
Contrast coordinates: each member's prior error about its own sensed component.
Declared expectations BEFORE running:
  VAL lgx2 with single-component beliefs reproduces lgx on the TDF instance (max abs diff < 1e-10);
  E1  N_lp is diffusive at every point (two actors per firm, opposite loadings on the contrast coordinates);
  E2  no prediction on whether a window (max(rbar, r_eff, r_lp, others), r(pair)] exists.
"""
import numpy as np
import lgx
import lgx2
from tdf import tdf_spec

PAIRS = {(0, 1), (2, 3)}


def ccp_spec(rho, Rc, kappa, nf=2, F=0.9, Q=0.05, R=1.0, qc=1e-4, QZ=0.05, sa2=0.01, h=1.0, beta=1.0):
    K = 3 * nf
    Fw = np.zeros((K, K)); Qw = np.zeros((K, K)); ag = []
    for f in range(nf):
        a, b, z = 3 * f, 3 * f + 1, 3 * f + 2
        Fw[a, a] = Fw[b, b] = F; Fw[z, a] = h; Fw[z, b] = -h
        Qw[np.ix_([a, b], [a, b])] = Q * np.array([[1.0, rho], [rho, 1.0]]); Qw[z, z] = QZ
        base = len(ag)
        for r, k in enumerate((a, b)):
            ag.append({"M": [a, b], "k": k, "R": R, "senders": [base + 1 - r], "kap": {a: kappa, b: -kappa},
                       "Z": z, "beta": beta, "sa2": sa2})
    return {"Fw": Fw, "Qw": Qw, "Rc": Rc, "qc": qc, "agents": ag}


def evaluate(sp, L=40):
    Pf = np.linalg.inv(lgx2.sigma_c2(sp, "full", L))
    if not lgx.diffusivity(Pf)["diffusive"]:
        return None
    Pe = np.linalg.inv(lgx2.sigma_private2(sp, "eff"))
    Pl = np.linalg.inv(lgx2.sigma_c2(sp, "lp", L))
    rb = lgx.baseline_mean_coupling(Pf)
    rP = lgx.contrast(Pf, (0, 1))["r"]
    bo = max(r for r, C, _ in lgx.all_regions(Pf, top=0) if C not in PAIRS)
    re = lgx.contrast(Pe, (0, 1))["r"] if lgx.diffusivity(Pe)["diffusive"] else np.nan
    dl = lgx.diffusivity(Pl)["diffusive"]
    rl = lgx.contrast(Pl, (0, 1))["r"] if dl else np.nan
    lo = np.nanmax([rb, bo, re, rl])
    return dict(rP=rP, rb=rb, bo=bo, re=re, rl=rl, dl=dl, lo=lo, Pf=Pf, Pe=Pe, Pl=Pl,
                de=lgx.diffusivity(Pe)["diffusive"])


if __name__ == "__main__":
    # validation against lgx on the TDF instance
    sp1 = tdf_spec(2, 2, kappa=0.68)
    sp2 = {"Fw": sp1["Fw"], "Qw": np.diag(sp1["Qw"]), "Rc": sp1["Rc"], "qc": sp1["qc"],
           "agents": [{"M": [a["k"]], "k": a["k"], "R": a["R"], "senders": a["senders"], "kap": {a["k"]: a["kappa"]},
                       "Z": a["Z"], "beta": a["beta"], "sa2": a["sa2"]} for a in sp1["agents"]]}
    for null in ("full", "lp"):
        d = np.max(np.abs(lgx2.sigma_c2(sp2, null, 40) - lgx.sigma_c(sp1, null, 40)))
        print(f"VAL {null}: max|lgx2 - lgx| = {d:.2e}")
    print(f"VAL eff: {np.max(np.abs(lgx2.sigma_private2(sp2) - lgx.sigma_private(sp1, 'eff'))):.2e}")
    best = None
    for rho in (0.5, 0.8, 0.95):
        for Rc in (0.1, 0.3, 1.0):
            for kap in (0.2, 0.4, 0.7, 1.0, 1.5, 2.0):
                ev = evaluate(ccp_spec(rho, Rc, kap))
                if ev is None:
                    print(f"rho={rho} Rc={Rc} kappa={kap}: full not diffusive"); continue
                w = ev["rP"] - ev["lo"]
                print(f"rho={rho:4.2f} Rc={Rc:3.1f} kappa={kap:3.1f}: r(pair)={ev['rP']:.4f} rbar={ev['rb']:.4f} "
                      f"r_eff={ev['re']:.4f} r_lp={ev['rl']:.4f} (N_lp dif {ev['dl']}, N_eff dif {ev['de']}) "
                      f"other={ev['bo']:.4f} width={w:+.4f}")
                if best is None or w > best[0]:
                    best = (w, rho, Rc, kap)
    print(f"best: {best}")
