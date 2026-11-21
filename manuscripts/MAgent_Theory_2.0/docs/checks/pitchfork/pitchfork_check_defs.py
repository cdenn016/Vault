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


