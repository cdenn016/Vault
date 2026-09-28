r"""Independent (Fable 5.1) numerical recheck: Gaussian-surrogate hidden KL and constants.

Held-M OU process dX = -K_M X dt + sqrt(2T) dW from N(x_circ, s^2 I).
Hidden block of K_M has eigenvalues (8+T, 4+5T, 4+5T); P_Z x_circ = 0 and K_M is
block diagonal on W_M + Z_M, so the hidden marginal is N(0, C(t)) with
C_k(t) = s^2 e^{-2 lambda_k t} + (T/lambda_k)(1 - e^{-2 lambda_k t}),
and the conditional law of z given the retained path equals this marginal.
Against kappa = N(0, T K_Z^{-1}),
    H(t) = sum_k (1/2)[u_k - log(1+u_k)],  u_k = e^{-2 lambda_k t}(s^2 lambda_k / T - 1).

Second formulation (independent of the eigen-closed form): build K_M as a 12x12
matrix, propagate mean and covariance with mpmath expm, condition z on y in an
explicit orthonormal (W|Z) basis, and average the Gaussian KL over y.
"""
from __future__ import annotations

import json
import mpmath as mp

mp.mp.dps = 110

N = 12


def a_b(i: int) -> mp.matrix:
    v = mp.zeros(N, 1)
    v[(i + 1) % 4] += 1
    v[i] -= 1
    v[8 + i] -= 1
    return v


def a_m(i: int) -> mp.matrix:
    v = mp.zeros(N, 1)
    v[4 + (i + 1) % 4] += 1
    v[4 + i] -= 1
    v[8 + i] -= 1
    return v


def build(T: mp.mpf, sel=(0, 2)):
    e, f = sel
    H = mp.zeros(N, N)
    for g in sel:
        H += 2 * (a_b(g) * a_b(g).T + a_m(g) * a_m(g).T)
    Dm = mp.zeros(4, N)
    for i in range(4):
        Dm[i, i] = 1
        Dm[i, 4 + i] = -1
    R = 2 * Dm.T * Dm
    K = H + T * (mp.eye(N) + R)
    n_plus = {g: (a_b(g) + a_m(g)) / (2 * mp.sqrt(2)) for g in sel}
    n_minus = {g: (a_b(g) - a_m(g)) / 2 for g in sel}
    u1 = (n_plus[e] - n_plus[f]) / mp.sqrt(2)
    Zb = [u1, n_minus[e], n_minus[f]]
    # Orthonormal basis of W = Z^perp by Gram-Schmidt on the standard basis
    basis = list(Zb)
    Wb = []
    for i in range(N):
        v = mp.zeros(N, 1)
        v[i] = 1
        for b in basis:
            v -= (b.T * v)[0] * b
        nv = mp.norm(v)
        if nv > mp.mpf("1e-50"):
            v = v / nv
            basis.append(v)
            Wb.append(v)
    assert len(Wb) == 9, len(Wb)
    Q = mp.zeros(N, N)  # columns: W (9) then Z (3)
    for j, b in enumerate(Wb + Zb):
        for i in range(N):
            Q[i, j] = b[i]
    return K, Q


def H_closed(eps, s, t):
    T = mp.mpf(eps) ** 8
    lams = [8 + T, 4 + 5 * T, 4 + 5 * T]
    tot = mp.mpf(0)
    for lam in lams:
        u = mp.exp(-2 * lam * t) * (mp.mpf(s) ** 2 * lam / T - 1)
        tot += (u - mp.log1p(u)) / 2
    return tot


def H_full(eps, s, t):
    """Full 12-d propagation and explicit conditioning (second formulation)."""
    T = mp.mpf(eps) ** 8
    s = mp.mpf(s)
    K, Q = build(T)
    E = mp.expm(-K * t)
    E2 = mp.expm(-2 * K * t)
    Kinv = mp.inverse(K)
    Sigma = E * (s ** 2 * mp.eye(N)) * E.T + T * Kinv * (mp.eye(N) - E2)
    x_circ = mp.zeros(N, 1)
    for i in range(8, 12):
        x_circ[i] = 1
    mu = E * x_circ
    # rotate to (y, z) coordinates
    S = Q.T * Sigma * Q
    mu_r = Q.T * mu
    Syy = S[0:9, 0:9]
    Szz = S[9:12, 9:12]
    Szy = S[9:12, 0:9]
    Kz = (Q.T * K * Q)[9:12, 9:12]
    P = Kz / T  # precision of kappa
    A = Szy * mp.inverse(Syy)  # regression matrix
    Sc = Szz - A * Szy.T  # conditional covariance (constant in y)
    cov_mu = A * Szy.T  # covariance of the conditional mean over y
    mu_z = mu_r[9:12, 0]
    val = (mp.fsum((P * Sc)[i, i] for i in range(3)) - 3 - mp.log(mp.det(P * Sc))
           + mp.fsum((P * cov_mu)[i, i] for i in range(3)) + (mu_z.T * P * mu_z)[0]) / 2
    return val, [Szy[i, j] for i in range(3) for j in range(9)], list(mu_z)



def bisect(f, a, b, iters: int = 400):
    """Bracketed bisection; f(a) and f(b) must differ in sign."""
    fa, fb = f(a), f(b)
    assert fa * fb < 0, (fa, fb)
    for _ in range(iters):
        c = (a + b) / 2
        fc = f(c)
        if fa * fc <= 0:
            b, fb = c, fc
        else:
            a, fa = c, fc
    return (a + b) / 2


rho = mp.mpf(1) / 100
results = {}
print("=== Gaussian-surrogate mean discarded hidden KL H(t), nats ===")
for eps in ["1e-2", "1e-3", "1e-4"]:
    L = mp.log(1 / mp.mpf(eps))
    for s_lab, s in [("rho/sqrt48", rho / mp.sqrt(48)), ("rho/sqrt14", rho / mp.sqrt(14)), ("rho", rho)]:
        for t_lab, tt in [("L/4", L / 4), ("L/2", L / 2), ("L/2+1", L / 2 + 1), ("L", L), ("2L=t_eps", 2 * L), ("2L+1=t*", 2 * L + 1)]:
            hc = H_closed(eps, s, tt)
            row = {"eps": eps, "s": s_lab, "t": t_lab, "t_value": mp.nstr(tt, 12), "H_closed": mp.nstr(hc, 12)}
            if eps == "1e-2" and t_lab in ("L/2+1", "2L=t_eps", "L", "L/2"):
                hf, szy, muz = H_full(eps, s, tt)
                rel = abs(hf - hc) / hc
                row["H_full"] = mp.nstr(hf, 12)
                row["rel_diff"] = mp.nstr(rel, 5)
                row["max_abs_Szy"] = mp.nstr(max(abs(v) for v in szy), 5)
                row["max_abs_mu_z"] = mp.nstr(max(abs(v) for v in muz), 5)
            T = mp.mpf(eps) ** 8
            row["T*H/exp(-8t)"] = mp.nstr(T * hc / mp.exp(-8 * tt), 8)
            results[f"{eps}|{s_lab}|{t_lab}"] = row
            print(row)

print("\n=== H = 1 crossing, t - L, and post-threshold asymptote ===")
for s_lab, s in [("rho/sqrt48", rho / mp.sqrt(48)), ("rho/sqrt14", rho / mp.sqrt(14)), ("rho", rho)]:
    for eps in ["1e-2", "1e-4"]:
        L = mp.log(1 / mp.mpf(eps))
        c = bisect(lambda tt: H_closed(eps, s, tt) - 1, L - 4, L + 1)
        print(f"s={s_lab} eps={eps}: H=1 at t-L = {mp.nstr(c - L, 8)}; leading-order (1/8)log(4s^2) = {mp.nstr(mp.log(4*s**2)/8, 8)}")
        HL = H_closed(eps, s, L)
        print(f"   H(L) = {mp.nstr(HL, 8)} vs 8 s^4 = {mp.nstr(8*s**4, 8)}; H(2L) = {mp.nstr(H_closed(eps, s, 2*L), 8)} vs 8 s^4 eps^16 = {mp.nstr(8*s**4*mp.mpf(eps)**16, 8)}")

print("\n=== Task 3 crossing times (noise-free held flow, model threshold |r^m| <= eps^2) ===")
for eps in ["1e-2", "1e-3", "1e-4"]:
    ep = mp.mpf(eps)
    T = ep ** 8
    L = mp.log(1 / ep)
    thr = ep ** 2
    t_center = mp.log(1 / thr) / (8 + T)
    delta = rho / 4
    t_hidden = mp.log(delta / thr) / (4 + 5 * T)
    t_super = bisect(lambda tt: mp.exp(-(8 + T) * tt) + delta * mp.exp(-(4 + 5 * T) * tt) - thr, mp.mpf('0.1'), mp.mpf(10))
    margin = thr / 8  # sqrt3 * delta_eps = eps^2/8
    t_ball = bisect(lambda tt: mp.exp(-(8 + T) * tt) + rho * mp.sqrt(2 * mp.exp(-2 * (8 + T) * tt) + mp.exp(-2 * (4 + 5 * T) * tt)) - (thr - margin), mp.mpf('0.1'), mp.mpf(10))
    tau_hidden = t_super + 1
    # Dirac seed z_2(0) = rho/4 hidden KL at tau (single coordinate lambda = 4+5T)
    lam = 4 + 5 * T
    a = mp.exp(-2 * lam * tau_hidden)
    kl_seed = (-a - mp.log1p(-a) + lam * a * delta ** 2 / T) / 2
    print(f"eps={eps}: center {mp.nstr(t_center,6)}, hidden rho/4 alone {mp.nstr(t_hidden,6)}, superposed {mp.nstr(t_super,6)}, ball+margin {mp.nstr(t_ball,6)}, L/2+1 = {mp.nstr(L/2+1,6)}")
    print(f"   tau = superposed+1 = {mp.nstr(tau_hidden,6)}; margin L/2+1-tau = {mp.nstr(L/2+1-tau_hidden,5)} (ball: {mp.nstr(L/2+1-(t_ball+1),5)})")
    print(f"   Dirac-seed hidden KL at tau: {mp.nstr(kl_seed,6)}; times eps^4: {mp.nstr(kl_seed*ep**4,6)}; 2e^-8 = {mp.nstr(2*mp.exp(-8),6)}")
    print(f"   Gaussian surrogate (s=rho/sqrt48) at tau: {mp.nstr(H_closed(eps, rho/mp.sqrt(48), tau_hidden),6)}")

print("\n=== Task 4 constants ===")
for eps in ["1e-2", "1e-3", "1e-4"]:
    ep = mp.mpf(eps)
    T = ep ** 8
    L = mp.log(1 / ep)
    tstar = 2 * L + 1
    p_eps = 73728 * ep ** 4 * tstar + 4 * tstar * mp.exp(-1 / T)
    eta = mp.mpf(9) / 2 * rho ** 2 * ep ** 8 + 3 / (4 * (1 - mp.exp(-8))) * ep ** 32
    hb = -p_eps * mp.log(p_eps) - (1 - p_eps) * mp.log(1 - p_eps)
    comb = (eta + hb) / (1 - p_eps)
    log10pref = mp.log10(4 * mp.sqrt(mp.mpf(8) / 3))
    log10exp = -1 / T / mp.log(10)
    print(f"eps={eps}: t*={mp.nstr(tstar,7)} p_eps={mp.nstr(p_eps,6)} eta={mp.nstr(eta,4)} h_b={mp.nstr(hb,6)} (eta+h_b)/(1-p)={mp.nstr(comb,6)} log10(4sqrt(8/3)e^-1/T) = {mp.nstr(log10pref,5)} + {mp.nstr(log10exp,17)}")
    # row ratio bounds at mobility eps: linear (1+eps t)/(1-eps t) and exponential 2e^{eps t}-1
    lin = (1 + ep * tstar) / (1 - ep * tstar)
    expo = 2 * mp.exp(ep * tstar) - 1
    print(f"   row ratio on [0,t*]: linear {mp.nstr(lin,5)}, exponential {mp.nstr(expo,5)}; on [0,2/eps] exponential {mp.nstr(2*mp.exp(2)-1,5)}")

with open("fable_recheck_numeric_output.json", "w", encoding="utf-8") as fh:
    json.dump(results, fh, indent=1)
