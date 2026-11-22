# Independent check of conj_coh_walls C4: submartingale drift, overshoot bounds, E[T_J] bound
import numpy as np, mpmath as mp
from scipy.special import erfc
mp.mp.dps = 40
phi = lambda b: mp.exp(-b*b/2)/mp.sqrt(2*mp.pi)
Pb  = lambda b: mp.erfc(b/mp.sqrt(2))/2
g1  = lambda b: phi(b) - b*Pb(b)
g2  = lambda b: (1+b*b)*Pb(b) - b*phi(b)
def H(b, two_alpha): return two_alpha*g1(b) - g2(b)
ta = mp.sqrt(mp.pi/2)
# check g1,g2 against direct quadrature at 3 points
for b in (mp.mpf('0.3'), mp.mpf('1.7'), mp.mpf('4')):
    q1 = mp.quad(lambda z: (z-b)*phi(z), [b, mp.inf]); q2 = mp.quad(lambda z: (z-b)**2*phi(z), [b, mp.inf])
    assert abs(q1-g1(b)) < 1e-30 and abs(q2-g2(b)) < 1e-30
grid = [mp.mpf(k)/200 for k in range(1, 200*30+1)]
Hmin = min(H(b, ta) for b in grid); 
print("H(0) =", mp.nstr(H(mp.mpf(0), ta), 5), " min H on (0,30] grid step 0.005 =", mp.nstr(Hmin, 8), " (>0 required), argmin b =", mp.nstr(min(grid, key=lambda b: H(b, ta)), 6))
print("H'(0) = ", mp.nstr(mp.diff(lambda b: H(b, ta), 0, direction=1), 12), " vs (4-pi)/(2 sqrt(2pi)) =", mp.nstr((4-mp.pi)/(2*mp.sqrt(2*mp.pi)), 12))
# planted error: alpha 0.9 alpha*  -> H(0) < 0
print("planted 2alpha=0.9*sqrt(pi/2): H(0) =", mp.nstr(H(mp.mpf(0), 0.9*ta), 8), " min on grid =", mp.nstr(min(H(b, 0.9*ta) for b in grid[:400]), 8), "(negative => control fails as it should)")
# also smallest alpha that works? check slightly smaller alpha fails at b->0+: 
print("planted 2alpha=0.999*sqrt(pi/2): H(0) =", mp.nstr(H(mp.mpf(0), mp.mpf('0.999')*ta), 8))
# overshoot: mu1(a) < sqrt(2/pi), E O^2 = 1 - a mu1 < 1, mu1' = -Var
for a in (mp.mpf('0.01'), mp.mpf('0.5'), mp.mpf('2'), mp.mpf('6')):
    mu1 = phi(a)/Pb(a) - a
    m2 = mp.quad(lambda z: (z-a)**2*phi(z), [a, mp.inf])/Pb(a)
    dmu = mp.diff(lambda t: phi(t)/Pb(t) - t, a)
    print("a=%s mu1=%s (<%s) EO2=%s 1-a*mu1=%s  mu1'=%s  -Var=%s" % (a, mp.nstr(mu1,10), mp.nstr(mp.sqrt(2/mp.pi),10), mp.nstr(m2,10), mp.nstr(1-a*mu1,10), mp.nstr(dmu,10), mp.nstr(-(m2-mu1**2),10)))
# E[T_J] by own Nystrom (composite Gauss-Legendre panels of width <= 0.5, 12 nodes each), h=1
def ET(r, npan_per_unit=2, q=12):
    npan = max(2, int(np.ceil(r*npan_per_unit)))
    xs, ws = np.polynomial.legendre.leggauss(q)
    edges = np.linspace(0, r, npan+1)
    y = np.concatenate([(edges[k]+edges[k+1])/2 + (edges[k+1]-edges[k])/2*xs for k in range(npan)])
    w = np.concatenate([(edges[k+1]-edges[k])/2*ws for k in range(npan)])
    pts = np.concatenate([[0.0], y]); n = len(pts)
    K = np.zeros((n, n))
    K[:, 0] = 0.5*erfc(pts/np.sqrt(2))                      # reflect to 0: P(Z >= b)
    K[:, 1:] = np.exp(-0.5*(pts[:, None]-y[None, :])**2)/np.sqrt(2*np.pi)*w[None, :]
    return np.linalg.solve(np.eye(n)-K, np.ones(n))[0]
c = (np.pi+4)/np.sqrt(2*np.pi)
print("r   E[T] (2 panels/unit)  E[T] (4 panels/unit)   r^2   upper r^2+%.6f r+2   Siegmund (r+1.1652)^2   wrong-upper r^2+2r+2 ok?" % c)
for r in (0.5, 1, 2, 4, 8, 16, 32):
    a, b = ET(r), ET(r, 4)
    print("%-4s %.8f  %.8f  %8.2f  %10.4f  %10.4f   %s" % (r, a, b, r*r, r*r+c*r+2, (r+1.1652)**2, b <= r*r+2*r+2))
    assert r*r <= b <= r*r+c*r+2
# small Monte Carlo for r=1 as an independent channel on the integral equation itself
rng = np.random.default_rng(5); ts = []
for _ in range(40000):
    b = 0.0; t = 0
    while b < 1.0:
        b = max(0.0, b - rng.standard_normal()); t += 1
    ts.append(t)
ts = np.array(ts); print("MC r=1: %.4f +/- %.4f  (Nystrom %.4f)" % (ts.mean(), ts.std()/np.sqrt(len(ts)), ET(1, 4)))
