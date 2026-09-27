import torch
torch.set_num_threads(1)
ck = torch.load(r"D:/DATA_KEEP/31.04_wikitext-103_K256_4-layer_noHM/final_model.pt", weights_only=True, map_location="cpu")
print(type(ck))
if isinstance(ck, dict):
    for k, v in ck.items():
        if isinstance(v, torch.Tensor):
            print("T", k, tuple(v.shape), v.dtype)
        elif isinstance(v, dict):
            print("D", k, len(v))
            for kk, vv in list(v.items())[:80]:
                print("   ", kk, tuple(vv.shape) if isinstance(vv, torch.Tensor) else type(vv))
        else:
            print("O", k, type(v))
