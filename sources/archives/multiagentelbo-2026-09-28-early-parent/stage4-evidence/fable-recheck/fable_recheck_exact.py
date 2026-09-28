r"""Independent (Fable 5.1) exact recheck of the four-cycle construction.

Written from the theory sources only (c13_formation.tex
def:rg-formation-cycle-experiment and ca_formation_proofs.tex, matching sector),
without reading the author's stage4_cycle_exact.py.

Coordinates x = (k_0..k_3, m_0..m_3, w_0..w_3). Edge e_i runs from i to i+1 (mod 4),
r^b_i = k_{i+1} - k_i - w_i, r^m_i = m_{i+1} - m_i - w_i,
D_{e_i} = (1/2)[(r^b_i)^2 + (r^m_i)^2], V_S = \sum_i D_{e(i,S_i)}.
R_ev = 2 D^T D with D x = k - m, Omega = I + R_ev, K_M = H_M + T Omega.
"""
from __future__ import annotations

import sympy as sp
from sympy import Matrix, Rational, eye, exp, sqrt, symbols, zeros

T = symbols("T", positive=True)
t = symbols("t", positive=True)
N = 12

k = sp.symbols("k0:4")
m = sp.symbols("m0:4")
w = sp.symbols("w0:4")
X = list(k) + list(m) + list(w)
xvec = Matrix(X)

FAILS = 0
COUNT = 0


def check(label: str, cond: bool) -> None:
    global FAILS, COUNT
    COUNT += 1
    if not cond:
        FAILS += 1
    print(f"[{'PASS' if cond else 'FAIL'}] {label}")


def a_b(i: int) -> Matrix:
    v = zeros(N, 1)
    v[(i + 1) % 4] += 1
    v[i] -= 1
    v[8 + i] -= 1
    return v


def a_m(i: int) -> Matrix:
    v = zeros(N, 1)
    v[4 + (i + 1) % 4] += 1
    v[4 + i] -= 1
    v[8 + i] -= 1
    return v


def rb(i: int):
    return (a_b(i).T * xvec)[0]


def rm(i: int):
    return (a_m(i).T * xvec)[0]


def Dcost(i: int):
    return Rational(1, 2) * (rb(i) ** 2 + rm(i) ** 2)


def edge(i: int, j: int) -> int:
    """Index of the edge joining agents i and j (e_i joins i and i+1)."""
    if (j - i) % 4 == 1:
        return i
    if (i - j) % 4 == 1:
        return j
    raise ValueError((i, j))


def V(S) -> sp.Expr:
    return sum(Dcost(edge(i, S[i])) for i in range(4))


Dmat = Matrix.hstack(eye(4), -eye(4), zeros(4, 4))
R_ev = 2 * Dmat.T * Dmat
Omega = eye(N) + R_ev
x_circ = Matrix([0] * 8 + [1] * 4)
loop = Matrix([0] * 8 + [1] * 4)  # covector of sum_i w_i

lam = symbols("lambda")

for S, name in [((1, 0, 3, 2), "S^(0)"), ((3, 2, 1, 0), "S^(1)")]:
    print(f"\n===== matching {name} = {S} =====")
    sel = sorted(set(edge(i, S[i]) for i in range(4)))
    ext = [i for i in range(4) if i not in sel]
    check(f"{name}: exactly two selected edges", len(sel) == 2)
    e, f = sel
    print(f"selected edges e={e}, f={f}; exterior edges {ext}")

    # Gram matrices and disjoint supports
    for g in range(4):
        G = Matrix([[ (a_b(g).T*a_b(g))[0], (a_b(g).T*a_m(g))[0]],
                    [ (a_m(g).T*a_b(g))[0], (a_m(g).T*a_m(g))[0]]])
        check(f"{name}: Gram(e_{g}) = [[3,1],[1,3]]", G == Matrix([[3, 1], [1, 3]]))
    supp_e = {i for i in range(N) if a_b(e)[i] != 0 or a_m(e)[i] != 0}
    supp_f = {i for i in range(N) if a_b(f)[i] != 0 or a_m(f)[i] != 0}
    check(f"{name}: selected edges have disjoint supports", not (supp_e & supp_f))

    # Hessian of V_S from the definition vs H_M formula
    H = sp.hessian(V(S), X)
    H_M = zeros(N, N)
    for g in sel:
        H_M += 2 * (a_b(g) * a_b(g).T + a_m(g) * a_m(g).T)
    check(f"{name}: Hessian(V_S) == 2 sum_g (a^b a^bT + a^m a^mT)", H == H_M)
    check(f"{name}: rank H_M = 4", H_M.rank() == 4)
    check(f"{name}: dim ker H_M = 8", len(H_M.nullspace()) == 8)

    n_plus = {g: (a_b(g) + a_m(g)) / (2 * sqrt(2)) for g in sel}
    n_minus = {g: (a_b(g) - a_m(g)) / 2 for g in sel}
    normals = [n_plus[e], n_plus[f], n_minus[e], n_minus[f]]
    Gn = Matrix.hstack(*normals).T * Matrix.hstack(*normals)
    check(f"{name}: four normals orthonormal", sp.simplify(Gn - eye(4)) == zeros(4, 4))
    for g in sel:
        check(f"{name}: H_M n+_{g} = 8 n+", sp.simplify(H_M * n_plus[g] - 8 * n_plus[g]) == zeros(N, 1))
        check(f"{name}: H_M n-_{g} = 4 n-", sp.simplify(H_M * n_minus[g] - 4 * n_minus[g]) == zeros(N, 1))
        check(f"{name}: R_ev n+_{g} = 0", sp.simplify(R_ev * n_plus[g]) == zeros(N, 1))
        check(f"{name}: R_ev n-_{g} = 4 n-", sp.simplify(R_ev * n_minus[g] - 4 * n_minus[g]) == zeros(N, 1))
    # R_ev leaves ker H_M invariant
    Kb = Matrix.hstack(*H_M.nullspace())
    check(f"{name}: R_ev preserves ker H_M", (H_M * R_ev * Kb).applyfunc(sp.simplify) == zeros(N, 8))

    K_M = H_M + T * Omega
    K_phys = H_M + T * eye(N)

    u1 = (n_plus[e] - n_plus[f]) / sqrt(2)
    u_plus = (n_plus[e] + n_plus[f]) / sqrt(2)
    Z = Matrix.hstack(u1, n_minus[e], n_minus[f])
    check(f"{name}: Z_M basis orthonormal", sp.simplify(Z.T * Z - eye(3)) == zeros(3, 3))
    Wcols = Z.T.nullspace()
    check(f"{name}: dim W_M = 9", len(Wcols) == 9)
    W = Matrix.hstack(*Wcols)
    check(f"{name}: W^T H_M Z = 0", (W.T * H_M * Z).applyfunc(sp.simplify) == zeros(9, 3))
    check(f"{name}: W^T Omega Z = 0", (W.T * Omega * Z).applyfunc(sp.simplify) == zeros(9, 3))
    KZ = (Z.T * K_M * Z).applyfunc(sp.simplify)
    check(f"{name}: K_M|Z = diag(8+T,4+5T,4+5T)", KZ == sp.diag(8 + T, 4 + 5 * T, 4 + 5 * T))
    check(f"{name}: K_M Z = Z K_Z (Z_M invariant)", (K_M * Z - Z * KZ).applyfunc(sp.simplify) == zeros(N, 3))
    KZp = (Z.T * K_phys * Z).applyfunc(sp.simplify)
    check(f"{name}: K_phys|Z = diag(8+T,4+T,4+T)", KZp == sp.diag(8 + T, 4 + T, 4 + T))
    check(f"{name}: K_M u_+ = (8+T) u_+", sp.simplify(K_M * u_plus - (8 + T) * u_plus) == zeros(N, 1))
    check(f"{name}: u_+ in W_M", sp.simplify(Z.T * u_plus) == zeros(3, 1))
    check(f"{name}: ker H_M subset W_M", (Z.T * Kb).applyfunc(sp.simplify) == zeros(3, 8))

    cp = sp.factor(K_M.charpoly(lam).as_expr())
    target = sp.factor((lam - T) ** 6 * (lam - 5 * T) ** 2 * (lam - 4 - 5 * T) ** 2 * (lam - 8 - T) ** 2)
    print(f"charpoly(K_M) = {cp}")
    check(f"{name}: charpoly(K_M) = (l-T)^6 (l-5T)^2 (l-4-5T)^2 (l-8-T)^2", sp.expand(cp - target) == 0)
    print("hidden eigenvalues (K_M|Z):", list(KZ.diagonal()))
    print("hidden eigenvalues (K_phys|Z):", list(KZp.diagonal()))

    # Hidden projections of +-x_circ
    for sgn, lab in [(1, "+x_circ"), (-1, "-x_circ")]:
        pz = (Z.T * (sgn * x_circ)).applyfunc(sp.simplify)
        print(f"P_Z({lab}) components in (u1, n-_e, n-_f): {list(pz)}")
        check(f"{name}: P_Z({lab}) = 0", pz == zeros(3, 1))
    print("u_+ . x_circ =", sp.simplify((u_plus.T * x_circ)[0]))

    # Loop covector
    lz = (Z.T * loop).applyfunc(sp.simplify)
    print(f"loop covector on Z_M basis: {list(lz)}")
    check(f"{name}: loop covector annihilates Z_M", lz == zeros(3, 1))
    for g in sel:
        check(f"{name}: loop . n+_{g} = -1/sqrt2", sp.simplify((loop.T * n_plus[g])[0] + 1 / sqrt(2)) == 0)

    # Exterior common residual (r^b_g + r^m_g)/2 and half-difference (r^b_g - r^m_g)/2
    for g in ext:
        c = (a_b(g) + a_m(g)) / 2
        cz = (Z.T * c).applyfunc(sp.simplify)
        print(f"exterior common residual e_{g} on Z_M: {list(cz)}")
        check(f"{name}: exterior common residual e_{g} annihilates Z_M", cz == zeros(3, 1))
        d = (a_b(g) - a_m(g)) / 2
        dz = (Z.T * d).applyfunc(sp.simplify)
        print(f"exterior half-difference e_{g} on Z_M: {list(dz)}")
        check(f"{name}: exterior half-difference e_{g} on Z_M = (0,-1/2,-1/2)",
              dz == Matrix([0, -Rational(1, 2), -Rational(1, 2)]))
        # therefore each exterior residual reads hidden coordinates
        bz = (Z.T * a_b(g)).applyfunc(sp.simplify)
        check(f"{name}: exterior r^b_{g} covector on Z_M = (0,-1/2,-1/2)",
              bz == Matrix([0, -Rational(1, 2), -Rational(1, 2)]))

    # Center path
    p = zeros(N, 1)
    for g in sel:
        p += a_b(g) + a_m(g)
    check(f"{name}: H_M (x_circ + p/4) = 0", sp.simplify(H_M * (x_circ + p / 4)) == zeros(N, 1))
    check(f"{name}: H_M p = 8 p", sp.simplify(H_M * p - 8 * p) == zeros(N, 1))
    check(f"{name}: R_ev x_circ = 0", R_ev * x_circ == zeros(N, 1))
    check(f"{name}: R_ev p = 0", R_ev * p == zeros(N, 1))
    xbar = exp(-T * t) * (x_circ + (1 - exp(-8 * t)) * p / 4)
    ode = (xbar.diff(t) + K_M * xbar).applyfunc(sp.simplify)
    check(f"{name}: xbar' = -K_M xbar", ode == zeros(N, 1))
    check(f"{name}: xbar(0) = x_circ", xbar.subs(t, 0) == x_circ)
    sub = dict(zip(X, list(xbar)))
    for g in sel:
        for lab, r in [("b", rb(g)), ("m", rm(g))]:
            val = sp.simplify(r.subs(sub) + exp(-(8 + T) * t))
            check(f"{name}: selected r^{lab}_{g}(xbar) = -e^(-(8+T)t)", val == 0)
    for g in ext:
        for lab, r in [("b", rb(g)), ("m", rm(g))]:
            val = sp.simplify(r.subs(sub) - exp(-T * t) * (-Rational(3, 2) + exp(-8 * t) / 2))
            check(f"{name}: exterior r^{lab}_{g}(xbar) = e^(-Tt)(-3/2 + e^(-8t)/2)", val == 0)
    check(f"{name}: kbar = mbar on the path", sp.simplify(Dmat * xbar) == zeros(4, 1))
    check(f"{name}: P_Z xbar(t) = 0", (Z.T * xbar).applyfunc(sp.simplify) == zeros(3, 1))
    check(f"{name}: z_+(xbar) = -e^(-(8+T)t)", sp.simplify((u_plus.T * xbar)[0] + exp(-(8 + T) * t)) == 0)

    # Cost decomposition in (z_+, z_1, z_2, z_3)
    z_plus = (u_plus.T * xvec)[0]
    z1 = (u1.T * xvec)[0]
    z2 = (n_minus[e].T * xvec)[0]
    z3 = (n_minus[f].T * xvec)[0]
    check(f"{name}: D_e = (z_+ + z_1)^2 + z_2^2", sp.expand(Dcost(e) - (z_plus + z1) ** 2 - z2 ** 2) == 0)
    check(f"{name}: D_f = (z_+ - z_1)^2 + z_3^2", sp.expand(Dcost(f) - (z_plus - z1) ** 2 - z3 ** 2) == 0)
    check(f"{name}: r^b_e = z_+ + z_1 + z_2", sp.expand(rb(e) - (z_plus + z1 + z2)) == 0)
    check(f"{name}: r^m_e = z_+ + z_1 - z_2", sp.expand(rm(e) - (z_plus + z1 - z2)) == 0)
    check(f"{name}: r^b_f = z_+ - z_1 + z_3", sp.expand(rb(f) - (z_plus - z1 + z3)) == 0)
    check(f"{name}: r^m_f = z_+ - z_1 - z_3", sp.expand(rm(f) - (z_plus - z1 - z3)) == 0)
    for g in sel:
        check(f"{name}: selected covectors e_{g} annihilate ker H_M",
              (Kb.T * a_b(g)) == zeros(8, 1) and (Kb.T * a_m(g)) == zeros(8, 1))
    # Exterior residual in the same coordinates: hidden part is -(z_2+z_3)/2 for r^b,
    # +(z_2+z_3)/2 for r^m (common part lies in W_M)
    for g in ext:
        hid_b = (Z.T * a_b(g)).T * Matrix([z1, z2, z3])
        check(f"{name}: exterior r^b_{g} hidden part = -(z_2+z_3)/2",
              sp.expand(hid_b[0] + (z2 + z3) / 2) == 0)
        hid_m = (Z.T * a_m(g)).T * Matrix([z1, z2, z3])
        check(f"{name}: exterior r^m_{g} hidden part = +(z_2+z_3)/2",
              sp.expand(hid_m[0] - (z2 + z3) / 2) == 0)

    # Hazard factors lambda/(lambda-2) = 1/(1 - 2 sigma^2/T) with sigma^2 = T/lambda
    for lam_val, expect in [(8 + T, (8 + T) / (6 + T)), (4 + 5 * T, (4 + 5 * T) / (2 + 5 * T))]:
        fac = sp.simplify(1 / (1 - 2 * (T / lam_val) / T))
        check(f"{name}: hazard factor for lambda={lam_val} is {expect}", sp.simplify(fac - expect) == 0)
        check(f"{name}: factor decreasing in T, value at 0 is {expect.subs(T,0)}",
              sp.simplify(sp.diff(expect, T)) .subs(T, 1) < 0)

print(f"\nTOTAL: {COUNT} checks, {FAILS} failures")
raise SystemExit(1 if FAILS else 0)
