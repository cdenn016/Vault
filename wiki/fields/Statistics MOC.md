---
type: moc
title: Statistics MOC
aliases: [field/statistics, Statistics sources, Information theory MOC]
tags: [moc]
status: stable
created: 2026-06-19
updated: 2026-10-02
---

# Statistics MOC

## Cut routing and tempered Gaussian posteriors, October 2, 2026

[[dennis-2026-projected-gradient]] reads routing by a comparison divergence alone as exact inference in a cut model (modular Bayesian inference) and shows that a channel-likelihood receiver has the exact tempered Gaussian posterior as minimizer, counting the receiver entropy once. [[dennis-2026-phi-natgrad]] derives a Fisher natural gradient for frame parameters from the reference-prior family. [[dennis-2026-neuron-free-agent-theory]] uses Gamma-precision (Student-t) records and a KL-budget constraint in one constrained ELBO.

## Joint particle-filter losses, October 2, 2026

[[multiagentelbo-2026-10-02-joint-particle-filter]] reports eight distinct passing tiny checks and one 616.507218-second CPU study using 128 saved paths at each of 512/1,024 agents. Every tested cloud underperforms the static-lift baseline, and persistent64 underperforms reset64. Mean joint ESS at observed assignment changes is 1.751/1.458 of 64 for persistent64; hold-row medians obscure this concentration. Paired losses estimate differences of expected path KL conditional on independent algorithmic tapes, not absolute KL or the tape-marginalized parent error. Exact filtering and finite-history weak consistency do not close the regular-filter or formation obligations. Work pauses after publication at the user's request.

## Joint retained path scores, October 2, 2026

[[multiagentelbo-2026-10-02-joint-retained-parent]] derives a source/Gaussian conditional-information score for normalized parents of projected configurations and assignments. Its 512/1,024-agent results report empirical paired standard errors and a posthoc control that separates pointwise approximation from observed-configuration information. Absolute retained-path KL and confidence-certified bounds remain unknown.

## Exterior experiments and predictive budgets, September 30, 2026

[[dennis-2026-spin-foam-boundary-methods]] records common reference/evidence recovery and support-preserving residual bounds separating posterior error from evidence and complete free energy. Its standard-Borel finite-horizon identity separates conditional history information from source-context row risk under dominance and finiteness conditions. Completed-prefix activation uses the actual source law. Useful finite memory and uniform family budgets remain open; the source is included in the tagged Bases view.

## Evidence-preserving Gaussian parents, September 30, 2026

[[multiagentelbo-2026-09-30-pointwise-gaussian-network]] records normalized priors and record likelihoods, complete Schur evidence terms, and equilibrium reverse conditionals. Ten tiny CPU tests and 45 comparisons in one 512-agent study passed. Latent-link mixtures and actual-history activation laws remain separate inference problems.

## Mixture references, September 27, 2026

[[ghahramani-1994-incomplete-data-em]] (Gaussian mixture regression) and [[hershey-2007-kl-gmm]] (variational KL for Gaussian mixtures) support [[Template routing]].

## Path-information references checked September 26, 2026

[[hartmann-2020-coarse-graining-nonreversible-sdes]] and [[backhoff-veraguas-2023-specific-relative-entropy]] distinguish time-marginal error, complete-path KL, and mesh-normalized specific entropy. See [[multiagentelbo-2026-09-26-selection-and-reference-review]] for the hypotheses and the separate model-specific application.


> Map of Content for the **`field/statistics`** discipline facet (statistics & information theory).
> Auto-populated by the **Bases** core plugin from the `field/*` tags.

Statistics & information theory (**161** sources) underpins the variational-inference and
information-geometry layers of the program: Bayesian inference, divergences, model selection
(MDL / BIC), forecasting, and the information bottleneck. Statistics is rarely a source's headline
field but pervades the corpus through cross-disciplinary tags.

The adaptive cyclic Gaussian construction [[multiagentelbo-2026-09-12-adaptive-cyclic-rg]] adds normalized changing-conditional learning, exact loop-preserving parents and finite-depth dynamical bounds in its admitted scope.

```base
filters:
  and:
    - 'file.hasTag("field/statistics")'
views:
  - type: table
    name: "Statistics sources"
    order:
      - title
    properties:
      - file.name
      - title
      - year
```

## Finite-depth dynamical RG continuation

[[multiagentelbo-2026-09-12-finite-depth-dynamical-rg]] records repeated nonlinear formation, exact normalized parent composition and separate finite-depth entropy and path estimates. Supplied weights and depth-dependent constants remain explicit.

## Cross-facet pivots
Compose with the topic facet via tag search — e.g. `tag:#field/statistics tag:#cluster/info-geometry`
or `tag:#field/statistics tag:#cluster/vfe`. See the [[Disciplines MOC]] hub for all fields.

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
- [[ay-2015-parametrized-measure-models]]
- [[bauschke-2003-duality-for-bregman-projections-onto-translated-cones-and-affine]]
- [[berman-2022-on-the-dynamics-of-inference-and-learning]]
- [[bertsekas-1983-distributed-asynchronous-computation-of-fixed-points]]
- [[bruveris-2016-geometry-of-the-fisher-rao-metric-on-the-space-of-smooth-densities-on]]
- [[casanellas-2020-the-embedding-problem-for-markov-matrices]]
- [[chigansky-undated-intrinsic-methods-in-filter-stability]]
- [[cho-2017-disintegration-and-bayesian-inversion-via-string-diagrams]]
- [[chojnowska-michalik-2002-symmetric-ornstein-uhlenbeck-semigroups-and-their-generators]]
- [[csiszar-2004-information-theory-and-statistics-a-tutorial]]
- [[davies-2010-embeddable-markov-matrices]]
- [[feray-2013-mod-phi-convergence-i-normality-zones-and-precise-deviations]]
- [[fritz-2019-a-synthetic-approach-to-markov-kernels-conditional-independence-and-th]]
- [[gagne-2017-a-categorical-characterization-of-relative-entropy-on-standard-borel-s]]
- [[gentner-2011-palm-theory-mass-transports-and-ergodic-theory-for-group-stationa]]
- [[le-2013-the-uniqueness-of-the-fisher-metric-as-information-metric]]
- [[levin-undated-markov-chains-and-mixing-times-retrieved-author-text]]
- [[lunardi-2020-the-ornstein-uhlenbeck-semigroup-in-finite-dimension]]
- [[mayerhofer-2010-on-the-parameter-domain-of-wishart-distributions-and-their-infinite-di]]
- [[owhadi-2015-conditioning-gaussian-measure-on-hilbert-space]]
- [[pollard-2011-a-note-on-insufficiency-and-the-preservation-of-fisher-information]]
- [[polyanskiy-2014-dissipation-of-information-in-channels-with-input-constraints]]
- [[polyanskiy-2024-information-theory-august-2024-prepublication-version]]
- [[rasmussen-2006-gaussian-processes-for-machine-learning-appendix-a-mathematical-b]]
- [[rebeschini-2013-comparison-theorems-for-gibbs-measures]]
- [[shalizi-1999-computational-mechanics-pattern-and-prediction-structure-and-simplicit]]
- [[travers-2012-exponential-bounds-for-convergence-of-entropy-rate-approximations-in-h]]
- [[tsitsiklis-1986-distributed-asynchronous-deterministic-and-stochastic-gradient-op]]
- [[turner-2011-two-problems-with-variational-expectation-maximisation-for-time-s]]

## Finite dynamical RG, September 12, 2026

[[multiagentelbo-2026-09-12-dynamical-rg]] records the normalized two-channel construction, coherence and two inherited reductions, including exact conditional VFE accounting and the limits of its finite-time approximation. Its discipline tags also include it in the automatic Bases view.


[[multiagentelbo-2026-09-12-nonlinear-dynamical-rg]] adds common microscopic kinetics, actual successive formation, nonlinear inherited parents and separate conditional-entropy control at finite scope.

## Nonlinear adaptive cyclic RG, September 13

[[multiagentelbo-2026-09-13-nonlinear-adaptive-attention-rg]] adds the scoped nonlinear adaptive construction, full marked activation and analytical conditional and path bounds.

## Finite-rate adaptive cyclic RG, September 13

[[multiagentelbo-2026-09-13-finite-rate-adaptive-cyclic-rg]] supplies the accelerated-energy positive-rate source construction, exact marked activations and full assignment-history comparison.

## Weakest-one adaptive cyclic RG, September 13

[[multiagentelbo-2026-09-13-fixed-weakest-energy-adaptive-cyclic-rg]] supplies the fixed-weakest-energy positive-rate construction, exact marked activations, joint entropy and full assignment-history comparison.

## Observed-link Gaussian parent reference, September 30, 2026

[[multiagentelbo-2026-09-30-gaussian-parent-dynamics]] records seven tiny CPU tests and 95 passing comparisons across five 512-agent cases, actual-history filtering and finite-path Markov information loss. External controls and network-sized conditionals do not establish endogenous learning or autonomous parent closure.

[[multiagentelbo-2026-09-30-spin-foam-integration-review]] records the eight-investigator review of the spin-foam boundary companion, four statements integrated into the MultiAgentELBO theory (memory identity on standard Borel records, two-sided bounded-tier divergence bounds, tree-transport composition, and recovery by likelihood descent), and their Claude Fable 5.1 verification.

[[multiagentelbo-2026-09-30-locality-parent-memory]] records parent-memory decay across locality priors at N = 64 to 2,048: local priors keep finite size-independent memory, while complete support becomes nearly Markov by exchangeability.
