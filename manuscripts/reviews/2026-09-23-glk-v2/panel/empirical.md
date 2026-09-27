# Empirical methods, ML engineering and numerics: referee report on GL(K)_attention_v2, Section 5

Lens: ML engineering, empirical methods and numerics. Investigator: Claude Opus 5.5. This report produces findings and does not claim any verification verdict. Date: 2026-09-23.

Scope: Main `GL(K)_attention_v2.tex` line 52 (the abstract's empirical sentence), lines 1093-1161 (Section 5, Algorithm 1, Table `tab:relational_run`), lines 1164-1185 (Discussion) and lines 1189-1191 (Conclusion). Data: the featured run `D:\DATA_KEEP\31.04_wikitext-103_K256_4-layer_noHM` and the other `D:\DATA_KEEP` runs. The prior review (2026-09-22: `review.md`, `figure-data-plan.md`, `publication-placeholders.tex`, `investigators/implementation-data.md`) was read first. Its R3/R4/F1-F6/T1-T2 are extended here, not repeated. Missing final data is not counted as a defect.

## What was executed (CPU only)

All torch work used `C:/anaconda/python.exe` with `CUDA_VISIBLE_DEVICES=-1` and `torch.set_num_threads(1)`. No GPU was used.

1. Record checks across all 13 same-generation runs: `config.json`, `summary.json`, `test_results.json`, `final_validation.json`, `provenance.json`, `research.json`, `parameter_motion.json`, `beta_channel_decomposition.json`, `estep_character.json`, `context_sensitivity.json`, `metrics.csv` (200 rows) and `metrics_per_layer.csv`.
2. `final_model.pt` was loaded with `torch.load(path, weights_only=True, map_location="cpu")`. The load succeeded; `model_state` has 42 entries. Only norms and spectra of stored tensors were computed. No model object was built and no forward pass ran on text. One central estimate passes synthetic LayerNorm-shaped vectors through the stored MLP weights and is labeled as synthetic wherever used.
3. Code reading at both recorded clean endpoints, `4e137ec` and `965718d`, via read-only `git show` in V3_Transformer, plus the present VFE_3.0 copy.
4. Tiny numeric checks with K <= 6: GL(r) invariance of the projected KL, the Noether identities for the comparison and content symmetries, AdamW versus SGD drift along the flat orbit, and the common-covariance-rescaling identity.

Scripts and outputs: `scratchpad/panel/emp/` (`ckpt_analysis.py/.json`, `residual_bounds.py`, `cov_share.py`, `symmetry_toy.py`, `curves.py`, `survey.py`).

## 1. Number-by-number verification of Section 5

Every number in Section 5, Table `tab:relational_run`, the abstract and the Conclusion matches the archive. The problems are interpretive and concern measurement validity; they are covered in Section 2.

| Quantity (Main line) | Manuscript | Archive record | Status |
|---|---|---|---|
| K, H=B, d_b=r_h=s_h, L (1100) | 256, 8, 32, 4 | config embed_dim 256, n_heads 8; irrep_dims 8x32; score/content rank 32; n_layers 4 | match |
| tau_h (1100, 1134) | sqrt(32) | `temperature_convention=kappa_beta_times_sqrt_ambient_head_dim`, kappa_beta 1; `config.tau = kappa*sqrt(d_head)` (4e137ec) | match |
| Cost bound (1100) | [0, 8K] | kl_max 2048 = 8x256; `safe_kl_clamp` clamps to [0, kl_max] (4e137ec families/base.py:27-29) | match |
| ALiBi (1134) | -2^{-h}(i-j), h=1..8 | `_press_slopes`: base x 2^{-8h/H}, alibi_slope 1, H=8 | match |
| Parameters (1136) | 456,654,162; 1,048,576; 4,203,520; 411,705,344 (90.16%) | n_params; relational total_parameters; block_mlp parameter_count; phi_embed (50257, 8192) | match |
| Updates, presentations (1136) | 240,000; 491,520,000 | accepted_updates 240000, skipped 0; tokens_seen 491,520,000 = 240,000 x 16 x 128 | match |
| Hardware and software (1136) | RTX 5090, 2.10.0.dev20251210+cu128, bf16 | provenance.json; amp_dtype bf16 | match |
| Protocol (1138) | N=128, stride 32; 280,541/280,542; 245,020 | eval_stride 32; scored_targets; test_data_n_tokens; final_val_scored_targets | match |
| Table rows (1146-1148) | 29.6088 at 216k; 30.0100 at 240k; 31.0389 | best_val_ppl 29.60883; final_val_ppl 30.00997; test_ppl 31.03891 | match |
| Test CE (1155) | 3.43524149 | test_ce 3.4352414889 | match |
| Final minibatch PPL (1155) | 20.6658 | metrics.csv train_ppl at step 240000 | match |
| Probe CEs (1157) | 3.0431 / 4.1923 / 5.1182 | beta_channel_decomposition.json | match |
| Singular values (1159) | 6.64 to 12.32 | per-layer minimum: 6.643, 12.323, 12.047, 10.443 | match |
| Condition numbers (1159) | about 88.7 to 550.5 | 550.46, 209.83, 88.69, 163.23 | match |
| Revisions (1155) | 4e137ec88f45, 965718d88cf7 | provenance run_start and final git_sha | match |
| Abstract (52), Conclusion (1191) | 31.04, single seed | test_ppl; seed 6 | match (see E6 on missing dataset and tokenizer) |

## 2. Findings (strongest first)

### E1. The explicit attention residual is numerically inert in the trained model
**Location:** Main eq. `relational_predictive_residual` (885-889), 1053, Algorithm 1 line 1117, 1132 ("the additive attention residual"), 1173.
**Severity:** high
**Evidence:**

1. What the diagnostic measures. `relational_mean_displacement_norm = (result - mu).norm()` with `result = mu + predictive_content(...)` (vfe3/gradients/relational.py:133-138, identical at 4e137ec and 965718d). It is therefore the Frobenius norm of the message m over the captured tensor. The capture is one 128-token validation window: `diagnostics()` "only sequence 0 is used" (model.py:1888), and `relational_conditional_cost_tokens=128`. The per-token RMS of ||m_i|| is 65,488 at layer 0, then 64,838, 96,087 and 32,823 at layers 1-3.
2. Layer 0 from stored weights. The token-mean table has Frobenius norm 380.07; row norms have median 1.74 and maximum 3.78. The ratio of the RMS message to the largest input row is therefore at least 1.73e4, and about 3.8e4 at the median row.
3. Direct archived record. `estep_character.json` reports `rel_displacement = ||mu_after - mu_before|| / ||mu_before|| = 22,315.7` at `captured_pre_transform_readout` (definition at 965718d `run_artifacts.py:3866`).
4. Layers 1-3. Here mu^(l) = u + MLP(u), with ||u|| <= 16 max|gamma| + ||b|| = 33.09. Spectral bounds on the stored MLPs give ||mu^(l)|| <= 2,321, 3,847 and 4,042, so the ratio is at least 27.9, 25.0 and 8.1 (rigorous, given the logged message norm). Passing synthetic LN-shaped inputs through the stored MLPs gives median ||mu^(l)|| of about 44, 41 and 37, so typical ratios are about 1.5e3, 2.3e3 and 0.9e3.
5. The brief's L4 premise needs one correction. `weight_norm_mu = 3024.9` is the root-sum-square over every optimizer group tagged role "mu" (VFE_3.0 vfe3/train.py:863-875; same aggregation at 965718d). The relational maps supply 92.6% of its square, so it is not the token-table norm. The corrected layer-0 ratio is larger than L4 estimated.
6. Mechanism. sigma_max(O_h T_h) grew from 1 at initialization (O_h T_h starts as a block projector, relational_operators.py init) to 26,239, 8,844, 5,461 and 4,578 across layers 0-3. The Frobenius norms of T and O grew 36-48x. The relational groups have `weight_decay: 0.0` (965718d build_optimizer) and the content learning rate was 0.01. The message already dominated early: at step 1,200 the layer-3 message RMS was 1,471 per token.
7. Consequence. LayerNorm is scale-invariant, so the residual perturbs the normalized state by at most 5.8e-5 at layer 0 (first order) and by about 1e-3 at layers 1-3. The add and LayerNorm run in fp32 islands (relational.py:127; fp32 LN in norms.py), so rounding does not erase mu there. The MLP branch input is cast to bf16, however (unit roundoff 2^-8 = 3.9e-3), which is coarser than mu's relative contribution at every layer.
8. Cross-run comparison. The 30.14 run (content lr 0.0025) has a layer-0 message RMS of 1,331 per token against an RMS input-row norm of at most 2.3, a ratio of about 600. In the word-level 48.42 run the ratio is about 100 at layer 0 and of order 2-7 at layer 3 (not inert). In the 15k-30k-step runs the residual stays active (ratios of order 1-10). `context_sensitivity.json` shows that randomizing the prefix moves the final state by 0.89 of its norm, consistent with a context-dominated state.

**Fix:** Report the per-layer ratio. State that the trained network is effectively a post-normalization stack with no attention skip (the MLP skip remains; cf. Dong, Cordonnier & Loukas 2021 on the role of skips), and that the receiving token enters the next layer only through its self-weight beta_ii and its receiving frame U_i. Proposed text after line 1159: "In the trained model the attention residual is numerically subordinate to the message. The archived readout probe records ||m||/||mu|| of about 2.2 x 10^4 at layer 0. The stored weights bound the ratio below by 8 to 28 at later layers, with a typical value near 10^3. Because LayerNorm is invariant to input scale, the explicit residual changes the normalized state by less than 10^-4 at layer 0. The evaluated network is therefore effectively a post-normalization stack without an attention skip connection. This follows from unregularized growth of the content products O_h T_h, whose largest singular values reach 4.6 x 10^3 to 2.6 x 10^4 from unity at initialization." Also add ||m||/||mu|| per layer, per token, to the logged diagnostics. Design the residual ablation knowing that the residual is already inert at convergence.
**Falsifies:** A full-validation forward measurement with ||mu^(l)||/||m^(l)|| >= 1e-2 for most tokens at layers 1-3 would retract "inert" for those layers. So would a frozen intervention replacing mu + m by m that raises validation CE by more than about 1e-3 nats.
**Status:** The residual is correct as a specification (D). The realized-model prose ("the additive attention residual") implies an operative residual, which the record contradicts. Line 1173 ("cannot establish causal necessity of ... the residual") understates what the data already show.
**Novelty vs prior review:** new. It tests lead L4 and corrects that lead's `weight_norm_mu` premise.

### E2. The stored covariance decayed to about 1.045 I, so the "Gaussian" routing is frame-metric routing
**Location:** Main 1095, 1134 ("each role projection retains its full 32x32 reduced covariance"), 1171, 1173; abstract line 50.
**Severity:** high
**Evidence:**

1. Configuration and code. The config sets `sigma_init=15`, `sigma_weight_decay=0.04` and `m_p_sigma_lr=0.001`. The log-variance table is decoupled-decayed by AdamW. The code's own comment (965718d train.py:304-308) reads: "The global decay pulls log sigma toward 0 (sigma toward 1) -- an unintended lognormal prior fighting the configured sigma_init". The encode path uses Sigma_i = diag(exp(sigma_log_embed[x_i])) with no other scale.
2. The decay dominates the final table. The integrated decay factor is exp(-0.04 x sum of lr_t), about exp(-4.85) = 0.0078, so decay alone takes log 15 = 2.708 to 0.021. The final table has entry mean 0.043 and RMS 0.067, with 86% of |entries| < 0.1. Variances are 1.045 +- 0.054 (1st-99th percentile 0.918-1.189). The per-token trace CV is 1.9% over all rows (research.json reports 0.047 on its own sample), and the median per-token condition number is 1.31. `weight_norm_sigma` fell from 9,277 at step 1,200 to 241. `grad_norm_sigma` is 0.004-0.009 against 0.31-0.77 for `grad_norm_mu`.
3. The same decay law reproduces the smallest stored rows. For never-seen tokens it predicts 1.4e-12 for the mean table and 1.1e-4 for the frame table. The observed smallest rows are 1.65e-12 and 3.8e-4.
4. The frames determine the routing covariance. C_i = U_i^{-1} Sigma_i U_i^{-T} has median block condition number 7.53 at positions 64 and 127 (50.6 at position 0). Replacing Sigma by its mean times I gives 7.40 (50.1). At least 98% of the anisotropy is therefore frame-induced.
5. Size of the covariance terms in the score. The static key logit bias (1/2) log det V_{K,j} / tau at layer 0 has an across-token standard deviation of 0.14 logits per head (0.11 with frames only).
6. The decay acted as a hidden temperature on the mean term. Under Sigma_i -> c Sigma_i for all i, the trace and log-determinant terms of eq. `projected_full_kl` are invariant and the Mahalanobis term scales by 1/c (executed: residual 3.6e-15, ratio 15.000000). The drift from c = 15 to about 1.045 therefore multiplied the mean term by about 14 at fixed maps and means, on a schedule set by weight decay rather than by the objective.
7. The collapse is systematic across the archive. `sigma_log_embed` moved 98.6% (31.04), 98.2% (30.14) and 97.8% (48.42) of its initial norm in the long runs, but only 25-45% in the 15k-30k-step runs. Short and long runs therefore also differ in covariance state.
8. Consequence for the controls. With U = I and Sigma about c I, the shared-key-covariance hypothesis of Prop. `projected_dot_product` holds to within +-5%. In this regime the identity-frame model is a biased dot-product router with whitened maps.

**Fix:** State in Section 5 that the stored variances decayed to about 1. The experiment therefore does not test learned per-token uncertainty; its covariance-dependent routing terms are static, frame-induced functions of token and position. Report `sigma_weight_decay` and its effect in the methods table (prior T1). For final runs meant to test covariance-aware routing, the existing exemption `sigma_weight_decay=0.0`, or decay toward the initialization, gives a live covariance channel; report a covariance-live arm. Proposed sentence: "Decoupled weight decay on the stored log-variances carried the initialized variance 15 to 1.045 +- 0.054 per coordinate. The reference covariances that enter routing are therefore determined, to within a few percent, by the token and positional frames."
**Falsifies:** Each of the following would weaken "collapsed". A frequency-weighted analysis could show that the variances of frequent tokens depart from 1 by 20% or more in a structured way. A frozen intervention replacing Sigma by I could change validation CE by 0.01 nats or more. An identity-frame model with the same Sigma could depart materially from the biased-dot-product formula.
**Status:** The statements are true as specifications (D). Read empirically ("Gaussian-KL router with full reduced covariance"), they inflate what the run exercises.
**Novelty vs prior review:** extends C7 (stored covariance as operational state) and R3 (role-specific decays). The new measurement changes the severity.

### E3. The reported conditioning diagnostics reflect drift of the unregularized comparison maps along a GL(r_h) symmetry, not the routing operator
**Location:** Main 1159, and the full-row-rank assumption at 384.
**Severity:** medium
**Evidence:**

1. The symmetries and their Noether identities. The routing cost is invariant under (S_Q, S_K) -> (A S_Q, A S_K) with A in GL(r_h) (executed residual 1.1e-14). The identity grad_{S_Q} S_Q^T + grad_{S_K} S_K^T = 0 holds to 3.2e-15, so gradient flow conserves S_Q S_Q^T + S_K S_K^T. For content, T_h T_h^T - O_h^T O_h is conserved (identity residual 4.5e-17); see Du, Hu & Lee 2018 and Kunin et al. 2021, both stated for gradient flow.
2. AdamW breaks the conservation. With `weight_decay: 0.0` on these groups, tr(S_Q S_Q^T + S_K S_K^T) grew 2,285x at layer 0 (2,189-2,277x at layers 1-3), and the raw_score_q/k Frobenius norms grew 36-54x. In a tiny executed toy using the same KL, SGD kept the trace between 6.0 and 6.8 over 4,000 steps while AdamW with weight decay 0 drove it to 18.0.
3. The raw singular values track that drift. The reported "minimum raw singular values 6.64 to 12.32" follow the common-scale growth: the layer-3 series runs from 0.93 at step 1,200 to 10.44 at the end. They carry no routing meaning.
4. Scale-free and invariant alternatives. Per-head condition numbers are 2.9-16.0 for S_Q and 1.65-2.45 for S_K. The invariant relative-gain spectrum, sqrt eig((S_K S_K^T)^{-1} S_Q S_Q^T), spans 0.106-5.35 with median 0.63-0.71. Principal-angle cosines between the query and key row spaces span 1.4e-4 to 0.85 (median about 0.37).
5. The condition numbers are not invariant either, and one line misdescribes the singular values. The projected-covariance condition numbers (88.7-550.5) change under A and come from one 128-token window. They bear on factorization accuracy, not on the operator. Because the singular values are weight properties, "These observations concern the sampled evaluations" misdescribes them.
6. The stated schedule is not the effective schedule. Adam's per-coordinate step makes the angular learning rate on scale-invariant weights fall as their norm grows (Heo et al. 2021, AdamP), so the warmup/cosine schedule is not the effective schedule on the routing function.

**Fix:** Replace the line-1159 diagnostics with invariant ones: the relative-gain spectrum and principal angles; generalized eigenvalues of (V_{Q,i}, V_{K,j}) over validation tokens; and O_h T_h spectra. State that the maps carry no weight decay and move along a flat GL(r_h) x GL(s_h) orbit. Two optional parameterization changes leave routing exactly unchanged: gauge-fix with orthonormal key rows plus a compensating query update, or remove the radial component AdamP-style. Proposed replacement for line 1159: "The routing costs are unchanged under (S_Q, S_K) -> (A S_Q, A S_K), A in GL(r_h), and these maps carry no weight decay. Their norms grew by factors of 36 to 54 along this flat direction, so raw singular values and projected-covariance condition numbers describe the stored coordinates rather than the operator. The invariant relative gains, the square roots of the eigenvalues of (S_K S_K^T)^{-1} S_Q S_Q^T, lie between 0.11 and 5.35."
**Falsifies:** Two findings would retract the invariance argument: an executed normalization that makes the raw maps quotient coordinates, or any scale-dependent step in the executed cost.
**Status:** E (numbers transcribed correctly), but presenting them as operator-health evidence inflates their meaning.
**Novelty vs prior review:** new. It confirms L5 and extends F5.

### E4. The frozen intervention probe scores 608 consecutive targets from the start of the validation set
**Location:** Main 1157.
**Severity:** medium
**Evidence:** `collect_beta_channel_decomposition` receives `_batch = next(iter(depth_loader))` with `depth_loader = val_loader` (run_artifacts.py, 965718d, near 3498-3509). The validation iterator is sequential, with seq_len 128, stride 32 and batch 16 (provenance `selection_data_identity`). Overlapping prefixes are masked to -100 (`TokenWindows`, pad_final). The probe therefore scores 128 + 15 x 32 = 608 targets, all from the first ~608 tokens of the validation stream. The intact CE on that passage is 3.043, against 3.4015 on the full validation set, so the passage is 0.36 nats easier. No interval is reported. With per-token CE spread of order 2-3 nats, the standard error of a 608-token mean is at least 0.1 nats before any within-article correlation. The per-layer probes cover only the first 128-token window of the same batch.
**Fix:** Describe the probe as "the first validation batch: 16 overlapping windows that score 608 consecutive targets". Rerun the three arms over the whole validation split with article-level bootstrap intervals.
**Falsifies:** If the executed loader was shuffled or used disjoint windows, the 608 count would be wrong.
**Status:** E, with the sample description overstated ("16 validation sequences").
**Novelty vs prior review:** extends F4 by quantifying its batch-local caveat.

### E5. Training versus held-out loss, passes over the data, and checkpoint choice
**Location:** Main 1136; Table `tab:relational_run` (1146-1151); 1155.
**Severity:** medium
**Evidence:**

1. Passes over the data. Provenance gives `train_data_n_tokens=116,840,318`, so the 491,520,000 presentations are 4.207 passes (metrics `corpus_pass` 4.2068; `steps_per_epoch` 57,050). The manuscript gives presentations but not the unique-token count or the number of passes.
2. Validation turns upward at the end. Validation CE falls monotonically through 3.8312 (120k), 3.7026, 3.5834, 3.4849 and 3.3881 (216k), then rises to 3.4015 at 240k: +0.0135 nats after the minimum. Over the same interval the windowed training CE falls from 3.382 to 3.199.
3. The quoted training PPL is a single minibatch. "Final training-log minibatch PPL 20.6658" comes from one 16 x 128 minibatch. Across the last 24k steps the logged minibatch CE ranges from 2.866 to 3.538 (PPL 17.6-34.4), with mean 3.199 (PPL 24.5).
4. The training loss is not on the evaluation protocol. Training windows are disjoint (stride 128), so training targets average contexts 0-127. Evaluation scores contexts 96-127, apart from the first window.
5. The best checkpoint was not evaluated on test. `best_model.pt` (step 216,000) exists, but test was run on the final weights, as the caption discloses.
6. Parameters versus tokens. The comparison "457M parameters against 117M tokens" is misleading: 98.6% of the parameters are per-type tables (E7). The context-processing parameters number 5.25M, about 22 unique training tokens per parameter. The measured overfitting is modest and appears late, at about 3.8-4.2 passes.

**Fix:** Report unique training tokens and passes. Delete the minibatch PPL, or replace it with a same-protocol evaluation of a fixed training-split sample (for example 10^6 targets at N=128, stride 32) to give an on-protocol generalization gap. Report test CE at both the best-validation and the final checkpoint, and state the selection rule (prior F4).
**Falsifies:** The protocol-mismatch statement would be wrong if the logged training CE were computed on the evaluation protocol. The executed `TokenWindows` walks the training stream by stride = seq_len with pad_final off.
**Status:** E. The minibatch value is correctly labeled "not a test result" but carries no information about generalization.
**Novelty vs prior review:** new.

### E6. The headline perplexity has no calibration, and the abstract omits the dataset and tokenizer
**Location:** Main 52, 1138, 1191.
**Severity:** medium
**Evidence:**

1. The abstract states "test perplexity 31.04" without naming the dataset, tokenizer or context.
2. Word-level normalization. Shoeybi et al. (2019, Megatron-LM, App. E.1) define PPL = exp(-(1/T_o) sum_{t<=T} log P) with T_o = 245,566 word-level test tokens. The total test NLL here is 963,726 nats, which gives about 50.6 (54.4 if end-of-line tokens are excluded, T_o = 241,211). The assumption is that both streams encode the same text; the cache manifest does not certify that.
3. Contextual references (unmatched). Word-level LSTM 48.7 and GCNN-8 44.9 (Dauphin et al. 2017); Transformer-XL Standard 24.0 and Large 18.3 (Dai et al. 2019); a GPT-2-tokenized 125M Transformer at 18.6 (Poli et al. 2023, "same tokenizer" table; longer context, whose length I could not verify).
4. The archive's word-level run is not on the standard protocol either. The 48.42 run scores 241,210 test targets rather than 245,569, and its vocabulary is 267,734 rather than 267,735 (Merity et al. 2017), consistent with end-of-line tokens not being scored.

**Fix:** Abstract: "A four-layer model trained on WikiText-103 with GPT-2 tokenization records token-level test perplexity 31.04 at context 128 (single seed)." Add the word-normalized figure together with its assumption, and a contextual table labeled "different protocols; not matched". Keep all GPT-2-token and word-level runs in separate tables (prior F4).
**Falsifies:** A tokenizer audit showing that the GPT-2 stream is not the same text as the word-level test set would invalidate the conversion. The qualitative placement (the range of 2016-2017 recurrent and convolutional models, well above matched-era transformers) survives any plausible denominator.
**Status:** The text is correctly scoped as E ("not directly comparable"), but the lack of any calibration invites misplacement.
**Novelty vs prior review:** new. The prior review said not to compare across tokenizations; the standard normalization is the accepted way to do so.

### E7. Capacity accounting: 98.6% of parameters sit in per-type tables, and 5.25M process context
**Location:** Main 1136, 1173.
**Severity:** medium
**Evidence:**

1. Parameter partition. The per-type tables hold 50,257 x (8,192 + 3 x 256) + 50,257 = 450,352,977 parameters (98.6%). The positional frames hold 1,048,576. The non-embedding, context-processing parameters are the relational maps (1,048,576), the MLPs (4,203,520) and LayerNorm (512): 5,252,608 in total (1.15%). These parts sum exactly to 456,654,162 (with the dead `decode_log_scale`). `summary.json` reports `active_params_per_token` = 18,176,849, dominated by the 12.9M decoder rows.
2. Convention. Kaplan et al. 2020 (Fig. 6) show that scaling trends are clean only when counted in non-embedding parameters.
3. What the frame table computes. It acts as token-type-conditioned block-diagonal linear maps at each layer's input (xi = U^{-1} mu) and output (m = U(...)), and at the decoder. Final row Frobenius norms have median 4.67 and maximum 7.69, so the cap of 12 is inactive at the end. About 5% of rows fall below 0.68, and about 1% sit near 3.8e-4 (never-seen tokens decayed by exp(-9.1) toward the identity).
4. Older evidence on table capacity. In an old-generation pair, the equal-size additive control (`encode_mode=per_token_additive`) scored 0.48 nats worse than frames (214.50 vs 132.78), but the pair also differed in mean and variance learning rates, so it is confounded.

**Fix:** Report the non-embedding count beside the total, and describe the frame table as a per-type table of conditioning operators. Match the baseline plan on non-embedding parameters and control for the per-type table: the `per_token_additive` arm already exists in the code.
**Falsifies:** The counts are arithmetic from the checkpoint. The interpretation would change only if frames depended on context, and by construction they are fixed through the stack.
**Status:** E. The capacity accounting is correct, but the comparison set it implies is incomplete.
**Novelty vs prior review:** extends F6.

### E8. The archive cannot supply matched comparisons, and every run shares model seed 6 and data-order seed 3
**Location:** Main 1173, 1181-1185.
**Severity:** medium
**Evidence:**

1. No seed variation. All 13 same-generation runs use seed 6 and data_seed 3 (provenance), so neither initialization nor data order has ever been varied.
2. The nearest candidate, 30.14, is not a controlled comparison. It matches the presentation budget exactly (240,000 x 8 x 256 = 491,520,000), but it differs in K, H, L, context (256), stride (128), batch size, mean learning rate, content learning rate (0.0025 vs 0.01) and kl_max. Its test CE is 0.029 nats lower.
3. Protocol alone can move CE by more than a component does. In an old-generation pair differing only in `eval_stride` (138.92 vs 133.18), CE moved by 0.042 nats, more than that generation's single-seed MLP ablation (143.73 vs 138.92: 0.034 nats).
4. The series are confounded. The K-series and depth series differ in steps, batch size, HeadMixer and content learning rate, and in the covariance state (E2).
5. "QKV" is an old-generation comparison. 52.24 vs 52.40 ("QKV" = `use_w_q`, `use_w_k`, `use_w_v`: learned block-local 32x32 query, key and value maps, 30,720 parameters) differ by 0.003 nats. That generation (relational_mode None, belief-gradient E-step, one layer, no LayerNorm) prevents transfer to the featured model.

**Fix:** Re-evaluate the 30.14 checkpoint at N=128, stride 32 (its positional table covers positions 0-127) to remove the protocol difference. Vary both model seed and data-order seed in future replicates, paired across arms.
**Falsifies:** Not applicable (factual inventory).
**Status:** The Discussion's limits are correct; this finding supplies the specifics.
**Novelty vs prior review:** extends the prior "Data available now" section with new specifics (data-order seed, protocol effect size, the meaning of QKV, a re-evaluation route).

### E9. The trained content links are far from the flat-composition regime
**Location:** Main 561-572 (eq. `main_link_composition`), 1189.
**Severity:** low
**Evidence:** The eigenvalue moduli of T_h O_h reach 3,668 at layer 0, with medians of 108-520. The RMS composition defect ||T_h O_h - I||_F / sqrt(32) spans 314-1,551 across heads and layers. sigma_max(O_h T_h) is at most 2.6e4. The summed reference operator sum_h O_h T_h has sigma_max 7,183-32,152 and sigma_min between 1e-4 and 1e-3.
**Fix:** If the Conclusion keeps "lattice-gauge structure at the level of link fields", add that the realized links are dominated by gain and lie far from the flat specialization. Loop observables would then be governed by gain rather than by anything resembling holonomy.
**Falsifies:** Not applicable.
**Status:** The algebra is unaffected. Reading the link geometry as an empirical property of this run is unsupported.
**Novelty vs prior review:** new data, bearing on lead L1.

### E10. Precision scope, environment and executed initialization
**Location:** Main 1136.
**Severity:** low
**Evidence:**

1. What bf16 actually covers. bf16 autocast wraps the stack, but routing and content (relational.py:127, `enabled=False`), LayerNorm (fp32), and decoder plus CE (the model's fp32 island with `.float()` inputs) all run in fp32. Only the coordinate MLP matmuls and non-island glue run in bf16.
2. Environment. PyTorch is a nightly dev wheel. Provenance records deterministic algorithms together with `cudnn_allow_tf32=true`.
3. Initialization. The step-0 norm of `phi_embed` recorded by parameter_motion is 660.56, below the 710.2 implied by `phi_scale` 0.035 with i.i.d. normal entries over 50,257 x 8,192 (ratio 0.930). The K=20 runs match their implied norm to within 0.04%. The executed K=256 initialization therefore cannot be recovered from the configuration alone.

**Fix:** Add one sentence on which operations run in bf16, record the nightly wheel's hash, and report the executed initialization (prior T1).
**Falsifies:** A recovered executed source whose phi initialization explains 660.56 would close the initialization point.
**Status:** E.
**Novelty vs prior review:** extends T1.

## 3. Leads tested

- **L1 (frames as dressing fields; four roles): CONFIRMED on the empirical side, with refinements.** Role (b) routing covariance is static per (token, position) by code: covariance passes through and frames are fixed through the stack. After the decay collapse (E2), it is also at least 98% frame-determined. Role (a) survives only through attention, because the residual is inert (E1). The receiving frame U_i and beta_ii are the only paths by which the receiving token's identity reaches the next layer. The link-field reading has no empirical signature in this run (E9). The dressing-field theory itself lies outside this lens.
- **L2 (Kretschmann): not tested (theory).** It is consistent with E3: the maps are unconstrained and drift along symmetry orbits.
- **L3 (static covariance acts as pair biases): CONFIRMED and sharpened.** Sigma is about 1.045 I (trace CV 1.9%), C_i's anisotropy is at least 98% frame-induced, and the log-det key bias has an across-token sd of 0.14 logits at layer 0. A common rescaling of Sigma acts only on the Mahalanobis term (1/c). With identity frames the router is exactly biased dot-product up to +-5%.
- **L4 (residual numerically inert): CONFIRMED, premise corrected.** `weight_norm_mu` aggregates all role-"mu" groups (92.6% from the relational maps); the token-mean table norm is 380.07 (RMS row 1.70). The archived direct record gives a ratio of 2.2e4. At layer 0 the residual share is at most 5.8e-5 (RMS over the probed window, largest input row). Layers 1-3 are bounded below at ratios 8-28, with a synthetic typical value near 1e3. bf16 does not erase mu at the fp32 add but makes it sub-resolution in the MLP branch. The effect is specific to this run's content learning rate and lack of decay; see 30.14 and 48.42.
- **L5 (comparison/content redundancy): CONFIRMED.** The invariance residual is 1.1e-14 and the Noether identities hold to 3.2e-15 and 4.5e-17. Norm growth is 36-54x with weight decay 0.0 on these groups at both endpoints. The gradient-flow-conserved trace grew 2,285x. The reported singular values and condition numbers are gauge-dependent, while the invariant relative gains span 0.106-5.35. Gauge-fixing is available without changing the function.
- **L6, L7, L8, L9: outside this lens; not tested.**
- **L10 (prose dominated by negations): partially relevant.** Lines 1093-1191 contain 30 negation tokens ("not" 16, "no" 7, "cannot" 3, "without" 2, "neither" 1, "nor" 1). Several disclaimers in Section 5 and the Discussion can now be replaced by measured statements (E1, E2, E4, E5), which strengthens the section without new training.

## 4. Existing runs mapped to placeholders

| Placeholder or question | Existing run(s) | Usable now? | Reason |
|---|---|---|---|
| T2 "current realization" row | 31.04 (K256, L4, N128/s32, 491.52M presentations) | yes, as preliminary | provenance drift is already disclosed; seed 6 only |
| Same-budget secondary point | 30.14 (K160, L6, H5, N256/s128, 491.52M) | only after re-evaluation at N128/s32 | differs in 9 settings; its positional table covers positions 0-127 |
| Width or depth curves | K-series 52.91, 44.19, 39.77, 36.49 (15k-30k steps); K20 depth series 131.38, 119.67, 116.89, 117.50 | no | different steps, batch, HeadMixer and content lr; covariance state differs from long runs (E2) |
| MLP necessity | old generation: 143.73_noMLP vs 138.92 (single difference) | historical only | E-step generation (relational_mode None, prior-bank decoder, one layer, no LN); Delta 0.034 nats, one seed |
| Learned Q/K/V maps vs frame transport | old generation: 52.24 vs 52.40_QKV (`use_w_q/k/v`, block-local 32x32) | historical only | Delta 0.003 nats; different generation |
| Positional frames | old generation: 145.53 vs 130.62 or 137.85 | no | two differences in each pair |
| Table capacity vs frame structure | old generation: 214.50 per_token_additive vs 132.78 | historical, confounded | learning rates differ |
| Word-level comparability | 48.42 (K128, L4, word vocab 267,734), 158.24 | separate table only | end-of-line tokens not scored (241,210 test targets); not the standard protocol |
| F5 numerical events | 31.04 metrics.csv: frame projections in 5 of 200 sampled rows, min scale 0.99989; 0 skipped of 240k; KL cap fraction 0 (one window) | partially | sampled; invariant diagnostics needed (E3) |
| F6 resources | 31.04 summary/metrics: 62,133 s (17.3 h), about 8.0k training tokens/s, peak 25.5 GB, RTX 5090, bf16 | yes, for the archived run | one run; no FLOP model |
| T1 methods record | 31.04 config, provenance and summary scheduler groups | mostly | executed source bytes and init are unrecoverable (E10) |
| Checkpoint dynamics | only step 240,000 survives (`checkpoints/step_240000.pt`, 7.3 GB with optimizer state) plus best and final weights | no trajectory | future runs should keep intermediate checkpoints or log per-table norms |

## 5. Prioritized figures, tables and data to gather

Items are ordered by value per unit of compute. P0 needs no training: it evaluates or inspects existing checkpoints. P1 needs retraining. P2 is logging to add to future runs. Each item is marked NEW or states which prior F/T item it extends.

**D1 (P0, NEW; proposed Table T3, "What the trained operator uses").** Purpose: measure which components the trained model depends on, replacing disclaimers with numbers. Evaluate on the full validation split (and test) with the final and best 31.04 weights, plus 30.14 final. Arms: intact; residual removed per layer (mu + m -> m); Sigma -> I and Sigma -> mean x I; token frames -> I; positional frames -> I; both frames -> I; routing energy removed; positional prior flattened on causal support. Arrays: per-token NLL for every arm (for article-level bootstrap intervals), plus per-layer per-token ||m|| and ||mu|| and per-head self-mass beta_ii. Licensed inference: frozen dependence of the trained operator, not necessity. Existing data: only two routing arms, on 608 tokens (E4).

**D2 (P0, NEW; extends Table `tab:relational_run`).** Purpose: an on-protocol generalization gap and a robustness check on checkpoint selection. Test CE at `best_model.pt` (step 216,000) and at final; a same-protocol training-split sample (10^6 targets, N=128, stride 32); unique training tokens (116,840,318) and passes (4.21). Arrays: summed NLL and scored targets per split and checkpoint. Existing data: the checkpoint exists, but test has not been evaluated on it.

**D3 (P0, NEW; F4 secondary).** Purpose: put the two runs with identical 491.52M-presentation budgets on one protocol. Re-evaluate the 30.14 checkpoint at N=128, stride 32. It still differs in K, H, L and learning rates, so it must be labeled "different architecture, same budget and protocol". Existing data: the checkpoint.

**D4 (P0, NEW; reporting).** Purpose: calibrate the headline. Compute word-normalized test PPL exactly as exp(summed NLL / T_o) after a tokenizer and text audit. Add a contextual table of published word-level and GPT-2-tokenized results, labeled "different protocols; not matched". Existing data: test NLL is available; the audit is not.

**D5 (P0; extends F5 and F3 panel C).** Purpose: operator diagnostics that are invariant under the symmetries, replacing raw singular values and condition numbers. Arrays: per-head relative-gain spectra and principal angles of (S_Q, S_K); O_h T_h and T_h O_h spectra and composition defect; generalized eigenvalues of (V_{Q,i}, V_{K,j}) over validation tokens; the Sigma spectrum; the frame-versus-Sigma split of C_i anisotropy; and a per-head KL decomposition into Mahalanobis, trace and log-det terms (F3 panel C). Existing data: the weight-only parts were computed in this review (`scratchpad/panel/emp/ckpt_analysis.json`); token-level parts need one evaluation pass.

**D6 (P1; extends F4/T2 and re-prioritizes it).** A 2x2 at the featured configuration and budget: frames {learned, identity} x covariance {decayed as in the run (sigma_weight_decay 0.04), live (0.0)}. In the decayed-Sigma, identity-frame cell the router is exactly the biased dot product of Prop. `projected_dot_product` up to +-5%, so that cell is the in-codebase transformer baseline. A separate dot-product arm is informative only in the Sigma-live column. The prior "matched mean-distance arm" drops in priority: in this regime it differs from the dot-product arm only by the key-map Gram constraint and the temperature. Licensed inference: separate effects of per-type multiplicative frame conditioning and of a live covariance channel.

**D7 (P1, NEW).** Purpose: separate raw per-type table capacity from frame structure. Use `encode_mode='per_token_additive'`: the same V x 8192 table, used additively, with identity frames. Existing data: only the old-generation, learning-rate-confounded pair 214.50/132.78.

**D8 (P1, NEW; external anchor).** A standard GPT-style pre-LN decoder with the same tokenizer, N=128, stride 32 and 491.52M presentations. Match non-embedding parameters (4 layers, d=256, 8 heads, MLP 2048, about 5.25M non-embedding parameters). Add one variant matched on active parameters or measured compute, and optionally one token-table-matched variant (an 8192-dimensional per-type embedding projected to 256). Licensed inference: where the realization sits relative to the standard architecture at equal context-processing capacity. It does not license claims about gauge covariance as such.

**D9 (P1; extends the prior residual and MLP controls).** Run `attention_residual=False` and `use_block_mlp=False` at the featured configuration. Prediction from E1: turning the residual off leaves converged CE nearly unchanged; a large change would mean the residual matters through early training dynamics. The MLP arm tests the component the "no neural architecture" program most needs to replace. Licensed inference: necessity within this realization only.

**D10 (P1, NEW).** Purpose: test whether orbit drift and residual inertness are optimizer artifacts that affect CE. Arms: content learning rate 0.0025 vs 0.01, and weight decay on T and O, or an AdamP-style radial projection, or gauge-fixing of (S_Q, S_K). Track ||m||/||mu||, the conserved traces, and CE.

**D11 (P1; extends F4).** Run at least 3 paired replicates that vary both the model seed and the data-order seed for the headline and the D6-D9 arms. Every archived run shares seed 6 and data seed 3. Set the replicate count from a pilot variance estimate.

**D12 (P2, NEW; proposed Figure F7, training dynamics).** Log at every evaluation: per-table norms (not role-aggregated), the common scale and invariant parts of (S_Q, S_K), sigma_max(O_h T_h), ||m||/||mu|| per layer, the log-variance mean and sd, frame-row norm quantiles, and frame projections with their denominators. Keep intermediate checkpoints; the archived run retains only step 240,000.

**D13 (P2; extends F6).** A capacity table: total parameters, per-type tables (98.6%), positional frames, non-embedding parameters (5.25M), active parameters per token (18.18M), and frame-row statistics.

### Proposed placeholders (TeX, same convention as the prior kit; no fabricated values)

```latex
% T3: frozen-checkpoint dependence; insert after Table tab:relational_run.
\begin{table}[p]
\centering
\small
\begin{tabular}{lccc}
\toprule
Frozen intervention (full validation split) & CE (nats) & $\Delta$ CE & 95\% interval \\
\midrule
Intact final weights & pending & 0 & pending \\
Residual removed at every layer ($\mu+m\to m$) & pending & pending & pending \\
Stored covariance replaced by $I$ & pending & pending & pending \\
Token frames replaced by $I$ & pending & pending & pending \\
Positional frames replaced by $I$ & pending & pending & pending \\
Routing energy removed & pending & pending & pending \\
Positional prior flattened on causal support & pending & pending & pending \\
\bottomrule
\end{tabular}
\caption{Dependence of the trained operator on its components, measured by frozen interventions on every validation target. Intervals come from an article-level bootstrap. These are properties of one trained model, not retraining ablations; they do not establish that any component is necessary.}
\label{tab:review-frozen-dependence}
\end{table}

% F7: training dynamics of symmetry-orbit coordinates; methods appendix.
\begin{figure}[p]
\centering
\glkReviewBox{48mm}{FIGURE F7: OPTIMIZATION ALONG SYMMETRY ORBITS\\[4mm]
Panel A: common scale and invariant relative gains of the comparison maps versus step.\\[3mm]
Panel B: largest singular value of $O_hT_h$ and message-to-residual ratio per layer.\\[3mm]
Panel C: stored log-variance mean and spread versus step, with the pure-decay curve.\\[3mm]
TO COLLECT: per-table norms and invariants at every evaluation.}
\caption{Parameter motion during training, split into directions that change the operator and directions along its symmetries. The comparison costs are invariant under a common invertible map of the query and key interfaces, and the content message depends on each head only through $O_hT_h$. Report weight decay and learning rate per group, since both control motion along these flat directions.}
\label{fig:review-orbit-dynamics}
\end{figure}
```

## 6. Boundaries of this review

This review read the manuscript's empirical scope, the full supplement and the prior review. It checked every Section 5 number against archived records. It loaded one checkpoint weights-only on CPU with the GPU hidden, and it read the relevant code at both recorded clean revisions without modifying any repository. The executing dirty source bytes are unrecoverable. Code-based statements therefore rest on the two clean endpoints, which agree on every path cited here.

Not done: no GPU work, no forward pass of the model on text, no training, no Lean, and no tamper or corruption tests. The layer 1-3 residual ratios are bounded rigorously only from below (8-28); the typical value (about 1e3) rests on synthetic inputs and should be measured (D1). Published reference numbers were checked against primary or secondary sources: Kaplan et al. 2020 Fig. 6 via ar5iv; Megatron-LM App. E.1 via arXiv HTML; the Hyena WikiText-103 table via arXiv HTML; Dauphin et al. 2017; Transformer-XL via secondary tables; Du, Hu & Lee 2018; Kunin et al. 2021; Heo et al. 2021; Dong, Cordonnier & Loukas 2021. The context length behind the Hyena Transformer figure was not verified.
