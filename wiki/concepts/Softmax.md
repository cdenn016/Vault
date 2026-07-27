---
type: concept
title: "Softmax"
aliases:
  - "softmax function"
  - "softmax normalization"
tags:
  - cluster/attention
  - cluster/vfe
  - project/transformer
  - project/multi-agent
status: draft
created: 2026-06-21
updated: 2026-07-27
---

# Softmax

The softmax function maps a real vector to a probability simplex via exponentiation and normalization, sigma(z)_i = exp(z_i) / sum_j exp(z_j). In transformer attention it converts query-key scores into a normalized attention distribution over keys, and it is equivalently the Gibbs/Boltzmann distribution at unit temperature. Softmax attention is the operation that modern Hopfield networks and streaming-LLM caches reinterpret, and within the VFE program its temperature/precision weighting connects to Fisher-information-based precision.

## Temperature is not free in an exact probabilistic reading

A softmax at temperature $\tau\neq1$ is routinely treated as the unit-temperature rule with rescaled
logits. That is a fine engineering choice but is **not** the exact optimum of the same probabilistic
model. Recovering it exactly needs a separately normalized *tempered* model with components
$f^{(\tau)}=f^{1/\tau}/Z(\tau)$, and the component normalizers do not cancel under row normalization
unless they are source-independent. The general identity holds for any densities,

$$D_{\mathrm{KL}}\left(\rho\Vert f^{(\tau)}\right)=\tfrac1\tau D_{\mathrm{KL}}(\rho\Vert f)+\left(\tfrac1\tau-1\right)H(\rho)+\log Z(\tau),$$

where the entropy term is source-free and cancels while the normalizer survives. For Gaussian
components $f_{ij}=\mathcal N(m_{ij},S_{ij})$ the tempered component is $\mathcal N(m_{ij},\tau S_{ij})$
and the exact row carries an extra per-source logit $-\tfrac12(1-1/\tau)\log\det S_{ij}$, which for
$\tau>1$ discounts higher-volume components
([[magent-exact-elbo-whitepaper-2026-07-27-attention-derivation]], built on the standard
power-likelihood construction).

## Related
[[Mechanistic interpretability of attention]], [[Attention mechanisms — theory and positional structure]], [[Precision weighting|Precision-weighted attention]], [[GL(K) gauge-equivariant attention]], [[Entropic regularization]], [[Mean-Field Approximation]], [[Maximum entropy]]

## Sources
[[ramsauer2021hopfield]], [[xiao2024efficient-streaming-llm]], [[magent-exact-elbo-whitepaper-2026-07-27-attention-derivation]]
