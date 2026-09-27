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
updated: 2026-09-23
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
(built on the standard
power-likelihood construction).

There is a sharper way to say this when the components arise as Gaussian link factors
$\mathcal N(y_i;\Omega_{ij}y_j,R_{ij})$. **The temperature simply is the link-noise scale**:
$R_{ij}=cS_{ij}$ reproduces the tempered row exactly at $\tau=c$, log-determinant logit included. So a
softmax temperature is not a free knob layered on top of a probabilistic model; it is a statement about
how noisy the model declares its channels to be. Demanding that the row reduce to a clean divergence
score, as an identity in the unconstrained sender mean, forces $R_{ij}=\tau S_{ij}$ and then forces
$\tau=1$ — divergence scoring and unit temperature are the same requirement.

## Softmax as a regularized argmax and as a posterior (2026-09-23)

The softmax row maximizes a linear score plus an entropy term. [[niculae-2017-regularized-attention]] derives it as the gradient of a regularized max over the simplex, with sparsemax as the squared-norm counterpart, and [[litman-2025-entropic-optimal-transport-attention]] states the same fact as a one-sided entropic optimal-transport problem whose regularization weight is the temperature. With a KL divergence to a prior in place of the entropy the solution is $\operatorname{softmax}(s/\tau+\log\pi)$ ([[litman-2026-attention-priors]], Proposition 3.1), and the row stays within a factor $e^{\pm\omega_i}$ of its prior, where $\omega_i$ is the range of the scores (Theorem 5.1). A binary observation with likelihood $\exp(-D_{ij}/\tau)$, the optimality-variable device of control as inference ([[levine-2018-control-as-inference]], [[kappen-2012-optimal-control-inference]]), turns the same row into an exact posterior over source labels at every temperature. This is the reading the GL(K) attention manuscript adopts ([[GL(K) gauge-equivariant attention]]).

> [!note] Editorial: This does not conflict with the preceding section. There the temperature tempers the component densities of a fixed mixture, whose normalizers then survive. Here it sets the likelihood of a binary record, which is a valid probability for every $\tau>0$ because $D_{ij}\ge0$, so each temperature defines its own normalized model.

## Related
[[Mechanistic interpretability of attention]], [[Attention mechanisms — theory and positional structure]], [[Precision weighting|Precision-weighted attention]], [[GL(K) gauge-equivariant attention]], [[Entropic regularization]], [[Mean-Field Approximation]], [[Maximum entropy]]

## Sources
[[ramsauer2021hopfield]], [[xiao2024efficient-streaming-llm]], [[niculae-2017-regularized-attention]], [[litman-2025-entropic-optimal-transport-attention]], [[litman-2026-attention-priors]], [[levine-2018-control-as-inference]], [[kappen-2012-optimal-control-inference]]
