r"""check15b: CCP under common declared coordinates c = (cos t, sin t), 36 directions (run inline originally; output
check15b_out.txt).  No expectation declared (exploratory)."""
import numpy as np, lgx, lgx2
from check13_ccp_scan import ccp_spec, PAIRS
sp = ccp_spec(0.5, 0.1, 0.7, sa2=0.01)
res = {}
for null in ("full", "eff", "lp"):
    mod = lgx2.build2(sp, null); im = mod["i_m"]; N = mod["N"]
    ia = [x for i in range(N) for x in (im(i)[0], im(i)[1])]
    if null == "eff":
        idx = mod["private_idx"]; A = mod["A"][np.ix_(idx, idx)]; Gp = mod["G"][np.ix_(idx, mod["noise_private"])]
        P = lgx.stat_cov(A, Gp @ Gp.T); sel = [idx.index(i) for i in ia]; res[null] = P[np.ix_(sel, sel)]
    else:
        res[null] = lgx.window_cond_cov(mod["A"], mod["Qx"], mod["iw"], ia, 60)
ok = 0
for th in np.linspace(0, np.pi, 37)[:-1]:
    c = np.array([np.cos(th), np.sin(th)]); T = np.kron(np.eye(4), c)
    Pf = np.linalg.inv(T @ res["full"] @ T.T); d = lgx.diffusivity(Pf)
    if not d["diffusive"]:
        print(f"theta={np.degrees(th):6.1f}: full not diffusive"); continue
    rb = lgx.baseline_mean_coupling(Pf); rP = lgx.contrast(Pf, (0, 1))["r"]
    Pe = np.linalg.inv(T @ res["eff"] @ T.T); Pl = np.linalg.inv(T @ res["lp"] @ T.T)
    re = lgx.contrast(Pe, (0, 1))["r"] if lgx.diffusivity(Pe)["diffusive"] else np.nan
    rl = lgx.contrast(Pl, (0, 1))["r"] if lgx.diffusivity(Pl)["diffusive"] else np.nan
    bo = max(r for r, C, _ in lgx.all_regions(Pf, top=0) if C not in PAIRS)
    lo = np.nanmax([rb, bo, re, rl]); w = rP > lo; ok += w
    print(f"theta={np.degrees(th):6.1f}: r(pair)={rP:.3f} rbar={rb:.3f} r_eff={re:.3f} r_lp={rl:.3f} window={'yes' if w else 'no'}")
print(f"common directions with a nonempty window (N_eff, N_lp below, baseline below): {ok}/36")
