"""Deciding script 4 (extension): persistent world at the round clock of def:fw-system, eta_{t+1} = F eta_t + w_t,
all slots open, messages deliver the sender's reading one round late (y_ij(t+1) = s_j(t) + nu_ij(t+1)),
exact steady-state Kalman filter on z_t = (eta_t, eta_{t-1}); declared error = filtered error of the current state.
Expected: (i) sum formulas agree with an augmented Lyapunov solve to < 1e-10; (ii) contrast grows with F and is ~1 at F=0
(lagged readings useless); (iii) the (c)-mechanism medium (N=8, kappa=3 random of 7) has a lower whole-population contrast;
(iv) closure of the average is exact with rho(A_f) > 0."""
import numpy as np
from scipy.linalg import solve_discrete_lyapunov as dlyap
from core import contrast

n, N, kappa, s, c, s2 = 4, 8, 3, 1.0, 0.1, 1e-3


def steady_filter(F, Q):
    Phi = np.array([[F, 0.0], [1.0, 0.0]]); G = np.array([[1.0], [0.0]])
    H = np.vstack([[1.0, 0.0]] + [[0.0, 1.0]] * kappa); R = np.diag([s] + [s + c] * kappa)
    Pm = np.eye(2)
    for _ in range(5000):
        K = Pm @ H.T @ np.linalg.inv(H @ Pm @ H.T + R); Pp = Pm - K @ H @ Pm
        Pm_new = Phi @ Pp @ Phi.T + Q * G @ G.T
        if np.abs(Pm_new - Pm).max() < 1e-15: Pm = Pm_new; break
        Pm = Pm_new
    K = Pm @ H.T @ np.linalg.inv(H @ Pm @ H.T + R); Pp = Pm - K @ H @ Pm
    return Phi, (np.eye(2) - K @ H) @ Phi, K[:, [0]], K[:, [1]], Pp


def group_cov(F, M, q):
    Q = 1 - F ** 2
    Phi, A, Ko, Km, Pp = steady_filter(F, Q)
    Xoo = dlyap(A, s * Ko @ Ko.T); Xmm = dlyap(A, Km @ Km.T); Xcc = dlyap(A, s2 * np.eye(2))
    Yom = A @ dlyap(A, s * Ko @ Km.T)
    var = Xoo + kappa * (s + c) * Xmm + Xcc
    cov = q * (Yom + Yom.T) + q ** 2 * (M - 2) * s * Xmm
    return var[0, 0], cov[0, 0], A, Ko, Km, Pp


def augmented(F, with_w=True):
    """Niche of n with deterministic attention (all co-members): state (eta_t, eta_{t-1}, zhat_1..n, m*, v(t))."""
    Q = 1 - F ** 2
    Phi, A, Ko, Km, Pp = steady_filter(F, Q)
    pm = 1.0
    for _ in range(5000):
        pp = 1.0 / (1.0 / pm + n / s); pm_new = F ** 2 * pp + Q
        if abs(pm_new - pm) < 1e-16: pm = pm_new; break
        pm = pm_new
    pp = 1.0 / (1.0 / pm + n / s); ks = pp / s                  # central gain per reading
    d = 2 + 2 * n + 1 + n
    iz = lambda i: 2 + 2 * i; im = 2 + 2 * n; iv = im + 1
    nxi = 1 + n + n * (n - 1) + 2 * n
    Aa = np.zeros((d, d)); B = np.zeros((d, nxi))
    Aa[0, 0] = F; Aa[1, 0] = 1.0; B[0, 0] = 1.0                 # eta_{t+1} = F eta_t + w ; lag slot
    for i in range(n): B[iv + i, 1 + i] = 1.0                   # v(t+1) fresh
    col = 1 + n
    for i in range(n):
        r = slice(iz(i), iz(i) + 2)
        Aa[r, iz(i):iz(i) + 2] += A
        Aa[r, [0]] += Ko * F; B[r, [0]] += Ko; B[r, [1 + i]] += Ko          # own s_i(t+1) = F eta_t + w + v'_i
        for j in range(n):
            if j == i: continue
            Aa[r, [0]] += Km; Aa[r, [iv + j]] += Km; B[r, [col]] += Km; col += 1   # y_ij(t+1) = eta_t + v_j(t) + nu
    for i in range(n):
        B[iz(i):iz(i) + 2, col:col + 2] = np.eye(2); col += 2                    # computation noise
    Aa[im, im] = (1 - n * ks) * F; Aa[im, 0] += n * ks * F; B[im, 0] += n * ks
    for j in range(n): B[im, 1 + j] += ks
    Wx = np.diag([Q if with_w else 0.0] + [s] * n + [c] * (n * (n - 1)) + [s2] * (2 * n))
    S = dlyap(Aa, B @ Wx @ B.T)
    E = np.zeros((n + 1, d))
    for i in range(n): E[i, iz(i)] = 1.0; E[i, 0] = -1.0                       # e_i = zhat_i[0] - eta_t
    E[n, im] = 1.0; E[n, 0] = -1.0
    return E @ S @ E.T, Pp[0, 0], pp, max(abs(np.linalg.eigvals(A)))

print("F | niche: var cov r(A) [aug check] | medium r(V) | rho(A_f) | alpha_I (encoded N(ybar,P_f))")
for F in (0.0, 0.5, 0.9, 0.95, 0.99):
    v, cv, A, Ko, Km, Pp = group_cov(F, n, 1.0)
    rA = 1 + n * cv / (v - cv)
    Sc, Pf, Pstar, rhoA = augmented(F, with_w=False)
    chk = max(abs(Sc[0, 0] - v), abs(Sc[0, 1] - cv))
    Pi = np.linalg.inv(Sc[:n, :n]); rA2 = contrast(Pi, range(n))
    vh, cvh, *_ = group_cov(F, N, kappa / (N - 1)); rH = 1 + N * cvh / (vh - cvh)
    St, *_ = augmented(F, with_w=True)
    w = np.r_[np.full(n, 1.0 / n), -1.0]; d2 = w @ St @ w        # E (ybar_0 - m*)^2 including world-driven parts
    aI = 0.5 * (Pf / Pstar - 1 - np.log(Pf / Pstar) + d2 / Pstar)
    print(F, "|", round(v, 6), round(cv, 6), round(rA, 4), f"[{chk:.1e}, {abs(rA - rA2):.1e}]", "|", round(rH, 4), "|",
          round(rhoA, 4), "|", round(aI, 5))
