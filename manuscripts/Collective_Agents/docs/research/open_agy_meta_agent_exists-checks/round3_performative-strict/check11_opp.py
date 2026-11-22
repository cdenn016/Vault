r"""check11: opposite-preference pairs with relays (OPP), a candidate in which every null stays diffusive.

Population: two pairs; pair f = {b_f, s_f} senses world component f (AR(1), F, Q), its members relay raw readings to
each other (literal latency, Rc), and both act on a renewed outcome eta^{2+f} = beta (u_b + u_s) + w^Z.  Preferences
(Proposition E forces opposite maps for opposite signs on one component): b prefers eta^{2+f}_{t+1} = +h eta^f_{t+1},
s prefers eta^{2+f}_{t+1} = -h eta^f_{t+1}; D2 act rule u_j ~ N(-gamma Lam beta s2 z_j, s2) with z_b = -h F m_b^+,
z_s = +h F m_s^+, i.e. lgx kappa_b = -gamma Lam beta s2 h F, kappa_s = -kappa_b.
Every coupling is attractive (two actors of opposite sign), so N_lp, N_rn, N_fr stay diffusive (no same-sign pair).
Declared expectations BEFORE running:
  E1 some (kappa, Rc) give a level r0 with r(pair) >= r0 > max(rbar, r_eff(pair), r_lp(pair)) (relays alone and the
     collider alone both below the baseline): no strong prediction, the static estimate says yes when the two
     mechanisms contribute comparable couplings;
  E2 at such an instance N_eff, N_hab and N_lp select nothing and are diffusive.
"""
import numpy as np
import lgx

F, Q, R, qc, QZ, beta = 0.9, 0.05, 1.0, 1e-4, 0.05, 1.0


def opp_spec(kappa, Rc, sa2=0.01, R=R, F=F, Q=Q, qc=qc, QZ=QZ):
    Fw = np.zeros((4, 4)); Fw[0, 0] = Fw[1, 1] = F
    ag = []
    for f in range(2):
        for r, sg in ((0, 1.0), (1, -1.0)):
            ag.append({"k": f, "R": R, "senders": [2 * f + 1 - r], "kappa": sg * kappa, "Z": 2 + f, "beta": beta,
                       "sa2": sa2, "readacts": []})
    return {"Fw": Fw, "Qw": [Q, Q, QZ, QZ], "Rc": Rc, "qc": qc, "agents": ag}


PAIRS = {(0, 1), (2, 3)}


def evaluate(kappa, Rc, L=40):
    sp = opp_spec(kappa, Rc)
    Pf = np.linalg.inv(lgx.sigma_c(sp, "full", L))
    if not lgx.diffusivity(Pf)["diffusive"]:
        return None
    Pe = np.linalg.inv(lgx.sigma_private(sp, "eff"))
    Pl = np.linalg.inv(lgx.sigma_c(sp, "lp", L))
    rb = lgx.baseline_mean_coupling(Pf)
    rP = lgx.contrast(Pf, (0, 1))["r"]
    bo = max(r for r, C, _ in lgx.all_regions(Pf, top=0) if C not in PAIRS)
    re = lgx.contrast(Pe, (0, 1))["r"]
    rl = lgx.contrast(Pl, (0, 1))["r"] if lgx.diffusivity(Pl)["diffusive"] else np.nan
    return dict(rP=rP, rb=rb, bo=bo, re=re, rl=rl, lo=max(rb, bo, re, rl), Pf=Pf, Pe=Pe, Pl=Pl,
                dl=lgx.diffusivity(Pl)["diffusive"])


if __name__ == "__main__":
    best = None
    for Rc in (0.3, 1.0, 3.0, 10.0):
        for kap in (0.2, 0.4, 0.6, 0.8, 1.0, 1.3, 1.6, 2.0):
            ev = evaluate(kap, Rc)
            if ev is None:
                print(f"Rc={Rc} kappa={kap}: full not diffusive"); continue
            w = ev["rP"] - ev["lo"]
            print(f"Rc={Rc:5.1f} kappa={kap:3.1f}: r(pair)={ev['rP']:.4f} rbar={ev['rb']:.4f} r_eff={ev['re']:.4f} "
                  f"r_lp={ev['rl']:.4f} (N_lp diffusive {ev['dl']}) other={ev['bo']:.4f} width={w:+.4f}")
            if best is None or w > best[0]:
                best = (w, Rc, kap)
    print(f"best: {best}")
