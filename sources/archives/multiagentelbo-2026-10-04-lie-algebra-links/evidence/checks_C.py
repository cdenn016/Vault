#!/usr/bin/env python
r"""Float64 validation checks for frag_C_dynamics.tex (inference dynamics, link histories,
linearized link equation).  Validation of identities at small size only; nothing here is a
manuscript claim, and no finite computation is evidence for a general statement.

Run with:  C:/anaconda/python.exe checks_C.py  (NumPy/SciPy, CPU, one BLAS thread).

Sections
  A  Fisher metric of the Gaussian generator family in (mean, precision) coordinates.
  B  Natural-gradient flow (generators jointly with matter means): monotone free energy;
     explicit Euler step in natural parameters = Gaussian Bayesian learning rule (full and
     block-diagonal precision); mirror-descent bound for the BLR step; one-step exactness on a
     quadratic integrand.
  C  Exact M-coordinate of the anchor: no curvature, quadratic (translation) curvature, cosine
     (SO(2)) curvature; covariance M-step and the self-loop non-existence witness.
  D  Most probable histories: 1D double well (equation, monotonicity, rearrangement), time-like
     defect variant with gl(2) generators (exact gradient with the Frechet derivative, residual,
     leading-order bound).
  E  Linearized link equation on a triangle x three episodes, gl(2) generators, nontrivial fiber
     metric: gradient/Hessian at zero, O(source^2) agreement with the exact stationary history,
     both kinetic variants.
  F  Positivity of the operator K (run inside E: smallest eigenvalue of K against the anchor
     precision bound).
  Notation map to the fragment: Phi = S^hist (history action), H_e = W_a (record weight),
  Hol = rho(Theta^<-) (time-like holonomy), Z_n = backward functions Z^<-_n.
  G  Four-cycle held sheet: Hessian blocks of c08, invariant stationary-covariance slice of the
     Fisher natural gradient, common rate, equal channel residuals; contrast with supplied rates.
  H  History prior: backward-function (h-transform) kernels reproduce the Gibbs law; naive
     increment kernels do not.
  I  Time-like loop defect: quadratic expansion and the exponential-derivative mass tensor.
"""
import os

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")

import itertools  # noqa: E402

import numpy as np  # noqa: E402
from numpy.polynomial.hermite_e import hermegauss  # noqa: E402
from scipy.linalg import expm, expm_frechet  # noqa: E402
from scipy.optimize import minimize  # noqa: E402

np.set_printoptions(precision=5, linewidth=140)
RNG = np.random.default_rng(20261003)
RESULTS = []


def report(name, value, tol, cmp="le"):
    ok = bool(value <= tol) if cmp == "le" else bool(value >= tol)
    RESULTS.append((name, ok))
    sym = "<=" if cmp == "le" else ">="
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {value:.3e}  ({sym} {tol:.1e})")
    return ok


def header(s):
    print("\n" + "=" * 100 + "\n" + s + "\n" + "=" * 100)


# ----------------------------------------------------------------------------------------------
# generic helpers
# ----------------------------------------------------------------------------------------------
def gh_rule(d, n):
    """Tensor Gauss-Hermite rule for E[f(Z)], Z ~ N(0, I_d)."""
    x, w = hermegauss(n)
    w = w / np.sqrt(2.0 * np.pi)
    idx = np.array(list(itertools.product(range(n), repeat=d)))
    return x[idx], np.prod(w[idx], axis=1)


def kl_gauss(m0, S0, m1, S1):
    d = len(m0)
    S1i = np.linalg.inv(S1)
    dm = m1 - m0
    return 0.5 * (np.trace(S1i @ S0) + dm @ S1i @ dm - d
                  + np.linalg.slogdet(S1)[1] - np.linalg.slogdet(S0)[1])


def spd(k, rng, scale=1.0, floor=0.3):
    Q = rng.standard_normal((k, k))
    return scale * (Q @ Q.T / k + floor * np.eye(k))


def rk4(f, y, dt):
    k1 = f(y)
    k2 = f(y + 0.5 * dt * k1)
    k3 = f(y + 0.5 * dt * k2)
    k4 = f(y + dt * k3)
    return y + dt * (k1 + 2 * k2 + 2 * k3 + k4) / 6.0


def L_frechet(A, E):
    r"""Frechet derivative of exp at A in direction E: \int_0^1 e^{sA} E e^{(1-s)A} ds."""
    return expm_frechet(A, E, compute_expm=False)


# ----------------------------------------------------------------------------------------------
# A. Fisher metric of N(mu, Lambda^{-1})
# ----------------------------------------------------------------------------------------------
def check_A():
    header("A. Fisher metric of the Gaussian generator family in (mean, precision) coordinates")
    d = 3
    mu = RNG.standard_normal(d)
    Lam = spd(d, RNG)

    # natural parameters u1 = Lam mu, u2 = -Lam/2 ; log-partition psi(u)
    def psi(u1, u2):
        return -0.25 * u1 @ np.linalg.solve(u2, u1) - 0.5 * np.linalg.slogdet(-2 * u2)[1] \
            + 0.5 * d * np.log(2 * np.pi)

    # coordinates theta = (mu, Lambda entries upper-tri) ; map to natural parameters
    iu = np.triu_indices(d)

    def unpack(th):
        m = th[:d]
        L = np.zeros((d, d))
        L[iu] = th[d:]
        L = L + L.T - np.diag(np.diag(L))
        return m, L

    th0 = np.concatenate([mu, Lam[iu]])

    def psi_th(th):
        m, L = unpack(th)
        return psi(L @ m, -0.5 * L)

    def nat(th):
        m, L = unpack(th)
        return np.concatenate([L @ m, (-0.5 * L)[iu]])

    # Fisher in theta coords = J^T (Hess_u psi) J ; Hess_u psi by central differences in u
    n = len(th0)
    h = 1e-4
    u0 = nat(th0)

    def psi_u(u):
        u1 = u[:d]
        U2 = np.zeros((d, d))
        U2[iu] = u[d:]
        U2 = U2 + U2.T - np.diag(np.diag(U2))
        return psi(u1, U2)

    # pairing note: with off-diagonal parametrization u2_ij (i<j) appearing twice in Tr(u2 ww^T)
    Hu = np.zeros((n, n))
    for a in range(n):
        for b in range(n):
            ea = np.zeros(n); ea[a] = h
            eb = np.zeros(n); eb[b] = h
            Hu[a, b] = (psi_u(u0 + ea + eb) - psi_u(u0 + ea - eb) - psi_u(u0 - ea + eb)
                        + psi_u(u0 - ea - eb)) / (4 * h * h)
    Jac = np.zeros((n, n))
    for a in range(n):
        ea = np.zeros(n); ea[a] = 1e-6
        Jac[:, a] = (nat(th0 + ea) - nat(th0 - ea)) / 2e-6
    G_num = Jac.T @ Hu @ Jac

    # closed form: g = dmu^T Lam dmu + 1/2 Tr(Lam^{-1} dL Lam^{-1} dL)
    Li = np.linalg.inv(Lam)
    G_cf = np.zeros((n, n))
    for a in range(n):
        for b in range(n):
            ea = np.zeros(n); ea[a] = 1.0
            eb = np.zeros(n); eb[b] = 1.0
            ma, La = unpack(ea)
            mb, Lb = unpack(eb)
            G_cf[a, b] = ma @ Lam @ mb + 0.5 * np.trace(Li @ La @ Li @ Lb)
    err = np.max(np.abs(G_num - G_cf)) / np.max(np.abs(G_cf))
    report("Fisher metric (mu,Lambda) closed form vs J^T Hess(psi) J (rel)", err, 1e-6)
    report("min eigenvalue of Fisher metric (positive)", np.min(np.linalg.eigvalsh(G_cf)), 0.0, "ge")

    # Monte Carlo cross-check of E[s s^T] (sampling only, loose tolerance)
    N = 400000
    Z = RNG.multivariate_normal(np.zeros(d), Li, size=N)
    S = np.zeros((N, n))
    for a in range(n):
        ea = np.zeros(n); ea[a] = 1.0
        ma, La = unpack(ea)
        S[:, a] = Z @ (Lam @ ma) - 0.5 * (np.einsum("ni,ij,nj->n", Z, La, Z) - np.trace(Li @ La))
    G_mc = S.T @ S / N
    report("Fisher metric vs Monte Carlo E[s s^T] (rel, sampling)", np.max(np.abs(G_mc - G_cf)) /
           np.max(np.abs(G_cf)), 2e-2)


# ----------------------------------------------------------------------------------------------
# B. SO(2) triangle with Gaussian generator recognition and Gaussian matter means
# ----------------------------------------------------------------------------------------------
JR = np.array([[0.0, -1.0], [1.0, 0.0]])


def rot(t):
    c, s = np.cos(t), np.sin(t)
    R = np.empty(t.shape + (2, 2))
    R[..., 0, 0] = c
    R[..., 0, 1] = -s
    R[..., 1, 0] = s
    R[..., 1, 1] = c
    return R


class SO2Triangle:
    """Generators w in R^3 (one per edge, so(2) coordinate), loop sum s = w0+w1+w2,
    loop term c(2-2cos s) = (1/2)||R(s)-I||_F^2 * c, anchor N(alpha, sig0sq I),
    linear-Gaussian comparison records E_e = 1/2|k_i - R(w_e) k_j|^2_{H_e}, product Gaussian
    matter recognition k_i ~ N(m_i, C_i) with matter prior N(0, I)."""

    edges = [(1, 0), (2, 1), (0, 2)]  # (source j, receiver i)

    def __init__(self, rng, c=0.9, sig0sq=0.8):
        self.c = c
        self.sig0sq = sig0sq
        self.alpha = 0.3 * rng.standard_normal(3)
        self.H = [spd(2, rng) for _ in range(3)]
        self.beta = rng.uniform(0.4, 1.0, size=3)
        self.C = [spd(2, rng, 0.3) for _ in range(3)]
        self.Z, self.W = gh_rule(3, 22)

    def ell_derivs(self, Om, m):
        """Om: (N,3) generator nodes. Returns ell, grad_w, hess_w, grad_m (per node)."""
        N = Om.shape[0]
        ell = 0.5 * np.sum((Om - self.alpha) ** 2, axis=1) / self.sig0sq
        g = (Om - self.alpha) / self.sig0sq
        Hs = np.zeros((N, 3, 3))
        Hs[:, [0, 1, 2], [0, 1, 2]] += 1.0 / self.sig0sq
        s = Om.sum(axis=1)
        ell += self.c * (2 - 2 * np.cos(s))
        g += (2 * self.c * np.sin(s))[:, None]
        Hs += (2 * self.c * np.cos(s))[:, None, None] * np.ones((3, 3))
        gm = np.zeros((N, 3, 2))
        for e, (j, i) in enumerate(self.edges):
            H, b, Cj, Ci = self.H[e], self.beta[e], self.C[j], self.C[i]
            R = rot(Om[:, e])
            Rp = np.einsum("ab,nbc->nac", JR, R)
            Rpp = -R
            Rmj = R @ m[j]
            r = m[i] - Rmj
            Rpmj = Rp @ m[j]
            Rppmj = Rpp @ m[j]
            f = 0.5 * np.einsum("na,ab,nb->n", r, H, r) + 0.5 * np.trace(H @ Ci) \
                + 0.5 * np.einsum("ab,nbc,cd,nad->n", H, R, Cj, R)
            fp = -np.einsum("na,ab,nb->n", r, H, Rpmj) + np.einsum("ab,nbc,cd,nad->n", H, Rp, Cj, R)
            fpp = np.einsum("na,ab,nb->n", Rpmj, H, Rpmj) - np.einsum("na,ab,nb->n", r, H, Rppmj) \
                + np.einsum("ab,nbc,cd,nad->n", H, Rpp, Cj, R) + np.einsum("ab,nbc,cd,nad->n", H, Rp, Cj, Rp)
            ell += b * f
            g[:, e] += b * fp
            Hs[:, e, e] += b * fpp
            gm[:, i, :] += b * (r @ H)            # H symmetric: H r
            gm[:, j, :] += -b * np.einsum("nba,nb->na", R, r @ H)  # -R^T H r
        return ell, g, Hs, gm

    def ell_only(self, Om, m):
        ell = 0.5 * np.sum((Om - self.alpha) ** 2, axis=1) / self.sig0sq
        ell += self.c * (2 - 2 * np.cos(Om.sum(axis=1)))
        for e, (j, i) in enumerate(self.edges):
            H, b, Cj, Ci = self.H[e], self.beta[e], self.C[j], self.C[i]
            R = rot(Om[:, e])
            r = m[i] - R @ m[j]
            ell += b * (0.5 * np.einsum("na,ab,nb->n", r, H, r) + 0.5 * np.trace(H @ Ci)
                        + 0.5 * np.einsum("ab,nbc,cd,nad->n", H, R, Cj, R))
        return ell

    def expect(self, mu, Sig, m):
        L = np.linalg.cholesky(Sig)
        Om = mu + self.Z @ L.T
        ell, g, Hs, gm = self.ell_derivs(Om, m)
        W = self.W
        return (W @ ell, np.einsum("n,ni->i", W, g), np.einsum("n,nij->ij", W, Hs),
                np.einsum("n,nij->ij", W, gm))

    def F(self, mu, Sig, m):
        L = np.linalg.cholesky(Sig)
        El = self.W @ self.ell_only(mu + self.Z @ L.T, m)
        ent = 0.5 * np.linalg.slogdet(2 * np.pi * np.e * Sig)[1]
        matter = sum(0.5 * (m[i] @ m[i] + np.trace(self.C[i])) for i in range(3))
        return El - ent + matter


def check_B():
    header("B. Natural-gradient flow, Bayesian learning rule, and its descent bound (SO(2) triangle)")
    model = SO2Triangle(RNG)
    mu0 = 0.8 * RNG.standard_normal(3)
    Sig0 = spd(3, RNG, 0.4)
    m0 = RNG.standard_normal((3, 2))

    # --- B1: joint natural-gradient flow of (mu, Sigma) and matter means, monotone F
    def pack(mu, Sig, m):
        return np.concatenate([mu, Sig.ravel(), m.ravel()])

    def unpack(y):
        mu = y[:3]
        Sig = y[3:12].reshape(3, 3)
        Sig = 0.5 * (Sig + Sig.T)
        m = y[12:].reshape(3, 2)
        return mu, Sig, m

    def field(y):
        mu, Sig, m = unpack(y)
        _, Eg, EH, Egm = model.expect(mu, Sig, m)
        dmu = -Sig @ Eg
        dSig = Sig - Sig @ EH @ Sig        # natural gradient in Sigma: -2 Sig (EH/2 - Sig^{-1}/2) Sig
        dm = np.stack([-model.C[i] @ (Egm[i] + m[i]) for i in range(3)])
        return pack(dmu, dSig, dm)

    y = pack(mu0, Sig0, m0)
    Fs = [model.F(*unpack(y))]
    dt = 0.02
    for _ in range(400):
        y = rk4(field, y, dt)
        Fs.append(model.F(*unpack(y)))
    Fs = np.array(Fs)
    dF = np.diff(Fs)
    print(f"  F(0) = {Fs[0]:.6f}, F(8) = {Fs[-1]:.6f}, total decrease {Fs[0]-Fs[-1]:.4f}")
    report("max increase of F along RK4 natural-gradient flow (400 steps)", max(dF.max(), 0.0), 1e-10)
    report("Sigma stays positive definite (min eig at end)",
           np.min(np.linalg.eigvalsh(unpack(y)[1])), 0.0, "ge")

    # --- B2: explicit Euler step in natural parameters == BLR (full precision)
    mu, Sig, m = mu0, Sig0, m0
    Lam = np.linalg.inv(Sig)
    dts = 0.37
    _, Eg, EH, _ = model.expect(mu, Sig, m)
    Lam_b = (1 - dts) * Lam + dts * EH
    mu_b = mu - dts * np.linalg.solve(Lam_b, Eg)

    def Ftil(w1, w2):
        return model.F(w1, w2 - np.outer(w1, w1), m)

    w1 = mu.copy()
    w2 = Sig + np.outer(mu, mu)
    h = 1e-5
    g1 = np.zeros(3)
    for a in range(3):
        e = np.zeros(3); e[a] = h
        g1[a] = (Ftil(w1 + e, w2) - Ftil(w1 - e, w2)) / (2 * h)
    G2 = np.zeros((3, 3))
    for a in range(3):
        for b in range(a, 3):
            E = np.zeros((3, 3))
            E[a, b] = h
            E[b, a] = h
            val = (Ftil(w1, w2 + E) - Ftil(w1, w2 - E)) / (2 * h)
            if a == b:
                G2[a, a] = val
            else:
                G2[a, b] = G2[b, a] = val / 2.0
    u1 = Lam @ mu - dts * g1
    u2 = -0.5 * Lam - dts * G2
    Lam_e = -2 * u2
    mu_e = np.linalg.solve(Lam_e, u1)
    report("BLR precision vs natural-parameter Euler step (full family, rel)",
           np.max(np.abs(Lam_e - Lam_b)) / np.max(np.abs(Lam_b)), 1e-7)
    report("BLR mean vs natural-parameter Euler step (full family, abs)", np.max(np.abs(mu_e - mu_b)), 1e-7)

    # Bonnet / Price identities used in the BLR derivation (quadrature, finite differences)
    Eell = lambda mm, SS: model.expect(mm, SS, m)[0]  # noqa: E731
    gmu = np.array([(Eell(mu + h * np.eye(3)[a], Sig) - Eell(mu - h * np.eye(3)[a], Sig)) / (2 * h)
                    for a in range(3)])
    report("Bonnet: grad_mu E[ell] = E[grad ell]", np.max(np.abs(gmu - Eg)), 1e-7)
    GS = np.zeros((3, 3))
    for a in range(3):
        for b in range(a, 3):
            E = np.zeros((3, 3)); E[a, b] = h; E[b, a] = h
            val = (Eell(mu, Sig + E) - Eell(mu, Sig - E)) / (2 * h)
            GS[a, b] = GS[b, a] = val if a == b else val / 2.0
    report("Price: grad_Sigma E[ell] = E[hess ell]/2", np.max(np.abs(GS - 0.5 * EH)), 1e-6)

    # --- B3: block-diagonal (here diagonal, one coordinate per edge) subfamily
    d_s = np.diag(Sig).copy()
    lam_d = 1.0 / d_s
    Sigd = np.diag(d_s)
    _, Egd, EHd, _ = model.expect(mu, Sigd, m)
    lam_b = (1 - dts) * lam_d + dts * np.diag(EHd)
    mu_bd = mu - dts * Egd / lam_b

    def Ftil_d(w1, w2d):
        return model.F(w1, np.diag(w2d - w1 ** 2), m)

    w2d = d_s + mu ** 2
    g1d = np.array([(Ftil_d(mu + h * np.eye(3)[a], w2d) - Ftil_d(mu - h * np.eye(3)[a], w2d)) / (2 * h)
                    for a in range(3)])
    g2d = np.array([(Ftil_d(mu, w2d + h * np.eye(3)[a]) - Ftil_d(mu, w2d - h * np.eye(3)[a])) / (2 * h)
                    for a in range(3)])
    u1d = lam_d * mu - dts * g1d
    u2d = -0.5 * lam_d - dts * g2d
    lam_e = -2 * u2d
    mu_ed = u1d / lam_e
    report("block-diagonal BLR (projected Hessian) vs Euler step, precision (rel)",
           np.max(np.abs(lam_e - lam_b)) / np.max(np.abs(lam_b)), 1e-7)
    report("block-diagonal BLR vs Euler step, mean (abs)", np.max(np.abs(mu_ed - mu_bd)), 1e-7)

    # --- B4: mirror-descent bound along BLR steps (full family, matter fixed)
    iu = np.triu_indices(3)

    def to_vec(w1, w2):
        return np.concatenate([w1, w2[iu]])

    def from_vec(v):
        w1 = v[:3]
        W2 = np.zeros((3, 3))
        W2[iu] = v[3:]
        W2 = W2 + W2.T - np.diag(np.diag(W2))
        return w1, W2

    def Fv(v):
        w1, w2 = from_vec(v)
        return Ftil(w1, w2)

    def negent(v):
        w1, w2 = from_vec(v)
        return -0.5 * np.linalg.slogdet(2 * np.pi * np.e * (w2 - np.outer(w1, w1)))[1]

    def hess_fd(fun, v, hh=2e-4):
        n = len(v)
        Hm = np.zeros((n, n))
        for a in range(n):
            for b in range(a, n):
                ea = np.zeros(n); ea[a] = hh
                eb = np.zeros(n); eb[b] = hh
                val = (fun(v + ea + eb) - fun(v + ea - eb) - fun(v - ea + eb) + fun(v - ea - eb)) / (4 * hh * hh)
                Hm[a, b] = Hm[b, a] = val
        return Hm

    for dts_b in (0.25, 0.6):
        muc, Sigc = mu0.copy(), Sig0.copy()
        worst = -np.inf
        ok_desc = True
        for step in range(4):
            Lc = np.linalg.inv(Sigc)
            _, Egc, EHc, _ = model.expect(muc, Sigc, m)
            Ln = (1 - dts_b) * Lc + dts_b * EHc
            if np.min(np.linalg.eigvalsh(Ln)) <= 0:
                print("   (precision left the domain; stop)")
                break
            mun = muc - dts_b * np.linalg.solve(Ln, Egc)
            Sign = np.linalg.inv(Ln)
            v0 = to_vec(muc, Sigc + np.outer(muc, muc))
            v1 = to_vec(mun, Sign + np.outer(mun, mun))
            cG = 0.0
            for s in np.linspace(0, 1, 7):
                vs = (1 - s) * v0 + s * v1
                HF = hess_fd(Fv, vs)
                HP = hess_fd(negent, vs)
                w = np.linalg.eigvals(np.linalg.solve(HP, HF)).real
                cG = max(cG, w.max())
            F0 = model.F(muc, Sigc, m)
            F1 = model.F(mun, Sign, m)
            k01 = kl_gauss(muc, Sigc, mun, Sign)
            k10 = kl_gauss(mun, Sign, muc, Sigc)
            bound = F0 - k01 / dts_b - (1 / dts_b - cG) * k10
            worst = max(worst, F1 - bound)
            if dts_b <= 1.0 / cG and not (F1 < F0):
                ok_desc = False
            print(f"   dt={dts_b}: step {step}: F {F0:.6f} -> {F1:.6f}, c_G={cG:.3f}, 1/dt={1/dts_b:.3f}, "
                  f"bound slack {bound - F1:.3e}")
            muc, Sigc = mun, Sign
        report(f"mirror-descent bound F(t+1) <= F(t) - KL/dt - (1/dt - c_G) KL' (dt={dts_b}); worst violation",
               max(worst, 0.0), 1e-6)
        RESULTS.append((f"strict decrease whenever dt <= 1/c_G (dt={dts_b})", ok_desc))
        print(f"  [{'PASS' if ok_desc else 'FAIL'}] strict decrease whenever dt <= 1/c_G (dt={dts_b})")

    # --- B5: quadratic integrand: BLR with dt = 1 reaches the Gaussian minimizer in one step
    P = spd(3, RNG)
    bvec = RNG.standard_normal(3)
    mu_q, Lam_q = RNG.standard_normal(3), spd(3, RNG)
    # E[grad ell] = P mu - b ; E[hess ell] = P
    Lam_1 = P
    mu_1 = mu_q - np.linalg.solve(Lam_1, P @ mu_q - bvec)
    report("quadratic integrand, dt=1: precision = P", np.max(np.abs(Lam_1 - P)), 1e-14)
    report("quadratic integrand, dt=1: mean = P^{-1} b", np.max(np.abs(mu_1 - np.linalg.solve(P, bvec))), 1e-12)


# ----------------------------------------------------------------------------------------------
# C. Anchor M-coordinate
# ----------------------------------------------------------------------------------------------
def check_C():
    header("C. Exact M-coordinate of the anchor (with and without curvature); covariance M-step")
    # C1: no curvature: maximizer of E_R log N(w; a, S0) is mu_R
    d = 3
    S0 = np.diag(RNG.uniform(0.3, 1.5, d))
    S0i = np.linalg.inv(S0)
    muR = RNG.standard_normal(d)
    SigR = spd(d, RNG, 0.5)

    def negJ0(a):
        dm = muR - a
        return 0.5 * (np.trace(S0i @ SigR) + dm @ S0i @ dm)

    res = minimize(negJ0, np.zeros(d), method="BFGS", options={"gtol": 1e-12})
    report("c_p = 0: anchor M-coordinate equals recognition mean", np.max(np.abs(res.x - muR)), 1e-7)

    # C2: translation instance on a triangle, loop sum quadratic: alpha_new = (I + S0 K_C) mu_R
    c = 0.7
    one = np.ones((d, 1))
    KC = c * (one @ one.T)
    Pp = S0i + KC        # prior precision

    def negJ2(a):
        mP = np.linalg.solve(Pp, S0i @ a)
        dm = muR - mP
        return 0.5 * (np.trace(Pp @ SigR) + dm @ Pp @ dm) - 0.5 * np.linalg.slogdet(Pp)[1]

    res = minimize(negJ2, np.zeros(d), method="BFGS", options={"gtol": 1e-12})
    a_cf = (np.eye(d) + S0 @ KC) @ muR
    report("translation instance: alpha_new = (I + S0 K_C) mu_R", np.max(np.abs(res.x - a_cf)), 1e-6)
    print(f"   recognition loop sum {muR.sum():.4f}; anchor shift |alpha_new - mu_R| = "
          f"{np.linalg.norm(a_cf - muR):.4f}")

    # C3: SO(2) triangle, loop term c(2-2cos s): moment matching and gradient formula
    xs, ws = hermegauss(120)
    ws = ws / np.sqrt(2 * np.pi)
    cc = 1.3
    S0 = 0.6 * np.eye(d)
    S0i = np.linalg.inv(S0)
    v1 = (S0 @ np.ones(d))
    vs = np.ones(d) @ S0 @ np.ones(d)

    def wfun(s):
        return np.exp(-cc * (2 - 2 * np.cos(s)))

    def prior_stats(a):
        sbar = a.sum()
        s = sbar + np.sqrt(vs) * xs
        Zs = ws @ wfun(s)
        Ms = ws @ ((s - sbar) * wfun(s))
        return Zs, a + v1 * Ms / (vs * Zs)    # Z_S(a), E_P[w]

    def J3(a):
        dm = muR - a
        return -0.5 * (np.trace(S0i @ SigR) + dm @ S0i @ dm) - np.log(prior_stats(a)[0])

    a_test = RNG.standard_normal(d)
    h = 1e-6
    gfd = np.array([(J3(a_test + h * np.eye(d)[k]) - J3(a_test - h * np.eye(d)[k])) / (2 * h) for k in range(d)])
    gcf = S0i @ (muR - prior_stats(a_test)[1])
    report("SO(2) curvature: grad J = Sigma0^{-1}(E_R w - E_P w) (finite differences)", np.max(np.abs(gfd - gcf)), 1e-7)
    res = minimize(lambda a: -J3(a), muR.copy(), method="BFGS", options={"gtol": 1e-11})
    a_new = res.x
    report("SO(2) curvature: prior mean at maximizer equals recognition mean",
           np.max(np.abs(prior_stats(a_new)[1] - muR)), 1e-6)
    print(f"   |alpha_new - mu_R| = {np.linalg.norm(a_new - muR):.4f} (nonzero: M-coordinate is not the mean)")
    report("SO(2) curvature: alpha_new differs from mu_R", np.linalg.norm(a_new - muR), 1e-3, "ge")
    # strict concavity: Hessian of J3 negative definite at a few points
    worst = -np.inf
    for _ in range(5):
        a0 = 2 * RNG.standard_normal(d)
        Hm = np.zeros((d, d))
        hh = 1e-4
        for i in range(d):
            for j in range(d):
                ei = hh * np.eye(d)[i]
                ej = hh * np.eye(d)[j]
                Hm[i, j] = (J3(a0 + ei + ej) - J3(a0 + ei - ej) - J3(a0 - ei + ej) + J3(a0 - ei - ej)) / (4 * hh * hh)
        worst = max(worst, np.max(np.linalg.eigvalsh(0.5 * (Hm + Hm.T))))
    report("SO(2) curvature: J strictly concave (max Hessian eigenvalue < 0)", -worst, 1e-6, "ge")

    # C4: covariance M-step.  (i) no curvature: (mu, v) maximizes; (ii) self-loop witness
    mu1, v = 0.4, 1.7

    def J_self(a, s2, c_):
        # prior N(a/(1+c s2), s2/(1+c s2)) ; recognition N(mu1, v)
        mean = a / (1 + c_ * s2)
        var = s2 / (1 + c_ * s2)
        return -0.5 * np.log(2 * np.pi * var) - (v + (mu1 - mean) ** 2) / (2 * var)

    res = minimize(lambda p: -J_self(p[0], np.exp(p[1]), 0.0), np.array([0.0, 0.0]), method="BFGS",
                   options={"gtol": 1e-12})
    report("covariance M-step, c=0: maximizer (mu, v)",
           max(abs(res.x[0] - mu1), abs(np.exp(res.x[1]) - v)), 1e-6)
    c_ = 1.0 / v * 1.25   # v >= 1/c
    grid = np.exp(np.linspace(np.log(0.05), np.log(1e5), 400))
    vals = np.array([J_self(mu1 * (1 + c_ * s2), s2, c_) for s2 in grid])
    report("self-loop witness: J(s2) strictly increasing on (0, 1e5] when v >= 1/c (min increment)",
           np.min(np.diff(vals)), 0.0, "ge")
    print(f"   sup J = {(-0.5*np.log(2*np.pi/c_) - v*c_/2):.6f} approached, J(1e5) = {vals[-1]:.6f}")


# ----------------------------------------------------------------------------------------------
# D. Most probable histories
# ----------------------------------------------------------------------------------------------
def energy_1d(w_int, a, b, m, V):
    w = np.concatenate([[a], w_int, [b]])
    return 0.5 * m * np.sum(np.diff(w) ** 2) + np.sum(V(w_int))


def grad_1d(w_int, a, b, m, dV):
    w = np.concatenate([[a], w_int, [b]])
    return m * (2 * w[1:-1] - w[2:] - w[:-2]) + dV(w_int)


def check_D():
    header("D. Most probable histories: 1D double well, rearrangement, time-like defect with gl(2)")
    V = lambda x: (x ** 2 - 1) ** 2  # noqa: E731
    dV = lambda x: 4 * x * (x ** 2 - 1)  # noqa: E731
    d2V = lambda x: 12 * x ** 2 - 4  # noqa: E731
    N = 20

    def newton_1d(x, m):
        for _ in range(50):
            g = grad_1d(x, -1.0, 1.0, m, dV)
            if np.max(np.abs(g)) < 1e-13:
                break
            Hm = m * (2 * np.eye(N - 1) - np.eye(N - 1, k=1) - np.eye(N - 1, k=-1)) + np.diag(d2V(x))
            x = x - np.linalg.solve(Hm, g)
        return x

    for m in (0.3, 2.0, 10.0):
        mins = []
        jac1 = lambda w, *a: grad_1d(w, -1.0, 1.0, m, dV)  # noqa: E731
        for _ in range(300):
            x0 = RNG.uniform(-2.0, 2.0, N - 1)
            r = minimize(energy_1d, x0, args=(-1.0, 1.0, m, V), jac=jac1, method="L-BFGS-B",
                         options={"gtol": 1e-12, "ftol": 1e-15, "maxiter": 20000})
            mins.append(r.x)
        # each local minimum and its clamp-and-sort rearrangement, re-minimized
        cands = []
        for x in mins:
            for start in (x, np.sort(np.clip(x, -1.0, 1.0))):
                r = minimize(energy_1d, start, args=(-1.0, 1.0, m, V), jac=jac1, method="L-BFGS-B",
                             options={"gtol": 1e-12, "ftol": 1e-15, "maxiter": 20000})
                xx = newton_1d(r.x, m)
                cands.append((energy_1d(xx, -1.0, 1.0, m, V), xx))
        cands.sort(key=lambda t: t[0])
        best = cands[0]
        w = np.concatenate([[-1.0], best[1], [1.0]])
        res = np.max(np.abs(grad_1d(best[1], -1.0, 1.0, m, dV)))
        report(f"double well m={m}: Euler-Lagrange residual at best minimizer", res, 1e-10)
        report(f"double well m={m}: best minimizer strictly increasing (min increment)", np.min(np.diff(w)), 0.0, "ge")
        nonmono = [f for f, x in cands if np.any(np.diff(np.concatenate([[-1.0], x, [1.0]])) < -1e-9)]
        gap = (min(nonmono) - best[0]) if nonmono else np.inf
        print(f"   m={m}: best E={best[0]:.6f}; non-monotone local minima found: {len(nonmono)}; "
              f"lowest non-monotone E - best E = {gap:.4f}")
        RESULTS.append((f"double well m={m}: no non-monotone local minimum below the monotone best",
                        bool(gap > 0)))
        print(f"  [{'PASS' if gap > 0 else 'FAIL'}] double well m={m}: no non-monotone local minimum below "
              f"the monotone best")

    # rearrangement inequality used in the proof: E(sort(clamp(w))) <= E(w), strict if not monotone
    worst = -np.inf
    strict_ok = True
    for _ in range(20000):
        x = RNG.uniform(-2.5, 2.5, N - 1)
        m = RNG.uniform(0.1, 5.0)
        y = np.sort(np.clip(x, -1.0, 1.0))
        E0 = energy_1d(x, -1.0, 1.0, m, V)
        E1 = energy_1d(y, -1.0, 1.0, m, V)
        worst = max(worst, E1 - E0)
        full = np.concatenate([[-1.0], x, [1.0]])
        if np.any(np.diff(full) < -1e-12) and not (E1 < E0):
            strict_ok = False
    report("clamp-and-sort never increases the history energy (max E(sorted)-E(original))", max(worst, 0.0), 1e-12)
    RESULTS.append(("clamp-and-sort strictly decreases energy of non-monotone histories", strict_ok))
    print(f"  [{'PASS' if strict_ok else 'FAIL'}] clamp-and-sort strictly decreases energy of non-monotone histories")

    # hypothesis without a double well: V = x^2, a=-1, b=2 (V >= V(a) left of a, >= V(b) right of b)
    V2 = lambda x: x ** 2  # noqa: E731
    dV2 = lambda x: 2 * x  # noqa: E731
    r = minimize(energy_1d, np.zeros(N - 1), args=(-1.0, 2.0, 1.0, V2),
                 jac=lambda w, *a: grad_1d(w, -1.0, 2.0, 1.0, dV2), method="BFGS", options={"gtol": 1e-12})
    wv = np.concatenate([[-1.0], r.x, [2.0]])
    report("V = x^2, ends (-1, 2): minimizer nondecreasing (min increment)", np.min(np.diff(wv)), -1e-12, "ge")

    # control: the hypothesis fails (deep well outside [a, b]); global minimizer is not monotone
    V3 = lambda x: (x ** 2 - 1) ** 2 - 6.0 * np.exp(-4 * (x - 2.5) ** 2)  # noqa: E731
    best = None
    for _ in range(300):
        x0 = RNG.uniform(-2.0, 3.5, N - 1)
        r = minimize(energy_1d, x0, args=(-1.0, 1.0, 0.3, V3), method="L-BFGS-B",
                     options={"gtol": 1e-11, "ftol": 1e-15})
        if best is None or r.fun < best[0]:
            best = (r.fun, r.x)
    wv = np.concatenate([[-1.0], best[1], [1.0]])
    print(f"   control (deep well at 2.5 outside [a,b], m=0.3): global minimizer max value {wv.max():.3f}, "
          f"monotone: {bool(np.all(np.diff(wv) >= -1e-9))}  (hypothesis of (c) fails; non-monotone expected)")

    # --- D2: time-like defect variant, gl(2) generators with a nontrivial fiber metric
    K = 2
    Gf = spd(K, RNG, 1.0, 0.5)
    wG, VG = np.linalg.eigh(Gf)
    Gh = VG @ np.diag(np.sqrt(wG)) @ VG.T
    Ghi = VG @ np.diag(1 / np.sqrt(wG)) @ VG.T
    Gi = np.linalg.inv(Gf)

    def toA(Y):
        return Ghi @ Y @ Gh

    def gA_to_gY(gA):
        return Ghi @ gA @ Gh

    def Qdef(Hm):
        D = Hm - np.eye(K)
        return 0.5 * np.trace(Gi @ D.T @ Gf @ D)

    def Qdef_gradH(Hm):
        D = Hm - np.eye(K)
        return Gf @ D @ Gi

    def U_timelike(Yp, Y):
        Ap, A = toA(Yp), toA(Y)
        return Qdef(expm(-Ap) @ expm(A))

    def U_grads(Yp, Y):
        """(grad wrt earlier Y, grad wrt later Yp), Frobenius in Y coords (= <,>_G gradients)."""
        Ap, A = toA(Yp), toA(Y)
        Ep, E = expm(-Ap), expm(A)
        Gam = Qdef_gradH(Ep @ E)
        gE = Ep.T @ Gam
        gEp = Gam @ E.T
        gA = L_frechet(A.T, gE)
        gAp = -L_frechet(-Ap.T, gEp)
        return gA_to_gY(gA), gA_to_gY(gAp)

    # gradient check
    Y1, Y0 = 0.6 * RNG.standard_normal((K, K)), 0.6 * RNG.standard_normal((K, K))
    gY0, gY1 = U_grads(Y1, Y0)
    h = 1e-6
    fd0 = np.zeros((K, K))
    fd1 = np.zeros((K, K))
    for a in range(K):
        for b in range(K):
            E = np.zeros((K, K)); E[a, b] = h
            fd0[a, b] = (U_timelike(Y1, Y0 + E) - U_timelike(Y1, Y0 - E)) / (2 * h)
            fd1[a, b] = (U_timelike(Y1 + E, Y0) - U_timelike(Y1 - E, Y0)) / (2 * h)
    report("time-like defect: Frechet-derivative gradient (earlier arg) vs FD", np.max(np.abs(gY0 - fd0)), 1e-8)
    report("time-like defect: Frechet-derivative gradient (later arg) vs FD", np.max(np.abs(gY1 - fd1)), 1e-8)

    # adjoint identity <X, L(A,E)>_G = <L(A^*,X), E>_G with A^* = G^{-1} A^T G
    A = RNG.standard_normal((K, K)); X = RNG.standard_normal((K, K)); E = RNG.standard_normal((K, K))
    Ast = Gi @ A.T @ Gf
    lhs = np.trace(Gi @ X.T @ Gf @ L_frechet(A, E))
    rhs = np.trace(Gi @ L_frechet(Ast, X).T @ Gf @ E)
    report("adjoint of L(A,.) for <,>_G is L(A^*,.)", abs(lhs - rhs), 1e-12)

    # history: n1 = 6, potential V_n(Y) = |Y|^2/(2 s0) - <b_n, Y>, mass m
    n1, mass, s0 = 6, 1.3, 0.7

    def make_hist(scale):
        bn = scale * RNG.standard_normal((n1 + 1, K, K))

        def Phi(z):
            Ys = z.reshape(n1 + 1, K, K)
            val = sum(0.5 * np.sum(Ys[n] ** 2) / s0 - np.sum(bn[n] * Ys[n]) for n in range(n1 + 1))
            val += mass * sum(U_timelike(Ys[n + 1], Ys[n]) for n in range(n1))
            return val

        def gPhi(z):
            Ys = z.reshape(n1 + 1, K, K)
            g = np.stack([Ys[n] / s0 - bn[n] for n in range(n1 + 1)])
            for n in range(n1):
                ge, gl = U_grads(Ys[n + 1], Ys[n])
                g[n] += mass * ge
                g[n + 1] += mass * gl
            return g.ravel()

        return bn, Phi, gPhi

    rows = []
    for scale in (0.3, 0.1, 0.03, 0.01):
        bn, Phi, gPhi = make_hist(scale)
        r = minimize(Phi, np.zeros((n1 + 1) * K * K), jac=gPhi, method="BFGS", options={"gtol": 1e-12})
        zst, exact_res = newton_min(gPhi, r.x)
        Ys = zst.reshape(n1 + 1, K, K)
        # Gaussian-increment equation residual at the defect minimizer (interior n)
        rad = max(np.linalg.norm(Ys[n]) for n in range(n1 + 1))
        ratios = []
        resG_max = 0.0
        for n in range(1, n1):
            resG = mass * (2 * Ys[n] - Ys[n + 1] - Ys[n - 1]) + Ys[n] / s0 - bn[n]
            incr = np.linalg.norm(Ys[n + 1] - Ys[n]) + np.linalg.norm(Ys[n] - Ys[n - 1])
            ratios.append(np.linalg.norm(resG) / (mass * rad * incr))
            resG_max = max(resG_max, np.linalg.norm(resG))
        rows.append((scale, exact_res, rad, resG_max, max(ratios)))
    print("   scale   |exact grad|   radius r   |Gaussian-eq residual|   max residual/(m r |increments|)")
    for row in rows:
        print("   %.3f   %.2e      %.3e   %.3e               %.3f" % row)
    report("time-like defect history: exact equation residual at computed minimizer (largest scale)",
           rows[0][1], 1e-9)
    report("leading-order bound: residual/(m r increments) stays bounded (max over scales)",
           max(r_[4] for r_ in rows), 5.0)
    report("Gaussian-equation residual decays faster than radius (ratio last/first of resid/r^2)",
           (rows[-1][3] / rows[-1][2] ** 2) / (rows[0][3] / rows[0][2] ** 2), 3.0)


# ----------------------------------------------------------------------------------------------
# E/F. Linearized link equation on a triangle x three episodes (gl(2) with a fiber metric; so(3))
# ----------------------------------------------------------------------------------------------
class TriangleHistory:
    """Generators on a triangle x (n1+1) episodes in a represented Lie algebra g of gl(K), with an
    orthonormal basis B_k of g for <A,B>_G = Tr(G^{-1} A^T G B); coordinates y_{n,e,k} and
    A_{n,e} = sum_k y_{n,e,k} B_k.  Edges e0:1->0, e1:2->1, e2:0->2; loop (e0,e1,e2); comparison
    records on e0, e1, e2 and on the reversal of e0."""

    def __init__(self, rng, eps, kinetic="defect", n1=2, algebra="gl2"):
        self.n1, self.kin = n1, kinetic
        self.s0, self.c, self.mass = 0.5, 0.8, 0.7     # anchor variance (precision 2), loop coeff, mass
        if algebra == "gl2":
            K = 2
            Gf = spd(K, rng, 1.0, 0.4)
            w, Vv = np.linalg.eigh(Gf)
            Gh = Vv @ np.diag(np.sqrt(w)) @ Vv.T
            Ghi = Vv @ np.diag(1 / np.sqrt(w)) @ Vv.T
            basis = []
            for a in range(K):
                for b in range(K):
                    E = np.zeros((K, K))
                    E[a, b] = 1.0
                    basis.append(Ghi @ E @ Gh)
            mbar = np.array([1.0, -0.5])
        else:
            K = 3
            Gf = np.eye(3)
            w = np.ones(3)
            basis = []
            for (a, b) in [(2, 1), (0, 2), (1, 0)]:
                E = np.zeros((3, 3))
                E[a, b] = 1 / np.sqrt(2)
                E[b, a] = -1 / np.sqrt(2)
                basis.append(E)
            mbar = np.array([1.0, -0.5, 0.7])
        self.K, self.Gf, self.Gi = K, Gf, np.linalg.inv(Gf)
        self.condG = w.max() / w.min()
        self.B = basis
        self.k = len(basis)
        gram = np.array([[np.trace(self.Gi @ Bp.T @ Gf @ Bq) for Bq in basis] for Bp in basis])
        assert np.max(np.abs(gram - np.eye(self.k))) < 1e-12
        self.records = [(0, +1, 0, 1), (1, +1, 1, 2), (2, +1, 2, 0), (0, -1, 1, 0)]
        self.Hrec = [spd(K, rng) for _ in self.records]
        self.beta = rng.uniform(0.3, 1.0, size=(n1 + 1, len(self.records)))
        self.mu = [[mbar + eps * rng.standard_normal(K) for _ in range(3)] for _ in range(n1 + 1)]
        self.Sg = [[eps * spd(K, rng, 1.0) for _ in range(3)] for _ in range(n1 + 1)]

    def A(self, y):
        return sum(yk * Bk for yk, Bk in zip(y, self.B))

    def comp(self, gF):
        """Coordinate gradient from a Frobenius gradient: directional derivatives along B_k."""
        return np.array([np.sum(gF * Bk) for Bk in self.B])

    def Qdef(self, Hm):
        D = Hm - np.eye(self.K)
        return 0.5 * np.trace(self.Gi @ D.T @ self.Gf @ D)

    def QgradH(self, Hm):
        D = Hm - np.eye(self.K)
        return self.Gf @ D @ self.Gi

    def Phi(self, z):
        n1, k = self.n1, self.k
        Ys = z.reshape(n1 + 1, 3, k)
        val = 0.0
        for n in range(n1 + 1):
            As = [self.A(Ys[n, e]) for e in range(3)]
            val += 0.5 * np.sum(Ys[n] ** 2) / self.s0
            val += self.c * self.Qdef(expm(As[0]) @ expm(As[1]) @ expm(As[2]))
            for r, (e, sg, i, j) in enumerate(self.records):
                G = expm(sg * As[e])
                Hm = self.Hrec[r]
                mi, mj, Sj = self.mu[n][i], self.mu[n][j], self.Sg[n][j]
                d = mi - G @ mj
                val += self.beta[n, r] * 0.5 * (d @ Hm @ d + np.trace(Hm @ self.Sg[n][i])
                                                 + np.trace(Hm @ G @ Sj @ G.T))
        for n in range(n1):
            for e in range(3):
                if self.kin == "defect":
                    val += self.mass * self.Qdef(expm(-self.A(Ys[n + 1, e])) @ expm(self.A(Ys[n, e])))
                else:
                    val += self.mass * 0.5 * np.sum((Ys[n + 1, e] - Ys[n, e]) ** 2)
        return val

    def grad(self, z):
        n1, k = self.n1, self.k
        Ys = z.reshape(n1 + 1, 3, k)
        g = np.zeros_like(Ys)
        for n in range(n1 + 1):
            As = [self.A(Ys[n, e]) for e in range(3)]
            Es = [expm(a) for a in As]
            g[n] += Ys[n] / self.s0
            Gam = self.c * self.QgradH(Es[0] @ Es[1] @ Es[2])
            gE = [Gam @ (Es[1] @ Es[2]).T, Es[0].T @ Gam @ Es[2].T, (Es[0] @ Es[1]).T @ Gam]
            for e in range(3):
                g[n, e] += self.comp(L_frechet(As[e].T, gE[e]))
            for r, (e, sg, i, j) in enumerate(self.records):
                X = sg * As[e]
                G = expm(X)
                Hm = self.Hrec[r]
                mi, mj, Sj = self.mu[n][i], self.mu[n][j], self.Sg[n][j]
                S2 = Sj + np.outer(mj, mj)
                gG = self.beta[n, r] * Hm @ (G @ S2 - np.outer(mi, mj))   # Frobenius gradient wrt G
                g[n, e] += sg * self.comp(L_frechet(X.T, gG))
        for n in range(n1):
            for e in range(3):
                if self.kin == "defect":
                    Ap, A0 = self.A(Ys[n + 1, e]), self.A(Ys[n, e])
                    Ep, E0 = expm(-Ap), expm(A0)
                    Gam = self.QgradH(Ep @ E0)
                    g[n, e] += self.mass * self.comp(L_frechet(A0.T, Ep.T @ Gam))
                    g[n + 1, e] += -self.mass * self.comp(L_frechet(-Ap.T, Gam @ E0.T))
                else:
                    dlt = Ys[n + 1, e] - Ys[n, e]
                    g[n, e] += -self.mass * dlt
                    g[n + 1, e] += self.mass * dlt
        return g.ravel()

    def K_operator(self):
        """K (quadratic form), source j (linear form), N_0 (source-dependent Hessian part), and the
        bound cond(G) max_{n,e} sum_{records on e or its reversal} beta |J|_F."""
        n1, k = self.n1, self.k
        BA = self.B
        nE = 3 * k
        dim = (n1 + 1) * nE
        Kop = np.zeros((dim, dim))
        jvec = np.zeros(dim)
        N0 = np.zeros((dim, dim))
        Cmat = np.kron(np.ones((1, 3)), np.eye(k))      # loop sum in coordinates
        curr_per_edge = np.zeros((n1 + 1, 3))
        for n in range(n1 + 1):
            blk = slice(n * nE, (n + 1) * nE)
            Kop[blk, blk] += np.eye(nE) / self.s0 + self.c * Cmat.T @ Cmat
            for r, (e, sg, i, j) in enumerate(self.records):
                Hm = self.Hrec[r]
                mi, mj, Sj = self.mu[n][i], self.mu[n][j], self.Sg[n][j]
                S2 = Sj + np.outer(mj, mj)
                Jc = Hm @ (np.outer(mi - mj, mj) - Sj)               # current at zero generators
                b = self.beta[n, r]
                curr_per_edge[n, e] += b * np.linalg.norm(Jc)
                off = n * nE + e * k
                for p in range(k):
                    jvec[off + p] += b * sg * np.trace(Jc.T @ BA[p])
                    for q in range(k):
                        Kop[off + p, off + q] += b * np.trace(Hm @ BA[p] @ S2 @ BA[q].T)
                        N0[off + p, off + q] += -b * 0.5 * np.trace(Jc.T @ (BA[p] @ BA[q] + BA[q] @ BA[p]))
        Lpath = np.zeros((n1 + 1, n1 + 1))
        for n in range(n1):
            Lpath[n, n] += 1
            Lpath[n + 1, n + 1] += 1
            Lpath[n, n + 1] -= 1
            Lpath[n + 1, n] -= 1
        Kop += self.mass * np.kron(Lpath, np.eye(nE))
        return Kop, jvec, N0, self.condG * curr_per_edge.max()


def newton_min(fun_grad, z0, tol=1e-13, maxit=40, h=1e-6):
    z = z0.copy()
    for _ in range(maxit):
        g = fun_grad(z)
        if np.max(np.abs(g)) < tol:
            break
        n = len(z)
        Hm = np.zeros((n, n))
        for a in range(n):
            e = np.zeros(n)
            e[a] = h
            Hm[:, a] = (fun_grad(z + e) - fun_grad(z - e)) / (2 * h)
        Hm = 0.5 * (Hm + Hm.T)
        z = z - np.linalg.solve(Hm, g)
    return z, np.max(np.abs(fun_grad(z)))


def check_E():
    header("E/F. Linearized link equation vs exact stationary history (triangle x 3 episodes)")
    for algebra in ("gl2", "so3"):
        for kin in ("defect", "gaussian"):
            tag = f"{algebra},{kin}"
            print(f"  algebra {algebra}, kinetic variant: {kin}")
            rng = np.random.default_rng(7)
            mdl = TriangleHistory(rng, 0.05, kin, algebra=algebra)
            dim = (mdl.n1 + 1) * 3 * mdl.k
            z = 0.2 * RNG.standard_normal(dim)
            h = 1e-6
            gfd = np.array([(mdl.Phi(z + h * np.eye(dim)[a]) - mdl.Phi(z - h * np.eye(dim)[a])) / (2 * h)
                            for a in range(dim)])
            report(f"[{tag}] analytic gradient of Phi vs FD", np.max(np.abs(gfd - mdl.grad(z))), 1e-7)
            Kop, jvec, N0, nubound = mdl.K_operator()
            g0 = mdl.grad(np.zeros(dim))
            report(f"[{tag}] grad Phi(0) = -j", np.max(np.abs(g0 + jvec)), 1e-12)
            H0 = np.zeros((dim, dim))
            for a in range(dim):
                e = np.zeros(dim)
                e[a] = 1e-6
                H0[:, a] = (mdl.grad(e) - mdl.grad(-e)) / 2e-6
            H0 = 0.5 * (H0 + H0.T)
            report(f"[{tag}] Hess Phi(0) = K + N_0", np.max(np.abs(H0 - Kop - N0)), 1e-7)
            evK = np.linalg.eigvalsh(Kop)
            report(f"[{tag}] K self-adjoint (max asym)", np.max(np.abs(Kop - Kop.T)), 1e-13)
            report(f"[{tag}] min eig K - c_a (K >= anchor precision floor c_a = 1/s0)", evK.min() - 1 / mdl.s0,
                   -1e-12, "ge")
            nN0 = np.max(np.abs(np.linalg.eigvalsh(N0)))
            report(f"[{tag}] ||N_0|| <= cond(G) max_e sum beta |J|_F (bound minus value)", nubound - nN0,
                   -1e-12, "ge")
            print(f"     spec K in [{evK.min():.4f}, {evK.max():.4f}], c_a = {1/mdl.s0:.4f}, "
                  f"||N_0|| = {nN0:.3e}, bound {nubound:.3e}")
            print("     eps      |j|        |w_lin|     |w_* - w_lin|   rel.err   ||N0||     2|j|/c_a   |w_*|")
            rel = []
            ok_ball = True
            for eps in (0.1, 0.03, 0.01, 0.003, 0.001):
                rng = np.random.default_rng(11)
                mdl = TriangleHistory(rng, eps, kin, algebra=algebra)
                Kop, jvec, N0, _ = mdl.K_operator()
                wlin = np.linalg.solve(Kop, jvec)
                wst, gres = newton_min(mdl.grad, wlin)
                err = np.linalg.norm(wst - wlin)
                rel.append((eps, err / np.linalg.norm(wlin), np.linalg.norm(wlin), err, gres))
                nN0 = np.max(np.abs(np.linalg.eigvalsh(N0)))
                ca = 1 / mdl.s0
                if nN0 <= ca / 2 and np.linalg.norm(wst) > 2 * np.linalg.norm(jvec) / ca:
                    ok_ball = False
                print(f"     {eps:.3f}   {np.linalg.norm(jvec):.3e}  {np.linalg.norm(wlin):.3e}   {err:.3e}       "
                      f"{err/np.linalg.norm(wlin):.2e}  {nN0:.2e}   {2*np.linalg.norm(jvec)/ca:.3e}  "
                      f"{np.linalg.norm(wst):.3e}   (|grad| {gres:.1e})")
            slope = np.polyfit(np.log([r_[0] for r_ in rel]), np.log([r_[3] for r_ in rel]), 1)[0]
            report(f"[{tag}] |w_* - w_lin| ~ eps^p with p (expect 2)", abs(slope - 2.0), 0.15)
            report(f"[{tag}] relative error at eps=1e-3", rel[-1][1], 5e-3)
            RESULTS.append((f"[{tag}] |w_*| <= 2|j|/c_a whenever ||N_0|| <= c_a/2", ok_ball))
            print(f"  [{'PASS' if ok_ball else 'FAIL'}] [{tag}] |w_*| <= 2|j|/c_a whenever ||N_0|| <= c_a/2")


# ----------------------------------------------------------------------------------------------
# G. Four-cycle held sheet (prop:obs-slow-model-link-dichotomy) and the Fisher natural gradient
# ----------------------------------------------------------------------------------------------
def check_G():
    header("G. Four-cycle held sheet: Fisher natural gradient of the Gaussian configuration family")
    T = 0.05
    # x = (kbar0..3, mbar0..3, w0..3); residual rows
    def rb(i):
        r = np.zeros(12); r[(i + 1) % 4] += 1; r[i] -= 1; r[8 + i] -= 1; return r

    def rm(i):
        r = np.zeros(12); r[4 + (i + 1) % 4] += 1; r[4 + i] -= 1; r[8 + i] -= 1; return r

    Dm = np.zeros((4, 12))
    for i in range(4):
        Dm[i, i] = 1; Dm[i, 4 + i] = -1
    Rev = 2 * Dm.T @ Dm
    Hs = np.zeros((12, 12))
    for i in (0, 2):        # S^(0): e0 and e2 attended from both ends: V = 2 D_e0 + 2 D_e2
        Hs += 2 * (np.outer(rb(i), rb(i)) + np.outer(rm(i), rm(i)))   # 2 * 1/2 * 2 (second derivative)
    Hs = Hs / 1.0
    # V = 2 * D_e with D_e = 1/2 (rb^2 + rm^2): Hess = 2 * (rb rb^T + rm rm^T)
    Hs = Hs + T * np.eye(12) + T * Rev
    # orthonormal coordinates for edge e0: (kbar^-_0, mbar^-_0, w_0)
    s2 = 1 / np.sqrt(2)
    u1 = np.zeros(12); u1[1] = s2; u1[0] = -s2
    u2 = np.zeros(12); u2[5] = s2; u2[4] = -s2
    u3 = np.zeros(12); u3[8] = 1
    Ublk = np.stack([u1, u2, u3])
    blk = Ublk @ Hs @ Ublk.T
    blk_ref = np.array([[4 + 3 * T, -2 * T, -2 * np.sqrt(2)], [-2 * T, 4 + 3 * T, -2 * np.sqrt(2)],
                        [-2 * np.sqrt(2), -2 * np.sqrt(2), 4 + T]])
    report("held-sheet Hessian block of c08 eq. (obs-cycle-held-blocks) reproduced", np.max(np.abs(blk - blk_ref)), 1e-12)
    v1 = np.zeros(12); v1[1] = s2; v1[0] = s2
    v2 = np.zeros(12); v2[5] = s2; v2[4] = s2
    pb = np.stack([v1, v2]) @ Hs @ np.stack([v1, v2]).T
    report("pair block T[[3,-2],[-2,3]] reproduced", np.max(np.abs(pb - T * np.array([[3, -2], [-2, 3]]))), 1e-12)

    Hinv = np.linalg.inv(Hs)
    x0 = np.concatenate([np.zeros(8), np.ones(4)])

    def field(y):
        mu = y[:12]
        Sg = y[12:].reshape(12, 12)
        Sg = 0.5 * (Sg + Sg.T)
        dmu = -Sg @ Hs @ mu / T
        dS = Sg - Sg @ Hs @ Sg / T
        return np.concatenate([dmu, dS.ravel()])

    y = np.concatenate([x0, (T * Hinv).ravel()])
    dt, tmax = 0.01, 5.0
    devS, devmu, devr = 0.0, 0.0, 0.0
    t = 0.0
    for _ in range(int(tmax / dt)):
        y = rk4(field, y, dt)
        t += dt
        mu = y[:12]
        Sg = y[12:].reshape(12, 12)
        devS = max(devS, np.max(np.abs(Sg - T * Hinv)))
        devmu = max(devmu, np.max(np.abs(mu - np.exp(-t) * x0)))
        devr = max(devr, max(abs(rb(i) @ mu - rm(i) @ mu) for i in range(4)))
    report("stationary-covariance slice invariant: max |Sigma(t) - T H^{-1}|", devS, 1e-10)
    report("mean on the slice: max |mu(t) - e^{-t} x0|", devmu, 1e-9)
    report("belief and model residuals coincide on every edge: max |r^b - r^m|", devr, 1e-10)
    # off the slice: Sigma relaxes to T H^{-1}
    y = np.concatenate([x0, np.eye(12).ravel()])
    for _ in range(int(20.0 / dt)):
        y = rk4(field, y, dt)
    print(f"   from Sigma_0 = I: |Sigma(20) - T H^-1|_max = {np.max(np.abs(y[12:].reshape(12,12) - T*Hinv)):.2e}")

    # contrast: supplied rates (eps_m = eps_w = 0.04), mean flow of c08 at small T
    epsm = 0.04
    Tz = 1e-6
    Hz = Hs - T * np.eye(12) - T * Rev + Tz * np.eye(12) + Tz * Rev
    M = np.diag(np.concatenate([np.ones(4), epsm * np.ones(4), epsm * np.ones(4)]))
    x = x0.copy()
    dt = 0.001
    t = 0.0
    window = []
    while t < 1 / (12 * epsm) + 1e-9:
        x = rk4(lambda z: -M @ Hz @ z, x, dt)
        t += dt
        if t >= 0.25 * np.log(4 / epsm):
            window.append((abs(rb(0) @ x), abs(rm(0) @ x)))
    window = np.array(window)
    print(f"   supplied rates eps_m=eps_w={epsm}: on [log(4/eps)/4, 1/(12 eps)] max|r^b|={window[:,0].max():.4f} "
          f"(<= 2 eps = {2*epsm}), min|r^m|={window[:,1].min():.4f} (>= 1/2)")
    RESULTS.append(("contrast: supplied-rate flow shows belief-agreeing, model-disagreeing window",
                    bool(window[:, 0].max() <= 2 * epsm + 1e-6 and window[:, 1].min() >= 0.5)))


# ----------------------------------------------------------------------------------------------
# H. History prior: h-transform kernels vs Gibbs law (scalar Gaussian)
# ----------------------------------------------------------------------------------------------
def check_H():
    header("H. History prior: backward-function kernels reproduce the Gibbs law; naive kernels do not")
    s2, m, n1 = 1.0, 0.8, 3
    P = np.eye(n1 + 1) / s2
    for n in range(n1):
        P[n, n] += m; P[n + 1, n + 1] += m; P[n, n + 1] -= m; P[n + 1, n] -= m
    Cg = np.linalg.inv(P)
    # backward exponents a_n:  Z_n(w) ~ exp(-a_n w^2 / 2), a_{n1} = 0
    a = np.zeros(n1 + 1)
    p = np.zeros(n1)
    for n in range(n1 - 1, -1, -1):
        p[n] = 1 / s2 + m + a[n + 1]
        a[n] = m - m ** 2 / p[n]
    v0 = 1 / (1 / s2 + a[0])
    # chain: w_{n+1} = (m/p_n) w_n + noise var 1/p_n
    C = np.zeros((n1 + 1, n1 + 1))
    C[0, 0] = v0
    for n in range(n1):
        A = m / p[n]
        C[n + 1, :n + 1] = A * C[n, :n + 1]
        C[:n + 1, n + 1] = C[n + 1, :n + 1]
        C[n + 1, n + 1] = A * A * C[n, n] + 1 / p[n]
    report("composed h-transform chain covariance = Gibbs covariance", np.max(np.abs(C - Cg)), 1e-14)
    # naive chain: root N(0, s2), kernel N(m w/(1/s2+m), 1/(1/s2+m))
    pn = 1 / s2 + m
    Cn = np.zeros((n1 + 1, n1 + 1))
    Cn[0, 0] = s2
    for n in range(n1):
        A = m / pn
        Cn[n + 1, :n + 1] = A * Cn[n, :n + 1]
        Cn[:n + 1, n + 1] = Cn[n + 1, :n + 1]
        Cn[n + 1, n + 1] = A * A * Cn[n, n] + 1 / pn
    print(f"   Gibbs root variance {Cg[0,0]:.6f}, naive-chain root variance {Cn[0,0]:.6f}; "
          f"max cov difference {np.max(np.abs(Cn - Cg)):.4f}")
    report("naive increment kernels give a different law (max cov difference)", np.max(np.abs(Cn - Cg)), 1e-3, "ge")
    # witness of the text: n1 = 1, root precision (1+2m)/(1+m)
    P1 = np.array([[1 + m, -m], [-m, 1 + m]])
    report("n1=1 witness: Gibbs root precision = (1+2m)/(1+m)", abs(1 / np.linalg.inv(P1)[0, 0] - (1 + 2 * m) / (1 + m)), 1e-14)


# ----------------------------------------------------------------------------------------------
# I. Time-like loop defect: expansions
# ----------------------------------------------------------------------------------------------
def check_I():
    header("I. Time-like loop defect: quadratic expansion and the exponential-derivative mass tensor")
    K = 3
    Gf = spd(K, RNG, 1.0, 0.5)
    Gi = np.linalg.inv(Gf)

    def ipG(A, B):
        return np.trace(Gi @ A.T @ Gf @ B)

    def Qdef(Hm):
        D = Hm - np.eye(K)
        return 0.5 * ipG(D, D)

    A0 = RNG.standard_normal((K, K))
    A1 = RNG.standard_normal((K, K))
    print("   t        U(tA1,tA0)/(1/2|tA0-tA1|^2_G)")
    prev = None
    for t in (1e-1, 1e-2, 1e-3, 1e-4):
        val = Qdef(expm(-t * A1) @ expm(t * A0)) / (0.5 * ipG(t * (A0 - A1), t * (A0 - A1)))
        print(f"   {t:.0e}   {val:.10f}")
        prev = val
    report("ratio -> 1 at small generators (t=1e-4)", abs(prev - 1), 1e-3)
    # finite a, small increment: U(a + d, a) / (1/2 |Psi_a d|^2), Psi_a(E) = L(-A,E) e^{A}
    a = 0.8 * RNG.standard_normal((K, K))
    E = RNG.standard_normal((K, K))
    print("   delta    U(a+delta,a)/(1/2|Psi_a delta|^2)    U/(1/2|delta|^2)")
    for t in (1e-2, 1e-3, 1e-4):
        d = t * E
        U = Qdef(expm(-(a + d)) @ expm(a))
        Psi = L_frechet(-a, d) @ expm(a)
        r1 = U / (0.5 * ipG(Psi, Psi))
        r2 = U / (0.5 * ipG(d, d))
        print(f"   {t:.0e}   {r1:.10f}                       {r2:.6f}")
    report("mass tensor at finite generator: ratio -> 1 (t=1e-4)", abs(r1 - 1), 1e-3)
    # Psi_a(E) = int_0^1 e^{-sA} E e^{sA} ds (quadrature check)
    s, w = np.polynomial.legendre.leggauss(30)
    s = 0.5 * (s + 1); w = 0.5 * w
    Pq = sum(wi * expm(-si * a) @ E @ expm(si * a) for si, wi in zip(s, w))
    report("L(-A,E) e^{A} = int_0^1 e^{-sA} E e^{sA} ds", np.max(np.abs(Pq - L_frechet(-a, E) @ expm(a))), 1e-12)


if __name__ == "__main__":
    check_A()
    check_B()
    check_C()
    check_D()
    check_E()
    check_G()
    check_H()
    check_I()
    header("SUMMARY")
    npass = sum(ok for _, ok in RESULTS)
    print(f"  {npass}/{len(RESULTS)} checks passed")
    for name, ok in RESULTS:
        if not ok:
            print(f"  FAILED: {name}")
