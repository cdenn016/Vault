r"""Check 9: relay variant P1 (kmsg = 2): partner-randomization test with 999 null draws, and a +-5% box (center and
the 16-point 2^(7-3) design of check 6, every third point per chunk) for the grade (4.5, 0.03, 0.03, 0.01, 0.99).
Box quantities by sampled Monte Carlo (full model, N_hab, N_pr, M-F medium with kmsg = 2; 1500 world paths x 2
replicas x 250 rounds), exact mean-coupling and M-perm baselines from the estimated Sigma^c, fixed-state memory
bracket, full-policy agency (11 policies per member, class G2).

Declared expectations before running: N_pr test p = 0.001 (every draw below 2.5); NEGATIVE CONTROL: 199 full-model
draws put S_0 in their bulk; on the box every point passes, with the M-F baseline the closest lower edge (about 4.1).
Usage: python check9_relay_test_box.py test | box <chunk 0..2>
"""
import sys
import time
import itertools
import numpy as np
from scipy.linalg import solve_discrete_lyapunov
import sim
from aud import Par, riccati_fixed, b_of, diffusive, contrast, all_regions, mean_coupling_baseline, \
    symmetrize_audience, A_F, info

t0 = time.time()
A = (1, 2, 3, 4)
what = sys.argv[1]


def exch(S):
    N = S.shape[0]
    d = np.trace(S) / N
    o = (S.sum() - np.trace(S)) / (N * (N - 1))
    return d - o, o


def rA_of(S):
    Pi = np.linalg.inv(symmetrize_audience(S))
    return contrast(Pi, A) if diffusive(Pi)[0] else np.nan


if what == "test":
    par = Par(kmsg=2)
    args = (par.F, par.Q, par.R, par.RS, par.Rc, par.qc, par.n, par.kmsg, par.gamma)
    S0 = 5.3724
    o = sim.run(*args, K=999 * 60, T=260, burn=80, seed=9001, mode="pr", nbatch=999)
    r = np.array([rA_of(S) for S in o["S_b"]])
    nd = int(np.sum(np.isnan(r)))
    p = (1 + np.sum(r >= S0) + nd) / (len(r) + 1)
    print(f"P1 N_pr, 999 draws (60 world paths each): undefined {nd}; r(A) min {np.nanmin(r):.3f} median "
          f"{np.nanmedian(r):.3f} max {np.nanmax(r):.3f}; p (undefined scored as >= S_0) = {p:.4f}  ({time.time()-t0:.0f}s)")
    of = sim.run(*args, K=199 * 60, T=260, burn=80, seed=9002, mode="full", nbatch=199)
    rf = np.array([rA_of(S) for S in of["S_b"]])
    print(f"NEG full model, 199 draws: min {np.nanmin(rf):.3f} median {np.nanmedian(rf):.3f} max {np.nanmax(rf):.3f}; "
          f"p = {(1 + np.sum(rf >= S0)) / (len(rf) + 1):.3f}  ({time.time()-t0:.0f}s)")
    sys.exit()

chunk = int(sys.argv[2])
base = Par(kmsg=2)
center = np.array([base.F, base.Q, base.R, base.RS, base.Rc, base.qc, base.gamma])
pts = [np.zeros(7)]
for a, b, c, d in itertools.product((-1, 1), repeat=4):
    pts.append(np.array([a, b, c, d, a * b * c, b * c * d, a * c * d], float))
sets = [()] + [(j,) for j in range(4)] + list(itertools.combinations(range(4), 2))
hasS = np.array([1 if 0 in s else 0 for s in sets])
nm = np.array([sum(1 for j in s if j != 0) for s in sets])
profs = np.array(list(itertools.product(range(len(sets)), repeat=4)))
kS = hasS[profs].sum(1)
lnE = np.full(len(profs), 4 * np.log(1.0 / len(sets)))


def agency(par):
    Pm, _ = riccati_fixed(par, 1 / par.R, b_of(par, 1, 1))
    G = np.array([-info(Pm, 1 / par.R, b_of(par, hasS[k], nm[k])) for k in range(len(sets))])
    lw = -par.gamma * G; lw -= lw.max(); q = np.exp(lw); q /= q.sum()
    lnP = np.log(q)[profs].sum(1); P = np.exp(lnP)
    GC = -0.5 * np.log1p(np.arange(5) * (Pm[1, 1] + par.RS) / par.Rc)
    den = float(np.sum(P * (lnP - lnE)))
    best = den
    for gC in np.geomspace(1e-1, 1e5, 300):
        lwg = lnE - gC * GC[kS]; mx = lwg.max()
        best = min(best, float(np.sum(P * (lnP - (lwg - (mx + np.log(np.exp(lwg - mx).sum())))))))
    return 1 - best / den


def memory(par):
    Pm, Pp = riccati_fixed(par, 1 / par.R, b_of(par, 1, 1))
    M = A_F(par.F) @ Pp @ np.linalg.inv(Pm)
    k_rel = Pp[:, 1] / (par.R + par.Rc)
    Qn = par.qc * np.eye(2) + par.Rc * A_F(par.F) @ np.outer(k_rel, k_rel) @ A_F(par.F).T
    S1 = solve_discrete_lyapunov(M, Qn)
    c = np.array([1.0, 0.0]); ac = []; Pk = S1.copy()
    for k in range(52):
        ac.append(float(c @ Pk @ c)); Pk = M @ Pk
    def cv(m):
        T = np.array([[ac[abs(i - j)] for j in range(m + 1)] for i in range(m + 1)])
        return T[m, m] - T[:m, m] @ np.linalg.solve(T[:m, :m], T[:m, m])
    return 0.5 * np.log(cv(1) / cv(50))


res = []
for k in range(chunk, len(pts), 3):
    x = center * (1 + 0.05 * pts[k])
    par = Par(F=x[0], Q=x[1], R=x[2], RS=x[3], Rc=x[4], qc=x[5], gamma=x[6], kmsg=2)
    args = (par.F, par.Q, par.R, par.RS, par.Rc, par.qc, par.n, par.kmsg, par.gamma)
    sd = 1000 + 37 * k
    of = sim.run(*args, K=1500, T=250, burn=70, seed=sd, mode="full")
    Sf = symmetrize_audience(of["S"])
    Pi = np.linalg.inv(Sf)
    dif = diffusive(Pi)[0]
    rA = contrast(Pi, A)
    rAb = np.array([rA_of(S) for S in of["S_b"]])
    se = np.nanstd(rAb, ddof=1) / np.sqrt(np.sum(~np.isnan(rAb)))
    oth = max(contrast(Pi, C) for C in all_regions(5) if C != A)
    mcb = mean_coupling_baseline(Pi)[0]
    al, be = exch(Sf); mperm = 1 + 5 * be / al
    oF = sim.run(*args, K=1500, T=250, burn=70, seed=sd + 1, mode="full", src=False, Rmed=par.R)
    a2, b2 = exch(oF["S"]); mF = 1 + 5 * b2 / a2
    nh = rA_of(sim.run(*args, K=800, T=250, burn=70, seed=sd + 2, mode="hab")["S"])
    npr = rA_of(sim.run(*args, K=800, T=250, burn=70, seed=sd + 3, mode="pr")["S"])
    dM = memory(par)
    ag = agency(par)
    lower = max(mcb, mperm, mF)
    ok = dif and rA - 3 * se >= 4.5 > lower and oth < 4.5 and max(nh, npr) < lower and dM <= 0.03 and ag >= 0.99
    res.append(ok)
    print(f"pt {k:2d}: r(A) {rA:.3f}+-{se:.3f}; other {oth:.3f}; baselines mc {mcb:.3f} perm {mperm:.3f} M-F {mF:.3f}; "
          f"N_hab {nh:.3f} N_pr {npr:.3f}; d_M {dM:.4f}; agency {ag:.5f}; GRADE {'PASS' if ok else 'FAIL'}  "
          f"({time.time()-t0:.0f}s)", flush=True)
print(f"chunk {chunk}: {sum(res)}/{len(res)} pass")
