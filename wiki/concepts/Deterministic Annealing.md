---
type: concept
title: "Deterministic Annealing"
aliases:
  - "deterministicannealing"
tags:
  - cluster/info-geometry
  - cluster/methodology
  - project/transformer
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Deterministic Annealing

Deterministic annealing is an optimization strategy for clustering and rate-distortion / information-bottleneck problems that introduces a temperature (Lagrange) parameter and solves a sequence of free-energy minimizations from high to low temperature, tracking a smooth path of soft assignments and undergoing phase-transition-like cluster splits as the temperature drops. It avoids many local minima of hard clustering by deterministically optimizing an entropy-regularized objective instead of stochastically sampling. It links the information-bottleneck objective to a statistical-mechanics free energy, resonating with the program's free-energy and renormalization/coarse-graining framing.

## Related
[[Information bottleneck]], [[Information bottleneck|Distributional Clustering]], [[Variational free energy]], [[Meta-entropy]]

## Sources
[[slonim-2000-agglomerative-ib]]
