r"""Attack on the 'strict-construction' candidate (instance I**): independent re-implementation from the
specification in the candidate's report (written without importing or copying the candidate's code).

Specification used (candidate report, section 2):
  world, per niche component: eta_{t+1} = F eta_t + w_t, w_t ~ N(0, Q), stationary; members model x_t = (eta_t, eta_{t-1}).
  round-t observations of member i:
     s_i(t)   = eta_t + v_i(t),        v ~ N(0, R)       (own sensor, always read)
     o_i(t)   = eta_t + rho_i(t),      rho ~ N(0, Rs)    (private sensor, iff sigma_i(t) = 1)
     y_ij(t)  = s_j(t-1) + nu_ij(t),   nu ~ N(0, Rc)     (attended informative mate j)
     y'_ij(t) = o_j(t-1) + nu'_ij(t),  nu' ~ N(0, Rc)    (attended mate j with sigma_j(t-1) = 1)
     channels of the other niche: zero information (zero gain).
  exact Kalman filter on x_t; prediction m^-(t+1) = A_F m^+(t) + xi(t), xi ~ N(0, qc I_2), A_F = [[F, 0], [1, 0]].
  policy for round t+1: (sigma', M'), M' a subset of the nm mates and nz zero-gain channels with |M'| <= cap;
  uniform habits over all policies; G = -I(x_{t+1}; round-(t+1) observations) + psi sigma'.
  protocols: 'frozen' every member draws (sigma', M') from q_i prop. exp(-gamma G) every round;
             'real'   nrev uniformly chosen revisers per group draw sigma' from the marginal, the others keep sigma;
                      every member draws M' | sigma'.
Method differences from the candidate (deliberate): every one of the 2 x 64 policies is enumerated explicitly
(no count cells); the world-conditional second moment is assembled from a per-replica private-noise recursion and
a separate common-mode (world-innovation) recursion for the pair, instead of one joint matrix.
"""
from __future__ import annotations

import os
for _v in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS"):
    os.environ[_v] = "1"
import itertools
from dataclasses import dataclass, replace

import numpy as np


@dataclass(frozen=True)
class Cfg:
    F: float = 0.9
    Q: float = 0.05
    R: float = 1.0
    Rc: float = 0.1
    Rs: float = 2.0
    psi: float = 0.030
    gamma: float = 400.0
    qc: float = 1e-4
    n: int = 4          # informative agents in the simulated group
    nz: int = 4         # zero-gain channels per receiver
    cap: int = 3        # message capacity
    proto: str = "real"
    nrev: int = 1
    p0: float = 0.09

    def w(self, **kw) -> "Cfg":
        return replace(self, **kw)


AF = lambda F: np.array([[F, 0.0], [1.0, 0.0]])


def prior_cov(c: Cfg, p: float) -> np.ndarray:
    r"""P^-(t+1) = A_F P^+(t) A_F^T + diag(Q, 0) + qc I, which depends on P^+ only through p = P^+_00."""
    return np.array([[c.F ** 2 * p + c.Q + c.qc, c.F * p], [c.F * p, p + c.qc]])


class Policies:
    r"""Explicit enumeration of the message sets of one receiver (nm mates, nz zero-gain channels, |M| <= cap)."""

    def __init__(self, nm: int, nz: int, cap: int):
        self.sets = [cmb for k in range(cap + 1) for cmb in itertools.combinations(range(nm + nz), k)]
        self.S = np.array([[1.0 if ch in cmb else 0.0 for ch in range(nm)] for cmb in self.sets])  # (nset, nm)
        self.size = np.array([len(cmb) for cmb in self.sets])
        self.full_sets = [r for r, cmb in enumerate(self.sets) if len(cmb) == cap]


def info_gain(c: Cfg, Pm: np.ndarray, a, b):
    r"""I(x; obs) = 1/2 ln det(I + P^- diag(a, b)) for observations of eta (info a) and of the lagged state (info b)."""
    return 0.5 * np.log((1.0 + a * Pm[0, 0]) * (1.0 + b * Pm[1, 1]) - a * b * Pm[0, 1] ** 2)


def logits_member(c: Cfg, pol: Policies, Pm: np.ndarray, sig_mates: np.ndarray, gamma: float) -> np.ndarray:
    r"""-gamma G(sigma', M') for sigma' in {0, 1} and every enumerated message set; shape (2, nset)."""
    b = pol.S.sum(1) / (c.R + c.Rc) + (pol.S @ sig_mates) / (c.Rs + c.Rc)
    out = np.empty((2, len(pol.sets)))
    for s in (0, 1):
        a = 1.0 / c.R + s / c.Rs
        G = -info_gain(c, Pm, a, b) + c.psi * s
        out[s] = -gamma * G
    return out


def _softmax_draw(rng, lg: np.ndarray) -> int:
    q = np.exp(lg - lg.max())
    q /= q.sum()
    return int(rng.choice(len(q), p=q))


def lse(x, axis=None):
    m = np.max(x, axis=axis, keepdims=True)
    return np.squeeze(m + np.log(np.sum(np.exp(x - m), axis=axis, keepdims=True)), axis=axis)


@dataclass
class PathRec:
    p_prev: np.ndarray   # (T, n): P^+_00 of the previous round (fixes P^-(t))
    sig: np.ndarray      # (T, n): sigma_i(t)
    sig_prev: np.ndarray  # (T, n): sigma_i(t-1)
    att: list            # att[t][i]: tuple of attended informative mates (group indices)
    states: list         # decision states (t, p after round-t update, sigma(t)) if requested


def simulate(c: Cfg, T: int, rng: np.random.Generator, mode: str = "full", keep_states: bool = False) -> PathRec:
    r"""Policy/covariance path of one group. mode: 'full' (EFE), 'hab' (gamma = 0), 'pr' (partners redrawn uniformly
    every round among all nm + nz channels, |M| = cap; sigma' by EFE given the drawn partners)."""
    n = c.n
    nm = n - 1
    pol = Policies(nm, c.nz, c.cap)
    mates = [[j for j in range(n) if j != i] for i in range(n)]
    p = np.full(n, c.p0)
    sig = np.zeros(n, dtype=int)
    sig_prev = np.zeros(n, dtype=int)
    att = [tuple() for _ in range(n)]
    rec_p = np.zeros((T, n)); rec_s = np.zeros((T, n), int); rec_sp = np.zeros((T, n), int); rec_a = []
    states = []
    gam = 0.0 if mode == "hab" else c.gamma
    for t in range(T):
        rec_p[t] = p; rec_s[t] = sig; rec_sp[t] = sig_prev; rec_a.append(att)
        # round-t update (claimed covariance only; data-independent)
        pn = np.empty(n)
        for i in range(n):
            Pm = prior_cov(c, p[i])
            a = 1.0 / c.R + sig[i] / c.Rs
            b = sum(1.0 / (c.R + c.Rc) + sig_prev[j] / (c.Rs + c.Rc) for j in att[i])
            Pp = np.linalg.inv(np.linalg.inv(Pm) + np.diag([a, b]))
            pn[i] = Pp[0, 0]
        p = pn
        if keep_states:
            states.append((t, p.copy(), sig.copy()))
        # decisions for round t+1
        revisers = set(range(n)) if c.proto == "frozen" else set(rng.choice(n, size=c.nrev, replace=False).tolist())
        new_sig = sig.copy()
        new_att = [None] * n
        for i in range(n):
            Pm = prior_cov(c, p[i])
            sm = sig[mates[i]].astype(float)
            lg = logits_member(c, pol, Pm, sm, gam)
            if mode == "pr":
                r = pol.full_sets[int(rng.integers(len(pol.full_sets)))]
                if i in revisers:
                    l = lg[:, r]
                    new_sig[i] = int(rng.random() < 1.0 / (1.0 + np.exp(l[0] - l[1])))
            else:
                if c.proto == "frozen":
                    k = _softmax_draw(rng, lg.ravel())
                    new_sig[i], r = divmod(k, lg.shape[1])
                else:
                    if i in revisers:
                        m = lse(lg, axis=1)
                        new_sig[i] = int(rng.random() < 1.0 / (1.0 + np.exp(m[0] - m[1])))
                    r = _softmax_draw(rng, lg[new_sig[i]])
            new_att[i] = tuple(mates[i][ch] for ch in pol.sets[r] if ch < nm)
        sig_prev, sig, att = sig, new_sig, new_att
    return PathRec(rec_p, rec_s, rec_sp, rec_a, states)


def round_mats(c: Cfg, p_prev: float, own: int, att_i, sig_prev_vec):
    r"""Per member and round: Mx = A_F P^+ (P^-)^{-1}; loadings (2-vectors) of e^-(t+1) on own v(t), own rho(t), and on
    each attended mate's carried v_j(t-1), rho_j(t-1); fresh private covariance from relay-channel and computation
    noise; and p = P^+_00."""
    Af = AF(c.F)
    Pm = prior_cov(c, p_prev)
    a = 1.0 / c.R + own / c.Rs
    no = int(sum(sig_prev_vec[j] for j in att_i))
    b = len(att_i) / (c.R + c.Rc) + no / (c.Rs + c.Rc)
    Pp = np.linalg.inv(np.linalg.inv(Pm) + np.diag([a, b]))
    Mx = Af @ Pp @ np.linalg.inv(Pm)
    kown = Af @ Pp[:, 0] / c.R
    kslot = Af @ Pp[:, 0] / c.Rs * own
    krs = Af @ Pp[:, 1] / (c.R + c.Rc)
    kro = Af @ Pp[:, 1] / (c.Rs + c.Rc)
    Npriv = c.qc * np.eye(2) + c.Rc * (len(att_i) * np.outer(krs, krs) + no * np.outer(kro, kro))
    return Mx, kown, kslot, krs, kro, Npriv, Pp[0, 0]


def replica_mats(c: Cfg, path: PathRec):
    r"""For every round: (Mx blockdiag (2n x 2n), transition T of the private state, fresh covariance N)."""
    n = c.n
    T = path.sig.shape[0]
    d = 4 * n
    out = []
    for t in range(T):
        Mxb = np.zeros((2 * n, 2 * n))
        Tm = np.zeros((d, d))
        N = np.zeros((d, d))
        for i in range(n):
            Mx, kown, kslot, krs, kro, Np_, _ = round_mats(c, path.p_prev[t, i], int(path.sig[t, i]), path.att[t][i],
                                                          path.sig_prev[t])
            e = slice(2 * i, 2 * i + 2)
            Mxb[e, e] = Mx
            Tm[e, e] = Mx
            for j in path.att[t][i]:
                Tm[e, 2 * n + j] = krs                       # carried v_j(t-1)
                if path.sig_prev[t, j]:
                    Tm[e, 3 * n + j] = kro                   # carried rho_j(t-1)
            N[e, e] = c.R * np.outer(kown, kown) + c.Rs * np.outer(kslot, kslot) + Np_
            N[e, 2 * n + i] = c.R * kown; N[2 * n + i, e] = c.R * kown
            N[e, 3 * n + i] = c.Rs * kslot; N[3 * n + i, e] = c.Rs * kslot
            N[2 * n + i, 2 * n + i] = c.R
            N[3 * n + i, 3 * n + i] = c.Rs
        out.append((Mxb, Tm, N))
    return out


def pair_second_moment(c: Cfg, pa: PathRec, pb: PathRec, t_eval, fresh_relays: bool = False):
    r"""Average over t in t_eval of 1/2 E[(e^a - e^b)(e^a - e^b)^T | pi^a, pi^b] for the scalar prior errors, from
    1/2 [Cov_priv^a + Cov_priv^b] + 1/2 E[(c^a - c^b)(c^a - c^b)^T], c = response to the shared world path.
    fresh_relays (NEGATIVE CONTROL): the carried noises a receiver reads are independent copies (not the sender's)."""
    n = c.n
    ma = replica_mats(c, pa)
    mb = replica_mats(c, pb)
    T = pa.sig.shape[0]
    d = 4 * n
    Xa = np.zeros((d, d)); Xb = np.zeros((d, d))
    V0 = c.Q / (1 - c.F ** 2)
    Cx0 = V0 * np.array([[1.0, c.F], [c.F, 1.0]])
    L = np.zeros((4 * n, 2))
    for k in range(2 * n):
        L[2 * k:2 * k + 2] = -np.eye(2)
    Z = L @ Cx0 @ L.T
    g = np.zeros(4 * n); g[0::2] = -1.0
    first = [2 * i for i in range(n)]
    J = np.zeros((n, 4 * n))
    for i in range(n):
        J[i, 2 * i] = 1.0; J[i, 2 * n + 2 * i] = -1.0
    acc = np.zeros((n, n)); accp = np.zeros((n, n)); cnt = 0
    tset = set(t_eval)
    for t in range(T):
        if t in tset:
            Pa = Xa[np.ix_(first, first)]; Pb = Xb[np.ix_(first, first)]
            D = J @ Z @ J.T
            acc += 0.5 * (Pa + Pb + D); accp += 0.5 * (Pa + Pb); cnt += 1
        Mxa, Ta, Na = ma[t]; Mxb_, Tb, Nb = mb[t]
        if fresh_relays:
            # relayed carried noises replaced by fresh independent noises of the same variance
            for (Tm, N) in ((Ta, Na), (Tb, Nb)):
                C = Tm[:2 * n, 2 * n:]
                Dv = np.diag([c.R] * n + [c.Rs] * n)
                for i in range(n):          # each receiver gets its own independent copy: block-diagonal only
                    e = slice(2 * i, 2 * i + 2)
                    N[e, e] += C[e] @ Dv @ C[e].T
                Tm[:2 * n, 2 * n:] = 0.0
        Xa = Ta @ Xa @ Ta.T + Na
        Xb = Tb @ Xb @ Tb.T + Nb
        Ab = np.zeros((4 * n, 4 * n)); Ab[:2 * n, :2 * n] = Mxa; Ab[2 * n:, 2 * n:] = Mxb_
        Z = Ab @ Z @ Ab.T + c.Q * np.outer(g, g)
    return acc / cnt, accp / cnt


def compound(S: np.ndarray):
    n = S.shape[0]
    d = np.trace(S) / n
    o = (S.sum() - np.trace(S)) / (n * (n - 1))
    return d - o, o


def sigma_c(c: Cfg, npairs: int, T: int, burn: int, every: int, seed: int, mode: str = "full",
            fresh_relays: bool = False):
    rng = np.random.default_rng(seed)
    t_eval = list(range(burn, T, every))
    al, be, alp, bep, opn, Ss = [], [], [], [], [], []
    for _ in range(npairs):
        pa = simulate(c, T, rng, mode)
        pb = simulate(c, T, rng, mode)
        S, Sp = pair_second_moment(c, pa, pb, t_eval, fresh_relays)
        a_, b_ = compound(S); ap_, bp_ = compound(Sp)
        al.append(a_); be.append(b_); alp.append(ap_); bep.append(bp_); Ss.append(S)
        opn.append(0.5 * (pa.sig[burn:].mean() + pb.sig[burn:].mean()))
    al = np.array(al); be = np.array(be)
    K = len(al)
    r = 1 + c.n * be.mean() / al.mean()
    loo = np.array([1 + c.n * (be.sum() - be[k]) / (al.sum() - al[k]) for k in range(K)])
    se = float(np.sqrt((K - 1) / K * np.sum((loo - loo.mean()) ** 2)))
    Smean = np.mean(Ss, 0)
    return dict(alpha=al.mean(), beta=be.mean(), se_alpha=al.std(ddof=1) / np.sqrt(K), se_beta=be.std(ddof=1) / np.sqrt(K),
                r=r, se_r=se, alpha_priv=np.mean(alp), beta_priv=np.mean(bep), open=float(np.mean(opn)), S=Smean)
