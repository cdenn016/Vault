r"""L08: PIFB2 multi-head (1265-1270), RoPE (1272-1275), causal mask/holonomy (418, 1778),
self-pair energy, and sender-row causality of the scalar potential. Float64."""
import numpy as np
from scipy.linalg import expm
rng = np.random.default_rng(1)

def softmax(x):
    x = x - x.max(); e = np.exp(x); return e/e.sum()
def kl(m0, S0, m1, S1):
    S1i = np.linalg.inv(S1); dm = m1 - m0
    return 0.5*(np.trace(S1i@S0) + dm@S1i@dm - len(m0) + np.linalg.slogdet(S1)[1] - np.linalg.slogdet(S0)[1])

# (1) Multi-head: block-diagonal GL(d_h)^H transport + one row beta (eq:pointwise_free_energy)
H, dh, N = 3, 2, 5; K = H*dh; kappa = 1.0
mus = rng.normal(size=(N, K)); i = 4
U = [np.kron(np.eye(1), np.eye(K)) for _ in range(N)]
Ub = [np.zeros((K, K)) for _ in range(N)]
for n in range(N):
    for h in range(H):
        Ub[n][h*dh:(h+1)*dh, h*dh:(h+1)*dh] = rng.normal(size=(dh, dh)) + 2*np.eye(dh)
E_h = np.zeros((H, N))
for j in range(N):
    Om = Ub[i]@np.linalg.inv(Ub[j])
    for h in range(H):
        sl = slice(h*dh, (h+1)*dh)
        E_h[h, j] = kl(mus[i, sl], np.eye(dh), Om[sl, sl]@mus[j, sl], Om[sl, sl]@Om[sl, sl].T)
E_full = np.array([kl(mus[i], np.eye(K), (Ub[i]@np.linalg.inv(Ub[j]))@mus[j],
                      (Ub[i]@np.linalg.inv(Ub[j]))@(Ub[i]@np.linalg.inv(Ub[j])).T) for j in range(N)])
print("(1) block-diag KL additivity residual:", np.abs(E_full - E_h.sum(0)).max())
b_single = softmax(-E_full/(kappa*np.sqrt(K)))
b_heads = np.array([softmax(-E_h[h]/(kappa*np.sqrt(dh))) for h in range(H)])
print("    single-row beta (tau=kappa sqrt K):", np.round(b_single, 4))
print("    per-head beta rows (tau=kappa sqrt d_h):\n", np.round(b_heads, 4))
print("    max |per-head - single| =", np.abs(b_heads - b_single).max(),
      "; heads differ among themselves by", np.abs(b_heads[0]-b_heads[1]).max())

# (2) RoPE
d = 4; th = 10000.0**(-2*np.arange(d//2)/d)
def R(m):
    Z = np.zeros((d, d))
    for n, t in enumerate(th):
        c, s = np.cos(m*t), np.sin(m*t); Z[2*n:2*n+2, 2*n:2*n+2] = [[c, -s], [s, c]]
    return Z
q, k = rng.normal(size=d), rng.normal(size=d)
print("(2) RoPE relative property: (R3 q).(R1 k) - (R7 q).(R5 k) =", (R(3)@q)@(R(1)@k) - (R(7)@q)@(R(5)@k))
print("    R_i^T R_j == R_{j-i}:", np.abs(R(3).T@R(5) - R(2)).max())
# KL cross term with U_i = R(theta_i) and shared C=I: x_i.k_j = mu_i^T U_i^{-T} U_j^T mu_j
mi, mj = rng.normal(size=d), rng.normal(size=d); ii, jj = 5, 2
cross = (np.linalg.solve(R(ii), mi))@(R(jj).T@mj)
print("    KL cross term with U=R(theta): matches mu_i^T R_{i-j} mu_j:", abs(cross - mi@R(ii-jj)@mj),
      "; matches RoPE kernel mu_i^T R_{j-i} mu_j:", abs(cross - mi@R(jj-ii)@mj))
# noncompact abelian: U_m = expm(m A), A arbitrary in gl(d); Sigma = C fixed -> KL depends only on i-j
A = 0.3*rng.normal(size=(d, d)); C = np.eye(d) + 0.2*np.diag(rng.random(d))
def Uab(m): return expm(m*A)
def Egauge(a, b, Uf):
    Om = Uf(a)@np.linalg.inv(Uf(b)); return kl(mi, C, Om@mj, Om@C@Om.T)
print("    noncompact abelian GL frames: E(3,1)-E(6,4) =", Egauge(3, 1, Uab) - Egauge(6, 4, Uab),
      " (A not antisymmetric: |A+A^T|=", np.abs(A+A.T).max().round(3), ")")
B = 0.3*rng.normal(size=(d, d))
def Unab(m): return expm(m*A + m**2*B)   # non-commuting phi_m
print("    non-commuting frames: E(3,1)-E(6,4) =", Egauge(3, 1, Unab) - Egauge(6, 4, Unab))

# (3) causal DAG triangle: holonomy produces frustration (nonzero minimal energy) without directed cycles
def rot(t): return np.array([[np.cos(t), -np.sin(t)], [np.sin(t), np.cos(t)]])
mu1 = np.array([1.0, 0.0])
print("(3) causal triangle 1<2<3 (3 attends 1,2; 2 attends 1); Om_21=Om_32=I, Om_31=rot(theta)")
for theta in (0.0, 0.5, 1.0, 2.0):
    # receiver-only minimization, isotropic unit covariances, beta fixed = 1/2 for row 3, no priors
    mu2 = mu1.copy()                           # q_2 minimizes KL(q_2 || Om_21 q_1) -> Om_21 mu1
    t1, t2 = rot(theta)@mu1, mu2               # targets of q_3
    mu3 = 0.5*(t1 + t2)
    Emin = 0.5*(0.5*np.sum((mu3-t1)**2) + 0.5*np.sum((mu3-t2)**2))
    Hol = np.linalg.inv(rot(theta))@np.eye(2)@np.eye(2)   # Om_13 Om_32 Om_21
    print(f"    theta={theta}: min row-3 energy = {Emin:.6f};  |H - I|_F^2 = {np.sum((Hol-np.eye(2))**2):.6f};  ratio = {Emin/max(np.sum((Hol-np.eye(2))**2),1e-300):.4f}")

# (4) self pair: Omega_ii = I -> E_ii = 0 is the row minimum; with uniform causal prior beta_ii is the row max
cnt = 0; T = 2000
for _ in range(T):
    n = 5; Uv = [rng.normal(size=(2, 2)) + 2*np.eye(2) for _ in range(n)]
    ms = rng.normal(size=(n, 2)); Ss = [np.eye(2)*rng.uniform(0.5, 2) for _ in range(n)]
    ii = n-1; E = []
    for j in range(n):
        Om = Uv[ii]@np.linalg.inv(Uv[j]); E.append(kl(ms[ii], Ss[ii], Om@ms[j], Om@Ss[j]@Om.T))
    E = np.array(E); cnt += (np.argmin(E) == ii) and abs(E[ii]) < 1e-12
print(f"(4) self pair has E_ii=0 and is the row argmin of E in {cnt}/{T} random rows")

# (5) sender rows of the scalar potential under a causal prior carry future information
# F = sum_{l>=i} beta_{li} E_{li}; dF/dmu_0 includes l=1,2 terms (future tokens) unless receiver-only
n = 3; ms = rng.normal(size=(n, 2)); tau = 1.0
def F_total(ms):
    tot = 0.0
    for l in range(n):
        E = np.array([0.5*np.sum((ms[l]-ms[j])**2) for j in range(l+1)])
        tot += -tau*np.log(np.sum(np.exp(-E/tau))/(l+1))     # reduced row value -tau log Z_l
    return tot
def grad0(ms, h=1e-6):
    g = np.zeros(2)
    for a in range(2):
        mp, mm = ms.copy(), ms.copy(); mp[0, a] += h; mm[0, a] -= h
        g[a] = (F_total(mp) - F_total(mm))/(2*h)
    return g
g_before = grad0(ms); ms2 = ms.copy(); ms2[2] += np.array([3.0, -2.0])
print("(5) full scalar gradient at token 0 changes when future token 2 changes:", np.abs(grad0(ms2) - g_before).max())
print("    receiver-only gradient at token 0 (row 0 has only the self pair) =", 0.0, "(independent of tokens 1,2)")
