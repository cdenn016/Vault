r"""Check 6: robustness of every clause of instance P0 on a box around the declared point (open-subset part of the
differ clause, def:agy-nulls, 05_agency.tex:333), declared grade (r0, alpha_M, alpha_I, alpha_pr, Agency0) =
(4.5, 0.03, 0.03, 0.01, 0.99).

Design: center plus a 2^(7-3) fractional factorial (16 corners) over (F, Q, R, RS, Rc, qc, gamma) at relative
half-width hw (argument), generators E = ABC, F' = BCD, G = ACD.  Per point: exact full-model Sigma^c, diffusivity,
r(A), largest other region, mean-coupling and M-perm baselines (exact); M-F baseline, N_hab and N_pr (sampled-noise
Monte Carlo, 800 world paths x 2 replicas x 250 rounds); Markov defect and inference KL (exact); agency index under
the full-policy reading (exact, class G2) and the EFE deviation probability.

Declared expectations before running (hw = 0.05): at every point Pi^c diffusive, r(A) >= 4.5 > every baseline,
N_hab and N_pr below 2.0, d_M <= 0.03, inference KL <= 0.03, agency >= 0.99.
NEGATIVE CONTROL: the point with Rc multiplied by 100 must fail the collective clause (r(A) < 4.5).
Usage: python check6_box.py hw chunk  (chunk 0..2 runs points chunk::3; chunk 3 runs the negative control)
"""
import sys
import time
import itertools
import numpy as np
from scipy.linalg import solve_discrete_lyapunov
import sim
from aud import Par, riccati_fixed, b_of, stationary_fixed, coords, diffusive, contrast, all_regions, \
    mean_coupling_baseline, type_law, symmetrize_audience, posterior, A_F, info

hw = float(sys.argv[1])
chunk = int(sys.argv[2])
t0 = time.time()
base = Par()
names = ["F", "Q", "R", "RS", "Rc", "qc", "gamma"]
center = np.array([base.F, base.Q, base.R, base.RS, base.Rc, base.qc, base.gamma])
pts = [np.zeros(7)]
for a, b, c, d in itertools.product((-1, 1), repeat=4):
    pts.append(np.array([a, b, c, d, a * b * c, b * c * d, a * c * d], float))
A = (1, 2, 3, 4)
R0, AM, AI, AG = 4.5, 0.03, 0.03, 0.99


def exch(S):
    N = S.shape[0]
    d = np.trace(S) / N
    o = (S.sum() - np.trace(S)) / (N * (N - 1))
    return d - o, o


def closure(par):
    n = par.n
    Pm, Pp = riccati_fixed(par, 1.0 / par.R, b_of(par, 1, 0))
    M = A_F(par.F) @ Pp @ np.linalg.inv(Pm)
    # Markov defect of the scalar average (members iid without input: equal to one member's coordinate)
    S1 = solve_discrete_lyapunov(M, par.qc * np.eye(2))
    c = np.array([1.0, 0.0])
    L = 60
    ac = []
    P = S1.copy()
    for k in range(L + 2):
        ac.append(float(c @ P @ c)); P = M @ P
    def cv(m):
        T = np.array([[ac[abs(i - j)] for j in range(m + 1)] for i in range(m + 1)])
        return T[m, m] - T[:m, m] @ np.linalg.solve(T[:m, :m], T[:m, m])
    dM = 0.5 * np.log(cv(1) / cv(L))
    # inference (best constant encoding), union model
    Af = A_F(par.F)
    P = np.eye(2) * par.Q / (1 - par.F ** 2)
    for _ in range(5000):
        Pn = Af @ posterior(P, n / par.R, 1.0 / (par.RS + par.Rc / n)) @ Af.T + np.diag([par.Q, 0.0])
        if np.max(np.abs(Pn - P)) < 1e-17:
            P = Pn; break
        P = Pn
    PU = P
    PUp = posterior(PU, n / par.R, 1.0 / (par.RS + par.Rc / n))
    MU = Af @ PUp @ np.linalg.inv(PU)
    k_own = Pp[:, 0] / par.R; k_S = Pp[:, 1] / (par.RS + par.Rc)
    kU_s = PUp[:, 0] / (par.R / n); kU_y = PUp[:, 1] / (par.RS + par.Rc / n)
    Am = np.zeros((5, 5)); Am[0:2, 0:2] = M; Am[0:2, 4] = Af @ k_S; Am[2:4, 2:4] = MU; Am[2:4, 4] = Af @ kU_y
    G = np.zeros((5, 6))
    G[0:2, 0] = Af @ k_own; G[0:2, 1] = Af @ k_S; G[0:2, 2] = [1, 0]; G[0:2, 3] = [0, 1]
    G[2:4, 0] = Af @ kU_s; G[2:4, 1] = Af @ kU_y; G[4, 4] = 1.0; G[0, 5] = -1.0; G[2, 5] = -1.0
    Qf = np.diag([par.R / n, par.Rc / n, par.qc / n, par.qc / n, par.RS, par.Q])
    SZ = solve_discrete_lyapunov(Am, G @ Qf @ G.T)
    d = np.array([1.0, 0, -1.0, 0, 0])
    return dM, float(d @ SZ @ d) / (2 * PU[0, 0])


def agency(par, Pm_A):
    import itertools as it
    G0 = -info(Pm_A, 1 / par.R, 0.0); GS = -info(Pm_A, 1 / par.R, b_of(par, 1, 0)); Gm = -info(Pm_A, 1 / par.R, b_of(par, 0, 1))
    Gv = np.array([G0, GS, Gm, Gm, Gm])
    lw = np.log(0.2) - par.gamma * Gv; lw -= lw.max(); q = np.exp(lw); q /= q.sum()
    profs = list(it.product(range(5), repeat=par.n))
    lq = np.log(q)
    lnP = np.array([lq[list(p)].sum() for p in profs])
    kS = np.array([sum(1 for x in p if x == 1) for p in profs])
    lnE = np.full(len(profs), par.n * np.log(0.2))
    Vu = Pm_A[1, 1] + par.RS
    GC = -0.5 * np.log1p(np.arange(par.n + 1) * Vu / par.Rc)
    P = np.exp(lnP)
    def kl(lq_):
        return float(np.sum(P * (lnP - lq_)))
    den = kl(lnE)
    best = den
    for gC in np.concatenate([[0.0], np.geomspace(1e-2, 1e4, 400)]):
        lwg = lnE - gC * GC[kS]
        mx = lwg.max()
        best = min(best, kl(lwg - (mx + np.log(np.exp(lwg - mx).sum()))))
    return 1 - best / den, 1 - q[1]


def evaluate(x, label):
    par = Par(F=x[0], Q=x[1], R=x[2], RS=x[3], Rc=x[4], qc=x[5], gamma=x[6])
    Pm_S, _ = riccati_fixed(par, 1.0 / par.RS, 0.0)
    Pm_A, _ = riccati_fixed(par, 1.0 / par.R, b_of(par, 1, 0))
    S, _, _ = stationary_fixed(par, [tuple()] + [(0,)] * par.n, np.array([Pm_S] + [Pm_A] * par.n))
    Sc = coords(par, S)
    Pi = np.linalg.inv(Sc)
    dif = diffusive(Pi)[0]
    rA = contrast(Pi, A)
    oth = max(contrast(Pi, C) for C in all_regions(par.N) if C != A)
    mcb = mean_coupling_baseline(Pi)[0]
    al, be = exch(Sc)
    mperm = 1 + par.N * be / al
    args = (par.F, par.Q, par.R, par.RS, par.Rc, par.qc, par.n, par.kmsg, par.gamma)
    oF = sim.run(*args, K=800, T=250, burn=70, seed=int(1e6 * abs(x).sum()) % 99991, mode="full", src=False, Rmed=par.R)
    a2, b2 = exch(oF["S"])
    mF = 1 + par.N * b2 / a2
    out = {}
    for mode in ("hab", "pr"):
        o = sim.run(*args, K=800, T=250, burn=70, seed=(int(1e6 * abs(x).sum()) + len(mode)) % 99991, mode=mode)
        out[mode] = contrast(np.linalg.inv(symmetrize_audience(o["S"])), A)
    dM, klI = closure(par)
    ag, pdev = agency(par, Pm_A)
    lower = max(mcb, mperm, mF)
    ok = (dif and rA >= R0 > lower and oth < R0 and out["hab"] < lower and out["pr"] < lower and dM <= AM
          and klI <= AI and ag >= AG)
    print(f"{label}: diff {dif}; r(A) {rA:.3f}; other {oth:.3f}; baselines mc {mcb:.3f} perm {mperm:.3f} M-F {mF:.3f}; "
          f"N_hab {out['hab']:.3f} N_pr {out['pr']:.3f}; d_M {dM:.4f}; KL_I {klI:.4f}; agency {ag:.8f} (p_dev {pdev:.1e}); "
          f"GRADE {'PASS' if ok else 'FAIL'}  ({time.time()-t0:.0f}s)", flush=True)
    return ok


if chunk == 3:
    x = center.copy(); x[4] *= 100
    evaluate(x, "NEG Rc x 100")
else:
    res = []
    for k in range(chunk, len(pts), 3):
        x = center * (1 + hw * pts[k])
        res.append(evaluate(x, f"pt {k:2d} {np.round(pts[k]).astype(int).tolist()}"))
    print(f"chunk {chunk}: {sum(res)}/{len(res)} pass")
