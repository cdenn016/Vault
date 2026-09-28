r"""High-precision numerics for the stage-4 early-activation obligations on the
four-cycle of def:rg-formation-cycle-experiment (T = eps^8, fixed base point).

Task 2 (Gaussian-surrogate forgetting curve).  Held-M Ornstein--Uhlenbeck process
dX = -A_M X dt + sqrt(2T) dW, A_M = H_M + T(I + R_ev), started from N(x_circ, s^2 I).
The mean discarded conditional relative entropy of the hidden coordinates z (basis
u_1, n^-_e, n^-_f of Z_M) given the retained coordinates y (basis of W_M) against
kappa = N(0, T K_Z^{-1}) is
  H(t) = E_y KL( q_t(z|y) || kappa ).
Formulation A (block closed form, uses A_M W_M subset W_M, A_M Z_M subset Z_M and
P_Z x_circ = 0, all verified exactly in stage4_cycle_exact.py):
  H_A(t) = sum_k (1/2)[u_k - log(1+u_k)],  u_k = e^{-2 lambda_k t}(s^2 lambda_k/T - 1).
Formulation B (generic): full 12x12 Gaussian covariance via a numerical
eigendecomposition of A_M, Gaussian conditioning of z on y in the exact W/Z basis,
  H_B = (1/2)[tr(P S_c) - 3 - log det(P S_c) + tr(P E[mu mu^T])],  P = K_Z/T.

Task 3 (first qualifying completion time on the center path).
Task 4 (constants at eps = 1e-2, and supplementary window constants).

Run: python stage4_numeric.py  (mpmath, CPU only; no stochastic simulation)
"""
from __future__ import annotations

import json

import mpmath as mp
import sympy as sp

mp.mp.dps = 150
RHO = mp.mpf(1) / 100


# ---------------------------------------------------------------- construction
def build_S0() -> tuple[mp.matrix, mp.matrix, mp.matrix, mp.matrix, mp.matrix]:
    """Return H_M, R_ev, W basis (12x9), Z basis (12x3), x_circ for S^(0) as mp matrices."""
    N = 12

    def e(i: int) -> sp.Matrix:
        v = sp.zeros(N, 1)
        v[i] = 1
        return v

    a_b = [e((i + 1) % 4) - e(i % 4) - e(8 + i) for i in range(4)]
    a_m = [e(4 + (i + 1) % 4) - e(4 + i % 4) - e(8 + i) for i in range(4)]
    sel = [0, 2]
    H = 2 * sum((a_b[g] * a_b[g].T + a_m[g] * a_m[g].T for g in sel), sp.zeros(N, N))
    Dm = sp.zeros(4, N)
    for i in range(4):
        Dm[i, i] = 1
        Dm[i, 4 + i] = -1
    R = 2 * Dm.T * Dm
    npl = {g: (a_b[g] + a_m[g]) / (2 * sp.sqrt(2)) for g in sel}
    nmi = {g: (a_b[g] - a_m[g]) / 2 for g in sel}
    Zb = sp.Matrix.hstack((npl[0] - npl[2]) / sp.sqrt(2), nmi[0], nmi[2])
    Wb = sp.Matrix.hstack(*sp.GramSchmidt((Zb.T).nullspace(), orthonormal=True))
    xc = sp.Matrix([0] * 8 + [1] * 4)

    def to_mp(Mx: sp.Matrix) -> mp.matrix:
        return mp.matrix([[mp.mpf(sp.N(Mx[i, j], 170)) for j in range(Mx.shape[1])]
                          for i in range(Mx.shape[0])])

    return to_mp(H), to_mp(R), to_mp(Wb), to_mp(Zb), to_mp(xc)


H_M, R_EV, WB, ZB, XC = build_S0()
I12 = mp.eye(12)


def lambdas(T: mp.mpf) -> list[mp.mpf]:
    return [8 + T, 4 + 5 * T, 4 + 5 * T]


def xlog1p_gap(u: mp.mpf) -> mp.mpf:
    r"""u - log(1+u), with a series for tiny |u| (second formulation of the same scalar)."""
    if abs(u) < mp.mpf(10) ** -30:
        return u ** 2 / 2 - u ** 3 / 3 + u ** 4 / 4 - u ** 5 / 5
    return u - mp.log1p(u)


def H_block(t: mp.mpf, T: mp.mpf, s: mp.mpf) -> mp.mpf:
    r"""Formulation A: H(t) = sum_k (1/2)[u_k - log(1+u_k)]."""
    tot = mp.mpf(0)
    for lam in lambdas(T):
        u = mp.e ** (-2 * lam * t) * (s ** 2 * lam / T - 1)
        tot += xlog1p_gap(u) / 2
    return tot


_EIG: dict = {}


def H_full(t: mp.mpf, T: mp.mpf, s: mp.mpf) -> mp.mpf:
    r"""Formulation B: full 12-dim Gaussian conditioning, eigendecomposition of A_M."""
    A = H_M + T * (I12 + R_EV)
    key = mp.nstr(T, 40)
    if key not in _EIG:
        _EIG[key] = mp.eigsy(A)
    E, Q = _EIG[key]
    d_cov = [s ** 2 * mp.e ** (-2 * E[i] * t) + T / E[i] * (1 - mp.e ** (-2 * E[i] * t)) for i in range(12)]
    d_mean = [mp.e ** (-E[i] * t) for i in range(12)]
    Sig = Q * mp.diag(d_cov) * Q.T
    mean = Q * mp.diag(d_mean) * Q.T * XC
    B = mp.matrix(12, 12)
    for i in range(12):
        for j in range(9):
            B[i, j] = WB[i, j]
        for j in range(3):
            B[i, 9 + j] = ZB[i, j]
    Sp = B.T * Sig * B
    mp_ = B.T * mean
    Syy = Sp[0:9, 0:9]
    Szy = Sp[9:12, 0:9]
    Szz = Sp[9:12, 9:12]
    mz = mp_[9:12, 0]
    G = Szy * mp.inverse(Syy)
    Sc = Szz - G * Szy.T
    Emm = mz * mz.T + G * Szy.T
    KZ = ZB.T * A * ZB
    P = KZ / T
    PS = P * Sc
    tr = sum(PS[i, i] for i in range(3))
    trm = sum((P * Emm)[i, i] for i in range(3))
    return (tr - 3 - mp.log(mp.det(PS)) + trm) / 2


def point_seed_KL(t: mp.mpf, T: mp.mpf, lam: mp.mpf, z0: mp.mpf) -> mp.mpf:
    r"""One hidden coordinate from a Dirac initial value z0:
    KL(N(z0 a^{1/2}, (T/lam)(1-a)) || N(0,T/lam)) = (1/2)[-a - log(1-a) + lam a z0^2/T], a = e^{-2 lam t}."""
    a = mp.e ** (-2 * lam * t)
    return (-a - mp.log1p(-a) + lam * a * z0 ** 2 / T) / 2


def first_cross(f, lo: mp.mpf, hi: mp.mpf) -> mp.mpf:
    """Root of a function decreasing through zero on [lo,hi] by bisection (robust)."""
    assert f(lo) > 0 and f(hi) < 0
    for _ in range(600):
        mid = (lo + hi) / 2
        if f(mid) > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def fmt(x: mp.mpf, n: int = 8) -> str:
    return mp.nstr(x, n)


out: dict = {"task2": {}, "task3": {}, "task4": {}}
lines: list[str] = []


def say(s: str = "") -> None:
    print(s)
    lines.append(s)


# ---------------------------------------------------------------- task 2
say("TASK 2: Gaussian-surrogate forgetting curve of the held-M OU, mp.dps = 150")
say("H = mean discarded conditional KL (nats); ratio = T*H/exp(-8t); plateau ~ s^2(4+5T)")
scales = {"rho/sqrt48": RHO / mp.sqrt(48), "rho/sqrt14 (uniform-ball 2nd moment)": RHO / mp.sqrt(14), "rho": RHO}
for eps_s in ("1e-2", "1e-3", "1e-4"):
    eps = mp.mpf(eps_s)
    T = eps ** 8
    L = mp.log(1 / eps)
    times = {"L/4": L / 4, "L/2": L / 2, "L/2+1": L / 2 + 1, "L": L, "1.5L": 1.5 * L, "2L": 2 * L, "2L+1": 2 * L + 1}
    for sname, s in scales.items():
        say(f"\n eps={eps_s}  T={fmt(T,3)}  L=log(1/eps)={fmt(L,6)}  s={sname}={fmt(s,6)}  s^2(4+5T)={fmt(s**2*(4+5*T),6)}")
        say(f"  {'t':>7} {'t value':>10} {'H_A (block)':>16} {'T*H/e^-8t':>14} {'|H_A-H_B|/H_A':>14}")
        rows = {}
        for tn, tv in times.items():
            hA = H_block(tv, T, s)
            hB = H_full(tv, T, s)
            rel = abs(hA - hB) / hA
            ratio = T * hA / mp.e ** (-8 * tv)
            say(f"  {tn:>7} {fmt(tv,6):>10} {fmt(hA,8):>16} {fmt(ratio,8):>14} {fmt(rel,3):>14}")
            rows[tn] = {"t": fmt(tv, 10), "H": fmt(hA, 12), "T_H_over_e8t": fmt(ratio, 12), "relerr_A_vs_B": fmt(rel, 3)}
        t_one = first_cross(lambda x: H_block(x, T, s) - 1, mp.mpf(0), 3 * L)
        t_tenth = first_cross(lambda x: H_block(x, T, s) - mp.mpf("0.1"), mp.mpf(0), 3 * L)
        say(f"  H(t)=1 at t - L = {fmt(t_one - L, 8)};  H(t)=0.1 at t - L = {fmt(t_tenth - L, 8)};"
            f"  (1/8)log(4 s^2) = {fmt(mp.log(4*s**2)/8, 8)}")
        rows["t_H_eq_1_minus_L"] = fmt(t_one - L, 10)
        rows["t_H_eq_0.1_minus_L"] = fmt(t_tenth - L, 10)
        out["task2"][f"eps={eps_s},s={sname}"] = rows

# ---------------------------------------------------------------- task 3
say("\nTASK 3: first internal-threshold crossing on the center path and with hidden discrepancy")
say(" thresholds: belief KL=(r^b)^2/2 <= sqrt(T)=eps^4  <=>  |r^b| <= sqrt2 eps^2;"
    "  model KL=(r^m)^2/(2*1/2) <= eps^4  <=>  |r^m| <= eps^2")
say(" edge e: r^b = z_+ + z_1 + z_2, r^m = z_+ + z_1 - z_2 (exact, stage4_cycle_exact.py);"
    " center path z_+=-e^{-(8+T)t}, z_1=z_2=0")


for eps_s in ("1e-2", "1e-3", "1e-4"):
    eps = mp.mpf(eps_s)
    T = eps ** 8
    L = mp.log(1 / eps)
    lf, ls_ = 8 + T, 4 + 5 * T
    dlt = RHO / 4
    thr_b, thr_m = mp.sqrt(2) * eps ** 2, eps ** 2
    t_c_b = (4 * L - mp.log(2)) / (2 * lf)          # e^{-lf t} = sqrt2 eps^2
    t_c_m = 2 * L / lf                               # e^{-lf t} = eps^2
    t_h_b = mp.log(dlt / thr_b) / ls_                # dlt e^{-ls t} = sqrt2 eps^2
    t_h_m = mp.log(dlt / thr_m) / ls_                # dlt e^{-ls t} = eps^2
    # combined, worst sign for each channel (|r| = e^{-lf t} + dlt e^{-ls t} in the channel where signs agree)
    comb_same = lambda thr: first_cross(lambda x: mp.e ** (-lf * x) + dlt * mp.e ** (-ls_ * x) - thr, mp.mpf(0), 10 * L)
    t_comb_m = comb_same(thr_m)   # z_2 > 0 makes |r^m| the sum; then |r^b| = |dlt e^{-ls t} - e^{-lf t}| <= max, never binds
    t_comb_b = comb_same(thr_b)
    t_comb = max(t_comb_m, t_comb_b)  # sup over the sign of z_2 of the last crossing time
    # worst case over the whole initial ball |x0 - x_circ| < rho (noise-free):
    # sup |r^m(t)| = e^{-lf t} + rho sqrt(2 e^{-2 lf t} + e^{-2 ls t})
    ball = lambda thr, margin: first_cross(
        lambda x: mp.e ** (-lf * x) + RHO * mp.sqrt(2 * mp.e ** (-2 * lf * x) + mp.e ** (-2 * ls_ * x)) - (thr - margin),
        mp.mpf(0), 10 * L)
    noise_res = eps ** 2 / 8  # sqrt3 * delta_eps, delta_eps = eps^2/(8 sqrt3)
    t_ball_m = ball(thr_m, 0)
    t_ball_b = ball(thr_b, 0)
    t_ball_m_noise = ball(thr_m, noise_res)
    t_ball_b_noise = ball(thr_b, noise_res)
    # boundary clause: exterior belief KL > 1/2 <=> |r^b_ext| > 1; center path |r_ext| = e^{-Tt}(3/2 - e^{-8t}/2)
    t_bdry_center = mp.mpf(0)
    t_bdry_ball = first_cross(lambda x: (1 + mp.sqrt(3) * (RHO + eps ** 2 / (8 * mp.sqrt(3)))) -
                              mp.e ** (-T * x) * (mp.mpf(3) / 2 - mp.e ** (-8 * x) / 2), mp.mpf(0), mp.mpf(1))
    tau_center = t_c_m + 1
    tau_comb = max(t_comb, t_bdry_ball) + 1
    tau_ball = max(t_ball_m_noise, t_ball_b_noise, t_bdry_ball) + 1
    binds = "center-path common normal" if t_c_m >= t_h_m else "hidden n^- discrepancy"
    say(f"\n eps={eps_s}: L={fmt(L,6)}, L/4={fmt(L/4,6)}, L/2={fmt(L/2,6)}, t_eps=2L={fmt(2*L,6)}")
    say(f"  center path only:        belief crosses at {fmt(t_c_b,8)}, model at {fmt(t_c_m,8)} (model binds)")
    say(f"  hidden z_2(0)=rho/4 only: belief crosses at {fmt(t_h_b,8)}, model at {fmt(t_h_m,8)} (model binds)")
    say(f"  -> of the two single mechanisms, the later one is: {binds}")
    say(f"  superposed, worst sign:  model {fmt(t_comb_m,8)}, belief {fmt(t_comb_b,8)} -> internal crossing {fmt(t_comb,8)}")
    say(f"  worst case over ball |x0-x_circ|<rho (noise-free): model {fmt(t_ball_m,8)}, belief {fmt(t_ball_b,8)}")
    say(f"  worst case over ball with noise margin eps^2/8:   model {fmt(t_ball_m_noise,8)}, belief {fmt(t_ball_b_noise,8)}")
    say(f"  boundary clause |r_ext|>1: center path all t>0; ball+noise worst case after t={fmt(t_bdry_ball,6)}")
    say(f"  implied first qualifying completion time tau: center {fmt(tau_center,8)}, rho/4-seed {fmt(tau_comb,8)},"
        f" ball worst {fmt(tau_ball,8)};  L/2+1 = {fmt(L/2+1,8)}")
    # hidden information at tau for a Dirac seed z_2(0)=rho/4 (single coordinate, rate 4+5T)
    kl_seed = point_seed_KL(tau_comb, T, ls_, dlt)
    kl_seed_ball = point_seed_KL(tau_ball, T, ls_, RHO)
    say(f"  hidden KL at tau (Dirac seed z_2(0)=rho/4): {fmt(kl_seed,8)};  times eps^4: {fmt(kl_seed*eps**4,8)}")
    say(f"  hidden KL at ball-worst tau (Dirac seed z_2(0)=rho): {fmt(kl_seed_ball,8)};  times eps^4: {fmt(kl_seed_ball*eps**4,8)}")
    for sname, s in scales.items():
        say(f"  surrogate H at tau_(rho/4-seed) for s={sname}: {fmt(H_block(tau_comb, T, s),8)}")
    out["task3"][eps_s] = {
        "center_belief": fmt(t_c_b, 10), "center_model": fmt(t_c_m, 10),
        "hidden_rho4_belief": fmt(t_h_b, 10), "hidden_rho4_model": fmt(t_h_m, 10),
        "binding_single_mechanism": binds, "superposed_worst": fmt(t_comb, 10),
        "ball_worst_model": fmt(t_ball_m, 10), "ball_worst_belief": fmt(t_ball_b, 10),
        "ball_worst_model_noise": fmt(t_ball_m_noise, 10), "boundary_ball_noise": fmt(t_bdry_ball, 6),
        "tau_center": fmt(tau_center, 10), "tau_rho4_seed": fmt(tau_comb, 10), "tau_ball_worst": fmt(tau_ball, 10),
        "L_half_plus_1": fmt(L / 2 + 1, 10),
        "hidden_KL_at_tau_dirac_rho4": fmt(kl_seed, 10), "hidden_KL_at_tau_dirac_rho4_times_eps4": fmt(kl_seed * eps ** 4, 10),
        "hidden_KL_at_tau_ball_dirac_rho": fmt(kl_seed_ball, 10),
    }

# ---------------------------------------------------------------- task 3b
say("\nTASK 3b: which matched pair of S^(0) crosses first (noise-free), as a function of hidden initial data")
say(" edge e: r^b=z_++z_1+z_2, r^m=z_++z_1-z_2;  edge f: r^b=z_+-z_1+z_3, r^m=z_+-z_1-z_3;  z_+(0)=-1")


def last_exceed(zp0: mp.mpf, zh: mp.mpf, zn: mp.mpf, eps: mp.mpf) -> mp.mpf:
    """Last time at which a pair's belief or model KL exceeds sqrt(T), noise-free held flow."""
    T = eps ** 8
    lf, ls_ = 8 + T, 4 + 5 * T
    def g(x: mp.mpf) -> mp.mpf:
        cm = (zp0 + zh) * mp.e ** (-lf * x)
        nm = zn * mp.e ** (-ls_ * x)
        return max(abs(cm + nm) - mp.sqrt(2) * eps ** 2, abs(cm - nm) - eps ** 2)
    # g is eventually negative; scan then bisect the last sign change
    grid = [mp.mpf(k) / 200 for k in range(0, 200 * 8)]
    last = None
    for a_, b_ in zip(grid[:-1], grid[1:]):
        if g(a_) > 0 and g(b_) <= 0:
            last = (a_, b_)
    lo, hi = last
    for _ in range(300):
        mid = (lo + hi) / 2
        if g(mid) > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


for eps_s in ("1e-2", "1e-4"):
    eps = mp.mpf(eps_s)
    d = RHO / 4
    for (z1, z2, z3) in ((d, 0, 0), (-d, 0, 0), (0, d, 0), (0, 0, d), (d, 0, d), (-d, d, 0)):
        te = last_exceed(mp.mpf(-1), mp.mpf(z1), mp.mpf(z2), eps)
        tf = last_exceed(mp.mpf(-1), -mp.mpf(z1), mp.mpf(z3), eps)
        first = "{0,1} (edge e)" if te < tf else "{2,3} (edge f)"
        say(f"  eps={eps_s} (z1,z2,z3)(0)=({fmt(z1,3)},{fmt(z2,3)},{fmt(z3,3)}): t_e={fmt(te,10)}, t_f={fmt(tf,10)} -> first block {first}")

# ---------------------------------------------------------------- task 4
say("\nTASK 4: constants")


def hb(p: mp.mpf) -> mp.mpf:
    return -p * mp.log(p) - (1 - p) * mp.log1p(-p)


for eps_s in ("1e-2", "1e-3", "1e-4"):
    eps = mp.mpf(eps_s)
    T = eps ** 8
    L = mp.log(1 / eps)
    tstar = 2 * L + 1
    eT = mp.e ** (-1 / T)
    log10_eT = -1 / (T * mp.log(10))
    p_tilde = 73728 * eps ** 4 * tstar + 5 * tstar * eT
    p_eps = 73728 * eps ** 4 * tstar + 4 * tstar * eT
    eta = mp.mpf(9) / 2 * RHO ** 2 * eps ** 8 + 3 / (4 * (1 - mp.e ** -8)) * eps ** 32
    bound = (eta + hb(p_tilde)) / (1 - p_tilde)
    haz_pref = 4 * mp.sqrt(mp.mpf(8) / 3)
    ratio_lin = (mp.mpf(1) / 2 + eps * tstar / 2) / (mp.mpf(1) / 2 - eps * tstar / 2)
    ratio_exp = 2 * mp.e ** (eps * tstar) - 1
    ratio_H = 2 * mp.e ** 2 - 1  # on [0, 2/eps]
    # held-law hidden information bound of the proof at t_eps vs the surrogate value there
    held_bound_teps = 9 * RHO ** 2 / (2 * T) * mp.e ** (-8 * 2 * L) + 3 / (4 * (1 - mp.e ** -8)) * mp.e ** (-16 * 2 * L)
    # supplementary window constants for the following-window coupling
    per_unit_tube = 73728 * eps ** 4
    h_tube_01 = mp.mpf("0.1") / per_unit_tube - tstar
    delta = eps ** 2 / (8 * mp.sqrt(3))
    marg = mp.sqrt(3) * (RHO + delta)
    t_ext_13 = mp.log((mp.mpf(3) / 2 - mp.e ** (-8) / 2) / (mp.mpf(13) / 10 + marg)) / T  # after t>=1 approx, e^{-8t}<=e^{-8}
    t_ext_1 = mp.log((mp.mpf(3) / 2 - mp.e ** (-8) / 2) / (1 + marg)) / T
    say(f"\n eps={eps_s}: T={fmt(T,3)}, t*={fmt(tstar,10)}")
    say(f"  p_tilde = 73728 eps^4 t* + 5 t* e^(-1/T) = {fmt(p_tilde,12)}   (p_eps with 4: {fmt(p_eps,12)})")
    say(f"  log10 e^(-1/T) = {fmt(log10_eT,12)}")
    say(f"  eta_eps = {fmt(eta,12)};  proof's held bound at t_eps = {fmt(held_bound_teps,12)} (equal: {abs(held_bound_teps-eta) < mp.mpf(10)**-140})")
    say(f"  h_b(p_tilde) = {fmt(hb(p_tilde),12)} nats;  (eta + h_b(p_tilde))/(1 - p_tilde) = {fmt(bound,12)}")
    say(f"  hazard 4 sqrt(8/3) e^(-1/T): log10 = log10(4 sqrt(8/3)) + log10 e^(-1/T) = {fmt(mp.log10(haz_pref),8)} + ({fmt(log10_eT,20)})")
    say(f"  with learned-row ratio 1.23: log10 prefactor = {fmt(mp.log10(mp.mpf('1.23')*haz_pref),8)}; with 2e^2-1: {fmt(mp.log10(ratio_H*haz_pref),8)}")
    say(f"  row ratio on [0,t*]: linear bound {fmt(ratio_lin,10)}, exponential bound 2e^(eps t*)-1 = {fmt(ratio_exp,10)};"
        f" on [0,2/eps]: 2e^2-1 = {fmt(ratio_H,10)};  4*1.23 = 4.92 <= 5")
    say(f"  supplementary: Chebyshev tube failure per unit time 73728 eps^4 = {fmt(per_unit_tube,6)};"
        f" window h after t* with total bound 0.1: h = {fmt(h_tube_01,6)} (T^(-1/2) = {fmt(T**-0.5,6)})")
    say(f"  supplementary: center-path exterior residual minus sqrt3(rho+delta) stays >= 13/10 until t ~ {fmt(t_ext_13*T,6)}/T,"
        f" >= 1 until t ~ {fmt(t_ext_1*T,6)}/T")
    out["task4"][eps_s] = {
        "tstar": fmt(tstar, 12), "p_tilde": fmt(p_tilde, 14), "p_eps": fmt(p_eps, 14), "log10_e_minus_1_over_T": fmt(log10_eT, 14),
        "eta": fmt(eta, 14), "h_b_p_tilde": fmt(hb(p_tilde), 14), "eta_plus_hb_over_1_minus_p": fmt(bound, 14),
        "hazard_prefactor": fmt(haz_pref, 14), "log10_hazard": fmt(mp.log10(haz_pref) + log10_eT, 18),
        "row_ratio_linear_tstar": fmt(ratio_lin, 12), "row_ratio_exp_tstar": fmt(ratio_exp, 12), "row_ratio_2_over_eps": fmt(ratio_H, 12),
        "tube_failure_per_unit_time": fmt(per_unit_tube, 8), "h_window_tube_0.1": fmt(h_tube_01, 8),
        "t_ext_13_10_times_T": fmt(t_ext_13 * T, 8), "t_ext_1_times_T": fmt(t_ext_1 * T, 8),
    }

if __name__ == "__main__":
    with open("stage4_numeric_output.json", "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=1)
