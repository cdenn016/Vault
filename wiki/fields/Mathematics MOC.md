---
type: moc
title: Mathematics MOC
aliases: [field/mathematics, Mathematics sources, Math MOC]
tags: [moc]
status: stable
created: 2026-06-19
updated: 2026-08-03
---

# Mathematics MOC

> Map of Content for the **`field/mathematics`** discipline facet. Auto-populated by the **Bases**
> core plugin from the `field/*` tags.

Mathematics (**235** sources) supplies the geometric and analytic backbone of the program:
SPD / Riemannian geometry, Lie theory and gauge geometry, [[Information geometry and natural gradient|information geometry]],
and the kinetic-PDE / mean-field-game machinery behind [[Statistical physics of social systems and collective behavior|opinion dynamics]].

The **harmonic-map / discrete-gauge-theory cluster** from Schnörr's Heidelberg group sits here as well:
[[cassel-2024-sigma-flows]] (harmonic maps into a Fisher-Rao statistical manifold; Lyapunov decrease
only, existence and global convergence explicitly open), [[cassel-2025-bundle-scale-spaces]] and
[[cassel-2025-yang-mills-data]] (discrete vector bundles, gauged Laplacians, a discrete Yang-Mills
energy), and [[gonzalez-alvarado-2025-patch-assignment]] (Riemannian gradient flows on products of
simplices, characterised as critical points of a Lagrangian action).

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
