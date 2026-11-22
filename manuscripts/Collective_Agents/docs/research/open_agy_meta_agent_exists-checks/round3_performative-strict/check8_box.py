r"""check8: +-5% robustness box for the TDF instance (2^(8-4) resolution-IV design plus centre, 17 points) over
(F, Q, R, Rc, qc, kappa, s2, QZ); act parameters derived with beta = h = Lam = 1: gamma = kappa/s2,
sE2 = s2/(1 - kappa).  Per point: full diffusivity, local window (max(rbar, best non-firm region), r(C0)], selected
partitions of the full model, N_eff and N_hab at a common level r0, N_lp diffusivity, alpha_I and d_M of the firm,
agency index (D2, 300 stationary decision states).
Declared expectations BEFORE running:
  E1 the 17 local windows have a nonempty intersection, and at a level r0 in it the full model selects {C0, C1} and
     N_eff, N_hab select {B0, S0, B1, S1} at every point;
  E2 N_lp non-diffusive at every point;
  E3 alpha_I <= 0.05 and d_M <= 1e-3 at every point; agency index >= 0.1 at every point.
"""
import numpy as np
from scipy.optimize import minimize_scalar
import lgx
from tdf import tdf_spec, groups

G = groups(2, 2)
firms = {G["C0"], G["C1"]}
deps = {G["B0"], G["S0"], G["B1"], G["S1"]}
c0 = dict(F=0.9, Q=0.05, R=1.0, Rc=0.1, qc=1e-4, kappa=0.68, s2=0.01, QZ=0.05)
keys = list(c0)


HW = float(__import__("os").environ.get("BOX_HW", "0.05"))


def design():
    pts = [dict(c0)]
    for a in (-1, 1):
        for b in (-1, 1):
            for c in (-1, 1):
                for d in (-1, 1):
                    lv = [a, b, c, d, b * c * d, a * c * d, a * b * c, a * b * d]
                    pts.append({k: c0[k] * (1 + HW * s) for k, s in zip(keys, lv)})
    return pts


def closure(p, Kg):
    F, Q, R, Rc, qc = p["F"], p["Q"], p["R"], p["Rc"], p["qc"]
    AF = np.array([[F, 0.0], [1.0, 0.0]]); H = np.eye(2)
    Ai = AF @ (np.eye(2) - Kg @ H)
    Qi = Rc * AF @ np.outer(Kg[:, 1], Kg[:, 1]) @ AF.T + qc * np.eye(2)
    Aint = np.kron(np.eye(2), Ai); Qn = np.kron(np.eye(2), Qi)
    Sx = lgx.stat_cov(Aint, Qn)
    Py = np.array([[0.5, 0.0, 0.5, 0.0]])
    Lg = 300
    Ak = np.eye(4); acov = []
    for k in range(Lg + 2):
        acov.append((Py @ Ak @ Sx @ Py.T).item()); Ak = Aint @ Ak
    T = np.array([[acov[abs(a - b)] for b in range(Lg + 1)] for a in range(Lg + 1)])
    cvec = np.array(acov[1:Lg + 2])[::-1]
    dM = 0.5 * np.log((acov[0] - acov[1] ** 2 / acov[0]) / (acov[0] - cvec @ np.linalg.solve(T, cvec)))
    PU = Q
    for _ in range(100000):
        Pp = 1.0 / (1.0 / PU + 2.0 / R); PUn = F * F * Pp + Q
        if abs(PUn - PU) < 1e-16:
            break
        PU = PUn
    KU = Pp / R
    d = 9; A = np.zeros((d, d)); Gm = np.zeros((d, 9))
    A[0, 0] = F; Gm[0, 0] = np.sqrt(Q); A[1, 0] = 1.0
    for i, (mi, vi, vj, nui, qi) in enumerate([((2, 3), 6, 7, 3, 5), ((4, 5), 7, 6, 4, 7)]):
        Mx = np.zeros((2, d)); Mx[:, list(mi)] = np.eye(2)
        ox = np.zeros((2, d)); on = np.zeros((2, 9))
        ox[0, 0] = 1.0; on[0, 1 + i] = np.sqrt(R); ox[1, 1] = 1.0; ox[1, vj] = 1.0; on[1, nui] = np.sqrt(Rc)
        A[list(mi)] = AF @ (Mx + Kg @ (ox - H @ Mx)); Gm[list(mi)] = AF @ (Kg @ on)
        Gm[mi[0], qi] += np.sqrt(qc); Gm[mi[1], qi + 1] += np.sqrt(qc); Gm[vi, 1 + i] = np.sqrt(R)
    A[8, 8] = F * (1 - 2 * KU); A[8, 0] = 2 * F * KU; Gm[8, 1] = Gm[8, 2] = F * KU * np.sqrt(R)
    Sj = lgx.stat_cov(A, Gm @ Gm.T)
    dv = np.zeros(d); dv[2] = dv[4] = 0.5; dv[8] = -1.0
    return 2 * dM, 2 * 0.5 * float(dv @ Sj @ dv) / PU


def agency(p, mod, spec):
    kap, s2 = p["kappa"], p["s2"]
    gamma = kap / s2; sE2 = s2 / (1 - kap)
    C0 = list(G["C0"]); n = 4
    P = lgx.stat_cov(mod["A"], mod["Qx"])
    Ux = mod["Ux"][C0]; Un = mod["Un"][C0].copy(); Un[:, mod["n_a"]] = 0.0
    Cmu = Ux @ P @ Ux.T + (Un * mod["sd"] ** 2) @ Un.T
    MU = np.random.default_rng(7).multivariate_normal(np.zeros(n), 0.5 * (Cmu + Cmu.T), size=300)
    sig = np.array([1.0, 1.0, -1.0, -1.0])

    def kl(m1, S1, m2, S2):
        S2i = np.linalg.inv(S2); dm = m2 - m1
        return 0.5 * (np.trace(S2i @ S1) + dm @ S2i @ dm - len(m1) + np.log(np.linalg.det(S2) / np.linalg.det(S1)))

    def group(gC, zC):
        Gam = np.eye(n) / sE2 + gC * np.ones((n, n)); Si = np.linalg.inv(Gam)
        return -gC * zC * Si @ np.ones(n), Si

    def zC(mu):
        m = -mu / (kap * sig)
        return m[:2].mean() - m[2:].mean()

    den = sum(kl(mu, s2 * np.eye(n), np.zeros(n), sE2 * np.eye(n)) for mu in MU)
    f = lambda lg: sum(kl(mu, s2 * np.eye(n), *group(np.exp(lg), zC(mu))) for mu in MU)
    grid = np.linspace(-6, 8, 57); vals = [f(x) for x in grid]; j = int(np.argmin(vals))
    res = minimize_scalar(f, bracket=(grid[max(j - 1, 0)], grid[j], grid[min(j + 1, 56)]))
    return 1 - min(res.fun, vals[j]) / den


if __name__ == "__main__":
    print(f"half-width {HW}")
    rows = []
    for idx, p in enumerate(design()):
        sp = tdf_spec(2, 2, F=p["F"], Q=p["Q"], R=p["R"], Rc=p["Rc"], qc=p["qc"], kappa=p["kappa"], sa2=p["s2"],
                      QZ=p["QZ"])
        mod = lgx.build(sp, "full")
        Pf = np.linalg.inv(lgx.sigma_c(sp, "full", 40))
        Pe = np.linalg.inv(lgx.sigma_private(sp, "eff"))
        Ph = np.linalg.inv(lgx.sigma_c(sp, "hab", 40))
        Pl = np.linalg.inv(lgx.sigma_c(sp, "lp", 40))
        df = lgx.diffusivity(Pf)
        rb = lgx.baseline_mean_coupling(Pf)
        allr = lgx.all_regions(Pf, top=0)
        rC = lgx.contrast(Pf, G["C0"])["r"]
        bo = max(r for r, C, lr in allr if C not in firms)
        dM, aI = closure(p, mod["gains"][0]["K"])
        ag = agency(p, mod, sp)
        rows.append((idx, df["diffusive"], max(rb, bo), rC, rb, bo, Pe, Ph, Pf, lgx.diffusivity(Pl)["diffusive"],
                     dM, aI, ag))
        print(f"pt{idx:2d}: diffusive={df['diffusive']} window=({max(rb, bo):.4f}, {rC:.4f}] rbar={rb:.4f} "
              f"N_lp diffusive={lgx.diffusivity(Pl)['diffusive']} d_M={dM:.2e} alpha_I={aI:.4f} agency={ag:.4f}")
    lo = max(r[2] for r in rows); hi = min(r[3] for r in rows)
    print(f"\nintersection of local windows: ({lo:.4f}, {hi:.4f}]  nonempty={hi > lo}")
    if hi > lo:
        r0 = 0.5 * (lo + hi)
        ok = 0
        for (idx, d, l, h, rb, bo, Pe, Ph, Pf, dl, dM, aI, ag) in rows:
            sf = set(lgx.selected(Pf, r0, rb)); se = set(lgx.selected(Pe, r0, rb)); sh = set(lgx.selected(Ph, r0, rb))
            good = (sf == firms) and (se == deps) and (sh == deps)
            ok += good
            if not good:
                print(f"  pt{idx}: full {sf} N_eff {se} N_hab {sh}")
        print(f"at r0 = {r0:.4f}: full selects {{C0,C1}} and N_eff, N_hab select the four departments at {ok}/17 points")
    print(f"max alpha_I {max(r[11] for r in rows):.4f}; max d_M {max(r[10] for r in rows):.2e}; "
          f"min agency {min(r[12] for r in rows):.4f}; N_lp non-diffusive at {sum(not r[9] for r in rows)}/17")
