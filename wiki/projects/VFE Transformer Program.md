---
type: project
title: "VFE Transformer Program"
aliases:
  - "VFE Transformer"
  - "Gauge-Theoretic VFE Transformer"
  - "Variational Free-Energy Transformer"
tags:
  - cluster/vfe
  - cluster/gauge-theory
  - cluster/info-geometry
  - cluster/spd-geometry
  - cluster/attention
  - project/transformer
status: draft
created: 2026-06-18
updated: 2026-06-21
---

# VFE Transformer Program

## Goal

The VFE Transformer Program builds and studies a transformer whose forward pass is an explicit act of *variational inference* rather than a plain feature transformation. Each token carries a Gaussian belief — a mean `mu` and a symmetric-positive-definite covariance `Sigma` — and the network's job is to minimize a variational free energy (equivalently, to maximize an evidence lower bound) over those beliefs while it predicts the next token. This recasts perception-as-inference ideas from computational neuroscience and machine learning, namely [[Variational free energy]] and the [[Evidence lower bound (ELBO)]], into a concrete sequence-modeling architecture trained on language.

Three ambitions distinguish this program from a standard transformer. First, inference is *iterative and amortized*: an E-step relaxes per-token beliefs toward lower free energy while an M-step learns the parameters, mirroring the coordinate-ascent view of EM ([[neal-1998-variational-em]]). Second, representations are *geometric*: the per-token features live in gauge frames acted on by a block general-linear group, and the covariance lives on the curved SPD manifold, so optimization respects the underlying [[Fisher information metric]] and the [[SPD-manifold geometry and Riemannian optimization]]. Third, attention is *precision-weighted*: relevance is modulated by belief precision exactly as prediction-error signaling is gated by precision in predictive coding ([[rao-1999-predictive-coding]], [[friston-2010-free-energy-principle]]). The program is therefore a deliberate convergence of four literatures — variational free energy, gauge-equivariant deep learning, information geometry, and SPD-manifold optimization — fused inside the attention mechanism.

## Architecture / approach

The reference configuration is intentionally small so that the geometry, not scale, drives behavior: a **1-layer** transformer whose per-token Gaussian belief has dimension **K = embed_dim**. The live click-run config is **embed_dim = 70 with 7 heads**; an earlier configuration used **embed_dim = K = 20 with 2 heads**. The parameter count tracks K and the vocabulary, so it is config-dependent rather than a fixed figure. Each ingredient links out to its concept or method page.

**Variational inference core.** Training minimizes a free-energy / ELBO objective on per-token diagonal Gaussian beliefs (`family = gaussian_diagonal`). This is the objective of the [[Variational autoencoder (VAE)]] read through the [[Free-energy principle active inference]] lens, derived explicitly for Gaussian beliefs in [[bogacz-2017-free-energy-tutorial]] and operationalized as a [[Predictive coding network]]. Belief updates use the [[Reparameterization trick]] where gradients flow through sampled latents ([[kingma-2013-auto-encoding-variational-bayes]]), and the inference loop is a form of [[Iterative amortized inference]] that refines beliefs by repeatedly consuming free-energy gradients ([[marino-2018-iterative-amortized-inference]]). The E-step / M-step decomposition is the [[Variational EM]] schedule justified by [[neal-1998-variational-em]]; `gradient_mode = filtering` performs partial, online belief relaxation rather than full inference to convergence, a variant that the incremental-EM and predictive-coding-approximates-backprop results license ([[millidge-2020-pc-approximates-backprop]]).

**Gauge structure.** The `gauge_group = block_glk` is a block general-linear group GL(k): token features carry frames that may be re-expressed by local linear changes of basis, a [[Gauge transformation]]. Following the algebra-first construction of [[finzi-2020-lieconv]], group elements are parameterized in the Lie algebra ("phi") and mapped to the group via a [[Baker-Campbell-Hausdorff formula|Baker-Campbell-Hausdorff]] (BCH) retraction, so composition stays exact to the configured order. Per-block **[[Killing form|Killing-form]] preconditioning** supplies a natural metric on the algebra for the M-step. The broader rationale — that a declared symmetry group should structure a network and that beliefs are moved between frames by [[Parallel transport]] (accumulating [[Holonomy]] around loops) — comes from [[cohen-2016-gcnn]], [[cohen-2019-gauge-cnn]], and the Erlangen-program synthesis of [[bronstein-2021-geometric-deep-learning]]. Where features are organized into [[Irreducible representation]] blocks and coupled, the [[Clebsch-Gordan coefficients]] / tensor-product machinery of [[thomas-2018-tensor-field-networks]], [[weiler-2019-e2-steerable]], and [[kondor-2018-compact-group-conv]] provides the bookkeeping for [[Group equivariance]].

**Information geometry.** The objective uses `divergence_family = renyi`: a one-parameter family of [[Renyi divergence]] / [[Alpha-divergence]] bounds that interpolates between the ELBO and the log marginal likelihood ([[li-turner-2016-renyi-vi]]), with ordinary KL recovered exactly in the order→1 limit ([[vanerven-2014-renyi-kl]]). Parameter updates follow the [[Natural gradient]] — the ordinary gradient preconditioned by the inverse [[Fisher information metric]] ([[amari-1998-natural-gradient]], [[amari-2000-methods-information-geometry]]) — realized in practice via Gauss-Newton / damping perspectives ([[martens-2020-natural-gradient-insights]]) and block-Kronecker Fisher approximations ([[martens-2015-kfac]]). The per-block, reparameterization-invariant flavor of these updates matches Ollivier's family of Fisher-based metrics for neural nets ([[ollivier-2015-riemannian-metrics-nn]]).

**SPD covariance geometry.** Each belief covariance `Sigma` is a symmetric-positive-definite matrix updated by an `spd_affine` retraction on the SPD cone under the affine-invariant Riemannian metric ([[pennec-2006-affine-invariant-tensor]], [[bhatia-2007-positive-definite-matrices]]), with the Log-Euclidean metric as a cheaper commutative alternative ([[arsigny-2006-log-euclidean]]). Retractions and vector transports stand in for geodesics and parallel transport for both the SPD covariance and the GL(k) gauge parameters ([[absil-2008-optimization-matrix-manifolds]]), and convergence of mini-batch Riemannian SGD on these manifolds is guaranteed by [[bonnabel-2013-riemannian-sgd]]. Treating a covariance as a first-class differentiable object follows the SPDNet template ([[huang-2017-spdnet]]).

**Attention.** Attention is `precision_weighted`, so affinities are scaled by belief precision in the spirit of [[Precision weighting]] and the kernel-smoother view of attention ([[tsai-2019-kernel-attention]]), modifying the scaled dot-product baseline of [[vaswani-2017-attention]]. An **attention-entropy** term regularizes the attention distribution, and **causal beta / gamma priors** shape the temporal weighting (the live config uses a `causal_alibi` prior). Positional information is layered through registry-selected mechanisms: the live config injects gauge-structured position via a **learned phi composed by BCH (order 4)** (`pos_phi='learned'`). Two further channels exist but are OFF in the current run — **gauge-RoPE** (`pos_rotation='rope'`, base 100; the `rope_on_value` flag selects whether the rotation drives both the attention score and value aggregation, or only the Q/K score) and **T5 relative-position buckets** (a `t5_relative_bias` attention prior). The closest existing precedent for attention computed directly with SPD geometry is [[wang-2023-riemannian-self-attention-spd]]. See [[Attention mechanisms — theory and positional structure]] for the broader theme. The methodological scaffolding for this whole inference loop is collected under [[Inference machinery — variational EM and filtering]], and the wiki's own conventions follow [[karpathy-llm-wiki-pattern]].

## Experiments

Run artifacts (checkpoints, `metrics.csv`, `config.json`, figures) now persist under `V3_Transformer/vfe3_runs/`. Most runs stay in the repo and are not catalogued here; only runs that produce a **finding worth synthesizing** are ingested as `sources/runs/` notes.

| run | K / heads | dataset | test ppl | finding |
|-----|-----------|---------|----------|---------|
| [[2026-06-21-k160-hyperprior-saturation]] | 160 / 4 | wikitext-103 | 76.53 (1 ep), 66.48 (2 ep) | hyper-prior $\lambda_h\mathrm{KL}(s\|r)$ pins at the `kl_max=100` clamp at large K → [[Divergence clamp saturation]] |

> [!note] Finding (2026-06-21) — divergence clamp saturation at large K. At K=160 the K-linear $\mathrm{KL}(s_i\|r)$ saturates the K-independent `kl_max=100` safety-net clamp for ~100% of the vocab (measured median 125, max 584). The hard clamp's gradient is zero above the ceiling, and the filtering kernel's self-mask reproduces that exactly, so the $\lambda_h$ hyper-prior regularizer is **silently disabled** and the learnable centroid `r` is **gradient-frozen** while pinned (under `s_e_step=True` the term is gated out of the scored loss, so this is a dead regularizer, not corrupted training; the model still trains via the live gamma coupling + likelihood). Fix applied: scale the safety-net clamp with width — `kl_max = 8 * embed_dim` in `train_vfe3.py` — which is theory-neutral below the ceiling. Full mechanism, scope, and rejected alternatives: [[Divergence clamp saturation]]; analysis doc `V3_Transformer/docs/2026-06-21-edits.md`.

## Status & next steps

The architecture is configured and three runs have been launched, but the program is at the **pre-results** stage: the immediate blocker is that **checkpoints and metrics are not being persisted**, so even the launched runs cannot yet be evaluated or compared.

Next steps, in rough priority order:

1. Fix artifact saving so training launches write checkpoints and a metrics log; confirm the free-energy / ELBO curve and validation perplexity are being recorded.
2. Add belief-geometry diagnostics — SPD-covariance conditioning, natural-gradient step norms, and gauge [[Holonomy]] around token loops — to verify the geometric machinery behaves as intended.
3. Ablate the distinctive ingredients against the [[vaswani-2017-attention]] baseline: precision-weighting on/off, Renyi order sweep (toward the KL limit), `spd_affine` vs. Log-Euclidean retraction, and the BCH+RoPE+T5 positional stack.
4. Sweep the `filtering` E-step depth to map the amortization-gap / compute trade-off identified by [[marino-2018-iterative-amortized-inference]].
5. **(Done, 2026-06-18)** Repaired the non-flat path. The bilinear `transport_mode='regime_ii'` edge factor $\delta_{ij}=\mu_i^\top W\mu_j$ is gauge-covariant only at $W=0$ (2026-06-18 audit finding), so the gauge-invariant "Route B" — `gauge_invariant_edge_features` (congruence-invariant Mahalanobis/trace/log-det of the belief KL) feeding a learned `connection_M` — was wired as a new registered builder `transport_mode='regime_ii_covariant'`: non-flat **and** gauge-covariant for any weight, default-off, threaded end-to-end and trainable (the config auto-enables `oracle_unroll_grad` for both non-flat regimes), pinned by `tests/test_regime_ii_covariant.py`. Still open: no Yang–Mills kinetic term, and `TODO(Route A)` (commutant-restricted connection on a compact subgroup for exact equivariance + a bounded Wilson action). See [[Non-flat connection and the photon analogy]].

## Cross-links

**Related project:** [[Gauge-Theoretic Multi-Agent VFE Model]] — the multi-agent, continuous-time instantiation of the same GL(K)-gauge VFE theory (this transformer is the language-model instantiation).

**Manuscripts:** [[gl-k-attention]] · [[participatory-it-from-bit]]

**Themes:** [[Variational free energy and predictive coding]] · [[Gauge equivariance and geometric deep learning]] · [[Information geometry and natural gradient]] · [[SPD-manifold geometry and Riemannian optimization]] · [[Attention mechanisms — theory and positional structure]] · [[Inference machinery — variational EM and filtering]]

**Key concepts:** [[Variational free energy]] · [[Evidence lower bound (ELBO)]] · [[Prediction error]] · [[Precision weighting]] · [[Gauge transformation]] · [[Holonomy]] · [[Non-flat connection and the photon analogy]] · [[Natural gradient]] · [[Fisher information metric]] · [[Renyi divergence]] · [[Divergence clamp saturation]] · [[Irreducible representation]] · [[Clebsch-Gordan coefficients]]

**Key sources:** [[friston-2010-free-energy-principle]] · [[neal-1998-variational-em]] · [[bogacz-2017-free-energy-tutorial]] · [[kingma-2013-auto-encoding-variational-bayes]] · [[cohen-2019-gauge-cnn]] · [[bronstein-2021-geometric-deep-learning]] · [[finzi-2020-lieconv]] · [[amari-1998-natural-gradient]] · [[li-turner-2016-renyi-vi]] · [[pennec-2006-affine-invariant-tensor]] · [[absil-2008-optimization-matrix-manifolds]] · [[wang-2023-riemannian-self-attention-spd]] · [[vaswani-2017-attention]]

## Engineering, ML-training & methodology references

Background/implementation references cited by the engineering and ML-engineer review lenses (software-engineering practice, general DL-training mechanics, model baselines, and tooling) — not core VFE theory.

- [[loshchilov-hutter-2017-sgdr-warm-restarts]] — Cosine-annealing-with-restarts schedule;
- [[smith-2017-cyclical-learning-rates]] — Cyclical/one-cycle learning-rate practice;
- [[ioffe-szegedy-2015-batch-normalization]] — Batch normalization;
- [[srivastava-2014-dropout]] — Dropout regularization;
- [[glorot-bengio-2010-understanding-difficulty-training]] — Xavier initialization and training-difficulty analysis;
- [[he-2015-delving-deep-rectifiers]] — He/Kaiming initialization and PReLU;
- [[micikevicius-2018-mixed-precision-training]] — FP16/FP32 mixed-precision training;
- [[goodfellow-bengio-courville-2016-deep-learning]] — The standard deep-learning textbook;
- [[baydin-2017-automatic-differentiation-survey]] — AD survey;
- [[martin-2008-clean-code]] — Software-engineering practice canon informing code-quality standards for the vfe3 implementation (not VFE research theory).
- [[martin-2017-clean-architecture]] — Software-engineering practice canon informing code-quality standards for the vfe3 implementation (not VFE research theory).
- [[fowler-2018-refactoring]] — Software-engineering practice canon informing code-quality standards for the vfe3 implementation (not VFE research theory).
- [[mcconnell-2004-code-complete]] — Software-engineering practice canon informing code-quality standards for the vfe3 implementation (not VFE research theory).
- [[hunt-thomas-2019-pragmatic-programmer]] — Software-engineering practice canon informing code-quality standards for the vfe3 implementation (not VFE research theory).
- [[knuth-art-of-computer-programming]] — Software-engineering practice canon informing code-quality standards for the vfe3 implementation (not VFE research theory).
- [[beazley-jones-2013-python-cookbook]] — Software-engineering practice canon informing code-quality standards for the vfe3 implementation (not VFE research theory).
- [[pep-8-style-guide-python-code]] — Python/PyTorch standards doc informing implementation conventions of the vfe3 codebase.
- [[pep-257-docstring-conventions]] — Python/PyTorch standards doc informing implementation conventions of the vfe3 codebase.
- [[pep-484-type-hints]] — Python/PyTorch standards doc informing implementation conventions of the vfe3 codebase.
- [[pep-695-type-parameter-syntax]] — Python/PyTorch standards doc informing implementation conventions of the vfe3 codebase.
- [[pytorch-documentation]] — Python/PyTorch standards doc informing implementation conventions of the vfe3 codebase.
- [[sculley-2015-hidden-technical-debt-ml]] — ML-systems technical-debt taxonomy;
- [[hooker-2020-hardware-lottery]] — Essay on how hardware shapes which research ideas win;
- [[touvron-2023-llama]] — Open foundation-model release;
- [[touvron-2023-llama2]] — Open foundation/chat-model release;
