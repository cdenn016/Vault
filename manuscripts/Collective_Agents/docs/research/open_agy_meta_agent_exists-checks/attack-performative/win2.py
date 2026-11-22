r"""Variant builder: members' exact (time-varying) Kalman filter with the public act U as a KNOWN INPUT
(the investigator's member model), for contemporaneous relays (delay 0, PN as stated) or one-round-stale relays
(delay 1, the literal channel latency of def:fw-system, 02_framework.tex:15: y_ij(t+1) = u_j(t) + nu_ij(t+1)),
with optional private internal noise q_int added to each member's prediction (Q^n > 0 in def:agy-closure).

Implementation: eta_t = zeta_t + (U-part), zeta the act-free world (functions of eta_0 and w only).  The member's
known-input Kalman estimate is E[zeta_t | its U-free observations] + U-part, computed by exact conditioning on
coefficient rows (U-free observations depend only on eta_0, w, v, nu, so this is the member's model law).
"""
from __future__ import annotations

import numpy as np
from win import cond_mean_row


def build_kf(F: float, Q: float, R: float, Rc: float, b: float, g: float, T: int, delay: int = 0,
             q_int: float = 0.0, n: int = 4) -> dict:
    pairs = [(i, j) for i in range(n) for j in range(n) if i != j]
    per = 1 + n + len(pairs) + n  # w, v, nu, internal noise
    NT = 1 + per * T
    sig0 = np.sqrt(Q / (1 - F * F))

    def unit(k: int) -> np.ndarray:
        e = np.zeros(NT)
        e[k] = 1.0
        return e

    zeta = [sig0 * unit(0)]
    upart = [np.zeros(NT)]  # U-part of eta_t
    eta = [zeta[0].copy()]
    vrow = []  # vrow[t][k] = sqrt(R) v_k(t)
    obs = [[] for _ in range(n)]  # U-free observation rows
    m = [np.zeros(NT) for _ in range(n)]
    E_rows = []
    for t in range(T):
        base = 1 + per * t
        iw = base
        iv = [base + 1 + k for k in range(n)]
        inu = {p: base + 1 + n + q for q, p in enumerate(pairs)}
        ii = [base + 1 + n + len(pairs) + k for k in range(n)]
        vrow.append([np.sqrt(R) * unit(iv[k]) for k in range(n)])
        E_rows.append(np.array([m[i] - eta[t] for i in range(n)]))
        mp = []
        for i in range(n):
            obs[i].append(zeta[t] + vrow[t][i])
            if t - delay >= 0:
                for j in range(n):
                    if j != i:
                        obs[i].append(zeta[t - delay] + vrow[t - delay][j] + np.sqrt(Rc) * unit(inu[(i, j)]))
            row, _ = cond_mean_row(zeta[t], np.array(obs[i]))
            mp.append(row + upart[t])
        U = -g * sum(mp)
        zeta.append(F * zeta[t] + np.sqrt(Q) * unit(iw))
        upart.append(F * upart[t] + b * U)
        eta.append(zeta[t + 1] + upart[t + 1])
        newm = []
        for i in range(n):
            mi = F * mp[i] + b * U
            if q_int > 0:
                mi = mi + np.sqrt(q_int) * unit(ii[i])
            newm.append(mi)
        m = newm
    return {"eta": np.array(eta), "E": E_rows}
