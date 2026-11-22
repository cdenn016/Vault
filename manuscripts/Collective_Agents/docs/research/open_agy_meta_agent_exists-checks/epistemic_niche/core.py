r"""Epistemic-niche meta-agent construction, episode clock (one sensing round + one delivery round).

Niche of m members. World component eta ~ N(0, P0), renewed every episode, independent across niches.
Member i opens its slot (pi_i = 1) -> own reading o_i = eta + v_i, Var v_i = s (its private sensing noise).
Messages carry raw readings; receiver i hears open sender j as o_j + nu_ij, Var nu_ij = c (receiver-specific).
Exact Gaussian posterior of member i with n_ch received channels:
    P_i = (1/P0 + pi_i/s + n_ch/(s+c))^{-1},   e_i = m_i - eta.
World-conditional second moment (def:col-contrast, last sentence):
    Sigma^c = E_{pi,U}[Cov(e | eta, pi, U)] + Cov_{pi,U}(P)/P0 + s2comp * I,
because E[e_i | eta, pi, U] = -P_i eta / P0 and E[eta^2] = P0.
"""
import itertools
import numpy as np
from scipy.optimize import minimize_scalar


def profiles(m: int) -> np.ndarray:
    return np.array(list(itertools.product([0, 1], repeat=m)), dtype=int)


def f_info(x, P0: float):
    r"""Expected free energy of receiving precision x about eta ~ N(.,P0): -I = -\tfrac12\ln(1+P_0x)."""
    return -0.5 * np.log1p(P0 * np.asarray(x, float))


def deliberation_law(m, kappa, P0, s, c, gamma):
    r"""P^\infty(\pi) \propto \exp(-\gamma g(S)), uniform product habits, exact potential
    g(S+1)-g(S) = f(1/s + min(kappa,S)/(s+c)) - f(min(kappa,S)/(s+c))."""
    profs = profiles(m)
    g = np.zeros(m + 1)
    for S in range(m):
        k = min(kappa, S)
        g[S + 1] = g[S] + f_info(1.0 / s + k / (s + c), P0) - f_info(k / (s + c), P0)
    lw = -gamma * g[profs.sum(1)]
    w = np.exp(lw - lw.max())
    return w / w.sum(), g


def chain_law(m, kappa, P0, s, c, gamma, a_own=None):
    """Stationary law of protocol (P4) built from the members' own EFEs, and max detailed-balance violation.
    a_own: per-member own-slot precision (heterogeneous values are a negative control)."""
    profs = profiles(m)
    M = len(profs)
    idx = {tuple(p): k for k, p in enumerate(profs)}
    a_own = np.full(m, 1.0 / s) if a_own is None else np.asarray(a_own, float)
    T = np.zeros((M, M))
    for k, p in enumerate(profs):
        for i in range(m):
            nch = min(kappa, p.sum() - p[i])
            G = np.array([f_info(a_own[i] * x + nch / (s + c), P0) for x in (0, 1)])
            pr = np.exp(-gamma * (G - G.min()))
            pr /= pr.sum()
            for x in (0, 1):
                q = p.copy()
                q[i] = x
                T[k, idx[tuple(q)]] += pr[x] / m
    w, V = np.linalg.eig(T.T)
    v = np.real(V[:, np.argmin(np.abs(w - 1))])
    v = v / v.sum()
    F = v[:, None] * T
    return v, float(np.abs(F - F.T).max())


def sigma_c_enum(m, prof_law, att_fn, P0, s, c, s2comp=0.0, mean_var=True):
    """Exact Sigma^c of one niche; att_fn(i, p) -> list of (tuple of attended co-members, prob),
    attention independent across receivers given the profile p."""
    profs = profiles(m)
    En = np.zeros((m, m)); EP = np.zeros(m); EPP = np.zeros((m, m))
    for k, p in enumerate(profs):
        w = prof_law[k]
        if w <= 0:
            continue
        op = p.astype(bool)
        recs = []
        for i in range(m):
            lst = []
            for U, pu in att_fn(i, p):
                mk = np.zeros(m, bool)
                mk[list(U)] = True
                mk &= op
                mk[i] = False
                Pi = 1.0 / (1.0 / P0 + p[i] / s + mk.sum() / (s + c))
                lst.append((mk, pu, Pi))
            recs.append(lst)
        for i in range(m):
            for mk, pu, Pi in recs[i]:
                En[i, i] += w * pu * Pi ** 2 * (p[i] / s + mk.sum() / (s + c))
                EP[i] += w * pu * Pi
                EPP[i, i] += w * pu * Pi ** 2
        for i in range(m):
            for l in range(i + 1, m):
                acc = accPP = 0.0
                for mi, pui, Pi in recs[i]:
                    for ml, pul, Pl in recs[l]:
                        sh = mi & ml
                        sh[i] = False
                        sh[l] = False
                        # int(): numpy bool + bool is logical or, which undercounts (bug found in explore2)
                        term = (int(ml[i]) + int(mi[l])) / (s + c) + s * int(sh.sum()) / (s + c) ** 2
                        acc += pui * pul * Pi * Pl * term
                        accPP += pui * pul * Pi * Pl
                En[i, l] += w * acc; En[l, i] += w * acc
                EPP[i, l] += w * accPP; EPP[l, i] += w * accPP
    return En + mean_var * (EPP - np.outer(EP, EP)) / P0 + s2comp * np.eye(m)


def sigma_c_capacity(m, prof_law, kappa, P0, s, c, s2comp=0.0, mean_var=True):
    """Exact Sigma^c when each receiver attends min(kappa, #open others) open others uniformly
    (EFE ties), independently across receivers given the profile."""
    profs = profiles(m)
    En = np.zeros((m, m)); EP = np.zeros(m); EPP = np.zeros((m, m))
    for k, p in enumerate(profs):
        w = prof_law[k]
        if w <= 0:
            continue
        S = p.sum()
        Sm = S - p
        nch = np.minimum(kappa, Sm)
        q = np.where(Sm > 0, nch / np.maximum(Sm, 1), 0.0)
        P = 1.0 / (1.0 / P0 + p / s + nch / (s + c))
        for i in range(m):
            En[i, i] += w * P[i] ** 2 * (p[i] / s + nch[i] / (s + c))
            for l in range(i + 1, m):
                nsh = S - p[i] - p[l]
                term = (p[i] * q[l] + p[l] * q[i]) / (s + c) + s * q[i] * q[l] * nsh / (s + c) ** 2
                En[i, l] += w * P[i] * P[l] * term
                En[l, i] = En[i, l]
        EP += w * P
        EPP += w * np.outer(P, P)
    return En + mean_var * (EPP - np.outer(EP, EP)) / P0 + s2comp * np.eye(m)


def diffusive(Pi, tol=1e-12):
    off = Pi - np.diag(np.diag(Pi))
    return bool(off.max() <= tol and Pi.sum(1).min() >= -tol), float(off.max()), float(Pi.sum(1).min())


def contrast(Pi, C):
    r"""r(C) = xi_in/xi_out of def:col-contrast on the whole-population precision Pi."""
    C = np.asarray(C)
    n = len(C)
    eps = Pi.sum(1)
    a = -(Pi - np.diag(np.diag(Pi)))
    aC = a[np.ix_(C, C)]
    Mc = np.diag(eps[C]) + np.diag(aC.sum(1)) - aC
    xout = Pi[np.ix_(C, C)].sum() / n
    Q, _ = np.linalg.qr(np.column_stack([np.ones(n), np.eye(n)[:, : n - 1]]))
    Z = Q[:, 1:]
    return float(np.linalg.eigvalsh(Z.T @ Mc @ Z).min() / xout)


def region_contrasts(Pi):
    N = Pi.shape[0]
    return {C: contrast(Pi, C) for r in range(2, N + 1) for C in itertools.combinations(range(N), r)}


def block_diag(*Ms):
    n = sum(M.shape[0] for M in Ms)
    out = np.zeros((n, n)); k = 0
    for M in Ms:
        d = M.shape[0]; out[k:k + d, k:k + d] = M; k += d
    return out


def agency_index(lawP, m, P0, s, gC_max=200.0):
    r"""def:agy-agency-index with class {uniform product habits, belief N(.,P0), psi=0, slot likelihood N(eta,s),
    gamma_C in [0,gC_max]} (gamma_C = 0 is the habit-only model)."""
    profs = profiles(m)
    GC = f_info(profs.sum(1) / s, P0)
    P = np.asarray(lawP); mk = P > 0
    den = float(np.sum(P[mk] * (np.log(P[mk]) + m * np.log(2.0))))

    def kl(gC):
        lg = -gC * GC
        lg = lg - (np.log(np.exp(lg - lg.max()).sum()) + lg.max())
        return float(np.sum(P[mk] * (np.log(P[mk]) - lg[mk])))

    res = minimize_scalar(kl, bounds=(0.0, gC_max), method="bounded", options={"xatol": 1e-12})
    return 1.0 - res.fun / den, float(res.x), float(res.fun), den, kl


def inference_kl(m, prof_law, P0, s, c, s2comp=0.0):
    r"""E KL( N(mbar, Pbar) || N(m*, P*) ): encoded belief = members' average mean with average claimed variance,
    union posterior from all open slot readings (exterior-facing sensations)."""
    profs = profiles(m); tot = 0.0
    for k, p in enumerate(profs):
        w = prof_law[k]
        if w <= 0:
            continue
        S = p.sum(); Sm = S - p
        P = 1.0 / (1.0 / P0 + p / s + Sm / (s + c))
        Ps = 1.0 / (1.0 / P0 + S / s)
        ce = np.mean(P * (p / s + Sm / (s + c))) - Ps * S / s
        var = ce ** 2 * P0
        for j in range(m):
            if p[j]:
                cj = (P[j] / s + (P.sum() - P[j]) / (s + c)) / m - Ps / s
                var += cj ** 2 * s
        var += np.sum((P / (m * (s + c))) ** 2 * c * Sm) + s2comp / m
        Pb = P.mean()
        tot += w * 0.5 * (Pb / Ps - 1.0 - np.log(Pb / Ps) + var / Ps)
    return float(tot)
