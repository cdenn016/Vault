r"""Audience route for open:agy-meta-agent-exists (round 3): library.

Population V = {0 = S} u {1..n} (the audience A = {1..n}); one scalar world component.

  world            eta_{t+1} = F eta_t + w_t,  w ~ N(0, Q), stationary, 0 < F < 1.
  model state      x_t = (eta_t, eta_{t-1}) for every agent; prior N(m^-_a(t), P^-_a(t)); exact Kalman filters.
  own sensor       s_a(t) = eta_t + v_a(t),  v ~ N(0, Rown[a]),  Rown[0] = RS (source), Rown[i] = R (audience);
                   structural (read every round).
  broadcast        every agent writes its raw reading u_a(t) = s_a(t) every round (fixed speech act, not chosen).
  channel          y_ij(t+1) = u_j(t) + nu_ij(t+1), nu ~ N(0, Rc), receiver-specific; one-round latency, row [0, 1]
                   on x_{t+1}, claimed noise Rown[j] + Rc (exact: the content is a fresh raw datum).
  attention        audience member i chooses a set J of message channels among the n other agents, |J| <= kmsg,
                   from its policy posterior  q_i(J) ~ E(J) exp(-gamma G_i(J)),  E uniform over all such sets;
                   G_i(J) = -I(x_{t+1}; s_i(t+1), y_iJ(t+1)) + psi |J|  under P^-_i(t+1).
                   The source reads nothing but its own sensor (capacity zero for messages).
  prediction       m^-(t+1) = A_F m^+(t) + xi,  xi ~ N(0, qc I_2),  P^-(t+1) = A_F P^+ A_F^T + diag(Q, 0) + qc I_2.
  coordinates      e_a(t) = m^-_{a,0}(t) - eta_t  (prior error of eta_t), for every agent, the source included.

Error recursion (exact codes, so eta enters only through the common innovation):
  E_a^-(t+1) = A_F P^+ (P^-)^{-1} E_a^-(t) + A_F k_own v_a(t) + sum_{j in J} A_F k_j (v_j(t-1) + nu_aj(t)) + xi_a(t)
               - (w_t, 0)^T,
  with k_own = P^+ e_0 / Rown[a], k_j = P^+ e_1 / (Rown[j] + Rc).  The relayed sensing noise v_j(t-1) is the
  sender's private input (record convention: not conditioned on), so it is kept as a state variable V_j.
"""
from __future__ import annotations

import os
for _v in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS"):
    os.environ.setdefault(_v, "1")
import itertools
from dataclasses import dataclass, replace
from math import comb

import numpy as np
from scipy.linalg import solve_discrete_lyapunov


@dataclass(frozen=True)
class Par:
    F: float = 0.9
    Q: float = 0.05
    R: float = 1.0        # audience own-sensor noise
    RS: float = 0.01      # source sensor noise
    Rc: float = 0.002     # receiver-specific channel noise
    qc: float = 1e-4      # computation noise on predicted means
    n: int = 4            # audience size
    kmsg: int = 1         # audience message capacity
    gamma: float = 40.0
    psi: float = 0.0      # pragmatic cost per message channel (0: none)

    def with_(self, **kw) -> "Par":
        return replace(self, **kw)

    @property
    def N(self) -> int:
        return self.n + 1

    def Rown(self) -> np.ndarray:
        r = np.full(self.N, self.R)
        r[0] = self.RS
        return r


def A_F(F: float) -> np.ndarray:
    return np.array([[F, 0.0], [1.0, 0.0]])


def prior_next(par: Par, Pp: np.ndarray) -> np.ndarray:
    Af = A_F(par.F)
    return Af @ Pp @ Af.T + np.diag([par.Q, 0.0]) + par.qc * np.eye(2)


def posterior(Pm: np.ndarray, a: float, b: float) -> np.ndarray:
    return np.linalg.inv(np.linalg.inv(Pm) + np.diag([a, b]))


def info(Pm: np.ndarray, a, b):
    r"""I(x; obs) = 1/2 ln det(I + P^- diag(a, b))."""
    a = np.asarray(a, float)
    b = np.asarray(b, float)
    return 0.5 * np.log((1 + a * Pm[0, 0]) * (1 + b * Pm[1, 1]) - a * b * Pm[0, 1] ** 2)


def riccati_fixed(par: Par, a: float, b: float, iters: int = 4000) -> tuple[np.ndarray, np.ndarray]:
    r"""Stationary (P^-, P^+) of a filter with own-sensor precision a and channel precision b every round."""
    v0 = par.Q / (1 - par.F ** 2) if par.F < 1 else 1.0
    Pm = np.diag([v0, v0]) + par.qc * np.eye(2)
    for _ in range(iters):
        Pp = posterior(Pm, a, b)
        Pn = prior_next(par, Pp)
        if np.max(np.abs(Pn - Pm)) < 1e-16:
            Pm = Pn
            break
        Pm = Pn
    return Pm, posterior(Pm, a, b)


# ------------------------------------------------------------------------------------------------------------
# attention policies of the audience
# ------------------------------------------------------------------------------------------------------------

def att_types(par: Par):
    r"""Types (s, m): s = 1 if the source channel is in J, m = number of mates in J; multiplicity C(n-1, m)."""
    ty, mult = [], []
    for s in (0, 1):
        for m in range(0, par.n):
            if s + m <= par.kmsg and m <= par.n - 1:
                ty.append((s, m))
                mult.append(comb(par.n - 1, m))
    return ty, np.array(mult, float)


def b_of(par: Par, s: int, m: int) -> float:
    return s / (par.RS + par.Rc) + m / (par.R + par.Rc)


def efe_types(par: Par, Pm: np.ndarray):
    ty, mult = att_types(par)
    G = np.array([-info(Pm, 1.0 / par.R, b_of(par, s, m)) + par.psi * (s + m) for s, m in ty])
    return ty, mult, G


def type_law(par: Par, Pm: np.ndarray, gamma: float | None = None):
    r"""Law over attention types under the policy posterior (habits uniform over sets)."""
    g = par.gamma if gamma is None else gamma
    ty, mult, G = efe_types(par, Pm)
    lw = np.log(mult) - g * G
    lw -= lw.max()
    p = np.exp(lw)
    return ty, p / p.sum(), G, mult


# ------------------------------------------------------------------------------------------------------------
# policy paths
# ------------------------------------------------------------------------------------------------------------

@dataclass
class Path:
    Pm: np.ndarray      # (T, N, 2, 2) claimed prior covariance at round t
    att: list           # att[t][a] = tuple of senders whose channel agent a reads at round t
    dev: int            # audience member-rounds whose attention differs from 'all read the source only'


def simulate_path(par: Par, T: int, rng: np.random.Generator, mode: str = "full",
                  warm: bool = True) -> Path:
    r"""mode: 'full' (EFE attention), 'hab' (gamma = 0: habits uniform over sets), 'pr' (partners redrawn uniformly
    every round among the n other agents, kmsg per round = the full model's attention rate), 'fixedS' (every audience
    member reads exactly the source), 'none' (no message channels).  The source reads nothing in every mode.
    warm: start every agent at the full model's stationary covariance (the decision state)."""
    N, n = par.N, par.n
    Rown = par.Rown()
    others = [[j for j in range(N) if j != i] for i in range(N)]
    ty, mult = att_types(par)
    # start
    PmS, _ = riccati_fixed(par, 1.0 / par.RS, 0.0)
    Pm_full, _ = riccati_fixed(par, 1.0 / par.R, b_of(par, 1, max(0, par.kmsg - 1)))
    Pm = [PmS.copy()] + [Pm_full.copy() if warm else np.eye(2) * par.Q / (1 - par.F ** 2) for _ in range(n)]
    cur = [tuple()] + [tuple(sorted([0] + [1 + ((i + k) % n) for k in range(1, par.kmsg)]))
                       if (warm and mode in ("full", "fixedS")) else tuple() for i in range(n)]
    if mode == "fixedS":
        cur = [tuple()] + [(0,) for _ in range(n)]
    Pm_hist = np.zeros((T, N, 2, 2))
    att = []
    dev = 0
    for t in range(T):
        for a in range(N):
            Pm_hist[t, a] = Pm[a]
        att.append(tuple(cur))
        new = [tuple()]
        Pn = [None] * N
        for a in range(N):
            b = sum(1.0 / (Rown[j] + par.Rc) for j in cur[a])
            Pp = posterior(Pm[a], 1.0 / Rown[a], b)
            Pn[a] = prior_next(par, Pp)
        for i in range(1, N):
            if mode == "fixedS":
                J = (0,)
            elif mode == "none":
                J = tuple()
            elif mode == "pr":
                J = tuple(sorted(rng.choice(others[i], size=par.kmsg, replace=False)))
            else:
                if mode == "hab":
                    p = mult / mult.sum()
                else:
                    _, p, _, _ = type_law(par, Pn[i])
                k = rng.choice(len(ty), p=p)
                s, m = ty[k]
                mates = [j for j in others[i] if j != 0]
                chosen = list(rng.choice(mates, size=m, replace=False)) if m > 0 else []
                J = tuple(sorted(([0] if s else []) + [int(x) for x in chosen]))
            if not (len(J) == par.kmsg and 0 in J):
                dev += 1
            new.append(J)
        Pm = Pn
        cur = new
    return Path(Pm_hist, att, dev)


# ------------------------------------------------------------------------------------------------------------
# exact second moments
# ------------------------------------------------------------------------------------------------------------

def agent_round(par: Par, a: int, Pm: np.ndarray, J, Rown: np.ndarray):
    r"""Mx (2x2), relay gains {j: A_F k_j (2,)}, noise block (3x3) for (E_a(t+1), V_a(t+1))."""
    Af = A_F(par.F)
    b = sum(1.0 / (Rown[j] + par.Rc) for j in J)
    Pp = posterior(Pm, 1.0 / Rown[a], b)
    Mx = Af @ Pp @ np.linalg.inv(Pm)
    k_own = Pp[:, 0] / Rown[a]
    kj = {j: Af @ (Pp[:, 1] / (Rown[j] + par.Rc)) for j in J}
    Ek = Rown[a] * np.outer(k_own, k_own)
    for j in J:
        kk = Pp[:, 1] / (Rown[j] + par.Rc)
        Ek = Ek + par.Rc * np.outer(kk, kk)
    blk = np.zeros((3, 3))
    blk[:2, :2] = Af @ Ek @ Af.T + par.qc * np.eye(2)
    blk[:2, 2] = Af @ (k_own * Rown[a])
    blk[2, :2] = blk[:2, 2]
    blk[2, 2] = Rown[a]
    return Mx, kj, blk


def idx(par: Par):
    r"""Index maps for one replica's state [E_0(2), ..., E_{N-1}(2), V_0, ..., V_{N-1}]."""
    N = par.N
    E = [(2 * a, 2 * a + 1) for a in range(N)]
    V = [2 * N + a for a in range(N)]
    return E, V, 3 * N


def one_replica_mats(par: Par, Pm_t: np.ndarray, att_t, dead: bool = False, excl_src: bool = False):
    r"""Transition A (d1 x d1) and fresh-noise covariance Nz for one replica at one round (private noises only).
    dead: relays deliver pure noise of the claimed variance (N_lp), no sender noise is carried.
    excl_src: the source's private inputs (sensing and computation noise) are conditioned on (zero variance), for the
    member-restricted order parameter Omega_int(A | zeta_S)."""
    Rown = par.Rown()
    E, V, d1 = idx(par)
    A = np.zeros((d1, d1))
    Nz = np.zeros((d1, d1))
    for a in range(par.N):
        Mx, kj, blk = agent_round(par, a, Pm_t[a], att_t[a], Rown)
        ea = list(E[a])
        A[np.ix_(ea, ea)] = Mx
        if dead:
            for j, g in kj.items():
                # pure noise of variance Rown[j] + Rc replaces v_j(t-1) + nu: fresh and private to the receiver
                Nz[np.ix_(ea, ea)] += (Rown[j] + par.Rc - par.Rc) * np.outer(g, g)
        else:
            for j, g in kj.items():
                A[ea, V[j]] += g
        ids = ea + [V[a]]
        if not (excl_src and a == 0):
            Nz[np.ix_(ids, ids)] += blk
    return A, Nz


def stationary_fixed(par: Par, att_fixed, Pm_fixed, dead: bool = False):
    r"""Exact stationary private-noise covariance (world-conditional, fixed attention and fixed covariances)."""
    A, Nz = one_replica_mats(par, Pm_fixed, att_fixed, dead=dead)
    S = solve_discrete_lyapunov(A, Nz)
    return 0.5 * (S + S.T), A, Nz


def coords(par: Par, S: np.ndarray) -> np.ndarray:
    E, _, _ = idx(par)
    c = [E[a][0] for a in range(par.N)]
    return S[np.ix_(c, c)]


def pair_moments(par: Par, pa: Path, pb: Path, t_eval, dead: bool = False, excl_src: bool = False):
    r"""Exact second moments of the prior errors of two replicas sharing the world path, with independent private
    noises and the given policy paths.  Returns per t in t_eval: (1/2 Cov(e^a - e^b), Cov(e^a|eta,pi^a), Cov(e^b|..))."""
    E, V, d1 = idx(par)
    D = 2 * d1
    T = pa.Pm.shape[0]
    C = np.zeros((D, D))
    Cp = [np.zeros((d1, d1)), np.zeros((d1, d1))]
    uw = np.zeros(D)
    for r in (0, 1):
        for a in range(par.N):
            uw[r * d1 + E[a][0]] = -1.0
    ce = [E[a][0] for a in range(par.N)]
    cea = ce
    ceb = [d1 + c for c in ce]
    out = []
    te = set(t_eval)
    for t in range(T):
        if t in te:
            Caa = C[np.ix_(cea, cea)]
            Cbb = C[np.ix_(ceb, ceb)]
            Cab = C[np.ix_(cea, ceb)]
            out.append((0.5 * (Caa + Cbb - Cab - Cab.T), Cp[0][np.ix_(ce, ce)].copy(), Cp[1][np.ix_(ce, ce)].copy()))
        Aa, Na = one_replica_mats(par, pa.Pm[t], pa.att[t], dead=dead, excl_src=excl_src)
        Ab, Nb = one_replica_mats(par, pb.Pm[t], pb.att[t], dead=dead, excl_src=excl_src)
        A = np.zeros((D, D))
        A[:d1, :d1] = Aa
        A[d1:, d1:] = Ab
        Nz = np.zeros((D, D))
        Nz[:d1, :d1] = Na
        Nz[d1:, d1:] = Nb
        C = A @ C @ A.T + Nz + par.Q * np.outer(uw, uw)
        Cp[0] = Aa @ Cp[0] @ Aa.T + Na
        Cp[1] = Ab @ Cp[1] @ Ab.T + Nb
    return out


def sigma_mc(par: Par, mode: str, npairs: int, T: int, burn: int, every: int, seed: int, dead: bool = False,
             warm: bool = True, excl_src: bool = False):
    rng = np.random.default_rng(seed)
    t_eval = list(range(burn, T, every))
    sig, priv, devs = [], [], 0
    for _ in range(npairs):
        pa = simulate_path(par, T, rng, mode, warm=warm)
        pb = simulate_path(par, T, rng, mode, warm=warm)
        devs += pa.dev + pb.dev
        res = pair_moments(par, pa, pb, t_eval, dead=dead, excl_src=excl_src)
        sig.append(np.mean([x[0] for x in res], axis=0))
        priv.append(np.mean([0.5 * (x[1] + x[2]) for x in res], axis=0))
    sig = np.array(sig)
    priv = np.array(priv)
    return dict(S=sig.mean(0), S_pairs=sig, Priv=priv.mean(0), dev_rate=devs / (2 * npairs * T * par.n))


# ------------------------------------------------------------------------------------------------------------
# contrast machinery, written from def:col-contrast (04_collectives.tex:182-188) and eq:col-diffusive (:147-151)
# ------------------------------------------------------------------------------------------------------------

def diffusive(Pi: np.ndarray, tol: float = 0.0):
    off = Pi - np.diag(np.diag(Pi))
    return bool(off.max() <= tol and Pi.sum(1).min() >= -tol), float(off.max()), float(Pi.sum(1).min())


def contrast(Pi: np.ndarray, C) -> float:
    C = list(C)
    n = len(C)
    eps = Pi.sum(1)
    a = -(Pi - np.diag(np.diag(Pi)))
    aC = a[np.ix_(C, C)]
    LC = np.diag(aC.sum(1)) - aC
    M = np.diag(eps[C]) + LC
    phi = np.ones(n) / np.sqrt(n)
    xout = float(phi @ Pi[np.ix_(C, C)] @ phi)
    Z = np.linalg.svd(np.eye(n) - np.outer(phi, phi))[0][:, : n - 1]
    xin = float(np.linalg.eigvalsh(Z.T @ M @ Z).min())
    return xin / xout


def all_regions(N: int):
    for r in range(2, N + 1):
        for C in itertools.combinations(range(N), r):
            yield C


def region_table(Pi: np.ndarray):
    return {C: contrast(Pi, C) for C in all_regions(Pi.shape[0])}


def mean_coupling_baseline(Pi: np.ndarray):
    r"""Clause (c) with the mean coupling: exchangeable medium, coupling abar on every pair, uniform leak epsbar;
    the baseline is the sup over regions of the medium (attained by the whole medium, checked by enumeration)."""
    N = Pi.shape[0]
    a = -(Pi - np.diag(np.diag(Pi)))
    abar = a[np.triu_indices(N, 1)].mean()
    ebar = Pi.sum(1).mean()
    Pm = (ebar + (N - 1) * abar) * np.eye(N) - abar * (np.ones((N, N)) - np.eye(N))
    best = max(contrast(Pm, C) for C in all_regions(N))
    return best, abar, ebar, 1 + N * abar / ebar


def symmetrize_audience(S: np.ndarray) -> np.ndarray:
    r"""Project an (N x N) covariance onto the family invariant under permutations of the audience {1..n}."""
    N = S.shape[0]
    n = N - 1
    out = np.zeros_like(S)
    out[0, 0] = S[0, 0]
    c = S[0, 1:].mean()
    out[0, 1:] = c
    out[1:, 0] = c
    B = S[1:, 1:]
    d = np.trace(B) / n
    o = (B.sum() - np.trace(B)) / (n * (n - 1))
    out[1:, 1:] = o
    out[1:, 1:][np.diag_indices(n)] = d
    return out
