r"""check16: CCP under the common declared coordinate e^a + e^b (direction 45 degrees), declared before this run.
Expectations declared BEFORE running: N_pr annealed (zero-gain, p = 1/3) diffusive with r(pair) below 5.261 (the N_eff
value that sets the window's lower edge); +-1% box: common level with full = pairs and N_eff, N_hab, N_lp = nothing at
17/17 points."""
import numpy as np, lgx, lgx2
from check13_ccp_scan import ccp_spec, PAIRS
import check8_box as cb
c = np.array([1.0, 1.0]) / np.sqrt(2)


def all_cov(sp, null, L=40):
    mod = lgx2.build2(sp, null); im = mod["i_m"]; N = mod["N"]
    ia = [x for i in range(N) for x in (im(i)[0], im(i)[1])]
    if null == "eff":
        idx = mod["private_idx"]; A = mod["A"][np.ix_(idx, idx)]; Gp = mod["G"][np.ix_(idx, mod["noise_private"])]
        P = lgx.stat_cov(A, Gp @ Gp.T); sel = [idx.index(i) for i in ia]; return P[np.ix_(sel, sel)]
    return lgx.window_cond_cov(mod["A"], mod["Qx"], mod["iw"], ia, L)


def annealed_all(sp, rel_prob, nseq, seed, T=70, tstar=45):
    rng = np.random.default_rng(seed); N = len(sp["agents"]); cache = {}
    def mats(pat):
        if pat not in cache:
            mod = lgx2.build2(sp, "full", present=list(pat)); cache[pat] = (mod["A"], mod["G"], mod["iw"], mod["i_m"], mod["d"], mod["p"])
        return cache[pat]
    A0, G0, iw, im, d, p = mats(tuple([True] * N))
    L0 = np.linalg.cholesky(lgx.stat_cov(A0, G0 @ G0.T) + 1e-14 * np.eye(d))
    ia = [x for i in range(N) for x in (im(i)[0], im(i)[1])]
    comps = [x for i in range(N) for x in sp["agents"][i]["M"]]
    covs, Ks, Gs = [], [], []
    for _ in range(nseq):
        X = np.zeros((d, d + p * T)); X[:, :d] = L0; H = [X[iw]]
        for t in range(T):
            A, G, *_ = mats(tuple(bool(x) for x in (rng.random(N) < rel_prob)))
            if t == tstar:
                E = X[ia] - np.array([X[iw][k] for k in comps])
            X = A @ X; X[:, d + p * t: d + p * (t + 1)] += G; H.append(X[iw])
        Hm = np.vstack(H); Gm = Hm @ Hm.T; CE = E @ Hm.T; Kc = np.linalg.solve(Gm, CE.T).T
        covs.append(E @ E.T - Kc @ CE.T); Ks.append(Kc); Gs.append(Gm)
    Sg = np.mean(Gs, axis=0); Kb = np.mean(Ks, axis=0)
    S = np.mean(covs, axis=0) + np.mean([k @ Sg @ k.T for k in Ks], axis=0) - Kb @ Sg @ Kb.T
    return 0.5 * (S + S.T)


T = np.kron(np.eye(4), c)
sp = ccp_spec(0.5, 0.1, 0.7, sa2=0.01)
for seed in (1, 2, 3):
    S = T @ annealed_all(sp, 1 / 3, 120, seed) @ T.T
    P = np.linalg.inv(S); d = lgx.diffusivity(P)
    print(f"N_pr annealed (sum coordinate) seed {seed}: diffusive={d['diffusive']}; r(pair)="
          f"{lgx.contrast(P, (0, 1))['r'] if d['diffusive'] else float('nan'):.4f}")
cb.c0 = dict(F=0.9, Q=0.05, R=1.0, Rc=0.1, qc=1e-4, kappa=0.7, s2=0.01, QZ=0.05); cb.keys = list(cb.c0); cb.HW = 0.01
los, his, rows = [], [], []
for q in cb.design():
    spp = ccp_spec(0.5, q["Rc"], q["kappa"], F=q["F"], Q=q["Q"], R=q["R"], qc=q["qc"], QZ=q["QZ"], sa2=q["s2"])
    Ps = {nl: np.linalg.inv(T @ all_cov(spp, nl) @ T.T) for nl in ("full", "eff", "lp", "hab")}
    rb = lgx.baseline_mean_coupling(Ps["full"]); rP = lgx.contrast(Ps["full"], (0, 1))["r"]
    bo = max(r for r, C, _ in lgx.all_regions(Ps["full"], top=0) if C not in PAIRS)
    nl = [lgx.contrast(Ps[k], (0, 1))["r"] for k in ("eff", "lp", "hab") if lgx.diffusivity(Ps[k])["diffusive"]]
    los.append(max([rb, bo] + nl)); his.append(rP); rows.append((Ps, rb))
r0 = 0.5 * (max(los) + min(his)); ok = 0
for Ps, rb in rows:
    ok += (set(lgx.selected(Ps["full"], r0, rb)) == PAIRS and all(lgx.selected(Ps[k], r0, rb) == [] for k in ("eff", "lp", "hab"))
           and all(lgx.diffusivity(Ps[k])["diffusive"] for k in ("eff", "lp", "hab")))
print(f"sum coordinate, box +-1%: intersection ({max(los):.4f}, {min(his):.4f}]; at r0={r0:.4f}: verdicts (nulls diffusive and selecting nothing) at {ok}/17")
