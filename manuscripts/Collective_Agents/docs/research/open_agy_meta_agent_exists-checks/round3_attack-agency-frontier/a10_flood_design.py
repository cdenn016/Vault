r"""Attack run a10: a flooding design D5 = D1 with Rs = 1 (psi = g_max(1) + 0.06) and attention habits
E(mate) = 1 - 3 eps, E(0) = E(o1) = E(o2) = eps.  Checks only what changes relative to D1: N_hab (attention ~ mate,
slots Bin(8, 1/2) at Rs = 1), the members' policy law, and the index under R-outsider.  (Full model, mechanism
medium, N_pr and inference are unchanged because slots stay closed; memory: a9 exact MI 4.8e-3 <= 0.02.)
Declared expectation: N_hab about 1.25 (< b = 2.493); index -> 1 - O(eps) under R-outsider.
NEGATIVE CONTROL: eps = 1/4 (uniform habits) must give the D1 formula m/(m+2) = 0.8."""
import time
import numpy as np
from scipy.optimize import minimize_scalar
from mylib import Par, steady, gains, efe, info_x, lbin, mc
t0 = time.time()
base = Par(Rs=1.0)
g = max(info_x(base, steady(base, c, 0), cc, 1) - info_x(base, steady(base, c, 0), cc, 0) for c in (0, 1) for cc in (0, 1))
par = base.w(psi=g + 0.06)
print(f"D5: Rs = 1, g_max {g:.5f}, psi {par.psi:.5f}")
o = mc(par, "hab", B=3000, T=500, burn=150, seed=101, q_mate=(1.0, 1.0))
print(f"N_hab (attention on the mate, slots from habits): r {o['r']:.4f} +- {o['se']:.4f}  ({time.time()-t0:.1f}s)")
m = par.m; lb = lbin(m); Pm = steady(par, 1, 0)
_, _, _, _, Pp = gains(par, Pm, 1, 0); vstar = Pp[0, 0]
for eps in (0.25, 1e-2, 1e-4, 1e-8):
    E = np.array([eps, 1 - 3 * eps, eps, eps]); cset = [0, 1, 0, 0]
    lw = np.array([[np.log(E[s]) + lb[k] - par.gamma * efe(par, Pm, cset[s], k) for k in range(m + 1)] for s in range(4)])
    lw -= lw.max(); Pk = np.exp(lw); Pk /= Pk.sum(); pa = Pk.sum(1)
    KLa = 2 * float(np.sum(pa * np.log(pa / E)))
    pk = Pk / pa[:, None]
    lpk = np.where(pk > 0, np.log(np.maximum(pk, 1e-300)) - lb[None, :], 0.0)
    KLs = 2 * float(np.sum(pa[:, None] * pk * (lpk + m * np.log(2.0))))
    K = np.arange(2 * m + 1); lb2 = lbin(2 * m)
    pK = sum(pa[i] * pa[j] * np.convolve(pk[i], pk[j]) for i in range(4) for j in range(4))
    Elp = 2 * float(np.sum(pa[:, None] * pk * lpk))
    def mis(gm):
        GC = -0.5 * np.log1p(K * vstar / par.Rs) + par.psi * K
        lZ = np.logaddexp.reduce(lb2 - 2 * m * np.log(2.0) - gm * GC)
        return KLa + Elp + 2 * m * np.log(2.0) + gm * float(np.sum(pK * GC)) + lZ
    r = minimize_scalar(lambda z: mis(np.exp(z)), bounds=(-12, 9), method="bounded", options=dict(xatol=1e-10))
    f = min(float(r.fun), mis(0.0))
    print(f"eps = {eps:g}: P(mate) = {pa[1]:.10f}; KL_a {KLa:.3e}; KL_s|a {KLs:.4f}; index (R-outsider, habits fixed) "
          f"{1 - f / (KLa + KLs):.6f}")
print(f"({time.time()-t0:.1f}s)")
