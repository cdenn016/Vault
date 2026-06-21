---
type: concept
title: "Energy-Based Models"
tags:
  - cluster/attention
  - project/transformer
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Energy-Based Models

Energy-based models (EBMs) specify a scalar energy function E(x) over configurations whose minima are the preferred (high-probability) states, with a Gibbs distribution p(x) proportional to exp(-E(x)) tying low energy to high likelihood. Inference and retrieval proceed by descending the energy landscape; learning shapes the landscape so data lie at minima. Hopfield networks are the canonical EBM for associative memory, and the modern continuous-state energy E = -lse(beta, X^T xi) + (1/2)||xi||^2 yields softmax attention as its minimization step. EBM structure parallels the VFE free-energy functional, where the variational free energy plays the role of an energy whose minimization pins beliefs to priors while permitting soft retrieval from coupled states.

## Related
[[Associative Memory]], [[Variational Free Energy]], [[Attention Mechanism]]

## Sources
[[ramsauer2021hopfield]]
