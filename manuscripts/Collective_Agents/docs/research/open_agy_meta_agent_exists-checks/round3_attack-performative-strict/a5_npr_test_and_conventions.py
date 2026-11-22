r"""a5: (i) the literal partner-randomization test of prop:agy-tests(b) for the
CCP with n_null = 999 draws (each draw: the every-round null's second moment
estimated from 10 independent partner sequences, zero-gain convention; statistic:
the pair's contrast), against S_0 = 4.3336; (ii) which pure-noise variance
reproduces the candidate's N_lp = 1.2397.

Declared expectations (before running):
 E1 every null draw S_l < S_0, so p = 1/1000 <= 0.01.
 E2 NEGATIVE CONTROL: the same estimator with the mate always read gives draws
    equal to S_0 (ties count), so p = 1 and the test accepts.
 E3 N_lp with pure-noise variance R + Rc = 1.1 gives about 1.24.
"""
import numpy as np
import io, contextlib
with contextlib.redirect_stdout(io.StringIO()):
    import a2_npr as N   # my own time-varying code (its demo output suppressed)
from ccp_lib import *

rng = np.random.default_rng(31337)
L, Lr, burn = 40, 40, 40
nT = burn + L + Lr + 1
S0 = 4.33360016


def stat(W):
    return (W[0, 0] + W[0, 1]) / (W[0, 0] - W[0, 1]) if is_diffusive(np.linalg.inv(W)) else np.inf


draws = []
for d in range(999):
    acc = np.zeros((2, 2))
    for k in range(10):
        rb = (rng.random(nT) < 1 / 3).astype(int)
        rs = (rng.random(nT) < 1 / 3).astype(int)
        acc += N.firm_window_zero_gain(rb, rs, L, Lr, burn)
    draws.append(stat(acc / 10))
draws = np.array(draws)
pval = (1 + np.sum(draws >= S0)) / (len(draws) + 1)
print("E1 999 draws: min %.3f median %.3f max %.3f; #(S_l >= S_0) = %d; p = %.4f"
      % (draws.min(), np.median(draws), draws.max(), np.sum(draws >= S0), pval))
ones = np.ones(nT, dtype=int)
ctrl = [stat(N.firm_window_zero_gain(ones, ones, L, Lr, burn)) for _ in range(5)]
print("E2 control draws (mate always read):", np.round(ctrl, 6), " p =", (1 + np.sum(np.array(ctrl) >= S0 - 1e-9)) / (len(ctrl) + 1))

p = default_params()
filt = member_filters(p)
T = coord_map("own")
for var in (p["Rc"], p["R"] + p["Rc"], p["Q"] / (1 - p["F"] ** 2) + p["R"] + p["Rc"]):
    pp = dict(p); pp["Rc"] = var
    A, B, C, Dm, qv = private_system(pp, filt, "lp")
    o = summarize_pair(window_condition(A, B, C, Dm, qv, T, L=60))
    print("E3 N_lp with pure-noise variance %.4f: r(pair) = %.4f" % (var, o["r_pair"]))
