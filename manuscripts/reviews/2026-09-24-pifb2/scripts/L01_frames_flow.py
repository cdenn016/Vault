"""L01: additive Lie-algebra frame average (non)equivariance; Frobenius-body frame flow equivariance under left vs right
translation; directional KL derivative eq:kl_omega_directional; first-order BCH transport truncation holonomy. PIFB2.tex 1573-1575, 1644, 965-1004, 2363-2395, 2649."""
import numpy as np
from scipy.linalg import expm, logm
rng = np.random.default_rng(3)
inv = np.linalg.inv
K = 3
rl = lambda A: np.real(logm(A))
# (F1) additive average phi_I = mean(phi_i) under diagonal left translation U_i -> g U_i
base = 0.3 * rng.standard_normal((K, K)); dirs = [rng.standard_normal((K, K)) for _ in range(3)]
G0 = rng.standard_normal((K, K)); G0 = G0 - G0.T  # compact direction, so logs stay principal
print("(F1) deviation |exp(mean log(g U_i)) - g exp(mean phi_i)| ; rows: spread eps, cols: |log g| in {0.1,0.5,1.0}")
for eps in (1e-1, 1e-2, 1e-3):
    phis = [base + eps * dd for dd in dirs]
    row = []
    for s in (0.1, 0.5, 1.0):
        g = expm(s * G0 / np.linalg.norm(G0))
        lhs = expm(np.mean([rl(g @ expm(p)) for p in phis], axis=0)); rhs = g @ expm(np.mean(phis, axis=0))
        row.append(np.abs(lhs - rhs).max())
    print("   eps=%.0e :" % eps, ["%.2e" % r for r in row])
phis = [0.02 * rng.standard_normal((K, K)) for _ in range(3)]
g = expm(1.0 * G0 / np.linalg.norm(G0))
print("   small frames (|phi|~0.02) but |log g|=1: deviation %.2e" % np.abs(expm(np.mean([rl(g @ expm(p)) for p in phis], axis=0)) - g @ expm(np.mean(phis, axis=0))).max())
# (F2) Frobenius-body flow equivariance
def kl(m1, S1, m2, S2):
    k = len(m1); S2i = inv(S2); dm = m2 - m1
    return 0.5 * (np.log(np.linalg.det(S2) / np.linalg.det(S1)) + np.trace(S2i @ S1) + dm @ S2i @ dm - k)
def spd():
    X = rng.standard_normal((K, K)); return X @ X.T + K * np.eye(K)
N = 3
mu = [rng.standard_normal(K) for _ in range(N)]; Sg = [spd() for _ in range(N)]
def Fval(U, mu=mu, Sg=Sg):
    t = 0.0
    for i in range(N):
        for j in range(N):
            if i != j:
                O = U[i] @ inv(U[j]); t += kl(mu[i], Sg[i], O @ mu[j], O @ Sg[j] @ O.T)
    return t
def gradU(U, mu=mu, Sg=Sg, e=1e-6):
    out = []
    for i in range(N):
        Gi = np.zeros((K, K))
        for a in range(K):
            for b in range(K):
                Up = [u.copy() for u in U]; Um = [u.copy() for u in U]
                Up[i][a, b] += e; Um[i][a, b] -= e
                Gi[a, b] = (Fval(Up, mu, Sg) - Fval(Um, mu, Sg)) / (2 * e)
        out.append(Gi)
    return out
def step(U, eta=1e-2, mu=mu, Sg=Sg):
    Gs = gradU(U, mu, Sg); return [U[i] @ expm(-eta * U[i].T @ Gs[i]) for i in range(N)]
U = [expm(0.4 * rng.standard_normal((K, K))) for _ in range(N)]
gR = expm(0.6 * rng.standard_normal((K, K)))  # non-orthogonal
Q, _ = np.linalg.qr(rng.standard_normal((K, K)))
def Oms(U): return np.array([U[0] @ inv(U[1]), U[1] @ inv(U[2])])
U1 = step(U); U1R = step([u @ gR for u in U]); U1Q = step([u @ Q for u in U])
print("(F2) F invariant under right translation: |F(Ug)-F(U)| = %.2e" % abs(Fval([u @ gR for u in U]) - Fval(U)))
print("     after one Frobenius-body step, |Omega(U g) - Omega(U)|: g non-orthogonal %.2e ; g orthogonal %.2e ; step size |Omega(U1)-Omega(U)| %.2e"
      % (np.abs(Oms(U1R) - Oms(U1)).max(), np.abs(Oms(U1Q) - Oms(U1)).max(), np.abs(Oms(U1) - Oms(U)).max()))
gL = [expm(0.6 * rng.standard_normal((K, K))) for _ in range(N)]
muL = [gL[i] @ mu[i] for i in range(N)]; SgL = [gL[i] @ Sg[i] @ gL[i].T for i in range(N)]
UL = [gL[i] @ U[i] for i in range(N)]
U1L = step(UL, mu=muL, Sg=SgL)
print("     per-agent left action (q co-transformed): |U1(gU) - g U1(U)| = %.2e" % max(np.abs(U1L[i] - gL[i] @ U1[i]).max() for i in range(N)))
# (F3) directional derivative formula
i, j = 0, 1
O = U[i] @ inv(U[j]); A = O @ Sg[j] @ O.T; Lam = inv(A); r = mu[i] - O @ mu[j]
X = rng.standard_normal((K, K)); e = 1e-6
f = lambda Om: kl(mu[i], Sg[i], Om @ mu[j], Om @ Sg[j] @ Om.T)
fd = (f(expm(e * X) @ O) - f(expm(-e * X) @ O)) / (2 * e)
Nij = np.eye(K) - Lam @ Sg[i] - Lam @ np.outer(r, O @ mu[j]) - Lam @ np.outer(r, r)
print("(F3) eq:kl_omega_directional: FD %.10f vs formula %.10f" % (fd, np.trace(X.T @ Nij)))
D = Nij @ inv(O).T; D2 = inv(O).T - Lam @ Sg[i] @ inv(O).T - Lam @ np.outer(r, mu[j]) - Lam @ np.outer(r, r) @ Lam @ O @ Sg[j]
Xd = rng.standard_normal((K, K)); fd2 = (f(O + e * Xd) - f(O - e * Xd)) / (2 * e)
print("     eq:kl_omega_unconstrained: |N O^-T - expanded| = %.2e ; FD vs tr(Xd^T D): %.2e" % (np.abs(D - D2).max(), abs(fd2 - np.trace(Xd.T @ D))))
phi0 = 0.5 * rng.standard_normal((K, K)); Ga = rng.standard_normal((K, K)); s = np.linspace(0, 1, 2001)
integ = np.trapezoid([expm((1 - t) * phi0) @ Ga @ expm(t * phi0) for t in s], s, axis=0)
fdexp = (expm(phi0 + e * Ga) - expm(phi0 - e * Ga)) / (2 * e)
print("(F4) eq:frechet_dexp integral vs FD: %.2e" % np.abs(integ - fdexp).max())
# (F5) first-order BCH truncation of transport breaks the cocycle
for sc in (0.3, 0.1, 0.03):
    ph = [sc * rng.standard_normal((K, K)) for _ in range(3)]
    Ot = lambda a, b: expm(ph[a] - ph[b])
    Hh = Ot(0, 1) @ Ot(1, 2) @ Ot(2, 0)
    comm = max(np.abs(ph[a] @ ph[b] - ph[b] @ ph[a]).max() for a in range(3) for b in range(3))
    print("(F5) scale %.2f: truncated-transport triangle holonomy |H - I| = %.2e ; max |[phi_a,phi_b]| = %.2e" % (sc, np.abs(Hh - np.eye(K)).max(), comm))
print("(F1b) fixed spread eps=0.05, |log g|=0.5; vary base-frame magnitude |phi_bar|:")
dirs2 = [rng.standard_normal((K, K)) for _ in range(3)]; B0 = rng.standard_normal((K, K)); B0 = B0 - B0.T; B0 /= np.linalg.norm(B0)
g = expm(0.5 * G0 / np.linalg.norm(G0))
for bm in (0.0, 0.3, 1.0):
    phis = [bm * B0 + 0.05 * dd for dd in dirs2]
    dev = np.abs(expm(np.mean([rl(g @ expm(p)) for p in phis], axis=0)) - g @ expm(np.mean(phis, axis=0))).max()
    print("   |phi_bar|=%.1f : deviation %.2e" % (bm, dev))
