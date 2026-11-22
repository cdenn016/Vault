r"""a6: independent numerical test of the candidate's Theorem O.

Exchangeable isolated niche of n members: scalar AR(1) world eta (F, Q), each
member senses eta (noise R) and relays its raw reading to all others with one-
round latency through receiver-specific noise Rc; exact steady-state Kalman
filters on (eta_t, eta_{t-1}) with computation noise qc; acts with
heterogeneous, mixed-sign gains u_i = -g_i m_i^+[0] + eps_i on a renewed outcome
eta^Z_{t+1} = sum_i u_i + w^Z that nobody senses.  Contrast coordinate: prior
error about eta_t.  Theorem O (n >= 3, dim span{P_D g} = 1 < n-1) claims: if
Pi^c is diffusive then r(C) <= r_eff(C).

Declared expectations (before running):
 E1 n = 3 and n = 4: zero violations r > r_eff (1 + 1e-9) among diffusive draws.
 E2 n = 2 mixed-sign gains (NOT covered): violations occur (r > r_eff) in a
    positive fraction of diffusive draws -- this is the control that the test
    can detect a gain.
 E3 n = 2 same-sign gains (the candidate's conjecture): zero violations.
"""
import sys
import numpy as np
from scipy.linalg import solve_discrete_are, solve_discrete_lyapunov


def build(n, F, Q, R, Rc, qc, g, s2, QZ):
    Phi = np.array([[F, 0.0], [1.0, 0.0]])
    Qtot = np.array([[Q, 0.0], [0.0, 0.0]]) + qc * np.eye(2)
    H = np.zeros((n, 2)); H[0, 0] = 1.0; H[1:, 1] = 1.0
    Rm = np.diag([R] + [R + Rc] * (n - 1))
    P = solve_discrete_are(Phi.T, H.T, Qtot, Rm)
    K = P @ H.T @ np.linalg.inv(H @ P @ H.T + Rm)
    M = np.eye(2) - K @ H
    # state: z_i (2 each) then vlag_i ; noise: v_i (n), nu_ij (n*(n-1)), c_i (2n), eps_i (n), wZ
    nx = 3 * n
    pairs = [(i, j) for i in range(n) for j in range(n) if i != j]
    nxi = n + len(pairs) + 2 * n + n + 1
    iv = lambda i: i
    inu = {pr: n + k for k, pr in enumerate(pairs)}
    ic = lambda i: n + len(pairs) + 2 * i
    ie = lambda i: n + len(pairs) + 2 * n + i
    iw = nxi - 1
    qv = np.zeros(nxi)
    qv[:n] = R; qv[n:n + len(pairs)] = Rc; qv[n + len(pairs):n + len(pairs) + 2 * n] = qc
    qv[n + len(pairs) + 2 * n: n + len(pairs) + 3 * n] = s2; qv[iw] = QZ
    A = np.zeros((nx, nx)); B = np.zeros((nx, nxi)); C = np.zeros((1, nx)); Dm = np.zeros((1, nxi))
    for i in range(n):
        ZpS = np.zeros((2, nx)); ZpX = np.zeros((2, nxi))
        ZpS[:, 2 * i:2 * i + 2] = M
        ZpX[:, iv(i)] += K[:, 0]
        col = 1
        for j in range(n):
            if j == i:
                continue
            ZpS[:, 2 * n + j] += K[:, col]
            ZpX[:, inu[(i, j)]] += K[:, col]
            col += 1
        A[2 * i:2 * i + 2] = Phi @ ZpS
        B[2 * i:2 * i + 2] = Phi @ ZpX
        B[2 * i:2 * i + 2, ic(i):ic(i) + 2] += np.eye(2)
        C[0] += -g[i] * ZpS[0]
        Dm[0] += -g[i] * ZpX[0]
        Dm[0, ie(i)] += 1.0
    Dm[0, iw] += 1.0
    for i in range(n):
        B[2 * n + i, iv(i)] = 1.0
    T = np.zeros((n, nx))
    for i in range(n):
        T[i, 2 * i] = 1.0
    return A, B, C, Dm, qv, T


def window_condition(A, B, C, Dm, qv, T, L=40):
    nx, nxi = B.shape
    S0 = solve_discrete_lyapunov(A, B @ np.diag(qv) @ B.T)
    nsteps = 2 * L + 1
    dimU = nx + nxi * nsteps
    coef = np.zeros((nx, dimU)); coef[:, :nx] = np.eye(nx)
    O = np.zeros((nsteps, dimU)); tgt = None
    for k in range(nsteps):
        if k == L:
            tgt = T @ coef
        cx = np.zeros((nxi, dimU)); cx[:, nx + k * nxi:nx + (k + 1) * nxi] = np.eye(nxi)
        O[k] = (C @ coef + Dm @ cx)[0]
        coef = A @ coef + B @ cx
    dg = np.tile(qv, nsteps)
    cov = lambda X, Y: X[:, :nx] @ S0 @ Y[:, :nx].T + (X[:, nx:] * dg) @ Y[:, nx:].T
    Soo = cov(O, O); Sto = cov(tgt, O); Stt = cov(tgt, tgt)
    return Stt - Sto @ np.linalg.solve(Soo, Sto.T), T @ S0 @ T.T


def contrast_whole(Sig):
    Pi = np.linalg.inv(Sig)
    off = Pi - np.diag(np.diag(Pi))
    dif = bool(np.all(off <= 1e-12) and np.all(Pi.sum(1) >= -1e-12))
    n = Pi.shape[0]
    a = -off; eps = Pi.sum(1)
    phi = np.ones(n) / np.sqrt(n)
    xout = phi @ Pi @ phi
    Lc = np.diag(a.sum(1)) - a
    Z = np.linalg.svd(np.ones((1, n)))[2][1:].T
    xin = np.linalg.eigvalsh(Z.T @ (np.diag(eps) + Lc) @ Z).min()
    return dif, xin / xout


rng = np.random.default_rng(int(sys.argv[1]) if len(sys.argv) > 1 else 4)
ndraw = int(sys.argv[2]) if len(sys.argv) > 2 else 150
for n, sign_mode in ((3, "mixed"), (4, "mixed"), (2, "mixed"), (2, "same")):
    viol, ndiff, maxgain = 0, 0, -np.inf
    for d in range(ndraw):
        F = rng.uniform(0.5, 0.95); Q = rng.uniform(0.01, 0.2); R = rng.uniform(0.3, 3.0)
        Rc = 10 ** rng.uniform(-2, 0.5); qc = 10 ** rng.uniform(-5, -3)
        s2 = 10 ** rng.uniform(-3, -1); QZ = 10 ** rng.uniform(-3, -0.3)
        if sign_mode == "mixed":
            g = rng.uniform(-1.5, 1.5, n)
            if n == 2 and g[0] * g[1] > 0:
                g[1] = -g[1]
        else:
            g = rng.uniform(0.05, 1.5, n)
        A, B, C, Dm, qv, T = build(n, F, Q, R, Rc, qc, g, s2, QZ)
        if max(abs(np.linalg.eigvals(A))) >= 1:
            continue
        Sc, Se = window_condition(A, B, C, Dm, qv, T)
        dif, r = contrast_whole(Sc)
        dife, re = contrast_whole(Se)
        if not (dif and dife):
            continue
        ndiff += 1
        rel = r / re - 1
        maxgain = max(maxgain, rel)
        if rel > 1e-9:
            viol += 1
    print("n=%d %-5s gains: diffusive draws %d, violations r > r_eff: %d, largest relative gain r/r_eff-1 = %.3e"
          % (n, sign_mode, ndiff, viol, maxgain))
