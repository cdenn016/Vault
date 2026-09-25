r"""L10: Cholesky parametrization chain rule and positivity claims (PIFB2 2653-2660);
vech/duplication-matrix statement for the Fisher block (2635); trace-free remark (2328).
"""
import numpy as np
rng = np.random.default_rng(9)
K = 4
def spd(K):
    A = rng.standard_normal((K, K)); return A @ A.T + 0.5 * np.eye(K)
P = spd(K); mp = rng.standard_normal(K)
def F(S):  # KL(N(0,S)||N(mp,P)) as a test objective
    Pi = np.linalg.inv(P); return 0.5 * (np.trace(Pi @ S) + mp @ Pi @ mp - K + np.linalg.slogdet(P)[1] - np.linalg.slogdet(S)[1])
def gradS(S): return 0.5 * (np.linalg.inv(P) - np.linalg.inv(S))
sp = lambda x: np.log1p(np.exp(x)); sig = lambda x: 1 / (1 + np.exp(-x))
def L_of(theta, mode):  # theta: lower-tri raw params; diagonal passed through positive map
    L = np.tril(theta, -1); d = np.diag(theta); L = L + np.diag(sp(d) if mode == "softplus" else np.abs(d)); return L
# chain rule: dF/dL = tril(2 G L); dF/dtheta_kk = (2 G L)_kk * map'(theta_kk)
th = np.tril(rng.standard_normal((K, K))); h = 1e-6; worst = 0
for mode in ("softplus", "abs"):
    L = L_of(th, mode); G = gradS(L @ L.T); an = np.tril(2 * G @ L); dm = sig(np.diag(th)) if mode == "softplus" else np.sign(np.diag(th))
    an[np.diag_indices(K)] *= dm
    num = np.zeros((K, K))
    for a in range(K):
        for b in range(a + 1):
            E = np.zeros((K, K)); E[a, b] = 1
            num[a, b] = (F(L_of(th + h * E, mode) @ L_of(th + h * E, mode).T) - F(L_of(th - h * E, mode) @ L_of(th - h * E, mode).T)) / (2 * h)
    worst = max(worst, np.linalg.norm(an - num) / np.linalg.norm(num))
print(f"Cholesky chain rule dF/dL = tril(2 G L) (with positive-map factor on the diagonal), FD rel err = {worst:.2e}")
# stationarity equivalence: the linear map G -> tril(G L) on Sym is injective for invertible lower-triangular L
L = L_of(th, "softplus"); idx = [(a, b) for a in range(K) for b in range(a + 1)]
M = []
for (a, b) in idx:
    Gs = np.zeros((K, K)); Gs[a, b] = Gs[b, a] = 1; M.append(np.tril(Gs @ L)[np.tril_indices(K)])
sv = np.linalg.svd(np.array(M).T, compute_uv=False)
print(f"map Sym -> lower-tri, G -> tril(G L): dim {len(idx)}, smallest singular value {sv.min():.3e} (injective => grad_L = 0 iff grad_Sigma = 0)")
# positivity claims: abs map reaches zero; softplus underflows in fp32/fp64
th0 = th.copy(); th0[1, 1] = 0.0; S0 = L_of(th0, "abs") @ L_of(th0, "abs").T
print(f"abs map, raw diagonal entry = 0: min eig of Sigma = {np.linalg.eigvalsh(S0).min():.2e} (singular, not SPD)")
for dt, name in ((np.float32, "fp32"), (np.float64, "fp64")):
    with np.errstate(under="ignore"):
        xs = np.array([-20, -90, -104, -110, -750], dtype=dt); vals = np.log1p(np.exp(xs))
    print(f"softplus in {name}: x={xs.tolist()} -> {vals.tolist()}")
# a Euclidean step on raw L across zero under abs: the realized entry passes near zero
print("realized |x| along a straight Euclidean path through x=0: min over path of |x| = 0 exactly when the path crosses zero")

# vech statement (2635): inverse of (1/2) D^T (S^-1 kron S^-1) D is 2 D^+ (S kron S) D^+T, and natural gradient unchanged
K = 3; S = spd(K)
D = np.zeros((K * K, K * (K + 1) // 2)); col = 0; pos = {}
for b in range(K):
    for a in range(b, K):
        D[a * K + b, col] = 1; D[b * K + a, col] = 1; pos[(a, b)] = col; col += 1
Dp = np.linalg.pinv(D); Si = np.linalg.inv(S)
Fv = 0.5 * D.T @ np.kron(Si, Si) @ D
inv_claim = 2 * np.kron(S, S)
print(f"\nvech Fisher block: |Fv^-1 - 2 D^+ (S kron S) D^+T|/|.| = {np.linalg.norm(np.linalg.inv(Fv) - 2 * Dp @ np.kron(S, S) @ Dp.T)/np.linalg.norm(np.linalg.inv(Fv)):.2e};"
      f"  Fv^-1 is not 2(S kron S) restricted: size mismatch {Fv.shape} vs {inv_claim.shape}")
G = rng.standard_normal((K, K)); G = G + G.T; gv = D.T @ G.ravel()  # gradient in vech coordinates
nat_v = np.linalg.solve(Fv, gv); nat = 2 * S @ G @ S
print(f"natural gradient via vech coordinates vs 2 S G S: rel err {np.linalg.norm(D @ nat_v - nat.ravel())/np.linalg.norm(nat):.2e}")

# trace-free remark (2328): tr(S^-1 U) = 0 is not tr U = 0 unless S = I
U = rng.standard_normal((K, K)); U = U + U.T; U -= np.trace(U) / K * np.eye(K)
print(f"\ntrace-free U (tr U = {np.trace(U):.1e}) at random S: tr(S^-1 U) = {np.trace(Si @ U):.3f}  (second metric term nonzero)")
