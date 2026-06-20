---
type: moc
title: "{{Field}} MOC"
aliases: []
tags: [moc]
status: stable
created: 2026-06-19
updated: 2026-06-19
---

# {{Field}} MOC

> Map of Content for the **`field/{{slug}}`** discipline facet — the source notes whose academic
> discipline of origin is {{field}}. The table is auto-populated by the **Bases** core plugin from
> the `field/*` tags; it updates itself as sources are added. (Do not use Dataview — not installed.)

Orientation: what this discipline contributes to the program and which research clusters its sources
mostly land in.

```base
filters:
  and:
    - 'file.hasTag("field/{{slug}}")'
views:
  - type: table
    name: "{{Field}} sources"
    order:
      - title
    properties:
      - file.name
      - title
      - year
```

## Cross-facet pivots
Discipline composes with the topic (`cluster/*`) and project (`project/*`) facets via tag search —
e.g. `tag:#field/{{slug}} tag:#cluster/info-geometry`. See the [[Disciplines MOC]] hub for all fields.
