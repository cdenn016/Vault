"""L05: symbolic check of Lemma lem:shadow_mf_optimum (PIFB2 App. G).

(1) parent-predictive prior  int N(k_i; w k_P, s2) N(k_P; mu, S) dk_P = N(w mu, w^2 S + s2)
(2) strict mean-field component  exp E_q[log chi] -> N(w mu, s2)
(3) rigid limit s2 -> 0 of (1) -> N(w mu, w^2 S) = pushforward
(4) mean-field VFE term E_{q_i q_P}[-log chi] diverges like 1/s2 as s2->0 for
    nondegenerate factors (the rigid limit of the variational problem is singular).
"""
import sympy as sp

k, kp, mu, w, m = sp.symbols('k k_P mu omega m', real=True)
S, s2, Si = sp.symbols('S sigma2 Sigma_i', positive=True)

def N(x, mean, var):
    return sp.exp(-(x - mean)**2 / (2*var)) / sp.sqrt(2*sp.pi*var)

# (1) marginal
marg = sp.integrate(N(k, w*kp, s2) * N(kp, mu, S), (kp, -sp.oo, sp.oo), conds='none')
target = N(k, w*mu, w**2*S + s2)
r1 = sp.simplify(sp.log(sp.simplify(marg)) - sp.log(target))
print('(1) log marginal - log N(w mu, w^2 S + s2) =', sp.simplify(sp.expand(r1)))

# (2) mean-field component: E_{N(kp;mu,S)} log chi(k|kp)
Elog = sp.integrate(sp.expand_log(sp.log(N(k, w*kp, s2)), force=True) * N(kp, mu, S),
                    (kp, -sp.oo, sp.oo), conds='none')
Elog = sp.simplify(Elog)
# k-dependence: coefficient of k^2 and k
poly = sp.Poly(sp.expand(Elog), k)
print('(2) MF log-component k^2 coeff =', sp.simplify(poly.coeff_monomial(k**2)),
      '; k coeff =', sp.simplify(poly.coeff_monomial(k)),
      '=> precision 1/s2, mean w*mu (parent variance S dropped into constant)')

# (3) rigid limit of predictive variance
print('(3) lim_{s2->0} predictive variance =', sp.limit(w**2*S + s2, s2, 0))

# (4) MF expected link energy for product q_i=N(m,Si), q_P=N(mu,S)
E_link = ((m - w*mu)**2 + Si + w**2*S) / (2*s2) + sp.log(2*sp.pi*s2)/2
print('(4) E[-log chi] =', E_link, '; limit s2->0+ :', sp.limit(E_link, s2, 0, '+'))

# Jensen gap (closed form): predictive-prior cross-entropy vs MF conditional cross-entropy, q_i = N(m, Si)
V = w**2*S + s2
ce_pred = sp.log(2*sp.pi*V)/2 + (Si + (m - w*mu)**2)/(2*V)
gap = sp.simplify(E_link - ce_pred)
print('(5) E_{q_i q_P}[-log chi] - E_{q_i}[-log int chi q_P] =', gap)
vals = {m: 0.3, mu: -0.2, w: 1.7, S: 0.8, Si: 0.5, s2: 0.1}
print('    numeric gap at sample point =', float(gap.subs(vals)), '(>=0 by Jensen: the shadow term undercuts the MF-VFE term)')
# numeric check of ce_pred by quadrature
import numpy as np
from scipy.integrate import quad
f = lambda x: -np.log(np.exp(-(x-1.7*-0.2)**2/(2*(1.7**2*0.8+0.1)))/np.sqrt(2*np.pi*(1.7**2*0.8+0.1))) * np.exp(-(x-0.3)**2/(2*0.5))/np.sqrt(2*np.pi*0.5)
print('    quadrature check of predictive cross-entropy residual =', quad(f,-30,30)[0]-float(ce_pred.subs(vals)))
