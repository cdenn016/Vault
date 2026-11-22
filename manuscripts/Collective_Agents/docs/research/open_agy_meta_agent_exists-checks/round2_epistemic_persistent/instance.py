r"""The declared instance I* (fixed before the deciding runs)."""
from lib import Par

PAR = Par(F=0.9, Q=0.05, R=1.0, Rc=0.1, Rs=2.0, Rsh=0.0, psi=0.024, gamma=400.0, qc=1e-4, n=4, n_zero=4, kmsg=3)
MEDIUM = PAR.with_(n=8, n_zero=0)   # clause (c) mechanism medium: one world component, 8 agents of one type
T, BURN, EVERY = 400, 80, 4

import os
from lib import simulate_policy_path, simulate_policy_path_real
PROTO = os.environ.get("PROTO", "fast")   # 'fast': (P4) to stationarity at a frozen decision state; 'real': one event per round
SUFFIX = "_real" if PROTO == "real" else ""


def M(mode: str) -> str:
    return ("real_" + mode) if PROTO == "real" else mode


def sim(par, Tn, rng, mode="full"):
    return simulate_policy_path_real(par, Tn, rng, mode) if PROTO == "real" else simulate_policy_path(par, Tn, rng, mode)
