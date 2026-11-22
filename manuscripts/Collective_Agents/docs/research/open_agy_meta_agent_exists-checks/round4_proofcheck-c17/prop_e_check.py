r"""Check of the Proposition E weight formulas (Gaussian habits, additive effects on scalar acted component Z).

eta in R^K, member j: belief m_j, act u_j in R with effect b_j e_Z on eta, outcome o = h^T eta' (+noise),
M_j = h_Z b_j (outcome-space effect, the 'mu_j' of the write-up), preference N(o*, 1/Lam), precision gamma,
habit u_j ~ N(ubar_j, sig_j^2).  z_j = h^T F m_j - o*.
D2: member j's posterior with others at habit draws.   D1: group posterior with potential
Phi(u) = G_C(u) + sum_j Lam (z_j - z_C) M_j u_j,  G_C(u) = Lam/2 (z_C + sum_j M_j u_j)^2.
World mean act input on Z: I = sum_j b_j E[u_j].  Claimed: dI/dm_{j,k} = -w_j (h^T F)_k / h_Z with
 D2: w_j = gamma Lam M_j^2 s_j^2, s_j^2 = (sig_j^-2 + gamma Lam M_j^2)^-1;
 D1: w_j = gamma Lam sig_j^2 M_j^2 / (1 + gamma Lam sum_k sig_k^2 M_k^2).
Means are computed by direct quadratic-form solves; derivatives by central differences.
"""
import os
os.environ.setdefault("OMP_NUM_THREADS", "1")
import numpy as np

rng = np.random.default_rng(11)
K, n = 3, 4
F = rng.normal(size=(K, K)); h = rng.normal(size=K); Zi = 0
b = rng.normal(size=n); M = h[Zi] * b
Lam, gam, ostar, zC = 1.7, 0.9, rng.normal(), rng.normal()
sig2 = rng.uniform(0.3, 2.0, n); ubar = rng.normal(size=n)
m = rng.normal(size=(n, K))

def zvec(m):
    return np.array([h @ F @ m[j] - ostar for j in range(n)])

def mean_D2(m):
    z = zvec(m); out = np.zeros(n)
    for j in range(n):
        # -log q(u_j) = (u_j-ubar_j)^2/(2 sig_j^2) + gam*Lam/2 (z_j + M_j u_j + sum_{k!=j} M_k ubar_k)^2
        c = z[j] + sum(M[k] * ubar[k] for k in range(n) if k != j)
        prec = 1 / sig2[j] + gam * Lam * M[j] ** 2
        out[j] = (ubar[j] / sig2[j] - gam * Lam * M[j] * c) / prec
    return out

def Phi(u, m):
    z = zvec(m)
    return Lam / 2 * (zC + M @ u) ** 2 + Lam * np.sum((z - zC) * M * u)

def mean_D1(m):
    # energy E(u) = sum (u-ubar)^2/(2 sig2) + gam*Phi(u); quadratic: extract gradient at 0 and Hessian
    Hs = np.diag(1 / sig2) + gam * Lam * np.outer(M, M)
    eps = 1e-6
    g0 = np.array([((np.sum((eps * np.eye(n)[i] - ubar) ** 2 / (2 * sig2)) + gam * Phi(eps * np.eye(n)[i], m))
                    - (np.sum((-eps * np.eye(n)[i] - ubar) ** 2 / (2 * sig2)) + gam * Phi(-eps * np.eye(n)[i], m))) / (2 * eps)
                   for i in range(n)])
    return np.linalg.solve(Hs, -g0)

def inputZ(meanfun, m):
    return b @ meanfun(m)

hF = h @ F
s2 = 1 / (1 / sig2 + gam * Lam * M ** 2)
w_D2 = gam * Lam * M ** 2 * s2
w_D1 = gam * Lam * sig2 * M ** 2 / (1 + gam * Lam * np.sum(sig2 * M ** 2))
for name, fun, w in (("D2", mean_D2, w_D2), ("D1", mean_D1, w_D1)):
    num = np.zeros((n, K)); d = 1e-5
    for j in range(n):
        for k in range(K):
            mp = m.copy(); mp[j, k] += d; mm = m.copy(); mm[j, k] -= d
            num[j, k] = (inputZ(fun, mp) - inputZ(fun, mm)) / (2 * d)
    pred = -np.outer(w, hF) / h[Zi]
    print(f"{name}: max |numerical - formula| = {np.max(np.abs(num - pred)):.3e}; weights w = {np.round(w, 6)}")
    signs = np.sign(num)
    print(f"{name}: sign pattern of dI/dm_(j,k) (rows j, cols k):\n{signs.astype(int)}")
    print(f"{name}: predicted common sign per k = {(-np.sign(h[Zi] * hF)).astype(int)}")
# individual D1 acts need not be sign-uniform: loading of E[u_i] on m_j
J = np.zeros((n, n))
for j in range(n):
    mp = m.copy(); mp[j, 0] += 1e-5; mm = m.copy(); mm[j, 0] -= 1e-5
    J[:, j] = (mean_D1(mp) - mean_D1(mm)) / 2e-5
print("D1: d E[u_i]/d m_(j,0) matrix (individual acts), for reference:\n", np.round(J, 4))
