import json, math, torch
src = open("fwd_probe.py", encoding="utf-8").read()
exec(src.split("def tv(")[0])
out = {}
for name, text in TEXTS.items():
    ids = enc.encode(text)[:128]; N = len(ids); idt = torch.tensor(ids)
    mu = P["prior_bank.mu_embed"][idt].clone()
    sig = torch.exp(P["prior_bank.sigma_log_embed"][idt])
    X = P["prior_bank.phi_embed"][idt].reshape(N, H, d, d); Y = P["pos_phi_free"][:N].reshape(N, H, d, d)
    U = torch.matrix_exp(X) @ torch.matrix_exp(Y); Uinv = torch.matrix_exp(-Y) @ torch.matrix_exp(-X)
    Bp = alibi(N); g, bb = P["block_norm.weight"], P["block_norm.bias"]
    rows = []
    for l, ops in enumerate(LAYERS):
        m, ex = layer_attention(ops, mu, U, Uinv, sig, Bp)
        u = ln(mu + m, g, bb)
        W1, b1 = P["block_mlps.%d.fc1.weight" % l], P["block_mlps.%d.fc1.bias" % l]
        W2, b2 = P["block_mlps.%d.fc2.weight" % l], P["block_mlps.%d.fc2.bias" % l]
        f = gelu(u @ W1.T + b1) @ W2.T + b2
        xc = (mu - mu.mean(0, keepdim=True)); s = torch.linalg.svdvals(xc); p = s/s.sum()
        erank_in = float(torch.exp(-(p*torch.log(p.clamp_min(1e-300))).sum()))
        beta = ex["beta"]
        rows.append(dict(layer=l, mlp_branch_over_u_median=float((f.norm(dim=-1)/u.norm(dim=-1)).median()),
                         stream_effective_rank_input=erank_in,
                         D_max=float(ex["D"].max()), D_median=float(ex["D"][torch.isfinite(Bp)].median()),
                         mass_on_pos0_by_head_rows_ge_64=[float(beta[h, 64:, 0].mean()) for h in range(H)],
                         self_mass_by_head=[float(torch.diagonal(beta[h])[1:].mean()) for h in range(H)]))
        mu = u + f
    xc = (mu - mu.mean(0, keepdim=True)); s = torch.linalg.svdvals(xc); p = s/s.sum()
    rows.append(dict(final_stream_effective_rank=float(torch.exp(-(p*torch.log(p.clamp_min(1e-300))).sum()))))
    out[name] = rows
print(json.dumps(out, indent=1))
