"""L01: Regime-I frame removability, untied carving in gauge-fixed variables, local right redundancy vs frame-twist form,
parent-frame cancellation, GL(2,C) worked example. PIFB2.tex 194-208, 341, 1095-1133, 1575, 1898-1976."""
import numpy as np
from scipy.linalg import expm, sqrtm
rng = np.random.default_rng(1)
inv = np.linalg.inv
K, N = 3, 5
def kl(m1, S1, m2, S2):
    k = len(m1); S2i = inv(S2); dm = m2 - m1
    return 0.5 * (np.log(np.linalg.det(S2) / np.linalg.det(S1)) + np.trace(S2i @ S1) + dm @ S2i @ dm - k)
def spd():
    X = rng.standard_normal((K, K)); return X @ X.T + K * np.eye(K)
mu = [rng.standard_normal(K) for _ in range(N)]; Sig = [spd() for _ in range(N)]
U = [expm(0.7 * rng.standard_normal((K, K))) for _ in range(N)]
def energies(mu, Sig, U):
    E = np.zeros((N, N))
    for i in range(N):
        for j in range(N):
            O = U[i] @ inv(U[j]); E[i, j] = kl(mu[i], Sig[i], O @ mu[j], O @ Sig[j] @ O.T)
    return E
E = energies(mu, Sig, U)
mup = [inv(U[i]) @ mu[i] for i in range(N)]; Sigp = [inv(U[i]) @ Sig[i] @ inv(U[i]).T for i in range(N)]
Ep = energies(mup, Sigp, [np.eye(K)] * N)
print("(R1) all pair energies E_ij(q,U) vs E_ij(U^-1 q, I): max diff", np.abs(E - Ep).max(), "; max E =", E.max())
tau = 1.0
beta = lambda E: np.exp(-E / tau) / np.exp(-E / tau).sum(1, keepdims=True)
print("     attention rows beta identical:", np.abs(beta(E) - beta(Ep)).max())
# untied carving in gauge-fixed variables
i, j = 0, 1
x_i = inv(U[i]) @ mu[i]; k_j = U[j].T @ inv(Sig[j]) @ mu[j]; Hj = U[j].T @ inv(Sig[j]) @ U[j]; y_j = inv(U[j]) @ mu[j]
print("(R2) x_i^T k_j vs x_i^T H_j y_j (gauge-fixed precision times gauge-fixed mean):", abs(x_i @ k_j - x_i @ Hj @ y_j))
print("     H_j = inverse of gauge-fixed covariance U_j^-1 Sigma_j U_j^-T:", np.abs(Hj - inv(inv(U[j]) @ Sig[j] @ inv(U[j]).T)).max(),
      "; H_j symmetric:", np.abs(Hj - Hj.T).max(), "; min eig:", np.linalg.eigvalsh(Hj).min())
Mij = inv(U[i]).T @ U[j].T @ inv(Sig[j])
print("     mixed-frame M_ij asymmetry |M-M^T|:", np.abs(Mij - Mij.T).max(), "; mu_i^T M_ij mu_j - x_i^T H_j y_j:", abs(mu[i] @ Mij @ mu[j] - x_i @ Hj @ y_j))
# full KL general decomposition check (eq:full_kl_general)
P_i = inv(U[i]) @ Sig[i] @ inv(U[i]).T; r_j = mu[j] @ inv(Sig[j]) @ mu[j]
rhs = 0.5 * (np.log(np.linalg.det(Sig[j])) - np.log(np.linalg.det(Sig[i])) + 2 * np.log(abs(np.linalg.det(U[i]))) - 2 * np.log(abs(np.linalg.det(U[j])))
             - K + np.trace(Hj @ P_i) + x_i @ Hj @ x_i - 2 * x_i @ k_j + r_j)
print("(R3) eq:full_kl_general residual:", abs(E[i, j] - rhs))
# parent-frame cancellation: constituent priors and parent-level KL independent of U_I
mI, SI = rng.standard_normal(K), spd()
UI1, UI2 = expm(rng.standard_normal((K, K))), expm(rng.standard_normal((K, K)))
def prior(i, UI, muI, SigI):
    O = U[i] @ inv(UI); return O @ muI, O @ SigI @ O.T
muI2, SI2 = UI2 @ inv(UI1) @ mI, UI2 @ inv(UI1) @ SI @ (UI2 @ inv(UI1)).T  # same frame-free (m,S)
p1 = prior(2, UI1, mI, SI); p2 = prior(2, UI2, muI2, SI2)
print("(R4) constituent prior under two parent frames with fixed frame-free (m,S): mean diff", np.abs(p1[0] - p2[0]).max(), " cov diff", np.abs(p1[1] - p2[1]).max())
# local (c-dependent) diagonal right translation: Omega invariant, frame-twist form not
cs = np.linspace(0, 1, 41); dc = cs[1] - cs[0]
Aa = [0.5 * rng.standard_normal((K, K)) for _ in range(3)]; Ab = [0.5 * rng.standard_normal((K, K)) for _ in range(3)]
Ufun = lambda A, c: expm(A[0] + c * A[1] + c * c * A[2])
U1 = np.array([Ufun(Aa, c) for c in cs]); U2 = np.array([Ufun(Ab, c) for c in cs])
gfun = np.array([inv(Ufun(Aa, c)) for c in cs])  # g(c) = U1(c)^-1
U1g = np.array([U1[n] @ gfun[n] for n in range(len(cs))]); U2g = np.array([U2[n] @ gfun[n] for n in range(len(cs))])
Om = np.array([U1[n] @ inv(U2[n]) for n in range(len(cs))]); Omg = np.array([U1g[n] @ inv(U2g[n]) for n in range(len(cs))])
def twist(Ua, n):
    dU = (Ua[n + 1] - Ua[n - 1]) / (2 * dc); A = inv(Ua[n]) @ dU; return np.trace(A @ A)
n0 = 20
print("(R5) c-dependent diagonal right translation: max |Omega_12(c) change|:", np.abs(Om - Omg).max())
print("     agent-1 frame-twist tr(A_c A_c): before", twist(U1, n0), " after", twist(U1g, n0), "; agent-2:", twist(U2, n0), "->", twist(U2g, n0))
# GL(2,C) worked example: imaginary temporal component removable by complexified right translation; reality of transport
T = np.diag([1., -1.])
psi_t = lambda t: 0.8 * t + 0.3 * t**2
psi_x = lambda x: 0.5 * x
def Ufr(t, x, off=0.0): return expm((1j * (psi_t(t) + off) + psi_x(x)) * T)
t0, x0, e = 0.4, 0.2, 1e-6
def G(Uf):
    At = inv(Uf(t0, x0)) @ (Uf(t0 + e, x0) - Uf(t0 - e, x0)) / (2 * e)
    Ax = inv(Uf(t0, x0)) @ (Uf(t0, x0 + e) - Uf(t0, x0 - e)) / (2 * e)
    return np.array([[np.trace(At @ At), np.trace(At @ Ax)], [np.trace(Ax @ At), np.trace(Ax @ Ax)]])
G0 = G(Ufr)
print("(R6) worked example G:", np.round(G0, 6).tolist(), " Re-projected diag:", np.real(np.diag(G0)).round(6).tolist())
gC = lambda t: expm(-1j * psi_t(t) * T)
Ufr_g = lambda t, x: Ufr(t, x) @ gC(t)
G1 = G(Ufr_g)
print("     after complexified diagonal right translation g(tau)=exp(-i psi_tau T):", np.round(G1, 6).tolist())
Oij = Ufr(t0, x0) @ inv(Ufr(t0, x0, off=0.37))
print("     two agents with different psi_tau (offset 0.37): max |Im Omega_ij| =", np.abs(np.imag(Oij)).max(), " (real transport requires offset in pi Z)")
eta = np.diag([-1., 1.]); Lb = np.array([[np.cosh(.7), np.sinh(.7)], [np.sinh(.7), np.cosh(.7)]]); Pt = np.diag([-1., 1.])
print("(R7) boost preserves eta:", np.abs(Lb.T @ eta @ Lb - eta).max(), "; time reflection preserves eta:", np.abs(Pt.T @ eta @ Pt - eta).max(), " det", np.linalg.det(Pt), "(O(1,1) has 4 components)")
