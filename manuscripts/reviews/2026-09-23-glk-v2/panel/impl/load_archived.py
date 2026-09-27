"""Replay the archived schema-25 config through VFE_3.0's current loader (read-only)."""
import sys, os, json, warnings
sys.dont_write_bytecode = True
sys.path.insert(0, r"C:\Users\chris and christine\Desktop\VFE_3.0")
import torch
torch.set_num_threads(1)
from dataclasses import fields, asdict
from vfe3.config import VFE3Config, config_from_serialized
arch = json.load(open(r"D:\DATA_KEEP\31.04_wikitext-103_K256_4-layer_noHM\config.json"))["config"]
names = {f.name: f for f in fields(VFE3Config)}
payload = dict(arch)
payload.pop("__vfe3_config_schema__", None)
# Mirror config_from_serialized's migrations to list what it would still refuse.
migrated = dict(payload)
for k in ("grad_clip_per_role", "exp_fp64_mode", "relational_mode", "relational_readout_mode"):
    migrated.pop(k, None)
unknown = sorted(k for k in migrated if k not in names)
print("n archived fields:", len(arch))
print("unknown to current dataclass after built-in migrations:", unknown)
try:
    config_from_serialized(arch, source="archived")
except Exception as e:
    print("config_from_serialized(raw archived) ->", type(e).__name__, str(e)[:300])
try:
    config_from_serialized(payload, source="archived-no-schema")
except Exception as e:
    print("config_from_serialized(no schema key) ->", type(e).__name__, str(e)[:400])
