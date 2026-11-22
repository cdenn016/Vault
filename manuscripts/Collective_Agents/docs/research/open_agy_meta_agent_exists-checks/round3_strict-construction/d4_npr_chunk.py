r"""Deciding script D4 (chunk): independent draws of the selector statistic under N_pr redrawn every round
(prop:agy-tests(b), 05_agency.tex:367).  Each draw is an independent estimate of the null's niche contrast r(A)
(the declared selector's statistic at the candidate block) from 20 world paths x 2 replicas x 400 rounds (burn 80),
sampled-noise Monte Carlo.  Usage: python d4_npr_chunk.py <mode> <ndraw> <seed> <tag>; mode 'pr' (null) or 'full'
(NEGATIVE CONTROL: the same estimator on the full model)."""
import sys, time
import numpy as np
from lib3 import compound
from mc3 import run
from instance3 import PAR, PROTO

mode, ndraw, seed, tag = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
t0 = time.time()
o = run(PAR, K=ndraw * 20, T=400, burn=80, seed=seed, mode=mode, nbatch=ndraw)
S = np.array([1 + 4 * compound(s)[1] / compound(s)[0] for s in o.S_batches])
np.save(f"d4_{PROTO}_{mode}_{tag}.npy", S)
print(f"{PROTO} {mode} chunk {tag}: {len(S)} draws, min {S.min():.4f} median {np.median(S):.4f} max {S.max():.4f}; "
      f"open rate {o.open_rate:.3f}  ({time.time()-t0:.0f}s)")
