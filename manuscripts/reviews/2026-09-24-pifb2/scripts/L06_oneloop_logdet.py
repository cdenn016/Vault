r"""L06: Y-dependence of the one-loop term (T/2) log det' H_I^perp in eq:rg_laplace (PIFB2.tex ~3719).

With H = L_I (x) F restricted to the barycentric constraint {sum_i w_i xi_i = 0} (dimension (n-1)K),
  log det(H|_constraint) = K log det'(L_I) + (n-1) log det F + c(w),
with c(w) = K log[ (1.w)^2 / (|1|^2 |w|^2) ] independent of F.  For the mean sector F = Sigma_I^{-1},
so the loop term shifts the coefficient of log det Sigma_I in the parent functional by -(n-1) T/2:
an induced renormalization of the parent's entropy weight proportional to cluster size.
"""
import numpy as np

rng = np.random.default_rng(4)
for trial in range(3):
    n, K = 4, 3
    A = rng.uniform(0.2, 2, size=(n, n)); A = np.triu(A, 1); A = A + A.T
    L = np.diag(A.sum(1)) - A
    M = rng.normal(size=(K, K)); F = M @ M.T + np.eye(K)
    w = rng.dirichlet(np.ones(n))
    # orthonormal basis of w-perp in R^n, tensor with R^K
    Qf, _ = np.linalg.qr(np.column_stack([w, rng.normal(size=(n, n - 1))]))
    B = Qf[:, 1:]                      # n x (n-1), orthonormal, orthogonal to w
    P = np.kron(B, np.eye(K))          # nK x (n-1)K
    H = np.kron(L, F)
    lhs = np.linalg.slogdet(P.T @ H @ P)[1]
    ev = np.linalg.eigvalsh(L); detp = np.prod(ev[1:])
    one = np.ones(n)
    cw = K * np.log((one @ w) ** 2 / ((one @ one) * (w @ w)))
    rhs = K * np.log(detp) + (n - 1) * np.linalg.slogdet(F)[1] + cw
    print("trial %d: log det restricted = %.12f, formula = %.12f, resid = %.1e" % (trial, lhs, rhs, abs(lhs - rhs)))
