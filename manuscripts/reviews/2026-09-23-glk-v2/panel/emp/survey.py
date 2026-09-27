import json, csv, os, math, glob
roots = sorted(glob.glob("D:/DATA_KEEP/*_wikitext-103_*")) + sorted(glob.glob("D:/DATA_KEEP/wikitext-103-word/*"))
for d in roots:
    try:
        cfg = json.load(open(os.path.join(d, "config.json")))["config"]
    except Exception as e:
        print("NOCFG", d, e); continue
    name = os.path.basename(d)
    keys = ["embed_dim", "n_layers", "n_heads", "max_seq_len", "eval_stride", "batch_size", "max_steps", "use_head_mixer",
            "weight_decay", "sigma_weight_decay", "mu_weight_decay", "phi_weight_decay", "sigma_init", "mu_init_std",
            "phi_scale", "m_p_sigma_lr", "m_p_mu_lr", "m_phi_lr", "m_relational_score_lr", "m_relational_content_lr",
            "phi_mstep_max_matrix_norm", "min_lr_frac", "relational_mode", "relational_readout_mode", "attention_residual",
            "decode_mode", "use_block_mlp", "vocab_size", "kl_max", "seed", "amp_dtype", "norm_type_block"]
    print("=====", name)
    print("  ", {k: cfg.get(k) for k in keys})
    pm = os.path.join(d, "parameter_motion.json")
    if os.path.exists(pm):
        m = json.load(open(pm))["motion"]
        for k in ("prior_bank.mu_embed", "prior_bank.sigma_log_embed", "prior_bank.phi_embed"):
            if k in m:
                print("   motion", k, "init %.2f abs %.2f rel %.3f" % (m[k]["init_norm"], m[k]["abs"], m[k]["rel"] or float("nan")))
        rel = [(k, v["rel"]) for k, v in m.items() if "relational_operators" in k]
        if rel:
            print("   relational rel growth min %.1f max %.1f" % (min(r for _, r in rel), max(r for _, r in rel)))
    mpl = os.path.join(d, "metrics_per_layer.csv")
    if os.path.exists(mpl):
        for r in csv.DictReader(open(mpl, newline="")):
            print("   layer %s disp %.4g tokens %s content_smax %s score_min_sv %s cov_cond %s" % (
                r.get("layer"), float(r.get("relational_mean_displacement_norm") or "nan"), r.get("relational_conditional_cost_tokens"),
                r.get("relational_content_max_singular_value"), r.get("relational_score_raw_min_singular_value"),
                r.get("relational_projected_cov_max_condition")))
    mc = os.path.join(d, "metrics.csv")
    if os.path.exists(mc):
        rows = list(csv.DictReader(open(mc, newline="")))
        last = rows[-1]
        print("   last weight_norm_sigma", last.get("weight_norm_sigma"), "weight_norm_mu", last.get("weight_norm_mu"), "corpus_pass", last.get("corpus_pass"))
    tr = os.path.join(d, "test_results.json")
    if os.path.exists(tr):
        t = json.load(open(tr))
        print("   test_ppl %.4f test_ce %.5f scored %s best_val %.4f@%s final_val %.4f" % (t["test_ppl"], t["test_ce"], t.get("scored_targets"), t.get("best_val_ppl"), t.get("best_step"), t.get("final_val_ppl", float("nan"))))
    pv = os.path.join(d, "provenance.json")
    if os.path.exists(pv):
        p = json.load(open(pv))
        print("   train_tokens", p.get("train_data_n_tokens"), "data_seed", p.get("data_seed"), "drift", p.get("code_identity_drift"))
