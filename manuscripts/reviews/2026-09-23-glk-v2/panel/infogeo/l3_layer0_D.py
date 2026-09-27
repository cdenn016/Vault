r"""Layer-0 raw projected KL values (all terms static at layer 0) on the unigram sample; cap = 2048."""
import json, math, os
import numpy as np
import scipy.linalg as sla
here = os.path.dirname(os.path.abspath(__file__))
Z = np.load(os.path.join(here, "l3_slices.npz"))
H, d = 8, 32
s_all = Z["sigma_log_all"]; toks = Z["toks"].astype(int); n = len(toks)
Cref, xi0 = [], []
for k in range(n):
    X = Z["phi_rows"][k].reshape(H, d, d); Y = Z["pos_rows"][k].reshape(H, d, d)
    Ui = sla.block_diag(*[sla.expm(X[b]) @ sla.expm(Y[b]) for b in range(H)])
    Uii = np.linalg.inv(Ui)
    Cref.append(Uii @ np.diag(np.exp(s_all[toks[k]])) @ Uii.T); xi0.append(Uii @ Z["mu_rows"][k])
SQ, SK = Z["SQ0"], Z["SK0"]
stats = []
for h in range(H):
    a = [SQ[h] @ x for x in xi0]; b = [SK[h] @ x for x in xi0]
    VQ = [SQ[h] @ C @ SQ[h].T for C in Cref]; VK = [SK[h] @ C @ SK[h].T for C in Cref]
    D = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            P = np.linalg.inv(VK[j]); dl = a[i] - b[j]
            D[i, j] = 0.5 * (np.trace(P @ VQ[i]) + dl @ P @ dl - d + np.linalg.slogdet(VK[j])[1] - np.linalg.slogdet(VQ[i])[1])
    within = (D - D.min(1, keepdims=True)).max(1)
    stats.append({"head": h + 1, "D_min": float(D.min()), "D_median": float(np.median(D)), "D_max": float(D.max()),
                  "row_range_median_logits": float(np.median(within) / math.sqrt(32))})
print(json.dumps(stats, indent=1))
json.dump(stats, open(os.path.join(here, "l3_layer0_D.json"), "w"), indent=1)
