r"""Multi-component beliefs (generalizes lgx.build): agent i models a set M_i of world components jointly, on the
state (eta_{M,t}, eta_{M,t-1}); it senses its own component k(i) every round and reads relays of senders' raw readings
s_j(t-1) = eta^{k(j)}_{t-1} + v_j(t-1) (+ receiver-specific nu, literal latency), k(j) in M_i.  World innovations may be
correlated (full Qw).  Acts u_i = -sum_c kap_i[c] m^+_{i,(c,now)} + a_i on component Z_i with loading beta_i.
Contrast coordinate: prior error of agent i about its own component k(i).
'present' (per agent, default all True) switches the agent's relays on (exact gain) or off (own-sensor gain column
only, the zero-gain convention), for time-varying partner sequences.
Nulls: 'full', 'eff' (act effect replaced by forcing), 'lp' (relays deliver pure noise, gains kept),
'hab' (acts from habits).
"""
from __future__ import annotations

import numpy as np
import lgx


def build2(spec: dict, null: str = "full", present=None) -> dict:
    Fw = np.asarray(spec["Fw"], float); Qw = np.asarray(spec["Qw"], float)
    K = Fw.shape[0]; ag = spec["agents"]; N = len(ag); Rc = float(spec["Rc"]); qc = float(spec.get("qc", 0.0))
    if present is None:
        present = [True] * N
    Lw = np.linalg.cholesky(Qw + 1e-300 * np.eye(K)) if np.all(np.linalg.eigvalsh(Qw) > 0) else None
    if Lw is None:  # allow singular blocks: eigen-decomposition square root
        ev, U = np.linalg.eigh(Qw); Lw = U @ np.diag(np.sqrt(np.clip(ev, 0, None)))
    edges = [(i, j) for i in range(N) for j in ag[i]["senders"]]
    E = len(edges)
    dims = [2 * len(a["M"]) for a in ag]
    off = np.cumsum([0] + dims)
    i_eta = list(range(K)); i_lag = list(range(K, 2 * K))
    i_m = lambda i: list(range(2 * K + off[i], 2 * K + off[i + 1]))
    i_v = lambda j: 2 * K + off[N] + j
    d = 2 * K + off[N] + N
    nq = off[N]
    n_w = list(range(K)); n_v = lambda j: K + j; n_nu = lambda e: K + N + e
    n_qc = lambda i: list(range(K + N + E + off[i], K + N + E + off[i + 1]))
    n_a = lambda i: K + N + E + nq + i; n_f = lambda k: K + N + E + nq + N + k
    p = K + N + E + nq + N + K
    sd = np.ones(p)
    for j in range(N):
        sd[n_v(j)] = np.sqrt(ag[j]["R"])
    for e, (i, j) in enumerate(edges):
        sd[n_nu(e)] = np.sqrt(Rc) if null != "lp" else np.sqrt(ag[j]["R"] + Rc)
    for i in range(N):
        sd[n_qc(i)] = np.sqrt(qc); sd[n_a(i)] = np.sqrt(ag[i].get("sa2", 0.0))
    Mx, Mn, gains = [], [], []
    for i in range(N):
        a = ag[i]; M = list(a["M"]); m = len(M)
        FM = Fw[np.ix_(M, M)]
        AF = np.block([[FM, np.zeros((m, m))], [np.eye(m), np.zeros((m, m))]])
        Qp = np.block([[Qw[np.ix_(M, M)], np.zeros((m, m))], [np.zeros((m, m)), np.zeros((m, m))]]) + qc * np.eye(2 * m)
        rows = [np.eye(2 * m)[M.index(a["k"])]] + [np.eye(2 * m)[m + M.index(ag[j]["k"])] for j in a["senders"]]
        H = np.array(rows)
        Rm = np.diag([a["R"]] + [ag[j]["R"] + Rc for j in a["senders"]])
        P = lgx.riccati_prior(AF, Qp, H, Rm)
        Kg = P @ H.T @ np.linalg.inv(H @ P @ H.T + Rm)
        gains.append({"P": P, "K": Kg, "H": H, "AF": AF, "M": M})
        nobs = 1 + len(a["senders"])
        ox = np.zeros((nobs, d)); on = np.zeros((nobs, p))
        ox[0, i_eta[a["k"]]] = 1.0; on[0, n_v(i)] = 1.0
        for r, j in enumerate(a["senders"]):
            e = edges.index((i, j))
            if null == "lp":
                on[1 + r, n_nu(e)] = 1.0
            else:
                ox[1 + r, i_lag[ag[j]["k"]]] = 1.0; ox[1 + r, i_v(j)] = 1.0; on[1 + r, n_nu(e)] = 1.0
        mx = np.zeros((2 * m, d)); mx[:, i_m(i)] = np.eye(2 * m)
        Kuse = Kg.copy()
        if not present[i]:
            Kuse[:, 1:] = 0.0
        Mx.append(mx + Kuse @ (ox - H @ mx)); Mn.append(Kuse @ on)
    Ux = np.zeros((N, d)); Un = np.zeros((N, p))
    for i in range(N):
        a = ag[i]
        if a.get("Z", -1) < 0:
            continue
        if null != "hab":
            for c, kc in a.get("kap", {}).items():
                r = a["M"].index(c)
                Ux[i] -= kc * Mx[i][r]; Un[i] -= kc * Mn[i][r]
        Un[i, n_a(i)] += 1.0
    A = np.zeros((d, d)); G = np.zeros((d, p))
    A[np.ix_(i_eta, i_eta)] = Fw
    G[np.ix_(i_eta, n_w)] = Lw
    acted = set()
    for i in range(N):
        Z = ag[i].get("Z", -1)
        if Z < 0:
            continue
        acted.add(Z)
        if null != "eff":
            A[Z] += ag[i]["beta"] * Ux[i]; G[Z] += ag[i]["beta"] * Un[i]
    if null == "eff":
        for k in acted:
            G[k, n_f(k)] = 1.0
    A[i_lag, i_eta] = 1.0
    for i in range(N):
        rows = i_m(i)
        A[rows] = gains[i]["AF"] @ Mx[i]; G[rows] = gains[i]["AF"] @ Mn[i]
        G[np.ix_(rows, n_qc(i))] += np.eye(len(rows))
    for j in range(N):
        G[i_v(j), n_v(j)] = 1.0
    Gs = G * sd[None, :]
    ia = [i_m(i)[ag[i]["M"].index(ag[i]["k"])] for i in range(N)]
    priv = [x for i in range(N) for x in i_m(i)] + [i_v(j) for j in range(N)]
    npriv = [n_v(j) for j in range(N)] + [n_nu(e) for e in range(E)] + [x for i in range(N) for x in n_qc(i)] \
        + [n_a(i) for i in range(N)]
    return {"A": A, "Qx": Gs @ Gs.T, "G": Gs, "iw": i_eta, "ia": ia, "gains": gains, "d": d, "p": p, "K": K,
            "N": N, "Ux": Ux, "Un": Un, "sd": sd, "n_a": [n_a(i) for i in range(N)], "private_idx": priv,
            "noise_private": npriv, "i_m": i_m}


def sigma_c2(spec, null="full", L=40):
    mod = build2(spec, null)
    return lgx.window_cond_cov(mod["A"], mod["Qx"], mod["iw"], mod["ia"], L)


def sigma_private2(spec, null="eff"):
    mod = build2(spec, null)
    idx = mod["private_idx"]
    A = mod["A"][np.ix_(idx, idx)]; Gp = mod["G"][np.ix_(idx, mod["noise_private"])]
    P = lgx.stat_cov(A, Gp @ Gp.T)
    sel = [idx.index(i) for i in mod["ia"]]
    return P[np.ix_(sel, sel)]


def annealed_pr(spec, rel_prob, nseq, seed, T=70, tstar=45, null="full"):
    r"""Annealed second moment under partner randomization with the zero-gain convention: each round each agent's relay
    is present with probability rel_prob (its mate drawn), else absent; exact row propagation per sequence; mixture part
    as in round-1 attack A8 (P(seq | eta) ~ P(seq))."""
    rng = np.random.default_rng(seed)
    N = len(spec["agents"])
    cache = {}

    def mats(pat):
        if pat not in cache:
            mod = build2(spec, null, present=list(pat))
            cache[pat] = (mod["A"], mod["G"], mod["iw"], mod["ia"], mod["d"], mod["p"])
        return cache[pat]

    A0, G0, iw, ia, d, p = mats(tuple([True] * N))
    P0 = lgx.stat_cov(A0, G0 @ G0.T)
    L0 = np.linalg.cholesky(P0 + 1e-14 * np.eye(d))
    covs, Ks, Gs = [], [], []
    for _ in range(nseq):
        ncol = d + p * T
        X = np.zeros((d, ncol)); X[:, :d] = L0          # stationary start of the full-schedule law
        H = [X[iw]]; Erows = None
        for t in range(T):
            pat = tuple(bool(x) for x in (rng.random(N) < rel_prob))
            A, G, *_ = mats(pat)
            if t == tstar:
                Erows = X[ia] - X[[0]] * 0  # prior means; errors differ by eta rows (removed by conditioning)
                Erows = X[ia] - np.array([X[iw][spec["agents"][i]["k"]] for i in range(N)])
            Xn = A @ X
            Xn[:, d + p * t: d + p * (t + 1)] += G
            X = Xn
            H.append(X[iw])
        Hm = np.vstack(H); Gm = Hm @ Hm.T; CE = Erows @ Hm.T
        Kc = np.linalg.solve(Gm, CE.T).T
        covs.append(Erows @ Erows.T - Kc @ CE.T); Ks.append(Kc); Gs.append(Gm)
    Sg = np.mean(Gs, axis=0); Kb = np.mean(Ks, axis=0)
    mix = np.mean([k @ Sg @ k.T for k in Ks], axis=0) - Kb @ Sg @ Kb.T
    S = np.mean(covs, axis=0) + mix
    return 0.5 * (S + S.T)
