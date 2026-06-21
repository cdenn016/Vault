---
type: concept
title: "Contrastive learning"
aliases:
  - "contrastivelearning"
tags:
  - cluster/attention
  - cluster/vfe
  - project/transformer
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Contrastive learning

Contrastive learning is a self-supervised representation-learning paradigm that pulls together representations of positive (similar) pairs while pushing apart negative (dissimilar) pairs, typically via an InfoNCE-style objective that lower-bounds mutual information. It learns useful embeddings without labels and connects to free-energy/predictive-coding objectives: Hinton's forward-forward algorithm replaces backprop with a contrastive comparison of positive (real) versus negative (fabricated) data, a layer-local goodness criterion reminiscent of energy-based and Boltzmann-machine learning.

## Related
[[Variational free energy]], [[Predictive coding]]

## Sources
[[hinton-2022-forward-forward]]
