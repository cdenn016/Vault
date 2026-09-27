"""(1) Closed walks on causal support and the content of routed loop traces.
(2) Framing consequence of L6: Gibbs row as exact posterior at every tau under a Bernoulli record."""
import itertools, numpy as np
from scipy.linalg import expm
rng = np.random.default_rng(7)
N, K, H, s = 5, 3, 2, 2
# (1) directed edge j -> i exists iff j <= i (Main l.945). A product L_{i0 i1} L_{i1 i2} ... needs i_k >= i_{k+1}.
closed, nonconst = 0, 0
for rlen in range(1, 5):
    for w in itertools.product(range(N), repeat=rlen):
        seq = list(w) + [w[0]]
        if all(seq[k] >= seq[k + 1] for k in range(rlen)):
            closed += 1
            nonconst += len(set(w)) > 1
print("causal closed walks (length 1-4):", closed, " with >1 distinct site:", nonconst)
U = [expm(0.5 * rng.standard_normal((K, K))) for _ in range(N)]
T = [rng.standard_normal((s, K)) for _ in range(H)]; O = [rng.standard_normal((K, s)) for _ in range(H)]
beta = rng.dirichlet(np.ones(N), size=(H, N))
A = lambda i, j: sum(beta[h, i, j] * O[h] @ T[h] for h in range(H))
Cl = lambda i, j: U[i] @ A(i, j) @ np.linalg.inv(U[j])
worst = 0.0
for i in range(N):
    for rlen in range(1, 5):
        Hf = np.linalg.matrix_power(Cl(i, i), rlen)
        worst = max(worst, abs(np.trace(Hf) - np.trace(np.linalg.matrix_power(A(i, i), rlen))))
print("self-loop trace, framed minus frame-free (standard W_O W_V operator):", f"{worst:.2e}")
# (2) Bernoulli compatibility record P(o=1|z,J=j)=exp(-D_ij/tau), D>=0 (capped cost also >=0).
D = np.abs(rng.standard_normal(6)) * 3; D_cap = np.minimum(D, 2.0); pi = rng.dirichlet(np.ones(6))
for tau in [0.3, 1.0, np.sqrt(32)]:
    for DD, tag in [(D, "uncapped"), (D_cap, "capped")]:
        lik1 = np.exp(-DD / tau); lik0 = 1 - lik1
        assert np.all((lik1 > 0) & (lik1 <= 1)) and np.allclose(lik1 + lik0, 1)
        post = pi * lik1 / (pi * lik1).sum()
        gibbs = np.exp(np.log(pi) - DD / tau); gibbs /= gibbs.sum()
        print(f"tau={tau:6.3f} {tag:8s} max|posterior - Gibbs| = {np.abs(post - gibbs).max():.1e}")
