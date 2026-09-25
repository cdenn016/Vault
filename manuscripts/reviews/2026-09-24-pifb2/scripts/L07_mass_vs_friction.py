r"""L07: what the actual first-order flow says about 'mass' (PIFB2.tex 1325-1532, 1755-1764).

Checks
 (a) isolated Gaussian agent, F = KL(q||p): linearized natural-gradient flow at q=p has rate eta
     for every prior precision s (mean and covariance), Euclidean flow has rate eta*s;
     static compliance to a constant force f is H^{-1} f = Sigma_p f.
 (b) coupled agents, full (receiver+sender) gradient, frozen beta, GL transports: Jacobian of the
     natural-gradient flow -eta G^{-1} H has real spectrum (no oscillation frequency omega exists).
 (c) receiver-only truncation with a rotating holonomy on a directed 3-cycle: complex eigenvalues
     (the only place an 'omega' appears is the nonpotential field the paper sets aside).
"""
import numpy as np

rng = np.random.default_rng(3)
eta = 1.0

print("== (a) isolated agent ==")
for s in [1.0, 10.0, 1e3]:
    Lp = s * np.array([[2.0, 0.3], [0.3, 1.0]])
    Sp = np.linalg.inv(Lp)
    # mean: nat grad  mu' = -eta Sigma Lp (mu-mubar), at Sigma = Sp  -> -eta I
    Jn = -eta * Sp @ Lp
    Je = -eta * Lp
    # covariance: Sigma' = -2 eta Sigma (1/2)(Lp - Sigma^{-1}) Sigma ; FD Jacobian on Sym_2 at Sigma=Sp
    def fS(S):
        return -eta * S @ (Lp - np.linalg.inv(S)) @ S
    h = 1e-7 / s
    basis = [np.array([[1.0, 0], [0, 0]]), np.array([[0, 0], [0, 1.0]]), np.array([[0, 1.0], [1.0, 0]]) / np.sqrt(2)]
    J = np.zeros((3, 3))
    for a, E in enumerate(basis):
        d = (fS(Sp + h * E) - fS(Sp - h * E)) / (2 * h)
        for b, Eb in enumerate(basis):
            J[b, a] = np.sum(d * Eb)
    print(f"s={s:g}: nat-grad mean rates {np.round(-np.linalg.eigvals(Jn).real, 6)}, cov rates {np.round(-np.linalg.eigvals(J).real, 6)}; "
          f"Euclid mean rates {np.round(-np.linalg.eigvals(Je).real, 3)}; compliance ||H^-1|| = {np.linalg.norm(Sp, 2):.3g}")

print("== (b) coupled full-gradient flow: spectrum of G^{-1}H ==")
K, N = 2, 3


def hess_full(mu_flat, Lam, beta, Om, Lp):
    """Mean-sector Hessian of F = sum_i 1/2|mu_i-mubar_i|^2_{Lp_i} + sum_ij beta_ij 1/2|mu_i - Om_ij mu_j|^2_{tilde Lam_j}."""
    H = np.zeros((N * K, N * K))
    for i in range(N):
        H[i*K:(i+1)*K, i*K:(i+1)*K] += Lp[i]
        for j in range(N):
            if i == j:
                continue
            Oinv = np.linalg.inv(Om[i][j])
            Lt = Oinv.T @ Lam[j] @ Oinv
            # d/dmu of 1/2 (mu_i - O mu_j)^T Lt (mu_i - O mu_j)
            B = np.zeros((K, N * K)); B[:, i*K:(i+1)*K] = np.eye(K); B[:, j*K:(j+1)*K] = -Om[i][j]
            H += beta[i, j] * B.T @ Lt @ B
    return H


maxim = 0
for t in range(2000):
    Lam = [np.diag(rng.uniform(0.1, 10, K)) for _ in range(N)]
    Lp = [np.diag(rng.uniform(0.1, 10, K)) for _ in range(N)]
    beta = rng.random((N, N)); np.fill_diagonal(beta, 0); beta /= beta.sum(1, keepdims=True)
    Om = [[np.eye(K) + 0.5 * rng.normal(size=(K, K)) for _ in range(N)] for _ in range(N)]
    H = hess_full(None, Lam, beta, Om, Lp)
    Ginv = np.zeros((N*K, N*K))
    for i in range(N):
        Ginv[i*K:(i+1)*K, i*K:(i+1)*K] = np.linalg.inv(Lam[i])
    ev = np.linalg.eigvals(-eta * Ginv @ H)
    maxim = max(maxim, np.abs(ev.imag).max())
print("max |Im eig| of -eta G^{-1} H over 2000 random GL instances (asymmetric beta):", maxim)

print("== (c) receiver-only field, directed 3-cycle, SO(2) holonomy ==")
th = 2 * np.pi / 3 * 0.9
R = lambda a: np.array([[np.cos(a), -np.sin(a)], [np.sin(a), np.cos(a)]])
Om = [[np.eye(2)] * 3 for _ in range(3)]
Om = [[np.eye(2) for _ in range(3)] for _ in range(3)]
Om[0][1] = R(th); Om[1][2] = R(th); Om[2][0] = R(th)
beta = np.zeros((3, 3)); beta[0, 1] = beta[1, 2] = beta[2, 0] = 1.0
Lam = [np.eye(2)] * 3; lp = 0.1
J = np.zeros((6, 6))
for i in range(3):
    J[2*i:2*i+2, 2*i:2*i+2] -= lp * np.eye(2)
    for j in range(3):
        if beta[i, j] > 0:
            J[2*i:2*i+2, 2*i:2*i+2] -= beta[i, j] * np.eye(2)
            J[2*i:2*i+2, 2*j:2*j+2] += beta[i, j] * Om[i][j]
ev = np.linalg.eigvals(J)
print("receiver-only Jacobian eigenvalues:", np.round(ev, 4))
H = hess_full(None, Lam, beta, Om, [lp * np.eye(2)] * 3)
print("full-gradient Jacobian eigenvalues:", np.round(np.linalg.eigvals(-H), 4))

print("== (d) harmonic frequencies under the kinetic-metric postulate (PIFB2 1500-1512) ==")
import sympy as sp
a, b, c, lam_p, k_c = sp.symbols('a b c lambda_p k_c', positive=True)
M = sp.Matrix([[a, b], [b, c]])          # generic symmetric inertia = stiffness = frozen-beta Hessian
w2 = sp.symbols('w2')
print("postulate (inertia = stiffness = M): det(K - w^2 M) = 0 roots:", sp.solve(sp.factor((M - w2 * M).det()), w2))
# alternative reading at 1330: inertia = bare prior precision lam_p, stiffness = lam_p + coupling k_c
print("bare-mass reading: w^2 =", sp.simplify((lam_p + k_c) / lam_p), "-> ~ k_c/lam_p only when k_c >> lam_p")

print("== (e) state-dependent alpha: rank-one residual and definiteness thresholds (PIFB2 1515-1520) ==")
x, lam, c0, b0 = sp.symbols('x lambda c_0 b_0', positive=True)
D = lam * x**2 / 2                                   # KL for a mean displacement at matched covariance (1D)
alpha = c0 / (b0 + D)
reduced = c0 * sp.log(b0 + D)                        # reduced objective after optimizing alpha (d/dD = alpha)
h_red = sp.simplify(sp.diff(reduced, x, 2))
claimed = alpha * lam - alpha**2 / c0 * (lam * x)**2
print("reduced Hessian - claimed rank-one form:", sp.simplify(h_red - claimed))
Dv = sp.symbols('D', positive=True)
print("reduced Hessian sign factor (in D):", sp.factor(sp.simplify((h_red / (alpha * lam)).subs(x, sp.sqrt(2 * Dv / lam)))))
h_un = sp.simplify(sp.diff(alpha * D, x, 2))
print("alpha*D Hessian sign factor (in D):", sp.factor(sp.simplify((h_un * (b0 + D)**3 / (c0 * b0 * lam)).subs(x, sp.sqrt(2 * Dv / lam)))))
