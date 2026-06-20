---
type: moc
title: Physics MOC
aliases: [field/physics, Physics sources]
tags: [moc]
status: stable
created: 2026-06-19
updated: 2026-06-19
---

# Physics MOC

> Map of Content for the **`field/physics`** discipline facet. The table is auto-populated by the
> **Bases** core plugin from the `field/*` tags and updates itself as sources are added.

Physics is the largest discipline in the corpus (**149** sources). Its notes occupy three regions of
the program: the statistical-physics / sociophysics of collective behaviour (in [[Statistical physics of social systems and collective behavior|social-physics]]), the quantum-foundations and emergent-gravity wing of the
[[Participatory realism and quantum foundations|participatory]] program, and the gauge-theory /
[[Information geometry and natural gradient|information-geometry]] core shared with the transformer.

```base
filters:
  and:
    - 'file.hasTag("field/physics")'
views:
  - type: table
    name: "Physics sources"
    order:
      - title
    properties:
      - file.name
      - title
      - year
```

## Cross-facet pivots
Compose with the topic facet via tag search — e.g. `tag:#field/physics tag:#cluster/gauge-theory`
(gauge theory of physics origin) or `tag:#field/physics tag:#cluster/participatory/quantum-foundations`.
See the [[Disciplines MOC]] hub for all fields.
