r"""Independent window builder for one performative niche (attack on PN; not derived from pc.py / pcg.py).

Every scalar variable is a coefficient row over standardized independent noises xi ~ N(0, I):
  coordinate 0: eta_0 / sigma_0; per round t (17 coordinates): w_t, v_0..v_3(t), nu_ij(t) (12 ordered pairs i != j).
One niche of n = 4 members (the other niche is an independent copy; cross entries of Pi^c vanish).

Model (the investigator's PN, check5/pcg conventions):
  s_k(t) = eta_t + v_k(t),  y_ij(t) = eta_t + v_j(t) + nu_ij(t)   (receiver-specific nu, raw relay, same round)
  base mode : m_i^+(t) = c0 m_i(t) + Ks s_i(t) + Kc sum_j y_ij(t)  (steady-state Kalman, U treated as known input)
  exact mode: m_i^+(t) = E[eta_t | s_i, y_ij up to t, U up to t-1]   (exact conditioning under the true joint law)
  U(t) = -g sum_i m_i^+(t);   eta_{t+1} = F eta_t + b U(t) + w_t
  base : m_i(t+1) = F m_i^+(t) + b U(t)
  exact: m_i(t+1) = F E[eta_t | data up to t incl. U(t)] + b U(t)
  optional internal noise: m_i(t+1) += xint_i(t) with variance q_int (needs extra coordinates)
Prior errors e_i(t) = m_i(t) - eta_t (def:fw-level0 convention).
"""
from __future__ import annotations

import numpy as np


def kalman_ss(F: float, Q: float, info: float) -> tuple[float, float]:
    r"""Scalar steady-state Kalman: P^- = F^2 P^+ + Q, (P^+)^{-1} = (P^-)^{-1} + info."""
    # closed form of the positive root of info F^2 x^2 + (1 - F^2 + info Q) x - Q = 0 for x = P^-? use iteration
    Pm = Q
    for _ in range(200000):
        Pp = 1.0 / (1.0 / Pm + info)
        Pn = F * F * Pp + Q
        if abs(Pn - Pm) < 1e-16:
            Pm = Pn
            break
        Pm = Pn
    return Pm, 1.0 / (1.0 / Pm + info)


def cond_mean_row(target: np.ndarray, D: np.ndarray) -> tuple[np.ndarray, float]:
    r"""E[target | D] as a coefficient row and Var(target | D); rows are coefficient vectors over xi ~ N(0,I)."""
    # scale rows of D to unit norm for conditioning
    sc = np.linalg.norm(D, axis=1)
    Ds = D / sc[:, None]
    G = Ds @ Ds.T
    c = Ds @ target
    lam = np.linalg.solve(G, c)
    row = lam @ Ds
    var = float(target @ target - c @ lam)
    return row, var


def build(F: float, Q: float, R: float, Rc: float, b: float, g: float, T: int, mode: str = "base",
          q_int: float = 0.0, n: int = 4, sig0: float | None = None, probe_t: int | None = None) -> dict:
    pairs = [(i, j) for i in range(n) for j in range(n) if i != j]
    per = 1 + n + len(pairs) + (n if q_int > 0 else 0)
    NT = 1 + per * T
    if sig0 is None:
        sig0 = np.sqrt(Q / (1 - F * F))
    Pm, Pp = kalman_ss(F, Q, 1.0 / R + (n - 1) / (R + Rc))
    Ks, Kc = Pp / R, Pp / (R + Rc)
    c0 = 1.0 - Ks - (n - 1) * Kc

    def unit(k: int) -> np.ndarray:
        e = np.zeros(NT)
        e[k] = 1.0
        return e

    eta = [sig0 * unit(0)]
    m = [np.zeros(NT) for _ in range(n)]
    D = [[] for _ in range(n)]  # data rows per member
    E_rows, Mp_rows, U_rows = [], [], []
    probe = {}
    for t in range(T):
        base = 1 + per * t
        iw = base
        iv = [base + 1 + k for k in range(n)]
        inu = {p: base + 1 + n + q for q, p in enumerate(pairs)}
        iint = [base + 1 + n + len(pairs) + k for k in range(n)] if q_int > 0 else None
        s = [eta[t] + np.sqrt(R) * unit(iv[k]) for k in range(n)]
        y = {(i, j): eta[t] + np.sqrt(R) * unit(iv[j]) + np.sqrt(Rc) * unit(inu[(i, j)]) for (i, j) in pairs}
        E_rows.append(np.array([m[i] - eta[t] for i in range(n)]))
        mp = []
        for i in range(n):
            D[i].append(s[i])
            for j in range(n):
                if j != i:
                    D[i].append(y[(i, j)])
            if mode == "base":
                mp.append(c0 * m[i] + Ks * s[i] + Kc * sum(y[(i, j)] for j in range(n) if j != i))
            else:
                row, _ = cond_mean_row(eta[t], np.array(D[i]))
                mp.append(row)
        U = -g * sum(mp)
        Mp_rows.append(np.array(mp))
        U_rows.append(U)
        if probe_t is not None and t == probe_t:
            # informativeness of the public act for member 0 in this mode
            Dp = np.array(D[0])
            _, v_priv_pastU = cond_mean_row(eta[t], Dp)       # private data to t, U to t-1 (member's information set)
            _, v_withU = cond_mean_row(eta[t], np.vstack([Dp, U]) if g != 0 else Dp)  # plus U(t)
            mse_mp = float((mp[0] - eta[t]) @ (mp[0] - eta[t]))
            probe = {"mse_member_estimate": mse_mp, "var_given_info_set": v_priv_pastU,
                     "var_given_info_set_plus_U_t": v_withU, "Pp_claimed": Pp}
        eta_next = F * eta[t] + b * U + np.sqrt(Q) * unit(iw)
        newm = []
        for i in range(n):
            if g != 0:
                D[i].append(U)
            if mode == "base":
                mi = F * mp[i] + b * U
            else:
                row, _ = cond_mean_row(eta[t], np.array(D[i]))
                mi = F * row + b * U
            if q_int > 0:
                mi = mi + np.sqrt(q_int) * unit(iint[i])
            newm.append(mi)
        m = newm
        eta.append(eta_next)
    return {"eta": np.array(eta), "E": E_rows, "Mp": Mp_rows, "U": np.array(U_rows), "NT": NT,
            "gains": (Ks, Kc, c0, Pm, Pp), "probe": probe}


def world_conditional(mod: dict, tstar: int) -> np.ndarray:
    r"""Cov(e(t*) | eta_0..eta_T) from coefficient rows: E P_perp E^T, P_perp the projector off span(eta rows)."""
    H = mod["eta"]
    E = mod["E"][tstar]
    # orthonormal basis of the row space of H
    Qh, _ = np.linalg.qr(H.T)
    Ep = E - (E @ Qh) @ Qh.T
    S = Ep @ Ep.T
    return 0.5 * (S + S.T)


def contrast_block(Pi: np.ndarray) -> dict:
    r"""Diffusivity and contrast of the whole block (cut 0): r = x_in / x_out (def:col-contrast)."""
    n = Pi.shape[0]
    off = Pi - np.diag(np.diag(Pi))
    rows = Pi.sum(axis=1)
    phi = np.ones(n) / np.sqrt(n)
    xout = float(phi @ Pi @ phi)
    Z = np.linalg.qr(np.column_stack([phi, np.eye(n)[:, :n - 1]]))[0][:, 1:]
    xin = float(np.linalg.eigvalsh(Z.T @ Pi @ Z).min())
    return {"max_off": float(off.max()), "min_row": float(rows.min()), "diffusive": bool(off.max() <= 0 and rows.min() >= 0),
            "r": xin / xout, "xin": xin, "xout": xout,
            "cs_dev": float(np.abs(off[~np.eye(n, dtype=bool)] - off[0, 1]).max())}


def closed_form(n: int, F: float, Q: float, R: float, Rc: float, b: float, g: float) -> float:
    r"""Investigator's Prop P closed form r = v / alpha (re-typed independently from the statement)."""
    Pm, Pp = kalman_ss(F, Q, 1.0 / R + (n - 1) / (R + Rc))
    Ks, Kc = Pp / R, Pp / (R + Rc)
    c0 = 1 - Ks - (n - 1) * Kc
    sx = (Ks + (n - 1) * Kc) ** 2 * R + (n - 1) * Kc ** 2 * Rc
    sp = (Ks - Kc) ** 2 * R + (n - 1) * Kc ** 2 * Rc
    phi = F - b * g * n
    rho = c0 * phi
    s = n * b * b * g * g * sx / Q
    v = phi ** 2 * sx / np.sqrt((1 + rho ** 2 + s) ** 2 - 4 * rho ** 2)
    alpha = F ** 2 * sp / (1 - F ** 2 * c0 ** 2)
    return v / alpha
