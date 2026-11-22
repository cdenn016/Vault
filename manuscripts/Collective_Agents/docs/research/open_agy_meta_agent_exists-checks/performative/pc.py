r"""World-conditional precision of linear-Gaussian populations whose agents act on the world.

Conventions (def:col-world-conditional, 04_collectives.tex:130-132): the world-conditional law of the
agents' errors is their conditional law given the whole world path (here: a two-sided window of
2L+1 rounds around time 0, checked for convergence in L).  World innovations are NOT conditioned
separately; there are no sender-side broadcast noises in these models (all relay noise is
receiver-specific and acts are deterministic functions of beliefs).  Because the world path is
conditioned, Cov(e_i(0) | eta) = Cov(m_i(0) | eta) for the error e_i = m_i - eta_{c(i)}.

State x_t = (eta_t (Kw), m_t (N)); x_{t+1} = A x_t + G xi_t, xi_t ~ N(0, I).
"""
from __future__ import annotations

import numpy as np
from scipy.linalg import solve_discrete_lyapunov, cho_factor, cho_solve


def stationary_cov(A: np.ndarray, Qx: np.ndarray) -> np.ndarray:
    r"""Solve P = A P A^T + Qx (requires rho(A) < 1)."""
    rho = max(abs(np.linalg.eigvals(A)))
    if rho >= 1:
        raise ValueError(f"unstable A, rho={rho}")
    P = solve_discrete_lyapunov(A, Qx)
    return 0.5 * (P + P.T)


def world_conditional_cov(A: np.ndarray, Qx: np.ndarray, iw: list[int], ia: list[int], L: int) -> np.ndarray:
    r"""Cov(x_0[ia] | x_s[iw], s = -L..L) for the stationary process x_{t+1} = A x_t + noise(Qx).

    Uses Cov(x_s, x_{s'}) = A^{s-s'} P for s >= s'.
    """
    d = A.shape[0]
    P = stationary_cov(A, Qx)
    T = 2 * L + 1
    nw = len(iw)
    APs = [P]
    for _ in range(2 * L):
        APs.append(A @ APs[-1])
    Cw = np.array([M[np.ix_(iw, iw)] for M in APs])  # (2L+1, nw, nw): Cov(x_{s+k}, x_s)[w,w]
    S = np.zeros((T * nw, T * nw))
    for a in range(T):
        for b in range(T):
            k = a - b
            S[a * nw:(a + 1) * nw, b * nw:(b + 1) * nw] = Cw[k] if k >= 0 else Cw[-k].T
    K = np.zeros((len(ia), T * nw))
    for a in range(T):
        s = a - L
        C = APs[-s] if s <= 0 else APs[s].T  # Cov(x_0, x_s)
        K[:, a * nw:(a + 1) * nw] = C[np.ix_(ia, iw)]
    Sig0 = P[np.ix_(ia, ia)]
    cf = cho_factor(S)
    Sc = Sig0 - K @ cho_solve(cf, K.T)
    return 0.5 * (Sc + Sc.T)


def diffusivity(Pi: np.ndarray, tol: float = 1e-12) -> dict:
    r"""Diffusive (eq:col-diffusive): off-diagonal entries <= 0 and row sums >= 0."""
    off = Pi - np.diag(np.diag(Pi))
    rows = Pi.sum(axis=1)
    scale = np.max(np.abs(np.diag(Pi)))
    return {
        "max_offdiag": float(off.max()),
        "min_rowsum": float(rows.min()),
        "diffusive": bool(off.max() <= tol * scale and rows.min() >= -tol * scale),
    }


def contrast(Pi: np.ndarray, C: list[int]) -> dict:
    r"""Rates and contrast of def:col-contrast for a diffusive precision Pi and region C.

    x_out = phi^T Pi phi, x_in = min_{f perp 1_C} f^T (diag(eps)+L_C) f / f^T f, r = x_in / x_out.
    """
    N = Pi.shape[0]
    C = list(C)
    n = len(C)
    eps = Pi.sum(axis=1)
    a = -(Pi - np.diag(np.diag(Pi)))
    out = [k for k in range(N) if k not in C]
    cut_i = a[np.ix_(C, out)].sum(axis=1) if out else np.zeros(n)
    M = Pi[np.ix_(C, C)] - np.diag(cut_i)
    phi = np.ones(n) / np.sqrt(n)
    xout = float(phi @ Pi[np.ix_(C, C)] @ phi)
    # orthonormal basis of 1^perp
    Z = np.linalg.qr(np.column_stack([phi, np.random.default_rng(0).standard_normal((n, n - 1))]))[0][:, 1:]
    xin = float(np.linalg.eigvalsh(Z.T @ M @ Z).min())
    return {"xout": xout, "xin": xin, "r": xin / xout, "eps_C": eps[C], "cut": float(cut_i.sum())}


def riccati_scalar(F: float, Q: float, info: float) -> tuple[float, float]:
    r"""Steady-state scalar Kalman: P^- = F^2 P^+ + Q, 1/P^+ = 1/P^- + info. Returns (P^-, P^+)."""
    Pm = Q
    for _ in range(100000):
        Pp = 1.0 / (1.0 / Pm + info)
        Pm_new = F * F * Pp + Q
        if abs(Pm_new - Pm) < 1e-15:
            Pm = Pm_new
            break
        Pm = Pm_new
    Pp = 1.0 / (1.0 / Pm + info)
    return Pm, Pp


def build_population(spec: dict) -> dict:
    r"""Build (A, Qx, iw, ia) for a linear-Gaussian population with raw-data relays and acts.

    spec keys:
      F (Kw,), Qw (Kw,): world AR coefficients and innovation variances (independent components).
      comp (N,): component sensed and believed by each agent.
      R (N,): sensing noise variances.
      reads: list of lists, reads[i] = agents whose raw observation i receives (receiver-specific noise Rc).
      Rc: relay noise variance.
      act_comp (N,): component each agent acts on (-1 for no act); gain g (N,) with u_i = -g_i m_i^+.
      b: act loading (scalar, same for all).
      known: list of sets, known[i] = agents whose realized acts i reads exactly (A1 within that set).
      model_unknown: if True, agent i models an unknown act u_j on its own component as -g_j m_i^+.
      gains: optional dict i -> (k_s, {j: k_ij}) to override the exact steady-state Kalman gains.
    Exact Kalman gains: agent i's model treats its component as AR with coefficient
      F_eff = F - b * sum_{j unknown, acting on c(i)} g_j (if model_unknown) and noise Qw,
      own observation noise R_i, relays from j (same component) with noise R_j + Rc.
    """
    F = np.asarray(spec["F"], float)
    Qw = np.asarray(spec["Qw"], float)
    comp = list(spec["comp"])
    R = np.asarray(spec["R"], float)
    reads = spec["reads"]
    Rc = float(spec["Rc"])
    act_comp = list(spec["act_comp"])
    g = np.asarray(spec["g"], float)
    b = float(spec["b"])
    known = spec["known"]
    model_unknown = spec.get("model_unknown", True)
    Kw = len(F)
    N = len(comp)
    gains = {}
    for i in range(N):
        c = comp[i]
        unk = [j for j in range(N) if act_comp[j] == c and j not in known[i] and g[j] != 0]
        Feff = F[c] - (b * sum(g[j] for j in unk) if model_unknown else 0.0)
        info = 1.0 / R[i] + sum(1.0 / (R[j] + Rc) for j in reads[i] if comp[j] == c)
        Pm, Pp = riccati_scalar(Feff, Qw[c], info)
        ks = Pp / R[i]
        kij = {j: (Pp / (R[j] + Rc) if comp[j] == c else 0.0) for j in reads[i]}
        gains[i] = (ks, kij, Feff, Pm, Pp)
    if "gains" in spec:
        for i, (ks, kij) in spec["gains"].items():
            gains[i] = (ks, kij) + gains[i][2:]
    # noise vector xi = (w (Kw), v (N), nu_edges (E))
    edges = [(i, j) for i in range(N) for j in reads[i]]
    E = len(edges)
    d = Kw + N
    m0 = Kw
    # m^+ = Cm m + Ceta eta + Dv v + Dnu nu
    Cm = np.zeros((N, N))
    Ceta = np.zeros((N, Kw))
    Dv = np.zeros((N, N))
    Dnu = np.zeros((N, E))
    for i in range(N):
        ks, kij = gains[i][0], gains[i][1]
        c = comp[i]
        tot = ks + sum(kij.values())
        Cm[i, i] = 1.0 - tot
        Ceta[i, c] += ks
        Dv[i, i] += ks
        for e_idx, (ii, j) in enumerate(edges):
            if ii == i:
                k = kij[j]
                Ceta[i, comp[j]] += k
                Dv[i, j] += k
                Dnu[i, e_idx] += k
    # acts u = -diag(g) m^+  (only for agents with act_comp >= 0)
    gv = np.array([g[j] if act_comp[j] >= 0 else 0.0 for j in range(N)])
    U_m = -np.diag(gv) @ Cm
    U_eta = -np.diag(gv) @ Ceta
    U_v = -np.diag(gv) @ Dv
    U_nu = -np.diag(gv) @ Dnu
    # world: eta' = F eta + B u + w, B[c, j] = b if act_comp[j] == c
    B = np.zeros((Kw, N))
    for j in range(N):
        if act_comp[j] >= 0 and gv[j] != 0:
            B[act_comp[j], j] = b
    # beliefs: m_i' = F_c m_i^+ + b * sum_{j in known[i], act_comp[j]==c} u_j + (model of unknown acts)
    Pm_pred = np.zeros((N, N))  # m' contribution through m^+ coefficients: m' = Pm_pred @ m^+ + Pu @ u
    Pu = np.zeros((N, N))
    for i in range(N):
        c = comp[i]
        Feff = F[c]
        if model_unknown:
            unk = [j for j in range(N) if act_comp[j] == c and j not in known[i] and gv[j] != 0]
            Feff = F[c] - b * sum(gv[j] for j in unk)
        Pm_pred[i, i] = Feff
        for j in known[i]:
            if act_comp[j] == c and gv[j] != 0:
                Pu[i, j] = b
    A = np.zeros((d, d))
    G = np.zeros((d, Kw + N + E))
    # eta block
    A[:Kw, :Kw] = np.diag(F) + B @ U_eta
    A[:Kw, m0:] = B @ U_m
    G[:Kw, :Kw] = np.diag(np.sqrt(Qw))
    G[:Kw, Kw:Kw + N] = (B @ U_v) * np.sqrt(R)[None, :]
    G[:Kw, Kw + N:] = (B @ U_nu) * np.sqrt(Rc)
    # m block: m' = Pm_pred (Cm m + Ceta eta + Dv v + Dnu nu) + Pu (U_m m + U_eta eta + U_v v + U_nu nu)
    Mm = Pm_pred @ Cm + Pu @ U_m
    Meta = Pm_pred @ Ceta + Pu @ U_eta
    Mv = Pm_pred @ Dv + Pu @ U_v
    Mnu = Pm_pred @ Dnu + Pu @ U_nu
    A[m0:, :Kw] = Meta
    A[m0:, m0:] = Mm
    G[m0:, Kw:Kw + N] = Mv * np.sqrt(R)[None, :]
    G[m0:, Kw + N:] = Mnu * np.sqrt(Rc)
    Qx = G @ G.T
    return {"A": A, "Qx": Qx, "iw": list(range(Kw)), "ia": list(range(m0, m0 + N)), "gains": gains,
            "edges": edges}


def pi_c(spec: dict, L: int = 120) -> tuple[np.ndarray, dict]:
    mod = build_population(spec)
    Sc = world_conditional_cov(mod["A"], mod["Qx"], mod["iw"], mod["ia"], L)
    return np.linalg.inv(Sc), mod


def exch_closed_form(n: int, F: float, Q: float, R: float, Rc: float, b: float, g: float) -> dict:
    r"""Closed form for one exchangeable niche (all-to-all raw relays, exact Kalman, deterministic acts
    u_j = -g m_j^+, all members read the total act exactly).

    sigma_xi^2 = (K_s + (n-1) K_c)^2 R + K_c^2 (n-1) R_c,  sigma_perp^2 = (K_s - K_c)^2 R + K_c^2 (n-1) R_c,
    c_0 = P^+/P^-, phi_cl = F - b g n, rho = c_0 phi_cl, s = sigma_xi^2 b^2 g^2 n / Q,
    v = phi_cl^2 sigma_xi^2 / sqrt((1+rho^2+s)^2 - 4 rho^2),  alpha = F^2 sigma_perp^2 / (1 - F^2 c_0^2),
    r = v / alpha.
    """
    Pm, Pp = riccati_scalar(F, Q, 1.0 / R + (n - 1) / (R + Rc))
    Ks, Kc = Pp / R, Pp / (R + Rc)
    c0 = 1 - Ks - (n - 1) * Kc
    sx = (Ks + (n - 1) * Kc) ** 2 * R + Kc ** 2 * (n - 1) * Rc
    sp = (Ks - Kc) ** 2 * R + Kc ** 2 * (n - 1) * Rc
    phi = F - b * g * n
    rho = c0 * phi
    s = sx * b * b * g * g * n / Q
    v = phi ** 2 * sx / np.sqrt((1 + rho ** 2 + s) ** 2 - 4 * rho ** 2)
    alpha = F ** 2 * sp / (1 - F ** 2 * c0 ** 2)
    return {"v": v, "alpha": alpha, "r": v / alpha, "c0": c0, "phi_cl": phi, "s": s, "sx": sx, "sp": sp,
            "Pm": Pm, "Pp": Pp, "Ks": Ks, "Kc": Kc}
