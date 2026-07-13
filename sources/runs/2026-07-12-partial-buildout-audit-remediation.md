---
type: run
title: "Partial-buildout audit remediation — seven completion plans (2026-07-12)"
aliases:
  - "2026-07-12 audit remediation"
  - "partial-buildout remediation"
  - "PB-01..PB-15 remediation"
tags:
  - cluster/vfe
  - cluster/gauge-theory
  - cluster/info-geometry
  - project/transformer
  - field/cs-ml
  - field/mathematics
created: 2026-07-13
updated: 2026-07-13
---

# Partial-buildout audit remediation — seven completion plans (2026-07-12)

**Kind:** implementation / remediation record (V3_Transformer). No training metrics. A 2026-07-12 deep audit of `origin/main` @ `4265358` inventoried fifteen partial buildouts (PB-01..PB-15) — features with executable artifacts that stopped before a required configuration, runtime, persistence, or testing boundary — and produced seven completion plans. All seven were executed on 2026-07-12/13 (per-task TDD, per-task adversarial review, whole-plan reviews) and merged as PRs #168–#175. The test suite grew from 2363 to 2741 tests (0 failures). PB-09 (observation-conditioned inference) was deliberately excluded: it is owned by the pre-registered [[Nudged two-phase EM]] plan ([[2026-07-11-backprop-free-plan-and-pure-fep-postmortem]]).

## What was completed, by finding

- **PB-01..04 — artifact and resume integrity.** Ablation cell reuse is now bound to a versioned `cell_contract.json` carrying code identity, corpus SHA-256, and a semantic config fingerprint (stale resume fails closed and recomputes). `train()` gained a one-shot terminal-callback seam so default ablation cells publish a complete artifact set (terminal metrics row, EMA-selected `best_model.pt`, validation-only summary, resumable checkpoint pairing raw weights with raw optimizer moments). Checkpoints embed a validated best-model bundle so cross-run-directory resume restores the selected weights. The EFE ring experiment persists atomic per-seed `trained`/`complete` bundles.
- **PB-05 — H-step EFE policy generation.** `policy_mode="efe_rollout"` is now reachable through `VFEModel.generate` via a bounded top-k beam menu (at most `width` live beams per depth; exhaustive-search parity pinned on a tiny vocabulary). Generation commits the first action of the selected policy; the `policy_mode="none"` branch is byte-identical (golden-pinned).
- **PB-06 — sigma-gate consumer binding.** `sigma_mc` went from a permanent stub to an executable Monte Carlo ambiguity estimator (sealed `antithetic_shared_v1`: 16 shared antithetic samples, local seed-0 generator, safe-Cholesky for full covariance) behind a four-identity fail-closed gate: a model-behavior fingerprint (semantic config + state-dict bytes), a content-based governing-spec identity, a consumer code identity, and a sealed measurement-context fingerprint bound to exact corpus bytes. The empirical FAIL of [[2026-06-29-sigma-gate-fail-and-collapse]] remains authoritative — the shipped preregistration manifest carries only the FAIL entry, so no shipped configuration can enable `sigma_mc`; a future PASS requires a new preregistered identity plus a reviewed manifest update (non-circular because the manifest is excluded from code-identity hashing). Three governing records deleted in a bulk docs cleanup were restored byte-exact from their git blobs, including [[2026-06-28-active-inference-efe-policy-scorer-spec]]'s repo copy.
- **PB-10 — typed hierarchical evaluator.** One `HierarchicalFreeEnergyTerms` evaluator now assembles the q/p/s/h decomposition (self-coupling, belief coupling, attention entropy, two-hop, hyper-prior, model coupling, meta-entropy, observation NLL) with explicit reductions; the legacy scalar `free_energy()` keeps its float32 reduction order byte-for-byte (`torch.equal`-pinned against a reimplemented oracle).
- **PB-11 — model-channel family and transport parity.** The s/r model channel left its diagonal-Gaussian, flat-transport island: packed strict-lower Cholesky storage gives full-SPD s/r tables under `gaussian_full` (zero-init, exactly diagonal at start); `_refine_s`/`_hyper_prior_kl`/`_gamma_energy` dispatch through the configured family; nonflat transport (`regime_ii`, `regime_ii_covariant`, link/charted) is shared with the belief channel via registry statefulness metadata. **Supersession:** `gaussian_full + s_e_step=True` now constructs and runs — the 2026-07-08 usability fact that a meaningful reflection run required `s_e_step=False` ([[2026-07-08-phi-reflection-buildout]]) no longer binds.
- **PB-12 — phi/reflection objective parity.** The phi coordinate substep (`phi_alignment_loss`) now carries the two-hop block (detached hop weights on both factors, same score/value split as `free_energy`), and the Metropolis reflection scorer evaluates the exact active fixed-belief objective — folded precision/tied-gamma priors via one shared effective-prior builder, entry-derived query-adaptive tau, handoff-adjusted final-block prior, active transport/RoPE/fp64 numerics, and `lambda_twohop`. `lambda_twohop=0` and reflections-off are byte-identical no-ops; an executable identity probe against the merge base proved the pure route bit-exact.
- **PB-13 — CG covariance pushforward.** Clebsch-Gordan coupling gained an exact analytic Jacobian at the current mean with delta-method covariance $J\Sigma J^\top$ (symmetrized; explicitly a first-order Gaussian moment closure), opt-in via `cg_covariance_mode="delta_full"`, plus an opt-in q-only moment-divergence regularizer `cg_energy_weight · mean D(q_\text{post}\|q_\text{pre})` that trains path weights under both attached and detached E-step estimators.
- **PB-14 — family-consistent decode.** Generic `family`/`family_chunked` decode registrants score $-D_\text{configured}(q\|p_v)/\tau_\text{eff}$ through the configured family and divergence with no ranking clamp; configuration now fails closed (instead of warning) when a non-Gaussian or noncanonical objective lacks a family-consistent decoder.
- **PB-07 — reporting registries.** Metric and figure registries became production-reachable (declarative `FigureSpec` dispatch with atomic publication and failure isolation); the four orphaned sweep plots (capacity scaling, Pareto frontier, ablation forest, LR grid) gained persisted-artifact production routes keyed to validation bits/token, never test BPC.
- **PB-15 — gradient clipping** became a validated `VFE3Config.grad_clip` field wired through every click-run driver. **PB-08 (partial)** — uncapped corpora stay memory-mapped in native dtype with window-local int64 casting; the provenance corpus hash was dtype-normalized to keep cross-run identity stable.

## Validation

Every plan: per-task red/green TDD with JUnit-verified counts, independent per-task adversarial review with fix loops, and a final whole-branch review before its squash merge. Full-suite gates at each boundary (2406 → 2432 → 2495 → 2508 → 2623 → 2661 → 2741 tests, 0 failures throughout). Two bit-exactness probes: the Plan-5 pure-route identity probe (encoded beliefs, per-layer E-step iterates, logits, loss, gradients, optimizer state compared `torch.equal` against a detached merge-base worktree) and the Plan-4 legacy-reduction-order oracle. Three guarded CUDA smokes (phi-reflection parity, full-covariant hierarchy, `efe_rollout`+`sigma_mc` synthetic-PASS) skip on the CPU host and await an RTX 5090 run.

## Relevance to this research

This closes the implementation gaps between the [[gl-k-attention|GL(K) manuscript]]'s stated objective and the executed one: the frame-alignment subproblem and the Metropolis reflection scorer now descend/score the same active objective as the mean/covariance E-step (previously flagged as an omission on the [[VFE Transformer Program]] page), and the q/p/s/h hierarchy of the [[participatory-it-from-bit|PIFB]] functional has a single typed evaluator. For [[Expected Free Energy]] work, generation-time H-step policy scoring is now executable while the epistemic (sigma) arm stays honestly gated on the unresolved [[2026-06-29-sigma-gate-fail-and-collapse]] finding — the gate design makes "silently enabling sigma_mc" impossible without a new preregistered measurement.
