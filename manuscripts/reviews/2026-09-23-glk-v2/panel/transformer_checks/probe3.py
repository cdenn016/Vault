import json, math, torch
src = open("fwd_probe.py", encoding="utf-8").read()
exec(src.split("def tv(")[0])
out = {}
for name, text in TEXTS.items():
    ids = enc.encode(text)[:128]; N = len(ids); idt = torch.tensor(ids)
    mu = P["prior_bank.mu_embed"][idt].clone(); sig = torch.exp(P["prior_bank.sigma_log_embed"][idt])
    X = P["prior_bank.phi_embed"][idt].reshape(N, H, d, d); Y = P["pos_phi_free"][:N].reshape(N, H, d, d)
    U = torch.matrix_exp(X) @ torch.matrix_exp(Y); Uinv = torch.matrix_exp(-Y) @ torch.matrix_exp(-X)
    Bp = alibi(N); g, bb = P["block_norm.weight"], P["block_norm.bias"]; allowed = torch.isfinite(Bp)
    rows = []
    for l, ops in enumerate(LAYERS):
        m, ex = layer_attention(ops, mu, U, Uinv, sig, Bp)
        a, b, VK = ex["a"], ex["b"], ex["VK"]
        Pbar = torch.linalg.inv(VK.mean(0))              # (H,r,r) sequence-shared key metric
        Wh = torch.linalg.cholesky(Pbar)
        qv = torch.einsum("hba,ihb->iha", Wh, a); kv = torch.einsum("hba,jhb->jha", Wh, b)
        dot = torch.einsum("iha,jha->hij", qv, kv); kn = (kv**2).sum(-1).T.unsqueeze(1).expand(H, N, N)
        p_dot = torch.softmax(dot/TAU + Bp, -1); p_bias = torch.softmax(dot/TAU - kn/(2*TAU) + Bp, -1)
        L1 = (p_bias - p_dot).abs().sum(-1)                     # (H,N)
        knm = torch.where(allowed, kn, torch.nan)
        eps = (torch.nan_to_num(knm, nan=-1e300).amax(-1) - torch.nan_to_num(knm, nan=1e300).amin(-1))/(4*TAU)
        sharp = 2*torch.tanh(eps/2); stated = torch.expm1(2*eps)
        sel = (slice(None), slice(1, None))
        rows.append(dict(layer=l, L1_median=float(L1[sel].median()), eps_median=float(eps[sel].median()),
                         sharp_median=float(sharp[sel].median()), stated_median=float(stated[sel].median()),
                         frac_rows_stated_vacuous=float((stated[sel] >= 2).double().mean()),
                         violations_sharp=int((L1[sel] > sharp[sel] + 1e-12).sum()),
                         violations_stated=int((L1[sel] > stated[sel] + 1e-12).sum())))
        u = ln(mu + m, g, bb)
        W1, b1 = P["block_mlps.%d.fc1.weight" % l], P["block_mlps.%d.fc1.bias" % l]
        W2, b2 = P["block_mlps.%d.fc2.weight" % l], P["block_mlps.%d.fc2.bias" % l]
        mu = u + gelu(u @ W1.T + b1) @ W2.T + b2
    out[name] = rows
print(json.dumps(out, indent=1))
