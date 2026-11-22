r"""Finite-window check of Lemma M in Setting G.

Model (all linear-Gaussian, started at t=0 from x_0 = 0, eta_0 ~ N(0,1)):
    a_t      = Gamma x_t + P eta_t + Gx xi_t + nu_t
    eta_{t+1}= F eta_t + B a_t + w_t
    x_{t+1}  = A x_t + G1 eta_{t+1} + G0 eta_t + H beta_t + E xi_t
beta = shared (sender-side broadcast) noise, conditioned on by the definition.
Private process: z_{t+1} = A z_t + E xi_t, z_0 = 0,
    ytil_t = B Gamma z_t + B Gx xi_t + B nu_t + w_t.
Checks, at a middle time tau:
 (1) Cov(S x_tau | eta_{0..T+1}, beta_{0..T}) == Cov(S z_tau | ytil_{0..T})      (full model)
 (2) Cov(S x_tau | eta_{0..T+1}) without beta differs when H != 0            (beta needed)
 (3) N_eff: eta driven by independent forcing; Cov(S x_tau | eta, beta) == Cov(S z_tau)
 (4) Side check: F = 1 world stabilized by acts (closed loop stable, null world unit root).
"""
import os
os.environ.setdefault("OMP_NUM_THREADS", "1")
import numpy as np

rng = np.random.default_rng(7)
nag, d = 2, 2            # agents, local state dim
nx = nag * d
nxi = 4                  # private inputs (2 per agent)
na = nag                 # one scalar act per agent
T = 40
tau = 20

def stable(M, rho):
    ev = np.max(np.abs(np.linalg.eigvals(M)))
    return M * (rho / ev)

A = stable(rng.normal(size=(nx, nx)), 0.6)
Gamma = 0.15 * rng.normal(size=(na, nx))
P = 0.3 * rng.normal(size=(na, 1))
Gx = rng.normal(size=(na, nxi))
B = rng.normal(size=(1, na))
F = np.array([[0.7]])
G1 = 0.2 * rng.normal(size=(nx, 1))
G0 = 0.2 * rng.normal(size=(nx, 1))
H = 0.5 * rng.normal(size=(nx, 1))
E = rng.normal(size=(nx, nxi))
S = rng.normal(size=(nag, nx))
qw, qnu, qb = 0.5, 0.3, 0.7

# closed-loop matrix of (eta, x): check stability
Mcl = np.block([[F + B @ P, B @ Gamma],
                [G1 @ (F + B @ P) + G0, A + G1 @ B @ Gamma]])
print("closed-loop spectral radius:", np.max(np.abs(np.linalg.eigvals(Mcl))))

# noise index layout: eta0 | w_t | xi_t | nu_t | beta_t | forcing_t (null only)
nW, nXI, nNU, nB, nFo = T + 1, (T + 1) * nxi, (T + 1) * na, T + 1, (T + 1) * na
off = {}
k = 0
for name, size in [("eta0", 1), ("w", nW), ("xi", nXI), ("nu", nNU), ("beta", nB), ("fo", nFo)]:
    off[name] = k
    k += size
Ntot = k

def unit(name, t, dim, scale):
    M = np.zeros((dim, Ntot))
    base = off[name] + t * dim
    M[:, base:base + dim] = np.eye(dim) * np.sqrt(scale)
    return M

def run(null):
    eta = [unit("eta0", 0, 1, 1.0)]
    x = [np.zeros((nx, Ntot))]
    z = [np.zeros((nx, Ntot))]
    ytil = []
    for t in range(T + 1):
        xi = unit("xi", t, nxi, 1.0)
        nu = unit("nu", t, na, qnu)
        w = unit("w", t, 1, qw)
        beta = unit("beta", t, 1, qb)
        a = Gamma @ x[t] + P @ eta[t] + Gx @ xi + nu
        if null:
            forcing = unit("fo", t, na, 1.0)   # exogenous, independent of xi
            eta_next = F @ eta[t] + B @ forcing + w
        else:
            eta_next = F @ eta[t] + B @ a + w
        x_next = A @ x[t] + G1 @ eta_next + G0 @ eta[t] + H @ beta + E @ xi
        ytil.append(B @ Gamma @ z[t] + B @ Gx @ xi + B @ nu + w)
        z.append(A @ z[t] + E @ xi)
        eta.append(eta_next)
        x.append(x_next)
    return eta, x, z, ytil

def ccov(Lx, Ly):
    Sxx = Lx @ Lx.T
    if Ly is None:
        return Sxx
    Sxy = Lx @ Ly.T
    Syy = Ly @ Ly.T
    return Sxx - Sxy @ np.linalg.solve(Syy, Sxy.T)

for null in (False, True):
    eta, x, z, ytil = run(null)
    Leta = np.vstack(eta)                       # eta_0..eta_{T+1}
    Lbeta = np.vstack([unit("beta", t, 1, qb) for t in range(T + 1)])
    Ly = np.vstack(ytil)
    lhs = ccov(S @ x[tau], np.vstack([Leta, Lbeta]))
    lhs_nobeta = ccov(S @ x[tau], Leta)
    rhs_cond = ccov(S @ z[tau], Ly)
    rhs_marg = ccov(S @ z[tau], None)
    tag = "N_eff" if null else "full "
    print(f"[{tag}] Cov(Sx|eta,beta) =\n{lhs}")
    print(f"[{tag}] max|Cov(Sx|eta,beta) - Cov(Sz|ytil)| = {np.max(np.abs(lhs - rhs_cond)):.3e}")
    print(f"[{tag}] max|Cov(Sx|eta,beta) - Cov(Sz)|      = {np.max(np.abs(lhs - rhs_marg)):.3e}")
    print(f"[{tag}] max|Cov(Sx|eta only) - Cov(Sx|eta,beta)| = {np.max(np.abs(lhs_nobeta - lhs)):.3e}")
    if not null:
        Sig_c = lhs
    else:
        Sig_eff = lhs
D = Sig_eff - Sig_c
print("eigenvalues of Sigma_eff - Sigma_c:", np.linalg.eigvalsh(D))
print("eigenvalues of Pi_c - Pi_eff:", np.linalg.eigvalsh(np.linalg.inv(Sig_c) - np.linalg.inv(Sig_eff)))

# (4) unit-root world stabilized by acts
F1, g, k1 = 1.0, 0.5, 0.6
# eta' = eta + a + w, a = -g mu, mu' = mu + a + k1(eta' - (mu + a) + noise)  (agent filter)
Mcl1 = np.array([[1.0, -g], [k1 * 1.0, (1 - k1) * (1 - g) + k1 * (-g)]])
print("unit-root example: closed-loop eigenvalues", np.linalg.eigvals(Mcl1), " null world F =", F1)
