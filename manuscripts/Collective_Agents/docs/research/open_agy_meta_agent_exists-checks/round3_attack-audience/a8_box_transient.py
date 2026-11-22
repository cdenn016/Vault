r"""A8: (1) Markov defect from non-stationary Gaussian initial laws (input-conditional
form of def:agy-closure(i), 05_agency.tex:20: d_M = sup_t I(y_{t+1}; y_{0:t-1} | y_t));
(2) all 2^7 = 128 corners of the +-5% box over (F,Q,R,R_S,R_c,qc,gamma) for the exact
clauses: diffusivity, r(A) >= 4.5 > max(mean-coupling, M-perm baselines),
d_M <= 0.03, inference KL (best constant, exact union) <= 0.03, EFE choice of S.

Declared expectations: (1) the sup over t equals the stationary limit 0.025717 for the
stationary initial law, and may exceed it for other initial laws (unknown).
(2) candidate's 17-point fractional design: r(A) in [4.574, 6.310], largest lower
edge 4.431, d_M <= 0.0276, KL <= 0.0291.  The full factorial may find worse corners.
Negative control: corner evaluation at the center reproduces A1/A5 values.
"""
import os, sys, itertools
for v in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS"):
    os.environ[v] = "1"
import numpy as np
from scipy.linalg import solve_discrete_lyapunov
from alib import P0Model, contrast, all_regions, diffusive_parts, mean_coupling_baseline, perm_average, riccati_fixed, AF

# ---------------- (1) transients ----------------
m = P0Model()
M = m.Mm
qc = m.qc
Sst = solve_discrete_lyapunov(M, qc * np.eye(2))


def defect_path(S0, tmax=60):
    # covariance of (x_0..x_T) for x_{t+1} = M x_t + n_t, x_0 ~ N(0,S0); y_t = x_{t,0}
    T = tmax + 2
    covs = [S0]
    for t in range(1, T):
        covs.append(M @ covs[-1] @ M.T + qc * np.eye(2))
    def C(s, t):  # Cov(x_s, x_t), s >= t
        return np.linalg.matrix_power(M, s - t) @ covs[t]
    Y = np.zeros((T, T))
    for s in range(T):
        for t in range(s + 1):
            Y[s, t] = C(s, t)[0, 0]
            Y[t, s] = Y[s, t]
    out = []
    for t in range(1, tmax):
        # I(y_{t+1}; y_{0:t-1} | y_t)
        def cv(idx):
            a = t + 1
            if len(idx) == 0:
                return Y[a, a]
            S12 = Y[a, idx]; S22 = Y[np.ix_(idx, idx)]
            return Y[a, a] - S12 @ np.linalg.solve(S22 + 1e-30 * np.eye(len(idx)), S12)
        v1 = cv([t]); vall = cv(list(range(0, t + 1)))
        out.append(0.5 * np.log(v1 / vall))
    return np.array(out)


for name, S0 in (("stationary", Sst), ("x0 = 0 (deterministic)", 1e-14 * np.eye(2)),
                 ("qc I", qc * np.eye(2)), ("10x stationary", 10 * Sst),
                 ("eta-direction only", np.diag([Sst[0, 0], 1e-14]))):
    d = defect_path(S0)
    print("initial law %-24s: sup_t I_t = %.6f at t=%d ; I_t at t=1,2,5,50: %s" %
          (name, d.max(), d.argmax() + 1, np.round(d[[0, 1, 4, 49]], 6)))
sys.stdout.flush()

# ---------------- (2) full factorial box ----------------
center = dict(F=0.9, Q=0.05, R=1.0, RS=0.01, Rc=0.002, qc=1e-4, gamma=40.0)
keys = list(center)
regs = all_regions(5)


def evaluate(p):
    mm = P0Model(**p)
    probs, _ = mm.policy_probs()
    Sc = mm.sigma_c()
    Pi = np.linalg.inv(Sc)
    _, _, mo, mr = diffusive_parts(Pi)
    dif = mo <= 0 and mr >= 0
    rA = contrast(Pi, [1, 2, 3, 4]) if dif else np.nan
    rother = max(contrast(Pi, C) for C in regs if C != [1, 2, 3, 4]) if dif else np.nan
    mc = mean_coupling_baseline(Pi) if dif else np.nan
    Sp = perm_average(Sc)
    mp_ = max(contrast(np.linalg.inv(Sp), C) for C in regs)
    Sx = solve_discrete_lyapunov(mm.Mm, np.eye(2))
    L = 120
    ac = np.array([(np.linalg.matrix_power(mm.Mm, k) @ Sx)[0, 0] for k in range(L + 2)])
    S11 = ac[0]
    def cvar(idx):
        S12 = np.array([ac[1 + l] for l in idx]); S22 = np.array([[ac[abs(a - b)] for b in idx] for a in idx])
        return S11 - S12 @ np.linalg.solve(S22, S12)
    dM = 0.5 * np.log(cvar([0]) / cvar(list(range(L))))
    # inference vs exact union (no qc): KL best constant = 1/2 (E ebar^2 - P_U)/P_U
    T0, W0 = mm.system(include_world=True)
    SZ = solve_discrete_lyapunov(T0, W0)
    avg = np.zeros(T0.shape[0]); avg[[2 + 2 * i for i in range(4)]] = 0.25
    msey = avg @ SZ @ avg
    Pm_u, _ = riccati_fixed(p["F"], p["Q"], 0.0, np.eye(2), np.diag([p["R"] / 4, p["RS"] + p["Rc"] / 4]))
    PU = Pm_u[0, 0]
    kl = 0.5 * (msey - PU) / PU
    return dict(pS=probs["S"], dif=dif, rA=rA, rother=rother, mc=mc, mp=mp_, dM=dM, kl=kl)


c = evaluate(center)
print("\ncenter: ", {k: (round(v, 6) if isinstance(v, float) else v) for k, v in c.items()})
rows = []
for signs in itertools.product((-1, 1), repeat=7):
    p = {k: center[k] * (1 + 0.05 * s) for k, s in zip(keys, signs)}
    r = evaluate(p)
    r["signs"] = signs
    rows.append(r)
ok = [r for r in rows if r["dif"] and r["rA"] >= 4.5 and max(r["mc"], r["mp"], 1.0) < 4.5 and r["rother"] < 4.5
      and r["dM"] <= 0.03 and r["kl"] <= 0.03 and r["pS"] > 0.999]
print("corners passing every exact clause at grade (4.5, 0.03, 0.03): %d / 128" % len(ok))
print("ranges: r(A) [%.4f, %.4f]; lower edge max(mc, M-perm) [%.4f, %.4f]; other regions max %.4f; d_M max %.5f; KL max %.5f; min p(S) %.6f" %
      (min(r["rA"] for r in rows), max(r["rA"] for r in rows), min(max(r["mc"], r["mp"]) for r in rows),
       max(max(r["mc"], r["mp"]) for r in rows), max(r["rother"] for r in rows), max(r["dM"] for r in rows),
       max(r["kl"] for r in rows), min(r["pS"] for r in rows)))
bad = [r for r in rows if r not in ok]
for r in bad[:12]:
    print("  FAIL corner", r["signs"], "rA=%.4f edge=%.4f dM=%.5f KL=%.5f" % (r["rA"], max(r["mc"], r["mp"]), r["dM"], r["kl"]))
print("failures by clause: rA<4.5: %d ; edge>=4.5: %d ; d_M>0.03: %d ; KL>0.03: %d" %
      (sum(r["rA"] < 4.5 for r in rows), sum(max(r["mc"], r["mp"]) >= 4.5 for r in rows),
       sum(r["dM"] > 0.03 for r in rows), sum(r["kl"] > 0.03 for r in rows)))
