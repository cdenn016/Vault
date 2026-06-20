---
type: moc
title: Neuroscience MOC
aliases: [field/neuroscience, Neuroscience sources]
tags: [moc]
status: stable
created: 2026-06-19
updated: 2026-06-19
---

# Neuroscience MOC

> Map of Content for the **`field/neuroscience`** discipline facet. Auto-populated by the **Bases**
> core plugin from the `field/*` tags.

Neuroscience (**38** sources) concentrates in two places: the predictive-coding / active-inference
account of the brain (the neuroscientific root of [[Variational free energy and predictive coding|VFE]])
and the scientific theories of consciousness (IIT, global workspace, neural correlates) in
[[Consciousness and the hard problem]].

```base
filters:
  and:
    - 'file.hasTag("field/neuroscience")'
views:
  - type: table
    name: "Neuroscience sources"
    order:
      - title
    properties:
      - file.name
      - title
      - year
```

## Cross-facet pivots
Compose with the topic facet via tag search — e.g. `tag:#field/neuroscience tag:#cluster/vfe`
or `tag:#field/neuroscience tag:#cluster/participatory/consciousness`. See the [[Disciplines MOC]] hub.
