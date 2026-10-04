"""Numerical probes for verify_V4b.md (float64, CPU). They test closed forms only; no verdict rests on them.

Checks:
  A. prop:glink-induced-action (iv): det factorization with W_sharp, first/second t-derivatives, skew constancy.
  B. prop:glink-induced-action (v): cycle determinant eq:glink-cycle-determinant (m=3, K=2) and the K=1 witness.
  C. prop:glink-hopping (i),(ii),(v): spectral radius bound, log-det series, triangle coefficient and remainder bound.
  D. Concern (1): triangle with SO(3) links, det Lambda = alpha*(alpha+beta*Q_p)^2.
  E. Concern (2): K=1 theta graph, det Lambda >= C|s|^2 near the flat set (lower bound via Cauchy-Binet fundamental-cycle terms).
  F. Concern (3): K=3 chart link similar to diag(c',c',lambda), two-sided perturbations with non-real compressed spectrum stay chart links.
"""
import numpy as np
from scipy.linalg import expm, logm

rng = np.random.default_rng(20261004)
out = []
def log(s):
    print(s); out.append(s)

def build_Lambda(N, K, edges, W, A, links):
    """edges: list of (i, j) for copy e: j -> i; links[e] = K x K matrix acting on z_j."""
    Lam = np.zeros((N * K, N * K))
    for i in range(N):
        Lam[i*K:(i+1)*K, i*K:(i+1)*K] += A[i]
    for e, (i, j) in enumerate(edges):
        D = np.zeros((K, N * K))
        D[:, i*K:(i+1)*K] += np.eye(K)
        D[:, j*K:(j+1)*K] -= links[e]
        Lam += D.T @ W[e] @ D
    return Lam

# ---------- A ----------
K = 3
ai, aj, we = 0.7, 1.3, 0.9
ups = rng.standard_normal((K, K)); ups = 0.5 * (ups + ups.T)
wsharp = ai * we / (ai + we)
def Sind_two(t, ups_):
    links = [expm(t * ups_)]
    Lam = build_Lambda(2, K, [(0, 1)], [we * np.eye(K)], [ai * np.eye(K), aj * np.eye(K)], links)
    return 0.5 * np.log(np.linalg.det(Lam))
# det factorization with W_sharp (general matrices)
Ai = rng.standard_normal((K, K)); Ai = Ai @ Ai.T + 0.3 * np.eye(K)
Aj = rng.standard_normal((K, K)); Aj = Aj @ Aj.T + 0.3 * np.eye(K)
We = rng.standard_normal((K, K)); We = We @ We.T + 0.3 * np.eye(K)
om = 0.4 * rng.standard_normal((K, K)); Th = expm(om)
Lam = build_Lambda(2, K, [(0, 1)], [We], [Ai, Aj], [Th])
Wsh = np.linalg.inv(np.linalg.inv(We) + np.linalg.inv(Ai))
rhs = np.linalg.det(Ai + We) * np.linalg.det(Aj + Th.T @ Wsh @ Th)
log(f"A1 det factorization rel err: {abs(np.linalg.det(Lam)-rhs)/abs(rhs):.2e}")
h = 1e-4
d1 = (Sind_two(h, ups) - Sind_two(-h, ups)) / (2*h)
d2 = (Sind_two(h, ups) - 2*Sind_two(0, ups) + Sind_two(-h, ups)) / h**2
d1_pred = wsharp * np.trace(ups) / (aj + wsharp)
d2_pred = 2 * wsharp * aj * np.sum(ups**2) / (aj + wsharp)**2
log(f"A2 d/dt S_ind at 0: fd {d1:.8f} pred {d1_pred:.8f}; d2: fd {d2:.6f} pred {d2_pred:.6f}")
sk = rng.standard_normal((K, K)); sk = sk - sk.T
log(f"A3 skew constancy: |S(1.3)-S(0)| = {abs(Sind_two(1.3, sk)-Sind_two(0, sk)):.2e}")

# ---------- B ----------
K = 2; m = 3
links = [expm(0.5 * rng.standard_normal((K, K))) for _ in range(m)]
Ws = []
for _ in range(m):
    Wm = rng.standard_normal((K, K)); Ws.append(Wm @ Wm.T + 0.2 * np.eye(K))
edges = [((a) % m, (a + 1) % m) for a in range(m)]  # e_a: i_{a+1} -> i_a
Lam = build_Lambda(m, K, edges, Ws, [np.zeros((K, K))] * m, links)
Thp = links[0] @ links[1] @ links[2]
rhs = np.linalg.det(np.eye(K) - Thp)**2 * np.prod([np.linalg.det(Wm) for Wm in Ws])
log(f"B1 cycle determinant (m=3,K=2) rel err: {abs(np.linalg.det(Lam)-rhs)/abs(rhs):.2e}")
a0, w_ = 0.8, 0.37
g = np.exp(w_)
Lam1 = build_Lambda(2, 1, [(0, 1), (1, 0)], [np.eye(1), np.eye(1)], [a0*np.eye(1)]*2, [np.array([[g]]), np.array([[1/g]])])
pred = 0.5 * np.log(a0**2 + 4*a0*np.cosh(w_)**2) - np.log(2*np.pi)
val = 0.5 * np.log(np.linalg.det(Lam1)) - np.log(2*np.pi)
log(f"B2 K=1 witness: S_ind {val:.10f} pred {pred:.10f}")

# ---------- C ----------
def so3():
    Q, R = np.linalg.qr(rng.standard_normal((3, 3)))
    Q = Q * np.sign(np.diag(R))
    if np.linalg.det(Q) < 0: Q[:, 0] *= -1
    return Q
K = 3; N = 3
edges = [(0, 1), (1, 2), (2, 0)]  # e_0: 1->0, e_1: 2->1, e_2: 0->2 : cycle p = (e_0,e_1,e_2)
a = np.array([3.0, 3.5, 4.0]); w = np.array([0.25, 0.3, 0.2])
links = [so3() for _ in range(3)]
A = [a[i]*np.eye(K) for i in range(N)]; W = [w[e]*np.eye(K) for e in range(3)]
Lam = build_Lambda(N, K, edges, W, A, links)
Lam0 = build_Lambda(N, K, edges, W, A, [np.eye(K)]*3)
# diag part
adiag = np.array([a[i] + sum(w[e] for e, (s, t) in enumerate(edges) if i in (s, t)) for i in range(N)])
Ld = np.kron(np.diag(adiag), np.eye(K))
Lhop = Ld - Lam
M = np.linalg.solve(Ld, Lhop)
spr = max(abs(np.linalg.eigvals(M)))
bound = 1 - min(a[i]/adiag[i] for i in range(N))
log(f"C1 spectral radius {spr:.6f} <= bound {bound:.6f}: {spr <= bound + 1e-12}")
series = 0.0; Mr = np.eye(N*K)
for r in range(1, 400):
    Mr = Mr @ M; series += np.trace(Mr) / r
lhs = 0.5*np.log(np.linalg.det(Lam)); rhs = 0.5*np.log(np.linalg.det(Ld)) - 0.5*series
log(f"C2 log-det series (400 terms) err: {abs(lhs-rhs):.2e}")
Thp = links[0] @ links[1] @ links[2]
Qp = K - np.trace(Thp)
whop = w.max()/adiag.min()
coef = np.prod(w)/np.prod(adiag)
diff = 0.5*np.log(np.linalg.det(Lam)) - 0.5*np.log(np.linalg.det(Lam0))
rem = diff - coef*Qp
rem_bound = K/5*((2*whop)**5/(1-2*whop) + 2*whop**5/(1-whop))
log(f"C3 triangle: w_hop {whop:.4f}, diff {diff:.6e}, coef*Q {coef*Qp:.6e}, remainder {rem:.3e}, bound {rem_bound:.3e}, ok {abs(rem) <= rem_bound}")

# ---------- D ----------
alpha = np.linalg.det(np.diag(a) + np.array([[w[0]+w[2], -w[0], -w[2]], [-w[0], w[0]+w[1], -w[1]], [-w[2], -w[1], w[1]+w[2]]]))
beta = np.prod(w)
pred = alpha*(alpha + beta*Qp)**2
log(f"D1 SO(3) triangle: det Lambda {np.linalg.det(Lam):.8e} vs alpha(alpha+beta Q)^2 {pred:.8e}, rel err {abs(np.linalg.det(Lam)-pred)/pred:.2e}")
# general O(3) link (det = -1 allowed? GL+ requires det>0; use SO(3) only). Also check for a non-SO link: isometric links of GL+(3) with G=I are SO(3).

# ---------- E ----------
# K=1 theta graph: vertices 0,1; copies e0: 1->0, e1: 0->1, e2: 0->1 ; cycle rank 2
def detLam_theta(om):
    links = [np.array([[np.exp(o)]]) for o in om]
    return np.linalg.det(build_Lambda(2, 1, [(0,1),(1,0),(1,0)], [np.eye(1)]*3, [np.zeros((1,1))]*2, links))
# fundamental cycles (tree = e0): s1 = om0+om1 (cycle e0,e1), s2 = om0+om2
worst = 0.0
for _ in range(2000):
    om = 0.3*rng.standard_normal(3)
    s = np.array([om[0]+om[1], om[0]+om[2]])
    d = detLam_theta(om)
    lb = np.exp(-2*np.sum(np.abs(om)))*np.sum((1-np.exp(s))**2)
    worst = max(worst, lb/d)
log(f"E1 theta K=1: max over samples of (lower bound)/(det Lambda) = {worst:.4f} (must be <= 1)")

# ---------- F ----------
K = 3
S = rng.standard_normal((K, K)) + 2*np.eye(K)
cprime, lam = -0.8, 1.7
M = S @ np.diag([cprime, cprime, lam]) @ np.linalg.inv(S)
# is M a chart link? real log exists: check logm has real form via Culver (double negative eigenvalue, semisimple)
E = rng.standard_normal((K, K))
# choose E so that compressed 2x2 block (in S basis) has non-real eigenvalues
Et = np.linalg.inv(S) @ E @ S
Et[:2, :2] = np.array([[0.1, -1.0], [1.0, 0.1]])
E = S @ Et @ np.linalg.inv(S)
ok = True
for t in [1e-3, -1e-3, 5e-2, -5e-2]:
    ev = np.linalg.eigvals(M + t*E)
    neg_real = [z for z in ev if abs(z.imag) < 1e-12 and z.real < 0]
    ok = ok and (len(neg_real) == 0) and np.linalg.det(M + t*E) > 0
log(f"F1 K=3 two-sided perturbation of diag(c',c',lambda)-type chart link keeps no negative eigenvalue: {ok}")

with open(r"C:\Users\CHRISA~1\AppData\Local\Temp\claude\C--Users-chris-and-christine-Desktop-VFE-3-0\4e2da218-3dfb-44f7-95ba-4761b2a9cb35\scratchpad\lie_links\verify_V4b_checks_output.txt", "w") as f:
    f.write("\n".join(out) + "\n")
