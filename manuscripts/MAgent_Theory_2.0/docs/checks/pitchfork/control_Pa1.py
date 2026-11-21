"""Negative control: dictionary reference precision Pa (default 1) instead of 3/4; text claims c ~ +0.023, Tc ~ 0.319.
Uses the tensor formula Phi_ssss = A4[p^4] + 4 D3[p^3] - 3 k^T H^-1 k + 32 Tc (verified exactly equal to the
series LS computation in pitchfork_check.py), at 40-digit mpmath precision. Not interval validated.
Usage: python control_Pa1.py [Pa]
"""
import sys
import sympy as sp
import mpmath as mp
from pitchfork_check_defs import model, X, eps, R

mp.mp.dps = 40
Pa = sp.Rational(sys.argv[1]) if len(sys.argv) > 1 else sp.Integer(1)
A, Dl, C1, C2 = model(Pa)
# symmetric stationary point at s=0: mu0=0, mu2=-mu1, a2=-a1, v1=v2, V1=V2
m1, al, w0, w1, W = sp.symbols('m1 al w0 w1 W')
symsub = {X[0]: 0, X[1]: m1, X[2]: -m1, X[3]: al, X[4]: -al, X[5]: w0, X[6]: w1, X[7]: w1, X[8]: W, X[9]: W}
eqs = [sp.diff(A, X[i]).subs(symsub) for i in (1, 3, 5, 6, 8)]
sol = sp.nsolve(eqs, [m1, al, w0, w1, W], [-sp.Rational(4, 3), sp.Rational(1, 3), 1, 1, 1], prec=40)
vals = dict(zip([m1, al, w0, w1, W], list(sol)))
xs = [sp.sympify(symsub[x]).subs(vals) for x in X]
print('stationary point:', [sp.N(v, 12) for v in xs])
sub = dict(zip(X, xs))
print('max |grad A|:', max(abs(sp.N(sp.diff(A, x).subs(sub), 30)) for x in X))
H = sp.Matrix(10, 10, lambda i, j: sp.N(sp.diff(A, X[i], X[j]).subs(sub), 40))
g = sp.Matrix([sp.N(sp.diff(Dl, x).subs(sub), 40) for x in X])
Hig = H.LUsolve(g)
Tc = (g.T*Hig)[0]/4
p = -Hig
lin = dict(zip(X, [xs[i]+p[i]*eps for i in range(10)]))
A4 = sp.N(sp.diff(A.subs(lin), eps, 4).subs(eps, 0), 40)
D3 = sp.N(sp.diff(Dl.subs(lin), eps, 3).subs(eps, 0), 40)
A3pp = sp.Matrix([sp.N(sp.diff(sp.diff(A, x).subs(lin), eps, 2).subs(eps, 0), 40) for x in X])
D2p = sp.Matrix([sp.N(sp.diff(sp.diff(Dl, x).subs(lin), eps, 1).subs(eps, 0), 40) for x in X])
k = A3pp + 2*D2p
kHk = (k.T*H.LUsolve(k))[0]
c = (A4 + 4*D3 - 3*kHk + 32*Tc)/6
print('Pa =', Pa, ' Tc =', sp.N(Tc, 15), ' c =', sp.N(c, 15))
