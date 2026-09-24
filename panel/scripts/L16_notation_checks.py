"""L16: numerical checks of two formulas stated in the notation/appendix text of PIFB2.tex.

(1) Line 3948: Killing form of gl(K), B(X,Y) = 2K tr(XY) - 2 tr(X) tr(Y); indefinite and degenerate.
(2) Line 994-995: right-trivialized differential of exp,
    D exp_phi[H] = Psi_R(ad_phi)(H) exp(phi),  Psi_R(z) = (e^z - 1)/z,
    and the left-trivialized form at line 981, dexp^L_phi(v) = exp(-phi) D exp_phi[v].
"""
import numpy as np
from scipy.linalg import expm

rng = np.random.default_rng(0)


def killing_numeric(X: np.ndarray, Y: np.ndarray) -> float:
    r"""B(X,Y) = tr(ad_X ad_Y), with ad acting on gl(K) flattened (K^2 x K^2)."""
    K = X.shape[0]
    I = np.eye(K)
    adX = np.kron(X, I) - np.kron(I, X.T)  # row-major vec: vec(XZ - ZX)
    adY = np.kron(Y, I) - np.kron(I, Y.T)
    return float(np.trace(adX @ adY))


for K in (2, 3, 4):
    X, Y = rng.standard_normal((K, K)), rng.standard_normal((K, K))
    lhs = killing_numeric(X, Y)
    rhs = 2 * K * np.trace(X @ Y) - 2 * np.trace(X) * np.trace(Y)
    # Gram matrix of B on the standard basis: eigenvalue signs
    E = [np.eye(K)[:, [a]] @ np.eye(K)[[b], :] for a in range(K) for b in range(K)]
    G = np.array([[killing_numeric(A, Bm) for Bm in E] for A in E])
    ev = np.linalg.eigvalsh((G + G.T) / 2)
    print(f"K={K}: |B_numeric - formula| = {abs(lhs - rhs):.2e};"
          f" Gram eigen signs +{(ev > 1e-9).sum()} -{(ev < -1e-9).sum()} 0:{(abs(ev) <= 1e-9).sum()}")


for K in (2, 3, 4, 5):
    E = [np.eye(K)[:, [a]] @ np.eye(K)[[b], :] for a in range(K) for b in range(K)]
    T = np.array([[np.trace(A @ Bm) for Bm in E] for A in E])
    ev = np.linalg.eigvalsh(T)
    print(f"trace form tr(XY) on gl({K}): +{(ev > 1e-12).sum()} -{(ev < -1e-12).sum()}"
          f"  (line 1573 claims ({K*(K+1)//2}, {K*(K-1)//2}))")


def ad_series(phi: np.ndarray, H: np.ndarray, coef, n: int = 40) -> np.ndarray:
    """sum_k coef(k) ad_phi^k (H)."""
    out = np.zeros_like(H)
    term = H.copy()
    for k in range(n):
        out += coef(k) * term
        term = phi @ term - term @ phi
    return out


fact = [1.0]
for k in range(1, 60):
    fact.append(fact[-1] * k)
K = 3
phi = 0.7 * rng.standard_normal((K, K))
H = rng.standard_normal((K, K))
h = 1e-6
fd = (expm(phi + h * H) - expm(phi - h * H)) / (2 * h)
right = ad_series(phi, H, lambda k: 1.0 / fact[k + 1]) @ expm(phi)  # (e^z-1)/z = sum z^k/(k+1)!
left = expm(phi) @ ad_series(phi, H, lambda k: (-1) ** k / fact[k + 1])  # (1-e^{-z})/z
print(f"right-trivialized Psi_R=(e^z-1)/z: rel err {np.linalg.norm(fd - right) / np.linalg.norm(fd):.2e}")
print(f"left-trivialized  exp(-phi) D exp[H] = (1-e^-z)/z (H): rel err "
      f"{np.linalg.norm(expm(-phi) @ fd - ad_series(phi, H, lambda k: (-1) ** k / fact[k + 1])) / np.linalg.norm(fd):.2e}")
print(f"consistency left vs right: {np.linalg.norm(left - right) / np.linalg.norm(right):.2e}")
