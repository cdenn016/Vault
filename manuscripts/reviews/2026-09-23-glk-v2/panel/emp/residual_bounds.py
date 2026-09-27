# Rigorous per-layer bounds on ||mu^(l)|| from stored weights (no forward pass), combined with the
# archived per-layer message norms (relational_mean_displacement_norm over one 128-token window).
import json, math, torch
torch.set_num_threads(1)
ck = torch.load(r"D:/DATA_KEEP/31.04_wikitext-103_K256_4-layer_noHM/final_model.pt", weights_only=True, map_location="cpu")
sd = ck["model_state"]
g = sd["block_norm.weight"].double(); b = sd["block_norm.bias"].double()
K = g.numel()
B_u = math.sqrt(K) * float(g.abs().max()) + float(b.norm())      # ||gamma*zhat+b|| with ||zhat||<=sqrt(K)
disp = {0: 740908.8125, 1: 733558.0, 2: 1087101.875, 3: 371354.78125}   # metrics_per_layer.csv
ntok = 128
mu_rows = sd["prior_bank.mu_embed"].double().norm(dim=1)
res = {"B_u": B_u, "mu_row_median": float(mu_rows.median()), "mu_row_max": float(mu_rows.max())}
for L in range(4):
    W1 = sd["block_mlps.%d.fc1.weight" % L].double(); b1 = sd["block_mlps.%d.fc1.bias" % L].double()
    W2 = sd["block_mlps.%d.fc2.weight" % L].double(); b2 = sd["block_mlps.%d.fc2.bias" % L].double()
    s1 = float(torch.linalg.matrix_norm(W1, ord=2)); s2 = float(torch.linalg.matrix_norm(W2, ord=2))
    res["mlp%d" % L] = {"fc1_spec": s1, "fc2_spec": s2, "b1": float(b1.norm()), "b2": float(b2.norm()),
                         "B_mu_next": B_u + s2 * (s1 * B_u + float(b1.norm())) + float(b2.norm())}
for L in range(4):
    m_rms = disp[L] / math.sqrt(ntok)
    if L == 0:
        lo = m_rms / float(mu_rows.max()); typ = m_rms / float(mu_rows.median())
        res["layer0"] = {"m_rms_per_token": m_rms, "ratio_lower_bound_vs_max_row": lo, "ratio_vs_median_row": typ}
    else:
        Bmu = res["mlp%d" % (L - 1)]["B_mu_next"]
        res["layer%d" % L] = {"m_rms_per_token": m_rms, "B_mu_rigorous": Bmu, "ratio_lower_bound": m_rms / Bmu}
print(json.dumps(res, indent=1))
