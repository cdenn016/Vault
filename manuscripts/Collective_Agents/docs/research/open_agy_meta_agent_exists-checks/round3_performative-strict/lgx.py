r"""Exact world-conditional covariances for linear-Gaussian populations with performative acts (round 3,
label performative-strict).

Conventions (record open_agy_meta_agent_exists.md, Conventions table):
  * world-conditional law (def:col-world-conditional, 04_collectives.tex:130-132): conditional law of the agents'
    errors given the whole world path; every relay noise here is receiver-specific and an agent's own sensing noise is
    a private input even when relayed, so no channel noise is added to the conditioning set;
  * contrast coordinates: prior errors e_i(t) = m^-_{i,0}(t) - eta^{k(i)}_t (as in instance I*); given the path,
    Cov(e | eta) = Cov(m^-_{.,0} | eta);
  * literal one-round latency of def:fw-system (02_framework.tex:15): a relay of s_j(t-1) is read at round t;
  * exact steady-state Kalman filters on (eta_t, eta_{t-1}) with computation noise qc I_2 added to the predicted mean
    and included in P^- (instance-I* convention).

Full state X_t = (eta_t [K], eta_{t-1} [K], m^-_i(t) [2 per agent], v_j(t-1) [1 per agent]).
Round-t noises xi_t = (w [K], v [N], nu [E edges], qcn [2N], a [N act noise], f [K exogenous forcing, N_eff]).

Model of one round:
  s_i(t) = eta^{k(i)}_t + v_i(t);  y_ij(t) = eta^{k(j)}_{t-1} + v_j(t-1) + nu_ij(t)   (j in senders(i));
  m^+_i = m^-_i + K_i (o_i - H_i m^-_i);
  u_i(t) = -kappa_i m^+_{i,0}(t) + a_i(t)            (acting agents; kappa signed);
  eta_{t+1} = Fw eta_t + sum_i beta_i e_{Z(i)} u_i(t) + w_t;
  m^-_i(t+1) = A_F m^+_i + e_0 sum_{j in readacts(i)} beta_j u_j(t) + qcn_i,  A_F = [[F_k, 0], [1, 0]].
Nulls (def:agy-nulls, tab:agy-nulls 05_agency.tex:332-360):
  'eff' : each act's effect on eta replaced by exogenous forcing f (independent of every private input); agents'
          update rules, including the use of realized acts they read, are unchanged;
  'lp'  : each relay delivers pure noise of variance R_j + Rc; gains kept;
  'hab' : gamma = 0, acts drawn from habits: u_i = a_i (no belief dependence).
"""
from __future__ import annotations

import os
for _v in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS"):
    os.environ.setdefault(_v, "1")
from itertools import combinations

import numpy as np
from scipy.linalg import solve_discrete_lyapunov, cho_factor, cho_solve


# ----------------------------------------------------------------------------------------------------------------
# generic linear algebra
# ----------------------------------------------------------------------------------------------------------------
def stat_cov(A: np.ndarray, Qx: np.ndarray) -> np.ndarray:
    r"""Stationary covariance P = A P A^T + Qx (requires rho(A) < 1)."""
    rho = max(abs(np.linalg.eigvals(A))) if A.size else 0.0
    if rho >= 1:
        raise ValueError(f"unstable, rho={rho}")
    P = solve_discrete_lyapunov(A, Qx)
    return 0.5 * (P + P.T)


def window_cond_cov(A: np.ndarray, Qx: np.ndarray, iw: list[int], ia: list[int], L: int) -> np.ndarray:
    r"""Cov(x_0[ia] | x_s[iw], s = -L..L) for the stationary process x_{t+1} = A x_t + noise(Qx).

    Uses Cov(x_{s+k}, x_s) = A^k P (k >= 0).  Exact Gaussian conditioning on a two-sided window.
    """
    P = stat_cov(A, Qx)
    T = 2 * L + 1
    nw = len(iw)
    APs = [P]
    for _ in range(2 * L):
        APs.append(A @ APs[-1])
    Cw = [M[np.ix_(iw, iw)] for M in APs]
    S = np.zeros((T * nw, T * nw))
    for a in range(T):
        for b in range(T):
            k = a - b
            S[a * nw:(a + 1) * nw, b * nw:(b + 1) * nw] = Cw[k] if k >= 0 else Cw[-k].T
    Kc = np.zeros((len(ia), T * nw))
    for a in range(T):
        s = a - L
        C = APs[-s] if s <= 0 else APs[s].T  # Cov(x_0, x_s)
        Kc[:, a * nw:(a + 1) * nw] = C[np.ix_(ia, iw)]
    cf = cho_factor(S)
    Sc = P[np.ix_(ia, ia)] - Kc @ cho_solve(cf, Kc.T)
    return 0.5 * (Sc + Sc.T)


def riccati_prior(AF: np.ndarray, Qp: np.ndarray, H: np.ndarray, Rm: np.ndarray, iters: int = 100000) -> np.ndarray:
    r"""Steady-state prior covariance P^- of the Kalman filter x' = AF x + q (Qp), o = H x + r (Rm)."""
    P = Qp.copy() + np.eye(AF.shape[0]) * 1e-6
    for _ in range(iters):
        S = H @ P @ H.T + Rm
        Pp = P - P @ H.T @ np.linalg.solve(S, H @ P)
        Pn = AF @ Pp @ AF.T + Qp
        if np.max(np.abs(Pn - P)) < 1e-15:
            P = Pn
            break
        P = Pn
    return 0.5 * (P + P.T)


# ----------------------------------------------------------------------------------------------------------------
# population builder
# ----------------------------------------------------------------------------------------------------------------
def build(spec: dict, null: str = "full") -> dict:
    r"""Linear system X_{t+1} = A X_t + G xi_t for a population spec under a null ('full', 'eff', 'lp', 'hab').

    spec keys:
      Fw (K x K) exogenous world transition; Qw (K,) innovation variances (independent components);
      Rc relay noise; qc computation noise; agents: list of dicts with keys
        k (component sensed/modeled), R (sensing noise), senders (list of agents whose raw reading it relays-in),
        kappa (signed act gain, 0 for no act), Z (acted component or -1), beta (act loading), sa2 (act noise var),
        readacts (list of agents whose realized acts it adds to its prediction of its own component).
      Agents model their component k as AR(1) with coefficient Fw[k,k] and innovation Qw[k].
    """
    Fw = np.asarray(spec["Fw"], float)
    Qw = np.asarray(spec["Qw"], float)
    K = len(Qw)
    ag = spec["agents"]
    N = len(ag)
    Rc = float(spec["Rc"])
    qc = float(spec.get("qc", 0.0))
    edges = [(i, j) for i in range(N) for j in ag[i]["senders"]]
    E = len(edges)
    # state indices
    i_eta = list(range(K))
    i_lag = list(range(K, 2 * K))
    i_m = lambda i: (2 * K + 2 * i, 2 * K + 2 * i + 1)
    i_v = lambda j: 2 * K + 2 * N + j
    d = 2 * K + 3 * N
    # noise indices
    n_w = list(range(K))
    n_v = lambda j: K + j
    n_nu = lambda e: K + N + e
    n_qc = lambda i: (K + N + E + 2 * i, K + N + E + 2 * i + 1)
    n_a = lambda i: K + N + E + 2 * N + i
    n_f = lambda k: K + N + E + 3 * N + k
    p = K + N + E + 3 * N + K
    sd = np.zeros(p)
    sd[n_w] = np.sqrt(Qw)
    for j in range(N):
        sd[n_v(j)] = np.sqrt(ag[j]["R"])
    for e, (i, j) in enumerate(edges):
        sd[n_nu(e)] = np.sqrt(Rc) if null != "lp" else np.sqrt(ag[j]["R"] + Rc)
    for i in range(N):
        sd[list(n_qc(i))] = np.sqrt(qc)
        sd[n_a(i)] = np.sqrt(ag[i].get("sa2", 0.0))
    for k in range(K):
        sd[n_f(k)] = 1.0  # exogenous forcing scale (irrelevant for the world-conditional covariance)
    gains = []
    # posterior m^+_i = Mx_i X + Mn_i xi  (2 x d, 2 x p)
    Mx = []
    Mn = []
    for i in range(N):
        a = ag[i]
        k = a["k"]
        AF = np.array([[Fw[k, k], 0.0], [1.0, 0.0]])
        Qp = np.diag([Qw[k], 0.0]) + qc * np.eye(2)
        snd = a["senders"]
        for j in snd:
            assert ag[j]["k"] == k, "relays only between agents modeling the same component"
        H = np.array([[1.0, 0.0]] + [[0.0, 1.0]] * len(snd))
        Rm = np.diag([a["R"]] + [ag[j]["R"] + Rc for j in snd])
        P = riccati_prior(AF, Qp, H, Rm)
        Kg = P @ H.T @ np.linalg.inv(H @ P @ H.T + Rm)  # 2 x (1+len(snd))
        gains.append({"P": P, "K": Kg, "H": H, "Rm": Rm, "AF": AF})
        # innovation o - H m^-: rows as linear maps
        ox = np.zeros((1 + len(snd), d))
        on = np.zeros((1 + len(snd), p))
        ox[0, i_eta[k]] = 1.0
        on[0, n_v(i)] = 1.0
        for r, j in enumerate(snd):
            e = edges.index((i, j))
            if null == "lp":
                on[1 + r, n_nu(e)] = 1.0
            else:
                ox[1 + r, i_lag[k]] = 1.0
                ox[1 + r, i_v(j)] = 1.0
                on[1 + r, n_nu(e)] = 1.0
        mx = np.zeros((2, d))
        mx[:, list(i_m(i))] = np.eye(2)
        Mx.append(mx + Kg @ (ox - H @ mx))
        Mn.append(Kg @ on)
    # acts u_i = Ux_i X + Un_i xi
    Ux = np.zeros((N, d))
    Un = np.zeros((N, p))
    for i in range(N):
        kap = ag[i].get("kappa", 0.0)
        if ag[i].get("Z", -1) < 0:
            continue
        if null != "hab":
            Ux[i] = -kap * Mx[i][0]
            Un[i] = -kap * Mn[i][0]
        Un[i, n_a(i)] += 1.0
    A = np.zeros((d, d))
    G = np.zeros((d, p))
    # world
    A[np.ix_(i_eta, i_eta)] = Fw
    G[i_eta, n_w] = 1.0
    for i in range(N):
        Z = ag[i].get("Z", -1)
        if Z < 0:
            continue
        b = ag[i]["beta"]
        if null == "eff":
            G[Z, n_f(Z)] += 0.0  # forcing added below once per component
        else:
            A[Z] += b * Ux[i]
            G[Z] += b * Un[i]
    if null == "eff":
        for k in range(K):
            if any(ag[i].get("Z", -1) == k for i in range(N)):
                G[k, n_f(k)] = 1.0
    # lag
    A[i_lag, i_eta] = 1.0
    # beliefs
    for i in range(N):
        AF = gains[i]["AF"]
        rows = list(i_m(i))
        A[rows] = AF @ Mx[i]
        G[rows] = AF @ Mn[i]
        for j in ag[i].get("readacts", []):
            A[rows[0]] += ag[j]["beta"] * Ux[j]
            G[rows[0]] += ag[j]["beta"] * Un[j]
        G[rows[0], n_qc(i)[0]] += 1.0
        G[rows[1], n_qc(i)[1]] += 1.0
    # lagged sensing noise
    for j in range(N):
        G[i_v(j), n_v(j)] = 1.0
    Gs = G * sd[None, :]
    return {"A": A, "Qx": Gs @ Gs.T, "G": Gs, "iw": i_eta, "ia": [i_m(i)[0] for i in range(N)], "gains": gains,
            "edges": edges, "d": d, "K": K, "N": N, "Ux": Ux, "Un": Un, "sd": sd,
            "n_a": [n_a(i) for i in range(N)],
            "private_idx": [x for i in range(N) for x in i_m(i)] + [i_v(j) for j in range(N)],
            "noise_private": [n_v(j) for j in range(N)] + [n_nu(e) for e in range(E)]
                             + [x for i in range(N) for x in n_qc(i)] + [n_a(i) for i in range(N)]}


def sigma_c(spec: dict, null: str = "full", L: int = 60) -> np.ndarray:
    r"""World-conditional covariance of the prior errors (N x N) by exact two-sided window conditioning."""
    mod = build(spec, null)
    return window_cond_cov(mod["A"], mod["Qx"], mod["iw"], mod["ia"], L)


def sigma_private(spec: dict, null: str = "full") -> np.ndarray:
    r"""Stationary covariance of the private-noise response of the agents' states (the N_eff law, Lemma M):
    the agents' block of A with the world coordinates removed, driven by private noises only."""
    mod = build(spec, null)
    idx = mod["private_idx"]
    A = mod["A"][np.ix_(idx, idx)]
    Gp = mod["G"][np.ix_(idx, mod["noise_private"])]
    P = stat_cov(A, Gp @ Gp.T)
    sel = [idx.index(i) for i in mod["ia"]]
    return P[np.ix_(sel, sel)]


# ----------------------------------------------------------------------------------------------------------------
# contrast tools (def:col-contrast 04_collectives.tex:182-188, def:col-baseline :197-209, def:col-collective :214-221)
# ----------------------------------------------------------------------------------------------------------------
def diffusivity(Pi: np.ndarray, tol: float = 1e-10) -> dict:
    off = Pi - np.diag(np.diag(Pi))
    rows = Pi.sum(axis=1)
    sc = np.max(np.abs(np.diag(Pi)))
    return {"max_off": float(off.max()), "min_row": float(rows.min()),
            "diffusive": bool(off.max() <= tol * sc and rows.min() >= -tol * sc)}


def contrast(Pi: np.ndarray, C) -> dict:
    r"""x_out = phi^T Pi phi; x_in = min_{f perp 1_C, supp f in C} f^T (diag(eps) + L_C) f / f^T f; r = x_in/x_out."""
    N = Pi.shape[0]
    C = list(C)
    n = len(C)
    a = -(Pi - np.diag(np.diag(Pi)))
    out = [k for k in range(N) if k not in C]
    cut_i = a[np.ix_(C, out)].sum(axis=1) if out else np.zeros(n)
    M = Pi[np.ix_(C, C)] - np.diag(cut_i)
    phi = np.ones(n) / np.sqrt(n)
    xout = float(phi @ Pi[np.ix_(C, C)] @ phi)
    Zb = np.linalg.svd(np.eye(n) - np.outer(phi, phi))[0][:, :n - 1]
    xin = float(np.linalg.eigvalsh(Zb.T @ M @ Zb).min())
    eps = Pi.sum(axis=1)[C]
    return {"xout": xout, "xin": xin, "r": xin / xout, "leak_ratio": float(eps.max() / eps.mean()),
            "cut": float(cut_i.sum())}


def all_regions(Pi: np.ndarray, top: int = 10) -> list:
    r"""Contrast of every region of size >= 2 (sorted, descending)."""
    N = Pi.shape[0]
    res = []
    for m in range(2, N + 1):
        for C in combinations(range(N), m):
            c = contrast(Pi, C)
            res.append((c["r"], C, c["leak_ratio"]))
    res.sort(key=lambda x: -x[0])
    return res[:top] if top else res


def baseline_mean_coupling(Pi: np.ndarray) -> float:
    r"""Clause (c) of def:col-baseline with the mean coupling: exchangeable medium of the same size N with coupling
    abar = mean_{i<j} a_ij and uniform leak epsbar; with uniform leak the supremum is attained by the whole medium,
    rbar = 1 + N abar / epsbar (record, Conventions)."""
    N = Pi.shape[0]
    a = -(Pi - np.diag(np.diag(Pi)))
    abar = a[np.triu_indices(N, 1)].mean()
    epsbar = Pi.sum(axis=1).mean()
    return 1.0 + N * abar / epsbar


def selected(Pi: np.ndarray, r0: float, rbar: float) -> list:
    r"""Regions that are collectives at level r0 (r(C) >= r0, r0 > max(leak ratio, rbar)); requires diffusive Pi."""
    if not diffusivity(Pi)["diffusive"]:
        return ["NON-DIFFUSIVE"]
    if r0 <= rbar:
        return ["INADMISSIBLE r0"]
    out = []
    for r, C, lr in all_regions(Pi, top=0):
        if r >= r0 and r0 > lr:
            out.append(C)
    return out


def loewner_gap(S_big: np.ndarray, S_small: np.ndarray) -> float:
    r"""Smallest eigenvalue of S_big - S_small (>= 0 means S_small <= S_big in Loewner order)."""
    D = S_big - S_small
    return float(np.linalg.eigvalsh(0.5 * (D + D.T)).min())
