---
type: theme
title: Gauge VFE ELBO curriculum
aliases:
  - Gauge-theoretic VFE ELBO reading curriculum
  - Gauge VFE textbook curriculum
tags:
  - cluster/vfe
  - cluster/gauge-theory
  - cluster/info-geometry
  - cluster/spd-geometry
  - cluster/multi-agent
  - project/transformer
  - project/multi-agent
status: stable
created: 2026-07-19
updated: 2026-07-19
---

# Gauge VFE ELBO curriculum

## Purpose and scope

No single textbook develops the full construction used by this research program. A general gauge-covariant VFE or ELBO needs several independently defined layers: normalized probabilistic models and posterior families; convex and variational duality; information geometry; smooth manifolds and Lie groups; principal bundles, connections, and curvature; SPD covariance geometry; Riemannian and numerical optimization; and, for optional extensions, statistical mechanics, active inference, representation theory, renormalization, and effective actions.

> [!note] Editorial: ranking rule
> The order below is a curriculum judgment based on marginal importance to this program, not an objective theorem and not a strict reading order. The source notes support the books' bibliographic records and subject coverage; they cannot establish a unique ordinal ranking.

## Ranked core

1. **[[murphy-2022-probabilistic-machine-learning-introduction|Murphy, Probabilistic Machine Learning: An Introduction]] and [[murphy-2023-probabilistic-machine-learning-advanced-topics|Advanced Topics]].** The general probabilistic-modeling and inference spine.
2. **[[wainwright-2008-graphical-models-variational|Wainwright and Jordan, Graphical Models, Exponential Families, and Variational Inference]].** The most direct source for exponential-family duality, exact variational principles, mean field, Bethe/Kikuchi objectives, and variational parameter estimation.
3. **[[boyd-vandenberghe-2004-convex-optimization|Boyd and Vandenberghe, Convex Optimization]].** Convex conjugacy, duality, entropy, and positive-semidefinite optimization beneath the variational machinery.
4. **[[klenke-2020-probability-theory|Klenke, Probability Theory]].** The measure-theoretic foundation for probability kernels, conditional laws, and configuration-level KL identities.
5. **[[amari-2016-information-geometry-applications|Amari, Information Geometry and Its Applications]].** Fisher geometry, dual affine connections, divergences, exponential families, and natural gradients.
6. **[[lee-2012-smooth-manifolds|Lee, Introduction to Smooth Manifolds]].** The smooth-manifold, tangent-bundle, differential-form, and Lie-action foundation.
7. **[[hall-2015-lie-groups|Hall, Lie Groups, Lie Algebras, and Representations]].** Matrix Lie groups, exponential maps, BCH, Lie algebras, and basic representation theory.
8. **[[tu-2017-differential-geometry-connections-curvature|Tu, Differential Geometry]].** Bundles, connections, curvature, parallel transport, and characteristic classes.
9. **[[bhatia-2007-positive-definite-matrices|Bhatia, Positive Definite Matrices]].** Congruence actions, SPD metrics, matrix means, and covariance geometry.
10. **[[naber-2011-topology-geometry-gauge-fields-foundations|Naber, Topology, Geometry and Gauge Fields: Foundations]].** The explicit bridge from bundle geometry to gauge-field practice.
11. **[[boumal-2023-optimization-smooth-manifolds|Boumal, An Introduction to Optimization on Smooth Manifolds]].** Riemannian gradients, retractions, Hessians, and implementable manifold optimization.
12. **[[trefethen-bau-1997-numerical-linear-algebra|Trefethen and Bau, Numerical Linear Algebra]].** Conditioning, factorizations, stable solves, and eigenproblems.
13. **[[higham-2008-functions-of-matrices|Higham, Functions of Matrices]].** Reliable exponentials, logarithms, roots, Fréchet derivatives, and conditioning.

Ranks 1–13 form the defensible state-level ELBO, gauge, SPD, and optimization core. Klenke may be used as a reference by readers who already have graduate measure-theoretic probability.

## High-value companions and dynamic specialization

14. **[[mackay-2003-information-theory-inference-learning|MacKay, Information Theory, Inference, and Learning Algorithms]].** The most intuitive bridge among information theory, Bayesian inference, variational methods, and statistical mechanics.
15. **[[sethna-2021-statistical-mechanics|Sethna, Statistical Mechanics]].** Gibbs ensembles, free energies, order parameters, phase structure, emergence, and introductory RG.
16. **[[sarkka-svensson-2023-bayesian-filtering-smoothing|Särkkä and Svensson, Bayesian Filtering and Smoothing]].** Structured temporal inference, filtering, smoothing, and state-space models.

## Conditional extensions

17. **[[parr-2022-active-inference|Parr, Pezzulo, and Friston, Active Inference]].** Required for perception–action, policy, expected-free-energy, or process-theory claims, not for an ordinary ELBO.
18. **[[fulton-harris-1991-representation-theory|Fulton and Harris, Representation Theory]].** Required for systematic irreducible decomposition, tensor products, characters, and Clebsch–Gordan machinery.
19. **[[cardy-1996-scaling-renormalization|Cardy, Scaling and Renormalization in Statistical Physics]].** Required before treating population aggregation as a genuine RG transformation.
20. **[[calzetta-hu-2022-nonequilibrium-quantum-field-theory|Calzetta and Hu, Nonequilibrium Quantum Field Theory]].** Specialized preparation for a genuine 2PI effective-action extension.

> [!warning] Scope boundary
> [[Evidence lower bound (ELBO)|An ELBO]], [[Active Inference|active inference]], a configuration Gibbs distribution, a 1PI/2PI effective action, and an [[Renormalization group flow|RG flow]] are related constructions but are not interchangeable. The final four books should not be presented as prerequisites for the basic gauge-covariant Gaussian ELBO.

## Suggested reading order

Use Klenke first if measure-theoretic probability is not already secure. Then read Murphy's introduction, Boyd–Vandenberghe, and Wainwright–Jordan before beginning the geometry sequence Lee → Hall → Tu and Naber. Read Amari and Bhatia once both the probability and manifold prerequisites are in place, followed by Boumal, Trefethen–Bau, and Higham. Murphy's advanced volume and Särkkä–Svensson can then support structured and temporal inference. Sethna precedes Cardy; Parr, Fulton–Harris, and Calzetta–Hu belong only on the branch that uses their respective machinery.

## Acquisition status on 2026-07-19

The vault stores personal-use and author-hosted files only in the ignored `sources/pdfs/` cache. They are not public Git artifacts. “Metadata only” means that no freely authorized complete PDF was found in the source audit; it does not rule out access through the user's institutional subscriptions.

| Source | Vault status |
|---|---|
| [[murphy-2022-probabilistic-machine-learning-introduction]] | Complete author draft, CC BY-NC-ND: `sources/pdfs/murphy-2022-pml-introduction-author-draft.pdf` |
| [[murphy-2023-probabilistic-machine-learning-advanced-topics]] | Complete author draft, CC BY-NC-ND: `sources/pdfs/murphy-2023-pml-advanced-topics-author-draft.pdf` |
| [[wainwright-2008-graphical-models-variational]] | Complete author-hosted monograph: `sources/pdfs/wainwright-jordan-2008-graphical-models-variational-inference.pdf` |
| [[boyd-vandenberghe-2004-convex-optimization]] | Complete author-hosted book with publisher permission: `sources/pdfs/boyd-vandenberghe-2004-convex-optimization.pdf` |
| [[klenke-2020-probability-theory]] | Metadata/subscription access only |
| [[amari-2016-information-geometry-applications]] | Metadata/subscription access only |
| [[lee-2012-smooth-manifolds]] | Authorized front matter and Chapter 1: `sources/pdfs/lee-2012-smooth-manifolds-front-matter.pdf`, `sources/pdfs/lee-2012-smooth-manifolds-chapter-1.pdf` |
| [[hall-2015-lie-groups]] | Metadata and author supplements only; the public first-edition predecessor was not substituted for the ranked second edition |
| [[tu-2017-differential-geometry-connections-curvature]] | Metadata/subscription access only |
| [[bhatia-2007-positive-definite-matrices]] | Authorized sample: `sources/pdfs/bhatia-2007-positive-definite-matrices-sample.pdf` |
| [[naber-2011-topology-geometry-gauge-fields-foundations]] | Metadata/subscription access only |
| [[boumal-2023-optimization-smooth-manifolds]] | Complete author prepublication version for personal use: `sources/pdfs/boumal-2023-optimization-smooth-manifolds-prepublication.pdf` |
| [[trefethen-bau-1997-numerical-linear-algebra]] | Publisher metadata; the publisher's front-matter endpoint rejected automated acquisition |
| [[higham-2008-functions-of-matrices]] | Authorized Chapter 5 sample: `sources/pdfs/higham-2008-functions-of-matrices-chapter-5-sample.pdf` |
| [[mackay-2003-information-theory-inference-learning]] | Complete author-hosted book for personal use: `sources/pdfs/mackay-2003-information-theory-inference-learning.pdf` |
| [[sethna-2021-statistical-mechanics]] | Complete author-hosted second edition: `sources/pdfs/sethna-2021-statistical-mechanics-2e.pdf` |
| [[sarkka-svensson-2023-bayesian-filtering-smoothing]] | Complete author prepublication version for personal use: `sources/pdfs/sarkka-svensson-2023-bayesian-filtering-smoothing-prepublication.pdf` |
| [[parr-2022-active-inference]] | Complete MIT Press OA edition exists under CC BY-NC-ND, but the publisher endpoint returned HTTP 403 to automated acquisition; official OA link retained in the source note |
| [[fulton-harris-1991-representation-theory]] | Metadata/subscription access only |
| [[cardy-1996-scaling-renormalization]] | Metadata and author supplements only |
| [[calzetta-hu-2022-nonequilibrium-quantum-field-theory]] | Complete Cambridge OA reissue, CC BY-NC-ND: `sources/pdfs/calzetta-hu-2022-nonequilibrium-quantum-field-theory-open-access.pdf` |

## Related synthesis

- [[Variational free energy and predictive coding]]
- [[Inference machinery — variational EM and filtering]]
- [[Information geometry and natural gradient]]
- [[SPD-manifold geometry and Riemannian optimization]]
- [[Gauge equivariance and geometric deep learning]]
- [[Statistical physics of social systems and collective behavior]]
