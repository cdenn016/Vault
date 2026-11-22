r"""Declared instance I** (fixed before the deciding runs).

I* (record C11) with the public slots replaced by private optional sensors (read by the owner, relayed raw with the
one-round latency inside the owner's message to every agent that attends it), and psi raised from 0.024 to 0.030
(at 0.024 the clause (c) mechanism window is empty: medium 8.29 > r(A) 7.80, explore1_out.txt).
Two protocols are declared and analysed separately: 'real' (one reviser per niche per round; the mechanism medium of
8 agents has 2 revisers per round, the same per-agent rate 1/4) and 'frozen' ((P4) at the frozen decision state,
which in I** is the product of the members' policy posteriors, realizable with one-round latency).
Grade under test: (r0, alpha_M, alpha_I, alpha_pr) = (7.9, 0.02, 0.09, 0.01), n_null = 999; Agency0 = the frontier.
"""
import os
from lib3 import Par

PROTO = os.environ.get("PROTO", "real")
PAR = Par(F=0.9, Q=0.05, R=1.0, Rc=0.1, Rs=2.0, psi=0.030, gamma=400.0, qc=1e-4, n=4, n_zero=4, kmsg=3,
          proto=PROTO, nrev=1, p0=0.09)
MEDIUM = PAR.with_(n=8, n_zero=0, nrev=2)
T, BURN, EVERY = 400, 80, 4
R0 = 7.9
ALPHA_M, ALPHA_I, ALPHA_PR, N_NULL = 0.02, 0.09, 0.01, 999
SUFFIX = "_" + PROTO
