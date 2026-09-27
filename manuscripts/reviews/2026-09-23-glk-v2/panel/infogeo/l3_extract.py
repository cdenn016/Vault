r"""Extract (read-only, CPU, one thread, mmap) the small slices needed for the L3 analysis."""
import os
os.environ["CUDA_VISIBLE_DEVICES"] = ""
import torch
torch.set_num_threads(1)
P = r"D:\DATA_KEEP\31.04_wikitext-103_K256_4-layer_noHM\final_model.pt"
sd = torch.load(P, weights_only=True, map_location="cpu", mmap=True)["model_state"]
g = torch.Generator().manual_seed(31)
logu = sd["prior_bank.unigram_log_prior"].double()
pu = torch.softmax(logu, 0)
n_tok = 48
toks = torch.multinomial(pu, n_tok, replacement=False, generator=g)
poss = torch.randint(0, 128, (n_tok,), generator=g)
keep = {"toks": toks, "poss": poss, "unigram_p": pu,
        "sigma_log_all": sd["prior_bank.sigma_log_embed"].clone(),
        "phi_rows": sd["prior_bank.phi_embed"][toks].clone(),
        "pos_rows": sd["pos_phi_free"][poss].clone(),
        "mu_rows": sd["prior_bank.mu_embed"][toks].clone()}
names = ["relational_operators"] + [f"relational_operators_extra.{k}" for k in range(3)]
for li, n in enumerate(names):
    keep[f"SQ{li}"] = sd[n + ".raw_score_q"].clone()
    keep[f"SK{li}"] = sd[n + ".raw_score_k"].clone()
    keep[f"T{li}"] = sd[n + ".T"].clone()
    keep[f"O{li}"] = sd[n + ".O"].clone()
import numpy as np
np.savez(os.path.join(os.path.dirname(os.path.abspath(__file__)), "l3_slices.npz"),
         **{k: v.double().numpy() for k, v in keep.items()})
print("saved", {k: tuple(v.shape) for k, v in keep.items()})
