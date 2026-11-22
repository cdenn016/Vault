r"""Independent re-implementation (attack on 'agency-frontier', round 3) of design D1 from its written specification.

Written from the specification in the candidate report, not from the candidate's code.  Differences in method:
covariance-form Kalman gains by sequential scalar updates (candidate: information form); stationary covariances by
fixed-point iteration of the augmented second-moment map (candidate: scipy Lyapunov solver); mechanism medium by
exact averaging over all 81 attention configurations per round (candidate: hand-reduced 2x2 recursion); Markov
defect by a zero-noise Kalman filter on the coarse variable (candidate: Toeplitz conditioning).

Model, one niche of n members (niches are independent copies):
  eta_{t+1} = F eta_t + w,  w ~ N(0, Q);  member state x_t = (eta_t, eta_{t-1});  prior N(m^-, P^-), e = m^- - x.
  round t data: own sensor eta_t + v_i(t) (R), k open private slots eta_t + rho (Rs each, owner only),
  relay of the mate's own reading s_j(t-1) + nu_ij(t) (observation of eta_{t-1}, noise R + Rc; v_j(t-1) is the
  mate's private sensing noise, not conditioned on: record convention, def:col-world-conditional 04_collectives:131).
  prediction m^-(t+1) = A_F m^+ + xi,  xi ~ N(0, qc I_2), claimed P^-(t+1) = A_F P^+ A_F^T + diag(Q,0) + qc I.
"""
from __future__ import annotations

import os
for _v in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS"):
    os.environ[_v] = "1"
import itertools
from dataclasses import dataclass, replace
from math import comb, lgamma

import numpy as np


@dataclass(frozen=True)
class Par:
    F: float = 0.9
    Q: float = 0.05
    R: float = 1.0
    Rc: float = 0.1
    Rs: float = 10.0
    qc: float = 1e-4
    psi: float = 0.06701572565861963
    gamma: float = 400.0
    m: int = 8

    def w(self, **kw) -> "Par":
        return replace(self, **kw)


def AF(par: Par) -> np.ndarray:
    return np.array([[par.F, 0.0], [1.0, 0.0]])


def predict_cov(par: Par, Pp: np.ndarray) -> np.ndarray:
    A = AF(par)
    return A @ Pp @ A.T + np.diag([par.Q, 0.0]) + par.qc * np.eye(2)


def gains(par: Par, Pm: np.ndarray, c: int, k: int):
    r"""Sequential scalar covariance-form update: first the pooled own+slot reading of eta_t (variance r1),
    then (if c = 1) the relay as a reading of eta_{t-1} with variance R + Rc.
    Returns Mbb = A_F (I-K2h2)(I-K1h1) and the loadings of the next prior error on v_i(t), on one slot noise,
    on the relay noise (v_j(t-1)+nu), plus P^+."""
    a = 1.0 / par.R + k / par.Rs
    r1 = 1.0 / a
    h1 = np.array([1.0, 0.0])
    K1 = Pm @ h1 / (h1 @ Pm @ h1 + r1)
    I1 = np.eye(2) - np.outer(K1, h1)
    P1 = I1 @ Pm @ I1.T + r1 * np.outer(K1, K1)          # Joseph form
    if c >= 1:
        if c != 1:
            raise ValueError("c <= 1 in D1")
        h2 = np.array([0.0, 1.0])
        r2 = par.R + par.Rc
        K2 = P1 @ h2 / (h2 @ P1 @ h2 + r2)
        I2 = np.eye(2) - np.outer(K2, h2)
        P2 = I2 @ P1 @ I2.T + r2 * np.outer(K2, K2)
    else:
        K2 = np.zeros(2)
        I2 = np.eye(2)
        P2 = P1
    A = AF(par)
    Mbb = A @ I2 @ I1
    l_own = A @ I2 @ K1 * (r1 / par.R)     # coefficient on v_i(t)
    l_slot = A @ I2 @ K1 * (r1 / par.Rs)   # coefficient on each rho
    l_rel = A @ K2                         # coefficient on v_j(t-1) + nu_ij(t)
    return Mbb, l_own, l_slot, l_rel, P2


def steady(par: Par, c: int, k: int, it: int = 20000) -> np.ndarray:
    Pm = np.diag([0.3, 0.3])
    for _ in range(it):
        _, _, _, _, Pp = gains(par, Pm, c, k)
        Pn = predict_cov(par, Pp)
        if np.max(np.abs(Pn - Pm)) < 1e-16:
            return Pn
        Pm = Pn
    return Pm


def fixed_point(Amap, Qmat, it: int = 200000, tol: float = 1e-22) -> np.ndarray:
    S = np.zeros_like(Qmat)
    for _ in range(it):
        Sn = Amap @ S @ Amap.T + Qmat
        if np.max(np.abs(Sn - S)) < tol:
            return Sn
        S = Sn
    return S


def sigma_c_pattern(par: Par, reads: list, ks: list, dead: bool = False, Pms: list | None = None):
    r"""Exact world-conditional covariance (first components of the prior errors) for a deterministic pattern:
    reads[i] = index of the sender i reads every round (or None), ks[i] = open slots.  State
    z = (e_1..e_N in R^2, vprev_1..vprev_N).  dead: relay content replaced by pure noise of variance R + Rc."""
    N = len(reads)
    D = 3 * N
    A = np.zeros((D, D))
    cols = []
    for i in range(N):
        c = 0 if reads[i] is None else 1
        Pm = steady(par, c, ks[i]) if Pms is None else Pms[i]
        Mbb, lo, ls, lr, _ = gains(par, Pm, c, ks[i])
        A[2 * i:2 * i + 2, 2 * i:2 * i + 2] = Mbb
        if c and not dead:
            A[2 * i:2 * i + 2, 2 * N + reads[i]] = lr
        col = np.zeros(D); col[2 * i:2 * i + 2] = lo * np.sqrt(par.R); col[2 * N + i] = np.sqrt(par.R); cols.append(col)
        if ks[i] > 0:
            col = np.zeros(D); col[2 * i:2 * i + 2] = ls * np.sqrt(ks[i] * par.Rs); cols.append(col)
        if c:
            var = (par.R + par.Rc) if dead else par.Rc
            col = np.zeros(D); col[2 * i:2 * i + 2] = lr * np.sqrt(var); cols.append(col)
        for d in range(2):
            col = np.zeros(D); col[2 * i + d] = np.sqrt(par.qc); cols.append(col)
    Bm = np.array(cols).T
    S = fixed_point(A, Bm @ Bm.T)
    idx = [2 * i for i in range(N)]
    return S[np.ix_(idx, idx)], S


def contrast(Pi: np.ndarray, C) -> float:
    r"""def:col-contrast (04_collectives.tex:182-188) on the whole-population precision."""
    C = list(C)
    n = len(C)
    eps = Pi.sum(axis=1)
    aC = -Pi[np.ix_(C, C)].copy()
    np.fill_diagonal(aC, 0.0)
    L = np.diag(aC.sum(axis=1)) - aC
    Mx = np.diag(eps[C]) + L
    phi = np.ones(n) / np.sqrt(n)
    xout = float(phi @ Pi[np.ix_(C, C)] @ phi)
    # orthonormal basis of 1-perp via QR
    Bq, _ = np.linalg.qr(np.column_stack([phi, np.eye(n)[:, : n - 1]]))
    Z = Bq[:, 1:]
    xin = float(np.linalg.eigvalsh(Z.T @ Mx @ Z).min())
    return xin / xout


def diffusive(Pi: np.ndarray, tol: float = 1e-12):
    off = Pi - np.diag(np.diag(Pi))
    return bool(off.max() <= tol and Pi.sum(1).min() >= -tol), float(off.max()), float(Pi.sum(1).min())


def all_regions(Pi: np.ndarray):
    N = Pi.shape[0]
    out = {}
    for s in range(2, N + 1):
        for C in itertools.combinations(range(N), s):
            out[C] = contrast(Pi, C)
    return out


def medium_exact(par: Par, N: int = 4, it: int = 100000, tol: float = 1e-22):
    r"""Mechanism medium of clause (c): one world component, N agents, each reads one uniformly random other agent
    every round (EFE ties among informative senders), slots closed.  Exact average over all (N-1)^N configurations
    of the second-moment map; E[Cov(e|eta)] (the gains do not depend on whom one reads, so the mixture part is 0)."""
    Pm = steady(par, 1, 0)
    Mbb, lo, ls, lr, _ = gains(par, Pm, 1, 0)
    D = 3 * N
    configs = list(itertools.product(*[[j for j in range(N) if j != i] for i in range(N)]))
    As = []
    for cf in configs:
        A = np.zeros((D, D))
        for i in range(N):
            A[2 * i:2 * i + 2, 2 * i:2 * i + 2] = Mbb
            A[2 * i:2 * i + 2, 2 * N + cf[i]] = lr
        As.append(A)
    As = np.array(As)
    cols = []
    for i in range(N):
        col = np.zeros(D); col[2 * i:2 * i + 2] = lo * np.sqrt(par.R); col[2 * N + i] = np.sqrt(par.R); cols.append(col)
        col = np.zeros(D); col[2 * i:2 * i + 2] = lr * np.sqrt(par.Rc); cols.append(col)
        for d in range(2):
            col = np.zeros(D); col[2 * i + d] = np.sqrt(par.qc); cols.append(col)
    Bm = np.array(cols).T
    Qm = Bm @ Bm.T
    S = np.zeros((D, D))
    for _ in range(it):
        Sn = np.einsum("cij,jk,clk->il", As, S, As) / len(As) + Qm
        if np.max(np.abs(Sn - S)) < tol:
            S = Sn
            break
        S = Sn
    idx = [2 * i for i in range(N)]
    return S[np.ix_(idx, idx)]


def info_x(par: Par, Pm: np.ndarray, c: int, k: int) -> float:
    r"""I(x_{t+1}; own + k slots + c relays) under prior Pm (own and slots read eta_{t+1}, relay reads eta_t)."""
    a = 1.0 / par.R + k / par.Rs
    b = c / (par.R + par.Rc)
    return 0.5 * float(np.log(np.linalg.det(np.eye(2) + Pm @ np.diag([a, b]))))


def efe(par: Par, Pm: np.ndarray, c: int, k: int) -> float:
    return -info_x(par, Pm, c, k) + par.psi * k


def lbin(m: int) -> np.ndarray:
    return np.array([lgamma(m + 1) - lgamma(k + 1) - lgamma(m - k + 1) for k in range(m + 1)])


# --------------------------------------------------------------------------------------------------------------
# two-replica Monte Carlo (own implementation): one niche of n = 2, shapes (B, 2 replicas, 2 agents)
# --------------------------------------------------------------------------------------------------------------

def mc(par: Par, mode: str, B: int, T: int, burn: int, seed: int, q_mate=(0.25, 0.25), slot_p: float = 0.5,
       pr_rate: float = 1.0 / 3.0, nb: int = 20, dead: bool = False, indep_world: bool = False,
       support_mult=(1, 3)):
    r"""mode 'full': (type, k) ~ mult * C(m,k) exp(-gamma G(c,k)), types (mate: c=1, mult 1; other: c=0, mult 3).
    mode 'hab': mate read with probability q_mate[i] (member-specific), k ~ Bin(m, slot_p).
    mode 'pr' : mate read with probability pr_rate each round (partner uniform over the 3 others), k by EFE given c.
    Returns alpha, beta (compound-symmetric reading of E[Cov(e|eta)]), r = 1 + 2 beta/alpha, batch SE of r."""
    rng = np.random.default_rng(seed)
    m = par.m
    Af = AF(par)
    sh = (B, 2, 2)
    P0 = steady(par, 1, 0)
    P00 = np.full(sh, P0[0, 0]); P01 = np.full(sh, P0[0, 1]); P11 = np.full(sh, P0[1, 1])
    e0 = np.zeros(sh); e1 = np.zeros(sh)
    vprev = np.zeros(sh)
    c = np.ones(sh, dtype=int) if mode == "full" else np.zeros(sh, dtype=int)
    k = np.zeros(sh, dtype=int)
    acc = np.zeros((B, 2, 2)); cnt = 0
    lb = lbin(m)
    ks = np.arange(m + 1)
    open_acc = 0.0; c_acc = 0.0
    for t in range(T):
        if t >= burn:
            d = e0[:, 0, :] - e0[:, 1, :]
            acc += 0.5 * d[:, :, None] * d[:, None, :]
            cnt += 1
            open_acc += k.mean(); c_acc += c.mean()
        v = np.sqrt(par.R) * rng.standard_normal(sh)
        rho = np.sqrt(k * par.Rs) * rng.standard_normal(sh)          # sum of the k slot noises
        nu = np.sqrt(par.Rc) * rng.standard_normal(sh)
        mate_v = vprev[:, :, ::-1]
        if dead:
            n2 = np.sqrt(par.R + par.Rc) * rng.standard_normal(sh)
        else:
            n2 = mate_v + nu
        # --- update 1: pooled own+slots reading of eta_t: variance r1, noise n1 = r1 (v/R + rho/Rs)
        a = 1.0 / par.R + k / par.Rs
        r1 = 1.0 / a
        n1 = r1 * (v / par.R + rho / par.Rs)
        s = P00 + r1
        K10 = P00 / s; K11 = P01 / s
        # e <- e - K1 (e0 - n1)
        inn = e0 - n1
        e0n = e0 - K10 * inn; e1n = e1 - K11 * inn
        Q00 = P00 - K10 * P00; Q01 = P01 - K10 * P01; Q11 = P11 - K11 * P01
        # --- update 2: relay reading of eta_{t-1} (component 1), variance R + Rc, if c = 1
        r2 = par.R + par.Rc
        s2 = Q11 + r2
        K20 = np.where(c == 1, Q01 / s2, 0.0); K21 = np.where(c == 1, Q11 / s2, 0.0)
        inn2 = e1n - n2
        e0p = e0n - K20 * inn2; e1p = e1n - K21 * inn2
        R00 = Q00 - K20 * Q01; R01 = Q01 - K20 * Q11; R11 = Q11 - K21 * Q11
        # --- predict
        wv = np.sqrt(par.Q) * rng.standard_normal((B, 2) if indep_world else (B, 1))
        wv = np.broadcast_to(wv[:, :, None], sh)
        xi0 = np.sqrt(par.qc) * rng.standard_normal(sh); xi1 = np.sqrt(par.qc) * rng.standard_normal(sh)
        e0 = par.F * e0p + xi0 - wv
        e1 = e0p + xi1
        P00 = par.F ** 2 * R00 + par.Q + par.qc
        P01 = par.F * R00
        P11 = R00 + par.qc
        vprev = v
        # --- policy for the next round
        if mode == "hab":
            qm = np.broadcast_to(np.asarray(q_mate)[None, None, :], sh)
            c = (rng.random(sh) < qm).astype(int)
            k = rng.binomial(m, slot_p, size=sh)
        else:
            # information of each (c, k) under the current priors
            aa = 1.0 / par.R + ks / par.Rs                                  # (m+1,)
            def info(cc):
                bb = cc / (par.R + par.Rc)
                return 0.5 * np.log((1 + aa * P00[..., None]) * (1 + bb * P11[..., None])
                                    - aa * bb * P01[..., None] ** 2)
            G0 = -info(0) + par.psi * ks
            G1 = -info(1) + par.psi * ks
            if mode == "full":
                lw = np.stack([np.log(support_mult[1]) + lb - par.gamma * G0,
                               np.log(support_mult[0]) + lb - par.gamma * G1], axis=-2)   # (..., 2, m+1): c=0, c=1
                lw = lw - lw.max(axis=(-2, -1), keepdims=True)
                p = np.exp(lw).reshape(sh + (2 * (m + 1),))
                p /= p.sum(-1, keepdims=True)
                u = rng.random(sh + (1,))
                idx = (np.cumsum(p, -1) < u).sum(-1)
                idx = np.minimum(idx, 2 * (m + 1) - 1)
                c = idx // (m + 1); k = idx % (m + 1)
            elif mode == "pr":
                c = (rng.random(sh) < pr_rate).astype(int)
                Gc = np.where(c[..., None] == 1, G1, G0)
                lw = lb - par.gamma * Gc
                lw = lw - lw.max(-1, keepdims=True)
                p = np.exp(lw); p /= p.sum(-1, keepdims=True)
                u = rng.random(sh + (1,))
                k = np.minimum((np.cumsum(p, -1) < u).sum(-1), m)
            else:
                raise ValueError(mode)
    S = acc / cnt
    def ab(Sm):
        al = 0.5 * (Sm[0, 0] + Sm[1, 1]) - Sm[0, 1]
        return al, Sm[0, 1]
    al, be = ab(S.mean(0))
    rs = []
    for j in range(nb):
        a_, b_ = ab(S[j::nb].mean(0))
        rs.append(1 + 2 * b_ / a_)
    rs = np.array(rs)
    return dict(alpha=al, beta=be, r=1 + 2 * be / al, se=rs.std(ddof=1) / np.sqrt(nb),
                open_rate=open_acc / max(cnt, 1), c_rate=c_acc / max(cnt, 1), S=S.mean(0))
