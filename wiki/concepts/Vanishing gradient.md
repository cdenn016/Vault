---
type: concept
title: "Vanishing gradient"
aliases:
  - "Vanishing gradients"
  - "Vanishing gradient problem"
  - "Vanishing Gradient Problem"
  - "vanishinggradientproblem"
  - "exploding gradient problem"
tags:
  - cluster/attention
  - project/transformer
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Vanishing gradient

The vanishing gradient problem is the tendency of gradients to shrink exponentially as they backpropagate through many layers or time steps, stalling learning in deep or recurrent networks. Saturating nonlinearities and repeated multiplication by small Jacobian factors are the usual culprits. Architectural remedies that preserve a near-linear gradient path — residual connections, gating, and gated linear units (GLU) — mitigate it, which is why gating-based designs are relevant to the program's deep gauge-equivariant stacks.

## Related
[[Attention mechanisms — theory and positional structure]]

## Sources
[[dauphin-2017-gated-convnets]]
