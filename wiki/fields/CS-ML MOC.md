---
type: moc
title: CS-ML MOC
aliases: [field/cs-ml, CS-ML sources, Machine learning MOC, CS/ML MOC]
tags: [moc]
status: stable
created: 2026-06-19
updated: 2026-08-03
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
