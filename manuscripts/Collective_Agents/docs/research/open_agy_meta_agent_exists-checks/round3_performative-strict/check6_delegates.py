r"""check6: TDF with one acting delegate per department (members 0 and 2 of each firm act, 1 and 3 do not).

Motivation (proved fact used in the design): with a rank-one act functional, every pair of acting members with
loadings of one sign receives a repulsive increment; with only two actors of opposite sign per firm there is no such
pair, so the deletion nulls and partner randomization can stay diffusive.
Declared expectations BEFORE running (no prediction on the window; the firm graph is now path-like):
  E1 N_lp (relays deliver noise, acts kept) is diffusive for every kappa (no repulsive pair);
  E2 whether a window (rbar, r(C0)] with the firm selected exists: no prediction.
"""
import numpy as np
import lgx
from tdf import tdf_spec, groups

nd, nf = 2, 2
G = groups(nd, nf)
firms = {G["C0"], G["C1"]}


def deleg_spec(kappa, Rc=0.1, nd=2, nf=2, **kw):
    sp = tdf_spec(nd, nf, Rc=Rc, kappa=kappa, **kw)
    for f in range(nf):
        for dep in range(2):
            for r in range(1, nd):
                sp["agents"][2 * nd * f + nd * dep + r]["kappa"] = 0.0
    return sp


if __name__ == "__main__":
    for Rc in (0.1, 0.02):
        print(f"--- Rc = {Rc}")
        for kap in [0.3, 0.6, 1.0, 1.5, 2.0, 3.0, 5.0, 8.0]:
            sp = deleg_spec(kap, Rc=Rc)
            Pf = np.linalg.inv(lgx.sigma_c(sp, "full", 40))
            df = lgx.diffusivity(Pf)
            Pl = np.linalg.inv(lgx.sigma_c(sp, "lp", 40))
            dl = lgx.diffusivity(Pl)
            if not df["diffusive"]:
                print(f"kappa={kap}: full not diffusive (max off {df['max_off']:.3f}); N_lp diffusive={dl['diffusive']}")
                continue
            rb = lgx.baseline_mean_coupling(Pf)
            allr = lgx.all_regions(Pf, top=0)
            rC = lgx.contrast(Pf, G["C0"])["r"]
            bo = max(r for r, C, lr in allr if C not in firms)
            boC = [C for r, C, lr in allr if C not in firms][0]
            print(f"kappa={kap}: r(C0)={rC:.4f} rbar={rb:.4f} best other={bo:.4f} {boC} width={rC - max(rb, bo):+.4f}; "
                  f"N_lp diffusive={dl['diffusive']}")
