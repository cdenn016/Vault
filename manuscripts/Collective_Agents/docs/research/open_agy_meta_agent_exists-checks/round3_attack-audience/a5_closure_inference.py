r"""A5: closure (Markov defect, closure defect) and inference for P0, own code.

Declared expectations (candidate): d_M = 0.0257 (independent of qc), d_cl = 0.251;
best-constant forward KL 0.02509, claimed-variance KL 0.0266, reverse 0.0245,
all against the 'union-model predictive of eta_t'.
I additionally compute the inference KL against three union models:
  U-exact   : posterior given all members' data, eta_C = (eta, u_S) so the four
              channel copies are conditionally independent given u_S; no computation noise
  U-qc      : same, with the members' computation noise in its mean and covariance
  U-product : 'product of the members' likelihoods' in the members' own coordinates,
              each channel read as N(eta_{t-1}, R_S+R_c) independently (overcounts v_S)
Negative control (must fail): the KL of a single member's prior mean against U-exact
should exceed that of the average; the KL of the union mean itself must be 0.
"""
import os
for v in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS"):
    os.environ[v] = "1"
import numpy as np
from scipy.linalg import solve_discrete_lyapunov
from alib import P0Model, riccati_fixed, AF

m = P0Model()
F, Q, R, RS, Rc, qc, n = m.F, m.Q, m.R, m.RS, m.Rc, m.qc, m.n
A = AF(F)

# ---------------- Markov defect of y = one member's prior mean (= the average's law) ----
M = m.Mm
for qcv in (1e-4, 1e-2):
    Sx = solve_discrete_lyapunov(M, qcv * np.eye(2))
    L = 400
    ac = np.array([(np.linalg.matrix_power(M, k) @ Sx)[0, 0] for k in range(L + 2)])
    def cond_var(target_lag_list, cond_lags):
        # variance of y_{t+1} given y at times t - lags
        idx = cond_lags
        S11 = ac[0]
        S12 = np.array([ac[1 + l] for l in idx])
        S22 = np.array([[ac[abs(a - b)] for b in idx] for a in idx])
        return S11 - S12 @ np.linalg.solve(S22, S12)
    v1 = cond_var(None, [0])
    vals = []
    for H in (1, 2, 5, 20, 100, 300):
        vH = cond_var(None, list(range(0, H + 1)))
        vals.append((H, 0.5 * np.log(v1 / vH)))
    print("qc=%.0e  I(y_{t+1}; y_{t-1..t-H} | y_t):" % qcv, ", ".join("H=%d: %.6f" % hv for hv in vals))

# closure defect for the 8-dim block system with y = average of first coordinates
Mb = np.kron(np.eye(n), M)
Qn = qc * np.eye(2 * n)
Sb = solve_discrete_lyapunov(Mb, Qn)
P = np.zeros((1, 2 * n)); P[0, 0::2] = 1.0 / n
Sxy = Sb - Sb @ P.T @ np.linalg.solve(P @ Sb @ P.T, P @ Sb)
dcl = 0.5 * np.log(np.linalg.det(np.eye(1) + np.linalg.solve(P @ Qn @ P.T, P @ Mb @ Sxy @ Mb.T @ P.T)))
print("closure defect d_cl (eq:agy-closure-defect) = %.6f" % dcl)

# ---------------- inference ----------------
# joint system: members (as in P0Model.system with world) + union filter error
T0, W0 = m.system(include_world=True)  # dims: eps_S(2), eps_i(2n), vS_lag(1)
dim0 = T0.shape[0]
iv = dim0 - 1


def union_filter(Rown, Rch, qcu):
    Pm, Pp = riccati_fixed(F, Q, qcu, np.eye(2), np.diag([Rown, Rch]))
    K = Pp @ np.linalg.inv(np.diag([Rown, Rch]))
    Mu = A @ Pp @ np.linalg.inv(Pm)
    return Pm, Pp, K, Mu


def joint_cov(Ku, Mu, qc_in_mean):
    """Augment with eps_U (2). Rebuild the noise loadings explicitly."""
    dim = dim0 + 2
    T = np.zeros((dim, dim))
    T[:dim0, :dim0] = T0
    T[dim0:, dim0:] = Mu
    T[dim0:, iv] = (A @ Ku)[:, 1]  # v_S(t-1) enters union channel average
    cols, var = [], []
    # v_S(t)
    g = np.zeros(dim); g[0:2] = (A @ m.KS)[:, 0]; g[iv] = 1.0
    cols.append(g); var.append(RS)
    for i in range(n):  # own sensor v_i
        g = np.zeros(dim); s = 2 + 2 * i
        g[s:s + 2] = (A @ m.Km)[:, 0]
        g[dim0:] = (A @ Ku)[:, 0] / n
        cols.append(g); var.append(R)
    for i in range(n):  # channel noise nu_iS
        g = np.zeros(dim); s = 2 + 2 * i
        g[s:s + 2] = (A @ m.Km)[:, 1]
        g[dim0:] = (A @ Ku)[:, 1] / n
        cols.append(g); var.append(Rc)
    for a_ in range(n + 1):
        for c in range(2):
            g = np.zeros(dim); g[2 * a_ + c] = 1.0
            cols.append(g); var.append(qc)
    if qc_in_mean:
        for c in range(2):
            g = np.zeros(dim); g[dim0 + c] = 1.0
            cols.append(g); var.append(qc)
    g = np.zeros(dim)
    for a_ in range(n + 1):
        g[2 * a_] = -1.0
    g[dim0] = -1.0
    cols.append(g); var.append(Q)
    G = np.column_stack(cols)
    return solve_discrete_lyapunov(T, G @ np.diag(var) @ G.T)


vm = m.Pm[0, 0]  # members' claimed prior variance of eta_t
avg = np.zeros(dim0 + 2); avg[[2 + 2 * i for i in range(n)]] = 1.0 / n
one = np.zeros(dim0 + 2); one[2] = 1.0
uni = np.zeros(dim0 + 2); uni[dim0] = 1.0
for label, Rch, qcu, qmean in (("U-exact", RS + Rc / n, 0.0, False),
                               ("U-qc", RS + Rc / n, qc, True),
                               ("U-product", (RS + Rc) / n, 0.0, False)):
    Pm_u, Pp_u, Ku, Mu = union_filter(R / n, Rch, qcu)
    S = joint_cov(Ku, Mu, qmean)
    PU = Pm_u[0, 0]
    mseU = uni @ S @ uni
    for nm, vec in (("average y", avg), ("one member", one), ("union mean", uni)):
        d = vec - uni
        D = d @ S @ d
        fwd_best = 0.5 * D / PU
        fwd_claim = 0.5 * (vm / PU - 1 - np.log(vm / PU) + D / PU)
        rev_best = 0.5 * np.log(1 + D / PU)
        print("%-9s claimed P_U=%.6e actual MSE_U=%.6e | %-10s D=%.4e  KL fwd(best v)=%.5f  fwd(claimed %.4e)=%.5f  rev(best)=%.5f" %
              (label, PU, mseU, nm, D, fwd_best, vm, fwd_claim, rev_best))
