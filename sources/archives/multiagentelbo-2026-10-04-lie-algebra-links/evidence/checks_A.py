r"""Float64 validation checks for fragment A (exponential chart, loop defect, generator prior).

These checks validate identities of frag_A_geometry.tex at small size. They are validation
only: no statement of the fragment rests on them, and a finite computation is never evidence
for a general claim.

Run:  C:/anaconda/python.exe checks_A.py  > checks_A_output.txt
"""
from __future__ import annotations

import os

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import math

import numpy as np
from scipy.linalg import expm, logm, null_space, polar, sqrtm

RNG = np.random.default_rng(20261003)
RESULTS: list[tuple[str, float, float, bool]] = []
E_CONST = math.e / 2.0 + math.e**2 / 8.0  # cubic constant of prop:link-loop-defect(e)


def record(name: str, value: float, tol: float, ok: bool | None = None) -> None:
    """Record a check: value compared with tolerance (ok overrides the default value<=tol)."""
    passed = (value <= tol) if ok is None else ok
    RESULTS.append((name, float(value), float(tol), bool(passed)))
    print(f"[{'PASS' if passed else 'FAIL'}] {name}: value={value:.3e} tol={tol:.1e}")


def rel(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.linalg.norm(a - b) / max(1.0, np.linalg.norm(b)))


def spd(n: int, rng: np.random.Generator, spread: float = 1.0) -> np.ndarray:
    r"""Random SPD matrix with eigenvalues spread over [e^{-spread}, e^{spread}]."""
    q, _ = np.linalg.qr(rng.standard_normal((n, n)))
    ev = np.exp(rng.uniform(-spread, spread, n))
    return (q * ev) @ q.T


def glplus(n: int, rng: np.random.Generator, scale: float = 0.4) -> np.ndarray:
    a = np.eye(n) + scale * rng.standard_normal((n, n))
    if np.linalg.det(a) < 0:
        a[:, 0] *= -1.0
    return a


def gnorm2(h: np.ndarray, g: np.ndarray) -> float:
    r"""\|H\|_G^2 = Tr(G^{-1} H^T G H)."""
    return float(np.trace(np.linalg.solve(g, h.T @ g @ h)))


def ginner(h1: np.ndarray, h2: np.ndarray, g: np.ndarray) -> float:
    return float(np.trace(np.linalg.solve(g, h1.T @ g @ h2)))


def defect(p: np.ndarray, g: np.ndarray) -> float:
    r"""Loop defect Q = (1/2)\|I - P\|_G^2."""
    return 0.5 * gnorm2(np.eye(p.shape[0]) - p, g)


def prod_exp(hs: list[np.ndarray]) -> np.ndarray:
    out = np.eye(hs[0].shape[0])
    for h in hs:
        out = out @ expm(h)
    return out


def E(n: int, i: int, j: int) -> np.ndarray:
    """Matrix unit E_{ij} (1-based indices, as in the manuscript)."""
    m = np.zeros((n, n))
    m[i - 1, j - 1] = 1.0
    return m


# ----------------------------------------------------------------------------------------------
def check_c1_exp_naturality() -> None:
    print("\n== C1 lem:link-exp-naturality ==")
    rng = RNG
    worst = 0.0
    for _ in range(20):
        g = glplus(4, rng)
        a = 0.6 * rng.standard_normal((4, 4))
        worst = max(worst, rel(g @ expm(a) @ np.linalg.inv(g), expm(g @ a @ np.linalg.inv(g))))
    record("C1a g exp(A) g^-1 = exp(Ad_g A), GL(4)", worst, 1e-12)
    # adjoint representation of GL(3) on gl(3) (column-major vec): Ad_g = (g^{-T} kron g),
    # d(Ad)_A = ad_A = I kron A - A^T kron I
    worst_b = worst_c = 0.0
    for _ in range(20):
        a = 0.6 * rng.standard_normal((3, 3))
        g = glplus(3, rng)
        ad_a = np.kron(np.eye(3), a) - np.kron(a.T, np.eye(3))
        ea = expm(a)
        Ad_ea = np.kron(np.linalg.inv(ea).T, ea)
        worst_b = max(worst_b, rel(expm(ad_a), Ad_ea))
        Ad_g = np.kron(np.linalg.inv(g).T, g)
        gag = g @ a @ np.linalg.inv(g)
        ad_gag = np.kron(np.eye(3), gag) - np.kron(gag.T, np.eye(3))
        worst_c = max(worst_c, rel(ad_gag, Ad_g @ ad_a @ np.linalg.inv(Ad_g)))
    record("C1b rho(exp A) = exp(d rho A) for rho = Ad of GL(3)", worst_b, 1e-11)
    record("C1c d rho(Ad_g A) = rho(g) d rho(A) rho(g)^-1", worst_c, 1e-11)


# ----------------------------------------------------------------------------------------------
# triangle of the running example (0-based vertices): e1: 1->0, e2: 2->1, e3: 0->2;
# the walk p=(e1,e2,e3) is closed at vertex 0 (e_a : i_{a+1} -> i_a).
TRI = [(1, 0), (2, 1), (0, 2)]  # (source j, target i)


def check_c2_generator_gauge() -> None:
    print("\n== C2 prop:link-generator-gauge ==")
    rng = RNG
    K = 3
    U = [glplus(K, rng) for _ in range(3)]
    w = [0.5 * rng.standard_normal((K, K)) for _ in range(3)]
    links = [U[i] @ expm(w[e]) @ np.linalg.inv(U[j]) for e, (j, i) in enumerate(TRI)]
    # reversal
    err = max(rel(U[j] @ expm(-w[e]) @ np.linalg.inv(U[i]), np.linalg.inv(links[e]))
              for e, (j, i) in enumerate(TRI))
    record("C2a reversal: links of -w are inverse links", err, 1e-12)
    # passive re-expression
    g = [glplus(K, rng) for _ in range(3)]
    Up = [g[i] @ U[i] for i in range(3)]
    err = max(rel(g[i] @ links[e] @ np.linalg.inv(g[j]), Up[i] @ expm(w[e]) @ np.linalg.inv(Up[j]))
              for e, (j, i) in enumerate(TRI))
    record("C2b passive: g_i Theta g_j^-1 = U'_i exp(w) U'_j^-1 with U'=gU", err, 1e-12)
    # reference change sigma' = sigma g0
    g0 = glplus(K, rng)
    Ur = [U[i] @ g0 for i in range(3)]
    wr = [np.linalg.inv(g0) @ w[e] @ g0 for e in range(3)]
    err = max(rel(Ur[i] @ expm(wr[e]) @ np.linalg.inv(Ur[j]), links[e]) for e, (j, i) in enumerate(TRI))
    record("C2c reference change: frames U g0, generators Ad_{g0^-1} w give the same links", err, 1e-12)
    W = prod_exp(w)
    Wr = prod_exp(wr)
    record("C2d reference holonomy g0^-1 W g0", rel(Wr, np.linalg.inv(g0) @ W @ g0), 1e-12)
    # active automorphism with F(sigma) = sigma.kappa: phi_i = U_i kappa U_i^-1
    kap = glplus(K, rng)
    phi = [U[i] @ kap @ np.linalg.inv(U[i]) for i in range(3)]
    T = lambda i, j: U[i] @ np.linalg.inv(U[j])  # noqa: E731
    err_act = max(rel(phi[j], np.linalg.inv(T(i, j)) @ phi[i] @ T(i, j)) for i in range(3) for j in range(3))
    record("C2e active local functions satisfy phi_j = T_ij^-1 phi_i T_ij", err_act, 1e-12)
    err = max(rel(phi[i] @ links[e] @ np.linalg.inv(phi[j]),
                  U[i] @ expm(kap @ w[e] @ np.linalg.inv(kap)) @ np.linalg.inv(U[j]))
              for e, (j, i) in enumerate(TRI))
    record("C2f active: image links are the links of Ad_kappa w", err, 1e-12)
    hol = links[0] @ links[1] @ links[2]
    record("C2g Hol(p) = U_0 W U_0^-1", rel(hol, U[0] @ W @ np.linalg.inv(U[0])), 1e-12)


# ----------------------------------------------------------------------------------------------
def check_c3_chart_image() -> None:
    print("\n== C3 prop:link-chart-image ==")
    rng = RNG
    D = np.diag([-1.0, -2.0])
    P = expm(np.diag([0.0, math.log(2.0)])) @ expm(math.pi * (E(2, 2, 1) - E(2, 1, 2)))
    record("C3a exp(diag(0,log2)) exp(pi(E21-E12)) = diag(-1,-2)", rel(P, D), 1e-14)
    L = logm(D)
    imag = float(np.linalg.norm(np.imag(L)))
    record("C3b (sanity, not proof) principal logm(diag(-1,-2)) has imaginary part", imag, 1.0,
           ok=imag > 1.0)
    worst = 0.0
    for _ in range(20):
        a = 0.7 * rng.standard_normal((4, 4))
        worst = max(worst, abs(np.linalg.det(expm(a)) - math.exp(np.trace(a))) / math.exp(np.trace(a)))
    record("C3c det exp(A) = exp(tr A)", worst, 1e-12)
    worst = worst_sym = worst_skew = worst_tri = 0.0
    for _ in range(20):
        a = rng.standard_normal((3, 3))
        if np.linalg.det(a) < 0:
            a[:, 0] *= -1
        o, p = polar(a, side="left")  # a = p o, p SPD
        s = np.real(logm(p))
        z = np.real(logm(o))
        worst = max(worst, rel(expm(s) @ expm(z), a))
        worst_sym = max(worst_sym, float(np.linalg.norm(s - s.T)))
        worst_skew = max(worst_skew, float(np.linalg.norm(z + z.T)))
        # triangle walk traversing three pairs once: generators (s, z, 0) give holonomy a
        worst_tri = max(worst_tri, rel(prod_exp([s, z, np.zeros((3, 3))]), a))
    record("C3d A = exp(S) exp(V), GL+(3), S symmetric, V skew", worst, 1e-10)
    record("C3e S symmetric", worst_sym, 1e-10)
    record("C3f V skew", worst_skew, 1e-10)
    record("C3g triangle with generators (S,V,0) has reference holonomy A", worst_tri, 1e-10)


# ----------------------------------------------------------------------------------------------
def check_c4_blindness() -> None:
    print("\n== C4 prop:link-class-function-blindness, cor:link-no-invariant-defect ==")
    rng = RNG
    K = 3
    shear = np.eye(K) + E(K, 1, 2)
    for name, N, B in [("shear", E(K, 1, 2), np.eye(K)),
                       ("random unipotent", E(K, 1, 2) + E(K, 2, 3), rng.standard_normal((K, K)))]:
        if np.linalg.det(B) < 0:
            B[:, 0] *= -1.0
        Uni = B @ (np.eye(K) + N) @ np.linalg.inv(B)
        dists = []
        for t in [1e-1, 1e-2, 1e-3, 1e-4]:
            Tt = np.diag([t**k for k in range(K)])
            C = B @ Tt
            assert np.linalg.det(C) > 0
            dists.append(float(np.linalg.norm(np.linalg.inv(C) @ Uni @ C - np.eye(K))))
        ratio = dists[-1] / dists[0]
        record(f"C4a {name}: positive-determinant conjugates tend to I (dist at t=1e-4 / t=1e-1)", ratio,
               2e-3)
    # eigenvalue statistics vanish at the shear
    ev = np.linalg.eigvals(shear)
    stats = [float(np.sum(np.abs(ev - 1.0) ** 2)), float(K - np.real(np.sum(ev))),
             float(np.sqrt(np.mean(np.abs(np.log(ev.astype(complex))) ** 2)))]
    record("C4b eigenvalue statistics at the shear (max abs)", max(abs(s) for s in stats), 1e-14)
    # the loop defect is not a class function and sees the shear
    q_id = defect(shear, np.eye(K))
    record("C4c loop defect of the shear with G = I equals 1/2", abs(q_id - 0.5), 1e-15)
    worst_min = min(defect(shear, spd(K, rng, 1.5)) for _ in range(50))
    record("C4d loop defect of the shear is positive for random G (min)", worst_min, 0.0, ok=worst_min > 0)


# ----------------------------------------------------------------------------------------------
def check_c5_zero_set_frame_image() -> None:
    print("\n== C5 prop:link-loop-defect (a),(c) ==")
    rng = RNG
    K = 3
    G = spd(K, rng, 1.0)
    record("C5a defect(I) = 0", abs(defect(np.eye(K), G)), 1e-15)
    mins = min(defect(prod_exp([0.3 * rng.standard_normal((K, K)) for _ in range(3)]), G) for _ in range(200))
    record("C5b defect > 0 at random holonomies (min)", mins, 0.0, ok=mins > 0)
    # submultiplicativity and ||I||_G
    sub = max(math.sqrt(gnorm2(a @ b, G)) - math.sqrt(gnorm2(a, G)) * math.sqrt(gnorm2(b, G))
              for a, b in ((rng.standard_normal((K, K)), rng.standard_normal((K, K))) for _ in range(500)))
    record("C5c ||AB||_G <= ||A||_G ||B||_G (max excess)", sub, 1e-12, ok=sub <= 1e-12)
    record("C5d ||I||_G = sqrt(dim)", abs(math.sqrt(gnorm2(np.eye(K), G)) - math.sqrt(K)), 1e-14)
    worst_c = worst_law = worst_vert = worst_conv = 0.0
    for _ in range(20):
        U = [glplus(K, rng) for _ in range(3)]
        W = prod_exp([0.5 * rng.standard_normal((K, K)) for _ in range(3)])
        Gi = [np.linalg.inv(U[i]).T @ G @ np.linalg.inv(U[i]) for i in range(3)]
        hol = U[0] @ W @ np.linalg.inv(U[0])
        D = np.eye(K) - hol
        pen = float(np.trace(np.linalg.solve(Gi[0], D.T @ Gi[0] @ D)))
        worst_c = max(worst_c, abs(defect(W, G) - 0.5 * pen) / max(1.0, pen))
        g = glplus(K, rng)
        Up = g @ U[0]
        Gp = np.linalg.inv(Up).T @ G @ np.linalg.inv(Up)
        worst_law = max(worst_law, rel(Gp, np.linalg.inv(g).T @ Gi[0] @ np.linalg.inv(g)))
        Tij = U[1] @ np.linalg.inv(U[2])
        worst_vert = max(worst_vert, rel(Gi[1], np.linalg.inv(Tij).T @ Gi[2] @ np.linalg.inv(Tij)))
        worst_conv = max(worst_conv, rel(Up.T @ Gp @ Up, U[0].T @ Gi[0] @ U[0]))
    record("C5e defect = half the remark's penalty with the frame-image metric", worst_c, 1e-11)
    record("C5f frame image transforms by G -> R^-T G R^-1", worst_law, 1e-12)
    record("C5g G_i = rho(T_ij)^-T G_j rho(T_ij)^-1", worst_vert, 1e-12)
    record("C5h rho(U)^T G_i0 rho(U) is passive invariant", worst_conv, 1e-12)


# ----------------------------------------------------------------------------------------------
def check_c6_wilson() -> None:
    print("\n== C6 prop:link-loop-defect (d) ==")
    rng = RNG
    n = 4
    worst = worst_g = worst_iso = 0.0
    lo, hi = np.inf, -np.inf
    for _ in range(100):
        o, _ = np.linalg.qr(rng.standard_normal((n, n)))
        worst = max(worst, abs(defect(o, np.eye(n)) - (n - np.trace(o))))
        G = spd(n, rng, 1.2)
        Gh = np.real(sqrtm(G))
        og = np.linalg.solve(Gh, o @ Gh)
        worst_iso = max(worst_iso, rel(og.T @ G @ og, G))
        q = defect(og, G)
        worst_g = max(worst_g, abs(q - (n - np.trace(og))))
        lo, hi = min(lo, q), max(hi, q)
    record("C6a defect(O) = n - Tr O on O(4), G = I", worst, 1e-12)
    record("C6b G^{-1/2} O G^{1/2} is a G-isometry", worst_iso, 1e-11)
    record("C6c defect = n - Tr on G-isometries, random G", worst_g, 1e-10)
    record("C6d 0 <= defect <= 2n on isometries", max(-lo, hi - 2 * n), 0.0, ok=(lo >= -1e-12 and hi <= 2 * n))
    worst_rot = 0.0
    for _ in range(50):
        ax = rng.standard_normal(3)
        ax /= np.linalg.norm(ax)
        phi = rng.uniform(0, math.pi)
        Kx = np.array([[0, -ax[2], ax[1]], [ax[2], 0, -ax[0]], [-ax[1], ax[0], 0]])
        R = expm(phi * Kx)
        worst_rot = max(worst_rot, abs(defect(R, np.eye(3)) - 4 * math.sin(phi / 2) ** 2))
    record("C6e SO(3) rotation by phi: defect = 4 sin^2(phi/2)", worst_rot, 1e-12)


# ----------------------------------------------------------------------------------------------
def check_c7_reference_change() -> None:
    print("\n== C7 prop:link-loop-defect (b), lem:link-trace-form-scale ==")
    rng = RNG
    K = 3
    G = spd(K, rng, 1.0)
    Gh = np.real(sqrtm(G))
    worst_tr = worst_id = worst_conf = 0.0
    min_change = np.inf
    for _ in range(50):
        w = [0.6 * rng.standard_normal((K, K)) for _ in range(3)]
        W = prod_exp(w)
        q0 = defect(W, G)
        g0 = glplus(K, rng, 0.6)
        wr = [np.linalg.inv(g0) @ x @ g0 for x in w]
        Wr = prod_exp(wr)
        worst_tr = max(worst_tr, abs(defect(Wr, g0.T @ G @ g0) - q0) / max(1, q0))
        qfix = defect(Wr, G)
        worst_id = max(worst_id, abs(qfix - defect(W, np.linalg.inv(g0).T @ G @ np.linalg.inv(g0))) / max(1, q0))
        min_change = min(min_change, abs(qfix - q0) / max(1, q0))
        # conformal isometry c * O_G with O_G = G^{-1/2} O G^{1/2}
        o, _ = np.linalg.qr(rng.standard_normal((K, K)))
        c = math.exp(rng.uniform(-1, 1)) * (1 if rng.uniform() < 0.5 else -1)
        R = c * np.linalg.solve(Gh, o @ Gh)
        wc = [np.linalg.inv(R) @ x @ R for x in w]
        worst_conf = max(worst_conf, abs(defect(prod_exp(wc), G) - q0) / max(1, q0))
    record("C7a transported metric R^T G R: defect unchanged", worst_tr, 1e-10)
    record("C7b fixed metric at sigma' = defect at sigma with R^-T G R^-1", worst_id, 1e-10)
    record("C7c fixed metric, nonzero multiple of a G-isometry: defect unchanged", worst_conf, 1e-10)
    record("C7d fixed metric, generic g0: defect changes (min relative change, should be > 0)",
           min_change, 0.0, ok=min_change > 1e-6)
    # rank-one lemma
    G1 = spd(K, rng)
    G2s = 2.5 * G1
    G2r = spd(K, rng)
    worst_scale = max_diff = worst_formula = 0.0
    for _ in range(100):
        b = rng.standard_normal(K)
        cc = rng.standard_normal(K)
        H = np.outer(b, cc)
        worst_formula = max(worst_formula, abs(gnorm2(H, G1) - (b @ G1 @ b) * (cc @ np.linalg.solve(G1, cc))))
        worst_scale = max(worst_scale, abs(gnorm2(H, G2s) - gnorm2(H, G1)) / gnorm2(H, G1))
        max_diff = max(max_diff, abs(gnorm2(H, G2r) - gnorm2(H, G1)) / gnorm2(H, G1))
    record("C7e ||b c^T||_G^2 = (b^T G b)(c^T G^-1 c)", worst_formula, 1e-11)
    record("C7f positive multiple of G: rank-one norms agree", worst_scale, 1e-12)
    record("C7g non-proportional G': rank-one norms differ (max rel diff > 0)", max_diff, 0.0, ok=max_diff > 1e-3)
    # converse, second order: (Qfix - Q0)/t^2 -> q_{Gt}(H) - q_G(H)
    g0 = glplus(K, rng, 0.6)
    Gt = np.linalg.inv(g0).T @ G @ np.linalg.inv(g0)
    A = rng.standard_normal((K, K))
    target = 0.5 * (gnorm2(A, Gt) - gnorm2(A, G))
    errs = []
    for t in [1e-2, 1e-3, 1e-4]:
        W = expm(t * A)  # once-traversed pair carries tA, all other generators zero
        Wr = np.linalg.inv(g0) @ W @ g0
        errs.append(abs((defect(Wr, G) - defect(W, G)) / t**2 - target) / abs(target))
    record("C7h second-order limit of the defect change (rel err at t=1e-4)", errs[-1], 1e-3)
    # rotated walk
    w = [0.6 * rng.standard_normal((K, K)) for _ in range(3)]
    W = prod_exp(w)
    Wrot = prod_exp([w[1], w[2], w[0]])
    R0 = expm(w[0])
    lhs = defect(Wrot, G)
    rhs = defect(W, np.linalg.inv(R0).T @ G @ np.linalg.inv(R0))
    record("C7i rotated walk: defect = defect of p with rho(twist)^-T G rho(twist)^-1", abs(lhs - rhs) / max(1, lhs),
           1e-11)
    record("C7j rotated walk changes the defect for a non-isometric twist (rel change > 0)",
           abs(lhs - defect(W, G)) / max(1, lhs), 0.0, ok=abs(lhs - defect(W, G)) > 1e-6)
    # pulled-back inner product: <Ad_{g0^-1}A, Ad_{g0^-1}B>_{R^T G R} = <A,B>_G
    A1, A2 = rng.standard_normal((K, K)), rng.standard_normal((K, K))
    lhs = ginner(np.linalg.inv(g0) @ A1 @ g0, np.linalg.inv(g0) @ A2 @ g0, g0.T @ G @ g0)
    record("C7k Ad_{g0^-1} is an isometry from <,>_G to <,>_{R^T G R}", abs(lhs - ginner(A1, A2, G)) /
           max(1, abs(lhs)), 1e-11)
    # Ad_{g0} isometry of <,>_G on gl(K)  <=>  conformal isometry
    o, _ = np.linalg.qr(rng.standard_normal((K, K)))
    R = 1.7 * np.linalg.solve(Gh, o @ Gh)
    dev_conf = max(abs(gnorm2(R @ X @ np.linalg.inv(R), G) - gnorm2(X, G)) / gnorm2(X, G)
                   for X in (rng.standard_normal((K, K)) for _ in range(50)))
    dev_gen = max(abs(gnorm2(g0 @ X @ np.linalg.inv(g0), G) - gnorm2(X, G)) / gnorm2(X, G)
                  for X in (rng.standard_normal((K, K)) for _ in range(50)))
    record("C7l Ad of a conformal G-isometry preserves ||.||_G", dev_conf, 1e-11)
    record("C7m Ad of a generic g0 does not preserve ||.||_G (max rel dev > 0)", dev_gen, 0.0, ok=dev_gen > 1e-3)


# ----------------------------------------------------------------------------------------------
def check_c8_expansion() -> None:
    print("\n== C8 prop:link-loop-defect (e) ==")
    rng = RNG
    K = 3
    G = spd(K, rng, 1.0)
    w = [rng.standard_normal((K, K)) for _ in range(3)]
    ts = [0.3, 0.1, 0.03, 0.01, 0.003, 0.001]
    rems = []
    for t in ts:
        hs = [t * x for x in w]
        q = defect(prod_exp(hs), G)
        lead = 0.5 * gnorm2(sum(hs), G)
        rems.append(abs(q - lead))
    slope = np.polyfit(np.log(ts[2:]), np.log(rems[2:]), 1)[0]
    record("C8a remainder order (log-log slope, should be 3)", abs(slope - 3.0), 0.05)
    # bound on many random families with varsigma <= 1 and beyond
    max_ratio = 0.0
    viol = 0
    for _ in range(4000):
        Gr = spd(K, rng, 1.5)
        r = int(rng.integers(2, 6))
        hs = [rng.standard_normal((K, K)) for _ in range(r)]
        # adversarial ingredient: pairs with large commutators
        if rng.uniform() < 0.3:
            hs = [hs[0], hs[1], -hs[0], -hs[1]][:r] + hs[4:]
        norms = [math.sqrt(gnorm2(h, Gr)) for h in hs]
        target = rng.uniform(0.05, 3.0)
        scale = target / sum(norms)
        hs = [scale * h for h in hs]
        vs = target
        q = defect(prod_exp(hs), Gr)
        lead = 0.5 * gnorm2(sum(hs), Gr)
        R = abs(q - lead)
        ee = math.exp(vs) - 1 - vs
        if R > vs * ee + 0.5 * ee**2 + 1e-12:
            viol += 1
        if vs <= 1.0:
            max_ratio = max(max_ratio, R / vs**3)
    record("C8b general bound s(e^s-1-s)+(e^s-1-s)^2/2 violations", viol, 0.0)
    record(f"C8c max |R|/s^3 on s<=1 vs constant e/2+e^2/8={E_CONST:.4f}", max_ratio, E_CONST)


# ----------------------------------------------------------------------------------------------
def expm2(a: np.ndarray) -> np.ndarray:
    r"""Closed-form exponential of a batch of real 2x2 matrices, shape (...,2,2)."""
    tau = 0.5 * (a[..., 0, 0] + a[..., 1, 1])
    a0 = a.copy()
    a0[..., 0, 0] -= tau
    a0[..., 1, 1] -= tau
    d2 = a0[..., 0, 0] ** 2 + a0[..., 0, 1] * a0[..., 1, 0]  # delta^2 = -det(A0)
    pos = d2 >= 0
    rt = np.sqrt(np.abs(d2))
    with np.errstate(invalid="ignore", divide="ignore"):
        ch = np.where(pos, np.cosh(rt), np.cos(rt))
        sh = np.where(rt > 1e-8, np.where(pos, np.sinh(rt), np.sin(rt)) / np.where(rt > 1e-8, rt, 1.0),
                      1.0 + np.where(pos, 1.0, -1.0) * rt**2 / 6.0)
    out = sh[..., None, None] * a0
    out[..., 0, 0] += ch
    out[..., 1, 1] += ch
    return np.exp(tau)[..., None, None] * out


def check_c9_normalizer() -> None:
    print("\n== C9 prop:link-generator-prior (a): normalizer bounds by Monte Carlo ==")
    rng = RNG
    test = 0.9 * rng.standard_normal((50, 2, 2))
    err = max(rel(expm2(test[k]), expm(test[k])) for k in range(50))
    record("C9a closed-form 2x2 exponential agrees with scipy expm", err, 1e-12)
    n_samp = 200_000
    for s in [0.5, 1.0]:
        for c in [1.0, 5.0]:
            w = s * rng.standard_normal((n_samp, 3, 2, 2))  # base law N(0, s^2 I) on gl(2), Frobenius
            ex = expm2(w)
            P = ex[:, 0] @ ex[:, 1] @ ex[:, 2]
            D = np.eye(2) - P
            Q = 0.5 * np.einsum("nij,nij->n", D, D)
            S = c * Q
            Zhat = float(np.mean(np.exp(-S)))
            Zse = float(np.std(np.exp(-S)) / math.sqrt(n_samp))
            ES = float(np.mean(S))
            ESse = float(np.std(S) / math.sqrt(n_samp))
            lower = math.exp(-ES)
            ok = (lower <= Zhat + 4 * Zse) and (Zhat <= 1.0) and (Zhat > 0)
            print(f"   s={s}, c={c}: Z_hat={Zhat:.5f} (se {Zse:.1e}), E[S]={ES:.4f} (se {ESse:.1e}), "
                  f"exp(-E[S])={lower:.5f}")
            record(f"C9b exp(-E S) <= Z <= 1, s={s}, c={c} (margin Z-exp(-ES))", Zhat - lower, 0.0, ok=ok)
            # moment bound used in the proof: Q <= 2 n^r e^{2 varsigma}
            vs = np.sqrt(np.einsum("nkij,nkij->nk", w, w)).sum(axis=1)
            viol = int(np.sum(Q > 2 * 2**3 * np.exp(2 * vs)))
            record(f"C9c Q <= 2 n^r e^(2 varsigma) violations, s={s}, c={c}", viol, 0.0)
    # deterministic invariance of the prior density under Ad of a rotation (anchor 0, isotropic covariance)
    th = 0.83
    O = np.array([[math.cos(th), -math.sin(th)], [math.sin(th), math.cos(th)]])
    worst = 0.0
    s, c = 0.7, 2.0
    for _ in range(50):
        w = s * rng.standard_normal((3, 2, 2))
        wl = np.array([O.T @ x @ O for x in w])
        def logdens(v: np.ndarray) -> float:
            P = expm(v[0]) @ expm(v[1]) @ expm(v[2])
            return float(-np.sum(v * v) / (2 * s * s) - c * defect(P, np.eye(2)))
        worst = max(worst, abs(logdens(w) - logdens(wl)))
    record("C9d prior log-density invariant under Ad of an isometry fixing anchor/covariance", worst, 1e-11)


# ----------------------------------------------------------------------------------------------
def rho_aff(a: np.ndarray) -> np.ndarray:
    d = a.shape[0]
    m = np.eye(d + 1)
    m[:d, d] = a
    return m


def drho_aff(a: np.ndarray) -> np.ndarray:
    d = a.shape[0]
    m = np.zeros((d + 1, d + 1))
    m[:d, d] = a
    return m


def check_c10_translation() -> None:
    print("\n== C10 prop:link-translation-instance (a),(b),(c) ==")
    rng = RNG
    d = 2
    a, b = rng.standard_normal(d), rng.standard_normal(d)
    record("C10a rho(a) rho(b) = rho(a+b)", rel(rho_aff(a) @ rho_aff(b), rho_aff(a + b)), 1e-15)
    record("C10b exp(d rho(a)) = rho(a)", rel(expm(drho_aff(a)), rho_aff(a)), 1e-15)
    k = rng.standard_normal(d)
    record("C10c rho(a)(k,1) = (k+a,1)", rel(rho_aff(a) @ np.append(k, 1.0), np.append(k + a, 1.0)), 1e-15)
    # four-cycle e_i : i -> i+1 ; walk (e3,e2,e1,e0) based at 0 ; frames U_i in R^d
    U = rng.standard_normal((4, d))
    om = rng.standard_normal((4, d))
    edges = [(i, (i + 1) % 4) for i in range(4)]  # (source j, target i)
    ring = np.array([om[e] - U[t] + U[s] for e, (s, t) in enumerate(edges)])
    walk = [3, 2, 1, 0]
    # check walk convention e_a : i_{a+1} -> i_a with i_0 = 0
    verts = [0]
    for e in walk:
        s, t = edges[e]
        assert t == verts[-1]
        verts.append(s)
    assert verts[-1] == 0
    W = np.eye(d + 1)
    for e in walk:
        W = W @ rho_aff(ring[e])
    h = ring[walk].sum(axis=0)
    record("C10d reference holonomy = rho(loop sum)", rel(W, rho_aff(h)), 1e-14)
    record("C10e loop sum of twist generators = loop sum of link translations (frames telescope)",
           rel(h, om.sum(axis=0)), 1e-14)
    worst = worst_pull = 0.0
    for _ in range(50):
        G = spd(d + 1, rng, 1.2)
        gam = np.linalg.inv(G)[d, d]
        q = defect(W, G)
        worst = max(worst, abs(q - 0.5 * gam * h @ G[:d, :d] @ h) / max(1, q))
        worst_pull = max(worst_pull, abs(q - 0.5 * gnorm2(drho_aff(h), G)) / max(1, q))
    record("C10f defect = (1/2) gamma h^T G11 h (exact, no remainder)", worst, 1e-12)
    record("C10g defect = (1/2) ||d rho(C w)||_G^2 exactly", worst_pull, 1e-12)
    record("C10h G = I: defect = |h|^2/2", abs(defect(W, np.eye(d + 1)) - 0.5 * h @ h), 1e-14)
    anchors = np.array([U[s] - U[t] for (s, t) in edges])  # alpha_e = U_j - U_i for e: j -> i
    record("C10i coboundary anchors have zero loop sum", float(np.linalg.norm(anchors[walk].sum(axis=0))), 1e-14)
    kbar = rng.standard_normal(4)
    om1 = rng.standard_normal(4)
    rb = np.array([kbar[(i + 1) % 4] - kbar[i] - om1[i] for i in range(4)])
    record("C10j four-cycle: sum of residuals = - loop sum", abs(rb.sum() + om1.sum()), 1e-14)


# ----------------------------------------------------------------------------------------------
def check_c11_triangle_chain() -> None:
    print("\n== C11 prop:link-translation-instance (d): c13 triangle chain, N_tri = 2 ==")
    rng = RNG
    Ntri, N = 2, 6
    J1, J2, theta, Temp, sig2, kappa = 2.0, 1.0, 1.5, 0.1, 0.5, 0.5
    assert Temp <= J1 * (1 - sig2) / 2
    edges = [(0, 1), (1, 2), (2, 0), (3, 4), (4, 5), (5, 3), (2, 3)]  # (source j, target i)
    level = [1, 1, 1, 1, 1, 1, 2]
    tris = [[0, 1, 2], [3, 4, 5]]
    nE = len(edges)
    dim = 2 * N + nE
    assert dim == 10 * Ntri - 1

    def kb(i: int) -> int:
        return i

    def mb(i: int) -> int:
        return N + i

    def om(e: int) -> int:
        return 2 * N + e

    def r_row(e: int) -> np.ndarray:
        s, t = edges[e]
        row = np.zeros(dim)
        row[kb(t)] += 1.0
        row[kb(s)] -= 1.0
        row[om(e)] -= 1.0
        return row

    Otri = np.array([[1 / math.sqrt(2), -1 / math.sqrt(2), 0.0],
                     [1 / math.sqrt(6), 1 / math.sqrt(6), -2 / math.sqrt(6)]])
    disc = np.zeros((N, dim))
    for i in range(N):
        disc[i, kb(i)] = 1.0
        disc[i, mb(i)] = -1.0
    contr = np.vstack([Otri @ np.vstack([r_row(e) for e in q]) for q in tris])
    B1 = np.vstack([disc, contr])
    B2 = np.vstack([r_row(6)])
    B = np.vstack([B1, B2])
    Jdiag = np.array([J1] * B1.shape[0] + [J2] * B2.shape[0])
    loops = np.zeros((Ntri, dim))
    for qi, q in enumerate(tris):
        for e in q:
            loops[qi, om(e)] = 1 / math.sqrt(3)
    PH = loops.T @ loops
    H = B.T @ np.diag(Jdiag) @ B + J1 * PH
    inc = np.zeros((nE, N))
    for e, (s, t) in enumerate(edges):
        inc[e, t] += 1.0
        inc[e, s] -= 1.0
    V = np.vstack([np.eye(N), np.eye(N), inc])
    PK = V @ np.linalg.solve(V.T @ V, V.T)
    Dfrak = disc
    Rev = Dfrak.T @ Dfrak / (1 - sig2)
    Omega0 = theta * H + PK - Temp * Rev
    Mtheta = theta * B.T @ np.diag(Jdiag) @ B + PK - Temp * Rev
    record("C11a rank B = 6 N_tri - 1", abs(np.linalg.matrix_rank(B) - (6 * Ntri - 1)), 0.0)
    record("C11b loop covectors orthogonal to rows of B and to the gauge carrier",
           float(np.abs(B @ loops.T).max() + np.abs(V.T @ loops.T).max()), 1e-14)
    worst_q = worst_loop = worst_sum = 0.0
    for _ in range(20):
        x = rng.standard_normal(dim)
        r = np.array([r_row(e) @ x for e in range(nE)])
        dvals = disc @ x
        lhs = x @ H @ x
        rhs = J1 * np.sum(dvals**2) + sum((J1 if level[e] == 1 else J2) * r[e] ** 2 for e in range(nE))
        worst_q = max(worst_q, abs(lhs - rhs) / max(1, abs(lhs)))
        for qi, q in enumerate(tris):
            hq = loops[qi] @ x
            frak_h = sum(x[om(e)] for e in q)
            worst_loop = max(worst_loop, abs(np.sum(r[q] ** 2) - (np.sum((Otri @ r[q]) ** 2) + hq**2)))
            worst_sum = max(worst_sum, abs(np.sum(r[q]) + frak_h) + abs(hq - frak_h / math.sqrt(3)))
    record("C11c x^T H x = J1 sum d_i^2 + sum J_l r_e^2", worst_q, 1e-12)
    record("C11d |r_q|^2 = |O r_q|^2 + h_q^2", worst_loop, 1e-12)
    record("C11e sum r_e = -frak_h_q and h_q = frak_h_q/sqrt3", worst_sum, 1e-12)
    record("C11f Omega_0 positive definite (min eigenvalue)", float(np.linalg.eigvalsh(Omega0).min()), 0.0,
           ok=np.linalg.eigvalsh(Omega0).min() > 0)
    record("C11g Omega_0 loop covectors are eigenvectors with eigenvalue theta J1",
           float(np.abs(Omega0 @ loops.T - theta * J1 * loops.T).max()), 1e-12)
    ns = null_space(Mtheta, rcond=1e-10)
    span_err = float(np.linalg.norm(ns - loops.T @ (loops @ ns)))
    record("C11h ker M_theta = loop space (dim 2 and span)", abs(ns.shape[1] - Ntri) + span_err, 1e-10)
    worst_id = 0.0
    for _ in range(20):
        x = rng.standard_normal(dim)
        Qs = [0.5 * sum(x[om(e)] for e in q) ** 2 for q in tris]
        lhs = x @ Omega0 @ x / (2 * Temp)
        rhs = sum(theta * J1 / (3 * Temp) * Q for Q in Qs) + x @ Mtheta @ x / (2 * Temp)
        worst_id = max(worst_id, abs(lhs - rhs) / max(1, abs(lhs)))
    record("C11i prior exponent = sum (theta J1/(3T)) Q_q + x^T M x/(2T)", worst_id, 1e-12)
    Cov = Temp * np.linalg.inv(Omega0)
    frak = math.sqrt(3) * loops  # frak_h_q = sqrt3 * loop covector . x
    covh = frak @ Cov @ frak.T
    record("C11j Var(frak_h_q) = 3T/(theta J1), Cov between triangles = 0",
           float(np.abs(covh - 3 * Temp / (theta * J1) * np.eye(Ntri)).max()), 1e-12)
    Pperp = np.eye(dim) - PH
    record("C11k loop sums independent of the projection onto U+K",
           float(np.abs(frak @ Cov @ Pperp).max()), 1e-12)
    Khat = theta * H + (1 + kappa) * PK
    record("C11l quadratic energy E_theta has the same loop block theta J1",
           float(np.abs(Khat @ loops.T - theta * J1 * loops.T).max()), 1e-12)
    record("C11m T R_ev <= H/2 (min eigenvalue of H/2 - T R_ev)", float(np.linalg.eigvalsh(H / 2 - Temp * Rev).min()),
           0.0, ok=np.linalg.eigvalsh(H / 2 - Temp * Rev).min() > -1e-12)


# ----------------------------------------------------------------------------------------------
def check_c12_running_example() -> None:
    print("\n== C12 rem:link-running-example ==")
    Lx = E(3, 3, 2) - E(3, 2, 3)
    Lz = E(3, 2, 1) - E(3, 1, 2)
    Rz = expm(math.pi / 2 * Lz)
    Rx = expm(math.pi / 2 * Lx)
    record("C12a R_z(pi/2) = [[0,-1,0],[1,0,0],[0,0,1]]",
           rel(Rz, np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1.0]])), 1e-15)
    W = Rz @ Rx
    perm = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0.0]])
    record("C12b reference holonomy = cyclic permutation matrix", rel(W, perm), 1e-15)
    record("C12c Tr W = 0", abs(np.trace(W)), 1e-15)
    record("C12d rotation angle 2pi/3", abs(math.acos((np.trace(W) - 1) / 2) - 2 * math.pi / 3), 1e-12)
    record("C12e defect = 3", abs(defect(W, np.eye(3)) - 3.0), 1e-14)
    lead = 0.5 * gnorm2(math.pi / 2 * (Lz + Lx), np.eye(3))
    record("C12f quadratic term = pi^2/2", abs(lead - math.pi**2 / 2), 1e-13)
    vs = 2 * math.sqrt(gnorm2(math.pi / 2 * Lz, np.eye(3)))
    record("C12g varsigma = pi sqrt2 (> 1)", abs(vs - math.pi * math.sqrt(2)), 1e-13)
    record("C12h principal logarithm of R_z(pi/2) is (pi/2) L_z", rel(np.real(logm(Rz)), math.pi / 2 * Lz), 1e-12)
    # passive re-expression at agent 2 (index 1) changes links, not twists or holonomy
    rng = RNG
    ax = rng.standard_normal(3)
    ax /= np.linalg.norm(ax)
    Kx = np.array([[0, -ax[2], ax[1]], [ax[2], 0, -ax[0]], [-ax[1], ax[0], 0]])
    g2 = expm(1.1 * Kx)
    links = [Rz, Rx, np.eye(3)]
    new = [links[0] @ g2.T, g2 @ links[1], links[2]]  # Theta_e1 g2^-1, g2 Theta_e2
    U2 = g2
    twists = [np.eye(3).T @ new[0] @ U2, U2.T @ new[1] @ np.eye(3), new[2]]  # U_i^-1 Theta U_j with U = (I,g2,I)
    record("C12i passive g_2: twists unchanged", max(rel(twists[k], links[k]) for k in range(3)), 1e-14)
    record("C12j passive g_2: holonomy at agent 1 unchanged", rel(new[0] @ new[1] @ new[2], W), 1e-14)


def main() -> None:
    np.set_printoptions(precision=4, suppress=True)
    print("checks_A.py: float64 validation for fragment A; numpy", np.__version__)
    check_c1_exp_naturality()
    check_c2_generator_gauge()
    check_c3_chart_image()
    check_c4_blindness()
    check_c5_zero_set_frame_image()
    check_c6_wilson()
    check_c7_reference_change()
    check_c8_expansion()
    check_c9_normalizer()
    check_c10_translation()
    check_c11_triangle_chain()
    check_c12_running_example()
    n_fail = sum(1 for r in RESULTS if not r[3])
    print(f"\nSUMMARY: {len(RESULTS) - n_fail} passed, {n_fail} failed, {len(RESULTS)} checks")


if __name__ == "__main__":
    main()
