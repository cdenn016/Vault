---
type: moc
title: Philosophy MOC
aliases: [field/philosophy, Philosophy sources]
tags: [moc]
status: stable
created: 2026-06-19
updated: 2026-06-19
---

# Philosophy MOC

> Map of Content for the **`field/philosophy`** discipline facet. Auto-populated by the **Bases**
> core plugin from the `field/*` tags.

Philosophy (**62** sources) is the conceptual spine of the [[Participatory realism and quantum foundations|participatory]]
program and the [[Structural realism and philosophy of science]] theme: philosophy of mind (the hard
problem, panpsychism), philosophy of science and structural realism, epistemology, and the it-from-bit
metaphysics that motivates the participatory reading of the gauge-theoretic framework.

```base
filters:
  and:
    - 'file.hasTag("field/philosophy")'
views:
  - type: table
    name: "Philosophy sources"
    order:
      - title
    properties:
      - file.name
      - title
      - year
```

## Cross-facet pivots
Compose with the topic facet via tag search — e.g.
`tag:#field/philosophy tag:#cluster/participatory/philosophy-of-mind`. See the [[Disciplines MOC]] hub.
