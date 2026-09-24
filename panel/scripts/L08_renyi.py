r"""L08: eq:renyi_diagonal_itfb (PIFB2 ~1281). Univariate check against quadrature of
D_alpha(q||p) = (alpha-1)^{-1} log \int q^alpha p^{1-alpha}; sigma denotes a variance."""
import numpy as np
from scipy.integrate import quad
def npdf(x, m, v): return np.exp(-(x-m)**2/(2*v))/np.sqrt(2*np.pi*v)
def closed(a, mq, vq, mp, vp):
    vt = (1-a)*vq + a*vp
    return 0.5*(a*(mp-mq)**2/vt + ((1-a)*np.log(vq) + a*np.log(vp) - np.log(vt))/(a-1))
for a, mq, vq, mp, vp in [(0.5, 0.3, 1.2, -0.4, 0.7), (0.8, 1.0, 0.5, 0.0, 2.0), (1.5, 0.2, 1.0, 0.5, 1.3)]:
    I = quad(lambda x: npdf(x, mq, vq)**a*npdf(x, mp, vp)**(1-a), -40, 40)[0]
    print(f"alpha={a}: closed={closed(a,mq,vq,mp,vp):.12f} quad={np.log(I)/(a-1):.12f}")
