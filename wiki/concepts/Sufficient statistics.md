---
type: concept
title: "Sufficient statistics"
aliases:
  - "sufficient statistic"
  - "sufficiency"
  - "Sufficient Statistic"
tags:
  - cluster/info-geometry
  - cluster/vfe
  - project/transformer
  - project/multi-agent
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Sufficient statistics

A statistic T(X) is sufficient for a parameter theta if the conditional distribution of the data given T carries no further information about theta, equivalently (Fisher-Neyman) if the likelihood factorizes as p(x|theta) = h(x) g(T(x), theta). Sufficiency is the invariance principle underpinning information geometry: Chentsov's theorem shows the Fisher metric and the Amari-Chentsov tensor are the unique geometric structures invariant under sufficient statistics, and exponential families are exactly the models admitting finite-dimensional sufficient statistics (their natural parameters/expectation parameters being the dually flat coordinates used throughout the VFE program).

## Related
[[Fisher information metric]], [[Amari-Chentsov tensor]], [[Exponential family]], [[Information geometry and natural gradient]]

## Sources
[[ay2015-info-geometry-sufficient-statistics]]
