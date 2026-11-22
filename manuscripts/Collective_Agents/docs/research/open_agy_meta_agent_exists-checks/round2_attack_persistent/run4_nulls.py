r"""Check 4: the decisive differ nulls and three reading variants, with my own code (T-real throughout).

Windows from run2 (mine): mechanism (2.9477, 4.4185], mean coupling (3.9302, 4.4185].
Declared expectations (before running):
  N_hab (gamma = 0, uniform habits): r(A) about 1.74 (constructor 1.7412), below both lower edges.
  N_pr (partners redrawn every round, 3 of 7 channels uniformly): about 1.89 (constructor 1.8858).
  N_lp (relays deliver pure noise of the assigned variance; attention, slots, precisions kept): about 1.05.
  Slot statuses as world states (replicas share the reviser clock and the slot path, so the world-conditional law
  conditions on them): r(A) about 4.41 (constructor's N_eff diagnostic 4.4094), mechanism medium about 2.94; window
  nonempty.
  Attention habits concentrated on the mates (attention then never departs from habits): the full model is
  unchanged (about 4.42), but N_hab then keeps the relays and draws slots at 1/2: r(A) about 3.8, ABOVE the lower
  edge 2.95 -> N_hab would select A for r0 in (2.95, r_hab] and the differ clause fails.  (This tests whether the
  attention departure that sinks the full-policy agency index can be removed without losing N_hab.)
  EFE target eta_{t+1} only: attention deviation rate about 2-3 percent per member-round (my hand estimate);
  r(A) somewhat lower, about 4.2-4.4; medium about 2.95; N_pr about 1.9; window nonempty.
  NEGATIVE CONTROL: the full model through this script's pipeline with a fresh seed must NOT differ (r(A) within
  0.05 of 4.42).
"""
import time
import itertools
import numpy as np
from core import Par, run, compound, r_ab, contrast

t0 = time.time()
PAR = Par()
MED = Par(n=8, n_inf=7, n_zero=0, nslots=8)
LO_M, HI = 2.9477, 4.4185
K, T, BURN = 2000, 400, 80


def rr(out, n):
    al, be = compound(out.S)
    ab = np.array([compound(s) for s in out.S_batches])
    nb = len(ab)
    loo = np.array([r_ab(n, (ab[:, 0].sum() - ab[k, 0]) / (nb - 1), (ab[:, 1].sum() - ab[k, 1]) / (nb - 1))
                    for k in range(nb)])
    return al, be, r_ab(n, al, be), np.sqrt((nb - 1) / nb * np.sum((loo - loo.mean()) ** 2))


def maxregion(al, be):
    SA = al * np.eye(4) + be
    S8 = np.zeros((8, 8)); S8[:4, :4] = SA; S8[4:, 4:] = SA
    Pi = np.linalg.inv(S8)
    off = Pi - np.diag(np.diag(Pi))
    vals = {C: contrast(Pi, C) for k in range(2, 9) for C in itertools.combinations(range(8), k)}
    C = max(vals, key=vals.get)
    return vals[C], C, bool(off.max() <= 1e-12 and Pi.sum(1).min() >= 0)


def show(name, out, n=4, lo=LO_M):
    al, be, r, se = rr(out, n)
    mr, C, dif = maxregion(al, be) if n == 4 else (r, None, None)
    print(f"{name}: alpha={al:.6f} beta={be:.3e} r={r:.4f} +/- {se:.4f}; open rate {out.open_rate:.3f}; "
          f"deviation rate {out.dev_rate:.3e}" + (f"; max region contrast {mr:.4f} at {C}, diffusive={dif}; "
          f"below lower edge {lo:.4f}: {mr < lo}" if n == 4 else "") + f"  ({time.time()-t0:.0f}s)", flush=True)
    return r


show("N_hab (uniform habits)", run(PAR, K, T, BURN, 4101, mode="hab"))
show("N_pr (every round)", run(PAR, K, T, BURN, 4102, mode="pr"))
show("N_lp (relays pure noise)", run(PAR, K, T, BURN, 4103, mode="full", dead_relays=True))
show("NEG full model, fresh seed", run(PAR, K, T, BURN, 4104, mode="full"))
# slot statuses as world states
rs = show("slots conditioned: population", run(PAR, K, T, BURN, 4105, mode="full", share_slots=True))
rsm = show("slots conditioned: mechanism medium", run(MED, 1200, T, BURN, 4106, mode="full", share_slots=True), n=8)
print(f"  window under the slots-as-world-states reading: ({rsm:.4f}, {rs:.4f}]")
# concentrated attention habits
show("mates habits: full model", run(PAR, K, T, BURN, 4107, mode="full", att_habit="mates"))
show("mates habits: N_hab (slots at 1/2, relays kept)", run(PAR, K, T, BURN, 4108, mode="hab", att_habit="mates"))
show("mates habits: mechanism medium", run(MED, 1200, T, BURN, 4109, mode="full", att_habit="mates"), n=8)
# EFE target eta_{t+1} only
PE = PAR.with_(target="eta")
re_ = show("target eta: population", run(PE, K, T, BURN, 4110, mode="full"))
rem = show("target eta: mechanism medium", run(MED.with_(target="eta"), 1200, T, BURN, 4111, mode="full"), n=8)
show("target eta: N_pr", run(PE, K, T, BURN, 4112, mode="pr"), lo=rem)
print(f"  window under the eta-target reading: ({rem:.4f}, {re_:.4f}]")
print(f"total {time.time()-t0:.1f}s")
