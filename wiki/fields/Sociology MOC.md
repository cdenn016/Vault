---
type: moc
title: Sociology MOC
aliases: [field/sociology, Sociology sources]
tags: [moc]
status: stable
created: 2026-06-19
updated: 2026-06-19
---

# Sociology MOC

> Map of Content for the **`field/sociology`** discipline facet. Auto-populated by the **Bases**
> core plugin from the `field/*` tags.

Sociology (**66** sources) is the social-science half of the opinion-dynamics work — social networks,
political polarization and affective polarization, diffusion of innovations, echo chambers, and
collective social behaviour. It sits almost entirely within the
[[Statistical physics of social systems and collective behavior|social-physics]] cluster.

```base
filters:
  and:
    - 'file.hasTag("field/sociology")'
views:
  - type: table
    name: "Sociology sources"
    order:
      - title
    properties:
      - file.name
      - title
      - year
```

## Cross-facet pivots
Compose with the topic facet via tag search — e.g.
`tag:#field/sociology tag:#cluster/social-physics/networks-and-contagion`. See the [[Disciplines MOC]] hub.
