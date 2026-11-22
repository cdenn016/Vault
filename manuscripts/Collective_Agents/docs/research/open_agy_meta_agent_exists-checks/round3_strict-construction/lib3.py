r"""Round 3, strict construction: instance I** (private optional sensors relayed raw).

Model (declared; every component of an active state is attention or speech, def:fw-system 02_framework.tex:13):
  world, per niche component: eta_{t+1} = F eta_t + w_t, w_t ~ N(0, Q), stationary.  Niches have independent
      components; every agent models only its own niche's component on x_t = (eta_t, eta_{t-1}).
  round-t sensory channels of agent i (attention decided at the end of round t-1):
    own sensor          s_i(t) = eta_t + v_i(t),       v ~ N(0, R)      (structural: always in J_i)
    private sensor      o_i(t) = eta_t + rho_i(t),     rho ~ N(0, Rs)   (world channel in J_i iff sigma_i(t) = 1)
    message of mate j   y_ij(t)  = s_j(t-1) + nu_ij(t),  nu ~ N(0, Rc)    (j in M_i(t))
                        y'_ij(t) = o_j(t-1) + nu'_ij(t), nu' ~ N(0, Rc)   (j in M_i(t) and sigma_j(t-1) = 1)
    channels of the other niche: zero information about the agent's component (zero gain).
  speech (structural, one option): every agent writes its raw readings of round t, a presence flag for the private
    reading, and its intention sigma_j(t+1) into its message channel addressed to all others; latency one round.
  exact Kalman filter on x_t, prediction m^-(t+1) = A_F m^+(t) + xi(t), xi ~ N(0, qc I_2), A_F = [[F,0],[1,0]];
    P^-(t+1) = A_F P^+ A_F^T + diag(Q, 0) + qc I_2 depends on P^+ only through p = P^+_00.
  policy of agent i for round t+1: pi_i = (sigma_i, M_i), sigma_i in {0,1}, M_i a set of at most kmsg of its
    n_inf + n_zero message channels; uniform habits over the 2 * 64 policies; one precision gamma.
  EFE (one-step horizon): G_i(sigma, M) = -I(x_{t+1}; o_{t+1} | sigma, M) + psi * sigma, with the observations of
    round t+1: own sensor, private sensor if sigma, and from each attended mate j the relay of s_j(t) and, when
    sigma_j(t) = 1, of o_j(t).  G_i depends on the others' CURRENT statuses sigma_j(t) (known through the intention
    header received in round t) and not on their round-(t+1) choices.
  protocols:
    'real'   one (nrev) uniformly chosen reviser(s) per group and round redraw(s) the private-sensor status from the
             marginal policy posterior (soft-min over attention); every member redraws attention every round given
             its new status.  No message faster than one round.
    'frozen' (P4) at a decision state held fixed: because G_i does not depend on pi_{-i}(t+1), the stationary law
             of the (P4) chain is the product of the members' policy posteriors, i.e. every member draws
             (sigma_i, M_i) from q_i(pi) prop. E_i(pi) exp(-gamma G_i(pi)) every round.
"""
from __future__ import annotations

import os
for _v in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS"):
    os.environ.setdefault(_v, "1")
import itertools
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
    n: int = 4            # members of the simulated group (a niche: 4; the mechanism medium: 8)
    n_zero: int = 4       # zero-gain message channels per member (the other niche)
    kmsg: int = 3         # message capacity
    proto: str = "real"   # 'real' or 'frozen'
    nrev: int = 1         # revisers per group and round under 'real'
    p0: float = 0.09

    def with_(self, **kw) -> "Par":
        return replace(self, **kw)

    @property
    def n_inf(self) -> int:
        return self.n - 1


def A_F(F: float) -> np.ndarray:
    return np.array([[F, 0.0], [1.0, 0.0]])


def Pminus(par: Par, p):
    r"""P^-(t+1) entries (P00, P01, P11) from the posterior variance p of eta_t (vectorized)."""
    p = np.asarray(p, float)
    return par.F ** 2 * p + par.Q + par.qc, par.F * p, p + par.qc


def info(P00, P01, P11, a, b):
    r"""I(x; o) = 1/2 ln det(I + P^- diag(a, b)) = 1/2 ln[(1 + a P00)(1 + b P11) - a b P01^2]."""
    return 0.5 * np.log((1 + a * P00) * (1 + b * P11) - a * b * P01 ** 2)


def efe_grid(par: Par, P00, P01, P11):
    r"""G[..., s, m1, m0] = -I(x_{t+1}; round-(t+1) observations) + psi s, for own private-sensor status s,
    m1 attended mates whose sensor was open in round t and m0 attended mates whose sensor was closed (m1, m0 = 0..kmsg).
    """
    K = par.kmsg
    s = np.arange(2, dtype=float)[:, None, None]
    m1 = np.arange(K + 1, dtype=float)[None, :, None]
    m0 = np.arange(K + 1, dtype=float)[None, None, :]
    a = 1.0 / par.R + s / par.Rs
    b = (m0 + m1) / (par.R + par.Rc) + m1 / (par.Rs + par.Rc)
    P00 = np.asarray(P00)[..., None, None, None]
    P01 = np.asarray(P01)[..., None, None, None]
    P11 = np.asarray(P11)[..., None, None, None]
    return -info(P00, P01, P11, a, b) + par.psi * s


def log_att_weights(par: Par, k1) -> np.ndarray:
    r"""ln W(k1; m1, m0): log number of message sets (|M| <= kmsg among n_inf mates, k1 of them open, and n_zero
    zero-gain channels) with exactly m1 open and m0 closed mates; -inf where infeasible.  Vectorized in k1."""
    K = par.kmsg
    k1 = np.asarray(k1, int)
    out = np.full(k1.shape + (K + 1, K + 1), -np.inf)
    tbl = {}
    for kk in range(par.n_inf + 1):
        W = np.full((K + 1, K + 1), -np.inf)
        k0 = par.n_inf - kk
        for a in range(K + 1):
            for b in range(K + 1 - a):
                if a <= kk and b <= k0:
                    c = comb(kk, a) * comb(k0, b) * sum(comb(par.n_zero, z) for z in range(0, K - a - b + 1))
                    if c > 0:
                        W[a, b] = np.log(c)
        tbl[kk] = W
    for kk, W in tbl.items():
        out[k1 == kk] = W
    return out


def lse(x: np.ndarray, axis) -> np.ndarray:
    mx = np.max(x, axis=axis, keepdims=True)
    mx = np.where(np.isfinite(mx), mx, 0.0)
    return (mx + np.log(np.sum(np.exp(x - mx), axis=axis, keepdims=True))).squeeze(axis)


# ------------------------------------------------------------------------------------------------------------
# scalar policy-path simulation for one group (used by the exact pair algebra)
# ------------------------------------------------------------------------------------------------------------

@dataclass
class Path:
    p_prev: np.ndarray     # (T, n): posterior variance of eta_{t-1} after round t-1 (so P^-(t) = Pminus(p_prev[t]))
    sig: np.ndarray        # (T, n): sigma_i(t), own private sensor read at round t
    sig_prev: np.ndarray   # (T, n): sigma_i(t-1), i.e. whose private reading the relays of round t carry
    att: list              # att[t][i] = tuple of informative mates attended at round t
    own_ok: np.ndarray     # (T, n): 1 if the member's own private reading is fused (always 1 except diagnostics)
    dev: int = 0           # member-rounds with fewer than kmsg informative mates attended
    log: dict = field(default_factory=dict)


def _posterior_p(par: Par, p_prev: float, a: float, b: float) -> float:
    P00, P01, P11 = Pminus(par, p_prev)
    det = P00 * P11 - P01 ** 2
    i00, i01, i11 = P11 / det, -P01 / det, P00 / det
    L00, L11 = i00 + a, i11 + b
    return float(L11 / (L00 * L11 - i01 ** 2))


def simulate_policy(par: Par, T: int, rng: np.random.Generator, mode: str = "full", fixed_sig=None,
                    record_dec: bool = False) -> Path:
    r"""Policy/covariance process of one group of par.n members.
    mode: 'full'  EFE policies by par.proto;
          'hab'   gamma = 0: statuses and attention from the uniform habits (same protocol clock);
          'pr'    partners redrawn uniformly every round (kmsg of the n_inf + n_zero channels); status decisions by
                  the EFE given the drawn partners;
          'lp'    inter-agent channels deliver pure noise; receivers keep assigned precisions; headers lost, so every
                  member treats its mates' private sensors as closed (EFE and fusion); attention by EFE;
          'fr'    others held at their initial state: relays carry the initial content 0, headers say closed;
          'fixed' all mates attended, statuses fixed_sig every round.
    record_dec: store the decision records (p after update, sigma(t), sigma(t+1), attention(t+1)) in path.log."""
    n = par.n
    K = par.kmsg
    others = [[j for j in range(n) if j != i] for i in range(n)]
    p = np.full(n, par.p0)
    sig = np.zeros(n, dtype=int) if fixed_sig is None else np.array(fixed_sig, dtype=int)
    sig_prev = np.zeros(n, dtype=int)
    att = [tuple() for _ in range(n)]
    rec_p = np.zeros((T, n)); rec_s = np.zeros((T, n), dtype=int); rec_sp = np.zeros((T, n), dtype=int)
    rec_att = []
    dev = 0
    decs = []
    hdr_closed = mode in ("lp", "fr")
    for t in range(T):
        rec_p[t] = p; rec_s[t] = sig; rec_sp[t] = sig_prev; rec_att.append(att)
        # update of round t (claimed covariance)
        pn = np.empty(n)
        for i in range(n):
            a = 1.0 / par.R + sig[i] / par.Rs
            if hdr_closed:
                b = len(att[i]) / (par.R + par.Rc)
            else:
                b = sum(1.0 / (par.R + par.Rc) + sig_prev[j] / (par.Rs + par.Rc) for j in att[i])
            pn[i] = _posterior_p(par, p[i], a, b)
        p = pn
        # decisions for round t+1
        if mode == "fixed":
            new_sig = sig.copy()
            new_att = [tuple(others[i]) for i in range(n)]
        else:
            P00, P01, P11 = Pminus(par, p)
            G = efe_grid(par, P00, P01, P11)                         # (n, 2, K+1, K+1)
            k1_known = np.array([0 if hdr_closed else int(sig.sum() - sig[i]) for i in range(n)])
            lw = log_att_weights(par, k1_known)                      # (n, K+1, K+1)
            gam = 0.0 if mode == "hab" else par.gamma
            new_sig = sig.copy()
            if par.proto == "real":
                movers = rng.choice(n, size=par.nrev, replace=False)
            else:
                movers = np.arange(n)
            new_att = [None] * n
            if mode in ("pr", "pr0"):
                tot = par.n_inf + par.n_zero
                for i in range(n):
                    pick = rng.choice(tot, size=K, replace=False)
                    inf = sorted(others[i][k] for k in pick if k < par.n_inf)
                    new_att[i] = tuple(inf)
                    if len(inf) < min(K, par.n_inf):
                        dev += 1
                for i in movers:
                    # 'pr0' (variant): the decider does not know its partners' current statuses and evaluates its EFE
                    # as if they were closed; fusion still uses what actually arrives (presence flag)
                    m1 = 0 if mode == "pr0" else sum(sig[j] for j in new_att[i])
                    m0 = len(new_att[i]) - m1
                    d = gam * (G[i, 0, m1, m0] - G[i, 1, m1, m0])
                    new_sig[i] = int(rng.random() < 0.5 * (1 + np.tanh(0.5 * d)))
            else:
                for i in movers:
                    l1 = lse((lw[i] - gam * G[i, 1]).ravel(), 0)
                    l0 = lse((lw[i] - gam * G[i, 0]).ravel(), 0)
                    new_sig[i] = int(rng.random() < 0.5 * (1 + np.tanh(0.5 * (l1 - l0))))
                for i in range(n):
                    lq = (lw[i] - gam * G[i, new_sig[i]]).ravel()
                    q = np.exp(lq - lq.max()); q /= q.sum()
                    cell = rng.choice(q.size, p=q)
                    m1, m0 = divmod(cell, K + 1)
                    if hdr_closed:
                        pool = others[i]
                        chosen = list(rng.choice(pool, size=m1 + m0, replace=False)) if m1 + m0 > 0 else []
                    else:
                        op = [j for j in others[i] if sig[j] == 1]
                        cl = [j for j in others[i] if sig[j] == 0]
                        chosen = (list(rng.choice(op, size=m1, replace=False)) if m1 > 0 else []) + \
                                 (list(rng.choice(cl, size=m0, replace=False)) if m0 > 0 else [])
                    new_att[i] = tuple(sorted(int(c) for c in chosen))
                    if len(chosen) < min(K, par.n_inf):
                        dev += 1
        if record_dec:
            decs.append((t, p.copy(), sig.copy(), new_sig.copy(), [tuple(a) for a in new_att]))
        sig_prev = sig
        sig = new_sig
        att = new_att
    path = Path(rec_p, rec_s, rec_sp, rec_att, np.ones((T, n), dtype=int), dev)
    if record_dec:
        path.log["dec"] = decs
    return path


# ------------------------------------------------------------------------------------------------------------
# exact second moments given a pair of policy paths (shared world path, independent private inputs)
# ------------------------------------------------------------------------------------------------------------

def member_round(par: Par, p_prev: float, own_sig: int, att_i, sig_prev, mode: str = "full"):
    r"""One member, one round.  Returns Mx = A_F P^+ (P^-)^{-1}, the loadings of e^-(t+1) on the carried noises of
    each attended mate (dict j -> (load_v, load_rho)), the x-loading (2x2, nonzero only under 'lp'/'fr'), the fresh
    covariance block of (e^-(t+1), v_i(t), rho_i(t)) (4x4)."""
    F = par.F
    Af = A_F(F)
    P00, P01, P11 = Pminus(par, p_prev)
    Pm = np.array([[P00, P01], [P01, P11]])
    hdr_closed = mode in ("lp", "fr")
    a = 1.0 / par.R + own_sig / par.Rs
    n_s = len(att_i)
    n_o = 0 if hdr_closed else int(sum(sig_prev[j] for j in att_i))
    b = n_s / (par.R + par.Rc) + n_o / (par.Rs + par.Rc)
    Pp = np.linalg.inv(np.linalg.inv(Pm) + np.diag([a, b]))
    Mx = Af @ Pp @ np.linalg.inv(Pm)
    k_own = Pp[:, 0] / par.R
    k_slot = Pp[:, 0] / par.Rs
    k_rs = Pp[:, 1] / (par.R + par.Rc)
    k_ro = Pp[:, 1] / (par.Rs + par.Rc)
    loads = {}
    xload = np.zeros((2, 2))
    if mode in ("full", "hab", "pr", "pr0", "fixed"):
        for j in att_i:
            loads[j] = (Af @ k_rs, (Af @ k_ro) if sig_prev[j] else np.zeros(2))
        relay_var = par.Rc
        Ek = (par.R * np.outer(k_own, k_own) + own_sig * par.Rs * np.outer(k_slot, k_slot)
              + n_s * relay_var * np.outer(k_rs, k_rs) + n_o * relay_var * np.outer(k_ro, k_ro))
    elif mode == "lp":
        # relays: pure noise of the believed variance R + Rc; the update subtracts K_rs * eta_{t-1}
        xload[:, 1] = -n_s * (Af @ k_rs)
        Ek = (par.R * np.outer(k_own, k_own) + own_sig * par.Rs * np.outer(k_slot, k_slot)
              + n_s * (par.R + par.Rc) * np.outer(k_rs, k_rs))
    elif mode == "fr":
        # relays: deterministic initial content 0 plus the receiver-specific channel noise
        xload[:, 1] = -n_s * (Af @ k_rs)
        Ek = (par.R * np.outer(k_own, k_own) + own_sig * par.Rs * np.outer(k_slot, k_slot)
              + n_s * par.Rc * np.outer(k_rs, k_rs))
    else:
        raise ValueError(mode)
    blk = np.zeros((4, 4))
    blk[:2, :2] = Af @ Ek @ Af.T + par.qc * np.eye(2)
    blk[:2, 2] = Af @ (k_own * par.R)
    blk[:2, 3] = own_sig * (Af @ (k_slot * par.Rs))
    blk[2, :2] = blk[:2, 2]
    blk[3, :2] = blk[:2, 3]
    blk[2, 2] = par.R
    blk[3, 3] = par.Rs
    return Mx, loads, xload, blk, Pp


def pair_moments(par: Par, pa: Path, pb: Path, t_eval, mode: str = "full", fresh_relays: bool = False):
    r"""Exact second moments of the scalar prior errors e_i(t) = m^-_{i,0}(t) - eta_t of two replicas sharing the
    world path, with independent private inputs and the given policy paths.
    State Z = [x_t (2), E^a (2n), V^a (2n), E^b (2n), V^b (2n)], V_j = (v_j(t-1), rho_j(t-1)).
    Returns a list over t in t_eval of (Sigma_pair, Cov_a(e | eta, pi^a), Cov_b(e | eta, pi^b)), where
    Sigma_pair = 1/2 Cov(e^a - e^b) (its policy average is Sigma^c, second-moment convention).
    fresh_relays: NEGATIVE CONTROL, the relayed private noises are treated as fresh draws (not shared with the
    sender), everything else unchanged."""
    n = par.n
    T = pa.sig.shape[0]
    d1 = 4 * n
    D = 2 + 2 * d1
    Af = A_F(par.F)
    V0 = par.Q / (1 - par.F ** 2)
    Cx0 = V0 * np.array([[1.0, par.F], [par.F, 1.0]])
    Lx = np.zeros((D, 2)); Lx[0:2] = np.eye(2)
    for r in (0, 1):
        for i in range(n):
            Lx[2 + r * d1 + 2 * i: 2 + r * d1 + 2 * i + 2] = -np.eye(2)
    C = Lx @ Cx0 @ Lx.T
    Cp = [np.zeros((d1, d1)), np.zeros((d1, d1))]
    for r in (0, 1):
        o = 2 + r * d1 + 2 * n
        for i in range(n):
            C[o + 2 * i, o + 2 * i] += par.R; C[o + 2 * i + 1, o + 2 * i + 1] += par.Rs
            Cp[r][2 * n + 2 * i, 2 * n + 2 * i] = par.R; Cp[r][2 * n + 2 * i + 1, 2 * n + 2 * i + 1] = par.Rs
    uw = np.zeros(D); uw[0] = 1.0
    for r in (0, 1):
        for i in range(n):
            uw[2 + r * d1 + 2 * i] = -1.0
    ea = [2 + 2 * i for i in range(n)]
    eb = [2 + d1 + 2 * i for i in range(n)]
    ep = [2 * i for i in range(n)]
    tset = set(t_eval)
    out = []
    paths = (pa, pb)
    for t in range(T):
        if t in tset:
            Caa = C[np.ix_(ea, ea)]; Cbb = C[np.ix_(eb, eb)]; Cab = C[np.ix_(ea, eb)]
            out.append((0.5 * (Caa + Cbb - Cab - Cab.T), Cp[0][np.ix_(ep, ep)].copy(), Cp[1][np.ix_(ep, ep)].copy()))
        A = np.zeros((D, D)); A[0:2, 0:2] = Af
        Nz = np.zeros((D, D))
        Ap = [np.zeros((d1, d1)), np.zeros((d1, d1))]
        Np = [np.zeros((d1, d1)), np.zeros((d1, d1))]
        for r in (0, 1):
            pth = paths[r]
            off = 2 + r * d1
            for i in range(n):
                Mx, loads, xload, blk, _ = member_round(par, pth.p_prev[t, i], int(pth.sig[t, i]), pth.att[t][i],
                                                       pth.sig_prev[t], mode)
                ei = slice(off + 2 * i, off + 2 * i + 2)
                A[ei, ei] = Mx
                Ap[r][2 * i:2 * i + 2, 2 * i:2 * i + 2] = Mx
                A[ei, 0:2] += xload
                if fresh_relays:
                    # NEGATIVE CONTROL: relayed private noises replaced by independent fresh noises of the same
                    # variance (the eta content of the relays is kept, so the filter's information is unchanged)
                    extra = np.zeros((2, 2))
                    for j, (lv, lr) in loads.items():
                        extra += par.R * np.outer(lv, lv) + par.Rs * np.outer(lr, lr)
                    blk = blk.copy(); blk[:2, :2] += extra
                else:
                    for j, (lv, lr) in loads.items():
                        A[ei, off + 2 * n + 2 * j] = lv
                        A[ei, off + 2 * n + 2 * j + 1] = lr
                        Ap[r][2 * i:2 * i + 2, 2 * n + 2 * j] = lv
                        Ap[r][2 * i:2 * i + 2, 2 * n + 2 * j + 1] = lr
                ids = [off + 2 * i, off + 2 * i + 1, off + 2 * n + 2 * i, off + 2 * n + 2 * i + 1]
                Nz[np.ix_(ids, ids)] += blk
                idp = [2 * i, 2 * i + 1, 2 * n + 2 * i, 2 * n + 2 * i + 1]
                Np[r][np.ix_(idp, idp)] += blk
        C = A @ C @ A.T + Nz + par.Q * np.outer(uw, uw)
        for r in (0, 1):
            Cp[r] = Ap[r] @ Cp[r] @ Ap[r].T + Np[r]
    return out


def compound(S: np.ndarray):
    r"""Exchangeable projection alpha I + beta 11^T: beta = mean off-diagonal, alpha = mean diagonal - beta."""
    n = S.shape[0]
    d = np.trace(S) / n
    o = (S.sum() - np.trace(S)) / (n * (n - 1))
    return d - o, o


def sigma_c(par: Par, npairs: int, T: int, burn: int, every: int, seed: int, mode: str = "full",
            fixed_sig=None, fresh_relays: bool = False):
    r"""Policy-average of the exact pair moments (Monte Carlo over independent pairs of policy paths only)."""
    rng = np.random.default_rng(seed)
    t_eval = list(range(burn, T, every))
    S_l, P_l, opn, dev = [], [], 0.0, 0
    for _ in range(npairs):
        pa = simulate_policy(par, T, rng, mode, fixed_sig)
        pb = simulate_policy(par, T, rng, mode, fixed_sig)
        opn += pa.sig[burn:].mean() + pb.sig[burn:].mean()
        dev += pa.dev + pb.dev
        res = pair_moments(par, pa, pb, t_eval, mode, fresh_relays)
        S_l.append(np.mean([r[0] for r in res], axis=0))
        P_l.append(np.mean([0.5 * (r[1] + r[2]) for r in res], axis=0))
    S_l = np.array(S_l); P_l = np.array(P_l)
    S = S_l.mean(0); Pv = P_l.mean(0)
    al, be = compound(S); alp, bep = compound(Pv)
    ab = np.array([compound(s) for s in S_l])
    K = len(ab)
    loo = np.array([1 + par.n * (ab[:, 1].sum() - ab[k, 1]) / (ab[:, 0].sum() - ab[k, 0]) for k in range(K)])
    r_all = 1 + par.n * be / al
    se_r = float(np.sqrt((K - 1) / K * np.sum((loo - loo.mean()) ** 2))) if K > 1 else float("nan")
    return dict(S=S, Priv=Pv, alpha=al, beta=be, alpha_priv=alp, beta_priv=bep, r=r_all, se_r=se_r,
                r_priv=1 + par.n * bep / alp, ab=ab, open_rate=opn / (2 * npairs),
                dev_rate=dev / (2 * npairs * T * par.n),
                se_alpha=float(ab[:, 0].std(ddof=1) / np.sqrt(K)) if K > 1 else float("nan"),
                se_beta=float(ab[:, 1].std(ddof=1) / np.sqrt(K)) if K > 1 else float("nan"))


# ------------------------------------------------------------------------------------------------------------
# contrast machinery (def:col-contrast 04_collectives.tex:182-188; diffusive class :147-151)
# ------------------------------------------------------------------------------------------------------------

def is_diffusive(Pi: np.ndarray, tol: float = 1e-12):
    off = Pi - np.diag(np.diag(Pi))
    return bool(off.max() <= tol and Pi.sum(1).min() >= -tol), float(off.max()), float(Pi.sum(1).min())


def contrast(Pi: np.ndarray, C) -> float:
    C = list(C)
    n = len(C)
    eps = Pi.sum(1)
    a = -(Pi - np.diag(np.diag(Pi)))
    aC = a[np.ix_(C, C)]
    Mc = np.diag(eps[C]) + np.diag(aC.sum(1)) - aC
    phi = np.ones(n) / np.sqrt(n)
    xout = float(phi @ Pi[np.ix_(C, C)] @ phi)
    Z = np.linalg.svd(np.eye(n) - np.outer(phi, phi))[0][:, : n - 1]
    xin = float(np.linalg.eigvalsh(Z.T @ Mc @ Z).min())
    return xin / xout


def region_contrasts(Pi: np.ndarray):
    N = Pi.shape[0]
    return {C: contrast(Pi, C) for r in range(2, N + 1) for C in itertools.combinations(range(N), r)}


def population_precision(al: float, be: float, n: int = 4):
    SA = al * np.eye(n) + be * np.ones((n, n))
    S = np.zeros((2 * n, 2 * n)); S[:n, :n] = SA; S[n:, n:] = SA
    return np.linalg.inv(S), S


def mean_coupling_baseline(Pi: np.ndarray) -> float:
    r"""Clause (c) with the mean coupling: exchangeable medium, coupling abar between every pair, uniform leak ebar;
    with uniform leak the sup over regions is the whole medium, 1 + N abar / ebar (checked by enumeration)."""
    N = Pi.shape[0]
    abar = sum(-Pi[i, j] for i in range(N) for j in range(i + 1, N)) / (N * (N - 1) / 2)
    ebar = Pi.sum(1).mean()
    Pmc = np.diag(np.full(N, ebar)) + abar * (N * np.eye(N) - np.ones((N, N)))
    rc = region_contrasts(Pmc)
    return max(rc.values()), 1 + N * abar / ebar
