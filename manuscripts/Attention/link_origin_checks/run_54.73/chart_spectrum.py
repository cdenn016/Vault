import sys, json, numpy as np, torch
run = sys.argv[1]
ck = torch.load(run + "/final_model.pt", map_location="cpu", weights_only=False)
sd, cfg = ck["model_state"], json.load(open(run + "/config.json"))["config"]
L, H, K = cfg["n_layers"], cfg["n_heads"], cfg["embed_dim"]; d = K // H
names = ["relational_operators"] + [f"relational_operators_extra.{i}" for i in range(L - 1)]
print("Spectrum of the stacked unrouted operator M = sum_h O_h T_h (64 singular values), versus the stacked O and T")
for l, nm in enumerate(names):
    T = sd[nm + ".T"].double().numpy(); O = sd[nm + ".O"].double().numpy()
    Ost = np.concatenate([O[h] for h in range(H)], axis=1); Tst = np.concatenate([T[h] for h in range(H)], axis=0)
    M = Ost @ Tst
    sM = np.linalg.svd(M, compute_uv=False); sO = np.linalg.svd(Ost, compute_uv=False); sT = np.linalg.svd(Tst, compute_uv=False)
    f = lambda s, r: int(np.sum(s > r * s[0]))
    stable = float((sM**2).sum() / sM[0]**2)
    # fraction of ||M||_F^2 captured by the top-r singular directions
    c = np.cumsum(sM**2) / (sM**2).sum()
    r90 = int(np.searchsorted(c, 0.9) + 1); r99 = int(np.searchsorted(c, 0.99) + 1)
    print(f"layer {l}: #sigma(M) > 0.1*max = {f(sM,0.1)}, > 0.01*max = {f(sM,0.01)}, >1e-3*max = {f(sM,1e-3)} of {K}; stable rank {stable:.1f}; rank for 90% / 99% of ||M||_F^2: {r90} / {r99}")
    print(f"         sigma(O) in [{sO[-1]:.3f},{sO[0]:.2f}]  sigma(T) in [{sT[-1]:.3f},{sT[0]:.2f}]   top sigma(M): {np.round(sM[:4],2)}")
