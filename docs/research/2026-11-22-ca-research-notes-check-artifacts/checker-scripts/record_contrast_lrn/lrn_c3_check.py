"""Independent check of open_lrn_noncentral C3 (r_c = 1 closed forms).

Channels (none of them is the Schwinger t-integral used by the stored script):
  Q: direct quadrature of the defining expectation over the Gaussian code row in
     spherical coordinates (3 effective dimensions after symmetry reduction).
  MC: brute-force Monte Carlo from the definitions (K = 5, finite variance).
The closed form under test is re-typed here from the note / stored script.
"""
from __future__ import annotations
import math
import numpy as np
from scipy import special

rng = np.random.default_rng(7)


def f_alpha(alpha: float, lam: float) -> float:
    # f_alpha(lam) = int_0^1 (1-v)^(alpha-1) e^{-lam v} dv, evaluated by quadrature here (not hyp1f1)
    x, w = np.polynomial.legendre.leggauss(200)
    # substitute v = 1 - s^m to remove the endpoint singularity for alpha < 1
    m = 4
    s = 0.5 * (x + 1.0)
    v = 1.0 - s**m
    return float(np.sum(0.5 * w * (s ** (m * (alpha - 1.0))) * np.exp(-lam * v) * m * s ** (m - 1)))


def closed_form(K: int, H: np.ndarray, m: np.ndarray, u: float, Rc: float, sig: float, plant: str = "") -> float:
    h2 = float(H @ H)
    lam = h2 / (2 * sig**2)
    Hm = float(H @ m)
    mperp2 = float(m @ m) - Hm**2 / h2
    f0 = f_alpha(K / 2 - 1, lam)
    f1 = (1 - (K / 2 - 1) * f0) / lam
    f2 = (1 - (K / 2) * f1) / lam
    cR = 0.5 * lam * ((K - 1) * f1 - (K - 3) * f0)
    cu = cR - 2 * lam * f1 + 1
    cpar = 0.25 * (K**2 - 1) * (f1 - f2)
    cperp = 0.25 * (K + 1) * f2 - 0.25 * (K - 1) * f1
    cpu = 0.25 * (K - 1) * (K - 2) * (f1 - f0)
    if plant == "cperp_sign":
        cperp = -cperp
    if plant == "cpar_K2":
        cpar = 0.25 * (K**2) * (f1 - f2)
    return cR * Rc + cu * u**2 + cpar * Hm**2 + cperp * h2 * mperp2 + 2 * cpu * Hm * u


def quad_isotropic(K: int, p: float, H: np.ndarray, m: np.ndarray, u: float, Rc: float, sig: float,
                   nr: int = 260, nt: int = 140, nph: int = 140) -> float:
    """E[psi^2 | m,u] for P = p I_K, r_c = 1, by direct quadrature over the code row g = Hhat^T.
    Coordinates: g1 along H, g2 along m_perp, rho = norm of the remaining K-2 coordinates.
    psi0 = c0 + (H.g)(u - g.m)/|g|^2 (p cancels), noise part Rc (H.g)^2/|g|^4."""
    h = float(np.linalg.norm(H))
    Hm = float(H @ m)
    mpar = Hm / h
    mperp = math.sqrt(max(float(m @ m) - mpar**2, 0.0))
    c0 = Hm - u
    Rmax = h + 12 * sig
    xr, wr = np.polynomial.legendre.leggauss(nr)
    r = 0.5 * Rmax * (xr + 1); wr = 0.5 * Rmax * wr
    xt, wt = np.polynomial.legendre.leggauss(nt)
    th = 0.5 * math.pi * (xt + 1); wt = 0.5 * math.pi * wt
    xp, wp = np.polynomial.legendre.leggauss(nph)
    ph = 0.5 * math.pi * (xp + 1); wp = 0.5 * math.pi * wp          # phi in [0, pi]
    R, TH, PH = np.meshgrid(r, th, ph, indexing="ij")
    g1 = R * np.cos(TH); g2 = R * np.sin(TH) * np.cos(PH); rho = R * np.sin(TH) * np.sin(PH)
    S = R**2
    X = h * g1
    Y = mpar * g1 + mperp * g2
    psi0 = c0 + X * (u - Y) / S
    F = psi0**2 + Rc * X**2 / S**2
    dof = K - 2
    dens12 = np.exp(-((g1 - h) ** 2 + g2**2) / (2 * sig**2)) / (2 * math.pi * sig**2)
    dens_rho = rho ** (dof - 1) * np.exp(-rho**2 / (2 * sig**2)) / (2 ** (dof / 2 - 1) * math.gamma(dof / 2) * sig**dof)
    jac = R**2 * np.sin(TH)
    W3 = wr[:, None, None] * wt[None, :, None] * wp[None, None, :]
    return float(np.sum(W3 * jac * dens12 * dens_rho * F))


def quad_aniso_K3(P: np.ndarray, H: np.ndarray, m: np.ndarray, u: float, Rc: float, sig: float,
                  nr: int = 300, nt: int = 160, nph: int = 160) -> float:
    """Direct 3D quadrature over the code row g ~ N(H^T, sig^2 I_3) for general P (K = 3)."""
    c0 = float(H @ m) - u
    Rmax = float(np.linalg.norm(H)) + 12 * sig
    xr, wr = np.polynomial.legendre.leggauss(nr)
    r = 0.5 * Rmax * (xr + 1); wr = 0.5 * Rmax * wr
    xt, wt = np.polynomial.legendre.leggauss(nt)
    th = 0.5 * math.pi * (xt + 1); wt = 0.5 * math.pi * wt
    ph = (np.arange(nph) + 0.5) * 2 * math.pi / nph; wp = np.full(nph, 2 * math.pi / nph)
    R, TH, PH = np.meshgrid(r, th, ph, indexing="ij")
    G = np.stack([R * np.sin(TH) * np.cos(PH), R * np.sin(TH) * np.sin(PH), R * np.cos(TH)], axis=-1)
    PG = G @ P
    S = np.einsum("...k,...k->...", PG, G)
    X = PG @ H            # H P g
    Y = G @ m             # Hhat m
    psi0 = c0 + X * (u - Y) / S
    F = psi0**2 + Rc * X**2 / S**2
    dens = np.exp(-np.sum((G - H) ** 2, axis=-1) / (2 * sig**2)) / (2 * math.pi * sig**2) ** 1.5
    W3 = wr[:, None, None] * wt[None, :, None] * wp[None, None, :]
    return float(np.sum(W3 * R**2 * np.sin(TH) * dens * F))


def schwinger_1d(P, H, m, u, Rc, sig):
    """Note's C3(a) representation, re-typed, integrated with my own substitution v = 2 t sbar/(1+2 t sbar)."""
    ev, U = np.linalg.eigh(P)
    s = sig**2 * ev
    hb = U.T @ (U @ np.diag(np.sqrt(ev)) @ U.T @ H)
    zb = U.T @ (U @ np.diag(1 / np.sqrt(ev)) @ U.T @ m)
    c0 = float(H @ m) - u
    sbar = float(np.mean(s))
    x, w = np.polynomial.legendre.leggauss(400)
    v = 0.5 * (x + 1); w = 0.5 * w
    t = v / (2 * sbar * (1 - v)); dt = 1 / (2 * sbar * (1 - v) ** 2)
    tot = 0.0
    for tk, wk, dk in zip(t, w, dt):
        invd = 1 / (1 + 2 * tk * s)
        Z = np.prod(np.sqrt(invd)) * math.exp(-tk * np.sum(hb**2 * invd))
        mu = hb * invd; sg = s * invd
        mX = np.sum(hb * mu); mY = np.sum(zb * mu)
        vXX = np.sum(hb**2 * sg); vXY = np.sum(hb * zb * sg); vYY = np.sum(zb**2 * sg)
        EX = mX; EXY = mX * mY + vXY; EX2 = mX**2 + vXX
        EX2Y = mX**2 * mY + vXX * mY + 2 * mX * vXY
        EX2Y2 = (mX**2 + vXX) * (mY**2 + vYY) + 2 * vXY**2 + 4 * mX * mY * vXY
        tot += wk * dk * Z * (2 * c0 * (u * EX - EXY) + tk * ((u**2 + Rc) * EX2 - 2 * u * EX2Y + EX2Y2))
    return c0**2 + tot


def mc(P, H, m, u, Rc, sig, n):
    K = len(H)
    W = rng.standard_normal((n, K))
    Hh = H[None, :] + sig * W
    HhP = Hh @ P
    S = np.einsum("nk,nk->n", HhP, Hh)
    HO = (HhP @ H) / S
    psi0 = (H @ m - u) + HO * (u - Hh @ m)
    x = psi0**2 + Rc * HO**2
    return float(x.mean()), float(x.std(ddof=1) / math.sqrt(n))


print("f_alpha quadrature vs scipy hyp1f1/alpha:", abs(f_alpha(0.5, 1.3) - special.hyp1f1(1, 1.5, -1.3) / 0.5),
      abs(f_alpha(1.5, 2.2) - special.hyp1f1(1, 2.5, -2.2) / 1.5))

# Point 1: registered test instance (a): K=3 isotropic
H = np.array([1.1, -0.85, 0.6]); m = np.array([0.6, 0.3, 0.0]); u, Rc, sig, p = -0.75, 0.42, 0.58, 1.9
cf = closed_form(3, H, m, u, Rc, sig)
q1 = quad_isotropic(3, p, H, m, u, Rc, sig)
q1b = quad_isotropic(3, p, H, m, u, Rc, sig, nr=200, nt=100, nph=100)
q1c = quad_aniso_K3(p * np.eye(3), H, m, u, Rc, sig)
print(f"P1 K=3 iso: closed={cf:.12f}  quad(sym-reduced)={q1:.12f} (coarser grid {q1b:.12f})  quad(full 3D)={q1c:.12f}  note=0.559329501770")
for pl in ["cperp_sign", "cpar_K2"]:
    print(f"   planted {pl}: closed_wrong={closed_form(3, H, m, u, Rc, sig, pl):.12f}  gap={abs(closed_form(3, H, m, u, Rc, sig, pl)-q1):.3e}")

# Point 2: K=4 isotropic, different parameters, moderate/large sigma_H
H = np.array([0.7, 0.2, -0.4, 0.9]); m = np.array([-0.5, 1.1, 0.4, 0.3]); u, Rc, sig, p = 0.9, 0.8, 1.1, 0.6
cf = closed_form(4, H, m, u, Rc, sig)
q2 = quad_isotropic(4, p, H, m, u, Rc, sig)
lam = float(H @ H) / (2 * sig**2)
cR_el = 1 + 0.5 * math.exp(-lam) - 1.5 * (1 - math.exp(-lam)) / lam
cu_el = 0.5 * math.exp(-lam) + (1 - math.exp(-lam)) / (2 * lam)
print(f"P2 K=4 iso: closed={cf:.12f}  quad={q2:.12f}  diff={abs(cf-q2):.2e}")
print(f"   K=4 elementary c_R,c_u check (m=0): closed={closed_form(4,H,0*m,u,Rc,sig):.12f}  elementary={Rc*cR_el+u*u*cu_el:.12f}")
print(f"   planted cperp_sign gap={abs(closed_form(4, H, m, u, Rc, sig, 'cperp_sign')-q2):.3e}")

# Point 3: K=5 isotropic, small sigma_H relative to |H|, MC from definitions (finite variance) and quadrature
H = np.array([1.5, -0.3, 0.8, 0.1, -1.0]); m = np.array([0.2, -0.9, 0.5, 0.7, 0.4]); u, Rc, sig, p = -0.4, 0.3, 0.9, 2.3
cf = closed_form(5, H, m, u, Rc, sig)
q3 = quad_isotropic(5, p, H, m, u, Rc, sig)
mm, se = mc(p * np.eye(5), H, m, u, Rc, sig, 3_000_000)
print(f"P3 K=5 iso: closed={cf:.10f}  quad={q3:.10f}  MC={mm:.6f}+/-{se:.1e} (z={(mm-cf)/se:+.2f})")
print(f"   planted cpar_K2: z={(mm-closed_form(5, H, m, u, Rc, sig, 'cpar_K2'))/se:+.1f}")

# Point 4: C3(a) anisotropic K=3: direct 3D quadrature vs the 1D Schwinger integral
A = np.array([[1.2, 0.3, -0.2], [0.0, 0.8, 0.4], [0.0, 0.0, 1.6]])
P = A @ A.T
H = np.array([0.9, -0.5, 0.7]); m = np.array([0.4, 0.8, -0.6]); u, Rc, sig = 0.5, 0.6, 0.7
q4 = quad_aniso_K3(P, H, m, u, Rc, sig)
q4b = quad_aniso_K3(P, H, m, u, Rc, sig, nr=220, nt=120, nph=120)
s4 = schwinger_1d(P, H, m, u, Rc, sig)
print(f"P4 K=3 aniso (C3a): direct3D={q4:.11f} (coarser {q4b:.11f})  Schwinger1D={s4:.11f}  diff={abs(q4-s4):.2e}  iso-formula(wrong here)={closed_form(3,H,m,u,Rc,sig):.6f}")

# Edge regimes of the isotropic closed form: sigma_H -> 0 gives Rc, sigma_H -> infinity limit
H = np.array([1.0, 0.5, -0.5]); m = np.array([0.3, -0.2, 0.9]); u, Rc = 0.7, 0.5
print("edge sigma_H=1e-2:", closed_form(3, H, m, u, Rc, 1e-2), " (-> Rc = 0.5)")
big = closed_form(3, H, m, u, Rc, 60.0)
K = 3; Hm = float(H @ m)
lim = u**2 - 2 * ((K - 1) / K) * Hm * u + ((K - 1) / (K * (K - 1) * (K + 2))) * float(m @ m) * float(H @ H) + ((K - 1) * (K * K - 2) / (K * (K - 1) * (K + 2))) * Hm**2
print("edge sigma_H=60:", big, " note's C5(b)-type limit (r_c=1 Haar-projector moments):", lim)
