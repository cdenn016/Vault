r"""L08: PIFB2 sec:transformers (1006-1245). Float64 checks of the isotropic KL expansion,
eq:full_kl_general, the (R3) substitution, softmax cancellations, the (N) condition,
the concentration argument, the symmetric closure, and the balanced-factorization claims."""
import numpy as np
rng = np.random.default_rng(0)
d = 4

def kl(m0, S0, m1, S1):
    r"""KL(N(m0,S0) || N(m1,S1))."""
    S1i = np.linalg.inv(S1); dm = m1 - m0
    return 0.5*(np.trace(S1i@S0) + dm@S1i@dm - len(m0) + np.linalg.slogdet(S1)[1] - np.linalg.slogdet(S0)[1])

def spd(n):
    A = rng.normal(size=(n, n)); return A@A.T + n*np.eye(n)

def softmax(x):
    x = x - x.max(); e = np.exp(x); return e/e.sum()

# (a) isotropic KL with general transport = S(Omega) + |Omega^{-1} mu_i - mu_j|^2/(2 s2)
s2 = 0.7; Om = rng.normal(size=(d, d)); mi, mj = rng.normal(size=d), rng.normal(size=d)
G = Om@Om.T
S = 0.5*(np.linalg.slogdet(G)[1] + np.trace(np.linalg.inv(G)) - d)
lhs = kl(mi, s2*np.eye(d), Om@mj, s2*G)
rhs = S + np.sum((np.linalg.solve(Om, mi) - mj)**2)/(2*s2)
print("(a) isotropic KL decomposition residual:", abs(lhs-rhs), " S(Omega)=", S)
Q, _ = np.linalg.qr(rng.normal(size=(d, d)))
print("    S(orthogonal)=", 0.5*(np.linalg.slogdet(Q@Q.T)[1] + np.trace(np.linalg.inv(Q@Q.T)) - d))
Smin = min(0.5*(np.linalg.slogdet(A@A.T)[1] + np.trace(np.linalg.inv(A@A.T)) - d)
           for A in rng.normal(size=(2000, d, d)))
print("    min S over 2000 random GL draws (>=0 expected):", Smin)

# (b) eq:full_kl_general
Ui, Uj = rng.normal(size=(d, d)), rng.normal(size=(d, d)); Si, Sj = spd(d), spd(d)
Omij = Ui@np.linalg.inv(Uj)
x = np.linalg.solve(Ui, mi); P = np.linalg.solve(Ui, Si)@np.linalg.inv(Ui).T
H = Uj.T@np.linalg.solve(Sj, Uj); k = Uj.T@np.linalg.solve(Sj, mj); r = mj@np.linalg.solve(Sj, mj)
full = 0.5*(np.linalg.slogdet(Sj)[1] - np.linalg.slogdet(Si)[1] + 2*np.log(abs(np.linalg.det(Ui)))
            - 2*np.log(abs(np.linalg.det(Uj))) - d + np.trace(H@P) + x@H@x - 2*x@k + r)
print("(b) eq:full_kl_general residual:", abs(full - kl(mi, Si, Omij@mj, Omij@Sj@Omij.T)))
# common-frame invariance: KL(q_i||Om q_j) = KL(N(x_i,P_i)||N(x_j,P_j))
xj = np.linalg.solve(Uj, mj); Pj = np.linalg.solve(Uj, Sj)@np.linalg.inv(Uj).T
print("    common-frame (trivial transport) KL residual:", abs(kl(x, P, xj, Pj) - kl(mi, Si, Omij@mj, Omij@Sj@Omij.T)))
print("    H_j == P_j^{-1} residual:", np.abs(H - np.linalg.inv(Pj)).max(), " k_j == P_j^{-1} x_j residual:", np.abs(k - np.linalg.solve(Pj, xj)).max())

# (c) (R3): score with M replacing the cross term equals KL-attention under constant Omega = M^{-T}
N = 6; mus = rng.normal(size=(N, d)); M = rng.normal(size=(d, d)); tau = 1.3
i = 2
s_R3 = np.array([(mus[i]@mus[i] + mus[j]@mus[j] - 2*mus[i]@M@mus[j])/(2*s2) for j in range(N)])
OmC = np.linalg.inv(M).T
s_KL = np.array([kl(mus[i], s2*np.eye(d), OmC@mus[j], s2*OmC@OmC.T) for j in range(N)])
print("(c) beta(R3) vs beta(KL, Omega=M^{-T}) max diff:", np.abs(softmax(-s_R3/tau) - softmax(-s_KL/tau)).max())
# (d) query-norm cancellation: logit = [mu_i M mu_j - |mu_j|^2/2]/(s2 tau)
lt = np.array([(mus[i]@M@mus[j] - 0.5*mus[j]@mus[j])/s2 for j in range(N)])
print("(d) query-norm cancellation max diff:", np.abs(softmax(-s_R3/tau) - softmax(lt/tau)).max())

# (e) (N) as stated in thm:transformer_recovery (|K_j| const) vs the proof's |mu_j| const
WQ, WK = rng.normal(size=(d, d)), rng.normal(size=(d, d)); Mq = s2*WQ@WK.T
kdir = rng.normal(size=(N, d)); kdir /= np.linalg.norm(kdir, axis=1, keepdims=True)
musN = np.linalg.solve(WK.T, kdir.T).T          # K_j = mu_j^T W_K has unit norm for all j
Kn = np.linalg.norm(musN@WK, axis=1); mun = np.linalg.norm(musN, axis=1)
Qi = musN[0]@WQ; dk = d; kap = 1.0; tauv = kap*np.sqrt(dk)
beta_model = softmax(np.array([(musN[0]@Mq@musN[j] - 0.5*musN[j]@musN[j])/s2 for j in range(N)])/tauv)
beta_vas = softmax((musN@WK@Qi)/tauv)
print("(e) |K_j| spread:", Kn.max()-Kn.min(), " |mu_j| spread:", mun.max()-mun.min())
print("    (N)-as-stated: max |beta_model - beta_Vaswani| =", np.abs(beta_model - beta_vas).max())
musS = rng.normal(size=(N, d)); musS /= np.linalg.norm(musS, axis=1, keepdims=True)
b1 = softmax(np.array([(musS[0]@Mq@musS[j] - 0.5)/s2 for j in range(N)])/tauv)
b2 = softmax((musS@WK@(musS[0]@WQ))/tauv)
print("    |mu_j| const (proof's regime): max diff =", np.abs(b1 - b2).max())

# (f) concentration: across-key std of |mu_j|^2/2 vs content logits mu_i.mu_j (M=I), unit variance
for dd in (16, 256, 4096):
    X = rng.normal(size=(4000, dd)); q = rng.normal(size=dd)
    print(f"(f) d={dd}: std(|mu_j|^2/2)/std(mu_i.mu_j) =", np.std(0.5*np.sum(X**2, 1))/np.std(X@q))

# (g) symmetric closure Sigma_j = U_j C U_j^T: tr(H_j P_i), x_i^T H_j x_i become j-independent
C = spd(d); vals = []
for _ in range(5):
    Uj = rng.normal(size=(d, d)); Sj = Uj@C@Uj.T; Hj = Uj.T@np.linalg.solve(Sj, Uj)
    vals.append((np.trace(Hj@P), x@Hj@x))
vals = np.array(vals); print("(g) closure: spread of tr(H_j P_i), x^T H_j x over j:", np.ptp(vals, 0), " (row-constant, not zero:", vals[0], ")")

# (h) balanced factorization: gradient flow conserves A^T A - B^T B; balanced stabilizer is O(d)
A, B = rng.normal(size=(d, d)), rng.normal(size=(d, d)); T = rng.normal(size=(d, d))
def gradL(A, B):  # L = 0.5 |A B^T - T|^2
    R = A@B.T - T; return R@B, R.T@A
C0 = A.T@A - B.T@B; dt = 1e-4
for _ in range(2000):
    gA, gB = gradL(A, B); A, B = A - dt*gA, B - dt*gB
print("(h) gradient-flow drift of A^TA-B^TB (Euler, dt=1e-4, 2000 steps):", np.abs(A.T@A - B.T@B - C0).max(), " (O(dt) discretization)")
Mh = rng.normal(size=(d, d)); Uu, sv, Vt = np.linalg.svd(Mh); Aq = Uu*np.sqrt(sv); Ak = Vt.T*np.sqrt(sv)
print("    SVD balanced: |AqAk^T-M|=", np.abs(Aq@Ak.T - Mh).max(), " |Aq^TAq-Ak^TAk|=", np.abs(Aq.T@Aq - Ak.T@Ak).max())

# (i) tau: var(q.k) = d_k for unit-variance independent components
for dd in (16, 64):
    qv, kv = rng.normal(size=(200000, dd)), rng.normal(size=(200000, dd))
    print(f"(i) d_k={dd}: var(q.k)/d_k =", np.var(np.sum(qv*kv, 1))/dd)
