import torch, sys
torch.set_num_threads(1)
p = r"D:/DATA_KEEP/31.04_wikitext-103_K256_4-layer_noHM/final_model.pt"
try:
    ck = torch.load(p, weights_only=True, map_location="cpu")
except Exception as e:
    print("WEIGHTS_ONLY_LOAD_FAILED:", type(e).__name__, str(e)[:2000])
    sys.exit(2)
print(type(ck))
if isinstance(ck, dict):
    for k, v in ck.items():
        if isinstance(v, dict):
            print("KEY", k, "dict with", len(v), "entries")
        elif torch.is_tensor(v):
            print("KEY", k, "tensor", tuple(v.shape), v.dtype)
        else:
            print("KEY", k, type(v).__name__, str(v)[:200])
    sd = ck.get("model_state_dict") or ck.get("state_dict") or ck.get("model") or ck
    if isinstance(sd, dict):
        for k, v in sd.items():
            if torch.is_tensor(v):
                print("  ", k, tuple(v.shape), v.dtype)
            else:
                print("  ", k, type(v).__name__)
