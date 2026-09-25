"""L04: state-dependent precision, PIFB2 742-829 and 2269-2277.
 1. alpha* = c/(b+D) stationary & strictly convex; product rule; envelope cancellation with R in graph.
 2. Reduced adaptive value: min_alpha [alpha D + b alpha - c log alpha] = c + c log((b+D)/c).
 3. 'MAP precision' check: for a normalized hierarchical Gaussian prior k ~ N(mu_p, Sigma_p/alpha) with the
    stated Gamma(shape c+1, rate b) prior, the alpha-stationary point of E_q[-log p(k|alpha)] - log p(alpha) is
    (c + K/2)/(b + Q), Q = (1/2)E_q[(k-mu_p)^T Sigma_p^{-1}(k-mu_p)], which differs from c/(b+KL).
"""
import sympy as sp, numpy as np
a, b, c, D, Q, K = sp.symbols('alpha b c D Q K', positive=True)
th = sp.symbols('theta')
Dt = sp.Function('D')(th)
g = a*D + b*a - c*sp.log(a)
astar = sp.solve(sp.diff(g, a), a)[0]
print('1. alpha* =', astar, '; g\'\' =', sp.simplify(sp.diff(g, a, 2)))
ast = c/(b + Dt)
prod = sp.simplify(sp.diff(ast*Dt, th) - ast**2*b/c*sp.diff(Dt, th))
full = sp.simplify(sp.diff(ast*Dt + b*ast - c*sp.log(ast), th) - ast*sp.diff(Dt, th))
print('   product-rule residual:', prod, '; envelope (R in graph) residual:', full)
red = sp.simplify(g.subs(a, astar) - (c + c*sp.log((b + D)/c)))
print('2. reduced value residual vs c + c log((b+D)/c):', sp.simplify(sp.expand_log(red, force=True)))
# 3. hierarchical Gaussian with Gamma(c+1, b) prior on alpha
negjoint = a*Q - K/2*sp.log(a) + b*a - c*sp.log(a)
amap = sp.solve(sp.diff(negjoint, a), a)[0]
print('3. hierarchical MAP alpha =', sp.simplify(amap))
rng = np.random.default_rng(2); k = 3
M = rng.normal(size=(k, k)); Sp = M@M.T + np.eye(k); Sq = np.diag(rng.uniform(0.2, 2, k)); d = rng.normal(size=k)
Spi = np.linalg.inv(Sp)
Qv = 0.5*(np.trace(Spi@Sq) + d@Spi@d)
KLv = Qv - k/2 + 0.5*np.log(np.linalg.det(Sp)/np.linalg.det(Sq))
bv, cv = 1.0, 2.0
print(f'   numeric: K={k} Q={Qv:.4f} KL={KLv:.4f}; PIFB2 alpha*={cv/(bv+KLv):.4f}; hierarchical MAP={(cv+k/2)/(bv+Qv):.4f}')
