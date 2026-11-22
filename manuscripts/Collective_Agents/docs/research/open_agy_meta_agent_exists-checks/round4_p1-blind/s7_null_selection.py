"""Selector verdicts under each null at a level r_0 admissible for the full model (no new simulation;
reads the Sigma^c estimates saved by s2 and s3). Expectation: N_hab, N_pr, N_lp select nothing
(r(A) < r_0); N_fr under the spec convention selects A again (r(A)=7.10 > r_0), so the full model
does not differ from N_fr under that convention."""
import os
import sys
import json

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import numpy as np  # noqa: E402
import p1lib as L  # noqa: E402

s2 = json.load(open(os.path.join(HERE, "s2_full_output.json")))
s3 = json.load(open(os.path.join(HERE, "s3_nulls_output.json")))
lo = max(s2["item2"]["baseline_mean"][0], s2["medium"]["sup"][0])
hi = s2["item2"]["rA"][0]
print("full model: admissible levels r_0 in (%.5f, %.5f]" % (lo, hi))
for name in ("N_hab", "N_pr", "N_lp", "N_fr", "N_fr_cond_v0"):
    S = np.array(s3[name]["Sigma"])
    an = L.analyze_sigma(S)
    sel = {r0: [C for C, v in an["r_all"].items() if v >= r0 and r0 > max(an["baseline_mean"], 1.0)]
           for r0 in (lo + 1e-9, hi)}
    print("%-13s r(A)=%.5f  mean-coupling baseline of the null=%.5f  diffusive=%s  regions selected at r_0=lo+: %s, at r_0=r(A)_full: %s" % (
        name, an["rA"], an["baseline_mean"], an["diffusive"], sel[lo + 1e-9], sel[hi]))
