---
type: reference
title: "Ladder Variational Autoencoders"
aliases:
  - "Sønderby et al. 2016"
  - "Ladder VAE"
authors:
  - Casper Kaae Sønderby
  - Tapani Raiko
  - Lars Maaløe
  - Søren Kaae Sønderby
  - Ole Winther
year: 2016
arxiv: "1602.02282"
url: https://arxiv.org/abs/1602.02282
tags:
  - cluster/vfe
  - project/transformer
  - project/multi-agent
  - field/cs-ml
  - field/statistics
created: 2026-06-19
updated: 2026-06-19
---

# Ladder Variational Autoencoders

> [!info] Citation
> Casper Kaae Sønderby, Tapani Raiko, Lars Maaløe, Søren Kaae Sønderby, and Ole Winther (2016). "Ladder Variational Autoencoders." *Advances in Neural Information Processing Systems* 29 (NeurIPS 2016). arXiv:1602.02282. <https://arxiv.org/abs/1602.02282>

## TL;DR

The Ladder VAE makes deep hierarchical variational autoencoders actually trainable. The key move is to compute the approximate posterior at each latent layer by **combining a bottom-up data-dependent signal with a top-down prior signal** through a precision-weighted (Gaussian) merge, instead of a purely bottom-up inference network. This couples inference and generation across layers and lets information from the deep, abstract latents inform the posterior at every level, yielding deeper, more useful hierarchies of latent variables than the standard VAE.

## What it establishes

- A precision-weighted combination of bottom-up likelihood and top-down prior to form each layer's approximate posterior (a Gaussian product of experts).
- Inference that shares parameters with and is informed by the generative top-down pass, enabling many active stochastic layers.
- Better likelihoods and more interpretable hierarchical latents than bottom-up-only VAEs.

## Why the project cites it

The Ladder VAE's top-down precision-weighted posterior is the conventional-deep-learning precedent for PIFB's ([[participatory-it-from-bit]]) **cross-scale shadow priors**. In the project's tower the prior of a scale-$s$ agent is its parent's belief transported down, $p_i^{(s)} = \Omega_{i,I}[q_I^{(s+1)}]$, so the deep (coarse) scale's belief informs the fine scale's posterior through a top-down pass — structurally the same idea as the ladder's top-down prior signal merged with bottom-up evidence. The Gaussian precision-weighted merge is exactly the operation PIFB performs with its Gaussian belief tuples and the self-coupling KL term $\alpha\,\mathrm{KL}(q_i\|p_i)$, which at the optimum balances bottom-up likelihood against the transported top-down prior. This grounds the shadow-prior construction in established hierarchical [[Variational free energy]] inference and connects to [[Iterative amortized inference]] (the E-step refining beliefs against a top-down prior) and to [[Meta-agents and hierarchical emergence]].

```bibtex
@inproceedings{sonderby2016ladder,
  title         = {Ladder Variational Autoencoders},
  author        = {S{\o}nderby, Casper Kaae and Raiko, Tapani and Maal{\o}e, Lars and
                   S{\o}nderby, S{\o}ren Kaae and Winther, Ole},
  booktitle     = {Advances in Neural Information Processing Systems 29 (NeurIPS)},
  year          = {2016},
  eprint        = {1602.02282},
  archivePrefix = {arXiv},
  primaryClass  = {stat.ML},
  url           = {https://arxiv.org/abs/1602.02282}
}
```
