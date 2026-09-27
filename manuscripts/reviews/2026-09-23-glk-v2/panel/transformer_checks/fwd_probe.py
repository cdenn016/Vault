"""Independent float64 CPU recomputation of the featured run's predictive-content forward pass
from saved tensors (weights_only load), for L1/L3/L4 diagnostics. Read-only; no model code executed."""
import math, json, sys
import torch
torch.set_num_threads(1)
torch.set_default_dtype(torch.float64)
CK = r"D:/DATA_KEEP/31.04_wikitext-103_K256_4-layer_noHM/final_model.pt"
ck = torch.load(CK, weights_only=True, map_location="cpu")
P = {k: v.double() for k, v in ck["model_state"].items()}
cfg = ck["config"]
K, H, d = 256, 8, 32
TAU = math.sqrt(32.0); KLMAX = float(cfg["kl_max"]); LN_EPS = float(cfg["eps"])
assert cfg["kappa_beta"] == 1 and cfg["alibi_slope"] == 1 and cfg["beta_attention_prior"] == "causal_alibi"
LAYERS = ["relational_operators"] + ["relational_operators_extra.%d" % i for i in range(3)]

import tiktoken
enc = tiktoken.get_encoding("gpt2")
TEXTS = {
 "wikitext_style": " = Robert Boulter = \n Robert Boulter is an English film , television and theatre actor . He had a guest @-@ starring role on the television series The Bill in 2000 . This was followed by a starring role in the play Herons written by Simon Stephens , which was performed in 2001 at the Royal Court Theatre . He had a guest role in the television series Judge John Deed in 2002 . In 2004 Boulter landed a role as ' Craig ' in the episode ' Teddy 's Story ' of the television series The Long Firm ; he starred alongside actors Mark Strong and Derek Jacobi . He was cast in the 2005 theatre productions of the Philip Ridley play Mercury Fur , which was performed at the Drum Theatre in Plymouth and the Menier Chocolate Factory in London .",
 "science_style": " The river rises in the hills north of the town and flows south for about 40 kilometres before it joins the larger river near the coast . During the nineteenth century the valley was used for farming , and several mills were built along its banks . The railway reached the area in 1862 , and the population of the town grew rapidly as a result . Today the valley is known for its woodland and its wildlife , including several species of birds that are rare elsewhere in the country . The local council has created a nature reserve that covers most of the lower valley , and a walking path follows the river from its source to the sea .",
}

def bd_apply(M, v):   # M (N,H,d,d), v (N,K) -> (N,K)
    N = v.shape[0]
    return torch.einsum("nhij,nhj->nhi", M, v.reshape(N, H, d)).reshape(N, K)

def ln(x, g, b):
    mu = x.mean(-1, keepdim=True); var = x.var(-1, unbiased=False, keepdim=True)
    return (x - mu)/torch.sqrt(var + LN_EPS)*g + b

def gelu(x): return 0.5*x*(1+torch.erf(x/math.sqrt(2)))

def alibi(N):
    i = torch.arange(N).view(-1, 1); j = torch.arange(N).view(1, -1)
    slopes = torch.tensor([2.0**(-h) for h in range(1, H+1)]).view(H, 1, 1)
    B = -slopes*(i - j).abs().double()
    return B.masked_fill(~(j <= i).unsqueeze(0), float("-inf"))

def layer_attention(ops, mu, U, Uinv, sig, Bprior, want_parts=False):
    N = mu.shape[0]
    xi = bd_apply(Uinv, mu)                                   # (N,K) reference mean
    Cb = Uinv @ torch.diag_embed(sig.reshape(N, H, d)) @ Uinv.transpose(-1, -2)   # (N,H,d,d)
    C = torch.zeros(N, K, K)
    for h in range(H):
        C[:, h*d:(h+1)*d, h*d:(h+1)*d] = Cb[:, h]
    SQ, SK = P[ops + ".raw_score_q"], P[ops + ".raw_score_k"]   # (H,r,K)
    T, O = P[ops + ".T"], P[ops + ".O"]                        # (H,r,K), (H,K,r)
    a = torch.einsum("hrk,nk->nhr", SQ, xi); b = torch.einsum("hrk,nk->nhr", SK, xi)
    VQ = torch.einsum("hrk,nkl,hsl->nhrs", SQ, C, SQ); VK = torch.einsum("hrk,nkl,hsl->nhrs", SK, C, SK)
    VQ = 0.5*(VQ + VQ.transpose(-1, -2)); VK = 0.5*(VK + VK.transpose(-1, -2))
    Pk = torch.linalg.inv(VK)
    r = SQ.shape[1]
    tr = torch.einsum("jhab,ihba->hij", Pk, VQ)
    ldK = torch.linalg.slogdet(VK)[1].T      # (H,N)
    ldQ = torch.linalg.slogdet(VQ)[1].T
    aPa = torch.einsum("iha,jhab,ihb->hij", a, Pk, a)
    aPb = torch.einsum("iha,jhab,jhb->hij", a, Pk, b)
    bPb = torch.einsum("jha,jhab,jhb->hj", b, Pk, b).unsqueeze(1)
    static = 0.5*(tr - r + ldK.unsqueeze(1) - ldQ.unsqueeze(2))          # covariance-only terms
    meanpart = 0.5*(aPa - 2*aPb + bPb)                                    # Mahalanobis with key metric
    D = (static + meanpart).clamp(0.0, KLMAX)
    logits = -D/TAU + Bprior
    beta = torch.softmax(logits, -1)
    values = torch.einsum("hrk,nk->nhr", T, xi)
    pooled = torch.einsum("hij,jhr->ihr", beta, values)
    body = torch.einsum("hkr,nhr->nk", O, pooled)
    m = bd_apply(U, body)
    extra = dict(static=static, meanpart=meanpart, D=D, beta=beta, a=a, b=b, VQ=VQ, VK=VK, Pk=Pk, xi=xi, C=C, Cb=Cb)
    return m, extra

def run(ids, residual_mode="normal", collect=True):
    N = len(ids); idt = torch.tensor(ids)
    mu = P["prior_bank.mu_embed"][idt].clone()
    sig = torch.exp(P["prior_bank.sigma_log_embed"][idt]).clamp(min=1e-6)
    X = P["prior_bank.phi_embed"][idt].reshape(N, H, d, d); Y = P["pos_phi_free"][:N].reshape(N, H, d, d)
    U = torch.matrix_exp(X) @ torch.matrix_exp(Y); Uinv = torch.matrix_exp(-Y) @ torch.matrix_exp(-X)
    Bp = alibi(N); g, bb = P["block_norm.weight"], P["block_norm.bias"]
    rec = []
    for l, ops in enumerate(LAYERS):
        m, ex = layer_attention(ops, mu, U, Uinv, sig, Bp)
        if residual_mode == "normal": x = mu + m
        elif residual_mode == "no_residual": x = m
        elif residual_mode == "no_message": x = mu
        u = ln(x, g, bb)
        if collect:
            u_nores = ln(m, g, bb)
            rec.append(dict(layer=l,
                mu_norm_median=float(mu.norm(dim=-1).median()), mu_norm_max=float(mu.norm(dim=-1).max()),
                m_norm_median=float(m.norm(dim=-1).median()), m_norm_min=float(m.norm(dim=-1).min()),
                m_frob=float(m.norm()), ratio_median=float((m.norm(dim=-1)/mu.norm(dim=-1)).median()),
                ratio_min=float((m.norm(dim=-1)/mu.norm(dim=-1)).min()),
                ln_rel_change_median=float(((u - u_nores).norm(dim=-1)/(u - bb).norm(dim=-1)).median()),
                ln_rel_change_max=float(((u - u_nores).norm(dim=-1)/(u - bb).norm(dim=-1)).max()),
                extra=ex))
        W1, b1 = P["block_mlps.%d.fc1.weight" % l], P["block_mlps.%d.fc1.bias" % l]
        W2, b2 = P["block_mlps.%d.fc2.weight" % l], P["block_mlps.%d.fc2.bias" % l]
        mu = u + gelu(u @ W1.T + b1) @ W2.T + b2
    logits = mu @ P["prior_bank.output_proj_weight"].T + P["prior_bank.output_proj_bias"] + 1.0*P["prior_bank.unigram_log_prior"]
    lp = torch.log_softmax(logits, -1)
    tgt = torch.tensor(ids[1:])
    ce = float(-lp[:-1].gather(1, tgt.view(-1, 1)).mean())
    return ce, rec, dict(U=U, Uinv=Uinv, sig=sig, X=X, Y=Y)

def tv(p, q, mask):
    return float((0.5*(p - q).abs().sum(-1))[mask].mean())

out = {"checkpoint": CK}
# --- table-level statistics
ls = P["prior_bank.sigma_log_embed"]
out["log_sigma_table"] = dict(rms=float(ls.pow(2).mean().sqrt()), mean=float(ls.mean()),
    q01=float(ls.flatten().kthvalue(int(0.01*ls.numel())).values), q99=float(ls.flatten().kthvalue(int(0.99*ls.numel())).values),
    frac_abs_lt_0p2=float((ls.abs() < 0.2).double().mean()))
mu_tab = P["prior_bank.mu_embed"]
out["mu_table_frob"] = float(mu_tab.norm()); out["mu_table_row_rms"] = float(mu_tab.norm()/math.sqrt(mu_tab.shape[0]))
out["phi_table_frob"] = float(P["prior_bank.phi_embed"].norm()); out["pos_phi_frob"] = float(P["pos_phi_free"].norm())
out["ln_gamma_norm"] = float(P["block_norm.weight"].norm()); out["ln_bias_norm"] = float(P["block_norm.bias"].norm())
# logged-diagnostic reproduction: raw min singular values and O T max singular values per layer
lay = []
for l, ops in enumerate(LAYERS):
    sq = torch.linalg.svdvals(P[ops + ".raw_score_q"]).min(); sk = torch.linalg.svdvals(P[ops + ".raw_score_k"]).min()
    OT = P[ops + ".O"] @ P[ops + ".T"]
    lay.append(dict(layer=l, sq_min=float(sq), sk_min=float(sk), OT_max_sv=float(torch.linalg.svdvals(OT).max()),
                    SQ_frob=float(P[ops + ".raw_score_q"].norm()), T_frob=float(P[ops + ".T"].norm()), O_frob=float(P[ops + ".O"].norm())))
out["per_layer_maps"] = lay

for name, text in TEXTS.items():
    ids = enc.encode(text)[:128]
    N = len(ids)
    ce, rec, fr = run(ids)
    ce_nores, _, _ = run(ids, "no_residual", collect=False)
    ce_nomsg, _, _ = run(ids, "no_message", collect=False)
    res = dict(n_tokens=N, ce=ce, ce_no_attention_residual=ce_nores, ce_no_attention_message=ce_nomsg)
    mask = torch.zeros(H, N, dtype=torch.bool); mask[:, 1:] = True
    layers_out = []
    for r_ in rec:
        ex = r_.pop("extra")
        beta, static, meanpart = ex["beta"], ex["static"], ex["meanpart"]
        Bp = alibi(N)
        allowed = torch.isfinite(Bp)
        def rowstd(Z):
            Zm = torch.where(allowed, Z, torch.nan)
            return float(torch.nanmean(torch.sqrt(torch.nanmean((Zm - torch.nanmean(Zm, -1, keepdim=True))**2, -1))[:, 1:]))
        r_["row_std_static_over_tau"] = rowstd(static/TAU)
        r_["row_std_mean_over_tau"] = rowstd(meanpart/TAU)
        r_["row_std_alibi"] = rowstd(torch.where(allowed, Bp, torch.zeros_like(Bp)))
        r_["row_std_total_logit"] = rowstd(-ex["D"]/TAU + torch.where(allowed, Bp, torch.zeros_like(Bp)))
        # drop static pair bias (replace by its row mean on the allowed support)
        sm = torch.where(allowed, static, torch.nan); rowmean = torch.nanmean(sm, -1, keepdim=True)
        beta_nostatic = torch.softmax(-((rowmean + meanpart).clamp(0, KLMAX))/TAU + Bp, -1)
        r_["tv_drop_static_pair_bias"] = tv(beta, beta_nostatic, mask)
        # shared key covariance within the sequence (head-wise mean of V_K) -> Prop. specialization
        VKbar = ex["VK"].mean(0, keepdim=True).expand_as(ex["VK"]); Pbar = torch.linalg.inv(VKbar)
        a, b, VQ = ex["a"], ex["b"], ex["VQ"]
        trb = torch.einsum("jhab,ihba->hij", Pbar, VQ)
        Dsh = 0.5*(trb - 32 + torch.linalg.slogdet(VKbar)[1].T.unsqueeze(1) - torch.linalg.slogdet(VQ)[1].T.unsqueeze(2)
                   + torch.einsum("iha,jhab,ihb->hij", a, Pbar, a) - 2*torch.einsum("iha,jhab,jhb->hij", a, Pbar, b)
                   + torch.einsum("jha,jhab,jhb->hj", b, Pbar, b).unsqueeze(1))
        beta_shared = torch.softmax(-Dsh.clamp(0, KLMAX)/TAU + Bp, -1)
        r_["tv_shared_key_covariance"] = tv(beta, beta_shared, mask)
        # dot product without the key-norm bias under the shared covariance
        Wh = torch.linalg.cholesky(Pbar[0])      # (H,r,r) lower, Pbar = W W^T
        qv = torch.einsum("hba,ihb->iha", Wh, a); kv = torch.einsum("hba,jhb->jha", Wh, b)
        dot = torch.einsum("iha,jha->hij", qv, kv)
        knorm = (kv**2).sum(-1).T.unsqueeze(1)
        beta_dot = torch.softmax(dot/TAU + Bp, -1)
        beta_biased = torch.softmax(dot/TAU - knorm/(2*TAU) + Bp, -1)
        r_["tv_shared_vs_biased_dot_identity"] = tv(beta_shared, beta_biased, mask)
        r_["tv_full_vs_plain_dot"] = tv(beta, beta_dot, mask)
        kn = torch.where(allowed, knorm.expand(H, N, N), torch.nan)
        eps_rows = (torch.nan_to_num(kn, nan=-1e300).amax(-1) - torch.nan_to_num(kn, nan=1e300).amin(-1))/(4*TAU)
        r_["key_norm_eps_median"] = float(eps_rows[:, 1:].median())
        r_["self_mass_mean"] = float(torch.diagonal(beta, dim1=-2, dim2=-1)[:, 1:].mean())
        r_["attn_entropy_mean"] = float((-(beta*torch.log(beta.clamp_min(1e-300))).sum(-1))[:, 1:].mean())
        layers_out.append(r_)
    res["layers"] = layers_out
    # covariance vs frame Gram inverse, frames
    U, Uinv, sig = fr["U"], fr["Uinv"], fr["sig"]
    Cb = Uinv @ torch.diag_embed(sig.reshape(N, H, d)) @ Uinv.transpose(-1, -2)
    G_inv = Uinv @ Uinv.transpose(-1, -2)
    res["C_vs_frameGramInv_rel_frob_median"] = float(((Cb - G_inv).norm(dim=(-2, -1))/Cb.norm(dim=(-2, -1))).median())
    res["passage_log_sigma_rms"] = float(torch.log(sig).pow(2).mean().sqrt())
    sv = torch.linalg.svdvals(U)
    res["frame_block_cond_median"] = float((sv[..., 0]/sv[..., -1]).median()); res["frame_block_cond_max"] = float((sv[..., 0]/sv[..., -1]).max())
    res["frame_block_sv_max"] = float(sv[..., 0].max()); res["frame_block_sv_min"] = float(sv[..., -1].min())
    X = fr["X"]; Xbar = X.mean(0, keepdim=True)
    res["token_frame_dispersion_rel"] = float(((X - Xbar).flatten(1).norm(dim=-1)/X.flatten(1).norm(dim=-1)).median())
    Yt = fr["Y"]; res["pos_frame_step_rel_median"] = float(((Yt[1:] - Yt[:-1]).flatten(1).norm(dim=-1)/Yt[1:].flatten(1).norm(dim=-1)).median())
    res["mu0_norm_median"] = float(P["prior_bank.mu_embed"][torch.tensor(ids)].norm(dim=-1).median())
    out[name] = res
print(json.dumps(out, indent=1))
