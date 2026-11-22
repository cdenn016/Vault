"""Check ex:hie-noiseless-record claims from the Lyapunov equation of eq:hie-record (no closed form used)."""
import os
os.environ["OMP_NUM_THREADS"] = "2"; os.environ["OPENBLAS_NUM_THREADS"] = "2"; os.environ["MKL_NUM_THREADS"] = "2"
import numpy as np
from scipy.linalg import solve_continuous_lyapunov as lyap

def build(a, C, eps, beta, omega, delta, q, qz):
    N = a.shape[0]; n = len(C)
    M = np.zeros((N + 1, N + 1))
    L = np.diag(a.sum(1)) - a
    M[:N, :N] = eps * np.eye(N) + L
    for i in C:
        M[i, i] += beta; M[i, N] = -beta; M[N, i] = -omega / n
    M[N, N] = omega + delta
    Q = np.diag([q] * N + [qz])
    Sig = lyap(M, 2 * Q)            # M S + S M^T = 2Q
    return M, Sig

def diffusive(P, tol=1e-10):
    off = P - np.diag(np.diag(P))
    return bool(off.max() <= tol and (P.sum(1) >= -tol).all()), off.max(), P.sum(1).min()

np.set_printoptions(precision=6, suppress=True, linewidth=150)
# (1) closed K_2 witness: a=1, eps=.1, beta=.2, omega=.1, delta=0, q=1, qz=0
a = np.array([[0, 1.0], [1.0, 0]])
M, S = build(a, [0, 1], 0.1, 0.2, 0.1, 0.0, 1.0, 0.0)
P = np.linalg.inv(S)
print("K2 Pi:\n", P, "\nrow sums", P.sum(1), "diffusive", diffusive(P), "min eig Sigma", np.linalg.eigvalsh(S).min())
# threshold a = omega/n = 0.05
for av in (0.049, 0.05, 0.051):
    a = np.array([[0, av], [av, 0]])
    _, S = build(a, [0, 1], 0.1, 0.2, 0.1, 0.0, 1.0, 0.0)
    print("K2 a=", av, diffusive(np.linalg.inv(S)))
# closed K_2 with delta>0 at qz=0
_, S = build(np.array([[0, 1.0], [1.0, 0]]), [0, 1], 0.1, 0.2, 0.1, 0.01, 1.0, 0.0)
print("K2 delta=0.01 qz=0:", diffusive(np.linalg.inv(S)))
# closed ring of 8 from chk:hie-record-precision: expect uncoupled entry 0.0125 and record row sum 0.512
N = 8; a = np.zeros((N, N))
for i in range(N): a[i, (i + 1) % N] = a[(i + 1) % N, i] = 1.0
_, S = build(a, list(range(N)), 0.02, 0.2, 0.1, 0.0, 1.0, 0.0)
P = np.linalg.inv(S)
print("ring8 Pi[0,2]=", P[0, 2], "record row sum", P[N].sum(), "diffusive", diffusive(P)[0])
# closed K_8 with coupling 1 (>= omega/n): noiseless record
a = np.ones((N, N)) - np.eye(N)
_, S = build(a, list(range(N)), 0.02, 0.2, 0.1, 0.0, 1.0, 0.0)
print("closed K8 qz=0:", diffusive(np.linalg.inv(S)))
# closed ring, delta=0.01: window [1, 2.65] q_rev
a = np.zeros((N, N))
for i in range(N): a[i, (i + 1) % N] = a[(i + 1) % N, i] = 1.0
qrev = 0.1 * 1.0 / (8 * 0.2)
for k in (0.99, 1.0, 2.0, 2.6, 2.64, 2.66, 2.7, 4.0):
    _, S = build(a, list(range(N)), 0.02, 0.2, 0.1, 0.01, 1.0, k * qrev)
    print("ring8 delta=.01 kappa", k, diffusive(np.linalg.inv(S), 1e-9)[0])
# (2) open path 0-2-1, C={0,1}, outsider 2: marginal (agents) precision at qz=0
a = np.zeros((3, 3)); a[0, 2] = a[2, 0] = a[1, 2] = a[2, 1] = 1.0
for k in (0.0, 0.5, 1.0, 2.0):
    qrev3 = 0.1 * 1.0 / (2 * 0.2)
    _, S = build(a, [0, 1], 0.1, 0.2, 0.1, 0.0, 1.0, k * qrev3)
    Pj = np.linalg.inv(S); Pm = np.linalg.inv(S[:3, :3])
    print("path 0-2-1 kappa", k, "joint", diffusive(Pj, 1e-9)[0], "marginal", diffusive(Pm, 1e-9), )
