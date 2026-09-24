"""L04: PIFB2 673 'tau = kappa sqrt(K_q) ... canonical form is dimensionless in K_q'.
Diagonal Gaussians with iid per-coordinate parameters: mean of E_ij grows ~K, spread across sources ~sqrt(K).
So E/(kappa sqrt K) has O(1) logit differences but O(sqrt K) absolute logits."""
import numpy as np
rng = np.random.default_rng(4)
for K in (4, 16, 64, 256):
    Es = []
    for _ in range(400):
        m0, m1 = rng.normal(size=K), rng.normal(size=K); v0, v1 = rng.uniform(0.5, 2, K), rng.uniform(0.5, 2, K)
        Es.append(0.5*np.sum(v0/v1 + (m1-m0)**2/v1 - 1 + np.log(v1/v0)))
    Es = np.array(Es)
    print(f'K={K:4d}: mean E={Es.mean():8.2f} (mean/K={Es.mean()/K:.3f}); std E={Es.std():7.2f} (std/sqrt K={Es.std()/np.sqrt(K):.3f})')
