"""Numerical probes for verify_V5.md (float64, CPU). They test closed forms on explicit instances only.

A. prop:glink-unanchored-scalar (K=1): twisted incidence T, Cauchy-Binet identity, unicyclic
   determinant |det T_{E'_k}| = |1-e^{s_k}| * prod_{e in S} e^{omega_e}, and the lower bound of (i).
B. prop:glink-chart-infimum-semisimple: two-sided chart-link property for admissible E (K=3, K=5)
   and its failure for a non-admissible E.
C. Lead for open:glink-chart-infimum (not a verdict): K=4, M = -(I+N), N = J_2(0)+J_2(0); E with
   Lidskii matrix Phi_1 = Y_1^T E X_1 having non-real eigenvalues gives non-real eigenvalues near -1
   for both signs of t (chart links on both sides); a real-spectrum Phi_1 gives one-sided behavior.
"""
from __future__ import annotations

import itertools

import numpy as np
from scipy.linalg import expm, logm

rng = np.random.default_rng(20261004)


def twisted_incidence(copies: list[tuple[int, int]], omega: np.ndarray, N: int) -> np.ndarray:
    r"""Rows (Tz)_e = z_i - e^{omega_e} z_j for e=(j->i); a loop row is 1-e^{omega_e}."""
    T = np.zeros((len(copies), N))
    for r, (j, i) in enumerate(copies):
        if i == j:
            T[r, i] = 1.0 - np.exp(omega[r])
        else:
            T[r, i] += 1.0
            T[r, j] -= np.exp(omega[r])
    return T


def cycle_sum(copies: list[tuple[int, int]], omega: np.ndarray, walk: list[tuple[int, int]]) -> float:
    r"""(C omega)_p: sum of generators along the walk with the reversal convention."""
    s = 0.0
    for idx, sign in walk:
        s += sign * omega[idx]
    return s


# ---------------------------------------------------------------- A
print("A. prop:glink-unanchored-scalar, K=1")
# Multigraph on N=5 vertices. Spanning tree copies 0..3; extra copies: loop at 4, parallel copy on
# (1->0) oriented 0->1, and a chord 4->2 creating a longer cycle. Cycle rank r=3.
N = 5
copies = [(1, 0), (2, 1), (3, 1), (4, 3),  # tree: e0:1->0, e1:2->1, e2:3->1, e3:4->3
          (4, 4),                           # e4: loop at 4
          (0, 1),                           # e5: parallel to e0, opposite orientation (0->1)
          (4, 2)]                           # e6: chord 4->2
tree = [0, 1, 2, 3]
extras = [4, 5, 6]
# fundamental walks (copy index, +1 along E_+ orientation / -1 against), as closed walks
walks = {
    4: [(4, +1)],
    5: [(5, +1), (0, +1)],               # 0->1 via e5, then 1->0 via e0 (along its orientation)
    6: [(6, +1), (1, +1), (2, -1), (3, -1)],  # 4->2 via e6, 2->1 via e1, 1->3 against e2, 3->4 against e3
}
w = rng.uniform(0.5, 2.0, size=len(copies))
max_ratio_violation = 0.0
cb_err = 0.0
lb_violation = 0.0
for trial in range(200):
    omega = rng.normal(size=len(copies)) * 1.5
    T = twisted_incidence(copies, omega, N)
    Lam = T.T @ np.diag(w) @ T
    # Cauchy-Binet
    cb = 0.0
    for S in itertools.combinations(range(len(copies)), N):
        cb += np.prod(w[list(S)]) * np.linalg.det(T[list(S), :]) ** 2
    cb_err = max(cb_err, abs(cb - np.linalg.det(Lam)) / max(1.0, abs(cb)))
    # unicyclic determinants
    sum_abs = np.sum(np.abs(omega))
    ssq = 0.0
    for k in extras:
        rows = tree + [k]
        d = np.linalg.det(T[rows, :])
        s_k = cycle_sum(copies, omega, walks[k])
        ssq += s_k ** 2
        ratio = abs(d) / abs(1.0 - np.exp(s_k))
        # ratio must be exp(sum of a subset of omegas): check bounds e^{-sum|omega|} <= ratio <= e^{sum|omega|}
        viol = max(np.exp(-sum_abs) - ratio, ratio - np.exp(sum_abs), 0.0)
        max_ratio_violation = max(max_ratio_violation, viol)
    # lower bound of (i)
    lb = np.min(w) ** N * np.exp(-2.0 - 2.0 * sum_abs) * min(ssq, 1.0)
    lb_violation = max(lb_violation, lb - np.linalg.det(Lam))
print(f"  Cauchy-Binet relative error (max over 200 samples): {cb_err:.2e}")
print(f"  unicyclic ratio |det T_E'_k|/|1-e^s_k| outside [e^-sum|w|, e^sum|w|] by at most: {max_ratio_violation:.2e}")
print(f"  lower bound (i) exceeds det Lambda by at most: {lb_violation:.2e}  (<=0 means bound holds)")
# exact subset check on one sample: ratio equals exp(sum over a subset) -- report the subset found
omega = rng.normal(size=len(copies))
T = twisted_incidence(copies, omega, N)
for k in extras:
    d = np.linalg.det(T[tree + [k], :])
    s_k = cycle_sum(copies, omega, walks[k])
    ratio = abs(d) / abs(1.0 - np.exp(s_k))
    found = None
    for m in range(0, len(copies) + 1):
        for S in itertools.combinations(range(len(copies)), m):
            if abs(np.exp(np.sum(omega[list(S)])) - ratio) < 1e-10 * max(1.0, ratio):
                found = S
                break
        if found is not None:
            break
    print(f"  extra copy e{k}: |det|/|1-e^s| = exp(sum omega over subset {found})")

# cycle rank one: single term and divergence profile
copies1 = [(1, 0), (2, 1), (2, 2)]  # tree + loop at 2, N=3
w1 = np.array([1.0, 1.5, 0.7])
omega = rng.normal(size=3)
T1 = twisted_incidence(copies1, omega, 3)
Lam1 = T1.T @ np.diag(w1) @ T1
print(f"  cycle rank one: det Lambda - prod(w) (det T)^2 = {np.linalg.det(Lam1) - np.prod(w1) * np.linalg.det(T1) ** 2:.2e}; "
      f"det T = {np.linalg.det(T1):.6f}, (1-e^s)*e^(subset) with s=omega_loop: 1-e^s = {1 - np.exp(omega[2]):.6f}")

# ---------------------------------------------------------------- B
print("B. prop:glink-chart-infimum-semisimple")


def has_eig_on_negative_axis(A: np.ndarray, tol: float = 1e-9) -> bool:
    ev = np.linalg.eigvals(A)
    return bool(np.any((np.abs(ev.imag) < tol) & (ev.real <= 0.0)))


def test_semisimple(K: int, spec_neg: list[tuple[float, int]], spec_pos: list[float], label: str) -> None:
    S = rng.normal(size=(K, K))
    while abs(np.linalg.det(S)) < 0.1:
        S = rng.normal(size=(K, K))
    Sinv = np.linalg.inv(S)
    D = np.zeros((K, K))
    pos = 0
    blocks = []
    for c, n in spec_neg:
        D[pos:pos + n, pos:pos + n] = c * np.eye(n)
        blocks.append((pos, n))
        pos += n
    for lam in spec_pos:
        D[pos, pos] = lam
        pos += 1
    M = S @ D @ Sinv
    # admissible E: compressions with distinct non-real eigenvalues; random elsewhere
    Et = rng.normal(size=(K, K))
    for p0, n in blocks:
        B = np.zeros((n, n))
        for kk in range(n // 2):
            kv = kk + 1.0
            B[p0 + 2 * kk - p0:p0 + 2 * kk - p0 + 2, p0 + 2 * kk - p0:p0 + 2 * kk - p0 + 2] = [[0, -kv], [kv, 0]]
        Et[p0:p0 + n, p0:p0 + n] = B
    E = S @ Et @ Sinv
    ok = True
    for t in [1e-2, -1e-2, 1e-3, -1e-3, 1e-4, -1e-4]:
        A = M + t * E
        if has_eig_on_negative_axis(A):
            ok = False
        L = logm(A)
        if np.max(np.abs(L.imag)) > 1e-8 or np.max(np.abs(expm(L.real) - A)) > 1e-8:
            ok = False
    # non-admissible control: compression with real distinct eigenvalues of mixed sign
    Et2 = Et.copy()
    p0, n = blocks[0]
    Et2[p0:p0 + n, p0:p0 + n] = np.diag(np.linspace(-1.0, 1.0, n))
    E2 = S @ Et2 @ Sinv
    bad = []
    for t in [1e-2, -1e-2]:
        bad.append(has_eig_on_negative_axis(M + t * E2))
    print(f"  {label}: admissible E gives chart links on both sides at |t| in {{1e-2,1e-3,1e-4}}: {ok}; "
          f"non-admissible control has a negative real eigenvalue at t=+1e-2,-1e-2: {bad}")


test_semisimple(3, [(-1.0, 2)], [2.5], "K=3, spectrum {-1,-1,2.5}")
test_semisimple(5, [(-1.0, 2), (-2.0, 2)], [3.0], "K=5, spectrum {-1,-1,-2,-2,3}")

# ---------------------------------------------------------------- C
print("C. Lead for open:glink-chart-infimum (K=4, J_2+J_2 at -1); not a verdict")
Nn = np.zeros((4, 4))
Nn[0, 1] = 1.0
Nn[2, 3] = 1.0
M4 = -(np.eye(4) + Nn)
# right eigenvectors e1,e3 (indices 0,2); left eigenvectors e2,e4 (indices 1,3); Phi_1 = E[[1,3]][:, [0,2]]


def phi1(E: np.ndarray) -> np.ndarray:
    return E[np.ix_([1, 3], [0, 2])]


def report(E: np.ndarray, label: str) -> None:
    ev_phi = np.linalg.eigvals(phi1(E))
    out = []
    for t in [1e-2, -1e-2, 1e-4, -1e-4]:
        A = M4 + t * E
        ev = np.linalg.eigvals(A)
        near = ev[np.abs(ev + 1.0) < 0.5]
        nonreal = int(np.sum(np.abs(near.imag) > 1e-9))
        L = logm(A)
        real_log = (np.max(np.abs(L.imag)) < 1e-6) and (np.max(np.abs(expm(L.real) - A)) < 1e-6)
        out.append((t, nonreal, bool(real_log)))
    print(f"  {label}: eig(Phi_1) = {np.round(ev_phi, 4)}; (t, #non-real eigenvalues near -1 of 4, real log exists) = {out}")


E_nonreal = rng.normal(size=(4, 4))
E_nonreal[np.ix_([1, 3], [0, 2])] = [[0.3, -1.0], [1.0, 0.3]]
report(E_nonreal, "Phi_1 with non-real eigenvalues")
E_real = rng.normal(size=(4, 4))
E_real[np.ix_([1, 3], [0, 2])] = [[1.0, 0.0], [0.0, 2.0]]
report(E_real, "Phi_1 with real positive eigenvalues (control)")
# Leading-order check: with M4 + I = -N the Schur reduction gives s^2 = -t xi + O(|t|^{3/2}), xi in spec(E_21),
# i.e. eigenvalues near -1 are -1 +- sqrt(-xi t); residual should be O(t). Match by best permutation.
for t in [1e-4, -1e-4, 1e-6, -1e-6]:
    ev = np.linalg.eigvals(M4 + t * E_nonreal)
    near = ev[np.abs(ev + 1.0) < 0.5] + 1.0
    pred = np.array([np.sqrt(-xi * t + 0j) * s for xi in np.linalg.eigvals(phi1(E_nonreal)) for s in (1.0, -1.0)])
    best = min(np.max(np.abs(near[list(p)] - pred)) for p in itertools.permutations(range(4)))
    print(f"  leading-order check at t={t:+.0e}: max |(lambda+1) - (+-sqrt(-xi t))| = {best:.2e}; |t|^(1/2) = {abs(t) ** 0.5:.1e}, |t| = {abs(t):.0e}")
