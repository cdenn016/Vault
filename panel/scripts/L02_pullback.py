r"""L02: Pullback metrics G_i = sigma_i^* g_B on a 2D base (PIFB2.tex 1867-1893, 2015-2037).

(a) Recompute the Gaussian example G_{mu nu} = d_mu m^T S^-1 d_nu m + (1/2) tr(S^-1 d_mu S S^-1 d_nu S)
    from the KL second-order jet along the section (independent of the closed form).
(b) PSD and rank: rank G(c) = rank d sigma(c); isotropic constant case.
(c) Frame dependence: constant g (isometry) vs c-dependent g(c) acting on the section.
(d) The frame-stripped (ambient-frame) section qhat = rho(U^{-1}) q is invariant under the local
    lattice-gauge action U -> g(c) U, q -> rho(g(c)) q, so its pullback is a regulator-free
    locally-gauge-invariant tensor; the ordinary fixed-gauge pullback is not.
(e) Combined tensor tr(A A) + Fisher: signature depends on the generator normalization.
"""
import numpy as np
from scipy.linalg import expm
rng = np.random.default_rng(1)
K = 3

def kl(m1, S1, m2, S2):
    S2i = np.linalg.inv(S2); d = m2 - m1
    return 0.5*(np.log(np.linalg.det(S2)/np.linalg.det(S1)) + np.trace(S2i@S1) + d@S2i@d - len(m1))

# smooth section on R^2
Wm = rng.standard_normal((K, 2)); Wm2 = rng.standard_normal((K, 3))
B0 = rng.standard_normal((K, K)); B1 = rng.standard_normal((K, K)); B2 = rng.standard_normal((K, K))
def section(c):
    x, y = c
    m = Wm@np.array([x, y]) + Wm2@np.array([x*x, x*y, np.sin(y)])
    L = B0 + x*B1 + np.sin(x*y)*B2
    S = L@L.T + 0.3*np.eye(K)
    return m, S

def G_formula(sec, c, h=1e-5):
    m, S = sec(c); Si = np.linalg.inv(S)
    dm = []; dS = []
    for k in range(2):
        e = np.zeros(2); e[k] = h
        mp, Sp = sec(c+e); mm, Sm = sec(c-e)
        dm.append((mp-mm)/(2*h)); dS.append((Sp-Sm)/(2*h))
    G = np.zeros((2, 2))
    for a in range(2):
        for b in range(2):
            G[a, b] = dm[a]@Si@dm[b] + 0.5*np.trace(Si@dS[a]@Si@dS[b])
    return G

def G_kljet(sec, c, h=1e-4):
    # KL(q(c)||q(c+s)) = (1/2) G_ab s^a s^b + O(s^3), so G_ab = Hessian of KL at s=0
    m0, S0 = sec(c)
    f = lambda s: kl(m0, S0, *sec(c+s))
    G = np.zeros((2, 2))
    for a in range(2):
        for b in range(2):
            ea = np.zeros(2); ea[a] = h; eb = np.zeros(2); eb[b] = h
            G[a, b] = (f(ea+eb) - f(ea-eb) - f(-ea+eb) + f(-ea-eb))/(4*h*h)
    return G

c0 = np.array([0.37, -0.52])
Gf = G_formula(section, c0); Gk = G_kljet(section, c0)
print("(a) closed-form G:\n", Gf, "\n    KL-jet G:\n", Gk)
print(f"    rel.err ||Gf-Gk||/||Gf|| = {np.linalg.norm(Gf-Gk)/np.linalg.norm(Gf):.2e}")
print("    eigenvalues:", np.linalg.eigvalsh(Gf))

# (b) degenerate section: depends on c only through x+y  => d sigma has kernel (1,-1)
def section_deg(c):
    return section(np.array([c[0]+c[1], 0.2]))
Gd = G_formula(section_deg, c0)
print("(b) section factoring through x+y: eigenvalues", np.linalg.eigvalsh(Gd), " kernel check G(1,-1) =", Gd@np.array([1, -1]))
# isotropic constant covariance
sig2 = 0.49
def section_iso(c):
    m, _ = section(c); return m, sig2*np.eye(K)
Gi = G_formula(section_iso, c0)
dm = np.array([(section(c0+np.eye(2)[k]*1e-5)[0]-section(c0-np.eye(2)[k]*1e-5)[0])/2e-5 for k in range(2)])
print(f"    isotropic constant case: ||G - dm dm^T/sigma^2|| = {np.linalg.norm(Gi - dm@dm.T/sig2):.2e} (scale {np.linalg.norm(Gi):.2e})")

# (c) constant congruence g vs c-dependent g(c)
g_const = rng.standard_normal((K, K)) + 2*np.eye(K)
def act(g, sec):
    return lambda c: (g(c)@sec(c)[0], g(c)@sec(c)[1]@g(c).T)
Gc = G_formula(act(lambda c: g_const, section), c0)
print(f"(c) constant g in GL(3): ||G[g.sigma]-G[sigma]||/||G|| = {np.linalg.norm(Gc-Gf)/np.linalg.norm(Gf):.2e}")
X1 = rng.standard_normal((K, K)); X2 = rng.standard_normal((K, K))
g_loc = lambda c: expm(0.8*c[0]*X1 + 0.5*np.sin(c[1])*X2)
Gl = G_formula(act(g_loc, section), c0)
print(f"    local g(c):        ||G[g.sigma]-G[sigma]||/||G|| = {np.linalg.norm(Gl-Gf)/np.linalg.norm(Gf):.2e}  (ordinary fixed-gauge pullback is not locally invariant)")

# (d) frame-stripped section with Regime-I frames U(c)=exp(phi(c)); lattice action U->gU, q->rho(g)q
P1 = rng.standard_normal((K, K)); P2 = rng.standard_normal((K, K))
U = lambda c: expm(0.4*c[0]*P1 + 0.3*c[1]**2*P2)
def stripped(Ufun, sec):
    return lambda c: (np.linalg.solve(Ufun(c), sec(c)[0]), np.linalg.solve(Ufun(c), np.linalg.solve(Ufun(c), sec(c)[1]).T).T)
Ghat = G_formula(stripped(U, section), c0)
Ug = lambda c: g_loc(c)@U(c)
Ghat_g = G_formula(stripped(Ug, act(g_loc, section)), c0)
print(f"(d) frame-stripped pullback under local lattice gauge: ||Ghat'-Ghat||/||Ghat|| = {np.linalg.norm(Ghat_g-Ghat)/np.linalg.norm(Ghat):.2e}")
# global right translation U -> U g (constant), beliefs unchanged
Ur = lambda c: U(c)@g_const
Ghat_r = G_formula(stripped(Ur, section), c0)
print(f"    under global right translation U->U g:          ||Ghat'-Ghat||/||Ghat|| = {np.linalg.norm(Ghat_r-Ghat)/np.linalg.norm(Ghat):.2e}")
# the horizontal trace block under the same local lattice gauge
def trAA(Ufun, c, h=1e-5):
    A = []
    for k in range(2):
        e = np.zeros(2); e[k] = h
        dU = (Ufun(c+e)-Ufun(c-e))/(2*h)
        A.append(np.linalg.solve(Ufun(c), dU))
    return np.array([[np.trace(A[a]@A[b]) for b in range(2)] for a in range(2)])
T0 = trAA(U, c0); Tg = trAA(Ug, c0)
print(f"    horizontal tr(A A) under local lattice gauge:   ||T'-T||/||T|| = {np.linalg.norm(Tg-T0)/np.linalg.norm(T0):.2e} (not invariant, as the manuscript says)")

# local right translation U -> U h(c) (the action used in prop:regulator_obstruction): q_i and Omega_ij untouched
Uh = lambda c: U(c)@g_loc(c)
print(f"    local right U->U h(c): ordinary score pullback of q unchanged by construction (q not acted on); "
      f"tr(AA) rel.change {np.linalg.norm(trAA(Uh, c0)-T0)/np.linalg.norm(T0):.2e}; "
      f"frame-stripped pullback rel.change {np.linalg.norm(G_formula(stripped(Uh, section), c0)-Ghat)/np.linalg.norm(Ghat):.2e} (connection-relative)")

# (e) combined tensor signature vs generator normalization (Prop. 4d-type time direction)
# time direction: horizontal block -2 kappa (d psi)^2 with tr(T^2)=2 kappa ; Fisher tt entry f>0
f_tt = 0.9; dpsi = 0.6
for kappa in [0.5, 1.0, 2.0]:
    Gtt = -2*kappa*dpsi**2 + f_tt
    print(f"(e) tr(S^2) = {-2*kappa:+.1f}: combined G_tt = {Gtt:+.3f} -> {'timelike' if Gtt < 0 else 'NOT timelike'}")
