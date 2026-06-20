---
type: moc
title: Psychology MOC
aliases: [field/psychology, Psychology sources]
tags: [moc]
status: stable
created: 2026-06-19
updated: 2026-06-19
---

# Psychology MOC

> Map of Content for the **`field/psychology`** discipline facet. Auto-populated by the **Bases**
> core plugin from the `field/*` tags.

Psychology (**39** sources) is almost entirely the social- and cognitive-psychology foundation of the
[[Statistical physics of social systems and collective behavior|social-physics]] program — conformity
and social influence (Asch, Festinger, Sherif, Cialdini), social power, attitude change, and cognitive
bias — the empirical micro-behaviour the formal opinion-dynamics models abstract.

```base
filters:
  and:
    - 'file.hasTag("field/psychology")'
views:
  - type: table
    name: "Psychology sources"
    order:
      - title
    properties:
      - file.name
      - title
      - year
```

## Cross-facet pivots
Compose with the topic facet via tag search — e.g.
`tag:#field/psychology tag:#cluster/social-physics/social-influence`. See the [[Disciplines MOC]] hub.
