r"""Independent reconstruction of the audience instance P0 (and helpers) from the
candidate's Section 1 specification only.  Written without reading the
investigator's code.

Model (Section 1 of the candidate):
  world   eta_{t+1} = F eta_t + w_t,  w ~ N(0,Q)
  agents filter x_t = (eta_t, eta_{t-1}) exactly; computation noise qc*I_2 is
  added to predicted means and included in P^-.
  S: own sensor noise R_S, reads nothing.  members: own sensor noise R, read one
  channel among {none, S, mates} (kappa_msg = 1) chosen by EFE at precision gamma.
  broadcast u_a(t) = s_a(t); channel y_ij(t+1) = u_j(t) + nu_ij(t+1), nu ~ N(0,R_c).
  contrast coordinate e_a(t) = m^-_{a,0}(t) - eta_t.
"""
from __future__ import annotations

import itertools
import numpy as np
from scipy.linalg import solve_discrete_lyapunov

AF = lambda F: np.array([[F, 0.0], [1.0, 0.0]])


def riccati_fixed(F: float, Q: float, qc: float, H: np.ndarray, Rm: np.ndarray,
                  iters: int = 5000) -> tuple[np.ndarray, np.ndarray]:
    r"""Stationary predicted covariance P^- and posterior P^+ of the 2-state filter.

    P^+ = ((P^-)^{-1} + H^T R^{-1} H)^{-1},  P^-_{next} = A P^+ A^T + diag(Q,0) + qc I.
    """
    A = AF(F)
    Qx = np.diag([Q, 0.0]) + qc * np.eye(2)
    Pm = np.eye(2)
    Ri = np.linalg.inv(Rm)
    for _ in range(iters):
        Pp = np.linalg.inv(np.linalg.inv(Pm) + H.T @ Ri @ H)
        Pn = A @ Pp @ A.T + Qx
        if np.max(np.abs(Pn - Pm)) < 1e-17:
            Pm = Pn
            break
        Pm = Pn
    Pp = np.linalg.inv(np.linalg.inv(Pm) + H.T @ Ri @ H)
    return Pm, Pp


def info_gain(Pm: np.ndarray, H: np.ndarray, Rm: np.ndarray) -> float:
    r"""I(x; z) = 1/2 ln det(I + P^- H^T R^{-1} H) for z = Hx + N(0,R)."""
    M = np.eye(Pm.shape[0]) + Pm @ H.T @ np.linalg.inv(Rm) @ H
    return 0.5 * np.log(np.linalg.det(M))


def diffusive_parts(Pi: np.ndarray) -> tuple[np.ndarray, np.ndarray, float, float]:
    """couplings a_ij = -Pi_ij, leaks eps_i = row sums; returns max offdiag, min rowsum."""
    N = Pi.shape[0]
    a = -Pi.copy()
    np.fill_diagonal(a, 0.0)
    eps = Pi.sum(axis=1)
    off = Pi[~np.eye(N, dtype=bool)]
    return a, eps, float(off.max()), float(eps.min())


def contrast(Pi: np.ndarray, C: list[int]) -> float:
    r"""r(C) = xi_in/xi_out per def:col-contrast (04_collectives.tex:182-188).

    xi_out = phi^T Pi phi, phi = 1_C/sqrt(n);
    xi_in = min_{f perp 1_C, supp f in C} f^T (diag(eps)+L_C) f / f^T f.
    """
    a, eps, _, _ = diffusive_parts(Pi)
    n = len(C)
    phi = np.zeros(Pi.shape[0])
    phi[C] = 1.0 / np.sqrt(n)
    xo = phi @ Pi @ phi
    aC = a[np.ix_(C, C)]
    LC = np.diag(aC.sum(axis=1)) - aC
    B = np.diag(eps[C]) + LC
    # orthonormal basis of 1^perp in R^n
    Qb, _ = np.linalg.qr(np.column_stack([np.ones(n), np.eye(n)[:, : n - 1]]))
    U = Qb[:, 1:n]
    xi = np.linalg.eigvalsh(U.T @ B @ U).min()
    return float(xi / xo)


def all_regions(N: int) -> list[list[int]]:
    out = []
    for k in range(2, N + 1):
        out += [list(c) for c in itertools.combinations(range(N), k)]
    return out


def mean_coupling_baseline(Pi: np.ndarray) -> float:
    r"""Clause (c) with mean coupling: exchangeable medium, a-bar on every pair,
    uniform leak eps-bar; sup over all regions, computed by enumeration."""
    N = Pi.shape[0]
    a, eps, _, _ = diffusive_parts(Pi)
    abar = a[np.triu_indices(N, 1)].mean()
    ebar = eps.mean()
    Pm = -abar * np.ones((N, N))
    np.fill_diagonal(Pm, ebar + (N - 1) * abar)
    return max(contrast(Pm, C) for C in all_regions(N))


def perm_average(Sig: np.ndarray) -> np.ndarray:
    N = Sig.shape[0]
    acc = np.zeros_like(Sig)
    cnt = 0
    for p in itertools.permutations(range(N)):
        P = np.eye(N)[list(p)]
        acc += P @ Sig @ P.T
        cnt += 1
    return acc / cnt


class P0Model:
    r"""Stationary model with deterministic attention profile (each member reads
    the channel `reads[i]` every round; 'S' = source, None = nothing).

    Augmented error state Z(t) = [eps_S(2), eps_1(2),...,eps_n(2), v_S(t-1)].
    """

    def __init__(self, F=0.9, Q=0.05, R=1.0, RS=0.01, Rc=0.002, qc=1e-4, n=4, gamma=40.0):
        self.F, self.Q, self.R, self.RS, self.Rc, self.qc, self.n, self.gamma = F, Q, R, RS, Rc, qc, n, gamma
        A = AF(F)
        # source filter
        HS = np.array([[1.0, 0.0]])
        self.PmS, self.PpS = riccati_fixed(F, Q, qc, HS, np.array([[RS]]))
        self.KS = self.PpS @ HS.T / RS  # P^+ H^T R^{-1}
        self.MS = A @ self.PpS @ np.linalg.inv(self.PmS)
        # member filter reading S every round
        Hm = np.eye(2)
        Rm = np.diag([R, RS + Rc])
        self.Pm, self.Pp = riccati_fixed(F, Q, qc, Hm, Rm)
        self.Km = self.Pp @ Hm.T @ np.linalg.inv(Rm)  # 2x2: columns (own sensor, channel)
        self.Mm = A @ self.Pp @ np.linalg.inv(self.Pm)

    # ---------------- EFE of a member at the stationary state ----------------
    def efe_options(self) -> dict:
        r"""G_i(J) = -I(x_{t+1}; own sensor, channels in J) at the member's P^-."""
        Pm = self.Pm
        out = {}
        h_own = np.array([[1.0, 0.0]])
        opts = {"none": None, "S": self.RS + self.Rc, "mate": self.R + self.Rc}
        for k, rch in opts.items():
            if rch is None:
                H = h_own
                Rm = np.array([[self.R]])
            else:
                H = np.vstack([h_own, [[0.0, 1.0]]])
                Rm = np.diag([self.R, rch])
            out[k] = -info_gain(Pm, H, Rm)
        return out

    def policy_probs(self) -> dict:
        G = self.efe_options()
        # options: none, S, m1, m2, m3 (n-1 mates)
        names = ["none", "S"] + [f"m{j}" for j in range(1, self.n)]
        Gv = np.array([G["none"], G["S"]] + [G["mate"]] * (self.n - 1))
        lw = -self.gamma * Gv
        lw -= lw.max()
        p = np.exp(lw)
        p /= p.sum()
        return dict(zip(names, p)), dict(zip(names, Gv))

    # ---------------- world-conditional covariance ----------------
    def system(self, include_world: bool = False):
        n = self.n
        A = AF(self.F)
        dimZ = 2 + 2 * n + 1
        iv = dimZ - 1  # index of v_S(t-1)
        T = np.zeros((dimZ, dimZ))
        T[0:2, 0:2] = self.MS
        for i in range(n):
            s = 2 + 2 * i
            T[s:s + 2, s:s + 2] = self.Mm
            T[s:s + 2, iv] = (A @ self.Km)[:, 1]  # v_S(t-1) enters via channel column
        # noises: v_S, v_1..v_n, nu_1..nu_n, nS(2), n_1..n_n (2 each), [w]
        cols = []
        var = []
        # v_S(t)
        g = np.zeros(dimZ)
        g[0:2] = (A @ self.KS)[:, 0]
        g[iv] = 1.0
        cols.append(g); var.append(self.RS)
        for i in range(n):  # own sensor
            g = np.zeros(dimZ); s = 2 + 2 * i
            g[s:s + 2] = (A @ self.Km)[:, 0]
            cols.append(g); var.append(self.R)
        for i in range(n):  # channel noise nu_iS
            g = np.zeros(dimZ); s = 2 + 2 * i
            g[s:s + 2] = (A @ self.Km)[:, 1]
            cols.append(g); var.append(self.Rc)
        for a in range(n + 1):  # computation noise
            for c in range(2):
                g = np.zeros(dimZ); g[2 * a + c] = 1.0
                cols.append(g); var.append(self.qc)
        if include_world:
            g = np.zeros(dimZ)
            for a in range(n + 1):
                g[2 * a] = -1.0
            cols.append(g); var.append(self.Q)
        G = np.column_stack(cols)
        W = G @ np.diag(var) @ G.T
        return T, W

    def sigma_c(self) -> np.ndarray:
        T, W = self.system(include_world=False)
        SZ = solve_discrete_lyapunov(T, W)
        idx = [2 * a for a in range(self.n + 1)]
        return SZ[np.ix_(idx, idx)]


def fixed_schedule_sigma(reads: list, F=0.9, Q=0.05, R=1.0, RS=0.01, Rc=0.002, qc=1e-4,
                         include_world: bool = False, cond_vS: bool = False):
    r"""World-conditional covariance of prior errors for a fixed attention map.

    Agents: 0 = S (reads nothing, sensor RS); 1..n members (sensor R).
    reads[i-1] in {None, 0, 1..n}: the agent member i reads every round (one channel).
    Every agent broadcasts its raw reading; the channel to i from j carries
    v_j(t-1) + nu_ij(t), read with claimed noise R_j + Rc (exact for i).
    Augmented state: [eps_0..eps_n (2 each), vlag_0..vlag_n].
    Returns (Sigma_c on prior errors, filters dict).
    """
    n = len(reads)
    N = n + 1
    A = AF(F)
    Rsen = [RS] + [R] * n
    filt = []
    for a in range(N):
        src = None if a == 0 else reads[a - 1]
        if src is None:
            H = np.array([[1.0, 0.0]]); Rm = np.array([[Rsen[a]]])
        else:
            H = np.eye(2); Rm = np.diag([Rsen[a], Rsen[src] + Rc])
        Pm, Pp = riccati_fixed(F, Q, qc, H, Rm)
        K = Pp @ H.T @ np.linalg.inv(Rm)
        M = A @ Pp @ np.linalg.inv(Pm)
        filt.append(dict(src=src, Pm=Pm, Pp=Pp, K=K, M=M))
    dimZ = 2 * N + N
    vl = lambda j: 2 * N + j
    T = np.zeros((dimZ, dimZ))
    cols, var = [], []
    for a in range(N):
        f = filt[a]
        T[2 * a:2 * a + 2, 2 * a:2 * a + 2] = f["M"]
        if f["src"] is not None:
            T[2 * a:2 * a + 2, vl(f["src"])] = (A @ f["K"])[:, 1]
    for a in range(N):  # own sensing noise v_a(t): enters eps_a(t+1) and vlag_a(t+1)
        g = np.zeros(dimZ)
        g[2 * a:2 * a + 2] = (A @ filt[a]["K"])[:, 0]
        g[vl(a)] = 1.0
        cols.append(g); var.append(0.0 if (cond_vS and a == 0) else Rsen[a])
        if cond_vS and a == 0:
            pass
    for a in range(N):  # receiver-specific channel noise
        if filt[a]["src"] is not None:
            g = np.zeros(dimZ); g[2 * a:2 * a + 2] = (A @ filt[a]["K"])[:, 1]
            cols.append(g); var.append(Rc)
    for a in range(N):
        for c in range(2):
            g = np.zeros(dimZ); g[2 * a + c] = 1.0
            cols.append(g); var.append(qc)
    if include_world:
        g = np.zeros(dimZ)
        for a in range(N):
            g[2 * a] = -1.0
        cols.append(g); var.append(Q)
    G = np.column_stack(cols)
    W = G @ np.diag(var) @ G.T
    SZ = solve_discrete_lyapunov(T, W)
    idx = [2 * a for a in range(N)]
    return SZ[np.ix_(idx, idx)], filt
