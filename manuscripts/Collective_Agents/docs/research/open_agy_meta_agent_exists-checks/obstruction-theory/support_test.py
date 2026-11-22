"""Lemma Z (sign, support and path-product tests): if Pi is diffusive (PD Z-matrix) then Sigma = Pi^{-1} >= 0,
Sigma_ij > 0 iff i, j lie in one connected component of the coupling graph, and Sigma_ij Sigma_jk <= Sigma_ik Sigma_jj.
EXPECTED: 0 violations on random diffusive Pi; lazy rings n>=6 fail the support test at every tau (non-diffusive);
NEG CONTROL: n=5 lazy ring at tau=1 is diffusive; random positive covariances violate path-product sometimes."""
import itertools
import numpy as np
from common import is_diffusive
rng = np.random.default_rng(13)
v_sign = v_supp = v_pp = 0
for _ in range(300):
    N = rng.integers(3, 8)
    A = rng.uniform(0, 1, (N, N)) * (rng.uniform(size=(N, N)) < 0.5); A = np.triu(A, 1); A = A + A.T
    P = np.diag(A.sum(1) + rng.uniform(0.01, 1, N)) - A
    S = np.linalg.inv(P)
    v_sign += S.min() < -1e-12
    # connected components of coupling graph
    comp = -np.ones(N, int); c = 0
    for s in range(N):
        if comp[s] < 0:
            stack = [s]; comp[s] = c
            while stack:
                u = stack.pop()
                for w in np.nonzero(A[u] > 0)[0]:
                    if comp[w] < 0: comp[w] = c; stack.append(w)
            c += 1
    same = comp[:, None] == comp[None, :]
    v_supp += bool(((S > 1e-14) != same).any())
    for i, j, k in itertools.permutations(range(N), 3):
        if S[i, j] * S[j, k] > S[i, k] * S[j, j] * (1 + 1e-10) + 1e-14: v_pp += 1
print(f"[{'PASS' if v_sign == 0 else 'FAIL'}] diffusive => Sigma >= 0 (violations {v_sign})")
print(f"[{'PASS' if v_supp == 0 else 'FAIL'}] diffusive => support of Sigma = same coupling component (violations {v_supp})")
print(f"[{'PASS' if v_pp == 0 else 'FAIL'}] diffusive => path-product inequality (violations {v_pp})")
def lazy_ring(n):
    W = 0.5 * np.eye(n)
    for i in range(n): W[i, (i + 1) % n] += 0.25; W[i, (i - 1) % n] += 0.25
    return W
allbad = True
for n in range(6, 11):
    W = lazy_ring(n)
    for tau in [1e-6, 1e-3, 1.0, 10.0, 100.0, 1e4]:
        S = W @ W + tau * np.eye(n)
        zero_with_common = any(abs(S[0, k]) < 1e-15 and any(S[0, j] > 0 and S[j, k] > 0 for j in range(n)) for k in range(n))
        Pi = np.linalg.inv(S)
        diff = all(is_diffusive(Pi, tol=1e-12 * np.abs(Pi).max())[:2])
        if not (zero_with_common and not diff):
            print(f"   n={n}, tau={tau}: zero_with_common={zero_with_common}, max offdiag={is_diffusive(Pi)[2]:.3e}, max|Pi|={np.abs(Pi).max():.3e}")
        allbad &= zero_with_common and not diff
print(f"[{'PASS' if allbad else 'FAIL'}] lazy rings n=6..10: support test fails and Pi_Y non-diffusive at tau in 1e-6..1e4")
W5 = lazy_ring(5)
print(f"[{'PASS' if all(is_diffusive(np.linalg.inv(W5 @ W5 + 1.0 * np.eye(5)))[:2]) else 'FAIL'}] NEG CONTROL n=5, tau=1: diffusive")
cnt = 0
for _ in range(300):
    X = rng.uniform(0, 1, (4, 4)); S = X @ X.T + 0.05 * np.eye(4)
    cnt += any(S[i, j] * S[j, k] > S[i, k] * S[j, j] for i, j, k in itertools.permutations(range(4), 3))
print(f"[{'PASS' if cnt > 0 else 'FAIL'}] NEG CONTROL random positive covariances violate path-product in {cnt}/300 draws")
