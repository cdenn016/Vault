---
type: moc
title: Physics MOC
aliases: [field/physics, Physics sources]
tags: [moc]
status: stable
created: 2026-06-19
updated: 2026-09-11
---

# Physics MOC

> Map of Content for the **`field/physics`** discipline facet. The table is auto-populated by the
> **Bases** core plugin from the `field/*` tags and updates itself as sources are added.

Physics is the largest discipline in the corpus (**258** sources). Its notes occupy three regions of
the program: the statistical-physics / sociophysics of collective behavior (in [[Statistical physics of social systems and collective behavior|social-physics]]), the quantum-foundations and emergent-gravity wing of the
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

## MultiAgentELBO research ingestion, September 11, 2026

[[Gauge-VFE RG research synthesis September 2026]] connects the following new source records to the current theory. Existing sources are reused through [[multiagentelbo-2026-09-11-reference-register]].

- [[multiagentelbo-2026-09-11-conditional-geometry]]
- [[multiagentelbo-2026-09-11-continuum]]
- [[multiagentelbo-2026-09-11-formation]]
- [[multiagentelbo-2026-09-11-gaussian-closure]]
- [[multiagentelbo-2026-09-11-geometry-feedback]]
- [[multiagentelbo-2026-09-11-memory]]
- [[multiagentelbo-2026-09-11-neighborhoods]]
- [[multiagentelbo-2026-09-11-normalized-core]]
- [[multiagentelbo-2026-09-11-reference-register]]
- [[multiagentelbo-2026-09-11-research-snapshot]]
- [[multiagentelbo-2026-09-11-scale-and-inference]]
- [[multiagentelbo-2026-09-11-spatial]]
- [[multiagentelbo-2026-09-11-thermodynamic-fisher]]
- [[abramsky-2011-the-sheaf-theoretic-structure-of-non-locality-and-contextuality]]
- [[avramidi-1997-covariant-techniques-for-computation-of-the-heat-kernel]]
- [[barbieri-2020-gibbsian-representations-of-continuous-specifications-the-theorems-of]]
- [[berman-2022-the-inverse-of-exact-renormalization-group-flows-as-statistical-infere]]
- [[borgs-1995-surface-induced-finite-size-effects-for-first-order-phase-transitions]]
- [[camia-2012-planar-ising-magnetization-field-i-uniqueness-of-the-critical-scaling]]
- [[camia-2013-planar-ising-magnetization-field-ii-properties-of-the-critical-and-nea]]
- [[camia-2015-conformal-measure-ensembles-for-percolation-and-the-fk-ising-model]]
- [[camia-2017-exponential-decay-for-the-near-critical-scaling-limit-of-the-planar-is]]
- [[camia-2017-fk-ising-coupling-applied-to-near-critical-planar-models]]
- [[catanzaro-2025-renormalization-of-interacting-random-graph-models]]
- [[chelkak-2012-conformal-invariance-of-spin-correlations-in-the-planar-ising-model]]
- [[cuesta-2004-general-non-existence-theorem-for-phase-transitions-in-one-dimens]]
- [[dobrushin-1987-completely-analytical-interactions-constructive-description]]
- [[etingof-2024-lie-groups-and-lie-algebras-mit-lecture-notes]]
- [[fageot-2016-scaling-limits-of-solutions-of-spde-driven-by-l-evy-white-noises]]
- [[fernandez-2006-cluster-expansion-for-abstract-polymer-models-new-bounds-from-an-old-a]]
- [[howard-2024-bayesian-rg-flow-in-neural-network-field-theories]]
- [[levy-2001-yang-mills-measure-on-compact-surfaces]]
- [[lis-2020-on-boundary-correlations-in-planar-ashkin-teller-models]]
- [[pinho-1997-critical-behavior-of-the-ising-model-on-a-hierarchical-lattice-with-ap]]
- [[schlafly-1982-universal-connections-the-local-problem]]
- [[schmah-2007-a-cotangent-bundle-slice-theorem]]
- [[tice-2017-quasilinear-symmetric-hyperbolic-systems]]
- [[yin-2009-a-cluster-expansion-approach-to-renormalization-group-transformations]]
- [[multiagentelbo-2026-09-11-critical-comparisons]]
- [[multiagentelbo-2026-09-11-extension-studies]]
- [[multiagentelbo-2026-09-11-finite-program]]
- [[multiagentelbo-2026-09-11-implementation]]
