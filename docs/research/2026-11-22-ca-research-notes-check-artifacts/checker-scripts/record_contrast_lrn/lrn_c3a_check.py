"""C3(a): 1D Schwinger integral (re-typed, scipy.quad in t) vs direct 3D quadrature of the definition, anisotropic P, K=3.
Two parameter points plus a planted error (drop the 2*vXY^2 Isserlis term)."""
import math, numpy as np
from scipy import integrate
import importlib.util, sys, io, contextlib
spec = importlib.util.spec_from_file_location("c3", "lrn_c3_check.py")
src = open("lrn_c3_check.py").read().split("print(\"f_alpha quadrature")[0]
ns = {}
exec(src, ns)
quad_aniso_K3 = ns["quad_aniso_K3"]

def schwinger(P, H, m, u, Rc, sig, plant=False):
    ev, U = np.linalg.eigh(P)
    s = sig**2 * ev
    hb = U.T @ (U @ np.diag(np.sqrt(ev)) @ U.T @ H)
    zb = U.T @ (U @ np.diag(1 / np.sqrt(ev)) @ U.T @ m)
    c0 = float(H @ m) - u
    def f(t):
        invd = 1 / (1 + 2 * t * s)
        Z = np.prod(np.sqrt(invd)) * math.exp(-t * np.sum(hb**2 * invd))
        mu = hb * invd; sg = s * invd
        mX = np.sum(hb * mu); mY = np.sum(zb * mu)
        vXX = np.sum(hb**2 * sg); vXY = np.sum(hb * zb * sg); vYY = np.sum(zb**2 * sg)
        EX = mX; EXY = mX * mY + vXY; EX2 = mX**2 + vXX
        EX2Y = mX**2 * mY + vXX * mY + 2 * mX * vXY
        EX2Y2 = (mX**2 + vXX) * (mY**2 + vYY) + (0 if plant else 2 * vXY**2) + 4 * mX * mY * vXY
        return Z * (2 * c0 * (u * EX - EXY) + t * ((u**2 + Rc) * EX2 - 2 * u * EX2Y + EX2Y2))
    val, err = integrate.quad(f, 0, np.inf, epsabs=1e-13, epsrel=1e-13, limit=400)
    return c0**2 + val

A = np.array([[1.2, 0.3, -0.2], [0.0, 0.8, 0.4], [0.0, 0.0, 1.6]]); P = A @ A.T
for (H, m, u, Rc, sig) in [(np.array([0.9, -0.5, 0.7]), np.array([0.4, 0.8, -0.6]), 0.5, 0.6, 0.7),
                           (np.array([0.3, 0.2, -0.4]), np.array([1.0, -0.7, 0.2]), -0.8, 0.25, 1.4)]:
    d = quad_aniso_K3(P, H, m, u, Rc, sig)
    s1 = schwinger(P, H, m, u, Rc, sig)
    s2 = schwinger(P, H, m, u, Rc, sig, plant=True)
    print(f"direct3D={d:.11f}  Schwinger1D={s1:.11f}  diff={abs(d-s1):.2e}  planted(drop 2vXY^2) diff={abs(d-s2):.2e}")
