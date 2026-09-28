"""Independent numeric recheck of the Theorem S4.1 constants (verifier: Fable).

Model facts used (from c13/ca_formation_proofs):
  center path  e^{-K_M t} x_circ = e^{-Tt}(x_circ + n_c) - e^{-(8+T)t} n_c
  r_int(t) = -e^{-(8+T)t},  r_ext(t) = e^{-Tt}[-3/2 + e^{-8t}/2]
  residual covector norm sqrt3; common exterior residual c_g=(r^b+r^m)/2 norm sqrt2, annihilates Z_M
  z_+ = ((n+_e+n+_f)/sqrt2).y, covector norm 1, equals r_int on center
  D_e = (z_+ + z_1)^2 + z_2^2 ; z_1 ~ N(0,T/(8+T)), z_2 ~ N(0,T/(4+5T)) thermal
  MGF: E e^{(a+Z)^2/T} = (1-2s^2/T)^{-1/2} exp[a^2/(T(1-2s^2/T))]
"""
import math, json

eps = 1/100
T = eps**8
rho = 1/100
delta_eps = eps**2/(8*math.sqrt(3))
t_eps = 2*math.log(1/eps)
t_star = t_eps + 1

def gaps(theta_min, R_new):
    """Return (native gap crude, native gap sharp, parent gap) for t>=theta_min, Tt<=1/10,
    tube radius R = rho + delta_eps + R_new around sigma e^{-K_M t} x_circ."""
    R = rho + delta_eps + R_new
    r_int = math.exp(-(8+T)*theta_min)          # max |r_int| on window
    r_ext = math.exp(-0.1)*(1.5 - 0.5*math.exp(-8*theta_min))   # min |r_ext| on window
    # native, crude: each residual within sqrt3 R of center value
    D_int_crude = (r_int + math.sqrt(3)*R)**2
    D_ext_crude = (r_ext - math.sqrt(3)*R)**2
    # native, sharp: D = 2 z+^2 + z-^2 with orthonormal covectors
    D_int_sharp = (r_int + math.sqrt(2)*R)**2
    D_ext_sharp = (r_ext - math.sqrt(2)*R)**2   # = c_g^2 lower bound
    # parent: c_g^2 - (8+T)/(6+T) z_+^2 with |z_+| <= r_int + R
    fac = (8+T)/(6+T)
    c2 = (r_ext - math.sqrt(2)*R)**2
    zp2 = (r_int + R)**2
    g_par = c2 - fac*zp2
    return dict(R=R, r_int=r_int, r_ext=r_ext,
                g_nat_crude=D_ext_crude - D_int_crude,
                g_nat_sharp=D_ext_sharp - D_int_sharp,
                g_nat_mixed_ext_sharp=D_ext_sharp - D_int_crude,
                g_par=g_par)

out = {}
for name, th in [("theta>=1/4", 0.25), ("theta>=t_eps", t_eps)]:
    for tube, Rn in [("chebyshev", delta_eps), ("order-one 1/20", 0.05)]:
        out[f"{name} | {tube}"] = gaps(th, Rn)

# prefactor
pref = math.sqrt((8+T)/(6+T)) * math.sqrt((4+5*T)/(2+5*T))
out["parent MGF prefactor"] = dict(exact=pref, sqrt83=math.sqrt(8/3))
out["4(1+sqrt(8/3))"] = 4*(1+math.sqrt(8/3))
out["2*4(1+sqrt(8/3))"] = 8*(1+math.sqrt(8/3))

# prefix failure
ptilde_first = 73728*eps**4*t_star
Lam = lambda t, eL: 2*math.exp(eL*t) - 1
out["ptilde first term (eps=1/100)"] = ptilde_first
out["4 Lambda(t*) t* at eps_L=1 (log10 of value, before e^{-1/T})"] = math.log10(4*Lam(t_star,1.0)*t_star)
out["4 Lambda(t*) at eps_L=eps"] = 4*Lam(t_star, eps)
out["ptilde second term exponent -1/T"] = -1/T

# tube bounds
out["Chebyshev tube coeff check 384*192"] = 384*192
out["Gaussian tube exponent denominator 1600*24*2"] = 1600*24*2
h = 1.3e10
out["order-one tube at h=1.3e10"] = 24*math.exp(-1/(76800*T*h))
out["Chebyshev at h=1"] = 73728*eps**4
out["Gaussian at h=1 exponent"] = -1/(76800*T)

# rows at eps_L<=eps on [0,t*]
out["row range at eps_L=eps, t*"] = (math.exp(-eps*t_star)/2, 1-math.exp(-eps*t_star)/2)
lo = math.exp(-eps*t_star)/2; hi = 1-lo
out["mu(M) upper bound (ratio^4/(1+ratio^4))"] = (hi/lo)**4/(1+(hi/lo)**4)

# slow-ball mass of stationary retained Gaussian near center (8 order-one-variance dirs)
R0 = rho + delta_eps
# 6 dirs var 1, 2 dirs var 1/5, 1 fast dir var T/(8+T): mass <= vol8(R0)*max density over the 8 dirs
vol8 = math.pi**4/24 * R0**8
dens8 = (2*math.pi)**-3 * (5/(2*math.pi))   # (2pi)^{-3} for 6 unit-var dirs, (5/(2pi)) for 2 var-1/5 dirs
out["slow-ball mass estimate"] = vol8*dens8
out["author slow-ball (10/384) R0^8"] = 10/384*R0**8

print(json.dumps(out, indent=1))
