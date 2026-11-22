r"""Check V2: the grouped attention law and its KL to the uniform habit over the 64 message sets (agency3.member_laws)
against explicit enumeration of every message set (3 mates + 4 zero-gain channels, |M| <= 3), at random decision
states.  Declared expectation: agreement to 1e-10 in the slot-marginal probability and in KL(q(M|s) || U64).
NEGATIVE CONTROL: enumerating with the zero-gain channels wrongly given the gain of a closed mate must disagree by
more than 1e-3 in the KL.
"""
import itertools
import numpy as np
from lib3 import Pminus, info
from agency3 import member_laws
from instance3 import PAR

rng = np.random.default_rng(1)
chans = list(range(7))   # 0,1,2 = mates (in member order), 3..6 = zero-gain
sets = [S for k in range(4) for S in itertools.combinations(chans, k)]
assert len(sets) == 64
worst = [0.0, 0.0]; neg = 0.0
for trial in range(50):
    p = rng.uniform(0.089, 0.141, 4)
    sig = rng.integers(0, 2, 4)
    q1, KLa, _, _ = member_laws(PAR, p, sig)
    for i in range(4):
        mates = [j for j in range(4) if j != i]
        P00, P01, P11 = Pminus(PAR, p[i])
        for bad in (False, True):
            G = np.zeros((2, 64))
            for s in (0, 1):
                for k, S in enumerate(sets):
                    b = 0.0
                    for c in S:
                        if c < 3:
                            b += 1 / (PAR.R + PAR.Rc) + sig[mates[c]] / (PAR.Rs + PAR.Rc)
                        elif bad:
                            b += 1 / (PAR.R + PAR.Rc)
                    G[s, k] = -info(P00, P01, P11, 1 / PAR.R + s / PAR.Rs, b) + PAR.psi * s
            lw = -PAR.gamma * G
            lZ = np.log(np.exp(lw - lw.max()).sum(1)) + lw.max()
            qq1 = 1 / (1 + np.exp(lZ[0] - lZ[1]))
            for s in (0, 1):
                q = np.exp(lw[s] - lZ[s])
                kl = float(np.sum(q * np.log(64 * q)))
                if not bad:
                    worst[1] = max(worst[1], abs(kl - KLa[i, s]))
                else:
                    neg = max(neg, abs(kl - KLa[i, s]))
            if not bad:
                worst[0] = max(worst[0], abs(qq1 - q1[i]))
print(f"max |slot-marginal difference| {worst[0]:.2e}; max |attention KL difference| {worst[1]:.2e} (expected < 1e-10)")
print(f"NEG zero-gain channels given a closed mate's gain: max |KL difference| {neg:.3e} (expected > 1e-3)")
