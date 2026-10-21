---
type: moc
title: Physics MOC
aliases: [field/physics, Physics sources]
tags: [moc]
status: stable
created: 2026-06-19
updated: 2026-10-20
---

# Physics MOC

## Dynamic link fields, October 3, 2026

[[dennis-2026-dynamic-links]] treats attention link generators as latent lattice gauge variables on a depth-by-token lattice. It uses a Frobenius-defect curvature prior that reduces to Wilson's action on $O(K)$, with the kinetic term supplied by time-like loops. Its linearized link equation is a screened, massive Euclidean Maxwell equation, and the inertia of the maximum a posteriori path over depth has Euclidean sign. Integrating out undirected Gaussian matter induces $\tfrac12\log\det J$, whose hopping expansion begins with Wilson's triangle action. Agent-drafted, float64 checks at small size, nothing trained.

[[multiagentelbo-2026-10-04-lie-algebra-links]] makes the multi-agent links latent lattice gauge variables with a loop-action prior. Undirected matter induces the Wilson triangle term, time-like loop defects across learning episodes supply a mass, and the linearized operator has screened, massive Euclidean Proca structure. Cross-model checked; nothing trained.

[[lebowitz-1968-analytic-clustering-thermodynamic-functions]] (1968) proves joint analyticity of the Ising-ferromagnet pressure in temperature and field away from the Lee-Yang zeros.

[[dennis-2026-glk-attention-v2-rework-2026-10-05]] (2026-10-05) states the lattice reading of attention: the lattice is the communication graph above one context, not an Eguchi–Kawai reduction; invertible links are lattice-gauge data and quiver bifundamentals, singular head maps are sheaf data, and the exponential chart gives the hopping term $\sum_j\beta_{ij}\Theta_{ij}\mu_j$.

[[favoni-2022-lattice-gauge-equivariant-cnns]] (2022) constructs lattice gauge equivariant networks for $\mathrm{SU}(N_c)$ links: parallel-transport convolution, bilinear products that generate arbitrary contractible Wilson loops, and exponentiation and trace layers. [[disipio-2025-curved-spacetime-transformers]] (2025) maps attention onto a discrete connection, layers onto time slices and training onto a least-action principle by analogy with general relativity, and tests the prediction of bent embedding trajectories.

## Conditional Gaussian coarse-graining, September 30, 2026

> Map of Content for the **`field/physics`** discipline facet. The table is auto-populated by the
> **Bases** core plugin from the `field/*` tags and updates itself as sources are added.

Physics is the largest discipline in the corpus (**264** sources). Its notes occupy three regions of
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

## Matrix-link ingestion, September 20, 2026

[[wetterich-2014-linear-lattice-gauge-theory]] records the matrix-link source and its stated scope; [[Lattice gauge theory]] and [[GL(K) gauge-equivariant attention]] provide the synthesis. The source is included in the tagged Bases view.

## Spin-foam coarse-graining sources, September 30, 2026

[[Coarse Graining]] connects the boundary/refinement, tensor-interface, and GFT sources below to the pointwise multi-agent program. The Bases view also lists these physics-tagged sources automatically.

- [[asante-2022-spin-foams-refinement-renormalization]]
- [[bahr-2014-background-independent-renormalization]]
- [[bahr-2011-operator-spin-foams]]
- [[dittrich-2016-decorated-tensor-networks]]
- [[dittrich-2012-continuum-limit-spin-foams]]
- [[dittrich-2014-time-evolution-refining-coarse-graining]]
- [[delcamp-2017-nonabelian-decorated-tensor-networks]]
- [[delcamp-2017-fusion-basis]]
- [[cunningham-2020-fusion-charge-coarse-graining]]
- [[hauru-2018-graph-independent-local-truncations]]
- [[oriti-2006-group-field-theory]]
- [[benedetti-2015-functional-renormalization-tgft]]
- [[carrozza-2014-renormalization-su2-tgft]]
- [[gurau-2014-random-tensor-universality]]
- [[yosprakob-2024-reduced-nonabelian-tensor-networks]]
