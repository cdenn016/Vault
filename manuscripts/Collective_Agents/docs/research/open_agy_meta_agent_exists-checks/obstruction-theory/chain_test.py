"""Is 'no attractive coupling' ((Pi_0)_ij = 0) enough? Reversible chain 0-1-2-3, actors 0 and 3 only.
EXPECTATION (declared): unknown; if some draw is diffusive, null independence (not just (Pi_0)_03=0) is needed."""
import numpy as np
from scipy.linalg import solve_discrete_are, solve_discrete_lyapunov
from common import is_diffusive
rng = np.random.default_rng(5)
def sigma_c_rts(A, Q, b, q):
    N = A.shape[0]; bb = b.reshape(N, 1)
    Pp = solve_discrete_are(A.T, bb, Q, np.array([[q]]))
    S = (bb.T @ Pp @ bb).item() + q
    Pf = Pp - Pp @ bb @ bb.T @ Pp / S
    J = Pf @ A.T @ np.linalg.inv(Pp)
    return solve_discrete_lyapunov(J, Pf - J @ Pp @ J.T)
found, n_ok = None, 0
for _ in range(3000):
    w = rng.uniform(0.05, 0.45, 3); c = rng.uniform(0, 0.5, 4)
    W = np.diag(c)
    for i in range(3):
        W[i, i + 1] = W[i + 1, i] = w[i]
    if np.abs(np.linalg.eigvalsh(W)).max() >= 0.97: continue
    qv = rng.uniform(0.2, 2.0)
    Q = qv * np.eye(4)
    P0 = np.linalg.inv(solve_discrete_lyapunov(W, Q))
    b = np.array([rng.uniform(0.01, 1), 0, 0, rng.uniform(0.01, 1)]); q = 10 ** rng.uniform(-1.5, 1.5)
    Pc = np.linalg.inv(sigma_c_rts(W, Q, b, q))
    n_ok += 1
    d = is_diffusive(Pc)
    if d[0] and d[1] and found is None:
        found = (W, qv, b, q, P0, Pc)
print("draws", n_ok, "; diffusive instance found:", found is not None)
if found:
    W, qv, b, q, P0, Pc = found
    np.set_printoptions(precision=5, suppress=True)
    print("W=\n", W, "\nq_xi =", qv, " b =", b, " q =", q)
    print("(Pi_0)_03 =", P0[0, 3], "  null cov (Sigma_0)_03 > 0:", np.linalg.inv(P0)[0, 3] > 0)
    print("Pi^c=\n", Pc)
