---
type: moc
title: CS-ML MOC
aliases: [field/cs-ml, CS-ML sources, Machine learning MOC, CS/ML MOC]
tags: [moc]
status: stable
created: 2026-06-19
updated: 2026-10-03
---

# CS-ML MOC

## October 3 source-informed compression comparison

[[multiagentelbo-2026-10-03-source-informed-compression]] compares an activation-only frozen-weight source-sensitivity basis with half-block compression at matched ranks 64/128 on two saved paths per N512/N1024. Mean total loss relative to half-block changes by -1.295775/+0.085335 nats, with opposite source/configuration tradeoffs. Dense remains better. Fifteen tiny tests, four numerical path checks and 40 scalar reconstructions passed. No GPU ran. The underpowered sample supports no general superiority claim; both record channels are the next proposed design target. Dense workspaces and O1/O4 remain open, as do the historical parity failure and pending formal verification.

## October 3 compressed-message pilot

[[multiagentelbo-2026-10-03-compressed-message]] implements an optional reference-conditioned compressed Gaussian message and tests two unchanged switching paths per size at N512/N1024. Mean/covariance history entries fall by factors of 252-254, while dense constants and temporary computation remain. Mean compressed-minus-dense losses are 9.35635/8.06562 nats; compressed-minus-reset losses are -0.85301/-0.14410. The sample is underpowered. Ten tiny tests and 28 scalar checks passed; no GPU ran. A matched-rank source-informed basis comparison is next; O1/O4, the prior parity failure and pending formal verification remain open.

## October 3 reverse-budget large-network validation

[[multiagentelbo-2026-10-03-reverse-budget-validation]] records one fresh reverse-budget path each at N512/N1024 and four passing independent grid reconstructions in 119.086 CPU seconds. Fine sampled totals are 78.13565 and 151.90999 nats, about 92% source cost. N512 had three visible changes; N1024 had no proposals. These descriptive conservative functionals do not certify retained accuracy or measure retained KL. Quantitative O1/O4 and the prior parity failure remain open; sharper reverse-weighted retained-prediction accounting precedes a full replicated measurement.

## October 3 reverse-budget implementation checkpoint

[[multiagentelbo-2026-10-03-reverse-budget-implementation]] records the candidate-driven fine comparison and supplied-uniform candidate-prefix sampler. Thirty-three distinct focused tests and both grids of an independent N4 archive reconstruction passed. The N512/N1024 launcher, pre-run contract and large-network calculation remain pending. Finite-step validation does not establish continuous path accuracy or a small reverse budget; quantitative O1, native-driven integrability, the preceding parity failure and O4 remain open. No GPU calculation ran.

## October 3 projection parity diagnosis

[[multiagentelbo-2026-10-03-projection-parity-diagnosis]] records three bounded non-reproductions of the preceding projection parity failure: the first event with archived/off/on implementations, complete path000 on/off traces, and four separate spawned N512 cases. All 180 archived candidate-field comparisons were exact. The original failure remains unresolved and the 32-path study remains incomplete. Future failures now retain actual arrays, the reference field and mismatch location/magnitude; two tiny capture tests pass. No full-study retry, GPU or O1/O4 closure is claimed.

## Group-valued link origin, October 2, 2026

[[dennis-2026-link-origin]] shows the multi-head operator $U_iOB_{ij}TU_j^{-1}$ is the standard multi-head value path with frames and is generically group-valued, derives that an exponential-link construction yields a residual only on unwritten directions (none when heads tile the fiber, as the code requires), and rewrites SiLU and GELU as exponential self-links with generators $\log\sigma$ and $\log\Phi$, which the note labels a rewriting and not a derivation. Small-dimension numerical checks only; no model trained. Synthesis: [[Projected predictive attention]], [[Projected gradient attention]], [[Activation Functions]].

[[dennis-2026-link-curvature]] (2026-10-02) asks what edge-dependent links add to the attention link field: flat links are recurrent (state-space transition products), the head-sum routing has multiplicative cocycle defect and is flat only for $\beta_{ij}=c_i/c_j$, regression links give the low-rank channel a reduced-rank-regression reading, and additive affine updates can cross the singular boundary that multiplicative updates cannot. Agent-drafted, float64 checks at $K=4$, no training, no performance claim.

## vfe3 projected attention routes, October 2, 2026

[[dennis-2026-projected-gradient]] derives the receiver energies, cut-model routing, closed-form natural-parameter updates and profiled self-coupling of the gradient attention route; [[vfe3-2026-10-02-projected-route-consolidation]] records their implementation and the retirement of transported attention (CPU tests only, no training). [[dennis-2026-phi-natgrad]] gives the frame-table optimizers, and [[dennis-2026-neuron-free-agent-theory]] a conditional neuron-free construction (inconclusive for the full target). Synthesis: [[Projected gradient attention]].

## Gaussian network runtime baseline, September 30, 2026

[[multiagentelbo-2026-09-30-pointwise-gaussian-network]] records the tensor implementation and one CPU study of five 512-agent held-map cases. All 45 numerical comparisons passed; the dense representation and single execution delimit the performance result. No GPU or evolving-link experiment ran.

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

## Cross-facet pivots
Compose with the topic facet via tag search — e.g. `tag:#field/cs-ml tag:#cluster/attention`
or `tag:#field/cs-ml tag:#cluster/info-geometry`. See the [[Disciplines MOC]] hub for all fields.

## MultiAgentELBO research ingestion, September 11, 2026

[[Gauge-VFE RG research synthesis September 2026]] connects the following new source records to the current theory. Existing sources are reused through [[multiagentelbo-2026-09-11-reference-register]].

- [[multiagentelbo-2026-09-11-conditional-geometry]]
- [[multiagentelbo-2026-09-11-continuum]]
- [[multiagentelbo-2026-09-11-formation]]
- [[multiagentelbo-2026-09-11-gaussian-closure]]
- [[multiagentelbo-2026-09-11-geometry-feedback]]
- [[multiagentelbo-2026-09-11-memory]]
- [[multiagentelbo-2026-09-11-neighborhoods]]
- [[multiagentelbo-2026-09-11-normalized-core]]
- [[multiagentelbo-2026-09-11-reference-register]]
- [[multiagentelbo-2026-09-11-research-snapshot]]
- [[multiagentelbo-2026-09-11-scale-and-inference]]
- [[multiagentelbo-2026-09-11-spatial]]
- [[multiagentelbo-2026-09-11-thermodynamic-fisher]]
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

## Observed-link Gaussian parent reference, September 30, 2026

[[multiagentelbo-2026-09-30-gaussian-parent-dynamics]] records seven tiny CPU tests and 95 passing comparisons across five 512-agent cases, actual-history filtering and finite-path Markov information loss. External controls and network-sized conditionals do not establish endogenous learning or autonomous parent closure.

## Unified attention companion, October 3, 2026

[[dennis-2026-attention-unified]] consolidates exponential-link geometry, Gaussian inference, templates, and frame optimization with a dated implementation crosswalk. Option A is the author-selected primary construction; the file remains separate from the GL(K) manuscripts. No new training or large-network result is claimed.
