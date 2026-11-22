r"""Deciding script 3c: per-step closure defect under sustained attention patterns (every relay-count vector
(m_1..m_4) in {0..3}^4 held from round 100 on, slots from the instance's symmetric law), and under a pattern
switched every round between the two most unequal vectors.  Declared expectation: the largest per-step d_cl over
these reachable policy paths is below 0.03 nats; equal vectors give exactly 0 (negative-control direction: unequal
vectors give a positive defect at every step)."""
import itertools
import numpy as np
from lib import Pminus, posterior, simulate_policy_path, Path
from instance import PAR
from run_closure import closure_defects

base = simulate_policy_path(PAR, 260, np.random.default_rng(13), "full")


def run(pattern_fn):
    mates = []
    for t in range(260):
        row = []
        mv = pattern_fn(t)
        for i in range(4):
            full = tuple(j for j in range(4) if j != i)
            row.append(full[:mv[i]])
        mates.append(row)
    p = np.full(4, 0.09); Pm = np.zeros((260, 4, 2, 2))
    for t in range(260):
        for i in range(4):
            Pm[t, i] = Pminus(PAR, p[i])
            p[i] = posterior(Pm[t, i], 1 / PAR.R + base.vis[t, i] / PAR.Rs, len(mates[t][i]) / (PAR.R + PAR.Rc))[0, 0]
    return closure_defects(Path(Pm, mates, base.slots, base.vis, 0))


best = (0, None); eq_max = 0.0
for mv in itertools.product(range(4), repeat=4):
    dc = run(lambda t, mv=mv: mv if t >= 100 else (3, 3, 3, 3))
    v = dc[120:].max()
    if len(set(mv)) == 1:
        eq_max = max(eq_max, v)
    if v > best[0]:
        best = (v, mv)
print(f"sustained patterns: largest per-step d_cl {best[0]:.4e} at {best[1]}; equal patterns max {eq_max:.1e}")
dc = run(lambda t: ((3, 0, 0, 0) if t % 2 else (0, 3, 3, 3)) if t >= 100 else (3, 3, 3, 3))
print(f"alternating (3,0,0,0)/(0,3,3,3): largest per-step d_cl {dc[120:].max():.4e}")
