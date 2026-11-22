r"""a8: the record's convention that an agent's own sensing noise stays private when
it is relayed (open_agy_meta_agent_exists.md, Conventions, World-conditional law).
Alternative reading: a relayed sensing noise is a noise "shared by several
receivers" (def:col-world-conditional, 04_collectives.tex:131) and is conditioned on.
Declared expectation: under the alternative the CCP's window empties or N_eff rises
to the window (the relay correlation is removed and only explaining-away remains).
Negative control: with the convention of the record the code returns 4.3336."""
import numpy as np
from ccp_lib import *
p = default_params(); filt = member_filters(p); T = coord_map("own")
for tag, var_v in (("record convention (v private)", p["R"]), ("alternative (v conditioned)", 0.0)):
    A, B, C, Dm, qv = private_system(p, filt, "full")
    qv = qv.copy(); qv[0] = qv[1] = var_v
    full = summarize_pair(window_condition(A, B, C, Dm, qv, T, L=60))
    eff = summarize_pair(T @ stationary_cov(A, B, qv) @ T.T)
    print("%-32s full: diffusive %s r(pair)=%.4f rbar=%.4f | N_eff: r(pair)=%.4f" % (tag, full["diffusive"], full["r_pair"], full["rbar"], eff["r_pair"]))
