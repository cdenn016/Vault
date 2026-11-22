r"""Declared design D1 (fixed before the deciding runs).

Population: two niches A = {1,2}, B = {3,4} (N = 4) with independent AR(1) world components
  (F = 0.9, Q = 0.05), own sensor R = 1 every round, raw relay of the own reading to every other agent with
  one-round latency and receiver-specific channel noise Rc = 0.1, exact filters on (eta_t, eta_{t-1}) with
  computation noise qc = 1e-4 I_2.
Attention: message capacity kappa_msg = 1 (one message channel per round among the 3 others); declared support
  = every message set of size <= 1 (canonical: {}, {mate}, {o1}, {o2}), uniform habits (|S| = 4).
Slots: m = 8 private binary world slots per member (o = eta_t + rho, Rs = 10 each; revised from Rs = 1 after
  d1_memory_worst showed a reachable all-slots-open deviation with d_cl = 0.20 at Rs = 1), read by the owner only and not
  relayed; uniform habits on {0,1}^8; cost psi per open slot, psi = g_max + 0.06 with g_max the largest single-slot
  information gain over the reachable states (c in {0,1}); slots are world channels of the attention set
  (def:fw-system, 02_framework.tex:13), so opening one is attention, not an act.
One policy precision gamma = 400.  EFE G = -I(x_{t+1}; own + k slots + c relays) + psi k.
Contrast coordinate: prior error of eta_t.  Selector: contrast at level r0.  Baseline: clause (c) mechanism
  medium (one world component, 4 agents of one type, same capacity, support closure, slots, gamma, psi).
Coarse variable: scalar collective average of the members' prior means of eta_t.
Agency class G2: belief a translate of the member's anticipated belief (variance v* of eta_{t+1} after own sensor
  and the relay), slot likelihood N(eta, Rs), cost psi, uniform habits held fixed (attention and slots),
  gamma_C in [0, inf); G1: v_C free.  Full-policy reading: the joint policy is (attention, slots).
Decision states: the stationary state X* of the full model (single state, weight 1).
"""
import numpy as np
from flib import Par, canonical_types, steady_prior, efe_grid


def make_design(m: int = 8, Rs: float = 10.0, margin: float = 0.06, types=None) -> Par:
    base = Par(F=0.9, Q=0.05, R=1.0, Rc=0.1, Rs=Rs, psi=0.0, gamma=400.0, qc=1e-4, n=2, n_zero=2, m=m,
               types=canonical_types(1, 2, 1) if types is None else types)
    gmax = 0.0
    for c in (0, 1):
        Pm = steady_prior(base, c, 0)
        for cc in (0, 1):
            G = efe_grid(base, Pm[0, 0], Pm[0, 1], Pm[1, 1], np.array([cc]), np.array([0, 1]))
            gmax = max(gmax, float(G[0, 0] - G[0, 1]))
    return base.with_(psi=gmax + margin), gmax


D1, GMAX = make_design()
R0 = 3.5
