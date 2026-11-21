"""Exact recomputation of the pitchfork cubic coefficient, ch.18 link dynamics, sec. it2:ch-critical-mode.
Model reconstructed from eq. it2:threshold-objective and the stated references.
Usage: python pitchfork_check.py
"""
import sympy as sp
R = sp.Rational
X = list(sp.symbols('mu0 mu1 mu2 a1 a2 v0 v1 v2 V1 V2'))
mu0, mu1, mu2, a1, a2, v0, v1, v2, V1, V2 = X
s, eps, b = sp.symbols('s eps b')


def selfKL(mu, v, m, P):
    r"""KL(N(mu,v) || N(m,1/P)) = (P v + P (mu-m)^2 - 1 - log(P v))/2."""
    return R(1, 2)*(P*v + P*(mu-m)**2 - 1 - sp.log(P*v))


def model(Pa):
    F0 = (selfKL(mu0, v0, 0, 1) + selfKL(mu1, v1, R(-23, 15), R(5, 4)) + selfKL(mu2, v2, R(23, 15), R(5, 4))
          + selfKL(a1, V1, 0, Pa) + selfKL(a2, V2, 0, Pa))
    S0, S1, S2 = v0+1, v1+1, v2+1
    d1 = mu0-mu1-a1
    d2 = mu0-mu2-a2
    C1 = R(1, 2)*((S0+d1**2+V1)/S1 - 1 + sp.log(S1) - sp.log(S0))
    C2 = R(1, 2)*((S0+d2**2+V2)/S2 - 1 + sp.log(S2) - sp.log(S0))
    return F0 + (C1+C2)/2, C1-C2, C1, C2


xs = [0, R(-4, 3), R(4, 3), R(1, 3), R(-1, 3), 1, 1, 1, 1, 1]
sub = dict(zip(X, xs))
A, Dl, C1, C2 = model(R(3, 4))
G = A + s*Dl
hfun = (R(1, 2)+s)*sp.log(1+2*s) + (R(1, 2)-s)*sp.log(1-2*s)

# 1. stationarity, H, g, Tc
gradG = [sp.diff(G, xi) for xi in X]
print('grad A at x*:', [sp.simplify(sp.diff(A, xi).subs(sub)) for xi in X])
print('C1,C2 at x*:', sp.simplify(C1.subs(sub)), sp.simplify(C2.subs(sub)))
H = sp.Matrix(10, 10, lambda i, j: sp.simplify(sp.diff(A, X[i], X[j]).subs(sub)))
g = sp.Matrix([sp.simplify(sp.diff(Dl, xi).subs(sub)) for xi in X])
print('g =', list(g))
print('H leading minors all > 0:', all(H[:k, :k].det() > 0 for k in range(1, 11)))
Hig = H.LUsolve(g)
print('H^-1 g * 5059 =', list(Hig*5059))
Tc = (g.T*Hig)[0]/4
print('Tc =', Tc, ' equals text 3269/10118:', Tc == R(3269, 10118))
hs = sp.expand(sp.series(hfun, s, 0, 7).removeO())
print('h series:', hs)

# 2. Lyapunov-Schmidt by series substitution (independent of the tensor formula)
p = -Hig
c2 = sp.Matrix(sp.symbols('q0:10'))
c3 = sp.Matrix(sp.symbols('w0:10'))
Xs = [xs[i] + p[i]*s + c2[i]*s**2 + c3[i]*s**3 for i in range(10)]
subs_s = dict(zip(X, Xs))
res = [sp.expand(sp.series(e.subs(subs_s), s, 0, 4).removeO()) for e in gradG]
print('order-0,1 residuals (should be 0):', [sp.simplify(r.coeff(s, 0)) for r in res], [sp.simplify(r.coeff(s, 1)) for r in res])
sol2 = sp.solve([r.coeff(s, 2) for r in res], list(c2), dict=True)[0]
sol3 = sp.solve([sp.expand(r.coeff(s, 3).subs(sol2)) for r in res], list(c3), dict=True)[0]
Gs = sp.expand(sp.series(G.subs(subs_s), s, 0, 5).removeO().subs(sol2).subs(sol3))
T = sp.Symbol('T')
Phi = sp.expand(Gs + T*hs)
print('Phi coeff s^1, s^3:', sp.simplify(Phi.coeff(s, 1)), sp.simplify(Phi.coeff(s, 3)))
print('Phi coeff s^2 =', sp.factor(sp.simplify(Phi.coeff(s, 2))))
Phissss = sp.simplify(24*Phi.coeff(s, 4).subs(T, Tc))
c = Phissss/6
print('Phi_ssss(0,Tc) =', Phissss, '=', sp.N(Phissss, 30))
print('c =', c, '=', sp.N(c, 30))
print('c == text value -657534393590529472/6223404588394626861:', c == R(-657534393590529472, 6223404588394626861))
# negative control: straight-line restriction (omits stable response)
Gline = sp.expand(sp.series(G.subs(dict(zip(X, [xs[i]+p[i]*s for i in range(10)]))), s, 0, 5).removeO())
line4 = sp.simplify(24*Gline.coeff(s, 4) + 24*Tc*hs.coeff(s, 4))
print('straight-line Phi_ssss =', line4, '=', sp.N(line4, 20), ' equals text:', line4 == R(6368971071507328, 655026269697361))
print('32 Tc =', 32*Tc, sp.N(32*Tc, 20), '; 24*h4 coefficient =', 24*hs.coeff(s, 4))
resp = sp.simplify(line4 - Phissss)
print('response 3 k^T H^-1 k =', resp, sp.N(resp, 20), ' equals text:', resp == R(21485600170644766720, 2074468196131542287))
print('relative excess (resp-32Tc)/32Tc =', sp.N((resp-32*Tc)/(32*Tc), 10))
# tensor-formula components
lin = dict(zip(X, [xs[i]+p[i]*eps for i in range(10)]))
A4 = sp.simplify(sp.diff(A.subs(lin), eps, 4).subs(eps, 0))
D3 = sp.simplify(sp.diff(Dl.subs(lin), eps, 3).subs(eps, 0))
print('A4[p^4] =', A4, ' equals text:', A4 == R(236914859731152, 655026269697361))
print('D3[p^3] =', D3, ' equals text:', D3 == R(-31633266640, 129477420379))
A3pp = sp.Matrix([sp.simplify(sp.diff(sp.diff(A, xi).subs(lin), eps, 2).subs(eps, 0)) for xi in X])
D2p = sp.Matrix([sp.simplify(sp.diff(sp.diff(Dl, xi).subs(lin), eps, 1).subs(eps, 0)) for xi in X])
k = A3pp + 2*D2p
kHk = (k.T*H.LUsolve(k))[0]
print('3 k^T H^-1 k (tensor) equals series response:', 3*kHk == resp)
print('formula A4+4D3-3kHk+32Tc == 6c:', A4 + 4*D3 - 3*kHk + 32*Tc == 6*c)

# 3. metric length D
Mdiag = [X[i+5] if i < 5 else 2*X[i]**2 for i in range(10)]   # diag(v0,v1,v2,V1,V2, 2v0^2,...,2V2^2)
Mstar = sp.diag(*[sp.sympify(m).subs(sub) for m in Mdiag])
Dlen = (p.T*Mstar.inv()*p)[0]
print('D =', Dlen, ' equals text:', Dlen == R(19189456, 25593481))


# 4. center-manifold cubic via eigen-projection on the actual flows at Tc
def cm_cubic(F, Z, z0, scoord):
    sz = dict(zip(Z, z0))
    n = len(Z)
    J = sp.Matrix(n, n, lambda i, j: sp.simplify(sp.diff(F[i], Z[j]).subs(sz)))
    r = J.nullspace()
    assert len(r) == 1
    r = r[0]
    l = J.T.nullspace()
    assert len(l) == 1
    l = l[0]

    def dd(vec, order):
        line = dict(zip(Z, [z0[i] + vec[i]*eps for i in range(n)]))
        return sp.Matrix([sp.simplify(sp.diff(Fi.subs(line), eps, order).subs(eps, 0)) for Fi in F])
    F2rr = dd(r, 2)
    print('  l^T F2[r,r] (should be 0):', sp.simplify((l.T*F2rr)[0]))
    Aug = J.col_join(l.T)
    rhs = (-F2rr/2).col_join(sp.Matrix([0]))
    q = (Aug.T*Aug).LUsolve(Aug.T*rhs)
    assert sp.simplify(J*q + F2rr/2) == sp.zeros(n, 1)
    F2rq = (dd(r+q, 2) - F2rr - dd(q, 2))/2
    F3 = dd(r, 3)
    eta_a = sp.simplify((l.T*(F2rq + F3/6))[0] / (l.T*r)[0])
    line = dict(zip(Z, [z0[i] + r[i]*eps for i in range(n)]))
    sig = sp.simplify(sp.diff(scoord.subs(line), eps).subs(eps, 0))
    ev = sorted([sp.N(e, 8) for e in J.eigenvals(multiple=True)], key=lambda z: sp.re(z))
    print('  Jacobian eigenvalues at Tc:', ev)
    return sp.simplify(eta_a/sig**2)


Ered = A - Tc*sp.log(sp.cosh(Dl/(2*Tc)))
Fred = list(-(sp.diag(*Mdiag)*sp.Matrix([sp.diff(Ered, xi) for xi in X])))
sstar = -sp.tanh(Dl/(2*Tc))/2
eta_red = cm_cubic(Fred, X, xs, sstar)
print('Gibbs: center cubic =', eta_red, ' equals -c/D:', sp.simplify(eta_red + c/Dlen) == 0)
Z = X + [b]
Efull = (A - (C1+C2)/2) + b*C1 + (1-b)*C2 + Tc*(b*sp.log(2*b) + (1-b)*sp.log(2*(1-b)))
Mf = sp.diag(*(Mdiag + [b*(1-b)]))
Ffull = list(-(Mf*sp.Matrix([sp.diff(Efull, zi) for zi in Z])))
eta_full = cm_cubic(Ffull, Z, xs + [R(1, 2)], b - R(1, 2))
print('Full: center cubic =', eta_full, ' equals -c/(D+4):', sp.simplify(eta_full + c/(Dlen+4)) == 0)
print('signs (c, Gibbs cubic, full cubic):', sp.sign(c), sp.sign(eta_red), sp.sign(eta_full))
