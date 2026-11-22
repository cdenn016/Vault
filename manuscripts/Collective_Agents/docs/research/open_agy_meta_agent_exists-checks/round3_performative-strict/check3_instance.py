r"""check3: choose the TDF instance and decide the collective clause and the exact differ clauses.

Fine scan of kappa (beta = 1, act noise s2 = 0.01, QZ = 0.05) at Rc in {0.1, 0.05}; for each kappa: window
W = (max(rbar, best non-firm region), r(C0)] in the full model.  Then at the chosen kappa*:
  * full model: all 247 regions, diffusivity, baseline (clause (c), mean coupling), selected partition at a grid of
    levels r0 inside W;
  * N_eff (exact: private-noise law), N_hab (exact: acts from habits carry no belief information, so the law equals
    N_eff's; computed independently through build(..., 'hab')), N_lp (relays deliver pure noise, acts kept):
    selected partition at the same levels with the declared comparison medium held fixed (reading R3).
Declared expectations BEFORE running:
  E1 the maximal window width is attained near the saturation point v_d = alpha (d-mode variance equal to the
     within-department disagreement variance), where the firm is a uniform clique and r(C0) = v/alpha;
  E2 at kappa*: full selects exactly {C0, C1}; N_eff and N_hab select exactly {B0, S0, B1, S1}; N_lp selects nothing;
  NEG the same selector applied at kappa = 0 (no acts) selects no firm at any level in W.
"""
import numpy as np
import lgx
from tdf import tdf_spec, groups

nd, nf = 2, 2
G = groups(nd, nf)
firms = {G["C0"], G["C1"]}


def window(spec):
    Sf = lgx.sigma_c(spec, "full", 40)
    Pf = np.linalg.inv(Sf)
    d = lgx.diffusivity(Pf)
    if not d["diffusive"]:
        return None, Sf
    rb = lgx.baseline_mean_coupling(Pf)
    allr = lgx.all_regions(Pf, top=0)
    rC = lgx.contrast(Pf, G["C0"])["r"]
    best_other = max(r for r, C, lr in allr if C not in firms)
    return (max(rb, best_other), rC, rb, best_other), Sf


def part(Pi, r0, rb):
    sel = lgx.selected(Pi, r0, rb)
    names = {v: k for k, v in G.items()}
    return [names.get(c, c) if not isinstance(c, str) else c for c in sel]


if __name__ == "__main__":
    for Rc in (0.1, 0.05):
        best = None
        print(f"--- Rc = {Rc}")
        for kap in np.round(np.arange(0.55, 0.90, 0.025), 3):
            sp = tdf_spec(nd, nf, Rc=Rc, kappa=kap)
            w, _ = window(sp)
            if w is None:
                print(f"kappa={kap:.3f}: not diffusive")
                continue
            lo, hi, rb, bo = w
            dvec = np.array([1, 1, -1, -1]) / 2
            print(f"kappa={kap:.3f}: r(C0)={hi:.4f} rbar={rb:.4f} best other={bo:.4f} width={hi - lo:+.4f}")
            if best is None or hi - lo > best[1]:
                best = (kap, hi - lo, lo, hi)
        print(f"best kappa at Rc={Rc}: {best}")
    # chosen instance: Rc = 0.1, kappa from the scan's best at Rc = 0.1 (recomputed here)
    Rc = 0.1
    cand = [(k, window(tdf_spec(nd, nf, Rc=Rc, kappa=k))[0]) for k in np.round(np.arange(0.6, 0.8, 0.005), 3)]
    cand = [(k, w) for k, w in cand if w is not None]
    kstar, wstar = max(cand, key=lambda x: x[1][1] - x[1][0])
    lo, hi, rb, bo = wstar
    print(f"\nCHOSEN kappa*={kstar}: window ({lo:.5f}, {hi:.5f}], rbar={rb:.5f}, best non-firm region={bo:.5f}")
    sp = tdf_spec(nd, nf, Rc=Rc, kappa=kstar)
    Sf = lgx.sigma_c(sp, "full", 60)
    Pf = np.linalg.inv(Sf)
    Se = lgx.sigma_private(sp, "eff")
    Sh = lgx.sigma_c(sp, "hab", 60)
    Sl = lgx.sigma_c(sp, "lp", 60)
    print(f"|Sigma_hab - Sigma_eff|max = {np.max(np.abs(Sh - Se)):.2e} (expect ~0)")
    al = lambda S: float(np.array([1, -1, 0, 0]) / np.sqrt(2) @ S[:4, :4] @ np.array([1, -1, 0, 0]) / np.sqrt(2))
    dv = lambda S: float(np.array([1, 1, -1, -1]) / 2 @ S[:4, :4] @ np.array([1, 1, -1, -1]) / 2)
    print(f"within-dept disagreement var alpha={al(Sf):.6f}; d-mode var full={dv(Sf):.6f}, eff={dv(Se):.6f}")
    print(f"full: diffusive {lgx.diffusivity(Pf)}; Pi on firm 0:\n{np.array2string(Pf[:4, :4], precision=3)}")
    print("full top regions:", [(round(r, 4), C) for r, C, lr in lgx.all_regions(Pf, top=6)])
    levels = np.linspace(lo, hi, 6)[1:]
    for name, S in (("full", Sf), ("N_eff", Se), ("N_hab", Sh), ("N_lp", Sl)):
        P = np.linalg.inv(S)
        dd = lgx.diffusivity(P)
        tops = [(round(r, 4), C) for r, C, lr in lgx.all_regions(P, top=4)] if dd["diffusive"] else "n/a"
        print(f"{name}: diffusive={dd['diffusive']}; top regions {tops}")
        for r0 in levels:
            print(f"    r0={r0:.4f}: selected {part(P, r0, rb)}")
    S0 = lgx.sigma_c(tdf_spec(nd, nf, Rc=Rc, kappa=0.0), "full", 40)
    P0 = np.linalg.inv(S0)
    print(f"NEG kappa=0: r(C0)={lgx.contrast(P0, G['C0'])['r']:.4f}; selected at r0={levels[2]:.4f}: "
          f"{part(P0, levels[2], rb)}")
