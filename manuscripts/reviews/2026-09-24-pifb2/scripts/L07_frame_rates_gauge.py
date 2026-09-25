r"""L07: frame-sector relaxation rates are not gauge invariant (PIFB2.tex 949-1003).

Frame flow U' = -eta U xi, xi = U^{-1} grad_U F  ==  U' = -eta grad_U F (ambient Frobenius gradient).
Two agents, F(U1,U2) = KL(q1 || Omega q2), Omega = U1 U2^{-1}. F is invariant under the global
gauge map (U1,U2) -> (U1 g, U2 g). Compare the linearized relaxation spectrum (eigenvalues of the
Euclidean Hessian in U at a minimum) before and after a global gauge transformation g.
"""
import numpy as np

K = 2
mu1, mu2 = np.array([1.0, 0.5]), np.array([0.3, -0.2])
S1 = np.array([[1.0, 0.2], [0.2, 0.6]]); S2 = np.array([[0.8, -0.1], [-0.1, 1.2]])


def kl(m1, A, m2, B):
    Bi = np.linalg.inv(B); d = m2 - m1
    return 0.5 * (np.trace(Bi @ A) + d @ Bi @ d - K + np.log(np.linalg.det(B) / np.linalg.det(A)))


def F(x):
    U1 = x[:4].reshape(2, 2); U2 = x[4:].reshape(2, 2)
    Om = U1 @ np.linalg.inv(U2)
    return kl(mu1, S1, Om @ mu2, Om @ S2 @ Om.T)


def hess(f, x, h=1e-4):
    n = len(x); H = np.zeros((n, n))
    for a in range(n):
        for b in range(n):
            e = np.zeros(n); e[a] = h; d = np.zeros(n); d[b] = h
            H[a, b] = (f(x + e + d) - f(x + e - d) - f(x - e + d) + f(x - e - d)) / (4 * h * h)
    return 0.5 * (H + H.T)


# a minimizer: Omega0 maps q2 onto q1 exactly (Omega0 S2 Omega0^T = S1, Omega0 mu2 = mu1 needs a shift;
# use a pure-covariance match and set mu2 so that the mean also matches)
L1 = np.linalg.cholesky(S1); L2 = np.linalg.cholesky(S2)
Om0 = L1 @ np.linalg.inv(L2)
mu2 = np.linalg.solve(Om0, mu1)
U2 = np.eye(2); U1 = Om0 @ U2
x0 = np.concatenate([U1.ravel(), U2.ravel()])
print("F at minimizer:", F(x0))
for label, g in [("identity gauge", np.eye(2)), ("g = diag(10,1)", np.diag([10.0, 1.0])), ("g = diag(0.1,1)", np.diag([0.1, 1.0]))]:
    x = np.concatenate([(U1 @ g).ravel(), (U2 @ g).ravel()])
    ev = np.sort(np.linalg.eigvalsh(hess(F, x, h=1e-4 * min(1.0, np.diag(g).min()))))
    print(f"{label:16s}: F = {F(x):.2e}; nonzero relaxation rates (eta=1): {np.round(ev[ev > 1e-6], 4)}")


def right_invariant_metric(x):
    """Matrix of g_U(dU,dU) = |dU U^{-1}|_F^2 (blockwise for U1,U2) in the 8 entry coordinates."""
    G = np.zeros((8, 8))
    for blk in range(2):
        U = x[4 * blk:4 * blk + 4].reshape(2, 2); Ui = np.linalg.inv(U)
        E = [np.eye(4)[k].reshape(2, 2) for k in range(4)]
        for a in range(4):
            for b in range(4):
                G[4 * blk + a, 4 * blk + b] = np.sum((E[a] @ Ui) * (E[b] @ Ui))
    return G


print("right-invariant metric (right-trivialized velocity, fixed Frobenius form on gl(2)):")
for label, g in [("identity gauge", np.eye(2)), ("g = diag(10,1)", np.diag([10.0, 1.0])), ("g = diag(0.1,1)", np.diag([0.1, 1.0]))]:
    x = np.concatenate([(U1 @ g).ravel(), (U2 @ g).ravel()])
    ev = np.sort(np.linalg.eigvals(np.linalg.solve(right_invariant_metric(x), hess(F, x, h=1e-4 * min(1.0, np.diag(g).min())))).real)
    print(f"{label:16s}: nonzero relaxation rates: {np.round(ev[ev > 1e-5], 4)}")
