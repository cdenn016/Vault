r"""Attack run a3: closure clause of D1 (def:agy-closure, 05_agency.tex:13-24) with independent code, and the
worst-path memory reading R-mem along SUSTAINED deviations that the candidate did not explore.

Conventions (as the candidate states them): interior = members' prior means (R^2 each); blanket = own sensor, slots,
the mate's sensing carried by the relay; interior noise = relay read noise + computation noise; y = scalar average of
the first components.  For a policy path the interior law is propagated from the stationary symmetric state; per step
  d_cl(t) = 1/2 ln(1 + (P Q_t P^T)^{-1} P A_t Sigma_{x|y}(t) A_t^T P^T)            (eq:agy-closure-defect)
  MI(t)   = I(y_{t+1}; y_{0:t-1} | y_t, input path) = 1/2 ln(Var(y_{t+1}|y_t) / Var(y_{t+1}|y_{0:t}))
(exact, Gaussian, zero-noise Kalman filter on y), with MI(t) <= d_cl(t).
Declared expectations: stationary d_cl 8.906e-4, d_M 4.37e-5; single-round all-slots deviation d_cl 9.12e-3 (m=8,
Rs=10).  Sustained all-slots deviations: unknown; if some reachable path has max_t MI(t) > 0.02 the memory clause
fails under R-mem at alpha_M = 0.02; if only d_cl exceeds 0.02 the candidate's d_cl certificate fails but the clause
may hold.  Frontier lever: m = 18 and 50 at Rs = 10 (candidate's index table) -- expectation: single-round all-open
d_cl above 0.02 (precision 1.8 and 5.0 against 0.8 in D1).
Inference: E(y-u)^2 5.1236e-3, U 0.137207, best-constant 0.01867, claimed-variance 0.02043, reverse 0.01885.
NEGATIVE CONTROLS: (i) the R^2 average must give d_cl = 0 at the symmetric stationary step; (ii) a member's own prior
mean as encoding must give a larger inference defect than the average.
"""
import time
import numpy as np
from mylib import Par, steady, gains, predict_cov, fixed_point

t0 = time.time()


def interior(par, Pm, c, k):
    Mbb, lo, ls, lr, Pp = gains(par, Pm, c, k)
    Qi = c * par.Rc * np.outer(lr, lr) + par.qc * np.eye(2)
    return Mbb, Qi, Pp


def blk(a, b):
    Z = np.zeros((4, 4)); Z[:2, :2] = a; Z[2:, 2:] = b
    return Z


Pv = np.array([[0.5, 0.0, 0.5, 0.0]])


def dcl(A, Qn, S, P=Pv):
    PS = P @ S
    Sxy = S - PS.T @ np.linalg.solve(PS @ P.T, PS)
    Mm = P @ A @ Sxy @ A.T @ P.T
    return float(0.5 * np.log(np.linalg.det(np.eye(P.shape[0]) + np.linalg.solve(P @ Qn @ P.T, Mm))))


def run_path(par, path):
    r"""path: list of ((c1,k1),(c2,k2)) per round.  Returns max d_cl, max MI over the path."""
    Pm0 = steady(par, 1, 0)
    M0, Q0, _ = interior(par, Pm0, 1, 0)
    S = fixed_point(blk(M0, M0), blk(Q0, Q0))
    Pms = [Pm0.copy(), Pm0.copy()]
    # filter state for y-history: start from the stationary law, condition on y_0
    Sf = S.copy()
    s = (Pv @ Sf @ Pv.T)[0, 0]
    Sf = Sf - (Sf @ Pv.T @ Pv @ Sf) / s
    maxd, maxmi, arg_d, arg_mi = 0.0, 0.0, None, None
    for t, pol in enumerate(path):
        Ms, Qs, Pps = [], [], []
        for i in range(2):
            Mi, Qi, Pp = interior(par, Pms[i], *pol[i])
            Ms.append(Mi); Qs.append(Qi); Pps.append(Pp)
        A = blk(*Ms); Qn = blk(*Qs)
        d = dcl(A, Qn, S)
        # one-step conditional variance from the marginal law
        vy1 = (Pv @ (A @ S @ A.T + Qn) @ Pv.T)[0, 0]
        cyy = (Pv @ A @ S @ Pv.T)[0, 0]
        v1 = vy1 - cyy ** 2 / (Pv @ S @ Pv.T)[0, 0]
        # full-history: propagate filter and get innovation variance of y_{t+1}
        Sf = A @ Sf @ A.T + Qn
        sfull = (Pv @ Sf @ Pv.T)[0, 0]
        mi = 0.5 * np.log(v1 / sfull)
        Sf = Sf - (Sf @ Pv.T @ Pv @ Sf) / sfull
        if d > maxd:
            maxd, arg_d = d, t
        if mi > maxmi:
            maxmi, arg_mi = mi, t
        S = A @ S @ A.T + Qn
        Pms = [predict_cov(par, Pps[i]) for i in range(2)]
    return maxd, maxmi, arg_d, arg_mi


par = Par()
# ---------------- stationary
Pm0 = steady(par, 1, 0)
M0, Q0, _ = interior(par, Pm0, 1, 0)
A0 = blk(M0, M0); Qn0 = blk(Q0, Q0)
S0 = fixed_point(A0, Qn0)
d0 = dcl(A0, Qn0, S0)
P2 = np.kron(np.ones((1, 2)) / 2, np.eye(2))
d2 = dcl(A0, Qn0, S0, P2)
# stationary Markov defect by zero-noise filter
Sf = S0.copy(); svals = []
for j in range(400):
    s = (Pv @ Sf @ Pv.T)[0, 0]; svals.append(s)
    Sf = Sf - (Sf @ Pv.T @ Pv @ Sf) / s
    Sf = A0 @ Sf @ A0.T + Qn0
dM = 0.5 * np.log(svals[1] / svals[-1])
print(f"stationary: d_cl {d0:.4e}; d_M {dM:.4e}; NEG(i) R^2 average d_cl {d2:.1e}")
# ---------------- single-round worst deviation (all (c,k) pairs)
best = (0, None)
for c1 in (0, 1):
    for k1 in range(par.m + 1):
        for c2 in (0, 1):
            for k2 in range(par.m + 1):
                mx, _, _, _ = run_path(par, [((c1, k1), (c2, k2))])
                if mx > best[0]:
                    best = (mx, ((c1, k1), (c2, k2)))
print(f"single-round worst d_cl {best[0]:.4e} at {best[1]}  ({time.time() - t0:.1f}s)")
# ---------------- sustained deviations
stat = ((1, 0), (1, 0))
res = []
for L in (1, 2, 3, 5, 10, 20, 40, 80):
    for name, pol in (("m1 all slots, reads mate", ((1, par.m), (1, 0))),
                      ("m1 all slots, no relay", ((0, par.m), (1, 0))),
                      ("m1 no relay, no slots", ((0, 0), (1, 0)))):
        path = [pol] * L + [stat] * 40
        mx, mi, ad, am = run_path(par, path)
        res.append((name, L, mx, mi, ad, am))
for r in res:
    print(f"  {r[0]:26s} L={r[1]:3d}: max d_cl {r[2]:.4e} (round {r[4]}), max MI {r[3]:.4e} (round {r[5]})")
alt = [((1, par.m), (1, 0)), stat] * 30
mx, mi, _, _ = run_path(par, alt)
print(f"  alternating m1 all/none every round: max d_cl {mx:.4e}, max MI {mi:.4e}")
oop = [((1, par.m), (1, 0)), ((1, 0), (1, par.m))] * 30
mx, mi, _, _ = run_path(par, oop)
print(f"  both members all slots out of phase: max d_cl {mx:.4e}, max MI {mi:.4e}")
oop2 = [((0, par.m), (1, 0)), ((1, 0), (0, par.m))] * 30
mx, mi, _, _ = run_path(par, oop2)
print(f"  out of phase, deviator reads no relay: max d_cl {mx:.4e}, max MI {mi:.4e}  ({time.time() - t0:.1f}s)")
# ---------------- frontier lever: m = 18, 50 at Rs = 10, and Rs scaled with m
for m, Rs in ((18, 10.0), (50, 10.0), (18, 22.5), (50, 62.5)):
    pm = par.w(m=m, Rs=Rs)
    out = []
    for L in (1, 5, 40):
        mx, mi, _, _ = run_path(pm, [((1, m), (1, 0))] * L + [stat] * 40)
        out.append(f"L={L}: d_cl {mx:.4f} MI {mi:.4f}")
    print(f"frontier m={m} Rs={Rs}: " + "; ".join(out))
print(f"  ({time.time() - t0:.1f}s)")
# ---------------- inference, exact unconditional joint (deterministic limit)
Mbb, lo, ls, lr, _ = gains(par, Pm0, 1, 0)
U = 0.2
for _ in range(10000):
    Up = 1.0 / (1.0 / U + 2.0 / par.R)
    U = par.F ** 2 * Up + par.Q
g = U / (U + par.R / 2)
# state: e1(2), e2(2), vprev1, vprev2, eU ; noises: v1, v2, nu1, nu2, xi1(2), xi2(2), w
D = 7
A = np.zeros((D, D)); cols = []
A[0:2, 0:2] = Mbb; A[2:4, 2:4] = Mbb
A[0:2, 5] = lr; A[2:4, 4] = lr
A[6, 6] = par.F * (1 - g)
for i in range(2):
    col = np.zeros(D); col[2 * i:2 * i + 2] = lo * np.sqrt(par.R); col[4 + i] = np.sqrt(par.R)
    col[6] = par.F * g * 0.5 * np.sqrt(par.R); cols.append(col)
    col = np.zeros(D); col[2 * i:2 * i + 2] = lr * np.sqrt(par.Rc); cols.append(col)
    for d in range(2):
        col = np.zeros(D); col[2 * i + d] = np.sqrt(par.qc); cols.append(col)
col = np.zeros(D); col[0] = col[2] = col[6] = -np.sqrt(par.Q); cols.append(col)
Bm = np.array(cols).T
Sj = fixed_point(A, Bm @ Bm.T)
ell = np.zeros(D); ell[0] = ell[2] = 0.5; ell[6] = -1.0
dy2 = float(ell @ Sj @ ell)
v = Pm0[0, 0]
best_c = 0.5 * dy2 / U
claim = 0.5 * (v / U - 1 - np.log(v / U) + dy2 / U)
rev = 0.5 * (U / v - 1 - np.log(U / v) + dy2 / v)
ell1 = np.zeros(D); ell1[0] = 1.0; ell1[6] = -1.0
one = 0.5 * float(ell1 @ Sj @ ell1) / U
print(f"inference: U {U:.6f}; E(y-u)^2 {dy2:.6e}; best-constant {best_c:.5f}; claimed {claim:.5f}; reverse {rev:.5f};"
      f" NEG(ii) one member's mean {one:.5f}  ({time.time() - t0:.1f}s)")
