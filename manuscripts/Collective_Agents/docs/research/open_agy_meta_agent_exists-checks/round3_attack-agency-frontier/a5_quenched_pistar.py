r"""Attack run a5: (1) N_pr drawn ONCE (tab:agy-nulls, 05_agency.tex:350, "once or every round"), exact law;
(2) D1's own threshold pi* under Theorem A's definition of rho ("slots follow the design's habits"), against the
slot-free pi* = 0.577 that the candidate's cap numbers use; (3) Theorem A's cap for D1-type designs.

(1) Quenched partner draw: each of the 4 receivers draws one partner uniformly from the 3 others, once.  Cross-niche
reads carry zero gain, so niche A is (c1, c2) in {0,1}^2 with P(c_i = 1) = 1/3 independently.  Each configuration is
a deterministic pattern: exact Sigma^c, diffusivity, contrasts; statistic S = r(A) (candidate's test) and
S = max over regions.  The mutual configuration IS the full model (same gains, same slots), so S = S_0 exactly.
Declared expectation: P(S >= S_0) = 1/9 (r(A)) or 17/81 (max over regions); with n_null = 999 the p-value is
about 0.11 or 0.21, far above alpha_pr = 0.01 -> D1 fails N_pr under the quenched variant.
NEGATIVE CONTROL: the 'none' configuration must be diagonal (r = 1); the mutual configuration must equal 4.345220.
(2) Declared expectation: rho_D1(1) about 2.775 (candidate's flooding number), so pi*_D1 lies between 0.577 and 1.
"""
import itertools
import time
import numpy as np
from mylib import Par, sigma_c_pattern, contrast, diffusive, all_regions, mc

t0 = time.time()
par = Par()
S0 = 4.345220
res = {}
for c1, c2 in itertools.product((0, 1), repeat=2):
    reads = [1 if c1 else None, 0 if c2 else None, 3, 2]       # niche B mutual (any B config is independent)
    Sc, _ = sigma_c_pattern(par, reads, [0, 0, 0, 0])
    Pi = np.linalg.inv(Sc)
    dif = diffusive(Pi[:2, :2])
    rA = contrast(Pi, (0, 1)) if dif[0] else float("nan")
    res[(c1, c2)] = (rA, dif, Sc[:2, :2])
    print(f"niche-A config (1 reads 2: {c1}, 2 reads 1: {c2}): Sigma_A {np.round(Sc[:2, :2], 6).tolist()}; "
          f"diffusive {dif[0]} (max off-diag of Pi {dif[1]:.3g}, min row sum {dif[2]:.3g}); r(A) {rA:.6f}")
S0 = res[(1, 1)][0]   # full model's exact statistic (the mutual configuration IS the full model)
print(f'S0 (full model, exact) = {S0:.12f}')
pc = {0: 2 / 3, 1: 1 / 3}
P_ge_A = sum(pc[a] * pc[b] for (a, b), v in res.items() if v[0] >= S0 - 1e-9)
P_ge_max = 1 - (1 - P_ge_A) ** 2
print(f"P(r(A) >= S0) = {P_ge_A:.6f} (1/9 = {1 / 9:.6f}); P(max region >= S0) = {P_ge_max:.6f} (17/81 = {17 / 81:.6f})")
from scipy.stats import binom
for P in (P_ge_A, P_ge_max):
    print(f"  n_null = 999: E[p] = {(1 + 999 * P) / 1000:.4f}; Pr(p <= 0.01) = Pr(Bin(999,{P:.4f}) <= 9) = "
          f"{binom.cdf(9, 999, P):.2e}")
print(f"({time.time() - t0:.1f}s)")
# (2) slot-inclusive rho for D1
b = 2.493156
rows = []
for pi in (0.577, 0.7, 0.8, 0.9, 0.95, 1.0):
    o = mc(par, "hab", B=2500, T=500, burn=150, seed=int(500 + 100 * pi), q_mate=(pi, pi))
    rows.append((pi, o["r"], o["se"]))
    print(f"rho_D1({pi}) = {o['r']:.4f} +- {o['se']:.4f}  ({time.time() - t0:.1f}s)")
o = mc(par.w(m=0), "hab", B=2500, T=500, burn=150, seed=577, q_mate=(0.577, 0.577))
print(f"slot-free rho(0.577) = {o['r']:.4f} +- {o['se']:.4f} (candidate: = b = {b})")
pis = np.array([r[0] for r in rows]); rh = np.array([r[1] for r in rows])
if rh[-1] <= b:
    pstar = 1.0
else:
    j = int(np.searchsorted(rh, b))
    pstar = pis[j - 1] + (pis[j] - pis[j - 1]) * (b - rh[j - 1]) / (rh[j] - rh[j - 1])
d = np.log(1 / pstar)
cap = 16 * np.log(2) / (16 * np.log(2) + 2 * d)
cap_q = 16 * np.log(2) / (16 * np.log(2) + 2 * np.log(1 / 0.577))
print(f"pi*_D1 (slot-inclusive) = {pstar:.3f}; Theorem A cap at m = 8 (delta -> 0): {cap:.4f} "
      f"(with the slot-free pi* 0.577: {cap_q:.4f}); D1's index 0.8000; D1's KL_a 2 ln 4 = {2 * np.log(4):.3f} vs "
      f"bound 2 d(1||pi*) = {2 * d:.3f}  ({time.time() - t0:.1f}s)")
