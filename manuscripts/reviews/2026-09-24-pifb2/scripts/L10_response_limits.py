r"""L10: limits of the two-term 'physical interpretation' split at PIFB2 2408-2414.

For one receiver row with energies e_j = KL_ij and gradients g_j = grad KL_ij, the surrogate gradient is
  T1 + T2,  T1 = sum_j beta_j (1 - e_j/kappa) g_j,  T2 = (1/kappa)(sum_j beta_j e_j)(sum_k beta_k g_k),
and T1 + T2 = sum_j beta_j g_j - (1/kappa) Cov_beta(e, g)  (the response term of 2239).
Checks: (i) additive shift e_j -> e_j + c leaves beta and T1+T2 invariant but changes T1 and T2 separately;
(ii) kappa -> 0 at nondegenerate energies: T1, T2 diverge like 1/kappa, the net response vanishes;
(iii) two neighbors with gap delta: sup over kappa of |response| / |g1-g2| = max_x x e^{-x}/(1+e^{-x})^2 ~ 0.224, attained at kappa ~ delta/1.54; response bounded uniformly in kappa.
"""
import numpy as np
rng = np.random.default_rng(7)
e = np.array([0.8, 1.3, 2.9]); g = rng.standard_normal((3, 4))

def split(e, g, kap):
    w = np.exp(-(e - e.min()) / kap); b = w / w.sum()
    T1 = (b * (1 - e / kap)) @ g; T2 = (b @ e) / kap * (b @ g)
    resp = T1 + T2 - b @ g
    cov = (b * (e - b @ e)) @ (g - b @ g)
    return b, T1, T2, resp, cov

print("(i) shift invariance at kappa=0.5")
for c in (0.0, 5.0, 50.0):
    b, T1, T2, resp, cov = split(e + c, g, 0.5)
    print(f"  c={c:5.1f}: |T1|={np.linalg.norm(T1):9.3f} |T2|={np.linalg.norm(T2):9.3f} |T1+T2|={np.linalg.norm(T1+T2):.12f}")
print("(ii) nondegenerate energies e=(0.8,1.3,2.9)")
for kap in (10.0, 1.0, 0.3, 0.1, 0.03, 0.01):
    b, T1, T2, resp, cov = split(e, g, kap)
    print(f"  kappa={kap:6.2f}: |T1|={np.linalg.norm(T1):10.3e} |T2|={np.linalg.norm(T2):10.3e} |net response|={np.linalg.norm(resp):10.3e}  (check -Cov/kappa: {np.linalg.norm(resp + cov/kap):.1e})")
print("(iii) two neighbors, gap delta=0.01")
g2 = rng.standard_normal((2, 4)); d = np.linalg.norm(g2[0] - g2[1])
for kap in (1.0, 0.1, 0.02, 0.0065, 0.003, 0.001, 0.0001):
    b, T1, T2, resp, cov = split(np.array([0.8, 0.81]), g2, kap)
    print(f"  kappa={kap:7.4f}: |net response|/|g1-g2|={np.linalg.norm(resp)/d:8.4f}  |T1|={np.linalg.norm(T1):9.2e}")
x = np.linspace(0.01, 10, 100000); f = x*np.exp(-x)/(1+np.exp(-x))**2
print(f"  analytic sup = {f.max():.4f} at delta/kappa = {x[f.argmax()]:.3f}")
