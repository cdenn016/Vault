r"""Diagnostic script: N_eff and N_inf under the alternative reading in which switching a slot open is an act.
Declared expectation: neither null lowers r(A) below the mechanism baseline 2.9386 (so under a strict typing in
which N_eff and N_inf are type D whenever members act, the construction would fail both); under the primary reading
the model has no acts and both nulls are inapplicable.
N_eff here: the slot switch path replaced by exogenous forcing with the law of the act path and added to the shared
drive, i.e. conditioned on; computed as E[Cov(e | eta, policy path)] (this also conditions on the attention path,
whose mixture contribution is below 1e-6 at I*).
N_inf here: intention announcements deliver noise; each member decides its slot alone; slots keep their effect."""
import numpy as np
from lib import sigma_c
from instance import PAR, T, BURN, EVERY, M, PROTO
full = sigma_c(PAR, M("full"), 40, T, BURN, EVERY, seed=611)
print(f"N_eff diagnostic (slot path conditioned): r(A) = {full['r_priv']:.4f} (full model {full['r']:.4f})")
inf = sigma_c(PAR, M("inf"), 40, T, BURN, EVERY, seed=612)
print(f"N_inf diagnostic (intentions deleted): r(A) = {inf['r']:.4f}, open rate {inf['open_rate']:.3f}")
