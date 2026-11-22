r"""Library for the blind recomputation of instance P1.

Model (spec.md): scalar AR(1) world eta_{t+1}=F eta_t+w_t, agents filter x_t=(eta_t,eta_{t-1}) with an
exact Kalman filter whose prior covariance includes q_c I_2 (computation noise added to predicted means).
Own sensor s_a(t)=eta_t+v_a(t), var R_a; broadcast u_a(t)=s_a(t); message read in round t from j:
y_aj(t)=u_j(t-1)+nu_aj(t), var R_j+R_c, observation of eta_{t-1} (second component of x_t).

Error coordinates: eps_a(t)=m^-_a(t)-x_t (prior), e_a(t)=eps_a(t)[0].
  eps^+ = T eps^- + K_own v_a(t) + sum_j K_j (content_j - eta_{t-1} + nu_aj),  T = I-KH = P^+ (P^-)^{-1},
  eps^-(t+1) = A eps^+ + xi_a(t) - (w_t,0).
The error is split into a world-driven part g (function of the world path and the attention path)
and a private part h (function of private noises and the attention path). Given the attention paths,
everything is exactly Gaussian; noises are integrated out exactly (Rao-Blackwellization) and only the
attention paths are sampled. Second-moment convention:
  Sigma^c = E[Cov(e|eta)] = E_att[Cov(h|att)] + diag( E_eta Var_att(g|eta) ),
the last term from pairs of independent attention paths sharing the world (off-diagonal entries of it
vanish because members' attention paths are independent and S's attention is fixed).
"""
from __future__ import annotations

import os

for _k in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS"):
    os.environ[_k] = "4"

from itertools import combinations
from typing import Any

import numpy as np

BASE: dict[str, float] = dict(F=0.9, Q=0.05, R=1.0, RS=0.01, Rc=0.002, qc=1e-4, gamma=40.0)


# ----------------------------------------------------------------------------- 2x2 helpers
def inv2(M: np.ndarray) -> np.ndarray:
    """Batched inverse of 2x2 matrices (..., 2, 2)."""
    a, b, c, d = M[..., 0, 0], M[..., 0, 1], M[..., 1, 0], M[..., 1, 1]
    det = a * d - b * c
    out = np.empty_like(M)
    out[..., 0, 0] = d / det
    out[..., 0, 1] = -b / det
    out[..., 1, 0] = -c / det
    out[..., 1, 1] = a / det
    return out


def world_cov(p: dict[str, float]) -> np.ndarray:
    """Stationary covariance of (eta_t, eta_{t-1})."""
    s0 = p["Q"] / (1 - p["F"] ** 2)
    return s0 * np.array([[1.0, p["F"]], [p["F"], 1.0]])


# ----------------------------------------------------------------------------- model
class Model:
    r"""Population and attention mechanism.

    kind='pop':    agent 0 = source S (R_S, reads nothing), agents 1..4 = members (R), each member
                   chooses a subset of size <= 2 of {S, three co-members} (11 subsets).
    kind='medium': five agents of the members' type (R), each chooses a subset of size <= 2 of the
                   other four (11 subsets).
    att: 'efe' (prob ~ exp(gamma I)), 'hab' (uniform on the 11 subsets), 'pr' (uniform on the 6
         pairs), 'efeS' (efe restricted to {} and {S}), 'fixedS' (always {S}).
    content: 'full' (message = raw reading), 'lp' (pure noise N(0,R_j+R_c), private to the receiver),
             'fr' (frozen broadcast u_j(0)=s_j(0)).
    condS: condition also on the source's sensing-noise path (item 4).
    """

    def __init__(self, p: dict[str, float], kind: str = "pop", att: str = "efe",
                 content: str = "full", condS: bool = False, cond_v0: bool = False) -> None:
        self.p = dict(p)
        F, Q, qc = p["F"], p["Q"], p["qc"]
        self.A = np.array([[F, 0.0], [1.0, 0.0]])
        self.Qx = np.array([[Q + qc, 0.0], [0.0, qc]])
        self.kind, self.att, self.content, self.condS = kind, att, content, condS
        self.cond_v0 = cond_v0  # fr only: frozen broadcast noises v_j(0) put in the conditioning set
        assert not (cond_v0 and (condS or content != "fr"))
        N = 5
        self.N = N
        if kind == "pop":
            self.Rs = np.array([p["RS"], p["R"], p["R"], p["R"], p["R"]])
            self.receivers = [1, 2, 3, 4]
            cand = {a: [0] + [b for b in range(1, 5) if b != a] for a in range(1, 5)}
        elif kind == "medium":
            self.Rs = np.full(N, p["R"])
            self.receivers = list(range(N))
            cand = {a: [b for b in range(N) if b != a] for a in range(N)}
        else:
            raise ValueError(kind)
        self.wmsg = 1.0 / (self.Rs + p["Rc"])
        Nr = len(self.receivers)
        self.Ind = np.zeros((Nr, 11, N))
        self.subsets: list[list[tuple[int, ...]]] = []
        for r, a in enumerate(self.receivers):
            c = cand[a]
            subs = [()] + [(j,) for j in c] + list(combinations(c, 2))
            assert len(subs) == 11
            self.subsets.append(subs)
            for k, s in enumerate(subs):
                for j in s:
                    self.Ind[r, k, j] = 1.0
        self.sig = self.Ind @ self.wmsg  # (Nr, 11) message precision of each subset
        mask = np.ones(11, bool)
        if att == "pr":
            mask = np.array([len(s) == 2 for s in self.subsets[0]])
        elif att in ("efeS", "fixedS"):
            assert kind == "pop"
            mask = np.array([s in [(), (0,)] for s in self.subsets[0]])
            if att == "fixedS":
                mask = np.array([s == (0,) for s in self.subsets[0]])
        self.mask = mask
        self.hasS = np.array([[0 in s for s in subs] for subs in self.subsets])  # (Nr,11)

    # privacy masks
    def priv_mask(self) -> np.ndarray:
        m = np.ones(self.N)
        if self.condS:
            m[0] = 0.0
        return m


# ----------------------------------------------------------------------------- simulation engine
def simulate(model: Model, B: int, T_burn: int, T_avg: int, seed: int, G: int = 20,
             do_union: bool = False, do_memory: bool = False, T_mem: int = 60,
             P0: np.ndarray | None = None, store_types: bool = False) -> dict[str, Any]:
    """Rao-Blackwellized second moments over B sampled attention paths (B even)."""
    p = model.p
    rng = np.random.default_rng(seed)
    N, A, Rs, wmsg = model.N, model.A, model.Rs, model.wmsg
    F, Q, Rc, qc, gam = p["F"], p["Q"], p["Rc"], p["qc"], p["gamma"]
    B2 = B // 2
    assert B == 2 * B2 and B2 % G == 0
    grp_pair = np.arange(B2) % G
    grp_path = np.concatenate([grp_pair, grp_pair])
    content, condS = model.content, model.condS
    pm = model.priv_mask()
    recv = np.array(model.receivers)
    Nr = len(recv)

    if P0 is None:
        P0 = world_cov(p)
    Pm = np.broadcast_to(P0, (B, N, 2, 2)).copy()
    read = np.zeros((B, N, N))

    # ---- private part layout
    fr = content == "fr"
    dh = 3 * N + (N if fr else 0)
    iv, i0 = 2 * N, 3 * N
    Ch = np.zeros((B, dh, dh))
    eidx = np.arange(0, 2 * N, 2)
    var_lump = np.full(N, Rc) if content in ("full", "fr") else Rs + Rc

    # ---- shared part layout (pairs)
    cv0 = model.cond_v0
    dsh = 3 + 4 * N + (2 if condS else 0) + (N if cv0 else 0)
    ivs, ivs0 = 3 + 4 * N, 3 + 4 * N + 1
    iv0s = 3 + 4 * N

    def gi(s: int, a: int) -> int:
        return 3 + (s * N + a) * 2

    L0 = np.zeros((dsh, 2))
    L0[0, 0] = 1.0
    L0[1, 1] = 1.0
    L0[2, 0] = 1.0
    for s in range(2):
        for a in range(N):
            L0[gi(s, a), 0] = -1.0
            L0[gi(s, a) + 1, 1] = -1.0
    Csh = np.broadcast_to(L0 @ world_cov(p) @ L0.T, (B2, dsh, dsh)).copy()

    # ---- accumulators
    acc_h = np.zeros((G, N, N))
    acc_V = np.zeros((G, N))
    n_path_t = np.zeros(G)
    n_pair_t = np.zeros(G)
    acc_prob = np.zeros((Nr, 11))
    acc_cnt = np.zeros((Nr, 11))
    max_nonS = 0.0
    n_att = 0
    types = [] if store_types else None

    # ---- union / inference
    if do_union:
        assert model.kind == "pop" and content == "full" and not condS
        du = 15  # members eps (8), union eps (2), vprev (5)
        Cu = np.zeros((B, du, du))
        PmU = np.broadcast_to(P0, (B, 2, 2)).copy()
        cvec = np.zeros(du)
        cvec[[0, 2, 4, 6]] = 0.25
        cvec[8] = -1.0
        accU = {k: np.zeros(G) for k in ["d2/PU", "1/PU", "lnPU", "PU+d2", "v/PU", "ln(v/PU)",
                                          "PU/v", "d2/v", "d2", "PU", "v", "cnt"]}
        accU_t = []
        nU_bad = 0
    # ---- memory
    if do_memory:
        assert model.kind == "pop"
        Pv = np.zeros(8)
        Pv[[0, 2, 4, 6]] = 0.25
        PP = Pv @ Pv
        Sx = np.zeros((B, 8, 8))
        Sf2 = np.zeros((B, 8, 8))
        Sf1 = None
        I2 = np.zeros((B, T_burn + T_avg))
        I1 = np.zeros((B, T_avg))
        Dcl = np.zeros((B, T_burn + T_avg))
        eye8 = np.eye(8)

    T_tot = T_burn + T_avg
    for t in range(T_tot):
        rec = t >= T_burn
        # ------------------------------------------------ record prior quantities at round t
        if rec:
            Che = Ch[:, eidx][:, :, eidx]
            np.add.at(acc_h, grp_path, Che)
            n_path_t += np.bincount(grp_path, minlength=G)
            V = np.zeros((B2, N))
            for a in range(N):
                i0_, i1_ = gi(0, a), gi(1, a)
                V[:, a] = 0.5 * (Csh[:, i0_, i0_] + Csh[:, i1_, i1_] - 2 * Csh[:, i0_, i1_])
            np.add.at(acc_V, grp_pair, V)
            n_pair_t += np.bincount(grp_pair, minlength=G)
            if do_union:
                d2 = np.einsum("i,bij,j->b", cvec, Cu, cvec)
                v = Pm[:, 1:5, 0, 0].mean(1)
                PU = PmU[:, 0, 0]
                vals = {"d2/PU": d2 / PU, "1/PU": 1 / PU, "lnPU": np.log(PU), "PU+d2": PU + d2,
                        "v/PU": v / PU, "ln(v/PU)": np.log(v / PU), "PU/v": PU / v, "d2/v": d2 / v,
                        "d2": d2, "PU": PU, "v": v, "cnt": np.ones(B)}
                for k_, x_ in vals.items():
                    accU[k_] += np.bincount(grp_path, weights=x_, minlength=G)
        # ------------------------------------------------ Kalman update with the sets read now
        sigr = read @ wmsg  # (B,N)
        invPm = inv2(Pm)
        Lam = invPm.copy()
        Lam[..., 0, 0] += 1.0 / Rs
        Lam[..., 1, 1] += sigr
        Pp = inv2(Lam)
        Tm = Pp @ invPm
        AT = A @ Tm  # (B,N,2,2)
        AKown = (A @ (Pp[..., :, 0] / Rs[None, :, None])[..., None])[..., 0]  # (B,N,2)
        AK2 = (A @ Pp[..., :, 1][..., None])[..., 0]  # (B,N,2) per unit message precision
        W = read * wmsg[None, None, :]  # (B,N,N) message gains (receiver, sender)

        # ------------------------------------------------ private part
        M = np.zeros((B, dh, dh))
        Gv = np.zeros((B, dh, N))
        Nx = np.zeros((B, dh, dh))
        for a in range(N):
            sl = slice(2 * a, 2 * a + 2)
            M[:, sl, sl] = AT[:, a]
            Gv[:, sl, a] = AKown[:, a]
            Gv[:, iv + a, a] = 1.0
            if content == "full":
                M[:, sl, iv:iv + N] = AK2[:, a, :, None] * (W[:, a, :] * pm)[:, None, :]
            elif fr and not cv0:
                M[:, sl, i0:i0 + N] = AK2[:, a, :, None] * W[:, a, :][:, None, :]
            s2 = (W[:, a, :] ** 2 * var_lump[None, :]).sum(1)
            Nx[:, sl, sl] = s2[:, None, None] * (AK2[:, a, :, None] * AK2[:, a, None, :]) + qc * np.eye(2)
            if fr:
                if t == 0:
                    Gv[:, i0 + a, a] = 1.0
                else:
                    M[:, i0 + a, i0 + a] = 1.0
        Rv = Rs * pm
        if cv0 and t == 0:
            Rv = np.zeros(N)  # own reading at round 0 = frozen broadcast noise, conditioned
        Ch = M @ Ch @ M.transpose(0, 2, 1) + (Gv * Rv[None, None, :]) @ Gv.transpose(0, 2, 1) + Nx

        # ------------------------------------------------ shared part (pairs share the world)
        Msh = np.zeros((B2, dsh, dsh))
        Gsh = np.zeros((B2, dsh, 2 + (N if cv0 else 0)))
        Msh[:, 0, 0] = F
        Msh[:, 1, 0] = 1.0
        Msh[:, 2, 2] = 1.0
        Gsh[:, 0, 0] = 1.0
        for s in range(2):
            ps = slice(s * B2, (s + 1) * B2)
            for a in range(N):
                g = gi(s, a)
                sl = slice(g, g + 2)
                Msh[:, sl, sl] = AT[ps, a]
                Gsh[:, g, 0] = -1.0
                tot = (AK2[ps, a] * W[ps, a, :].sum(1)[:, None])  # (B2,2)
                if content == "lp":
                    Msh[:, sl, 1] -= tot
                elif fr:
                    Msh[:, sl, 2] += tot
                    Msh[:, sl, 1] -= tot
                if cv0:
                    if t == 0:
                        Gsh[:, sl, 2 + a] = AKown[ps, a]
                    else:
                        Msh[:, sl, iv0s:iv0s + N] += AK2[ps, a, :, None] * W[ps, a, :][:, None, :]
                if condS:
                    cS = AK2[ps, a] * W[ps, a, 0][:, None]
                    if content == "full":
                        Msh[:, sl, ivs] += cS
                    elif fr:
                        Msh[:, sl, ivs0] += cS
                    if a == 0:
                        Gsh[:, sl, 1] = AKown[ps, 0]
        if condS:
            Gsh[:, ivs, 1] = 1.0
            if t == 0:
                Gsh[:, ivs0, 1] = 1.0
            else:
                Msh[:, ivs0, ivs0] = 1.0
        if cv0:
            for j in range(N):
                if t == 0:
                    Gsh[:, iv0s + j, 2 + j] = 1.0
                else:
                    Msh[:, iv0s + j, iv0s + j] = 1.0
        Dn = np.array([Q, Rs[0] if condS else 0.0] + (list(Rs) if cv0 else []))
        Csh = Msh @ Csh @ Msh.transpose(0, 2, 1) + (Gsh * Dn[None, None, :]) @ Gsh.transpose(0, 2, 1)

        # ------------------------------------------------ union filter (unconditional moments)
        if do_union:
            kS = read[:, 1:5, 0].sum(1)
            if np.any((kS != 4) & (t > 0)):
                nU_bad += int(np.sum((kS != 4) & (t > 0)))
            invPU = inv2(PmU)
            LamU = invPU.copy()
            LamU[:, 0, 0] += 4.0 / p["R"]
            wS = np.where(kS > 0, 1.0 / (p["RS"] + Rc / np.maximum(kS, 1)), 0.0)
            LamU[:, 1, 1] += wS
            PpU = inv2(LamU)
            ATU = A @ (PpU @ invPU)
            AKU1 = (A @ (PpU[:, :, 0] / p["R"])[..., None])[..., 0]
            AKU2 = (A @ PpU[:, :, 1][..., None])[..., 0] * wS[:, None]
            Mu = np.zeros((B, du, du))
            Gu = np.zeros((B, du, 10))  # w, v_0..v_4, nu_1S..nu_4S
            Nu = np.zeros((B, du, du))
            for m in range(4):
                a = m + 1
                sl = slice(2 * m, 2 * m + 2)
                Mu[:, sl, sl] = AT[:, a]
                Mu[:, sl, 10:15] = AK2[:, a, :, None] * W[:, a, :][:, None, :]
                Gu[:, 2 * m, 0] = -1.0
                Gu[:, sl, 1 + a] = AKown[:, a]
                Gu[:, sl, 6 + m] = AK2[:, a] * W[:, a, 0][:, None]
                s2 = (W[:, a, 1:] ** 2).sum(1) * Rc
                Nu[:, sl, sl] = s2[:, None, None] * (AK2[:, a, :, None] * AK2[:, a, None, :]) + qc * np.eye(2)
                Gu[:, 8:10, 1 + a] = AKU1
                Gu[:, 8:10, 6 + m] = AKU2 * (read[:, a, 0] / np.maximum(kS, 1))[:, None]
            Mu[:, 8:10, 8:10] = ATU
            Mu[:, 8:10, 10] = AKU2
            Gu[:, 8, 0] = -1.0
            for a in range(5):
                Gu[:, 10 + a, 1 + a] = 1.0
            Du = np.array([Q, p["RS"], p["R"], p["R"], p["R"], p["R"], Rc, Rc, Rc, Rc])
            Cu = Mu @ Cu @ Mu.transpose(0, 2, 1) + (Gu * Du[None, None, :]) @ Gu.transpose(0, 2, 1) + Nu
            PmU = A @ PpU @ A.T + np.array([[Q, 0.0], [0.0, 0.0]])

        # ------------------------------------------------ memory (noise-driven part, q scaled to 1)
        if do_memory:
            At = np.zeros((B, 8, 8))
            for m in range(4):
                At[:, 2 * m:2 * m + 2, 2 * m:2 * m + 2] = AT[:, m + 1]
            VY0 = np.einsum("i,bij,j->b", Pv, Sx, Pv)
            cov = np.einsum("i,bij,j->b", Pv, At @ Sx, Pv)
            Sx_next = At @ Sx @ At.transpose(0, 2, 1) + eye8
            VY1 = np.einsum("i,bij,j->b", Pv, Sx_next, Pv)
            Vc = np.where(VY0 > 1e-300, VY1 - cov ** 2 / np.where(VY0 > 1e-300, VY0, 1.0), VY1)

            def filt(Sf: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
                sP = Sf @ Pv
                s = sP @ Pv
                upd = np.where((s > 1e-300)[:, None, None],
                               Sf - sP[:, :, None] * sP[:, None, :] / np.where(s > 1e-300, s, 1.0)[:, None, None],
                               Sf)
                Sn = At @ upd @ At.transpose(0, 2, 1) + eye8
                return Sn, np.einsum("i,bij,j->b", Pv, Sn, Pv)

            Sf2, Vf2 = filt(Sf2)
            I2[:, t] = 0.5 * np.log(Vc / Vf2)
            Dcl[:, t] = 0.5 * np.log(Vc / PP)
            if t == T_burn:
                Sf1 = Sx.copy()
            if t >= T_burn:
                Sf1, Vf1 = filt(Sf1)
                I1[:, t - T_burn] = 0.5 * np.log(Vc / Vf1)
            Sx = Sx_next

        # ------------------------------------------------ attention choice for the next round
        Pm_next = A @ Pp @ A.T + model.Qx
        Ln = inv2(Pm_next)
        ldPm = np.log(Pm_next[..., 0, 0] * Pm_next[..., 1, 1] - Pm_next[..., 0, 1] ** 2)  # (B,N)
        read_next = np.zeros((B, N, N))
        if model.att != "fixedS":
            a_ = Ln[:, recv, 0, 0] + 1.0 / Rs[recv][None, :]
            b_ = Ln[:, recv, 0, 1]
            c_ = Ln[:, recv, 1, 1]
            det = a_[..., None] * (c_[..., None] + model.sig[None]) - b_[..., None] ** 2  # (B,Nr,11)
            Iinfo = 0.5 * (ldPm[:, recv, None] + np.log(det))
            if model.att in ("efe", "efeS"):
                logit = gam * Iinfo
            else:
                logit = np.zeros_like(Iinfo)
            logit = np.where(model.mask[None, None, :], logit, -np.inf)
            logit -= logit.max(-1, keepdims=True)
            pr = np.exp(logit)
            pr /= pr.sum(-1, keepdims=True)
            k = np.argmax(logit + rng.gumbel(size=logit.shape), axis=-1)  # exact draw from pr
            if rec:
                acc_prob += pr.sum(0)
                np.add.at(acc_cnt, (np.repeat(np.arange(Nr)[None, :], B, 0), k), 1.0)
                n_att += B
                if model.kind == "pop":
                    nonS = (pr * (~model.hasS[None])).sum(-1)
                    max_nonS = max(max_nonS, float(nonS.max()))
            for r, a in enumerate(recv):
                read_next[:, a, :] = model.Ind[r][k[:, r]]
            if store_types and rec:
                types.append(k.copy())
        else:
            for a in recv:
                read_next[:, a, 0] = 1.0
        Pm = Pm_next
        read = read_next

    out: dict[str, Any] = dict(acc_h=acc_h, acc_V=acc_V, n_path_t=n_path_t, n_pair_t=n_pair_t,
                               att_prob=acc_prob / max(n_att, 1), att_freq=acc_cnt / max(n_att, 1),
                               max_nonS=max_nonS, G=G, Pm_last=Pm)
    if do_union:
        out["accU"] = accU
        out["nU_bad"] = nU_bad
    if do_memory:
        out["I2"] = I2
        out["I1"] = I1
        out["Dcl"] = Dcl
    if store_types:
        out["types"] = types
    return out


def group_sigmas(res: dict[str, Any]) -> np.ndarray:
    """Per-group estimates of Sigma^c (G,N,N)."""
    Sh = res["acc_h"] / res["n_path_t"][:, None, None]
    V = res["acc_V"] / res["n_pair_t"][:, None]
    return Sh + np.einsum("gi,ij->gij", V, np.eye(V.shape[1]))


def jackknife(stat, groups: np.ndarray) -> tuple[Any, Any]:
    """Grouped jackknife: stat(mean over groups) and its SE."""
    G = groups.shape[0]
    full = np.asarray(stat(groups.mean(0)))
    loo = np.array([np.asarray(stat(np.delete(groups, g, 0).mean(0))) for g in range(G)])
    se = np.sqrt((G - 1) / G * ((loo - loo.mean(0)) ** 2).sum(0))
    return full, se


# ----------------------------------------------------------------------------- contrast
def regions(n: int, minsize: int = 2) -> list[tuple[int, ...]]:
    out: list[tuple[int, ...]] = []
    for k in range(minsize, n + 1):
        out += list(combinations(range(n), k))
    return out


def contrast_from_precision(Pi: np.ndarray, C: tuple[int, ...]) -> dict[str, float]:
    r"""r(C)=x_in/x_out with x_out=phi^T Pi phi, x_in=min_{f perp 1_C} f^T(diag(eps)+L_C)f/f^Tf."""
    n = len(C)
    C = list(C)
    a = -Pi.copy()
    np.fill_diagonal(a, 0.0)
    eps = Pi.sum(1)
    phi = np.zeros(Pi.shape[0])
    phi[C] = 1 / np.sqrt(n)
    xout = phi @ Pi @ phi
    aC = a[np.ix_(C, C)]
    LC = np.diag(aC.sum(1)) - aC
    MC = np.diag(eps[C]) + LC
    # orthonormal basis of 1^perp in R^n
    Qm, _ = np.linalg.qr(np.column_stack([np.ones(n), np.eye(n)[:, : n - 1]]))
    U = Qm[:, 1:]
    xin = np.linalg.eigvalsh(U.T @ MC @ U).min()
    cut = sum(a[i, k] for i in C for k in range(Pi.shape[0]) if k not in C)
    return dict(r=xin / xout, xin=xin, xout=xout, cut=cut, epsbar=eps[C].mean(),
                epsmax=eps[C].max(), het=eps[C].max() / eps[C].mean(),
                rstar=(np.sort(np.linalg.eigvalsh(LC))[1] / (cut / n)) if cut > 0 else np.inf)


def analyze_sigma(S: np.ndarray, A_region: tuple[int, ...] = (1, 2, 3, 4)) -> dict[str, Any]:
    Pi = np.linalg.inv(S)
    N = S.shape[0]
    off = Pi - np.diag(np.diag(Pi))
    maxoff = off[~np.eye(N, dtype=bool)].max()
    rows = Pi.sum(1)
    res = dict(Pi=Pi, maxoff=maxoff, minrow=rows.min(), diffusive=bool(maxoff <= 0 and rows.min() >= 0),
               a=-off, eps=rows)
    rr = {C: contrast_from_precision(Pi, C)["r"] for C in regions(N)}
    res["r_all"] = rr
    res["rA"] = rr[tuple(A_region)]
    others = {C: v for C, v in rr.items() if C != tuple(A_region)}
    Cmax = max(others, key=others.get)
    res["max_other"] = (Cmax, others[Cmax])
    cA = contrast_from_precision(Pi, tuple(A_region))
    res["hetA"] = cA["het"]
    res["A_detail"] = cA
    iu = np.triu_indices(N, 1)
    abar = res["a"][iu].mean()
    ebar = rows.mean()
    Pih = (ebar + (N - 1) * abar) * np.eye(N) - abar * (np.ones((N, N)) - np.eye(N))
    rh = {C: contrast_from_precision(Pih, C)["r"] for C in regions(N)}
    res["abar"], res["ebar"] = abar, ebar
    res["baseline_mean"] = max(rh.values())
    return res


def exchangeable_baseline(S: np.ndarray) -> dict[str, Any]:
    """Symmetrize an (estimated) exchangeable Sigma and compute its sup contrast."""
    N = S.shape[0]
    d = np.diag(S).mean()
    o = S[~np.eye(N, dtype=bool)].mean()
    Ss = o * np.ones((N, N)) + (d - o) * np.eye(N)
    Pi = np.linalg.inv(Ss)
    a = -Pi[0, 1]
    eps = Pi.sum(1)[0]
    rr = {C: contrast_from_precision(Pi, C)["r"] for C in regions(N)}
    Cmax = max(rr, key=rr.get)
    return dict(a=a, eps=eps, sup=rr[Cmax], argsup=Cmax, by_size={k: max(v for C, v in rr.items() if len(C) == k)
                                                              for k in range(2, N + 1)})


# ----------------------------------------------------------------------------- exact attention law
def kalman_maps(p: dict[str, float]):
    F, Q, qc = p["F"], p["Q"], p["qc"]
    A = np.array([[F, 0.0], [1.0, 0.0]])
    Qx = np.array([[Q + qc, 0.0], [0.0, qc]])

    def pred(Pp: np.ndarray) -> np.ndarray:
        return A @ Pp @ A.T + Qx

    def upd(Pm: np.ndarray, Rown: float, sig: np.ndarray | float) -> np.ndarray:
        L = inv2(Pm)
        L[..., 0, 0] += 1.0 / Rown
        L[..., 1, 1] += sig
        return inv2(L)

    return A, Qx, pred, upd


def member_type_probs(p: dict[str, float], Pp: np.ndarray) -> np.ndarray:
    """Probabilities of the five types (s,m) in order (0,0),(0,1),(0,2),(1,0),(1,1), multiplicities
    1,3,3,1,3, for a population member whose current posterior covariance is Pp (...,2,2)."""
    A, Qx, pred, upd = kalman_maps(p)
    wm, wS = 1 / (p["R"] + p["Rc"]), 1 / (p["RS"] + p["Rc"])
    sig = np.array([0.0, wm, 2 * wm, wS, wS + wm])
    mult = np.array([1.0, 3.0, 3.0, 1.0, 3.0])
    Pm = pred(Pp)
    Ln = inv2(Pm)
    ld = np.log(Pm[..., 0, 0] * Pm[..., 1, 1] - Pm[..., 0, 1] ** 2)
    a_ = Ln[..., 0, 0] + 1 / p["R"]
    det = a_[..., None] * (Ln[..., 1, 1][..., None] + sig) - Ln[..., 0, 1][..., None] ** 2
    I = 0.5 * (ld[..., None] + np.log(det))
    lg = p["gamma"] * I + np.log(mult)
    lg -= lg.max(-1, keepdims=True)
    pr = np.exp(lg)
    return pr / pr.sum(-1, keepdims=True), I


def exact_attention_law(p: dict[str, float], L: int = 12, iters: int = 400) -> dict[str, Any]:
    """Stationary law of a member's type via the history chain truncated to the last L types,
    with the two source-including types (1,0),(1,1) as the reduced alphabet."""
    A, Qx, pred, upd = kalman_maps(p)
    wm, wS = 1 / (p["R"] + p["Rc"]), 1 / (p["RS"] + p["Rc"])
    # reference posterior: fixed point of the {S}-only recursion
    Pp = world_cov(p)
    for _ in range(500):
        Pp = upd(pred(Pp), p["R"], wS)
    nS = 1 << L
    codes = np.arange(nS)
    Ph = np.broadcast_to(Pp, (nS, 2, 2)).copy()
    sig2 = np.array([wS, wS + wm])  # bit 0 -> {S}, bit 1 -> {S,m}
    for k in range(L - 1, -1, -1):  # oldest first; bit 0 of code = most recent type
        bit = (codes >> k) & 1
        Ph = upd(pred(Ph), p["R"], sig2[bit])
    pr5, I5 = member_type_probs(p, Ph)  # (nS,5)
    pS = pr5[:, 3:5]
    nonS = pr5[:, :3].sum(1)
    q = pS / pS.sum(1, keepdims=True)
    pi = np.full(nS, 1.0 / nS)
    for _ in range(iters):
        new = np.zeros(nS)
        for tau in (0, 1):
            nc = ((codes << 1) | tau) & (nS - 1)
            new += np.bincount(nc, weights=pi * q[:, tau], minlength=nS)
        if np.abs(new - pi).max() < 1e-17:
            pi = new
            break
        pi = new
    law5 = pi @ pr5
    return dict(law5=law5, nonS=float(pi @ nonS), pi=pi, I5_mean=pi @ I5,
                v_prior=float(pi @ pred(Ph)[:, 0, 0]), v_post=float(pi @ Ph[:, 0, 0]))


def exact_attention_law_full(p: dict[str, float], L: int = 6, iters: int = 300) -> dict[str, Any]:
    """Same with all five types kept (base-5 history codes) for a cross-check."""
    A, Qx, pred, upd = kalman_maps(p)
    wm, wS = 1 / (p["R"] + p["Rc"]), 1 / (p["RS"] + p["Rc"])
    sig = np.array([0.0, wm, 2 * wm, wS, wS + wm])
    Pp = world_cov(p)
    for _ in range(500):
        Pp = upd(pred(Pp), p["R"], wS)
    nS = 5 ** L
    codes = np.arange(nS)
    Ph = np.broadcast_to(Pp, (nS, 2, 2)).copy()
    for k in range(L - 1, -1, -1):
        dig = (codes // 5 ** k) % 5
        Ph = upd(pred(Ph), p["R"], sig[dig])
    pr5, _ = member_type_probs(p, Ph)
    pi = np.full(nS, 1.0 / nS)
    for _ in range(iters):
        new = np.zeros(nS)
        for tau in range(5):
            nc = (codes * 5 + tau) % nS
            new += np.bincount(nc, weights=pi * pr5[:, tau], minlength=nS)
        if np.abs(new - pi).max() < 1e-18:
            pi = new
            break
        pi = new
    return dict(law5=pi @ pr5)


def law11_from_types(law5: np.ndarray) -> dict[str, float]:
    """Expand the type law to the eleven sets."""
    return {"{}": law5[0], "{m_k} (each of 3)": law5[1] / 3, "{m_k,m_l} (each of 3)": law5[2] / 3,
            "{S}": law5[3], "{S,m_k} (each of 3)": law5[4] / 3}


def pbar11(law5: np.ndarray) -> np.ndarray:
    return np.array([law5[0]] + [law5[1] / 3] * 3 + [law5[2] / 3] * 3 + [law5[3]] + [law5[4] / 3] * 3)


# ----------------------------------------------------------------------------- agency index
def agency_index(law5: np.ndarray, nonS: float, p: dict[str, float], V: float) -> dict[str, float]:
    r"""Agency index for four members with product actual law P = pbar^{x4}, uniform habits on the
    11 sets, group model P_g(pi) ~ exp(gamma_C I_C(k(pi))), I_C(k)=0.5 ln(1+k V/R_c), k = number of
    members whose set contains S (slots = readings of the source)."""
    pb = pbar11(law5)
    pb = pb / pb.sum()
    H = -(pb * np.log(pb)).sum()
    KL_E = 4 * (np.log(11) - H)
    one_m_rho = nonS  # P(member's set has no S)
    rho = 1 - one_m_rho
    ks = np.arange(5)
    from math import comb
    Pk = np.array([comb(4, k) * rho ** k * one_m_rho ** (4 - k) for k in ks])
    ck = np.array([comb(4, k) * 4.0 ** k * 7.0 ** (4 - k) for k in ks])
    IC = 0.5 * np.log(1 + ks * V / p["Rc"])
    dI = IC[4] - IC  # >= 0

    def KLg(g: float) -> float:
        lse = np.log(np.sum(ck * np.exp(-g * dI)))
        return -4 * H + g * np.sum(Pk * dI) + lse

    # minimize over gamma_C >= 0 (convex); golden search on log-scale bracket
    from scipy.optimize import minimize_scalar
    gs = np.concatenate([[0.0], np.logspace(-2, 4, 2000)])
    vals = np.array([KLg(g) for g in gs])
    i = int(vals.argmin())
    lo, hi = gs[max(i - 1, 0)], gs[min(i + 1, len(gs) - 1)]
    if hi > lo:
        r = minimize_scalar(KLg, bounds=(lo, hi), method="bounded", options=dict(xatol=1e-10))
        gstar, kmin = (r.x, r.fun) if r.fun <= vals[i] else (gs[i], vals[i])
    else:
        gstar, kmin = gs[i], vals[i]
    lim = -4 * H + np.log(256.0)  # gamma_C -> infinity with P(k<4)=0
    return dict(KL_E=KL_E, KL_inf=kmin, gamma_C=gstar, index=1 - kmin / KL_E, KL_limit_inf=lim,
                KL_g0=KLg(0.0))


# ----------------------------------------------------------------------------- exact fixed-{S} model
def exact_fixedS(p: dict[str, float], condS: bool = False) -> dict[str, Any]:
    """Members always read {S}; S reads nothing. Time-invariant: Lyapunov equation for the private part."""
    A, Qx, pred, upd = kalman_maps(p)
    N = 5
    Rs = np.array([p["RS"], p["R"], p["R"], p["R"], p["R"]])
    wS = 1 / (p["RS"] + p["Rc"])
    PpS = world_cov(p)
    PpM = world_cov(p)
    for _ in range(3000):
        PpS = upd(pred(PpS), p["RS"], 0.0)
        PpM = upd(pred(PpM), p["R"], wS)
    PmS, PmM = pred(PpS), pred(PpM)
    # probability of {} versus {S} at the fixed point (choice made from PpM)
    _, I5 = member_type_probs(p, PpM)
    dI = I5[3] - I5[0]
    p_empty = 1.0 / (1.0 + np.exp(p["gamma"] * dI))
    d = 3 * N
    M = np.zeros((d, d))
    Gv = np.zeros((d, N))
    Nx = np.zeros((d, d))
    Pps = [PpS] + [PpM] * 4
    Pms = [PmS] + [PmM] * 4
    pm = np.ones(N)
    if condS:
        pm[0] = 0.0
    for a in range(N):
        sl = slice(2 * a, 2 * a + 2)
        T = Pps[a] @ np.linalg.inv(Pms[a])
        M[sl, sl] = A @ T
        Gv[sl, a] = A @ Pps[a][:, 0] / Rs[a]
        Gv[2 * N + a, a] = 1.0
        if a > 0:
            AK2 = A @ Pps[a][:, 1] * wS
            M[sl, 2 * N + 0] = AK2 * pm[0]
            Nx[sl, sl] = np.outer(AK2, AK2) * p["Rc"]
        Nx[sl, sl] += p["qc"] * np.eye(2)
    Nn = Gv @ np.diag(Rs * pm) @ Gv.T + Nx
    vecC = np.linalg.solve(np.eye(d * d) - np.kron(M, M), Nn.reshape(-1))
    C = vecC.reshape(d, d)
    C = 0.5 * (C + C.T)
    e = np.arange(0, 2 * N, 2)
    return dict(Sigma=C[np.ix_(e, e)], p_empty=p_empty, dI=dI, PmM=PmM, PpM=PpM, PmS=PmS,
                resid=np.abs(M @ C @ M.T + Nn - C).max())


# ----------------------------------------------------------------------------- design
def frac_design() -> np.ndarray:
    """2^(7-3) resolution IV: base A,B,C,D; E=ABC, F=BCD, G=ACD; plus the center (first row)."""
    rows = [np.zeros(7)]
    for i in range(16):
        a, b, c, d = [1 if (i >> k) & 1 else -1 for k in (3, 2, 1, 0)]
        rows.append(np.array([a, b, c, d, a * b * c, b * c * d, a * c * d], float))
    return np.array(rows)


FACTORS = ["F", "Q", "R", "RS", "Rc", "qc", "gamma"]


def point_params(code: np.ndarray, rel: float = 0.05) -> dict[str, float]:
    p = dict(BASE)
    for f, c in zip(FACTORS, code):
        p[f] = BASE[f] * (1 + rel * c)
    return p
