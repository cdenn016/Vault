r"""Check 4: closure (def:agy-closure, 05_agency.tex:13-24) of the audience A in instance P0, declared coarse variable
y(t) = (1/n) sum_{i in A} m^-_{i,0}(t), the collective average of the members' prior means of eta_t (scalar).

Internal variables x = (m^-_i)_{i in A} in R^{2n}; given the blanket path (own sensors, source readings)
x_{t+1} = (I_n kron M) x_t + B x_B,t + n_t,  M = A_F P^+ (P^-)^{-1},  Q^n = qc I_{2n} > 0 (members do not read one
another, so A is block diagonal).  Memory: d_cl by eq:agy-closure-defect and the Markov defect
d_M = lim_L I(y_{t+1}; y_{t-L:t-1} | y_t) of the stationary law without input (equal to the input-conditional value,
05_agency.tex:20).  Inference: expected KL between the encoded belief N(y, v_enc) of eta_t and the union-model
predictive N(m_U, P_U) of eta_t; union model = dynamics of eta_C = (eta_t, u_S(t-1)) with the product of the members'
likelihoods (own sensors and source readings, each datum once), computed exactly by a joint Lyapunov equation with
the world innovations included.

Declared expectations before running: d_M <= 1e-3, d_cl <= 1e-2; best-constant inference KL between 0.005 and 0.05.
NEGATIVE CONTROLS: (i) a two-dimensional AR(1) whose coarse coordinate is an exact eigen-coordinate with independent
noise must give d_M = 0 to 1e-12, while a mixed coordinate gives d_M > 1e-3; (ii) comparing y(t) with the union
predictive of eta_{t+1} (wrong time) must give an inference KL at least ten times the correct one.
"""
import time
import numpy as np
from scipy.linalg import solve_discrete_lyapunov
from aud import Par, riccati_fixed, b_of, posterior, A_F

t0 = time.time()
par = Par()
n = par.n


def markov_defect(Mx, Qn, c, L=200):
    r"""Stationary scalar y = c^T x of x_{t+1} = Mx x_t + noise(Qn): d_M(L) = 1/2 ln Var(y1|y0) / Var(y1|y0..y_{-L})."""
    S = solve_discrete_lyapunov(Mx, Qn)
    acov = []
    P = S.copy()
    for k in range(L + 2):
        acov.append(float(c @ P @ c))      # Cov(y_{t+k}, y_t) = c^T Mx^k S c
        P = Mx @ P
    acov = np.array(acov)
    def condvar(m):
        # Var(y_{m} | y_{m-1}, ..., y_0) for a window of m+1 points (stationary Toeplitz)
        T = np.array([[acov[abs(i - j)] for j in range(m + 1)] for i in range(m + 1)])
        A11 = T[:m, :m]; a = T[:m, m]
        return T[m, m] - a @ np.linalg.solve(A11, a)
    v1 = condvar(1)
    out = {}
    for m in (2, 5, 10, 50, L):
        out[m] = 0.5 * np.log(v1 / condvar(m))
    return out


def closure_defect(Mx_full, Qn, Pmat):
    S = solve_discrete_lyapunov(Mx_full, Qn)
    Sxy = S - S @ Pmat.T @ np.linalg.inv(Pmat @ S @ Pmat.T) @ Pmat @ S
    PQ = Pmat @ Qn @ Pmat.T
    X = np.linalg.inv(PQ) @ Pmat @ Mx_full @ Sxy @ Mx_full.T @ Pmat.T
    return 0.5 * np.log(np.linalg.det(np.eye(X.shape[0]) + X))


# ---- members' stationary filter (all read the source) ----
Pm, Pp = riccati_fixed(par, 1.0 / par.R, b_of(par, 1, 0))
M = A_F(par.F) @ Pp @ np.linalg.inv(Pm)
print(f"member M = {np.round(M, 6).tolist()}, rank {np.linalg.matrix_rank(M, tol=1e-12)}")
Mfull = np.kron(np.eye(n), M)
Qn = par.qc * np.eye(2 * n)
Pmat = np.kron(np.ones((1, n)) / n, np.array([[1.0, 0.0]]))
dM = markov_defect(Mfull, Qn, Pmat[0])
dcl = closure_defect(Mfull, Qn, Pmat)
print(f"memory: d_M(L) = {{{', '.join(f'{k}: {v:.3e}' for k, v in dM.items())}}}; d_cl = {dcl:.3e}")

# ---- negative control (i) ----
Me = np.diag([0.8, 0.3])
dM0 = markov_defect(Me, np.diag([1.0, 1.0]), np.array([1.0, 0.0]))
dM1 = markov_defect(Me, np.diag([1.0, 1.0]), np.array([1.0, 1.0]))
print(f"NEG (i): eigen-coordinate d_M = {dM0[200]:.2e} (must be 0); mixed coordinate d_M = {dM1[200]:.3e} (must be > 1e-3)")

# ---- union model and inference ----
Af = A_F(par.F)
# union filter on x_t = (eta_t, eta_{t-1}) with sufficient statistics sbar (noise R/n) and ybar (noise RS + Rc/n);
# no computation noise (the union model is the ideal model of eta_C's dynamics)
def union_fixed():
    P = np.eye(2) * par.Q / (1 - par.F ** 2)
    for _ in range(5000):
        Pp_ = posterior(P, n / par.R, 1.0 / (par.RS + par.Rc / n))
        Pn = Af @ Pp_ @ Af.T + np.diag([par.Q, 0.0])
        if np.max(np.abs(Pn - P)) < 1e-17:
            P = Pn
            break
        P = Pn
    return P, posterior(P, n / par.R, 1.0 / (par.RS + par.Rc / n))


PU, PUp = union_fixed()
MU = Af @ PUp @ np.linalg.inv(PU)
k_own = Pp[:, 0] / par.R
k_S = Pp[:, 1] / (par.RS + par.Rc)
kU_s = PUp[:, 0] / (par.R / n)
kU_y = PUp[:, 1] / (par.RS + par.Rc / n)
# joint state Z = (Ebar (2), EU (2), VS (1)); fresh noises f = (vbar, nubar, xibar0, xibar1, vS, w)
A = np.zeros((5, 5))
A[0:2, 0:2] = M
A[0:2, 4] = Af @ k_S
A[2:4, 2:4] = MU
A[2:4, 4] = Af @ kU_y
G = np.zeros((5, 6))
G[0:2, 0] = Af @ k_own
G[0:2, 1] = Af @ k_S
G[0:2, 2] = [1.0, 0.0]
G[0:2, 3] = [0.0, 1.0]
G[2:4, 0] = Af @ kU_s
G[2:4, 1] = Af @ kU_y
G[4, 4] = 1.0
G[0, 5] = -1.0
G[2, 5] = -1.0
Qf = np.diag([par.R / n, par.Rc / n, par.qc / n, par.qc / n, par.RS, par.Q])
SZ = solve_discrete_lyapunov(A, G @ Qf @ G.T)
d = np.array([1.0, 0, -1.0, 0, 0])
D = float(d @ SZ @ d)
PU00 = PU[0, 0]
v_cl = Pm[0, 0]
kl_best = D / (2 * PU00)
kl_claim = 0.5 * (v_cl / PU00 + D / PU00 - 1 - np.log(v_cl / PU00))
kl_rev = 0.5 * np.log1p(D / PU00)
print(f"union predictive variance P_U = {PU00:.6e}; members' claimed P^-_00 = {v_cl:.6e}; E[(y - m_U)^2] = {D:.6e}")
print(f"inference KL: best constant {kl_best:.5f}; claimed variance {kl_claim:.5f}; reverse direction (best) {kl_rev:.5f}")
# check of the members' own claimed variance against the exact error variance of one member
Sm1 = solve_discrete_lyapunov(np.block([[M, (Af @ k_S)[:, None]], [np.zeros((1, 2)), np.zeros((1, 1))]]),
                              (lambda g, q: g @ q @ g.T)(np.block([[np.column_stack([Af @ k_own, Af @ k_S, np.eye(2), np.zeros(2), [-1.0, 0.0]])],
                                                                    [np.array([[0, 0, 0, 0, 1.0, 0]])]]),
                                                          np.diag([par.R, par.Rc, par.qc, par.qc, par.RS, par.Q])))
print(f"one member's actual prior error variance {Sm1[0,0]:.6e} vs claimed {v_cl:.6e} (exact filter: must agree)")
# ---- negative control (ii): wrong time ----
d2 = np.array([1.0, 0, 0, 0, 0])
# m_U for eta_{t+1}: F * (posterior mean of eta_t) -> error of union predictive of eta_{t+1} relative to eta_t is not
# directly in Z; use the crude wrong-time comparison y(t) vs m_U(t+1) = F m_U^+(t): difference = Ebar_0(t) - EU_0(t+1) - w_t
# approximated by comparing with a union predictive one step stale: y(t) vs m_U(t-1) shifted, i.e. add Var(eta_t - eta_{t-1}).
Dw = D + 2 * par.Q / (1 + par.F)
print(f"NEG (ii) stale union predictive (one round): KL best {Dw / (2 * PU00):.4f} vs correct {kl_best:.5f}")
print(f"({time.time() - t0:.1f}s)")
