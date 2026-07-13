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
updated: 2026-07-13
---

# VFE Transformer Program

## Goal

The VFE Transformer Program studies a structural-EM sequence model whose forward pass refines per-token Gaussian model and belief states. In the retained width sweep, one target-blind model-channel refinement is followed by one Fisher-preconditioned own-row belief refinement, after which the parameter M-step minimizes decode cross-entropy through both unrolled paths. These are not coordinate updates of one ELBO, so no global-descent or monotone-evidence guarantee follows. [[gl-k-attention-2026-07-09-review-revision]]

Three ambitions distinguish the program: iterative belief filtering, transported Gaussian comparisons, and precision-weighted attention. Gaussian mean/covariance updates retain their Fisher/AIRM interpretation. At each source SHA recorded for the audited width sweep, the committed optimizer gate and stored configuration route the frame table through AdamW; every provenance record marks a dirty worktree and no dirty diff survives, so the exact executed optimizer implementation cannot be reconstructed. Heavy-ball belongs only to the disabled custom outer frame optimizer, BCH/retraction only to disabled in-E-step frame revision, and the stored pullback preconditioner is inactive because both optional routes are off. None is a demonstrated full-$\mathrm{GL}(K)$ Fisher natural gradient. [[gl-k-attention-2026-07-09-review-revision]]

## Architecture / approach

The reference configuration is intentionally small enough for direct geometric diagnostics: a **1-layer** transformer whose per-token Gaussian belief has dimension **K = embed_dim**. This design choice does not establish that geometry, rather than scale or another coupled factor, causes the observed behavior. As of 2026-07-10, the live click-run config is **embed_dim = K = 20 with 2 heads**. The parameter count tracks K and the vocabulary, so it is config-dependent rather than a fixed figure. Each ingredient links out to its concept or method page. [[gl-k-attention-2026-07-09-review-revision]]

**Variational inference core.** The retained diagonal-Gaussian route uses `prior_source=model_channel` and `s_e_step=true`: one target-blind $s$ refinement toward a learned global, token-uniform $r$ and gamma-weighted model consensus supplies $q^{(0)}=p=s^{(1)}$, followed by one target-blind $q$ refinement. The decode M-step differentiates cross-entropy through both paths. The hyper-prior and gamma terms remain inside the $s$ refinement and are not added again to the scored outer scalar. This finite same-scale route is neither CAVI nor the full multiscale PIFB hierarchy, and its configured rates do not establish a slower $s$ timescale. [[gl-k-attention-2026-07-09-review-revision]]

**Optional two-hop coupling.** On the selected filtering/MM route, the experimental belief-only
extension is

$$
\mathcal F_2(\bar q;q)
=\lambda_2\sum_{h,i,k}
W_{ik}^{(2,h)}(\bar q)
\widehat E_{ik}^{q,h}(q_i;\bar q_k),
\qquad
W_{ik}^{(2,h)}(\bar q)
=\sum_j\beta_{ij}^{(h)}(\bar q)\beta_{jk}^{(h)}(\bar q),
$$

where $\bar q$ denotes the detached state and $\widehat E$ is the registry-selected, clamped
value energy with a live receiver query and detached source key. The scalar uses the clamped value,
and its derivative is gated by the destination clamp mask. Only the hop weights are detached
on every route; the smoothing oracle shares live query and key leaves for the endpoint-energy
derivative. Since $\beta$ is row-stochastic,
$W^{(2)}=\beta^2$ is its two-step Markov transition kernel. The implementation freezes both
attention factors and supplies no independent two-hop prior or categorical relative entropy, so the
term is a frozen-conductance endpoint-consensus surrogate rather than another Gibbs row or a
state-level ELBO. Under the flat vertex cocycle, $\Omega_{ij}\Omega_{jk}=\Omega_{ik}$ makes direct
endpoint transport agree with composed transport, but KL is not path-additive. In edge-local
Regime II, direct and path transports generally differ, removing that composed-path reading.

The selected `mm_exact` ablation does not take a literal gradient step: with covariance frozen and
`mm_damping=0.75`, the term adds a positive neighbor-precision block and changes only the damped
mean target. The anchored contraction bound extends if the preconditioned one-plus-two-hop neighbor
operator remains below one. This does not prove convergence for live state-dependent attention.
The executable scope is belief-only:
there is no gamma counterpart. As of the 2026-07-12 remediation
([[2026-07-12-partial-buildout-audit-remediation]]), the frame-alignment subproblem carries the
term (detached hop weights on both factors, same score/value split as the scalar evaluator), and
the Metropolis reflection accept/reject scorer evaluates the exact active fixed-belief objective
including it; `lambda_twohop=0` remains a byte-identical no-op on both paths. The no-snapshot
E-step trace used by the end-of-run report was not re-audited in that remediation and may still
omit the coefficient. The selected ablation keeps
frame refinement and reflections off while sweeping `lambda_twohop` over `0.0`, `0.001`, `0.005`,
and `0.01`. The canonical pure route keeps `lambda_twohop=0.0`. The term may enter the higher-order
configuration Gibbs energy if its partition function is finite, but it does not evade the fixed
state-level mean-field obstruction. [[vfe-population-generative-status-2026-07-12]]

**Gauge structure.** The real exponential chart reaches only $\operatorname{image}(\exp)\subsetneq\mathrm{GL}^+(K)$, and finite BCH composition is approximate. The optional Cartan/Killing object is a frame preconditioner, not a full-$\mathrm{GL}(K)$ natural metric. Regime-I transport $\Omega_{ij}=U_iU_j^{-1}$ telescopes, so loop holonomy is exactly identity; nontrivial holonomy belongs to an edge-relaxed path. [[gl-k-attention-2026-07-09-review-revision]]

**Information geometry.** Gaussian belief mean/covariance updates use their closed-form Fisher geometry. No audited identification makes the frame conditioner a Fisher, Gauss-Newton, or K-FAC natural gradient. [[gl-k-attention-2026-07-09-review-revision]]

**SPD covariance geometry.** Full-SPD covariances carry the affine-invariant metric, and the diagonal subset retains its belief-side Fisher geometry. A general $\mathrm{GL}(K)$ congruence does not preserve the live diagonal family except for monomial transports, so the implementation is projected or approximate outside that subgroup. [[gl-k-attention-2026-07-09-review-revision]]

**Attention.** Attention is `precision_weighted`, so affinities are scaled by belief precision in the spirit of [[Precision weighting]] and the kernel-smoother view of attention ([[tsai-2019-kernel-attention]]), modifying the scaled dot-product baseline of [[vaswani-2017-attention]]. An **attention-entropy** term regularizes the attention distribution, and **causal beta / gamma priors** shape the temporal weighting (the live config uses a `causal_alibi` prior). Positional information is layered through registry-selected mechanisms: the live config injects gauge-structured position via a **learned phi composed by BCH (order 4)** (`pos_phi='learned'`). Two further channels exist but are OFF in the current run — **gauge-RoPE** (`pos_rotation='rope'`, base 100; the `rope_on_value` flag selects whether the rotation drives both the attention score and value aggregation, or only the Q/K score) and **T5 relative-position buckets** (a `t5_relative_bias` attention prior). The closest existing precedent for attention computed directly with SPD geometry is [[wang-2023-riemannian-self-attention-spd]]. See [[Attention mechanisms — theory and positional structure]] for the broader theme. The methodological scaffolding for this whole inference loop is collected under [[Inference machinery — variational EM and filtering]], and the wiki's own conventions follow [[karpathy-llm-wiki-pattern]].

## Experiments

Run artifacts (checkpoints, `metrics.csv`, `config.json`, figures) now persist under `V3_Transformer/vfe3_runs/`. Most runs stay in the repo and are not catalogued here; only runs that produce a **finding worth synthesizing** are ingested as `sources/runs/` notes.

| run | K / heads | dataset | test ppl | finding |
|-----|-----------|---------|----------|---------|
| [[2026-06-21-k160-hyperprior-saturation]] | 160 / 4 | wikitext-103 | 76.53 (1 ep), 66.48 (2 ep) | hyper-prior $\lambda_h\mathrm{KL}(s\|r)$ pins at the `kl_max=100` clamp at large K → [[Divergence clamp saturation]] |
| [[2026-06-27-gauge-transport-ablation-suite]] | 20 / 2 | wikitext-103 | 154 (learned) vs ~279 (frozen) | historical single-seed development ablations plus the later 3-record width sweep; causal, divergence-order, and positional rankings are not retained in the revised manuscript without frozen multi-seed provenance |
| [[2026-07-05-blocks-k48-gauge-block-scaling]] | 48 / 16→2 | wikitext-103 | 124.57 → 92.15 | fixed-`embed_dim` gauge partition GL(3)$^{16}$→GL(24)$^2$ lowers CE strictly monotonically (S1, 3-seed std ≤ 1.08); reported as a within-sweep **structural ablation curve, not a scaling law** — a red/blue REMAND struck "publishable exponent", "parameter-efficient", and "complementary scaling axis" |

> [!note] Finding (2026-06-21) — divergence clamp saturation at large K. At K=160 the K-linear $\mathrm{KL}(s_i\|r)$ saturates the K-independent `kl_max=100` safety-net clamp for ~100% of the vocab (measured median 125, max 584). The hard clamp's gradient is zero above the ceiling, and the filtering kernel's self-mask reproduces that exactly, so the $\lambda_h$ hyper-prior regularizer is **silently disabled** and the learnable centroid `r` is **gradient-frozen** while pinned (under `s_e_step=True` the term is gated out of the scored loss, so this is a dead regularizer, not corrupted training; the model still trains via the live gamma coupling + likelihood). Fix applied: scale the safety-net clamp with width — `kl_max = 8 * embed_dim` in `train_vfe3.py` — which is theory-neutral below the ceiling. Full mechanism, scope, and rejected alternatives: [[Divergence clamp saturation]]; analysis doc `V3_Transformer/docs/2026-06-21-edits.md`.

> [!note] Finding (2026-07-05) — a second capacity axis (gauge-block partition), REMANDed to a curve. A new sweep `blocks_K48` ([[2026-07-05-blocks-k48-gauge-block-scaling]]) holds `embed_dim=48` fixed and enlarges the GL gauge block GL(3)$^{16}$→GL(24)$^2$ (`n_heads=48/g`, `n_gen=48·g`), the axis complementary to the width axis of [[2026-06-27-gauge-transport-ablation-suite]]. Test PPL falls strictly monotonically 124.57 → 92.15 across g = 3,6,8,12,24 at a 245.76M-token budget, robust over 3 seeds {6,23,64} (per-label std ≤ 1.08). A full-panel red/blue debate **REMANDed** the compound claim (unanimous 3-judge, Rule 2 scope override): only the ablation curve (**S1**) survives; it must be reported as a curve, **not** a scaling law. Struck: "publishable exponent" (axis-dependent — 0.929 vs `n_params` with CI [0.07, 1.73], 0.181 vs `n_gen`, degenerate vs FLOPs — over < 1 decade of range); "parameter-efficient" (the flat ~12.06M `active_params_per_token` is the definitional identity `5·V·K + 2·K + n_gen`, not a measurement; real transport grows 64× ∝ g², wall-time is U-shaped with GL24 the slowest run, and blocks is +4.8 to +12.8 PPL worse than width at matched total params); and "complementary scaling axis" (a cross-sweep comparison across a 2× token gap vs `grow_K_GL10`, non-identified under Chinchilla's `E + A·N^{-α} + B·D^{-β}`). Upgrade path (converts REMAND → win): a matched 491.52M-token blocks run + a non-gauge `V × m` learned-table control at `m = n_gen` + a tied-gauge (`tied_block_glk`, `n_gen = g²`, or `so_n`-tied) control. Absent from both manuscripts. Full adjudication: `V3_Transformer/docs/debates/2026-07-05-blocks-k48-gauge-block-scaling-axis/`.

## Status & next steps

The architecture is configured and run artifacts persist under `V3_Transformer/vfe3_runs/`. The revision ledger now governs eleven claim families, so analytic completeness is not claimed. Historical development artifacts remain useful for designing reruns but do not override the current evidence scope. [[gl-k-attention-2026-07-09-review-revision]]

Next steps, in rough priority order:

1. **(Done, 2026-06-18)** Artifact saving — training launches write checkpoints, a metrics log, `config.json`, and figures under `vfe3_runs/`; the free-energy / ELBO curve and validation perplexity are recorded.
2. Add belief-side SPD/Fisher diagnostics; reserve nontrivial holonomy diagnostics for edge-relaxed or otherwise nonflat transport because strict Regime I has $H=I$. [[gl-k-attention-2026-07-09-review-revision]]
3. Rerun the distinctive ingredients against the [[vaswani-2017-attention]] baseline with frozen provenance and multiple seeds (full roadmap: [[VFE Transformer Research Directions (2026-06-21)]]). The **gauge on/off / frozen-random** toggle exists and a 2026-06-27 single-seed development run showed a large learned-versus-frozen gap, but the revised manuscript does not retain that causal claim. The divergence-order and positional comparisons likewise remain rerun targets rather than validated rankings.
4. Sweep the `filtering` E-step depth to map the amortization-gap / compute trade-off identified by [[marino-2018-iterative-amortized-inference]].
5. **(Done, 2026-06-18)** Repaired the non-flat path. The bilinear `transport_mode='regime_ii'` edge factor $\delta_{ij}=\mu_i^\top W\mu_j$ is gauge-covariant only at $W=0$ (2026-06-18 audit finding), so the gauge-invariant "Route B" — `gauge_invariant_edge_features` (congruence-invariant Mahalanobis/trace/log-det of the belief KL) feeding a learned `connection_M` — was wired as a new registered builder `transport_mode='regime_ii_covariant'`: non-flat **and** gauge-covariant for any weight, default-off, threaded end-to-end and trainable (the config auto-enables `oracle_unroll_grad` for both non-flat regimes), pinned by `tests/test_regime_ii_covariant.py`. Still open: no Yang–Mills kinetic term, and `TODO(Route A)` (commutant-restricted connection on a compact subgroup for exact equivariance + a bounded Wilson action). See [[Non-flat connection and the photon analogy]].

> [!note] Design spec (2026-06-28) — active-inference EFE policy scorer (pre-registered, not implemented). A default-off, no-grad [[Expected Free Energy]] policy scorer over candidate token continuations is now specified and pre-registered for the vfe3 generation path ([[2026-06-28-active-inference-efe-policy-scorer-spec]]) — the first operationalization of EFE for the transformer, where it was previously native to the [[Gauge-Theoretic Multi-Agent VFE Model|multi-agent]] setting. It scores $G(\pi)=\mathrm{KL}[q(o\mid\pi)\,\|\,p(o\mid C)]+\mathbb{E}_{q(s\mid\pi)}H[p(o\mid s)]$ with an explicit peaked task preference and selects via $\mathrm{softmax}(-\gamma G)$, adding no learned parameters ($\texttt{policy\_mode='none'}$ is byte-identical to HEAD). Honest scope: at the v1 one-step sigma-free point belief the information-gain term is identically zero, so v1 is a *pragmatic preference-matching reranker*; information-seeking active inference, the agent-set/community case, and any train-time EFE are deferred, and no efficacy is claimed. *(Superseded in part 2026-07-12: `efe_one_step` and the H-step `efe_rollout` are now implemented and reachable through generation — see [[2026-07-12-partial-buildout-audit-remediation]].)*

> [!note] Finding (2026-06-29) — sigma-validation gate FAIL; the belief covariance is a near-static prior. The pre-registered $\sigma$-validation gate for the EFE scorer was measured and **FAILed** ([[2026-06-29-sigma-gate-fail-and-collapse]]): on the prior-bank decode checkpoint $\mathrm{tr}(\Sigma_q)$ is *anti-correlated* with realized cross-entropy ($\rho=-0.137$) and near-constant (cv $0.0445$), so $\sigma$ is not a usable epistemic signal and the EFE information-gain arm stays inert empirically. Root cause (code-verified, adversarially checked): the deployed belief E-step is **target-blind** — its $\nabla_\Sigma$ has no observation/data-precision term (the canonical $-\mathbb{E}_q[\log p(o\mid x)]$ is a gated stub with no live caller), so $\Sigma_q$ is pinned to a per-token prior table shrunk toward one shared centroid and never contracted by evidence; the anti-correlation sign is a mean-borne confound, not a covariance-readout effect; the SPD-retraction clamp is *not* the limiter. This matches the [[gl-k-attention|GL(K) manuscript]]'s explicit "the observation enters only the M-step loss, so the E-step is target-blind" ([[Variational EM|structural EM]]) and deviates from the canonical [[participatory-it-from-bit|PIFB]] functional, which places the observation term in the belief subsystem. Making $\sigma$ epistemic would require wiring an observation-precision term into the E-step covariance gradient. Full mechanism + manuscript reconciliation: `V3_Transformer/docs/research/active-inference/2026-06-29-why-sigma-collapses.md`.

> [!note] Coefficient correction (2026-07-10) — grow_K_GL10 descriptive fits. The weighted offset cross-entropy fit gives $\alpha=0.5561$ (95% nested-cluster bootstrap interval $[0.400,0.600]$), $A\approx9666$, $E=3.9453$, and $R^2=0.99955$. Every run uses 491.52 million tokens while tokens per parameter fall from 64.66 to 5.42; the mixer is off at $K=10$ and on at $K\geq20$; and some width cells span source SHAs. The coefficients summarize a heterogeneous development sweep, not an irreducible term, compute-optimal frontier, or transferable scaling law. [[gl-k-attention-2026-07-09-review-revision]]

> [!note] Routing correction (2026-07-10) — retained sweep is two-channel. All 36 archived configurations activate the same one-$s$/one-$q$ route with `e_s_mu_lr=0.85`, `e_s_sigma_lr=0.1`, `lambda_h=0.25`, `lambda_gamma=0.75`, `kappa_gamma=1`, `learnable_r=true`, and `r_update_mode=gradient`; every summary scaling point has `model_channel_active=true`. Learned outer parameters include the model tables, global $r$, token and learned positional frame parameters (`pos_phi='learned'`), the linear output and bias (`decode_bias=true`), and the mixer where active. The archived configs plus committed code at the recorded SHAs reconstruct this route, but every provenance record has `git_dirty=true` and no dirty diff survives, so the source SHAs do not identify the exact executed bytes. [[gl-k-attention-2026-07-09-review-revision]]

> [!note] Buildout (2026-07-08) — omega_direct element-store gauge + a learnable det-sign. A second [[GL(K) gauge group|GL(K)]] frame parameterization, `gauge_parameterization="omega_direct"`, stores each token's frame as a group element $U_i$ and transports by the stored cocycle $\Omega_{ij}=U_iU_j^{-1}$ instead of $\exp(\phi_i)\exp(-\phi_j)$ ([[2026-07-08-omega-direct-detsign-buildout]]). It was threaded through the gamma / model-coupling (s) channel with frame-fidelity (so the s-channel transports by $U$, not the $\exp(\phi)$ cocycle) and given a **learnable discrete orientation** via `omega_reflection="metropolis"`: a $\Delta F$-gated Metropolis flip over the $\det$ sign — the program's first mechanism for *learning* the discrete $\pi_0(\mathrm{GL}(K))=\mathbb{Z}/2$ gauge component, which the $\exp(\phi)$ parameterization (confined to $\mathrm{GL}^+(K)$) cannot reach. Two findings: (i) a **gauge-invariance** test certifies covariance but *cannot* certify which covariant transport is used ($U$ vs $\exp\phi$, both gauge-covariant) — frame *use* needs direct frame-perturbation tests; (ii) under the live `gaussian_diagonal` family the reflection is **near-inert** (it leaves the squared diagonal congruence invariant, so $\Delta F\approx 0$ and the det-sign thrashes at $\approx100\%$ acceptance) — it does useful sheet selection only with a full / off-diagonal covariance family or a low temperature. Default-off, opt-in; the pure $\exp(\phi)$ path stays byte-identical. `origin/main` @ `24500e9`.

> [!note] Buildout (2026-07-08) — the cheaper $R\exp(\phi)$ route on the phi path. The same learnable det-sign, but for the DEFAULT `phi` parameterization: prepend a per-token reflection to $\exp(\phi)$, $g_i=R_i\exp(\phi_i)$ (so $\det g_i=-e^{\operatorname{tr}\phi_i}<0$; $\det\exp(\phi)$ is *always* $>0$, which is why $\exp(\phi)$ alone is stuck in $\mathrm{GL}^+(K)$). This reaches the $\det<0$ sheet with a single sign **bit** per token instead of a stored $K\times K$ element ([[2026-07-08-phi-reflection-buildout]]); `phi_reflection="metropolis"` learns it via the *same* $\Delta F$-gated Metropolis flip, threaded through every channel. Reach is $R\cdot\mathrm{image}(\exp)$ (misses the non-exp interior `omega_direct` reaches) in exchange for reusing the full $\exp(\phi)$ / BCH / Killing machinery — realizing $\mathrm{GL}(K)=\{I,R\}\cdot\mathrm{GL}^+(K)$. The two findings above carry over (the discrete $\pm1$ sign has no continuous $g$-action, so a gauge-invariance test over it is empirically inert; near-inert under `gaussian_diagonal`, so a meaningful run needs `gaussian_full`; the `s_e_step=False` half of that restriction was lifted 2026-07-12 when the model channel gained full-SPD support — [[2026-07-12-partial-buildout-audit-remediation]]). The build also fixed a **latent `omega_direct` bug**: `block.py`'s post-E-step transforms dropped the stored frame for layers past the first under `head_mixer` / `cg_coupling` / `block_norm` at `n_layers>1` (now `_replace`-preserved). Default-off. `origin/main` @ `7ffb68e`.

> [!note] Buildout (2026-07-12) — partial-buildout audit remediated; EFE rollout live, sigma_mc gate-closed, model channel completed. A deep audit of `origin/main` @ `4265358` inventoried fifteen partial buildouts (PB-01..PB-15); seven completion plans were executed and merged the same day (PRs #168–#175; suite 2363 → 2741 tests, 0 failures) — full record: [[2026-07-12-partial-buildout-audit-remediation]]. Program-relevant deltas: (i) the [[Expected Free Energy]] scorer's `efe_rollout` mode is now **reachable through generation** via a bounded H-step beam menu (the 2026-06-28 spec is no longer "not implemented"), and `sigma_mc` has an executable antithetic MC estimator behind a **four-identity fail-closed gate** whose shipped preregistry carries only the empirical FAIL of 2026-06-29 — no shipped config can enable it; (ii) the phi frame-alignment subproblem and the Metropolis reflection scorer now evaluate the **exact active objective** (two-hop, folded priors, adaptive tau), closing the objective-parity omissions previously noted here; (iii) the s/r model channel gained full-SPD packed covariance storage, family dispatch, and shared nonflat transport — `gaussian_full + s_e_step=True` now constructs, superseding the 2026-07-08 usability restriction; (iv) CG coupling gained a first-order covariance pushforward and an opt-in moment-divergence energy; decode can follow the configured family/divergence; the q/p/s/h hierarchy has one typed evaluator with the legacy scalar reduction order pinned byte-for-byte. Guarded CUDA smokes await an RTX 5090 run.

> [!note] Plan (2026-07-11) — backprop-free learning track pre-registered ([[Nudged two-phase EM]]). A 14-agent adversarial investigation (recon / design / challenge / synthesis, file:line spot-verified) produced `V3_Transformer/docs/plans/2026-07-11-backprop-free-vfe-lm-plan.md` and the run note [[2026-07-11-backprop-free-plan-and-pure-fep-postmortem]]. Two banked results: (i) the adjudicated post-mortem of VFE_2.0's `pure_fep` clean-EM attempt (~25000 PPL): its target-blind fixed point structurally dropped the through-$q^*$ credit term $(\partial\mathrm{CE}/\partial q^*)(\partial q^*/\partial\theta)$ — everything but the prototype readout was reservoir computing — compounded by raw global-LR Euclidean M-steps at $1/\tau\sim 1/K$ gradient scale, encode/decode tying, and sign-monotone hyperparameter updates; (ii) a temperature degeneracy: $\partial F_{red}/\partial\tau=\mathrm{KL}(\beta\|\pi)\ge 0$ (sympy-verified), so softmax temperatures cannot be learned by descending $F$ — they need contrastive or held-out estimation. The prescription is a nudged two-phase EM (free phase = deployed inference; symmetric $\pm\lambda$ target-nudged continuations; EqProp contrasts carry all non-decode credit; analytic per-row Gauss-Newton decode; quarantine rule for sign-monotone knobs), realizing the [[participatory-it-from-bit|PIFB]]-canonical observation placement whose absence caused the 2026-06-29 sigma collapse. Design only — no training results; milestone gates run measured BPE unigram → KenLM 5-gram → the DFA band ([[launay-2020-dfa-transformers]], the only published backprop-free transformer LM PPLs) → 2x matched-K backprop vfe3.

## Cross-links

**Related project:** [[Gauge-Theoretic Multi-Agent VFE Model]] — the multi-agent, continuous-time instantiation of the same GL(K)-gauge VFE theory (this transformer is the language-model instantiation).

**Manuscripts:** [[gl-k-attention]] · [[participatory-it-from-bit]]

**Themes:** [[Variational free energy and predictive coding]] · [[Gauge equivariance and geometric deep learning]] · [[Information geometry and natural gradient]] · [[SPD-manifold geometry and Riemannian optimization]] · [[Attention mechanisms — theory and positional structure]] · [[Inference machinery — variational EM and filtering]]

**Methods:** [[Nudged two-phase EM]] — the pre-registered backprop-free learning prescription

**Key concepts:** [[Variational free energy]] · [[Evidence lower bound (ELBO)]] · [[Prediction error]] · [[Precision weighting]] · [[Gauge transformation]] · [[GL(K) gauge group]] · [[Holonomy]] · [[Non-flat connection and the photon analogy]] · [[Natural gradient]] · [[Fisher information metric]] · [[Renyi divergence]] · [[Divergence clamp saturation]] · [[Irreducible representation]] · [[Clebsch-Gordan coefficients]] · [[Expected Free Energy]] · [[Active Inference]]

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
