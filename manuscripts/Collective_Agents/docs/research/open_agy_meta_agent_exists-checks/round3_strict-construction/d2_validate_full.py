r"""Deciding script D2: the second moments of I** under random policies, two independent computations.

(i) exact pair algebra (lib3.pair_moments) averaged over policy-path pairs (d1_<proto>.npz);
(ii) sampled-noise Monte Carlo of the actual filters (mc3.run), two replicas per world path.
Declared expectations (before running): for each protocol, |alpha_MC - alpha_exact| and |beta_MC - beta_exact| below
3 combined standard errors, and r within 3 SE.  NEGATIVE CONTROL: the exact algebra with the relayed private noises
treated as fresh draws (40 pairs) must disagree with the Monte Carlo beta by more than 20 SE (its beta collapses to
the policy-mixture part, about 2e-5).  Second NEGATIVE CONTROL: the Monte Carlo with fresh relays reproduces the
collapse (r within 0.05 of 1), so the coupling is carried by the relayed private noises and nothing else.
"""
import time
import numpy as np
from lib3 import Par, sigma_c, compound
from mc3 import run
from instance3 import PAR, T, BURN, EVERY

t0 = time.time()
for proto in ("real", "frozen"):
    par = PAR.with_(proto=proto)
    ex = np.load(f"d1_{proto}.npz")
    al_e, be_e = float(ex["al"]), float(ex["be"])
    ab = ex["ab"]
    se_e = ab.std(0, ddof=1) / np.sqrt(len(ab))
    mc = run(par, K=3000, T=T, burn=BURN, seed=611 if proto == "real" else 612, nbatch=30)
    abm = np.array([compound(s) for s in mc.S_batches])
    al_m, be_m = compound(mc.S)
    se_m = abm.std(0, ddof=1) / np.sqrt(len(abm))
    za = (al_m - al_e) / np.hypot(se_m[0], se_e[0]); zb = (be_m - be_e) / np.hypot(se_m[1], se_e[1])
    r_m = 1 + 4 * be_m / al_m
    rb = 1 + 4 * abm[:, 1] / abm[:, 0]
    print(f"[{proto}] exact: alpha {al_e:.7f} beta {be_e:.7f} r {float(ex['r']):.4f}; MC (3000 worlds x 2): alpha "
          f"{al_m:.7f} beta {be_m:.7f} r {r_m:.4f} +/- {rb.std(ddof=1)/np.sqrt(len(rb)):.4f}; z_alpha {za:.2f} z_beta {zb:.2f}; "
          f"open rate MC {mc.open_rate:.4f}  ({time.time()-t0:.0f}s)", flush=True)
    fr = sigma_c(par, 40, T, BURN, EVERY, seed=613, fresh_relays=True)
    zf = (fr["beta"] - be_m) / np.hypot(se_m[1], fr["se_beta"])
    print(f"   NEG exact algebra with fresh relays: beta {fr['beta']:.3e} r {fr['r']:.4f}; z vs MC beta {zf:.1f} "
          f"(must be < -20)  ({time.time()-t0:.0f}s)", flush=True)
mcf = run(PAR, K=1000, T=300, burn=80, seed=614, nbatch=20, fresh_relays=True)
alf, bef = compound(mcf.S)
print(f"NEG2 MC with fresh relays (real): alpha {alf:.6f} beta {bef:.3e} r {1+4*bef/alf:.4f} (expected within 0.05 of 1)")
print(f"total {time.time()-t0:.0f}s")
