---
type: concept
title: "Central Limit Theorem"
aliases:
  - "centrallimittheorem"
  - "CLT"
tags:
  - cluster/info-geometry
  - cluster/methodology
  - project/transformer
  - project/multi-agent
status: stub
created: 2026-06-21
updated: 2026-09-26
---

# Central Limit Theorem

## Dependency-graph cumulants

For uniformly bounded random variables with a dependency graph, [[feray-2013-mod-phi-convergence-i-normality-zones-and-precise-deviations]] bounds joint cumulants by a spanning-tree count (Section 9.4.2, Eq. (47), arXiv v4 p. 78), yielding the sum-cumulant bounds of Theorems 9.7–9.8. A dependency graph requires independence of families separated by no edges, not merely small pairwise correlations. A particular limit theorem still needs its own normalization and variance hypotheses. The checked RG application is documented in [[multiagentelbo-2026-09-26-selection-and-reference-review]].


The central limit theorem states that the normalized sum of many independent (or weakly dependent) random variables converges in distribution to a Gaussian, regardless of the underlying distribution (given finite variance). In the renormalization-group reading (Jona-Lasinio), the Gaussian is the attractive fixed point of a coarse-graining transformation acting on probability distributions, and the CLT is the simplest instance of universality; non-Gaussian stable laws arise as other fixed points when variance diverges. This RG-on-probability picture motivates treating coarse-grained belief distributions as flowing toward fixed points.

## Related
[[Fixed Points]], [[Renormalization group flow|Renormalization group]]

## Sources
[[jona-lasinio-2001-renormalization-probability]]
