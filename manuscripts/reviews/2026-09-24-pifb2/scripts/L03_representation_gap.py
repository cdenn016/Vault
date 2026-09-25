r"""L03: scope of the conditional representation theorem (thm:representation_app, PIFB2.tex l.3036-3161) vs the
canonical scalar functional (eq:free_energy_functional_final, l.689; executable authority per l.733).
(1) sympy: for D(q,p)=int p f(q/p), the second-slot (sender) functional derivative is f(r) - r f'(r); for KL it is 1 - r,
    i.e. a 1/q-type term in the free-form stationarity of any agent that is also a sender. No nonzero f makes both
    the receiver derivative f'(r) and the sender derivative f(r)-r f'(r) affine in log r.
(2) numeric: two agents, 1D, Omega=1, beta_12=beta_21=1 (B=1), priors p1=N(0,1), p2=N(3,0.25). The best-response
    (geometric-pool) fixed point, i.e. the theorem's stationary form applied to each receiver with the neighbor held fixed,
    is not a stationary point of the joint scalar F = sum_i KL(q_i||p_i) + KL(q1||q2) + KL(q2||q1).
(3) free-form residual at the Gaussian joint minimizer: 2 log q1 - log p1 - log q2 - q2/q1 is not constant in x.
"""
import sympy as sp
import numpy as np
from scipy.optimize import minimize
r, a, b, c, d = sp.symbols('r a b c d', real=True)
f = sp.Function('f')
q, p = sp.symbols('q p', positive=True)
Dint = p*f(q/p)
sender = sp.simplify(sp.diff(Dint, p))
print("(1) d/dp [p f(q/p)] =", sender)
fKL = r*sp.log(r) - r + 1
print("    KL: receiver f'(r) =", sp.simplify(sp.diff(fKL, r)), "; sender f(r)-r f'(r) =", sp.simplify(fKL - r*sp.diff(fKL, r)))
# both affine in log r:  f' = a log r + b  and  f - r f' = c log r + d  =>  differentiate second: -r f'' = c/r, first: f'' = a/r
sol = sp.solve([sp.Eq(-r*(a/r), c/r)], [a, c], dict=True)
print("    compatibility -r*f'' = c/r with f'' = a/r for all r:", sp.simplify(-a - c/r), "= 0 for all r  => a = c = 0 (f affine, D = 0)")

def kl1(m1, v1, m2, v2): return 0.5*(np.log(v2/v1) + v1/v2 + (m2-m1)**2/v2 - 1)
mp1, vp1, mp2, vp2 = 0.0, 1.0, 3.0, 0.25
def Fjoint(x):
    m1, lv1, m2, lv2 = x; v1, v2 = np.exp(lv1), np.exp(lv2)
    return kl1(m1, v1, mp1, vp1) + kl1(m2, v2, mp2, vp2) + kl1(m1, v1, m2, v2) + kl1(m2, v2, m1, v1)
# best-response geometric pool: q_i ∝ p_i^{1/2} q_j^{1/2}
m1, v1, m2, v2 = 0.0, 1.0, 3.0, 0.25
for _ in range(200):
    l1 = 0.5/vp1 + 0.5/v2; n1 = (0.5*mp1/vp1 + 0.5*m2/v2)/l1
    l2 = 0.5/vp2 + 0.5/(1/l1); n2 = (0.5*mp2/vp2 + 0.5*n1*l1)/l2
    m1, v1, m2, v2 = n1, 1/l1, n2, 1/l2
x_nash = np.array([m1, np.log(v1), m2, np.log(v2)])
def grad(F, x, h=1e-6):
    return np.array([(F(x+h*e)-F(x-h*e))/(2*h) for e in np.eye(len(x))])
# receiver-only check: q1 best-responds to fixed q2
def F1(x1): return kl1(x1[0], np.exp(x1[1]), mp1, vp1) + kl1(x1[0], np.exp(x1[1]), m2, v2)
print(f"(2) geometric-pool fixed point: q1=N({m1:.4f},{v1:.4f}), q2=N({m2:.4f},{v2:.4f})")
print(f"    receiver-only gradient of F_1 at q1 (should be 0): {np.linalg.norm(grad(F1, x_nash[:2])):.1e}")
gj = grad(Fjoint, x_nash)
print(f"    joint-scalar gradient at that point: {np.round(gj, 5)}  norm {np.linalg.norm(gj):.4f}")
res = minimize(Fjoint, x_nash, method="BFGS", options={"gtol": 1e-12})
mj1, vj1, mj2, vj2 = res.x[0], np.exp(res.x[1]), res.x[2], np.exp(res.x[3])
print(f"    joint minimizer: q1=N({mj1:.4f},{vj1:.4f}), q2=N({mj2:.4f},{vj2:.4f}); F_joint {res.fun:.6f} vs at pool {Fjoint(x_nash):.6f}")
# (3) free-form stationarity residual of the joint scalar in q1 at the Gaussian joint minimizer
xs = np.linspace(-2, 4, 7)
lg = lambda x, m, v: -(x-m)**2/(2*v) - 0.5*np.log(2*np.pi*v)
resid = 2*lg(xs, mj1, vj1) - lg(xs, mp1, vp1) - lg(xs, mj2, vj2) - np.exp(lg(xs, mj2, vj2) - lg(xs, mj1, vj1))
print(f"(3) free-form residual 2log q1 - log p1 - log q2 - q2/q1 on x in [-2,4]: {np.round(resid, 3)} (not constant => no free-form Gaussian stationary point)")
