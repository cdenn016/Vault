r"""Parameterized full-model quantities of the CCP (closure, agency) for box scans.
Same construction as a3_closure_agency.py, wrapped as functions."""
import numpy as np
from scipy.optimize import minimize_scalar
from scipy.linalg import solve_discrete_lyapunov
from ccp_lib import *

NY, NE = 16, 14


def full_model(p):
    Phi, Qw, Gm = world_mats(p)
    filt = member_filters(p)
    F = p["F"]
    PU, KU = kalman_ss(F * np.eye(2), Qw, np.eye(2), p["R"] * np.eye(2))
    Qxi = np.zeros((NE, NE))
    Qxi[0:2, 0:2] = Qw
    Qxi[2, 2] = Qxi[3, 3] = p["R"]
    Qxi[4, 4] = Qxi[5, 5] = p["Rc"]
    Qxi[6:14, 6:14] = p["qc"] * np.eye(8)
    A = np.zeros((NY, NY)); B = np.zeros((NY, NE))
    A[0:4, 0:4] = Phi; B[0:4, 0:2] = Gm
    Epost = {}
    for j, (ie, own_i, lag_i, nu_i, c0) in {"b": (slice(4, 8), 2, 13, 4, 6), "s": (slice(8, 12), 3, 12, 5, 10)}.items():
        K, H = filt[j]["K"], filt[j]["H"]
        Mj = np.eye(4) - K @ H
        EpY = np.zeros((4, NY)); EpX = np.zeros((4, NE))
        EpY[:, ie] = Mj
        EpX[:, own_i] += K[:, 0]
        EpY[:, lag_i] += K[:, 1]
        EpX[:, nu_i] += K[:, 1]
        Epost[j] = (EpY, EpX)
        A[ie, :] = Phi @ EpY
        B[ie, :] = Phi @ EpX
        B[ie, c0:c0 + 4] += np.eye(4)
        B[ie, 0:2] += -Gm
    B[12, 2] = 1.0; B[13, 3] = 1.0
    MU = np.eye(2) - KU
    A[14:16, 14:16] = F * MU
    B[14:16, 2:4] = F * KU
    B[14:16, 0:2] += -np.eye(2)
    SY = solve_discrete_lyapunov(A, B @ Qxi @ B.T)
    SYX = np.zeros((NY + NE, NY + NE)); SYX[:NY, :NY] = SY; SYX[NY:, NY:] = Qxi
    return dict(p=p, Phi=Phi, filt=filt, PU=PU, KU=KU, A=A, B=B, Qxi=Qxi, SY=SY, SYX=SYX, Epost=Epost)


E2 = np.zeros((2, 4)); E2[0, 0] = 1; E2[1, 1] = 1


def alpha_I_prior_avg(m):
    Pd = np.zeros((2, NY)); Pd[:, 4:8] = 0.5 * E2; Pd[:, 8:12] += 0.5 * E2; Pd[:, 14:16] = -np.eye(2)
    return 0.5 * np.trace(np.linalg.solve(m["PU"], Pd @ m["SY"] @ Pd.T))


def alpha_I_post_avg(m):
    EbY, EbX = m["Epost"]["b"]; EsY, EsX = m["Epost"]["s"]
    KU = m["KU"]; MU = np.eye(2) - KU
    PUp = MU @ m["PU"]
    r = np.zeros((2, NY + NE))
    r[:, :NY] += 0.5 * E2 @ EbY + 0.5 * E2 @ EsY
    r[:, NY:] += 0.5 * E2 @ EbX + 0.5 * E2 @ EsX
    r[:, 14:16] += -MU
    r[:, NY + 2:NY + 4] += -KU
    return 0.5 * np.trace(np.linalg.solve(PUp, r @ m["SYX"] @ r.T))


def markov_defect_from_acf(acf, K):
    d = acf(0).shape[0]
    n = K + 2
    G = np.zeros((n * d, n * d))
    for a in range(n):
        for b in range(n):
            k = a - b
            G[a*d:(a+1)*d, b*d:(b+1)*d] = acf(k) if k >= 0 else acf(-k).T
    ti = list(range((n - 1) * d, n * d)); ci = list(range((n - 2) * d, (n - 1) * d)); pi_ = list(range(0, (n - 2) * d))

    def cv(t, c):
        Stt = G[np.ix_(t, t)]; Stc = G[np.ix_(t, c)]; Scc = G[np.ix_(c, c)]
        return Stt - Stc @ np.linalg.solve(Scc, Stc.T)
    return 0.5 * (np.log(np.linalg.det(cv(ti, ci))) - np.log(np.linalg.det(cv(ti, ci + pi_))))


def dM_inputfree_prior_avg(m, K=40):
    p = m["p"]; Phi = m["Phi"]; fb, fs = m["filt"]["b"], m["filt"]["s"]
    Mb = np.eye(4) - fb["K"] @ fb["H"]; Ms = np.eye(4) - fs["K"] @ fs["H"]
    Ai = np.zeros((10, 10))
    Ai[0:4, 0:4] = Phi @ Mb; Ai[0:4, 8] = Phi @ fb["K"][:, 1]
    Ai[4:8, 4:8] = Phi @ Ms; Ai[4:8, 9] = Phi @ fs["K"][:, 1]
    Qn = np.diag([p["qc"]] * 8 + [p["Rc"]] * 2)
    Si = solve_discrete_lyapunov(Ai, Qn)
    Py = np.zeros((2, 10)); Py[:, 0:4] = 0.5 * E2; Py[:, 4:8] = 0.5 * E2
    Apow = [np.eye(10)]
    for _ in range(K + 2):
        Apow.append(Ai @ Apow[-1])
    acf = lambda k: Py @ Apow[k] @ Si @ Py.T
    return markov_defect_from_acf(acf, K)


def agency_index(m, h=None, belief="avg_post"):
    p = m["p"]
    kap, s2 = p["kappa"], p["s2"]
    if h is None:
        h = (1 - kap) / s2     # D2: kappa = gL/(h+gL), s2 = 1/(h+gL)  => h = (1-kappa)/s2
    D_ = np.array([1.0, -1.0, 0, 0])

    def zmap(j):
        EpY, EpX = m["Epost"][j]
        r = np.zeros(NY + NE)
        r[:NY] = D_ @ EpY; r[0:4] += D_; r[NY:] = D_ @ EpX
        return r
    zb, zs = zmap("b"), zmap("s")
    if belief == "avg_post":
        zc = 0.5 * (zb + zs)
    elif belief == "prior_avg":
        zc = np.zeros(NY + NE); zc[0:4] += D_; zc[4:8] += 0.5 * D_; zc[8:12] += 0.5 * D_
    V = np.vstack([zb, zs, zc])
    Cz = V @ m["SYX"] @ V.T
    Ez2 = Cz[0, 0] + Cz[1, 1]
    klE = (s2 * 2 * h - 2 - 2 * np.log(s2 * h) + h * kap ** 2 * Ez2) / 2

    def klg(c):
        g = c / (h + 2 * c)
        cov_part = s2 * (2 * h + 2 * c) - 2 - 2 * np.log(s2) - np.log(h) - np.log(h + 2 * c)
        E_d2 = kap ** 2 * Ez2 - 2 * kap * g * (Cz[2, 0] + Cz[2, 1]) + 2 * g ** 2 * Cz[2, 2]
        E_s2 = kap ** 2 * (Cz[0, 0] + Cz[1, 1] + 2 * Cz[0, 1]) - 4 * kap * g * (Cz[2, 0] + Cz[2, 1]) + 4 * g ** 2 * Cz[2, 2]
        return 0.5 * (cov_part + h * E_d2 + c * E_s2)
    r = minimize_scalar(lambda lc: klg(np.exp(lc)), bounds=(-12, 12), method="bounded")
    return 1 - min(r.fun, klg(0.0)) / klE
