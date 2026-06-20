---
type: moc
title: Biology MOC
aliases: [field/biology, Biology sources]
tags: [moc]
status: stable
created: 2026-06-19
updated: 2026-06-19
---

# Biology MOC

> Map of Content for the **`field/biology`** discipline facet. Auto-populated by the **Bases**
> core plugin from the `field/*` tags.

Biology (**41** sources) covers evolutionary dynamics and evolutionary game theory (replicator
dynamics, cooperation on graphs), cultural evolution and social learning, and collective animal
behaviour / flocking. These supply the selection-and-transmission and self-organization mechanisms
behind the [[Statistical physics of social systems and collective behavior|social-physics]] program.

```base
filters:
  and:
    - 'file.hasTag("field/biology")'
views:
  - type: table
    name: "Biology sources"
    order:
      - title
    properties:
      - file.name
      - title
      - year
```

## Cross-facet pivots
Compose with the topic facet via tag search — e.g.
`tag:#field/biology tag:#cluster/social-physics/evolutionary-and-cultural`. See the [[Disciplines MOC]] hub.
