---
type: paper
title: "Emergent communication of multimodal deep generative models based on Metropolis-Hastings naming game"
aliases:
  - "Hoang et al. 2024 MH naming game"
authors:
  - Hoang, Nguyen Le
  - Taniguchi, Tadahiro
  - Hagiwara, Yoshinobu
  - Taniguchi, Akira
year: 2024
arxiv: null
url: https://doi.org/10.3389/frobt.2023.1290604
tags:
  - cluster/multi-agent
  - cluster/vfe
  - cluster/social-physics
  - cluster/social-physics/social-influence
  - project/multi-agent
  - project/social-physics
  - field/cs-ml
  - field/statistics
created: 2026-08-20
---

# Emergent communication of multimodal deep generative models based on Metropolis-Hastings naming game

> [!info] Citation
> Nguyen Le Hoang, Tadahiro Taniguchi, Yoshinobu Hagiwara, and Akira Taniguchi (2024). "Emergent communication of multimodal deep generative models based on Metropolis-Hastings naming game." *Frontiers in Robotics and AI* **10**, 1290604. https://doi.org/10.3389/frobt.2023.1290604

## TL;DR

Two agents combine multimodal variational autoencoders, mixture models, and a Metropolis--Hastings naming game to form perceptual categories and a shared vocabulary. The communication protocol has a declared generative model and MCMC interpretation, making it a concrete decentralized-inference comparator rather than a generic free-energy principle.

## Problem & setting

The agents observe corresponding objects through different modalities and must develop compatible internal categories and external signs without a centralized learner. Local latent representations and the shared word variable are jointly involved in inference.

## Method

Each agent uses a product-of-experts multimodal VAE and Gaussian mixture model. A speaker samples a word from its local posterior; a listener accepts or rejects it using a Metropolis--Hastings ratio and the agents alternate roles. This decomposes inference over the shared representation into local updates plus a communication step.

## Key results

Experiments on MNIST+SVHN and Multimodal165 report improved category formation, information sharing, and reconstruction relative to comparison systems. The result depends on the shared-data pairing, model factorization, and MH protocol; it is not an exact result for arbitrary networked beliefs.

## Relevance to this research

The method is a positive control for evidence-lineage-aware communication. The shared word has an explicit probabilistic role, unlike an untyped neighbor posterior. It also exposes discrete label alignment as a separate symmetry problem from gauge transport in [[Decentralized Bayesian inference]].

## Cross-links

- Concepts: [[Decentralized Bayesian inference]], [[Collective active inference]], [[Amortized inference]]
- Related sources: [[taniguchi-2024-collective-predictive-coding]], [[fukuoka-2026-variational-bayes-naming-game]]
- Project: [[Gauge-Theoretic Multi-Agent VFE Model]]

## BibTeX

```bibtex
@article{HoangEtAl2024EmergentCommunication,
  author  = {Hoang, Nguyen Le and Taniguchi, Tadahiro and Hagiwara, Yoshinobu and Taniguchi, Akira},
  title   = {Emergent communication of multimodal deep generative models based on Metropolis-Hastings naming game},
  journal = {Frontiers in Robotics and AI},
  volume  = {10},
  pages   = {1290604},
  year    = {2024},
  doi     = {10.3389/frobt.2023.1290604}
}
```
