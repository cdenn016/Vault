"""Symbolic checks (sympy) for the passive action, the comparison-space redundancy,
and the loop-trace word polynomial."""
import sympy as sp

# 1. passive action leaves reference moments invariant (generic 2x2 symbols)
g = sp.Matrix(2, 2, sp.symbols("g0:4"))
U = sp.Matrix(2, 2, sp.symbols("u0:4"))
m = sp.Matrix(2, 1, sp.symbols("m0:2"))
s11, s12, s22 = sp.symbols("s11 s12 s22")
S = sp.Matrix([[s11, s12], [s12, s22]])
xi = U.inv() * m
C = U.inv() * S * U.inv().T
xi_p = (g * U).inv() * (g * m)
C_p = (g * U).inv() * (g * S * g.T) * (g * U).inv().T
print("1a xi invariant:", sp.simplify(xi_p - xi) == sp.zeros(2, 1))
print("1b C invariant:", sp.simplify(C_p - C) == sp.zeros(2, 2))

# 2. scalar comparison space r = 1: KL invariant under (a S_Q, a S_K), not under (a S_Q, S_K / a)
a, x, y, v, w = sp.symbols("a x y v w", positive=True)


def kl1(m0, v0, m1, v1):
    return sp.Rational(1, 2) * (v0 / v1 + (m1 - m0) ** 2 / v1 - 1 + sp.log(v1) - sp.log(v0))


base = kl1(x, v, y, w)
co = kl1(a * x, a ** 2 * v, a * y, a ** 2 * w)
contra = kl1(a * x, a ** 2 * v, y / a, w / a ** 2)
print("2a cogredient residual:", sp.simplify(sp.expand_log(co - base, force=True)))
print("2b contragredient residual is zero:", sp.simplify(sp.expand_log(contra - base, force=True)) == 0)

# 3. loop trace of routed links = word polynomial in routing weights (H=2, 2x2, triangle)
M1 = sp.Matrix(2, 2, sp.symbols("p0:4"))
M2 = sp.Matrix(2, 2, sp.symbols("q0:4"))
b = {e: sp.symbols("b1_%s b2_%s" % (e, e)) for e in ("01", "12", "20")}
A = {e: b[e][0] * M1 + b[e][1] * M2 for e in b}
Us = [sp.Matrix(2, 2, sp.symbols("w%d_0:4" % k)) for k in range(3)]
Cl = {"01": Us[0] * A["01"] * Us[1].inv(), "12": Us[1] * A["12"] * Us[2].inv(),
      "20": Us[2] * A["20"] * Us[0].inv()}
lhs = (Cl["01"] * Cl["12"] * Cl["20"]).trace()
poly = 0
Ms = (M1, M2)
for h1 in range(2):
    for h2 in range(2):
        for h3 in range(2):
            poly += b["01"][h1] * b["12"][h2] * b["20"][h3] * (Ms[h1] * Ms[h2] * Ms[h3]).trace()
print("3 loop trace equals word polynomial:", sp.simplify(sp.together(lhs - poly)) == 0)
