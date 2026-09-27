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
updated: 2026-09-27
---

# Activation Functions

Activation functions are the pointwise nonlinearities applied between linear layers of a neural network (ReLU, ELU, sigmoid, tanh, GELU, etc.); their shape governs gradient flow and the expressivity of the network. Smooth, non-monotone units such as the GELU — x·Φ(x), the default in modern transformers — outperform piecewise-linear ReLU by avoiding zero-gradient dead regions. Notably, the VFE transformer (V3) is a no-neural-network model in its pure path, deriving all capacity from iterative VFE minimization rather than MLP activations; activation functions enter only in optional hybrid baselines.

The SiLU $x\sigma(x)=x\,e^x/(e^x+e^0)$ ([[elfwing-2018-silu]]) is a two-option softmax competition, and GELU is close to $x\sigma(1.702x)$. [[Template routing]] (2026-09-27) uses this to replace the $M$ independent two-way competitions of a GELU MLP with one $M$-way softmax over learned Gaussian templates, derived from a mixture-prior free energy ([[dennis-2026-template-routing]]). The current vfe3 predictive stack does use a GELU block MLP by default, so the pure-path remark above describes the older no-MLP path rather than the evaluated architecture.

## Related
[[Template routing]], [[Transformer Architecture]]

## Sources
[[hendrycks2016gaussian]], [[elfwing-2018-silu]], [[ramachandran2018searching]], [[dennis-2026-template-routing]]
