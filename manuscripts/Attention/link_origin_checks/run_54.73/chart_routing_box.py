import sys, json, csv, numpy as np, torch
run = sys.argv[1]
ck = torch.load(run + "/final_model.pt", map_location="cpu", weights_only=False)
sd, cfg = ck["model_state"], json.load(open(run + "/config.json"))["config"]
L, H, K = cfg["n_layers"], cfg["n_heads"], cfg["embed_dim"]; d = K // H
names = ["relational_operators"] + [f"relational_operators_extra.{i}" for i in range(L - 1)]
grid = np.linspace(0.0, 1.0, 41)
print("Edge operator with per-head weights b=(b1,b2) in [0,1]^2: I + O B T (residual present) and bare O B T")
for l, nm in enumerate(names):
    T = sd[nm + ".T"].double().numpy(); O = sd[nm + ".O"].double().numpy()
    Ost = np.concatenate([O[h] for h in range(H)], axis=1); Tst = np.concatenate([T[h] for h in range(H)], axis=0)
    worst_smin, neg_det, worst_cond, min_re = 1e9, 0, 0.0, 1e9
    for b1 in grid:
        for b2 in grid:
            B = np.diag(np.repeat([b1, b2], d))
            A = np.eye(K) + Ost @ B @ Tst
            sgn, _ = np.linalg.slogdet(A)
            s = np.linalg.svd(A, compute_uv=False)
            worst_smin = min(worst_smin, s[-1]); worst_cond = max(worst_cond, s[0] / s[-1]); neg_det += sgn <= 0
            min_re = min(min_re, np.linalg.eigvals(A).real.min())
    sd_O, sd_T = np.linalg.slogdet(Ost)[0], np.linalg.slogdet(Tst)[0]
    print(f"layer {l}: I+OBT over the box: min sigma_min={worst_smin:.3f}  max cond={worst_cond:.1f}  grid points with det<=0: {int(neg_det)}/{len(grid)**2}  min Re(eig)={min_re:.3f}")
    print(f"         bare OBT (b1,b2>0): sign det = sign det(O)*sign det(T) = {int(sd_O)}*{int(sd_T)} = {int(sd_O*sd_T):+d}  (routing-independent)")
rows = list(csv.DictReader(open(run + "/diagnostics/attention_stats.csv")))
last = max(int(r["step"]) for r in rows)
print(f"\nRealized routing at step {last} (attention_stats.csv): mean self weight, normalized entropy")
for r in rows:
    if int(r["step"]) == last:
        print(f"  layer {r['layer']} head {r['head']}: self_weight={float(r['self_weight']):.3f}  entropy_norm={float(r['entropy_norm']):.3f}  prior_overlap={float(r['prior_overlap']):.3f}")
