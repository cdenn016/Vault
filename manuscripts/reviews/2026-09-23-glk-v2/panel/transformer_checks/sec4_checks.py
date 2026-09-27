import numpy as np, sympy as sp, json
from scipy.special import softmax
from scipy.linalg import sqrtm
rng = np.random.default_rng(20260923)

def kl_gauss(a, Va, b, Vb):
    r = len(a); P = np.linalg.inv(Vb); d = a - b
    return 0.5*(np.trace(P@Va) + d@P@d - r + np.linalg.slogdet(Vb)[1] - np.linalg.slogdet(Va)[1])

def kl_expanded(a, Va, b, Vb):
    r = len(a); P = np.linalg.inv(Vb)
    return 0.5*(np.trace(P@Va) + a@P@a - 2*a@P@b + b@P@b - r + np.linalg.slogdet(Vb)[1] - np.linalg.slogdet(Va)[1])

def rand_spd(r, cond=10.0):
    Q,_ = np.linalg.qr(rng.standard_normal((r,r)))
    ev = np.exp(rng.uniform(0, np.log(cond), r))
    return Q@np.diag(ev)@Q.T

out = {}
res = 0.0
for _ in range(500):
    r = int(rng.integers(1, 9)); a,b = rng.standard_normal(r), rng.standard_normal(r); Va, Vb = rand_spd(r), rand_spd(r)
    res = max(res, abs(kl_gauss(a,Va,b,Vb) - kl_expanded(a,Va,b,Vb)))
out["kl_expansion_max_abs_residual"] = res

res = 0.0
for _ in range(300):
    r = int(rng.integers(1, 9)); n = int(rng.integers(2, 12)); tau = rng.uniform(0.2, 6)
    Vs = rand_spd(r, 50); W = np.real(sqrtm(np.linalg.inv(Vs)))
    a = rng.standard_normal(r)*2; VQ = rand_spd(r, 30); B = rng.standard_normal((n, r))*2
    pi = rng.dirichlet(np.ones(n))
    D = np.array([kl_gauss(a, VQ, B[j], Vs) for j in range(n)])
    beta = softmax(-D/tau + np.log(pi))
    q = W@a; K = B@W.T
    beta2 = softmax(K@q/tau - (K**2).sum(1)/(2*tau) + np.log(pi))
    res = max(res, np.abs(beta - beta2).max())
out["prop_dot_product_max_abs_residual"] = res

res = 0.0
for _ in range(200):
    r = int(rng.integers(1, 9)); s2 = rng.uniform(0.1, 5); a,b = rng.standard_normal(r), rng.standard_normal(r)
    res = max(res, abs(kl_gauss(a, s2*np.eye(r), b, s2*np.eye(r)) - ((a-b)**2).sum()/(2*s2)))
out["isotropic_distance_residual"] = res

res = 0.0
for _ in range(300):
    r = int(rng.integers(1, 9)); n = int(rng.integers(2, 12)); tau = rng.uniform(0.2, 6)
    q = rng.standard_normal(r)*2; K = rng.standard_normal((n, r))*2; pi0 = rng.dirichlet(np.ones(n))
    w = pi0*np.exp((K**2).sum(1)/(2*tau)); pi = w/w.sum()
    beta = softmax(K@q/tau - (K**2).sum(1)/(2*tau) + np.log(pi))
    p = softmax(K@q/tau + np.log(pi0))
    res = max(res, np.abs(beta - p).max())
out["compensation_prior_residual"] = res

D = np.array([kl_gauss(np.zeros(1), np.eye(1), np.array([bj]), np.eye(1)) for bj in (0.0, 1.0)])
out["counterexample_gaussian"] = softmax(-D).tolist()
out["counterexample_claimed"] = (np.array([1, np.exp(-0.5)])/(1+np.exp(-0.5))).tolist()
out["counterexample_dot"] = softmax(np.zeros(2)).tolist()

worst = 0.0; viol_sharp = 0; viol_stated = 0; slack_stated = []
for _ in range(20000):
    n = int(rng.integers(2, 20)); tau = rng.uniform(0.3, 6); r = int(rng.integers(1, 6))
    q = rng.standard_normal(r)*rng.uniform(0.1,3); K = rng.standard_normal((n, r))*rng.uniform(0.1,3)
    pi = rng.dirichlet(np.ones(n)*rng.uniform(0.2,3))
    nk = (K**2).sum(1); c = 0.5*(nk.max()+nk.min())
    eps = np.abs(nk - c).max()/(2*tau)
    p = softmax(K@q/tau + np.log(pi)); beta = softmax(K@q/tau - nk/(2*tau) + np.log(pi))
    l1 = np.abs(beta - p).sum()
    sharp = 2*np.tanh(eps/2); stated = np.expm1(2*eps)
    if l1 > sharp*(1+1e-12)+1e-15: viol_sharp += 1
    if l1 > stated*(1+1e-12)+1e-15: viol_stated += 1
    if sharp > 1e-12: worst = max(worst, l1/sharp)
    if l1 > 1e-12: slack_stated.append(stated/l1)
out["bound_trials"] = 20000
out["bound_violations_sharp_2tanh"] = viol_sharp
out["bound_violations_stated"] = viol_stated
out["bound_max_ratio_L1_over_2tanh"] = worst
out["stated_over_actual_median"] = float(np.median(slack_stated))
for eps in (0.1, 0.7, 2.0):
    s = 1/(1+np.exp(eps)); p = np.array([s, 1-s]); delta = np.array([eps, -eps])
    beta = p*np.exp(delta); beta /= beta.sum()
    out["two_point_eps" + str(eps)] = dict(L1=float(np.abs(beta-p).sum()), sharp=float(2*np.tanh(eps/2)), stated=float(np.expm1(2*eps)))

s, e = sp.symbols("s epsilon", positive=True)
t = sp.exp(2*e)
tv = s*t/(s*t+1-s) - s
crit = sp.solve(sp.diff(tv, s), s)
crit = [x for x in crit if sp.simplify(x.subs(e, 1)).is_positive]
tvmax = sp.simplify(tv.subs(s, crit[0]))
out["sympy_sstar"] = str(crit[0]); out["sympy_tvmax"] = str(tvmax)
out["sympy_tvmax_minus_tanh_half_eps_numeric"] = [float((tvmax - sp.tanh(e/2)).subs(e, v)) for v in (0.1, 0.7, 2.0, 5.0)]
out["stated_exceeds_trivial_2_when_eps_gt"] = float(np.log(3)/2)

for r in (32, 256):
    M = 20000
    X = rng.standard_normal((M, r)); Y = rng.standard_normal((M, r))
    nk = (X**2).sum(1); dot = (X*Y).sum(1); tau = np.sqrt(r)
    out["var_r" + str(r)] = dict(var_sqnorm=float(nk.var()), claimed_2r=2*r, var_dot=float(dot.var()), claimed_r=r,
                          sd_bias_term=float((nk/(2*tau)).std()), sd_logit_term=float((dot/tau).std()))

r = 32; tau = 3.1; q = rng.standard_normal(r); k = rng.standard_normal(r); c = (np.sqrt(r)/tau)**0.5
out["temperature_rescale_residual"] = float(abs(q@k/tau - (c*q)@(c*k)/np.sqrt(r)))
out["temperature_rescale_bias_residual"] = float(abs(k@k/(2*tau) - (c*k)@(c*k)/(2*np.sqrt(r))))

def R_of(pos, r, base=100.0):
    Rm = np.zeros((r, r))
    for m in range(r//2):
        th = pos*base**(-2*m/r); cth, sth = np.cos(th), np.sin(th)
        Rm[2*m:2*m+2, 2*m:2*m+2] = [[cth, -sth],[sth, cth]]
    return Rm
r = 8; res_rel = 0.0
for _ in range(200):
    a, b = rng.standard_normal(r), rng.standard_normal(r); VQ, VK = rand_spd(r, 40), rand_spd(r, 40)
    i, j = int(rng.integers(0, 60)), int(rng.integers(0, 60)); sft = int(rng.integers(1, 40))
    Ri, Rj = R_of(i, r), R_of(j, r)
    D1 = kl_gauss(Ri@a, Ri@VQ@Ri.T, Rj@b, Rj@VK@Rj.T)
    Ris, Rjs = R_of(i+sft, r), R_of(j+sft, r)
    D2 = kl_gauss(Ris@a, Ris@VQ@Ris.T, Rjs@b, Rjs@VK@Rjs.T)
    Rrel = R_of(i-j, r)
    D3 = kl_gauss(Rrel@a, Rrel@VQ@Rrel.T, b, VK)
    res_rel = max(res_rel, abs(D1-D2), abs(D1-D3))
out["rope_full_kl_relative_residual_anisotropic"] = res_rel

K_, r_ = 12, 4
SQ, SK = rng.standard_normal((r_, K_)), rng.standard_normal((r_, K_))
xi = rng.standard_normal((5, K_)); C = [rand_spd(K_, 20) for _ in range(5)]
A = rng.standard_normal((r_, r_)) + 3*np.eye(r_)
def Dmat(SQ, SK):
    return np.array([[kl_gauss(SQ@xi[i], SQ@C[i]@SQ.T, SK@xi[j], SK@C[j]@SK.T) for j in range(5)] for i in range(5)])
D0 = Dmat(SQ, SK)
out["cogredient_residual"] = float(np.abs(D0 - Dmat(A@SQ, A@SK)).max())
out["contragredient_change"] = float(np.abs(D0 - Dmat(A@SQ, np.linalg.inv(A).T@SK)).max())
out["projected_cov_condition_before_after_A"] = [float(np.linalg.cond(SQ@C[0]@SQ.T)), float(np.linalg.cond(A@SQ@C[0]@SQ.T@A.T))]
out["min_singular_SQ_before_after_A"] = [float(np.linalg.svd(SQ, compute_uv=False).min()), float(np.linalg.svd(A@SQ, compute_uv=False).min())]
def relspec(SQ, SK, i, j):
    return np.sort(np.real(np.linalg.eigvals(np.linalg.solve(SK@C[j]@SK.T, SQ@C[i]@SQ.T))))
out["relative_spectrum_invariance"] = float(np.abs(relspec(SQ,SK,0,1) - relspec(A@SQ,A@SK,0,1)).max())

def press_code(n):
    def p2(c): return [2.0**(-8.0*h/c) for h in range(1, c+1)]
    cp = 2**(n.bit_length()-1); sl = p2(cp)
    if cp != n: sl = sl + p2(2*cp)[::2][:n-cp]
    return sl
out["alibi_H8_code"] = press_code(8); out["alibi_H8_formula"] = [2.0**(-8*h/8) for h in range(1,9)]
out["alibi_H5_code"] = press_code(5); out["alibi_H5_formula"] = [2.0**(-8*h/5) for h in range(1,6)]
print(json.dumps(out, indent=1, default=float))
