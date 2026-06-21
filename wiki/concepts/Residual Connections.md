---
type: concept
title: "Residual Connections"
aliases:
  - "residualconnections"
  - "Skip connections"
  - "Residual connection"
tags:
  - cluster/attention
  - project/transformer
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Residual Connections

Architectural shortcuts that add a layer's input to its output (y = x + F(x)), so that each block need only learn a residual correction. They stabilize gradients in very deep networks (mitigating vanishing/exploding gradients), make the identity the default behavior, and are a core ingredient of Transformers. They can be read as a discretized step of an underlying dynamical update, connecting depth to iterative refinement of representations/beliefs.

## Related
[[srivastava2015highway|Highway networks]], [[Gating Mechanisms]], [[Deep Networks]], [[Attention mechanisms — theory and positional structure]]

## Sources
[[srivastava2015highway]], [[he-2016-resnet|he2016resnet]]
