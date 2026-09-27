# Weight-only statistics (no text, no forward pass): for sampled token types and three positions,
# the reference covariance C = U^-1 Sigma U^-T with U = exp(X_tok) exp(Y_pos) (block diagonal),
# and the static key term (1/2) log det(S_K C S_K^T)/tau of layer-0 maps (a per-key logit bias).
import math, torch
torch.set_num_threads(1); torch.manual_seed(0)
ck = torch.load(r"D:/DATA_KEEP/31.04_wikitext-103_K256_4-layer_noHM/final_model.pt", weights_only=True, map_location="cpu")
sd = ck["model_state"]
phi = sd["prior_bank.phi_embed"]; slog = sd["prior_bank.sigma_log_embed"].double(); pos = sd["pos_phi_free"].double()
SK = sd["relational_operators.raw_score_k"].double(); SQ = sd["relational_operators.raw_score_q"].double()
tau = math.sqrt(32.0)
ids = torch.cat([torch.arange(0, 400), torch.randperm(50257)[:400]])
X = phi[ids].double().reshape(-1, 8, 32, 32)
Ut = torch.linalg.matrix_exp(X)                                   # token factor
def blockdiag(Ub):                                                # (n,8,32,32) -> (n,256,256)
    n = Ub.shape[0]; M = torch.zeros(n, 256, 256, dtype=Ub.dtype)
    for b in range(8):
        M[:, 32*b:32*(b+1), 32*b:32*(b+1)] = Ub[:, b]
    return M
out = {}
for p in (0, 64, 127):
    Up = torch.linalg.matrix_exp(pos[p].reshape(8, 32, 32))
    U = Ut @ Up                                                   # exp(X_tok) exp(Y_pos), per block
    Uinv = torch.linalg.inv(U)
    Sig = slog[ids].exp().reshape(-1, 8, 32)
    C_full = Uinv @ torch.diag_embed(Sig) @ Uinv.transpose(-1, -2)
    C_frame = Uinv @ Uinv.transpose(-1, -2) * float(slog.exp().mean())
    cond = lambda A: (lambda e: e[..., -1] / e[..., 0])(torch.linalg.eigvalsh(A))
    cf, cfr = cond(C_full), cond(C_frame)
    cs = Sig.max(-1).values / Sig.min(-1).values
    # static key bias from covariance, layer-0 maps (all 8 heads), full-width S_K reads all blocks
    Cb = blockdiag(C_full)                                        # (n,256,256)
    VK = SK.unsqueeze(0) @ Cb.unsqueeze(1) @ SK.transpose(-1, -2).unsqueeze(0)   # (n,8,32,32)
    VQ = SQ.unsqueeze(0) @ Cb.unsqueeze(1) @ SQ.transpose(-1, -2).unsqueeze(0)
    ldk = torch.logdet(VK); ldq = torch.logdet(VQ)
    Cb0 = blockdiag(C_frame)                                      # frames only, Sigma replaced by mean*I
    ldk0 = torch.logdet(SK.unsqueeze(0) @ Cb0.unsqueeze(1) @ SK.transpose(-1, -2).unsqueeze(0))
    out[p] = {
        "cond_C_block_median": float(cf.median()), "cond_C_block_p95": float(cf.quantile(0.95)),
        "cond_frameonly_block_median": float(cfr.median()), "cond_Sigma_block_median": float(cs.median()),
        "keybias_half_logdetVK_over_tau_sd_across_tokens_per_head": [float(x) for x in (0.5 * ldk / tau).std(0)],
        "keybias_frames_only_sd_per_head": [float(x) for x in (0.5 * ldk0 / tau).std(0)],
        "keybias_range_max_minus_min_head_mean": float(((0.5 * ldk / tau).max(0).values - (0.5 * ldk / tau).min(0).values).mean()),
        "logdet_VQ_sd_per_head_mean": float(ldq.std(0).mean()),
    }
    print(p, out[p])
