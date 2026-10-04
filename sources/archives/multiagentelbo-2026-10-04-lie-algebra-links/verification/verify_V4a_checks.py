"""Numerical probes for verify_V4a (float64, CPU). Closed forms and explicit witnesses only."""
import numpy as np
from scipy.linalg import expm

rng = np.random.default_rng(0)
K = 3
h = 1e-6


def rand_spd(k):
    A = rng.standard_normal((k, k))
    return A @ A.T + k * np.eye(k)


def kl_gauss(m1, S1, m2, S2):
    k = len(m1)
    S2i = np.linalg.inv(S2)
    d = m1 - m2
    return 0.5 * (np.trace(S2i @ S1) + d @ S2i @ d - k + np.log(np.linalg.det(S2) / np.linalg.det(S1)))


def L(B, T):
    x, w = np.polynomial.legendre.leggauss(64)
    t = 0.5 * (x + 1)
    w = 0.5 * w
    return sum(wi * expm(ti * B) @ T @ expm((1 - ti) * B) for ti, wi in zip(t, w))


def fd_grad(fun, X):
    g = np.zeros_like(X)
    for a in range(X.shape[0]):
        for b in range(X.shape[1]):
            d = np.zeros_like(X)
            d[a, b] = h
            g[a, b] = (fun(X + d) - fun(X - d)) / (2 * h)
    return g


# (1) prop:glink-law-level-energy
mi, mj = rng.standard_normal(K), rng.standard_normal(K)
Si, Sj = rand_spd(K), rand_spd(K)
om = 0.7 * rng.standard_normal((K, K))
E, Em = expm(om), expm(-om)
Sji = np.linalg.inv(Sj)
lhs = kl_gauss(mi, Si, E @ mj, E @ Sj @ E.T)
rhs = (0.5 * np.trace(Sji @ Em @ Si @ Em.T) + 0.5 * (Em @ mi - mj) @ Sji @ (Em @ mi - mj)
       - K / 2 + 0.5 * np.log(np.linalg.det(Sj) / np.linalg.det(Si)) + np.trace(om))
print("law-level energy |lhs-rhs| =", abs(lhs - rhs))


def f_law(o):
    Eo = expm(o)
    return kl_gauss(mi, Si, Eo @ mj, Eo @ Sj @ Eo.T)


A = Sji @ (Em @ (Si + np.outer(mi, mi)) - np.outer(mj, mi))
grad = np.eye(K) - L(-om.T, A)
print("law-level gradient max|grad-fd| =", np.abs(grad - fd_grad(f_law, om)).max())

mu, S = rng.standard_normal(K), rand_spd(K)
ups = rng.standard_normal((K, K))
Sinv = np.linalg.inv(S)
kq = (ups @ mu) @ Sinv @ (ups @ mu) + np.trace(ups @ ups) + np.trace(Sinv @ ups @ S @ ups.T)
for t in [1e-2, 1e-3]:
    Et = expm(t * ups)
    val = kl_gauss(mu, S, Et @ mu, Et @ S @ Et.T)
    print("orbit expansion t =", t, " val/(t^2 kq/2) =", val / (t * t / 2 * kq))

# (2) prop:glink-sample-record
W = rand_spd(K)
o = rng.standard_normal(K)
cst = 0.5 * np.log(np.linalg.det(2 * np.pi * np.linalg.inv(W)))


def Eexp(M):
    r = mi - o - M @ mj
    return 0.5 * r @ W @ r + 0.5 * np.trace(W @ Si) + 0.5 * np.trace(W @ M @ Sj @ M.T) + cst


n = 200000
zi = mi + rng.standard_normal((n, K)) @ np.linalg.cholesky(Si).T
zj = mj + rng.standard_normal((n, K)) @ np.linalg.cholesky(Sj).T
M = rng.standard_normal((K, K))
res = o - zi + zj @ M.T
mc = np.mean(0.5 * np.einsum('na,ab,nb->n', res, W, res)) + cst
print("record energy MC =", mc, " closed form =", Eexp(M))
J = W @ (np.outer(mi - o - M @ mj, mj) - M @ Sj)
print("current: max|(-J)-fd| =", np.abs(-J - fd_grad(Eexp, M)).max())
Sm = Sj + np.outer(mj, mj)
Mstar = np.outer(mi - o, mj) @ np.linalg.inv(Sm)
print("rank Mstar =", np.linalg.matrix_rank(Mstar), " trace =", np.trace(Mstar),
      " Sherman-Morrison form =", mj @ Sji @ (mi - o) / (1 + mj @ Sji @ mj))
print("Mstar is minimizer: |J(Mstar)| =", np.abs(W @ (np.outer(mi - o - Mstar @ mj, mj) - Mstar @ Sj)).max())
om = 0.5 * rng.standard_normal((K, K))
Eo = expm(om)
Jg = W @ (np.outer(mi - o - Eo @ mj, mj) - Eo @ Sj)
g = -L(om.T, Jg)
print("generator gradient max|g-fd| =", np.abs(g - fd_grad(lambda X: Eexp(expm(X)), om)).max())

Jm = np.array([[0., -1.], [1., 0.]])
D = np.diag([1., -1.])
for vs, a in [(0.7, 0.3), (1.5, -0.4)]:
    om0 = a * np.eye(2) + np.pi * Jm
    Sj2 = vs ** 2 * np.eye(2)
    mj2 = np.array([1., 0.])
    d2 = -(1 + 2 * vs ** 2) * np.exp(a) * np.array([1., 0.])

    def F(X):
        Mx = expm(X)
        r = d2 - Mx @ mj2
        return 0.5 * r @ r + 0.5 * np.trace(Mx @ Sj2 @ Mx.T)

    print("saddle (vs,a)=", (vs, a), " max|grad| =", np.abs(fd_grad(F, om0)).max(),
          " |exp(om0)+e^a I| =", np.abs(expm(om0) + np.exp(a) * np.eye(2)).max())
    for t in [0.1, -0.1, 0.05, -0.05]:
        print("   t =", t, " dF =", F(om0 + t * D) - F(om0), " predicted t^3 term =", vs ** 2 * np.exp(2 * a) * t ** 3 / np.pi ** 2)

# (3) prop:glink-expected-loop
s2 = 0.2
print("K=1 repeated pair: E e^w E e^-w = exp(s2) =", np.exp(s2))
K2, eps, n = 2, 0.05, 400000
Z1 = eps * rng.standard_normal((n, K2, K2))
Z2 = eps * rng.standard_normal((n, K2, K2))


def expm_batch(Am):
    out = np.tile(np.eye(K2), (len(Am), 1, 1))
    term = out.copy()
    for k in range(1, 30):
        term = term @ Am / k
        out = out + term
    return out


T = expm_batch(Z1) @ expm_batch(Z2)
Dm = T - np.eye(K2)
Q = 0.5 * np.einsum('nab,nab->n', Dm, Dm)
print("flat means MC E Q =", Q.mean(), " predicted (1/2) sum Tr Lambda^-1 =", 0.5 * 2 * K2 * K2 * eps ** 2,
      " MC std err =", Q.std() / np.sqrt(n))

# (4) prop:glink-linear-spectrum
N, n1, Kd = 4, 3, 2
a_, b_, c_, m_ = 0.9, 0.4, 0.7, 1.3


def Qp(oms):
    Tm = np.eye(Kd)
    for o_ in oms:
        Tm = Tm @ expm(o_)
    Dq = Tm - np.eye(Kd)
    return 0.5 * np.trace(Dq.T @ Dq)


def Sh(x):
    x = x.reshape(n1 + 1, N, Kd, Kd)
    val = 0.
    for nn in range(n1 + 1):
        val += 0.5 * (a_ + b_) * np.sum(x[nn] ** 2) + c_ * Qp([x[nn, i] for i in range(N)])
    for nn in range(1, n1 + 1):
        val += 0.5 * m_ * np.sum((x[nn] - x[nn - 1]) ** 2)
    return val


dim = (n1 + 1) * N * Kd * Kd
H = np.zeros((dim, dim))
x0 = np.zeros(dim)
hh = 1e-4
for p in range(dim):
    for q in range(p, dim):
        ep = np.zeros(dim); ep[p] = hh
        eq = np.zeros(dim); eq[q] = hh
        H[p, q] = H[q, p] = (Sh(x0 + ep + eq) - Sh(x0 + ep - eq) - Sh(x0 - ep + eq) + Sh(x0 - ep - eq)) / (4 * hh * hh)
Lp = np.diag([1.] + [2.] * (n1 - 1) + [1.]) - np.diag(np.ones(n1), 1) - np.diag(np.ones(n1), -1)
Kop = np.kron(np.kron(np.eye(n1 + 1), (a_ + b_) * np.eye(N) + c_ * np.ones((N, N))) + np.kron(m_ * Lp, np.eye(N)), np.eye(Kd * Kd))
print("ring: max|Hess(S_hist)(0) - K| =", np.abs(H - Kop).max())
ev = np.sort(np.linalg.eigvalsh(Kop))
s = [4 * m_ * np.sin(np.pi * l / (2 * (n1 + 1))) ** 2 for l in range(n1 + 1)]
pred = sorted([a_ + b_ + c_ * N + v for v in s] * (Kd * Kd) + [a_ + b_ + v for v in s] * ((N - 1) * Kd * Kd))
print("ring: max|eig - predicted| =", np.abs(ev - np.array(pred)).max(), " min eig =", ev[0], " a+b =", a_ + b_)
q_ = a_ + b_
r1 = 1 + q_ / (2 * m_) + np.sqrt((1 + q_ / (2 * m_)) ** 2 - 1)
print("ring recursion roots product =", r1 * (1 / r1), " root1 =", r1, " check char. poly:", r1 ** 2 - (2 + q_ / m_) * r1 + 1)
