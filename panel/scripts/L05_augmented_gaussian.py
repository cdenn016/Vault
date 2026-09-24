"""L05: Gaussian instance of the augmented joint (PIFB2 App. G, Def. def:augmented_joint).

Tree: one parent k_P in R^K (top prior N(0, Lam_top^{-1})), two children k_i | k_P ~ N(Om_i k_P, s2 I),
observations o_i | k_i ~ N(k_i, R).  K = 2, float64.
Checks:
 (a) stacked precision blocks equal the text's statement (vs a finite-difference Hessian);
 (b) link-only precision is PSD with a K-dim kernel {k_i = Om_i k_P};
 (c) mean-field Gauss-Seidel sweeps converge to J^{-1} h;
 (d) exact child posterior vs PIFB2 shadow scheme (child = shadow of the exact parent posterior x own likelihood);
 (e) BP/EP cavity version reproduces the exact child posterior;
 (f) rigid-link limit s2 -> 0;
 (g) scalar case: min over Gaussians of the same-time shadow functional vs -log p_s2(o)  (bound test);
 (h) the M-step (empirical-Bayes) reading: min over (q, theta) of sum_i KL(q_i||p_theta,i) - E log lik = -max_theta log p_theta^{RE}(o).
"""
import numpy as np
from scipy.optimize import minimize
rng = np.random.default_rng(5)
K = 2

def rot(a):
    return np.array([[np.cos(a), -np.sin(a)], [np.sin(a), np.cos(a)]])

Om = [rot(0.7) @ np.diag([1.3, 0.8]), rot(-1.1) @ np.diag([0.9, 1.2])]   # GL+(2) transports
Lam_top = np.array([[1.5, 0.3], [0.3, 0.9]])
R = np.diag([0.4, 0.6]); Ri = np.linalg.inv(R)
o = [np.array([1.0, -0.5]), np.array([-0.8, 0.9])]

def build(s2):
    n = 3 * K
    J = np.zeros((n, n)); h = np.zeros(n)
    P = slice(0, K); C = [slice(K, 2*K), slice(2*K, 3*K)]
    J[P, P] = Lam_top + sum(Om[i].T @ Om[i] for i in range(2)) / s2
    for i in range(2):
        J[C[i], C[i]] = np.eye(K) / s2 + Ri
        J[C[i], P] = -Om[i] / s2; J[P, C[i]] = -Om[i].T / s2
        h[C[i]] = Ri @ o[i]
    return J, h, P, C

def neglog(y, s2):
    kP, k1, k2 = y[:K], y[K:2*K], y[2*K:]
    v = 0.5 * kP @ Lam_top @ kP
    for kk, i in ((k1, 0), (k2, 1)):
        d = kk - Om[i] @ kP; v += 0.5 * d @ d / s2
        e = o[i] - kk; v += 0.5 * e @ Ri @ e
    return v

s2 = 0.3
J, h, P, C = build(s2)
# (a) finite-difference Hessian
y0 = rng.normal(size=3*K); eps = 1e-4; H = np.zeros((6, 6))
for a in range(6):
    for b in range(6):
        ea = np.eye(6)[a]*eps; eb = np.eye(6)[b]*eps
        H[a, b] = (neglog(y0+ea+eb, s2) - neglog(y0+ea-eb, s2) - neglog(y0-ea+eb, s2) + neglog(y0-ea-eb, s2)) / (4*eps*eps)
print('(a) max |J_text - Hessian_fd| =', np.abs(J - H).max())
# (b) link-only precision
Jl = J.copy(); Jl[P, P] -= Lam_top
for i in range(2): Jl[C[i], C[i]] -= Ri
ev = np.linalg.eigvalsh(Jl)
print('(b) link-only eigenvalues:', np.round(ev, 12), ' kernel dim =', int(np.sum(np.abs(ev) < 1e-10)))
kP = rng.normal(size=K); v = np.concatenate([kP, Om[0] @ kP, Om[1] @ kP])
print('    |Jl v| on consistent-propagation vector =', np.linalg.norm(Jl @ v), '; min eig full J =', np.linalg.eigvalsh(J).min())
# (c) MF Gauss-Seidel
mu = np.zeros(6); blocks = [P] + C
for sweep in range(400):
    for B in blocks:
        rest = h[B] - J[B, :] @ mu + J[B, B] @ mu[B]
        mu[B] = np.linalg.solve(J[B, B], rest)
mexact = np.linalg.solve(J, h)
print('(c) MF Gauss-Seidel mean residual vs J^{-1}h =', np.abs(mu - mexact).max())

def child_compare(s2, label):
    J, h, P, C = build(s2)
    Cov = np.linalg.inv(J); m = Cov @ h
    muP, SP = m[P], Cov[P, P]
    m1, S1 = m[C[0]], Cov[C[0], C[0]]
    # PIFB2 shadow scheme with the exact parent posterior
    Sp = Om[0] @ SP @ Om[0].T + s2*np.eye(K)
    Lp = np.linalg.inv(Sp) + Ri
    Sq = np.linalg.inv(Lp); mq = Sq @ (np.linalg.solve(Sp, Om[0] @ muP) + Ri @ o[0])
    # cavity: remove child-1 message from the parent (tree BP): parent posterior from prior + child 2 only
    Jc = Lam_top.copy(); hc = np.zeros(K)
    # child-2 message to parent: integrate out k_2 from N(k2;Om2 kP,s2) N(o2;k2,R) -> N(o2; Om2 kP, s2 I + R)
    M2 = np.linalg.inv(s2*np.eye(K) + R)
    Jc += Om[1].T @ M2 @ Om[1]; hc += Om[1].T @ M2 @ o[1]
    Scav = np.linalg.inv(Jc); mcav = Scav @ hc
    Spc = Om[0] @ Scav @ Om[0].T + s2*np.eye(K)
    Sb = np.linalg.inv(np.linalg.inv(Spc) + Ri); mb = Sb @ (np.linalg.solve(Spc, Om[0] @ mcav) + Ri @ o[0])
    print(f'{label} s2={s2:g}: exact child-1 mean {np.round(m1,5)}, PIFB2-shadow mean {np.round(mq,5)}, cavity mean {np.round(mb,5)}')
    print(f'      |mean err| shadow={np.abs(mq-m1).max():.3e}  cavity={np.abs(mb-m1).max():.3e};'
          f'  |cov err| shadow={np.abs(Sq-S1).max():.3e}  cavity={np.abs(Sb-S1).max():.3e}')
    # precision excess of shadow scheme
    print('      shadow precision - exact precision =\n', np.round(np.linalg.inv(Sq) - np.linalg.inv(S1), 6), '\n      R^{-1} =\n', np.round(Ri, 6))

child_compare(0.3, '(d,e)')
child_compare(1e-8, '(f) rigid')

# (g) scalar bound test.  parent N(0,1/lt); children k_i|k_P ~ N(k_P, s2); o_i|k_i ~ N(k_i, r)
lt, s2s, r = 1.0, 0.05, 0.2
def neglog_evidence(os_):
    # marginal of o: o = kP 1 + (k - kP 1) + noise -> cov = 1/lt 11^T + (s2+r) I
    n = len(os_); Cv = np.ones((n, n))/lt + (s2s + r)*np.eye(n)
    return 0.5*(os_ @ np.linalg.solve(Cv, os_) + np.linalg.slogdet(2*np.pi*Cv)[1])
def KL(m1, v1, m2, v2):
    return 0.5*(v1/v2 + (m1-m2)**2/v2 - 1 + np.log(v2/v1))
def Fshadow(x, os_, lam=1.0):
    muP, lvP = x[0], x[1]; vP = np.exp(lvP)
    val = lam*KL(muP, vP, 0.0, 1/lt)
    for i, oi in enumerate(os_):
        mi, vi = x[2+2*i], np.exp(x[3+2*i])
        val += KL(mi, vi, muP, vP + s2s) + 0.5*((oi-mi)**2 + vi)/r + 0.5*np.log(2*np.pi*r)
    return val
for os_ in (np.array([2.0, -2.0]), np.array([1.0, 1.0]), np.array([3.0, -3.0, 0.5])):
    best = min((minimize(Fshadow, rng.normal(size=2+2*len(os_)), args=(os_,), method='BFGS', options={'gtol':1e-10}) for _ in range(8)), key=lambda z: z.fun)
    print(f'(g) o={os_}: min F_shadow = {best.fun:.6f}   -log p_s2(o) = {neglog_evidence(os_):.6f}   difference = {best.fun-neglog_evidence(os_):+.6f}')

# (h) empirical-Bayes / random-effects reading (no lambda term; parent = hyperparameter theta=(m,S))
def Feb(x, os_):
    m, vS = x[0], np.exp(x[1]); val = 0.0
    for i, oi in enumerate(os_):
        mi, vi = x[2+2*i], np.exp(x[3+2*i])
        val += KL(mi, vi, m, vS) + 0.5*((oi-mi)**2 + vi)/r + 0.5*np.log(2*np.pi*r)
    return val
def neg_ml2(x, os_):
    m, vS = x[0], np.exp(x[1])
    return sum(0.5*((oi-m)**2/(vS+r) + np.log(2*np.pi*(vS+r))) for oi in os_)
os_ = np.array([2.0, -1.0, 0.5])
a = min((minimize(Feb, rng.normal(size=2+2*len(os_)), args=(os_,), method='BFGS', options={'gtol':1e-11}) for _ in range(8)), key=lambda z: z.fun)
b = min((minimize(neg_ml2, rng.normal(size=2), args=(os_,), method='BFGS', options={'gtol':1e-11}) for _ in range(8)), key=lambda z: z.fun)
print(f'(h) min F_EB = {a.fun:.8f}   -max_theta log p_theta^RE(o) = {b.fun:.8f}   residual = {a.fun-b.fun:.2e}')
# M-step coordinate = barycenter with dispersion: at optimum theta equals weighted moments of q_i
ms = a.x[2::2]; vs = np.exp(a.x[3::2])
print('    theta* =', a.x[0], np.exp(a.x[1]), '  barycenter(q_i) mean, var(with dispersion) =', ms.mean(), vs.mean() + ((ms-ms.mean())**2).mean())
