r"""Brute-force check of the 5-agent selector T over all 10 balanced (2,3) bipartitions.

T = max over bipartitions {B2, B3} of mean_within / mean_between, with
mean_within over the 1 + 3 = 4 pairs inside B2 or B3 and mean_between over the 2*3 = 6 cross pairs.
Claimed closed form: T = max{ (I_SA + 3 I_AA) / (2 (I_SA + I_AA)), 3 (I_SA + I_AA) / (2 I_SA + 4 I_AA) },
claimed T <= 3/2 with equality iff I_SA = 0.
Single-threaded, pure Python, no numpy.
"""
import itertools
import math
from fractions import Fraction as Fr

N = 5  # index 0 = source S, 1..4 = members


def bipartitions() -> list[tuple[tuple[int, ...], tuple[int, ...]]]:
    out = []
    for two in itertools.combinations(range(N), 2):
        three = tuple(k for k in range(N) if k not in two)
        out.append((two, three))
    return out


def T_brute(mi):
    best = None
    rows = []
    for two, three in bipartitions():
        within = [mi(i, j) for blk in (two, three) for i, j in itertools.combinations(blk, 2)]
        between = [mi(i, j) for i in two for j in three]
        assert len(within) == 4 and len(between) == 6
        r = (sum(within) / len(within)) / (sum(between) / len(between))
        rows.append((two, three, r))
        if best is None or r > best:
            best = r
    return best, rows


def closed(Isa, Iaa):
    r1 = (Isa + 3 * Iaa) / (2 * (Isa + Iaa))
    r2 = 3 * (Isa + Iaa) / (2 * Isa + 4 * Iaa)
    return r1, r2


def mi_exch(Isa, Iaa):
    return lambda i, j: Isa if (i == 0 or j == 0) else Iaa


def cov_matrix(rsa: float, raa: float, sd: list[float]) -> list[list[float]]:
    C = [[0.0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            rho = 1.0 if i == j else (rsa if (i == 0 or j == 0) else raa)
            C[i][j] = rho * sd[i] * sd[j]
    return C


def is_pd(C: list[list[float]]) -> bool:
    n = len(C)
    L = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1):
            s = C[i][j] - sum(L[i][k] * L[j][k] for k in range(j))
            if i == j:
                if s <= 0:
                    return False
                L[i][i] = math.sqrt(s)
            else:
                L[i][j] = s / L[j][j]
    return True


def gauss_pair_mi(C, i, j):
    r"""I(X_i;X_j) = -\frac12 \ln(1 - \Sigma_{ij}^2 / (\Sigma_{ii}\Sigma_{jj}))."""
    return -0.5 * math.log(1.0 - C[i][j] ** 2 / (C[i][i] * C[j][j]))


print("== Part A: exact rational check of closed form, bound, equality set ==")
vals = [Fr(0), Fr(1, 7), Fr(1, 2), Fr(1), Fr(3), Fr(50)]
n_checked = 0
eq_points = []
for Isa in vals:
    for Iaa in vals:
        if Isa + Iaa == 0:
            continue
        T, _ = T_brute(mi_exch(Isa, Iaa))
        r1, r2 = closed(Isa, Iaa)
        assert T == max(r1, r2), (Isa, Iaa, T, r1, r2)
        assert T <= Fr(3, 2)
        if T == Fr(3, 2):
            eq_points.append((Isa, Iaa))
        n_checked += 1
print(f"checked {n_checked} rational (I_SA, I_AA) points: brute == closed form exactly, T <= 3/2 at all")
print("points with T == 3/2 exactly:", [(str(a), str(b)) for a, b in eq_points])
viol = [(str(a), str(b)) for a, b in eq_points if a != 0]
print("points with T == 3/2 but I_SA != 0 (violate 'equality iff I_SA=0'):", viol)

print()
print("== Part B: admissible covariances, MI computed from the covariance itself ==")
cases = [
    ("generic", 0.3, 0.2, [1.0, 1.0, 1.0, 1.0, 1.0]),
    ("generic, unequal variances", 0.8, 0.6, [2.0, 0.5, 1.5, 3.0, 1.0]),
    ("negative rho_AA", 0.25, -0.2, [1.0, 1.0, 1.0, 1.0, 1.0]),
    ("I_SA = 0", 0.0, 0.5, [1.0, 1.0, 1.0, 1.0, 1.0]),
    ("I_AA = 0 (candidate counterexample)", 0.3, 0.0, [1.0, 2.0, 1.0, 0.7, 1.0]),
]
for name, rsa, raa, sd in cases:
    C = cov_matrix(rsa, raa, sd)
    pd = is_pd(C)
    mi = lambda i, j, C=C: gauss_pair_mi(C, i, j)
    T, rows = T_brute(mi)
    Isa = -0.5 * math.log(1 - rsa ** 2)
    Iaa = -0.5 * math.log(1 - raa ** 2)
    r1, r2 = closed(Isa, Iaa)
    argmax = [(two, three) for two, three, r in rows if abs(r - T) < 1e-12]
    print(f"[{name}] rho_SA={rsa}, rho_AA={raa}, PD={pd}")
    print(f"   I_SA={Isa:.6f}, I_AA={Iaa:.6f}, denominators 2(I_SA+I_AA)={2*(Isa+Iaa):.6f}, 2I_SA+4I_AA={2*Isa+4*Iaa:.6f}")
    print(f"   brute T={T:.12f}  closed r1={r1:.12f} r2={r2:.12f} max={max(r1, r2):.12f}  |diff|={abs(T - max(r1, r2)):.2e}")
    print(f"   T <= 3/2: {T <= 1.5 + 1e-12};  |T - 3/2| = {abs(T - 1.5):.2e};  argmax bipartitions (2-block | 3-block): {argmax}")
    print("   all 10 ratios:", ", ".join(f"{two}|{three}:{r:.6f}" for two, three, r in rows))

print()
print("== Part C: grid scan of the admissible PD region (rho_SA, rho_AA) ==")
mx = -1.0
arg = None
npts = 0
for a_i in range(0, 100):
    a = a_i / 100
    for b_i in range(-33, 100):
        b = b_i / 100
        C = cov_matrix(a, b, [1.0] * N)
        if not is_pd(C):
            continue
        Isa = -0.5 * math.log(1 - a * a)
        Iaa = -0.5 * math.log(1 - b * b)
        if Isa + Iaa == 0:
            continue
        T, _ = T_brute(mi_exch(Isa, Iaa))
        npts += 1
        if T > mx:
            mx, arg = T, (a, b)
        if Isa > 0 and Iaa > 0:
            assert T < 1.5, (a, b, T)
print(f"scanned {npts} admissible PD grid points; max T = {mx!r} at (rho_SA, rho_AA) = {arg}")
print("strict T < 3/2 held at every grid point with I_SA > 0 and I_AA > 0")
