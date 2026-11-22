r"""Deciding script 3b: worst single-round attention configuration for the closure defect, and the reverse-direction
inference KL.  Declared expectations: the largest per-step d_cl over all 256 single-round relay-count vectors
(m_1..m_4) in {0..3}^4, entered from the stationary symmetric state, is attained at a maximally unequal vector and
is below 1e-2 nats; the reverse-direction best-constant KL is below the forward one."""
import itertools
import numpy as np
from lib import Pminus, posterior, simulate_policy_path, Path
from instance import PAR, T, BURN
import run_closure as rc

base = simulate_policy_path(PAR, 200, np.random.default_rng(11), "full")
best, worst = 0.0, None
for mv in itertools.product(range(4), repeat=4):
    mates = []
    for t in range(200):
        row = []
        for i in range(4):
            full = tuple(j for j in range(4) if j != i)
            row.append(full[:mv[i]] if t == 150 else full)
        mates.append(row)
    p = np.full(4, 0.09); Pm = np.zeros((200, 4, 2, 2))
    for t in range(200):
        for i in range(4):
            Pm[t, i] = Pminus(PAR, p[i])
            p[i] = posterior(Pm[t, i], 1 / PAR.R + base.vis[t, i] / PAR.Rs, len(mates[t][i]) / (PAR.R + PAR.Rc))[0, 0]
    dc = rc.closure_defects(Path(Pm, mates, base.slots, base.vis, 0))
    if dc.max() > best:
        best, worst = dc.max(), mv
print(f"worst single-round relay-count vector {worst}: max d_cl {best:.3e}")
rng = np.random.default_rng(7002)
D2, Ps = [], []
for k in range(40):
    pth = simulate_policy_path(PAR, T, rng, "full")
    for d2, pstar, pcl in rc.union_kl(pth, set(range(BURN, T, 4))):
        D2.append(d2); Ps.append(pstar)
D2, Ps = np.array(D2), np.array(Ps)
Pe = np.mean(Ps + D2)
print(f"reverse direction E KL(N(m*,P*) || N(ybar,P_enc)), best constant P_enc = {Pe:.5f}: "
      f"{0.5 * np.mean((Ps + D2) / Pe - 1 - np.log(Ps / Pe)):.5f} nats")
