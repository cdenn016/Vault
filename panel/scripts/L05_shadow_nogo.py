"""L05: the hypothesis of thm:state_level_elbo_nogo holds for the child-parent shadow edge KL(q_i || T q_I)
with q_I a varying factor (the same-time shadow). Finite alphabet, T a fixed positive stochastic matrix.
Mixed third variation d^3/(ds dt^2) KL(q_i + s a || T(q_I + t h)) at 0 equals int a g, g = (T h / T q_I)^2;
choosing a = q_i (g - E g) gives Var_{q_i}(g) > 0, while any fixed-joint mean-field KL has this variation = 0.
"""
import numpy as np
rng = np.random.default_rng(4)
n = 5
qi = rng.dirichlet(np.ones(n)); qI = rng.dirichlet(np.ones(n))
T = rng.dirichlet(np.ones(n), size=n).T          # column-stochastic: (T q)(k) = sum_u T[k,u] q[u]
h = rng.normal(size=n); h -= h.mean()             # zero-mass tangent
g = ((T @ h)/(T @ qI))**2
a = qi*(g - (qi*g).sum())
KL = lambda s, t: ((qi + s*a)*np.log((qi + s*a)/(T @ (qI + t*h)))).sum()
e = 1e-3
d3 = (KL(e, e) - 2*KL(e, 0) + KL(e, -e) - KL(-e, e) + 2*KL(-e, 0) - KL(-e, -e))/(2*e*e*e)
print('finite-difference mixed third variation =', d3, '; predicted Var_q_i(g) =', (qi*g*g).sum() - (qi*g).sum()**2)
