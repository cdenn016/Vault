---
type: concept
title: "Energy-Based Models"
tags:
  - cluster/attention
  - project/transformer
status: stub
created: 2026-06-21
updated: 2026-10-06
---

# Energy-Based Models

Energy-based models (EBMs) specify a scalar energy function E(x) over configurations whose minima are the preferred (high-probability) states, with a Gibbs distribution p(x) proportional to exp(-E(x)) tying low energy to high likelihood. Inference and retrieval proceed by descending the energy landscape; learning shapes the landscape so data lie at minima. Hopfield networks are the canonical EBM for associative memory, and the modern continuous-state energy E = -lse(beta, X^T xi) + (1/2)||xi||^2 yields softmax attention as its minimization step. EBM structure parallels the VFE free-energy functional, where the variational free energy plays the role of an energy whose minimization pins beliefs to priors while permitting soft retrieval from coupled states.

Two transformer papers turn the energy view into whole layers. [[hoover-2023-energy-transformer]] chooses an energy over layer-normalized tokens, a log-sum-exp attention term plus a Hopfield term over learned memories, and uses its gradient flow as a recurrent transformer block whose energy provably decreases. [[yang-2022-transformers-optimization-perspective]] instead seeks an energy whose descent steps reproduce a given transformer layer and finds one up to symmetric, depth-shared weights; it states that its energy explains the forward pass and is not an energy-based model over inputs and outputs in the sense of joint-space EBMs. [[yu-2023-white-box-transformers-sparse-rate-reduction]] uses a coding-rate objective rather than an energy in this sense, but its layers are likewise descent steps.

## Related
[[Associative Memory]], [[Variational Free Energy]], [[Attention Mechanism]]

## Sources
[[ramsauer2021hopfield]], [[hoover-2023-energy-transformer]], [[yang-2022-transformers-optimization-perspective]], [[yu-2023-white-box-transformers-sparse-rate-reduction]]
