"""Verifier (Claude Fable 5.1) constant checks for ca_parent_early.tex."""
import math
from math import exp, log, sqrt, gamma, pi

eps = 1/100; T = eps**8; rho = 1/100; d = eps**2/(8*sqrt(3)); L = log(1/eps)
t_eps = 2*L; t_star = t_eps + 1; theta_c = 0.5*L + 1
print("delta_eps", d, "rho+delta", rho + d, "<0.010008:", rho + d < 0.010008)
# Lemma held-seed (iii)
print("(1-sqrt3 rho)^2/2 =", (1-sqrt(3)*rho)**2/2, ">0.48:", (1-sqrt(3)*rho)**2/2 > 0.48)
sel = exp(-2) + sqrt(3)*(rho + d)
print("e^-2+sqrt3(rho+d) =", sel, "<0.153:", sel < 0.153)
ext = exp(-1/12)*(1.5 - exp(-2)/2) - sqrt(3)*(rho + d)
print("exterior margin =", ext, ">1.3004:", ext > 1.3004)
c15 = eps**4 + sqrt(3)*rho*eps**2 + eps**2/8
print("selected at u>=L/2 over eps^2 =", c15/eps**2, "<0.15:", c15/eps**2 < 0.15)
# tube constants
print("384*192 =", 384*192, " 192*96 =", 192*96, " 2*18432 =", 2*18432, " 400*192 =", 400*192, " 663552/36864 =", 663552/36864)
# seeded-parent (a) numbers
n1 = 73728*eps**4*t_star
print("73728 eps^4 t* =", n1, "<0.008:", n1 < 0.008)
print("increasing eps^4(2log(1/eps)+1)? derivative sign at eps=1/100:",
      4*eps**3*(2*L+1) - 2*eps**3 > 0)
# fourth moment of xi
print("E|xi|^4 <= (3T/4)^2 + 2*3*(T/4)^2 = 15T^2/16 ->", (3/4)**2 + 6/16, "== 15/16:", abs((3/4)**2 + 6/16 - 15/16) < 1e-15)
print("8 rho^4 + 8*(15/16) T^2 <= 9 rho^4:", 8*rho**4 + 7.5*T**2 <= 9*rho**4)
# physical correction
print("4(rho+d)^2+2T =", 4*(rho+d)**2 + 2*T, "<1/2000:", 4*(rho+d)**2 + 2*T < 1/2000)
# E|X0|^4 identity check by symbolic reasoning: (m^2+12)^2+4m^2+24 <= (m^2+14)^2
for m2 in (0.0, 1.0, 10.0, 100.0):
    lhs = (m2+12)**2 + 4*m2 + 24; rhs = (m2+14)**2
    print(" m^2=", m2, "lhs<=rhs:", lhs <= rhs)
# c_12 and 0.1427
c12 = gamma(7)/(sqrt(pi)*gamma(13/2))
print("c_12 =", c12, "46080/(10395 pi) =", 46080/(10395*pi), ">1.411:", c12 > 1.411)
val = 2*c12/13*(15/16)**6.5
print("(15/16)^{13/2} =", (15/16)**6.5, " 2c12/13 (15/16)^{13/2} =", val, ">=0.1427:", val >= 0.1427)
# first-completion constants
r_flat = (1+sqrt(2)*rho)*exp(-6/5) + exp(-3/5) + 1/8
print("(1+sqrt2 rho)e^{-6/5}+e^{-3/5}+1/8 =", r_flat, "<0.98:", r_flat < 0.98)
print("L/4+23/20 <= L/2+1 at eps=1/100:", L/4 + 23/20 <= theta_c, " theta_c<=2/eps:", theta_c <= 2/eps)
print("theta_c - 1 = L/2 =", L/2, ">=1/4:", L/2 >= 0.25, " theta_c<=t*:", theta_c <= t_star)
k = 0.5*exp(-46/5)*0.1427*rho
print("1/2 e^{-46/5} 0.1427 rho =", k, ">7.2e-8:", k > 7.2e-8)
print("e^{-8 theta_c} = eps^4 e^{-8}:", abs(exp(-8*theta_c) - eps**4*exp(-8)) < 1e-30)
print("e^{-8(L/4+23/20)} = eps^2 e^{-46/5}:", abs(exp(-8*(L/4+23/20)) - eps**2*exp(-46/5)) < 1e-20)
p_star = 73728*eps**4*t_star + 4*(2*exp(t_star)-1)*(t_star-0.25)*exp(-1/T)
print("p_* (eps_L=1) =", p_star, "<1/100:", p_star < 0.01)
print("c(m0=x_circ) =", exp(-0.25)*rho**12/737280*exp(-rho**2/2))
# seeded-parent (b): rows ratio bound at eps_L=eps on [0,t*]
print("eps t* =", eps*t_star, "<0.1022:", eps*t_star < 0.1022)
lo = 0.5*exp(-eps*t_star); print("row interval at eps_L=eps:", lo, 1-lo, "inside [0.4489,0.5511]:", lo >= 0.4489 and 1-lo <= 0.5511)
print("(0.4489/0.5511)^4 =", (0.4489/0.5511)**4, ">0.44:", (0.4489/0.5511)**4 > 0.44)
# parent dynamics gaps
R = rho + d + 1/20
print("R =", R, "<0.0601:", R < 0.0601)
cg = exp(-0.1)*(1.5 - exp(-2)/2) - sqrt(2)*R
print("|c_g| >= ", cg, ">1.21:", cg > 1.21)
De = (exp(-2) + sqrt(2)*R)**2; De2 = 2*(exp(-2) + R)**2
print("D_e <= (e^-2+sqrt2 R)^2 =", De, "<= 2(e^-2+R)^2 =", De2, "<0.08:", De2 < 0.08)
print("(4/3)(e^-2+R)^2 =", 4/3*(exp(-2)+R)**2, "<= 2(e^-2+R)^2:", 4/3*(exp(-2)+R)**2 <= De2)
print("1.21^2 - 0.08 =", 1.21**2 - 0.08, ">1:", 1.21**2 - 0.08 > 1)
print("sqrt((8+T)/(6+T)) <= sqrt(4/3):", sqrt((8+T)/(6+T)) <= sqrt(4/3), " sqrt((4+5T)/(2+5T)) <= sqrt2:", sqrt((4+5*T)/(2+5*T)) <= sqrt(2))
print("8(1+sqrt(8/3))/10 =", 8*(1+sqrt(8/3))/10, "<=3:", 8*(1+sqrt(8/3))/10 <= 3)
# remark: slow-ball mass
R0 = rho + d
mass = 10/384*R0**8
print("10 R0^8/384 =", mass, "<3e-18:", mass < 3e-18, " 2*5*(2pi)^-4*pi^4/24 == 10/384:", abs(2*5*(2*pi)**-4*pi**4/24 - 10/384) < 1e-15)
# DV normalizer: E exp(z^2/(4 s^2)) for z~N(0,s^2) = (1-1/2)^{-1/2} = sqrt2; two coords -> 2
print("DV normalizer two coords:", (1-0.5)**-0.5 * (1-0.5)**-0.5)
# tilt normalizer and Pi second moment
print("E_Pi |z'|^2 = T[1/(8+T)+2/(4+T)] <= 5T/8:", T*(1/(8+T)+2/(4+T)) <= 5*T/8)
print("log((4+5T)/(4+T)) <= 4T/(4+T) <= T:", log((4+5*T)/(4+T)) <= 4*T/(4+T) <= T)
# (c) asymptotics: theta = L - s -> e^{-2(4+5T)theta}/T = e^{8s} e^{-10 T theta}
s = 1.3; th = L - s
print("identity e^{-2(4+5T)th}/T vs e^{8s}e^{-10T th}:", exp(-2*(4+5*T)*th)/T, exp(8*s)*exp(-10*T*th))
