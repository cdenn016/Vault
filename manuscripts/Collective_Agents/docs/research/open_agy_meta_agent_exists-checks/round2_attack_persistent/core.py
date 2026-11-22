r"""Independent re-implementation for the attack on the round-2 persistent-world epistemic niche (record O1).

Written from the constructor's declared specification only (not from its lib.py).  Method: direct Monte Carlo of
the agents' actual Kalman filters with sampled noises, two replicas per world path (shared world, independent
policy randomness and private noises), so that
    Sigma^c = E[Cov(e(t) | eta)] = (1/2) E[(e^1 - e^2)(e^1 - e^2)^T]
(second-moment convention of def:col-contrast, 04_collectives.tex:187).

Model (declared specification):
  world component: eta_{t+1} = F eta_t + w_t, w ~ N(0, Q), stationary start.
  member model state x_t = (eta_t, eta_{t-1}); belief N(m^-(t), P^-(t)) before the round-t update.
  round-t observations of member i:
     own sensor            s_i(t) = eta_t + v_i(t),              v ~ N(0, R)
     relay of attended j   y_ij(t) = s_j(t-1) + nu_ij(t),        nu ~ N(0, Rc), reads eta_{t-1} (noise R+Rc)
     every open slot k     o_ik(t) = eta_t + rho_ik(t),          rho ~ N(0, Rs), private to the reader
  exact update (information form); prediction m^-(t+1) = A_F m^+(t) + xi, xi ~ N(0, qc I_2),
  P^-(t+1) = A_F P^+ A_F^T + diag(Q, 0) + qc I_2,  A_F = [[F, 0], [1, 0]].
  EFE of member i for round t+1:  G(m, n) = -I(target; own + m relays + n slots) + psi n,
     target 'x' = x_{t+1} = (eta_{t+1}, eta_t) (declared), 'eta' = eta_{t+1} only (alternative reading).
  Attention habits uniform over message sets of size <= kmsg among n_inf informative + n_zero zero-gain channels.
  T-real: one uniformly chosen reviser per round redraws its slot with log-odds gamma*(Gt(n_-r) - Gt(n_-r + 1)),
     Gt the soft-min of G over attention (habit-weighted); every member then draws its attention for t+1 from
     the conditional posterior given the open count it knows (reviser: new count; others: current count).
Modes: 'full', 'hab' (gamma = 0), 'pr' (partners redrawn uniformly every round, kmsg of the n_inf + n_zero
message channels; reviser's EFE given its drawn partners), 'fixed' (all mates, fixed slot count, no policy).
"""
from __future__ import annotations

import os
for _v in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS"):
    os.environ.setdefault(_v, "1")
from dataclasses import dataclass, replace, field
from math import comb

import numpy as np


@dataclass(frozen=True)
class Par:
    F: float = 0.9
    Q: float = 0.05
    R: float = 1.0
    Rc: float = 0.1
    Rs: float = 2.0
    psi: float = 0.024
    gamma: float = 400.0
    qc: float = 1e-4
    n: int = 4          # members of the simulated group (one niche, or the whole mechanism medium)
    n_inf: int = 3      # informative message channels per member
    n_zero: int = 4     # zero-gain message channels per member
    kmsg: int = 3       # message capacity
    nslots: int = 4     # slot channels carrying this group's world component (read by every member)
    target: str = "x"   # EFE information target
    p0: float = 0.09

    def with_(self, **kw) -> "Par":
        return replace(self, **kw)

    @property
    def mmax(self) -> int:
        return min(self.kmsg, self.n_inf)

    @property
    def w(self) -> np.ndarray:
        r"""Habit multiplicity of message sets with exactly m informative channels, m = 0..mmax."""
        return np.array([comb(self.n_inf, m) * sum(comb(self.n_zero, c) for c in range(0, self.kmsg - m + 1))
                         for m in range(self.mmax + 1)], dtype=float)


def efe(par: Par, P00, P01, P11) -> np.ndarray:
    r"""G[..., m, n] = -I(target; own sensor + m relays + n slots) + psi n under the prior P^- (arrays)."""
    m = np.arange(par.mmax + 1, dtype=float)[:, None]
    ns = np.arange(par.nslots + 1, dtype=float)[None, :]
    a = 1.0 / par.R + ns / par.Rs
    b = m / (par.R + par.Rc)
    p00 = np.asarray(P00)[..., None, None]
    p01 = np.asarray(P01)[..., None, None]
    p11 = np.asarray(P11)[..., None, None]
    if par.target == "x":
        # I = 1/2 ln det(I + P diag(a, b))
        info = 0.5 * np.log((1 + a * p00) * (1 + b * p11) - a * b * p01 ** 2)
    elif par.target == "eta":
        det = p00 * p11 - p01 ** 2
        i00, i01, i11 = p11 / det, -p01 / det, p00 / det
        L00, L11 = i00 + a, i11 + b
        post00 = L11 / (L00 * L11 - i01 ** 2)
        info = 0.5 * np.log(p00 / post00)
    else:
        raise ValueError(par.target)
    return -info + par.psi * ns


def _lse(x: np.ndarray, axis: int) -> np.ndarray:
    mx = x.max(axis=axis, keepdims=True)
    return (mx + np.log(np.exp(x - mx).sum(axis=axis, keepdims=True))).squeeze(axis)


@dataclass
class Out:
    S: np.ndarray                      # Sigma^c estimate (n x n), pooled
    S_batches: np.ndarray              # per-batch estimates (nb x n x n)
    open_rate: float
    dev_rate: float                    # fraction of member-rounds reading fewer than mmax informative relays
    inf: dict = field(default_factory=dict)
    agency: dict = field(default_factory=dict)


def run(par: Par, K: int, T: int, burn: int, seed: int, mode: str = "full", shared_world: bool = True,
        fixed_slots: int = 0, nbatch: int = 20, want_inf: bool = False, want_agency: bool = False,
        dead_relays: bool = False, share_slots: bool = False, att_habit: str = "uniform",
        hab_m=None) -> Out:
    r"""share_slots: the two replicas of a world share the reviser clock and the slot path (reading in which slot
    statuses are world states, so that the world-conditional law conditions on them); their attention and private
    noises stay independent.  att_habit: 'uniform' (declared) or 'mates' (habits concentrated on the set of all
    informative mates; attention then never departs from its habits)."""
    rng = np.random.default_rng(seed)
    n = par.n
    B = 2 * K
    Kw = K if shared_world else B
    world_of = np.repeat(np.arange(K), 2) if shared_world else np.arange(B)
    V0 = par.Q / (1 - par.F ** 2)
    eta = rng.normal(0.0, np.sqrt(V0), Kw)
    w = par.w if hab_m is None else np.asarray(hab_m, float)   # habit mass on message sets with m informative
    lw_hab = np.log(w)
    M = par.mmax + 1
    F = par.F
    p0 = par.p0
    P00 = np.full((B, n), F * F * p0 + par.Q + par.qc)
    P01 = np.full((B, n), F * p0)
    P11 = np.full((B, n), p0 + par.qc)
    m0 = np.zeros((B, n))
    m1 = np.zeros((B, n))
    if mode == "fixed":
        slots = np.zeros((B, n), dtype=int)
        slots[:, :fixed_slots] = 1
    else:
        slots = np.zeros((B, n), dtype=int)
    att = np.zeros((B, n, n), dtype=bool)
    s_prev = np.zeros((B, n))
    eye = np.eye(n, dtype=bool)
    ar = np.arange(B)
    S_acc = np.zeros((K, n, n))
    cnt = 0
    dev = 0
    devn = 0
    open_acc = 0.0
    # union filter (inference clause): mean (u0, u1), covariance (U00, U01, U11) per system
    u0 = np.zeros(B); u1 = np.zeros(B)
    U00 = np.full(B, V0); U01 = np.full(B, F * V0); U11 = np.full(B, V0)
    inf_acc = {k: 0.0 for k in ("n", "d0sq_over", "inv00", "ln00", "claim1", "q2", "lndet", "claim2",
                                "rev1_P", "rev1_dd", "rev2_00", "rev2_01", "rev2_11", "d0sq", "inv2_00",
                                "inv2_01", "inv2_11", "prop1")}
    ag = {"sym": [], "p": [], "newcount": [], "curcount": [], "klatt": [], "qm3": [], "qm_mean": []}
    for t in range(T):
        eta_b = eta[world_of]
        e = m0 - eta_b[:, None]                                  # prior error of eta_t
        if t >= burn:
            if shared_world:
                d = e[0::2] - e[1::2]                           # (K, n)
                S_acc += 0.5 * d[:, :, None] * d[:, None, :]
            else:
                d = e[0::2] - e[1::2]
                S_acc += 0.5 * d[:, :, None] * d[:, None, :]
            cnt += 1
            open_acc += slots.mean()
            if want_inf:
                yb0 = m0.mean(1); yb1 = m1.mean(1)
                dd0 = yb0 - u0; dd1 = yb1 - u1
                det = U00 * U11 - U01 ** 2
                j00, j01, j11 = U11 / det, -U01 / det, U00 / det
                inf_acc["n"] += B
                inf_acc["d0sq_over"] += np.sum(dd0 ** 2 / U00)
                inf_acc["d0sq"] += np.sum(dd0 ** 2)
                inf_acc["inv00"] += np.sum(1.0 / U00)
                inf_acc["ln00"] += np.sum(np.log(U00))
                pc00 = P00.mean(1); pc01 = P01.mean(1); pc11 = P11.mean(1)
                rat = pc00 / U00
                inf_acc["claim1"] += np.sum(rat - 1 - np.log(rat))
                inf_acc["prop1"] += np.sum(rat)
                inf_acc["q2"] += np.sum(j00 * dd0 ** 2 + 2 * j01 * dd0 * dd1 + j11 * dd1 ** 2)
                inf_acc["lndet"] += np.sum(np.log(det))
                inf_acc["inv2_00"] += np.sum(j00); inf_acc["inv2_01"] += np.sum(j01); inf_acc["inv2_11"] += np.sum(j11)
                trc = j00 * pc00 + 2 * j01 * pc01 + j11 * pc11
                detc = pc00 * pc11 - pc01 ** 2
                inf_acc["claim2"] += np.sum(trc - 2 - np.log(detc / det))
                inf_acc["rev1_P"] += np.sum(U00); inf_acc["rev1_dd"] += np.sum(dd0 ** 2)
                inf_acc["rev2_00"] += np.sum(U00 + dd0 ** 2)
                inf_acc["rev2_01"] += np.sum(U01 + dd0 * dd1)
                inf_acc["rev2_11"] += np.sum(U11 + dd1 ** 2)
        # ---------------- observations of round t ----------------
        s = eta_b[:, None] + np.sqrt(par.R) * rng.standard_normal((B, n))
        nopen = slots.sum(1).astype(float)
        slot_sum = nopen[:, None] * eta_b[:, None] + np.sqrt(nopen[:, None] * par.Rs) * rng.standard_normal((B, n))
        mcount = att.sum(2).astype(float)
        if dead_relays:
            relay_sum = np.sqrt(mcount * (par.R + par.Rc)) * rng.standard_normal((B, n)) \
                + mcount * eta_b[:, None] * 0.0
        else:
            relay_sum = np.einsum("bij,bj->bi", att, s_prev) + np.sqrt(mcount * par.Rc) * rng.standard_normal((B, n))
        # ---------------- exact update (information form) ----------------
        det = P00 * P11 - P01 ** 2
        i00, i01, i11 = P11 / det, -P01 / det, P00 / det
        a = 1.0 / par.R + nopen[:, None] / par.Rs
        bb = mcount / (par.R + par.Rc)
        L00, L01, L11 = i00 + a, i01, i11 + bb
        h0 = i00 * m0 + i01 * m1 + s / par.R + slot_sum / par.Rs
        h1 = i01 * m0 + i11 * m1 + relay_sum / (par.R + par.Rc)
        dL = L00 * L11 - L01 ** 2
        Q00, Q01, Q11 = L11 / dL, -L01 / dL, L00 / dL
        mp0 = Q00 * h0 + Q01 * h1
        # (mp1 not needed: A_F discards the second component)
        m0 = F * mp0 + np.sqrt(par.qc) * rng.standard_normal((B, n))
        m1 = mp0 + np.sqrt(par.qc) * rng.standard_normal((B, n))
        P00 = F * F * Q00 + par.Q + par.qc
        P01 = F * Q00
        P11 = Q00 + par.qc
        # union filter update and prediction
        if want_inf:
            dU = U00 * U11 - U01 ** 2
            k00, k01, k11 = U11 / dU, -U01 / dU, U00 / dU
            aU = n / par.R + n * nopen / par.Rs
            g0 = k00 * u0 + k01 * u1 + s.sum(1) / par.R + slot_sum.sum(1) / par.Rs
            g1 = k01 * u0 + k11 * u1
            M00, M01, M11 = k00 + aU, k01, k11
            dM = M00 * M11 - M01 ** 2
            W00, W01, W11 = M11 / dM, -M01 / dM, M00 / dM
            up0 = W00 * g0 + W01 * g1
            u0, u1 = F * up0, up0
            U00, U01, U11 = F * F * W00 + par.Q, F * W00, W00
        # ---------------- policies for round t+1 ----------------
        if mode == "fixed":
            mdraw = np.full((B, n), par.mmax)
            new_slots = slots
            r = None
        else:
            cur = slots.sum(1)
            r = rng.integers(n, size=B)
            if share_slots:
                r[1::2] = r[0::2]
            if mode == "hab":
                pr_open = np.full(B, 0.5)
                if att_habit == "mates":
                    qm = np.zeros((B, n, M)); qm[:, :, -1] = 1.0
                else:
                    qm = np.broadcast_to(w / w.sum(), (B, n, M))
            else:
                G = efe(par, P00, P01, P11)                       # (B, n, M, NS)
                if mode == "pr":
                    # partners: kmsg of the n_inf + n_zero channels uniformly; informative count hypergeometric
                    mdraw_pr = rng.hypergeometric(par.n_inf, par.n_zero, par.kmsg, size=(B, n))
                    Gr = G[ar, r, mdraw_pr[ar, r], :]               # (B, NS)
                else:
                    Gt = -_lse(lw_hab[None, None, :, None] - par.gamma * G, axis=2) / par.gamma   # (B, n, NS)
                    Gr = Gt[ar, r, :]
                n_oth = cur - slots[ar, r]
                dlog = par.gamma * (Gr[ar, n_oth] - Gr[ar, n_oth + 1])
                pr_open = 0.5 * (1.0 + np.tanh(0.5 * dlog))
            new = (rng.random(B) < pr_open).astype(int)
            if share_slots:
                new[1::2] = new[0::2]
            new_slots = slots.copy()
            new_slots[ar, r] = new
            newcount = new_slots.sum(1)
            if mode == "pr":
                mdraw = mdraw_pr
                qm = None
            else:
                if mode != "hab":
                    if att_habit == "mates":
                        qm = np.zeros((B, n, M)); qm[:, :, -1] = 1.0
                    else:
                        nk = np.where(np.arange(n)[None, :] == r[:, None], newcount[:, None], cur[:, None])
                        Gk = np.take_along_axis(G, nk[:, :, None, None], axis=3)[..., 0]     # (B, n, M)
                        lq = lw_hab[None, None, :] - par.gamma * Gk
                        lq = lq - lq.max(axis=2, keepdims=True)
                        qm = np.exp(lq)
                        qm /= qm.sum(axis=2, keepdims=True)
                u = rng.random((B, n, 1))
                mdraw = np.minimum((u > np.cumsum(qm, axis=2)).sum(axis=2), par.mmax)
            if want_agency and t >= burn:
                pp = Q00
                ag["sym"].append(np.ptp(pp, axis=1) < 1e-12)
                ag["p"].append(pp[:, 0].copy())
                ag["newcount"].append(newcount.copy())
                ag["curcount"].append(cur.copy())
                if qm is not None:
                    hab = w / w.sum()
                    with np.errstate(divide="ignore", invalid="ignore"):
                        kl = np.where(qm > 0, qm * (np.log(qm) - np.log(hab)[None, None, :]), 0.0).sum(2)
                    ag["klatt"].append(kl.sum(1))
                    ag["qm3"].append(qm[:, :, -1].mean(1))
                    ag["qm_mean"].append(np.asarray(qm).mean(0))      # (n, M): per-member law of m, averaged over systems
        if t >= burn:
            dev += int((mdraw < par.mmax).sum())
            devn += mdraw.size
        # attention sets: a uniformly random mdraw-subset of the informative mates (all other members)
        keys = rng.random((B, n, n))
        keys[:, eye] = 2.0
        rank = np.argsort(np.argsort(keys, axis=2), axis=2)
        att = rank < mdraw[:, :, None]
        slots = new_slots
        s_prev = s
        eta = F * eta + np.sqrt(par.Q) * rng.standard_normal(Kw)
    S_world = S_acc / cnt
    nb = nbatch
    S_b = np.array([S_world[i::nb].mean(0) for i in range(nb)])
    out = Out(S=S_world.mean(0), S_batches=S_b, open_rate=open_acc / cnt, dev_rate=dev / max(devn, 1))
    if want_inf:
        out.inf = inf_acc
    if want_agency:
        out.agency = {k: (np.concatenate(v) if (len(v) and np.ndim(v[0]) == 1) else (np.concatenate(v, 0) if len(v) else None))
                      for k, v in ag.items()}
    return out


# ------------------------------------------------------------------------------------------------------------
# contrast machinery written from def:col-contrast (04_collectives.tex:182-188) and eq:col-diffusive (:147-151)
# ------------------------------------------------------------------------------------------------------------

def is_diffusive(Pi: np.ndarray, tol: float = 0.0):
    off = Pi - np.diag(np.diag(Pi))
    return bool(off.max() <= tol and Pi.sum(1).min() >= -tol), float(off.max()), float(Pi.sum(1).min())


def contrast(Pi: np.ndarray, C) -> float:
    C = list(C)
    n = len(C)
    eps = Pi.sum(1)
    a = -(Pi - np.diag(np.diag(Pi)))
    aC = a[np.ix_(C, C)]
    LC = np.diag(aC.sum(1)) - aC
    Mx = np.diag(eps[C]) + LC
    phi = np.ones(n) / np.sqrt(n)
    xout = float(phi @ Pi[np.ix_(C, C)] @ phi)
    # orthonormal basis of 1^perp
    Z = np.linalg.svd(np.eye(n) - np.outer(phi, phi))[0][:, : n - 1]
    xin = float(np.linalg.eigvalsh(Z.T @ Mx @ Z).min())
    return xin / xout


def compound(S: np.ndarray):
    n = S.shape[0]
    dg = np.trace(S) / n
    of = (S.sum() - np.trace(S)) / (n * (n - 1))
    return dg - of, of


def r_ab(n: int, al: float, be: float) -> float:
    return 1.0 + n * be / al
