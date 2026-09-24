r"""L03: divergence checks for PIFB2.tex.
(a) Gaussian KL closed form eq:gaussian_kl (l.184) vs 2D grid quadrature.
(b) thm:glk_invariance (l.462): KL(Om P || Om Q) = KL(P||Q) for random Om in GL(3).
(c) Local expansion of f-divergences: D_f(p_th || p_{th+d}) = f''(1)/2 * g_F(d,d) for KL, squared Hellinger, chi^2
    (1D Gaussian, quadrature) -- tests the l.3152 claim that the Fisher Hessian property is not shared by generic f-divergences.
(d) Renyi diagonal closed form eq:renyi_diagonal_itfb (l.1289) vs quadrature; alpha -> 1 limit; blend failure for alpha>1.
(e) D_{1/2} = -2 log BC equals twice the Bhattacharyya distance D_B = -log BC (l.1295).
"""
import numpy as np
import warnings; warnings.filterwarnings('ignore')
from scipy import integrate
rng = np.random.default_rng(3)

def kl_gauss(m1, S1, m2, S2):
    K = len(m1); S2i = np.linalg.inv(S2); d = m2 - m1
    return 0.5*(np.log(np.linalg.det(S2)/np.linalg.det(S1)) + np.trace(S2i@S1) + d@S2i@d - K)

def logpdf(x, m, S):
    K = len(m); d = x - m
    Si = np.linalg.inv(S)
    return -0.5*np.einsum('...i,ij,...j->...', d, Si, d) - 0.5*np.log((2*np.pi)**K*np.linalg.det(S))

# (a)
m1 = np.array([0.3, -0.2]); S1 = np.array([[1.0, 0.3], [0.3, 0.7]])
m2 = np.array([-0.4, 0.5]); S2 = np.array([[1.5, -0.2], [-0.2, 1.1]])
g = np.linspace(-9, 9, 1201); X, Y = np.meshgrid(g, g); P = np.stack([X, Y], -1)
lq = logpdf(P, m1, S1); lp = logpdf(P, m2, S2); h = g[1]-g[0]
kl_num = np.sum(np.exp(lq)*(lq-lp))*h*h
kl_cf = kl_gauss(m1, S1, m2, S2)
print(f"(a) KL closed form {kl_cf:.12f}  quadrature {kl_num:.12f}  resid {abs(kl_cf-kl_num):.2e}")

# (b)
worst = 0
for _ in range(200):
    K = 3
    A = rng.normal(size=(K, K)); SP = A@A.T+0.2*np.eye(K)
    B = rng.normal(size=(K, K)); SQ = B@B.T+0.2*np.eye(K)
    mP = rng.normal(size=K); mQ = rng.normal(size=K)
    Om = rng.normal(size=(K, K))
    if rng.random() < 0.5: Om[0] *= -1  # include det<0 elements
    base = kl_gauss(mP, SP, mQ, SQ)
    tr = kl_gauss(Om@mP, Om@SP@Om.T, Om@mQ, Om@SQ@Om.T)
    worst = max(worst, abs(tr-base)/max(1, abs(base)))
print(f"(b) GL(3) invariance, 200 random (incl. det<0): max rel resid {worst:.2e}")

# (c) local expansion, 1D Gaussian theta=(mu, s=sigma^2)
def pdf1(x, m, v): return np.exp(-(x-m)**2/(2*v))/np.sqrt(2*np.pi*v)
def fdiv(f, th1, th2):
    # D_f(p||q) = int q f(p/q)
    val, _ = integrate.quad(lambda x: pdf1(x, *th2)*f(pdf1(x, *th1)/pdf1(x, *th2)), -30, 30, limit=400, epsabs=1e-14, epsrel=1e-12)
    return val
fs = {"KL": (lambda t: t*np.log(t)-t+1, 1.0),
      "sqHellinger(f=(sqrt t-1)^2)": (lambda t: (np.sqrt(t)-1)**2, 0.5),
      "chi2(f=(t-1)^2)": (lambda t: (t-1)**2, 2.0)}
th = (0.2, 1.3); d = np.array([1.0, 0.7])
gF = d[0]**2/th[1] + 0.5*(d[1]/th[1])**2
for eps in [1e-2, 1e-3]:
  for name, (f, f2) in fs.items():
    val = fdiv(f, th, (th[0]+eps*d[0], th[1]+eps*d[1]))
    pred = 0.5*f2*gF*eps**2
    print(f"(c) eps={eps:g} {name:30s} D/eps^2 {val/eps**2:.6f}  f''(1)/2*gF {pred/eps**2:.6f}  rel diff {abs(val-pred)/pred:.2e}")

# (d) Renyi diagonal closed form (sigma = variance)
def renyi_diag(a, mq, vq, mp, vp):
    vb = (1-a)*vq + a*vp
    if np.any(vb <= 0): return np.inf
    return 0.5*(a*np.sum((mp-mq)**2/vb) + (1/(a-1))*np.sum((1-a)*np.log(vq)+a*np.log(vp)-np.log(vb)))
def renyi_num1(a, mq, vq, mp, vp):
    lg = lambda x, m, v: -(x-m)**2/(2*v) - 0.5*np.log(2*np.pi*v)
    val, _ = integrate.quad(lambda x: np.exp(a*lg(x, mq, vq)+(1-a)*lg(x, mp, vp)), -25, 25, limit=500, epsabs=1e-15, epsrel=1e-13)
    return np.log(val)/(a-1)
mq, vq, mp, vp = 0.1, 0.8, -0.6, 1.4
for a in [0.3, 0.5, 2.0, 1.5]:
    cf = renyi_diag(a, np.array([mq]), np.array([vq]), np.array([mp]), np.array([vp]))
    nu = renyi_num1(a, mq, vq, mp, vp)
    print(f"(d) alpha={a}: closed {cf:.10f} quad {nu:.10f} resid {abs(cf-nu):.2e}")
# 2D diagonal = sum of 1D
a = 0.7
mq2 = np.array([0.1, 0.4]); vq2 = np.array([0.8, 2.0]); mp2 = np.array([-0.6, 0.0]); vp2 = np.array([1.4, 0.5])
cf2 = renyi_diag(a, mq2, vq2, mp2, vp2)
nu2 = sum(renyi_num1(a, mq2[k], vq2[k], mp2[k], vp2[k]) for k in range(2))
print(f"(d) 2D diagonal alpha=0.7: closed {cf2:.10f} sum-of-1D quad {nu2:.10f} resid {abs(cf2-nu2):.2e}")
klv = kl_gauss(np.array([mq]), np.array([[vq]]), np.array([mp]), np.array([[vp]]))
for e in [1e-3, 1e-6]:
    for a in [1-e, 1+e]:
        r = renyi_diag(a, np.array([mq]), np.array([vq]), np.array([mp]), np.array([vp]))
        print(f"(d) alpha=1{'+' if a>1 else '-'}{e:g}: Renyi {r:.12f} KL {klv:.12f} diff {abs(r-klv):.2e}")
# blend failure: alpha>1 with vp > vq*... : vb=(1-a)vq + a vp <= 0 needs vq > a vp/(a-1)
a = 3.0; vq_b, vp_b = 3.5, 1.0   # vb = -2*3.5 + 3 = -4 <0
print(f"(d) blend alpha=3, vq=3.5, vp=1: closed form -> {renyi_diag(a, np.array([0.]), np.array([vq_b]), np.array([0.]), np.array([vp_b]))}")
for L in [10, 20, 30]:
    val, _ = integrate.quad(lambda x: pdf1(x, 0, vq_b)**a*pdf1(x, 0, vp_b)**(1-a), -L, L, limit=500)
    print(f"      Hellinger integral truncated at |x|<{L}: {val:.3e} (grows without bound -> D=+inf)")

# (e) Bhattacharyya
bc, _ = integrate.quad(lambda x: np.sqrt(pdf1(x, mq, vq)*pdf1(x, mp, vp)), -40, 40, epsabs=1e-15)
D_half = renyi_diag(0.5, np.array([mq]), np.array([vq]), np.array([mp]), np.array([vp]))
print(f"(e) D_1/2 = {D_half:.10f}; -log BC (Bhattacharyya distance) = {-np.log(bc):.10f}; ratio {D_half/(-np.log(bc)):.10f}")
