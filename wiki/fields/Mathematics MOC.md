---
type: moc
title: Mathematics MOC
aliases: [field/mathematics, Mathematics sources, Math MOC]
tags: [moc]
status: stable
created: 2026-06-19
updated: 2026-06-19
---

# Mathematics MOC

> Map of Content for the **`field/mathematics`** discipline facet. Auto-populated by the **Bases**
> core plugin from the `field/*` tags.

Mathematics (**96** sources) supplies the geometric and analytic backbone of the program:
SPD / Riemannian geometry, Lie theory and gauge geometry, [[Information geometry and natural gradient|information geometry]],
and the kinetic-PDE / mean-field-game machinery behind [[Statistical physics of social systems and collective behavior|opinion dynamics]].

```base
filters:
  and:
    - 'file.hasTag("field/mathematics")'
views:
  - type: table
    name: "Mathematics sources"
    order:
      - title
    properties:
      - file.name
      - title
      - year
```

## Cross-facet pivots
Compose with the topic facet via tag search — e.g. `tag:#field/mathematics tag:#cluster/spd-geometry`
or `tag:#field/mathematics tag:#cluster/social-physics/opinion-dynamics`. See the [[Disciplines MOC]] hub.
