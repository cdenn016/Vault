import sys, glob, json, numpy as np, torch
run = sys.argv[1]
cfg = json.load(open(run + "/config.json"))["config"]
L, H, K = cfg["n_layers"], cfg["n_heads"], cfg["embed_dim"]; d = K // H
names = ["relational_operators"] + [f"relational_operators_extra.{i}" for i in range(L - 1)]
files = sorted(glob.glob(run + "/map_snapshots/step_*.pt"))
rows = []
for f in files:
    s = torch.load(f, map_location="cpu", weights_only=False); step, st = s["step"], s["state"]
    for l, nm in enumerate(names):
        T = st[nm + ".T"].double().numpy(); O = st[nm + ".O"].double().numpy()
        Ost = np.concatenate([O[h] for h in range(H)], axis=1); Tst = np.concatenate([T[h] for h in range(H)], axis=0)
        M = Ost @ Tst
        sg, _ = np.linalg.slogdet(M); sv = np.linalg.svd(M, compute_uv=False)
        w = np.linalg.eigvals(M); wi = np.linalg.eigvals(np.eye(K) + M)
        rows.append(dict(step=step, layer=l, sign_det_M=int(sg), smin_M=float(sv[-1]), smax_M=float(sv[0]),
                         n_neg_real_eig_M=int(np.sum((np.abs(w.imag) < 1e-9) & (w.real <= 0))), n_re_neg_M=int(np.sum(w.real < 0)),
                         min_re_M=float(w.real.min()), min_re_IplusM=float(wi.real.min()),
                         smin_IplusM=float(np.linalg.svd(np.eye(K) + M, compute_uv=False)[-1]),
                         stable_rank=float((sv**2).sum() / sv[0]**2)))
print("step  layer | sign det M | sigma_min(M) | #Re(eig M)<0 | min Re eig(M) | min Re eig(I+M) | sigma_min(I+M) | stable rank M")
for r in rows:
    print(f"{r['step']:>6}  {r['layer']}   |   {r['sign_det_M']:+d}   | {r['smin_M']:.2e} |  {r['n_re_neg_M']:>3}  | {r['min_re_M']:+.3f} | {r['min_re_IplusM']:+.3f} | {r['smin_IplusM']:.3f} | {r['stable_rank']:.1f}")
json.dump(rows, open(sys.argv[2], "w"), indent=1)
