---
type: moc
title: Mathematics MOC
aliases: [field/mathematics, Mathematics sources, Math MOC]
tags: [moc]
status: stable
created: 2026-06-19
updated: 2026-09-12
---

# Mathematics MOC

> Map of Content for the **`field/mathematics`** discipline facet. Auto-populated by the **Bases**
> core plugin from the `field/*` tags.

Mathematics (**236** sources) supplies the geometric and analytic backbone of the program:
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
- [[ay-2015-parametrized-measure-models]]
- [[barbieri-2020-gibbsian-representations-of-continuous-specifications-the-theorems-of]]
- [[bauschke-2003-duality-for-bregman-projections-onto-translated-cones-and-affine]]
- [[berman-2022-on-the-dynamics-of-inference-and-learning]]
- [[berman-2022-the-inverse-of-exact-renormalization-group-flows-as-statistical-infere]]
- [[bertsekas-1983-distributed-asynchronous-computation-of-fixed-points]]
- [[bertsekas-1991-some-aspects-of-parallel-and-distributed-iterative-algorithms-a-s]]
- [[borgs-1995-surface-induced-finite-size-effects-for-first-order-phase-transitions]]
- [[bruveris-2016-geometry-of-the-fisher-rao-metric-on-the-space-of-smooth-densities-on]]
- [[camia-2012-planar-ising-magnetization-field-i-uniqueness-of-the-critical-scaling]]
- [[camia-2013-planar-ising-magnetization-field-ii-properties-of-the-critical-and-nea]]
- [[camia-2015-conformal-measure-ensembles-for-percolation-and-the-fk-ising-model]]
- [[camia-2017-exponential-decay-for-the-near-critical-scaling-limit-of-the-planar-is]]
- [[camia-2017-fk-ising-coupling-applied-to-near-critical-planar-models]]
- [[casanellas-2020-the-embedding-problem-for-markov-matrices]]
- [[catanzaro-2025-renormalization-of-interacting-random-graph-models]]
- [[chelkak-2012-conformal-invariance-of-spin-correlations-in-the-planar-ising-model]]
- [[chigansky-undated-intrinsic-methods-in-filter-stability]]
- [[cho-2017-disintegration-and-bayesian-inversion-via-string-diagrams]]
- [[chojnowska-michalik-2002-symmetric-ornstein-uhlenbeck-semigroups-and-their-generators]]
- [[cohen-2012-formal-proofs-in-real-algebraic-geometry-from-ordered-fields-to-quanti]]
- [[cohen-undated-bundles-homotopy-and-manifolds]]
- [[csiszar-2004-information-theory-and-statistics-a-tutorial]]
- [[cuesta-2004-general-non-existence-theorem-for-phase-transitions-in-one-dimens]]
- [[dahlqvist-2018-borel-kernels-and-their-approximation-categorically]]
- [[davies-2010-embeddable-markov-matrices]]
- [[dobrushin-1987-completely-analytical-interactions-constructive-description]]
- [[dorfler-2011-kron-reduction-of-graphs-with-applications-to-electrical-networks]]
- [[etingof-2024-lie-groups-and-lie-algebras-mit-lecture-notes]]
- [[fageot-2016-scaling-limits-of-solutions-of-spde-driven-by-l-evy-white-noises]]
- [[feray-2013-mod-phi-convergence-i-normality-zones-and-precise-deviations]]
- [[fernandez-2006-cluster-expansion-for-abstract-polymer-models-new-bounds-from-an-old-a]]
- [[frank-2010-a-new-rearrangement-free-proof-of-the-sharp-hardy-littlewood-sobolev-i]]
- [[fritz-2019-a-synthetic-approach-to-markov-kernels-conditional-independence-and-th]]
- [[gagne-2017-a-categorical-characterization-of-relative-entropy-on-standard-borel-s]]
- [[gantumur-2011-the-cauchy-kovalevskaya-theorem-math-580-lecture-notes-2]]
- [[gentner-2011-palm-theory-mass-transports-and-ergodic-theory-for-group-stationa]]
- [[hansen-2018-toward-a-spectral-theory-of-cellular-sheaves]]
- [[howard-2024-bayesian-rg-flow-in-neural-network-field-theories]]
- [[joly-2024-graph-coarsening-with-message-passing-guarantees]]
- [[jotz-2008-closedness-of-the-tangent-spaces-to-the-orbits-of-proper-actions]]
- [[kuo-2009-on-decompositions-of-multivariate-functions]]
- [[le-2013-the-uniqueness-of-the-fisher-metric-as-information-metric]]
- [[levin-undated-markov-chains-and-mixing-times-retrieved-author-text]]
- [[levy-2001-yang-mills-measure-on-compact-surfaces]]
- [[lis-2020-on-boundary-correlations-in-planar-ashkin-teller-models]]
- [[loukas-2018-graph-reduction-with-spectral-and-cut-guarantees]]
- [[lunardi-2020-the-ornstein-uhlenbeck-semigroup-in-finite-dimension]]
- [[mayerhofer-2010-on-the-parameter-domain-of-wishart-distributions-and-their-infinite-di]]
- [[meinrenken-2003-group-actions-on-manifolds]]
- [[miller-2021-lectures-on-algebraic-topology]]
- [[oono-2019-graph-neural-networks-exponentially-lose-expressive-power-for-node-cla]]
- [[owhadi-2015-conditioning-gaussian-measure-on-hilbert-space]]
- [[pedersen-2000-the-existence-and-uniqueness-of-the-haar-integral-on-a-locally-co]]
- [[pinho-1997-critical-behavior-of-the-ising-model-on-a-hierarchical-lattice-with-ap]]
- [[pollard-2011-a-note-on-insufficiency-and-the-preservation-of-fisher-information]]
- [[polyanskiy-2014-dissipation-of-information-in-channels-with-input-constraints]]
- [[polyanskiy-2024-information-theory-august-2024-prepublication-version]]
- [[rasmussen-2006-gaussian-processes-for-machine-learning-appendix-a-mathematical-b]]
- [[rebeschini-2013-comparison-theorems-for-gibbs-measures]]
- [[schlafly-1982-universal-connections-the-local-problem]]
- [[schmah-2007-a-cotangent-bundle-slice-theorem]]
- [[shalizi-1999-computational-mechanics-pattern-and-prediction-structure-and-simplicit]]
- [[singh-2023-attention-marginal-probability-is-all-you-need]]
- [[tice-2017-quasilinear-symmetric-hyperbolic-systems]]
- [[travers-2012-exponential-bounds-for-convergence-of-entropy-rate-approximations-in-h]]
- [[tsitsiklis-1986-distributed-asynchronous-deterministic-and-stochastic-gradient-op]]
- [[turner-2011-two-problems-with-variational-expectation-maximisation-for-time-s]]
- [[watts-2013-the-orbit-space-and-basic-forms-of-a-proper-lie-groupoid]]
- [[yin-2009-a-cluster-expansion-approach-to-renormalization-group-transformations]]
- [[ying-2018-hierarchical-graph-representation-learning-with-differentiable-pooling]]
- [[multiagentelbo-2026-09-11-critical-comparisons]]
- [[multiagentelbo-2026-09-11-extension-studies]]
- [[multiagentelbo-2026-09-11-finite-program]]
- [[multiagentelbo-2026-09-11-implementation]]

## Finite dynamical RG, September 12, 2026

[[multiagentelbo-2026-09-12-dynamical-rg]] records the normalized two-channel construction, coherence and two inherited reductions, including exact conditional VFE accounting and the limits of its finite-time approximation. Its discipline tags also include it in the automatic Bases view.


[[multiagentelbo-2026-09-12-nonlinear-dynamical-rg]] adds common microscopic kinetics, actual successive formation, nonlinear inherited parents and separate conditional-entropy control at finite scope.
