"""L15: Pinsker-constant convention check for the CoverThomas2006 citation at PIFB2.tex:3902.
Cover and Thomas (2nd ed., Lemma 11.6.1) state D(P||Q) >= ||P-Q||_1^2 / (2 ln 2) in bits,
i.e. ||P-Q||_1 <= sqrt(2 D_nats). The total-variation form is TV = ||P-Q||_1 / 2 <= sqrt(D_nats / 2).
We check both numerically on random Bernoulli pairs and report the sup of the ratios."""
import numpy as np
rng = np.random.default_rng(0)
p = rng.uniform(1e-3, 1 - 1e-3, 200000); q = rng.uniform(1e-3, 1 - 1e-3, 200000)
kl = p*np.log(p/q) + (1-p)*np.log((1-p)/(1-q))
l1 = 2*np.abs(p-q); tv = l1/2
print("max TV/sqrt(KL)  =", np.max(tv/np.sqrt(kl)), " (1/sqrt2 =", 1/np.sqrt(2), ")")
print("max L1/sqrt(KL)  =", np.max(l1/np.sqrt(kl)), " (sqrt2   =", np.sqrt(2), ")")
eps = 1e-4; p0 = 0.5
k = p0*np.log(p0/(p0+eps)) + (1-p0)*np.log((1-p0)/(1-p0-eps))
print("near-tight ratio TV/sqrt(KL) at p=1/2, eps=1e-4:", eps/np.sqrt(k))
