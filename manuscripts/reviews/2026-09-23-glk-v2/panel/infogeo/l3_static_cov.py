r"""L3 / L5 quantification from archived final weights (slices extracted by l3_extract.py).

Reference covariance C_i = U_i^{-1} diag(exp(s_x)) U_i^{-T}, U_i = exp(X_x) exp(Y_i) (8 blocks of 32,
row-major elementary basis).  Covariance is passed through the stack unchanged and frames are fixed,
so every covariance-only KL term is a static function of (token, position, layer, head).
Logit units: divide by tau = sqrt(32).  Current vfe3 conventions; the run's source bytes are dirty.
"""
import json, math, os
import numpy as np
import scipy.linalg as sla

here = os.path.dirname(os.path.abspath(__file__))
Z = np.load(os.path.join(here, "l3_slices.npz"))
H, d, K = 8, 32, 256
tau = math.sqrt(32.0)
out = {}
s_all = Z["sigma_log_all"]
out["sigma_log_embed"] = {"mean": float(s_all.mean()), "std": float(s_all.std()), "min": float(s_all.min()),
                          "max": float(s_all.max()), "init_log15": math.log(15.0),
                          "median_within_token_std": float(np.median(s_all.std(1)))}
tr_all = np.exp(s_all).sum(1)
out["trace_Sigma_all_tokens"] = {"mean": float(tr_all.mean()), "cv": float(tr_all.std() / tr_all.mean())}
pu = Z["unigram_p"]
toks, poss = Z["toks"].astype(int), Z["poss"].astype(int)
n = len(toks)
w = pu / pu.sum()
tr_w_mean = float((w * tr_all).sum()); tr_w_cv = float(np.sqrt((w * (tr_all - tr_w_mean) ** 2).sum()) / tr_w_mean)
out["trace_Sigma_unigram_weighted"] = {"mean": tr_w_mean, "cv": tr_w_cv}
out["sample"] = {"n": n, "unigram_mass_covered": float(pu[toks].sum()),
                 "trace_cv_sample": float(np.exp(s_all[toks]).sum(1).std() / np.exp(s_all[toks]).sum(1).mean()),
                 "log_var_within_token_std_median": float(np.median(s_all[toks].std(1))),
                 "log_var_sample_mean": float(s_all[toks].mean())}

Cref, xi0, gap, xn, yn = [], [], [], [], []
for k in range(n):
    X = Z["phi_rows"][k].reshape(H, d, d); Y = Z["pos_rows"][k].reshape(H, d, d)
    xn.append(max(np.linalg.norm(X[b]) for b in range(H))); yn.append(max(np.linalg.norm(Y[b]) for b in range(H)))
    Ui = sla.block_diag(*[sla.expm(X[b]) @ sla.expm(Y[b]) for b in range(H)])
    Uii = np.linalg.inv(Ui)
    Sig = np.exp(s_all[toks[k]])
    C = Uii @ np.diag(Sig) @ Uii.T
    Cref.append(C); xi0.append(Uii @ Z["mu_rows"][k])
    gap.append(np.linalg.norm(C - Sig.mean() * (Uii @ Uii.T)) / np.linalg.norm(C))
out["frames"] = {"max_block_frobenius_X": float(max(xn)), "max_block_frobenius_Y": float(max(yn)),
                 "rel_gap_C_vs_meanvar_times_Gram_inverse_median": float(np.median(gap)),
                 "rel_gap_max": float(np.max(gap)),
                 "cond_C_median": float(np.median([np.linalg.cond(C) for C in Cref]))}


def split(T):
    g = T.mean(); row = T.mean(1, keepdims=True) - g; col = T.mean(0, keepdims=True) - g
    inter = T - g - row - col
    return float(np.sqrt((row ** 2).mean())), float(np.sqrt((col ** 2).mean())), float(np.sqrt((inter ** 2).mean()))


per_layer = []
for li in range(4):
    SQ, SK, T, O = Z[f"SQ{li}"], Z[f"SK{li}"], Z[f"T{li}"], Z[f"O{li}"]
    rows = []
    for h in range(H):
        VQ = [SQ[h] @ C @ SQ[h].T for C in Cref]
        VK = [SK[h] @ C @ SK[h].T for C in Cref]
        PK = [np.linalg.inv(V) for V in VK]
        ldK = np.array([np.linalg.slogdet(V)[1] for V in VK])
        trace = np.array([[0.5 * np.trace(PK[j] @ VQ[i]) for j in range(n)] for i in range(n)]) / tau
        src = 0.5 * ldK / tau
        condK = np.array([np.linalg.cond(V) for V in VK])
        Pbar = np.mean(PK, axis=0)
        spread = float(np.median([np.linalg.norm(Pk - Pbar) / np.linalg.norm(Pbar) for Pk in PK]))
        _, c_tr, i_tr = split(trace)
        Qsym = SQ[h] @ SQ[h].T + SK[h] @ SK[h].T
        bal = T[h] @ T[h].T - O[h].T @ O[h]
        row = {"head": h + 1,
               "src_logdet_std": float(src.std()), "trace_col_std": c_tr, "trace_pair_std": i_tr,
               "condVK_med": float(np.median(condK)), "condVK_max": float(condK.max()),
               "precision_rel_spread_med": spread,
               "sv_SQ_min_max": [float(np.linalg.svd(SQ[h], compute_uv=False).min()), float(np.linalg.svd(SQ[h], compute_uv=False).max())],
               "sv_SK_min_max": [float(np.linalg.svd(SK[h], compute_uv=False).min()), float(np.linalg.svd(SK[h], compute_uv=False).max())],
               "trQ_over_init": float(np.trace(Qsym) / (2 * d)),
               "balance_rel": float(np.linalg.norm(bal) / (np.linalg.norm(T[h] @ T[h].T) + np.linalg.norm(O[h].T @ O[h])))}
        if li == 0:
            a = np.array([SQ[h] @ x for x in xi0]); b = np.array([SK[h] @ x for x in xi0])
            maha = np.array([[0.5 * (a[i] - b[j]) @ PK[j] @ (a[i] - b[j]) for j in range(n)] for i in range(n)]) / tau
            cross = np.array([[-(a[i] @ PK[j] @ b[j]) for j in range(n)] for i in range(n)]) / tau
            _, c_m, i_m = split(maha)
            _, c_x, i_x = split(cross)
            full = maha + trace + src[None, :]
            _, c_f, i_f = split(full)
            row.update({"L0_maha_col_std": c_m, "L0_maha_pair_std": i_m, "L0_cross_pair_std": i_x,
                        "L0_total_col_std": c_f, "L0_total_pair_std": i_f})
        rows.append(row)
    per_layer.append({"layer": li, "heads": rows})
out["per_layer"] = per_layer
json.dump(out, open(os.path.join(here, "l3_static_cov.json"), "w"), indent=1, default=float)
print(json.dumps({k: v for k, v in out.items() if k != "per_layer"}, indent=1, default=float))
for L in per_layer:
    hs = L["heads"]
    keys = ["src_logdet_std", "trace_col_std", "trace_pair_std", "condVK_med", "condVK_max",
            "precision_rel_spread_med", "trQ_over_init", "balance_rel"]
    if L["layer"] == 0:
        keys += ["L0_maha_col_std", "L0_maha_pair_std", "L0_cross_pair_std", "L0_total_col_std", "L0_total_pair_std"]
    print("layer", L["layer"])
    for k in keys:
        print("   ", k, [round(h[k], 3) for h in hs])
    print("    sv_SQ_min_max", [[round(v, 2) for v in h["sv_SQ_min_max"]] for h in hs])
    print("    sv_SK_min_max", [[round(v, 2) for v in h["sv_SK_min_max"]] for h in hs])
