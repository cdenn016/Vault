r"""check14: the CCP instance clause by clause (rho = 0.5, Rc = 0.1, kappa = 0.7, F = 0.9, Q = 0.05, R = 1,
qc = 1e-4, QZ = 0.05, h = beta = Lam = 1, s2 = 0.01, so gamma = 70 and sE2 = 1/30).

Declared expectations BEFORE running:
  E1 full selects exactly the two pairs at every level in the window; N_eff, N_hab, N_lp diffusive and select
     nothing there (their r(pair) below the baseline);
  E2 N_pr (annealed, zero-gain convention, mate heard with probability 1/3): diffusive, r(pair) below the full value
     in every estimate (test p = 1/(n_null+1)); no prediction on whether it is below r0;
  E3 closure: 2-d pooled statistic (average of the members' current prior means of (eta^a, eta^b)); d_M <= 1e-3;
     alpha_I <= 0.1;
  E4 agency index (D2, class: pooled belief, common preference, habits fixed, gamma_C >= 0) > 0.1;
  E5 Omega_int(C | zeta_{V\C}) > 0: each member's path loads on the other's private sensing noise (proved by the
     relay); not computed;
  E6 +-1% box: common level with E1's verdicts at 17/17 points.
"""
import numpy as np
from scipy.optimize import minimize_scalar
import lgx
import lgx2
from check13_ccp_scan import ccp_spec, evaluate, PAIRS

RHO, RC, KAP = 0.5, 0.1, 0.7
F, Q, R, qc, QZ, h, beta, Lam, s2 = 0.9, 0.05, 1.0, 1e-4, 0.05, 1.0, 1.0, 1.0, 0.01
gamma = KAP / (Lam * beta * s2 * h)
sE2 = 1.0 / (1.0 / s2 - gamma * Lam * beta ** 2)


def closure(sp):
    mod = lgx2.build2(sp, "full")
    g = mod["gains"][0]; AF = g["AF"]; H = g["H"]; Kg = g["K"]
    Ai = AF @ (np.eye(4) - Kg @ H)
    Qi = sp["Rc"] * AF @ np.outer(Kg[:, 1], Kg[:, 1]) @ AF.T + sp["qc"] * np.eye(4)
    g2 = mod["gains"][1]
    Ai2 = g2["AF"] @ (np.eye(4) - g2["K"] @ g2["H"])
    Qi2 = sp["Rc"] * g2["AF"] @ np.outer(g2["K"][:, 1], g2["K"][:, 1]) @ g2["AF"].T + sp["qc"] * np.eye(4)
    Aint = np.block([[Ai, np.zeros((4, 4))], [np.zeros((4, 4)), Ai2]])
    Qn = np.block([[Qi, np.zeros((4, 4))], [np.zeros((4, 4)), Qi2]])
    Sx = lgx.stat_cov(Aint, Qn)
    P = 0.5 * np.array([[1, 0, 0, 0, 1, 0, 0, 0], [0, 1, 0, 0, 0, 1, 0, 0]], float)
    L = 150
    Ak = np.eye(8); ac = []
    for k in range(L + 2):
        ac.append(P @ Ak @ Sx @ P.T); Ak = Aint @ Ak
    T = np.block([[ac[a - b] if a >= b else ac[b - a].T for b in range(L + 1)] for a in range(L + 1)])
    c = np.hstack([ac[L + 1 - a] for a in range(L + 1)])          # Cov(y_{t+1}, y_{t-L+a})
    v_inf = ac[0] - c @ np.linalg.solve(T, c.T)
    v_one = ac[0] - ac[1] @ np.linalg.solve(ac[0], ac[1].T)
    dM = 0.5 * np.log(np.linalg.det(v_one) / np.linalg.det(v_inf))
    # inference: augment the full lgx2 system with the union filter on (eta^a_t, eta^b_t) from both own sensors
    A, G = mod["A"], mod["G"]; d, p = mod["d"], mod["p"]
    a_, b_ = 0, 1
    Fm = sp["Fw"][np.ix_([a_, b_], [a_, b_])]; Qm = sp["Qw"][np.ix_([a_, b_], [a_, b_])]
    Rm = np.diag([R, R])
    U = lgx.riccati_prior(Fm, Qm, np.eye(2), Rm)
    KU = U @ np.linalg.inv(U + Rm)
    Aa = np.zeros((d + 2, d + 2)); Ga = np.zeros((d + 2, p))
    Aa[:d, :d] = A; Ga[:d] = G
    Aa[d:, d:] = Fm @ (np.eye(2) - KU)
    Aa[d:, [a_, b_]] = Fm @ KU                                     # sensors read eta_t ...
    K = mod["K"]; N = mod["N"]
    vcols = [K + 0, K + 1]                                         # noise columns of v_b(t), v_s(t) (unscaled) ...
    Ga[d:, vcols] = Fm @ KU @ np.diag([np.sqrt(R), np.sqrt(R)])    # ... plus own sensing noise
    S = lgx.stat_cov(Aa, Ga @ Ga.T)
    im = mod["i_m"]
    ybar = np.zeros((2, d + 2))
    for i in (0, 1):
        ybar[0, im(i)[0]] += 0.5; ybar[1, im(i)[1]] += 0.5
    D = ybar.copy(); D[:, d:] -= np.eye(2)
    Edd = D @ S @ D.T
    aI = 0.5 * np.trace(np.linalg.solve(U, Edd))
    return dM, aI, U


def agency(sp, nst=300):
    mod = lgx2.build2(sp, "full")
    C0 = [0, 1]; n = 2
    Pst = lgx.stat_cov(mod["A"], mod["Qx"])
    Ux = mod["Ux"][C0]; Un = mod["Un"][C0].copy(); Un[:, mod["n_a"]] = 0.0
    Cmu = Ux @ Pst @ Ux.T + (Un * mod["sd"] ** 2) @ Un.T
    # pooled belief difference m_C^a - m_C^b from the act means: mu_j = -kappa (m_j^a - m_j^b) => z_j = -mu_j/(gamma Lam beta s2)
    MU = np.random.default_rng(7).multivariate_normal(np.zeros(n), 0.5 * (Cmu + Cmu.T), size=nst)

    def kl(m1, S1, m2, S2):
        S2i = np.linalg.inv(S2); dm = m2 - m1
        return 0.5 * (np.trace(S2i @ S1) + dm @ S2i @ dm - n + np.log(np.linalg.det(S2) / np.linalg.det(S1)))

    def group(gC, zC):
        Gam = np.eye(n) / sE2 + gC * Lam * beta ** 2 * np.ones((n, n)); Si = np.linalg.inv(Gam)
        return -gC * Lam * beta * zC * Si @ np.ones(n), Si

    zC = lambda mu: np.mean(-mu / (gamma * Lam * beta * s2))     # pooled belief: z_C = mean of the members' z_j
    den = sum(kl(mu, s2 * np.eye(n), np.zeros(n), sE2 * np.eye(n)) for mu in MU)
    f = lambda lg: sum(kl(mu, s2 * np.eye(n), *group(np.exp(lg), zC(mu))) for mu in MU)
    grid = np.linspace(-8, 10, 73); vals = [f(x) for x in grid]; j = int(np.argmin(vals))
    res = minimize_scalar(f, bounds=(grid[max(j - 1, 0)], grid[min(j + 1, 72)]), method="bounded")
    num = min(res.fun, vals[j])
    return 1 - num / den, den / nst


if __name__ == "__main__":
    sp = ccp_spec(RHO, RC, KAP, sa2=s2)
    ev = evaluate(sp, L=60)
    lo, hi = ev["lo"], ev["rP"]
    Ph = np.linalg.inv(lgx2.sigma_c2(sp, "hab", 60))
    print(f"gamma={gamma:.3f}, sE2={sE2:.5f}; r(pair)={hi:.5f} rbar={ev['rb']:.5f} r_eff={ev['re']:.5f} "
          f"r_lp={ev['rl']:.5f} r_hab={lgx.contrast(Ph, (0, 1))['r']:.5f} others={ev['bo']:.5f}; window ({lo:.5f}, {hi:.5f}]")
    print(f"Pi full pair block {np.array2string(ev['Pf'][:2, :2], precision=3)}; diffusive N_eff {ev['de']}, "
          f"N_lp {ev['dl']}, N_hab {lgx.diffusivity(Ph)['diffusive']}")
    for r0 in np.linspace(lo, hi, 5)[1:-1]:
        print(f"  r0={r0:.4f}: full {lgx.selected(ev['Pf'], r0, ev['rb'])}; N_eff {lgx.selected(ev['Pe'], r0, ev['rb'])}; "
              f"N_hab {lgx.selected(Ph, r0, ev['rb'])}; N_lp {lgx.selected(ev['Pl'], r0, ev['rb'])}")
    # N_pr validation and estimates
    Sv = lgx2.annealed_pr(sp, 1.0, 3, 0)
    print(f"VAL annealed_pr with the mate always heard vs stationary: {np.max(np.abs(Sv - lgx2.sigma_c2(sp, 'full', 60))):.2e}")
    for seed in (1, 2, 3):
        S = lgx2.annealed_pr(sp, 1.0 / 3.0, 120, seed)
        P = np.linalg.inv(S); dd = lgx.diffusivity(P)
        print(f"  N_pr annealed (zero-gain, p=1/3) seed {seed}: diffusive={dd['diffusive']}; r(pair)="
              f"{lgx.contrast(P, (0, 1))['r'] if dd['diffusive'] else float('nan'):.4f}; top "
              f"{lgx.all_regions(P, top=1)[0][:2] if dd['diffusive'] else None}")
    dM, aI, U = closure(sp)
    print(f"closure: d_M = {dM:.3e}; alpha_I = {aI:.4f} (union prior covariance diag {np.diag(U)})")
    ag, den = agency(sp)
    print(f"agency (D2): index = {ag:.4f}; mean KL(P||E) = {den:.3f} nats")
    # +-1% box over (F, Q, R, Rc, qc, kappa, s2, QZ) with rho fixed
    import check8_box as cb
    cb.c0 = dict(F=F, Q=Q, R=R, Rc=RC, qc=qc, kappa=KAP, s2=s2, QZ=QZ); cb.keys = list(cb.c0); cb.HW = 0.01
    los, his, rows = [], [], []
    for pnt in cb.design():
        spp = ccp_spec(RHO, pnt["Rc"], pnt["kappa"], F=pnt["F"], Q=pnt["Q"], R=pnt["R"], qc=pnt["qc"], QZ=pnt["QZ"],
                       sa2=pnt["s2"])
        e = evaluate(spp, L=40)
        Phh = np.linalg.inv(lgx2.sigma_c2(spp, "hab", 40))
        los.append(e["lo"]); his.append(e["rP"]); rows.append((e, Phh))
    r0 = 0.5 * (max(los) + min(his)); ok = 0
    for e, Phh in rows:
        ok += (set(lgx.selected(e["Pf"], r0, e["rb"])) == PAIRS and lgx.selected(e["Pe"], r0, e["rb"]) == []
               and lgx.selected(e["Pl"], r0, e["rb"]) == [] and lgx.selected(Phh, r0, e["rb"]) == [])
    print(f"box +-1%: intersection ({max(los):.4f}, {min(his):.4f}]; at r0={r0:.4f} verdicts hold at {ok}/17")
