---
type: moc
title: Statistics MOC
aliases: [field/statistics, Statistics sources, Information theory MOC]
tags: [moc]
status: stable
created: 2026-06-19
updated: 2026-06-19
---

# Statistics MOC

> Map of Content for the **`field/statistics`** discipline facet (statistics & information theory).
> Auto-populated by the **Bases** core plugin from the `field/*` tags.

Statistics & information theory (**60** sources) underpins the variational-inference and
information-geometry layers of the program: Bayesian inference, divergences, model selection
(MDL / BIC), forecasting, and the information bottleneck. Note the gap between primary (14) and
"touches" (60) — statistics is rarely a source's headline field but pervades the corpus.

```base
filters:
  and:
    - 'file.hasTag("field/statistics")'
views:
  - type: table
    name: "Statistics sources"
    order:
      - title
    properties:
      - file.name
      - title
      - year
```

## Cross-facet pivots
Compose with the topic facet via tag search — e.g. `tag:#field/statistics tag:#cluster/info-geometry`
or `tag:#field/statistics tag:#cluster/vfe`. See the [[Disciplines MOC]] hub for all fields.
