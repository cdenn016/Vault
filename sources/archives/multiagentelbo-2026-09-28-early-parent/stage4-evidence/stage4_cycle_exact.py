r"""Exact (sympy) construction of the homogeneous four-cycle of
def:rg-formation-cycle-experiment and the identities used in the proofs of
prop:rg-formation-endogenous-cycle (ca_formation_proofs.tex, eqs.
rg-formation-cycle-normals and rg-formation-cycle-center).

Coordinates x = (k_0..k_3, m_0..m_3, w_0..w_3) in R^12.  Edge e_i runs i -> i+1,
r^b_i = k_{i+1} - k_i - w_i,  r^m_i = m_{i+1} - m_i - w_i,
D_{e_i} = (1/2)[(r^b_i)^2 + (r^m_i)^2],
V_S = \sum_i D_{e(i,S_i)}   (a matched edge is counted from both ends),
U_S = V_S + (T/2)|x|^2 + (T/2) x^T R_ev x,  R_ev = 2 D^T D,  D x = k - m,
K_M = Hess U_M = H_M + T (I + R_ev).

Every check is an exact symbolic identity with T > 0 a free symbol; the script
asserts each one and prints a summary.  Run: python stage4_cycle_exact.py
"""
from __future__ import annotations

import sympy as sp

T, t, lam = sp.symbols("T t lambda", positive=True)
X = sp.Matrix(sp.symbols("k0:4") + sp.symbols("m0:4") + sp.symbols("w0:4"))
N = 12


def e(idx: int) -> sp.Matrix:
    v = sp.zeros(N, 1)
    v[idx] = 1
    return v


def kk(i: int) -> int:
    return i % 4


def mm(i: int) -> int:
    return 4 + i % 4


def ww(i: int) -> int:
    return 8 + i % 4


a_b = [e(kk(i + 1)) - e(kk(i)) - e(ww(i)) for i in range(4)]
a_m = [e(mm(i + 1)) - e(mm(i)) - e(ww(i)) for i in range(4)]
r_b = [(a_b[i].T * X)[0] for i in range(4)]
r_m = [(a_m[i].T * X)[0] for i in range(4)]
D_edge = [sp.Rational(1, 2) * (r_b[i] ** 2 + r_m[i] ** 2) for i in range(4)]


def edge_of(i: int, j: int) -> int:
    """Index of the edge joining receiver i and source j (j = i +- 1)."""
    return i % 4 if (j - i) % 4 == 1 else (i - 1) % 4


results: list[tuple[str, bool]] = []


def check(name: str, cond: bool) -> None:
    results.append((name, bool(cond)))
    assert cond, name


def is_zero_matrix(Mx: sp.Matrix) -> bool:
    return all(sp.simplify(v) == 0 for v in Mx)


# Gram matrix of each edge's two covectors
for i in range(4):
    G = sp.Matrix([[a_b[i].dot(a_b[i]), a_b[i].dot(a_m[i])],
                   [a_m[i].dot(a_b[i]), a_m[i].dot(a_m[i])]])
    check(f"Gram(a^b_{i},a^m_{i}) = [[3,1],[1,3]]", G == sp.Matrix([[3, 1], [1, 3]]))

# Evaluator matrix R_ev = 2 D^T D
Dmat = sp.zeros(4, N)
for i in range(4):
    Dmat[i, kk(i)] = 1
    Dmat[i, mm(i)] = -1
R_ev = 2 * Dmat.T * Dmat
Omega = sp.eye(N) + R_ev

x_circ = sp.Matrix([0] * 8 + [1] * 4)
loop_cov = sp.Matrix([0] * 8 + [1] * 4)  # covector of sum_i w_i

matchings = {"S0": (1, 0, 3, 2), "S1": (3, 2, 1, 0)}
report: dict[str, dict] = {}

for name, S in matchings.items():
    V = sum(D_edge[edge_of(i, S[i])] for i in range(4))
    H_def = sp.hessian(V, list(X))
    sel = sorted({edge_of(i, S[i]) for i in range(4)})
    ext = [g for g in range(4) if g not in sel]
    e_, f_ = sel
    H_M = 2 * sum((a_b[g] * a_b[g].T + a_m[g] * a_m[g].T for g in sel), sp.zeros(N, N))
    check(f"{name}: selected edges {sel}, exterior {ext}", len(sel) == 2)
    check(f"{name}: Hessian of V_S (both ends counted) equals 2 sum(a a^T)", H_def == H_M)
    check(f"{name}: rank H_M = 4 (kernel dim 8)", H_M.rank() == 4)

    npl = {g: (a_b[g] + a_m[g]) / (2 * sp.sqrt(2)) for g in sel}
    nmi = {g: (a_b[g] - a_m[g]) / 2 for g in sel}
    basis4 = [npl[e_], npl[f_], nmi[e_], nmi[f_]]
    Gram4 = sp.Matrix(4, 4, lambda i, j: sp.simplify(basis4[i].dot(basis4[j])))
    check(f"{name}: n^+_e,n^+_f,n^-_e,n^-_f orthonormal", Gram4 == sp.eye(4))
    for g in sel:
        check(f"{name}: H_M n^+_{g} = 8 n^+_{g}", is_zero_matrix(H_M * npl[g] - 8 * npl[g]))
        check(f"{name}: H_M n^-_{g} = 4 n^-_{g}", is_zero_matrix(H_M * nmi[g] - 4 * nmi[g]))
        check(f"{name}: R_ev n^+_{g} = 0", is_zero_matrix(R_ev * npl[g]))
        check(f"{name}: R_ev n^-_{g} = 4 n^-_{g}", is_zero_matrix(R_ev * nmi[g] - 4 * nmi[g]))

    u_plus = (npl[e_] + npl[f_]) / sp.sqrt(2)
    u1 = (npl[e_] - npl[f_]) / sp.sqrt(2)
    Zb = sp.Matrix.hstack(u1, nmi[e_], nmi[f_])  # 12 x 3, orthonormal columns
    check(f"{name}: Z_M basis orthonormal", sp.simplify(Zb.T * Zb) == sp.eye(3))
    Wraw = (Zb.T).nullspace()
    Wb = sp.Matrix.hstack(*sp.GramSchmidt(Wraw, orthonormal=True))
    Wb = Wb.applyfunc(sp.nsimplify)
    check(f"{name}: dim W_M = 9", Wb.shape == (12, 9))
    check(f"{name}: W_M basis orthonormal", sp.simplify(Wb.T * Wb) == sp.eye(9))
    check(f"{name}: W_M orthogonal to Z_M", is_zero_matrix(Wb.T * Zb))

    K_M = H_M + T * Omega
    check(f"{name}: H_M preserves Z_M and W_M (W^T H Z = 0)", is_zero_matrix(Wb.T * H_M * Zb))
    check(f"{name}: Omega preserves Z_M and W_M (W^T Omega Z = 0)", is_zero_matrix(Wb.T * Omega * Zb))
    K_Z = sp.simplify(Zb.T * K_M * Zb)
    check(f"{name}: K_M on Z_M in basis (u1,n^-_e,n^-_f) = diag(8+T,4+5T,4+5T)",
          is_zero_matrix(K_Z - sp.diag(8 + T, 4 + 5 * T, 4 + 5 * T)))
    # kernel of H_M inside W_M: projector check P_Z v = 0 for v in ker H_M
    kerH = H_M.nullspace()
    check(f"{name}: ker H_M subset W_M", all(is_zero_matrix(Zb.T * v) for v in kerH))
    check(f"{name}: fast common normal u_+ in W_M", is_zero_matrix(Zb.T * u_plus))
    check(f"{name}: K_M u_+ = (8+T) u_+", is_zero_matrix(K_M * u_plus - (8 + T) * u_plus))

    # full spectrum of K_M
    cp = sp.factor((lam * sp.eye(N) - K_M).det(method="berkowitz"))
    target = (lam - T) ** 6 * (lam - 5 * T) ** 2 * (lam - 4 - 5 * T) ** 2 * (lam - 8 - T) ** 2
    check(f"{name}: charpoly K_M = (l-T)^6 (l-5T)^2 (l-4-5T)^2 (l-8-T)^2",
          sp.expand(cp - target) == 0)

    # hidden projection of +- x_circ
    check(f"{name}: Z_M^T x_circ = 0", is_zero_matrix(Zb.T * x_circ))
    check(f"{name}: Z_M^T (-x_circ) = 0", is_zero_matrix(Zb.T * (-x_circ)))
    # loop covector and exterior common residuals annihilate Z_M
    check(f"{name}: loop covector annihilates Z_M", is_zero_matrix(loop_cov.T * Zb))
    check(f"{name}: loop pairs to -1/sqrt2 with n^+", all(
        sp.simplify(loop_cov.dot(npl[g]) + 1 / sp.sqrt(2)) == 0 for g in sel))
    for g in ext:
        ccov = (a_b[g] + a_m[g]) / 2
        check(f"{name}: exterior common residual (r^b_{g}+r^m_{g})/2 annihilates Z_M",
              is_zero_matrix(ccov.T * Zb))
        diff = sp.expand(D_edge[g] - ((r_b[g] + r_m[g]) / 2) ** 2 - ((r_b[g] - r_m[g]) / 2) ** 2)
        check(f"{name}: D_{g} = ((r^b+r^m)/2)^2 + ((r^b-r^m)/2)^2 (hence >= common^2)", diff == 0)
        # the exterior belief-minus-model difference does NOT annihilate Z_M in general
        dcov = (a_b[g] - a_m[g]) / 2
        report.setdefault(name, {})[f"ext_diff_{g}_on_Z"] = [sp.nsimplify(v) for v in (dcov.T * Zb)]

    # coordinate identities for selected costs
    zp = (u_plus.T * X)[0]
    z1 = (u1.T * X)[0]
    z2 = (nmi[e_].T * X)[0]
    z3 = (nmi[f_].T * X)[0]
    check(f"{name}: D_e = (z_+ + z_1)^2 + z_2^2", sp.expand(D_edge[e_] - ((zp + z1) ** 2 + z2 ** 2)) == 0)
    check(f"{name}: D_f = (z_+ - z_1)^2 + z_3^2", sp.expand(D_edge[f_] - ((zp - z1) ** 2 + z3 ** 2)) == 0)
    check(f"{name}: r^b_e = z_+ + z_1 + z_2", sp.expand(r_b[e_] - (zp + z1 + z2)) == 0)
    check(f"{name}: r^m_e = z_+ + z_1 - z_2", sp.expand(r_m[e_] - (zp + z1 - z2)) == 0)
    check(f"{name}: r^b_f = z_+ - z_1 + z_3", sp.expand(r_b[f_] - (zp - z1 + z3)) == 0)
    check(f"{name}: r^m_f = z_+ - z_1 - z_3", sp.expand(r_m[f_] - (zp - z1 - z3)) == 0)
    # selected residual covectors lie in range(H_M) = span of the four normals
    for g in sel:
        for cov in (a_b[g], a_m[g]):
            check(f"{name}: selected residual covector of edge {g} annihilates ker H_M",
                  all((cov.T * v)[0] == 0 for v in kerH))

    # center path
    p = sum((a_b[g] + a_m[g] for g in sel), sp.zeros(N, 1))
    check(f"{name}: x_circ + p/4 in ker H_M", is_zero_matrix(H_M * (x_circ + p / 4)))
    check(f"{name}: H_M p = 8 p", is_zero_matrix(H_M * p - 8 * p))
    check(f"{name}: R_ev x_circ = 0 and R_ev p = 0", is_zero_matrix(R_ev * x_circ) and is_zero_matrix(R_ev * p))
    xbar = sp.exp(-T * t) * (x_circ + (1 - sp.exp(-8 * t)) / 4 * p)
    check(f"{name}: d/dt xbar + K_M xbar = 0", is_zero_matrix(sp.simplify(xbar.diff(t) + K_M * xbar)))
    check(f"{name}: xbar(0) = x_circ", is_zero_matrix(xbar.subs(t, 0) - x_circ))
    for g in sel:
        for cov in (a_b[g], a_m[g]):
            check(f"{name}: selected residual on edge {g} = -exp(-(8+T)t)",
                  sp.simplify((cov.T * xbar)[0] + sp.exp(-(8 + T) * t)) == 0)
    for g in ext:
        for cov in (a_b[g], a_m[g]):
            check(f"{name}: exterior residual on edge {g} = exp(-Tt)(-3/2+exp(-8t)/2)",
                  sp.simplify((cov.T * xbar)[0] - sp.exp(-T * t) * (-sp.Rational(3, 2) + sp.exp(-8 * t) / 2)) == 0)
    check(f"{name}: along xbar kbar = mbar (evaluator force vanishes)", is_zero_matrix(Dmat * xbar))
    check(f"{name}: z_+ on xbar = -exp(-(8+T)t)", sp.simplify((u_plus.T * xbar)[0] + sp.exp(-(8 + T) * t)) == 0)
    check(f"{name}: hidden coords on xbar vanish", is_zero_matrix(sp.simplify(Zb.T * xbar)))
    report.setdefault(name, {}).update({
        "selected_edges": sel, "exterior_edges": ext,
        "W_basis_first_col": [str(v) for v in Wb[:, 0]],
    })

# Gaussian identity used in the hazard bound:
# E exp((a+Z)^2/T), Z ~ N(0, s2), s2 < T/2, equals (1-2 s2/T)^{-1/2} exp(a^2/(T(1-2 s2/T))).
a, z, s2 = sp.symbols("a z s2", positive=True)
c = 1 / (2 * s2) - 1 / T  # positive when s2 < T/2
expo = (a + z) ** 2 / T - z ** 2 / (2 * s2)
zc = a / (T * c)
completed = -c * (z - zc) ** 2 + a ** 2 / (T * (1 - 2 * s2 / T))
check("completing the square in E exp((a+Z)^2/T)", sp.simplify(sp.expand(expo - completed)) == 0)
prefactor = sp.sqrt(sp.pi / c) / sp.sqrt(2 * sp.pi * s2)
check("Gaussian normalizer gives (1-2 s2/T)^{-1/2}",
      sp.simplify(prefactor ** 2 - 1 / (1 - 2 * s2 / T)) == 0)
for s2val, lab, expected, bound in ((T / (8 + T), "8+T", (8 + T) / (6 + T), sp.Rational(4, 3)),
                                    (T / (4 + 5 * T), "4+5T", (4 + 5 * T) / (2 + 5 * T), 2)):
    # g = 1/(1-2 s2/T) is both the squared prefactor and the multiplier of a^2/T in the exponent
    g = sp.simplify(1 / (1 - 2 * s2val / T))
    check(f"rate {lab}: 1/(1-2 s2/T) = {expected}", sp.simplify(g - expected) == 0)
    dg = sp.factor(sp.diff(expected, T))
    check(f"rate {lab}: derivative {dg} < 0 for T>0 and value {bound} at T=0, so g <= {bound}",
          dg.is_negative and sp.limit(expected, T, 0) == bound)
    report.setdefault("gaussian_identity", {})[lab] = f"g={expected}, dg/dT={dg}"

if __name__ == "__main__":
    for nm, ok in results:
        print(("PASS " if ok else "FAIL ") + nm)
    print(f"\n{sum(ok for _, ok in results)}/{len(results)} exact checks passed")
    for k, v in report.items():
        print(k, v)
