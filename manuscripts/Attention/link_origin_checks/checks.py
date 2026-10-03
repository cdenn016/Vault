r"""Float64 checks for link_origin.tex (small dimensions; grounding only, not evidence about large N)."""
import numpy as np
from scipy.linalg import expm

rng = np.random.default_rng(0)
K, H = 6, 3
d = K // H
rel = lambda a, b: np.abs(a - b).max() / max(1.0, np.abs(b).max())

def phi(Z):
    r"""phi(Z) = sum_{n>=1} Z^{n-1}/n! = (e^Z - I) Z^{-1}, by series (valid for singular Z)."""
    out, term = np.zeros_like(Z), np.eye(Z.shape[0])
    for n in range(1, 60):
        out = out + term / np.prod(np.arange(1, n + 1, dtype=float))
        term = term @ Z
    return out

U = lambda: expm(0.3 * rng.standard_normal((K, K)))
Ui, Uj, Uk = U(), U(), U()
O = rng.standard_normal((K, d)); T = rng.standard_normal((d, K))

# (1) exp of a rank-d algebra element: exp(OT) = I + O phi(TO) T, exactly.
E = expm(O @ T)
print("exp(OT) = I + O phi(TO) T          rel err", rel(E, np.eye(K) + O @ phi(T @ O) @ T))
print("det exp(OT) = e^{tr(TO)}            rel err", rel(np.linalg.det(E), np.exp(np.trace(T @ O))))
v = np.linalg.svd(T)[2][-1]                                      # a vector in ker T
print("exp(OT) fixes ker T                 err", np.abs(E @ v - v).max())

# Link form: Theta = Omega + U_i O phi(TO) T U_j^-1, first order L = U_i O T U_j^-1.
Om = Ui @ np.linalg.inv(Uj)
Th = Ui @ E @ np.linalg.inv(Uj)
print("Theta = Omega + Ltilde              rel err",
      rel(Th, Om + Ui @ O @ phi(T @ O) @ T @ np.linalg.inv(Uj)))
for s in (1e-2, 1e-3):
    Ths = Ui @ expm(s * O @ T) @ np.linalg.inv(Uj)
    print(f"(Theta-Omega)/s - L at s={s:g}      rel err", rel((Ths - Om) / s, Ui @ O @ T @ np.linalg.inv(Uj)))

# Multi-head: X = O B T with B = blockdiag(beta_h I_d); exp(OBT) = I + O phi(B T O) B T.
Oh = rng.standard_normal((K, K)); Tm = rng.standard_normal((K, K))
beta = rng.dirichlet(np.ones(H) * 0.7) + 0.0
B = np.kron(np.diag(beta), np.eye(d))
print("exp(OBT) = I + O phi(BTO) B T       rel err",
      rel(expm(Oh @ B @ Tm), np.eye(K) + Oh @ phi(B @ Tm @ Oh) @ B @ Tm))

# (2) Block LDU (Levi) factorization relative to W = first d coordinates.
G = rng.standard_normal((K, K))
A, Bm, C, D = G[:d, :d], G[:d, d:], G[d:, :d], G[d:, d:]
S = D - C @ np.linalg.inv(A) @ Bm
Lo = np.block([[np.eye(d), np.zeros((d, K - d))], [C @ np.linalg.inv(A), np.eye(K - d)]])
Mi = np.block([[A, np.zeros((d, K - d))], [np.zeros((K - d, d)), S]])
Up = np.block([[np.eye(d), np.linalg.inv(A) @ Bm], [np.zeros((K - d, d)), np.eye(K - d)]])
print("G = n_- (A + S) n_+                 rel err", rel(G, Lo @ Mi @ Up))
print("det G = det A det S                 rel err", rel(np.linalg.det(G), np.linalg.det(A) * np.linalg.det(S)))

# Compression with oblique projectors equals the Levi block in an adapted basis.
Pi_R = O @ np.linalg.inv(T @ O) @ T                                # projector onto im O along ker T
print("Pi_R idempotent                     err", np.abs(Pi_R @ Pi_R - Pi_R).max())

# (3) Head-sum operator and its loop with a reversed (inverted) edge, TO = I case.
Q, _ = np.linalg.qr(rng.standard_normal((K, K)))
O3, T3 = Q, np.linalg.inv(Q)                                       # TO = I
b = {e: rng.dirichlet(np.ones(4))[:H] + 0.05 for e in ("ij", "jk", "ik")}
Bd = {e: np.kron(np.diag(b[e]), np.eye(d)) for e in b}
C_ = lambda Ua, e, Ub: Ua @ O3 @ Bd[e] @ T3 @ np.linalg.inv(Ub)
hol = C_(Ui, "ij", Uj) @ C_(Uj, "jk", Uk) @ np.linalg.inv(C_(Ui, "ik", Uk))
pred = Ui @ O3 @ np.kron(np.diag(b["ij"] * b["jk"] / b["ik"]), np.eye(d)) @ T3 @ np.linalg.inv(Ui)
print("head-sum loop = ratio of weights    rel err", rel(hol, pred))
# Exponential links in the same commuting case: curvature additive in beta.
X = {e: O3 @ Bd[e] @ T3 for e in b}
Th_ = lambda Ua, e, Ub: Ua @ expm(X[e]) @ np.linalg.inv(Ub)
hol1 = Th_(Ui, "ij", Uj) @ Th_(Uj, "jk", Uk) @ np.linalg.inv(Th_(Ui, "ik", Uk))
pred1 = Ui @ O3 @ np.kron(np.diag(np.exp(b["ij"] + b["jk"] - b["ik"])), np.eye(d)) @ T3 @ np.linalg.inv(Ui)
print("exp-link loop = e^(b_ij+b_jk-b_ik)  rel err", rel(hol1, pred1))
# Trace of a loop is frame invariant.
g = U()
print("loop trace invariant under g_i      rel err", rel(np.trace(g @ hol @ np.linalg.inv(g)), np.trace(hol)))
