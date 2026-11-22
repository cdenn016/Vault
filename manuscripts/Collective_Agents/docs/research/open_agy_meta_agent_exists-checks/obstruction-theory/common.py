"""Shared helpers for the obstruction-theory checks (scalar errors, def:col-contrast)."""
import numpy as np


def is_diffusive(Pi, tol=1e-12):
    """Return (offdiag_ok, rowsum_ok, max_offdiag, min_rowsum) for a symmetric matrix Pi."""
    P = 0.5 * (Pi + Pi.T)
    mask = ~np.eye(P.shape[0], dtype=bool)
    max_off = P[mask].max() if P.shape[0] > 1 else -np.inf
    rs = P.sum(axis=1)
    return (max_off <= tol, rs.min() >= -tol, max_off, rs.min())


def contrast(Pi, C):
    """Contrast r(C) = xin/xout of def:col-contrast (04_collectives.tex:182-188).

    Pi must be diffusive; leaks are row sums over the whole population, L_C uses
    only couplings inside C, xout = phi_C^T Pi phi_C.
    """
    P = 0.5 * (Pi + Pi.T)
    N = P.shape[0]
    C = list(C)
    n = len(C)
    eps = P.sum(axis=1)
    a = -P.copy()
    np.fill_diagonal(a, 0.0)
    aC = a[np.ix_(C, C)]
    LC = np.diag(aC.sum(axis=1)) - aC
    M = np.diag(eps[C]) + LC
    # orthonormal basis of 1^perp in R^n
    Q, _ = np.linalg.qr(np.column_stack([np.ones(n), np.eye(n)[:, : n - 1]]))
    Z = Q[:, 1:n]
    xin = np.linalg.eigvalsh(Z.T @ M @ Z).min()
    phi = np.zeros(N)
    phi[C] = 1.0 / np.sqrt(n)
    xout = phi @ P @ phi
    return xin / xout, xin, xout


def baseline_exchangeable_mean(Pi):
    """Baseline of clause (c) with mean coupling and uniform leak (def:col-baseline(c)).

    Comparison medium: abar between every pair, uniform leak epsbar.
    Its baseline is attained by the whole population: 1 + N abar/epsbar
    (regions of size m<N have (eps+m a)/(eps+(N-m)a) < 1 + N a/eps).
    """
    P = 0.5 * (Pi + Pi.T)
    N = P.shape[0]
    eps = P.sum(axis=1)
    a = -P.copy()
    np.fill_diagonal(a, 0.0)
    abar = a[np.triu_indices(N, 1)].mean()
    epsbar = eps.mean()
    # brute-force check over region sizes in the comparison medium
    vals = []
    for m in range(2, N + 1):
        xin = epsbar + m * abar
        xout = epsbar + (N - m) * abar
        vals.append(xin / xout)
    return max(vals), 1 + N * abar / epsbar, abar, epsbar
