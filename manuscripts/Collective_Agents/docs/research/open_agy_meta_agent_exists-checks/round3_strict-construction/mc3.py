r"""Sampled-noise Monte Carlo of I** (independent of the exact pair algebra in lib3.pair_moments).

B = 2K systems, two replicas per world path (shared eta path; independent sensing, read, channel and computation
noises and independent policy randomness).  The actual filters are run on sampled data, and
    Sigma^c = E[Cov(e(t) | eta)] = 1/2 E[(e^1 - e^2)(e^1 - e^2)^T]
(second-moment convention, def:col-contrast 04_collectives.tex:187).  Policies follow lib3's rules, vectorized.
Optional: the union-model filter (all members' own sensors and open private sensors, no delay) for the inference
clause, and decision records for the agency index.
"""
from __future__ import annotations

import os
for _v in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS"):
    os.environ.setdefault(_v, "1")
from dataclasses import dataclass, field

import numpy as np

from lib3 import Par, Pminus, efe_grid, log_att_weights, lse


@dataclass
class Out:
    S: np.ndarray
    S_batches: np.ndarray
    open_rate: float
    dev_rate: float
    inf: dict = field(default_factory=dict)
    dec: dict = field(default_factory=dict)


def run(par: Par, K: int, T: int, burn: int, seed: int, mode: str = "full", shared_world: bool = True,
        nbatch: int = 20, want_inf: bool = False, fresh_relays: bool = False, want_dec: bool = False,
        fixed_sig=None) -> Out:
    rng = np.random.default_rng(seed)
    n = par.n
    Kq = par.kmsg
    B = 2 * K
    Kw = K if shared_world else B
    world_of = np.repeat(np.arange(K), 2) if shared_world else np.arange(B)
    F = par.F
    V0 = par.Q / (1 - F ** 2)
    eta = rng.normal(0.0, np.sqrt(V0), Kw)
    eta_prev = F * eta + rng.normal(0.0, np.sqrt(V0 * (1 - F * F)), Kw)  # (eta_{-1} given eta_0, reversed AR)
    p = np.full((B, n), par.p0)
    m0 = np.zeros((B, n)); m1 = np.zeros((B, n))
    sig = np.zeros((B, n), dtype=int) if fixed_sig is None else np.tile(np.array(fixed_sig, int), (B, 1))
    sig_prev = np.zeros((B, n), dtype=int)
    att = np.zeros((B, n, n), dtype=bool)
    s_prev = np.zeros((B, n)); o_prev = np.zeros((B, n))
    eye = np.eye(n, dtype=bool)
    ar = np.arange(B)
    S_acc = np.zeros((K, n, n))
    cnt = 0; open_acc = 0.0; dev = 0; devn = 0
    lw_tab = {}
    # union filter (predictive belief of eta_t given all members' exterior data through t-1)
    u = np.zeros(B); U = np.full(B, V0)
    inf = {k: 0.0 for k in ("n", "dd2_over_U", "inv_U", "ln_U", "U", "dd2", "claim_ratio_m1_ln",
                            "dd2_over_U_single")}
    dec = {k: [] for k in ("p", "sig", "newsig", "k1", "att_m1", "att_m0")}
    for t in range(T):
        eta_b = eta[world_of]
        etap_b = eta_prev[world_of]
        P00, P01, P11 = Pminus(par, p)
        e = m0 - eta_b[:, None]
        if t >= burn:
            d = e[0::2] - e[1::2]
            S_acc += 0.5 * d[:, :, None] * d[:, None, :]
            cnt += 1
            open_acc += sig.mean()
            if want_inf:
                yb = m0.mean(1)
                dd = yb - u
                inf["n"] += B
                inf["dd2_over_U"] += np.sum(dd ** 2 / U)
                inf["inv_U"] += np.sum(1.0 / U)
                inf["ln_U"] += np.sum(np.log(U))
                inf["U"] += np.sum(U)
                inf["dd2"] += np.sum(dd ** 2)
                pc = P00.mean(1)
                rat = pc / U
                inf["claim_ratio_m1_ln"] += np.sum(rat - 1 - np.log(rat))
                inf["dd2_over_U_single"] += np.sum((m0[:, 0] - u) ** 2 / U)
        # ---------------- data of round t ----------------
        s = eta_b[:, None] + np.sqrt(par.R) * rng.standard_normal((B, n))
        o = eta_b[:, None] + np.sqrt(par.Rs) * rng.standard_normal((B, n))
        attf = att.astype(float)
        c_s = attf.sum(2)
        att_o = attf * sig_prev[:, None, :]
        c_o = att_o.sum(2)
        if fresh_relays:
            # NEGATIVE CONTROL: relays carry eta_{t-1} plus FRESH noise of the sender's noise variance
            rs = c_s * etap_b[:, None] + np.sqrt(c_s * (par.R + par.Rc)) * rng.standard_normal((B, n))
            ro = c_o * etap_b[:, None] + np.sqrt(c_o * (par.Rs + par.Rc)) * rng.standard_normal((B, n))
        else:
            rs = np.einsum("bij,bj->bi", attf, s_prev) + np.sqrt(c_s * par.Rc) * rng.standard_normal((B, n))
            ro = np.einsum("bij,bj->bi", att_o, o_prev) + np.sqrt(c_o * par.Rc) * rng.standard_normal((B, n))
        det = P00 * P11 - P01 ** 2
        i00, i01, i11 = P11 / det, -P01 / det, P00 / det
        a = 1.0 / par.R + sig / par.Rs
        bb = c_s / (par.R + par.Rc) + c_o / (par.Rs + par.Rc)
        h0 = i00 * m0 + i01 * m1 + s / par.R + sig * o / par.Rs
        h1 = i01 * m0 + i11 * m1 + rs / (par.R + par.Rc) + ro / (par.Rs + par.Rc)
        L00, L01, L11 = i00 + a, i01, i11 + bb
        dL = L00 * L11 - L01 ** 2
        Q00, Q01 = L11 / dL, -L01 / dL
        mp0 = Q00 * h0 + Q01 * h1
        p_new = Q00
        m0 = F * mp0 + np.sqrt(par.qc) * rng.standard_normal((B, n))
        m1 = mp0 + np.sqrt(par.qc) * rng.standard_normal((B, n))
        if want_inf:
            nopen = sig.sum(1)
            aU = n / par.R + nopen / par.Rs
            gU = u / U + s.sum(1) / par.R + (sig * o).sum(1) / par.Rs
            Up = 1.0 / (1.0 / U + aU)
            up = Up * gU
            u = F * up
            U = F * F * Up + par.Q
        # ---------------- policies for round t+1 ----------------
        if mode == "fixed":
            new_sig = sig.copy()
            new_att = ~eye[None, :, :].repeat(B, 0)
        else:
            Pn00, Pn01, Pn11 = Pminus(par, p_new)
            G = efe_grid(par, Pn00, Pn01, Pn11)                         # (B, n, 2, K+1, K+1)
            k1 = sig.sum(1)[:, None] - sig                               # open mates in round t
            lw = log_att_weights(par, k1)                               # (B, n, K+1, K+1)
            gam = 0.0 if mode == "hab" else par.gamma
            if par.proto == "real":
                movers = np.zeros((B, n), dtype=bool)
                rk = np.argsort(rng.random((B, n)), axis=1)[:, : par.nrev]
                np.put_along_axis(movers, rk, True, axis=1)
            else:
                movers = np.ones((B, n), dtype=bool)
            if mode == "pr":
                tot = par.n_inf + par.n_zero
                m_inf = rng.hypergeometric(par.n_inf, par.n_zero, Kq, size=(B, n))
                keys = rng.random((B, n, n)); keys[:, eye] = 2.0
                rank = np.argsort(np.argsort(keys, axis=2), axis=2)
                new_att = rank < m_inf[:, :, None]
                m1d = (new_att & (sig[:, None, :] == 1)).sum(2)
                m0d = m_inf - m1d
                g1 = np.take_along_axis(np.take_along_axis(G[:, :, 1], m1d[:, :, None, None], 2)[:, :, 0],
                                        m0d[:, :, None], 2)[:, :, 0]
                g0 = np.take_along_axis(np.take_along_axis(G[:, :, 0], m1d[:, :, None, None], 2)[:, :, 0],
                                        m0d[:, :, None], 2)[:, :, 0]
                dlog = gam * (g0 - g1)
                pr1 = 0.5 * (1 + np.tanh(0.5 * dlog))
                draw = (rng.random((B, n)) < pr1).astype(int)
                new_sig = np.where(movers, draw, sig)
                dev += int((m_inf < min(Kq, par.n_inf)).sum()) if t >= burn else 0
                devn += B * n if t >= burn else 0
            else:
                X1 = (lw - gam * G[:, :, 1]).reshape(B, n, -1)
                X0 = (lw - gam * G[:, :, 0]).reshape(B, n, -1)
                dlog = lse(X1, 2) - lse(X0, 2)
                pr1 = 0.5 * (1 + np.tanh(0.5 * dlog))
                draw = (rng.random((B, n)) < pr1).astype(int)
                new_sig = np.where(movers, draw, sig)
                Gs = np.where(new_sig[:, :, None, None] == 1, G[:, :, 1], G[:, :, 0])
                lq = (lw - gam * Gs).reshape(B, n, -1)
                lq = lq - lq.max(2, keepdims=True)
                q = np.exp(lq); q /= q.sum(2, keepdims=True)
                cq = np.cumsum(q, 2)
                cell = (rng.random((B, n, 1)) * cq[:, :, -1:] > cq).sum(2)
                cell = np.minimum(cell, q.shape[2] - 1)
                am1, am0 = np.divmod(cell, Kq + 1)
                if t >= burn:
                    dev += int(((am1 + am0) < min(Kq, par.n_inf)).sum()); devn += B * n
                keys = rng.random((B, n, n)); keys[:, eye] = 3.0
                op = (sig[:, None, :] == 1) & ~eye[None]
                cl = (sig[:, None, :] == 0) & ~eye[None]
                ko = np.where(op, keys, 3.0); kc = np.where(cl, keys, 3.0)
                ro_ = np.argsort(np.argsort(ko, axis=2), axis=2)
                rc_ = np.argsort(np.argsort(kc, axis=2), axis=2)
                new_att = ((ro_ < am1[:, :, None]) & op) | ((rc_ < am0[:, :, None]) & cl)
                if want_dec and t >= burn:
                    dec["p"].append(p_new.copy()); dec["sig"].append(sig.copy()); dec["newsig"].append(new_sig.copy())
                    dec["k1"].append(k1.copy()); dec["att_m1"].append(am1.copy()); dec["att_m0"].append(am0.copy())
        s_prev = s; o_prev = o
        sig_prev = sig; sig = new_sig; att = new_att
        p = p_new
        eta_prev = eta
        eta = F * eta + np.sqrt(par.Q) * rng.standard_normal(Kw)
    S_world = S_acc / cnt
    S_b = np.array([S_world[i::nbatch].mean(0) for i in range(nbatch)])
    out = Out(S=S_world.mean(0), S_batches=S_b, open_rate=open_acc / cnt, dev_rate=dev / max(devn, 1))
    if want_inf:
        out.inf = inf
    if want_dec:
        out.dec = {k: np.concatenate(v, 0) for k, v in dec.items() if len(v)}
    return out
