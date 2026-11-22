r"""check2: scan of the two-department firm (TDF) in the act strength kappa (beta = 1).

Declared expectations BEFORE running (from the symmetry argument: acts pin only the between-department mode d):
  E1  under N_eff (= kappa 0 law) the firm C has r = 1 (departments uncorrelated) and the departments carry the
      relay contrast r_eff(B) = v/alpha;
  E2  full model: Sigma_full differs from Sigma_eff only on the d-mode of each firm (within-department and firm
      collective eigenvalues unchanged to 1e-10);
  E3  r_full(C) = min(v/alpha, v/v_d) <= r_eff(B), increasing in kappa until diffusivity fails at
      1/v_d > 2/alpha - 1/v (nd = 2);
  E4  there are kappa with a nonempty window (max(rbar, r(B), other regions), r(C)] in the full model;
  NEG kappa = 0: r(C) = 1 exactly (the firm is not a collective without acts).
"""
import numpy as np
import lgx
from tdf import tdf_spec, analyze, groups

nd, nf = 2, 2
base = dict(F=0.9, Q=0.05, R=1.0, Rc=0.1, qc=1e-4, beta=1.0, sa2=0.01, QZ=0.05, h=1.0)

if __name__ == "__main__":
    Se = lgx.sigma_private(tdf_spec(nd, nf, kappa=0.0, **base), "eff")
    ae = analyze(None, nd, nf, Sig=Se)
    v_al = ae["r"]["B0"]
    print(f"N_eff (kappa-independent): r(B0)={ae['r']['B0']:.6f} r(C0)={ae['r']['C0']:.6f} rbar_eff={ae['rbar']:.4f}")
    # eigen-structure on firm 0
    C0 = list(groups(nd, nf)["C0"])
    dvec = np.array([1, 1, -1, -1]) / 2.0
    wvec = np.array([1, -1, 0, 0]) / np.sqrt(2)
    cvec = np.ones(4) / 2.0
    for kap in [0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.5, 2.0, 3.0]:
        sp = tdf_spec(nd, nf, kappa=kap, **base)
        Sf = lgx.sigma_c(sp, "full", 40)
        a = analyze(sp, nd, nf, Sig=Sf)
        SC = Sf[np.ix_(C0, C0)]
        SCe = Se[np.ix_(C0, C0)]
        ev = lambda S, x: float(x @ S @ x)
        line = (f"kappa={kap:4.2f}: d-var {ev(SC, dvec):.6f} (eff {ev(SCe, dvec):.6f}); w-var diff "
                f"{ev(SC, wvec) - ev(SCe, wvec):+.1e}; c-var diff {ev(SC, cvec) - ev(SCe, cvec):+.1e}; "
                f"cross(B,S) {SC[0, 2]:+.3e}")
        print(line)
        if a["diff"]["diffusive"]:
            r = a["r"]
            others = [x for x in a["top"] if x[1] not in (groups(nd, nf)["C0"], groups(nd, nf)["C1"])]
            print(f"    diffusive: r(C0)={r['C0']:.4f} r(B0)={r['B0']:.4f} r(S0)={r['S0']:.4f} rbar={a['rbar']:.4f} "
                  f"next region {others[0][0]:.4f} {others[0][1]}; window "
                  f"({max(a['rbar'], others[0][0]):.4f}, {r['C0']:.4f}]; v/alpha (N_eff dept) = {v_al:.4f}")
        else:
            print(f"    NOT diffusive: max off {a['diff']['max_off']:.3e}, min row {a['diff']['min_row']:.3e}")
