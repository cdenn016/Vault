r"""Attack run a7: the padding lever (m costly private slots, Rs = 10 m / 8 so that the all-open precision and the
N_hab slot precision stay at D1's values) under the LITERAL eta_C (non-members' relays are slots with calibrated
V_o), against the candidate's R-outsider formula m/(m+2).
Declared expectation: index 0 for m = 8 (a4); positive once psi * m exceeds E_E[I_att] (about 1.09 nats at V_o = 1),
i.e. m >= 17; tends to 1 slowly (misfit ~ log m against a denominator ~ m).
NEGATIVE CONTROL: V_o = 0 must give m/(m+2)."""
import time
import numpy as np
from scipy.optimize import minimize_scalar
from mylib import Par, steady, gains, efe, info_x, lbin

t0 = time.time()


def index_lit(m, Vo):
    base = Par(m=m, Rs=10.0 * m / 8.0)
    gmax = 0.0
    for c in (0, 1):
        Pm_ = steady(base, c, 0)
        for cc in (0, 1):
            gmax = max(gmax, info_x(base, Pm_, cc, 1) - info_x(base, Pm_, cc, 0))
    par = base.w(psi=gmax + 0.06)
    Pm = steady(par, 1, 0)
    _, _, _, _, Pp = gains(par, Pm, 1, 0)
    vstar = Pp[0, 0]
    lb = lbin(m)
    sets = ["0", "mate", "o1", "o2"]; cset = [0, 1, 0, 0]
    ks = np.arange(m + 1)
    lw = np.array([[lb[k] - par.gamma * efe(par, Pm, cset[s], k) for k in ks] for s in range(4)])
    lw -= lw.max(); Pk = np.exp(lw); Pk /= Pk.sum(); pa = Pk.sum(1)
    with np.errstate(divide="ignore", invalid="ignore"):
        pk_a = Pk / pa[:, None]
        lpk = np.where(pk_a > 0, np.log(pk_a) - lb[None, :], 0.0)       # log prob of one pattern with count k
    KLa1 = float(np.sum(pa * np.log(4 * pa)))
    KLs1 = float(np.sum(pa[:, None] * pk_a * (lpk + m * np.log(2.0))))
    den = 2 * (KLa1 + KLs1)
    I = np.zeros((4, 4))
    for i in range(4):
        for j in range(4):
            for o in (2, 3):
                no = (i == o) + (j == o)
                if no:
                    I[i, j] += 0.5 * np.log1p(no * Vo / par.Rc)
    K = np.arange(2 * m + 1); lb2 = lbin(2 * m)
    W = pa[:, None] * pa[None, :]
    # E over (a1,a2) of E[ln P(s1|a1) + ln P(s2|a2)] and of the actual law of K = k1 + k2
    Elp = float(np.sum(W * (np.sum(pk_a * lpk, 1)[:, None] + np.sum(pk_a * lpk, 1)[None, :])))
    pK = np.zeros(2 * m + 1)
    for i in range(4):
        for j in range(4):
            pK += W[i, j] * np.convolve(pk_a[i], pk_a[j])

    def mis(g):
        la = np.log(1 / 16) + g * I; la -= np.logaddexp.reduce(la.ravel())
        att = float(np.sum(W * (np.log(W) - la)))
        GC = -0.5 * np.log1p(K * vstar / par.Rs) + par.psi * K
        lZ = np.logaddexp.reduce(lb2 - 2 * m * np.log(2.0) - g * GC)
        slot = Elp + 2 * m * np.log(2.0) + g * float(np.sum(pK * GC)) + lZ
        return att + slot
    r = minimize_scalar(lambda z: mis(np.exp(z)), bounds=(-12, 9), method="bounded", options=dict(xatol=1e-10))
    f = min(float(r.fun), mis(0.0))
    return 1 - f / den, float(np.exp(r.x)), par.psi


for m in (8, 16, 17, 18, 24, 32, 64, 128, 256, 1024):
    i0, _, psi = index_lit(m, 0.0)
    i1, g1, _ = index_lit(m, 1.0)
    i2, g2, _ = index_lit(m, 1.263)
    print(f"m={m:5d} Rs={10 * m / 8:7.1f} psi {psi:.5f}: V_o=0 index {i0:.5f} (m/(m+2) = {m / (m + 2):.5f}); "
          f"V_o=1 {i1:.5f} (gamma_C* {g1:.3g}); V_o=1.263 {i2:.5f} (gamma_C* {g2:.3g})")
print(f"({time.time() - t0:.1f}s)")
