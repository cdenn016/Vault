"""L05: PIFB2 App. H checks.
(1) thm:nested_state_configuration_vfe on a finite discrete model (random R, Q_X);
(2) vacuum-prior decomposition T KL(R||P0) = E_R F_vac + T KL(R||nu0) + T log Z0;
(3) T_cfg -> 0 limit of the nested optimum: R* concentrates on argmin F_vac independently of o;
(4) 1D effective action: G = T (Gamma'')^{-1} and the one-loop value -T log Z = A + (T/2) log(A''/(2 pi T)) + O(T^2).
"""
import numpy as np
from scipy.integrate import quad
rng = np.random.default_rng(7)
nX, nY, no = 3, 4, 2
P0 = rng.dirichlet(np.ones(nX)); pY = rng.dirichlet(np.ones(nY), size=nX); po = rng.dirichlet(np.ones(no), size=(nX, nY))
o = 1; T = 0.7
joint = P0[:, None]*pY*po[:, :, o]; p_o = joint.sum(); post = joint/p_o
R = rng.dirichlet(np.ones(nX)); Q = rng.dirichlet(np.ones(nY), size=nX)
Fstate = [(Q[x]*np.log(Q[x]/pY[x])).sum() - (Q[x]*np.log(po[x, :, o])).sum() for x in range(nX)]
J = T*(R*np.log(R/P0)).sum() + T*(R*np.array(Fstate)).sum()
RQ = R[:, None]*Q
rhs = -T*np.log(p_o) + T*(RQ*np.log(RQ/post)).sum()
print('(1) nested identity residual J - rhs =', J - rhs)
# (2)
Fvac = rng.normal(size=nX); nu0 = rng.random(nX)*2   # nu0 not normalized
Z0 = (np.exp(-Fvac/T)*nu0).sum(); P0v = np.exp(-Fvac/T)*nu0/Z0
lhs = T*(R*np.log(R/P0v)).sum(); rhs2 = (R*Fvac).sum() + T*(R*np.log(R/nu0)).sum() + T*np.log(Z0)
print('(2) vacuum decomposition residual =', lhs - rhs2)
# (3) data-blindness of the T->0 limit: X in R, F_vac = X^2/2 (nu0 = Lebesgue), p(o|X) = N(o; X, 1); R* propto exp(-F_vac/T) p(o|X)
for T_ in (1.0, 0.1, 0.01, 0.001):
    for o_ in (0.0, 5.0):
        L = 8*np.sqrt(T_) + abs(o_)*T_/(1+T_)
        num = quad(lambda x: x*np.exp(-x*x/(2*T_) - (o_-x)**2/2), -L, L, points=[0], limit=200)[0]
        den = quad(lambda x: np.exp(-x*x/(2*T_) - (o_-x)**2/2), -L, L, points=[0], limit=200)[0]
        print(f'(3) T_cfg={T_:g} o={o_:g}: E_R*[X] = {num/den:.6f}  (closed form o T/(1+T) = {o_*T_/(1+T_):.6f})')
# (4) 1D action A(xi) = a xi^2/2 + g xi^4/24 + c xi^3/6
a, g, c = 1.3, 0.8, 0.4
Aof = lambda x: a*x*x/2 + c*x**3/6 + g*x**4/24
def W(Jsrc, T_):
    f = lambda x: np.exp(-(Aof(x) - Jsrc*x)/T_)
    return T_*np.log(quad(f, -12, 12, limit=400)[0])
T_ = 0.05; h = 1e-3
W0 = W(0, T_); Wp = W(h, T_); Wm = W(-h, T_)
phi = (Wp - Wm)/(2*h); W2 = (Wp - 2*W0 + Wm)/h**2
var = quad(lambda x: x*x*np.exp(-Aof(x)/T_), -12, 12)[0]/quad(lambda x: np.exp(-Aof(x)/T_), -12, 12)[0]
mean = quad(lambda x: x*np.exp(-Aof(x)/T_), -12, 12)[0]/quad(lambda x: np.exp(-Aof(x)/T_), -12, 12)[0]
print('(4) phi - <xi> =', phi - mean, ';  T W\'\' - Var(xi) =', T_*W2 - (var - mean**2))
# Gamma'' = 1/W'' (Legendre) -> G = T/Gamma'' = T W''
for T_ in (0.08, 0.04, 0.02, 0.01):
    exact = -W(0, T_)
    oneloop = Aof(0) + 0.5*T_*np.log(a/(2*np.pi*T_))
    print(f'    T={T_:g}: -T log Z - [A + (T/2) log(A\'\'/(2 pi T))] = {exact - oneloop:+.3e}  ratio to T^2 = {(exact-oneloop)/T_**2:+.4f}')
print('    predicted T^2 coefficient g/(8a^2) - 5c^2/(24a^3) =', g/(8*a*a) - 5*c*c/(24*a**3))
