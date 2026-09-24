"""L18: attention crosswalk checks.

 (a) PIFB2 raw-conductance pooling eq:rg_inter_cluster, kappa^R_IJ = sum_i w_i sum_j kappa_ij,
     equals the Theory's evidence-weighted block row (prop:rg-attention-single-edge-weights with
     c~_i = 1, a_{i|I} = w_i), and differs from the per-receiver prior-weighted collapse
     (prop:rg-attention-per-receiver-collapse) unless the row normalizers Z_i agree.
 (b) PIFB2 value aggregation mu_hat = sum_j beta_ij Omega_ij mu_j is the sharp-record limit of the
     Theory's exact receiver update (prop:obs-selective-receiver-update (c)) with S^Q=U_i^{-1},
     S^K=U_j^{-1}: value map -> Omega_ij and the skip weight Sigma+ Sigma^{-1} -> 0.
 (c) Law-point energy is not an expected sample energy: strict convexity of q -> KL(q_i||q) along a
     mixture (Theory prop:prob-law-point-energy), 1D Gaussian mixture by quadrature.
 (d) Clock-dissipation identity (PIFB2 eq:clock_dissipation; Theory eq:hist-vfe-clock-rate/-dissipation).
"""
import numpy as np

rng = np.random.default_rng(3)

# (a)
nI, nsrc, tau = 3, 5, 0.7
E = rng.uniform(0, 3, size=(nI, nsrc))
pi = rng.dirichlet(np.ones(nsrc), size=nI)
w = rng.dirichlet(np.ones(nI))
kappa = pi * np.exp(-E / tau)
Z = kappa.sum(1)
beta = kappa / Z[:, None]
blocks = [[0, 1], [2, 3, 4]]
kR = np.array([sum(w[i] * kappa[i, J].sum() for i in range(nI)) for J in blocks])
betaR = kR / kR.sum()
alpha_ev = w * Z / (w * Z).sum()
beta_ev = np.array([sum(alpha_ev[i] * beta[i, J].sum() for i in range(nI)) for J in blocks])
beta_pw = np.array([sum(w[i] * beta[i, J].sum() for i in range(nI)) for J in blocks])
print(f"(a) PIFB2 conductance row {betaR}, Theory evidence-weighted {beta_ev}, diff {np.abs(betaR-beta_ev).max():.2e}")
print(f"    per-receiver prior-weighted collapse {beta_pw}, differs by {np.abs(betaR-beta_pw).max():.3e} (Z_i = {Z})")

# (b)
K = 3
def rgl():
    A = rng.normal(size=(K, K)); return A if np.linalg.det(A) > 0.3 else rgl()
Ui, Uj = rgl(), rgl()
A = rng.normal(size=(K, K)); Sig_i = A @ A.T + np.eye(K)
SQ, SK = np.linalg.inv(Ui), np.linalg.inv(Uj)
Om = Ui @ np.linalg.inv(Uj)
for wprec in (1e0, 1e3, 1e6):
    Wt = wprec * np.eye(K)
    Splus = np.linalg.inv(np.linalg.inv(Sig_i) + SQ.T @ Wt @ SQ)
    Lval = Splus @ SQ.T @ Wt @ SK
    skip = Splus @ np.linalg.inv(Sig_i)
    print(f"(b) W~={wprec:.0e}: |L_val - Omega_ij| = {np.abs(Lval-Om).max():.3e}, |skip| = {np.abs(skip).max():.3e}")

# (c)
x = np.linspace(-30, 30, 200001); dx = x[1] - x[0]
npdf = lambda m, s: np.exp(-(x - m) ** 2 / (2 * s * s)) / np.sqrt(2 * np.pi * s * s)
qi, p1, p2 = npdf(0.0, 1.0), npdf(1.0, 1.5), npdf(-2.0, 0.8)
klq = lambda p: np.sum(qi * (np.log(qi + 1e-300) - np.log(p + 1e-300))) * dx
s = 0.4
lhs = klq(s * p1 + (1 - s) * p2); rhs = s * klq(p1) + (1 - s) * klq(p2)
print(f"(c) KL(q||mix) = {lhs:.6f} < s KL(q||p1)+(1-s)KL(q||p2) = {rhs:.6f}; strict gap {rhs-lhs:.4e}")

# (d) metric-preconditioned gradient flow on a quadratic, G SPD constant
n = 4
B = rng.normal(size=(n, n)); H = B @ B.T + np.eye(n)
C = rng.normal(size=(n, n)); G = C @ C.T + np.eye(n)
eta = 0.37
xv = rng.normal(size=n)
grad = H @ xv
xdot = -eta * np.linalg.solve(G, grad)
speed2 = xdot @ G @ xdot
dFdt = grad @ xdot
print(f"(d) (dtau/dt)^2 = {speed2:.12f}, eta(-dF/dt) = {-eta*dFdt:.12f}, diff {abs(speed2+eta*dFdt):.1e}")
