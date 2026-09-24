"""G2 crosswalk: PIFB2 Appendices H and I against Theory c09/c11/c12 and g07/g09.

(1) PIFB2 eq:rg_exact_free_energy / thm:rg_pushforward versus Theory thm:rg-effective-action.
    x in R^2, proper reference nu_s = N(0,I), F quadratic-plus-linear, T_cfg = 0.7, R(x) = mean.
    Theory: H^c(z) = -log E_nu[exp(-F/T) | Z=z] (conditional partition), reference nu^c = R_# nu_s.
    PIFB2: F_{s+1}(z) = -T log d(R_#(e^{-F/T} nu_s))/d nu_{s+1}, with a separately chosen proper
    nu_{s+1} = N(0,1).  Claimed relation: F_{s+1} = T H^c - T log(d nu^c / d nu_{s+1}).
    Also Z_{s+1} = Z_s.
(2) PIFB2 thm:rg_exact_closure, constant-block case, versus Theory g07 prop:cg-normalized-schur-action
    (with source h and constant): -log int exp(-E(x, xi)) dxi = 1/2 L_eff x^2 - h_eff x + c_eff.
(3) Theory prop:rg-scale-functoriality (iii) witness: majority with first-member tie-break is not
    functorial on the non-chain poset {pairs, triples}.  (PIFB2 thm:rg_semigroup is the chain case.)
(4) Theory g09 prop:grg-aggregation-semigroup: Galerkin aggregation closes the interaction family and
    composes, A_{S2} A_{S1} = A_{S1 S2}.
(5) PIFB2 thm:nested_state_configuration_vfe equals the Theory tower VFE (def:full-graph-tower-vfe)
    for the two-level latent (X, Y), up to the overall factor T_cfg.
"""
import numpy as np
from scipy import integrate

rng = np.random.default_rng(11)

# ---------------- (1) pushforward ----------------
print("(1) exact pushforward: PIFB2 coarea form vs Theory conditional-partition form")
T = 0.7
Kmat = np.array([[1.3, 0.4], [0.4, 0.9]]); bvec = np.array([0.3, -0.5])
F = lambda x1, x2: 0.5 * (Kmat[0, 0]*x1*x1 + 2*Kmat[0, 1]*x1*x2 + Kmat[1, 1]*x2*x2) + bvec[0]*x1 + bvec[1]*x2
phi = lambda x, v: np.exp(-0.5 * x * x / v) / np.sqrt(2 * np.pi * v)
def rho_tilde(z):  # density of R_#(e^{-F/T} nu_s) wrt Lebesgue dz; x1=z+t, x2=z-t, Jacobian 2
    f = lambda t: np.exp(-F(z + t, z - t) / T) * phi(z + t, 1) * phi(z - t, 1)
    return 2 * integrate.quad(f, -12, 12, epsabs=1e-13)[0]
def cond_partition(z):  # E_nu[e^{-F/T} | Z=z], t | z ~ N(0, 1/2) under nu_s
    f = lambda t: np.exp(-F(z + t, z - t) / T) * phi(t, 0.5)
    return integrate.quad(f, -12, 12, epsabs=1e-13)[0]
worst = 0.0
for z in (-1.3, -0.2, 0.0, 0.7, 1.9):
    F_pifb2 = -T * np.log(rho_tilde(z) / phi(z, 1.0))
    Hc = -np.log(cond_partition(z))
    rhs = T * Hc - T * np.log(phi(z, 0.5) / phi(z, 1.0))
    worst = max(worst, abs(F_pifb2 - rhs))
print(f"   max |F_(s+1) - [T H^c - T log dnu^c/dnu_(s+1)]| over 5 z = {worst:.2e}")
Zs = integrate.dblquad(lambda x2, x1: np.exp(-F(x1, x2) / T) * phi(x1, 1) * phi(x2, 1), -12, 12, -12, 12, epsabs=1e-12)[0]
Zs1 = integrate.quad(rho_tilde, -10, 10, epsabs=1e-12)[0]
print(f"   Z_s = {Zs:.12f}, Z_(s+1) = {Zs1:.12f}, diff {abs(Zs-Zs1):.2e}")
print("   pushforward reference nu^c = N(0,1/2) is a probability measure (sigma-finite); see ledger item (b)")

# ---------------- (2) Schur closure ----------------
print("(2) constant-block closure = normalized Schur marginal (g07) incl. source and constant")
M = rng.normal(size=(3, 3)); Lam = M @ M.T + 1.0 * np.eye(3)
h = rng.normal(size=3); c = 0.37
Lrr = Lam[0, 0]; Lrh = Lam[0, 1:]; Mh = Lam[1:, 1:]
Mi = np.linalg.inv(Mh)
L_eff = Lrr - Lrh @ Mi @ Lrh
h_eff = h[0] - Lrh @ Mi @ h[1:]
c_eff = c + 0.5 * np.log(np.linalg.det(Mh)) - 1.0 * np.log(2 * np.pi) - 0.5 * h[1:] @ Mi @ h[1:]
worst = 0.0
for x in (-0.8, 0.1, 1.2):
    E = lambda u, v: 0.5 * np.array([x, v, u]) @ Lam @ np.array([x, v, u]) - h @ np.array([x, v, u]) + c
    val = integrate.dblquad(lambda u, v: np.exp(-E(u, v)), -15, 15, -15, 15, epsabs=1e-13)[0]
    worst = max(worst, abs(-np.log(val) - (0.5 * L_eff * x * x - h_eff * x + c_eff)))
print(f"   max |-log int e^-E dxi - (1/2 L_eff x^2 - h_eff x + c_eff)| = {worst:.2e}")

# ---------------- (3) functoriality witness ----------------
print("(3) majority with first-member tie-break on six agents")
maj = lambda blk: int(sum(blk) * 2 > len(blk)) if sum(blk) * 2 != len(blk) else blk[0]
y = (0, 0, 1, 0, 1, 0)
pairs_then_triple = maj([maj(y[0:2]), maj(y[2:4]), maj(y[4:6])])
triples_then_pair = maj([maj(y[0:3]), maj(y[3:6])])
print(f"   pairs->triple: {pairs_then_triple}; triples->pair: {triples_then_pair}  (Theory: 1 and 0)")

# ---------------- (4) aggregation semigroup ----------------
print("(4) Galerkin aggregation on the interaction family")
N, K = 6, 2
def psd():
    Q = rng.normal(size=(K, K)); return Q @ Q.T
A = [psd() + 0.2*np.eye(K) for _ in range(N)]
Wd = {(i, j): psd() for i in range(N) for j in range(i+1, N) if rng.uniform() < 0.6}
Lam6 = np.zeros((N*K, N*K))
for i in range(N): Lam6[i*K:(i+1)*K, i*K:(i+1)*K] += A[i]
for (i, j), Wij in Wd.items():
    for a, bq in ((i, i), (j, j)): Lam6[a*K:(a+1)*K, bq*K:(bq+1)*K] += Wij
    Lam6[i*K:(i+1)*K, j*K:(j+1)*K] -= Wij; Lam6[j*K:(j+1)*K, i*K:(i+1)*K] -= Wij
S1h = np.zeros((6, 3)); S1h[[0, 1], 0] = 1; S1h[[2, 3], 1] = 1; S1h[[4, 5], 2] = 1
S2h = np.zeros((3, 2)); S2h[[0, 1], 0] = 1; S2h[2, 1] = 1
S1, S2 = np.kron(S1h, np.eye(K)), np.kron(S2h, np.eye(K))
Lc = S1.T @ Lam6 @ S1
off = [Lc[a*K:(a+1)*K, b*K:(b+1)*K] for a in range(3) for b in range(3) if a != b]
ok_fam = all(np.allclose(B, B.T) and np.linalg.eigvalsh(-B).min() > -1e-12 for B in off)
print(f"   coarse off-diagonal blocks symmetric and -PSD (in family): {ok_fam}")
print(f"   max|A_S2 A_S1 - A_(S1 S2)| = {np.abs(S2.T @ Lc @ S2 - (S1 @ S2).T @ Lam6 @ (S1 @ S2)).max():.2e}")

# ---------------- (5) nested VFE = tower VFE ----------------
print("(5) nested state/configuration VFE vs two-level tower VFE")
nX, nY = 3, 4; Tc = 1.7
P0 = rng.dirichlet(np.ones(nX)); pY = rng.dirichlet(np.ones(nY), size=nX); po = rng.uniform(0.1, 0.9, size=(nX, nY))
R = rng.dirichlet(np.ones(nX)); QX = rng.dirichlet(np.ones(nY), size=nX)
Fstate = np.array([np.sum(QX[x] * np.log(QX[x] / pY[x])) - np.sum(QX[x] * np.log(po[x])) for x in range(nX)])
J = Tc * np.sum(R * np.log(R / P0)) + Tc * np.sum(R * Fstate)
joint = P0[:, None] * pY * po; pO = joint.sum(); post = joint / pO
Qj = R[:, None] * QX
tower = -np.log(pO) + np.sum(Qj * np.log(Qj / post))
print(f"   |J/T_cfg - F_tower| = {abs(J / Tc - tower):.2e}")
