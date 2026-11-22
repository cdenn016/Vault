r"""check12: the OPP instance (Rc = 0.3, kappa = 1.0) clause by clause.

Act parameters: beta = 1, h = 2, F = 0.9, Lam = 1, s2 = 0.01; kappa = gamma Lam beta s2 h F = 1.0 gives
lam = gamma Lam beta^2 sE2 = 1.25, sE2 = s2 (1 + lam) = 0.0225, gamma = 55.56.
Declared expectations BEFORE running:
  E1 full selects exactly the two pairs at every level in (max(rbar, r_eff, r_lp, others), r(pair)];
     N_eff, N_hab, N_lp diffusive and select nothing there;
  E2 N_pr annealed ('zero' and 'kept'): diffusive, r(pair) below the window's lower edge, in every estimate;
  E3 closure: d_M <= 1e-3 and alpha_I <= 0.05 for the pair average (eta_C = eta^f_t, one-dimensional);
  E4 agency index positive but small (opposite preferences: the class explains only the contraction of the
     total act), for the declared class (group preference N(0, 1/Lam) on the outcome, habits fixed, gamma_C >= 0);
  E5 +-1% box over (F, Q, R, Rc, qc, kappa, s2, QZ): a common level r0 with E1's verdicts at 17/17 points.
"""
import numpy as np
from scipy.optimize import minimize_scalar
import lgx
from check11_opp import opp_spec, evaluate, PAIRS
from check8_box import closure, design

F, Q, R, Rc, qc, QZ, beta, h, Lam, s2 = 0.9, 0.05, 1.0, 0.3, 1e-4, 0.05, 1.0, 2.0, 1.0, 0.01
KAP = 1.0
lam = 1.0 / (h * F / (KAP * beta) - 1.0)          # KAP = lam/(1+lam) * h F / beta
sE2 = s2 * (1 + lam)
gamma = lam / (Lam * beta ** 2 * sE2)
assert abs(gamma * Lam * beta * s2 * h * F - KAP) < 1e-12


def simulate(spec, seq, T, tstar, mode):
    ag = spec["agents"]; N = len(ag); Kc = len(spec["Qw"])
    Qw = np.asarray(spec["Qw"]); Fw = np.asarray(spec["Fw"])
    mod = lgx.build(spec, "full"); Kg = mod["gains"][0]["K"]
    AF = np.array([[spec["Fw"][0][0], 0.0], [1.0, 0.0]])
    comp = [a["k"] for a in ag]; kap = [a["kappa"] for a in ag]; mate = {i: ag[i]["senders"][0] for i in range(N)}
    Zc = [a["Z"] for a in ag]; Rr = ag[0]["R"]; Rcc = spec["Rc"]; qcc = spec["qc"]; sa = ag[0]["sa2"]
    per = Kc + 2 * N + 2 * N + N
    ncol = Kc + per * T
    eta = np.zeros((Kc, ncol))
    for k in range(Kc):
        eta[k, k] = np.sqrt(Qw[k] / (1 - Fw[k, k] ** 2)) if Fw[k, k] > 0 else np.sqrt(Qw[k])
    lag = np.zeros((Kc, ncol)); m = np.zeros((N, 2, ncol)); vlag = np.zeros((N, ncol)); H = [eta.copy()]; E = None
    for t in range(T):
        base = Kc + per * t
        v = lambda j: base + Kc + j; nu = lambda i: base + Kc + N + i
        qn = lambda i, c: base + Kc + 2 * N + 2 * i + c; an = lambda i: base + Kc + 4 * N + i
        if t == tstar:
            E = np.array([m[i, 0] - eta[comp[i]] for i in range(N)])
        mp = np.zeros((N, 2, ncol))
        for i in range(N):
            s = eta[comp[i]].copy(); s[v(i)] += np.sqrt(Rr)
            p = seq[t, i]
            inn0 = s - m[i, 0]
            if p == mate[i] or mode == "kept":
                y = lag[comp[p]] + vlag[p]; y = y.copy(); y[nu(i)] += np.sqrt(Rcc)
                mp[i] = m[i] + np.outer(Kg[:, 0], inn0) + np.outer(Kg[:, 1], y - m[i, 1])
            else:
                mp[i] = m[i] + np.outer(Kg[:, 0], inn0)
        u = np.array([-kap[i] * mp[i, 0] for i in range(N)])
        for i in range(N):
            u[i, an(i)] += np.sqrt(sa)
        new = Fw @ eta
        for k in range(Kc):
            new[k, base + k] += np.sqrt(Qw[k])
        for i in range(N):
            new[Zc[i]] += ag[i]["beta"] * u[i]
        for i in range(N):
            m[i] = AF @ mp[i]; m[i, 0, qn(i, 0)] += np.sqrt(qcc); m[i, 1, qn(i, 1)] += np.sqrt(qcc)
        vlag = np.zeros((N, ncol))
        for j in range(N):
            vlag[j, v(j)] = np.sqrt(Rr)
        lag = eta; eta = new; H.append(eta.copy())
    Hm = np.vstack(H); G = Hm @ Hm.T; CE = E @ Hm.T
    Ks = np.linalg.solve(G, CE.T).T
    return E @ E.T - Ks @ CE.T, Ks, G


def annealed(spec, mode, nseq, seed, T=70, tstar=45):
    rng = np.random.default_rng(seed); N = len(spec["agents"])
    covs, Ks, Gs = [], [], []
    for _ in range(nseq):
        seq = np.zeros((T, N), dtype=int)
        for i in range(N):
            seq[:, i] = rng.choice([j for j in range(N) if j != i], size=T)
        c, k, g = simulate(spec, seq, T, tstar, mode); covs.append(c); Ks.append(k); Gs.append(g)
    Sg = np.mean(Gs, axis=0); Kb = np.mean(Ks, axis=0)
    mix = np.mean([k @ Sg @ k.T for k in Ks], axis=0) - Kb @ Sg @ Kb.T
    S = np.mean(covs, axis=0) + mix
    return 0.5 * (S + S.T)


def agency(spec, mod, ntates=300):
    C0 = [0, 1]; n = 2
    P = lgx.stat_cov(mod["A"], mod["Qx"])
    Ux = mod["Ux"][C0]; Un = mod["Un"][C0].copy(); Un[:, mod["n_a"]] = 0.0
    Cmu = Ux @ P @ Ux.T + (Un * mod["sd"] ** 2) @ Un.T
    MU = np.random.default_rng(7).multivariate_normal(np.zeros(n), 0.5 * (Cmu + Cmu.T), size=ntates)

    def kl(m1, S1, m2, S2):
        S2i = np.linalg.inv(S2); dm = m2 - m1
        return 0.5 * (np.trace(S2i @ S1) + dm @ S2i @ dm - n + np.log(np.linalg.det(S2) / np.linalg.det(S1)))

    def group(gC, zC):
        Gam = np.eye(n) / sE2 + gC * Lam * beta ** 2 * np.ones((n, n)); Si = np.linalg.inv(Gam)
        return -gC * Lam * beta * zC * Si @ np.ones(n), Si

    den = sum(kl(mu, s2 * np.eye(n), np.zeros(n), sE2 * np.eye(n)) for mu in MU)
    out = {}
    # declared class 1: group target 0 on the outcome (z_C = 0); class 2: group adopts b's map (z_C = -h F mbar)
    # member 0 acts u = -KAP m (its z = +h F m), member 1 acts u = +KAP m (its z = -h F m)
    mbar = lambda mu: np.mean([-mu[0] / KAP, mu[1] / KAP])
    for name, zf in (("target-0", lambda mu: 0.0),
                     ("member-0 map", lambda mu: +h * F * mbar(mu)),
                     ("member-1 map", lambda mu: -h * F * mbar(mu))):
        f = lambda lg: sum(kl(mu, s2 * np.eye(n), *group(np.exp(lg), zf(mu))) for mu in MU)
        grid = np.linspace(-8, 10, 73); vals = [f(x) for x in grid]; j = int(np.argmin(vals))
        res = minimize_scalar(f, bounds=(grid[max(j - 1, 0)], grid[min(j + 1, 72)]), method="bounded")
        best = min((res.fun, float(res.x)), (vals[j], float(grid[j])))
        out[name] = (1 - best[0] / den, float(np.exp(best[1])))
    return out, den / len(MU)


if __name__ == "__main__":
    sp = opp_spec(KAP, Rc, sa2=s2)
    ev = evaluate(KAP, Rc, L=60)
    lo, hi = ev["lo"], ev["rP"]
    print(f"instance: r(pair)={hi:.5f}; rbar={ev['rb']:.5f}; r_eff={ev['re']:.5f}; r_lp={ev['rl']:.5f}; "
          f"others={ev['bo']:.5f}; window ({lo:.5f}, {hi:.5f}]")
    Ph = np.linalg.inv(lgx.sigma_c(sp, "hab", 60))
    for r0 in np.linspace(lo, hi, 5)[1:-1]:
        print(f"  r0={r0:.4f}: full {lgx.selected(ev['Pf'], r0, ev['rb'])}; N_eff {lgx.selected(ev['Pe'], r0, ev['rb'])}; "
              f"N_hab {lgx.selected(Ph, r0, ev['rb'])}; N_lp {lgx.selected(ev['Pl'], r0, ev['rb'])}")
    print(f"  diffusive: N_eff {lgx.diffusivity(ev['Pe'])['diffusive']}, N_hab {lgx.diffusivity(Ph)['diffusive']}, "
          f"N_lp {ev['dl']}; Pi full pair block {np.array2string(ev['Pf'][:2, :2], precision=3)}")
    # validation of the row propagation with fixed mates
    N = 4; T = 70
    seq = np.array([[sp['agents'][i]['senders'][0] for i in range(N)]] * T)
    c, _, _ = simulate(sp, seq, T, 45, "zero")
    print(f"VAL row propagation vs stationary: {np.max(np.abs(c - lgx.sigma_c(sp, 'full', 60))):.2e}")
    for mode in ("zero", "kept"):
        for seed in (1, 2, 3):
            S = annealed(sp, mode, 120, seed)
            P = np.linalg.inv(S); d = lgx.diffusivity(P)
            rpp = lgx.contrast(P, (0, 1))["r"] if d["diffusive"] else np.nan
            top = lgx.all_regions(P, top=1)[0] if d["diffusive"] else None
            print(f"  N_pr annealed '{mode}' seed {seed}: diffusive={d['diffusive']} (max off {d['max_off']:+.3f}); "
                  f"r(pair)={rpp:.4f}; max region {top}")
    mod = lgx.build(sp, "full")
    dM2, aI2 = closure(dict(F=F, Q=Q, R=R, Rc=Rc, qc=qc), mod["gains"][0]["K"])
    print(f"closure (pair = one department): d_M = {dM2 / 2:.3e}, alpha_I = {aI2 / 2:.4f}")
    ag, den = agency(sp, mod)
    print(f"agency: mean KL(P||E) = {den:.3f} nats; index by declared class: "
          + "; ".join(f"{k}: {v[0]:.4f} (gamma_C {v[1]:.3g})" for k, v in ag.items()))
    # +-1% box
    c0 = dict(F=F, Q=Q, R=R, Rc=Rc, qc=qc, kappa=KAP, s2=s2, QZ=QZ)
    import check8_box as cb
    cb.c0 = c0; cb.keys = list(c0); cb.HW = 0.01
    los, his, pts = [], [], cb.design()
    rows = []
    for p in pts:
        spp = opp_spec(p["kappa"], p["Rc"], sa2=p["s2"], R=p["R"], F=p["F"], Q=p["Q"], qc=p["qc"], QZ=p["QZ"])
        Pf = np.linalg.inv(lgx.sigma_c(spp, "full", 40)); Pe = np.linalg.inv(lgx.sigma_private(spp, "eff"))
        Pl = np.linalg.inv(lgx.sigma_c(spp, "lp", 40))
        rb = lgx.baseline_mean_coupling(Pf); rP = lgx.contrast(Pf, (0, 1))["r"]
        bo = max(r for r, C, _ in lgx.all_regions(Pf, top=0) if C not in PAIRS)
        l = max(rb, bo, lgx.contrast(Pe, (0, 1))["r"], lgx.contrast(Pl, (0, 1))["r"])
        los.append(l); his.append(rP); rows.append((Pf, Pe, Pl, rb))
    r0 = 0.5 * (max(los) + min(his)); ok = 0
    for Pf, Pe, Pl, rb in rows:
        ok += (set(lgx.selected(Pf, r0, rb)) == PAIRS and lgx.selected(Pe, r0, rb) == []
               and lgx.selected(Pl, r0, rb) == [])
    print(f"box +-1%: intersection ({max(los):.4f}, {min(his):.4f}]; at r0={r0:.4f} verdicts hold at {ok}/17")
