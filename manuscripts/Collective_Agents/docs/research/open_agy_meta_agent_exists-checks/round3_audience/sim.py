r"""Vectorized sampled-noise Monte Carlo of the audience population (independent of aud.py's exact algebra).

Two replicas per world path (shared world, independent private noises and policy randomness), so that
  Sigma^c = E[Cov(e(t) | eta)] = (1/2) E[(e^1 - e^2)(e^1 - e^2)^T]   (second-moment convention, 04_collectives.tex:187).
Written from the declared specification in aud.py's docstring; it re-implements the filters in information form.
Modes: 'full' (EFE attention), 'hab' (gamma = 0), 'pr' (partners redrawn uniformly every round, kmsg per round),
'fixedS' (audience reads the source only), 'dead' (channels deliver pure noise, attention as 'fixedS').
Medium modes (mechanism baseline): set src=False, then every agent is of the audience type and has capacity kmsg.
"""
from __future__ import annotations

import os
for _v in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS"):
    os.environ.setdefault(_v, "1")
from math import comb

import numpy as np


def run(F, Q, R, RS, Rc, qc, n, kmsg, gamma, K, T, burn, seed, mode="full", src=True, Rmed=None, nbatch=20,
        psi=0.0, shared=True):
    r"""Return dict with per-batch Sigma^c estimates (nbatch, N, N), pooled estimate, attention statistics."""
    rng = np.random.default_rng(seed)
    N = n + 1
    Rown = np.full(N, R if Rmed is None else Rmed, float)
    if src:
        Rown[0] = RS
    cap = np.full(N, kmsg)
    if src:
        cap[0] = 0
    B = 2 * K
    Kw = K if shared else B
    world_of = np.repeat(np.arange(K), 2) if shared else np.arange(B)
    V0 = Q / (1 - F ** 2)
    eta = rng.normal(0.0, np.sqrt(V0), Kw)
    # claimed prior covariances (B, N) for components 00, 01, 11 and prior means m0, m1
    P00 = np.full((B, N), V0 + qc)
    P01 = np.full((B, N), F * V0)
    P11 = np.full((B, N), V0 + qc)
    m0 = np.zeros((B, N))
    m1 = np.zeros((B, N))
    att = np.zeros((B, N, N), dtype=bool)          # att[b, i, j]: i reads j's channel this round
    s_prev = np.zeros((B, N))
    ar = np.arange(B)
    S_acc = np.zeros((K, N, N))
    cnt = 0
    nread_src = 0.0
    nread_tot = 0.0
    # attention types for EFE: sets of size <= kmsg among the N-1 others
    others = [[j for j in range(N) if j != i] for i in range(N)]
    for t in range(T):
        eb = eta[world_of]
        e = m0 - eb[:, None]
        if t >= burn:
            d = e[0::2] - e[1::2]
            S_acc += 0.5 * d[:, :, None] * d[:, None, :]
            cnt += 1
            if src:
                nread_src += att[:, 1:, 0].mean()
            nread_tot += att.sum(2).mean()
        # observations of round t
        s = eb[:, None] + np.sqrt(Rown)[None, :] * rng.standard_normal((B, N))
        # channel precision and channel sums: y_ij = s_j(t-1) + nu_ij, claimed noise Rown[j] + Rc
        prec_j = 1.0 / (Rown + Rc)                       # (N,)
        bsum = (att * prec_j[None, None, :]).sum(2)      # (B, N)
        if mode == "dead":
            noise_var = (Rown + Rc)[None, None, :] * att
            ysum = (np.sqrt(noise_var) * rng.standard_normal((B, N, N)) * prec_j[None, None, :]).sum(2)
        else:
            ysum = ((att * (s_prev[:, None, :] + np.sqrt(Rc) * rng.standard_normal((B, N, N))))
                    * prec_j[None, None, :]).sum(2)
        # information-form update on x_t = (eta_t, eta_{t-1})
        det = P00 * P11 - P01 ** 2
        i00, i01, i11 = P11 / det, -P01 / det, P00 / det
        L00 = i00 + 1.0 / Rown[None, :]
        L01 = i01
        L11 = i11 + bsum
        h0 = i00 * m0 + i01 * m1 + s / Rown[None, :]
        h1 = i01 * m0 + i11 * m1 + ysum
        dL = L00 * L11 - L01 ** 2
        Q00, Q01, Q11 = L11 / dL, -L01 / dL, L00 / dL
        mp0 = Q00 * h0 + Q01 * h1
        m0 = F * mp0 + np.sqrt(qc) * rng.standard_normal((B, N))
        m1 = mp0 + np.sqrt(qc) * rng.standard_normal((B, N))
        P00 = F * F * Q00 + Q + qc
        P01 = F * Q00
        P11 = Q00 + qc
        # attention for round t+1
        new = np.zeros((B, N, N), dtype=bool)
        for i in range(N):
            if cap[i] == 0:
                continue
            oth = others[i]
            if mode in ("fixedS", "dead"):
                new[:, i, 0] = True
                continue
            if mode == "pr":
                keys = rng.random((B, len(oth)))
                order = np.argsort(keys, axis=1)[:, : cap[i]]
                for c in range(cap[i]):
                    new[ar, i, np.array(oth)[order[:, c]]] = True
                continue
            # enumerate sets by (has a precise sender s, number of ordinary senders m): channel precisions differ
            # only between the source (Rown[0]) and the others (Rown[1..]); in a medium all are equal.
            prec_o = prec_j[oth]
            uniq = np.unique(np.round(prec_o, 14))
            # build the list of all sets of size <= cap (small N): exact enumeration
            sets = [()]
            for k in range(1, cap[i] + 1):
                from itertools import combinations
                sets += list(combinations(oth, k))
            bset = np.array([prec_j[list(S_)].sum() if len(S_) else 0.0 for S_ in sets])
            # info under each system's prior P^-_i(t+1)
            a = 1.0 / Rown[i]
            p00 = P00[:, i][:, None]; p01 = P01[:, i][:, None]; p11 = P11[:, i][:, None]
            info = 0.5 * np.log((1 + a * p00) * (1 + bset[None, :] * p11) - a * bset[None, :] * p01 ** 2)
            G = -info + psi * np.array([len(S_) for S_ in sets])[None, :]
            if mode == "hab":
                lw = np.zeros_like(G)
            else:
                lw = -gamma * G
            lw = lw - lw.max(1, keepdims=True)
            pr = np.exp(lw)
            pr /= pr.sum(1, keepdims=True)
            u = rng.random((B, 1))
            k = np.minimum((u > np.cumsum(pr, 1)).sum(1), len(sets) - 1)
            for si, S_ in enumerate(sets):
                sel = k == si
                for j in S_:
                    new[sel, i, j] = True
        att = new
        s_prev = s
        eta = F * eta + np.sqrt(Q) * rng.standard_normal(Kw)
    S_world = S_acc / cnt
    S_b = np.array([S_world[i::nbatch].mean(0) for i in range(nbatch)])
    return dict(S=S_world.mean(0), S_b=S_b, read_src=nread_src / max(cnt, 1), read_tot=nread_tot / max(cnt, 1))
