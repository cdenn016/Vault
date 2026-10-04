"""Numerical probes for verify_V1 (float64, CPU). They validate explicit witnesses and
closed forms reconstructed by hand; no verdict rests on them."""
from __future__ import annotations

import itertools
import math

import numpy as np
import sympy as sp
from scipy.linalg import expm, logm

rng = np.random.default_rng(20261004)
out: list[str] = []


def log(s: str) -> None:
    print(s)
    out.append(s)


def comm(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return a @ b - b @ a


# ---------------------------------------------------------------- 1. BCH through third order
log("== 1. BCH third-order coefficients and remainder scaling (eq:link-bch-third)")
K = 3
X0 = rng.standard_normal((K, K))
Y0 = rng.standard_normal((K, K))
X0 /= np.linalg.norm(X0, 2)
Y0 /= np.linalg.norm(Y0, 2)
for s in [0.2, 0.1, 0.05, 0.025]:
    X = s * X0
    Y = s * Y0
    L = logm(expm(X) @ expm(Y)).real
    bch3 = X + Y + 0.5 * comm(X, Y) + (comm(X, comm(X, Y)) + comm(Y, comm(Y, X))) / 12.0
    bch2 = X + Y + 0.5 * comm(X, Y)
    r3 = np.linalg.norm(L - bch3, 2)
    r2 = np.linalg.norm(L - bch2, 2)
    log(f"  s={s:6.3f}  |Log-BCH3|={r3:.3e}  |Log-BCH3|/s^4={r3/s**4:.4f}  |Log-BCH2|/s^3={r2/s**3:.4f}")

# Taylor coefficients b_l of -log(2-e^u) and c_3 = sum_{l>=4} b_l 2^{4-l}
u = sp.symbols("u")
ser = sp.series(-sp.log(2 - sp.exp(u)), u, 0, 40).removeO()
b = [float(ser.coeff(u, l)) for l in range(40)]
c3 = sum(b[l] * 2.0 ** (4 - l) for l in range(4, 40))
log(f"  b_1..b_5 = {[round(x,6) for x in b[1:6]]};  c_3 (truncated at l=39) = {c3:.6f}")
# check |BCH_{>=4}| <= c3 (|X|+|Y|)^4 on random pairs with |X|+|Y| <= 1/2
worst = 0.0
for _ in range(300):
    A = rng.standard_normal((K, K))
    B = rng.standard_normal((K, K))
    A /= np.linalg.norm(A, 2)
    B /= np.linalg.norm(B, 2)
    a = rng.uniform(0, 0.5)
    bb = rng.uniform(0, 0.5 - a)
    X = a * A
    Y = bb * B
    L = logm(expm(X) @ expm(Y)).real
    bch3 = X + Y + 0.5 * comm(X, Y) + (comm(X, comm(X, Y)) + comm(Y, comm(Y, X))) / 12.0
    ratio = np.linalg.norm(L - bch3, 2) / max((a + bb) ** 4, 1e-300)
    worst = max(worst, ratio)
log(f"  max over 300 pairs of |BCH_>=4|/(|X|+|Y|)^4 = {worst:.4f}  (bound c_3 = {c3:.4f})")
log(f"  -log(2-e^(1/2)) = {-math.log(2-math.exp(0.5)):.4f} < pi/2 = {math.pi/2:.4f}")

# ---------------------------------------------------------------- 2. cumulant forms, exact Gaussian moments
log("== 2. Cumulant forms kappa_3, kappa_4 of def:link-coarse-generator, exact Isserlis computation")


def gaussian_expect(poly: sp.Expr, zs: list[sp.Symbol]) -> sp.Rational:
    """E[poly(z)] for iid standard normal z (Isserlis on monomials)."""
    P = sp.Poly(sp.expand(poly), *zs)
    total = sp.Integer(0)
    for monom, coeff in P.terms():
        val = sp.Integer(1)
        for k in monom:
            if k % 2 == 1:
                val = sp.Integer(0)
                break
            val *= sp.factorial2(k - 1) if k > 0 else 1
        total += coeff * val
    return sp.nsimplify(total)


def joint_cumulant(vars_: list[sp.Expr], zs: list[sp.Symbol]) -> sp.Expr:
    """Joint cumulant cum(X_1,...,X_n) via the moment-cumulant (partition) formula."""
    n = len(vars_)
    idx = list(range(n))

    def partitions(items):
        if not items:
            yield []
            return
        first = items[0]
        for smaller in partitions(items[1:]):
            for i, block in enumerate(smaller):
                yield smaller[:i] + [[first] + block] + smaller[i + 1:]
            yield [[first]] + smaller

    total = sp.Integer(0)
    for part in partitions(idx):
        k = len(part)
        term = sp.Integer((-1) ** (k - 1) * math.factorial(k - 1))
        for block in part:
            term *= gaussian_expect(sp.Mul(*[vars_[i] for i in block]), zs)
        total += term
    return sp.nsimplify(total)


def mat(sym_entries):
    return sp.Matrix(2, 2, sym_entries)


def brk(a, b):
    return a * b - b * a


def frob(a, b):
    return (a.T * b).trace()


z = sp.symbols("z1:9")
zeta1 = mat(z[0:4])  # zeta_{e'} with iid N(0,1) entries (Lambda_{e'} = Id)
# Instance A: unit precisions, centered, upsilon = E_12
ups = sp.Matrix([[0, 1], [0, 0]])
zeta2 = mat(z[4:8])
chi1, chi2 = zeta1, zeta2  # centered
psi1 = frob(ups, chi1 + chi2)
psi2 = sp.Rational(1, 2) * frob(ups, brk(chi1, chi2))
psi3 = sp.Rational(1, 12) * frob(ups, brk(chi1, brk(chi1, chi2)) + brk(chi2, brk(chi2, chi1)))
zs = list(z)
c1122 = joint_cumulant([psi1, psi1, psi2, psi2], zs)
c1113 = joint_cumulant([psi1, psi1, psi1, psi3], zs)
c1112 = joint_cumulant([psi1, psi1, psi1, psi2], zs)
c112 = joint_cumulant([psi1, psi1, psi2], zs)
tau2_coeff = 6 * c1122 + 4 * c1113
log(f"  Instance A (unit precisions, upsilon=E12): cum(1,1,2,2)={c1122}, cum(1,1,1,3)={c1113}, "
    f"cum(1,1,1,2)={c1112}, cum(1,1,2)={c112}")
log(f"    tau^2 coefficient 6cum(1,1,2,2)+4cum(1,1,1,3) = {tau2_coeff}  (manuscript: kappa_4 = 12)")
# direct kappa_4 formula
ups1 = ups  # Lambda^{-1} upsilon with Lambda = Id
ups2 = ups
k4_direct = (3 * gaussian_expect(frob(ups, brk(ups1, zeta2)) ** 2, zs)
             + 3 * gaussian_expect(frob(ups, brk(zeta1, ups2)) ** 2, zs)
             + 2 * frob(ups, brk(ups1, brk(ups1, ups2)) + brk(ups2, brk(ups2, ups1))))
log(f"    kappa_4 by its displayed formula = {sp.nsimplify(k4_direct)}")

# Instance B: Lambda_{e'} = Id, Lambda_e^{-1} = Id + P_{E12}, upsilon = E11 + E12, kappa_3 = 1
ups_b = sp.Matrix([[1, 1], [0, 0]])
u0 = sp.Matrix([[0, 1], [0, 0]])
# zeta_e = L b with L = (Id + P)^{1/2} = Id + (sqrt2 - 1) P,  P = projection onto line of u0
bmat = mat(z[4:8])
Pb = frob(u0, bmat) / frob(u0, u0) * u0
zeta2b = bmat + (sp.sqrt(2) - 1) * Pb
# covariance check: E[<a,zeta2b><c,zeta2b>] = <a,(Id+P)c>
a_t = sp.Matrix([[1, 2], [3, 4]])
c_t = sp.Matrix([[-1, 0], [2, 5]])
cov_lhs = gaussian_expect(frob(a_t, zeta2b) * frob(c_t, zeta2b), zs)
cov_rhs = frob(a_t, c_t) + frob(u0, a_t) * frob(u0, c_t) / frob(u0, u0)
log(f"  Instance B covariance check: E[<a,z><c,z>]={sp.nsimplify(sp.expand(cov_lhs))} vs <a,(Id+P)c>={cov_rhs}")
psi2b = sp.Rational(1, 2) * frob(ups_b, brk(zeta1, zeta2b))
psi1b = frob(ups_b, zeta1 + zeta2b)
c112b = joint_cumulant([psi1b, psi1b, psi2b], zs)
ups_e_b = ups_b + frob(u0, ups_b) / frob(u0, u0) * u0  # Lambda_e^{-1} upsilon
k3_direct = frob(ups_b, brk(ups_b, ups_e_b))
log(f"  Instance B: cum(1,1,2) = {sp.nsimplify(sp.expand(c112b))};  kappa_3 by formula = {k3_direct}  "
    f"(upsilon_e = {list(ups_e_b)})")

# ---------------------------------------------------------------- 3. Monte Carlo of the actual principal log
log("== 3. Monte Carlo: cum_4 of tau^{-1}<E12, Log(e^{tau chi1} e^{tau chi2})> (instance A, event-restricted)")


def opnorm2(M: np.ndarray) -> np.ndarray:
    # largest singular value of a batch of 2x2 matrices
    a, b_, c, d = M[:, 0, 0], M[:, 0, 1], M[:, 1, 0], M[:, 1, 1]
    s1 = a * a + b_ * b_ + c * c + d * d
    det = a * d - b_ * c
    disc = np.sqrt(np.maximum(s1 * s1 - 4 * det * det, 0.0))
    return np.sqrt(0.5 * (s1 + disc))


def expm2(M: np.ndarray) -> np.ndarray:
    # scaling and squaring with Taylor degree 12 (batch of 2x2)
    n = M.shape[0]
    nrm = opnorm2(M)
    s = np.maximum(0, np.ceil(np.log2(np.maximum(nrm, 1e-16) / 0.25))).astype(int)
    A = M / (2.0 ** s)[:, None, None]
    E = np.broadcast_to(np.eye(2), (n, 2, 2)).copy()
    term = E.copy()
    for k in range(1, 13):
        term = term @ A / k
        E = E + term
    smax = int(s.max())
    for _ in range(smax):
        mask = s > 0
        E[mask] = E[mask] @ E[mask]
        s = s - 1
    return E


def logm2(A: np.ndarray) -> np.ndarray:
    # principal log of a batch of 2x2 real matrices via eigenvalues (Cayley-Hamilton), complex arithmetic
    a, b_, c, d = A[:, 0, 0], A[:, 0, 1], A[:, 1, 0], A[:, 1, 1]
    tr = a + d
    det = a * d - b_ * c
    disc = (tr * tr / 4 - det).astype(complex)
    sq = np.sqrt(disc)
    l1 = tr / 2 + sq
    l2 = tr / 2 - sq
    L1 = np.log(l1)
    L2 = np.log(l2)
    I = np.broadcast_to(np.eye(2), A.shape)
    diff = l2 - l1
    small = np.abs(diff) < 1e-9
    alpha = np.where(small, L1 - l1 * (1 / l1), (l2 * L1 - l1 * L2) / np.where(small, 1, diff))
    beta = np.where(small, 1 / l1, (L2 - L1) / np.where(small, 1, diff))
    return (alpha[:, None, None] * I + beta[:, None, None] * A).real


def k_stats(x: np.ndarray):
    m = x.mean()
    y = x - m
    m2 = (y ** 2).mean()
    m3 = (y ** 3).mean()
    m4 = (y ** 4).mean()
    return m2, m3, m4 - 3 * m2 * m2


ups_np = np.array([[0.0, 1.0], [0.0, 0.0]])
for tau in [0.2, 0.1]:
    N = 4_000_000
    chunk = 500_000
    vals = []
    nev = 0
    for _ in range(N // chunk):
        chi1 = rng.standard_normal((chunk, 2, 2))
        chi2 = rng.standard_normal((chunk, 2, 2))
        w1 = tau * chi1
        w2 = tau * chi2
        event = (opnorm2(w1) + opnorm2(w2)) <= 0.5
        nev += int(event.sum())
        A = expm2(w1) @ expm2(w2)
        Lg = logm2(A)
        poly = (np.einsum("ij,nij->n", ups_np, chi1 + chi2)
                + 0.5 * tau * np.einsum("ij,nij->n", ups_np, chi1 @ chi2 - chi2 @ chi1)
                + tau ** 2 / 12 * np.einsum("ij,nij->n", ups_np,
                                             (chi1 @ (chi1 @ chi2 - chi2 @ chi1) - (chi1 @ chi2 - chi2 @ chi1) @ chi1)
                                             + (chi2 @ (chi2 @ chi1 - chi1 @ chi2) - (chi2 @ chi1 - chi1 @ chi2) @ chi2)))
        full = np.einsum("ij,nij->n", ups_np, Lg) / tau
        psi = np.where(event, full, poly)
        vals.append(psi)
    psi = np.concatenate(vals)
    m2, k3, k4 = k_stats(psi)
    log(f"  tau={tau}: event prob={nev/N:.4f}, var={m2:.4f} (psi_1 var 2), cum_3={k3:.4f}, "
        f"cum_4={k4:.4f}, 12 tau^2={12*tau**2:.4f}, cum_4/tau^2={k4/tau**2:.3f}  (MC std ~ {math.sqrt(384/N):.4f})")

# ---------------------------------------------------------------- 4. loop-defect remainder bound (prop:link-loop-defect(e))
log("== 4. eq:link-defect-expansion remainder on random generators, G^fib random SPD, K=3, r=3")
Gf = rng.standard_normal((3, 3))
Gf = Gf @ Gf.T + 0.5 * np.eye(3)
Gi = np.linalg.inv(Gf)


def gnorm2(H: np.ndarray) -> float:
    return float(np.trace(Gi @ H.T @ Gf @ H))


worst_ratio = 0.0
for _ in range(2000):
    Om = [rng.standard_normal((3, 3)) for _ in range(3)]
    scale = rng.uniform(0.01, 1.0)
    Om = [scale * o / math.sqrt(gnorm2(o)) * rng.uniform(0.1, 1.0) for o in Om]
    vs = sum(math.sqrt(gnorm2(o)) for o in Om)
    if vs > 1.0:
        continue
    hol = expm(Om[0]) @ expm(Om[1]) @ expm(Om[2])
    Q = 0.5 * gnorm2(np.eye(3) - hol)
    quad = 0.5 * gnorm2(sum(Om))
    rhs = vs * (math.exp(vs) - 1 - vs) + 0.5 * (math.exp(vs) - 1 - vs) ** 2
    assert abs(Q - quad) <= rhs * (1 + 1e-9) + 1e-14, (Q, quad, rhs)
    worst_ratio = max(worst_ratio, abs(Q - quad) / (2.3 * vs ** 3))
log(f"  all 2000 samples satisfy the displayed bound; max |Q - quad|/(2.3 vs^3) = {worst_ratio:.4f}")
log(f"  e/2 + e^2/8 = {math.e/2 + math.e**2/8:.5f} < 2.3")

# ---------------------------------------------------------------- 5. explicit matrix witnesses
log("== 5. explicit witnesses")
J = np.array([[0.0, -1.0], [1.0, 0.0]])  # E_21 - E_12
hol = expm(np.diag([0.0, math.log(2.0)])) @ expm(math.pi * J) @ expm(np.zeros((2, 2)))
log(f"  prop:link-chart-image(e) triangle: diag(0,log2), pi(E21-E12), 0 -> {np.round(hol, 12).tolist()}")
Kx = 4
M = expm(np.block([[math.pi * J, np.zeros((2, 2))], [np.zeros((2, 2)), np.zeros((2, 2))]])) @ expm(
    np.diag([0.0, math.log(2), math.log(3), math.log(4)]))
log(f"  prop:link-coarse-generator-law(ii) K=4 witness eigenvalues: {np.round(np.linalg.eigvals(M).real, 10).tolist()}")
Rz = expm(math.pi / 2 * np.array([[0, -1, 0], [1, 0, 0], [0, 0, 0]], float))
Rx = expm(math.pi / 2 * np.array([[0, 0, 0], [0, 0, -1], [0, 1, 0]], float))
P = Rz @ Rx
log(f"  running example Rz(pi/2)Rx(pi/2) = {np.round(P, 12).tolist()}, trace={np.trace(P):.6f}, "
    f"defect 3-Tr={3-np.trace(P):.6f}, (1,1,1) fixed: {np.allclose(P @ np.ones(3), np.ones(3))}")
C = math.pi / 2 * (np.array([[0, -1, 0], [1, 0, 0], [0, 0, 0]]) + np.array([[0, 0, 0], [0, 0, -1], [0, 1, 0]]))
log(f"  quadratic term 1/2|C|_F^2 = {0.5*np.sum(C*C):.6f} (pi^2/2={math.pi**2/2:.6f}); "
    f"varsigma = {2*math.sqrt(np.sum((math.pi/2*np.array([[0,-1,0],[1,0,0],[0,0,0]]))**2)):.6f} (pi sqrt2={math.pi*math.sqrt(2):.6f})")
# class-function blindness: conjugate a shear to near-identity with det>0 conjugators
T0 = np.array([[0, 1.0, 2.0], [0, 0, 3.0], [0, 0, 0]])
for t in [1.0, 0.1, 0.01]:
    S = np.diag([1.0, t, t * t])
    log(f"  shear conjugation t={t}: |S^-1 T0 S| = {np.linalg.norm(np.linalg.inv(S) @ T0 @ S, 2):.4e}")
# trace-form scale lemma: rank-one norms with G'' = 2 G' vs G'' not proportional
Gp = np.array([[2.0, 0.3], [0.3, 1.0]])
bvec = rng.standard_normal(2)
cvec = rng.standard_normal(2)
H = np.outer(bvec, cvec)


def tf(Gm, H):
    return math.sqrt(np.trace(np.linalg.inv(Gm) @ H.T @ Gm @ H))


log(f"  lem:link-trace-form-scale: |H|_G'={tf(Gp,H):.6f}, |H|_2G'={tf(2*Gp,H):.6f}, "
    f"|H|_G'+E11={tf(Gp+np.diag([1.0,0]),H):.6f}; rank-one formula={math.sqrt((bvec@Gp@bvec)*(cvec@np.linalg.inv(Gp)@cvec)):.6f}")
# Wilson identity on isometries: random G-isometry B = G^{-1/2} O G^{1/2}
w, V = np.linalg.eigh(Gf)
Gh = V @ np.diag(np.sqrt(w)) @ V.T
Ghi = np.linalg.inv(Gh)
O, _ = np.linalg.qr(rng.standard_normal((3, 3)))
B = Ghi @ O @ Gh
log(f"  prop:link-loop-defect(d): B^T G B = G? {np.allclose(B.T@Gf@B, Gf)}; "
    f"1/2|I-B|_G^2={0.5*gnorm2(np.eye(3)-B):.6f}, dimV - Tr B={3-np.trace(B):.6f}")

with open(r"C:\Users\CHRISA~1\AppData\Local\Temp\claude\C--Users-chris-and-christine-Desktop-VFE-3-0\4e2da218-3dfb-44f7-95ba-4761b2a9cb35\scratchpad\lie_links\verify_V1_checks_output.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(out) + "\n")
