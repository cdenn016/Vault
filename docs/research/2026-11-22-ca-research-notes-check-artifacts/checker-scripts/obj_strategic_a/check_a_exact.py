"""Independent exact / high-precision checks for open_obj_strategic_a (reviewer script, part A).

Exact rational algebra (SymPy) for C3, C5, C7 and the O2 example; own code path
(full Kronecker operator restricted by a symmetrizer, not the note's 6-dim basis).
Each block ends with a planted-error negative control that must FAIL the same test.
"""
from __future__ import annotations

import itertools
import math

import numpy as np
import sympy as sp

R = sp.Rational


def heat_bath_A(K: sp.Matrix, dims: list[int]) -> list[sp.Matrix]:
    r"""A_i = I - E_i K_ii^{-1} E_i^T K  (eq:obj-update)."""
    d = sum(dims)
    offs = [0]
    for x in dims:
        offs.append(offs[-1] + x)
    out = []
    for i in range(len(dims)):
        s, e = offs[i], offs[i + 1]
        E = sp.zeros(d, e - s)
        for k in range(e - s):
            E[s + k, k] = 1
        Kii = K[s:e, s:e]
        assert Kii == Kii.T
        out.append(sp.eye(d) - E * Kii.inv() * E.T * K)
    return out


def T_apply(As: list[sp.Matrix], S: sp.Matrix) -> sp.Matrix:
    n = len(As)
    acc = sp.zeros(*S.shape)
    for A in As:
        acc += A * S * A.T
    return acc / n


def sym_basis(d: int) -> list[sp.Matrix]:
    out = []
    for i in range(d):
        for j in range(i, d):
            B = sp.zeros(d, d)
            B[i, j] = 1
            B[j, i] = 1
            out.append(B)
    return out


def sym_coords(S: sp.Matrix) -> sp.Matrix:
    d = S.shape[0]
    return sp.Matrix([S[i, j] for i in range(d) for j in range(i, d)])


def T_matrix(As: list[sp.Matrix]) -> sp.Matrix:
    d = As[0].shape[0]
    basis = sym_basis(d)
    cols = [sym_coords(T_apply(As, B)) for B in basis]
    return sp.Matrix.hstack(*cols)


def solve_Sinf(As: list[sp.Matrix], rhs: sp.Matrix) -> sp.Matrix:
    """Solve S = T(S) + rhs on Sym_d exactly."""
    d = rhs.shape[0]
    Tm = T_matrix(As)
    sol = (sp.eye(Tm.shape[0]) - Tm).LUsolve(sym_coords(rhs))
    S = sp.zeros(d, d)
    k = 0
    for i in range(d):
        for j in range(i, d):
            S[i, j] = sol[k]
            S[j, i] = sol[k]
            k += 1
    return S


def main() -> None:
    lam, c, x = sp.symbols("lam c x")

    # ------------------------------------------------------------------ C5
    print("[C5] canceling star K(c)")
    Kc = sp.Matrix([[1, -c, c], [-1, 1, 0], [-1, 0, 1]])
    As = heat_bath_A(Kc, [1, 1, 1])
    for A in As:
        assert sp.simplify(A * A - A) == sp.zeros(3, 3)
    assert sp.factor(Kc.charpoly(lam).as_expr()) == (lam - 1) ** 3
    W = As[1] * As[2] * As[0] * As[1] * As[2]
    assert W == sp.zeros(3, 3)
    print("  A2 A3 A1 A2 A3 = 0 for symbolic c: True; charpoly(K) = (lam-1)^3: True")
    # which length<=5 words vanish identically in c?
    zero_words = []
    for L in range(1, 6):
        for w in itertools.product(range(3), repeat=L):
            if any(w[k] == w[k + 1] for k in range(L - 1)):
                continue
            P = sp.eye(3)
            for i in w:
                P = P * As[i]
            if sp.simplify(P) == sp.zeros(3, 3):
                zero_words.append(tuple(i + 1 for i in w))
    print("  nonrepeating zero words of length<=5:", zero_words)
    Tm = T_matrix(As)
    cp = sp.factor((lam * sp.eye(6) - Tm).det())
    stated = R(1, 729) * (3 * lam - 2) * (3 * lam - 1) * (
        81 * lam**4 - 162 * lam**3 + (117 - 18 * c**2) * lam**2 - (36 - 24 * c**2) * lam + (4 - 10 * c**2)
    )
    print("  charpoly(T) equals note's factorization:", sp.expand(cp - stated) == 0)
    print("  det(I-T) =", sp.factor(cp.subs(lam, 1)))
    S_note = sp.Matrix(
        [
            [2 * c**2 + 1, (4 * c**2 + 3 * c + 2) / 4, (4 * c**2 - 3 * c + 2) / 4],
            [(4 * c**2 + 3 * c + 2) / 4, c**2 + 2, c**2 + R(1, 2)],
            [(4 * c**2 - 3 * c + 2) / 4, c**2 + R(1, 2), c**2 + 2],
        ]
    ) / (1 - c**2)
    resid = sp.simplify(S_note - T_apply(As, S_note) - sp.eye(3) / 3)
    print("  note's S_inf(c) solves S = T(S) + I/3 :", resid == sp.zeros(3, 3))
    M1 = sp.factor(S_note[0, 0])
    M2 = sp.factor(S_note[:2, :2].det())
    M3 = sp.factor(S_note.det())
    ok_min = (
        sp.simplify(M1 - (2 * c**2 + 1) / (1 - c**2)) == 0
        and sp.simplify(M2 - (16 * c**4 - 24 * c**3 + 55 * c**2 - 12 * c + 28) / (16 * (1 - c**2) ** 2)) == 0
        and sp.simplify(M3 - 3 * (4 * c**4 + 25 * c**2 + 16) / (16 * (1 - c**2) ** 3)) == 0
    )
    print("  minors M1,M2,M3 match the note:", ok_min)
    num = 16 * c**4 - 24 * c**3 + 55 * c**2 - 12 * c + 28
    print("  M2 numerator SOS identity:", sp.expand(num - ((4 * c**2 - 3 * c) ** 2 + 46 * (c - R(3, 23)) ** 2 + 28 - R(18, 23))) == 0)
    # planted error: S_note with one entry altered must fail the fixed-point test
    S_bad = S_note.copy()
    S_bad[1, 2] = (c**2 + 1) / (1 - c**2)
    S_bad[2, 1] = S_bad[1, 2]
    print("  NEG CONTROL (altered S_23): fixed point holds?", sp.simplify(S_bad - T_apply(As, S_bad) - sp.eye(3) / 3) == sp.zeros(3, 3))
    for cv in [R(1, 2), R(9, 10), 1, R(11, 10), 2, 4]:
        ev = np.linalg.eigvals(np.array(Tm.subs(c, cv).tolist(), dtype=float))
        print(f"  c={cv}: rho(T) = {max(abs(e) for e in ev):.6f}")
    # (A1 A2)^r e1 and the H_m lower bound
    e1 = sp.Matrix([1, 0, 0])
    okr = all((As[0] * As[1]) ** r * e1 == sp.Matrix([c**r, c ** (r - 1), 0]) for r in range(1, 6))
    print("  (A1A2)^r e1 = (c^r, c^(r-1), 0), r=1..5:", okr)
    for m in [1, 2, 3]:
        word = [0, 1] * m + [0, 2] + [1, 2, 0, 1, 2]  # H_m prefix then an absorbing tail
        P = sp.eye(3)
        Sig = sp.zeros(3, 3)
        for i in word:
            v = P[:, i]
            Sig += v * v.T
            P = P * As[i]
        assert sp.simplify(P) == sp.zeros(3, 3)
        lower = sum(c ** (2 * r) for r in range(m + 1))
        diff = sp.expand(Sig[0, 0] - lower)
        print(f"  H_{m} sample word: Sigma_11 - sum_r c^(2r) = {diff}  (must be >= 0 for all c)")

    # ------------------------------------------------------------------ C7
    print("[C7] K_(3)")
    M3m = sp.Matrix([[1, R(11, 10), -R(1, 4)], [R(11, 10), 1, R(1, 4)], [R(1, 2), -R(1, 2), 1]])
    D3 = sp.diag(1, 1, R(1, 100))
    K3 = D3 * M3m
    As3 = heat_bath_A(K3, [1, 1, 1])
    As3M = heat_bath_A(M3m, [1, 1, 1])
    print("  A_i(K3) == A_i(M3):", all(a == b for a, b in zip(As3, As3M)))
    S3 = solve_Sinf(As3, sp.eye(3) / 3)
    print("  gamma*S_inf (rhs I/3) =", S3.tolist())
    print("  minors:", S3[0, 0], S3[:2, :2].det(), S3.det())
    # the stationary second moment for K3 itself uses rhs K_d^{-1}/3, not I/3
    S3K = solve_Sinf(As3, D3.inv() / 3)
    print("  with correct rhs K_d^{-1}/3: minors:", S3K[0, 0], S3K[:2, :2].det(), S3K.det())
    cp3 = sp.factor(K3.charpoly(lam).as_expr())
    print("  charpoly(K3) =", cp3)
    T3 = T_matrix(As3)
    ev3 = np.linalg.eigvals(np.array(T3.tolist(), dtype=float))
    print(f"  rho(T) = {max(abs(e) for e in ev3):.6f};  eig(K3) = {[sp.N(r, 8) for r in sp.Poly(K3.charpoly(lam).as_expr(), lam).nroots()]}")
    print("  NEG CONTROL (D3=I): eig(M3) =", [sp.N(r, 6) for r in sp.Poly(M3m.charpoly(lam).as_expr(), lam).nroots()])

    # ------------------------------------------------------------------ C3
    print("[C3] K_(2,2)")
    K4 = sp.Matrix([[10, 0, 10, 10], [0, 1, R(1, 2), 1], [-R(1, 2), -1, 1, 0], [10, 10, 0, 10]])
    K11, K12, K21, K22 = K4[:2, :2], K4[:2, 2:], K4[2:, :2], K4[2:, 2:]
    A12 = -K11.inv() * K12
    A21 = -K22.inv() * K21
    Mm = A12 * A21
    print("  A12 =", A12.tolist(), " A21 =", A21.tolist(), " M =", Mm.tolist())
    zz = sp.Symbol("z")
    print("  det(-zI-K) =", sp.expand((-zz * sp.eye(4) - K4).det()))
    print("  eig(K) =", [sp.N(r, 8) for r in sp.Poly(K4.charpoly(lam).as_expr(), lam).nroots()])
    As4 = heat_bath_A(K4, [2, 2])
    T4 = T_matrix(As4)
    cp4 = sp.factor(T4.charpoly(lam).as_expr())
    print("  charpoly(T) on Sym_4 =", cp4)
    # block-power identities for generic rational rectangular blocks (d1=2,d2=3)
    B12 = sp.Matrix([[R(1, 3), -R(2, 5), R(1, 7)], [R(3, 4), R(1, 2), -R(5, 6)]])
    B21 = sp.Matrix([[R(2, 3), -R(1, 4)], [R(1, 5), R(3, 7)], [-R(1, 2), R(1, 9)]])
    A1 = sp.Matrix(sp.BlockMatrix([[sp.zeros(2, 2), B12], [sp.zeros(3, 2), sp.eye(3)]]))
    A2 = sp.Matrix(sp.BlockMatrix([[sp.eye(2), sp.zeros(2, 3)], [B21, sp.zeros(3, 3)]]))
    MM, MP = B12 * B21, B21 * B12
    ok = True
    for m in range(1, 5):
        ok &= (A1 * A2) ** m == sp.Matrix(sp.BlockMatrix([[MM**m, sp.zeros(2, 3)], [B21 * MM ** (m - 1), sp.zeros(3, 3)]]))
        ok &= (A1 * A2) ** m * A1 == sp.Matrix(sp.BlockMatrix([[sp.zeros(2, 2), MM**m * B12], [sp.zeros(3, 2), MP**m]]))
        ok &= (A2 * A1) ** m == sp.Matrix(sp.BlockMatrix([[sp.zeros(2, 2), B12 * MP ** (m - 1)], [sp.zeros(3, 2), MP**m]]))
        ok &= (A2 * A1) ** m * A2 == sp.Matrix(sp.BlockMatrix([[MM**m, sp.zeros(2, 3)], [B21 * MM**m, sp.zeros(3, 3)]]))
    print("  four block-power identities, m=1..4, d=(2,3):", ok)

    # ------------------------------------------------------------------ O2 example (reviewer's own)
    print("[O2] reviewer example with K_d = I")
    a12, a13, a21, a23, a31 = sp.symbols("a12 a13 a21 a23 a31")
    Ng = sp.Matrix([[0, a12, a13], [a21, 0, a23], [a31, 0, 0]])  # a32 = 0
    Kg = sp.eye(3) - Ng
    Ag = heat_bath_A(Kg, [1, 1, 1])
    Wg = sp.simplify(Ag[1] * Ag[2] * Ag[0] * Ag[1] * Ag[2])
    print("  A2A3A1A2A3 (a32=0) =", sp.factor(Wg[0, 0]), "* (1,p,q)^T e1^T ; full matrix:", Wg.applyfunc(sp.factor).tolist())
    cpN = sp.expand(Ng.charpoly(x).as_expr())
    constraint = a12 * (a21 + a23 * a31) + a13 * a31
    print("  charpoly(N) =", cpN, "; minus (x^3 + g x - g) with g=a12 a23 a31, modulo constraint:",
          sp.simplify((cpN - (x**3 + a12 * a23 * a31 * x - a12 * a23 * a31)).subs(a21, sp.solve(constraint, a21)[0])))
    Ko = sp.Matrix([[1, -1, 0], [-7, 1, -7], [1, 0, 1]])
    Ao = heat_bath_A(Ko, [1, 1, 1])
    print("  K_o =", Ko.tolist(), "; A2A3A1A2A3 == 0:", Ao[1] * Ao[2] * Ao[0] * Ao[1] * Ao[2] == sp.zeros(3, 3))
    print("  charpoly(K_o) =", sp.factor(Ko.charpoly(lam).as_expr()), "; eig =", [sp.N(r, 8) for r in sp.Poly(Ko.charpoly(lam).as_expr(), lam).nroots()])
    barA = (Ao[0] + Ao[1] + Ao[2]) / 3
    print("  rho(barA) =", max(abs(np.linalg.eigvals(np.array(barA.tolist(), dtype=float)))))
    To = T_matrix(Ao)
    print("  rho(T) =", max(abs(np.linalg.eigvals(np.array(To.tolist(), dtype=float)))))
    Kn = sp.Matrix([[1, -1, 0], [-7, 1, -6], [1, 0, 1]])  # violates the constraint
    An = heat_bath_A(Kn, [1, 1, 1])
    print("  NEG CONTROL (a23=6, constraint broken): word zero?", An[1] * An[2] * An[0] * An[1] * An[2] == sp.zeros(3, 3))


if __name__ == "__main__":
    main()
