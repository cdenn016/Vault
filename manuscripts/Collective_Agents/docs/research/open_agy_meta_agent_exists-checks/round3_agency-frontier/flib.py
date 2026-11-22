r"""Agency-frontier library (round 3): niche class with private slots, raw relays with one-round latency,
expected-free-energy attention under a message capacity, uniform habits on a declared support.

Model (one niche; niches are independent copies with independent world components, so the population's
world-conditional covariance is block diagonal over niches and the cross-niche block is exactly zero):
  world component   eta_{t+1} = F eta_t + w_t,  w ~ N(0, Q)
  member state      x_t = (eta_t, eta_{t-1}); prior N(m^-_i(t), P^-_i(t)); prior error e_i(t) = m^-_i(t) - x_t
  round-t data      own sensor s_i(t) = eta_t + v_i(t)                 (R),    always read
                    k_i(t) open private slots o = eta_t + rho          (Rs each), read by the owner only, not relayed
                    relay of attended mate j: s_j(t-1) + nu_ij(t)      (row [0,1], noise R + Rc; v_j(t-1) shared)
  exact Kalman update, prediction m^-(t+1) = A_F m^+(t) + xi,  xi ~ N(0, qc I_2),  A_F = [[F,0],[1,0]].
  EFE for the round-(t+1) policy, decided at the end of round t:
     G(c, k) = -I(x_{t+1}; own sensor + k slots + c relays) + psi k,   c = informative relays read.
  Policy of member i = (attention type, slot pattern); habits uniform on the declared attention support
  (types tau = (c_tau, mult_tau): mult_tau message sets with c_tau informative channels) times uniform on {0,1}^m.
Second-moment convention (def:col-contrast, 04_collectives.tex:187): Sigma^c = E[Cov(e(t) | eta)], estimated as
1/2 E[(e^1 - e^2)(e^1 - e^2)^T] over two replicas sharing the world innovations.
"""
from __future__ import annotations

import os
for _v in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS"):
    os.environ.setdefault(_v, "1")
from dataclasses import dataclass, replace, field
from math import comb, lgamma, log
import itertools

import numpy as np
from scipy.linalg import solve_discrete_lyapunov


@dataclass(frozen=True)
class Par:
    F: float = 0.9
    Q: float = 0.05
    R: float = 1.0
    Rc: float = 0.1
    Rs: float = 1.0          # noise of one private slot
    psi: float = 0.0         # pragmatic cost of one open slot (nats)
    gamma: float = 400.0
    qc: float = 1e-4
    n: int = 2               # members of the niche (or agents of the medium)
    n_zero: int = 2          # zero-gain message channels per member (the other niches' relays)
    m: int = 0               # private binary slots per member
    types: tuple = ((0, 1), (1, 1), (0, 2))   # declared attention support: (informative count, multiplicity)

    def with_(self, **kw) -> "Par":
        return replace(self, **kw)


def canonical_types(n_inf: int, n_zero: int, kmsg: int) -> tuple:
    r"""Uniform habits on all message sets of size <= kmsg among n_inf informative + n_zero zero-gain channels,
    grouped by (informative count c, zero count z): multiplicity C(n_inf,c) C(n_zero,z)."""
    out = []
    for c in range(0, min(kmsg, n_inf) + 1):
        for z in range(0, min(kmsg - c, n_zero) + 1):
            out.append((c, comb(n_inf, c) * comb(n_zero, z)))
    # merge equal c (EFE depends on c only)
    d: dict = {}
    for c, mu in out:
        d[c] = d.get(c, 0) + mu
    return tuple(sorted(d.items()))


AF0 = None


def A_F(F: float) -> np.ndarray:
    return np.array([[F, 0.0], [1.0, 0.0]])


def Pminus_from_post(par: Par, Pp00: float) -> np.ndarray:
    F = par.F
    return np.array([[F * F * Pp00 + par.Q + par.qc, F * Pp00], [F * Pp00, Pp00 + par.qc]])


def post(Pm: np.ndarray, a: float, b: float) -> np.ndarray:
    return np.linalg.inv(np.linalg.inv(Pm) + np.diag([a, b]))


def steady_prior(par: Par, c: int, k: int, iters: int = 3000) -> np.ndarray:
    r"""Claimed prior covariance P^- at the fixed point of a member reading c relays and k slots every round."""
    Pm = Pminus_from_post(par, 0.1)
    a = 1.0 / par.R + k / par.Rs
    b = c / (par.R + par.Rc)
    for _ in range(iters):
        Pp = post(Pm, a, b)
        Pm = Pminus_from_post(par, Pp[0, 0])
    return Pm


def info(Pm, a, b):
    r"""I(x; obs) = 1/2 ln det(I + P^- diag(a, b)) (broadcasts over a, b and over leading dims of Pm given as tuple)."""
    P00, P01, P11 = Pm
    return 0.5 * np.log((1 + a * P00) * (1 + b * P11) - a * b * P01 ** 2)


def efe_grid(par: Par, P00, P01, P11, cs: np.ndarray, ks: np.ndarray):
    r"""G[..., c, k] = -I(x_{t+1}; own + k slots + c relays) + psi k for arrays of prior entries."""
    a = 1.0 / par.R + ks[None, :] / par.Rs
    b = cs[:, None] / (par.R + par.Rc)
    p00 = np.asarray(P00)[..., None, None]
    p01 = np.asarray(P01)[..., None, None]
    p11 = np.asarray(P11)[..., None, None]
    I = 0.5 * np.log((1 + a * p00) * (1 + b * p11) - a * b * p01 ** 2)
    return -I + par.psi * ks[None, :]


def log_binom(m: int) -> np.ndarray:
    return np.array([lgamma(m + 1) - lgamma(k + 1) - lgamma(m - k + 1) for k in range(m + 1)])


# ---------------------------------------------------------------------------------------------------------------
# exact second moments for deterministic attention patterns (time-invariant gains)
# ---------------------------------------------------------------------------------------------------------------

def member_mats(par: Par, Pm: np.ndarray, c: int, k: int):
    a = 1.0 / par.R + k / par.Rs
    b = c / (par.R + par.Rc)
    Pp = post(Pm, a, b)
    Af = A_F(par.F)
    M = Af @ Pp @ np.linalg.inv(Pm)
    k_own = Af @ Pp[:, 0] / par.R
    k_slot = Af @ Pp[:, 0] / par.Rs
    k_rel = Af @ Pp[:, 1] / (par.R + par.Rc)
    return M, k_own, k_slot, k_rel, Pp


def exact_sigma_c(par: Par, att: np.ndarray, ks: np.ndarray, Pms: list | None = None, dead: bool = False):
    r"""World-conditional covariance of the prior errors (eta_t component) for a fixed attention matrix att[i, j]
    (i reads j's relay every round) and fixed open-slot counts ks[i], at the members' steady-state gains.
    State z = (e_1..e_n in R^2, u_1..u_n = v(t-1)); w is shared and conditioned on, so it is dropped.
    dead: relays carry pure noise (variance R + Rc) instead of the sender's reading (negative control / N_lp)."""
    n = att.shape[0]
    cs = att.sum(1).astype(int)
    if Pms is None:
        Pms = [steady_prior(par, int(cs[i]), int(ks[i])) for i in range(n)]
    D = 3 * n
    A = np.zeros((D, D))
    Bcols = []
    for i in range(n):
        M, k_own, k_slot, k_rel, _ = member_mats(par, Pms[i], int(cs[i]), int(ks[i]))
        A[2 * i:2 * i + 2, 2 * i:2 * i + 2] = M
        for j in range(n):
            if att[i, j] and not dead:
                A[2 * i:2 * i + 2, 2 * n + j] = k_rel
        # fresh noises of the round: v_i (shared with the u-slot), slots, relay channel noise (or dead content), xi
        col = np.zeros(D); col[2 * i:2 * i + 2] = k_own * np.sqrt(par.R); col[2 * n + i] = np.sqrt(par.R)
        Bcols.append(col)
        if ks[i] > 0:
            col = np.zeros(D); col[2 * i:2 * i + 2] = k_slot * np.sqrt(ks[i] * par.Rs); Bcols.append(col)
        if cs[i] > 0:
            var = (par.R + par.Rc) if dead else par.Rc
            col = np.zeros(D); col[2 * i:2 * i + 2] = k_rel * np.sqrt(cs[i] * var); Bcols.append(col)
        for d in range(2):
            col = np.zeros(D); col[2 * i + d] = np.sqrt(par.qc); Bcols.append(col)
    Bm = np.array(Bcols).T
    S = solve_discrete_lyapunov(A, Bm @ Bm.T)
    idx = [2 * i for i in range(n)]
    return S[np.ix_(idx, idx)], S, A


def compound(S: np.ndarray):
    n = S.shape[0]
    d = np.trace(S) / n
    o = (S.sum() - np.trace(S)) / (n * (n - 1))
    return d - o, o


def r_ab(n: int, al: float, be: float) -> float:
    return 1.0 + n * be / al


def contrast(Pi: np.ndarray, C) -> float:
    r"""r(C) of def:col-contrast (04_collectives.tex:182-188) on the whole-population precision Pi."""
    C = list(C)
    n = len(C)
    eps = Pi.sum(1)
    a = -(Pi - np.diag(np.diag(Pi)))
    aC = a[np.ix_(C, C)]
    Mx = np.diag(eps[C]) + np.diag(aC.sum(1)) - aC
    phi = np.ones(n) / np.sqrt(n)
    xout = float(phi @ Pi[np.ix_(C, C)] @ phi)
    Z = np.linalg.svd(np.eye(n) - np.outer(phi, phi))[0][:, : n - 1]
    xin = float(np.linalg.eigvalsh(Z.T @ Mx @ Z).min())
    return xin / xout


def is_diffusive(Pi: np.ndarray, tol: float = 1e-12):
    off = Pi - np.diag(np.diag(Pi))
    return bool(off.max() <= tol and Pi.sum(1).min() >= -tol), float(off.max()), float(Pi.sum(1).min())


def population_regions(al: float, be: float, n: int, niches: int = 2):
    r"""Population precision for `niches` independent exchangeable niches (alpha I + beta 11^T each) and the
    contrast of every region (for N <= 8 all regions; returned as dict size -> max over regions of that size,
    split into within-niche and niche-spanning)."""
    Sblk = al * np.eye(n) + be * np.ones((n, n))
    N = n * niches
    S = np.kron(np.eye(niches), Sblk)
    Pi = np.linalg.inv(S)
    out_in, out_span = {}, {}
    for size in range(2, N + 1):
        for C in itertools.combinations(range(N), size):
            r = contrast(Pi, C)
            span = len({c // n for c in C}) > 1
            d = out_span if span else out_in
            d[size] = max(d.get(size, -np.inf), r)
    return Pi, out_in, out_span


# ---------------------------------------------------------------------------------------------------------------
# exact second-moment recursion for the mechanism medium (each agent reads a fresh uniformly random c-subset of
# the other N-1 agents every round; all channels informative; fixed slot count)
# ---------------------------------------------------------------------------------------------------------------

def medium_exact(par: Par, N: int, c: int, k: int = 0, iters: int = 4000):
    r"""Exchangeable medium: diagonal block D and off-diagonal block O (2x2) of E[Cov(e | eta)].
    D' = M D M^T + c R k_rel k_rel^T + R k_own k_own^T + k Rs k_slot k_slot^T + c Rc k_rel k_rel^T + qc I
    O' = M O M^T + p R (M k_own k_rel^T + k_rel k_own^T M^T) + (N-2) p^2 R k_rel k_rel^T,   p = c/(N-1).
    Returns alpha, beta (eta_t component) and r_hom = 1 + N beta/alpha (whole medium)."""
    Pm = steady_prior(par, c, k)
    M, k_own, k_slot, k_rel, _ = member_mats(par, Pm, c, k)
    p = c / (N - 1)
    D = np.zeros((2, 2)); O = np.zeros((2, 2))
    R, Rc, Rs = par.R, par.Rc, par.Rs
    cD = c * R * np.outer(k_rel, k_rel) + R * np.outer(k_own, k_own) + k * Rs * np.outer(k_slot, k_slot) \
        + c * Rc * np.outer(k_rel, k_rel) + par.qc * np.eye(2)
    cO = p * R * (M @ np.outer(k_own, k_rel) + np.outer(k_rel, k_own) @ M.T) + (N - 2) * p * p * R * np.outer(k_rel, k_rel)
    for _ in range(iters):
        D = M @ D @ M.T + cD
        O = M @ O @ M.T + cO
    al = D[0, 0] - O[0, 0]
    be = O[0, 0]
    return al, be, r_ab(N, al, be)


# ---------------------------------------------------------------------------------------------------------------
# vectorized two-replica Monte Carlo
# ---------------------------------------------------------------------------------------------------------------

@dataclass
class MCOut:
    S: np.ndarray
    S_batches: np.ndarray
    open_rate: float
    mean_c: float
    inf: dict = field(default_factory=dict)


def mc(par: Par, mode: str, K: int, T: int, burn: int, seed: int, nbatch: int = 20,
       att_law: np.ndarray | None = None, slot_open_p: float | None = None, r_att: int | None = None,
       want_inf: bool = False, dead: bool = False, indep_world: bool = False) -> MCOut:
    r"""Two replicas per world path (shared w, independent private noises and policy draws).
    mode 'full'  : (type, k) ~ mult_tau C(m,k) exp(-gamma G(c_tau, k))  (members' policy posterior)
         'hab'   : gamma = 0: (type, k) ~ mult_tau C(m,k); att_law overrides the type law (habit mass per type)
         'pr'    : c ~ hypergeometric(n_inf=n-1, n_zero, r_att) every round; k ~ C(m,k) exp(-gamma G(c,k))
    slot_open_p: in 'hab', per-slot opening probability (default 1/2, uniform habits).
    dead: relays deliver pure noise (N_lp) ; indep_world: replicas get independent worlds (negative control)."""
    rng = np.random.default_rng(seed)
    n = par.n
    B = 2 * K
    types = np.array(par.types, dtype=float)
    tc = types[:, 0].astype(int)
    tmult = types[:, 1]
    cs = np.arange(0, n)                 # possible informative counts 0..n-1
    ks = np.arange(0, par.m + 1)
    lbin = log_binom(par.m)
    F = par.F
    # state
    P0 = steady_prior(par, int(tc.max()), 0)
    P00 = np.full((B, n), P0[0, 0]); P01 = np.full((B, n), P0[0, 1]); P11 = np.full((B, n), P0[1, 1])
    e0 = np.zeros((B, n)); e1 = np.zeros((B, n))
    u = np.zeros((B, n))
    att = np.zeros((B, n, n), dtype=bool)
    kk = np.zeros((B, n), dtype=int)
    eye = np.eye(n, dtype=bool)
    eU = np.zeros(B); UU = np.full(B, P0[0, 0])
    S_acc = np.zeros((K, n, n)); cnt = 0
    open_acc = 0.0; c_acc = 0.0
    inf_acc = dict(n=0, q=0.0, invU=0.0, lnU=0.0, dsq=0.0, claim=0.0, rev=0.0)
    Kw = B if indep_world else K
    for t in range(T):
        if t >= burn:
            d = e0[0::2] - e0[1::2]
            S_acc += 0.5 * d[:, :, None] * d[:, None, :]
            cnt += 1
            open_acc += kk.mean() / max(par.m, 1)
            c_acc += att.sum(2).mean()
            if want_inf:
                dy = e0.mean(1) - eU
                inf_acc["n"] += B
                inf_acc["q"] += np.sum(dy ** 2 / UU)
                inf_acc["invU"] += np.sum(1.0 / UU)
                inf_acc["lnU"] += np.sum(np.log(UU))
                inf_acc["dsq"] += np.sum(dy ** 2)
                vcl = P00.mean(1)
                rat = vcl / UU
                inf_acc["claim"] += np.sum(0.5 * (rat - 1 - np.log(rat)) + 0.5 * dy ** 2 / UU)
                inf_acc["rev"] += np.sum(0.5 * (UU / vcl - 1 - np.log(UU / vcl)) + 0.5 * dy ** 2 / vcl)
        # ---- data of round t (error form) ----
        v = np.sqrt(par.R) * rng.standard_normal((B, n))
        slot_term = np.sqrt(kk / par.Rs) * rng.standard_normal((B, n))         # sum rho / Rs
        c_now = att.sum(2).astype(float)
        if dead:
            rel = np.sqrt(c_now * (par.R + par.Rc)) * rng.standard_normal((B, n))
        else:
            rel = np.einsum("bij,bj->bi", att, u) + np.sqrt(c_now * par.Rc) * rng.standard_normal((B, n))
        a = 1.0 / par.R + kk / par.Rs
        b = c_now / (par.R + par.Rc)
        det = P00 * P11 - P01 ** 2
        i00, i01, i11 = P11 / det, -P01 / det, P00 / det
        L00, L01, L11 = i00 + a, i01, i11 + b
        h0 = i00 * e0 + i01 * e1 + v / par.R + slot_term
        h1 = i01 * e0 + i11 * e1 + rel / (par.R + par.Rc)
        dL = L00 * L11 - L01 ** 2
        Q00, Q01, Q11 = L11 / dL, -L01 / dL, L00 / dL
        ep0 = Q00 * h0 + Q01 * h1
        w = np.sqrt(par.Q) * rng.standard_normal(Kw)
        wb = w if indep_world else np.repeat(w, 2)
        xi = np.sqrt(par.qc) * rng.standard_normal((B, n, 2))
        e0 = F * ep0 + xi[:, :, 0] - wb[:, None]
        e1 = ep0 + xi[:, :, 1]
        P00 = F * F * Q00 + par.Q + par.qc
        P01 = F * Q00
        P11 = Q00 + par.qc
        # union filter (members' exterior-facing data: own sensors and open slots; no relays, no computation noise)
        aU = n / par.R + kk.sum(1) / par.Rs
        eUp = (eU / UU + v.sum(1) / par.R + slot_term.sum(1)) / (1.0 / UU + aU)
        UUp = 1.0 / (1.0 / UU + aU)
        eU = F * eUp - wb
        UU = F * F * UUp + par.Q
        # ---- policies for round t+1 ----
        if mode == "full" or mode == "pr":
            G = efe_grid(par, P00, P01, P11, cs, ks)        # (B, n, n, m+1)
        if mode == "full":
            lw = np.log(tmult)[:, None] + lbin[None, :] - par.gamma * G[:, :, tc, :]   # (B, n, ntype, m+1)
        elif mode == "hab":
            law = np.asarray(att_law, float) if att_law is not None else tmult / tmult.sum()
            po = 0.5 if slot_open_p is None else slot_open_p
            lk = lbin + ks * np.log(po) + (par.m - ks) * np.log(1 - po) if par.m > 0 else np.zeros(1)
            lw = np.broadcast_to(np.log(np.maximum(law, 1e-300))[:, None] + lk[None, :],
                                 (B, n, len(law), par.m + 1)).copy()
        elif mode == "pr":
            cdraw = rng.hypergeometric(n - 1, par.n_zero, r_att, size=(B, n))
            Gc = np.take_along_axis(G, cdraw[:, :, None, None], axis=2)[:, :, 0, :]   # (B, n, m+1)
            lw = (lbin[None, None, :] - par.gamma * Gc)[:, :, None, :]
        else:
            raise ValueError(mode)
        lw = lw - lw.max(axis=(2, 3), keepdims=True)
        pw = np.exp(lw)
        flat = pw.reshape(B, n, -1)
        cum = np.cumsum(flat, axis=2)
        cum /= cum[:, :, -1:]
        uu = rng.random((B, n, 1))
        idx = (uu > cum).sum(axis=2)
        idx = np.minimum(idx, flat.shape[2] - 1)
        ntype = lw.shape[2]
        ti = idx // (par.m + 1)
        kk = idx % (par.m + 1)
        if mode == "pr":
            cnew = cdraw
        else:
            cnew = tc[ti] if mode != "hab" or att_law is None else tc[ti]
        keys = rng.random((B, n, n)); keys[:, eye] = 2.0
        rank = np.argsort(np.argsort(keys, axis=2), axis=2)
        att = rank < cnew[:, :, None]
        u = v
    S_world = S_acc / cnt
    S_b = np.array([S_world[i::nbatch].mean(0) for i in range(nbatch)])
    out = MCOut(S=S_world.mean(0), S_batches=S_b, open_rate=open_acc / cnt, mean_c=c_acc / cnt)
    if want_inf:
        out.inf = inf_acc
    return out


def r_and_se(out: MCOut, n: int):
    al, be = compound(out.S)
    rb = np.array([r_ab(n, *compound(s)) for s in out.S_batches])
    return r_ab(n, al, be), rb.std(ddof=1) / np.sqrt(len(rb)), al, be


# ---------------------------------------------------------------------------------------------------------------
# closure (conventions of the round-2 attack, run3_closure.py): interior x = members' prior means (R^{2n}),
# blanket = own sensors, slot readings and the senders' sensings carried by relays; noise = relay read noise and
# computation noise.  Coarse variable y = scalar collective average of the members' first components.
# ---------------------------------------------------------------------------------------------------------------

def closure_numbers(par: Par, c: int, k: int, n: int, L: int = 60):
    Pm = steady_prior(par, c, k)
    M, k_own, k_slot, k_rel, Pp = member_mats(par, Pm, c, k)
    A = np.kron(np.eye(n), M)
    Qi = c * par.Rc * np.outer(k_rel, k_rel) + par.qc * np.eye(2)
    Qn = np.kron(np.eye(n), Qi)
    P1 = np.zeros((1, 2 * n)); P1[0, 0::2] = 1.0 / n
    Sig = solve_discrete_lyapunov(A, Qn)
    PS = P1 @ Sig
    Sxy = Sig - PS.T @ np.linalg.solve(PS @ P1.T, PS)
    Mm = P1 @ A @ Sxy @ A.T @ P1.T
    dcl = 0.5 * np.log(np.linalg.det(np.eye(1) + np.linalg.solve(P1 @ Qn @ P1.T, Mm)))
    gam = [float((P1 @ np.linalg.matrix_power(A, kk) @ Sig @ P1.T)[0, 0]) for kk in range(L + 2)]
    Tm = np.array([[gam[abs(i - j)] for j in range(L + 2)] for i in range(L + 2)])

    def cvar(hist):
        idx = list(range(L + 2 - 1 - hist, L + 1))
        S11 = Tm[np.ix_(idx, idx)]; s12 = Tm[np.ix_(idx, [L + 1])]
        return Tm[L + 1, L + 1] - float((s12.T @ np.linalg.solve(S11, s12))[0, 0])
    dM = 0.5 * np.log(cvar(1) / cvar(L))
    dM_half = 0.5 * np.log(cvar(1) / cvar(L // 2))
    return float(dcl), float(dM), float(dM_half)


def dcl_step(par: Par, Pm_list, c_list, k_list, Sig, n):
    r"""Per-step closure defect for a one-round deviation (members i read c_list[i] relays, k_list[i] slots) from
    the stationary interior covariance Sig."""
    A = np.zeros((2 * n, 2 * n)); Qn = np.zeros((2 * n, 2 * n))
    for i in range(n):
        M, k_own, k_slot, k_rel, _ = member_mats(par, Pm_list[i], int(c_list[i]), int(k_list[i]))
        A[2 * i:2 * i + 2, 2 * i:2 * i + 2] = M
        Qn[2 * i:2 * i + 2, 2 * i:2 * i + 2] = c_list[i] * par.Rc * np.outer(k_rel, k_rel) + par.qc * np.eye(2)
    P1 = np.zeros((1, 2 * n)); P1[0, 0::2] = 1.0 / n
    PS = P1 @ Sig
    Sxy = Sig - PS.T @ np.linalg.solve(PS @ P1.T, PS)
    Mm = P1 @ A @ Sxy @ A.T @ P1.T
    return float(0.5 * np.log(np.linalg.det(np.eye(1) + np.linalg.solve(P1 @ Qn @ P1.T, Mm))))


# ---------------------------------------------------------------------------------------------------------------
# agency index under the full-policy reading (def:agy-agency-index, 05_agency.tex:240-246) at one decision state
# ---------------------------------------------------------------------------------------------------------------

def member_policy_law(par: Par, Pm: np.ndarray):
    r"""Law of (attention type, slot count) of one member at prior Pm: P(tau, k) propto mult_tau C(m,k)
    exp(-gamma G(c_tau, k)).  Returns the (ntype, m+1) array of probabilities of (type, count) (a count k stands
    for C(m,k) equiprobable patterns)."""
    types = np.array(par.types, dtype=float)
    tc = types[:, 0].astype(int)
    ks = np.arange(par.m + 1)
    G = efe_grid(par, Pm[0, 0], Pm[0, 1], Pm[1, 1], np.arange(par.n), ks)[tc, :]
    lw = np.log(types[:, 1])[:, None] + log_binom(par.m)[None, :] - par.gamma * G
    lw -= lw.max()
    p = np.exp(lw)
    return p / p.sum(), G


def kl_terms_member(par: Par, Pm: np.ndarray):
    r"""Per-member KL_a = KL(P_a || E^a), KL_{s|a} = E_{P_a} KL(P_{s|a} || E^s) with uniform habits on the declared
    support (per message set) and on {0,1}^m."""
    P, G = member_policy_law(par, Pm)
    types = np.array(par.types, dtype=float)
    mult = types[:, 1]
    Ssize = mult.sum()
    pa = P.sum(1)                                     # law of the type
    # KL over message sets: each set of type tau has prob pa[tau]/mult[tau]; habit 1/|S|
    m_ = pa > 0
    KLa = float(np.sum(pa[m_] * np.log((pa[m_] / mult[m_]) * Ssize)))
    KLs = 0.0
    lb = log_binom(par.m)
    for t in range(len(pa)):
        if pa[t] <= 0:
            continue
        pk = P[t] / pa[t]                              # law of the count given the type
        mk = pk > 0
        # each pattern with count k has prob pk/C(m,k); habit 2^-m
        KLs += pa[t] * float(np.sum(pk[mk] * (np.log(pk[mk]) - lb[mk] + par.m * np.log(2.0))))
    return KLa, KLs, P, G
