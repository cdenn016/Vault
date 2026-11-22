r"""Check 5: clause-by-clause evaluation of the performative niche candidate PN.

PN: two niches A = {0..3}, B = {4..7}; world components eta^A, eta^B independent AR(1) (F, Q);
members of niche k sense eta^k (noise R), relay raw observations to all niche-mates (receiver-specific
noise Rc), run the exact steady-state Kalman filter, act on eta^k with u_j = -g m_j^+ (deterministic),
and read their niche's realized total act exactly (A1).  No channel between niches.

Declared expectations:
 (C1) Pi^c block diagonal, each block compound symmetric, diffusive, r(A) = closed form; the collectives
      at level r0 are exactly A and B for max(r_sub, rbar_hom) < r0 <= r(A) (enumeration of all regions).
 (CL) The collective average of a niche is exactly closed given its blanket path (column sums of the
      interior update equal), so d_cl = d_M = 0; the inference tolerance alpha_I (expected relative
      entropy between N(mbar, P^-) and the union-model predictive law) is positive and is computed.
 (NE) N_eff (acts' effect on eta replaced by exogenous forcing): collider removed, closed-loop feedback
      kept; contrast rises to r_eff = closed form with s = 0.
 (NI) N_inf (others' acts unreadable; member models them as -g m_i^+): contrast changes; computed.
 (AG) Agency index of the act component at decision states (uniform habits held fixed, gamma_C >= 0
      free): close to 1 when the disagreement is small; computed over 200 draws.
"""
import itertools
import numpy as np
from pc import world_conditional_cov, diffusivity, contrast, exch_closed_form, riccati_scalar
from pcg import build

F, Q, R, Rc, b, g = 0.9, 0.05, 1.0, 0.2, 0.2, 0.15
n = 4
N = 2 * n
A_ = list(range(n)); B_ = list(range(n, N))


def pn_spec(g=g, F=F, Q=Q, R=R, Rc=Rc, b=b, known=True, mu=0.0):
    comp = [0] * n + [1] * n
    reads = [[j for j in (A_ if i < n else B_) if j != i] for i in range(N)]
    Rcd = {(i, j): Rc for i in range(N) for j in reads[i]}
    kn = [set(A_) if i < n else set(B_) for i in range(N)] if known else [set([i]) for i in range(N)]
    return {"F": [F, F], "Qw": [Q, Q], "comp": comp, "R": [R] * N, "reads": reads, "Rc": Rcd,
            "act": comp[:], "g": [g] * N, "b": b, "known": kn, "mu": [mu] * N}


def regions_report(Pi, rbar):
    best = {}
    for m in range(2, N + 1):
        for C in itertools.combinations(range(N), m):
            c = contrast(Pi, list(C))
            best[C] = c["r"]
    top = sorted(best.items(), key=lambda kv: -kv[1])[:6]
    return top


def mean_coupling_baseline(Pi):
    a = -(Pi - np.diag(np.diag(Pi)))
    abar = a[np.triu_indices(N, 1)].mean(); epsbar = Pi.sum(axis=1).mean()
    return 1 + N * abar / epsbar


if __name__ == "__main__":
    print("== (C1) collective clause at the base point ==")
    m = build(pn_spec())
    Sc = world_conditional_cov(m["A"], m["Qx"], m["iw"], m["ia"], 120)
    Pi = np.linalg.inv(Sc)
    dif = diffusivity(Pi)
    cf = exch_closed_form(n, F, Q, R, Rc, b, g)
    cA = contrast(Pi, A_)
    rbar = mean_coupling_baseline(Pi)
    eps = Pi.sum(axis=1)
    a_in = -Pi[0, 1]
    r_sub = (eps[0] + (n - 1) * a_in) / (eps[0] + a_in)
    print("  diffusive=%s max cross |Pi_AB|=%.2e  r(A)=%.6f (closed form %.6f)  phi_cl=%.3f s=%.4f" % (
        dif["diffusive"], np.abs(Pi[np.ix_(A_, B_)]).max(), cA["r"], cf["r"], cf["phi_cl"], cf["s"]))
    cf0 = exch_closed_form(n, F, Q, R, Rc, b, 0.0)
    print("  no-act contrast r_0 = %.6f; act factor D = r/r_0 = %.6f" % (cf0["r"], cf["r"] / cf0["r"]))
    print("  leak eps=%.5f coupling a=%.5f  r_sub=%.5f  rbar_hom(mean coupling, clause c)=%.5f  eps_max/eps_mean=%.6f" % (
        eps[0], a_in, r_sub, rbar, eps[A_].max() / eps[A_].mean()))
    print("  admissible window for 'collectives = {A,B}': (%.5f, %.5f]  significance r/rbar = %.4f" % (max(r_sub, rbar), cA["r"], cA["r"] / rbar))
    top = regions_report(Pi, rbar)
    print("  top regions by contrast:", [(C, round(r, 5)) for C, r in top])

    print("== (CL) closure of the collective average ==")
    Pm, Pp = riccati_scalar(F, Q, 1 / R + (n - 1) / (R + Rc))
    Ks, Kc = Pp / R, Pp / (R + Rc)
    c0 = 1 - Ks - (n - 1) * Kc
    # interior update given blanket path: m' = F c0 m + inputs (acts and sensory/relay inputs are blanket or noise)
    Aint = F * c0 * np.eye(n)
    print("  interior update column sums:", np.round(Aint.sum(axis=0), 12), "-> equal: average exactly closed (d_cl = 0)")
    # inference tolerance: members' predictive N(mbar, P^-) vs union predictive N(m_cent, Pc^-)
    Pcm, Pcp = riccati_scalar(F, Q, n / R)
    # error of mbar and of the centralized filter, jointly: stationary covariance via a small linear system
    # mbar error: ebar' = F[(c0) ebar + (Ks+(n-1)Kc) vbar + Kc nubar] - w ;  centralized: ec' = F[(1-n Kcent) ec + Kcent n vbar] - w
    Kcent = Pcp / R
    # state (ebar, ec), noises (vbar ~ N(0,R/n), nubar ~ N(0,(n-1)Rc/n), w ~ N(0,Q))
    Am = np.array([[F * c0, 0.0], [0.0, F * (1 - n * Kcent)]])
    Gm = np.array([[F * (Ks + (n - 1) * Kc) * np.sqrt(R / n), F * Kc * np.sqrt((n - 1) * Rc / n), -np.sqrt(Q)],
                   [F * Kcent * n * np.sqrt(R / n), 0.0, -np.sqrt(Q)]])
    from pc import stationary_cov
    S = stationary_cov(Am, Gm @ Gm.T)
    d2 = S[0, 0] - 2 * S[0, 1] + S[1, 1]  # E (mbar - m_cent)^2
    # KL(N(mbar,Pm) || N(mc,Pcm)) expected and KL(N(mc,Pcm) || N(mbar,Pm)) expected
    kl1 = 0.5 * (Pm / Pcm - 1 + np.log(Pcm / Pm) + d2 / Pcm)
    kl2 = 0.5 * (Pcm / Pm - 1 + np.log(Pm / Pcm) + d2 / Pm)
    print("  P^-(member)=%.5f  P^-(union)=%.5f  E(mbar-m_union)^2=%.3e  true MSE(mbar)=%.5f" % (Pm, Pcm, d2, S[0, 0]))
    print("  alpha_I (expected KL(belief||union)) = %.4e ; reverse direction %.4e" % (kl1, kl2))

    print("== (NE) N_eff and (NI) N_inf ==")
    sx, sp_ = cf["sx"], cf["sp"]
    phi = cf["phi_cl"]
    v_eff = phi ** 2 * sx / (1 - (c0 * phi) ** 2)
    r_eff = v_eff / cf["alpha"]
    print("  N_eff: r_eff = %.5f (full r = %.5f); mean-coupling baseline of the null = %.5f" % (
        r_eff, cf["r"], 1 + 2 * (n - 1) * (r_eff - 1) / (2 * n - 1)))
    # N_inf variant 1: member reads only its own act, models others' acts as -g m_i^+ (Riccati with Feff)
    sp = pn_spec(known=False, mu=1.0)
    mi = build(sp)
    Sci = world_conditional_cov(mi["A"], mi["Qx"], mi["iw"], mi["ia"], 120)
    Pii = np.linalg.inv(Sci)
    di = diffusivity(Pii)
    ri = contrast(Pii, A_)["r"] if di["diffusive"] else float("nan")
    print("  N_inf (others' acts modeled as -g m_i^+): diffusive=%s r(A)=%.5f  null baseline=%.5f" % (
        di["diffusive"], ri, mean_coupling_baseline(Pii) if di["diffusive"] else float("nan")))
    # N_inf variant 2: member ignores others' acts (mu = 0)
    sp = pn_spec(known=False, mu=0.0)
    mi = build(sp)
    Sci = world_conditional_cov(mi["A"], mi["Qx"], mi["iw"], mi["ia"], 120)
    Pii = np.linalg.inv(Sci)
    di = diffusivity(Pii)
    ri = contrast(Pii, A_)["r"] if di["diffusive"] else float("nan")
    print("  N_inf (others' acts ignored): diffusive=%s r(A)=%.5f  null baseline=%.5f" % (
        di["diffusive"], ri, mean_coupling_baseline(Pii) if di["diffusive"] else float("nan")))

    print("== (AG) agency index of the act component (declared discrete deliberation model) ==")
    rng = np.random.default_rng(1)
    U = [-1.0, 0.0, 1.0]
    prof = np.array(list(itertools.product(U, repeat=n)))  # (81, n)
    Lam, gam = 4.0, 2.0
    alpha_dis = cf["alpha"]  # variance of each disagreement mode
    Z = np.linalg.qr(np.column_stack([np.ones(n) / 2, rng.standard_normal((n, n - 1))]))[0][:, 1:]
    idx = []
    for draw in range(200):
        mC = 0.3
        dev = Z @ (np.sqrt(alpha_dis) * rng.standard_normal(n - 1))
        mi_ = mC + dev
        z = F * mi_; zC = F * mC
        tot = b * prof.sum(axis=1)
        GC = 0.5 * Lam * (zC + tot) ** 2
        tilt = (Lam * b * (z - zC)[None, :] * prof).sum(axis=1)
        logp = -gam * (GC + tilt); p = np.exp(logp - logp.max()); p /= p.sum()
        E = np.full(len(prof), 1.0 / len(prof))
        den = np.sum(p * np.log(p / E))
        best = np.inf
        for gC in np.linspace(0, 6, 601):
            lq = -gC * GC; q = np.exp(lq - lq.max()); q /= q.sum()
            best = min(best, np.sum(p * np.log(p / q)))
        idx.append(1 - best / den)
    idx = np.array(idx)
    print("  disagreement sd per mode = %.4f; agency index over 200 decision states: min %.4f median %.4f max %.4f" % (
        np.sqrt(alpha_dis), idx.min(), np.median(idx), idx.max()))
    # negative control: large disagreement (x30 sd) must lower the index
    idx2 = []
    for draw in range(50):
        dev = Z @ (30 * np.sqrt(alpha_dis) * rng.standard_normal(n - 1)); mi_ = 0.3 + dev
        z = F * mi_; zC = F * 0.3
        tot = b * prof.sum(axis=1); GC = 0.5 * Lam * (zC + tot) ** 2
        tilt = (Lam * b * (z - zC)[None, :] * prof).sum(axis=1)
        logp = -gam * (GC + tilt); p = np.exp(logp - logp.max()); p /= p.sum()
        den = np.sum(p * np.log(p * len(prof)))
        best = np.inf
        for gC in np.linspace(0, 6, 601):
            lq = -gC * GC; q = np.exp(lq - lq.max()); q /= q.sum()
            best = min(best, np.sum(p * np.log(p / q)))
        idx2.append(1 - best / den)
    print("  NEG (30x disagreement): agency index median %.4f (must be lower)" % np.median(idx2))
