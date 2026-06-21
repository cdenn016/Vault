---
type: concept
title: "Activation Functions"
aliases:
  - "Activation Function"
tags:
  - cluster/attention
  - project/transformer
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Activation Functions

Activation functions are the pointwise nonlinearities applied between linear layers of a neural network (ReLU, ELU, sigmoid, tanh, GELU, etc.); their shape governs gradient flow and the expressivity of the network. Smooth, non-monotone units such as the GELU — x·Φ(x), the default in modern transformers — outperform piecewise-linear ReLU by avoiding zero-gradient dead regions. Notably, the VFE transformer (V3) is a no-neural-network model in its pure path, deriving all capacity from iterative VFE minimization rather than MLP activations; activation functions enter only in optional hybrid baselines.

## Related
[[Transformer Architecture]]

## Sources
[[hendrycks2016gaussian]]
