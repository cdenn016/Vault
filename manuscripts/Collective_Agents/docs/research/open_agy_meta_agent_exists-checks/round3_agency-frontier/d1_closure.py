r"""D1 deciding run 3: closure clause (def:agy-closure, 05_agency.tex:13-24) for the scalar collective average.

Conventions as in the round-2 attack (run3_closure.py): interior x = members' prior means (R^4); blanket = own
sensors, slot readings and the senders' sensings carried by relays; interior noise = relay read noise and
computation noise (Q^n > 0).  y = (m^-_{1,0} + m^-_{2,0})/2.
Inference: the encoded belief N(y_t, v) against the union-model predictive posterior N(u_t, U) of eta_t given all
members' exterior-facing data (own sensors, open slots) up to t-1; best constant v, claimed-variance v, reverse.
Declared expectations: stationary d_M about 4.4e-5, per-step d_cl about 8.9e-4 (x2); worst single-round deviation
d_cl below 0.01; inference best-constant about 0.019 (x2), exact and MC agreeing within 3 SE.
NEGATIVE CONTROLS: (i) encoding one member's prior mean instead of the average must give a larger inference defect;
(ii) the R^2 average must give d_cl = 0 (A preserves its kernel) while the scalar average gives d_cl > 0 -- the
scalar declaration is the binding one.
"""
import time
import itertools
import numpy as np
from scipy.linalg import solve_discrete_lyapunov
from flib import closure_numbers, dcl_step, steady_prior, member_mats, mc, A_F
from design import D1

t0 = time.time()
par = D1
n = 2
dcl, dM, dMh = closure_numbers(par, c=1, k=0, n=n, L=80)
print(f"(1) stationary: d_cl per step {dcl:.4e}; d_M {dM:.4e} (window 40: {dMh:.4e})")
Pm = steady_prior(par, 1, 0)
M, k_own, k_slot, k_rel, _ = member_mats(par, Pm, 1, 0)
A = np.kron(np.eye(n), M)
Qn = np.kron(np.eye(n), par.Rc * np.outer(k_rel, k_rel) + par.qc * np.eye(2))
Sig = solve_discrete_lyapunov(A, Qn)
worst, arg = 0.0, None
for cs in itertools.product((0, 1), repeat=n):
    for ks in itertools.product((0, 1, 2), repeat=n):
        v = dcl_step(par, [Pm, Pm], cs, ks, Sig, n)
        if v > worst:
            worst, arg = v, (cs, ks)
print(f"(2) worst single-round deviation (relays read, slots open) from the stationary state: d_cl {worst:.4e} at {arg}")
# sustained deviation: member 1 reads nothing for L rounds (its gains drift), then one step
Pm1 = Pm.copy()
Sg = Sig.copy()
mx = 0.0
for L in range(1, 61):
    Mi, ko, ks_, kr, Pp = member_mats(par, Pm1, 0, 0)
    Mj, _, _, krj, _ = member_mats(par, Pm, 1, 0)
    Ad = np.zeros((4, 4)); Ad[:2, :2] = Mi; Ad[2:, 2:] = Mj
    Qd = np.zeros((4, 4)); Qd[:2, :2] = par.qc * np.eye(2); Qd[2:, 2:] = par.Rc * np.outer(krj, krj) + par.qc * np.eye(2)
    mx = max(mx, dcl_step(par, [Pm1, Pm], [0, 1], [0, 0], Sg, n))
    Sg = Ad @ Sg @ Ad.T + Qd
    Pm1 = np.array([[par.F ** 2 * Pp[0, 0] + par.Q + par.qc, par.F * Pp[0, 0]], [par.F * Pp[0, 0], Pp[0, 0] + par.qc]])
print(f"(3) member 1 reading no relay for up to 60 rounds: max per-step d_cl {mx:.4e}")
# negative control (ii): R^2 average
P2 = np.kron(np.ones((1, n)) / n, np.eye(2))
PS = P2 @ Sig
Sxy = Sig - PS.T @ np.linalg.solve(PS @ P2.T, PS)
Mm = P2 @ A @ Sxy @ A.T @ P2.T
d2 = 0.5 * np.log(np.linalg.det(np.eye(2) + np.linalg.solve(P2 @ Qn @ P2.T, Mm)))
print(f"NEG (ii) R^2 average: d_cl {d2:.2e} (expected 0); scalar average {dcl:.3e} (> 0)")
# (4) inference, exact deterministic limit: joint state (e_1, e_2 in R^2, u_1, u_2 = v(t-1), e_U), unconditional
F = par.F
Up = None
U = 0.1
for _ in range(5000):
    Uplus = 1.0 / (1.0 / U + n / par.R)
    U = F * F * Uplus + par.Q
gU = (1.0 / U) * Uplus
hU = (1.0 / par.R) * Uplus
D = 2 * n + n + 1
Am = np.zeros((D, D)); cols = []
iU = D - 1
for i in range(n):
    Am[2 * i:2 * i + 2, 2 * i:2 * i + 2] = M
    j = 1 - i
    Am[2 * i:2 * i + 2, 2 * n + j] = k_rel
Am[iU, iU] = F * gU
for i in range(n):
    col = np.zeros(D); col[2 * i:2 * i + 2] = k_own * np.sqrt(par.R); col[2 * n + i] = np.sqrt(par.R)
    col[iU] = F * hU * np.sqrt(par.R); cols.append(col)
    col = np.zeros(D); col[2 * i:2 * i + 2] = k_rel * np.sqrt(par.Rc); cols.append(col)
    for d in range(2):
        col = np.zeros(D); col[2 * i + d] = np.sqrt(par.qc); cols.append(col)
col = np.zeros(D)
for i in range(n):
    col[2 * i] = -np.sqrt(par.Q)
col[iU] = -np.sqrt(par.Q); cols.append(col)
Bm = np.array(cols).T
Sj = solve_discrete_lyapunov(Am, Bm @ Bm.T)
ell = np.zeros(D); ell[0] = ell[2] = 1.0 / n; ell[iU] = -1.0
dy2 = float(ell @ Sj @ ell)
v_cl = Pm[0, 0]
best = 0.5 * dy2 / U
claim = 0.5 * (v_cl / U - 1 - np.log(v_cl / U) + dy2 / U)
rev = 0.5 * (U / v_cl - 1 - np.log(U / v_cl) + dy2 / v_cl)
ell1 = np.zeros(D); ell1[0] = 1.0; ell1[iU] = -1.0
best1 = 0.5 * float(ell1 @ Sj @ ell1) / U
print(f"(4) exact inference (deterministic limit): U {U:.6f}, E(y-u)^2 {dy2:.6e}; best-constant {best:.5f}; "
      f"claimed-variance {claim:.5f}; reverse {rev:.5f}")
print(f"NEG (i) encoding member 1's prior mean alone: best-constant {best1:.5f} (must exceed {best:.5f})")
o = mc(par, "full", K=1500, T=400, burn=80, seed=3001, want_inf=True)
I = o.inf
vstar = 1.0 / (I["invU"] / I["n"])
bmc = 0.5 * (vstar * I["invU"] / I["n"] - 1 - np.log(vstar) + I["lnU"] / I["n"] + I["q"] / I["n"])
print(f"(5) MC inference (stochastic policy): best-constant {bmc:.5f}; claimed {I['claim']/I['n']:.5f}; "
      f"reverse {I['rev']/I['n']:.5f}  ({time.time()-t0:.0f}s)")
