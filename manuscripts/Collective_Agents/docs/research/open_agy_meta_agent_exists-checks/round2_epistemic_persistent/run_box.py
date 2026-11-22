r"""Deciding script 5: robustness box, +/-5% in each of (F, Q, R, Rc, Rs, psi, gamma, qc) around I*, design = the
2^(8-4) resolution-IV fractional factorial (16 corners; generators E=ABC, F=BCD, G=ACD, H=ABD) plus the centre.
Run in chunks:  python run_box.py <chunk 0..3>  (writes box_chunk<k>.txt); python run_box.py summary.
At each point: r(A) (24 policy pairs), mechanism medium (8 pairs), mean-coupling baseline 1 + (6/7)(r(A)-1),
N_hab and N_pr (10 pairs each), largest sub-region contrast, agency index at the median symmetric decision state in
class G2, strict inference KL (20 paths).
Declared expectations (before running): under the mechanism reading the declared r0 = 3.5 is admissible
(r_M < 3.5 <= r(A)) at all 17 points and both decisive nulls stay below r_M at all points; under the mean-coupling
reading a single r0 is admissible at some but not all corners (the window is narrow, (r(A)-1)/7 wide); agency
index >= 0.999999 and strict alpha_I < 0.09 at all points.
"""
import sys
import time
import itertools
import numpy as np
from lib import (sigma_c, Pminus, posterior, efe_table, softmin_att, attention_weights, p4_chain, profiles,
                 simulate_policy_path)
from instance import PAR, MEDIUM, M, sim, PROTO, SUFFIX
from lib import simulate_policy_path_real, gibbs_law_sym

R0 = 3.5
names = ["F", "Q", "R", "Rc", "Rs", "psi", "gamma", "qc"]
base = [PAR.F, PAR.Q, PAR.R, PAR.Rc, PAR.Rs, PAR.psi, PAR.gamma, PAR.qc]
design = []
for a, b, c, d in itertools.product([-1, 1], repeat=4):
    design.append([a, b, c, d, a * b * c, b * c * d, a * c * d, a * b * d])
design.append([0] * 8)


HW = float(sys.argv[2]) if len(sys.argv) > 2 else 0.05
TAG = ("" if HW == 0.05 else f"_hw{HW:g}") + SUFFIX


def point(k):
    s = design[k]
    kw = {nm: v * (1 + HW * si) for nm, v, si in zip(names, base, s)}
    return PAR.with_(**kw)


def agency_g2(par, p):
    w = attention_weights(par, 3, 4)
    Gt = np.array([softmin_att(par, efe_table(par, Pminus(par, p), 3, 4), w)] * 4)
    L, _ = p4_chain(par.gamma, Gt)
    NP = profiles(4).sum(1)
    vC = posterior(Pminus(par, p), 1 / par.R, 3 / (par.R + par.Rc))[0, 0]
    E = np.full(16, 1 / 16)
    def law(g):
        G = -0.5 * np.log1p(NP * vC / (par.Rs + par.Rsh)) + par.psi * NP
        lw = -g * G; lw -= lw.max(); q = np.exp(lw); return q / q.sum()
    kl = lambda p_, q_: float(np.sum(p_ * np.log(p_ / q_)))
    gs = np.linspace(0, 3 * par.gamma, 3001)
    vals = [kl(L, law(g)) for g in gs]
    g0 = gs[int(np.argmin(vals))]
    from scipy.optimize import minimize_scalar
    r = minimize_scalar(lambda g: kl(L, law(g)), bounds=(max(0, g0 - 2), g0 + 2), method="bounded",
                        options=dict(xatol=1e-10))
    return 1 - min(r.fun, min(vals)) / kl(L, E), kl(L, E)


def agency_real(par, rng, nrounds=30000):
    r"""Real-time (P4): coarse decision state = every deliberation round at a symmetric covariance state; class G2
    (v_C = the members' anticipated variance at the median p; gamma_C free; habits fixed)."""
    from math import comb
    from scipy.optimize import minimize_scalar
    Pv, Nn = [], []
    for _ in range(nrounds // 5000):
        _, dec = simulate_policy_path_real(par, 5000, rng, "full", record_dec=True)
        for t, pvv, prof in dec[100:]:
            if np.ptp(pvv) < 1e-12:
                Pv.append(pvv[0]); Nn.append(int(prof.sum()))
    c = np.bincount(Nn, minlength=5) / len(Nn)
    vC = posterior(Pminus(par, float(np.median(Pv))), 1 / par.R, 3 / (par.R + par.Rc))[0, 0]
    hab = np.array([comb(4, k) for k in range(5)]) / 16
    m = c > 0
    kl = lambda q: float(np.sum(c[m] * np.log(c[m] / q[m])))
    def law(g):
        nn = np.arange(5)
        G = -0.5 * np.log1p(nn * vC / (par.Rs + par.Rsh)) + par.psi * nn
        lw = np.log([comb(4, k) for k in range(5)]) - g * G; lw -= lw.max(); q = np.exp(lw); return q / q.sum()
    r = minimize_scalar(lambda g: kl(law(g)), bounds=(0, 3000), method="bounded", options=dict(xatol=1e-8))
    return 1 - min(r.fun, kl(hab)) / kl(hab), kl(hab)


def alpha_I(par, rng, npaths=16):
    from run_closure import union_kl
    D2, Ps = [], []
    for _ in range(npaths):
        pth = sim(par, 300, rng)
        for d2, pstar, pcl in union_kl(pth, set(range(80, 300, 4)), par):
            D2.append(d2); Ps.append(pstar)
    D2, Ps = np.array(D2), np.array(Ps)
    Pe = 1.0 / np.mean(1.0 / Ps)
    return 0.5 * np.mean(Pe / Ps - 1 - np.log(Pe / Ps) + D2 / Ps)


def run_point(k):
    par = point(k)
    t0 = time.time()
    full = sigma_c(par, M("full"), 24, 400, 80, 4, seed=1000 + k)
    med = sigma_c(par.with_(n=8, n_zero=0), M("full"), 8, 400, 80, 4, seed=2000 + k)
    hab = sigma_c(par, M("hab"), 10, 400, 80, 4, seed=3000 + k)
    pr = sigma_c(par, M("pr"), 10, 400, 80, 4, seed=4000 + k)
    rA, rM = full["r"], med["r"]
    a_eps = (rA - 1) / 4
    rsub = (1 + 3 * a_eps) / (1 + a_eps)
    rmc = 1 + 6 / 7 * (rA - 1)
    rng = np.random.default_rng(5000 + k)
    pv = []
    for _ in range(6):
        pth = sim(par, 300, rng)
        for t in range(80, 300):
            if np.allclose(pth.Pm[t], pth.Pm[t][0], atol=1e-12, rtol=0):
                pv.append(pth.Pm[t][0, 1, 1] - par.qc)
    ag, den = agency_g2(par, float(np.median(pv))) if PROTO != "real" else agency_real(par, rng)
    aI = alpha_I(par, rng)
    return dict(k=k, s=design[k], rA=rA, rM=rM, rmc=rmc, hab=hab["r"], pr=pr["r"], rsub=rsub, agency=ag, den=den, aI=aI,
                open=full["open_rate"], dev=full["dev_rate"], t=time.time() - t0)


if __name__ == "__main__":
    if sys.argv[1] == "summary":
        rows = []
        for c in range(4):
            with open(f"box{TAG}_chunk{c}.txt") as f:
                for line in f:
                    if line.startswith("{"):
                        rows.append(eval(line, {"array": np.array}))
        rows.sort(key=lambda d: d["k"])
        ok_mech = [d["rM"] < R0 <= d["rA"] and max(d["hab"], d["pr"], d["rsub"]) < d["rM"] for d in rows]
        loc = sum(max(d["hab"], d["pr"], d["rsub"]) < d["rM"] < d["rA"] for d in rows)
        print(f"half-width {HW}: local mechanism windows nonempty with N_hab, N_pr and every sub-region below the "
              f"lower edge at {loc}/{len(rows)} points")
        print(f"points {len(rows)}; mechanism reading, r0 = {R0} admissible with both nulls and sub-regions below the "
              f"lower edge: {sum(ok_mech)}/{len(rows)}")
        print(f"  r(A) range {min(d['rA'] for d in rows):.4f}..{max(d['rA'] for d in rows):.4f}; "
              f"r_M range {min(d['rM'] for d in rows):.4f}..{max(d['rM'] for d in rows):.4f}; "
              f"N_hab max {max(d['hab'] for d in rows):.4f}; N_pr max {max(d['pr'] for d in rows):.4f}; "
              f"sub-region max {max(d['rsub'] for d in rows):.4f}")
        lo = max(d["rM"] for d in rows); hi = min(d["rA"] for d in rows)
        print(f"  r0 admissible at every point (mechanism): ({lo:.4f}, {hi:.4f}]")
        lo2 = max(d["rmc"] for d in rows)
        print(f"  mean-coupling: lower edges up to {lo2:.4f}, r(A) down to {hi:.4f}: a common r0 exists: {lo2 < hi}; "
              f"points where the local mean-coupling window is nonempty and both nulls lie below it: "
              f"{sum(d['rmc'] < d['rA'] and max(d['hab'], d['pr'], d['rsub']) < d['rmc'] for d in rows)}/{len(rows)}")
        for r0 in (4.0, 4.1, 4.2):
            print(f"  mean-coupling r0 = {r0}: admissible at {sum(d['rmc'] < r0 <= d['rA'] for d in rows)}/{len(rows)}")
        print(f"  agency (G2) min {min(d['agency'] for d in rows):.9f}; departure from habits min "
              f"{min(d['den'] for d in rows):.4f}; open rate {min(d['open'] for d in rows):.3f}.."
              f"{max(d['open'] for d in rows):.3f}; attention deviation rate max {max(d['dev'] for d in rows):.1e}")
        print(f"  strict alpha_I range {min(d['aI'] for d in rows):.4f}..{max(d['aI'] for d in rows):.4f}")
    else:
        c = int(sys.argv[1])
        with open(f"box{TAG}_chunk{c}.txt", "w") as f:
            for k in range(c * 5, min(17, c * 5 + 5)):
                d = run_point(k)
                print(d, flush=True)
                f.write(repr({kk: (float(v) if isinstance(v, (float, np.floating)) else v) for kk, v in d.items()})
                        + "\n")
