"""L05: sign of the 'savings' from removing intra-cluster alignment terms at the Gibbs optimum.
Row value at beta*: A_i = -tau log sum_j pi_j exp(-E_j/tau)  (Gibbs/DV value of sum beta E + tau KL(beta||pi)).
Remove the intra-cluster sources j in I (keep the extra-cluster sources), either with the prior left unnormalized
or renormalized over the remaining sources.  High coherence: intra-cluster E ~ eps small.
"""
import numpy as np
rng = np.random.default_rng(3)
def A(E, logpi, tau):
    z = logpi - E/tau; mx = z.max(); return -tau*(mx + np.log(np.exp(z - mx).sum()))
tau = 1.0
worst_unnorm, worst_renorm, trials = np.inf, np.inf, 0
for t in range(20000):
    nin, nout = rng.integers(1, 6), rng.integers(1, 6)
    eps = 10**rng.uniform(-3, -0.5)
    Ein = rng.uniform(0, eps, nin); Eout = rng.uniform(eps, 5.0, nout)   # extra-cluster sources less aligned
    pi = rng.dirichlet(np.ones(nin+nout)); lp = np.log(pi)
    full = A(np.r_[Ein, Eout], lp, tau)
    un = A(Eout, lp[nin:], tau)                              # drop terms, prior not renormalized
    rn = A(Eout, lp[nin:] - np.log(pi[nin:].sum()), tau)     # renormalized prior over survivors
    worst_unnorm = min(worst_unnorm, un - full); worst_renorm = min(worst_renorm, rn - full); trials += 1
print(f'{trials} random rows with intra-cluster E < eps <= extra-cluster E:')
print('  min over trials of [A_after - A_before], prior unnormalized :', worst_unnorm)
print('  min over trials of [A_after - A_before], prior renormalized :', worst_renorm)
print('  (both >= 0: removing the coherent sources RAISES the optimized row value; no savings)')
# energetic part only (what the |I| eps bound caps), before re-optimization
E = np.r_[0.01, 0.02, 2.0, 3.0]; lp = np.log(np.full(4, 0.25))
b = np.exp(lp - E/tau); b /= b.sum()
print('  example row: sum_{j in I} beta_j E_j =', (b[:2]*E[:2]).sum(), ' <= eps =', 0.02,
      ';  A_before =', A(E, lp, tau), ' A_after(renorm) =', A(E[2:], lp[2:]-np.log(0.5), tau))
