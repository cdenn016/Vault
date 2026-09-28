"""Discrete sanity checks for Lemma 1(b) and the moment constants of Lemma 7 (Fable verifier)."""
from __future__ import annotations

import itertools
import math
import random

random.seed(7)

# Lemma 1(b): sum_b w_b H(q_b) = H(q) + I(B; Z | Y), with H(q) = sum_y q(y) KL(q(z|y) || kappa_y)
Y = 3
Z = 4
Bv = 2
# random joint law of (B, Y, Z) and random kernel kappa
joint = {}
tot = 0.0
for b, y, z in itertools.product(range(Bv), range(Y), range(Z)):
    v = random.random()
    joint[(b, y, z)] = v
    tot += v
joint = {k: v / tot for k, v in joint.items()}
kappa = {}
for y in range(Y):
    w = [random.random() for _ in range(Z)]
    s = sum(w)
    kappa[y] = [x / s for x in w]


def H_of(q_yz: dict) -> float:
    qy = {y: sum(q_yz[(y, z)] for z in range(Z)) for y in range(Y)}
    out = 0.0
    for y in range(Y):
        if qy[y] == 0:
            continue
        for z in range(Z):
            p = q_yz[(y, z)] / qy[y]
            if p > 0:
                out += qy[y] * p * math.log(p / kappa[y][z])
    return out


q = {(y, z): sum(joint[(b, y, z)] for b in range(Bv)) for y in range(Y) for z in range(Z)}
w = {b: sum(joint[(b, y, z)] for y in range(Y) for z in range(Z)) for b in range(Bv)}
qb = {b: {(y, z): joint[(b, y, z)] / w[b] for y in range(Y) for z in range(Z)} for b in range(Bv)}
lhs = sum(w[b] * H_of(qb[b]) for b in range(Bv))
# I(B; Z | Y) = H(B|Y) - H(B|Y,Z)
py = {y: sum(q[(y, z)] for z in range(Z)) for y in range(Y)}
pby = {(b, y): sum(joint[(b, y, z)] for z in range(Z)) for b in range(Bv) for y in range(Y)}
HB_Y = -sum(pby[(b, y)] * math.log(pby[(b, y)] / py[y]) for b in range(Bv) for y in range(Y))
HB_YZ = -sum(joint[(b, y, z)] * math.log(joint[(b, y, z)] / q[(y, z)]) for b in range(Bv) for y in range(Y) for z in range(Z))
rhs = H_of(q) + (HB_Y - HB_YZ)
print("Lemma1(b): lhs =", lhs, " rhs =", rhs, " diff =", lhs - rhs)
HB = -sum(w[b] * math.log(w[b]) for b in range(Bv))
print("  0 <= I(B;Z|Y) =", HB_Y - HB_YZ, " <= H(B) =", HB)

# Lemma 7 moment constant: E|X_0|^4 for N(m0, I_12) equals (|m0|^2+12)^2 + 4|m0|^2 + 24 <= (|m0|^2+14)^2
for m2 in (0.0, 1.0, 7.3, 100.0):
    lhs4 = (m2 + 12) ** 2 + 4 * m2 + 24
    print(f"|m0|^2={m2}: E|X0|^4={lhs4}  (|m0|^2+14)^2={(m2 + 14) ** 2}  ok={lhs4 <= (m2 + 14) ** 2}")
# Monte Carlo confirmation of E|X_0|^4 at m0 = (1,0,...,0)
n = 200000
acc = 0.0
for _ in range(n):
    s = (1.0 + random.gauss(0, 1)) ** 2 + sum(random.gauss(0, 1) ** 2 for _ in range(11))
    acc += s * s
print("MC E|X0|^4 at |m0|^2=1:", acc / n, " formula:", 13 ** 2 + 4 + 24)

# Donsker-Varadhan MGF for Prop 2: E exp((4+5T)|z_perp|^2/(4T)) under nu = N(0, T/(4+5T)) per coord => 2
T = 1e-16
lam = 4 + 5 * T
c = lam / (4 * T)
s2 = T / lam
print("E e^{c z^2} per coordinate =", (1 - 2 * c * s2) ** -0.5, " two coordinates =", (1 - 2 * c * s2) ** -1)

# Exterior-margin threshold in T*theta (where e^{-x}(3/2 - e^{-2}/2) - sqrt3(rho+delta) = 1.3)
rho = 0.01
delta = 1e-4 / (8 * math.sqrt(3))
x = math.log((1.5 - math.exp(-2) / 2) / (1.3 + math.sqrt(3) * (rho + delta)))
print("T theta threshold for 13/10:", x, " 1/12 =", 1 / 12)

# Prop 2 lower bound positivity threshold in eps at theta = (1/2) log(1/eps) + 1, m0 = 0
for eps in (0.01, 0.0095, 0.009, 0.005):
    T = eps ** 8
    th = 0.5 * math.log(1 / eps) + 1
    lb = ((4 + 5 * T) / (4 * T)) * (rho ** 2 / 7) * math.exp(-2 * (4 + 5 * T) * th - 2 * rho * (2 + rho)) - math.log(2)
    print(f"eps={eps}: Prop2 bound at (1/2)log(1/eps)+1 (sub-Gaussian p neglected) = {lb:.3f}")

# Prop 3 correction at eps = 1/100, m0 = 0: largest t with correction < 1
eps = 0.01
T = eps ** 8
c_m0 = math.exp(-0.25) * rho ** 12 / 737280 * math.exp(-0.5 * (2 + rho) ** 2)
b = 2 * c_m0
def corr(t: float) -> float:
    logp = math.log(24) - eps ** (-4) / (36864 * t)
    p = math.exp(logp)
    Lam = 17 * 14 / (2 * T) + 4 * (math.log(2) + eps * t) * math.sqrt(t + t * t)
    return p * math.log(1 / (p * b)) + math.sqrt(p / b) * Lam
lo, hi = 10.0, 40.0
for _ in range(60):
    mid = (lo + hi) / 2
    if corr(mid) < 1:
        lo = mid
    else:
        hi = mid
print("Prop3 correction < 1 for t <=", lo, "; at t_star:", corr(10.2103), "; at 32.72:", corr(32.72))
