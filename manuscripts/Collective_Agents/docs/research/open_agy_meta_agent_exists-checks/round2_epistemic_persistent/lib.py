r"""Persistent-world epistemic niche (record obligation O1): library.

Model (declared in the report):
  world, per niche component: eta_{t+1} = F eta_t + w_t, w_t ~ N(0,Q), stationary, 0 < F < 1, Q > 0.
  member state x_t = (eta_t, eta_{t-1}); prior belief N(m^-_i(t), P^-_i(t)); prior error e_i(t) = m^-_{i,0}(t) - eta_t.
  observations of round t (attention decided at round t-1):
    own sensor      s_i(t) = eta_t + v_i(t),                  row [1,0], noise R      (structural, always read)
    relay of mate j y_ij(t) = s_j(t-1) + nu_ij(t),            row [0,1], noise R+Rc   (one-round latency)
    open slot k     o_ik(t) = eta_t + rho_ik(t),              row [1,0], noise Rs     (public channel, every member)
  exact Kalman update; prediction m^-(t+1) = A_F m^+(t) + xi(t), xi ~ N(0, qc I_2), A_F = [[F,0],[1,0]],
  P^-(t+1) = A_F P^+ A_F^T + diag(Q,0) + qc I_2   (P^- depends on P^+ only through p = P^+_{00}).
Policies (decided at round t for round t+1), one precision gamma:
  attention: J^msg subset of the message channels, |J^msg| <= kmsg; habits uniform over those subsets;
             the own sensor and every slot channel are structural members of the attention set.
  slot: pi_k in {0,1}, uniform product habits; slot preference: cost psi per open slot (slot-product).
  EFE of member i:  G_i(m, n) = -I(x_{t+1}; o_{t+1}) + psi * n,  m = informative relays read, n = open slots read.
  Protocol: slots by (P4) on the members' marginal policy posteriors (soft-min over attention), then attention
  drawn from its conditional policy posterior given the deliberated profile.
"""
from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
import itertools
from dataclasses import dataclass, replace
from math import comb

import numpy as np


@dataclass(frozen=True)
class Par:
    F: float = 0.9
    Q: float = 0.05
    R: float = 1.0
    Rc: float = 0.2
    Rs: float = 2.0       # private read noise of a slot reading
    Rsh: float = 0.0      # instrument noise of a slot, shared by its readers (sender-side, conditioned)
    psi: float = 0.024
    gamma: float = 400.0
    qc: float = 1e-4
    n: int = 4            # members whose relays are informative to each other (niche size; N in the medium)
    n_zero: int = 4       # zero-gain message channels available to each member (the other niche)
    kmsg: int = 3         # message capacity: kappa minus the structural own sensor and slot channels

    def with_(self, **kw) -> "Par":
        return replace(self, **kw)


def A_F(F: float) -> np.ndarray:
    return np.array([[F, 0.0], [1.0, 0.0]])


def Pminus(par: Par, p: float) -> np.ndarray:
    r"""Prior covariance of x_{t+1} from the posterior variance p of eta_t: A_F P^+ A_F^T + diag(Q,0) + qc I."""
    F = par.F
    return np.array([[F * F * p + par.Q + par.qc, F * p], [F * p, p + par.qc]])


def info_ab(Pm: np.ndarray, a, b):
    r"""I(x; o) = 1/2 ln det(I + P^- diag(a,b)) = 1/2 ln[(1+a P00)(1+b P11) - a b P01^2] (vectorized in a, b)."""
    a = np.asarray(a, float)
    b = np.asarray(b, float)
    return 0.5 * np.log((1 + a * Pm[0, 0]) * (1 + b * Pm[1, 1]) - a * b * Pm[0, 1] ** 2)


def posterior(Pm: np.ndarray, a: float, b: float) -> np.ndarray:
    Im = np.linalg.inv(Pm)
    return np.linalg.inv(Im + np.diag([a, b]))


def attention_weights(par: Par, n_inf: int, n_zero: int) -> np.ndarray:
    r"""Habit multiplicity w(m) of message sets of size <= kmsg containing exactly m informative channels."""
    k = par.kmsg
    w = np.zeros(min(k, n_inf) + 1)
    for m in range(len(w)):
        w[m] = comb(n_inf, m) * sum(comb(n_zero, c) for c in range(0, k - m + 1))
    return w


def efe_table(par: Par, Pm: np.ndarray, mmax: int, nslots: int) -> np.ndarray:
    r"""G[m, n] = -I(x; own + m relays + n slots) + psi n."""
    m = np.arange(mmax + 1)[:, None]
    nn = np.arange(nslots + 1)[None, :]
    a = 1.0 / par.R + nn / (par.Rs + par.Rsh)
    b = m / (par.R + par.Rc)
    return -info_ab(Pm, a, b) + par.psi * nn


def softmin_att(par: Par, G: np.ndarray, w: np.ndarray) -> np.ndarray:
    r"""Marginal slot EFE: Gt[n] = -(1/gamma) ln sum_m w(m) exp(-gamma G[m,n])."""
    g = par.gamma
    X = -g * G + np.log(w)[:, None]
    mx = X.max(axis=0)
    return -(mx + np.log(np.exp(X - mx).sum(axis=0))) / g


def profiles(n: int) -> np.ndarray:
    return np.array(list(itertools.product([0, 1], repeat=n)), dtype=int)


_PROF_CACHE: dict = {}


def _prof(n: int):
    if n not in _PROF_CACHE:
        P = profiles(n)
        _PROF_CACHE[n] = (P, {tuple(p): k for k, p in enumerate(P)})
    return _PROF_CACHE[n]


def p4_chain(gamma: float, Gt: np.ndarray, habits1: np.ndarray | None = None):
    r"""(P4) chain over slot profiles. Gt[i, n_total] is member i's (marginal) EFE as a function of the total number
    of open slots; habits1[i] = E_i(1). Returns (stationary law over profiles, transition matrix)."""
    nmem = Gt.shape[0]
    P, idx = _prof(nmem)
    M = len(P)
    if habits1 is None:
        habits1 = np.full(nmem, 0.5)
    T = np.zeros((M, M))
    S = P.sum(1)
    ks = np.arange(M)
    for i in range(nmem):
        bit = 2 ** (nmem - 1 - i)          # itertools.product order: member 0 is the most significant bit
        Sm = S - P[:, i]
        d = (np.log(habits1[i]) - gamma * Gt[i, Sm + 1]) - (np.log(1 - habits1[i]) - gamma * Gt[i, Sm])
        pr1 = 0.5 * (1 + np.tanh(0.5 * d))  # logistic, overflow-safe
        t0 = ks - P[:, i] * bit
        np.add.at(T, (ks, t0), (1 - pr1) / nmem)
        np.add.at(T, (ks, t0 + bit), pr1 / nmem)
    Aeq = T.T - np.eye(M)
    Aeq[-1, :] = 1.0
    rhs = np.zeros(M); rhs[-1] = 1.0
    v = np.linalg.solve(Aeq, rhs)
    v = np.clip(v, 0.0, None); v /= v.sum()
    return v, T


def gibbs_law_sym(gamma: float, Gt_row: np.ndarray, nmem: int) -> np.ndarray:
    r"""Law of the number of open slots at a symmetric decision state: P(n) ∝ C(nmem,n) exp(-gamma Gt(n))."""
    lw = np.array([np.log(comb(nmem, k)) - gamma * Gt_row[k] for k in range(nmem + 1)])
    lw -= lw.max()
    p = np.exp(lw)
    return p / p.sum()


# ----------------------------------------------------------------------------------------------------------------
# policy path simulation for one group of members
# ----------------------------------------------------------------------------------------------------------------

@dataclass
class Path:
    Pm: np.ndarray        # (T, nmem, 2, 2) claimed prior covariance at round t (before the update of round t)
    mates: list           # mates[t][i] = tuple of mates whose relay i reads at round t
    slots: np.ndarray     # (T, nmem) slot open at round t
    vis: np.ndarray       # (T, nmem) number of open slots that member i reads at round t
    att_dev: int          # number of member-rounds with fewer than the maximal number of informative relays


def simulate_policy_path(par: Par, T: int, rng: np.random.Generator, mode: str = "full",
                         p0: float | None = None, sym_tol: float = 1e-11, fixed_slots: int | None = None) -> Path:
    r"""Simulate the policy/covariance process of one group of par.n members (claimed covariances).
    mode: 'full'  EFE attention and (P4) slots (marginal policy posteriors), attention drawn given the profile;
          'hab'   gamma = 0: attention and slots from the habits;
          'pr'    partners redrawn every round, kmsg uniformly among the message channels; slots by (P4) given the
                  drawn partners (exact EFE given the partners);
          'lp'    inter-agent channels deliver pure noise, receivers keep their assigned precisions (claimed
                  covariances as in the full model), intentions deleted: each member decides its slot alone with the
                  others' slots treated as closed; attention by EFE (pattern kept);
          'fr'    every other agent frozen at its initial state in each member's update and action law: relays carry
                  the declared deterministic initial content 0, the others' slots appear closed, slots decided alone;
          'fixed' all mates read every round; fixed_slots of the slots (members 0..k-1) open every round;
          'inf'   diagnostic for N_inf under the reading that slot switching is an act: intention announcements
                  deleted (each member decides its slot alone, others treated as closed), everything else full."""
    nmem = par.n
    n_inf = nmem - 1
    w_full = attention_weights(par, n_inf, par.n_zero)
    mmax = len(w_full) - 1
    if p0 is None:
        p0 = 0.09
    p = np.full(nmem, p0)
    Pm_hist = np.zeros((T, nmem, 2, 2))
    slots = np.zeros((T, nmem), dtype=int)
    vis = np.zeros((T, nmem), dtype=int)
    mates: list = []
    cur_slots = np.zeros(nmem, dtype=int)
    cur_m = [tuple() for _ in range(nmem)]
    dev = 0
    others_list = [[j for j in range(nmem) if j != i] for i in range(nmem)]
    P_, _ = _prof(nmem)
    for t in range(T):
        Pms = [Pminus(par, p[i]) for i in range(nmem)]
        for i in range(nmem):
            Pm_hist[t, i] = Pms[i]
        slots[t] = cur_slots
        if mode == "fr":
            vis[t] = cur_slots
        else:
            vis[t] = int(cur_slots.sum())
        mates.append(cur_m)
        for i in range(nmem):
            P_plus = posterior(Pms[i], 1.0 / par.R + vis[t, i] / (par.Rs + par.Rsh), len(cur_m[i]) / (par.R + par.Rc))
            p[i] = P_plus[0, 0]
        Pnext = [Pminus(par, p[i]) for i in range(nmem)]
        if mode == "fixed":
            k = nmem if fixed_slots is None else fixed_slots
            new_slots = np.zeros(nmem, dtype=int); new_slots[:k] = 1
            new_m = [tuple(others_list[i]) for i in range(nmem)]
        elif mode == "hab":
            new_slots = (rng.random(nmem) < 0.5).astype(int)
            new_m = []
            for i in range(nmem):
                m = rng.choice(mmax + 1, p=w_full / w_full.sum())
                if m < mmax:
                    dev += 1
                new_m.append(tuple(sorted(rng.choice(others_list[i], size=m, replace=False))) if m > 0 else tuple())
        else:
            G = [efe_table(par, Pnext[i], mmax, nmem) for i in range(nmem)]
            if mode == "pr":
                tot = n_inf + par.n_zero
                new_m = []
                for i in range(nmem):
                    pick = rng.choice(tot, size=par.kmsg, replace=False)
                    inf = [others_list[i][k] for k in pick if k < n_inf]
                    if len(inf) < mmax:
                        dev += 1
                    new_m.append(tuple(sorted(inf)))
                Gt = np.array([G[i][len(new_m[i]), :] for i in range(nmem)])
            else:
                Gt = np.array([softmin_att(par, G[i], w_full) for i in range(nmem)])
            if mode in ("lp", "fr", "inf"):
                new_slots = np.zeros(nmem, dtype=int)
                for i in range(nmem):
                    pr1 = 1.0 / (1.0 + np.exp(par.gamma * (Gt[i, 1] - Gt[i, 0])))
                    new_slots[i] = int(rng.random() < pr1)
            else:
                sym = np.max(np.abs(Gt - Gt[0])) < sym_tol
                if sym:
                    law_n = gibbs_law_sym(par.gamma, Gt[0], nmem)
                    k = rng.choice(nmem + 1, p=law_n)
                    new_slots = np.zeros(nmem, dtype=int)
                    if k > 0:
                        new_slots[rng.choice(nmem, size=k, replace=False)] = 1
                else:
                    law, _ = p4_chain(par.gamma, Gt)
                    new_slots = P_[rng.choice(len(P_), p=law)].copy()
            if mode in ("full", "lp", "fr", "inf"):
                new_m = []
                for i in range(nmem):
                    no = int(new_slots[i]) if mode == "fr" else int(new_slots.sum())
                    lw = np.log(w_full) - par.gamma * G[i][:, no]
                    lw -= lw.max()
                    pr = np.exp(lw); pr /= pr.sum()
                    m = rng.choice(mmax + 1, p=pr)
                    if m < mmax:
                        dev += 1
                    new_m.append(tuple(sorted(rng.choice(others_list[i], size=m, replace=False))) if m > 0 else tuple())
        cur_slots = new_slots
        cur_m = new_m
    return Path(Pm_hist, mates, slots, vis, dev)


def simulate_policy_path_real(par: Par, T: int, rng: np.random.Generator, mode: str = "full",
                              p0: float | None = None, record_dec: bool = False):
    r"""Real-time (P4): one deliberation event per round.  At the end of round t one member r, chosen uniformly,
    resamples its slot for round t+1 from its marginal policy posterior (soft-min of its full EFE over its attention
    sets) given the others' slots, which it observes on the slot channels it reads (no intention messages); the
    others keep their slots.  Every member then draws its attention for round t+1 from its conditional policy
    posterior given the profile it knows (the reviser: the new profile; the others: the current one, since the
    reviser's change reaches them only when the slot opens).  No message is faster than one round.
    mode: 'full'; 'hab' (gamma = 0: the reviser draws its slot and every member its attention from the habits);
    'pr' (partners redrawn uniformly every round, kmsg of the message channels; reviser's EFE given its partners);
    'lp' (relays deliver pure noise, assigned precisions kept; slots kept and observed); 'fr' (others frozen at the
    initial state: relays carry 0, the others' slots appear closed); 'inf' (diagnostic for the reading in which a
    slot switch is an act: the others' slot channels deliver noise, so each member reads only its own slot).
    If record_dec, also returns the decision record: list of (t, p of every member at the decision, new profile)."""
    nmem = par.n
    n_inf = nmem - 1
    w_full = attention_weights(par, n_inf, par.n_zero)
    mmax = len(w_full) - 1
    p = np.full(nmem, 0.09 if p0 is None else p0)
    Pm_hist = np.zeros((T, nmem, 2, 2))
    slots = np.zeros((T, nmem), dtype=int)
    vis = np.zeros((T, nmem), dtype=int)
    mates: list = []
    cur_slots = np.zeros(nmem, dtype=int)
    cur_m = [tuple() for _ in range(nmem)]
    dev = 0
    others_list = [[j for j in range(nmem) if j != i] for i in range(nmem)]
    dec = []
    own_only = mode in ("fr", "inf")
    for t in range(T):
        Pms = [Pminus(par, p[i]) for i in range(nmem)]
        for i in range(nmem):
            Pm_hist[t, i] = Pms[i]
        slots[t] = cur_slots
        vis[t] = cur_slots if own_only else int(cur_slots.sum())
        mates.append(cur_m)
        for i in range(nmem):
            p[i] = posterior(Pms[i], 1.0 / par.R + vis[t, i] / (par.Rs + par.Rsh),
                             len(cur_m[i]) / (par.R + par.Rc))[0, 0]
        Pnext = [Pminus(par, p[i]) for i in range(nmem)]
        r = int(rng.integers(nmem))
        new_slots = cur_slots.copy()
        if mode == "hab":
            new_slots[r] = int(rng.random() < 0.5)
            new_m = []
            for i in range(nmem):
                m = rng.choice(mmax + 1, p=w_full / w_full.sum())
                if m < mmax:
                    dev += 1
                new_m.append(tuple(sorted(rng.choice(others_list[i], size=m, replace=False))) if m > 0 else tuple())
        else:
            G = [efe_table(par, Pnext[i], mmax, nmem) for i in range(nmem)]
            if mode == "pr":
                tot = n_inf + par.n_zero
                new_m = []
                for i in range(nmem):
                    pick = rng.choice(tot, size=par.kmsg, replace=False)
                    inf = [others_list[i][k] for k in pick if k < n_inf]
                    if len(inf) < mmax:
                        dev += 1
                    new_m.append(tuple(sorted(inf)))
                Gr = G[r][len(new_m[r]), :]
            else:
                Gr = softmin_att(par, G[r], w_full)
            Sm = 0 if own_only else int(cur_slots.sum() - cur_slots[r])
            pr1 = 0.5 * (1 + np.tanh(0.5 * par.gamma * (Gr[Sm] - Gr[Sm + 1])))
            new_slots[r] = int(rng.random() < pr1)
            if mode != "pr":
                new_m = []
                for i in range(nmem):
                    if own_only:
                        no = int(new_slots[i])
                    else:
                        no = int(new_slots.sum()) if i == r else int(cur_slots.sum())
                    lw = np.log(w_full) - par.gamma * G[i][:, no]
                    lw -= lw.max()
                    prm = np.exp(lw); prm /= prm.sum()
                    m = rng.choice(mmax + 1, p=prm)
                    if m < mmax:
                        dev += 1
                    new_m.append(tuple(sorted(rng.choice(others_list[i], size=m, replace=False))) if m > 0 else tuple())
        if record_dec:
            dec.append((t, p.copy(), new_slots.copy()))
        cur_slots = new_slots
        cur_m = new_m
    path = Path(Pm_hist, mates, slots, vis, dev)
    return (path, dec) if record_dec else path


# ----------------------------------------------------------------------------------------------------------------
# exact second moments given policy paths
# ----------------------------------------------------------------------------------------------------------------

def round_mats(par: Par, Pm: np.ndarray, nrel: int, nvis: int, dead_var: float | None = None):
    r"""One member, one round: A_F (I-KH), A_F k_rel, the fresh noise block (3x3) of (e^-(t+1), v_i(t)) excluding
    relayed sender noise, and P^+.  dead_var: None for live relays; otherwise each relay carries pure noise of
    that variance instead of s_j(t-1) (the eta_{t-1} term is added by the caller)."""
    a = 1.0 / par.R + nvis / (par.Rs + par.Rsh)
    b = nrel / (par.R + par.Rc)
    Pp = posterior(Pm, a, b)
    Af = A_F(par.F)
    Mx = Af @ (Pp @ np.linalg.inv(Pm))
    k_own = Pp[:, 0] / par.R
    k_rel = Pp[:, 1] / (par.R + par.Rc)
    k_slot = Pp[:, 0] / (par.Rs + par.Rsh)
    rel_var = par.Rc if dead_var is None else dead_var
    Ek = (par.R * np.outer(k_own, k_own) + nrel * rel_var * np.outer(k_rel, k_rel)
          + nvis * par.Rs * np.outer(k_slot, k_slot))
    blk = np.zeros((3, 3))
    blk[:2, :2] = Af @ Ek @ Af.T + par.qc * np.eye(2)
    blk[:2, 2] = Af @ (k_own * par.R)
    blk[2, :2] = blk[:2, 2]
    blk[2, 2] = par.R
    return Mx, Af @ k_rel, blk, Pp, Af @ k_slot


def pair_moments(par: Par, pa: Path, pb: Path, t_eval: list, dead_var: float | None = None,
                 fresh_relays: bool = False):
    r"""Exact second moments of the prior errors of two replicas that share the world path and have independent
    private noises and the given policy paths.  State Z = [x_t (eta_t, eta_{t-1}), E^a (2n), V^a (n), E^b, V^b],
    V = previous-round sensing noises (carried by next round's relays).  Returns at each t in t_eval the triple
    (1/2 Cov(e^a - e^b), Cov(e^a | eta, pi^a), Cov(e^b | eta, pi^b)); the policy average of the first is Sigma^c
    (second-moment convention) and of the others E[Cov(e | eta, pi)]."""
    n = par.n
    T = pa.Pm.shape[0]
    d1 = 3 * n
    D = 2 + 2 * d1
    Af = A_F(par.F)
    V0 = par.Q / (1 - par.F ** 2)
    Cx0 = V0 * np.array([[1.0, par.F], [par.F, 1.0]])
    L = np.zeros((D, 2))
    L[0:2] = np.eye(2)
    for r in (0, 1):
        for i in range(n):
            L[2 + r * d1 + 2 * i: 2 + r * d1 + 2 * i + 2] = -np.eye(2)
    C = L @ Cx0 @ L.T
    for r in (0, 1):
        o = 2 + r * d1 + 2 * n
        C[o:o + n, o:o + n] += par.R * np.eye(n)
    Cp = [np.zeros((d1, d1)), np.zeros((d1, d1))]
    for r in (0, 1):
        Cp[r][2 * n:, 2 * n:] = par.R * np.eye(n)
    uw = np.zeros(D)
    uw[0] = 1.0
    for r in (0, 1):
        for i in range(n):
            uw[2 + r * d1 + 2 * i] = -1.0
    out = []
    t_eval_set = set(t_eval)
    paths = (pa, pb)
    ea = [2 + 2 * i for i in range(n)]
    eb = [2 + d1 + 2 * i for i in range(n)]
    epa = [2 * i for i in range(n)]
    for t in range(T):
        if t in t_eval_set:
            Caa = C[np.ix_(ea, ea)]; Cbb = C[np.ix_(eb, eb)]; Cab = C[np.ix_(ea, eb)]
            Sig = 0.5 * (Caa + Cbb - Cab - Cab.T)
            out.append((Sig, Cp[0][np.ix_(epa, epa)].copy(), Cp[1][np.ix_(epa, epa)].copy()))
        A = np.zeros((D, D))
        A[0:2, 0:2] = Af
        Nz = np.zeros((D, D))
        Ap = [np.zeros((d1, d1)), np.zeros((d1, d1))]
        Np = [np.zeros((d1, d1)), np.zeros((d1, d1))]
        kslots = [[None] * n, [None] * n]
        for r in (0, 1):
            pth = paths[r]
            off = 2 + r * d1
            for i in range(n):
                mts = pth.mates[t][i]
                Mx, krel, blk, _, kslot = round_mats(par, pth.Pm[t, i], len(mts), int(pth.vis[t, i]),
                                                     (par.R + par.Rc) if fresh_relays else dead_var)
                kslots[r][i] = kslot
                A[off + 2 * i: off + 2 * i + 2, off + 2 * i: off + 2 * i + 2] = Mx
                Ap[r][2 * i: 2 * i + 2, 2 * i: 2 * i + 2] = Mx
                if fresh_relays:
                    pass  # NEGATIVE CONTROL: relayed sensing noise treated as fresh, eta information kept
                elif dead_var is None:
                    for j in mts:
                        A[off + 2 * i: off + 2 * i + 2, off + 2 * n + j] = krel
                        Ap[r][2 * i: 2 * i + 2, 2 * n + j] = krel
                elif len(mts) > 0:
                    A[off + 2 * i: off + 2 * i + 2, 1] += -len(mts) * krel
                ids = [off + 2 * i, off + 2 * i + 1, off + 2 * n + i]
                Nz[np.ix_(ids, ids)] += blk
                idp = [2 * i, 2 * i + 1, 2 * n + i]
                Np[r][np.ix_(idp, idp)] += blk
        C = A @ C @ A.T + Nz + par.Q * np.outer(uw, uw)
        if par.Rsh > 0:
            # instrument noise omega_k(t) of each slot: shared by every member (both replicas) that reads slot k
            for k in range(n):
                u = np.zeros(D)
                for r in (0, 1):
                    pth = paths[r]
                    if pth.slots[t, k] == 0:
                        continue
                    for i in range(n):
                        if pth.vis[t, i] == int(pth.slots[t].sum()) or i == k:
                            u[2 + r * d1 + 2 * i: 2 + r * d1 + 2 * i + 2] = kslots[r][i]
                if np.any(u):
                    C += par.Rsh * np.outer(u, u)
        for r in (0, 1):
            Cp[r] = Ap[r] @ Cp[r] @ Ap[r].T + Np[r]
    return out


def compound(S: np.ndarray):
    r"""Exchangeable (compound-symmetric) projection: alpha = mean diag - mean offdiag, beta = mean offdiag."""
    n = S.shape[0]
    d = np.trace(S) / n
    o = (S.sum() - np.trace(S)) / (n * (n - 1))
    return d - o, o


def contrast(Pi: np.ndarray, C) -> float:
    r"""r(C) = xi_in / xi_out of def:col-contrast on the whole-population precision Pi."""
    C = np.asarray(C)
    n = len(C)
    eps = Pi.sum(1)
    a = -(Pi - np.diag(np.diag(Pi)))
    aC = a[np.ix_(C, C)]
    Mc = np.diag(eps[C]) + np.diag(aC.sum(1)) - aC
    xout = Pi[np.ix_(C, C)].sum() / n
    Qm, _ = np.linalg.qr(np.column_stack([np.ones(n), np.eye(n)[:, : n - 1]]))
    Z = Qm[:, 1:]
    return float(np.linalg.eigvalsh(Z.T @ Mc @ Z).min() / xout)


def diffusive(Pi: np.ndarray, tol: float = 1e-12):
    off = Pi - np.diag(np.diag(Pi))
    return bool(off.max() <= tol and Pi.sum(1).min() >= -tol), float(off.max()), float(Pi.sum(1).min())


def region_contrasts(Pi: np.ndarray):
    N = Pi.shape[0]
    return {C: contrast(Pi, C) for r in range(2, N + 1) for C in itertools.combinations(range(N), r)}


def sigma_c(par: Par, mode: str, npairs: int, T: int, burn: int, every: int, seed: int,
            dead_var: float | None = None, fixed_slots: int | None = None, fresh_relays: bool = False):
    r"""Monte Carlo over pairs of independent policy paths (exact Gaussian algebra per pair).
    Returns Sigma^c (raw policy average and its compound projection), E[Cov(e|eta,pi)], batch statistics."""
    rng = np.random.default_rng(seed)
    t_eval = list(range(burn, T, every))
    sig_list, priv_list, dev_tot, open_tot = [], [], 0, 0.0
    for _ in range(npairs):
        if mode.startswith("real_"):
            pa = simulate_policy_path_real(par, T, rng, mode[5:])
            pb = simulate_policy_path_real(par, T, rng, mode[5:])
        else:
            pa = simulate_policy_path(par, T, rng, mode, fixed_slots=fixed_slots)
            pb = simulate_policy_path(par, T, rng, mode, fixed_slots=fixed_slots)
        dev_tot += pa.att_dev + pb.att_dev
        open_tot += pa.slots[burn:].mean() + pb.slots[burn:].mean()
        res = pair_moments(par, pa, pb, t_eval, dead_var=dead_var, fresh_relays=fresh_relays)
        sig_list.append(np.mean([r[0] for r in res], axis=0))
        priv_list.append(np.mean([0.5 * (r[1] + r[2]) for r in res], axis=0))
    sig = np.array(sig_list)
    priv = np.array(priv_list)
    S = sig.mean(0)
    Pv = priv.mean(0)
    al, be = compound(S)
    alp, bep = compound(Pv)
    ab = np.array([compound(s) for s in sig])
    se = ab.std(0, ddof=1) / np.sqrt(len(ab)) if len(ab) > 1 else np.array([np.nan, np.nan])
    return dict(S=S, Priv=Pv, alpha=al, beta=be, alpha_priv=alp, beta_priv=bep, se_alpha=se[0], se_beta=se[1],
                r=1 + par.n * be / al, r_priv=1 + par.n * bep / alp, dev_rate=dev_tot / (2 * npairs * T * par.n),
                open_rate=open_tot / (2 * npairs), ab=ab)


def r_from_ab(n: int, al: float, be: float) -> float:
    return 1 + n * be / al
