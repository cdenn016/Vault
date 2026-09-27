"""Build the archived run's settings on VFE_3.0's dataclass; report dropped keys, defaults, mutations, warnings."""
import sys, json, warnings
sys.dont_write_bytecode = True
sys.path.insert(0, r"C:\Users\chris and christine\Desktop\VFE_3.0")
import torch
torch.set_num_threads(1)
from dataclasses import fields, asdict
from vfe3.config import VFE3Config

ARCH = r"D:\DATA_KEEP\31.04_wikitext-103_K256_4-layer_noHM\config.json"

def archived_kwargs(overrides=None):
    arch = json.load(open(ARCH))["config"]
    names = {f.name for f in fields(VFE3Config)}
    kw, dropped = {}, {}
    for k, v in arch.items():
        if k == "__vfe3_config_schema__":
            continue
        if k in ("relational_mode", "relational_readout_mode", "grad_clip_per_role", "exp_fp64_mode"):
            dropped[k] = v
            continue
        if k not in names:
            dropped[k] = v
            continue
        kw[k] = v
    assert (arch["relational_mode"], arch["relational_readout_mode"]) == ("projected_filtering", "predictive_content")
    kw["attention_mode"] = "projected_predictive"
    if overrides:
        kw.update(overrides)
    return kw, dropped

if __name__ == "__main__":
    kw, dropped = archived_kwargs()
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        cfg = VFE3Config(**kw)
    eff = asdict(cfg)
    changed = {k: (v, eff[k]) for k, v in kw.items() if k in eff and eff[k] != v}
    defaults = sorted(set(eff) - set(kw))
    print("dropped (retired/migrated):", json.dumps(dropped, default=str))
    print("constructor-changed supplied values:", changed)
    print("n default-supplied fields:", len(defaults))
    print("default-supplied:", defaults)
    for x in w:
        print("WARN:", str(x.message)[:600])
    print("derived: relational_mode=", cfg.relational_mode, " readout=", cfg.relational_readout_mode,
          " d_head=", cfg.d_head, " phi_retract_mode=", cfg.phi_retract_mode)
    for k in ("m_layernorm_lr", "m_pos_phi_lr", "decode_av_precision", "diagonal_covariance", "effective_e_step_gradient"):
        print(k, "=", getattr(cfg, k, "<absent>"))
