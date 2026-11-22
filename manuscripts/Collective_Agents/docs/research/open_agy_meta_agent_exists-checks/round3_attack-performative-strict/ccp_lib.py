r"""Independent implementation of the correlated-component pair (CCP) of the
'performative-strict' candidate, written from the report's specification only.

One firm: member b senses eta^a, member s senses eta^b; both run exact Kalman
filters on x_t = (eta^a_t, eta^b_t, eta^a_{t-1}, eta^b_{t-1}) with computation
noise qc*I_4 added to the predicted mean (and included in P^-); each reads the
mate's raw reading with one-round latency through receiver-specific noise Rc.
Acts (rule D2): u_j(t) = -kappa * D m_j^+(t) + eps_j(t), D = [1,-1,0,0],
eps_j ~ N(0, s2).  Outcome: eta^Z_{t+1} = (eta^a_t - eta^b_t) + u_b + u_s + w^Z.

World-conditional law (def:col-world-conditional): condition on the whole
world path. Given (eta^a, eta^b) the private parts z_j of the prior errors are
independent of the world; conditioning on eta^Z is conditioning on
    o_t = -kappa D (z_b^+(t) + z_s^+(t)) + eps_b(t) + eps_s(t) + w^Z(t).
"""
import os
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
import itertools
import numpy as np
from scipy.linalg import solve_discrete_are, solve_discrete_lyapunov

D = np.array([1.0, -1.0, 0.0, 0.0])


def default_params():
    return dict(F=0.9, Q=0.05, rho=0.5, R=1.0, Rc=0.1, qc=1e-4,
                kappa=0.7, s2=0.01, QZ=0.05)


def world_mats(p):
    F, Q, rho = p["F"], p["Q"], p["rho"]
    Phi = np.zeros((4, 4))
    Phi[0, 0] = F
    Phi[1, 1] = F
    Phi[2, 0] = 1.0
    Phi[3, 1] = 1.0
    Qw = Q * np.array([[1.0, rho], [rho, 1.0]])
    G = np.zeros((4, 2))
    G[0, 0] = 1.0
    G[1, 1] = 1.0
    return Phi, Qw, G


def kalman_ss(Phi, Qtot, H, Rm):
    r"""Steady-state prior covariance P^- and gain K = P^- H^T (H P^- H^T + R)^{-1}.
    Solves P = Phi P Phi^T - Phi P H^T (R + H P H^T)^{-1} H P Phi^T + Qtot."""
    P = solve_discrete_are(Phi.T, H.T, Qtot, Rm)
    S = H @ P @ H.T + Rm
    K = P @ H.T @ np.linalg.inv(S)
    # verify by one Riccati step
    Pp = (np.eye(len(P)) - K @ H) @ P
    Pn = Phi @ Pp @ Phi.T + Qtot
    assert np.max(np.abs(Pn - P)) < 1e-10, np.max(np.abs(Pn - P))
    return P, K


def member_filters(p, relay=True, own_R=None):
    """Return dict with H, R, P^-, K for b and s (own sensor first, relay second)."""
    Phi, Qw, G = world_mats(p)
    Qtot = G @ Qw @ G.T + p["qc"] * np.eye(4)
    oR = p["R"] if own_R is None else own_R
    out = {}
    for j, (own, rel) in {"b": (0, 3), "s": (1, 2)}.items():
        if relay:
            H = np.zeros((2, 4))
            H[0, own] = 1.0
            H[1, rel] = 1.0
            Rm = np.diag([oR, p["R"] + p["Rc"]])
        else:
            H = np.zeros((1, 4))
            H[0, own] = 1.0
            Rm = np.array([[oR]])
        P, K = kalman_ss(Phi, Qtot, H, Rm)
        out[j] = dict(H=H, R=Rm, P=P, K=K)
    return out


# noise vector of the one-firm private process (15):
# 0 v_b(t), 1 v_s(t), 2 nu_bs(t), 3 nu_sb(t), 4-7 c_b(t), 8-11 c_s(t),
# 12 eps_b(t), 13 eps_s(t), 14 wZ(t)
# state (10): 0-3 z_b(t), 4-7 z_s(t), 8 v_b(t-1), 9 v_s(t-1)
NX, NXI = 10, 15


def private_system(p, filt, relay_mode="full", own_var=None, collider=True):
    r"""Linear system S_{t+1} = A S_t + B xi_t, o_t = C S_t + Dm xi_t for one firm.

    relay_mode: 'full'   relay noise = v_mate(t-1) + nu(t)
                'lp'     relay delivers pure channel noise nu(t) (gains kept)
                'frozen' relay content and noise frozen (no private input)
                'none'   no relay channel (filters with own sensor only)
    own_var: variance of own sensing noise (default p['R'])."""
    Phi, _, _ = world_mats(p)
    kap = p["kappa"]
    qv = np.zeros(NXI)
    qv[0] = qv[1] = p["R"] if own_var is None else own_var
    qv[2] = qv[3] = p["Rc"]
    qv[4:12] = p["qc"]
    qv[12] = qv[13] = p["s2"]
    qv[14] = p["QZ"]
    A = np.zeros((NX, NX))
    B = np.zeros((NX, NXI))
    C = np.zeros((1, NX))
    Dm = np.zeros((1, NXI))
    for j, (zs, own_i, mate_lag, nu_i, c0) in {
            "b": (0, 0, 9, 2, 4), "s": (4, 1, 8, 3, 8)}.items():
        H, K = filt[j]["H"], filt[j]["K"]
        M = np.eye(4) - K @ H
        # z^+ = M z + K n ; n = [own noise ; relay noise]
        Zp_S = np.zeros((4, NX))
        Zp_S[:, zs:zs + 4] = M
        Zp_X = np.zeros((4, NXI))
        Zp_X[:, own_i] += K[:, 0]
        if K.shape[1] == 2:
            if relay_mode == "full":
                Zp_S[:, mate_lag] += K[:, 1]
                Zp_X[:, nu_i] += K[:, 1]
            elif relay_mode == "lp":
                Zp_X[:, nu_i] += K[:, 1]
            elif relay_mode == "frozen":
                pass
            else:
                raise ValueError(relay_mode)
        A[zs:zs + 4, :] = Phi @ Zp_S
        B[zs:zs + 4, :] = Phi @ Zp_X
        B[zs:zs + 4, c0:c0 + 4] += np.eye(4)
        if collider:
            C[0, :] += -kap * D @ Zp_S
            Dm[0, :] += -kap * D @ Zp_X
    A[8, :] = 0.0
    B[8, 0] = 1.0
    A[9, :] = 0.0
    B[9, 1] = 1.0
    if collider:
        Dm[0, 12] += 1.0
        Dm[0, 13] += 1.0
        Dm[0, 14] += 1.0
    return A, B, C, Dm, qv


def stationary_cov(A, B, qv):
    return solve_discrete_lyapunov(A, B @ np.diag(qv) @ B.T)


def window_condition(A, B, C, Dm, qv, T, L=60, Lr=None, S0cov=None):
    r"""Cov(T S_{t0} | o_{t0-L..t0+Lr}) by exact Gaussian conditioning.
    T: (k, NX) target map. Initial state at t0-L has covariance S0cov
    (default: stationary covariance of (A,B))."""
    if Lr is None:
        Lr = L
    nx, nxi = B.shape
    if S0cov is None:
        S0cov = stationary_cov(A, B, qv)
    nsteps = L + Lr + 1
    dimU = nx + nxi * nsteps
    coefS = np.zeros((nx, dimU))
    coefS[:, :nx] = np.eye(nx)
    O = np.zeros((nsteps, dimU))
    tgt = None
    for k in range(nsteps):
        if k == L:
            tgt = T @ coefS
        cx = np.zeros((nxi, dimU))
        cx[:, nx + k * nxi: nx + (k + 1) * nxi] = np.eye(nxi)
        O[k] = (C @ coefS + Dm @ cx)[0]
        coefS = A @ coefS + B @ cx
    covU_diag = np.concatenate([np.zeros(nx), np.tile(qv, nsteps)])

    def cov(X, Y):
        r = X[:, :nx] @ S0cov @ Y[:, :nx].T
        r += (X[:, nx:] * covU_diag[nx:]) @ Y[:, nx:].T
        return r
    Soo = cov(O, O)
    Sto = cov(tgt, O)
    Stt = cov(tgt, tgt)
    return Stt - Sto @ np.linalg.solve(Soo, Sto.T)


def coord_map(name):
    """Return (2,NX) map from the firm state to the two members' scalar contrast
    coordinates (prior errors)."""
    T = np.zeros((2, NX))
    if name == "own":
        T[0, 0] = 1.0     # b: error about eta^a_t
        T[1, 5] = 1.0     # s: error about eta^b_t
    elif name == "a":
        T[0, 0] = 1.0
        T[1, 4] = 1.0
    elif name == "b":
        T[0, 1] = 1.0
        T[1, 5] = 1.0
    elif isinstance(name, tuple) and name[0] == "dir":
        th = np.deg2rad(name[1])
        c, s = np.cos(th), np.sin(th)
        T[0, 0], T[0, 1] = c, s
        T[1, 4], T[1, 5] = c, s
    else:
        raise ValueError(name)
    return T


# ---------------- contrast machinery (generic, population level) -------------
def is_diffusive(Pi, tol=1e-12):
    off = Pi - np.diag(np.diag(Pi))
    return bool(np.all(off <= tol) and np.all(Pi.sum(1) >= -tol))


def rates(Pi, Cset):
    N = Pi.shape[0]
    Cset = list(Cset)
    n = len(Cset)
    a = -(Pi - np.diag(np.diag(Pi)))
    eps = Pi.sum(1)
    phi = np.zeros(N)
    phi[Cset] = 1 / np.sqrt(n)
    xout = phi @ Pi @ phi
    aC = a[np.ix_(Cset, Cset)]
    LC = np.diag(aC.sum(1)) - aC
    MC = np.diag(eps[Cset]) + LC
    Z = np.linalg.svd(np.ones((1, n)))[2][1:].T  # basis of 1^perp
    xin = np.linalg.eigvalsh(Z.T @ MC @ Z).min()
    return xin, xout, xin / xout


def all_regions(N):
    for n in range(2, N + 1):
        for C in itertools.combinations(range(N), n):
            yield C


def baseline_mean_coupling(Pi):
    """Clause (c) without mechanism: exchangeable medium with mean coupling
    abar over all pairs and uniform leak epsbar; sup of r over regions."""
    N = Pi.shape[0]
    a = -(Pi - np.diag(np.diag(Pi)))
    eps = Pi.sum(1)
    abar = a[np.triu_indices(N, 1)].mean()
    epsbar = eps.mean()
    Pm = (epsbar + (N - 1) * abar) * np.eye(N) - abar * (np.ones((N, N)) - np.eye(N))
    best = -np.inf
    for C in all_regions(N):
        best = max(best, rates(Pm, C)[2])
    return best, abar, epsbar


def population_from_pair(Sig2):
    """Two independent identical firms: 4x4 precision blockdiag(Pi2, Pi2)."""
    Pi2 = np.linalg.inv(Sig2)
    Pi = np.zeros((4, 4))
    Pi[:2, :2] = Pi2
    Pi[2:, 2:] = Pi2
    return Pi


def selected_partition(Pi, r0, rbar):
    """Regions that are collectives at level r0 (r(C) >= r0 > max(epsratio, rbar))."""
    eps = Pi.sum(1)
    sel = []
    for C in all_regions(Pi.shape[0]):
        r = rates(Pi, C)[2]
        er = eps[list(C)].max() / eps[list(C)].mean()
        if r >= r0 and r0 > max(er, rbar):
            sel.append(C)
    return sel


def summarize_pair(Sig2, label=""):
    Pi = population_from_pair(Sig2)
    dif = is_diffusive(Pi)
    out = dict(label=label, diffusive=dif, Pi2=Pi[:2, :2].copy())
    if dif:
        out["r_pair"] = rates(Pi, (0, 1))[2]
        others = [rates(Pi, C)[2] for C in all_regions(4) if C not in [(0, 1), (2, 3)]]
        out["r_others_max"] = max(others)
        out["rbar"] = baseline_mean_coupling(Pi)[0]
    return out
