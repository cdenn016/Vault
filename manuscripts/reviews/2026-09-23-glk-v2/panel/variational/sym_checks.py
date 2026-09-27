"""Symbolic checks (SymPy) for the variational identities of GL(K)_attention_v2 / supplementary_v2.

S1  Gibbs completion: A(beta) = sum b_j D_j + tau KL(b||pi) = tau KL(b||b*) - tau log Z  (3-simplex, general tau)
S2  Bernoulli compatibility record: exact label posterior and row free energy, A = tau * F_att
S3  Moment-matched covariance of the mixture-of-channels kernel (scalar, H=2, sources {self, j})
S4  Linear decoder = unit-temperature Gibbs readout of a shared-covariance Gaussian template bank (K=2)
S5  Shared-latent recognition mean with R=0 equals T times the key-side Gaussian lift of the query mean (K=2, r=1)
"""
import sympy as sp

out = []

# ---------------- S1 ----------------
tau = sp.symbols("tau", positive=True)
b1, b2 = sp.symbols("b1 b2", positive=True)
p1, p2, p3 = sp.symbols("p1 p2 p3", positive=True)
D1, D2, D3 = sp.symbols("D1 D2 D3", real=True)
b3 = 1 - b1 - b2
pi3 = [p1, p2, p3]
Ds = [D1, D2, D3]
bs = [b1, b2, b3]
Z = sum(pi3[k] * sp.exp(-Ds[k] / tau) for k in range(3))
bstar = [pi3[k] * sp.exp(-Ds[k] / tau) / Z for k in range(3)]
A = sum(bs[k] * Ds[k] for k in range(3)) + tau * sum(bs[k] * sp.log(bs[k] / pi3[k]) for k in range(3))
completion = tau * sum(bs[k] * sp.log(bs[k] / bstar[k]) for k in range(3)) - tau * sp.log(Z)
res1 = sp.simplify(sp.expand_log(A - completion, force=True))
out.append(f"S1 A - [tau KL(b||b*) - tau log Z] simplifies to: {res1}")

g = [sp.diff(A, v) for v in (b1, b2)]
sub = {b1: bstar[0], b2: bstar[1]}
gres = [sp.simplify(sp.expand_log(gi.subs(sub), force=True)) for gi in g]
out.append(f"S1 gradient of A on simplex at Gibbs row: {gres}")

# ---------------- S2 ----------------
lik = [sp.exp(-Ds[k] / tau) for k in range(3)]
post = [pi3[k] * lik[k] / sum(pi3[m] * lik[m] for m in range(3)) for k in range(3)]
res2a = [sp.simplify(post[k] - bstar[k]) for k in range(3)]
out.append(f"S2 exact label posterior minus Gibbs row: {res2a}")
Fb = sum(bs[k] * sp.log(bs[k] / (pi3[k] * lik[k])) for k in range(3))
Fatt = sum(bs[k] * sp.log(bs[k] / pi3[k]) for k in range(3)) + sum(bs[k] * Ds[k] for k in range(3)) / tau
res2b = sp.simplify(sp.expand_log(Fb - Fatt, force=True))
out.append(f"S2 sum b log(b/(pi*lik)) - [KL(b||pi) + tau^-1 sum b D] = {res2b}")
res2c = sp.simplify(sp.expand_log(A - tau * Fatt, force=True))
out.append(f"S2 A - tau*F_att = {res2c}")
Fatt_opt = Fatt.subs({b1: bstar[0], b2: bstar[1]})
res2d = sp.simplify(sp.expand_log(Fatt_opt + sp.log(Z), force=True))
out.append(f"S2 F_att(b*) + log P(o=1|z) = {res2d}")
out.append("S2 kernel normalization: exp(-D/tau) + (1-exp(-D/tau)) = " + str(sp.simplify(lik[0] + (1 - lik[0]))))

# ---------------- S3 ----------------
mu_i, mu_j = sp.symbols("mu_i mu_j", real=True)
s_i, s_j, qn = sp.symbols("s_i s_j q", positive=True)
bi1, bi2 = sp.symbols("beta_i1 beta_i2", positive=True)
l1i, l1j, l2i, l2j = sp.symbols("l1i l1j l2i l2j", real=True)
w = {("i", "i"): bi1 * bi2, ("i", "j"): bi1 * (1 - bi2), ("j", "i"): (1 - bi1) * bi2, ("j", "j"): (1 - bi1) * (1 - bi2)}
lk = {(1, "i"): l1i, (1, "j"): l1j, (2, "i"): l2i, (2, "j"): l2j}
mean_mix = 0
second_mix = 0
for (J1, J2), wt in w.items():
    ci = 1 + (lk[(1, J1)] if J1 == "i" else 0) + (lk[(2, J2)] if J2 == "i" else 0)
    cj = (lk[(1, J1)] if J1 == "j" else 0) + (lk[(2, J2)] if J2 == "j" else 0)
    m = ci * mu_i + cj * mu_j
    v = ci**2 * s_i + cj**2 * s_j + qn
    mean_mix += wt * m
    second_mix += wt * (v + m**2)
var_mix = sp.expand(second_mix - mean_mix**2)
beta = {(1, "i"): bi1, (1, "j"): 1 - bi1, (2, "i"): bi2, (2, "j"): 1 - bi2}
mh = {h: sum(beta[(h, J)] * lk[(h, J)] * (mu_i if J == "i" else mu_j) for J in "ij") for h in (1, 2)}
closed = qn + s_i
closed += sum(beta[(h, "i")] * 2 * lk[(h, "i")] * s_i for h in (1, 2))
for J, sJ in (("i", s_i), ("j", s_j)):
    for h in (1, 2):
        for hp in (1, 2):
            coef = beta[(h, J)] if h == hp else beta[(h, J)] * beta[(hp, J)]
            closed += coef * lk[(h, J)] * sJ * lk[(hp, J)]
for h in (1, 2):
    closed += sum(beta[(h, J)] * (lk[(h, J)] * (mu_i if J == "i" else mu_j))**2 for J in "ij") - mh[h]**2
res3m = sp.simplify(mean_mix - (mu_i + mh[1] + mh[2]))
res3v = sp.simplify(sp.expand(var_mix - closed))
out.append(f"S3 mixture mean - (mu_i + sum_h m_h) = {res3m}")
out.append(f"S3 mixture variance - closed form = {res3v}")

# ---------------- S4 ----------------
m1, m2 = sp.symbols("m1 m2", real=True)
S11, S22 = sp.symbols("S11 S22", positive=True); S12 = sp.symbols("S12", real=True)
a11, a22 = sp.symbols("a11 a22", positive=True); a12 = sp.symbols("a12", real=True)
wv = sp.Matrix(sp.symbols("w1 w2", real=True)); bv = sp.symbols("bv", real=True)
M = sp.Matrix([m1, m2]); S = sp.Matrix([[S11, S12], [S12, S22]]); Sig = sp.Matrix([[a11, a12], [a12, a22]])
mu_v = Sig * wv
P = Sig.inv()
KL = sp.Rational(1, 2) * ((P * S).trace() + ((M - mu_v).T * P * (M - mu_v))[0] - 2 + sp.log(Sig.det()) - sp.log(S.det()))
logit_gibbs = bv + sp.Rational(1, 2) * (wv.T * Sig * wv)[0] - KL
logit_lin = (wv.T * M)[0] + bv
diff4 = sp.simplify(sp.expand(logit_gibbs - logit_lin))
dep = [sp.simplify(sp.diff(diff4, v)) for v in list(wv) + [bv]]
out.append(f"S4 d/d(w_v,b_v) of [Gibbs logit - linear logit] = {dep}  (zero => class-independent offset)")

# ---------------- S5 ----------------
x1, x2, a = sp.symbols("x1 x2 a", real=True)
c11, c22 = sp.symbols("c11 c22", positive=True); c12 = sp.symbols("c12", real=True)
k1, k2, t1, t2 = sp.symbols("k1 k2 t1 t2", real=True)
xi = sp.Matrix([x1, x2]); C = sp.Matrix([[c11, c12], [c12, c22]])
SK = sp.Matrix([[k1, k2]]); T = sp.Matrix([[t1, t2]])
b = (SK * xi)[0]; VK = (SK * C * SK.T)[0]
cond_mean = (T * xi)[0] + (T * C * SK.T)[0] / VK * (a - b)
RK = C * SK.T / VK
lift = (T * (xi + RK * (a - b)))[0]
out.append(f"S5 shared-latent conditional mean at y=a minus T(xi + R_K (a-b)) = {sp.simplify(cond_mean - lift)}")

print("\n".join(out))
