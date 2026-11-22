r"""D1 deciding run 1: collective clause, baselines, regions, and the contrast nulls.

Declared expectations (before running), from x1/x2 exploration:
  exact deterministic-limit r(A) = 4.345 (pair reading each other, slots closed); MC of the actual stochastic policy
  within 3 SE of it; Pi^c diffusive with zero cross-niche block; other regions: spanning regions <= 1.
  mechanism medium (N=4, one random other per round, slots closed) = 2.493 exact, MC within 3 SE.
  mean-coupling baseline 1 + (4/3)(a/eps) = 3.23.  Window (3.23, 4.345] contains r0 = 3.5 under both readings.
  N_hab (gamma = 0, uniform habits: mate read 1/4 of rounds, slots open w.p. 1/2): about 1.06 (x2).
  N_pr (one channel of three redrawn every round, slots by EFE): about 1.75.
  N_lp / N_fr: beta = 0 exactly (exact solver with dead relays), MC within 3 SE of r = 1.
  Open-slot rate in the full model below 1e-6.
NEGATIVE CONTROLS (must fail): (i) Rc = 1e6 gives r(A) about 1 and an empty window; (ii) N_hab without slots
  (m = 0) and attention pinned on the mate must land near the full model (about 4.36), i.e. it would NOT differ,
  showing that the slot array, not attention, carries the N_hab separation in D1.
"""
import time
import numpy as np
from flib import (exact_sigma_c, compound, r_ab, mc, r_and_se, medium_exact, population_regions, is_diffusive,
                  steady_prior, member_policy_law)
from design import D1, GMAX, R0

t0 = time.time()
par = D1
n = par.n
print(f"D1: {par}\n  g_max (largest single-slot gain over reachable states) = {GMAX:.5f}, psi = {par.psi:.5f}")
Pm = steady_prior(par, 1, 0)
P, G = member_policy_law(par, Pm)
print(f"  member policy law at X*: P(type c=1) = {P[1].sum():.12f}, P(any slot open) = {1 - P[:, 0].sum():.3e}")
print(f"  EFE gaps: attention (c=0 vs c=1) {G[0,0]-G[1,0]:.5f} nats, slot (k=1 vs 0 at c=1) {G[1,1]-G[1,0]:.5f} nats")
att = ~np.eye(n, dtype=bool)
S, _, _ = exact_sigma_c(par, att, np.zeros(n, dtype=int))
al, be = compound(S)
rA = r_ab(n, al, be)
Pi, rin, rsp = population_regions(al, be, n, 2)
diff = is_diffusive(Pi)
print(f"(1) exact deterministic limit: alpha {al:.7f} beta {be:.7f} r(A) {rA:.6f}; diffusive {diff}; "
      f"coupling {-Pi[0,1]:.4f} leak {Pi.sum(1)[0]:.4f}; cross-niche entry {Pi[0,2]:.1e}")
print(f"    regions within a niche (size: max r) {rin}; regions spanning niches {rsp}")
o = mc(par, "full", K=2000, T=400, burn=80, seed=1001)
r, se, alm, bem = r_and_se(o, n)
print(f"(2) MC full model (stochastic policy, gamma=400): r(A) {r:.4f} +- {se:.4f} (z vs exact {(r-rA)/se:+.2f}); "
      f"open-slot rate {o.open_rate:.2e}; mean relays read {o.mean_c:.6f}  ({time.time()-t0:.0f}s)")
mal, mbe, rm = medium_exact(par, N=4, c=1)
med = par.with_(n=4, n_zero=0, types=((1, 3),))
om = mc(med, "full", K=1500, T=400, burn=80, seed=1002)
rmm, sem, _, _ = r_and_se(om, 4)
print(f"(3) mechanism medium: exact {rm:.6f}; MC (stochastic policy) {rmm:.4f} +- {sem:.4f} (z {(rmm-rm)/sem:+.2f}); "
      f"medium open-slot rate {om.open_rate:.2e}")
aeps = (rA - 1) / n
rmc = 1 + (2 * n * (n - 1) / (2 * n - 1)) * aeps
print(f"(4) mean-coupling baseline (clause (c), two disjoint pairs, a/eps = {aeps:.4f}): {rmc:.4f}; "
      f"window mechanism ({rm:.4f}, {rA:.4f}], mean coupling ({rmc:.4f}, {rA:.4f}]; r0 = {R0}")
oh = mc(par, "hab", K=2000, T=400, burn=80, seed=1003)
rh, seh, _, _ = r_and_se(oh, n)
print(f"(5) N_hab: {rh:.4f} +- {seh:.4f}; slot open rate {oh.open_rate:.3f}; mean relays {oh.mean_c:.3f}  "
      f"({time.time()-t0:.0f}s)")
op = mc(par, "pr", K=2000, T=400, burn=80, seed=1004, r_att=1)
rp, sep, _, _ = r_and_se(op, n)
print(f"(6) N_pr (redrawn every round): {rp:.4f} +- {sep:.4f}; mean informative relays {op.mean_c:.4f}; "
      f"open-slot rate {op.open_rate:.2e}")
Sd, _, _ = exact_sigma_c(par, att, np.zeros(n, dtype=int), dead=True)
ald, bed = compound(Sd)
ol = mc(par, "full", K=1500, T=400, burn=80, seed=1005, dead=True)
rl, sel, _, _ = r_and_se(ol, n)
print(f"(7) N_lp / N_rn / N_fr: exact beta {bed:.1e} (r = {r_ab(n, ald, bed):.6f}); MC dead relays {rl:.4f} +- {sel:.4f}")
# negative controls
pc = par.with_(Rc=1e6)
Sc, _, _ = exact_sigma_c(pc, att, np.zeros(n, dtype=int))
_, _, rmc6 = medium_exact(pc, N=4, c=1)
print(f"NEG (i) Rc = 1e6: r(A) {r_ab(n, *compound(Sc)):.5f}, medium {rmc6:.5f}  (window must be empty or degenerate)")
p0 = par.with_(m=0, types=((0, 1), (1, 1)))
on = mc(p0, "hab", K=1500, T=400, burn=80, seed=1006, att_law=np.array([0.0, 1.0]))
rn, sen, _, _ = r_and_se(on, n)
print(f"NEG (ii) N_hab with no slots and attention pinned on the mate: {rn:.4f} +- {sen:.4f} "
      f"(must be near {rA:.3f}, i.e. above r0)  ({time.time()-t0:.0f}s)")
print(f"total {time.time()-t0:.1f}s")
