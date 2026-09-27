"""Replay the archived model on CPU (current VFE_3.0 source) and compare with an independent
float64 implementation of manuscript Algorithm 1. Read-only: nothing is written into any repo."""
import sys, json, math, time, os, warnings
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, r"C:\Users\chris and christine\Desktop\VFE_3.0")
sys.path.insert(0, HERE)
import torch
torch.set_num_threads(1)
from replay_config import archived_kwargs
from vfe3.config import VFE3Config
from vfe3.model.model import VFEModel

RUN = r"D:\DATA_KEEP\31.04_wikitext-103_K256_4-layer_noHM"
SPLIT = sys.argv[2] if len(sys.argv) > 2 else "validation"
VAL = os.path.expanduser(r"~/.cache/tokenized_cache/wikitext-103_%s_tiktoken_tokens.pt" % SPLIT)
t0 = time.time()
val = torch.load(VAL, weights_only=True, map_location="cpu")
val = val if isinstance(val, torch.Tensor) else val["tokens"]
START = int(sys.argv[1]) if len(sys.argv) > 1 else 0
seq = val[START:START + 129].long()
x, y = seq[:128], seq[1:129]
uniq = torch.unique(torch.cat([x, y]))
remap = {int(t): i for i, t in enumerate(uniq.tolist())}
xs = torch.tensor([remap[int(t)] for t in x]).unsqueeze(0)
V = int(uniq.numel())
sd_full = torch.load(os.path.join(RUN, "final_model.pt"), weights_only=True, map_location="cpu", mmap=True)["model_state"]
kw, dropped = archived_kwargs({"vocab_size": V, "amp_dtype": None})
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    cfg = VFE3Config(**kw)
    model = VFEModel(cfg).eval()
sd = {}
for k, v in sd_full.items():
    sd[k] = (v[uniq].clone() if (k.startswith("prior_bank.") and v.dim() >= 1 and v.shape[0] == 50257)
             else v.clone())
res = model.load_state_dict(sd, strict=True)
with torch.no_grad(), warnings.catch_warnings():
    warnings.simplefilter("ignore")
    snap = model.build_diagnostic_snapshot(xs)
    per_layer = model.diagnostics_per_layer(xs, snapshot=snap)

# ---------------- independent float64 implementation of Algorithm 1 (manuscript) ----------------
D = torch.float64
H, d, K, L, N = 8, 32, 256, 4, 128
P = {k: v.to(D) for k, v in sd.items()}
tau = math.sqrt(32.0)
kl_max = 8.0 * K

def block_expm(rows):
    blocks = torch.linalg.matrix_exp(rows.reshape(-1, H, d, d))
    out = torch.zeros(rows.shape[0], K, K, dtype=D)
    for h in range(H):
        out[:, h*d:(h+1)*d, h*d:(h+1)*d] = blocks[:, h]
    return out

X = P["prior_bank.phi_embed"][xs[0]]
Y = P["pos_phi_free"][:N]
U = block_expm(X) @ block_expm(Y)
Uinv = torch.linalg.inv(U)
mu = P["prior_bank.mu_embed"][xs[0]]
Sig = torch.exp(P["prior_bank.sigma_log_embed"][xs[0]]).clamp(min=1e-6)
C = Uinv @ torch.diag_embed(Sig) @ Uinv.transpose(-1, -2)
i_idx = torch.arange(N).unsqueeze(1)
j_idx = torch.arange(N).unsqueeze(0)

def alibi(h):
    b = -(2.0 ** (-h)) * (i_idx - j_idx).to(D)
    return b.masked_fill(j_idx > i_idx, float("-inf"))

def ops(l):
    pre = "relational_operators." if l == 0 else "relational_operators_extra.%d." % (l - 1)
    return P[pre + "raw_score_q"], P[pre + "raw_score_k"], P[pre + "T"], P[pre + "O"]

def kl_rows(a, Vq, b, Vk):
    Lk = torch.linalg.cholesky(Vk)
    Pk = torch.cholesky_inverse(Lk)
    tr = torch.einsum("iab,jab->ij", Vq, Pk)
    delta = a.unsqueeze(1) - b.unsqueeze(0)
    quad = torch.einsum("ijr,jrs,ijs->ij", delta, Pk, delta)
    ld_k = 2 * torch.log(torch.diagonal(Lk, dim1=-2, dim2=-1)).sum(-1)
    ld_q = torch.logdet(Vq)
    return 0.5 * (tr + quad - a.shape[-1] + ld_k.unsqueeze(0) - ld_q.unsqueeze(1))

def layernorm(v, g, b, eps=1e-6):
    m = v.mean(-1, keepdim=True)
    s = v.var(-1, unbiased=False, keepdim=True)
    return (v - m) / torch.sqrt(s + eps) * g + b

def run_alg1(mu0, Sig_route=None, residual=True, record=None):
    Cr = C if Sig_route is None else Uinv @ torch.diag_embed(Sig_route) @ Uinv.transpose(-1, -2)
    mu_l = mu0.clone()
    g, bb = P["block_norm.weight"], P["block_norm.bias"]
    for l in range(L):
        SQ, SK, T, O = ops(l)
        xi = (Uinv @ mu_l.unsqueeze(-1)).squeeze(-1)
        msum = torch.zeros(N, K, dtype=D)
        betas = []
        for h in range(H):
            a = xi @ SQ[h].T
            b = xi @ SK[h].T
            Vq = SQ[h] @ Cr @ SQ[h].T
            Vk = SK[h] @ Cr @ SK[h].T
            Draw = kl_rows(a, Vq, b, Vk)
            DMAX.append((l, float(Draw.masked_fill(j_idx > i_idx, float("-inf")).max()), float(Draw.masked_fill(j_idx > i_idx, float("inf")).min()), float((Draw.masked_fill(j_idx > i_idx, float("nan")) / tau).nanmedian())))
            Dm = Draw.clamp(0.0, kl_max)
            beta = torch.softmax(alibi(h + 1) - Dm / tau, dim=-1)
            betas.append(beta)
            ah = beta @ (xi @ T[h].T)
            msum = msum + ah @ O[h].T
        m = (U @ msum.unsqueeze(-1)).squeeze(-1)
        mu_att = mu_l + m if residual else m
        u = layernorm(mu_att, g, bb)
        fc1w, fc1b = P["block_mlps.%d.fc1.weight" % l], P["block_mlps.%d.fc1.bias" % l]
        fc2w, fc2b = P["block_mlps.%d.fc2.weight" % l], P["block_mlps.%d.fc2.bias" % l]
        mlp = torch.nn.functional.gelu(u @ fc1w.T + fc1b) @ fc2w.T + fc2b
        if record is not None:
            u_m = layernorm(m, g, bb)
            record.append(dict(mu=mu_l.clone(), m=m.clone(), u=u.clone(), beta=torch.stack(betas),
                               ln_resid_sens=((u - u_m).norm(dim=-1) / u_m.norm(dim=-1))))
        mu_l = u + mlp
    return mu_l

def full_vocab_ce(mu_final):
    W = sd_full["prior_bank.output_proj_weight"].to(D)
    bo = sd_full["prior_bank.output_proj_bias"].to(D)
    lu = sd_full["prior_bank.unigram_log_prior"].to(D)
    z = mu_final @ W.T + bo + 1.0 * lu
    return torch.nn.functional.cross_entropy(z, y, reduction="mean").item(), z

DMAX = []
rec = []
with torch.no_grad():
    muL = run_alg1(mu, record=rec)
    ce_ref, z_ref = full_vocab_ce(muL)
    mu_code = snap.final_belief.mu[0].to(D)
    ce_code, z_code = full_vocab_ce(mu_code)
    muL_nores = run_alg1(mu, residual=False)
    ce_nores, _ = full_vocab_ce(muL_nores)
    muL_sigI = run_alg1(mu, Sig_route=torch.ones_like(Sig))
    ce_sigI, _ = full_vocab_ce(muL_sigI)

import csv
csv_rows = list(csv.DictReader(open(os.path.join(RUN, "metrics_per_layer.csv"))))
out = dict(start=START, V_local=V, load=str(res), seconds=round(time.time() - t0, 1),
           code_vs_alg1_max_abs_mu=float((mu_code - muL).abs().max()),
           code_vs_alg1_rel_mu=float((mu_code - muL).norm() / muL.norm()),
           code_vs_alg1_max_abs_logit=float((z_code - z_ref).abs().max()),
           ce_alg1=ce_ref, ce_code=ce_code, ce_no_residual=ce_nores, ce_sigma_identity_routing=ce_sigI,
           layers=[])
for l in range(L):
    cap = snap.layer_conditional_captures[l]
    beta_code = cap["beta_pre"][0].to(D)
    r = rec[l]
    mun = r["mu"].norm(dim=-1)
    mn = r["m"].norm(dim=-1)
    out["layers"].append(dict(
        csv_displacement=float(csv_rows[l]["relational_mean_displacement_norm"]),
        code_displacement=float(per_layer["relational_mean_displacement_norm"][l]),
        alg1_displacement=float(r["m"].norm()),
        csv_attn_entropy=float(csv_rows[l]["attn_entropy"]),
        code_attn_entropy=float(per_layer["attn_entropy"][l]),
        csv_cov_min_eig=float(csv_rows[l]["relational_projected_cov_min_eigenvalue"]),
        code_cov_min_eig=float(per_layer["relational_projected_cov_min_eigenvalue"][l]),
        csv_cov_max_cond=float(csv_rows[l]["relational_projected_cov_max_condition"]),
        code_cov_max_cond=float(per_layer["relational_projected_cov_max_condition"][l]),
        beta_max_abs_diff_code_vs_alg1=float((beta_code - r["beta"]).abs().max()),
        mu_token_norm_median=float(mun.median()), mu_token_norm_max=float(mun.max()),
        m_token_norm_median=float(mn.median()), m_token_norm_min=float(mn.min()),
        ratio_m_over_mu_median=float((mn / mun).median()), ratio_m_over_mu_min=float((mn / mun).min()),
        ln_residual_sensitivity_median=float(r["ln_resid_sens"].median()),
        ln_residual_sensitivity_max=float(r["ln_resid_sens"].max()),
        self_weight_mean=float(torch.diagonal(r["beta"], dim1=-2, dim2=-1).mean()),
    ))
sig_all = sd_full["prior_bank.sigma_log_embed"].to(D)
out["sigma_log_table"] = dict(rms=float(sig_all.pow(2).mean().sqrt()), absmax=float(sig_all.abs().max()),
                             frac_var_within_10pct=float(((sig_all.exp() > 0.9) & (sig_all.exp() < 1.1)).double().mean()),
                             seq_tokens_var_min=float(Sig.min()), seq_tokens_var_max=float(Sig.max()),
                             seq_tokens_var_median=float(Sig.median()))
out["dmax"] = DMAX[:32]
print(json.dumps({"start": START, "split": SPLIT, "dmax_by_layer": [max(v[1] for v in DMAX[:32] if v[0] == l) for l in range(4)], "dmin_by_layer": [min(v[2] for v in DMAX[:32] if v[0] == l) for l in range(4)], "median_D_over_tau_by_layer": [sorted(v[3] for v in DMAX[:32] if v[0] == l)[4] for l in range(4)]}))


