r"""L10: Appendix D (2662-2891) frozen-attention covariance fixed point, Hessian, A-coupling;
Appendix E (2892-2955) quadratic-form/KL identity; Appendix C BCH truncation (2651) and SO(3) generators (2641).

T(Sigma)_i = 2 (A_i + sum_j beta_ij (Omega_ij Sigma_j Omega_ij^T)^{-1})^{-1},  A_i = Sigma_p,i^{-1} + Lambda_o,i.
"""
import numpy as np
from scipy.linalg import expm, sqrtm
rng = np.random.default_rng(5)
def spd(K, c=0.5):
    A = rng.standard_normal((K, K)); return A @ A.T + c * np.eye(K)

def T(Sig, Om, beta, A):
    N = len(Sig); out = []
    for i in range(N):
        B = sum(beta[i][j] * np.linalg.inv(Om[i][j] @ Sig[j] @ Om[i][j].T) for j in range(N) if j != i)
        out.append(2 * np.linalg.inv(A[i] + B))
    return out
def thompson(X, Y):
    d = 0.0
    for x, y in zip(X, Y):
        ev = np.linalg.eigvals(np.linalg.solve(x, y)).real; d = max(d, abs(np.log(ev.max())), abs(np.log(ev.min())))
    return d
def iterate(Om, beta, A, Sp, n=400):
    Sig = [2 * s for s in Sp]; hist = [Sig]
    for _ in range(n): Sig = T(Sig, Om, beta, A); hist.append(Sig)
    return Sig, hist
def lam_C(Om, beta):
    N = len(Om); return [np.linalg.eigvalsh(sum(beta[i][j] * np.linalg.inv(Om[i][j] @ Om[i][j].T) for j in range(N) if j != i)).max() for i in range(N)]

N, K = 3, 3
beta = rng.dirichlet(np.ones(N - 1), size=N); beta = [[0 if j == i else beta[i][j - (j > i)] for j in range(N)] for i in range(N)]
Sp = [spd(K) for _ in range(N)]; Lo = [0.3 * spd(K, 0.1) for _ in range(N)]; A = [np.linalg.inv(Sp[i]) + Lo[i] for i in range(N)]

print("(1) flat GL+(3) links Omega_ij = U_i U_j^{-1}, |phi_i|_F = 1.5 (Regime I, zero holonomy)")
U = [expm(1.5 * (lambda P: P / np.linalg.norm(P))(rng.standard_normal((K, K)))) for _ in range(N)]
Om = [[U[i] @ np.linalg.inv(U[j]) for j in range(N)] for i in range(N)]
print("   lambda_max(C_i) in the given gauge:", np.round(lam_C(Om, beta), 3), " (proposition hypothesis requires < 2)")
Sig, hist = iterate(Om, beta, A, Sp)
res = max(np.linalg.norm(np.linalg.inv(Sig[i]) - 0.5 * (A[i] + sum(beta[i][j] * np.linalg.inv(Om[i][j] @ Sig[j] @ Om[i][j].T) for j in range(N) if j != i))) for i in range(N))
print(f"   iteration from 2 Sigma_p: fixed-point residual of eq:sigma_fixed_point_beta after 400 steps = {res:.2e}; min eig = {min(np.linalg.eigvalsh(s).min() for s in Sig):.3e}")
d = [thompson(h, Sig) for h in hist[:40]]; rates = [d[k + 1] / d[k] for k in range(5, 30) if d[k] > 1e-13]
print(f"   empirical Thompson contraction ratio ~ {np.median(rates):.3f}")
g = [np.linalg.inv(u) for u in U]  # gauge in which all links are identity
Om2 = [[g[i] @ Om[i][j] @ np.linalg.inv(g[j]) for j in range(N)] for i in range(N)]
A2 = [np.linalg.inv(g[i] @ Sp[i] @ g[i].T) + np.linalg.inv(g[i]).T @ Lo[i] @ np.linalg.inv(g[i]) for i in range(N)]
Sp2 = [g[i] @ Sp[i] @ g[i].T for i in range(N)]
print("   lambda_max(C_i) after gauge g_i = U_i^{-1}:", np.round(lam_C(Om2, beta), 3))
Sig2, _ = iterate(Om2, beta, A2, Sp2)
print(f"   covariance of the fixed point under gauge: max rel |g Sig* g^T - Sig*'| = {max(np.linalg.norm(g[i] @ Sig[i] @ g[i].T - Sig2[i]) / np.linalg.norm(Sig2[i]) for i in range(N)):.2e}")

print("\n(2) K=1, N=2, beta=1, links w=Omega_12, v=Omega_21 (holonomy h = w v), a = prior precision = 1")
for w, v in ((0.1, 10.0), (0.6, 0.6), (0.5, 1.0), (0.45, 1.0), (0.3, 1.0)):
    x1, x2 = 2.0, 2.0  # start at 2 Sigma_p, scalar form of T with a = 1
    traj = []
    for n in range(1, 2001):
        x1, x2 = (2 / (1 + 1 / (w * w * x2)), 2 / (1 + 1 / (v * v * x1))) if min(x1, x2) > 1e-280 else (0.0, 0.0)
        if n in (10, 100, 2000): traj.append((x1, x2))
    print(f"   w={w:4.2f} v={v:5.2f} h={w*v:5.2f}: lambda_max(C)=({1/w**2:7.2f},{1/v**2:5.2f}); Sigma after 10/100/2000 steps: " + ", ".join(f"({a:.2e},{b:.2e})" for a, b in traj) + f"; slope of T1oT2 at 0 = 4h^2 = {4*(w*v)**2:.2f}")
print("\n(3) own-block Hessian d2F/dSigma2[X] = Sigma^-1 X Sigma^-1 (2862) and A-coupled stationarity (2820), FD")
def Fi(Si, i, Sig, Om, Acoup=1.0):
    K = Si.shape[0]; val = 0.5 * (np.trace(np.linalg.inv(Sp[i]) @ Si) - np.linalg.slogdet(Si)[1]) + 0.5 * np.trace(Lo[i] @ Si)
    for j in range(N):
        if j != i:
            Aij = Om[i][j] @ Sig[j] @ Om[i][j].T
            val += Acoup * beta[i][j] * 0.5 * (np.trace(np.linalg.inv(Aij) @ Si) - np.linalg.slogdet(Si)[1])
    return val
Si = spd(K); X = rng.standard_normal((K, K)); X = X + X.T; Y = rng.standard_normal((K, K)); Y = Y + Y.T; h = 1e-4
num = (Fi(Si + h*X + h*Y, 0, Sig, Om) - Fi(Si + h*X - h*Y, 0, Sig, Om) - Fi(Si - h*X + h*Y, 0, Sig, Om) + Fi(Si - h*X - h*Y, 0, Sig, Om)) / (4*h*h)
ana = np.trace(np.linalg.inv(Si) @ X @ np.linalg.inv(Si) @ Y)
print(f"   Hessian bilinear form rel err = {abs(num-ana)/abs(ana):.2e}")
for Ac in (1.0, 7.0):
    Bi = sum(beta[0][j] * np.linalg.inv(Om[0][j] @ Sig[j] @ Om[0][j].T) for j in range(N) if j != 0)
    Sst = (1 + Ac) * np.linalg.inv(np.linalg.inv(Sp[0]) + Ac * Bi + Lo[0])
    gr = np.array([[(Fi(Sst + h*E, 0, Sig, Om, Ac) - Fi(Sst - h*E, 0, Sig, Om, Ac)) / (2*h) for E in [np.outer(np.eye(K)[a], np.eye(K)[b]) + np.outer(np.eye(K)[b], np.eye(K)[a]) for b in range(K)]] for a in range(K)])
    print(f"   A={Ac}: |grad F_i^(A)| at (1+A) Sigma^-1 = Sigma_p^-1 + A B + Lambda_o solution = {np.abs(gr).max():.2e}")

print("\n(4) Appendix E identity: (1/4) E[delta^T Lambda_ij delta] - (tau/2) KL(q_i||Om q_j) = tau K/2 + (tau/4) logdet(A^-1 Sigma_i)")
mx = 0
for _ in range(20):
    K = 3; Si, Sj = spd(K), spd(K); mi, mj = rng.standard_normal(K), rng.standard_normal(K); O = expm(rng.standard_normal((K, K))); tau = 1.7
    Aj = O @ Sj @ O.T; Lam = tau * np.linalg.inv(Aj); db = mi - O @ mj
    quad = np.trace(Lam @ (Si + Aj)) + db @ Lam @ db
    kl = 0.5 * (np.trace(np.linalg.inv(Aj) @ Si) + db @ np.linalg.inv(Aj) @ db - K + np.linalg.slogdet(Aj)[1] - np.linalg.slogdet(Si)[1])
    lhs = quad / 4 - tau / 2 * kl; rhs = tau * K / 2 + tau / 4 * np.linalg.slogdet(np.linalg.solve(Aj, Si))[1]
    mx = max(mx, abs(lhs - rhs) / abs(rhs))
# Monte Carlo sanity of eq:quadratic_expectation_formula
ki = rng.multivariate_normal(mi, Si, 400000); kj = rng.multivariate_normal(mj, Sj, 400000); dl = ki - kj @ O.T
mc = np.mean(np.einsum("ni,ij,nj->n", dl, Lam, dl))
print(f"   exact identity max rel err = {mx:.2e};  MC check of eq:quadratic_expectation_formula: rel diff {abs(mc-quad)/quad:.2e} (4e5 samples)")

print("\n(5) BCH truncation (2651): |log(e^{phi_i} e^{-phi_j}) - (phi_i - phi_j - 1/2[phi_i,phi_j])| vs scale eps (so(3))")
from scipy.linalg import logm
Pi, Pj = [(lambda M: M - M.T)(rng.standard_normal((3, 3))) for _ in range(2)]
prev = None
for eps in (0.2, 0.1, 0.05, 0.025):
    a, b = eps * Pi, eps * Pj
    L = np.real(logm(expm(a) @ expm(-b))); r = np.linalg.norm(L - (a - b - 0.5 * (a @ b - b @ a)))
    print(f"   eps={eps:.3f}: residual {r:.3e}" + (f", ratio {prev/r:.2f} (8 => O(eps^3))" if prev else "")); prev = r
Gx = np.array([[0,0,0],[0,0,-1],[0,1,0.]]); Gy = np.array([[0,0,1],[0,0,0],[-1,0,0.]]); Gz = np.array([[0,-1,0],[1,0,0],[0,0,0.]])
c = lambda X, Y: X @ Y - Y @ X
print(f"\n(6) spin-1 real generators: |[Gx,Gy]-Gz|={np.linalg.norm(c(Gx,Gy)-Gz):.0e}, |[Gy,Gz]-Gx|={np.linalg.norm(c(Gy,Gz)-Gx):.0e}, |[Gz,Gx]-Gy|={np.linalg.norm(c(Gz,Gx)-Gy):.0e}")
