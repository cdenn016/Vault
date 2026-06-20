---
type: moc
title: Economics MOC
aliases: [field/economics, Economics sources]
tags: [moc]
status: stable
created: 2026-06-19
updated: 2026-06-19
---

# Economics MOC

> Map of Content for the **`field/economics`** discipline facet. Auto-populated by the **Bases**
> core plugin from the `field/*` tags.

Economics (**22** sources, the smallest field) contributes game theory, information cascades and herd
behaviour, increasing-returns lock-in, Bayesian social learning, and the economic side of mean-field
games — the rational-choice counterpart to the physics-flavoured
[[Statistical physics of social systems and collective behavior|social-physics]] models.

```base
filters:
  and:
    - 'file.hasTag("field/economics")'
views:
  - type: table
    name: "Economics sources"
    order:
      - title
    properties:
      - file.name
      - title
      - year
```

## Cross-facet pivots
Compose with the topic facet via tag search — e.g.
`tag:#field/economics tag:#cluster/social-physics/networks-and-contagion`. See the [[Disciplines MOC]] hub.
