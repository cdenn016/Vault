r"""Independent re-implementation (falsification pass) of the epistemic-niche candidate.

Written from the model description only; it does not import the investigator's core.py.

Niche of n agents, scalar world component eta ~ N(0, P0) renewed every episode.
Slot open (pi_i = 1): own reading s_i = eta + v_i, Var v_i = Rs.
Delivery: receiver i hears an open informative sender k as s_k + nu_ik, Var nu_ik = Rc (receiver-specific).
Exact posterior, precision Lambda_i = 1/P0 + pi_i/Rs + j_i/(Rs+Rc), j_i = number of open informative senders heard.
Belief mean m_i plus computation noise c_i (Var sig2); error e_i = m_i - eta.

World-conditional second moment (def:col-contrast, last sentence):
    Sigma^c = E[Cov(e | eta)] = E_{pi,U}[Cov(e | eta, pi, U)] + (1/P0) Cov_{pi,U}(1/Lambda),
since E[e_i | eta, pi, U] = -eta / (P0 Lambda_i) and E eta^2 = P0.

Attention: each receiver picks a kappa-subset T of a pool of `pool` others; the informative ones are the open
co-members (full model) or the open others (exchangeable medium). Softmax at precision g_att over subsets, with
EFE -I = f(pi_i/Rs + |T cap open|/(Rs+Rc)); g_att = inf is top-kappa with uniform ties, g_att = 0 is uniform.
Given j, the attended informative set is uniform among j-subsets of the open informative others.
"""
import itertools
import math
import numpy as np
from scipy.optimize import minimize_scalar


def finfo(x, P0: float):
    r"""EFE of an epistemic slot set with total data precision x: -I = -\tfrac12\ln(1+P_0x)."""
    return -0.5 * np.log1p(P0 * np.asarray(x, float))


def profiles(n: int) -> np.ndarray:
    return np.array(list(itertools.product([0, 1], repeat=n)), dtype=int)


def stationary_chain(n: int, Gfun, gamma: float):
    """(P4): one member chosen uniformly resamples with prob prop. to exp(-gamma G_i) (uniform habits).
    Gfun(i, x, S_others) -> member i's EFE of choosing x given the number of open others.
    Returns profiles, stationary law, max |detailed-balance flux asymmetry|."""
    profs = profiles(n)
    idx = {tuple(p): k for k, p in enumerate(profs)}
    M = len(profs)
    T = np.zeros((M, M))
    for k, p in enumerate(profs):
        for i in range(n):
            So = int(p.sum() - p[i])
            G = np.array([Gfun(i, x, So) for x in (0, 1)])
            w = np.exp(-gamma * (G - G.min()))
            w = w / w.sum()
            for x in (0, 1):
                q = p.copy()
                q[i] = x
                T[k, idx[tuple(q)]] += w[x] / n
    A = T.T - np.eye(M)
    A[-1, :] = 1.0
    b = np.zeros(M)
    b[-1] = 1.0
    v = np.linalg.solve(A, b)
    F = v[:, None] * T
    return profs, v, float(np.abs(F - F.T).max())


def j_law(pi_i: int, S_oth: int, pool: int, kappa: int, g_att: float, P0, Rs, Rc):
    """Law of the number j of open informative others attended, under softmax attention over kappa-subsets
    of `pool` others of which S_oth are open informative."""
    js = np.arange(0, min(kappa, S_oth) + 1)
    cnt = np.array([math.comb(S_oth, j) * math.comb(pool - S_oth, kappa - j) for j in js], float)
    if np.isinf(g_att):
        w = np.zeros(len(js))
        w[-1] = 1.0
        return js, w
    G = finfo(pi_i / Rs + js / (Rs + Rc), P0)
    lw = np.log(np.maximum(cnt, 1e-300)) - g_att * G
    lw[cnt == 0] = -np.inf
    w = np.exp(lw - lw.max())
    return js, w / w.sum()


def sigma_c(n: int, law: np.ndarray, pool: int, kappa: int, g_att: float, P0, Rs, Rc, sig2, mean_term=True):
    """Exact Sigma^c of one exchangeable block (attention independent across receivers given the profile)."""
    profs = profiles(n)
    Ecov = np.zeros((n, n))
    Eb = np.zeros(n)
    Ebb = np.zeros((n, n))
    for k, p in enumerate(profs):
        w = law[k]
        if w <= 0:
            continue
        S = int(p.sum())
        a = np.zeros(n)   # E[1{given open informative other in U_i} / Lambda_i]
        b = np.zeros(n)   # E[1 / Lambda_i]
        b2 = np.zeros(n)  # E[1 / Lambda_i^2]
        dvar = np.zeros(n)
        for i in range(n):
            So = S - p[i]
            js, pj = j_law(p[i], So, pool, kappa, g_att, P0, Rs, Rc)
            Lam = 1.0 / P0 + p[i] / Rs + js / (Rs + Rc)
            b[i] = np.sum(pj / Lam)
            b2[i] = np.sum(pj / Lam ** 2)
            a[i] = np.sum(pj * (js / max(So, 1)) / Lam) if So > 0 else 0.0
            dvar[i] = np.sum(pj * (p[i] / Rs + js / (Rs + Rc)) / Lam ** 2)
        C = np.zeros((n, n))
        for i in range(n):
            C[i, i] = dvar[i] + sig2
            for l in range(i + 1, n):
                shared = S - p[i] - p[l]          # open informative senders other than i and l
                val = Rs * shared * (a[i] / (Rs + Rc)) * (a[l] / (Rs + Rc))
                val += Rs * p[i] * (b[i] / Rs) * (a[l] / (Rs + Rc))
                val += Rs * p[l] * (b[l] / Rs) * (a[i] / (Rs + Rc))
                C[i, l] = C[l, i] = val
        Ecov += w * C
        Eb += w * b
        Ebb += w * (np.outer(b, b) - np.diag(b * b) + np.diag(b2))
    return Ecov + (mean_term / P0) * (Ebb - np.outer(Eb, Eb))


def sigma_c_fixedU(n: int, law: np.ndarray, U: list, P0, Rs, Rc, sig2):
    """Exact Sigma^c of one niche with a FIXED (quenched) attention set U[i] of co-members for each receiver."""
    profs = profiles(n)
    nv = n + n * n + n                      # v_k, nu_ik, c_i
    Ecov = np.zeros((n, n))
    Eb = np.zeros(n)
    Ebb = np.zeros((n, n))
    var = np.concatenate([np.full(n, Rs), np.full(n * n, Rc), np.full(n, sig2)])
    for k, p in enumerate(profs):
        w = law[k]
        if w <= 0:
            continue
        Gm = np.zeros((n, nv))
        inv = np.zeros(n)
        for i in range(n):
            heard = [j for j in U[i] if p[j] and j != i]
            Lam = 1.0 / P0 + p[i] / Rs + len(heard) / (Rs + Rc)
            inv[i] = 1.0 / Lam
            if p[i]:
                Gm[i, i] = 1.0 / (Lam * Rs)
            for j in heard:
                Gm[i, j] += 1.0 / (Lam * (Rs + Rc))
                Gm[i, n + i * n + j] = 1.0 / (Lam * (Rs + Rc))
            Gm[i, n + n * n + i] = 1.0
        Ecov += w * (Gm * var) @ Gm.T
        Eb += w * inv
        Ebb += w * np.outer(inv, inv)
    return Ecov + (Ebb - np.outer(Eb, Eb)) / P0


def is_diffusive(Pi, tol=1e-12):
    off = Pi - np.diag(np.diag(Pi))
    return bool(off.max() <= tol and Pi.sum(1).min() >= -tol), float(off.max())


def contrast(Pi: np.ndarray, C) -> float:
    r"""def:col-contrast: r(C) = xi_in / xi_out with xi_out = phi^T Pi phi and
    xi_in = min over f perp 1_C, supp f in C, of f^T (diag(eps) + L_C) f / f^T f."""
    C = list(C)
    n = len(C)
    eps = Pi.sum(1)
    A = -(Pi - np.diag(np.diag(Pi)))
    AC = A[np.ix_(C, C)]
    K = np.diag(eps[C]) + np.diag(AC.sum(1)) - AC
    phi = np.ones(n) / math.sqrt(n)
    xout = phi @ Pi[np.ix_(C, C)] @ phi
    # orthonormal basis of 1^perp via Householder-free construction (Helmert)
    Z = np.zeros((n, n - 1))
    for m in range(1, n):
        Z[:m, m - 1] = 1.0
        Z[m, m - 1] = -m
        Z[:, m - 1] /= np.linalg.norm(Z[:, m - 1])
    xin = np.linalg.eigvalsh(Z.T @ K @ Z).min()
    return float(xin / xout)


def all_regions(N: int):
    for r in range(2, N + 1):
        for C in itertools.combinations(range(N), r):
            yield C


def blockdiag(*Ms):
    n = sum(M.shape[0] for M in Ms)
    out = np.zeros((n, n))
    k = 0
    for M in Ms:
        d = M.shape[0]
        out[k:k + d, k:k + d] = M
        k += d
    return out


def agency(law: np.ndarray, profs: np.ndarray, P0, Rs, gmax=200.0):
    """def:agy-agency-index, one decision state, class: uniform product habits, psi = 0,
    belief N(., P0), slot likelihood N(eta, Rs), gamma_C in [0, gmax]."""
    S = profs.sum(1)
    GC = finfo(S / Rs, P0)
    P = law
    mk = P > 0
    M = len(P)
    den = float(np.sum(P[mk] * np.log(P[mk] * M)))

    def kl(g):
        lq = -g * GC
        lq = lq - np.log(np.sum(np.exp(lq - lq.max()))) - lq.max()
        return float(np.sum(P[mk] * (np.log(P[mk]) - lq[mk])))
    grid = np.linspace(0, gmax, 4001)
    vals = np.array([kl(g) for g in grid])
    g0 = grid[vals.argmin()]
    lo, hi = max(0.0, g0 - gmax / 4000), min(gmax, g0 + gmax / 4000)
    res = minimize_scalar(kl, bounds=(lo, hi), method="bounded", options={"xatol": 1e-12})
    num = min(res.fun, vals.min())
    return 1.0 - num / den, float(res.x), num, den
