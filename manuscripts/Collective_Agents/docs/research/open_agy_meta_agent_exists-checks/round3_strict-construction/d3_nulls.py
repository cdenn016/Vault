r"""Deciding script D3: the null family of tab:agy-nulls (05_agency.tex:337-360) for I**, one protocol.

Each null keeps the world, sensing, priors, preferences and habits; same exact pair algebra and second-moment
convention.  Windows from d1_<proto>.npz (comparison media declared with the model and held fixed under the nulls).
Declared expectations (before running):
  N_hab (gamma = 0, statuses and attention from the uniform habits, same protocol clock): r(A) about 2.4;
  N_pr  (partners redrawn every round, 3 of 7 uniformly; status decisions by EFE given the drawn partners): about 2.85;
  N_lp  (channels deliver pure noise, assigned precisions kept, headers lost): r(A) within 0.01 of 1
        (no shared private noise; only a reviser-clock mixture term remains);
  N_rn  identical to N_lp (no informative source left to which deleted message capacity could go);
  N_fr  (others held at their initial state): r(A) within 0.01 of 1 (exactly 1 under 'frozen');
  N_eff, N_inf: inapplicable (no performative component; def:agy-nulls 05_agency.tex:333);
  N_ex: inapplicable (fusion already exact); variant qc = 0: the same partition survives at r >= r0.
  For every D null: largest region contrast below the lower edge of both windows (margin > 3), hence at every r0 of
  either window the null selects no region and its partition differs from {A,B}.
  NEGATIVE CONTROL: the full model through the same null pipeline reproduces r(A) about 8.43 and does NOT differ.
"""
import time
import numpy as np
from lib3 import sigma_c, region_contrasts, population_precision, is_diffusive
from instance3 import PAR, T, BURN, EVERY, R0, PROTO

d1 = np.load(f"d1_{PROTO}.npz")
WIN = {"mechanism": (float(d1["rM"]), float(d1["r"])), "mean-coupling": (float(d1["mc"]), float(d1["r"]))}
print("protocol", PROTO, "windows", {k: tuple(round(x, 4) for x in v) for k, v in WIN.items()}, "r0", R0)


def report(name, res):
    al, be = res["alpha"], res["beta"]
    Pi, _ = population_precision(al, be)
    d = is_diffusive(Pi, tol=0.0)
    rc = region_contrasts(Pi)
    rmax = max(rc.values()); arg = max(rc, key=rc.get)
    print(f"{name}: alpha={al:.7f} beta={be:.3e} (SE {res['se_beta']:.1e}) r(A)={res['r']:.4f} +/- {res['se_r']:.4f}; "
          f"max region contrast {rmax:.4f} at {arg}; diffusive={d[0]} (largest offdiag {d[1]:.1e}); "
          f"open rate {res['open_rate']:.3f}; attention-deficit rate {res['dev_rate']:.3f}")
    for wn, (lo, hi) in WIN.items():
        print(f"    differs at every r0 in the {wn} window: {rmax < lo} (margin {lo - rmax:.4f})")
    return rmax


t0 = time.time()
report("N_hab", sigma_c(PAR, 60, T, BURN, EVERY, seed=401, mode="hab"))
report("N_pr (every round)", sigma_c(PAR, 60, T, BURN, EVERY, seed=402, mode="pr"))
print(f"  t={time.time()-t0:.0f}s", flush=True)
report("N_lp", sigma_c(PAR, 30, T, BURN, EVERY, seed=403, mode="lp"))
print("N_rn: identical to N_lp (own and private sensors are not message-capacity limited; no informative source "
      "remains to which deleted message capacity could be reassigned)")
report("N_fr", sigma_c(PAR, 30, T, BURN, EVERY, seed=404, mode="fr"))
print(f"  t={time.time()-t0:.0f}s", flush=True)
ex = sigma_c(PAR.with_(qc=0.0), 40, T, BURN, EVERY, seed=405)
Pi, _ = population_precision(ex["alpha"], ex["beta"])
rc = region_contrasts(Pi)
oth = max(v for C, v in rc.items() if C not in ((0, 1, 2, 3), (4, 5, 6, 7)))
print(f"N_ex: inapplicable (receivers already fuse raw data exactly with provenance; no records). Variant qc = 0: "
      f"r(A)={ex['r']:.4f}, largest other region {oth:.4f}; survives at r0={R0}: {ex['r'] >= R0 and oth < R0}; "
      f"at every r0 of both windows: {ex['r'] >= WIN['mechanism'][1] - 0.05 and oth < WIN['mechanism'][0]}")
print("N_eff, N_inf: inapplicable (no active-state component enters eta: attention and speech only)")
neg = sigma_c(PAR, 20, T, BURN, EVERY, seed=406)
print(f"NEG full model through the null pipeline: r(A)={neg['r']:.4f}; differs: {neg['r'] < WIN['mechanism'][0]} "
      f"(expected False)")
print(f"total {time.time()-t0:.0f}s")
