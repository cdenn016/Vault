"""Shared helpers for the C17b check (numpy/scipy only, single-threaded)."""
import os
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")
import numpy as np
from scipy.linalg import solve_discrete_lyapunov


def comm(n, X0, X1):
    r"""Commutant element I_n \otimes X0 + 1 1^T \otimes X1."""
    return np.kron(np.eye(n), X0) + np.kron(np.ones((n, n)), X1)


def smoother_cov(A, E, Q, G, H, Rv, M=1024):
    r"""Two-sided Wiener smoother error Cov(z_0 | y_{all t}) for
    z_{t+1} = A z_t + E xi_t, y_t = G z_t + H xi_t + v_t, xi ~ N(0,Q), v ~ N(0,Rv) iid, independent.
    Error = (1/2pi) \int (S_zz - S_zy S_yy^{-1} S_yz) d omega, trapezoid rule on M points.
    Returns (error covariance, Cov(z_0) from the same quadrature, max imaginary residue)."""
    nz = A.shape[0]
    zs = np.exp(2j * np.pi * np.arange(M) / M)
    R = np.linalg.inv(zs[:, None, None] * np.eye(nz)[None] - A[None])
    Tz = R @ E                      # (M, nz, nxi)
    Ty = G[None] @ Tz + H[None]     # (M, p, nxi)
    TzQ = Tz @ Q
    TyH = np.conj(np.transpose(Ty, (0, 2, 1)))
    Szy = TzQ @ TyH
    Syy = (Ty @ Q) @ TyH + Rv[None]
    Szz = TzQ @ np.conj(np.transpose(Tz, (0, 2, 1)))
    X = np.linalg.solve(Syy, np.conj(np.transpose(Szy, (0, 2, 1))))
    err = (Szz - Szy @ X).mean(0)
    return err.real, Szz.mean(0).real, float(np.abs(err.imag).max())


def lyap(A, EQE):
    return solve_discrete_lyapunov(A, EQE)


def is_diffusive(P, rtol=1e-9):
    s = np.abs(P).max()
    off = P - np.diag(np.diag(P))
    return bool(off.max() <= rtol * s and P.sum(1).min() >= -rtol * s)


def rates(P, Cidx):
    r"""Rates of the manuscript's Definition (Contrast) for a diffusive precision P.
    a_ij = -P_ij, eps = P 1, L_C Laplacian of couplings inside C.
    xi_out = phi^T P phi, xi_in = min_{f perp 1_C, supp f in C} f^T(diag eps + L_C) f / f^T f."""
    Cidx = list(Cidx)
    n = len(Cidx)
    N = P.shape[0]
    a = -P.copy()
    np.fill_diagonal(a, 0.0)
    eps = P.sum(1)
    aCC = a[np.ix_(Cidx, Cidx)]
    LC = np.diag(aCC.sum(1)) - aCC
    Min = np.diag(eps[Cidx]) + LC
    out = [k for k in range(N) if k not in Cidx]
    adel = a[np.ix_(Cidx, out)].sum(1) if out else np.zeros(n)
    ident_res = np.abs(Min - (P[np.ix_(Cidx, Cidx)] - np.diag(adel))).max()
    # orthonormal basis of 1^perp in R^n
    Uq, _ = np.linalg.qr(np.column_stack([np.ones(n), np.eye(n)[:, : n - 1]]))
    U = Uq[:, 1:]
    xin = np.linalg.eigvalsh(U.T @ Min @ U).min()
    phi = np.ones(n) / np.sqrt(n)
    xout = phi @ P[np.ix_(Cidx, Cidx)] @ phi
    return xin, xout, ident_res, Min, adel
