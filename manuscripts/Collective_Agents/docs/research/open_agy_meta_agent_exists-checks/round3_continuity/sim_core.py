r"""O6: policy-covariance chain of instance I* with a FIXED number of uniforms per round (coupling-ready).

Same model and kernels as lib.simulate_policy_path (T-fast, mode 'full') and lib.simulate_policy_path_real (T-real,
mode 'full') of round2_epistemic_persistent (read-only import), but every round consumes exactly
    U = (U0, U1, U2[0..n-1], U3[0..n-1, 0..n-2])   (2 + n + n(n-1) uniforms),
so two copies driven by the same uniforms form a valid (synchronous, inverse-CDF) coupling of the chain.

Chain (record C11): Z_t = (p(t-1), pi_t), p = members' posterior variances of eta, pi = (slot profile, attention sets).
  update      p_i(t) = g(p_i(t-1); a = 1/R + |slots_t|/Rs, b = |mates_i(t)|/(R+Rc))       (Riccati, data-free)
  T-fast      slots_{t+1} ~ stationary law of the (P4) chain at the frozen decision state p(t) (computed exactly by
              lib.p4_chain at every state; at symmetric states it equals the Gibbs law used by lib);
  T-real      one reviser r = floor(n U0) flips its slot with probability logistic(gamma (Gt_r(S) - Gt_r(S+1)));
  attention   m_i ~ Gibbs(w(m) exp(-gamma G_i[m, count known to i])), mates = the m_i others with smallest keys U3_i.
gamma = inf: best response (soft-min -> min, logistic -> step), attention argmin.
"""
from __future__ import annotations

import os
import sys
for _v in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS"):
    os.environ[_v] = "1"
LIB = r"C:/Users/chris and christine/Desktop/Research/manuscripts/Collective_Agents/docs/research/open_agy_meta_agent_exists-checks/round2_epistemic_persistent"
if LIB not in sys.path:
    sys.path.insert(0, LIB)
from dataclasses import dataclass

import numpy as np
from lib import Par, Pminus, posterior, efe_table, softmin_att, attention_weights, p4_chain, profiles, Path

INF = float("inf")


def n_uniforms(n: int) -> int:
    return 2 + n + n * (n - 1)


@dataclass
class State:
    p: np.ndarray          # (n,) posterior variances after the previous round's update
    slots: np.ndarray      # (n,) slot profile used in the current round
    mates: list            # mates[i] = tuple of mates whose relay i reads in the current round


def _inv_cdf(prob: np.ndarray, u: float) -> int:
    c = np.cumsum(prob)
    k = int(np.searchsorted(c, u * c[-1], side="right"))
    return min(k, len(prob) - 1)


def _att_law(par: Par, Grow_by_m: np.ndarray, w: np.ndarray) -> np.ndarray:
    r"""Gibbs law of the number m of informative relays: w(m) exp(-gamma G[m]) (argmin at gamma = inf)."""
    if par.gamma == INF:
        q = np.zeros(len(w)); q[int(np.argmin(Grow_by_m))] = 1.0
        return q
    lw = np.log(w) - par.gamma * Grow_by_m
    lw -= lw.max()
    q = np.exp(lw)
    return q / q.sum()


def _mates_from_keys(i: int, n: int, m: int, keys: np.ndarray) -> tuple:
    others = [j for j in range(n) if j != i]
    order = np.argsort(keys)               # keys has length n-1, one per other member (fixed order)
    return tuple(sorted(others[k] for k in order[:m]))


def step(par: Par, st: State, U: np.ndarray, protocol: str) -> tuple[State, np.ndarray]:
    r"""One round: Riccati update with the current policy, then the decision for the next round.
    Returns (new state, prior covariances used in this round (n,2,2))."""
    n = par.n
    w = attention_weights(par, n - 1, par.n_zero)
    mmax = len(w) - 1
    Pms = np.array([Pminus(par, st.p[i]) for i in range(n)])
    vis = int(st.slots.sum())
    p_new = np.array([posterior(Pms[i], 1.0 / par.R + vis / (par.Rs + par.Rsh),
                                len(st.mates[i]) / (par.R + par.Rc))[0, 0] for i in range(n)])
    G = [efe_table(par, Pminus(par, p_new[i]), mmax, n) for i in range(n)]
    U0, U1, U2, U3 = U[0], U[1], U[2:2 + n], U[2 + n:].reshape(n, n - 1)
    if protocol == "fast":
        if par.gamma == INF:
            raise ValueError("T-fast at gamma = inf is not used")
        Gt = np.array([softmin_att(par, G[i], w) for i in range(n)])
        law, _ = p4_chain(par.gamma, Gt)
        P_ = profiles(n)
        new_slots = P_[_inv_cdf(law, U1)].copy()
        known = [int(new_slots.sum())] * n
    elif protocol == "real":
        r = min(int(U0 * n), n - 1)
        if par.gamma == INF:
            Gr = G[r].min(axis=0)
        else:
            Gr = softmin_att(par, G[r], w)
        Sm = int(st.slots.sum() - st.slots[r])
        if par.gamma == INF:
            d = Gr[Sm] - Gr[Sm + 1]
            pr1 = 1.0 if d > 0 else (0.0 if d < 0 else 0.5)
        else:
            pr1 = 0.5 * (1 + np.tanh(0.5 * par.gamma * (Gr[Sm] - Gr[Sm + 1])))
        new_slots = st.slots.copy()
        new_slots[r] = int(U1 < pr1)
        known = [int(new_slots.sum()) if i == r else int(st.slots.sum()) for i in range(n)]
    else:
        raise ValueError(protocol)
    new_mates = []
    for i in range(n):
        q = _att_law(par, G[i][:, known[i]], w)
        m = _inv_cdf(q, U2[i])
        new_mates.append(_mates_from_keys(i, n, m, U3[i]) if m > 0 else tuple())
    return State(p_new, new_slots, new_mates), Pms


def run_path(par: Par, T: int, rng: np.random.Generator, protocol: str, st0: State | None = None) -> Path:
    r"""A policy path in lib's Path format (Pm = prior covariance at round t, mates, slots, vis)."""
    n = par.n
    st = st0 if st0 is not None else State(np.full(n, 0.09), np.zeros(n, dtype=int), [tuple()] * n)
    Pm_hist = np.zeros((T, n, 2, 2))
    slots = np.zeros((T, n), dtype=int)
    vis = np.zeros((T, n), dtype=int)
    mates = []
    dev = 0
    nu = n_uniforms(n)
    for t in range(T):
        slots[t] = st.slots
        vis[t] = int(st.slots.sum())
        mates.append(st.mates)
        dev += sum(1 for mt in st.mates if len(mt) < n - 1)
        st, Pms = step(par, st, rng.random(nu), protocol)
        Pm_hist[t] = Pms
    return Path(Pm_hist, mates, slots, vis, dev)


def coupled_run(par: Par, T: int, rng: np.random.Generator, protocol: str, sa: State, sb: State,
                par_b: Par | None = None):
    r"""Two copies driven by the same uniforms.  Returns per-round policy equality and |p_a - p_b|_inf."""
    pb = par if par_b is None else par_b
    eq = np.zeros(T, dtype=bool)
    dp = np.zeros(T)
    nu = n_uniforms(par.n)
    for t in range(T):
        eq[t] = bool(np.array_equal(sa.slots, sb.slots) and sa.mates == sb.mates)
        dp[t] = float(np.max(np.abs(sa.p - sb.p)))
        U = rng.random(nu)
        sa, _ = step(par, sa, U, protocol)
        sb, _ = step(pb, sb, U, protocol)
    return eq, dp
