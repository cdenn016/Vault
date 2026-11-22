"""Two conventions on which C17b's step 2 rests, each shown load-bearing by an explicit instance.

(a) O2' read as invariance of the ONE-TIME law of (z_0, xi_0) only (not of the process law).
    n=3, d=1, no outside agents. Sigma_z = a P_D + a1 P_1, A = rho (P_1 + R_D), R_D = rotation by theta in D,
    E = I, Q = (1-rho^2) Sigma_z.  Then A Sigma_z A^T = rho^2 Sigma_z, so (z_0, xi_0) is invariant
    (independent, commutant covariances) but Cov(z_1, z_0) = rho(a1 P_1 + a R_D) is not.
    y_t = w0^T z_t + v_t with w0 in D (kappa = w0, W = span{w0}, dim 1 < n-1 = 2), H = 0.
(b) act noise nu correlated with the private inputs xi (setting says only 'independent across rounds').
    n=2, d=1: z_i' = rho z_i + xi_i, Q = commutant with positive correlation, y_t = 0.05 (z_1+z_2)_t + nu_t,
    nu_t = c (xi_1 - xi_2)_t + nu'_t.  Gamma_xi = 0, so the literal noise loading of y on xi_C is 0 = kappa (x) 0.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *

def report(tag, Sc, Se, f):
    Pc, Pe = np.linalg.inv(Sc), np.linalg.inv(Se)
    n = Sc.shape[0]
    C = list(range(n))
    alpha = f @ Se @ f
    print(f"[{tag}] Pi_eff diffusive: {is_diffusive(Pe)}, Pi^c diffusive: {is_diffusive(Pc)}")
    print(f"[{tag}] Pi^c =\n{np.round(Pc, 6)}")
    print(f"[{tag}] Pi_eff =\n{np.round(Pe, 6)}")
    print(f"[{tag}] |Sigma^c f - alpha f| = {np.abs(Sc @ f - alpha * f).max():.3e}, alpha = {alpha:.6f}")
    xin, xout, _, _, _ = rates(Pc, C)
    xin_e, xout_e, _, _, _ = rates(Pe, C)
    print(f"[{tag}] xi_in = {xin:.6f}, xi_in_eff = {xin_e:.6f}, 1/alpha = {1/alpha:.6f}")
    print(f"[{tag}] xi_out = {xout:.6f}, xi_out_eff = {xout_e:.6f}")
    print(f"[{tag}] r = {xin/xout:.6f}, r_eff = {xin_e/xout_e:.6f}, r <= r_eff ? {xin/xout <= xin_e/xout_e}")

# ---------------- (a)
n = 3
one = np.ones(n) / np.sqrt(n)
P1 = np.outer(one, one); PD = np.eye(n) - P1
b1 = np.array([1, -1, 0]) / np.sqrt(2); b2 = np.array([1, 1, -2]) / np.sqrt(6)
theta = np.pi / 2; rho = 0.8
RD = (np.cos(theta) * (np.outer(b1, b1) + np.outer(b2, b2))
      + np.sin(theta) * (np.outer(b2, b1) - np.outer(b1, b2)))
a, a1 = 1.0, 20.0
Sz_target = a * PD + a1 * P1
A = rho * (P1 + RD)
E = np.eye(n); Q = (1 - rho ** 2) * Sz_target
Sz = lyap(A, E @ Q @ E.T)
print("(a) one-time law: Sigma_z commutant residual", np.abs(Sz - Sz_target).max())
lag1 = A @ Sz
print("(a) Cov(z_1,z_0) =\n", np.round(lag1, 4), "\n   commutant? (equal diag & equal offdiag):",
      np.ptp(np.diag(lag1)) < 1e-12 and np.ptp(lag1[~np.eye(n, dtype=bool)]) < 1e-12)
w0 = b1
G = w0[None, :]; H = np.zeros((1, n)); Rv = np.array([[4.0]])
err, _, _ = smoother_cov(A, E, Q, G, H, Rv, M=2048)
f = b2  # unit, in D, orthogonal to W = span{w0}
report("a", (err + err.T) / 2, Sz, f)

# ---------------- (b)
n = 2
rho = 0.7
Q = np.array([[1.0, 0.8], [0.8, 1.0]])
A = rho * np.eye(n); E = np.eye(n)
c = 1.0
# nu_t = c (xi_1 - xi_2)_t + nu'_t  =>  effective same-time loading of y on xi is c(1,-1); nu' variance 0.5
G = 0.05 * np.ones((1, n)); Heff = c * np.array([[1.0, -1.0]]); Rv = np.array([[0.5]])
Sz = lyap(A, E @ Q @ E.T)
err, _, _ = smoother_cov(A, E, Q, G, Heff, Rv, M=2048)
f = np.array([1.0, -1.0]) / np.sqrt(2)
report("b", (err + err.T) / 2, Sz, f)
