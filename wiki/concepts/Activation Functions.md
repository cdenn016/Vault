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
updated: 2026-10-02
---

# Activation Functions

Activation functions are the pointwise nonlinearities applied between linear layers of a neural network (ReLU, ELU, sigmoid, tanh, GELU, etc.); their shape governs gradient flow and the expressivity of the network. Smooth, non-monotone units such as the GELU — x·Φ(x), the default in modern transformers — outperform piecewise-linear ReLU by avoiding zero-gradient dead regions. Notably, the VFE transformer (V3) is a no-neural-network model in its pure path, deriving all capacity from iterative VFE minimization rather than MLP activations; activation functions enter only in optional hybrid baselines.

The SiLU $x\sigma(x)=x\,e^x/(e^x+e^0)$ ([[elfwing-2018-silu]]) is a two-option softmax competition, and GELU is close to $x\sigma(1.702x)$. [[Template routing]] (2026-09-27) uses this to replace the $M$ independent two-way competitions of a GELU MLP with one $M$-way softmax over learned Gaussian templates, derived from a mixture-prior free energy ([[dennis-2026-template-routing]]). The current vfe3 predictive stack does use a GELU block MLP by default, so the pure-path remark above describes the older no-MLP path rather than the evaluated architecture.

Gated-exponential reading. Since $x\sigma(x)=\exp(\log\sigma(x))\,x$, SiLU is the diagonal exponential self-link $\xi_k\mapsto\xi_ke^{a_k(\xi)}$ with generator $a=\log\sigma$, and GELU likewise with $\log\Phi$; every positive gate has this form ([[elfwing-2018-silu]], [[hendrycks2016gaussian]]). [[dennis-2026-link-origin]] uses this to place a gated MLP in the same group-valued language as the attention links, as a state-dependent site term. The note states plainly that this is a rewriting and not a derivation, because nothing fixes the generator, and that the function $\varphi=(e^z-1)/z$ of the exponential link is not an activation for a routing-independent generator, since it acts on weights. A routed self-link gives a different object, a bounded block gate $e^{\beta_{ii}^{(h)}}\in(1,e)$ that can amplify but never suppress or flip a head block; whether it should replace part of the block MLP is open and untrained. [[Template routing]] supplies one principle for a normalized gate.

## Related
[[Template routing]], [[Transformer Architecture]]

## Sources
[[dennis-2026-link-origin]], [[hendrycks2016gaussian]], [[elfwing-2018-silu]], [[ramachandran2018searching]], [[dennis-2026-template-routing]]
