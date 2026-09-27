import sys
sys.dont_write_bytecode = True
import torch
torch.set_num_threads(1)
p = r"D:\DATA_KEEP\31.04_wikitext-103_K256_4-layer_noHM\final_model.pt"
obj = torch.load(p, weights_only=True, map_location="cpu", mmap=True)
print(type(obj))
if isinstance(obj, dict):
    for k, v in list(obj.items())[:60]:
        if isinstance(v, torch.Tensor):
            print(k, tuple(v.shape), v.dtype)
        elif isinstance(v, dict):
            print(k, "dict", len(v))
            for kk, vv in list(v.items())[:80]:
                print("   ", kk, tuple(vv.shape) if isinstance(vv, torch.Tensor) else type(vv).__name__)
        else:
            print(k, type(v).__name__, (str(v)[:120]))
