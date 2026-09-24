r"""G4 checks (c) and (d): slow-manifold metric, fast rates, barycenter chart, entropic force, calibration.

(c1) Linear two-timescale gradient flow  z' = -G^{-1} grad F,  F = 1/2 Y^T B Y + (1/2eps)(xi - C Y)^T A (xi - C Y).
     Exact slow invariant subspace xi = S_eps Y; compare with C; identity
     G_slow(D) - G_quot = (D - C*)^T G_xixi (D - C*),  C* = -G_xixi^{-1} G_xiY  (eq:rg_slow_graph_metric, 3704-3712);
     slow eigenvalues vs eig(G_slow(C)^{-1} B) and eig(G_quot^{-1} B);
     fast rates vs eig(A N G^{-1} N^T) (N = [-C, I]) and vs eig(G_xixi^{-1} A).
(c2) Barycenter chart: children x_i in R, metric diag(g), x = Y 1 + xi, w^T xi = 0.
     G_slow = sum g_i, G_quot = 1/sum(w_i^2/g_i); equal iff w propto g. Fast flow conserves g^T x, not w^T x.
(d1) Entropic-force counterexample to ||R_cl|| <= delta_{I,1} (eq:rg_schur_flow, 3715-3719) at T_cfg > 0.
(d2) Calibrated residual: delta_{I,0}^quot <= delta_{I,0} <= 2 delta_{I,0}^quot (eq:rg_closure, 3651-3663).
"""
import numpy as np
from scipy.integrate import solve_ivp

rng = np.random.default_rng(7)
m, r = 2, 3
Mg = rng.normal(size=(m+r, m+r)); G = Mg @ Mg.T + 0.5*np.eye(m+r)
B = np.array([[1.0, 0.3], [0.3, 0.6]])
Ma = rng.normal(size=(r, r)); A = Ma @ Ma.T + np.eye(r)
C = rng.normal(size=(r, m))
GYY, GYx, GxY, Gxx = G[:m, :m], G[:m, m:], G[m:, :m], G[m:, m:]
Cstar = -np.linalg.solve(Gxx, GxY)
Gquot = GYY - GYx @ np.linalg.solve(Gxx, GxY)


def Gslow(D):
    return GYY + GYx @ D + D.T @ GxY + D.T @ Gxx @ D


print('(c1) identity G_slow(D) - G_quot - (D-C*)^T Gxx (D-C*):',
      np.abs(Gslow(C) - Gquot - (C - Cstar).T @ Gxx @ (C - Cstar)).max())
print('     min eig of G_slow(C) - G_quot (Loewner gap) =', np.linalg.eigvalsh(Gslow(C) - Gquot).min())
N = np.hstack([-C, np.eye(r)])
Ginv = np.linalg.inv(G)
fast_pred = np.sort(np.linalg.eigvals(A @ N @ Ginv @ N.T).real)
fast_naive = np.sort(np.linalg.eigvals(np.linalg.solve(Gxx, A)).real)
slow_graph = np.sort(np.linalg.eigvals(np.linalg.solve(Gslow(C), B)).real)
slow_quot = np.sort(np.linalg.eigvals(np.linalg.solve(Gquot, B)).real)
print('     eps   |S-C|     |S-C|/eps  slow exact            err(graph C)  err(quot)   eps*fast exact vs A N G^-1 N^T')
for eps in [1e-1, 1e-2, 1e-3, 1e-4]:
    H = np.block([[B + C.T @ A @ C/eps, -C.T @ A/eps], [-A @ C/eps, A/eps]])
    ev, V = np.linalg.eig(Ginv @ H)
    order = np.argsort(ev.real)
    ev, V = ev[order].real, V[:, order].real
    Vs = V[:, :m]
    S = Vs[m:, :] @ np.linalg.inv(Vs[:m, :])
    slow = np.sort(ev[:m]); fast = np.sort(ev[m:])*eps
    print(f'  {eps:7.0e} {np.linalg.norm(S-C):.3e} {np.linalg.norm(S-C)/eps:8.4f}  {slow}  '
          f'{np.abs(slow-slow_graph).max():.2e}    {np.abs(slow-slow_quot).max():.2e}   '
          f'{np.abs(fast-fast_pred).max():.2e}')
print('     fast rates (units 1/eps): A N G^-1 N^T ->', fast_pred, '  naive G_xixi^-1 A ->', fast_naive)
print('     G_xixi eigenvalues (automatically SPD):', np.linalg.eigvalsh(Gxx))

# (c2) barycenter chart
print('\n(c2) barycenter chart, n=4 children')
n = 4
g = np.array([1.0, 2.0, 0.5, 1.5])
for w in [g/g.sum(), np.ones(n)/n, np.array([0.7, 0.1, 0.1, 0.1])]:
    Q, _ = np.linalg.qr(np.column_stack([w, np.eye(n)])); Bb = Q[:, 1:]
    P = np.column_stack([np.ones(n), Bb])
    Gc = P.T @ np.diag(g) @ P
    gs = Gc[0, 0]
    gq = Gc[0, 0] - Gc[0, 1:] @ np.linalg.solve(Gc[1:, 1:], Gc[1:, 0])
    print(f'  w={np.round(w, 3)}: G_slow={gs:.6f}  G_quot={gq:.6f}  1/sum(w^2/g)={1/np.sum(w**2/g):.6f}')
Adj = np.ones((n, n)) - np.eye(n); L = np.diag(Adj.sum(1)) - Adj
x0 = np.array([1.0, -0.5, 2.0, 0.3])
sol = solve_ivp(lambda t, x: -np.linalg.solve(np.diag(g), L @ x), [0, 40], x0, rtol=1e-12, atol=1e-14)
w = np.array([0.7, 0.1, 0.1, 0.1])
print('  fast-flow endpoint (consensus) =', sol.y[:, -1].round(10))
print('  g-weighted mean of x0 =', g @ x0/g.sum(), '  w-barycenter of x0 =', w @ x0,
      '  uniform mean =', x0.mean())

# (d1) entropic force
print('\n(d1) entropic-force counterexample: F = b Y^2/2 + a0 exp(kY) xi^2/(2 eps)')
b, a0, k, T = 1.0, 1.0, 2.0, 0.1
print('  F_exact_{s+1}(Y) = b Y^2/2 + (T/2) log(a0 e^{kY}/eps) + const; grad = bY + Tk/2 =', f'bY + {T*k/2}')
for eps in [1e-2, 1e-3]:
    rhs = lambda t, z: [-(b*z[0] + 0.5*a0*k*np.exp(k*z[0])*z[1]**2/eps), -a0*np.exp(k*z[0])*z[1]/eps]
    s = solve_ivp(rhs, [0, 0.5], [1.0, 0.3], rtol=1e-11, atol=1e-13, method='LSODA', dense_output=True)
    t1 = 0.5
    Y, xi = s.sol(t1)
    Ydot = rhs(t1, [Y, xi])[0]
    print(f'  eps={eps:.0e}: Ydot={Ydot:.8f}  -bY={-b*Y:.8f}  -grad F_exact={-(b*Y + T*k/2):.8f}'
          f'  => R_cl = {Ydot + b*Y + T*k/2:.6f} with delta_I1 = 0')

# (d2) calibration bound
print('\n(d2) calibrated vs optimal-shift residual on random neighborhoods')
worst_lo, worst_hi = np.inf, 0.0
for trial in range(2000):
    npts = 200
    Fex = rng.normal(size=npts)*rng.uniform(0.1, 3)
    D = rng.normal(size=npts)*rng.uniform(0.01, 1) + rng.uniform(-2, 2)
    Tt = 10**rng.uniform(-2, 1)
    Fag = Fex - D
    cZ = Tt*(np.log(np.sum(np.exp(-(Fag - Fag.min())/Tt))) - Fag.min()/Tt
             - np.log(np.sum(np.exp(-(Fex - Fex.min())/Tt))) + Fex.min()/Tt)
    d0 = np.abs(D - cZ).max()
    dq = 0.5*(D.max() - D.min())
    worst_lo = min(worst_lo, d0/dq); worst_hi = max(worst_hi, d0/dq)
print(f'  ratio delta_I0/delta_I0^quot over 2000 trials: min={worst_lo:.6f} max={worst_hi:.6f} (theory [1,2])')

# (c3) which "gap" is the internal relaxation rate?
print('\n(c3) internal relaxation rates of x\' = -g^{-1} L x vs lambda_{I,w} (Euclidean fiber norm)')
import scipy.linalg as sla
Lk = np.diag((np.ones((n, n)) - np.eye(n)).sum(1)) - (np.ones((n, n)) - np.eye(n))
Lk[0, 1] = Lk[1, 0] = -3.0; Lk[0, 0] = 5.0; Lk[1, 1] = 5.0   # weighted K4
for gg in [np.ones(n), g]:
    rates = np.sort(sla.eigh(Lk, np.diag(gg), eigvals_only=True))
    for w in [np.ones(n)/n, np.array([0.97, 0.01, 0.01, 0.01]), gg/gg.sum()]:
        Q, _ = np.linalg.qr(np.column_stack([w, np.eye(n)])); Bb = Q[:, 1:]
        lw = np.linalg.eigvalsh(Bb.T @ Lk @ Bb)[0]
        # g-norm version: min xi^T L xi / xi^T diag(g) xi on w-perp
        lwg = sla.eigh(Bb.T @ Lk @ Bb, Bb.T @ np.diag(gg) @ Bb, eigvals_only=True)[0]
        print(f'  g={gg}  w={np.round(w, 3)}: slowest internal rate={rates[1]:.6f}  lambda_Iw={lw:.6f}'
              f'  g-norm constrained={lwg:.6f}')
