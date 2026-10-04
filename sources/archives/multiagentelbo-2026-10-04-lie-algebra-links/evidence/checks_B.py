r"""Float64 validation checks for frag_B_variational.tex.

Latent generators in the collective evidence bound, the link field equation, the
held-link limit, and the induced action of undirected matter.  Every check below is a
finite computation at small size: it validates an identity, a gradient, or a limit of
the fragment on one instance and is not evidence for a general claim.

Run:  C:/anaconda/python.exe checks_B.py  (NumPy and SciPy, float64, CPU, seeded).
"""
from __future__ import annotations

import numpy as np
from numpy.linalg import det, eigvalsh, inv, matrix_rank, norm, slogdet, svd
from numpy.polynomial.hermite_e import hermegauss
from numpy.polynomial.legendre import leggauss
from scipy.linalg import expm, logm, sqrtm
from scipy.optimize import minimize

np.set_printoptions(precision=4, suppress=False, linewidth=110)
RNG = np.random.default_rng(20261003)
RESULTS: list[tuple[str, str, bool]] = []


def report(name: str, value: float, tol: float, note: str = "") -> None:
    ok = bool(np.isfinite(value) and abs(value) <= tol)
    RESULTS.append((name, f"{value:.3e} (tol {tol:.0e}) {note}", ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}: {value:.3e}  tol {tol:.0e}  {note}")


def info(name: str, text: str) -> None:
    print(f"[INFO] {name}: {text}")


def spd(n: int, scale: float = 1.0) -> np.ndarray:
    a = RNG.standard_normal((n, n))
    return scale * (a @ a.T / n + 0.5 * np.eye(n))


def opnorm(a: np.ndarray) -> float:
    return float(svd(a, compute_uv=False)[0])


# ---------------------------------------------------------------------------------
# Frechet derivative of the exponential, L(B,T) = int_0^1 e^{sB} T e^{(1-s)B} ds
# ---------------------------------------------------------------------------------
def L_block(B: np.ndarray, T: np.ndarray) -> np.ndarray:
    r"""\mathbf L(B,T) as the (1,2) block of exp([[B,T],[0,B]])."""
    n = B.shape[0]
    Z = np.zeros((2 * n, 2 * n))
    Z[:n, :n] = B
    Z[:n, n:] = T
    Z[n:, n:] = B
    return expm(Z)[:n, n:]


def L_quad(B: np.ndarray, T: np.ndarray, m: int = 40) -> np.ndarray:
    x, w = leggauss(m)
    s, w = 0.5 * (x + 1.0), 0.5 * w
    return sum(wi * expm(si * B) @ T @ expm((1.0 - si) * B) for si, wi in zip(s, w))


def check_exp_derivative() -> None:
    print("\n== C1 lem:link-exp-derivative ==")
    n = 3
    B = 0.8 * RNG.standard_normal((n, n))
    T = RNG.standard_normal((n, n))
    S = RNG.standard_normal((n, n))
    Lb, Lq = L_block(B, T), L_quad(B, T)
    report("L block formula vs Gauss-Legendre integral", norm(Lb - Lq) / norm(Lb), 1e-12)
    h = 1e-5
    fd = (expm(B + h * T) - expm(B - h * T)) / (2 * h)
    report("L vs central difference of expm", norm(fd - Lb) / norm(Lb), 1e-8)
    worst = 0.0
    for t in (1.0, 1e-1, 1e-2, 1e-3):
        rem = norm(expm(B + t * T) - expm(B) - t * Lb, 2)
        bound = 0.5 * (t * opnorm(T)) ** 2 * np.exp(opnorm(B) + t * opnorm(T))
        worst = max(worst, rem / bound)
    report("Duhamel remainder <= 1/2 |T|^2 e^{|B|+|T|} (max ratio - 1, must be <= 0)",
           max(worst - 1.0, 0.0), 0.0, f"max ratio {worst:.3f}")
    lhs = np.trace(S.T @ Lb)
    rhs = np.trace(L_block(B.T, S).T @ T)
    report("adjoint: <S,L(B,T)> = <L(B^T,S),T>", abs(lhs - rhs) / abs(lhs), 1e-12)
    # gradient of f(e^B), f(M) = 1/2|M-M0|^2 + tr(C^T M)
    M0, C = RNG.standard_normal((n, n)), RNG.standard_normal((n, n))
    f = lambda M: 0.5 * norm(M - M0) ** 2 + np.trace(C.T @ M)
    grad_formula = L_block(B.T, expm(B) - M0 + C)
    grad_fd = np.zeros((n, n))
    for a in range(n):
        for b in range(n):
            E = np.zeros((n, n))
            E[a, b] = 1.0
            grad_fd[a, b] = (f(expm(B + h * E)) - f(expm(B - h * E))) / (2 * h)
    report("grad of f(e^B) = L(B^T, grad f) vs FD", norm(grad_fd - grad_formula) / norm(grad_formula), 1e-8)
    # representation case: so(3) with a fiber metric G, inner product tr(G^{-1} a^T G b)
    basis = []
    for (a, b) in ((0, 1), (0, 2), (1, 2)):
        E = np.zeros((3, 3))
        E[a, b], E[b, a] = -1.0, 1.0
        basis.append(E)
    Gf = spd(3)
    Gi = inv(Gf)
    gram = np.array([[np.trace(Gi @ Ea.T @ Gf @ Eb) for Eb in basis] for Ea in basis])
    xi = 0.7 * RNG.standard_normal(3)
    Bx = sum(c * E for c, E in zip(xi, basis))
    Y = expm(Bx) - M0 + C
    LBY = L_block(Bx.T, Y)
    grad_coords = np.linalg.solve(gram, np.array([np.trace(LBY.T @ E) for E in basis]))
    partials = np.array([(f(expm(Bx + h * E)) - f(expm(Bx - h * E))) / (2 * h) for E in basis])
    report("so(3), G-metric: <(drho)^T L(B^T,grad f), eta>_G = df[eta]",
           norm(gram @ grad_coords - partials) / norm(partials), 1e-8)
    # derivative bounds |D^k exp(B)| <= e^{|B|} |T|^k for k = 1, 2
    r1, r2 = 0.0, 0.0
    for _ in range(300):
        Bk = 1.5 * RNG.standard_normal((n, n))
        Tk = RNG.standard_normal((n, n))
        r1 = max(r1, opnorm(L_block(Bk, Tk)) / (np.exp(opnorm(Bk)) * opnorm(Tk)))
        hh = 1e-3
        d2 = (expm(Bk + hh * Tk) - 2 * expm(Bk) + expm(Bk - hh * Tk)) / hh ** 2
        r2 = max(r2, opnorm(d2) / (np.exp(opnorm(Bk)) * opnorm(Tk) ** 2))
    report("max |L(B,T)|/(e^|B| |T|) - 1 (<= 0)", max(r1 - 1, 0.0), 0.0, f"max ratio {r1:.3f}")
    report("max |D^2 exp(B)[T,T]|/(e^|B| |T|^2) - 1 (<= 0)", max(r2 - 1, 0.0), 0.0, f"max ratio {r2:.3f}")


# ---------------------------------------------------------------------------------
# Gaussian gradients (Bonnet, Price) by quadrature and Monte Carlo
# ---------------------------------------------------------------------------------
A_EXP = np.array([0.3, -0.2])


def f2(x: np.ndarray) -> np.ndarray:
    """Entire test function, so Gauss-Hermite quadrature converges geometrically."""
    x0, x1 = x[..., 0], x[..., 1]
    return np.sin(x0) * x1 ** 2 + np.exp(x @ A_EXP) + np.cos(x0 * x1)


def grad_f2(x: np.ndarray) -> np.ndarray:
    x0, x1 = x[..., 0], x[..., 1]
    e = np.exp(x @ A_EXP)
    u = x0 * x1
    g0 = np.cos(x0) * x1 ** 2 + 0.3 * e - np.sin(u) * x1
    g1 = 2 * np.sin(x0) * x1 - 0.2 * e - np.sin(u) * x0
    return np.stack([g0, g1], axis=-1)


def hess_f2(x: np.ndarray) -> np.ndarray:
    x0, x1 = x[..., 0], x[..., 1]
    e = np.exp(x @ A_EXP)
    u = x0 * x1
    h00 = -np.sin(x0) * x1 ** 2 + 0.09 * e - np.cos(u) * x1 ** 2
    h11 = 2 * np.sin(x0) + 0.04 * e - np.cos(u) * x0 ** 2
    h01 = 2 * np.cos(x0) * x1 - 0.06 * e - np.cos(u) * u - np.sin(u)
    H = np.empty(x.shape[:-1] + (2, 2))
    H[..., 0, 0], H[..., 1, 1], H[..., 0, 1], H[..., 1, 0] = h00, h11, h01, h01
    return H


def gh_grid(dim: int, n: int) -> tuple[np.ndarray, np.ndarray]:
    z, w = hermegauss(n)
    w = w / np.sqrt(2 * np.pi)
    grids = np.meshgrid(*([z] * dim), indexing="ij")
    wgrids = np.meshgrid(*([w] * dim), indexing="ij")
    Z = np.stack([g.ravel() for g in grids], axis=-1)
    W = np.prod(np.stack([g.ravel() for g in wgrids], axis=-1), axis=-1)
    return Z, W


def check_gaussian_gradients() -> None:
    print("\n== C2 lem:link-gaussian-gradients (Bonnet, Price) ==")
    # analytic derivative bound check of the hessian formula
    x = RNG.standard_normal((5, 2))
    hh = 1e-6
    Hfd = np.stack([(grad_f2(x + hh * e) - grad_f2(x - hh * e)) / (2 * hh) for e in np.eye(2)], axis=-1)
    report("analytic Hessian of test function vs FD", norm(Hfd - hess_f2(x)) / norm(hess_f2(x)), 1e-7)
    m = np.array([0.2, -0.4])
    C = np.array([[0.5, 0.15], [0.15, 0.3]])
    Z, W = gh_grid(2, 80)

    def Ef(mm, CC, fun=f2):
        Lc = np.linalg.cholesky(CC)
        return np.tensordot(W, fun(mm + Z @ Lc.T), axes=(0, 0))

    h = 1e-5
    dm = np.array([(Ef(m + h * e, C) - Ef(m - h * e, C)) / (2 * h) for e in np.eye(2)])
    report("Bonnet: d/dm E f = E grad f (quadrature)", norm(dm - Ef(m, C, grad_f2)) / norm(dm), 1e-8)
    Delta = np.array([[0.3, -0.2], [-0.2, 0.5]])
    dC = (Ef(m, C + h * Delta) - Ef(m, C - h * Delta)) / (2 * h)
    price = 0.5 * np.trace(Delta @ Ef(m, C, hess_f2))
    report("Price: d/dC E f [Delta] = 1/2 tr(Delta E Hess f) (quadrature)", abs(dC - price) / abs(price), 1e-7)
    # Monte Carlo: compare the quadrature derivative with MC estimates of E grad f, E Hess f
    n = 400_000
    X = m + RNG.standard_normal((n, 2)) @ np.linalg.cholesky(C).T
    G = grad_f2(X)
    H = np.einsum("ij,nji->n", Delta, hess_f2(X)) * 0.5
    zg = np.max(np.abs(G.mean(0) - dm) / (G.std(0) / np.sqrt(n)))
    zh = abs(H.mean() - dC) / (H.std() / np.sqrt(n))
    report("Monte Carlo E grad f vs d/dm E f (max |z|, < 4)", max(zg - 4.0, 0.0), 0.0, f"|z| = {zg:.2f}")
    report("Monte Carlo 1/2 E tr(Delta Hess f) vs d/dC E f (|z|, < 4)", max(zh - 4.0, 0.0), 0.0, f"|z| = {zh:.2f}")


# ---------------------------------------------------------------------------------
# Vectorized 2x2 exponential and its Frechet derivative (for the field equation)
# ---------------------------------------------------------------------------------
def expm2(B: np.ndarray) -> np.ndarray:
    """exp of a stack of 2x2 real matrices, closed form."""
    t = 0.5 * (B[..., 0, 0] + B[..., 1, 1])
    A = B.copy()
    A[..., 0, 0] -= t
    A[..., 1, 1] -= t
    q = A[..., 0, 0] ** 2 + A[..., 0, 1] * A[..., 1, 0]  # A^2 = q I
    r = np.sqrt(q.astype(complex))
    small = np.abs(r) < 1e-6
    c = np.where(small, 1 + q / 2, np.cosh(r)).real
    rs = np.where(small, 1.0, r)
    s = np.where(small, 1 + q / 6, np.sinh(rs) / rs).real
    out = c[..., None, None] * np.eye(2) + s[..., None, None] * A
    return np.exp(t)[..., None, None] * out


SL, WL = leggauss(24)
SL, WL = 0.5 * (SL + 1), 0.5 * WL


def L2(B: np.ndarray, Y: np.ndarray) -> np.ndarray:
    """L(B, Y) for stacks of 2x2 matrices by Gauss-Legendre in s."""
    out = np.zeros(np.broadcast_shapes(B.shape, Y.shape))
    for s, w in zip(SL, WL):
        out += w * expm2(s * B) @ Y @ expm2((1 - s) * B)
    return out


def check_field_equation() -> None:
    print("\n== C3 prop:link-field-equation (G = GL+(2), one edge, Gaussian R) ==")
    B = RNG.standard_normal((7, 2, 2))
    report("closed-form 2x2 expm vs scipy", max(norm(expm2(B)[k] - expm(B[k])) for k in range(7)), 1e-12)
    report("vectorized L2 vs block formula", max(norm(L2(B, B[::-1])[k] - L_block(B[k], B[::-1][k])) for k in range(7)), 1e-12)
    # record data (reference coordinates), product matter recognition
    W = spd(2)
    mu_i, mu_j = np.array([1.0, 0.4]), np.array([0.6, -0.8])
    Sig_j = spd(2, 0.5)
    S_j = Sig_j + np.outer(mu_j, mu_j)

    def hvals(M):  # expected record energy up to an M-independent constant
        return 0.5 * (-2 * np.einsum("...ab,ab->...", W @ M, np.outer(mu_i, mu_j))
                      + np.einsum("...ba,bc,...cd,da->...", M, W, M, S_j))

    def J(M):  # current = -grad h
        return W @ (np.outer(mu_i, mu_j) - M @ S_j)

    alpha = 0.2 * RNG.standard_normal((2, 2))
    sig2 = 0.15
    Sinv = np.eye(4) / sig2

    def U(om):  # om: (..., 4)
        return hvals(expm2(om.reshape(om.shape[:-1] + (2, 2))))

    def gradU(om):
        Bm = om.reshape(om.shape[:-1] + (2, 2))
        g = L2(np.swapaxes(Bm, -1, -2), -J(expm2(Bm)))
        return g.reshape(om.shape)

    def hessU(om, h=1e-5):
        cols = [(gradU(om + h * e) - gradU(om - h * e)) / (2 * h) for e in np.eye(4)]
        Hm = np.stack(cols, axis=-1)
        return 0.5 * (Hm + np.swapaxes(Hm, -1, -2))

    Z, Wq = gh_grid(4, 9)

    def EU(mu, C, fun=U):
        Lc = np.linalg.cholesky(C)
        return np.tensordot(Wq, fun(mu + Z @ Lc.T), axes=(0, 0))

    a_vec = alpha.ravel()

    def F(mu, C):
        kl = 0.5 * (np.trace(Sinv @ C) + (mu - a_vec) @ Sinv @ (mu - a_vec) - 4
                    + 4 * np.log(sig2) - slogdet(C)[1])
        return kl + EU(mu, C)

    # gradient of U by FD at a point
    om0 = 0.4 * RNG.standard_normal(4)
    gfd = np.array([(U(om0 + 1e-6 * e) - U(om0 - 1e-6 * e)) / 2e-6 for e in np.eye(4)])
    report("grad U = L(om^T, -J(e^om)) vs FD", norm(gfd - gradU(om0)) / norm(gfd), 1e-8)
    mu = a_vec + 0.1 * RNG.standard_normal(4)
    C = 0.05 * spd(4)
    h = 1e-6
    dmu = np.array([(F(mu + h * e, C) - F(mu - h * e, C)) / (2 * h) for e in np.eye(4)])
    field = Sinv @ (mu - a_vec) + EU(mu, C, gradU)
    report("dF/dmu = Sigma^-1(mu-alpha) + E grad U (same quadrature)", norm(dmu - field) / norm(field), 1e-7)
    Delta = spd(4, 0.1)
    dC = (F(mu, C + h * Delta) - F(mu, C - h * Delta)) / (2 * h)
    pr = 0.5 * np.trace(Delta @ (Sinv - inv(C) + EU(mu, C, hessU)))
    report("dF/dC[Delta] = 1/2 tr(Delta(Sigma^-1 - C^-1 + E Hess U))", abs(dC - pr) / abs(pr), 1e-5)

    # stationary point: minimize F over (mu, chol C) and check both field conditions
    tril = np.tril_indices(4)

    def unpack(p):
        Lm = np.zeros((4, 4))
        Lm[tril] = p[4:]
        Lm[np.diag_indices(4)] = np.exp(Lm[np.diag_indices(4)])
        return p[:4], Lm @ Lm.T

    def obj(p):
        m_, C_ = unpack(p)
        return F(m_, C_)

    p0 = np.concatenate([a_vec, np.zeros(10)])
    p0[4:][[0, 2, 5, 9]] = np.log(np.sqrt(0.05))
    res = minimize(obj, p0, method="BFGS", options={"gtol": 1e-11, "maxiter": 5000})
    m_s, C_s = unpack(res.x)
    mean_res = Sinv @ (m_s - a_vec) + EU(m_s, C_s, gradU)
    prec_res = inv(C_s) - (Sinv + EU(m_s, C_s, hessU))
    info("stationary Gaussian link law", f"F = {res.fun:.10f}, iterations {res.nit}")
    report("mean condition residual at minimizer", norm(mean_res), 1e-6)
    report("precision condition Lambda = Sigma^-1 + E Hess U (rel. residual)", norm(prec_res) / norm(inv(C_s)), 1e-4)
    # point limit: E_{N(mu,C)} grad V -> grad V(mu) as C -> 0, and IFT curve
    gV = lambda om: Sinv @ (om - a_vec) + gradU(om)
    res_mode = minimize(lambda om: 0.5 * (om - a_vec) @ Sinv @ (om - a_vec) + U(om), a_vec,
                        jac=gV, method="BFGS", options={"gtol": 1e-13})
    mode = res_mode.x
    C0 = 0.05 * spd(4)
    errs = []
    for s in (0.4, 0.2, 0.1, 0.05):
        sol = minimize(lambda mm: 0.5 * norm(Sinv @ (mm - a_vec) + EU(mm, s ** 2 * C0, gradU)) ** 2,
                       mode, method="BFGS", options={"gtol": 1e-14})
        errs.append((s, norm(sol.x - mode)))
    info("point limit |mu(s) - mode| for C = s^2 C0", ", ".join(f"s={s}: {e:.2e}" for s, e in errs))
    rate = np.log(errs[-2][1] / errs[-1][1]) / np.log(2)
    report("point-limit rate ~ s^2 (observed exponent - 2)", abs(rate - 2.0), 0.15, f"exponent {rate:.3f}")


# ---------------------------------------------------------------------------------
# Loop defect gradient (triangle) and growth
# ---------------------------------------------------------------------------------
def check_loop_defect() -> None:
    print("\n== C3b loop-defect action on a triangle (gradient through L, growth) ==")
    K = 3
    Gf = spd(K)
    Gi = inv(Gf)
    lam = 0.7

    def S(oms):
        H = expm(oms[0]) @ expm(oms[1]) @ expm(oms[2])
        D = np.eye(K) - H
        return 0.5 * lam * np.trace(Gi @ D.T @ Gf @ D)

    oms = [0.5 * RNG.standard_normal((K, K)) for _ in range(3)]
    E = [expm(o) for o in oms]
    H = E[0] @ E[1] @ E[2]
    dSdH = -lam * Gf @ (np.eye(K) - H) @ Gi  # gradient for trace pairing: d/dH 1/2 tr(Gi D^T Gf D)
    # chain rule: H = E0 E1 E2; dH = dE0 E1E2 + E0 dE1 E2 + E0E1 dE2
    grads = [L_block(oms[0].T, dSdH @ (E[1] @ E[2]).T),
             L_block(oms[1].T, E[0].T @ dSdH @ E[2].T),
             L_block(oms[2].T, (E[0] @ E[1]).T @ dSdH)]
    h = 1e-6
    err = 0.0
    for k in range(3):
        for a in range(K):
            for b in range(K):
                Ep = [o.copy() for o in oms]
                Em = [o.copy() for o in oms]
                Ep[k][a, b] += h
                Em[k][a, b] -= h
                fd = (S(Ep) - S(Em)) / (2 * h)
                err = max(err, abs(fd - grads[k][a, b]))
    report("loop-defect gradient via L vs FD (max abs)", err, 1e-7)
    # growth: S(om) <= c1 exp(c2 |om|) along rays
    vals = []
    for t in (1, 2, 4, 8):
        d = [t * o for o in oms]
        vals.append((t, np.log(max(S(d), 1e-300)) / (t * sum(opnorm(o) for o in oms))))
    info("log S / (t sum|om|) along a ray (bounded by ~2)", ", ".join(f"t={t}: {v:.3f}" for t, v in vals))


# ---------------------------------------------------------------------------------
# Gaussian KL closed form, total correlation
# ---------------------------------------------------------------------------------
def check_gaussian_kl() -> None:
    print("\n== C9 prop:link-gaussian-recognition-vfe(a): Gaussian KL and total correlation ==")
    D = 4
    mu, alpha = RNG.standard_normal(D), RNG.standard_normal(D)
    Lam = inv(spd(D, 0.7))
    Sig = spd(D, 1.3)
    C = inv(Lam)
    kl = 0.5 * (np.trace(inv(Sig) @ C) + (mu - alpha) @ inv(Sig) @ (mu - alpha) - D
                + slogdet(Sig)[1] + slogdet(Lam)[1])
    n = 2_000_000
    X = mu + RNG.standard_normal((n, D)) @ np.linalg.cholesky(C).T

    def logpdf(x, m, S):
        Si = inv(S)
        d = x - m
        return -0.5 * (np.einsum("ni,ij,nj->n", d, Si, d) + slogdet(2 * np.pi * S)[1])

    ratio = logpdf(X, mu, C) - logpdf(X, alpha, Sig)
    z = abs(ratio.mean() - kl) / (ratio.std() / np.sqrt(n))
    report("closed-form KL(R||nu) vs Monte Carlo (|z| < 4)", max(z - 4.0, 0.0), 0.0, f"|z| = {z:.2f}, KL = {kl:.4f}")
    # block-diagonal nu (two blocks of 2): KL = TC + sum of block KLs
    Sig_b = np.zeros((D, D))
    Sig_b[:2, :2], Sig_b[2:, 2:] = spd(2), spd(2)
    kl_joint = 0.5 * (np.trace(inv(Sig_b) @ C) + (mu - alpha) @ inv(Sig_b) @ (mu - alpha) - D
                      + slogdet(Sig_b)[1] + slogdet(Lam)[1])
    blocks = [slice(0, 2), slice(2, 4)]
    kl_blocks = sum(0.5 * (np.trace(inv(Sig_b[b, b]) @ C[b, b]) + (mu[b] - alpha[b]) @ inv(Sig_b[b, b]) @ (mu[b] - alpha[b])
                           - 2 + slogdet(Sig_b[b, b])[1] - slogdet(C[b, b])[1]) for b in blocks)
    tc = 0.5 * (sum(slogdet(C[b, b])[1] for b in blocks) + slogdet(Lam)[1])
    report("KL(R||nu) = TC(R) + sum_e KL(R_e||nu_e)", abs(kl_joint - kl_blocks - tc), 1e-12)


# ---------------------------------------------------------------------------------
# Delta-rule current, rank-one stationary matrix, chart closure, fold witness
# ---------------------------------------------------------------------------------
def check_delta_rule_and_prior() -> None:
    print("\n== C4 cor:link-delta-rule: current = -E grad of record energy ==")
    K = 3
    W = spd(K)
    M = expm(0.5 * RNG.standard_normal((K, K)))
    # correlated Gaussian matter recognition for (k_i, k_j)
    mu = RNG.standard_normal(2 * K)
    Cfull = spd(2 * K, 0.6)
    mu_i, mu_j = mu[:K], mu[K:]
    Sig_ij, Sig_j = Cfull[:K, K:], Cfull[K:, K:]
    J_formula = W @ (np.outer(mu_i - M @ mu_j, mu_j) + Sig_ij - M @ Sig_j)
    n = 1_000_000
    Y = mu + RNG.standard_normal((n, 2 * K)) @ np.linalg.cholesky(Cfull).T
    ki, kj = Y[:, :K], Y[:, K:]
    resid = ki - kj @ M.T
    samples = np.einsum("ab,nb,nc->nac", W, resid, kj)
    J_mc = samples.mean(0)
    se = samples.std(0) / np.sqrt(n)
    z = np.max(np.abs(J_mc - J_formula) / se)
    report("delta-rule current vs Monte Carlo (max |z| < 4.5)", max(z - 4.5, 0.0), 0.0, f"max |z| = {z:.2f}")
    # attention-gated version with comparison maps
    SQ, SK = RNG.standard_normal((2, K)), RNG.standard_normal((2, K))
    Wt, beta = spd(2), 0.37
    Jg = beta * SK.T @ Wt @ (np.outer(SQ @ mu_i - SK @ M @ mu_j, mu_j) + SQ @ Sig_ij - SK @ M @ Sig_j)
    resid_g = ki @ SQ.T - kj @ (SK @ M).T
    Jg_mc = beta * np.einsum("ab,bc,nc,nd->ad", SK.T, Wt, resid_g, kj) / n
    report("attention-gated current vs Monte Carlo (rel.)", norm(Jg_mc - Jg) / norm(Jg), 5e-3)

    print("\n== C5 cor:link-prior-necessary(a): rank-one stationary matrix ==")
    Sig_j = spd(K, 0.5)
    S_j = Sig_j + np.outer(mu_j, mu_j)
    h_of = lambda Mm: 0.5 * (-2 * np.trace(W @ Mm @ np.outer(mu_j, mu_i)) + np.trace(Mm.T @ W @ Mm @ S_j))
    Mstar = np.outer(mu_i, mu_j) @ inv(S_j)
    sm = np.outer(mu_i, mu_j @ inv(Sig_j)) / (1 + mu_j @ inv(Sig_j) @ mu_j)
    report("Sherman-Morrison form of M*", norm(Mstar - sm), 1e-12)
    report("rank(M*) - 1", float(matrix_rank(Mstar, tol=1e-10) - 1), 0.0)
    grad = -W @ (np.outer(mu_i, mu_j) - Mstar @ S_j)
    report("grad h(M*) = 0", norm(grad), 1e-12)
    D = RNG.standard_normal((K, K))
    quad = h_of(Mstar + D) - h_of(Mstar) - 0.5 * np.trace(D.T @ W @ D @ S_j)
    report("h(M*+D) - h(M*) = 1/2|W^1/2 D S^1/2|^2 (strong convexity identity)", abs(quad), 1e-11)
    # correlated recognition: stationary matrix is the second-moment regression, can be invertible
    Mreg = (np.outer(mu_i, mu_j) + Sig_ij) @ inv(S_j)
    gradc = -W @ (np.outer(mu_i, mu_j) + Sig_ij - Mreg @ S_j)
    report("correlated recognition: grad at E[k_i k_j^T] E[k_j k_j^T]^-1 = 0", norm(gradc), 1e-12)
    info("correlated recognition", f"rank of regression matrix = {matrix_rank(Mreg)} (K = {K})")

    print("\n== C5b chart closure and fold-point stationary generators (K = 2) ==")
    J2 = np.array([[0.0, -1.0], [1.0, 0.0]])

    def setup(mi, mj, Sj, Wm):
        Sm = Sj + np.outer(mj, mj)
        hf = lambda Mm: 0.5 * (-2 * np.trace(Wm @ Mm @ np.outer(mj, mi)) + np.trace(Mm.T @ Wm @ Mm @ Sm))
        gh = lambda Mm: -Wm @ (np.outer(mi, mj) - Mm @ Sm)
        psi = lambda om: hf(expm(om.reshape(2, 2)))
        gpsi = lambda om: L_block(om.reshape(2, 2).T, gh(expm(om.reshape(2, 2)))).ravel()
        return hf, gh, psi, gpsi, np.outer(mi, mj) @ inv(Sm)

    # (i) aligned witness: mu_i = mu_j = e1, Sigma_j = I, W = I, om = -log3 I + 2 pi J
    hf, gh, psi, gpsi, Ms = setup(np.array([1.0, 0.0]), np.array([1.0, 0.0]), np.eye(2), np.eye(2))
    om_w = (-np.log(3.0) * np.eye(2) + 2 * np.pi * J2).ravel()
    report("witness: exp(om_w) = I/3", norm(expm(om_w.reshape(2, 2)) - np.eye(2) / 3), 1e-12)
    report("witness: grad psi(om_w) via L formula", norm(gpsi(om_w)), 1e-12)
    gfd = np.array([(psi(om_w + 1e-6 * e) - psi(om_w - 1e-6 * e)) / 2e-6 for e in np.eye(4)])
    report("witness: grad psi(om_w) via FD", norm(gfd), 1e-8)
    Lmat = np.stack([L_block(om_w.reshape(2, 2), e.reshape(2, 2)).ravel() for e in np.eye(4)], axis=1)
    sv = svd(Lmat, compute_uv=False)
    info("witness: singular values of L(om_w, .)", np.array2string(sv, precision=3))
    Hpsi = np.stack([(gpsi(om_w + 1e-5 * e) - gpsi(om_w - 1e-5 * e)) / 2e-5 for e in np.eye(4)], axis=1)
    info("witness: Hessian eigenvalues of psi at om_w (observation only)",
         np.array2string(eigvalsh(0.5 * (Hpsi + Hpsi.T)), precision=4))
    info("witness: h(I/3) - h(M*)", f"{hf(np.eye(2) / 3) - hf(Ms):.6f} (M* = diag{np.diag(Ms)})")
    # aligned case: chart sequence P diag(tau, eps) P^-1 -> M*, with real logarithms
    tau = np.trace(Ms)
    for eps in (1e-2, 1e-4, 1e-6):
        evals, P = np.linalg.eig(Ms)
        order = np.argsort(-evals.real)
        P = P[:, order].real
        Me = P @ np.diag([tau, eps]) @ inv(P)
        lg = logm(Me)
        info(f"aligned chart sequence eps={eps:g}",
             f"|Me - M*| = {norm(Me - Ms):.1e}, |expm(logm Me) - Me| = {norm(expm(lg.real) - Me):.1e}, "
             f"max |Im logm| = {np.max(np.abs(np.imag(lg))):.1e}")
    # aligned case: random-start minimization of psi: values approach h(M*) from above, links -> M*
    best = []
    for _ in range(40):
        r = minimize(psi, 0.8 * RNG.standard_normal(4), jac=gpsi, method="BFGS", options={"gtol": 1e-12, "maxiter": 4000})
        best.append((r.fun, det(expm(r.x.reshape(2, 2)))))
    bf = min(best)
    info("aligned case: min over 40 BFGS runs of psi - h(M*)", f"{bf[0] - hf(Ms):.3e}, det(link) = {bf[1]:.3e}")
    # (ii) anti-aligned case: mu_i = -e1, mu_j = e1, Sigma_j = I, W = I: tr M* < 0
    hf, gh, psi, gpsi, Ms = setup(np.array([-1.0, 0.0]), np.array([1.0, 0.0]), np.eye(2), np.eye(2))
    info("anti-aligned case", f"M* = {Ms.ravel()}, tr M* = {np.trace(Ms):.3f}")
    om_f = (np.log(1.0 / 3.0) * np.eye(2) + np.pi * J2).ravel()
    report("anti-aligned fold point om = log(1/3) I + pi J: exp = -I/3", norm(expm(om_f.reshape(2, 2)) + np.eye(2) / 3), 1e-12)
    report("anti-aligned fold point is stationary (L formula)", norm(gpsi(om_f)), 1e-12)
    vals = []
    for _ in range(200):
        r = minimize(psi, 1.5 * RNG.standard_normal(4), jac=gpsi, method="BFGS", options={"gtol": 1e-12, "maxiter": 4000})
        vals.append((r.fun, r.x))
    vbest, xbest = min(vals, key=lambda t: t[0])
    Lbest = expm(xbest.reshape(2, 2))
    info("anti-aligned: inf over chart links (200 BFGS runs) - h(M*)",
         f"{vbest - hf(Ms):.6f}; h(-I/3) - h(M*) = {hf(-np.eye(2) / 3) - hf(Ms):.6f}; "
         f"best link eigenvalues {np.linalg.eigvals(Lbest)}, det {det(Lbest):.4f}")
    def M_jordan(p):
        lam, r, t = p
        a, b = np.array([np.cos(t), np.sin(t)]), np.array([-np.sin(t), np.cos(t)])
        return lam * np.eye(2) + r * np.outer(a, b)
    jb = min((minimize(lambda p: hf(M_jordan(p)), RNG.standard_normal(3)) for _ in range(30)), key=lambda r: r.fun)
    info("anti-aligned: min of h over double-eigenvalue Jordan matrices (not chart links) - h(M*)",
         f"{jb.fun - hf(Ms):.6f} at eigenvalue {jb.x[0]:.5f} (= -(2-sqrt2)/2 = {-(2 - np.sqrt(2)) / 2:.5f}); "
         f"coupling r = {jb.x[1]:.4f}")
    gap_exact = (3.0 - 2.0 * np.sqrt(2.0)) / 4.0
    report("anti-aligned: Jordan-family minimum of h - h(M*) equals (3-2sqrt2)/4 (notes derivation)",
           abs(jb.fun - hf(Ms) - gap_exact), 1e-8)
    report("anti-aligned: BFGS chart infimum - h(M*) lies in [(3-2sqrt2)/4, (3-2sqrt2)/4 + 1e-4]",
           0.0 if 0.0 <= (vbest - hf(Ms)) - gap_exact <= 1e-4 else (vbest - hf(Ms)) - gap_exact, 0.0,
           f"excess {(vbest - hf(Ms)) - gap_exact:.2e}, |omega| = {norm(xbest):.1f}")
    # K = 2 non-attainment proof, step used: lam I + t E is a chart link when disc(E) < 0 and lam < 0
    worst = 0.0
    for _ in range(200):
        E = RNG.standard_normal((2, 2))
        if (E[0, 0] - E[1, 1]) ** 2 + 4 * E[0, 1] * E[1, 0] >= 0:
            E = E + 3.0 * J2  # pushes the discriminant negative
        if (E[0, 0] - E[1, 1]) ** 2 + 4 * E[0, 1] * E[1, 0] >= 0:
            continue
        Mt = -RNG.uniform(0.1, 2.0) * np.eye(2) + 1e-3 * E
        X = logm(Mt)
        worst = max(worst, np.max(np.abs(np.imag(X))), norm(expm(np.real(X)) - Mt) / norm(Mt))
    report("lam I + t E with disc(E) < 0, lam < 0, has a real logarithm (max |Im logm|, rel. residual)", worst, 1e-9)
    # neighbourhood of M* contains no matrix with a real logarithm: simple negative eigenvalue persists
    worst_gap = np.inf
    for _ in range(2000):
        P = Ms + 0.05 * RNG.standard_normal((2, 2))
        ev = np.linalg.eigvals(P)
        neg_real = [e for e in ev if abs(e.imag) < 1e-12 and e.real < 0]
        worst_gap = min(worst_gap, len(neg_real))
    report("anti-aligned: every perturbation within 0.05 of M* keeps a real negative eigenvalue (min count - 1)",
           float(worst_gap - 1), 0.0)


# ---------------------------------------------------------------------------------
# Law-level energy: stabilizer invariance, Mahalanobis invariant, orbit Fisher form
# ---------------------------------------------------------------------------------
def kl_gauss(m1, S1, m2, S2):
    K = len(m1)
    S2i = inv(S2)
    d = m2 - m1
    return 0.5 * (np.trace(S2i @ S1) + d @ S2i @ d - K + slogdet(S2)[1] - slogdet(S1)[1])


def rot_about(axis: np.ndarray, angle: float) -> np.ndarray:
    a = axis / norm(axis)
    Kx = np.array([[0, -a[2], a[1]], [a[2], 0, -a[0]], [-a[1], a[0], 0]])
    return expm(angle * Kx)


def check_law_level() -> None:
    print("\n== C6 prop:link-law-level-energy (Gaussian, GL+(3)) ==")
    K = 3
    mi, Si = RNG.standard_normal(K), spd(K)
    mj, Sj = RNG.standard_normal(K), spd(K)
    Si_h, Sj_h = np.real(sqrtm(Si)), np.real(sqrtm(Sj))
    D = lambda Th: kl_gauss(mi, Si, Th @ mj, Th @ Sj @ Th.T)
    Th = expm(0.5 * RNG.standard_normal((K, K)))
    worst = 0.0
    for _ in range(50):
        h = Si_h @ rot_about(inv(Si_h) @ mi, RNG.uniform(0, 2 * np.pi)) @ inv(Si_h)
        hp = Sj_h @ rot_about(inv(Sj_h) @ mj, RNG.uniform(0, 2 * np.pi)) @ inv(Sj_h)
        assert det(h) > 0 and det(hp) > 0
        worst = max(worst, abs(D(h @ Th @ hp) - D(Th)))
    report("D_e(h Th h') = D_e(Th) for stabilizer elements (absolute)", worst, 1e-10,
           f"at D_e(Th) = {D(Th):.3f}")
    g = expm(RNG.standard_normal((K, K)))
    mah = lambda m, S: np.sqrt(m @ inv(S) @ m)
    report("Mahalanobis norm invariant under GL+", abs(mah(g @ mi, g @ Si @ g.T) - mah(mi, Si)), 1e-12)
    # exact transport when Mahalanobis norms agree
    mj2 = mj * mah(mi, Si) / mah(mj, Sj)
    wi, wj = inv(Si_h) @ mi, inv(Sj_h) @ mj2
    ax = np.cross(wj, wi)
    ang = np.arccos(np.clip(wi @ wj / (norm(wi) * norm(wj)), -1, 1))
    O = rot_about(ax, ang)
    Th0 = Si_h @ O @ inv(Sj_h)
    D2 = lambda Tt: kl_gauss(mi, Si, Tt @ mj2, Tt @ Sj @ Tt.T)
    report("exact transport Th0 = Si^1/2 O Sj^-1/2: D_e(Th0) = 0", abs(D2(Th0)), 1e-12)
    # Hessian along right-trivialized curves exp(t xi) Th0 vs Gaussian orbit Fisher form
    def kq(xi):
        Sh_i = inv(Si_h)
        eta = Sh_i @ xi @ Si_h
        sym = 0.5 * (eta + eta.T)
        return norm(Sh_i @ xi @ mi) ** 2 + 2 * norm(sym) ** 2
    worst = 0.0
    for _ in range(20):
        xi = RNG.standard_normal((K, K))
        t = 1e-4
        d2 = (D2(expm(t * xi) @ Th0) - 2 * D2(Th0) + D2(expm(-t * xi) @ Th0)) / t ** 2
        worst = max(worst, abs(d2 - kq(xi)) / kq(xi))
    report("Hessian of D_e at Th0 = orbit Fisher form k_q(xi,xi) (rel.)", worst, 1e-5)
    # kernel dimension of k_q on gl(3): (K-1)(K-2)/2 = 1 for mu != 0, 3 for mu = 0
    basis = [np.eye(K * K)[a].reshape(K, K) for a in range(K * K)]

    def gram_kq(m, S):
        Sh = np.real(sqrtm(S))
        Shi = inv(Sh)
        rows = []
        for X in basis:
            eta = Shi @ X @ Sh
            rows.append(np.concatenate([Shi @ X @ m, np.sqrt(2) * (0.5 * (eta + eta.T)).ravel()]))
        A = np.array(rows)
        return A @ A.T

    for (m, label, expect) in ((mi, "mu != 0", (K - 1) * (K - 2) // 2), (np.zeros(K), "mu = 0", K * (K - 1) // 2)):
        ev = eigvalsh(gram_kq(m, Si))
        nul = int(np.sum(ev < 1e-10 * ev.max()))
        report(f"kernel dim of k_q ({label}) - expected {expect}", float(nul - expect), 0.0)


# ---------------------------------------------------------------------------------
# Held-link limit on a scalar example
# ---------------------------------------------------------------------------------
def check_held_limit() -> None:
    print("\n== C7 thm:link-held-limit (G = GL+(1), two scalar agents, one success record) ==")
    alpha = 0.3
    p_cond = lambda om: (2.0 + np.exp(2 * om)) ** -0.5  # p(o | om), N(0,1) agents, energy (k_i - e^om k_j)^2/2
    # check p(o|om) by quadrature
    Z2, W2 = gh_grid(2, 60)
    om_t = 0.7
    pq = np.tensordot(W2, np.exp(-0.5 * (Z2[:, 0] - np.exp(om_t) * Z2[:, 1]) ** 2), axes=(0, 0))
    report("p(o|om) = (2 + e^{2 om})^{-1/2} by quadrature", abs(pq - p_cond(om_t)), 1e-12)
    z1, w1 = hermegauss(120)
    w1 = w1 / np.sqrt(2 * np.pi)
    errs = []
    for s in (0.4, 0.2, 0.1, 0.05, 0.025):
        ps = np.dot(w1, p_cond(alpha + s * z1))
        errs.append((s, abs(-np.log(ps) + np.log(p_cond(alpha)))))
    info("evidence: |log p_s(o) - log p(o|alpha)|", ", ".join(f"s={s}: {e:.2e}" for s, e in errs))
    rate = np.log(errs[-2][1] / errs[-1][1]) / np.log(2)
    report("evidence convergence rate ~ s^2 (exponent - 2)", abs(rate - 2), 0.05, f"exponent {rate:.3f}")

    # restricted matter class: product Gaussians N(m_i,v_i) x N(m_j,v_j)
    def kl1(m, v):
        return 0.5 * (v + m ** 2 - 1 - np.log(v))

    def f_held(om, q):  # held-link free energy at link e^om, product Gaussian q = (mi, mj, vi, vj)
        mi, mj, vi, vj = q
        M = np.exp(om)
        return kl1(mi, vi) + kl1(mj, vj) + 0.5 * ((mi - M * mj) ** 2 + vi + M ** 2 * vj)

    def F_star(om):
        M2 = np.exp(2 * om)
        return 0.5 * (0.5 - 1 + np.log(2)) + 0.5 * (1 / (1 + M2) - 1 + np.log(1 + M2)) + 0.5 * (0.5 + M2 / (1 + M2))

    r = minimize(lambda p: f_held(alpha, (p[0], p[1], np.exp(p[2]), np.exp(p[3]))), np.zeros(4),
                 method="BFGS", options={"gtol": 1e-12})
    report("closed-form restricted held optimum F*(alpha) vs numeric", abs(r.fun - F_star(alpha)), 1e-9)

    def F_latent(p, s):  # R = N(mu, c), product with q; prior N(alpha, s^2)
        mu, logc, mi, mj, lvi, lvj = p
        c, vi, vj = np.exp(logc), np.exp(lvi), np.exp(lvj)
        EM, EM2 = np.exp(mu + c / 2), np.exp(2 * mu + 2 * c)
        matter = kl1(mi, vi) + kl1(mj, vj) + 0.5 * (mi ** 2 - 2 * mi * mj * EM + mj ** 2 * EM2 + vi + EM2 * vj)
        klR = 0.5 * (c / s ** 2 + (mu - alpha) ** 2 / s ** 2 - 1 + np.log(s ** 2 / c))
        return matter + klR, klR

    out = []
    for s in (0.4, 0.2, 0.1, 0.05, 0.025):
        best = None
        for start in range(6):
            p0 = np.array([alpha, np.log(s ** 2), 0.0, 0.0, np.log(0.5), np.log(0.5)]) + 0.1 * RNG.standard_normal(6) * (start > 0)
            rr = minimize(lambda p: F_latent(p, s)[0], p0, method="BFGS", options={"gtol": 1e-12, "maxiter": 10000})
            if best is None or rr.fun < best.fun:
                best = rr
        Fs, klR = F_latent(best.x, s)
        out.append((s, Fs - F_star(alpha), best.x[0] - alpha, np.exp(best.x[1]), klR))
    for s, gap, dmu, c, klR in out:
        info(f"restricted latent optimum s={s}",
             f"inf F_s - F*(alpha) = {gap:+.3e}, mu - alpha = {dmu:+.2e}, var(R) = {c:.2e}, KL(R||prior) = {klR:.2e}")
    report("restricted infimum converges to F*(alpha) (|gap| at s=0.025)", abs(out[-1][1]), 1e-3)
    report("near-minimizing R concentrates: KL(R||prior) at s=0.025", out[-1][4], 1e-3)


# ---------------------------------------------------------------------------------
# Induced action of undirected Gaussian matter; directed matter induces none
# ---------------------------------------------------------------------------------
def check_induced_action() -> None:
    print("\n== C8 prop:link-induced-action ==")
    lam0, w = 1.3, 0.8
    edges = [(0, 1), (1, 2), (2, 0)]  # e: j -> i written (i, j)

    def Jmat(om):
        Jm = lam0 * np.eye(3)
        for (i, j), o in zip(edges, om):
            v = np.zeros(3)
            v[i], v[j] = 1.0, -np.exp(o)
            Jm += w * np.outer(v, v)
        return Jm

    from scipy.integrate import nquad
    worst = 0.0
    vals = []
    for _ in range(3):
        om = 0.6 * RNG.standard_normal(3)
        Jm = Jmat(om)
        lim = 9.0 / np.sqrt(np.min(np.diag(Jm)))
        Zq, _ = nquad(lambda a, b, c: np.exp(-0.5 * np.array([a, b, c]) @ Jm @ np.array([a, b, c])),
                      [[-lim, lim]] * 3, opts={"epsabs": 1e-13, "epsrel": 1e-11})
        Zc = (2 * np.pi) ** 1.5 * det(Jm) ** -0.5
        worst = max(worst, abs(Zq - Zc) / Zc)
        vals.append((-np.log(Zq), 0.5 * slogdet(Jm)[1] - 1.5 * np.log(2 * np.pi)))
    report("undirected Gaussian matter normalizer by nested adaptive quadrature = (2pi)^{3/2} det J^{-1/2} (rel.)", worst, 1e-8)
    diffs = [abs((a1 - a2) - (b1 - b2)) for (a1, b1), (a2, b2) in zip(vals[:-1], vals[1:])]
    report("induced action S_ind = 1/2 log det J + const (differences)", max(diffs), 1e-8)
    # directed counterpart: k_j ~ N(0,1), k_i | k_j ~ N(e^om k_j, 1/w): integrates to one for every om
    Z2, W2 = gh_grid(2, 60)
    worst = 0.0
    for o in (-1.0, 0.0, 1.2):
        # int N(k_i; e^o k_j, 1/w) dk_i = 1: quadrature over k_i in standardized form
        ki = np.exp(o) * Z2[:, 1] + Z2[:, 0] / np.sqrt(w)
        dens = np.sqrt(w / (2 * np.pi)) * np.exp(-0.5 * w * (ki - np.exp(o) * Z2[:, 1]) ** 2)
        mass = np.dot(W2, dens / (np.sqrt(w) * np.exp(-0.5 * Z2[:, 0] ** 2) / np.sqrt(2 * np.pi)))
        worst = max(worst, abs(mass - 1.0))
    report("directed matter: conditional normalizer is one for every link", worst, 1e-12)
    # integrability witness: psi_12 = exp(Theta k1 k2) with N(0,1) self potentials
    th = 0.6
    Z = np.dot(W2, np.exp(th * Z2[:, 0] * Z2[:, 1]))
    report("Z(Theta) = (1 - Theta^2)^{-1/2} for Theta = 0.6", abs(Z - (1 - th ** 2) ** -0.5), 1e-10)
    info("integrability witness", "for Theta >= 1 the integral diverges (prop:gen-gibbs-counterexample), "
         "a set of positive Gaussian prior mass for Theta = e^om")
    # Monte Carlo of the generator marginal of the joint undirected latent model, one link varying
    om_grid = np.linspace(-9, 9, 4001)
    dens_marg = np.array([np.exp(-0.5 * o ** 2) * det(Jmat([o, 0.2, -0.1])) ** -0.5 for o in om_grid])
    n = 400_000
    oms = RNG.standard_normal(n)
    # importance weights det J^{-1/2} on the prior samples
    wts = np.array([det(Jmat([o, 0.2, -0.1])) ** -0.5 for o in oms[:100000]])
    m_imp = np.sum(wts * oms[:100000]) / np.sum(wts)
    se = np.sqrt(np.sum(wts ** 2 * (oms[:100000] - m_imp) ** 2)) / np.sum(wts)
    m_grid = np.trapezoid(om_grid * dens_marg, om_grid) / np.trapezoid(dens_marg, om_grid)
    z = abs(m_imp - m_grid) / se
    report("generator marginal of the joint undirected model: mean by prior sampling with weights det J^{-1/2} vs grid (|z| < 4)",
           max(z - 4.0, 0.0), 0.0, f"{m_imp:.4f} vs {m_grid:.4f}, |z| = {z:.2f}")


# ---------------------------------------------------------------------------------
# Conditional transfer: a held-link property that fails for the link-marginal law
# ---------------------------------------------------------------------------------
def check_transfer() -> None:
    print("\n== C10 prop:link-conditional-transfer(c): mixtures are not held-link laws ==")
    e = np.e
    kurt_exact = 3 * (1 + 2 * e ** 2 + e ** 8) / (1 + e ** 2) ** 2
    n = 4_000_000
    om = RNG.standard_normal(n)
    kj = RNG.standard_normal(n)
    ki = np.exp(om) * kj + RNG.standard_normal(n)
    info("kurtosis of k_i under the latent-link law", f"exact {kurt_exact:.2f} (Gaussian 3); "
         f"Monte Carlo {np.mean(ki ** 4) / np.mean(ki ** 2) ** 2:.2f} (heavy tails, slow MC)")
    report("kurtosis exceeds the Gaussian value 3 (exact formula)", max(3.0 - kurt_exact, 0.0), 0.0)
    # determinant hyperplane: |det exp(om)| = e^{tr om}
    B = RNG.standard_normal((3, 3))
    report("det exp(B) = exp(tr B)", abs(det(expm(B)) - np.exp(np.trace(B))), 1e-12)


def check_decomposition_and_moments() -> None:
    print("\n== C11 prop:link-latent-normalization(c) and lem:link-growth(a) ==")
    alpha, s = 0.3, 0.5
    mu_R, c_R = 0.1, 0.2
    mq = np.array([0.2, -0.1])
    vq = np.array([0.6, 0.4])
    Z3, W3 = gh_grid(3, 50)
    # nodes for Q = R x N(mq, diag vq)
    om = mu_R + np.sqrt(c_R) * Z3[:, 0]
    ki = mq[0] + np.sqrt(vq[0]) * Z3[:, 1]
    kj = mq[1] + np.sqrt(vq[1]) * Z3[:, 2]
    E = 0.5 * (ki - np.exp(om) * kj) ** 2
    lognorm = lambda x, m, v: -0.5 * (x - m) ** 2 / v - 0.5 * np.log(2 * np.pi * v)
    logq = lognorm(om, mu_R, c_R) + lognorm(ki, mq[0], vq[0]) + lognorm(kj, mq[1], vq[1])
    logjoint = lognorm(om, alpha, s ** 2) + lognorm(ki, 0, 1) + lognorm(kj, 0, 1) - E
    z1, w1 = hermegauss(150)
    w1 = w1 / np.sqrt(2 * np.pi)
    p_o = np.dot(w1, (2.0 + np.exp(2 * (alpha + s * z1))) ** -0.5)
    F_def = np.dot(W3, logq - logjoint)  # = -log p(o) + KL(Q || posterior), classical split
    klR = 0.5 * (c_R / s ** 2 + (mu_R - alpha) ** 2 / s ** 2 - 1 + np.log(s ** 2 / c_R))
    kl1 = lambda m, v: 0.5 * (v + m ** 2 - 1 - np.log(v))
    z2, w2 = hermegauss(150)
    w2 = w2 / np.sqrt(2 * np.pi)
    omn = mu_R + np.sqrt(c_R) * z2
    F_held = kl1(mq[0], vq[0]) + kl1(mq[1], vq[1]) + 0.5 * ((mq[0] - np.exp(omn) * mq[1]) ** 2 + vq[0] + np.exp(2 * omn) * vq[1])
    F_dec = klR + np.dot(w2, F_held)
    report("decomposition F = KL(R||prior) + E_R F_held (scalar model)", abs(F_def - F_dec), 1e-10)
    report("F >= -log p(o)", max(-np.log(p_o) - F_def, 0.0), 0.0, f"F = {F_def:.6f}, -log p(o) = {-np.log(p_o):.6f}")
    # exponential moment bound E e^{c|x|} <= e^{c|m|} (2 e^{c^2 |C|/2})^D
    D = 3
    m = RNG.standard_normal(D)
    Cm = spd(D, 0.5)
    X = m + RNG.standard_normal((1_000_000, D)) @ np.linalg.cholesky(Cm).T
    for cc in (0.5, 1.0, 2.0):
        lhs = np.mean(np.exp(cc * norm(X, axis=1)))
        rhs = np.exp(cc * norm(m)) * (2 * np.exp(cc ** 2 * opnorm(Cm) / 2)) ** D
        report(f"exponential moment bound, c = {cc} (lhs/rhs - 1 <= 0)", max(lhs / rhs - 1, 0.0), 0.0, f"ratio {lhs / rhs:.3e}")


def observe_branch_minima() -> None:
    r"""Observation only (no PASS/FAIL): local minimizers of the point-limit objective
    V(om) = |om|^2/(2 sigma^2) + l(exp om), l(M) = 1/2 E|k_i - M k_j|^2, for GL+(2), product
    recognition, mu_i = -e1, mu_j = e1, Sigma_j = W = I (anti-aligned case), anchor 0,
    prior covariance sigma^2 I.  Distinct limits with positive-definite Hessians are numerical
    evidence of non-global local minima on different branches of the matrix logarithm."""
    print("\n== C12 observation: branch minima of V (anti-aligned, GL+(2)) ==")
    rng = np.random.default_rng(7)
    mu_i, mu_j = np.array([-1.0, 0.0]), np.array([1.0, 0.0])
    S2 = np.eye(2) + np.outer(mu_j, mu_j)
    C2 = np.outer(mu_i, mu_j)

    def V_and_grad(x: np.ndarray, sigma: float) -> tuple[float, np.ndarray]:
        om = x.reshape(2, 2)
        M = expm(om)
        val = 0.5 * np.sum(om ** 2) / sigma ** 2 + 0.5 * np.trace(M @ S2 @ M.T) - np.trace(M.T @ C2)
        return val, (om / sigma ** 2 + L_block(om.T, M @ S2 - C2)).ravel()

    for sigma in (3.0, 10.0):
        sols = []
        for _ in range(200):
            x0 = rng.standard_normal(4) * rng.choice([0.5, 2.0, 6.0])
            r = minimize(V_and_grad, x0, args=(sigma,), jac=True, method="BFGS",
                         options={"gtol": 1e-10, "maxiter": 20000})
            if norm(r.jac) < 1e-7:
                H = np.stack([(V_and_grad(r.x + 1e-5 * e, sigma)[1] - V_and_grad(r.x - 1e-5 * e, sigma)[1]) / 2e-5
                              for e in np.eye(4)], axis=1)
                sols.append((round(float(r.fun), 7), float(eigvalsh(0.5 * (H + H.T)).min()), r.x))
        vals = sorted({s[0] for s in sols if s[1] > 1e-8})
        info(f"sigma = {sigma}", f"{len(sols)} converged runs; distinct local-minimum values {vals}")
        for v in vals:
            x = next(s[2] for s in sols if s[0] == v)
            info(f"   V = {v:.7f}", f"eig(om) = {np.round(np.linalg.eigvals(x.reshape(2, 2)), 4)}, "
                 f"eig(link) = {np.round(np.linalg.eigvals(expm(x.reshape(2, 2))), 4)}, |om| = {norm(x):.3f}")


def main() -> None:
    check_exp_derivative()
    check_gaussian_gradients()
    check_field_equation()
    check_loop_defect()
    check_gaussian_kl()
    check_delta_rule_and_prior()
    check_law_level()
    check_held_limit()
    check_induced_action()
    check_transfer()
    check_decomposition_and_moments()
    observe_branch_minima()
    print("\n== Summary ==")
    n_ok = sum(ok for _, _, ok in RESULTS)
    print(f"{n_ok}/{len(RESULTS)} checks passed")
    for name, txt, ok in RESULTS:
        if not ok:
            print(f"FAILED: {name}: {txt}")


if __name__ == "__main__":
    main()
