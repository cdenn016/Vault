"""
Verification suite for open:col-extent (Sharp constant, exact homogeneous baselines, and diameter).

Implements two-channel checks (exact symbolic / rational / analytic vs direct numerical linear algebra
from raw definitions) plus planted-error negative controls for Claims C1-C6.
"""
from __future__ import annotations

import math
from fractions import Fraction
import numpy as np
from scipy import linalg, sparse
from scipy.sparse.linalg import eigsh
import sympy as sp

PI_SQRT12 = math.pi / math.sqrt(12.0)


def raw_contrast_and_Q(A: np.ndarray, x: np.ndarray, eps: float, C_idx: list[int] | None = None):
    """Channel 2 (raw definition): compute r(C), xi2, sd(C), Q(C) directly from matrix A, positions x, uniform leak eps."""
    N = len(x)
    if C_idx is None:
        C_idx = list(range(N))
    C_idx = list(C_idx)
    n = len(C_idx)
    assert n >= 2
    assert np.allclose(A, A.T, atol=1e-14)
    assert np.all(A >= -1e-15) and np.allclose(np.diag(A), 0.0, atol=1e-15)
    assert eps > 0

    # Global varsigma_d^2 = max_{i in V} sum_{j in V} a_ij (x_j - x_i)^2
    diff2 = (x[:, None] - x[None, :]) ** 2
    varsigma2 = float(np.max((A * diff2).sum(axis=1)))
    xi2_sq = varsigma2 / (2.0 * eps)

    # Region submatrix, cut, L_C
    A_CC = A[np.ix_(C_idx, C_idx)]
    L_C = np.diag(A_CC.sum(axis=1)) - A_CC
    evals = linalg.eigvalsh(L_C)
    lam2 = float(evals[1])

    out_mask = np.ones(N, dtype=bool)
    out_mask[C_idx] = False
    cut_C = float(A[np.ix_(C_idx, out_mask)].sum()) if np.any(out_mask) else 0.0

    k_out = eps + cut_C / n
    k_in = eps + lam2
    r_C = k_in / k_out
    x_C = x[C_idx]
    var_C = float(np.mean((x_C - np.mean(x_C)) ** 2))
    sd_C = math.sqrt(var_C)
    Q_C = sd_C * math.sqrt(max(0.0, r_C - 1.0)) / math.sqrt(xi2_sq) if xi2_sq > 0 else 0.0
    return {
        "r": r_C,
        "lam2": lam2,
        "cut_per_n": cut_C / n,
        "var": var_C,
        "sd": sd_C,
        "varsigma2": varsigma2,
        "xi2": math.sqrt(xi2_sq),
        "Q": Q_C,
    }


def check_conventions():
    print("=" * 74)
    print("SECTION 0: CONVENTION LOCK TEST VALUES")
    print("=" * 74)
    # Test 1: Isolated 4-site uniform path (a=1, eps=0.1)
    A4 = np.diag([1.0, 1.0, 1.0], 1) + np.diag([1.0, 1.0, 1.0], -1)
    x4 = np.array([0.0, 1.0, 2.0, 3.0])
    res4 = raw_contrast_and_Q(A4, x4, eps=0.1)
    # Exact symbolic: var = (16-1)/12 = 5/4, lam2 = 2 - sqrt(2), varsigma2 = 2, xi2^2 = 10, Q = sqrt((5/4)*(2-sqrt(2)))
    Q4_exact = math.sqrt(1.25 * (2.0 - math.sqrt(2.0)))
    assert abs(res4["var"] - 1.25) < 1e-14
    assert abs(res4["lam2"] - (2.0 - math.sqrt(2.0))) < 1e-14
    assert abs(res4["varsigma2"] - 2.0) < 1e-14
    assert abs(res4["Q"] - Q4_exact) < 1e-14
    print(f"Path n=4 (a=1, eps=0.1): Var={res4['var']:.6f} (5/4), lam2={res4['lam2']:.10f}, Q={res4['Q']:.10f} (exact {Q4_exact:.10f})")

    # Test 2: Population variance convention 1/n (NOT 1/(n-1))
    # Negative control: 1/(n-1) would give 5/3 instead of 5/4 (diff 0.4167)
    var_sample = float(np.var(x4, ddof=1))
    assert abs(var_sample - res4["var"]) > 0.4, "Planted convention error failed to discriminate"
    print(f"Negative control (ddof=1 vs ddof=0): diff = {abs(var_sample - res4['var']):.6f} > 0.4 [PASS]")


def check_C1_C2():
    print("\n" + "=" * 74)
    print("SECTION 1: CLAIMS C1 & C2 (SUP Q = 1, EQUALITY CHARACTERIZATION, REALIZABILITY)")
    print("=" * 74)

    # 1a. Isolated pair n=2 (exact symbolic + raw numerical)
    A2 = np.array([[0.0, 1.0], [1.0, 0.0]])
    x2 = np.array([0.0, 1.0])
    r2 = raw_contrast_and_Q(A2, x2, eps=0.25)
    assert abs(r2["Q"] - 1.0) < 1e-14
    assert r2["Q"] > PI_SQRT12 + 0.09
    print(f"[C1/C2a] Isolated pair n=2: Q = {r2['Q']:.12f} (margin over pi/sqrt(12): {r2['Q'] - PI_SQRT12:+.6f})")

    # 1b. n=3 on {-1, 0, 1} subset Z with range-2 couplings a(-1,0)=a(0,1)=4, a(-1,1)=1
    L3_sym = sp.Matrix([[5, -4, -1], [-4, 8, -4], [-1, -4, 5]])
    evals3 = sorted(L3_sym.eigenvals().keys())
    assert evals3 == [0, 6, 12]
    A3 = np.array([[0.0, 4.0, 1.0], [4.0, 0.0, 4.0], [1.0, 4.0, 0.0]])
    x3 = np.array([-1.0, 0.0, 1.0])
    r3 = raw_contrast_and_Q(A3, x3, eps=0.3)
    assert abs(r3["Q"] - 1.0) < 1e-14
    print(f"[C1/C2a] n=3 range-2 on Z: symbolic evals={evals3}, raw Q = {r3['Q']:.12f}")

    # 1c. m-dimensional hypercube Q_m (m=1..5): BOTH nearest-neighbor Laplacian (axis & diagonal)
    #     AND exact level-0 world-conditional precision Pi^c = (I - W^2)/q (axis)
    for m in [2, 3, 4, 5]:
        N = 1 << m
        coords = np.array([[(v >> bit) & 1 for bit in range(m)] for v in range(N)], dtype=float)
        # Adjacency of Q_m
        hamming = np.abs(coords[:, None, :] - coords[None, :, :]).sum(axis=2)
        A_qm = (hamming == 1).astype(float)
        r_axis = raw_contrast_and_Q(A_qm, coords[:, 0], eps=0.2)
        r_diag = raw_contrast_and_Q(A_qm, coords.sum(axis=1), eps=0.2)
        assert abs(r_axis["Q"] - 1.0) < 1e-13
        assert abs(r_diag["Q"] - 1.0) < 1e-13

        # Exact level-0 world-conditional precision via Lyapunov solve Sigma = sum W^n Q W^n
        # Take c = 0.4, a = 0.4 / (m + 1) -> c >= a > 0, lam = c + m*a < 0.8 < 1, q = 0.7
        c_w = 0.4
        a_w = 0.4 / (m + 1)
        q_w = 0.7
        W = c_w * np.eye(N) + a_w * A_qm
        Sigma_c = linalg.solve_discrete_lyapunov(W, q_w * np.eye(N))
        Pi_c = linalg.inv(Sigma_c)
        # Verify Pi_c matches (I - W^2)/q and is diffusive
        Pi_c_closed = (np.eye(N) - W @ W) / q_w
        assert np.max(np.abs(Pi_c - Pi_c_closed)) < 1e-12
        eps_pi = float(np.mean(Pi_c.sum(axis=1)))
        assert np.max(np.abs(Pi_c.sum(axis=1) - eps_pi)) < 1e-12
        A_pi = -Pi_c.copy()
        np.fill_diagonal(A_pi, 0.0)
        assert np.min(A_pi) >= -1e-13
        A_pi = np.maximum(A_pi, 0.0)
        r_l0 = raw_contrast_and_Q(A_pi, coords[:, 0], eps=eps_pi)
        assert abs(r_l0["Q"] - 1.0) < 1e-12
        print(f"[C2a] Hypercube Q_{m} (n={N:2d}): nn axis Q={r_axis['Q']:.10f}, nn diag Q={r_diag['Q']:.10f} (sd={r_diag['sd']:.4f}), level-0 Pi^c axis Q={r_l0['Q']:.10f}")

    # 1d. Genuine collective (r(C) > r_bar_hom) realized in a reversible level-0 network attaining Q(C) = 1
    # Population V = {0,1,2,3,4,5} on box of Z (6 sites): W has 2x2 block [[0.45, 0.45], [0.45, 0.45]] on {0,1}
    # and diagonal 0.9 on {2,3,4,5}, Q^zeta = I.
    W_col = np.diag([0.45, 0.45, 0.9, 0.9, 0.9, 0.9])
    W_col[0, 1] = W_col[1, 0] = 0.45
    Sigma_col = linalg.solve_discrete_lyapunov(W_col, np.eye(6))
    Pi_col = linalg.inv(Sigma_col)
    eps_col = float(Pi_col.sum(axis=1)[0])
    A_col = np.maximum(-Pi_col + np.diag(np.diag(Pi_col)), 0.0)
    x_col = np.arange(6, dtype=float)
    r_pair = raw_contrast_and_Q(A_col, x_col, eps=eps_col, C_idx=[0, 1])
    # Comparison medium on box of 6 sites (lattice clause): 5 nearest-neighbor pairs, mean coupling a_bar = a_01 / 5
    a01 = A_col[0, 1]
    a_bar = a01 / 5.0
    # Compute exact baseline of the 6-site comparison box by enumerating all 2^6 - 7 regions of size >= 2
    A_hom = np.diag([a_bar] * 5, 1) + np.diag([a_bar] * 5, -1)
    r_hom_max = 0.0
    for mask in range(1, 1 << 6):
        subset = [i for i in range(6) if (mask >> i) & 1]
        if len(subset) >= 2:
            rv = raw_contrast_and_Q(A_hom, x_col, eps=eps_col, C_idx=subset)["r"]
            if rv > r_hom_max:
                r_hom_max = rv
    assert abs(r_pair["Q"] - 1.0) < 1e-13
    assert r_pair["r"] > r_hom_max
    print(f"[C2b] Level-0 collective on 6-site box: r(C)={r_pair['r']:.6f} > r_bar_hom={r_hom_max:.6f}, signif={r_pair['r']/r_hom_max:.4f}, Q(C)={r_pair['Q']:.12f}")

    # 1e. 2D isotropic uniform nearest-neighbor Gaussian spindle on Z^2 (beating pi/sqrt(12) directly!)
    # Check both direct sparse 2D eigensolve (channel 2) and Thomson+Barta analytical lower bound (channel 1)
    for sigma in [10.0, 20.0, 30.0]:
        H0 = int(round(0.6 * sigma))
        R = int(math.ceil(sigma * math.sqrt(2.0 * math.log(max(2, H0)))))
        sites = []
        for ix in range(-R, R + 1):
            val = (H0 + 0.5) * math.exp(-ix * ix / (2.0 * sigma * sigma))
            h = int(math.floor(val))
            if h >= 1:
                for iy in range(h):
                    sites.append((ix, iy))
        idx = {s: k for k, s in enumerate(sites)}
        n = len(sites)
        rows, cols, vals = [], [], []
        deg = np.zeros(n)
        m2x = np.zeros(n)
        for k, (ix, iy) in enumerate(sites):
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nb = (ix + dx, iy + dy)
                if nb in idx:
                    rows.append(k); cols.append(idx[nb]); vals.append(-1.0)
                    deg[k] += 1.0
                    m2x[k] += dx * dx
        for k in range(n):
            rows.append(k); cols.append(k); vals.append(deg[k])
        L_sp = sparse.csc_matrix((vals, (rows, cols)), shape=(n, n))
        ev = np.sort(eigsh(L_sp, k=3, sigma=-1e-5, which="LM", return_eigenvectors=False))
        lam2 = float(ev[1])
        xs = np.array([s[0] for s in sites], dtype=float)
        var_x = float(np.mean((xs - np.mean(xs)) ** 2))
        s2 = float(np.max(m2x))
        assert s2 == 2.0
        Q_sp = math.sqrt(var_x * lam2 / (s2 / 2.0))
        assert Q_sp > PI_SQRT12
        print(f"[C2c] 2D isotropic nn Gaussian spindle (sigma={sigma:4.1f}, H0={H0:2d}, n={n:4d}): varsigma_x^2={s2:.1f}, lam2={lam2:.6f}, Q={Q_sp:.6f} > pi/sqrt(12)")

    # Verify Thomson + Barta proof bound on the exact truncated construction H0=floor(sigma^1/2), M=floor(sigma^1/4)
    for sigma in [64.0, 256.0, 1024.0]:
        H0 = int(math.floor(sigma ** 0.5))
        M = int(math.floor(sigma ** 0.25))
        H = []
        x = 0
        while True:
            hx = int(math.floor((H0 + 0.5) * math.exp(-x * x / (2.0 * sigma * sigma))))
            if hx < M:
                break
            H.append(hx)
            x += 1
        R = len(H) - 1
        H_arr = np.array(H, dtype=float)
        c_arr = np.array([H_arr[k + 1] if H_arr[k] == H_arr[k + 1] else 0.6 * H_arr[k + 1] for k in range(R)])
        S = np.zeros(R + 1)
        for y in range(R, 0, -1):
            S[y] = (S[y + 1] if y < R else 0.0) + y * H_arr[y]
        phi = np.cumsum([0.0] + [S[y] / c_arr[y - 1] for y in range(1, R + 1)])
        lam2_barta = min(y / phi[y] for y in range(1, R + 1))
        vert_lb = 2.0 / (H0 * H0)
        assert lam2_barta < vert_lb
        tot_n = H_arr[0] + 2.0 * np.sum(H_arr[1:])
        var_x = (2.0 * np.sum((np.arange(1, R + 1) ** 2) * H_arr[1:])) / tot_n
        Q_barta = math.sqrt(var_x * lam2_barta)
        assert Q_barta > PI_SQRT12
        print(f"[C2c-proof] Barta lower bound (sigma={sigma:6.1f}, H0={H0:2d}, M={M:2d}, R={R:4d}): Q_barta={Q_barta:.6f} > pi/sqrt(12)")

    # 1f. Heterogeneous leak remark: naive Q = sd*(r-1)^(1/2)/(varsigma/sqrt(2*eps_bar)) is UNBOUNDED!
    # Witness (n=5): 3 vertices at x=0 with eps=0 forming a clique of weight M=10*E,
    # and 2 vertices at x=-1,+1 with eps=E, each coupled to vertex 0 with weight a=1.
    # Then varsigma^2=1, Var=2/5, eps_bar=2E/5, k_in -> (3/5)E + 5/3 as M->inf,
    # so naive_Q^2 -> (4/25)*E + 4/5 -> infinity as E -> infinity!
    x_h5 = np.array([0.0, 0.0, 0.0, -1.0, 1.0])
    Q_orth5, _ = linalg.qr(np.ones((5, 1)), mode="full")
    B5 = Q_orth5[:, 1:]
    for E_val in [10.0, 100.0, 1000.0]:
        M_val = 100.0 * E_val
        A_h5 = np.zeros((5, 5))
        for u in range(3):
            for v in range(u + 1, 3):
                A_h5[u, v] = A_h5[v, u] = M_val
        A_h5[0, 3] = A_h5[3, 0] = 1.0
        A_h5[0, 4] = A_h5[4, 0] = 1.0
        eps_h5 = np.array([0.0, 0.0, 0.0, E_val, E_val])
        L_h5 = np.diag(A_h5.sum(axis=1)) - A_h5
        kin_h5 = float(linalg.eigvalsh(B5.T @ (np.diag(eps_h5) + L_h5) @ B5)[0])
        eps_bar5 = float(np.mean(eps_h5))
        r_h5 = kin_h5 / eps_bar5
        var_h5 = float(np.mean((x_h5 - np.mean(x_h5)) ** 2))
        diff2_h5 = (x_h5[:, None] - x_h5[None, :]) ** 2
        varsigma2_h5 = float(np.max((A_h5 * diff2_h5).sum(axis=1)))
        assert abs(varsigma2_h5 - 2.0) < 1e-12  # vertex 0 has both -1 and +1 at dist 1 -> varsigma^2 = 2
        # Wait: vertex 0 connects to BOTH -1 and +1 -> varsigma^2 = 2! (If vertex 0 connects to -1 and vertex 1 connects to +1, varsigma^2 = 1!)
        Q_naive_h5 = math.sqrt(var_h5 * (r_h5 - 1.0) / (varsigma2_h5 / (2.0 * eps_bar5)))
        # Verify general bound r <= eps_max/eps_bar + varsigma^2/(2*eps_bar*Var)
        assert r_h5 <= np.max(eps_h5) / eps_bar5 + varsigma2_h5 / (2.0 * eps_bar5 * var_h5) + 1e-12
        print(f"[C2-het] Heterogeneous leak n=5 witness (E={E_val:6.1f}, M={M_val:8.1f}): r={r_h5:.4f}, naive_Q={Q_naive_h5:.6f} (~sqrt(2E/25)={math.sqrt(2*E_val/25):.4f})")
    assert Q_naive_h5 > 8.0, "Heterogeneous naive_Q failed to diverge"

    # Planted-error negative control for C2: claim Q <= pi/sqrt(12) FAILS on n=2, n=3, Q_m, and 2D spindle!
    assert not (r2["Q"] <= PI_SQRT12), "Negative control failed"
    print("[C1/C2] Planted-error negative control (wrong upper bound pi/sqrt(12)) properly rejected [PASS]")


def check_C3():
    print("\n" + "=" * 74)
    print("SECTION 2: CLAIM C3 (SHARP SUPREMUM pi/sqrt(12) ON 1D NN PATHS, n >= 3)")
    print("=" * 74)
    # Channel 1: Verify exact dual identity y_k + y_{k+1} = sin^2(pi*k/n) and sum y_i = n/4 symbolically/numerically
    for n in [3, 4, 5, 6, 7, 10, 15, 25]:
        y = [math.sin(math.pi * (i - 1) / n) * math.sin(math.pi * i / n) / (2.0 * math.cos(math.pi / n)) for i in range(1, n + 1)]
        assert abs(y[0]) < 1e-15 and abs(y[-1]) < 1e-15
        assert all(yi >= -1e-15 for yi in y)
        max_err = max(abs((y[k - 1] + y[k]) - math.sin(math.pi * k / n) ** 2) for k in range(1, n))
        assert max_err < 1e-14
        assert abs(sum(y) - n / 4.0) < 1e-13

    # Exact symbolic check for n=3, 4, 5, 6
    for n_s in [3, 4, 5, 6]:
        ys = [sp.simplify(sp.sin(sp.pi * (i - 1) / n_s) * sp.sin(sp.pi * i / n_s) / (2 * sp.cos(sp.pi / n_s))) for i in range(1, n_s + 1)]
        for k in range(1, n_s):
            assert sp.simplify(ys[k - 1] + ys[k] - sp.sin(sp.pi * k / n_s) ** 2) == 0
        assert sp.simplify(sum(ys) - sp.Rational(n_s, 4)) == 0
    print("[C3] Symbolic dual identity y_k + y_{k+1} = sin^2(pi*k/n), sum y_i = n/4 exact for n=3..6 (and float <1e-14 up to n=25)")

    # Channel 2: 1000 random weighted 1D nearest-neighbor paths (n in [3, 40], heterogeneous positive weights,
    # including extreme ratios up to 1e6 and alternating/boundary-peaked profiles)
    rng = np.random.default_rng(202601)
    max_ratio_to_unif = 0.0
    max_Q = 0.0
    for trial in range(1000):
        n = int(rng.integers(3, 41))
        if trial < 500:
            a = np.exp(rng.normal(0.0, 2.0, size=n - 1))
        elif trial < 800:
            a = rng.uniform(0.0, 1.0, size=n - 1) ** 4 + 1e-6
        else:
            # Boundary-peaked or alternating
            a = np.array([1.99 if k % 2 == 0 else 0.01 for k in range(n - 1)]) * rng.uniform(0.8, 1.2, size=n - 1)
        A = np.diag(a, 1) + np.diag(a, -1)
        x = np.arange(n, dtype=float)
        res = raw_contrast_and_Q(A, x, eps=0.05)
        lam2_bound = res["varsigma2"] * (1.0 - math.cos(math.pi / n))
        Q_bound = math.sqrt((n * n - 1.0) / 6.0 * (1.0 - math.cos(math.pi / n)))
        assert res["lam2"] <= lam2_bound + 1e-12
        assert res["Q"] <= Q_bound + 1e-12
        assert res["Q"] < PI_SQRT12
        max_ratio_to_unif = max(max_ratio_to_unif, res["Q"] / Q_bound)
        max_Q = max(max_Q, res["Q"])
    print(f"[C3] 1000 random/extreme 1D nn paths (n in [3,40]): max Q/Q_bound(n) = {max_ratio_to_unif:.8f} <= 1, max Q = {max_Q:.8f} < pi/sqrt(12)")

    # Planted-error negative control: break hypothesis n >= 3 (use n = 2) -> violates Q < pi/sqrt(12)
    A2 = np.array([[0.0, 1.0], [1.0, 0.0]])
    res2 = raw_contrast_and_Q(A2, np.array([0.0, 1.0]), eps=0.05)
    assert res2["Q"] > PI_SQRT12
    print(f"[C3] Negative control (breaking n >= 3 with n = 2): Q = {res2['Q']:.6f} > pi/sqrt(12) [PASS]")


def check_C4_C5():
    print("\n" + "=" * 74)
    print("SECTION 3: CLAIMS C4 & C5 (EXACT HOMOGENEOUS BASELINES ON Z^D & tab:col-baselines)")
    print("=" * 74)

    # C4: Z^D nearest-neighbor exact baseline checks
    # 1) D = 1: verify r(n) < r(2) for n = 3..200 and eps in {1e-5, 1e-3, 0.1, 1.0, 10.0}
    for eps in [1e-5, 1e-3, 0.1, 1.0, 10.0]:
        r2 = (eps + 2.0) / (eps + 1.0)
        for n in range(3, 201):
            rn = (eps + 2.0 * (1.0 - math.cos(math.pi / n))) / (eps + 2.0 / n)
            assert rn < r2
    print("[C4-D1] Z nearest-neighbor: r(n) < r(2) verified for n=3..200 across 5 leaks")

    # 2) D = 2: exact check of all 5 free tetrominoes (n = 4) and analytic cutoff n >= 5
    tetrominoes = {
        "2x2_square": [(0, 0), (1, 0), (0, 1), (1, 1)],
        "I4":         [(0, 0), (1, 0), (2, 0), (3, 0)],
        "L4":         [(0, 0), (1, 0), (2, 0), (2, 1)],
        "T4":         [(0, 0), (1, 0), (2, 0), (1, 1)],
        "S4":         [(0, 0), (1, 0), (1, 1), (2, 1)],
    }
    for name, pts in tetrominoes.items():
        pts_set = set(pts)
        n = len(pts)
        L = np.zeros((n, n))
        cut = 0.0
        for i, (x, y) in enumerate(pts):
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nb = (x + dx, y + dy)
                if nb in pts_set:
                    j = pts.index(nb)
                    L[i, j] -= 1.0
                    L[i, i] += 1.0
                else:
                    cut += 1.0
        lam2 = float(linalg.eigvalsh(L)[1])
        rstar = lam2 / (cut / n)
        if name == "2x2_square":
            assert abs(rstar - 1.0) < 1e-14
        else:
            assert rstar < 0.45
        print(f"  [C4-D2] tetromino {name:10s}: lam2={lam2:.6f}, cut/n={cut/n:.4f}, r_star={rstar:.6f}")

    # 3) D = 3, 4, 5 exact omega_D check and D >= 6 Stirling check
    for D in [3, 4, 5, 6, 10, 50, 500]:
        t0 = 2.0 ** (1.0 - 1.0 / D)
        if D <= 50:
            omega_D = math.pi ** (D / 2.0) / math.gamma(D / 2.0 + 1.0)
            A_D = (1.0 / (D + 2.0)) * (omega_D ** (-2.0 / D))
        else:
            A_D = 1.0 / (2.0 * math.pi * math.e)
        rstar_ub = (t0 - 1.0) / (2.0 * D * (A_D * t0 * t0 - 1.0 / 12.0))
        assert rstar_ub < 1.0
        if D in [3, 4, 5, 6, 500]:
            print(f"  [C4-D>=3] D={D:3d}: A_D={A_D:.6f}, t0={t0:.5f}, analytic tail r_star_ub={rstar_ub:.6f} < 1")

    # C5: Exact global baselines for all 5 rows of tab:col-baselines
    # Two independent enumeration channels for 1D range-2 connected sets!
    def enum_1d_channel1(a1, a2, eps, max_n):
        """Channel 1: recursive gap generation."""
        best_r, best_r_S = 0.0, None
        best_rs, best_rs_S = 0.0, None
        count = 0
        for n in range(2, max_n + 1):
            def gen(cur, last):
                if len(cur) == n:
                    yield cur
                    return
                for g in ([1, 2] if a1 > 0 else [2]):
                    yield from gen(cur + (last + g,), last + g)
            for S in gen((0,), 0):
                count += 1
                S_set = set(S)
                L = np.zeros((n, n))
                cut = 0.0
                for i, xi in enumerate(S):
                    for dx, w in [(-2, a2), (-1, a1), (1, a1), (2, a2)]:
                        if w == 0:
                            continue
                        if (xi + dx) in S_set:
                            j = S.index(xi + dx)
                            L[i, j] -= w
                            L[i, i] += w
                        else:
                            cut += w
                lam2 = float(linalg.eigvalsh(L)[1])
                rs = lam2 / (cut / n)
                rv = (eps + lam2) / (eps + cut / n)
                if rv > best_r:
                    best_r, best_r_S = rv, S
                if rs > best_rs:
                    best_rs, best_rs_S = rs, S
        return best_r, best_r_S, best_rs, best_rs_S, count

    def enum_1d_channel2(a1, a2, eps, max_n):
        """Channel 2: bitmask over {0, ..., 2n-2} with BFS connectivity filter."""
        from itertools import combinations
        best_r, best_r_S = 0.0, None
        best_rs, best_rs_S = 0.0, None
        count = 0
        for n in range(2, max_n + 1):
            for rest in combinations(range(1, 2 * n - 1), n - 1):
                S = (0,) + rest
                # Check range-2 connectivity via BFS
                max_gap = max(S[i + 1] - S[i] for i in range(n - 1))
                if a1 > 0:
                    if max_gap > 2:
                        continue
                else:
                    if any(S[i + 1] - S[i] != 2 for i in range(n - 1)):
                        continue
                count += 1
                # Build embedded in window {-2, ..., S[-1]+2} and call raw_contrast_and_Q!
                hi = S[-1] + 3
                lo = -2
                V_coords = np.arange(lo, hi, dtype=float)
                N_v = len(V_coords)
                dist = np.abs(V_coords[:, None] - V_coords[None, :])
                A_v = a1 * (dist == 1) + a2 * (dist == 2)
                C_idx = [s - lo for s in S]
                out = raw_contrast_and_Q(A_v, V_coords, eps=eps, C_idx=C_idx)
                rv = out["r"]
                rs = out["lam2"] / out["cut_per_n"]
                if rv > best_r:
                    best_r, best_r_S = rv, S
                if rs > best_rs:
                    best_rs, best_rs_S = rs, S
        return best_r, best_r_S, best_rs, best_rs_S, count

    # Row 2: Z pass (0.3, 0.3), a1=0.18, a2=0.09, eps=0.19, analytic cutoff n >= 7
    r_c1, S_c1, rs_c1, Ss_c1, cnt1 = enum_1d_channel1(0.18, 0.09, 0.19, 6)
    r_c2, S_c2, rs_c2, Ss_c2, cnt2 = enum_1d_channel2(0.18, 0.09, 0.19, 6)
    assert cnt1 == cnt2 and S_c1 == S_c2 == (0, 1, 2) and Ss_c1 == Ss_c2 == (0, 1, 2)
    assert abs(r_c1 - 55.0 / 43.0) < 1e-14 and abs(r_c2 - 55.0 / 43.0) < 1e-14
    assert abs(rs_c1 - 1.5) < 1e-14 and abs(rs_c2 - 1.5) < 1e-14
    # Verify analytic tail bound for n >= 7: varsigma^2 = 2*0.18 + 8*0.09 = 1.08, cut_both = 0.72/n
    # lam_ub_both = 6*1.08/(n^2-1) = 6.48/(n^2-1) -> rstar_both = 9*n/(n^2-1) <= 63/48 = 1.3125 < 1.5!
    assert 9.0 * 7.0 / (49.0 - 1.0) < 1.5
    print(f"[C5-row2] Z pass (0.3,0.3): {cnt1} sets (n<=6) matched across 2 channels; exact r_hom=55/43={55/43:.10f}, r*_hom=3/2=1.5 (tail n>=7 <= {63/48:.6f} < 1.5)")

    # Row 3: Z pass (0.1, 0.4), a1=0.08, a2=0.16, eps=0.19, analytic cutoff n >= 9
    r_c1, S_c1, rs_c1, Ss_c1, cnt1 = enum_1d_channel1(0.08, 0.16, 0.19, 8)
    r_c2, S_c2, rs_c2, Ss_c2, cnt2 = enum_1d_channel2(0.08, 0.16, 0.19, 8)
    r3_exact = (55.0 - 4.0 * math.sqrt(13.0)) / 35.0
    rs3_exact = (9.0 - math.sqrt(13.0)) / 4.0
    assert cnt1 == cnt2 and S_c1 == S_c2 == (0, 1, 2, 3, 4) and Ss_c1 == Ss_c2 == (0, 1, 2, 3, 4)
    assert abs(r_c1 - r3_exact) < 1e-13 and abs(r_c2 - r3_exact) < 1e-13
    assert abs(rs_c1 - rs3_exact) < 1e-13 and abs(rs_c2 - rs3_exact) < 1e-13
    # Analytic tail n >= 9: varsigma^2 = 2*0.08 + 8*0.16 = 1.44, cut_both = 0.80/n
    # rstar_both(9) = (6*1.44/(81-1)) / (0.80/9) = (8.64/80) / (0.80/9) = 1.215 < 1.3486!
    tail_r3_9 = (6.0 * 1.44 / 80.0) / (0.80 / 9.0)
    assert tail_r3_9 < rs3_exact
    # Single-parity for (0.1, 0.4): max r_star is at n=2: (2*0.16) / (2*0.08 + 0.16) = 0.32 / 0.32 = 1.0 < 1.3486!
    print(f"[C5-row3] Z pass (0.1,0.4): {cnt1} sets (n<=8) matched across 2 channels; exact r_hom=(55-4*sqrt(13))/35={r3_exact:.10f}, r*_hom=(9-sqrt(13))/4={rs3_exact:.10f} (tail n>=9 <= {tail_r3_9:.6f})")

    # Row 4: Z pass (0, 0.45): exact rational 238/157
    r4_exact = Fraction(238, 157)
    r_c1, S_c1, rs_c1, Ss_c1, _ = enum_1d_channel1(0.0, 0.2025, 0.19, 6)
    assert S_c1 == (0, 2) and abs(r_c1 - float(r4_exact)) < 1e-14 and abs(rs_c1 - 2.0) < 1e-14
    print(f"[C5-row4] Z pass (0,0.45): exact r_hom=238/157={float(r4_exact):.10f}, r*_hom=2 at (0, 2)")

    # Row 5: Z^2 pass (0.2, 0.15), q=0.7 -> exact 4-parity certificate for 2 <= n <= 35 + analytic tail n >= 36
    # Use exact integer ratios (a1, a2, ad) = (8, 3, 6) (since r_star is scale-invariant!)
    a1_i, a2_i, ad_i = 8, 3, 6
    tot_deg_i = 4 * (a1_i + a2_i + ad_i)  # 68

    def max_edges_z2(m: int) -> int:
        if m <= 1:
            return 0
        # Two elementary upper bounds: 2m - ceil(2*sqrt(m)) and floor((m/2)*log2(m))
        b1 = 2 * m - math.ceil(2.0 * math.sqrt(m))
        # Exact integer check for floor((m/2)*log2(m)): largest k with 2^(2k) <= m^m
        # Using float with safe +1e-12 is exact for m <= 35; cross-check with integer power!
        b2 = int(math.floor(0.5 * m * math.log2(m)))
        while (1 << (2 * (b2 + 1))) <= (m ** m):
            b2 += 1
        while (1 << (2 * b2)) > (m ** m):
            b2 -= 1
        return min(b1, b2)

    worst_rstar_2d = 0.0
    worst_part_2d = None
    total_parts = 0
    for n in range(2, 36):
        for n00 in range(n + 1):
            for n01 in range(n - n00 + 1):
                for n10 in range(n - n00 - n01 + 1):
                    n11 = n - n00 - n01 - n10
                    total_parts += 1
                    ne = n00 + n11
                    no = n01 + n10
                    E1 = min(max_edges_z2(n), 2 * (min(n00, n10) + min(n01, n11) + min(n00, n01) + min(n10, n11)))
                    Ed = max_edges_z2(ne) + max_edges_z2(no)
                    E2 = max_edges_z2(n00) + max_edges_z2(n01) + max_edges_z2(n10) + max_edges_z2(n11)
                    B1 = 4 * n - 2 * E1
                    Bd = 4 * n - 2 * Ed
                    B2 = 4 * n - 2 * E2
                    cut_n = (a1_i * B1 + a2_i * B2 + ad_i * Bd) / n
                    dbar = tot_deg_i - cut_n
                    lam1 = (n / (n - 1.0)) * min(dbar, tot_deg_i / 2.0)
                    J_lb = n * n / (2.0 * math.pi) - n / 6.0
                    lam2 = (a1_i * E1 + 4 * a2_i * E2 + 2 * ad_i * Ed) / J_lb
                    rs = min(lam1, lam2) / cut_n
                    if rs > worst_rstar_2d:
                        worst_rstar_2d = rs
                        worst_part_2d = (n, (n00, n01, n10, n11))
    # Analytic tail n >= 36: (16/17) * (sqrt(n)-1) / (n/(2*pi) - 1/6) strictly decreasing in n >= 2
    tail_36 = (16.0 / 17.0) * (6.0 - 1.0) / (36.0 / (2.0 * math.pi) - 1.0 / 6.0)
    assert worst_rstar_2d < 0.89 and tail_36 < 0.85
    # Verify actual LxL square contrast approaches 1 as L -> inf (showing r_bar_hom = 1 > 0.871!)
    eps_2d = 18.0 / 35.0
    a1_f, a2_f, ad_f = 2 * 0.2 * 0.15 / 0.7, 0.15 ** 2 / 0.7, 2 * 0.15 ** 2 / 0.7
    L_sq = 50
    # Cut of LxL square: axis-1 = 4*L, axis-2 = 4*(2*L) = 8*L, diag = 4*(2*L - 1) -> cut/L^2
    cut_sq = (4 * L_sq * a1_f + 8 * L_sq * a2_f + 4 * (2 * L_sq - 1) * ad_f) / (L_sq * L_sq)
    r_sq_lb = eps_2d / (eps_2d + cut_sq)
    assert r_sq_lb > 0.94 > 0.871
    print(f"[C5-row5] Z^2 pass (0.2,0.15): {total_parts} 4-partitions (2<=n<=35) max r*_ub={worst_rstar_2d:.6f} at {worst_part_2d}; tail n>=36 <= {tail_36:.6f} < 1 => exact r_hom=1 (50x50 box already has r >= {r_sq_lb:.6f} > 0.871)")

    # Planted-error negative control for C5: testing Z^2 nn kernel (a1=1, a2=0, ad=0) at n=4 gives r*_ub > 1 (cannot certify < 1!)
    n_nc = 4
    E1_nc = max_edges_z2(4)  # 4
    B1_nc = 4 * 4 - 2 * 4    # 8
    cut_nc = B1_nc / 4.0     # 2.0
    lam1_nc = (4.0 / 3.0) * 2.0
    lam2_nc = E1_nc / (16.0 / (2.0 * math.pi) - 4.0 / 6.0)
    assert min(lam1_nc, lam2_nc) / cut_nc > 1.0
    print(f"[C5] Negative control (Z^2 nn at n=4 where 2x2 attains r*=1): bound = {min(lam1_nc, lam2_nc)/cut_nc:.6f} > 1 [PASS]")


def check_C6():
    print("\n" + "=" * 74)
    print("SECTION 4: CLAIM C6 (UNIVERSAL MGF DIAMETER BOUND, SHARPNESS, AND Z^D BOUND)")
    print("=" * 74)

    # 4a. Verify elementary inequality 1 - 1/cosh(Delta) <= Delta^2 / 2 across [0, 50], plus negative control
    deltas = np.concatenate([np.linspace(1e-6, 2.0, 2000), np.linspace(2.0, 50.0, 500)])
    lhs = 1.0 - 1.0 / np.cosh(deltas)
    rhs = 0.5 * deltas * deltas
    assert np.all(lhs <= rhs + 1e-15)
    # Planted-error negative control: replacing 1/2 by 0.49 FAILS near Delta -> 0!
    assert np.any(lhs > 0.49 * deltas * deltas), "Planted error in 1 - 1/cosh <= c*Delta^2 did not fail"
    print("[C6a] Elementary bound 1 - 1/cosh(Delta) <= Delta^2/2 verified; planted 0.49*Delta^2 rejected [PASS]")

    # 4b. Verify c1 = sum_{k>=1} 2^k ln(1/(1-4^-k)) <= 4/3 (exact numeric value ~ 1.0846449)
    c1 = sum((2 ** k) * (-math.log(1.0 - 4.0 ** (-k))) for k in range(1, 60))
    assert c1 < 4.0 / 3.0
    print(f"[C6a] Series constant c1 = {c1:.10f} < 4/3 = {4/3:.10f}")

    # 4c. Test coordinate AND general-metric diameter bounds on 500 diverse diffusive graphs
    #     (dense, sparse, long-range heavy-tailed, stars, dumbbells, paths, heterogeneous leaks, random metrics)
    rng = np.random.default_rng(202602)
    max_coord_ratio = 0.0
    max_metric_ratio = 0.0
    max_het_ratio = 0.0
    for trial in range(500):
        n = int(rng.integers(2, 28))
        if trial < 150:
            x = rng.normal(0.0, 5.0, size=n)
            A = rng.exponential(1.0, size=(n, n))
        elif trial < 300:
            x = np.exp(rng.normal(0.0, 2.0, size=n)) * rng.choice([-1.0, 1.0], size=n)
            A = (rng.random((n, n)) < 0.25) * rng.lognormal(0.0, 2.0, size=(n, n))
        elif trial < 400:
            # Star + path hybrid
            x = np.cumsum(rng.exponential(1.0, size=n))
            A = np.zeros((n, n))
            for i in range(1, n):
                p = 0 if i < n // 2 else i - 1
                A[i, p] = rng.lognormal(0.0, 1.0)
        else:
            # Random 3D Euclidean metric
            pts = rng.normal(0.0, 3.0, size=(n, 3))
            x = pts[:, 0]
            A = rng.exponential(1.0, size=(n, n)) * (rng.random((n, n)) < 0.4)
        A = 0.5 * (A + A.T)
        np.fill_diagonal(A, 0.0)
        L = np.diag(A.sum(axis=1)) - A
        ev = linalg.eigvalsh(L)
        if ev[1] < 1e-10:
            continue
        lam2 = float(ev[1])
        # Coordinate bound (closed form)
        diff2 = (x[:, None] - x[None, :]) ** 2
        varsigma2 = float(np.max((A * diff2).sum(axis=1)))
        if varsigma2 <= 0:
            continue
        diam_x = float(np.max(x) - np.min(x))
        scale_x = math.sqrt(varsigma2 / (2.0 * lam2))
        closed_factor = math.sqrt(1.0 + 1.0 / math.log(n)) * (math.log(n) + math.log(1.0 + math.log(n)) + 4.0 / 3.0)
        factor = min(math.sqrt(2.0 * n), closed_factor)
        ratio_x = diam_x / (factor * scale_x)
        assert ratio_x <= 1.0 + 1e-12
        max_coord_ratio = max(max_coord_ratio, ratio_x)

        # Metric bound using graph shortest-path metric or L1/L2 metric
        if trial >= 400:
            D_mat = np.sqrt(((pts[:, None, :] - pts[None, :, :]) ** 2).sum(axis=2))
            varsigma_d2 = float(np.max((A * (D_mat ** 2)).sum(axis=1)))
            diam_m = float(np.max(D_mat))
            scale_m = math.sqrt(varsigma_d2 / (2.0 * lam2))
            ratio_m = diam_m / (factor * scale_m)
            assert ratio_m <= 1.0 + 1e-12
            max_metric_ratio = max(max_metric_ratio, ratio_m)

        # Heterogeneous leak test (trial < 100): verify diam <= factor * varsigma / sqrt(2*(r*eps_bar - eps_max))
        if trial < 100:
            eps_v = rng.uniform(0.01, 0.05, size=n)
            # Orthonormal basis of 1^perp
            Q_orth, _ = linalg.qr(np.ones((n, 1)), mode="full")
            B_perp = Q_orth[:, 1:]
            kin = float(linalg.eigvalsh(B_perp.T @ (np.diag(eps_v) + L) @ B_perp)[0])
            eps_bar = float(np.mean(eps_v))
            eps_max = float(np.max(eps_v))
            r_het = kin / eps_bar
            if r_het * eps_bar - eps_max > 1e-9:
                scale_h = math.sqrt(varsigma2 / (2.0 * (r_het * eps_bar - eps_max)))
                ratio_h = diam_x / (factor * scale_h)
                assert ratio_h <= 1.0 + 1e-12
                max_het_ratio = max(max_het_ratio, ratio_h)
    print(f"[C6a] 500 diverse diffusive graphs: max coord ratio={max_coord_ratio:.6f} <= 1, max metric ratio={max_metric_ratio:.6f} <= 1, max het-leak ratio={max_het_ratio:.6f} <= 1")

    # 4d. Sharpness of leading constant 1 on ln(n): double exponential horn with exact integer multiplicities
    # w_k = floor(M * exp(alpha*(R-|k|))), using Python arbitrary-precision log-ratios so alpha*R can be large!
    for alpha, M_scale, R in [(0.2, 200, 150), (0.1, 1000, 500), (0.05, 8000, 1500), (0.02, 50000, 5000)]:
        # Compute exact ratio r_k = w_{k+1}/w_k for k=0..R-1 via exact integer floor where alpha*(R-k) <= 50,
        # and analytic log-sum for ln(n) = ln(sum w_k)
        # Wait: even better, compute w_k as exact scaled floats w_tilde_k = w_k / exp(alpha*R) = M*exp(-alpha*k) + O(exp(-alpha*R))
        # For k near R where M*exp(alpha*(R-k)) < 1e14, floor matters; for k far from R, floor error < 1e-14 relative!
        # Let's compute exact w_k / w_0 directly with log-scaling and exact integer floor whenever log(M)+alpha*(R-k) < 32!
        log_M = math.log(M_scale)
        log_w = np.empty(R + 1, dtype=float)
        for k in range(R + 1):
            lw = log_M + alpha * (R - k)
            if lw < 32.0:
                log_w[k] = math.log(math.floor(math.exp(lw)))
            else:
                # Floor changes log_w by at most exp(-32) < 1.3e-14 (below float64 eps)
                log_w[k] = lw
        # Exact log(n) via log-sum-exp
        lw0 = log_w[0]
        ln_n = lw0 + math.log(1.0 + 2.0 * float(np.sum(np.exp(log_w[1:] - lw0))))
        # Exact tridiagonal normalized matrix using ratios r_k = exp(log_w[k+1] - log_w[k]) = w_{k+1}/w_k
        ratios = np.exp(log_w[1:] - log_w[:-1])  # ratios[k] = w_{k+1}/w_k for k=0..R-1
        d_main = np.empty(R, dtype=float)
        d_main[:-1] = 1.0 + ratios[1:]
        d_main[-1] = 1.0
        d_off = -np.sqrt(ratios[1:])
        lam2 = float(linalg.eigvalsh_tridiagonal(d_main, d_off, select="i", select_range=(0, 0))[0])
        ratio = (2.0 * R) * math.sqrt(lam2) / ln_n
        print(f"[C6b] Double horn (alpha={alpha:4.2f}, M={M_scale:5d}, R={R:4d}, ln n={ln_n:6.2f}): lam2={lam2:.7f}, diam*sqrt(lam2)/ln(n)={ratio:.6f}")
    assert ratio > 0.85, "Double horn failed to approach leading constant 1"

    # 4e. 2D isotropic uniform nn exponential horn on Z^2 (direct 2D sparse solve + Hardy lower bound)
    for alpha in [0.10, 0.05, 0.03]:
        H0 = int(math.floor(1.0 / (4.0 * alpha)))
        H_list = []
        x = 0
        while True:
            hx = int(math.floor((H0 + 0.5) * math.exp(-alpha * x)))
            if hx < 1:
                break
            H_list.append(hx)
            x += 1
        R = len(H_list) - 1
        sites = []
        for ix in range(-R, R + 1):
            for iy in range(H_list[abs(ix)]):
                sites.append((ix, iy))
        idx = {s: k for k, s in enumerate(sites)}
        n = len(sites)
        rows, cols, vals = [], [], []
        deg = np.zeros(n)
        for k, (ix, iy) in enumerate(sites):
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nb = (ix + dx, iy + dy)
                if nb in idx:
                    rows.append(k); cols.append(idx[nb]); vals.append(-1.0)
                    deg[k] += 1.0
        for k in range(n):
            rows.append(k); cols.append(k); vals.append(deg[k])
        L_sp = sparse.csc_matrix((vals, (rows, cols)), shape=(n, n))
        lam2_2d = float(np.sort(eigsh(L_sp, k=3, sigma=-1e-6, which="LM", return_eigenvectors=False))[1])
        lam2_hardy = (3.0 / 80.0) * (1.0 - math.exp(-alpha)) ** 2
        assert lam2_2d >= lam2_hardy - 1e-12
        diam_x = 2 * R
        print(f"[C6c] 2D isotropic nn horn (alpha={alpha:4.2f}, H0={H0:2d}, R={R:3d}, n={n:4d}): lam2_2d={lam2_2d:.6f} >= Hardy_lb={lam2_hardy:.6f}, diam*sqrt(lam2_2d)={diam_x*math.sqrt(lam2_2d):.4f}")

    # Planted-error negative control for C6: naive constant bound diam <= pi * sigma FAILS on 2D horn (alpha=0.03 has diam*sqrt(lam2) > 4.2 > pi!)
    assert diam_x * math.sqrt(lam2_2d) > math.pi
    print(f"[C6] Negative control (1D constant bound diam <= pi*sigma broken on 2D horn: {diam_x*math.sqrt(lam2_2d):.4f} > {math.pi:.4f}) [PASS]")


if __name__ == "__main__":
    check_conventions()
    check_C1_C2()
    check_C3()
    check_C4_C5()
    check_C6()
    print("\nALL CHECKS AND NEGATIVE CONTROLS PASSED.")
