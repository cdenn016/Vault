"""P0: Markov defect of the collective average given the blanket path (noise-driven part),
from the stationary law of the noise-driven part and from a deterministic start; and the
F = 1 diagnostic.  Reuses my own engine p0_rebuild (imported functions only)."""
import importlib, sys, io, contextlib
import numpy as np

buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    import p0_rebuild as eng   # runs its own printout; silenced here

P, K, H = eng.riccati(eng.R, [eng.RS + eng.RC])
M = eng.A2 @ (np.eye(2) - K @ H)
print("member closed-loop M = A(I-KH):\n", M, "\n rank:", np.linalg.matrix_rank(M, tol=1e-12),
      " eigenvalues:", np.linalg.eigvals(M))
Nq = eng.QC / 4 * np.eye(2)          # computation noise of the average of 4 members
e1 = np.array([1.0, 0.0])


def cmi(C, t):
    """I(y_{t+1}; y_{0:t-1} | y_t) from the covariance C of (y_0..y_{t+1})."""
    def ld(idx):
        idx = [i for i in idx]
        if not idx:
            return 0.0
        sub = C[np.ix_(idx, idx)]
        return np.linalg.slogdet(sub)[1]
    past = list(range(0, t)); a = [t]; b = [t + 1]
    return 0.5 * (ld(past + a) + ld(a + b) - ld(a) - ld(past + a + b))


def ycov(S0, T):
    """covariance of y_0..y_T for z_{t+1} = M z_t + n_t, z_0 ~ N(0,S0)."""
    St = [S0]
    for _ in range(T):
        St.append(M @ St[-1] @ M.T + Nq)
    C = np.zeros((T + 1, T + 1))
    for s in range(T + 1):
        Ms = np.eye(2)
        for t in range(s, T + 1):
            C[t, s] = C[s, t] = e1 @ Ms @ St[s] @ e1
            Ms = M @ Ms
    return C


Sst = eng.dlyap(M, Nq)
C = ycov(Sst, 60)
print("stationary noise-driven initial law: I at history 1,4,9,49:",
      [round(cmi(C, t), 5) for t in (1, 4, 9, 49)])
# deterministic start: z_0 = 0, so y_0 is constant; drop it (tiny jitter avoids log 0)
Cd = ycov(np.zeros((2, 2)), 40)[1:, 1:]
vals = [cmi(Cd, t) for t in range(1, 30)]
print("deterministic start: sup_t = %.6f at index %d (y_1 is the first random value)" % (max(vals), 1 + int(np.argmax(vals))))
# members' stationary law is outside the proviso; not recomputed.

# F = 1 diagnostic (N_fg)
eng.F = 1.0
eng.A2 = np.array([[1.0, 0.0], [1.0, 0.0]])
S, _ = eng.sigma_c(((0,), (0,), (0,), (0,)))
Pi = np.linalg.inv(S)
print("F=1: diffusive %s r(A) %.4f r(A u S) %.4f" % (eng.diffusive(Pi), eng.contrast(Pi, (1, 2, 3, 4)), eng.contrast(Pi, (0, 1, 2, 3, 4))))
