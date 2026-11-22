r"""General builder: scalar beliefs about one sensed component, raw relays with per-edge noise,
deterministic linear acts on any component, per-agent knowledge of acts and model of unknown acts.

Agent i: believes and senses component c(i) (noise R_i); reads raw relays y_ij = eta_{c(j)} + v_j + nu_ij
from j in reads[i] with noise Rc[(i,j)] (only relays of the same component carry information; the
exact filter gives zero gain to others).  Exact steady-state Kalman gains of agent i's model:
  eta_c' = Feff_i eta_c + (known acts) + w,  Feff_i = F_c - b * sum_{j unknown acting on c} mu_i g_j,
with own noise R_i and relay noises R_j + Rc_ij.
Acts: u_j = -g_j m_j^+ on component a(j) (a(j) = -1: no act).  m_i' = Feff_i m_i^+ + b sum_{j in known[i],
a(j)=c(i)} u_j.  World: eta' = F eta + B u + w.
"""
from __future__ import annotations
import numpy as np
from pc import riccati_scalar


def build(spec: dict) -> dict:
    F = np.asarray(spec["F"], float); Qw = np.asarray(spec["Qw"], float)
    comp = list(spec["comp"]); R = np.asarray(spec["R"], float)
    reads = spec["reads"]; Rc = spec["Rc"]  # dict (i,j) -> noise
    act = list(spec["act"]); g = np.asarray(spec["g"], float); b = float(spec["b"])
    known = spec["known"]; mu = spec.get("mu", [1.0] * len(comp))
    Kw = len(F); N = len(comp)
    edges = [(i, j) for i in range(N) for j in reads[i]]
    E = len(edges)
    gains = []
    for i in range(N):
        c = comp[i]
        unk = [j for j in range(N) if act[j] == c and j not in known[i] and g[j] != 0]
        Feff = F[c] - mu[i] * b * sum(g[j] for j in unk)
        info = 1.0 / R[i] + sum(1.0 / (R[j] + Rc[(i, j)]) for j in reads[i] if comp[j] == c)
        Pm, Pp = riccati_scalar(Feff, Qw[c], info)
        kij = {j: (Pp / (R[j] + Rc[(i, j)]) if comp[j] == c else 0.0) for j in reads[i]}
        gains.append((Pp / R[i], kij, Feff, Pm, Pp))
    nxi = Kw + N + E
    Cm = np.zeros((N, N)); Ceta = np.zeros((N, Kw)); D = np.zeros((N, nxi))
    for i in range(N):
        ks, kij, Feff, Pm, Pp = gains[i]
        c = comp[i]
        Cm[i, i] = 1 - ks - sum(kij.values())
        Ceta[i, c] += ks
        D[i, Kw + i] += ks * np.sqrt(R[i])
        for e, (ii, j) in enumerate(edges):
            if ii == i and kij[j] != 0:
                Ceta[i, comp[j]] += kij[j]
                D[i, Kw + j] += kij[j] * np.sqrt(R[j])
                D[i, Kw + N + e] += kij[j] * np.sqrt(Rc[(i, j)])
    gv = np.array([g[j] if act[j] >= 0 else 0.0 for j in range(N)])
    B = np.zeros((Kw, N))
    for j in range(N):
        if act[j] >= 0 and gv[j] != 0:
            B[act[j], j] = b
    # u = -diag(gv) (Cm m + Ceta eta + D xi)
    Um, Ueta, UD = -gv[:, None] * Cm, -gv[:, None] * Ceta, -gv[:, None] * D
    d = Kw + N
    A = np.zeros((d, d)); G = np.zeros((d, nxi))
    A[:Kw, :Kw] = np.diag(F) + B @ Ueta
    A[:Kw, Kw:] = B @ Um
    G[:Kw, :Kw] = np.diag(np.sqrt(Qw))
    G[:Kw, :] += B @ UD
    for i in range(N):
        c = comp[i]; Feff = gains[i][2]
        kn = [j for j in known[i] if act[j] == c and gv[j] != 0]
        A[Kw + i, Kw:] = Feff * Cm[i] + b * sum(Um[j] for j in kn) if kn else Feff * Cm[i]
        A[Kw + i, :Kw] = Feff * Ceta[i] + (b * sum(Ueta[j] for j in kn) if kn else 0)
        G[Kw + i] = Feff * D[i] + (b * sum(UD[j] for j in kn) if kn else 0)
    return {"A": A, "Qx": G @ G.T, "iw": list(range(Kw)), "ia": list(range(Kw, Kw + N)), "gains": gains}
