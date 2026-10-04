r"""Float64 validation checks for the Gaussian latent-link chapter (frag_D_suppG.tex)
and the coarse-graining statements (frag_D_main.tex).

Validation only: every check grounds an identity, a gradient, an expansion, or a
sampling prediction at small size.  Nothing here is a manuscript claim.

Run:  C:/anaconda/python.exe checks_D.py  > checks_D_output.txt
"""
from __future__ import annotations

import itertools
import os

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import numpy as np
from scipy.linalg import expm, logm

np.set_printoptions(precision=6, suppress=False, linewidth=120)
RNG = np.random.default_rng(20261003)


# ----------------------------------------------------------------------------- helpers
def spd(K: int, rng: np.random.Generator, scale: float = 1.0, floor: float = 0.3) -> np.ndarray:
    """Random symmetric positive-definite matrix."""
    M = rng.normal(size=(K, K))
    return scale * (M @ M.T / K + floor * np.eye(K))


def frechet(X: np.ndarray, E: np.ndarray) -> np.ndarray:
    r"""L(X,E)=\int_0^1 e^{sX}Ee^{(1-s)X}ds via the block-triangular exponential."""
    K = X.shape[0]
    B = np.zeros((2 * K, 2 * K))
    B[:K, :K] = X
    B[K:, K:] = X
    B[:K, K:] = E
    return expm(B)[:K, K:]


def frechet2(X: np.ndarray, Y: np.ndarray) -> np.ndarray:
    r"""L^{(2)}(X;Y,Y)=d^2/dt^2 e^{X+tY}|_{t=0} via the 3x3 block exponential."""
    K = X.shape[0]
    B = np.zeros((3 * K, 3 * K))
    for a in range(3):
        B[a * K:(a + 1) * K, a * K:(a + 1) * K] = X
    B[:K, K:2 * K] = Y
    B[K:2 * K, 2 * K:] = Y
    return 2.0 * expm(B)[:K, 2 * K:]


def gauss_kl(m1, S1, m2, S2) -> float:
    r"""KL(N(m1,S1)||N(m2,S2))."""
    K = len(m1)
    S2i = np.linalg.inv(S2)
    d = m2 - m1
    return 0.5 * (np.trace(S2i @ S1) + d @ S2i @ d - K
                  + np.linalg.slogdet(S2)[1] - np.linalg.slogdet(S1)[1])


def gip(A: np.ndarray, B: np.ndarray, G: np.ndarray) -> float:
    r"""<A,B>_G = Tr(G^{-1} A^T G B)."""
    return float(np.trace(np.linalg.solve(G, A.T @ G @ B)))


def report(name: str, value: float, tol: float | None = None) -> None:
    if tol is None:
        print(f"  {name}: {value:.3e}")
    else:
        flag = "PASS" if value <= tol else "FAIL"
        print(f"  {name}: {value:.3e}  (tol {tol:.0e})  {flag}")


# vectorized 2x2 exponential and principal logarithm ------------------------------
def expm2(X: np.ndarray) -> np.ndarray:
    r"""Batched exp of 2x2 real matrices: e^X=e^\tau(c I + s N), N=X-\tau I, N^2=\delta I."""
    tau = 0.5 * (X[..., 0, 0] + X[..., 1, 1])
    N = X.copy()
    N[..., 0, 0] -= tau
    N[..., 1, 1] -= tau
    delta = N[..., 0, 0] ** 2 + N[..., 0, 1] * N[..., 1, 0]
    r = np.sqrt(np.abs(delta))
    pos = delta > 0
    c = np.where(pos, np.cosh(r), np.cos(r))
    with np.errstate(invalid="ignore", divide="ignore"):
        s = np.where(r > 1e-12, np.where(pos, np.sinh(r), np.sin(r)) / np.where(r > 1e-12, r, 1.0),
                     1.0 + delta / 6.0)
    out = s[..., None, None] * N
    out[..., 0, 0] += c
    out[..., 1, 1] += c
    return np.exp(tau)[..., None, None] * out


def logm2(M: np.ndarray):
    r"""Batched principal log of 2x2 real matrices; returns (Log, exists_mask).
    exists iff no eigenvalue in (-inf,0]."""
    m = 0.5 * (M[..., 0, 0] + M[..., 1, 1])
    N = M.copy()
    N[..., 0, 0] -= m
    N[..., 1, 1] -= m
    delta = N[..., 0, 0] ** 2 + N[..., 0, 1] * N[..., 1, 0]
    det = M[..., 0, 0] * M[..., 1, 1] - M[..., 0, 1] * M[..., 1, 0]
    r = np.sqrt(np.abs(delta))
    exists = np.where(delta >= 0, m - r > 0, det > 0)
    with np.errstate(invalid="ignore", divide="ignore"):
        # complex pair: log = log(sqrt det) I + (theta/r) N, theta = atan2(r, m)
        theta = np.arctan2(r, m)
        coef_c = np.where(r > 1e-14, theta / np.where(r > 1e-14, r, 1.0), 1.0 / m)
        # real distinct positive: log = 0.5 log det I + (artanh(r/m)/r) N
        coef_r = np.where(r > 1e-14, np.arctanh(np.clip(r / m, -1 + 1e-16, 1 - 1e-16)) / np.where(r > 1e-14, r, 1.0),
                          1.0 / m)
    coef = np.where(delta < 0, coef_c, coef_r)
    alpha = 0.5 * np.log(np.where(det > 0, det, 1.0))
    L = coef[..., None, None] * N
    L[..., 0, 0] += alpha
    L[..., 1, 1] += alpha
    return L, exists


def batch_stats(x: np.ndarray, nb: int = 40):
    """Batch-means estimate and standard error of a statistic computed per batch."""
    return x.mean(), x.std(ddof=1) / np.sqrt(len(x))


def cum3(x: np.ndarray) -> float:
    xc = x - x.mean()
    return float(np.mean(xc ** 3))


def cum4(x: np.ndarray) -> float:
    xc = x - x.mean()
    m2 = np.mean(xc ** 2)
    return float(np.mean(xc ** 4) - 3 * m2 ** 2)


def batched_cumulant(x: np.ndarray, f, nb: int = 50):
    xs = np.array_split(x, nb)
    vals = np.array([f(b) for b in xs])
    return vals.mean(), vals.std(ddof=1) / np.sqrt(nb)


# ============================================================================ CHECK 1
def check_law_level_energy() -> None:
    print("\n[1] prop:glink-law-level-energy: closed form, log-volume term, gradient, reductions")
    rng = np.random.default_rng(1)
    K = 3
    mu_i, mu_j = rng.normal(size=K), rng.normal(size=K)
    S_i, S_j = spd(K, rng), spd(K, rng)
    om = 0.7 * rng.normal(size=(K, K))
    R = expm(om)
    direct = gauss_kl(mu_i, S_i, R @ mu_j, R @ S_j @ R.T)
    V = expm(-om)
    Sji = np.linalg.inv(S_j)
    r = V @ mu_i - mu_j
    closed = 0.5 * (np.trace(Sji @ V @ S_i @ V.T) + r @ Sji @ r - K
                    + np.linalg.slogdet(S_j)[1] - np.linalg.slogdet(S_i)[1]) + np.trace(om)
    report("|KL direct - closed form| / KL", abs(direct - closed) / abs(direct), 1e-12)
    report("|log det e^om - Tr om|", abs(np.linalg.slogdet(R)[1] - np.trace(om)), 1e-12)

    def D(w):
        Rw = expm(w)
        return gauss_kl(mu_i, S_i, Rw @ mu_j, Rw @ S_j @ Rw.T)

    Nmat = Sji @ (V @ (S_i + np.outer(mu_i, mu_i)) - np.outer(mu_j, mu_i))
    grad = np.eye(K) - frechet(-om.T, Nmat)
    h = 1e-6
    fd = np.zeros((K, K))
    for a in range(K):
        for b in range(K):
            E = np.zeros((K, K))
            E[a, b] = h
            fd[a, b] = (D(om + E) - D(om - E)) / (2 * h)
    report("max |grad formula - central FD| / max|grad|", np.abs(grad - fd).max() / np.abs(grad).max(), 1e-7)

    # passive invariance: local coordinates with frames U_i, U_j
    U_i, U_j = rng.normal(size=(K, K)) + 2 * np.eye(K), rng.normal(size=(K, K)) + 2 * np.eye(K)
    Theta = U_i @ R @ np.linalg.inv(U_j)
    local = gauss_kl(U_i @ mu_i, U_i @ S_i @ U_i.T, Theta @ (U_j @ mu_j), Theta @ (U_j @ S_j @ U_j.T) @ Theta.T)
    report("|KL local frames - KL reference coords|", abs(local - direct), 1e-10)

    # reduction (b): covariance-matched twist -> twisted pair energy with W = Sigma_i^{-1}
    S_i_b = R @ S_j @ R.T
    kb = gauss_kl(mu_i, S_i_b, R @ mu_j, R @ S_j @ R.T)
    d = mu_i - R @ mu_j
    report("covariance-matched reduction |KL - 1/2 d^T S_i^{-1} d|", abs(kb - 0.5 * d @ np.linalg.solve(S_i_b, d)), 1e-11)

    # reduction (c): orbit Fisher form
    ups = rng.normal(size=(K, K))
    mu, S = mu_i, S_i
    Si = np.linalg.inv(S)
    kq = (ups @ mu) @ Si @ (ups @ mu) + np.trace(ups @ ups) + np.trace(Si @ ups @ S @ ups.T)
    for t in [1e-2, 1e-3, 1e-4]:
        Rt = expm(t * ups)
        val = gauss_kl(mu, S, Rt @ mu, Rt @ S @ Rt.T) / t ** 2
        print(f"  orbit Fisher: t={t:.0e}  KL/t^2 = {val:.8f}   k_q/2 = {0.5 * kq:.8f}   rel.err {abs(val - 0.5 * kq) / (0.5 * kq):.2e}")


# ============================================================================ CHECK 2
def check_sample_record() -> None:
    print("\n[2] prop:glink-sample-record: expected record energy, current, rank-one minimizer, saddle")
    rng = np.random.default_rng(2)
    K = 3
    mu_i, mu_j, o = rng.normal(size=K), rng.normal(size=K), 0.3 * rng.normal(size=K)
    S_i, S_j, W = spd(K, rng), spd(K, rng), spd(K, rng)
    om = 0.6 * rng.normal(size=(K, K))
    R = expm(om)
    const = 0.5 * np.linalg.slogdet(2 * np.pi * np.linalg.inv(W))[1]

    def E_closed(Rm):
        res = o - mu_i + Rm @ mu_j
        return 0.5 * res @ W @ res + 0.5 * np.trace(W @ S_i) + 0.5 * np.trace(W @ Rm @ S_j @ Rm.T) + const

    for rep in range(3):
        n = 4_000_000
        zi = mu_i + rng.normal(size=(n, K)) @ np.linalg.cholesky(S_i).T
        zj = mu_j + rng.normal(size=(n, K)) @ np.linalg.cholesky(S_j).T
        res = o - zi + zj @ R.T
        samp = 0.5 * np.einsum("na,ab,nb->n", res, W, res) + const
        mc, se = samp.mean(), samp.std(ddof=1) / np.sqrt(n)
        print(f"  expected energy (rep {rep}): closed {E_closed(R):.6f}  MC {mc:.6f} +- {se:.6f}  z = {(mc - E_closed(R)) / se:+.2f}")

    J = W @ (np.outer(mu_i - o - R @ mu_j, mu_j) - R @ S_j)
    h = 1e-6
    fdR = np.zeros((K, K))
    fdw = np.zeros((K, K))
    for a in range(K):
        for b in range(K):
            E = np.zeros((K, K))
            E[a, b] = h
            fdR[a, b] = (E_closed(R + E) - E_closed(R - E)) / (2 * h)
            fdw[a, b] = (E_closed(expm(om + E)) - E_closed(expm(om - E))) / (2 * h)
    report("max |dE/dT + J| / max|J|", np.abs(fdR + J).max() / np.abs(J).max(), 1e-7)
    report("max |grad_om E + L(om^T,J)| / max", np.abs(fdw + frechet(om.T, J)).max() / np.abs(fdw).max(), 1e-7)
    Ssec = S_j + np.outer(mu_j, mu_j)
    Tstar = np.outer(mu_i - o, mu_j) @ np.linalg.inv(Ssec)
    Jst = W @ (np.outer(mu_i - o - Tstar @ mu_j, mu_j) - Tstar @ S_j)
    sv = np.linalg.svd(Tstar, compute_uv=False)
    report("|J(T_*)| (stationarity)", np.abs(Jst).max(), 1e-12)
    print(f"  singular values of T_*: {sv}  (rank one)")
    trM = mu_j @ np.linalg.solve(S_j, mu_i - o) / (1 + mu_j @ np.linalg.solve(S_j, mu_j))
    report("Tr M* vs mu_j^T S_j^-1 (mu_i-o)/(1+mu_j^T S_j^-1 mu_j)", abs(np.trace(Tstar) - trM), 1e-12)
    # spectrum of L(B,.) = (int_0^1 e^{t ad_B} dt)(.) e^B : eigenvalues int_0^1 e^{t(l_a-l_b)}dt (times e^{l_b})
    for Bm in [rng.normal(size=(3, 3)), np.array([[0.2, -2 * np.pi / 2, 0], [np.pi, 0.2, 0], [0, 0, -0.4]])]:
        Kb = Bm.shape[0]
        Lop = np.zeros((Kb * Kb, Kb * Kb))
        for p_ in range(Kb * Kb):
            Ep = np.zeros(Kb * Kb)
            Ep[p_] = 1.0
            Lop[:, p_] = frechet(Bm, Ep.reshape(Kb, Kb)).reshape(-1)
        Aop = np.kron(np.eye(Kb), np.linalg.inv(expm(Bm)).T) @ Lop  # right-multiply by e^{-B} (row-major vec)
        lam_b = np.linalg.eigvals(Bm)
        dl = (lam_b[:, None] - lam_b[None, :]).reshape(-1)
        pred_ev = np.where(np.abs(dl) > 1e-14, (np.exp(dl) - 1) / np.where(np.abs(dl) > 1e-14, dl, 1), 1.0)
        got = np.linalg.eigvals(Aop)
        err = max(min(abs(g - pv) for g in got) for pv in pred_ev)
        print(f"  eig(int_0^1 e^(t ad_B)dt) vs int_0^1 e^(t(l_a-l_b))dt: max mismatch {err:.1e};"
              f"  min |eig| = {np.abs(got).min():.2e}")

    # case v^T u >= 0: infimum over the chart approached at T_*
    u = mu_i - o
    v = np.linalg.solve(Ssec, mu_j)
    lam = v @ u
    if lam <= 0:  # reflect the receiver mean so that v^T u > 0
        mu_i = o - u
        u = mu_i - o
        lam = v @ u
        Tstar = np.outer(u, mu_j) @ np.linalg.inv(Ssec)
    print(f"  v^T u = {lam:+.4f}")
    if lam > 0:
        # T_* = u v^T is diagonalizable: P diag(lam,0,...) P^{-1}
        evals, P = np.linalg.eig(Tstar)
        idx = np.argsort(-np.abs(evals))
        evals, P = evals[idx].real, P[:, idx].real
        for nn in [2, 5, 10, 20]:
            Xn = P @ np.diag([np.log(lam)] + [-nn] * (K - 1)) @ np.linalg.inv(P)
            print(f"    n={nn:2d}: E(e^X_n) - E(T_*) = {E_closed(expm(Xn)) - E_closed(Tstar):.3e}")

    # saddle at a critical point of exp (K=2)
    s, c = 0.7, 1.3
    K2 = 2
    W2, Sj2, muj2, mui2, o2 = np.eye(2), s * np.eye(2), np.array([1.0, 0.0]), np.array([-c, 0.0]), np.zeros(2)

    def E2(Rm):
        res = o2 - mui2 + Rm @ muj2
        return 0.5 * res @ W2 @ res + 0.5 * np.trace(W2 @ Rm @ Sj2 @ Rm.T)

    rho = c / (1 + 2 * s)
    Jm = np.array([[0.0, -1.0], [1.0, 0.0]])
    om0 = np.log(rho) * np.eye(2) + np.pi * Jm
    R0 = expm(om0)
    J0 = W2 @ (np.outer(mui2 - o2 - R0 @ muj2, muj2) - R0 @ Sj2)
    g0 = -frechet(om0.T, J0)
    report("saddle: |e^om0 + rho I|", np.abs(R0 + rho * np.eye(2)).max(), 1e-12)
    report("saddle: |grad_om E at om0|", np.abs(g0).max(), 1e-12)
    print(f"    |dE/dT at e^om0| = {np.abs(J0).max():.3e} (nonzero: stationary only through the critical point of exp)")
    for t in [3e-2, 1e-2, -1e-2, -3e-2]:
        dlt = t * np.diag([1.0, -1.0])
        dE = E2(expm(om0 + dlt)) - E2(R0)
        pred = s * rho ** 2 * t * t ** 2 / np.pi ** 2
        print(f"    t={t:+.0e}: E(e^(om0+d)) - E(e^om0) = {dE:+.4e}   predicted s rho^2 t^3/pi^2 = {pred:+.4e}")


# ============================================================================ CHECK 3
def check_expected_loop() -> None:
    print("\n[3] prop:glink-expected-loop: product formulas, defect formula, first-order expansion, repeats")
    rng = np.random.default_rng(3)
    K, m = 2, 3
    mus = [0.4 * rng.normal(size=(K, K)) for _ in range(m)]
    Cch = [0.3 * rng.normal(size=(K * K, K * K)) for _ in range(m)]  # covariance square roots
    G = spd(K, rng)
    Gi = np.linalg.inv(G)
    n = 600_000

    def sample(k, nn, rr):
        z = rr.normal(size=(nn, K * K)) @ Cch[k].T
        return mus[k] + z.reshape(nn, K, K)

    # per-edge moments from one sample set, direct product from another
    rr1, rr2 = np.random.default_rng(31), np.random.default_rng(32)
    Mk, MMk = [], []
    for k in range(m):
        Ek = expm2(sample(k, n, rr1))
        Mk.append(Ek.mean(0))
        MMk.append(np.einsum("nac,nbd->abcd", Ek, Ek).reshape(K * K, K * K) / n)
    Mp = Mk[0] @ Mk[1] @ Mk[2]
    MMp = MMk[0] @ MMk[1] @ MMk[2]
    Ws = expm2(sample(0, n, rr2)) @ expm2(sample(1, n, rr2)) @ expm2(sample(2, n, rr2))
    Wmean = Ws.mean(0)
    Wse = Ws.std(0, ddof=1) / np.sqrt(n)
    print("  E[W_p] product of per-edge means vs direct MC (z-scores):")
    print("   ", np.round((Mp - Wmean) / Wse, 2).ravel())
    WW = np.einsum("nac,nbd->nabcd", Ws, Ws).reshape(n, K * K, K * K)
    WWm, WWse = WW.mean(0), WW.std(0, ddof=1) / np.sqrt(n)
    zmax = np.abs((MMp - WWm) / WWse).max()
    print(f"  E[W_p (x) W_p] product vs direct MC: max |z| = {zmax:.2f} over {K**4} entries")
    # loop defect via the index formula
    a = G.reshape(-1)
    b = Gi.reshape(-1)
    EQ_formula = 0.5 * (a @ MMp @ b - 2 * np.trace(Mp) + K)
    Qs = 0.5 * np.array([gip(Wi - np.eye(K), Wi - np.eye(K), G) for Wi in Ws[:200_000]])
    print(f"  E Q_p: formula from moments {EQ_formula:.5f}   direct MC {Qs.mean():.5f} +- {Qs.std(ddof=1)/np.sqrt(len(Qs)):.5f}")
    # index identity Tr(G^{-1}W^T G W) = a^T (W(x)W) b
    Wt = Ws[0]
    report("index identity for <W,W>_G", abs(gip(Wt, Wt, G) - a @ np.kron(Wt, Wt) @ b), 1e-12)

    # first-order expansion, antithetic common random numbers.  The manuscript formula keeps the
    # copy-diagonal second derivatives; the cross terms D_k D_l have zero mean for independent copies.
    ns = 2000
    Z = [rng.normal(size=(ns, K * K)) @ Cch[k].T for k in range(m)]

    def Qfun(oms):
        Wm = np.eye(K)
        for w in oms:
            Wm = Wm @ expm(w)
        D_ = Wm - np.eye(K)
        return 0.5 * gip(D_, D_, G)

    E_mu = [expm(mu) for mu in mus]
    W_mu = E_mu[0] @ E_mu[1] @ E_mu[2]
    full2 = np.zeros(ns)
    diag2 = np.zeros(ns)
    for s_ in range(ns):
        Ys = [Z[k][s_].reshape(K, K) for k in range(m)]
        L1 = [frechet(mus[k], Ys[k]) for k in range(m)]
        L2 = [frechet2(mus[k], Ys[k]) for k in range(m)]
        Wp = np.zeros((K, K))
        Wpp = np.zeros((K, K))
        for k in range(m):
            fac = [E_mu[j] for j in range(m)]
            fac[k] = L1[k]
            Wp += fac[0] @ fac[1] @ fac[2]
            fac2 = [E_mu[j] for j in range(m)]
            fac2[k] = L2[k]
            term = fac2[0] @ fac2[1] @ fac2[2]
            Wpp += term
            Pk = np.eye(K)
            for j in range(k):
                Pk = Pk @ E_mu[j]
            Qk = np.eye(K)
            for j in range(k + 1, m):
                Qk = Qk @ E_mu[j]
            A1 = Pk @ L1[k] @ Qk
            diag2[s_] += gip(A1, A1, G) + gip(W_mu - np.eye(K), term, G)
            for l in range(k + 1, m):
                fac3 = [E_mu[j] for j in range(m)]
                fac3[k] = L1[k]
                fac3[l] = L1[l]
                Wpp += 2 * fac3[0] @ fac3[1] @ fac3[2]
        full2[s_] = gip(Wp, Wp, G) + gip(W_mu - np.eye(K), Wpp, G)
    base = Qfun(mus)
    S2full = 0.5 * full2.mean()
    cross = 0.5 * (full2 - diag2)
    print(f"  cross terms 1/2(D^2 - sum_k D_k^2): sample mean {cross.mean():+.4f} +- {cross.std(ddof=1)/np.sqrt(ns):.4f} (zero mean)")
    print("  Taylor residual with sample second derivative / sigma^4 (antithetic, common draws):")
    for sig in [0.4, 0.2, 0.1, 0.05]:
        tot = 0.0
        for s_ in range(ns):
            Yp = [sig * Z[k][s_].reshape(K, K) for k in range(m)]
            tot += 0.5 * (Qfun([mus[k] + Yp[k] for k in range(m)]) + Qfun([mus[k] - Yp[k] for k in range(m)]))
        tot /= ns
        resid = tot - base - sig ** 2 * S2full
        print(f"    sigma={sig:.2f}: residual = {resid:+.3e},  / sigma^4 = {resid / sig ** 4:+.4f}")
    # flat means: Q = 1/2 ||sum_k Y_k||_G^2 + O(|Y|^3); expectation 1/2 sum_k E||Y_k||_G^2
    print("  flat means (mu=0): antithetic mean of Q / mean of 1/2||sum Y_k||_G^2 as sigma->0:")
    for sig in [0.2, 0.1, 0.05]:
        tot, lead = 0.0, 0.0
        for s_ in range(ns):
            Yp = [sig * Z[k][s_].reshape(K, K) for k in range(m)]
            tot += 0.5 * (Qfun(Yp) + Qfun([-y for y in Yp]))
            ssum = Yp[0] + Yp[1] + Yp[2]
            lead += 0.5 * gip(ssum, ssum, G)
        print(f"    sigma={sig:.2f}: ratio = {tot / lead:.6f}")
    # repeated reversal pair: walk (e, e-bar)
    Ksc = 1
    sg = 0.5
    y = sg * np.random.default_rng(33).normal(size=400_000)
    print(f"  repeated pair (K=1, sigma={sg}): E[e^w e^-w] = 1, product of means E e^w E e^-w = "
          f"{np.mean(np.exp(y)) * np.mean(np.exp(-y)):.5f} (exact e^(sigma^2) = {np.exp(sg**2):.5f})")


# ============================================================================ CHECK 4
def assemble(Kd, A, edges, Rs, Ws):
    """Precision of 1/2 sum z_i^T A_i z_i + 1/2 sum_e (z_i - R_e z_j)^T W_e (z_i - R_e z_j), e=(i,j): j->i."""
    Nn = len(A)
    L = np.zeros((Nn * Kd, Nn * Kd))
    for i in range(Nn):
        L[i * Kd:(i + 1) * Kd, i * Kd:(i + 1) * Kd] += A[i]
    for (i, j), R, W in zip(edges, Rs, Ws):
        D = np.zeros((Kd, Nn * Kd))
        D[:, i * Kd:(i + 1) * Kd] += np.eye(Kd)
        D[:, j * Kd:(j + 1) * Kd] -= R
        L += D.T @ W @ D
    return L


def hopping_split(Kd, A, edges, Rs, Ws):
    """M = blockdiag(A_i + sum_in W + sum_out R^T W R), H = M - Lambda."""
    Nn = len(A)
    M = np.zeros((Nn * Kd, Nn * Kd))
    for i in range(Nn):
        M[i * Kd:(i + 1) * Kd, i * Kd:(i + 1) * Kd] += A[i]
    for (i, j), R, W in zip(edges, Rs, Ws):
        M[i * Kd:(i + 1) * Kd, i * Kd:(i + 1) * Kd] += W
        M[j * Kd:(j + 1) * Kd, j * Kd:(j + 1) * Kd] += R.T @ W @ R
    Lam = assemble(Kd, A, edges, Rs, Ws)
    return M, M - Lam


def S_ind(Lam, h=None):
    n = Lam.shape[0]
    val = 0.5 * np.linalg.slogdet(Lam)[1] - 0.5 * n * np.log(2 * np.pi)
    if h is not None:
        val -= 0.5 * h @ np.linalg.solve(Lam, h)
    return val


def check_induced_action() -> None:
    print("\n[4] prop:glink-induced-action, cor:glink-unanchored-cycle, prop:glink-hopping")
    rng = np.random.default_rng(4)
    K = 2
    # multigraph: triangle 0-1-2, pendant 3, parallel copy 0->1 (second), loop at 2
    edges = [(0, 1), (1, 2), (2, 0), (2, 3), (1, 0), (2, 2)]
    Nn = 4
    A = [spd(K, rng, 0.8) for _ in range(Nn)]
    Ws = [spd(K, rng) for _ in edges]
    oms = [0.8 * rng.normal(size=(K, K)) for _ in edges]
    Rs = [expm(w) for w in oms]
    Lam = assemble(K, A, edges, Rs, Ws)
    h = rng.normal(size=Nn * K)
    # direct Gaussian integration by importance sampling with a mismatched proposal
    n = Nn * K
    nsamp = 2_000_000
    sc = 1.2
    Lmat = np.linalg.inv(Lam)
    mu = Lmat @ h
    prop_cov = sc * Lmat
    Lc = np.linalg.cholesky(prop_cov)
    zs = mu + rng.normal(size=(nsamp, n)) @ Lc.T
    logq = -0.5 * np.einsum("na,ab,nb->n", zs - mu, np.linalg.inv(prop_cov), zs - mu) \
        - 0.5 * np.linalg.slogdet(2 * np.pi * prop_cov)[1]
    logf = zs @ h - 0.5 * np.einsum("na,ab,nb->n", zs, Lam, zs)
    wts = np.exp(logf - logq - (logf - logq).max())
    logZ_is = np.log(wts.mean()) + (logf - logq).max()
    se = wts.std(ddof=1) / np.sqrt(nsamp) / wts.mean()
    print(f"  -log Z_matter: closed form {S_ind(Lam, h):.6f}   importance sampling {-logZ_is:.6f} (rel. SE {se:.1e})")

    # joint normalization, K=1 single edge: marginal of omega by quadrature vs nu e^{-S_ind}
    a_i, a_j, w = 0.7, 1.1, 1.5
    grid = np.linspace(-9, 9, 721)
    dz = grid[1] - grid[0]
    Z1, Z2 = np.meshgrid(grid, grid, indexing="ij")
    vals = []
    for omg in [-1.0, 0.0, 0.8]:
        R = np.exp(omg)
        E_ = 0.5 * a_i * Z1 ** 2 + 0.5 * a_j * Z2 ** 2 + 0.5 * w * (Z1 - R * Z2) ** 2
        quad = np.log(np.exp(-E_).sum() * dz * dz)
        Lm = np.array([[a_i + w, -w * R], [-w * R, a_j + w * R * R]])
        vals.append((omg, quad, -S_ind(Lm)))
    for omg, quad, cf in vals:
        print(f"    omega={omg:+.1f}: log int e^-E dz (quadrature) {quad:.10f}  closed -S_ind {cf:.10f}")

    # lower bound over random large GL configurations
    worst = np.inf
    lower = S_ind(assemble(K, A, [], [], []), h)
    for _ in range(500):
        Rr = [expm(3.0 * rng.normal(size=(K, K))) for _ in edges]
        worst = min(worst, S_ind(assemble(K, A, edges, Rr, Ws), h) - lower)
    print(f"  min over 500 random large configurations of S_ind - S_lower = {worst:.3e} (must be >= 0)")

    # forest with isometric links and isotropic data in a fiber metric G
    Gf = spd(K, rng)
    Gh = np.linalg.cholesky(Gf)  # Gf = Gh Gh^T ; isometry R^T Gf R = Gf  <=> Gh^T R Gh^{-T} orthogonal
    tree = [(0, 1), (1, 2), (1, 3)]
    vals = []
    for _ in range(20):
        Rr = []
        for _e in tree:
            Om = rng.normal(size=(K, K))
            O = expm(Om - Om.T)
            Rr.append(np.linalg.solve(Gh.T, O @ Gh.T))
        vals.append(S_ind(assemble(K, [1.3 * Gf, 0.4 * Gf, 2.0 * Gf, 0.9 * Gf], tree, Rr, [0.7 * Gf, 1.1 * Gf, 0.5 * Gf])))
    print(f"  forest, isometric links, isotropic data: spread of S_ind over 20 link draws = {np.ptp(vals):.2e}")
    report("check R^T G R = G", np.abs(Rr[0].T @ Gf @ Rr[0] - Gf).max(), 1e-12)

    # single edge formula and symmetric directions
    Ai, Aj, We = spd(K, rng), spd(K, rng), spd(K, rng)
    Rr = expm(rng.normal(size=(K, K)))
    Lm = assemble(K, [Ai, Aj], [(0, 1)], [Rr], [We])
    Wt = np.linalg.inv(np.linalg.inv(We) + np.linalg.inv(Ai))
    lhs = np.linalg.slogdet(Lm)[1]
    rhs = np.linalg.slogdet(Ai + We)[1] + np.linalg.slogdet(Aj + Rr.T @ Wt @ Rr)[1]
    report("single edge: |log det Lambda - [log det(A_i+W) + log det(A_j + R^T Wt R)]|", abs(lhs - rhs), 1e-11)
    ai, aj, ww = 0.9, 1.4, 1.7
    wt = ww * ai / (ww + ai)
    Ssym = rng.normal(size=(K, K))
    Ssym = Ssym + Ssym.T

    def s_edge(t):
        return S_ind(assemble(K, [ai * np.eye(K), aj * np.eye(K)], [(0, 1)], [expm(t * Ssym)], [ww * np.eye(K)]))

    hh = 1e-4
    d1 = (s_edge(hh) - s_edge(-hh)) / (2 * hh)
    d2 = (s_edge(hh) - 2 * s_edge(0) + s_edge(-hh)) / hh ** 2
    print(f"  symmetric generator: dS/dt(0) FD {d1:.8f} vs wt Tr S/(a_j+wt) {wt * np.trace(Ssym) / (aj + wt):.8f}")
    print(f"                       d2S/dt2(0) FD {d2:.6f} vs 2 wt a_j |S|^2/(a_j+wt)^2 {2 * wt * aj * np.sum(Ssym**2) / (aj + wt) ** 2:.6f}")
    Om = rng.normal(size=(K, K))
    print(f"  skew generator on one edge: S_ind change {s_edge(0) - S_ind(assemble(K, [ai*np.eye(K), aj*np.eye(K)], [(0, 1)], [expm(Om - Om.T)], [ww*np.eye(K)])):.2e}")
    # non-integrability (K=1): det -> a_j(a_i+w) as omega -> -inf
    for omg in [-2.0, -5.0, -10.0, -20.0]:
        R = np.exp(omg)
        Lm = np.array([[a_i + w, -w * R], [-w * R, a_j + w * R * R]])
        print(f"    K=1 edge, omega={omg:+.0f}: det Lambda = {np.linalg.det(Lm):.10f}  limit a_j(a_i+w) = {a_j * (a_i + w):.10f}")

    # unanchored cycle determinant det Lambda = det(I-Hol)^2 prod det W
    for Kd in [2, 3]:
        for mm in [2, 3, 4]:
            cyc = [(k, (k + 1) % mm) for k in range(mm)]
            Rc = [expm(0.7 * rng.normal(size=(Kd, Kd))) for _ in cyc]
            Wc = [spd(Kd, rng) for _ in cyc]
            Lm = assemble(Kd, [np.zeros((Kd, Kd))] * mm, cyc, Rc, Wc)
            Hol = np.eye(Kd)
            for R in Rc:
                Hol = Hol @ R
            pred = np.linalg.det(np.eye(Kd) - Hol) ** 2 * np.prod([np.linalg.det(Wk) for Wk in Wc])
            print(f"  unanchored {mm}-cycle, K={Kd}: det Lambda {np.linalg.det(Lm):.10e}  det(I-Hol)^2 prod det W {pred:.10e}")
    # g10 witness on the flat slice
    a0 = 0.6
    for omg in [0.0, 0.5, -1.2]:
        Lm = assemble(1, [a0 * np.eye(1)] * 2, [(0, 1), (1, 0)], [np.array([[np.exp(omg)]]), np.array([[np.exp(-omg)]])],
                      [np.eye(1), np.eye(1)])
        print(f"  g10 slice omega={omg:+.1f}: 1/2 log det {0.5*np.linalg.slogdet(Lm)[1]:.10f}  "
              f"1/2 log(a0^2+4 a0 cosh^2) {0.5*np.log(a0**2 + 4*a0*np.cosh(omg)**2):.10f}")
    # unanchored pair: regular zero of f(t) = det(I - e^{tI} e^{Y*})
    Kd = 3
    Ystar = np.diag([0.0, np.log(2.0), np.log(3.0)])

    def f(t):
        return np.linalg.det(np.eye(Kd) - np.exp(t) * expm(Ystar))

    print(f"  unanchored pair: f(0) = {f(0.0):.2e}, f'(0) FD = {(f(1e-6) - f(-1e-6)) / 2e-6:.6f}  (-(1-2)(1-3) = -2)")
    prev = None
    for dl in [1e-2, 1e-4, 1e-6, 1e-8]:
        ts = np.concatenate([-np.logspace(np.log10(0.3), np.log10(dl), 6000), np.logspace(np.log10(dl), np.log10(0.3), 6000)])
        ts.sort()
        g = 1.0 / np.abs([f(t) for t in ts])
        neg = ts < 0
        integ = np.trapezoid(g[neg], ts[neg]) + np.trapezoid(g[~neg], ts[~neg])
        inc = "" if prev is None else f"   increment {integ - prev:.4f} (log 100 = {np.log(100):.4f})"
        print(f"    int_(delta<|t|<0.3) |f|^-1 dt, delta={dl:.0e}: {integ:.4f}{inc}")
        prev = integ

    # forest with general links: Lambda = T^T Lambda_flat T, Lambda_flat in the interaction family
    tree = [(1, 0), (2, 1), (3, 1)]  # residual z_i - R z_j, e: j -> i ; root 0
    Rt = [expm(0.8 * rng.normal(size=(K, K))) for _ in tree]
    At = [spd(K, rng) for _ in range(4)]
    Wt_ = [spd(K, rng) for _ in tree]
    Lt = assemble(K, At, tree, Rt, Wt_)
    # tree transports from the root 0: z_i = T_i y_i, T_0 = I, T_i = R_e T_j on the tree copy e: j -> i
    T = [np.eye(K) for _ in range(4)]
    T[1] = Rt[0] @ T[0]
    T[2] = Rt[1] @ T[1]
    T[3] = Rt[2] @ T[1]
    Afl = [T[i].T @ At[i] @ T[i] for i in range(4)]
    Wfl = [T[i].T @ W @ T[i] for (i, j), W in zip(tree, Wt_)]
    Lflat = assemble(K, Afl, tree, [np.eye(K)] * 3, Wfl)
    lhs = np.linalg.slogdet(Lt)[1]
    # det(T^T L T) = det(T)^2 det L  ->  log det Lflat = log det Lt + 2 log|det T|
    report("forest: |log det Lambda_flat - (log det Lambda + 2 sum log|det T_i|)|",
           abs(np.linalg.slogdet(Lflat)[1] - (lhs + 2 * sum(np.linalg.slogdet(Ti)[1] for Ti in T))), 1e-10)
    Tb = np.zeros((4 * K, 4 * K))
    for i in range(4):
        Tb[i * K:(i + 1) * K, i * K:(i + 1) * K] = T[i]
    report("forest: |T^T Lambda T - Lambda_flat|", np.abs(Tb.T @ Lt @ Tb - Lflat).max(), 1e-10)

    # hopping series and walk sums on the multigraph above
    M, H = hopping_split(K, A, edges, Rs, Ws)
    X = np.linalg.solve(M, H)
    rho = np.max(np.abs(np.linalg.eigvals(X)))
    ser = 0.5 * np.linalg.slogdet(M)[1]
    Xn = np.eye(n)
    for k in range(1, 400):
        Xn = Xn @ X
        ser -= 0.5 * np.trace(Xn) / k
    print(f"  hopping: spectral radius {rho:.4f}; |series(400) - 1/2 log det Lambda| = "
          f"{abs(ser - 0.5 * np.linalg.slogdet(Lam)[1]):.2e}")
    # walk enumeration: oriented copies f: j->i with block M_i^{-1} W_f R_f (reversal: W_fbar R_fbar)
    hops = []
    for (i, j), R, W in zip(edges, Rs, Ws):
        hops.append((i, j, np.linalg.solve(M[i*K:(i+1)*K, i*K:(i+1)*K], W @ R)))
        Wb = R.T @ W @ R
        Rb = np.linalg.inv(R)
        hops.append((j, i, np.linalg.solve(M[j*K:(j+1)*K, j*K:(j+1)*K], Wb @ Rb)))
    for nlen in [1, 2, 3, 4]:
        tot = 0.0
        for seq in itertools.product(range(len(hops)), repeat=nlen):
            # walk: step k uses hop (i_k <- j_k); consecutive: j_k == i_{k+1}; closed: j_last == i_0
            ok = all(hops[seq[k]][1] == hops[seq[k + 1]][0] for k in range(nlen - 1)) and hops[seq[-1]][1] == hops[seq[0]][0]
            if ok:
                P = np.eye(K)
                for s_ in seq:
                    P = P @ hops[s_][2]
                tot += np.trace(P)
        print(f"    n={nlen}: Tr[(M^-1 H)^n] {np.trace(np.linalg.matrix_power(X, nlen)):+.12f}   walk sum {tot:+.12f}")
    # automatic convergence: spectral radius over random large configurations, against 1 - theta
    rmax, viol = 0.0, 0
    for _ in range(300):
        Rr = [expm(2.5 * rng.normal(size=(K, K))) for _ in edges]
        Mr, Hr = hopping_split(K, A, edges, Rr, Ws)
        rr_ = np.max(np.abs(np.linalg.eigvals(np.linalg.solve(Mr, Hr))))
        theta = min(np.min(np.linalg.eigvals(np.linalg.solve(Mr[i*K:(i+1)*K, i*K:(i+1)*K], A[i])).real) for i in range(Nn))
        viol += int(rr_ > 1 - theta + 1e-12)
        rmax = max(rmax, rr_)
    print(f"  max spectral radius of M^-1 H over 300 random large configurations (A_i > 0): {rmax:.6f} (< 1);"
          f" violations of rho <= 1 - theta: {viol}")


# ============================================================================ CHECK 5
def check_wilson() -> None:
    print("\n[5] prop:glink-hopping: Wilson triangle coefficient at increasing self precision")
    rng = np.random.default_rng(5)
    K = 3
    Gf = spd(K, rng)
    Gh = np.linalg.cholesky(Gf)
    tri = [(0, 1), (1, 2), (2, 0)]
    w = 1.0
    Rr = []
    for _ in tri:
        Om = 0.9 * rng.normal(size=(K, K))
        Rr.append(np.linalg.solve(Gh.T, expm(Om - Om.T) @ Gh.T))
    Hol = Rr[0] @ Rr[1] @ Rr[2]
    Q = 0.5 * gip(Hol - np.eye(K), Hol - np.eye(K), Gf)
    report("isometric: |Q - (K - Tr Hol)|", abs(Q - (K - np.trace(Hol))), 1e-12)
    for a in [3.0, 10.0, 30.0, 100.0, 300.0]:
        abar = a + 2 * w
        Lm = assemble(K, [a * Gf] * 3, tri, Rr, [w * Gf] * 3)
        L0 = assemble(K, [a * Gf] * 3, tri, [np.eye(K)] * 3, [w * Gf] * 3)
        dS = S_ind(Lm) - S_ind(L0)
        lead = (w / abar) ** 3 * Q
        kap = w / abar
        bound = (K / 5) * ((2 * kap) ** 5 / (1 - 2 * kap) + 2 * kap ** 5 / (1 - kap))
        print(f"  a={a:6.1f}: [S_ind - S_ind(flat)] / (kappa^3 Q) = {dS / lead:.6f};  |rem| = {abs(dS - lead):.2e} <= bound {bound:.2e}")


# ============================================================================ CHECK 6
def check_spectrum() -> None:
    print("\n[6] prop:glink-linear-spectrum: ring of N agents x (n1+1) episodes, dense eigensolver")
    rng = np.random.default_rng(6)
    for (N, n1) in [(5, 3), (6, 4), (3, 0)]:
        d = 4  # dim gl(2)
        alpha, b, c, mm = 0.7, 0.3, 1.9, 2.4
        ones = np.ones((N, N))
        LP = np.zeros((n1 + 1, n1 + 1))
        for nn in range(n1):
            LP[nn, nn] += 1
            LP[nn + 1, nn + 1] += 1
            LP[nn, nn + 1] -= 1
            LP[nn + 1, nn] -= 1
        Kop = ((alpha + b) * np.eye(N * (n1 + 1)) + c * np.kron(ones, np.eye(n1 + 1)) + mm * np.kron(np.eye(N), LP))
        Kop = np.kron(Kop, np.eye(d))
        ev = np.sort(np.linalg.eigvalsh(Kop))
        pred = []
        for q in range(N):
            for m_ in range(n1 + 1):
                pred += [alpha + b + c * N * (q == 0) + 4 * mm * np.sin(np.pi * m_ / (2 * (n1 + 1))) ** 2] * d
        pred = np.sort(pred)
        print(f"  N={N}, n1={n1}: max |eig - formula| = {np.abs(ev - pred).max():.2e};  min eig {ev.min():.6f}  (alpha+b = {alpha + b})")
    # also check the quadratic loop term is the Hessian of c*Q_p at 0 (ring of 4, gl(2), G random)
    K = 2
    N = 4
    G = spd(K, rng)
    c = 1.0

    def loopQ(x):
        Wm = np.eye(K)
        for k in range(N):
            Wm = Wm @ expm(x[k * K * K:(k + 1) * K * K].reshape(K, K))
        D_ = Wm - np.eye(K)
        return c * 0.5 * gip(D_, D_, G)

    dim = N * K * K
    hh = 1e-4
    H = np.zeros((dim, dim))
    for p in range(dim):
        for q in range(dim):
            ep = np.zeros(dim)
            eq = np.zeros(dim)
            ep[p] = hh
            eq[q] = hh
            H[p, q] = (loopQ(ep + eq) - loopQ(ep - eq) - loopQ(-ep + eq) + loopQ(-ep - eq)) / (4 * hh * hh)
    # predicted: c * C^* C with <.,.>_G : quadratic form 1/2 c ||sum_k x_k||_G^2
    Gi = np.linalg.inv(G)
    Bm = np.zeros((K * K, K * K))  # matrix of <X,Y>_G in the entry basis
    for p in range(K * K):
        for q in range(K * K):
            Ep = np.zeros(K * K)
            Eq = np.zeros(K * K)
            Ep[p] = 1
            Eq[q] = 1
            Bm[p, q] = gip(Ep.reshape(K, K), Eq.reshape(K, K), G)
    pred = c * np.kron(np.ones((N, N)), Bm)
    report("Hessian of c Q_p at 0 vs c C^*C (rel)", np.abs(H - pred).max() / np.abs(pred).max(), 1e-6)


# ============================================================================ CHECK 7
def check_coarse_generator() -> None:
    print("\n[7] prop:link-coarse-generator-law: no-log probability, BCH remainder, cumulants")
    rng = np.random.default_rng(7)
    # (a) GL+(2): probability of no real logarithm of e^A e^B (two distinct negative eigenvalues)
    n = 2_000_000
    for sig in [0.5, 1.0, 1.5, 2.5]:
        Aa = sig * rng.normal(size=(n, 2, 2))
        Bb = sig * rng.normal(size=(n, 2, 2))
        C = expm2(Aa) @ expm2(Bb)
        tr = C[:, 0, 0] + C[:, 1, 1]
        det = C[:, 0, 0] * C[:, 1, 1] - C[:, 0, 1] * C[:, 1, 0]
        disc = tr ** 2 - 4 * det
        noreal = (disc > 0) & (tr < 0)
        _, ex = logm2(C)
        print(f"  sigma={sig}: P(no real log) = {noreal.mean():.5f} +- {np.sqrt(noreal.mean()*(1-noreal.mean())/n):.5f};"
              f"  P(no principal log) = {1 - ex.mean():.5f}")
    n3 = 200_000
    A3 = 1.5 * rng.normal(size=(n3, 3, 3))
    B3 = 1.5 * rng.normal(size=(n3, 3, 3))
    C3 = expm(A3) @ expm(B3)
    ev = np.linalg.eigvals(C3)
    isreal = np.all(np.abs(ev.imag) < 1e-9, axis=1)
    evr = np.sort(ev.real, axis=1)
    two_neg = isreal & (evr[:, 0] < 0) & (evr[:, 1] < 0) & (evr[:, 2] > 0) & (np.abs(evr[:, 0] - evr[:, 1]) > 1e-9)
    print(f"  K=3, sigma=1.5: P(two distinct negative and one positive eigenvalue: no real log) = {two_neg.mean():.5f}")
    witness = expm(np.pi * np.array([[0, -1.0], [1.0, 0]])) @ expm(np.diag([0.0, np.log(2.0)]))
    print(f"  witness exp(pi J) exp(diag(0,log 2)) = {np.round(witness, 12).ravel()}")
    Kd = 4
    J4 = np.zeros((Kd, Kd))
    J4[0, 1], J4[1, 0] = -np.pi, np.pi
    w4 = expm(J4) @ expm(np.diag([0.0, np.log(2), np.log(3), np.log(4)]))
    print(f"  witness K=4 eigenvalues: {np.round(np.sort(np.linalg.eigvals(w4).real), 10)}")

    # (b) BCH degree three and the remainder scaling
    X, Y = rng.normal(size=(3, 3)), rng.normal(size=(3, 3))

    def br(P, Q):
        return P @ Q - Q @ P

    for t in [0.2, 0.1, 0.05, 0.025]:
        Zt = logm(expm(t * X) @ expm(t * Y)).real
        ser = t * (X + Y) + t ** 2 / 2 * br(X, Y) + t ** 3 / 12 * (br(X, br(X, Y)) + br(Y, br(Y, X)))
        print(f"    t={t:.3f}: |Log(e^tX e^tY) - BCH_3| = {np.abs(Zt - ser).max():.3e}   / t^4 = {np.abs(Zt - ser).max() / t ** 4:.4f}")
    # symbolic: degree-2 and degree-3 components from the grouped log series (noncommutative)
    import sympy as sp
    Xs_, Ys_ = sp.symbols("X Y", commutative=False)
    P1 = Xs_ + Ys_
    P2 = Xs_ ** 2 / 2 + Xs_ * Ys_ + Ys_ ** 2 / 2
    P3 = Xs_ ** 3 / 6 + Xs_ ** 2 * Ys_ / 2 + Xs_ * Ys_ ** 2 / 2 + Ys_ ** 3 / 6

    def sbr(P, Q):
        return P * Q - Q * P

    d2 = sp.expand(P2 - P1 ** 2 / 2 - sbr(Xs_, Ys_) / 2)
    d3 = sp.expand(P3 - (P1 * P2 + P2 * P1) / 2 + P1 ** 3 / 3
                   - (sbr(Xs_, sbr(Xs_, Ys_)) + sbr(Ys_, sbr(Ys_, Xs_))) / 12)
    print(f"  sympy (noncommutative): BCH_2 - [X,Y]/2 = {d2};  BCH_3 - ([X,[X,Y]]+[Y,[Y,X]])/12 = {d3}")
    # majorant constants used in the proof
    gmax = -np.log(2 - np.exp(0.5))
    print(f"  -log(2-e^(1/2)) = {gmax:.6f} < pi/2 = {np.pi/2:.6f}: {gmax < np.pi/2};  2*that < 2*pi: {2*gmax < 2*np.pi}")
    u = sp.symbols("u")
    ser_u = sp.series(-sp.log(2 - sp.exp(u)), u, 0, 30).removeO()
    bcoef = [float(ser_u.coeff(u, k)) for k in range(30)]
    c3 = sum(bcoef[k] * 2.0 ** (4 - k) for k in range(4, 30))
    print(f"  Taylor coefficients b_1..b_6 of -log(2-e^u): {np.round(bcoef[1:7], 6)} (all >= 0: {min(bcoef[1:]) >= 0});"
          f"  c3 = sum_(n>=4) b_n 2^(4-n) ~ {c3:.4f} (partial sum to n=29)")

    # (b') the principal logarithm stays in the Lie subalgebra (so(3), sl(3), upper triangular b(3))
    def opnorm(A):
        return np.linalg.norm(A, 2)

    worst = {"so(3)": 0.0, "sl(3)": 0.0, "b(3)": 0.0}
    for _ in range(300):
        for name in worst:
            A1, A2 = rng.normal(size=(3, 3)), rng.normal(size=(3, 3))
            if name == "so(3)":
                A1, A2 = A1 - A1.T, A2 - A2.T
            elif name == "sl(3)":
                A1 -= np.trace(A1) / 3 * np.eye(3)
                A2 -= np.trace(A2) / 3 * np.eye(3)
            else:
                A1, A2 = np.triu(A1), np.triu(A2)
            sc = 0.5 * rng.uniform(0.2, 1.0) / (opnorm(A1) + opnorm(A2))
            Lg = logm(expm(sc * A1) @ expm(sc * A2)).real
            if name == "so(3)":
                res = np.abs(Lg + Lg.T).max()
            elif name == "sl(3)":
                res = abs(np.trace(Lg))
            else:
                res = np.abs(np.tril(Lg, -1)).max()
            worst[name] = max(worst[name], res)
    print("  Log(e^A e^B) in the subalgebra for ||A||+||B||<=1/2: worst residuals " +
          ", ".join(f"{k}: {v:.1e}" for k, v in worst.items()))

    # (c) Gaussian integration-by-parts identities for the cumulant coefficients (gl(2), anisotropic)
    nn = 4_000_000
    Ca = spd(4, rng, 0.5)
    Cb = spd(4, rng, 0.5)
    La, Lb = np.linalg.cholesky(Ca), np.linalg.cholesky(Cb)
    Ys = (rng.normal(size=(nn, 4)) @ La.T).reshape(nn, 2, 2)
    Zs = (rng.normal(size=(nn, 4)) @ Lb.T).reshape(nn, 2, 2)
    ups = rng.normal(size=(2, 2))
    a = (Ca @ ups.reshape(-1)).reshape(2, 2)
    b = (Cb @ ups.reshape(-1)).reshape(2, 2)

    def ip(U, V):  # Frobenius, batched in second argument allowed
        return np.einsum("ab,...ab->...", U, V)

    s = ip(ups, Ys) + ip(ups, Zs)
    comm = Ys @ Zs - Zs @ Ys
    q = 0.5 * ip(ups, comm)
    t1 = Ys @ comm - comm @ Ys  # [Y,[Y,Z]]
    commZY = -comm
    t2 = Zs @ commZY - commZY @ Zs  # [Z,[Z,Y]]
    rho = (ip(ups, t1) + ip(ups, t2)) / 12.0
    pred3 = ip(ups, a @ b - b @ a)
    est3 = batched_cumulant(np.stack([s, q], 1), lambda u: np.mean((u[:, 0] - u[:, 0].mean()) ** 2 * (u[:, 1] - u[:, 1].mean())))
    print(f"  cum(psi1,psi1,psi2): MC {est3[0]:.5f} +- {est3[1]:.5f}   formula kappa3 = <u,[u_e',u_e]> = {pred3:.5f}")
    va = ip(ups, a[None] @ Zs - Zs @ a[None])
    vb = ip(ups, Ys @ b[None] - b[None] @ Ys)
    pred_ssqq = 0.5 * (np.mean(va ** 2) + np.mean(vb ** 2))
    est_ssqq = batched_cumulant(np.stack([s, q], 1),
                                lambda u: np.mean(u[:, 0] ** 2 * u[:, 1] ** 2) - np.mean(u[:, 0] ** 2) * np.mean(u[:, 1] ** 2)
                                - 2 * np.mean(u[:, 0] * u[:, 1]) ** 2)
    print(f"  cum(psi1,psi1,psi2,psi2): MC {est_ssqq[0]:.5f} +- {est_ssqq[1]:.5f}   formula 2E(d psi2)^2 = {pred_ssqq:.5f}")

    def rho_at(Pm, Qm):
        c1 = Pm @ Qm - Qm @ Pm
        return (ip(ups, Pm @ c1 - c1 @ Pm) + ip(ups, Qm @ (-c1) - (-c1) @ Qm)) / 12.0

    pred_sssr = 6 * rho_at(a, b)
    est_sssr = batched_cumulant(np.stack([s, rho], 1),
                                lambda u: np.mean(u[:, 0] ** 3 * u[:, 1]) - 3 * np.mean(u[:, 0] ** 2) * np.mean(u[:, 0] * u[:, 1]))
    print(f"  cum(psi1,psi1,psi1,psi3): MC {est_sssr[0]:.5f} +- {est_sssr[1]:.5f}   formula 6 psi3(u_e',u_e) = {pred_sssr:.5f}")
    # exact expectations by tensor Gauss-Hermite quadrature: 4 nodes per standard coordinate integrate
    # every polynomial of degree <= 7 in each coordinate exactly, which covers all moments used here
    from numpy.polynomial.hermite_e import hermegauss
    xg, wg = hermegauss(4)
    wg = wg / np.sqrt(2 * np.pi)
    grid = np.array(np.meshgrid(*([xg] * 8), indexing="ij")).reshape(8, -1).T
    wts = np.prod(np.array(np.meshgrid(*([wg] * 8), indexing="ij")).reshape(8, -1).T, axis=1)
    Yq = (grid[:, :4] @ La.T).reshape(-1, 2, 2)
    Zq = (grid[:, 4:] @ Lb.T).reshape(-1, 2, 2)
    sq = ip(ups, Yq) + ip(ups, Zq)
    cq = Yq @ Zq - Zq @ Yq
    qq = 0.5 * ip(ups, cq)
    rq = (ip(ups, Yq @ cq - cq @ Yq) + ip(ups, Zq @ (-cq) - (-cq) @ Zq)) / 12.0
    dq = 0.5 * ip(ups, a[None] @ Zq - Zq @ a[None]) + 0.5 * ip(ups, Yq @ b[None] - b[None] @ Yq)

    def Eq(v):
        return float(np.sum(wts * v))

    ex3 = Eq(sq ** 2 * qq) - Eq(sq ** 2) * Eq(qq)
    ex4 = Eq(sq ** 2 * qq ** 2) - Eq(sq ** 2) * Eq(qq ** 2) - 2 * Eq(sq * qq) ** 2
    ex4b = Eq(sq ** 3 * rq) - 3 * Eq(sq ** 2) * Eq(sq * rq)
    print(f"  exact quadrature: cum(psi1,psi1,psi2) {ex3:.12f} vs kappa3 {pred3:.12f};"
          f"  cum(psi1,psi1,psi2,psi2) {ex4:.12f} vs 2E(d psi2)^2 {2 * Eq(dq ** 2):.12f};"
          f"  cum(psi1,psi1,psi1,psi3) {ex4b:.12f} vs 6 psi3 {pred_sssr:.12f};  E psi1 = {Eq(sq):.1e}, E psi2 = {Eq(qq):.1e}")

    # (c') exact values of the cumulant forms at the stated instances, and the invariant case
    def kappa_forms(ups_, Cp, Cq, basis):
        r"""kappa3, kappa4 for covariance operators Cp=Lambda_e'^{-1}, Cq=Lambda_e^{-1} given as matrices
        in an orthonormal basis (list of matrices) of g for the Frobenius pairing."""
        def coords(M):
            return np.array([np.sum(Bk * M) for Bk in basis])

        def mat(v):
            return sum(vk * Bk for vk, Bk in zip(v, basis))

        uc = coords(ups_)
        up, uq = mat(Cp @ uc), mat(Cq @ uc)
        k3 = np.sum(ups_ * (up @ uq - uq @ up))
        # linear functionals zeta -> <u,[up,zeta]> and zeta' -> <u,[zeta',uq]>
        l1 = np.array([np.sum(ups_ * (up @ Bk - Bk @ up)) for Bk in basis])
        l2 = np.array([np.sum(ups_ * (Bk @ uq - uq @ Bk)) for Bk in basis])
        e1 = l1 @ Cq @ l1  # zeta_e ~ N(0, Cq)
        e2 = l2 @ Cp @ l2  # zeta_e' ~ N(0, Cp)
        c1 = up @ uq - uq @ up
        dd = (up @ c1 - c1 @ up) + (uq @ (-c1) - (-c1) @ uq)
        k4 = 3 * e1 + 3 * e2 + 2 * np.sum(ups_ * dd)
        return k3, k4

    for Kk in [2, 3]:
        basis = []
        for a_ in range(Kk):
            for b_ in range(Kk):
                Eab = np.zeros((Kk, Kk))
                Eab[a_, b_] = 1.0
                basis.append(Eab)
        dim = Kk * Kk
        E12 = np.zeros((Kk, Kk))
        E12[0, 1] = 1.0
        E11 = np.zeros((Kk, Kk))
        E11[0, 0] = 1.0
        k3i, k4i = kappa_forms(E12, np.eye(dim), np.eye(dim), basis)
        # kappa3 identically zero at unit precisions: random directions
        k3r = max(abs(kappa_forms(rng.normal(size=(Kk, Kk)), np.eye(dim), np.eye(dim), basis)[0]) for _ in range(20))
        pvec = np.array([np.sum(E12 * Bk) for Bk in basis])
        Cq = np.eye(dim) + np.outer(pvec, pvec)
        k3a, _ = kappa_forms(E11 + E12, np.eye(dim), Cq, basis)
        print(f"  K={Kk}: unit precisions: kappa4(E12) = {k4i:.12f} (claim 12), max|kappa3| over random u = {k3r:.1e};"
              f"  anisotropic: kappa3(E11+E12) = {k3a:.12f} (claim 1)")
    # invariant inner product on so(3) (Frobenius restricted to skew matrices), isotropic precisions
    so3 = []
    for (a_, b_) in [(0, 1), (0, 2), (1, 2)]:
        Bk = np.zeros((3, 3))
        Bk[a_, b_], Bk[b_, a_] = 1 / np.sqrt(2), -1 / np.sqrt(2)
        so3.append(Bk)
    worst3 = 0.0
    for _ in range(50):
        v = rng.normal(size=3)
        u_ = sum(vk * Bk for vk, Bk in zip(v, so3))
        k3s, k4s = kappa_forms(u_, 0.7 * np.eye(3), 1.9 * np.eye(3), so3)
        worst3 = max(worst3, abs(k3s), abs(k4s))
    print(f"  so(3), invariant pairing, isotropic precisions: max |kappa3|,|kappa4| over random u = {worst3:.1e} (claim 0)")

    # (d) small-scale non-Gaussianity of the principal-log coarse generator
    print("  (d) gl(2), centered isotropic sigma=1: excess kurtosis of Z_12 vs leading 3 eps^2 (kappa4(E12)=12)")
    nn = 8_000_000
    for eps in [0.4, 0.3, 0.2]:
        Aa = eps * rng.normal(size=(nn, 2, 2))
        Bb = eps * rng.normal(size=(nn, 2, 2))
        Zl, ex = logm2(expm2(Aa) @ expm2(Bb))
        evt = (np.sqrt((Aa ** 2).sum((1, 2))) + np.sqrt((Bb ** 2).sum((1, 2)))) <= 0.6  # Frobenius >= operator norm
        z12 = Zl[ex, 0, 1]
        kur = batched_cumulant(z12, lambda u: cum4(u) / np.var(u) ** 2)
        c4 = batched_cumulant(z12, cum4)
        print(f"    eps={eps}: P(principal log exists) {ex.mean():.6f}, P(event ||.||<=0.6) {evt.mean():.4f};  "
              f"excess kurtosis {kur[0]:.4f} +- {kur[1]:.4f} (lead 3eps^2={3*eps**2:.4f});  "
              f"cum4/eps^6 {c4[0]/eps**6:.3f} +- {c4[1]/eps**6:.3f} (lead 12)")
    print("  (e) third-cumulant witness: Var B_12 doubled, u = E11+E12, nonzero means; cum3/eps^4 vs 3 kappa3 = 3")
    for eps in [0.3, 0.2, 0.1]:
        mA = np.array([[0.3, -0.2], [0.1, 0.4]])
        mB = np.array([[-0.1, 0.5], [0.2, 0.0]])
        Aa = eps * (mA + rng.normal(size=(nn, 2, 2)))
        Bn = rng.normal(size=(nn, 2, 2))
        Bn[:, 0, 1] *= np.sqrt(2.0)
        Bb = eps * (mB + Bn)
        Zl, ex = logm2(expm2(Aa) @ expm2(Bb))
        x = Zl[ex, 0, 0] + Zl[ex, 0, 1]
        c3 = batched_cumulant(x, cum3)
        print(f"    eps={eps}: cum3/eps^4 = {c3[0]/eps**4:.4f} +- {c3[1]/eps**4:.4f}   (leading 3 kappa3 = 3)")
    print("  (f) so(3), centered isotropic: both leading coefficients vanish; excess kurtosis of Z_x is O(eps^4)")
    for eps in [0.6, 0.4, 0.2]:
        nn3 = 2_000_000
        a3 = eps * rng.normal(size=(nn3, 3))
        b3 = eps * rng.normal(size=(nn3, 3))

        def rot(v):
            th = np.linalg.norm(v, axis=1)
            k = v / np.where(th > 0, th, 1)[:, None]
            Kx = np.zeros((len(v), 3, 3))
            Kx[:, 0, 1], Kx[:, 0, 2], Kx[:, 1, 2] = -k[:, 2], k[:, 1], -k[:, 0]
            Kx = Kx - np.transpose(Kx, (0, 2, 1))
            return np.eye(3) + np.sin(th)[:, None, None] * Kx + (1 - np.cos(th))[:, None, None] * (Kx @ Kx)

        Rm = rot(a3) @ rot(b3)
        th = np.arccos(np.clip((np.trace(Rm, axis1=1, axis2=2) - 1) / 2, -1, 1))
        keep = th < 2.5
        Rm, th = Rm[keep], th[keep]
        fac = np.where(th > 1e-8, th / (2 * np.sin(np.where(th > 1e-8, th, 1.0))), 0.5)
        zx = fac * (Rm[:, 2, 1] - Rm[:, 1, 2])
        kur = batched_cumulant(zx, lambda u: cum4(u) / np.var(u) ** 2)
        print(f"    eps={eps}: excess kurtosis of Z_x = {kur[0]:+.5f} +- {kur[1]:.5f}   (eps^2 = {eps**2:.3f}, eps^4 = {eps**4:.4f})")


# ============================================================================ CHECK 8
def check_null_set() -> None:
    print("\n[8] cor:link-holonomy-parent-almost-sure: determinant hyperplane and the SL(2) contrast")
    rng = np.random.default_rng(8)
    for K in [2, 3]:
        nn = 100_000
        # triangle e0: 1->0, e1: 2->1, e2: 0->2 ; walk (e0,e1,e2) based at 0 ; frames arbitrary
        U = [rng.normal(size=(K, K)) + 2 * np.eye(K) for _ in range(3)]
        anchors = [0.5 * rng.normal(size=(K, K)) for _ in range(3)]
        Ls = [0.4 * rng.normal(size=(K * K, K * K)) for _ in range(3)]
        oms = [anchors[k] + (rng.normal(size=(nn, K * K)) @ Ls[k].T).reshape(nn, K, K) for k in range(3)]
        ex = [expm(o) for o in oms]
        Th = [U[0] @ ex[0] @ np.linalg.inv(U[1]), U[1] @ ex[1] @ np.linalg.inv(U[2]), U[2] @ ex[2] @ np.linalg.inv(U[0])]
        Hol = Th[0] @ Th[1] @ Th[2]
        ld = np.linalg.slogdet(Hol)[1]
        lin = sum(np.trace(o, axis1=1, axis2=2) for o in oms)
        print(f"  K={K}: max |log|det Hol| - sum Tr om| = {np.abs(ld - lin).max():.2e};  "
              f"#(|det Hol| = 1 exactly) = {(ld == 0).sum()} of {nn};  "
              f"P(|log|det Hol|| < 1e-2) = {(np.abs(ld) < 1e-2).mean():.2e}, < 1e-3: {(np.abs(ld) < 1e-3).mean():.2e}")
    # SL(2) contrast: elliptic holonomy with positive probability, fixed Gaussian exists
    nn = 200_000
    def sl2(nn_):
        Xs = 0.8 * rng.normal(size=(nn_, 2, 2))
        trc = 0.5 * (Xs[:, 0, 0] + Xs[:, 1, 1])
        Xs[:, 0, 0] -= trc
        Xs[:, 1, 1] -= trc
        return Xs
    H = expm2(sl2(nn)) @ expm2(sl2(nn)) @ expm2(sl2(nn))
    tr = H[:, 0, 0] + H[:, 1, 1]
    ell = np.abs(tr) < 2
    print(f"  SL(2) triangle: P(elliptic loop holonomy) = {ell.mean():.4f} (positive)")
    Hk = H[np.argmax(ell)]
    lam, vec = np.linalg.eig(Hk)
    v = vec[:, 0]
    P = np.column_stack([v.real, v.imag])
    S = P @ P.T
    report("SL(2): fixed Gaussian N(0,PP^T): |H S H^T - S|", np.abs(Hk @ S @ Hk.T - S).max(), 1e-10)
    print(f"  det of an sl(2) holonomy sample: {np.linalg.det(Hk):.12f}")
    # witness of cor (v): (pi/2) J on the non-tree copy of a triangle, zero on tree copies, random frames
    Jm = np.array([[0.0, -1.0], [1.0, 0.0]])
    Uf = [rng.normal(size=(2, 2)) + 2 * np.eye(2) for _ in range(3)]
    Uf = [Ui / np.sqrt(abs(np.linalg.det(Ui))) for Ui in Uf]

    def tri_hol(g0, g1, g2):
        Th0 = Uf[0] @ expm(g0) @ np.linalg.inv(Uf[1])
        Th1 = Uf[1] @ expm(g1) @ np.linalg.inv(Uf[2])
        Th2 = Uf[2] @ expm(g2) @ np.linalg.inv(Uf[0])
        return Th0 @ Th1 @ Th2

    Hw = tri_hol(np.zeros((2, 2)), np.zeros((2, 2)), 0.5 * np.pi * Jm)
    print(f"  witness: Tr k = {np.trace(Hw):+.2e} (claim 0)")
    worst_tr = 0.0
    worst_orth = 0.0
    for _ in range(2000):
        gs = [0.05 * sl2(1)[0] for _ in range(3)]
        Hp = tri_hol(gs[0], gs[1], 0.5 * np.pi * Jm + gs[2])
        worst_tr = max(worst_tr, abs(np.trace(Hp)))
        lam_, vec_ = np.linalg.eig(Hp)
        Pm = np.column_stack([vec_[:, 0].real, vec_[:, 0].imag])
        Rm = np.linalg.solve(Pm, Hp @ Pm)
        worst_orth = max(worst_orth, np.abs(Rm @ Rm.T - np.eye(2)).max())
    print(f"  sl(2) perturbations of size 0.05: max |Tr k| = {worst_tr:.3f} (< 2), max |R R^T - I| in the eigenvector basis = {worst_orth:.1e}")
    # main prop (ii): the witness diag(-1,-2,3,..,K) and an open neighbourhood stay in X_K
    for Kk in [2, 3, 4]:
        J_ = np.zeros((Kk, Kk))
        J_[0, 1], J_[1, 0] = -np.pi, np.pi
        Wt = expm(J_) @ expm(np.diag([0.0] + [np.log(k + 1.0) for k in range(1, Kk)]))
        inside = 0
        for _ in range(2000):
            ev_ = np.linalg.eigvals(Wt + 0.05 * rng.normal(size=(Kk, Kk)))
            real = np.all(np.abs(ev_.imag) < 1e-12)
            evs = np.sort(ev_.real)
            ok = real and (evs[0] < 0) and (evs[1] < 0) and (Kk == 2 or evs[2] > 0) and np.all(np.diff(evs) > 0)
            inside += ok
        print(f"  K={Kk}: witness eigenvalues {np.round(np.sort(np.linalg.eigvals(Wt).real), 10)};"
              f"  perturbations (0.05) staying in X_K: {inside}/2000")


if __name__ == "__main__":
    check_law_level_energy()
    check_sample_record()
    check_expected_loop()
    check_induced_action()
    check_wilson()
    check_spectrum()
    check_coarse_generator()
    check_null_set()
    print("\nDone.")
