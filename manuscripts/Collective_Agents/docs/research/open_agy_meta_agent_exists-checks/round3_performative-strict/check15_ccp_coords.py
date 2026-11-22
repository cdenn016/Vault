r"""check15: dependence of the CCP verdict on the declared scalar contrast coordinate (members hold 2-d beliefs).
Declarations: 'own' (each member's prior error about the component it senses; used in check14), 'a' (every member's
error about eta^a), 'b' (about eta^b), 'diff' (about eta^a - eta^b, the outcome-relevant combination).
Declared expectation BEFORE running: 'own' reproduces check14; 'diff' fails (the acts reveal the collective mode of
that coordinate, so contrast falls); no prediction for 'a' and 'b'.
"""
import numpy as np, lgx, lgx2
from check13_ccp_scan import ccp_spec, PAIRS
sp = ccp_spec(0.5, 0.1, 0.7, sa2=0.01)
res = {}
for null in ("full", "eff", "lp", "hab"):
    mod = lgx2.build2(sp, null)
    im = mod["i_m"]; N = mod["N"]
    ia = [x for i in range(N) for x in (im(i)[0], im(i)[1])]
    if null == "eff":
        idx = mod["private_idx"]; A = mod["A"][np.ix_(idx, idx)]
        Gp = mod["G"][np.ix_(idx, mod["noise_private"])]
        P = lgx.stat_cov(A, Gp @ Gp.T); sel = [idx.index(i) for i in ia]; S = P[np.ix_(sel, sel)]
    else:
        S = lgx.window_cond_cov(mod["A"], mod["Qx"], mod["iw"], ia, 60)
    res[null] = S
own = np.zeros((4, 8)); a = np.zeros((4, 8)); b = np.zeros((4, 8)); dif = np.zeros((4, 8))
for i in range(4):
    own[i, 2 * i + (0 if i % 2 == 0 else 1)] = 1.0
    a[i, 2 * i] = 1.0; b[i, 2 * i + 1] = 1.0; dif[i, 2 * i] = 1.0; dif[i, 2 * i + 1] = -1.0
for name, T in (("own", own), ("a", a), ("b", b), ("diff", dif)):
    Pf = np.linalg.inv(T @ res["full"] @ T.T)
    d = lgx.diffusivity(Pf)
    line = f"{name:5s}: full diffusive={d['diffusive']}"
    if d["diffusive"]:
        rb = lgx.baseline_mean_coupling(Pf); rP = lgx.contrast(Pf, (0, 1))["r"]
        nul = {}
        for nn in ("eff", "lp", "hab"):
            Pn = np.linalg.inv(T @ res[nn] @ T.T)
            nul[nn] = lgx.contrast(Pn, (0, 1))["r"] if lgx.diffusivity(Pn)["diffusive"] else float("nan")
        bo = max(r for r, C, _ in lgx.all_regions(Pf, top=0) if C not in PAIRS)
        lo = max(rb, bo, *[v for v in nul.values() if v == v])
        line += (f"; r(pair)={rP:.4f} rbar={rb:.4f} others={bo:.4f} nulls {', '.join(f'{k}={v:.4f}' for k, v in nul.items())}"
                 f"; window ({lo:.4f}, {rP:.4f}] nonempty={rP > lo}")
    else:
        line += f" (max off {d['max_off']:+.3f})"
    print(line)
