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
updated: 2026-10-27
---

# VFE Transformer Program

## Paper arms: frames against capacity and baselines, October 25 to 26, 2026

[[vfe3-2026-10-26-paper-arms]] is the registered main-results comparison at $K=128$, six layers, ALiBi without rotary encoding, one epoch of WikiText-103, three seed pairs per arm. The frame decision rule stands on all three clauses: the per-type read-table comparator is worse by 0.361 nats of test CE, frames frozen at random initialization by 0.207, and an identity-frame model with a per-type additive table of the frame table's size by 0.154, against a 0.03-nat margin. Random frames recover almost none of the 0.212-nat cost of removing frames and the equal-size table recovers about 27%, so the advantage belongs to learned frame structure and not to additive capacity; a per-type multiplicative map without gauge structure remains untested. Two results bound the broader claim. A conventional transformer of matched total parameters ([[vaswani-2017-attention]]) beats the VFE model by 0.160 nats, and giving the read-table comparator the VFE model's optimizer shrinks its gap from 0.361 to 0.119 nats. Per step, the VFE model leads every conventional arm early (by 0.153 nats of train CE over the matched-total transformer at step 1,000) and is overtaken by the matched-total transformer near step 4,700 on validation; that arm's hidden-matrix learning rate was untuned. Covariance-blind (mean-distance) routing matches Gaussian-KL routing within 0.002 nats.

## Backprop-free local learning test, October 21 to 25, 2026

[[vfe3-2026-10-25-local-learner-test]] is the first executed test of the program's backprop-free half. On a linear-Gaussian byte model with a probit vocabulary tree and one assumed-density filter, stepwise EM on posterior statistics reached 0.925 and 0.906 of backpropagation's one-pass gain at state sizes 32 and 64, beat a target-blind control by 0.59 to 0.89 bits per byte, and held backpropagation's optimum as a fixed point; the remaining gap is optimization speed. Group-valued transitions $G=e^{L}$ cost both rules, because the learned transitions have isolated negative eigenvalues and no real logarithm ([[culver-1966-existence]]). The trained $K=192$ transformer's exponential content links show near-annihilated directions instead; whether that costs loss awaits a matched affine-chart run. The test does not bear on nonlinear dynamics or on the attention architecture; a switching linear-Gaussian stage and a $d=128$ trend point are recorded as future work in VFE_3.0's `TODO.md`.

## Edge-dependent and latent content links, October 6, 2026

[[dennis-2026-edge-latent-links]] records the theory and implementation of the opt-in `content_link_edges` (`lowrank`, `pure_gauge`) and `content_link_latent` arms merged on October 5: closed-form rank-$r$ message and covariance, the pure-gauge holonomy control, causal receiver-factor inference with its local convergence condition, the loop prior, and the measured CPU costs. The arms are implemented and tested at small size; no training result is recorded. See [[GL(K) gauge-equivariant attention]].

## Manuscript rework, October 5, 2026

[[dennis-2026-glk-attention-v2-rework-2026-10-05]] rebuilds the main GL(K) manuscript (body cut to 32 pages, supplement revived as S1 to S10) around agents on a bundle over one context, the comparison link, and a routed-transport theorem in which a standard transformer layer is the affine chart with a full residual; see [[GL(K) gauge-equivariant attention]]. The October 7 peer review and revision is [[dennis-2026-glk-attention-v2-review-2026-10-07]]. A separate note, [[dennis-2026-minimal-agent-model]], declares a tied key-and-content agent whose receiving map and residual are derived by Bayesian conditioning, a candidate non-neural communication layer. It was implemented in VFE_3.0 on October 6 as the selectable readout `predictive_readout="minimal_agent"`, together with the `prototype_agents` block MLP (`VFE_3.0/docs/2026-10-06.md`).

## Lie-algebra links in the main manuscript, October 4, 2026

[[dennis-2026-glk-lie-algebra-links-v2]] integrates the exponential links of Option A, the three implemented `content_link_chart` options and the `channel_likelihood`/`closed_form` receiver into the main GL(K) manuscript (revision drafted by Claude Opus 5.5; 58 float64 identity checks; no cross-model review). The charts apply the stored maps through the effective receiving maps $\widetilde O=O$, $T^{-1}+O$ and $e^{OT}T^{-1}$, which represent the same tiled mean maps up to the real-logarithm domain.

## Backpropagation-free generative language architecture, October 4, 2026

[[dennis-2026-backprop-free-vfe-language-architecture]] develops a proposed fully non-neural continuation of the program. It replaces target-blind forward refinements and outer backpropagation with a declared causal latent-agent model: prefix-only fast beliefs and finite-entropy link posteriors infer current context; persistent template, channel, anchor, and hyperprior variables learn slowly through posterior statistics or local analytic scores. Two normalized observation laws are specified: a probabilistic vocabulary tree driven by a link-bearing Gaussian state, and a contextual Gaussian-template kernel with categorical concept emissions. The latter's observation-to-carrier score is $\gamma-\rho$, so the contextual normalizer is part of the learning signal. The report separates exact model-evidence or fixed-$q$ ELBO learning from the perplexity of a finite deployed inference schedule.

This advances the causal-observation gap recorded in [[dennis-2026-neuron-free-agent-theory]] but does not close the full replacement question. Small CPU formula checks support selected derivatives and normalization only. A complete scalable recognition family, nonconjugate update schedule, matched large-population language study, and predictive tests of learned parent structure remain open. No VFE_3.0 code, configuration, GPU job, or training run was changed.


## Dynamic links (theory), October 3, 2026

[[dennis-2026-dynamic-links]] works out how the exponential links could become dynamic: the link generators are latent variables with a normalized prior inside the free energy, and their evolution is inference. The note boxes the resulting free energy and derives a delta-rule link field equation, the necessity of the link prior, a linearized screened Euclidean Maxwell equation whose kinetic term comes from time-like loops of the depth-by-token lattice, and the Wilson action induced by undirected Gaussian matter. The current `content_link_chart="exponential"` (VFE 3.0 PR #41) is its static limit with anchor $\bar X=OT$. Nothing is implemented or trained. The obvious implementation path is per-context deviations from $OT$ obtained by a few Fisher-preconditioned steps or by one linearized solve. The all-edge cost $O(LN^2K^3)$ per step points to restricted supports, low-rank deviations or amortization. Open: loop weights and couplings, multi-head cross-edge terms, and the Gauss-law constraint from time-like links. The multi-agent theory now carries the same chart as latent per-edge generators ([[multiagentelbo-2026-10-04-lie-algebra-links]]), and two statements of the note were corrected on October 4: the invariance group of the Frobenius defect, and the location of the unregularized chart infimum.

## Unified attention companion, October 3, 2026

The author subsequently retired the six superseded working `.tex` notes. `manuscripts/Attention/attention_unified.tex` is their replacement; earlier originals remain in Git history, and immutable source notes retain their dated provenance. The author moved the gradients and extension companions into `manuscripts/Attention/Misc_Attention_Docs/` and removed the six superseded PDFs. See [retirement mapping](../../docs/attention-note-retirement-2026-10-03.md).

[[dennis-2026-attention-unified]] unifies the six Attention notes and maps their relationship to all four current GL(K) manuscripts. The author's primary future integration choice is Option A exponential group-valued links; compression and the current routed head sum are supporting comparisons. The standalone file was `manuscripts/Attention/attention_unified.tex`, removed from the vault by the author on 2026-10-06 (the source note keeps its record); no GL(K) source was edited. The companion corrects the real-log chart scope, complement-residual assumptions, causal inverse-edge loop distinction, Fisher stabilizer/completion boundary, and frozen-receiver posterior interpretation.

The inspected VFE_3.0 launcher selects projected predictive attention with moment-matched diagonal covariance and AdamW frames. Other derived paths are labeled selectable or proposed. Routing-holonomy diagnostics already present as working-tree changes were inspected and tested. An independent VFE_3.0 publication committed those same file bytes in pull request 40 during consolidation; this manuscript task made no implementation changes. Historical performance numbers and small-dimensional identity checks are kept separate from current execution evidence; no new training or GPU study was run.

## Current executable state, October 2, 2026

After VFE_3.0 PRs #32 (October 1) and #34 to #39 (October 2), recorded in `VFE_3.0/docs/2026-10-02.md`, the executable model has two attention routes, [[Projected predictive attention]] and [[Projected gradient attention]]; two structure groups, `block_glk` and `so_n` (the latter with one equal irrep block per head); and two belief families, `gaussian_diagonal` and `gaussian_full`. Transported attention ($\Omega_{ij}=U_iU_j^{-1}$ carrying comparison and content), `projected_conditional`, the `mm_exact` E-step, the canonical free-energy code, Rényi divergences, `regime_ii` transport, the `gaussian_diagonal_exact` and `gaussian_frame_diagonal` families, and the `glk`, `tied_block_glk`, `so_k`, `sp` and `sp_n` groups are retired, with loader migrations for saved configs and unchanged checkpoint parameter names. SU(N) is not implemented. The gradient route now defaults to the channel-likelihood receiver with closed-form natural-parameter updates, derived in [[dennis-2026-projected-gradient]] in answer to the October 1 audit's finding that the PR #30 Euler step was unstable at launcher rates, and it accepts the profiled state-dependent self-coupling $\alpha^\star=c_0/(b_0+D)$ as a majorize-minimize step. All verification was CPU-only with tiny models (bitwise equivalence to the pre-change trees where behavior was meant to be unchanged; full suites with zero failures). No GPU or training run of the new gradient receiver exists, unequal so_n irrep towers remain unsupported, and damped diagonal closed-form steps carry no descent guarantee.

> [!warning] Pure path. The October 1 audit reported that after PR #32 no configuration executes the canonical free energy with gauge-KL routing, and that remains true. Both routes route by learned comparison maps; [[dennis-2026-projected-gradient]] reads this as exact inference in a declared cut model, which is a different model, not a restoration of the canonical functional. Whether to restore an opt-in canonical route was left to the user.

The frame-table optimizers of 2026-09-28 (belief-Fisher natural gradient and the `group_log` retraction) are written up in [[dennis-2026-phi-natgrad]]. A September 20 rigorous theory search, [[dennis-2026-neuron-free-agent-theory]], gives a conditional neuron-free construction (source and reliability inference plus KL-budget scale control in one constrained ELBO) and leaves the full replacement question inconclusive.

## Group-valued origin of the matrix links, October 2, 2026

[[dennis-2026-link-origin]] (agent-drafted technical note, identities checked in float64 at $K=6$ or $7$, nothing trained) relates the singular links of the projected routes to group-valued links through an exponential link, a parabolic compression with Schur complement, and the head-sum operator, and derives that the code's tiled heads ($K=Hd$) correspond to no residual at all in the exponential construction ([[Lattice gauge theory]], [[Projected predictive attention]], [[Projected gradient attention]]). Open theory directions it records: whether a projected residual stream with $Hd<K$ trains as well as the additive residual, whether a self-gate $e^{\beta_{ii}}$ or a state-dependent self-link should replace part of the block MLP ([[Activation Functions]]), an edge-dependent generator (without which the tiled exponential link adds no expressive power), hidden-block identifiability under the chosen receiver energy, and measuring the routing triangle defect in trained models ([[Holonomy]]).

## Link curvature and chart-natural optimization, October 2, 2026

[[dennis-2026-link-curvature]] (agent-drafted companion to [[dennis-2026-link-origin]], float64 checks at $K=4$, nothing trained) defines the triangle holonomy of the causal link field, shows that flat means recurrent and invertible flat means pure gauge, tabulates the holonomy of the candidate edge-dependent generators (positional flat, constant maximally curved, routed exponent additive defect, head sum multiplicative defect), and adds the regression link of a joint Gaussian whose curvature is the partial cross-covariance and whose rank-$d$ optimum is reduced-rank regression ([[Holonomy]], [[Lattice gauge theory]], [[Canonical Correlation Analysis]]). It also shows that the singular boundary of $\mathrm{GL}(K)$ is at infinite Fisher distance and that additive affine updates can cross it while multiplicative updates cannot ([[Natural gradient]]). Open theory directions it records: whether trained routing has holonomy closer to the flat pattern $\beta_{ij}=c_i/c_j$ than to uniform attention (computable from logged routing weights, unmeasured); whether the learned $(O,T)$ match reduced-rank regression directions; a correlated variational family to supply the cross-covariances; multiplicative or Fisher-preconditioned updates for the content maps; and whether any of this relates to perplexity, which is unknown.

## Projected predictive route note and covariance toggle, September 27, 2026

[[dennis-2026-projected-predictive]] documents the `projected_predictive` route end to end and maps each launcher toggle to its equation ([[Projected predictive attention]]). Passthrough keeps $\Sigma$ at encode. The new opt-in `predictive_covariance="moment_matched"` assigns the exact moment-matched covariance of the predictive kernel instead, which makes $\Sigma$ context dependent and feeds it to the next layer's routing, the prior-bank decoder, and [[Template routing]]. `train_vfe3.py` now lists `predictive_covariance`, `predictive_covariance_floor`, `block_mlp_mode`, and `block_mlp_covariance` at their defaults. The matched comparison against passthrough has not been run.

## Template routing toggle, September 27, 2026

[[Template routing]] is a derived candidate for the block MLP whose interpretation the matrix-links manuscripts left open. Token beliefs route by $\rho^*_{ia}\propto\pi_ae^{-\mathrm{KL}(q_i\|p_a)}$ to $M$ learned diagonal Gaussian templates and receive $\sum_a\rho^*_{ia}w_a$; the rule follows from a mixture-prior free energy and reduces to a softmax-gated MLP when the templates share a covariance ([[dennis-2026-template-routing]]). It is available as `block_mlp_mode="gaussian_template"` in the VFE_3.0 working copy (passthrough covariance, local coordinates, about 1.5× the MLP's parameters at equal expansion). Unit tests pass on CPU; no training run or matched ablation exists, so the MLP interpretation is proposed, not settled.

## Current manuscript: v2 revision references, September 23, 2026

The v2 revision, *Gauge-Covariant Gaussian Attention through Projected Matrix Links* (`manuscripts/Attention/GL(K)_attention_v2.tex`), positions the construction against newly cited sources, summarized in [[GL(K) gauge-equivariant attention]] and [[Attention mechanisms — theory and positional structure]]. The learned frames are a local dressing field, so the passive $\mathrm{GL}(K)$ covariance is artificial and constrains no learned map ([[Dressing field method]], [[francois-2019-artificial-gauge-symmetries]]). The row objective, the positional log-priors, and the isotropic L2 limit have precedents ([[movellan-2020-probabilistic-transformers]], [[kim-2021-lipschitz-self-attention]], [[litman-2026-attention-priors]], [[bianchessi-2026-bayesian-attention-mechanism]]). A binary compatibility record from control as inference ([[levine-2018-control-as-inference]]) makes Gibbs routing an exact posterior at every temperature. For the reported run, the revision attributes basis-dependent conditioning diagnostics to optimizer drift along a parameter symmetry ([[kunin-2021-neural-mechanics]]). It attributes the collapse of the stored variances from 15 to about 1.045 to AdamW's decoupled weight decay on the log-variances ([[loshchilov-hutter-2019-adamw]]).

## Current manuscript: matrix links, September 20, 2026

[[dennis-2026-glk-matrix-links-2026-09-20]] records the revised *Gauge-Covariant Gaussian Attention and Predictive Communication* manuscript. Full Gaussian states are the theoretical objects; projected comparisons determine routing, while independent sending/receiving maps define $L_{ij}^{(h)}=U_iO_hT_hU_j^{-1}$. The resulting matrix-link algebra, rank and composition statements, and loop scope are documented in [[GL(K) gauge-equivariant attention]] and [[Lattice gauge theory]]. The MLP interpretation remains open, and the revision adds no new training result or curvature measurement. The architecture and experiment descriptions below retain their historical configuration dates rather than defining the current predictive-content stack.


## Goal

The VFE Transformer Program studies a structural-EM sequence model whose forward pass refines per-token Gaussian model and belief states. In the mid-2026 configuration, one target-blind model-channel refinement is followed by one Fisher-preconditioned own-row belief refinement, after which the parameter M-step minimizes decode cross-entropy through both unrolled paths. These are not coordinate updates of one ELBO, so no global-descent or monotone-evidence guarantee follows.

Three ambitions distinguish the program: iterative belief filtering, transported Gaussian comparisons, and precision-weighted attention. Gaussian mean/covariance updates retain their Fisher/AIRM interpretation. Heavy-ball belongs only to the disabled custom outer frame optimizer, BCH/retraction only to disabled in-E-step frame revision, and the stored pullback preconditioner is inactive because both optional routes are off. None is a demonstrated full-$\mathrm{GL}(K)$ Fisher natural gradient.

## Architecture / approach

> [!warning] Superseded (2026-10-02). The Goal and Architecture text below describes the mid-2026 `V3_Transformer` configuration (transported comparisons, `mm_exact`, model channel, precision-weighted attention, Rényi orders, BCH positional composition, `regime_ii` transport). Those routes are retired in the VFE_3.0 working copy; see the October 2 section above and `VFE_3.0/docs/2026-10-02.md`. The text below is kept as the historical record of the evidence they produced.

The reference configuration is intentionally small enough for direct geometric diagnostics: a **1-layer** transformer whose per-token Gaussian belief has dimension **K = embed_dim**. This design choice does not establish that geometry, rather than scale or another coupled factor, causes the observed behavior. As of 2026-07-10, the live click-run config is **embed_dim = K = 20 with 2 heads**. The parameter count tracks K and the vocabulary, so it is config-dependent rather than a fixed figure. Each ingredient links out to its concept or method page.

**Variational inference core.** The retained diagonal-Gaussian route uses `prior_source=model_channel` and `s_e_step=true`: one target-blind $s$ refinement toward a learned global, token-uniform $r$ and gamma-weighted model consensus supplies $q^{(0)}=p=s^{(1)}$, followed by one target-blind $q$ refinement. The decode M-step differentiates cross-entropy through both paths. The hyper-prior and gamma terms remain inside the $s$ refinement and are not added again to the scored outer scalar. This finite same-scale route is neither CAVI nor the full multiscale PIFB hierarchy, and its configured rates do not establish a slower $s$ timescale.

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
there is no gamma counterpart. As of the 2026-07-12 remediation,
the frame-alignment subproblem carries the
term (detached hop weights on both factors, same score/value split as the scalar evaluator), and
the Metropolis reflection accept/reject scorer evaluates the exact active fixed-belief objective
including it; `lambda_twohop=0` remains a byte-identical no-op on both paths. The no-snapshot
E-step trace used by the end-of-run report was not re-audited in that remediation and may still
omit the coefficient. The selected ablation keeps
frame refinement and reflections off while sweeping `lambda_twohop` over `0.0`, `0.001`, `0.005`,
and `0.01`. The canonical pure route keeps `lambda_twohop=0.0`. The term may enter the higher-order
configuration Gibbs energy if its partition function is finite, but it does not evade the fixed
state-level mean-field obstruction.

**Gauge structure.** The real exponential chart reaches only $\operatorname{image}(\exp)\subsetneq\mathrm{GL}^+(K)$, and finite BCH composition is approximate. The optional Cartan/Killing object is a frame preconditioner, not a full-$\mathrm{GL}(K)$ natural metric. Regime-I transport $\Omega_{ij}=U_iU_j^{-1}$ telescopes, so loop holonomy is exactly identity; nontrivial holonomy belongs to an edge-relaxed path.

**Information geometry.** Gaussian belief mean/covariance updates use their closed-form Fisher geometry. No audited identification makes the frame conditioner a Fisher, Gauss-Newton, or K-FAC natural gradient.

**SPD covariance geometry.** Full-SPD covariances carry the affine-invariant metric, and the diagonal subset retains its belief-side Fisher geometry. A general $\mathrm{GL}(K)$ congruence does not preserve the live diagonal family except for monomial transports, so the implementation is projected or approximate outside that subgroup.

**Attention.** Attention is `precision_weighted`, so affinities are scaled by belief precision in the spirit of [[Precision weighting]] and the kernel-smoother view of attention ([[tsai-2019-kernel-attention]]), modifying the scaled dot-product baseline of [[vaswani-2017-attention]]. An **attention-entropy** term regularizes the attention distribution, and **causal beta / gamma priors** shape the temporal weighting (the live config uses a `causal_alibi` prior). Positional information is layered through registry-selected mechanisms: the live config injects gauge-structured position via a **learned phi composed by BCH (order 4)** (`pos_phi='learned'`). Two further channels exist but are OFF in the current run — **gauge-RoPE** (`pos_rotation='rope'`, base 100; the `rope_on_value` flag selects whether the rotation drives both the attention score and value aggregation, or only the Q/K score) and **T5 relative-position buckets** (a `t5_relative_bias` attention prior). The closest existing precedent for attention computed directly with SPD geometry is [[wang-2023-riemannian-self-attention-spd]]. See [[Attention mechanisms — theory and positional structure]] for the broader theme. The methodological scaffolding for this whole inference loop is collected under [[Inference machinery — variational EM and filtering]], and the wiki's own conventions follow [[karpathy-llm-wiki-pattern]].

## Experiments

Run artifacts persist under `VFE_3.0/vfe3_runs/` and are not catalogued here. On October 25, 2026 the author removed the earlier run notes and their results from the vault; the runs ingested since, each at the user's request, are [[vfe3-2026-10-25-local-learner-test]] and [[vfe3-2026-10-26-paper-arms]].

## Status & next steps

The architecture is configured and run artifacts persist under `V3_Transformer/vfe3_runs/`. The revision ledger now governs eleven claim families, so analytic completeness is not claimed. Historical development artifacts remain useful for designing reruns but do not override the current evidence scope.

Next steps, in rough priority order:

1. **(Done, 2026-06-18)** Artifact saving — training launches write checkpoints, a metrics log, `config.json`, and figures under `vfe3_runs/`; the free-energy / ELBO curve and validation perplexity are recorded.
2. Add belief-side SPD/Fisher diagnostics; reserve nontrivial holonomy diagnostics for edge-relaxed or otherwise nonflat transport because strict Regime I has $H=I$.
3. Rerun the distinctive ingredients against the [[vaswani-2017-attention]] baseline with frozen provenance and multiple seeds. The **gauge on/off / frozen-random** toggle exists. The divergence-order and positional comparisons likewise remain rerun targets rather than validated rankings.
4. Sweep the E-step depth to map the amortization-gap / compute trade-off identified by [[marino-2018-iterative-amortized-inference]].
5. **(Done, 2026-06-18)** Repaired the non-flat path. The bilinear `transport_mode='regime_ii'` edge factor $\delta_{ij}=\mu_i^\top W\mu_j$ is gauge-covariant only at $W=0$ (2026-06-18 audit finding), so the gauge-invariant "Route B" — `gauge_invariant_edge_features` (congruence-invariant Mahalanobis/trace/log-det of the belief KL) feeding a learned `connection_M` — was wired as a new registered builder `transport_mode='regime_ii_covariant'`: non-flat **and** gauge-covariant for any weight, default-off, threaded end-to-end and trainable (the config auto-enables `oracle_unroll_grad` for both non-flat regimes), pinned by `tests/test_regime_ii_covariant.py`. Still open: no Yang–Mills kinetic term, and `TODO(Route A)` (commutant-restricted connection on a compact subgroup for exact equivariance + a bounded Wilson action). See [[Non-flat connection and the photon analogy]].

> [!note] Design spec (2026-06-28) — active-inference EFE policy scorer (pre-registered, not implemented). A default-off, no-grad [[Expected Free Energy]] policy scorer over candidate token continuations is now specified and pre-registered for the vfe3 generation path — the first operationalization of EFE for the transformer, where it was previously native to the [[Gauge-Theoretic Multi-Agent VFE Model|multi-agent]] setting. It scores $G(\pi)=\mathrm{KL}[q(o\mid\pi)\,\|\,p(o\mid C)]+\mathbb{E}_{q(s\mid\pi)}H[p(o\mid s)]$ with an explicit peaked task preference and selects via $\mathrm{softmax}(-\gamma G)$, adding no learned parameters ($\texttt{policy\_mode='none'}$ is byte-identical to HEAD). Honest scope: at the v1 one-step sigma-free point belief the information-gain term is identically zero, so v1 is a *pragmatic preference-matching reranker*; information-seeking active inference, the agent-set/community case, and any train-time EFE are deferred, and no efficacy is claimed. *(Superseded in part 2026-07-12: `efe_one_step` and the H-step `efe_rollout` are now implemented and reachable through generation.)*

> [!note] Buildout (2026-07-08) — omega_direct element-store gauge + a learnable det-sign. A second [[GL(K) gauge group|GL(K)]] frame parameterization, `gauge_parameterization="omega_direct"`, stores each token's frame as a group element $U_i$ and transports by the stored cocycle $\Omega_{ij}=U_iU_j^{-1}$ instead of $\exp(\phi_i)\exp(-\phi_j)$. It was threaded through the gamma / model-coupling (s) channel with frame-fidelity (so the s-channel transports by $U$, not the $\exp(\phi)$ cocycle) and given a **learnable discrete orientation** via `omega_reflection="metropolis"`: a $\Delta F$-gated Metropolis flip over the $\det$ sign — the program's first mechanism for *learning* the discrete $\pi_0(\mathrm{GL}(K))=\mathbb{Z}/2$ gauge component, which the $\exp(\phi)$ parameterization (confined to $\mathrm{GL}^+(K)$) cannot reach. Two findings: (i) a **gauge-invariance** test certifies covariance but *cannot* certify which covariant transport is used ($U$ vs $\exp\phi$, both gauge-covariant) — frame *use* needs direct frame-perturbation tests; (ii) under the live `gaussian_diagonal` family the reflection is **near-inert** (it leaves the squared diagonal congruence invariant, so $\Delta F\approx 0$ and the det-sign thrashes at $\approx100\%$ acceptance) — it does useful sheet selection only with a full / off-diagonal covariance family or a low temperature. Default-off, opt-in; the pure $\exp(\phi)$ path stays byte-identical. `origin/main` @ `24500e9`.

> [!note] Buildout (2026-07-08) — the cheaper $R\exp(\phi)$ route on the phi path. The same learnable det-sign, but for the DEFAULT `phi` parameterization: prepend a per-token reflection to $\exp(\phi)$, $g_i=R_i\exp(\phi_i)$ (so $\det g_i=-e^{\operatorname{tr}\phi_i}<0$; $\det\exp(\phi)$ is *always* $>0$, which is why $\exp(\phi)$ alone is stuck in $\mathrm{GL}^+(K)$). This reaches the $\det<0$ sheet with a single sign **bit** per token instead of a stored $K\times K$ element; `phi_reflection="metropolis"` learns it via the *same* $\Delta F$-gated Metropolis flip, threaded through every channel. Reach is $R\cdot\mathrm{image}(\exp)$ (misses the non-exp interior `omega_direct` reaches) in exchange for reusing the full $\exp(\phi)$ / BCH / Killing machinery — realizing $\mathrm{GL}(K)=\{I,R\}\cdot\mathrm{GL}^+(K)$. The two findings above carry over (the discrete $\pm1$ sign has no continuous $g$-action, so a gauge-invariance test over it is empirically inert; near-inert under `gaussian_diagonal`, so a meaningful run needs `gaussian_full`; the `s_e_step=False` half of that restriction was lifted 2026-07-12 when the model channel gained full-SPD support). The build also fixed a **latent `omega_direct` bug**: `block.py`'s post-E-step transforms dropped the stored frame for layers past the first under `head_mixer` / `cg_coupling` / `block_norm` at `n_layers>1` (now `_replace`-preserved). Default-off. `origin/main` @ `7ffb68e`.

> [!note] Buildout (2026-07-12) — partial-buildout audit remediated; EFE rollout live, sigma_mc gate-closed, model channel completed. A deep audit of `origin/main` @ `4265358` inventoried fifteen partial buildouts (PB-01..PB-15); seven completion plans were executed and merged the same day (PRs #168–#175; suite 2363 → 2741 tests, 0 failures). Program-relevant deltas: (i) the [[Expected Free Energy]] scorer's `efe_rollout` mode is now **reachable through generation** via a bounded H-step beam menu (the 2026-06-28 spec is no longer "not implemented"), and `sigma_mc` has an executable antithetic MC estimator behind a **four-identity fail-closed gate** that no shipped config can enable; (ii) the phi frame-alignment subproblem and the Metropolis reflection scorer now evaluate the **exact active objective** (two-hop, folded priors, adaptive tau), closing the objective-parity omissions previously noted here; (iii) the s/r model channel gained full-SPD packed covariance storage, family dispatch, and shared nonflat transport — `gaussian_full + s_e_step=True` now constructs, superseding the 2026-07-08 usability restriction; (iv) CG coupling gained a first-order covariance pushforward and an opt-in moment-divergence energy; decode can follow the configured family/divergence; the q/p/s/h hierarchy has one typed evaluator with the legacy scalar reduction order pinned byte-for-byte. Guarded CUDA smokes await an RTX 5090 run.

> [!note] Plan (2026-07-11) — backprop-free learning track pre-registered ([[Nudged two-phase EM]]). A 14-agent adversarial investigation (recon / design / challenge / synthesis, file:line spot-verified) produced `V3_Transformer/docs/plans/2026-07-11-backprop-free-vfe-lm-plan.md`. Two banked results: (i) a target-blind E-step fixed point drops the through-$q^*$ credit term $(\partial\mathrm{CE}/\partial q^*)(\partial q^*/\partial\theta)$, leaving everything but the readout as reservoir computing; (ii) a temperature degeneracy: $\partial F_{red}/\partial\tau=\mathrm{KL}(\beta\|\pi)\ge 0$ (sympy-verified), so softmax temperatures cannot be learned by descending $F$ — they need contrastive or held-out estimation. The prescription is a nudged two-phase EM (free phase = deployed inference; symmetric $\pm\lambda$ target-nudged continuations; EqProp contrasts carry all non-decode credit; analytic per-row Gauss-Newton decode; quarantine rule for sign-monotone knobs), realizing the [[participatory-it-from-bit|PIFB]]-canonical observation placement. Design only — no training results; milestone gates run measured BPE unigram → KenLM 5-gram → the DFA band ([[launay-2020-dfa-transformers]], the only published backprop-free transformer LM PPLs) → 2x matched-K backprop vfe3.

> [!note] Buildout (2026-07-25) — the mechanism diagnostics are now end-of-run artifacts. Every measurement in this investigation came from a throwaway script, which is exactly how the depth probe stayed misattributed for weeks. Three probes were promoted into `finalize_run`, each persisting JSON, rendering a registered figure, and printing its headline to the run log: `collect_estep_character` (belief displacement across depth, trajectory straightness, and the pair/prior split of the fused `mm_exact` precision), `collect_beta_channel_decomposition` (the M6 arms — positional prior against content energy), and `collect_context_sensitivity` (prefix randomization staged `raw_prior → model_channel → belief_estep`). Only the last is expensive and it is the only one behind `emit_expensive_diagnostics` (default False); gating the cheap tier would recreate the condition being fixed. The character probe carries a falsification hook — it reproduces the kernel's own `mu_star` from the decomposition it reports and warns if that residual leaves zero — so a probe that stops matching the kernel is visible in the artifact rather than in a later investigation. Two defects of the original diagnostic's family were caught by its tests before merge: `inference/e_step.py` binds the update kernel at import, so patching only the definition module left the live call site untouched while the probe reported success, and the β decomposition is route-agnostic rather than `mm_exact`-only. `origin/main` @ `7b27217`; CPU lane `tests=4269 failures=4` (the 4 pre-existing rope failures stale on main), CUDA lane 24 passed.

> [!note] Refutation (2026-07-25) — the cross-scale shadow prior does not transfer from the multi-agent model. A six-expert panel (gauge theory, variational inference, transformer architecture, implementation scoping, literature, falsification) rejected porting PIFB's $p_i^{(s)}=\Omega_{i,I}[q_I^{(s+1)}]$ to V3 as an observation channel, on four independent grounds. (i) **No gauge degeneracy exists for a likelihood to break.** V3's two flat directions — the rigid right action $U_i\mapsto U_ig$ and global conjugation of all tables — are parameterization redundancies invisible to every observable, and both are already lifted by `phi_weight_decay`; a bank-referenced likelihood has both arguments co-transforming and is frame-blind. The multi-agent mechanism needs a source in a declared *non*-co-transforming frame, and V3's only such object is $p_i$ (plus the target token, already booked as cross-entropy). (ii) **The token cannot be both prior and observation** — putting the likelihood on $o_t$ is not the LM objective, putting it on $o_{t+1}$ requires the current token to re-enter through the prior, and doing both is a Gibbs posterior at inverse temperature 2 ([[bissiri-2016-general-bayesian-updating]]). (iii) The shadow term is the Gaussian **belief-propagation message**, so the object is a Bethe-family free energy — stationary-point-only once attention adds within-scale loops ([[yedidia-freeman-weiss-2005-region-free-energy]]) — not the mean-field ELBO term the manuscript's exactness result covers. (iv) Stripped of gauge apparatus the construction is [[sonderby-2016-ladder-vae|Ladder VAE]] applied to text, whose record is density estimation on binarized MNIST/OMNIGLOT/NORB with **no language benchmark at all**; there is no widely adopted hierarchical latent LM, and top-down structure does not cure posterior collapse. The panel also recorded the mechanism it originally proposed — consensus collapse from $\alpha^*=c_0/(b_0+D)$ anchor decay — and then had it refuted by its own Stage A measurements. Not recommended for construction.

## Cross-links

**Reference curriculum:** [[Gauge VFE ELBO curriculum]]

**Related project:** [[Gauge-Theoretic Multi-Agent VFE Model]] — the multi-agent, continuous-time instantiation of the same GL(K)-gauge VFE theory (this transformer is the language-model instantiation).

**Manuscripts:** [[gl-k-attention]] · [[dennis-2026-glk-lie-algebra-links-v2]] · [[participatory-it-from-bit]] · [[dennis-2026-projected-predictive]] · [[dennis-2026-projected-gradient]] · [[dennis-2026-phi-natgrad]] · [[dennis-2026-template-routing]] · [[dennis-2026-neuron-free-agent-theory]] · [[dennis-2026-link-origin]] · [[dennis-2026-link-curvature]] · [[dennis-2026-dynamic-links]]

**Methods (attention routes):** [[Projected predictive attention]] · [[Projected gradient attention]] · [[Template routing]]

**Themes:** [[Variational free energy and predictive coding]] · [[Gauge equivariance and geometric deep learning]] · [[Information geometry and natural gradient]] · [[SPD-manifold geometry and Riemannian optimization]] · [[Attention mechanisms — theory and positional structure]] · [[Inference machinery — variational EM and filtering]]

**Methods:** [[Nudged two-phase EM]] — the pre-registered backprop-free learning prescription ·
[[Rigorous theory search]] — the truth-preserving proof and effective-theory search protocol used
for research-level derivations

**Key concepts:** [[Variational free energy]] · [[Evidence lower bound (ELBO)]] · [[Prediction error]] · [[Precision weighting]] · [[Gauge transformation]] · [[GL(K) gauge group]] · [[Holonomy]] · [[Non-flat connection and the photon analogy]] · [[Natural gradient]] · [[Fisher information metric]] · [[Renyi divergence]] · [[Irreducible representation]] · [[Clebsch-Gordan coefficients]] · [[Expected Free Energy]] · [[Active Inference]]

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
