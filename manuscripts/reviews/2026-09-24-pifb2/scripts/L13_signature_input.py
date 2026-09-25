"""L13: the signature of the frame-twist pullback in prop:4d_signature is fixed by the chosen generators.

For commuting disjoint-support generators (p real skew 2x2 blocks, q traceless mutually
trace-orthogonal diagonals), the trace-form Gram matrix tr(T_a T_b) has signature (p neg, q pos),
and the pullback G = J^T Gram J along any full-rank frame map has the same signature.
Also: the trace form on gl(K,R) has K(K+1)/2 positive and K(K-1)/2 negative directions for every K,
so an indefinite ("Lorentzian-available") restriction exists for every K >= 2.
"""
import numpy as np
rng = np.random.default_rng(0)

def gens(p, q):
    K = 2 * p + (q + 1)
    Ts = []
    for b in range(p):
        S = np.zeros((K, K)); S[2*b, 2*b+1] = -1; S[2*b+1, 2*b] = 1; Ts.append(S)
    off = 2 * p; n = q + 1
    # orthonormal basis of traceless diagonals on n coordinates (Helmert basis)
    H = np.zeros((q, n))
    for a in range(q):
        H[a, :a+1] = 1; H[a, a+1] = -(a+1); H[a] /= np.linalg.norm(H[a])
    for a in range(q):
        D = np.zeros((K, K)); D[off:off+n, off:off+n] = np.diag(H[a]); Ts.append(D)
    return K, Ts

def sig(M, tol=1e-10):
    w = np.linalg.eigvalsh((M + M.T) / 2)
    return int((w < -tol).sum()), int((w > tol).sum())

worst = 0.0
for p, q in [(1, 3), (2, 2), (3, 1), (1, 1), (0, 4), (2, 5)]:
    K, Ts = gens(p, q)
    comm = max(np.abs(A @ B - B @ A).max() for A in Ts for B in Ts)
    Gram = np.array([[np.trace(A @ B) for B in Ts] for A in Ts])
    J = rng.standard_normal((p + q, p + q))  # d psi / d c, generic full rank
    G = J.T @ Gram @ J
    worst = max(worst, comm)
    print(f"p={p} skew, q={q} diag, K={K}: max|[T_a,T_b]|={comm:.1e}, Gram sig(neg,pos)={sig(Gram)}, pullback sig={sig(G)}")
for K in [2, 3, 4, 6]:
    # trace form on gl(K,R) in the elementary basis E_ij: tr(E_ij E_kl) = d_jk d_il
    B = np.zeros((K*K, K*K))
    for i in range(K):
        for j in range(K):
            for k in range(K):
                for l in range(K):
                    B[i*K+j, k*K+l] = float(j == k and i == l)
    print(f"gl({K},R) trace form sig(neg,pos) = {sig(B)}; expected ({K*(K-1)//2},{K*(K+1)//2})")
print("max commutator residual", worst)
