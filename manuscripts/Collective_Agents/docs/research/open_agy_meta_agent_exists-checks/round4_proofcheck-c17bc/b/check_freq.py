"""Validate the frequency-domain smoother against direct finite-window Gaussian conditioning,
including H != 0 (same-time noise loading) so the z-xi cross-covariance at negative lags enters."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *

rng = np.random.default_rng(7)
nz, nx, p = 4, 3, 2
A = rng.normal(size=(nz, nz)); A *= 0.8 / max(abs(np.linalg.eigvals(A)))
E = rng.normal(size=(nz, nx)); Bq = rng.normal(size=(nx, nx)); Q = Bq @ Bq.T
G = rng.normal(size=(p, nz)); H = rng.normal(size=(p, nx)); Br = rng.normal(size=(p, p)); Rv = 0.3 * Br @ Br.T + 0.1 * np.eye(p)
err_f, Sz_f, im = smoother_cov(A, E, Q, G, H, Rv, M=2048)
Sz = lyap(A, E @ Q @ E.T)
print("Cov(z0) quadrature vs Lyapunov:", np.abs(Sz_f - Sz).max(), " imag residue", im)

T = 70
times = list(range(-T, T + 1))
def Czz(t, s):  # Cov(z_t, z_s)
    k = t - s
    return np.linalg.matrix_power(A, k) @ Sz if k >= 0 else Sz @ np.linalg.matrix_power(A.T, -k)
def Czx(t, s):  # Cov(z_t, xi_s)
    k = t - s
    return np.linalg.matrix_power(A, k - 1) @ E @ Q if k >= 1 else np.zeros((nz, nx))
def Cyy(t, s):
    # Cov(H xi_t, G z_s) = H Cov(xi_t, z_s) = H Czx(s,t)^T
    c = G @ Czz(t, s) @ G.T + G @ Czx(t, s) @ H.T + H @ Czx(s, t).T @ G.T
    if t == s:
        c = c + H @ Q @ H.T + Rv
    return c
Y = np.block([[Cyy(t, s) for s in times] for t in times])
Zy = np.hstack([Czz(0, s) @ G.T + Czx(0, s) @ H.T for s in times])
err_d = Sz - Zy @ np.linalg.solve(Y, Zy.T)
print("smoother error: freq vs direct (T=70) max abs diff:", np.abs(err_f - err_d).max())
print("smoother error diag (freq):", np.round(np.diag(err_f), 6))
