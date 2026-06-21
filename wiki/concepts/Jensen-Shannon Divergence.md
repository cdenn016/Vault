---
type: concept
title: "Jensen-Shannon Divergence"
aliases:
  - "Jensen–Shannon divergence"
  - "JSD"
  - "jensenshannondivergence"
tags:
  - cluster/info-geometry
  - cluster/methodology
  - project/transformer
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Jensen-Shannon Divergence

The Jensen-Shannon divergence is a symmetrized, smoothed measure of dissimilarity between two probability distributions: the average KL divergence of each distribution from their mixture, equal to the mutual information between the source label and the sample. Unlike the KL divergence it is symmetric, always finite, and its square root is a metric. It appears as the natural merge cost in agglomerative information-bottleneck and distributional clustering, where merging two clusters incurs a (weighted) JS-divergence penalty between their conditional distributions.

## Related
[[Information bottleneck]], [[Information bottleneck|Distributional Clustering]], [[Variational free energy]]

## Sources
[[slonim-2000-agglomerative-ib]]
