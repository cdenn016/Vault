r"""Check 13b: Proposition A (closed forms for the source-plus-exchangeable-audience structure) against direct
inversion and enumeration, on the scan of check 13 and on 300 random admissible (sigma, c, alpha, beta).
Declared expectation before running: max |closed - direct| <= 1e-9 (relative) for r(A), r(A u S), the couplings,
the leaks and the mean-coupling baseline; NEGATIVE CONTROL: a structure with beta' < 0 (beta < c^2/sigma) must be
reported non-diffusive by both the closed form and the direct test."""
import numpy as np
from aud import contrast, diffusive, mean_coupling_baseline

def closed(sig, c, al, be, n):
    bp = be - c * c / sig
    D = al + n * bp
    aAA = bp / (al * D); aSA = c / (sig * D)
    eA = (1 - c / sig) / D
    PiSS = 1 / sig + n * c * c / (sig * sig * D)
    eS = PiSS - n * aSA
    rA = 1 - c / sig + n * bp / al
    xout = (eS + n * eA) / (n + 1)
    Rf = (n * PiSS + 2 * n * aSA + 1 / D) / (n + 1)
    rAS = min(1 / al, Rf) / xout
    N = n + 1
    abar = (n * (n - 1) / 2 * aAA + n * aSA) / (N * (N - 1) / 2)
    ebar = (eS + n * eA) / N
    diff_ = (bp >= 0) and (c >= 0) and (c <= sig) and (eS >= 0)
    return dict(rA=rA, rAS=rAS, aAA=aAA, aSA=aSA, eA=eA, eS=eS, mc=1 + N * abar / ebar, diffusive=diff_)

rng = np.random.default_rng(0)
worst = 0.0
nd_agree = 0
for trial in range(300):
    n = int(rng.integers(2, 7))
    al = rng.uniform(0.1, 2); be = rng.uniform(0, 2); sig = rng.uniform(0.1, 3); c = rng.uniform(0, 1) * min(sig, np.sqrt(be * sig))
    S = np.zeros((n + 1, n + 1)); S[0, 0] = sig; S[0, 1:] = c; S[1:, 0] = c
    S[1:, 1:] = be; S[1:, 1:][np.diag_indices(n)] = al + be
    Pi = np.linalg.inv(S)
    cf = closed(sig, c, al, be, n)
    dd = diffusive(Pi, tol=1e-12)[0]
    if dd != cf["diffusive"]:
        print("diffusivity disagreement", trial); continue
    if not dd:
        nd_agree += 1; continue
    A = tuple(range(1, n + 1))
    direct = dict(rA=contrast(Pi, A), rAS=contrast(Pi, tuple(range(n + 1))), aAA=-Pi[1, 2], aSA=-Pi[0, 1],
                  eA=Pi.sum(1)[1], eS=Pi.sum(1)[0], mc=mean_coupling_baseline(Pi)[3])
    for k in direct:
        worst = max(worst, abs(direct[k] - cf[k]) / max(1.0, abs(direct[k])))
print(f"300 random structures: max relative deviation closed vs direct {worst:.2e}; non-diffusive cases agreed {nd_agree}")
cf = closed(1.0, 0.9, 1.0, 0.5, 4)   # beta' = 0.5 - 0.81 < 0
S = np.zeros((5, 5)); S[0, 0] = 1.0; S[0, 1:] = 0.9; S[1:, 0] = 0.9; S[1:, 1:] = 0.5; S[1:, 1:][np.diag_indices(4)] = 1.5
print(f"NEG beta' < 0: closed-form diffusive {cf['diffusive']}, direct {diffusive(np.linalg.inv(S), tol=1e-12)[0]}")
