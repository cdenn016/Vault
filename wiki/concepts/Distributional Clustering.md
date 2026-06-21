---
type: concept
title: "Distributional Clustering"
aliases:
  - "distributionalclustering"
tags:
  - cluster/info-geometry
  - cluster/cs-ml
  - cluster/methodology
  - project/transformer
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Distributional Clustering

Distributional clustering groups objects by the similarity of their associated conditional probability distributions rather than by feature vectors, merging objects whose conditional distributions over some relevance variable are close (typically in KL or Jensen-Shannon divergence). It is the conceptual core of the information-bottleneck family: clusters are chosen to preserve mutual information with the relevance variable while compressing the input. In the program it connects to information-theoretic coarse-graining and the formation of meta-agents by grouping units with similar predictive/belief distributions.

## Related
[[Information bottleneck]], [[Jensen-Shannon Divergence]], [[Deterministic Annealing]], [[Meta-agents and hierarchical emergence]]

## Sources
[[slonim-2000-agglomerative-ib]]
