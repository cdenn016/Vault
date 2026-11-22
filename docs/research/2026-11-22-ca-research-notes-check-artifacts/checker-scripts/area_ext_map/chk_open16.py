import os
os.environ["OMP_NUM_THREADS"] = "2"; os.environ["OPENBLAS_NUM_THREADS"] = "2"
import numpy as np
from scipy.linalg import solve_continuous_lyapunov as lyap
N = 16; a = np.zeros((N, N))
for i in range(8):
    a[i, (i + 1) % 8] = a[(i + 1) % 8, i] = 1.0
    a[8 + i, 8 + (i + 1) % 8] = a[8 + (i + 1) % 8, 8 + i] = 1.0
    a[i, 8 + i] = a[8 + i, i] = 0.05
eps, beta, omega, q, n = 0.02, 0.2, 0.1, 1.0, 8
def prec(qz, delta=0.0):
    M = np.zeros((N + 1, N + 1)); M[:N, :N] = eps * np.eye(N) + np.diag(a.sum(1)) - a
    for i in range(8):
        M[i, i] += beta; M[i, N] = -beta; M[N, i] = -omega / n
    M[N, N] = omega + delta
    S = lyap(M, 2 * np.diag([q] * N + [qz]))
    return np.linalg.inv(S), np.linalg.inv(S[:N, :N])
Pj, Pm = prec(0.0)
for name, P in (("joint", Pj), ("marginal", Pm)):
    off = P - np.diag(np.diag(P)); i, j = np.unravel_index(off.argmax(), off.shape)
    print(name, "largest positive entry rel", off.max() / np.abs(P).max(), "at", (i, j), "min row sum", P.sum(1).min())
qrev = omega * q / (n * beta)
for k in (0.5, 0.99, 1.0, 1.01, 2.0):
    Pj, Pm = prec(k * qrev)
    off = Pj - np.diag(np.diag(Pj))
    print("kappa", k, "joint diffusive", bool(off.max() <= 1e-10 and Pj.sum(1).min() >= -1e-10))
