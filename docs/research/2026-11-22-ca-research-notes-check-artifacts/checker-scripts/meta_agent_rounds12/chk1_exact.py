r"""Exact (rational/symbolic) checks of C1, C4 (Z3 cofactor), C5 (CE2, F-share), C6 (lazy ring).
Each block has a planted-error negative control."""
import itertools
import random

import sympy as sp
from sympy import Matrix, Rational as Q, eye, ones, simplify, symbols


def contrast_exact(Pi, C):
    """def:col-contrast for a diffusive Pi (sympy Matrix) and region C; xin from the pencil on 1^perp."""
    N = Pi.shape[0]
    n = len(C)
    eps = [sum(Pi[i, j] for j in range(N)) for i in range(N)]
    cut = sum(-Pi[i, k] for i in C for k in range(N) if k not in C)
    xout = sum(Pi[i, j] for i in C for j in C) / n
    assert simplify(xout - (sum(eps[i] for i in C) / n + cut / n)) == 0
    M = sp.zeros(n, n)
    for p, i in enumerate(C):
        M[p, p] = eps[i] + sum(-Pi[i, j] for j in C if j != i)
        for q_, j in enumerate(C):
            if j != i:
                M[p, q_] = Pi[i, j]
    B = sp.zeros(n, n - 1)
    for k in range(1, n):
        B[0, k - 1] = 1
        B[k, k - 1] = -1
    lam = symbols("lam")
    ev = sp.roots(sp.factor((B.T * M * B - lam * B.T * B).det()), lam)
    xin = min(ev.keys(), key=lambda z: sp.N(z))
    return xin / xout, xin, xout


print("== C1: exchangeable block alpha I + beta 11^T ==")
al, be = symbols("alpha beta", positive=True)
for n in (2, 3, 5):
    P = (al * eye(n) + be * ones(n, n)).inv()
    ok1 = simplify(P[0, 1] + be / (al * (al + n * be))) == 0
    ok2 = simplify(sum(P[0, j] for j in range(n)) - 1 / (al + n * be)) == 0
    print(f" n={n}: offdiag == -beta/(alpha(alpha+n beta)): {ok1}; row sum == 1/(alpha+n beta): {ok2}")
for a_, b_, n in [(Q(1), Q(1, 2), 4), (Q(3, 10), Q(2), 6), (Q(7, 5), Q(0), 3), (Q(2), Q(1, 100), 2)]:
    S = sp.zeros(n + 2, n + 2)
    S[:n, :n] = a_ * eye(n) + b_ * ones(n, n)
    S[n:, n:] = Matrix([[2, -1], [-1, 2]]).inv()
    r, xin, xout = contrast_exact(S.inv(), list(range(n)))
    print(f" alpha={a_}, beta={b_}, n={n}: r={r}; claim 1+n beta/alpha={1 + n * b_ / a_} equal={simplify(r - (1 + n * b_ / a_)) == 0};"
          f" planted wrong claim 1+beta/alpha equal={simplify(r - (1 + b_ / a_)) == 0}")
a_, b_, n = Q(1), Q(-1, 5), 4
P = (a_ * eye(n) + b_ * ones(n, n)).inv()
print(f" beta=-1/5 (> -alpha/n): offdiag = {P[0, 1]} (>0 expected), formula {-b_ / (a_ * (a_ + n * b_))}")
n, a, e = 4, Q(1), Q(1, 10)
N = 2 * n
abar = Q(2 * sp.binomial(n, 2), sp.binomial(N, 2)) * a
print(f" two cliques n=4,a=1,eps=1/10: clique r={1 + n * a / e}; baseline 1+N abar/eps={1 + N * abar / e}={float(1 + N * abar / e):.4f};"
      f" conventions-row formula {1 + Q(2 * n * (n - 1), 2 * n - 1) * a / e}")
rm = [(e + m * abar) / (e + (N - m) * abar) for m in range(2, N + 1)]
print("  exchangeable medium r(m) increasing in m:", all(rm[i] < rm[i + 1] for i in range(len(rm) - 1)), "; r(N) =", rm[-1])

print("== C4: Z3 cofactor identity and exact rational draws ==")
s11, s12, s13, s22, s23, s33 = symbols("s11 s12 s13 s22 s23 s33")
S3 = Matrix([[s11, s12, s13], [s12, s22, s23], [s13, s23, s33]])
print(" (S^-1)_13 det == s12 s23 - s13 s22:", simplify(S3.inv()[0, 2] * S3.det() - (s12 * s23 - s13 * s22)) == 0,
      "; planted (s12 s23 - s13 s11):", simplify(S3.inv()[0, 2] * S3.det() - (s12 * s23 - s13 * s11)) == 0)
random.seed(1)
viol = [0, 0, 0]
tot = 0
negrow = 0
for _ in range(120):
    n = random.choice([3, 4, 5])
    A = sp.zeros(n, n)
    for i in range(n):
        for j in range(i + 1, n):
            if random.random() < 0.6:
                A[i, j] = A[j, i] = -Q(random.randint(1, 9), 10)
    for i in range(n):
        A[i, i] = -sum(A[i, j] for j in range(n) if j != i) + Q(random.randint(-3, 9), 10)
    if not A.is_positive_definite:
        continue
    tot += 1
    negrow += any(sum(A[i, j] for j in range(n)) < 0 for i in range(n))
    S = A.inv()
    if min(S) < 0:
        viol[0] += 1
    for i, j, k in itertools.permutations(range(n), 3):
        if S[i, j] * S[j, k] > S[i, k] * S[j, j]:
            viol[1] += 1
            break
    for sub in itertools.combinations(range(n), 3):
        Pm = S.extract(list(sub), list(sub)).inv()
        if max(Pm[i, j] for i in range(3) for j in range(3) if i != j) > 0:
            viol[2] += 1
            break
print(f" exact rational PD Z-matrices: {tot} accepted, {negrow} with a negative row sum; violations Z1,Z3,Z4 = {viol}")
Pbad = Matrix([[2, Q(1, 2), 0], [Q(1, 2), 2, 0], [0, 0, 1]])
Sb = Pbad.inv()
print(" negative control (PD, one positive off-diagonal): min Sigma =", min(Sb), "-> Z1 fails:", min(Sb) < 0)

print("== C5: CE2 and F-share ==")
G = Matrix([[1, 0], [0, 1], [1, 1]])
S = eye(3) + G * G.T
print(" CE2 8*Pi =", (8 * S.inv()).tolist(), "; Sigma_12 =", S[0, 1])
Gm = Matrix([[1, 1, 0], [1, -1, 1], [0, 0, 1]])
Sm = eye(3) + Gm * Gm.T
print(" mixed-sign control: Sigma =", Sm.tolist(), "; max offdiag Pi =",
      max(Sm.inv()[i, j] for i in range(3) for j in range(3) if i != j))

print("== C6: lazy ring ==")
sig2, tau = symbols("sigma2 tau", positive=True)


def ring(n):
    W = sp.zeros(n, n)
    for i in range(n):
        W[i, i] = Q(1, 2)
        W[i, (i + 1) % n] += Q(1, 4)
        W[i, (i - 1) % n] += Q(1, 4)
    return W


W4 = ring(4)
P4 = (sig2 * W4 * W4.T + tau * eye(4)).inv()
claim = Q(1, 4) * (1 / (sig2 + tau) - 2 / (sig2 / 4 + tau) + 1 / tau)
print(" n=4: Pi_13 == closed form:", simplify(P4[0, 2] - claim) == 0, "; Pi_13 =", sp.factor(sp.together(P4[0, 2])))
print(" n=4: Pi_12 =", sp.factor(sp.together(P4[0, 1])), "; row sum =", simplify(sum(P4[0, j] for j in range(4))))
print(" n=4, sigma2=1: Pi_13 at tau=49/100, 1/2, 51/100:",
      [P4[0, 2].subs({sig2: 1, tau: t}) for t in (Q(49, 100), Q(1, 2), Q(51, 100))])
print(" planted wrong threshold tau<sigma2: Pi_13 at tau=3/4 =", P4[0, 2].subs({sig2: 1, tau: Q(3, 4)}), "(negative, so sigma2 is not the threshold)")
print(" kernel of W4^T:", [list(v) for v in W4.T.nullspace()])
for n in (5, 6, 7, 8):
    W = ring(n)
    WW = W * W.T
    Pn = (WW + Q(1, 1000) * eye(n)).inv()
    Pbig = (WW + 1000 * eye(n)).inv()
    mo = lambda P: max(P[0, j] for j in range(1, n))
    print(f" n={n}: (WW^T)_0d, d=0..{n // 2}: {[WW[0, d] for d in range(n // 2 + 1)]}; max offdiag Pi at tau=1e-3: {float(mo(Pn)):.4g}; at tau=1e3: {float(mo(Pbig)):.3e}")
n = 4
Wc = ones(n, n) / n
Pc = (sig2 * Wc * Wc.T + tau * eye(n)).inv()
print(" complete averaging: offdiag =", simplify(Pc[0, 1]), "(<=0); C1 with alpha=tau, beta=sigma2/n gives r=1+sigma2/tau")
p = Matrix([1, 2])
PK = eye(2) - p * p.T / 5
print(" scope control: W=pp^T/|p|^2, p=(1,2): P_K =", PK.tolist(), "is a Z-matrix although W is not uniform averaging;")
print("   W=diag(0,1,1): K=span(e_1), P_K=diag(1,0,0) is a Z-matrix. The 'exactly when' of C6 needs 1 perp K.")
