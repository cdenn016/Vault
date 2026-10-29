r"""Interval certificates for the reduced gap equation and the union radius of Item_7_formation_feedback.tex.

Outward-rounded interval arithmetic (mpmath.iv, 30 digits) with adaptive bisection, single thread. For
    F(d) = rho (s - d) - 2 w_n(d) d,  w_n(d) = n e^{-a d^2} / (n - 1 + n e^{-a d^2}),  a = n lam / (2T),
a subinterval is accepted when the enclosure of F excludes zero, or when the enclosure of F' excludes zero (then F
is strictly monotone there and has a zero exactly when its endpoint values, enclosed as point intervals, differ in
sign). For d >= s both terms of F are negative, so the zeros in (0, infinity) are those in (0, s), and F(0) = rho s > 0.
The radius function is Gamma_n(d) = log((2n-1)/pp) - 2 log(n-1+n e^{-n lam d^2/(2T)}) - n lam d^2/(4T).
Blocks print (27a)-(27e).
"""
import os
os.environ.setdefault("OMP_NUM_THREADS", "1")
from mpmath import iv, mp

iv.dps = 30; mp.dps = 30
LO = lambda x: mp.mpf(iv.mpf(x)._mpi_[0])
HI = lambda x: mp.mpf(iv.mpf(x)._mpi_[1])
lam, T, rho, ps = 6, 1, iv.mpf("0.005"), iv.mpf("0.05")
pp = (1 - ps) / 11


def F(d, s, n=3):
    a = iv.mpf(n) * lam / (2 * T); e = n * iv.exp(-a * d * d)
    return rho * (s - d) - 2 * e / ((n - 1) + e) * d


def dF(d, s, n=3):
    a = iv.mpf(n) * lam / (2 * T); e = n * iv.exp(-a * d * d); w = e / ((n - 1) + e)
    dw = -2 * a * d * w * (n - 1) / ((n - 1) + e)          # derivative of w_n
    return -rho - 2 * w - 2 * d * dw


def pos(x): return x.a > 0
def neg(x): return x.b < 0


def zeros(s, n=3, lo="0", hi=None, depth=60):
    r"""Certified zero count of F on [lo, hi] with enclosing brackets."""
    hi = s if hi is None else hi
    lo, hi = str(lo), str(hi)
    stack = [(LO(lo), HI(hi), 0)]; brackets = []; boxes = 0
    while stack:
        a_, b_, k = stack.pop(); X = iv.mpf([a_, b_]); boxes += 1
        Fx = F(X, iv.mpf(s), n)
        if pos(Fx) or neg(Fx): continue
        D = dF(X, iv.mpf(s), n)
        if pos(D) or neg(D):
            fa, fb = F(iv.mpf(a_), iv.mpf(s), n), F(iv.mpf(b_), iv.mpf(s), n)
            if (pos(fa) and neg(fb)) or (neg(fa) and pos(fb)):
                if b_ - a_ > mp.mpf("1e-9") and k < depth:
                    m = (a_ + b_) / 2; stack += [(a_, m, k + 1), (m, b_, k + 1)]
                else:
                    brackets.append((float(a_), float(b_)))
                continue
            if (pos(fa) and pos(fb)) or (neg(fa) and neg(fb)): continue
        if k >= depth: raise RuntimeError("no decision on [%s, %s]" % (a_, b_))
        m = (a_ + b_) / 2; stack += [(a_, m, k + 1), (m, b_, k + 1)]
    return sorted(brackets), boxes


def band(f, lo, hi, sign, bound, depth=40):
    lo, hi = str(lo), str(hi)
    r"""Certify sign*(f(x) - bound) > 0 on [lo, hi]; returns the number of boxes used."""
    stack = [(LO(lo), HI(hi), 0)]; boxes = 0
    while stack:
        a_, b_, k = stack.pop(); boxes += 1; y = f(iv.mpf([a_, b_]))
        if (sign < 0 and (y - bound).b < 0) or (sign > 0 and (y - bound).a > 0): continue
        if k >= depth: return None
        m = (a_ + b_) / 2; stack += [(a_, m, k + 1), (m, b_, k + 1)]
    return boxes


def Gam(d, n=3):
    a = iv.mpf(n) * lam / (2 * T)
    return iv.log((2 * n - 1) / pp) - 2 * iv.log((n - 1) + n * iv.exp(-a * d * d)) - a / 2 * d * d


fmt = lambda br: [f"({a:.7f}, {b:.7f})" for a, b in br]
br, nb = zeros("1.1")
print("(27a) n = 3, s = 1.1: zeros in (0, inf):", len(br), fmt(br), f"[{nb} boxes]")
du_lo, du_hi = br[1]; ds_lo, ds_hi = br[2]
s11 = iv.mpf("1.1")
for lo, hi, sg, bd, name in ((0.12909, du_lo - 0.005, -1, -3.2e-5, "F < -3.2e-5"),
                             (du_hi + 0.005, ds_lo - 0.005, 1, 1.6e-5, "F > 1.6e-5"),
                             (ds_hi + 0.005, 1.6, -1, -1.7e-5, "F < -1.7e-5")):
    print(f"      {name} on [{lo:.5f}, {hi:.5f}]:", band(lambda X: F(X, s11), lo, hi, sg, bd) is not None)
print("      F' > 0.005 on [d_u - 0.005, d_u + 0.005]:",
      band(lambda X: dF(X, s11), du_lo - 0.005, du_hi + 0.005, 1, 0.005) is not None,
      "; F' < -0.002 on [d_s - 0.005, d_s + 0.005]:",
      band(lambda X: dF(X, s11), ds_lo - 0.005, ds_hi + 0.005, -1, -0.002) is not None)
for s in ("1.2", "1.3", "1.0"):
    br_, _ = zeros(s); print(f"(27b) n = 3, s = {s}: zeros:", len(br_), fmt(br_))
for n in (2, 4, 6):
    br_, _ = zeros("1.1", n=n); print(f"(27c) n = {n}, s = 1.1: zeros:", len(br_), fmt(br_))
for s in ("1.0722", "1.0723"):
    br_, _ = zeros(s); print(f"(27d) n = 3, s = {s}: zeros:", len(br_))
g1, g2 = Gam(iv.mpf("0.76849")), Gam(iv.mpf("0.76851"))
print("(27e) Gamma_3(0.76849) > 0:", pos(g1), "; Gamma_3(0.76851) < 0:", neg(g2),
      "; Gamma_3 < -1.5 on [0.96804, 1.6]:", band(Gam, 0.96804, 1.6, -1, -1.5) is not None,
      "; Gamma_3 < -2.5 on [1.09, 1.11]:", band(Gam, 1.09, 1.11, -1, -2.5) is not None)
