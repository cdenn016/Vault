r"""G3: check the Karcher-mean uniqueness radius quoted at PIFB2.tex:1573 and 3762.

PIFB2 states that the frame Karcher mean on SO(K_q) with d(U,V) = ||log(U^{-1}V)||_F is
unique on balls below the Kendall/Afsari radius, "pi/2 under the unit-curvature
normalization", "which also lies below the injectivity radius".

Afsari (2011), as restated in Afsari-Tron-Vidal (SIAM J. Control Optim. 2013, eq. 2.1):
    r_cx = (1/2) min{ inj M, pi / sqrt(Delta) },
with Delta an upper bound on sectional curvature. For a bi-invariant metric on a
compact Lie group, K(X,Y) = (1/4) |[X,Y]|^2 / (|X|^2 |Y|^2 - <X,Y>^2).

This script (i) maximizes K over random 2-planes of so(n), n = 3, 4, 5, under the
Frobenius metric <X,Y> = tr(X^T Y); (ii) reads off inj from the shortest closed
geodesic exp(t E_12) (cut point at rotation angle pi, Frobenius length pi*sqrt 2);
(iii) converts r_cx to the unit-curvature normalization and to rotation angle; and
(iv) shows that the Frechet mean of two rotations at angles +-alpha about one axis
is non-unique at alpha = pi/2 (angle) and jumps to the antipode for alpha > pi/2.
"""
from __future__ import annotations

import numpy as np
from scipy.linalg import expm, logm
from scipy.optimize import minimize


def skew(v: np.ndarray, n: int) -> np.ndarray:
    """Map a vector of length n(n-1)/2 to a skew matrix."""
    X = np.zeros((n, n))
    iu = np.triu_indices(n, 1)
    X[iu] = v
    return X - X.T


def sec_curv(a: np.ndarray, b: np.ndarray, n: int) -> float:
    r"""K(X,Y) = (1/4)|[X,Y]|_F^2 / (|X|^2|Y|^2 - <X,Y>^2) for the bi-invariant Frobenius metric."""
    X, Y = skew(a, n), skew(b, n)
    C = X @ Y - Y @ X
    ip = lambda A, B: float(np.trace(A.T @ B))
    den = ip(X, X) * ip(Y, Y) - ip(X, Y) ** 2
    return 0.25 * ip(C, C) / den


def max_curv(n: int, rng: np.random.Generator, trials: int = 40) -> float:
    m = n * (n - 1) // 2
    best = 0.0
    for _ in range(trials):
        z0 = rng.standard_normal(2 * m)
        res = minimize(lambda z: -sec_curv(z[:m], z[m:], n), z0, method="BFGS")
        best = max(best, -res.fun)
    return best


def frechet_two_rotations(alpha: float) -> tuple[float, float]:
    """Frechet function at identity and at the antipode R(pi), data R(+-alpha) about z, Frobenius-log distance."""
    def R(t: float) -> np.ndarray:
        c, s = np.cos(t), np.sin(t)
        return np.array([[c, -s, 0], [s, c, 0], [0, 0, 1.0]])

    def d2(A: np.ndarray, B: np.ndarray) -> float:
        # angle-based distance avoids logm branch issues at angle pi
        th = np.arccos(np.clip((np.trace(A.T @ B) - 1) / 2, -1, 1))
        return 2.0 * th**2  # ||log||_F^2 = 2 theta^2

    pts = [R(alpha), R(-alpha)]
    f_id = sum(d2(np.eye(3), P) for P in pts)
    f_pi = sum(d2(R(np.pi), P) for P in pts)
    return f_id, f_pi


def main() -> None:
    rng = np.random.default_rng(0)
    for n in (3, 4, 5):
        Kmax = max_curv(n, rng)
        inj = np.pi * np.sqrt(2)  # half of the closed geodesic exp(t E_12), length 2 pi sqrt 2
        r_cx = 0.5 * min(inj, np.pi / np.sqrt(Kmax))
        scale = np.sqrt(Kmax)  # distances rescale by sqrt(Kmax) when the metric is normalized to Kmax = 1
        print(
            f"SO({n}) Frobenius: Kmax={Kmax:.6f} (1/8={1/8:.6f}); inj={inj:.6f}; "
            f"r_cx={r_cx:.6f}; unit-curvature: inj={inj*scale:.6f} (pi/2={np.pi/2:.6f}), "
            f"r_cx={r_cx*scale:.6f} (pi/4={np.pi/4:.6f}); rotation-angle r_cx={r_cx/np.sqrt(2):.6f}"
        )
    # cut-point check: ||log R(theta)||_F = sqrt(2) theta below pi
    th = 3.0
    Rz = expm(skew(np.array([th, 0.0, 0.0]), 3))
    print(f"||log R(3.0)||_F = {np.linalg.norm(logm(Rz).real):.12f}, sqrt2*3 = {np.sqrt(2)*3:.12f}")
    for alpha in (np.pi / 2 - 0.05, np.pi / 2, np.pi / 2 + 0.05):
        f_id, f_pi = frechet_two_rotations(alpha)
        print(f"alpha={alpha:.4f}: F(I)={f_id:.6f}, F(R_pi)={f_pi:.6f}, argmin={'I' if f_id < f_pi - 1e-12 else ('tie' if abs(f_id-f_pi) < 1e-12 else 'R_pi')}")


if __name__ == "__main__":
    main()
