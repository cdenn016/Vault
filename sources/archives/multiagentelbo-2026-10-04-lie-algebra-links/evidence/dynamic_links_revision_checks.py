"""Float64 checks of the two dynamic_links.tex corrections (small K, grounding only)."""
import numpy as np
from scipy.linalg import expm, schur

rng = np.random.default_rng(0)
K = 3


def frob_defect(W):
    return 0.5 * np.linalg.norm(W - np.eye(W.shape[0])) ** 2


# (a) Phi(h W h^-1) = Phi(W) for all W iff h is a nonzero multiple of an orthogonal matrix.
Q, _ = np.linalg.qr(rng.standard_normal((K, K)))
errs = []
for c in (-2.5, 0.3, 7.0):
    h = c * Q
    for _ in range(50):
        W = expm(0.5 * rng.standard_normal((K, K)))
        errs.append(abs(frob_defect(h @ W @ np.linalg.inv(h)) - frob_defect(W)))
print("(a) max |Phi(cQ W (cQ)^-1) - Phi(W)| =", max(errs))
h = np.diag([1.0, 2.0, 1.0])  # not a multiple of an orthogonal matrix
W = np.eye(K) + np.outer([1.0, 0, 0], [0, 1.0, 0])
print("(a) non-conformal h changes Phi:", frob_defect(W), "->", frob_defect(h @ W @ np.linalg.inv(h)))


# (b) chart infimum: l(G) = 1/2 E||z' - G z_j||_A^2 with z_j ~ N(xi_j, C_j); G* = xi' xi_j^T S_j^-1.
def setup(sign):
    xi_j = rng.standard_normal(K)
    C = np.eye(K) + 0.3 * np.diag(rng.random(K))
    xi_p = rng.standard_normal(K)
    s = xi_j @ np.linalg.solve(C, xi_p)
    if np.sign(s) != sign:
        xi_p = -xi_p
    S = C + np.outer(xi_j, xi_j)
    Gs = np.outer(xi_p, xi_j) @ np.linalg.inv(S)
    return xi_j, C, xi_p, S, Gs


A = np.eye(K)


def ell(G, xi_j, C, xi_p):
    r = xi_p - G @ xi_j
    return 0.5 * (r @ A @ r + np.trace(A @ G @ C @ G.T))


for sign in (+1, -1):
    xi_j, C, xi_p, S, Gs = setup(sign)
    tau = np.trace(Gs)
    sm = (xi_j @ np.linalg.solve(C, xi_p)) / (1 + xi_j @ np.linalg.solve(C, xi_j))
    print(f"(b) sign {sign:+d}: tr G* = {tau:.6f}, Sherman-Morrison = {sm:.6f}, rank = {np.linalg.matrix_rank(Gs)}")
    if sign > 0:
        for eps in (1e-1, 1e-3, 1e-6):
            G = Gs + eps * np.eye(K)
            ev = np.linalg.eigvals(G)
            print(f"    eps={eps:g}: min Re eig {ev.real.min():.2e}, l-l* = {ell(G, xi_j, C, xi_p) - ell(Gs, xi_j, C, xi_p):.3e}")
    else:
        # random descent over generators: chart infimum stays strictly above l(G*)
        lstar = ell(Gs, xi_j, C, xi_p)
        best = np.inf
        for _ in range(200):
            X = 3.0 * rng.standard_normal((K, K))
            best = min(best, ell(expm(X), xi_j, C, xi_p) - lstar)
        print(f"    neg case: l(G*) = {lstar:.4f}; best random chart gap = {best:.4f} (> 0 expected)")

# stationary generator at a critical point of exp (K=2): xi' = xi_j = e1, C = A = I
Jrot = np.array([[0.0, -1.0], [1.0, 0.0]])
X = -np.log(3) * np.eye(2) + 2 * np.pi * Jrot
e1 = np.array([1.0, 0.0])
f = lambda X: (lambda G: 0.5 * ((e1 - G @ e1) @ (e1 - G @ e1) + np.trace(G @ G.T)))(expm(X))
g = np.zeros((2, 2))
h = 1e-6
for a in range(2):
    for b in range(2):
        E = np.zeros((2, 2)); E[a, b] = h
        g[a, b] = (f(X + E) - f(X - E)) / (2 * h)
print("stationary generator: e^X =", np.round(expm(X), 12).tolist(), " |grad| =", np.abs(g).max())
