"""Independent numeric checks for the seeded hidden-information claim (Fable verifier).

All quantities are plain floats; nothing here is a proof, only a check of the
displayed constants and of the exterior-residual margin at T*theta = 1/12.
"""
from __future__ import annotations

import math

rho = 1 / 100


def h_b(p: float) -> float:
    if p <= 0 or p >= 1:
        return 0.0
    return -p * math.log(p) - (1 - p) * math.log(1 - p)


def eta(theta: float, T: float) -> float:
    return 9 * rho**2 * math.exp(-8 * theta) / (2 * T) + 3 * math.exp(-16 * theta) / (
        4 * (1 - math.exp(-8 * theta))
    )


def r_ratio(theta: float, epsL: float) -> float:
    return 2 * math.exp(epsL * theta) - 1


def tau_cheb(theta: float, eps: float) -> float:
    return 73728 * eps**4 * theta


def log_tau_subg(theta: float, eps: float) -> float:
    return math.log(24) - eps ** (-4) / (36864 * theta)


def p_theta(theta: float, eps: float, epsL: float, tube: str) -> float:
    T = eps**8
    tau = tau_cheb(theta, eps) if tube == "cheb" else math.exp(log_tau_subg(theta, eps))
    dep = 4 * r_ratio(theta, epsL) * (theta - 0.25) * math.exp(-1 / T) if 1 / T < 700 else 0.0
    return tau + dep


def kappa(theta: float, eps: float, epsL: float, tube: str) -> float:
    T = eps**8
    p = p_theta(theta, eps, epsL, tube)
    return (eta(theta, T) + h_b(p)) / (1 - p)


eps = 1 / 100
T = eps**8
t_eps = 2 * math.log(1 / eps)
t_star = t_eps + 1
print("eps, T, t_eps, t_star:", eps, T, t_eps, t_star)
for th in (t_eps, t_star):
    print(f"theta={th:.4f}: eta={eta(th, T):.3e}  r={r_ratio(th, eps):.4f}  "
          f"p_cheb={p_theta(th, eps, eps, 'cheb'):.3e}  kappa_cheb={kappa(th, eps, eps, 'cheb'):.3e}  "
          f"log tau_subg={log_tau_subg(th, eps):.1f}  kappa_subg={kappa(th, eps, eps, 'subg'):.3e}")

# Exterior residual margin: e^{-T t}(3/2 - e^{-8t}/2) - sqrt3 (rho + delta_eps) >= 13/10 on [1/4, theta]
delta_eps = eps**2 / (8 * math.sqrt(3))
g_quarter = math.exp(-T / 4) * (1.5 - math.exp(-2) / 2)
g_end = math.exp(-1 / 12) * (1.5 - math.exp(-2) / 2)  # worst case at T theta = 1/12 with e^{-8 theta} <= e^{-2}
pert = math.sqrt(3) * (rho + delta_eps)
print("exterior at t=1/4:", g_quarter - pert, " exterior at T theta=1/12:", g_end - pert, " need > 1.3")
print("interior at t=1/4:", math.exp(-2) + pert, " need < 0.2")
# Sanity: T theta = 0.09 fails
print("exterior at T theta=0.09:", math.exp(-0.09) * (1.5 - math.exp(-2) / 2) - pert)

# Contrast qualification: selected residual <= e^{-8t} + sqrt3 rho e^{-4t} + eps^2/8 <= eps^2 for t >= (1/2) log(1/eps)
t_half = 0.5 * math.log(1 / eps)
print("selected residual bound at t=(1/2)log(1/eps), in units of eps^2:",
      (math.exp(-8 * t_half) + math.sqrt(3) * rho * math.exp(-4 * t_half) + eps**2 / 8) / eps**2)

# Lower-bound proposition 2: two-coordinate inequality (x1+x2)/2 - 1 - (1/2) log(x1 x2) >= (x1+x2)/4 - log 2
worst = min(
    (s / 2 - 1 - math.log(s / 2)) - (s / 4 - math.log(2))  # x1 = x2 = s/2 is the worst split at fixed s
    for s in [k / 1000 for k in range(1, 200000)]
)
print("min over s of [phi2(s) - (s/4 - log2)] (should be >= 0, = 0 at s=4):", worst)

# Prop 2 magnitude at theta = (1/2) log(1/eps) + 1 and theta = log(1/eps) - s
lam = 4 + 5 * T
for th in (t_half + 1, math.log(1 / eps) - 2, math.log(1 / eps) - 1, math.log(1 / eps)):
    p = p_theta(th, eps, eps, "cheb")
    lb = (lam / (4 * T)) * ((rho**2 / 7) * math.exp(-2 * lam * th - 2 * rho * (0 + 2 + rho)) - 3 * rho**2 * math.sqrt(p)) - math.log(2)
    print(f"Prop2 lower bound at theta={th:.3f}: {lb:.3e}")

# Seed probability at m0 = 0
c_m0 = math.exp(-0.25) * rho**12 / 737280 * math.exp(-0.5 * (2 + rho) ** 2)
print("c(m0=0) =", c_m0, " 2c =", 2 * c_m0)

# Prop 3 correction sizes with sub-Gaussian tube, m0 = 0, epsL = eps
b = 2 * c_m0
for t in (t_star, 100.0, 1e3, 1e4, 1e5, 1e6, 1e7, eps ** (-4) / (663552 * math.log(1 / eps))):
    if 1 / T < 700:
        pass
    logp = log_tau_subg(t, eps)
    p = math.exp(logp)
    Lam = 17 * (0 + 14) / (2 * T) + 4 * (math.log(2) + eps * t) * math.sqrt(t + t * t)
    corr = p * math.log(1 / (p * b)) + math.sqrt(p / b) * Lam if p > 0 else 0.0
    print(f"t={t:.3e}: log p={logp:.1f}  correction={corr:.3e}")
