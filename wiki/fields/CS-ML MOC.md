---
type: moc
title: CS-ML MOC
aliases: [field/cs-ml, CS-ML sources, Machine learning MOC, CS/ML MOC]
tags: [moc]
status: stable
created: 2026-06-19
updated: 2026-06-19
---

# CS-ML MOC

> Map of Content for the **`field/cs-ml`** discipline facet (computer science & machine learning).
> Auto-populated by the **Bases** core plugin from the `field/*` tags.

Computer science & machine learning (**80** sources) covers the transformer / attention literature
(in [[Attention mechanisms — theory and positional structure|attention]] and
[[Transformer interpretability and scaling]]), neural-network optimization and information-bottleneck
theory, and computational network science.

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
