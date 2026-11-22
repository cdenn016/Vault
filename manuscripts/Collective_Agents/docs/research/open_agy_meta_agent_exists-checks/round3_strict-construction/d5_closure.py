r"""Deciding script D5: closure (def:agy-closure, 05_agency.tex:13-24) of the scalar collective average for I**.

Internal variables x = (m^-_i(t))_{i in A} in R^8; given the blanket path (own and private sensor readings, the
members' readings carried by the relays) and the policy path,
   x_{t+1} = A(t) x_t + B(t) x_B(t) + n_t,  A(t) = blockdiag_i A_F P^+_i (P^-_i)^{-1},
   n_t = relay-channel noise A_F K nu + computation noise xi,  Q^n(t) >= qc I_8 > 0.
Coarse variable (declared): y = P1 x, P1 = (1/4)(1,0,1,0,1,0,1,0), the average of the members' prior means of eta_t,
i.e. the collective average of the contrast coordinates.
Memory: d_cl(t) = 1/2 ln(1 + (P Q^n P^T)^{-1} P A Sigma_{x|y} A^T P^T) (eq:agy-closure-defect) with
Sigma = Cov(x_t | blanket and policy paths); d_M <= sup_t d_cl(t) by data processing (input-conditional form).
Inference: E KL(N(ybar, s) || N(u, U)), (u, U) the union-model predictive belief of eta_t (all members' own and open
private sensors through t-1, no delay), s the best constant encoding; also the claimed-variance encoding and the
reverse direction.
Declared expectations (before running):
  sampled paths (both protocols): max d_cl of P1 below 0.01; stationary exact d_M at fixed profiles below 1e-3;
  worst single-round pattern from a stationary state below 0.02;
  NEGATIVE CONTROL 1: the R^2 average P2 at a symmetric fixed profile has d_cl = 0 to 1e-12 (A preserves ker P2);
  NEGATIVE CONTROL 2: P2 at an asymmetric fixed profile (member 0's sensor permanently open) has d_cl > 1e-6.
  inference (best constant) between 0.06 and 0.09 in both protocols;
  NEGATIVE CONTROL 3: one member's prior mean in place of the average gives a larger inference defect.
"""
import itertools, time
import numpy as np
from lib3 import Par, Pminus, A_F, simulate_policy
from mc3 import run
from instance3 import PAR, ALPHA_M, ALPHA_I

t0 = time.time()
n = 4
Af = A_F(PAR.F)
P1 = np.zeros((1, 2 * n)); P1[0, 0::2] = 1.0 / n
P2 = np.kron(np.ones((1, n)) / n, np.eye(2))


def member_mats(par, p_prev, own, ns, no):
    P00, P01, P11 = Pminus(par, p_prev)
    Pm = np.array([[P00, P01], [P01, P11]])
    a = 1.0 / par.R + own / par.Rs
    b = ns / (par.R + par.Rc) + no / (par.Rs + par.Rc)
    Pp = np.linalg.inv(np.linalg.inv(Pm) + np.diag([a, b]))
    Ai = Af @ Pp @ np.linalg.inv(Pm)
    krs = Pp[:, 1] / (par.R + par.Rc); kro = Pp[:, 1] / (par.Rs + par.Rc)
    Qi = Af @ (ns * par.Rc * np.outer(krs, krs) + no * par.Rc * np.outer(kro, kro)) @ Af.T + par.qc * np.eye(2)
    return Ai, Qi, Pp[0, 0]


def dcl(P, A, Qn, Sig):
    PS = P @ Sig
    Sxy = Sig - PS.T @ np.linalg.solve(PS @ P.T, PS)
    M = P @ A @ Sxy @ A.T @ P.T
    return 0.5 * np.log(np.linalg.det(np.eye(P.shape[0]) + np.linalg.solve(P @ Qn @ P.T, M)))


def step(par, ps, cfg):
    A = np.zeros((8, 8)); Qn = np.zeros((8, 8)); pn = []
    for i, (own, ns, no) in enumerate(cfg):
        Ai, Qi, pp = member_mats(par, ps[i], own, ns, no)
        A[2*i:2*i+2, 2*i:2*i+2] = Ai; Qn[2*i:2*i+2, 2*i:2*i+2] = Qi; pn.append(pp)
    return A, Qn, np.array(pn)


# (1) sampled policy paths, both protocols
for proto in ("real", "frozen"):
    par = PAR.with_(proto=proto)
    rng = np.random.default_rng(5101)
    vals1, vals2 = [], []
    for k in range(25):
        pth = simulate_policy(par, 400, rng, "full")
        Sig = np.zeros((8, 8))
        for t in range(400):
            cfg = [(int(pth.sig[t, i]), len(pth.att[t][i]), int(sum(pth.sig_prev[t, j] for j in pth.att[t][i])))
                   for i in range(n)]
            A, Qn, _ = step(par, pth.p_prev[t], cfg)
            if t >= 80:
                vals1.append(dcl(P1, A, Qn, Sig)); vals2.append(dcl(P2, A, Qn, Sig))
            Sig = A @ Sig @ A.T + Qn
    v1 = np.array(vals1); v2 = np.array(vals2)
    print(f"(1) [{proto}] 25 paths x 320 steps: P1 d_cl max {v1.max():.4e}, mean {v1.mean():.4e}, 99.9% {np.quantile(v1, 0.999):.4e}; "
          f"P2 d_cl max {v2.max():.3e}  ({time.time()-t0:.0f}s)", flush=True)


def stationary(par, cfg_fn, L=600):
    p = np.full(n, par.p0)
    for _ in range(L):
        _, _, p = step(par, p, cfg_fn())
    A, Qn, _ = step(par, p, cfg_fn())
    Sig = np.zeros((8, 8))
    for _ in range(600):
        Sig = A @ Sig @ A.T + Qn
    return p, A, Qn, Sig


def exact_dM(A, Sig, P, L=40):
    gam = [float((P @ np.linalg.matrix_power(A, k) @ Sig @ P.T)[0, 0]) for k in range(L + 2)]
    Tm = np.array([[gam[abs(i - j)] for j in range(L + 2)] for i in range(L + 2)])
    def cvar(h):
        idx = list(range(L + 1 - h, L + 1))
        S11 = Tm[np.ix_(idx, idx)]; s12 = Tm[np.ix_(idx, [L + 1])]
        return Tm[L + 1, L + 1] - float((s12.T @ np.linalg.solve(S11, s12))[0, 0])
    return 0.5 * np.log(cvar(1) / cvar(L))


# (2) fixed profiles: exact stationary d_M, symmetric/asymmetric controls, worst single-round patterns
profiles = {"none open": (0, 0, 0, 0), "one open": (1, 0, 0, 0), "two open": (1, 1, 0, 0), "all open": (1, 1, 1, 1)}
worst_all = 0.0
for name, sig in profiles.items():
    cfg = lambda: [(sig[i], 3, sum(sig[j] for j in range(n) if j != i)) for i in range(n)]
    p, A, Qn, Sig = stationary(PAR, cfg)
    d1v, d2v = dcl(P1, A, Qn, Sig), dcl(P2, A, Qn, Sig)
    dM = exact_dM(A, Sig, P1)
    worst, arg = 0.0, None
    opts = [(o, ns, no) for o in (0, 1) for ns in range(4) for no in range(ns + 1)]
    for combo in itertools.product(opts, repeat=n):
        Ad, Qd, _ = step(PAR, p, list(combo))
        v = dcl(P1, Ad, Qd, Sig)
        if v > worst:
            worst, arg = v, combo
    worst_all = max(worst_all, worst)
    print(f"(2) fixed profile {name}: stationary step d_cl P1 {d1v:.4e}, P2 {d2v:.2e}; exact stationary d_M(P1) "
          f"{dM:.4e}; worst single-round pattern P1 {worst:.4e} at {arg}  ({time.time()-t0:.0f}s)", flush=True)
# negative controls 1 and 2 on P2
print(f"NEG1 P2 at the symmetric profile 'none open': d_cl must be 0 to 1e-12 (see line above)")
print(f"NEG2 P2 at 'one open' (asymmetric gains) must exceed 1e-6 (see line above)")
# (3) sustained adversarial sequence: long stretch at one pattern, then the worst single-round pattern
seqs = [((1, 0, 0), (0, 3, 1), (0, 3, 1), (0, 3, 1)), ((0, 0, 0), (0, 3, 0), (0, 3, 0), (1, 3, 0)),
        ((1, 3, 0), (1, 3, 1), (0, 1, 0), (0, 0, 0))]
for sq in seqs:
    p = np.full(n, PAR.p0); Sig = np.zeros((8, 8))
    for _ in range(300):
        A, Qn, p = step(PAR, p, list(sq))
        Sig = A @ Sig @ A.T + Qn
    best = 0.0
    opts = [(o, ns, no) for o in (0, 1) for ns in range(4) for no in range(ns + 1)]
    for combo in itertools.product(opts, repeat=n):
        Ad, Qd, _ = step(PAR, p, list(combo))
        best = max(best, dcl(P1, Ad, Qd, Sig))
    worst_all = max(worst_all, best)
    print(f"(3) sustained {sq} for 300 rounds, then the worst single round: P1 d_cl {best:.4e}")
print(f"MEMORY: worst explored P1 d_cl {worst_all:.4e} vs alpha_M = {ALPHA_M}: holds {worst_all <= ALPHA_M} "
      f"(margin {ALPHA_M - worst_all:.4e})  ({time.time()-t0:.0f}s)", flush=True)

# (4) inference clause, sampled Monte Carlo with the union filter
for proto in ("real", "frozen"):
    o = run(PAR.with_(proto=proto), K=1500, T=400, burn=80, seed=5201, want_inf=True)
    I = o.inf; N = I["n"]
    E = {k: I[k] / N for k in I if k != "n"}
    best_c = 0.5 * (E["dd2_over_U"] + np.log(E["inv_U"]) + E["ln_U"])
    claim = 0.5 * (E["claim_ratio_m1_ln"] + E["dd2_over_U"])
    rev = 0.5 * (np.log(E["U"] + E["dd2"]) - E["ln_U"])
    single = 0.5 * (E["dd2_over_U_single"] + np.log(E["inv_U"]) + E["ln_U"])
    print(f"    NEG3 [{proto}] one member's prior mean in place of the average (best constant): {single:.4f} "
          f"(must exceed {best_c:.4f})")
    print(f"(4) [{proto}] inference: best constant {best_c:.4f}; claimed variance {claim:.4f}; reverse {rev:.4f}; "
          f"alpha_I = {ALPHA_I}: holds (best constant) {best_c <= ALPHA_I} (margin {ALPHA_I - best_c:.4f})  "
          f"({time.time()-t0:.0f}s)", flush=True)
print(f"total {time.time()-t0:.0f}s")
