"""Causality and batch-composition check of the predictive path on VFE_3.0 HEAD (git export)."""
import sys, os, json, warnings
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "vfe_head"))
import torch
torch.set_num_threads(1)
from dataclasses import fields
from vfe3.config import VFE3Config
from vfe3.model.model import VFEModel
RUN = r"D:\DATA_KEEP\31.04_wikitext-103_K256_4-layer_noHM"
toks = torch.load(os.path.expanduser(r"~/.cache/tokenized_cache/wikitext-103_test_tiktoken_tokens.pt"), weights_only=True, map_location="cpu")
A = toks[0:129].long(); Bq = toks[5000:5129].long()
uniq = torch.unique(torch.cat([A, Bq]))
remap = {int(t): i for i, t in enumerate(uniq.tolist())}
ids = lambda s: torch.tensor([remap[int(t)] for t in s[:128]])
xa, xb = ids(A), ids(Bq)
arch = json.load(open(os.path.join(RUN, "config.json")))["config"]
names = {f.name for f in fields(VFE3Config)}
kw = {k: v for k, v in arch.items() if k in names}
kw.update(vocab_size=int(uniq.numel()), amp_dtype=None)
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    cfg = VFE3Config(**kw)
    model = VFEModel(cfg).eval()
sd_full = torch.load(os.path.join(RUN, "final_model.pt"), weights_only=True, map_location="cpu", mmap=True)["model_state"]
sd = {k: (v[uniq].clone() if (k.startswith("prior_bank.") and v.dim() >= 1 and v.shape[0] == 50257) else v.clone()) for k, v in sd_full.items()}
print("load:", model.load_state_dict(sd, strict=True), " dropped:", sorted(set(arch) - names))
def logits(x):
    with torch.no_grad(), warnings.catch_warnings():
        warnings.simplefilter("ignore")
        return model.forward_beliefs(x, return_logits=True)[1]
la = logits(xa.unsqueeze(0))[0]
xp = xa.clone(); g = torch.Generator().manual_seed(0)
xp[64:] = xb[torch.randperm(128, generator=g)[:64]]
lp = logits(xp.unsqueeze(0))[0]
lab = logits(torch.stack([xa, xb]))
print("max |logit diff| at positions <64 after changing positions >=64:", float((la[:64] - lp[:64]).abs().max()))
print("max |logit diff| at positions >=64 (should be large):", float((la[64:] - lp[64:]).abs().max()))
print("batch composition: max |logit(A alone) - logit(A in [A,B])|:", float((la - lab[0]).abs().max()))
y = torch.tensor([remap[int(t)] for t in A[1:129]])
