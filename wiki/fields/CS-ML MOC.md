---
type: moc
title: CS-ML MOC
aliases: [field/cs-ml, CS-ML sources, Machine learning MOC, CS/ML MOC]
tags: [moc]
status: stable
created: 2026-06-19
updated: 2026-09-11
---

# CS-ML MOC

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
- [[multiagentelbo-2026-09-11-critical-comparisons]]
- [[multiagentelbo-2026-09-11-extension-studies]]
- [[multiagentelbo-2026-09-11-finite-program]]
- [[multiagentelbo-2026-09-11-implementation]]
