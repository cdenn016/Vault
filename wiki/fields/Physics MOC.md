---
type: moc
title: Physics MOC
aliases: [field/physics, Physics sources]
tags: [moc]
status: stable
created: 2026-06-19
updated: 2026-11-13
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

## Chris Fields collection, November 1, 2026

[[Chris Fields and physics as communication]] provides the reading order, comparison, and access limits. The following sources carry this discipline tag and also appear in the live Bases view.

- [[fields-2026-amplituhedra-generic-quantum-processes]]
- [[fields-2026-from-complementarity-to-non-duality-seeing-objects-and-processes-as-pragmatic-constructs]]
- [[fields-2025-distributed-information-and-computation-in-generic-quantum-systems]]
- [[fields-2025-er-epr-is-an-operational-theorem]]
- [[fields-2025-how-do-inner-screens-enable-imaginative-experience-applying-the-free-energy-principle-directly-to-th]]
- [[fields-2025-life-its-origin-and-its-distribution-a-perspective-from-the-conway-kochen-theorem-and-the-free-energ]]
- [[fields-2025-operational-protocols-cannot-certify-classicality]]
- [[fields-2025-thoughts-and-thinkers-on-the-complementarity-between-objects-and-processes]]
- [[fields-2025-whether-a-quantum-computation-employs-nonlocal-resources-is-operationally-undecidable]]
- [[fields-2024-qecc-tqft-i-protocols]]
- [[fields-2024-qecc-tqft-ii-spacetimes]]
- [[fields-2024-making-the-thermodynamic-cost-of-active-inference-explicit]]
- [[fields-2024-nash-equilibria-and-undecidability-in-generic-physical-interactions-a-free-energy-perspective]]
- [[fields-2024-principled-limitations-on-self-representation-for-generic-physical-systems]]
- [[fields-2024-search-for-entanglement-between-spatially-separated-living-systems-experiment-design-results-and-les]]
- [[fields-2024-the-free-energy-principle-induces-compartmentalization]]
- [[friston-2023-a-variational-synthesis-of-evolutionary-and-developmental-dynamics]]
- [[fields-2023-all-quantum-systems-are-strange-a-commentary-on-path-integrals-particular-kinds-and-strange-things-b]]
- [[fields-2023-control-flow-i-active-inference]]
- [[fields-2023-control-flow-ii-tensor-networks]]
- [[fields-2023-regulative-development-as-a-model-for-origin-of-life-and-artificial-life-studies]]
- [[fields-2023-separability-contextuality-and-the-quantum-frame-problem]]
- [[fields-2022-a-free-energy-principle-for-generic-quantum-systems]]
- [[kuchling-2022-metacognition-as-a-consequence-of-competing-evolutionary-time-scales]]
- [[fields-2022-neurons-as-hierarchies-of-quantum-reference-frames]]
- [[marciano-2022-quantum-neural-networks-and-topological-quantum-field-theories]]
- [[fields-2022-sequential-measurements-topological-quantum-field-theories-and-topological-quantum-neural-networks]]
- [[fields-2022-the-free-energy-principle-induces-neuromorphic-development]]
- [[fields-2022-the-physical-meaning-of-the-holographic-principle]]
- [[addazi-2021-generalized-holographic-principle-gauge-invariance-and-the-emergence-of-gravity-a-la-wilczek]]
- [[fields-2021-metabolic-limits-on-classical-information-processing-by-biological-cells]]
- [[fields-2021-minimal-physicalism-as-a-scale-free-substrate-for-cognition-and-consciousness]]
- [[fields-2021-reference-frame-induced-symmetry-breaking-on-holographic-screens]]
- [[fields-2020-holographic-screens-are-classical-information-channels]]
- [[fields-2020-markov-blankets-are-general-physical-interaction-surfaces]]
- [[fields-2020-representing-measurement-as-a-thermodynamic-symmetry-breaking]]
- [[fields-2019-decoherence-as-a-sequence-of-entanglement-swaps]]
- [[fields-2019-sharing-nonfungible-information-requires-shared-nonfungible-information]]
- [[fields-2019-somatic-multicellularity-as-a-satisficing-solution-to-the-prediction-error-minimization-problem]]
- [[fields-2018-sciences-of-observation]]
- [[fields-2018-some-consequences-of-the-thermodynamic-cost-of-system-identification]]
- [[fields-2017-eigenforms-interfaces-and-holographic-encoding-toward-an-evolutionary-account-of-objects-and-spaceti]]
- [[fields-2016-building-observer-into-system]]
- [[fields-2016-decompositional-equivalence-a-fundamental-symmetry-underlying-quantum-theory]]
- [[fields-2016-effective-dark-energy-from-decoherence]]
- [[fields-2016-unitary-quantum-theory-as-a-formal-framework-for-a-theory-of-consciousness]]
- [[fields-2014-a-physics-based-metaphysics-is-a-metaphysics-based-metaphysics]]
- [[fields-2014-consistent-quantum-mechanics-admits-no-mereotopology]]
- [[fields-2014-equivalence-of-the-symbol-grounding-and-quantum-system-identification-problems]]
- [[fields-2014-hilbert-space-factorization-is-a-limited-and-expensive-information-processing-resource]]
- [[fields-2014-on-the-ollivier-poulin-zurek-definition-of-objectivity]]
- [[fields-2014-this-boundary-less-world]]
- [[fields-2013-a-whole-box-of-pandoras-systems-boundaries-and-free-will-in-quantum-theory]]
- [[fields-2013-bell-s-theorem-from-moore-s-theorem]]
- [[fields-2013-imposing-system-observer-symmetry-on-the-von-neumann-description-of-measurement]]
- [[fields-2013-on-recognizing-an-object-with-a-partition]]
- [[fields-2012-a-model-theoretic-interpretation-of-environment-induced-superselection]]
- [[fields-2012-autonomy-all-the-way-down-systems-and-dynamics-in-quantum-bayesianism]]
- [[fields-2012-if-physics-is-an-information-science-what-is-an-observer]]
- [[fields-2012-implementation-of-classical-communication-in-a-quantum-world]]
- [[fields-2011-classical-system-boundaries-cannot-be-determined-within-quantum-darwinism]]
- [[fields-2011-quantum-mechanics-from-five-physical-assumptions]]
- [[fields-2010-computational-costs-of-data-definition-at-the-quantum-classical-interface]]
- [[fields-2010-quantum-darwinism-requires-an-extra-theoretical-assumption-of-encoding-redundancy]]
- [[fields-2009-information-contents-and-architectural-requirements-of-observer-ready-states]]
- [[fields-2009-three-consequences-of-decompositional-consistency]]
- [[fields-1989-consequences-of-nonclassical-measurement-for-the-algorithmic-description-of-continuous-dynamical-systems]]

## Communication policies and collective boundaries, November 7, 2026

These sources are connected in [[Active inference communication and collective boundaries]].

- [[beck-2025-dynamic-markov-blanket-detection]]

## Collective agents references, November 10, 2026

These 81 sources are grouped by question in [[Collective agents literature map]].

- [[aguilera-2023-free-energy-principle]]
- [[aguilera-2023-knitting-markov-blanket]]
- [[aizenman-1989-rounding-first-order]]
- [[aizenman-1990-rounding-effects-quenched]]
- [[allen-1979-microscopic-antiphase-boundary]]
- [[bamieh-2012-coherence-large-scale]]
- [[barnett-2023-dynamical-independence-discovering]]
- [[berg-1977-physics-chemoreception]]
- [[berglund-2006-noise-induced-phenomena]]
- [[bettencourt-2007-growth-innovation-scaling]]
- [[bettencourt-2013-origins-scaling-cities]]
- [[bialek-2005-physical-limits-biochemical]]
- [[biskup-2004-scaling-chemical-distance]]
- [[bleher-1995-purity-limiting-gibbs]]
- [[blume-1993-statistical-mechanics-strategic]]
- [[bradde-2017-pca-meets-rg]]
- [[bravyi-2006-lieb-robinson-bounds]]
- [[bray-1994-phase-ordering-kinetics]]
- [[bricmont-1988-phase-transition-3d]]
- [[burridge-2017-spatial-evolution-human]]
- [[campanino-2003-ornstein-zernike-finite]]
- [[castello-2006-ordering-dynamics-two]]
- [[cavagna-2010-scale-free-correlations]]
- [[combes-1973-asymptotic-behaviour-eigenfunctions]]
- [[creutzig-2009-past-future-information]]
- [[ding-2023-correlation-length-two]]
- [[ding-2026-phase-transition-critical]]
- [[dobrushin-1968-description-random-field]]
- [[dobrushin-1970-prescribing-system-random]]
- [[duminil-copin-2016-proof-sharpness-phase]]
- [[dyson-1969-existence-phase-transition]]
- [[evans-2000-broadcasting-trees-ising]]
- [[fisher-1972-critical-exponents-long]]
- [[fisher-2001-nonequilibrium-dynamics-random]]
- [[friston-2021-parcels-particles-markov]]
- [[friston-2021-stochastic-chaos-markov]]
- [[friston-2022-very-particular-comment]]
- [[friston-2023-path-integrals-particular]]
- [[givon-2004-extracting-macroscopic-dynamics]]
- [[gomez-marin-2007-bounding-dissipation-stochastic]]
- [[gordon-2021-relevance-renormalization-group]]
- [[gross-1975-logarithmic-sobolev-inequalities]]
- [[haken-1983-synergetics-introduction]]
- [[hartich-2014-stochastic-thermodynamics-bipartite]]
- [[hastings-2004-locality-quantum-markov]]
- [[hastings-2006-spectral-gap-exponential]]
- [[heins-2022-sparse-coupling-markov]]
- [[horowitz-2014-thermodynamics-continuous-information]]
- [[imry-1975-random-field-instability]]
- [[ito-2013-information-thermodynamics-causal]]
- [[kato-1949-upper-lower-bounds]]
- [[kawai-2007-dissipation-phase-space]]
- [[kivela-2014-multilayer-networks]]
- [[koch-janusz-2018-mutual-information-neural]]
- [[kolchinsky-2018-semantic-information-autonomous]]
- [[kuwahara-2020-clustering-conditional-mutual]]
- [[kuwahara-2020-strictly-linear-light]]
- [[lambiotte-2008-geographical-dispersal-mobile]]
- [[lenggenhager-2020-optimal-renormalization-group]]
- [[lieb-1972-finite-group-velocity]]
- [[lin-2017-why-does-deep]]
- [[marchioro-1978-velocity-perturbation-infinite]]
- [[meshulam-2019-coarse-graining-fixed]]
- [[metivier-2014-spreading-perturbations-long]]
- [[mora-2010-limits-sensing-temporal]]
- [[nachtergaele-2006-lieb-robinson-bounds]]
- [[newman-2006-modularity-community-structure]]
- [[olver-2010-nist-handbook-mathematical]]
- [[onsager-1944-crystal-statistics-two]]
- [[ornstein-1914-accidental-deviations-density]]
- [[pavliotis-2008-multiscale-methods-averaging]]
- [[raz-2009-estimating-lieb-robinson]]
- [[ribeiro-2023-mathematical-models-explain]]
- [[roldan-2010-estimating-dissipation-single]]
- [[sachdeva-2021-optimal-prediction-resource]]
- [[sagawa-2009-minimal-energy-cost]]
- [[sang-2025-stability-mixed-state]]
- [[shalizi-2025-what-macrostate-subjective]]
- [[temple-1928-rayleigh-principle-applied]]
- [[toulouse-1977-frustration-effect-spin]]
- [[tran-2020-hierarchy-linear-light]]

## Bayesian mechanics literature, November 13, 2026

- [[dacosta-2023-entropy-production-stationary-diffusions]]
- [[feng-2011-potential-flux-decomposition]]
- [[friston-2012-fep-biological-systems]]
- [[friston-2012-free-energy-value-attractors]]
- [[friston-2020-sentience-markovian-monism]]
- [[friston-2021-interesting-observations-fep]]
- [[friston-2026-generative-modelling-nonequilibrium]]
- [[heins-2022-particular-flows-attracting-sets]]
- [[heins-2026-collective-sensing-bayesian-inference]]
- [[isomura-2023-bayesian-mechanics-self-organising]]
- [[kim-2021-bayesian-mechanics-perceptual-inference]]
- [[kim-2024-bayesian-mechanics-synaptic-learning]]
- [[millidge-2021-mathematical-walkthrough-fep]]
- [[parr-2021-memory-markov-blankets]]
- [[pearson-2026-flux-defined-markov-blanket]]
- [[polettini-2012-nonequilibrium-thermodynamics-gauge]]
- [[ramstead-2022-notation-minima-comment]]
- [[sakthivadivel-2022-entropy-maximising-parallel-transport]]
- [[sakthivadivel-2022-functorial-statistical-physics]]
- [[sakthivadivel-2022-regarding-flows-fep]]
- [[sakthivadivel-2022-weak-markov-blankets]]
- [[sakthivadivel-2023-worked-example-classical-objects]]
- [[sakthivadivel-2026-markov-interacting-particles]]
- [[sandved-smith-2024-metacognitive-particles]]
- [[spisak-2026-self-orthogonalizing-attractor-networks]]
- [[ueltzhoffer-2021-thermodynamic-efficiency-dissipative]]

## Symmetry and hierarchical emergence, November 14, 2026

- [[rosas-2026-symmetry-hierarchical-emergence]]
