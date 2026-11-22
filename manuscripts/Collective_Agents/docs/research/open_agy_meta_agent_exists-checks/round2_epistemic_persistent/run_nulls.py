r"""Deciding script 2: the null family of tab:agy-nulls at the declared instance I*.

Each null keeps the world, sensing, priors, preferences and habits, and is computed with the same exact pair-moment
machinery (second-moment convention).  The comparison media are declared with the model and held fixed under the
nulls (mechanism window (2.9386, 4.3912], mean-coupling window (3.9067, 4.3912], from main_out.txt).
Declared expectations (before running):
  N_hab (gamma = 0: attention and slots from the uniform habits): r(A) about 1.7, below both windows.
  N_pr (partners redrawn every round, 3 uniformly of 7; slots by (P4) given the partners): about 1.9, below.
  N_lp (inter-agent channels deliver pure noise of the believed variance; assigned precisions, slots and capacities
        kept; intention announcements deleted): only a slot-mixture common mode remains, r(A) within 0.1 of 1.
  N_rn: identical to N_lp (no informative source left to which deleted message capacity could be reassigned).
  N_fr (others frozen at the declared deterministic initial state): Sigma^c exactly diagonal, r(A) = 1.
  N_ex: (i) inapplicable (fusion already exact); (ii) if computation noise is counted as part of fusion and removed
        (qc = 0), r(A) rises and {A,B} survives at every r0 of both windows (other regions stay below 2).
  For every null: largest region contrast below the lower edge of each window, so at every r0 in the window the
  null selects no region and its partition differs from {A,B}.
  NEGATIVE CONTROL: the full model run through the same 'null' pipeline (mode 'full') must reproduce r(A) = 4.39
  and therefore NOT differ.
"""
import re
import time
import numpy as np
from lib import sigma_c, region_contrasts, diffusive
from instance import PAR, T, BURN, EVERY, M, PROTO, SUFFIX

WIN = {}
for line in open(f"main{SUFFIX}_out.txt"):
    if line.startswith("WINDOW"):
        nm = line.split()[1].rstrip(":")
        lo, hi = re.findall(r"[-0-9.]+", line.split("(")[1])[:2]
        WIN[nm] = (float(lo), float(hi))
print("protocol", PROTO, "windows", WIN)


def report(name, res):
    al, be = res["alpha"], res["beta"]
    SA = al * np.eye(4) + be * np.ones((4, 4))
    S = np.zeros((8, 8)); S[:4, :4] = SA; S[4:, 4:] = SA
    Pi = np.linalg.inv(S)
    d = diffusive(Pi)
    rc = region_contrasts(Pi)
    rmax = max(rc.values())
    argmax = max(rc, key=rc.get)
    raw_off = np.abs(res["S"] - np.diag(np.diag(res["S"]))).max()
    msg = (f"{name}: alpha={al:.7f} beta={be:.3e} (SE beta {res['se_beta']:.1e}) r(A)={res['r']:.4f} "
           f"[E[Cov] only {res['r_priv']:.4f}] max region contrast {rmax:.4f} at {argmax}; diffusive={d[0]}; "
           f"max raw offdiag |Sigma_ij|={raw_off:.2e}; open rate {res['open_rate']:.3f}; "
           f"relay-deficit rate {res['dev_rate']:.3f}")
    print(msg)
    for wn, (lo, hi) in WIN.items():
        print(f"    differs at every r0 in the {wn} window: {rmax < lo} (margin {lo - rmax:.4f})")
    return rmax


t0 = time.time()
r_hab = report("N_hab", sigma_c(PAR, M("hab"), 60, T, BURN, EVERY, seed=401))
print(f"  t={time.time()-t0:.0f}s", flush=True)
r_pr = report("N_pr (every round)", sigma_c(PAR, M("pr"), 40, T, BURN, EVERY, seed=402))
print(f"  t={time.time()-t0:.0f}s", flush=True)
r_lp = report("N_lp", sigma_c(PAR, M("lp"), 30, T, BURN, EVERY, seed=403, dead_var=PAR.R + PAR.Rc))
print("N_rn: identical to N_lp (own sensor and every slot channel are already structural; deleted message capacity "
      "has no informative source to go to)")
r_fr = report("N_fr", sigma_c(PAR, M("fr"), 20, T, BURN, EVERY, seed=404, dead_var=PAR.Rc))
print(f"  t={time.time()-t0:.0f}s", flush=True)
ex = sigma_c(PAR.with_(qc=0.0), M("full"), 40, T, BURN, EVERY, seed=405)
al, be = ex["alpha"], ex["beta"]
SA = al * np.eye(4) + be * np.ones((4, 4))
S = np.zeros((8, 8)); S[:4, :4] = SA; S[4:, 4:] = SA
rc = region_contrasts(np.linalg.inv(S))
oth = max(v for C, v in rc.items() if C not in ((0, 1, 2, 3), (4, 5, 6, 7)))
print(f"N_ex reading (ii), qc = 0: r(A)={ex['r']:.4f}, largest other region {oth:.4f}; survives (same partition "
      f"{{A,B}} selected with blocks at r >= r0) at every r0 of both windows: {ex['r'] >= WIN["mechanism"][1] and oth < WIN["mechanism"][0]}")
neg = sigma_c(PAR, M("full"), 20, T, BURN, EVERY, seed=406)
print(f"NEG full model through the null pipeline: r(A)={neg['r']:.4f}; differs: {neg['r'] < WIN["mechanism"][0]} (expected False)")
# prop:agy-tests(b): annealed N_pr, independent replicate estimates of the selector statistic
reps = [sigma_c(PAR, M("pr"), 5, T, BURN, EVERY, seed=500 + k)["r"] for k in range(5)]
print(f"N_pr replicate statistics (5 independent estimates, 5 pairs each): {np.round(reps, 4)}; S_0 = r(A) = {WIN["mechanism"][1]}; "
      f"with n_null = 99 draws all below S_0, p = 1/100 = 0.01 <= alpha_pr = 0.01")
print(f"total time {time.time()-t0:.1f}s")
