"""L04: attention-row identities for PIFB2 516-734, 831-871, 2212-2515.

Checks (symbolic where possible, float64 otherwise):
 1. KKT stationarity of sum_j b_j E_j + tau sum_j b_j log(b_j/pi_j) on the simplex -> softmax(-E/tau + log pi).
 2. Value at optimum = -tau log Z (Gibbs variational principle).
 3. Envelope: d/dx F(b*(x),x) = sum_j b*_j dE_j/dx.
 4. Surrogate: d/dx sum_j b*_j E_j = sum b dE - tau^{-1} Cov_b(E, dE); Appendix-A split
    sum b dE (1 - E/tau) + tau^{-1} <E> <dE> equals the same.
 5. Sender-row surrogate term (PIFB2 eq:sender_autograd) equals -tau^{-1} Cov over row l.
 6. dF_red/dtau = KL(b*||pi) >= 0  (F_red monotone in tau; F-minimization over tau collapses tau->0).
 7. Substituting b*(tau) into the tau=1 row (eq:mixture_energy_entropy) gives (1-1/tau)<E> - log Z, not -tau log Z.
 8. Hard limit tau->0: surrogate gradient -> dE_{argmin}; Appendix-A pieces individually diverge ~E_min/tau.
"""
import numpy as np
import sympy as sp

N = 3
x, tau = sp.symbols('x tau', positive=True)
lam = sp.symbols('lam')
b = sp.symbols('b0:%d' % N, positive=True)
pi = sp.symbols('p0:%d' % N, positive=True)
# generic smooth energies of a scalar state x
E = [sp.Function('E%d' % j)(x) for j in range(N)]

# 1. KKT
L = sum(b[j]*E[j] + tau*b[j]*sp.log(b[j]/pi[j]) for j in range(N)) - lam*(sum(b) - 1)
sol = [sp.solve(sp.diff(L, b[j]), b[j])[0] for j in range(N)]
Zs = sum(pi[j]*sp.exp(-E[j]/tau) for j in range(N))
bstar = [pi[j]*sp.exp(-E[j]/tau)/Zs for j in range(N)]
# ratio test: sol_j / sol_k should equal bstar_j / bstar_k (lambda cancels)
r1 = sp.simplify(sol[0]/sol[1] - bstar[0]/bstar[1])
print('1. KKT ratio residual (symbolic):', r1)

# 2. value
Fval = sum(bstar[j]*E[j] + tau*bstar[j]*sp.log(bstar[j]/pi[j]) for j in range(N))
r2 = sp.simplify(sp.expand_log(Fval + tau*sp.log(Zs), force=True))
print('2. F(b*) + tau log Z residual (symbolic):', r2)

# 3. envelope
Fred = -tau*sp.log(Zs)
r3 = sp.simplify(sp.diff(Fred, x) - sum(bstar[j]*sp.diff(E[j], x) for j in range(N)))
print('3. envelope residual (symbolic):', r3)

# 4. surrogate
S = sum(bstar[j]*E[j] for j in range(N))
dE = [sp.diff(E[j], x) for j in range(N)]
mE = sum(bstar[j]*E[j] for j in range(N)); mdE = sum(bstar[j]*dE[j] for j in range(N))
cov = sum(bstar[j]*E[j]*dE[j] for j in range(N)) - mE*mdE
r4 = sp.simplify(sp.diff(S, x) - (mdE - cov/tau))
split = sum(bstar[j]*dE[j]*(1 - E[j]/tau) for j in range(N)) + mE*mdE/tau
r4b = sp.simplify(split - (mdE - cov/tau))
print('4. surrogate = mean - Cov/tau residual:', r4, '; Appendix-A split residual:', r4b)

# 7. tau=1 form evaluated at b*(tau)
F1 = sum(bstar[j]*(E[j] + sp.log(bstar[j]) - sp.log(pi[j])) for j in range(N))
r7 = sp.simplify(sp.expand_log(F1 - ((1 - 1/tau)*mE - sp.log(Zs)), force=True))
print('7. tau=1 row at b*(tau) minus [(1-1/tau)<E> - log Z]:', r7)

# numerics with concrete energies
rng = np.random.default_rng(0)
def row(Ev, piv, t):
    w = piv*np.exp(-(Ev - Ev.min())/t); return w/w.sum()
for trial in range(3):
    Ev = rng.uniform(0, 5, 5); piv = rng.dirichlet(np.ones(5)); t = rng.uniform(0.3, 3)
    bb = row(Ev, piv, t)
    Fv = bb@Ev + t*np.sum(bb*np.log(bb/piv)); Z = np.sum(piv*np.exp(-Ev/t))
    # 6. dF_red/dtau vs KL
    h = 1e-6
    Fr = lambda tt: -tt*np.log(np.sum(piv*np.exp(-Ev/tt)))
    dF = (Fr(t+h) - Fr(t-h))/(2*h); KL = np.sum(bb*np.log(bb/piv))
    F1v = bb@(Ev + np.log(bb) - np.log(piv))
    print(f'num trial {trial}: |F(b*)+tau logZ|={abs(Fv + t*np.log(Z)):.2e}; dFred/dtau={dF:.6f} KL(b*||pi)={KL:.6f} diff={abs(dF-KL):.2e}; '
          f'tau=1 form at b*(tau)={F1v:.4f} vs -tau logZ={-t*np.log(Z):.4f}')

# 5. sender row: row l energies, only E_li depends on x_i
El = rng.uniform(0, 4, 4); dEl = np.zeros(4); dEl[2] = 1.7; t = 0.8; bl = row(El, np.ones(4)/4, t)
fd = []
for s in (+1, -1):
    Ep = El + s*1e-6*dEl; bp = row(Ep, np.ones(4)/4, t); fd.append(bp@Ep)
fdv = (fd[0]-fd[1])/2e-6
formula = bl[2]*(1 - El[2]/t)*dEl[2] + (bl@El)*bl[2]*dEl[2]/t
covl = np.sum(bl*El*dEl) - (bl@El)*(bl@dEl)
print(f'5. sender row: FD={fdv:.9f} eq:sender_autograd={formula:.9f} b dE - Cov/tau={bl@dEl - covl/t:.9f}')

# 8. hard limit
Ev = np.array([1.0, 2.5, 4.0]); g = np.array([0.3, -1.0, 2.0])
for t in (1.0, 0.1, 0.02, 0.005):
    bb = row(Ev, np.ones(3)/3, t)
    cov = np.sum(bb*Ev*g) - (bb@Ev)*(bb@g)
    piece1 = np.sum(bb*g*(1 - Ev/t)); Rmu = (bb@Ev)*(bb@g)/t
    print(f'8. tau={t:6.3f} surrogate grad={bb@g - cov/t:+.6f} (dE_argmin={g[0]:+.3f}) piece1={piece1:+.3e} R_mu={Rmu:+.3e} Cov/tau={cov/t:+.3e}')
