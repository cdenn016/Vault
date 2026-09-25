"""L04: PIFB2 694-711 (absorbed presence), 885-918 (environmental agents), 922-927 (symmetry breaking).
A. Absorbed prior pi~_ij = chi_i chi_j pi_ij / sum_k chi_i chi_k pi_ik: chi_i cancels, so the receiver row
   carries full weight where chi_i -> 0; with hard chi_i = 0 it is 0/0. Compare with explicit chi_i-weighted row.
B. Env agent: Gaussian sensor, identity readout. FD gradients of KL(q||q_e), cross-entropy, Gaussian NLL.
   Nonlinear readout o = tanh(w.k)+noise: mean gradient of E_q[-log p(o|k)] is not affine in mu -> no Gaussian q_e matches it.
C. Symmetry: F = sum KL(q_i||p_i) + alignment rows + obs term with fixed likelihood.
   (a) right action U_i -> U_i g (all i incl. parent): F invariant with or without obs term.
   (b) diagonal left action U_i -> h U_i, q_i -> h q_i, parent too: alignment+prior invariant, obs term changes.
"""
import numpy as np
from scipy.linalg import expm
rng = np.random.default_rng(3); K = 2
def spd(): M = rng.normal(size=(K, K)); return M@M.T + 0.5*np.eye(K)
def kl(m0, S0, m1, S1):
    S1i = np.linalg.inv(S1); d = m1 - m0
    return 0.5*(np.trace(S1i@S0) + d@S1i@d - K + np.log(np.linalg.det(S1)/np.linalg.det(S0)))
# ---- A
E = np.array([0.4, 1.3, 2.2]); pi = np.ones(3)/3; tau = 1.0; chi_j = np.array([1.0, 0.8, 0.5])
for chi_i in (1.0, 0.1, 1e-6):
    w = chi_i*chi_j*pi; pt = w/w.sum()
    bstar = pt*np.exp(-E/tau); bstar /= bstar.sum()
    absorbed = bstar@E + tau*np.sum(bstar*np.log(bstar/pt))
    print(f'A. chi_i={chi_i:g}: absorbed-row value={absorbed:.6f} (independent of chi_i); receiver-weighted chi_i*row={chi_i*absorbed:.6f}')
# ---- B
mu = rng.normal(size=K); S = spd(); m = rng.normal(size=K); So = spd(); Lo = np.linalg.inv(So)
def nll(mu, S):  # E_q[-log N(o; k, So)], o=m
    d = mu - m; return 0.5*(d@Lo@d + np.trace(Lo@S) + np.log(np.linalg.det(2*np.pi*So)))
def xent(mu, S):  # -E_q log N(k; m, So)
    return nll(mu, S)
def klf(mu, S): return kl(mu, S, m, So)
def gmu(f, mu, S, h=1e-6):
    return np.array([(f(mu + h*e, S) - f(mu - h*e, S))/(2*h) for e in np.eye(K)])
def gS(f, mu, S, h=1e-6):
    G = np.zeros((K, K))
    for a in range(K):
        for c in range(K):
            E_ = np.zeros((K, K)); E_[a, c] = h
            G[a, c] = (f(mu, S + E_) - f(mu, S - E_))/(2*h)
    return G
print('B. |dmu KL - dmu NLL| =', np.abs(gmu(klf, mu, S) - gmu(nll, mu, S)).max())
print('   |dSigma KL - (1/2)(Lo - S^-1)| =', np.abs(gS(klf, mu, S) - 0.5*(Lo - np.linalg.inv(S))).max(),
      '; |dSigma NLL - Lo/2| =', np.abs(gS(nll, mu, S) - 0.5*Lo).max(),
      '; |xent - (KL + H)| =', abs(xent(mu, S) - (klf(mu, S) + 0.5*np.log(np.linalg.det(2*np.pi*np.e*S)))))
# nonlinear readout, 1D latent for clarity
xg, wg = np.polynomial.hermite_e.hermegauss(80); wg = wg/wg.sum()
o, s_o, s_q = 0.3, 0.2, 0.25
def nll1(mu):
    k = mu + s_q*xg; return np.sum(wg*0.5*(o - np.tanh(2*k))**2/s_o**2)
mus = np.linspace(-1.5, 1.5, 7)
grads = np.array([(nll1(u + 1e-6) - nll1(u - 1e-6))/2e-6 for u in mus])
lin = np.polyfit(mus, grads, 1); res = grads - np.polyval(lin, mus)
print('   nonlinear readout: d/dmu E_q[-log p(o|k)] at mu grid =', np.round(grads, 4), '; max residual from best affine fit =', f'{np.abs(res).max():.3f}')
# ---- C
N = 3
U = [expm(0.5*rng.normal(size=(K, K))) for _ in range(N)]; UI = expm(0.5*rng.normal(size=(K, K)))
q = [(rng.normal(size=K), spd()) for _ in range(N)]; qI = (rng.normal(size=K), spd())
o = rng.normal(size=K); Lobs = np.linalg.inv(spd())
def push(M, g): return (M@g[0], M@g[1]@M.T)
def F(U, q, UI, qI, obs=True, tau=1.0):
    tot = 0.0
    for i in range(N):
        p_i = push(U[i]@np.linalg.inv(UI), qI)           # cross-scale shadow prior
        tot += kl(*q[i], *p_i)
        Ei = np.array([kl(*q[i], *push(U[i]@np.linalg.inv(U[j]), q[j])) for j in range(N) if j != i])
        tot += -tau*np.log(np.mean(np.exp(-Ei/tau)))       # reduced row, uniform prior
        if obs:
            d = q[i][0] - o; tot += 0.5*(d@Lobs@d + np.trace(Lobs@q[i][1]))   # fixed Gaussian likelihood, identity readout
    return tot
g = expm(0.7*rng.normal(size=(K, K))); h = expm(0.7*rng.normal(size=(K, K)))
F0 = F(U, q, UI, qI); F0n = F(U, q, UI, qI, obs=False)
Fa = F([Ui@g for Ui in U], q, UI@g, qI)
Fb = F([h@Ui for Ui in U], [push(h, qi) for qi in q], h@UI, push(h, qI))
Fbn = F([h@Ui for Ui in U], [push(h, qi) for qi in q], h@UI, push(h, qI), obs=False)
print(f'C. right action U->Ug, with obs term: |dF|={abs(Fa-F0):.2e}')
print(f'   diagonal left action (U,q)->(hU,hq): without obs |dF|={abs(Fbn-F0n):.2e}; with fixed obs likelihood |dF|={abs(Fb-F0):.3f}')
