r"""Consistency of the reconstruction with the archived per-layer diagnostics (cond, min eig)."""
import json, math, os
import numpy as np
import scipy.linalg as sla
here = os.path.dirname(os.path.abspath(__file__))
Z = np.load(os.path.join(here, "l3_slices.npz"))
H, d = 8, 32
s_all = Z["sigma_log_all"]; toks = Z["toks"].astype(int)
Cref = []
for k in range(len(toks)):
    X = Z["phi_rows"][k].reshape(H, d, d); Y = Z["pos_rows"][k].reshape(H, d, d)
    Ui = sla.block_diag(*[sla.expm(X[b]) @ sla.expm(Y[b]) for b in range(H)])
    Uii = np.linalg.inv(Ui)
    Cref.append(Uii @ np.diag(np.exp(s_all[toks[k]])) @ Uii.T)
res = {}
for li in range(4):
    SQ, SK = Z[f"SQ{li}"], Z[f"SK{li}"]
    eQ = np.array([np.linalg.eigvalsh(SQ[h] @ C @ SQ[h].T) for h in range(H) for C in Cref])
    eK = np.array([np.linalg.eigvalsh(SK[h] @ C @ SK[h].T) for h in range(H) for C in Cref])
    res[f"layer{li}"] = {"max_cond_VQ": float((eQ[:, -1] / eQ[:, 0]).max()), "max_cond_VK": float((eK[:, -1] / eK[:, 0]).max()),
                         "min_eig_VQ": float(eQ.min()), "min_eig_VK": float(eK.min())}
print(json.dumps(res, indent=1))
json.dump(res, open(os.path.join(here, "l3_consistency.json"), "w"), indent=1)
