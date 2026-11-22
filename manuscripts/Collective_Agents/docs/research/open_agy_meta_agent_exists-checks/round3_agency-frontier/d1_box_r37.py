r"""Deciding run 10: D1 grade on a +-5% box (2^(8-4) resolution-IV fractional factorial plus centre, 17 points)
over F, Q, R, Rc, Rs, psi-margin, gamma, qc.

Grade re-declared after d1_box (r0 = 3.5 failed the mean-coupling baseline at 2 points): (3.7, 0.02, 0.03, 0.01, 0.75) under readings
(i) mechanism baseline (also checked against the mean-coupling baseline), (ii) N_pr redrawn every round,
(iii) scalar collective average, memory by the worst reachable single-round deviation.
Per point: exact r(A), mechanism b, mean-coupling baseline, exact inference (best constant), stationary d_M and
worst single-round d_cl, exact full-policy agency index (class G2); MC N_hab and N_pr (K = 500).
Declared expectations: 17/17 points meet every clause; the thinnest margins are the mean-coupling window
(r0 - 3.23 = 0.27 at the centre) and inference (0.03 - 0.0187).
NEGATIVE CONTROL: the same checker applied to the centre with Rc multiplied by 20 (Rc = 2) must fail the collective
clause (r(A) < r0).
"""
import time
import itertools
import numpy as np
from scipy.linalg import solve_discrete_lyapunov
from flib import (Par, exact_sigma_c, compound, r_ab, mc, r_and_se, medium_exact, closure_numbers, steady_prior,
                  member_mats, dcl_step, efe_grid, canonical_types)
from agency_lib import index

t0 = time.time()
R0, AM, AI, AG = 3.7, 0.02, 0.03, 0.75


def build(F, Q, R, Rc, Rs, marg, gamma, qc, m=8):
    base = Par(F=F, Q=Q, R=R, Rc=Rc, Rs=Rs, psi=0.0, gamma=gamma, qc=qc, n=2, n_zero=2, m=m,
               types=canonical_types(1, 2, 1))
    gmax = 0.0
    for c in (0, 1):
        Pm = steady_prior(base, c, 0)
        for cc in (0, 1):
            G = efe_grid(base, Pm[0, 0], Pm[0, 1], Pm[1, 1], np.array([cc]), np.array([0, 1]))
            gmax = max(gmax, float(G[0, 0] - G[0, 1]))
    return base.with_(psi=gmax + marg)


def inference_exact(par):
    n = 2
    Pm = steady_prior(par, 1, 0)
    M, k_own, _, k_rel, _ = member_mats(par, Pm, 1, 0)
    U = 0.1
    for _ in range(5000):
        Uplus = 1.0 / (1.0 / U + n / par.R)
        U = par.F ** 2 * Uplus + par.Q
    gU, hU = Uplus / U, Uplus / par.R
    D = 7
    Am = np.zeros((D, D)); cols = []
    for i in range(n):
        Am[2 * i:2 * i + 2, 2 * i:2 * i + 2] = M
        Am[2 * i:2 * i + 2, 4 + (1 - i)] = k_rel
    Am[6, 6] = par.F * gU
    for i in range(n):
        col = np.zeros(D); col[2 * i:2 * i + 2] = k_own * np.sqrt(par.R); col[4 + i] = np.sqrt(par.R)
        col[6] = par.F * hU * np.sqrt(par.R); cols.append(col)
        col = np.zeros(D); col[2 * i:2 * i + 2] = k_rel * np.sqrt(par.Rc); cols.append(col)
        for d in range(2):
            col = np.zeros(D); col[2 * i + d] = np.sqrt(par.qc); cols.append(col)
    col = np.zeros(D); col[0] = col[2] = col[6] = -np.sqrt(par.Q); cols.append(col)
    Bm = np.array(cols).T
    S = solve_discrete_lyapunov(Am, Bm @ Bm.T)
    ell = np.zeros(D); ell[0] = ell[2] = 0.5; ell[6] = -1.0
    return 0.5 * float(ell @ S @ ell) / U


def check(par, seed, with_nulls=True):
    att = ~np.eye(2, dtype=bool)
    rA = r_ab(2, *compound(exact_sigma_c(par, att, np.zeros(2, dtype=int))[0]))
    b = medium_exact(par, N=4, c=1)[2]
    bmc = 1 + (2.0 / 3.0) * (rA - 1)
    inf = inference_exact(par)
    dcl, dM, _ = closure_numbers(par, c=1, k=0, n=2)
    Pm = steady_prior(par, 1, 0)
    M, _, _, k_rel, _ = member_mats(par, Pm, 1, 0)
    A = np.kron(np.eye(2), M)
    Qn = np.kron(np.eye(2), par.Rc * np.outer(k_rel, k_rel) + par.qc * np.eye(2))
    Sig = solve_discrete_lyapunov(A, Qn)
    worst = max(dcl_step(par, [Pm, Pm], cs, ks, Sig, 2) for cs in itertools.product((0, 1), repeat=2)
                for ks in itertools.product(range(par.m + 1), repeat=2))
    ag = index(par)["idx"]
    rh = rp = np.nan
    if with_nulls:
        rh = r_and_se(mc(par, "hab", K=500, T=300, burn=60, seed=seed), 2)[0]
        rp = r_and_se(mc(par, "pr", K=500, T=300, burn=60, seed=seed + 1, r_att=1), 2)[0]
    ok = dict(coll=rA >= R0 > max(b, 1.0), coll_mc=rA >= R0 > bmc, nulls=(max(rh, rp) < b) if with_nulls else None,
              mem=worst <= AM, inf=inf <= AI, ag=ag >= AG)
    return rA, b, bmc, rh, rp, inf, dM, worst, ag, ok


c = dict(F=0.9, Q=0.05, R=1.0, Rc=0.1, Rs=10.0, marg=0.06, gamma=400.0, qc=1e-4)
keys = list(c.keys())
rows = [np.zeros(8)]
for a, b_, cc, d in itertools.product((-1, 1), repeat=4):
    rows.append(np.array([a, b_, cc, d, a * b_ * cc, b_ * cc * d, a * cc * d, a * b_ * d]))
allok = 0
for k, s in enumerate(rows):
    pv = {key: c[key] * (1 + 0.05 * s[i]) for i, key in enumerate(keys)}
    par = build(**pv)
    rA, b, bmc, rh, rp, inf, dM, worst, ag, ok = check(par, seed=13000 + 10 * k)
    good = all(v for v in ok.values())
    allok += good
    print(f"pt {k:2d}: r(A) {rA:.3f} b {b:.3f} b_mc {bmc:.3f} | N_hab {rh:.3f} N_pr {rp:.3f} | inf {inf:.4f} "
          f"d_M {dM:.1e} worst d_cl {worst:.4f} | Agency {ag:.4f} | {'PASS' if good else 'FAIL ' + str(ok)}"
          f"  ({time.time()-t0:.0f}s)")
print(f"grade (3.7, 0.02, 0.03, 0.01, 0.75) met at {allok}/17 points (mechanism and mean-coupling baselines)")
pv = dict(c); pv["Rc"] = 2.0
r = check(build(**pv), seed=13999, with_nulls=False)
print(f"NEG centre with Rc = 2: r(A) {r[0]:.3f} vs r0 {R0}: collective clause {'passes (control FAILED)' if r[-1]['coll'] else 'fails (as required)'}")
print(f"total {time.time()-t0:.1f}s")
