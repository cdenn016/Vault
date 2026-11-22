"""Summary of the box (item 10): table, admissible r_0, maxima, and main-effect extrapolation to the
128 corners (resolution IV: main effects are not aliased with two-factor interactions)."""
import os
import sys
import json

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import numpy as np  # noqa: E402
import p1lib as L  # noqa: E402

rows = {}
for fn in ("s5_box_00_07.json", "s5_box_08_15.json", "s5_box_16_16.json"):
    rows.update({int(k): v for k, v in json.load(open(os.path.join(HERE, fn))).items()})
idx = sorted(rows)
assert idx == list(range(17))
D = L.frac_design()
hdr = ("pt", "code(F,Q,R,RS,Rc,qc,g)", "r(A)", "se", "base_mean", "base_med", "se", "max other", "region",
       "het_A", "mem_det", "KL_best", "N_hab", "N_pr", "agency")
print("%3s %-24s %9s %7s %9s %9s %7s %9s %-17s %8s %8s %9s %7s %7s %9s" % hdr)
cols = {k: [] for k in ("rA", "bm", "bmed", "other", "het", "mem", "kl", "hab", "pr", "ag")}
for i in idx:
    r = rows[i]
    c = "".join("+" if x > 0 else ("-" if x < 0 else "0") for x in r["code"])
    print("%3d %-24s %9.5f %7.1g %9.5f %9.5f %7.1g %9.5f %-17s %8.5f %8.5f %9.6f %7.4f %7.4f %9.6f" % (
        i, c, r["rA"][0], r["rA"][1], r["base_mean"][0], r["base_medium"][0], r["base_medium"][1],
        r["max_other"][0], r["max_other_region"], r["hetA"][0], r["mem_det_sup"][0], r["KL_best"],
        r["N_hab"][0], r["N_pr"][0], r["agency"]))
    for k, v in zip(cols, (r["rA"][0], r["base_mean"][0], r["base_medium"][0], r["max_other"][0], r["hetA"][0],
                           r["mem_det_sup"][0], r["KL_best"], r["N_hab"][0], r["N_pr"][0], r["agency"])):
        cols[k].append(v)
cols = {k: np.array(v) for k, v in cols.items()}
lower = np.maximum.reduce([cols["bm"], cols["bmed"], cols["het"]])
print("\nall points diffusive:", all(rows[i]["diffusive"] for i in idx))
print("min r(A) over the 17 points = %.5f at point %d" % (cols["rA"].min(), int(cols["rA"].argmin())))
print("max mean-coupling baseline = %.5f at point %d" % (cols["bm"].max(), int(cols["bm"].argmax())))
print("max mechanism-medium baseline = %.5f at point %d" % (cols["bmed"].max(), int(cols["bmed"].argmax())))
print("max leak heterogeneity on A = %.5f" % cols["het"].max())
print("pointwise margin min_p [r_p(A) - max(base_mean_p, base_med_p, het_p)] = %.5f" % (cols["rA"] - lower).min())
print("largest r_0 admissible at all 17 points = min_p r_p(A) = %.5f; admissible interval (%.5f, %.5f]" % (
    cols["rA"].min(), lower.max(), cols["rA"].min()))
print("largest memory defect (deterministic start, sup_t) = %.5f at point %d" % (cols["mem"].max(), int(cols["mem"].argmax())))
print("largest inference KL (best constant) = %.6f at point %d" % (cols["kl"].max(), int(cols["kl"].argmax())))
print("largest other-region contrast = %.5f; N_hab range [%.4f, %.4f]; N_pr range [%.4f, %.4f]; agency range [%.6f, %.6f]" % (
    cols["other"].max(), cols["hab"].min(), cols["hab"].max(), cols["pr"].min(), cols["pr"].max(),
    cols["ag"].min(), cols["ag"].max()))

# main effects from the 16 factorial runs (+-1 coded), linear extrapolation to the extreme corners
X = D[1:]
print("\nmain effects (half the high-minus-low difference), factors", L.FACTORS)
ext = {}
for k in ("rA", "bm", "bmed", "mem", "kl"):
    y = cols[k][1:]
    beta = X.T @ y / 16.0
    mean = y.mean()
    lo, hi = mean - np.abs(beta).sum(), mean + np.abs(beta).sum()
    ext[k] = (lo, hi)
    print("  %-5s mean %.5f  effects %s  linear corner range [%.5f, %.5f]" % (k, mean, np.round(beta, 5), lo, hi))
print("linear-model worst case over the 128 corners: min r(A) ~ %.4f vs max baseline ~ %.4f (not computed points)" % (
    ext["rA"][0], max(ext["bm"][1], ext["bmed"][1])))
