---
type: theme
title: Statistical physics of social systems and collective behavior
aliases:
  - Statistical physics of social systems
  - Sociophysics neighborhood
  - Collective behavior models
  - Social physics landscape
tags:
  - cluster/social-physics
  - project/social-physics
status: stable
created: 2026-06-19
updated: 2026-11-18
---

# Statistical physics of social systems and collective behavior

## Norm formation and founding memory (2026-09-28)

A verified reference scan (gathered by Claude Opus 5.5, verified by Claude Fable 5.1) adds experimental and theoretical work on how a collective's founding conditions are kept or forgotten. Sherif's autokinetic monograph ([[sherif-1935-social-factors-perception]], restated in [[sherif-1936-psychology-social-norms]]) shows a shared norm formed by mutual convergence that persists when members are later tested alone, with less complete convergence when members begin from private norms. Replacement-generation experiments show an arbitrary founding tradition decaying toward the natural norm as members turn over ([[jacobs-1961-arbitrary-tradition]], known here only through [[macneil-1976-norm-change-arbitrariness]]), and more arbitrary norms losing a larger fraction of their displacement per generation. Organizational imprinting ([[marquis-2013-imprinting-multilevel-theory]], [[stinchcombe-1965-social-structure-organizations]]) treats the opposite case, founding features that persist. Conformist transmission makes the founding frequency select a permanent basin within the model ([[boyd-1982-cultural-transmission-cooperation]]), stochastically stable conventions are selected in a zero-noise limit ([[young-1993-evolution-conventions]]), and web experiments show conventions emerging after an initial transient and tipping points sharp only at large size and long times ([[centola-2015-spontaneous-emergence-conventions]], [[centola-2018-tipping-points-social-convention]]; see [[Phase transitions in social systems]]). [[campbell-1958-common-fate-social-entities]] is recorded at metadata level only.

## Transitions, finite size, and founding memory (2026-09-28)

A second verified scan (same gatherer and verifier) separates genuine transitions from finite-size crossovers; the synthesis is in [[Phase transitions in social systems]]. On the standard reading of [[yang-1952-phase-transitions-condensation]] a sharp transition needs an infinite-system limit, and [[fisher-1972-finite-size-scaling-critical-region]] describe the rounding and shift a finite system shows instead (both at abstract level). The Axelrod transition in the largest-domain fraction ([[castellano-marsili-vespignani-2000-axelrod-transition]]), the Kuramoto onset with its $O(N^{-1/2})$ finite-$N$ fluctuations ([[strogatz-2000-kuramoto-to-crawford]]), the Vicsek flocking transition ([[vicsek-1995-self-driven-particles]]), link condensation onto the fittest node in growing networks ([[bianconi-2001-bose-einstein-condensation-networks]]), and the bifurcations in the number of opinion clusters in the population-density limit ([[ben-naim-2003-bifurcations-compromise]]) are all order-parameter statements in a size or growth limit. With cultural drift, by contrast, the order–disorder change in Axelrod's model is controlled by $rN\ln N$ and, in the authors' words, is not a phase transition because it disappears in the thermodynamic limit ([[klemm-2003-global-culture-noise-induced-transition]]). Two of these bear on founding memory. The relaxation time $N\ln N$ in Klemm et al. and the coarsening time $t_{\mathrm{co}}\sim L^2$ in Castellano et al. both grow with size, so a founding configuration that a small group outlives can outlast every accessible time scale in a large one. In [[deffuant2000-bounded-confidence]] the cluster an agent joins is fixed by its initial opinion.

## The landscape

Statistical social physics contains many mechanism-specific models rather than one universal update law. The [[Voter model]] studies stochastic imitation; [[Discrete spin and majority-rule models of opinion]] study conformist alignment and frustration; [[Bounded confidence]] models selective interaction; [[Threshold models and complex contagion]] model reinforcement-dependent adoption; [[Synchronization and the Kuramoto model]] studies phase locking; and kinetic or mean-field approaches pass from agents to population densities. The surveys [[castellano-2009-statistical-physics-social-dynamics]], [[galam-2008-sociophysics]], [[flache-2017-social-influence-models]], and [[jusup-2022-social-physics]] organize this plural landscape. Classical averaging models include DeGroot ([[degroot-1974-consensus]]), Friedkin–Johnsen ([[friedkin1990-social-influence-opinions]]), and the bounded-confidence models of [[hegselmann-2002-opinion]] and [[deffuant2000-bounded-confidence]]. Diffusion of innovations requires an adoption state, hazard, irreversibility rule, and population equation; [[bass-1969-product-growth]] is the formal model, and visual or qualitative S-curve language cannot substitute for it.

## Polarization and active sampling

The active confirmation-biased sampling in [[albarracin-2022-epistemic-communities]] changes which evidence is sampled and can maintain segregated epistemic communities. See [[Echo chambers and polarization]] and [[Collective active inference]].

## Mechanics and dynamics of opinion

Several works treat opinion change with mechanical or second-order structure:

- [[martins-2015-opinion-particles]] develops Bayesian-inspired opinion particles with inertia and a harmonic example.
- [[xue-hirche-cao-2020-opinion-port-hamiltonian]] uses port-Hamiltonian systems and passivity for opinion networks.
- [[baumann-sokolov-tyloo-2020-second-order-consensus]] obtains Laplacian-mode resonance in second-order consensus under periodic coupling.
- [[sampson-porter-restrepo-2025-oscillatory-opinion]] obtains oscillatory and excitable opinion dynamics through individual--group feedback.
- [[nevin-mandell-atak-1983-behavioral-momentum]] operationalizes behavioral persistence under disruption.

The information-geometric mechanics neighborhood is also relevant: [[chirco-2022-statistical-bundle-dynamics]], [[girolami-calderhead-2011-riemann-hmc]], [[leok-zhang-2017-information-geometric-mechanics]], and [[pistone-2018-statistical-bundle-lagrangian]] show that mechanics on statistical manifolds and Fisher-dependent kinetic geometry have substantial precedent.

## Continuum and multi-scale directions

[[Kinetic theory of opinion dynamics]] and [[Mean-field games and continuum limits]] are natural external tools for passing from finite populations to field descriptions. [[Renormalization group flow]] is an adjacent coarse-graining program.

## Inference, communication, and population-limit bridge (2026-08-10)

The decentralized literature separates inference error from network error. [[campbell-how-2014-decentralized-bayes]]
addresses fusion of separately approximated posteriors; [[battistelli-chisci-2014-kl-density-consensus]]
and [[bandyopadhyay-chung-2018-logop-filtering]] address logarithmic pooling and density consensus;
[[julier-uhlmann-1997-covariance-intersection]] handles unknown cross-correlation conservatively;
and [[duchi-2014-distributed-estimation]] makes bit/message budgets part of the statistical problem.
These distinctions are banked in [[Decentralized Bayesian inference]],
[[Communication-constrained inference]], and [[Conservative information fusion]].

Social learning adds different assumptions again. [[lalitha-2018-distributed-hypothesis-testing]],
[[jadbabaie-2012-non-bayesian-social-learning]], and [[aumann-1976-agreeing-disagree]] separate
network learning rates, heuristic belief aggregation, and common-prior/common-knowledge agreement.

For large populations, [[lovasz-szegedy-2006-dense-graph-limits]],
[[bayraktar-2023-graphon-mean-field-systems]], [[sznitman-1991-propagation-chaos]], and
[[caines-huang-2021-graphon-mean-field-games]] type distinct deterministic, stochastic, and strategic
routes. For higher-order diagnostics, [[rosas-2019-o-information]],
[[williams-beer-2010-pid]], and [[lyu-2026-pid-inconsistencies]] require estimator and axiom choices;
compact algebra is not evidence of scalable or unique empirical decomposition.

## Sources synthesized

- [[martins-2015-opinion-particles]], [[nevin-mandell-atak-1983-behavioral-momentum]], [[xue-hirche-cao-2020-opinion-port-hamiltonian]], [[baumann-sokolov-tyloo-2020-second-order-consensus]], [[bass-1969-product-growth]], [[sampson-porter-restrepo-2025-oscillatory-opinion]] -- mechanics, dynamics, and diffusion models.
- [[degroot-1974-consensus]], [[friedkin1990-social-influence-opinions]], [[hegselmann-2002-opinion]], [[deffuant2000-bounded-confidence]] -- classical averaging models.
- [[albarracin-2022-epistemic-communities]] -- active-sampling polarization.
- [[castellano-2009-statistical-physics-social-dynamics]], [[galam-2008-sociophysics]], [[flache-2017-social-influence-models]], [[jusup-2022-social-physics]] -- field maps.
- [[sherif-1935-social-factors-perception]], [[jacobs-1961-arbitrary-tradition]], [[macneil-1976-norm-change-arbitrariness]], [[marquis-2013-imprinting-multilevel-theory]], [[stinchcombe-1965-social-structure-organizations]], [[boyd-1982-cultural-transmission-cooperation]], [[young-1993-evolution-conventions]], [[centola-2015-spontaneous-emergence-conventions]], [[centola-2018-tipping-points-social-convention]], [[campbell-1958-common-fate-social-entities]] -- norm formation and founding memory (2026-09-28).
- [[yang-1952-phase-transitions-condensation]], [[fisher-1972-finite-size-scaling-critical-region]], [[castellano-marsili-vespignani-2000-axelrod-transition]], [[klemm-2003-global-culture-noise-induced-transition]], [[strogatz-2000-kuramoto-to-crawford]], [[vicsek-1995-self-driven-particles]], [[bianconi-2001-bose-einstein-condensation-networks]], [[ben-naim-2003-bifurcations-compromise]] -- transitions, finite size, and founding memory (2026-09-28).

## See also

- [[Gauge VFE ELBO curriculum]]
- [[Sociophysics]]
- [[Opinion dynamics]]
- [[Echo chambers and polarization]]
- [[Belief perseverance and confirmation bias]]
- [[Collective active inference]]
