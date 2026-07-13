import sympy as sp

x, tau, b0, c0, D = sp.symbols("x tau b0 c0 D", positive=True)

# Same-functional mass/stiffness degeneracy.
h1, h2 = sp.symbols("h1 h2", positive=True)
H = sp.diag(h1, h2)
assert H.inv() * H == sp.eye(2)

# Independent kinetic and stiffness tensors.
m1, m2, k1, k2 = sp.symbols("m1 m2 k1 k2", positive=True)
assert sp.diag(m1, m2).inv() * sp.diag(k1, k2) == sp.diag(k1 / m1, k2 / m2)

# Canonical versus entropy-suppressed two-edge attention.
beta = sp.exp(-x / tau) / (1 + sp.exp(-x / tau))
F_red = -tau * sp.log((1 + sp.exp(-x / tau)) / 2)
S = beta * x
assert sp.simplify(sp.diff(F_red, x) - beta) == 0
assert sp.simplify(sp.diff(S, x) - (beta - x * beta * (1 - beta) / tau)) == 0
assert sp.N(sp.diff(S, x).subs({x: 2, tau: 1})) < 0

# Adaptive-precision derivatives.
alpha = c0 / (b0 + D)
R = b0 * alpha - c0 * sp.log(alpha)
assert sp.simplify(sp.diff(alpha * D, D) - b0 * c0 / (b0 + D) ** 2) == 0
assert sp.simplify(sp.diff(alpha * D + R, D) - c0 / (b0 + D)) == 0

# Finite-temperature attractive coupling shrinks a two-cluster gap.
a, sigma2 = sp.symbols("a sigma2", positive=True)
gap = 2 * a
beta_cross = sp.exp(-gap**2 / (2 * sigma2 * tau)) / (
    1 + sp.exp(-gap**2 / (2 * sigma2 * tau))
)
gap_dot = -2 * beta_cross * gap / sigma2
assert sp.ask(sp.Q.negative(gap_dot)) is True

# Linear consensus and anchored equilibrium identities.
w, lam, anchor = sp.symbols("w lam anchor", positive=True)
L = sp.Matrix([[w, -w], [-w, w]])
A = sp.diag(anchor, anchor)
assert (sp.ones(1, 2) * L) == sp.zeros(1, 2)
assert sp.simplify((A + lam * L).inv() * A * sp.ones(2, 1) - sp.ones(2, 1)) == sp.zeros(2, 1)

# A nonuniform reversible Dirichlet energy retains D_rho under the unweighted
# primary product Fisher metric, while the additional G_rho metric cancels it.
rho1, rho2 = sp.symbols("rho1 rho2", positive=True)
D_rho = sp.diag(rho1, rho2)
I2 = sp.eye(2)
primary_generator = I2.inv() * D_rho * L
weighted_generator = D_rho.inv() * D_rho * L
assert sp.simplify(primary_generator - D_rho * L) == sp.zeros(2)
assert sp.simplify(weighted_generator - L) == sp.zeros(2)
assert sp.simplify(primary_generator - L).subs({rho1: 2, rho2: 3}) != sp.zeros(2)

# At fixed Fisher geometry and learning rate, scalar first-order relaxation
# becomes faster, not slower, as positive stiffness increases.
eta, g, stiffness_lo, stiffness_hi = sp.symbols(
    "eta g stiffness_lo stiffness_hi", positive=True
)
rate_lo = eta * stiffness_lo / g
rate_hi = eta * stiffness_hi / g
tau_lo = 1 / rate_lo
tau_hi = 1 / rate_hi
assert sp.simplify(tau_hi / tau_lo - stiffness_lo / stiffness_hi) == 0
assert (tau_hi < tau_lo).subs({stiffness_hi: 2, stiffness_lo: 1}) is sp.S.true

# Complete derivatives of a fixed asymmetric scalar potential conserve net force.
x1, x2, beta12, beta21, ell1, ell2 = sp.symbols(
    "x1 x2 beta12 beta21 ell1 ell2", positive=True
)
V = (
    beta12 * ell2 * (x1 - x2) ** 2 / 2
    + beta21 * ell1 * (x2 - x1) ** 2 / 2
)
force1 = -sp.diff(V, x1)
force2 = -sp.diff(V, x2)
assert sp.simplify(force1 + force2) == 0

# Damped forced-oscillator resonance for independently chosen m and k.
m, k, gamma, omega = sp.symbols("m k gamma omega", positive=True)
denominator = (k - m * omega**2) ** 2 + gamma**2 * omega**2
omega_sq = k / m - gamma**2 / (2 * m**2)
stationarity = sp.diff(denominator, omega) / (2 * omega)
assert sp.simplify(stationarity.subs(omega**2, omega_sq)) == 0

print("belief-inertia symbolic checks: PASS")
