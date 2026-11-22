r"""Deciding script 4c: real-time (P4) with one coarse decision state (the stationary regime, symmetric rounds), and
with decision states (p-bin, current open count).  Declared expectation: the stationary marginal law of the open
count is closer to a group posterior than the p-binned laws (index in G1 above 0.95); the (p, current count) laws are
one-step kernels with support {n-1, n, n+1} and fit poorly (index below 0.9) -- reported, not a pass criterion."""
import numpy as np
from math import comb
from run_agency_real import collect, index, e2, hab_c, kl_counts
from lib import gibbs_law_sym, softmin_att, efe_table, Pminus, attention_weights
from instance import PAR
P, N, M0 = collect("full", 160000, 9201)
c = np.bincount(N, minlength=5) / len(N)
pm = float(np.median(P))
g = gibbs_law_sym(PAR.gamma, softmin_att(PAR, efe_table(PAR, Pminus(PAR, pm), 3, 4), attention_weights(PAR, 3, 4)), 4)
p11 = sum(c[k] * k * (k - 1) / 12 for k in range(5)); p10 = sum(c[k] * k * (4 - k) / 12 for k in range(5))
p00 = sum(c[k] * (4 - k) * (3 - k) / 12 for k in range(5))
print(f"stationary marginal law of the open count (n={len(N)}): {np.round(c, 4)}; Gibbs at median p {pm:.5f}: "
      f"{np.round(g, 4)}; KL(P||E) {kl_counts(c, hab_c):.5f}; log odds ratio {np.log(p11 * p00 / p10**2):.4f}")
for name, kw in (("G1", {}), ("G2 (v_C = E2 at median p)", {"vfix": [e2(pm)]})):
    A_, num, den, fit = index([c], **kw)
    print(f"  coarse decision state, {name}: index {A_:.5f} (min KL {num:.2e}, den {den:.5f}, fit {fit})")
# decision states (p-bin around the median, current count)
_, dec_counts = None, None
PP, NN, NC = [], [], []
from lib import simulate_policy_path_real
rng = np.random.default_rng(9202)
for k in range(20):
    _, dec = simulate_policy_path_real(PAR, 5000, rng, "full", record_dec=True)
    prev = None
    for t, pv, prof in dec[100:]:
        if prev is not None and np.ptp(pv) < 1e-12:
            PP.append(pv[0]); NN.append(int(prof.sum())); NC.append(prev)
        prev = int(prof.sum())
PP, NN, NC = map(np.array, (PP, NN, NC))
lo, hi = np.quantile(PP, [0.4, 0.6])
for n0 in range(5):
    sel = (PP >= lo) & (PP <= hi) & (NC == n0)
    if sel.sum() < 500:
        continue
    cc = np.bincount(NN[sel], minlength=5) / sel.sum()
    A_, num, den, fit = index([cc])
    print(f"  decision state (median p-bin, current count {n0}), n={sel.sum()}: law {np.round(cc, 3)}; G1 index {A_:.4f}")
