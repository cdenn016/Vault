r"""L10: chart action of the global right translation U_i -> U_i g (PIFB2 2512).
log(e^phi e^{t xi}) - phi = t * (ad_phi / (1 - e^{-ad_phi}))(xi) + O(t^2) = t*(xi + 1/2[phi,xi] + 1/12[phi,[phi,xi]] + ...) + O(t^2).
The 1/2[phi,xi] term is first order in xi, so 'phi -> phi + xi to first order in xi' holds only when phi is also small.
"""
import numpy as np
from scipy.linalg import expm, logm
rng = np.random.default_rng(4)
xi = rng.standard_normal((3, 3)); xi /= np.linalg.norm(xi)
for sphi in (0.01, 0.1, 0.5, 1.0):
    phi = rng.standard_normal((3, 3)); phi *= sphi / np.linalg.norm(phi)
    t = 1e-6
    lin = (np.real(logm(expm(phi) @ expm(t * xi))) - np.real(logm(expm(phi) @ expm(-t * xi)))) / (2 * t)
    c = phi @ xi - xi @ phi; pred = xi + 0.5 * c + (phi @ c - c @ phi) / 12
    print(f"|phi|_F={sphi:4.2f}: first-order-in-xi shift vs xi: rel diff {np.linalg.norm(lin - xi):.3e}; vs xi+1/2[phi,xi]+1/12[phi,[phi,xi]]: {np.linalg.norm(lin - pred):.2e}")
