import csv, math, sys
path = sys.argv[1]
rows = list(csv.DictReader(open(path, newline="")))
def f(r, k):
    try:
        return float(r[k])
    except Exception:
        return float("nan")
print("val evaluations:")
for r in rows:
    v = f(r, "val_ce")
    if not math.isnan(v):
        print("  step %6d val_ce %.5f val_ppl %.4f pass %.3f gap %.4f" % (f(r, "step"), v, f(r, "val_ppl"), f(r, "corpus_pass"), f(r, "generalization_gap")))
tr = [(f(r, "step"), f(r, "train_ce")) for r in rows]
def window_mean(lo, hi):
    xs = [c for s, c in tr if lo <= s <= hi and not math.isnan(c)]
    return (sum(xs) / len(xs), len(xs), min(xs), max(xs)) if xs else None
for lo, hi in [(0, 24000), (24000, 48000), (48000, 72000), (72000, 96000), (96000, 120000), (120000, 144000), (144000, 168000), (168000, 192000), (192000, 216000), (216000, 240000)]:
    print("train_ce window %6d-%6d mean %.4f n %d min %.3f max %.3f" % ((lo, hi) + window_mean(lo, hi)))
# epoch boundaries
spe = f(rows[0], "steps_per_epoch")
print("steps_per_epoch", spe, "tokens/epoch", spe * 16 * 128)
print("presentations", 240000 * 16 * 128, "corpus passes", 240000 * 16 * 128 / 116840318)
# throughput / memory
for k in ("peak_mem_mb", "train_step_ms_mean", "train_step_tokens_per_s", "tokens_per_s", "wall_clock_s", "grad_norm", "grad_norm_mu", "grad_norm_sigma", "grad_norm_phi", "grad_norm_relational_score", "grad_norm_relational_content"):
    vals = [f(r, k) for r in rows]
    vals = [v for v in vals if not math.isnan(v)]
    if vals:
        print(k, "first %.4g last %.4g min %.4g max %.4g" % (vals[0], vals[-1], min(vals), max(vals)))
for k in ("val_guard_sigma_floor_frac", "val_guard_sigma_ceil_frac", "val_guard_energy_klmax_frac", "val_nonfinite_frac", "val_phi_exp_clamp_frac", "val_phi_matrix_norm_max", "val_pos_phi_exp_clamp_frac", "val_future_leakage", "val_row_sum_error", "val_prev_token_mass", "val_pos_content_r2", "val_attn_collapsed_heads", "val_head_redundancy_js", "phi_chart_projected_rows", "phi_chart_preproject_max", "step_skipped", "loss_finite", "grad_finite"):
    vals = [(f(r, "step"), f(r, k)) for r in rows]
    vals = [(s, v) for s, v in vals if not math.isnan(v)]
    if vals:
        print(k, "n=%d" % len(vals), "last %.6g max %.6g min %.6g" % (vals[-1][1], max(v for _, v in vals), min(v for _, v in vals)))
