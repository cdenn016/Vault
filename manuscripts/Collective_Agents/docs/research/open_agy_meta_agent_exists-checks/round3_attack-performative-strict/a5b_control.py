r"""a5b: precision of the a5 negative control (mate always read, L=40 windows).
Expectation: the control statistic equals S_0 to < 1e-6, so with ties counted
at 1e-6 the test accepts the full model (p = 1)."""
import io, contextlib
import numpy as np
with contextlib.redirect_stdout(io.StringIO()):
    import a2_npr as N
L, Lr, burn = 40, 40, 40
nT = burn + L + Lr + 1
W = N.firm_window_zero_gain(np.ones(nT, dtype=int), np.ones(nT, dtype=int), L, Lr, burn)
s = (W[0, 0] + W[0, 1]) / (W[0, 0] - W[0, 1])
print("control statistic %.10f ; S_0 4.33360016 ; difference %.2e" % (s, s - 4.33360016))
