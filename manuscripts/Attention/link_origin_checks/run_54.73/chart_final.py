r"""Chart diagnostic for a trained projected_predictive run (CPU, read-only): per layer, the stacked unrouted operator
M = sum_h O_h T_h (reference coordinates) and I + M. Reports sign(det), sigma_min/max, eigenvalue location, the
principal-log condition (no eigenvalue on (-inf, 0]), and the distance from the depth-scaled initialization."""
import sys, json, numpy as np, torch
run = sys.argv[1]
ck = torch.load(run + "/final_model.pt", map_location="cpu", weights_only=False)
sd, cfg = ck["model_state"], json.load(open(run + "/config.json"))["config"]
L, H, K = cfg["n_layers"], cfg["n_heads"], cfg["embed_dim"]; d = K // H
init_scale = 1.0 / np.sqrt(2 * L) if cfg["relational_output_init"] == "depth_scaled" else 1.0
names = ["relational_operators"] + [f"relational_operators_extra.{i}" for i in range(L - 1)]

def stats(A, tag):
    A = A.astype(np.float64)
    sign, logdet = np.linalg.slogdet(A)
    s = np.linalg.svd(A, compute_uv=False)
    w = np.linalg.eigvals(A)
    real_neg = int(np.sum((np.abs(w.imag) < 1e-9 * max(1, np.abs(w).max())) & (w.real <= 0)))
    return dict(tag=tag, sign_det=int(sign), logabsdet=round(float(logdet), 3), sigma_min=float(s[-1]), sigma_max=float(s[0]),
                cond=float(s[0] / s[-1]), min_re=float(w.real.min()), max_re=float(w.real.max()), max_im=float(np.abs(w.imag).max()),
                n_on_closed_neg_axis=real_neg, n_re_neg=int(np.sum(w.real < 0)))

rows = []
for l, nm in enumerate(names):
    T = sd[nm + ".T"].double().numpy(); O = sd[nm + ".O"].double().numpy()          # (H,d,K), (H,K,d)
    Ost = np.concatenate([O[h] for h in range(H)], axis=1)                           # (K,K)
    Tst = np.concatenate([T[h] for h in range(H)], axis=0)                           # (K,K)
    M = Ost @ Tst
    M0 = init_scale * np.eye(K)
    Mh = [O[h] @ T[h] for h in range(H)]
    TO = Tst @ Ost
    r = dict(layer=l,
             M=stats(M, "M=sum_h O_h T_h"), IplusM=stats(np.eye(K) + M, "I+M"),
             rel_move_from_init=float(np.linalg.norm(M - M0) / np.linalg.norm(M0)),
             head_frob=[float(np.linalg.norm(m)) for m in Mh],
             head_rank_numeric=[int(np.linalg.matrix_rank(m, tol=1e-6 * np.linalg.norm(m, 2))) for m in Mh],
             TO_offdiag_over_diag=float(np.linalg.norm(TO[:d, d:]) / max(1e-30, np.linalg.norm(TO[:d, :d]))),
             stackedO_cond=float(np.linalg.cond(Ost)), stackedT_cond=float(np.linalg.cond(Tst)),
             trace_M=float(np.trace(M)), trace_M0=float(np.trace(M0)))
    rows.append(r)
json.dump(rows, open(run + "/chart_diagnostic.json", "w"), indent=1) if len(sys.argv) > 2 and sys.argv[2] == "write" else None
for r in rows:
    print(f"\n== layer {r['layer']}  rel_move_from_init={r['rel_move_from_init']:.3f}  tr M={r['trace_M']:.2f} (init {r['trace_M0']:.2f})  head ||M_h||={['%.2f'%x for x in r['head_frob']]} rank={r['head_rank_numeric']}")
    print(f"   cond(stacked O)={r['stackedO_cond']:.1f} cond(stacked T)={r['stackedT_cond']:.1f}  ||(TO)_offdiag||/||(TO)_diag||={r['TO_offdiag_over_diag']:.3f}")
    for k in ("M", "IplusM"):
        s = r[k]
        print(f"   {s['tag']:>16}: sign det={s['sign_det']:+d} log|det|={s['logabsdet']:.2f}  sigma_min={s['sigma_min']:.3e} sigma_max={s['sigma_max']:.2f} cond={s['cond']:.1f}  "
              f"Re(eig) in [{s['min_re']:.3f},{s['max_re']:.3f}] max|Im|={s['max_im']:.3f}  #Re<0={s['n_re_neg']}  #on(-inf,0]={s['n_on_closed_neg_axis']}")
