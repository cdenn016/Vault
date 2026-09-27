# Weights-only, CPU-only, single-thread inspection of the archived final checkpoint.
# Never builds or runs the model. Computes norms/spectra of stored tensors only,
# plus clearly labeled synthetic evaluations of the coordinate MLP on LN-shaped inputs.
import json, math, sys
import torch
torch.set_num_threads(1)
torch.manual_seed(0)
P = r"D:/DATA_KEEP/31.04_wikitext-103_K256_4-layer_noHM/final_model.pt"
OUTP = sys.argv[1]
ck = torch.load(P, weights_only=True, map_location="cpu")
sd = ck["model_state"]
out = {"names": {k: [list(v.shape), str(v.dtype)] for k, v in sd.items()}}
for k, v in sd.items():
    print(k, tuple(v.shape), v.dtype)

def q(x, ps=(0.0, 0.01, 0.05, 0.25, 0.5, 0.75, 0.95, 0.99, 1.0)):
    x = x.flatten().double()
    xs, _ = torch.sort(x)
    n = len(xs)
    qs = [float(xs[min(int(round(p * (n - 1))), n - 1)]) for p in ps]
    d = {"q%03d" % int(round(p * 100)): v for p, v in zip(ps, qs)}
    d.update(mean=float(x.mean()), std=float(x.std()), rms=float(x.square().mean().sqrt()))
    return d

V, K = sd["prior_bank.mu_embed"].shape
mu = sd["prior_bank.mu_embed"].double()
rown = mu.norm(dim=1)
out["mu_embed"] = {"fro": float(mu.norm()), "row_norm": q(rown), "rms_row_norm": float(mu.norm() / math.sqrt(V))}
print("mu_embed", out["mu_embed"])
s = sd["prior_bank.sigma_log_embed"].double()
var = s.exp()
tr = var.sum(1)
cond = var.max(1).values / var.min(1).values
out["sigma_log_embed"] = {"fro": float(s.norm()), "entries": q(s), "variance": q(var),
                          "trace": q(tr), "trace_cv": float(tr.std() / tr.mean()),
                          "row_condition": q(cond), "frac_abs_lt_0p1": float((s.abs() < 0.1).double().mean()),
                          "init_log15": math.log(15.0)}
print("sigma_log_embed", out["sigma_log_embed"])
del s, var
phi = sd["prior_bank.phi_embed"]
pr = phi.double().norm(dim=1)
out["phi_embed"] = {"fro": float(phi.double().norm()), "row_fro": q(pr),
                    "frac_rows_ge_11p99": float((pr >= 11.99).double().mean()),
                    "n_rows_ge_11p99": int((pr >= 11.99).sum())}
print("phi_embed", out["phi_embed"])
gen = torch.Generator().manual_seed(0)
idx = torch.randperm(V, generator=gen)[:1500]
idx = torch.unique(torch.cat([idx, torch.arange(0, 500)]))
blocks = phi[idx].double().reshape(-1, 8, 32, 32)
spec = torch.linalg.matrix_norm(blocks, ord=2)
Uexp = torch.linalg.matrix_exp(blocks)
svU = torch.linalg.svdvals(Uexp)
condU = svU[..., 0] / svU[..., -1]
tr_blk = torch.diagonal(blocks, dim1=-2, dim2=-1).sum(-1)
out["phi_embed_sample"] = {"n_rows": int(len(idx)), "block_spectral": q(spec), "block_trace": q(tr_blk),
                           "exp_block_cond": q(condU), "exp_block_logdet": q(torch.linalg.slogdet(Uexp)[1])}
print("phi sample", out["phi_embed_sample"])
pp = sd.get("pos_phi_free")
if pp is not None:
    ppr = pp.double().reshape(pp.shape[0], -1).norm(dim=1)
    pb = pp.double().reshape(pp.shape[0], 8, 32, 32)
    svp = torch.linalg.svdvals(torch.linalg.matrix_exp(pb))
    out["pos_phi_free"] = {"shape": list(pp.shape), "row_fro": q(ppr),
                           "block_spectral": q(torch.linalg.matrix_norm(pb, ord=2)),
                           "exp_block_cond": q(svp[..., 0] / svp[..., -1])}
    print("pos_phi", out["pos_phi_free"])
layers = {0: "relational_operators."}
for e in range(3):
    layers[e + 1] = "relational_operators_extra.%d." % e
rel = {}
I32 = torch.eye(32, dtype=torch.float64)
for L, pre in layers.items():
    SQ = sd[pre + "raw_score_q"].double(); SK = sd[pre + "raw_score_k"].double()
    T = sd[pre + "T"].double(); O = sd[pre + "O"].double()
    r = {"fro": {"SQ": float(SQ.norm()), "SK": float(SK.norm()), "T": float(T.norm()), "O": float(O.norm())}}
    svq = torch.linalg.svdvals(SQ); svk = torch.linalg.svdvals(SK)
    r["SQ_sv"] = {"min": float(svq.min()), "max": float(svq.max()), "median": float(svq.median()),
                  "cond_per_head": [float(x) for x in (svq[:, 0] / svq[:, -1])]}
    r["SK_sv"] = {"min": float(svk.min()), "max": float(svk.max()), "median": float(svk.median()),
                  "cond_per_head": [float(x) for x in (svk[:, 0] / svk[:, -1])]}
    GQ = SQ @ SQ.transpose(-1, -2); GK = SK @ SK.transpose(-1, -2)
    lam = torch.linalg.eigvals(torch.linalg.solve(GK, GQ)).real
    r["relative_gain_sqrt_eig"] = {"min": float(lam.clamp(min=0).sqrt().min()), "max": float(lam.clamp(min=0).sqrt().max()),
                                   "median": float(lam.clamp(min=0).sqrt().median())}
    r["geo_mean_sv"] = {"SQ": [float(x) for x in svq.log().mean(-1).exp()], "SK": [float(x) for x in svk.log().mean(-1).exp()]}
    Qq = torch.linalg.qr(SQ.transpose(-1, -2)).Q; Qk = torch.linalg.qr(SK.transpose(-1, -2)).Q
    cosines = torch.linalg.svdvals(Qq.transpose(-1, -2) @ Qk)
    r["rowspace_cosines"] = {"min": float(cosines.min()), "median": float(cosines.median()), "max": float(cosines.max())}
    OT = O @ T; TO = T @ O
    svOT = torch.linalg.svdvals(OT)
    r["OT_sv"] = {"max_per_head": [float(x) for x in svOT[:, 0]], "sv32_per_head": [float(x) for x in svOT[:, 31]],
                  "median_top32": float(svOT[:, :32].median())}
    eTO = torch.linalg.eigvals(TO)
    r["TO_eig_abs"] = {"max": float(eTO.abs().max()), "min": float(eTO.abs().min()), "median": float(eTO.abs().median())}
    r["composition_defect_rms"] = [float(x) for x in ((TO - I32).norm(dim=(-2, -1)) / math.sqrt(32))]
    r["T_head_fro"] = [float(x) for x in T.norm(dim=(-2, -1))]
    r["O_head_fro"] = [float(x) for x in O.norm(dim=(-2, -1))]
    svS = torch.linalg.svdvals(OT.sum(0))
    r["sum_h_OT_sv"] = {"max": float(svS.max()), "min": float(svS.min()), "median": float(svS.median())}
    rel[L] = r
    print("layer", L, json.dumps(r))
out["relational"] = rel
g = sd["block_norm.weight"].double(); b = sd["block_norm.bias"].double()
out["block_norm"] = {"gamma": q(g), "gamma_fro": float(g.norm()), "beta": q(b), "beta_fro": float(b.norm()),
                     "LN_output_norm_bounds": [float(16.0 * g.abs().min() - b.norm()), float(16.0 * g.abs().max() + b.norm())]}
print("block_norm", out["block_norm"])
W = sd["prior_bank.output_proj_weight"].double(); bo = sd["prior_bank.output_proj_bias"].double()
svW = torch.linalg.svdvals(W)
out["decoder"] = {"W_fro": float(W.norm()), "W_sv_max": float(svW.max()), "W_sv_min": float(svW.min()),
                  "W_row_norm": q(W.norm(dim=1)), "bias": q(bo)}
print("decoder", out["decoder"])
mlp = {}
zs = torch.randn(4096, 256, dtype=torch.float64)
zs = (zs - zs.mean(1, keepdim=True)) / zs.std(1, unbiased=False, keepdim=True)
u = zs * g + b
for L in range(4):
    W1 = sd["block_mlps.%d.fc1.weight" % L].double(); b1 = sd["block_mlps.%d.fc1.bias" % L].double()
    W2 = sd["block_mlps.%d.fc2.weight" % L].double(); b2 = sd["block_mlps.%d.fc2.bias" % L].double()
    s1 = float(torch.linalg.matrix_norm(W1, ord=2)); s2 = float(torch.linalg.matrix_norm(W2, ord=2))
    mo = torch.nn.functional.gelu(u @ W1.T + b1) @ W2.T + b2
    y = u + mo
    un = u.norm(dim=1)
    bound = s2 * (s1 * float(un.max()) + float(b1.norm())) + float(b2.norm())
    mlp[L] = {"fc1_spec": s1, "fc2_spec": s2, "upper_bound_mlp_out": bound,
              "synthetic_u_norm": q(un), "synthetic_mlp_out_norm": q(mo.norm(dim=1)),
              "synthetic_mu_next_norm": q(y.norm(dim=1)), "upper_bound_mu_next": float(un.max()) + bound}
    print("mlp", L, json.dumps(mlp[L]))
out["mlp"] = mlp
out["other"] = {k: list(v.shape) for k, v in sd.items()
                if not any(k.startswith(p) for p in ("prior_bank.", "relational_operators", "block_", "pos_phi"))}
json.dump(out, open(OUTP, "w"), indent=1)
print("DONE")
