---
type: moc
title: CS-ML MOC
aliases: [field/cs-ml, CS-ML sources, Machine learning MOC, CS/ML MOC]
tags: [moc]
status: stable
created: 2026-06-19
updated: 2026-10-20
---

# CS-ML MOC

## Transformer layers derived from an objective, October 6, 2026

[[yang-2022-transformers-optimization-perspective]] (NeurIPS 2022) gives an energy whose majorization-minimization and alternating gradient steps reproduce softmax self-attention, a symmetric feed-forward map and ReLU, with descent theorems and energy-descent curves as evidence. [[hoover-2023-energy-transformer]] (NeurIPS 2023) builds a recurrent block as gradient descent of an engineered attention-plus-Hopfield energy and reports masked-image completion and graph benchmarks. [[yu-2023-white-box-transformers-sparse-rate-reduction]] (NeurIPS 2023) derives attention and a sparse-coding MLP from sparse rate reduction and comes within 1.6 top-1 points of ViT-S on ImageNet-1K at about 22M parameters. All three train by backpropagation. Synthesis: [[Attention mechanisms — theory and positional structure]], [[GL(K) gauge-equivariant attention]].

## Group-valued link origin, October 2, 2026

[[dennis-2026-link-origin]] shows the multi-head operator $U_iOB_{ij}TU_j^{-1}$ is the standard multi-head value path with frames and is generically group-valued, derives that an exponential-link construction yields a residual only on unwritten directions (none when heads tile the fiber, as the code requires), and rewrites SiLU and GELU as exponential self-links with generators $\log\sigma$ and $\log\Phi$, which the note labels a rewriting and not a derivation. Small-dimension numerical checks only; no model trained. Synthesis: [[Projected predictive attention]], [[Projected gradient attention]], [[Activation Functions]].

[[dennis-2026-link-curvature]] (2026-10-02) asks what edge-dependent links add to the attention link field: flat links are recurrent (state-space transition products), the head-sum routing has multiplicative cocycle defect and is flat only for $\beta_{ij}=c_i/c_j$, regression links give the low-rank channel a reduced-rank-regression reading, and additive affine updates can cross the singular boundary that multiplicative updates cannot. Agent-drafted, float64 checks at $K=4$, no training, no performance claim.

[[dennis-2026-dynamic-links]] (2026-10-03) works out per-context, inferred attention links. Its link field equation is driven by a delta-rule current, prediction error times source state, as in fast-weight memories. Without a prior the per-context optimum is a rank-one transport outside the exponential chart, so the anchor is necessary. The implemented `content_link_chart="exponential"` is the static limit, and amortized link inference would be a fast-weight program. Agent-drafted, float64 checks at small size, no training, no performance claim.

[[multiagentelbo-2026-10-04-lie-algebra-links]] (2026-10-04) brings latent Lie-algebra links into the multi-agent theory. Their natural-gradient recognition flow has the Bayesian learning rule as its Euler step, and their field equation has the delta-rule current. It does not claim an identification with a trained fast-weight architecture. Drafted by Claude Opus 5.5 and cross-checked by Claude Fable 5.1; nothing trained.

[[dennis-2026-glk-lie-algebra-links-v2]] (2026-10-04) derives the standard multi-head value path as the first-order channel of a group-valued exponential link, with order zero a head-routed flat transport and order two cross-head mixing, and states the implemented `content_link_chart` options as three charts of the same tiled mean maps. In the matched single-seed $K=20$ runs of [[vfe3-2026-10-03-link-charts-and-channel-receiver]] the charts reached test cross-entropies within 0.0037 nats, while the trained links differed in singular-set crossing and conditioning; the closed-form channel receiver was 0.0276 nats worse in a configuration that does not isolate it.

[[vfe3-2026-10-05-k30-multiseed]] (2026-10-05) measures the seed noise floor of one VFE_3.0 configuration ($K=30$, four layers, one epoch) over three seeds: test PPL 87.19 with SD 0.33 and test CE SD 0.0037 nats, so single-seed differences under about 0.9 PPL are not established there.

[[dennis-2026-glk-attention-v2-rework-2026-10-05]] (2026-10-05) presents attention as communication among statistical agents, with a standard transformer layer as the affine chart of a routed group-link transport, and anchors its language model on [[vfe3-2026-10-05-k128-exponential-and-parameter-accounting]] (2026-10-05): a $K=128$ exponential-chart model at test perplexity 34.48 (one seed). The October 7 revision ([[dennis-2026-glk-attention-v2-review-2026-10-07]]) compares it with a per-type read-table transformer of nearly equal size trained under the same protocol ([[vfe3-2026-10-06-block-read-baseline]], 55.10, one seed); the earlier pairs against plain transformers (39.77 against 90.15, 52.91 against 117.63) were an earlier study and are not paper results.

[[barbero-2022-sheaf-attention-networks]] (2022; abstract only) extends graph attention networks to cellular sheaves and reports gains over GAT on oversmoothing and heterophily benchmarks. [[barbero-2022-sheaf-neural-networks-connection-laplacians]] (2022) precomputes orthogonal sheaf restriction maps by local PCA and SVD alignment, giving a discrete $O(d)$-bundle with a connection Laplacian, and nears learned-sheaf diffusion at lower cost on nine node-classification sets. [[disipio-2025-curved-spacetime-transformers]] (2025) reads attention as a discrete connection by analogy with general relativity and measures layerwise turning angles of token trajectories against a random-direction null. [[favoni-2022-lattice-gauge-equivariant-cnns]] (2022) builds gauge-equivariant convolution and bilinear layers on $\mathrm{SU}(N_c)$ lattice links that generate Wilson loops.

## vfe3 projected attention routes, October 2, 2026

[[dennis-2026-projected-gradient]] derives the receiver energies, cut-model routing, closed-form natural-parameter updates and profiled self-coupling of the gradient attention route; [[vfe3-2026-10-02-projected-route-consolidation]] records their implementation and the retirement of transported attention (CPU tests only, no training). [[dennis-2026-phi-natgrad]] gives the frame-table optimizers, and [[dennis-2026-neuron-free-agent-theory]] a conditional neuron-free construction (inconclusive for the full target). Synthesis: [[Projected gradient attention]].

## Feed-forward memory and mixture-of-experts references, September 27, 2026

[[sukhbaatar-2019-persistent-memory]], [[geva-2021-ffn-key-value-memories]], [[jacobs-1991-mixtures-of-local-experts]], [[ghahramani-1994-incomplete-data-em]], [[hershey-2007-kl-gmm]] and [[elfwing-2018-silu]] support [[Template routing]].

## Research tooling reference, September 26, 2026

[[exa-2026-agent-create-run]] archives the official Agent API effort and budget fields. Its role is methodological under [[Rigorous theory search]], not evidence for mathematical results.

> Map of Content for the **`field/cs-ml`** discipline facet (computer science & machine learning).
> Auto-populated by the **Bases** core plugin from the `field/*` tags.

Computer science & machine learning (**263** sources) covers the transformer / attention literature
(in [[Attention mechanisms — theory and positional structure|attention]] and
[[Transformer interpretability and scaling]]), neural-network optimization and information-bottleneck
theory, and computational network science.

It also carries the **Heidelberg geometric-imaging line** (Schnörr's group, DFG SPP 2298 / STRUCTURES
EXC 2181/1), the closest external programme to this vault's own bundle construction: assignment and
sigma flows on statistical manifolds — [[cassel-2024-sigma-flows]],
[[gonzalez-alvarado-2025-patch-assignment]] — and associated-bundle gauge structure for graph
networks — [[cassel-2025-bundle-scale-spaces]], [[cassel-2025-yang-mills-data]]. All four are dual
`field/cs-ml` + `field/mathematics`; see the [[Mathematics MOC]] for the geometric side.

```base
filters:
  and:
    - 'file.hasTag("field/cs-ml")'
views:
  - type: table
    name: "CS / ML sources"
    order:
      - title
    properties:
      - file.name
      - title
      - year
```

## Backpropagation-free gauge-VFE language construction, October 4, 2026

[[dennis-2026-backprop-free-vfe-language-architecture]] records an exploratory non-neural causal model with analytic local learning, link-bearing categorical observations, and explicit boundaries between ELBO/model evidence and finite-predictor perplexity. Its small CPU checks are formula grounding only; scalable inference and language performance remain open.

## Cross-facet pivots
Compose with the topic facet via tag search — e.g. `tag:#field/cs-ml tag:#cluster/attention`
or `tag:#field/cs-ml tag:#cluster/info-geometry`. See the [[Disciplines MOC]] hub for all fields.

## MultiAgentELBO research ingestion, September 11, 2026

- [[bertsekas-1983-distributed-asynchronous-computation-of-fixed-points]]
- [[bertsekas-1991-some-aspects-of-parallel-and-distributed-iterative-algorithms-a-s]]
- [[cohen-2012-formal-proofs-in-real-algebraic-geometry-from-ordered-fields-to-quanti]]
- [[dahlqvist-2018-borel-kernels-and-their-approximation-categorically]]
- [[fritz-2019-a-synthetic-approach-to-markov-kernels-conditional-independence-and-th]]
- [[hansen-2018-toward-a-spectral-theory-of-cellular-sheaves]]
- [[joly-2024-graph-coarsening-with-message-passing-guarantees]]
- [[loukas-2018-graph-reduction-with-spectral-and-cut-guarantees]]
- [[oono-2019-graph-neural-networks-exponentially-lose-expressive-power-for-node-cla]]
- [[shalizi-1999-computational-mechanics-pattern-and-prediction-structure-and-simplicit]]
- [[singh-2023-attention-marginal-probability-is-all-you-need]]
- [[tsitsiklis-1986-distributed-asynchronous-deterministic-and-stochastic-gradient-op]]
- [[turner-2011-two-problems-with-variational-expectation-maximisation-for-time-s]]
- [[ying-2018-hierarchical-graph-representation-learning-with-differentiable-pooling]]

## Matrix-link ingestion, September 20, 2026

[[dennis-2026-glk-matrix-links-2026-09-20]] records the matrix-link source and its stated scope; [[Lattice gauge theory]] and [[GL(K) gauge-equivariant attention]] provide the synthesis. The source is included in the tagged Bases view.

## Selective-communication formation assessment, September 20, 2026

[[multiagentelbo-2026-selective-communication-formation]] records communicated/private-law separation, quotient compatibility and the proposed normalized cycle extension. Its formation and blanket claims remain explicitly conditional; the source is included in this discipline's tagged Bases view.

## Unified attention companion, October 3, 2026

[[dennis-2026-attention-unified]] consolidates exponential-link geometry, Gaussian inference, templates, and frame optimization with a dated implementation crosswalk. Option A is the author-selected primary construction; the file remains separate from the GL(K) manuscripts. No new training or large-network result is claimed.
