r"""Exact world-conditional covariance of the audience model under a FIXED attention
pattern with any number of channels per agent (drawn-once partner randomization).

Model (obs:agy-audience, P0/P1): world eta_{t+1} = F eta_t + w_t; agents filter
x_t = (eta_t, eta_{t-1}) exactly, computation noise qc*I_2 added to predicted means
and included in P^-.  Agent 0 = source S (sensor RS, reads nothing); agents 1..n are
members (sensor R).  Every agent broadcasts its raw reading; agent a reads the
channels reads[a] (a tuple of senders) every round, each message carrying
v_j(t-1) + nu_aj(t) about eta_{t-1}, read with its exact variance R_j + Rc.

Prior-error recursion (world path conditioned, so w drops out):
  eps_a(t+1) = M_a eps_a(t) + A K_a[:,0] v_a(t) + sum_k A K_a[:,k] (v_{j_k}(t-1) + nu_{a j_k}(t)) + xi_a(t),
  M_a = A P^+_a (P^-_a)^{-1},  K_a = P^+_a H_a^T R_a^{-1}.
Augmented state Z = [eps_0..eps_n (2 each), vlag_0..vlag_n], vlag_j(t) = v_j(t-1).
The contrast coordinate is e_a = eps_a[0] (eta_t component of the prior error).
"""
from __future__ import annotations

import itertools
import numpy as np
from scipy.linalg import solve_discrete_lyapunov


def AF(F: float) -> np.ndarray:
    return np.array([[F, 0.0], [1.0, 0.0]])


def riccati(F: float, Q: float, qc: float, H: np.ndarray, Rm: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    r"""Stationary P^- and P^+ of the 2-state filter:
    P^+ = ((P^-)^{-1} + H^T R^{-1} H)^{-1},  P^-_{next} = A P^+ A^T + diag(Q,0) + qc I."""
    A = AF(F)
    Qx = np.diag([Q, 0.0]) + qc * np.eye(2)
    Ri = np.linalg.inv(Rm)
    Pm = np.eye(2)
    for _ in range(20000):
        Pp = np.linalg.inv(np.linalg.inv(Pm) + H.T @ Ri @ H)
        Pn = A @ Pp @ A.T + Qx
        if np.max(np.abs(Pn - Pm)) < 1e-16:
            Pm = Pn
            break
        Pm = Pn
    Pp = np.linalg.inv(np.linalg.inv(Pm) + H.T @ Ri @ H)
    return Pm, Pp


def sigma_fixed(reads: list[tuple[int, ...]], F: float = 0.9, Q: float = 0.05, R: float = 1.0,
                RS: float = 0.01, Rc: float = 0.002, qc: float = 1e-4,
                cond_vS: bool = False) -> np.ndarray:
    r"""World-conditional covariance Sigma^c (N x N, N = n+1) of the prior errors e_a
    for the fixed pattern `reads` (reads[0] must be () for the source)."""
    N = len(reads)
    A = AF(F)
    Rsen = [RS] + [R] * (N - 1)
    filt = []
    for a in range(N):
        src = reads[a]
        H = np.array([[1.0, 0.0]] + [[0.0, 1.0]] * len(src))
        Rm = np.diag([Rsen[a]] + [Rsen[j] + Rc for j in src])
        Pm, Pp = riccati(F, Q, qc, H, Rm)
        K = Pp @ H.T @ np.linalg.inv(Rm)
        M = A @ Pp @ np.linalg.inv(Pm)
        filt.append((src, A @ K, M))
    dim = 3 * N
    vl = lambda j: 2 * N + j
    T = np.zeros((dim, dim))
    cols, var = [], []
    for a, (src, AK, M) in enumerate(filt):
        T[2 * a:2 * a + 2, 2 * a:2 * a + 2] = M
        for k, j in enumerate(src):
            T[2 * a:2 * a + 2, vl(j)] = AK[:, 1 + k]
    for a, (src, AK, M) in enumerate(filt):  # own sensing noise v_a(t)
        g = np.zeros(dim)
        g[2 * a:2 * a + 2] = AK[:, 0]
        g[vl(a)] = 1.0
        cols.append(g)
        var.append(0.0 if (cond_vS and a == 0) else Rsen[a])
    for a, (src, AK, M) in enumerate(filt):  # receiver-specific channel noises
        for k, j in enumerate(src):
            g = np.zeros(dim)
            g[2 * a:2 * a + 2] = AK[:, 1 + k]
            cols.append(g)
            var.append(Rc)
    for a in range(N):  # computation noise
        for c in range(2):
            g = np.zeros(dim)
            g[2 * a + c] = 1.0
            cols.append(g)
            var.append(qc)
    G = np.column_stack(cols)
    W = G @ np.diag(var) @ G.T
    SZ = solve_discrete_lyapunov(T, W)
    idx = [2 * a for a in range(N)]
    return SZ[np.ix_(idx, idx)]


def is_diffusive(Pi: np.ndarray, tol: float = 1e-9) -> tuple[bool, float, float]:
    """Diffusive: off-diagonal <= 0 and row sums >= 0 (tolerance relative to the scale)."""
    N = Pi.shape[0]
    off = Pi[~np.eye(N, dtype=bool)]
    rs = Pi.sum(axis=1)
    scale = np.abs(np.diag(Pi)).max()
    ok = off.max() <= tol * scale and rs.min() >= -tol * scale
    return bool(ok), float(off.max()), float(rs.min())


def contrast(Pi: np.ndarray, C: list[int]) -> float:
    r"""r(C) = xi_in/xi_out (def:col-contrast): xi_out = phi^T Pi phi with phi = 1_C/sqrt(n);
    xi_in = min over f perp 1_C supported on C of f^T(diag(eps)+L_C)f / f^T f."""
    a = -Pi.copy()
    np.fill_diagonal(a, 0.0)
    eps = Pi.sum(axis=1)
    n = len(C)
    phi = np.zeros(Pi.shape[0])
    phi[C] = 1.0 / np.sqrt(n)
    xo = phi @ Pi @ phi
    aC = a[np.ix_(C, C)]
    B = np.diag(eps[C]) + np.diag(aC.sum(axis=1)) - aC
    Qb, _ = np.linalg.qr(np.column_stack([np.ones(n), np.eye(n)[:, :n - 1]]))
    U = Qb[:, 1:n]
    return float(np.linalg.eigvalsh(U.T @ B @ U).min() / xo)


def regions(N: int) -> list[list[int]]:
    return [list(c) for k in range(2, N + 1) for c in itertools.combinations(range(N), k)]


def max_region(Pi: np.ndarray) -> tuple[float, list[int]]:
    best, arg = -np.inf, None
    for C in regions(Pi.shape[0]):
        r = contrast(Pi, C)
        if r > best:
            best, arg = r, C
    return best, arg


def mi_ratio(Sig: np.ndarray) -> tuple[float, tuple]:
    r"""Substitute selector of s05_agency.tex:252: the largest ratio of mean within-block
    to mean between-block world-conditional mutual information over balanced bipartitions.
    Pairwise MI of jointly Gaussian scalars: I_ij = -1/2 ln(1 - rho_ij^2)."""
    N = Sig.shape[0]
    d = np.sqrt(np.diag(Sig))
    rho = Sig / np.outer(d, d)
    I = -0.5 * np.log(np.clip(1.0 - rho ** 2, 1e-300, None))
    best, arg = -np.inf, None
    sizes = [N // 2] if N % 2 else [N // 2]
    seen = set()
    for k in sizes:
        for B1 in itertools.combinations(range(N), k):
            B2 = tuple(x for x in range(N) if x not in B1)
            key = frozenset([B1, B2])
            if key in seen:
                continue
            seen.add(key)
            within = [I[i, j] for B in (B1, B2) for i, j in itertools.combinations(B, 2)]
            between = [I[i, j] for i in B1 for j in B2]
            w, b = float(np.mean(within)), float(np.mean(between))
            ratio = np.inf if b <= 1e-15 * max(w, 1e-300) else w / b
            if ratio > best:
                best, arg = ratio, (B1, B2)
    return best, arg
