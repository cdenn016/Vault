---
type: paper
title: "Variational Bayes naming game: decentralized multi-agent inference for symbol emergence"
aliases:
  - "Fukuoka et al. 2026 VBNG"
  - VBNG
authors:
  - Keita Fukuoka
  - Masatoshi Nagano
  - Tomoaki Nakamura
  - Akira Taniguchi
  - Tadahiro Taniguchi
year: 2026
arxiv: null
url: https://doi.org/10.1080/01691864.2026.2661967
tags:
  - cluster/multi-agent
  - cluster/vfe
  - project/multi-agent
  - field/cs-ml
created: 2026-08-10
---

# Variational Bayes naming game: decentralized multi-agent inference for symbol emergence

> [!info] Citation
> Fukuoka, K., Nagano, M., Nakamura, T., Taniguchi, A., & Taniguchi, T. (2026). Variational Bayes naming game: decentralized multi-agent inference for symbol emergence. *Advanced Robotics*, 40(9), 435-453. https://doi.org/10.1080/01691864.2026.2661967

## TL;DR

The Variational Bayes Naming Game (VBNG) is a decentralized variational-inference procedure for sharing discrete signs among three or more agents. In the paper's synthetic and patched-MNIST experiments, VBNG approaches a centralized variational-Bayes topline and is faster than the recursive Metropolis-Hastings naming-game comparator.

## Problem & setting

Each agent observes only its own incomplete view of an object, yet the population must infer a shared latent sign. A centralized multimodal model can combine all observations but violates decentralization; earlier sampling-based naming games are more expensive and were originally designed for dyads.

## Method

The authors decompose a categorical/multinomial latent-variable model across agents. Listener and speaker roles exchange discrete signs, while local variational-Bayes updates combine the communicated natural parameters. The method is evaluated against recursive Metropolis-Hastings naming games and a centralized VB topline on synthetic vectors and nine-agent patched MNIST.

## Key results

The article reports classification and agreement comparable to the centralized topline in its experiments, robustness when individual views are ambiguous, and convergence two to four times faster than the sampling comparator for tested populations of up to ten agents. These are empirical results for a specific shared-symbol model and chosen communication protocol; they do not establish exact decentralized inference for arbitrary correlated joint laws.

## Relevance to this research

VBNG is a concrete finite benchmark for [[Collective active inference]] and shared latent variables. Its local-message versus centralized-topline comparison could be reproduced against an exact finite posterior and ELBO. It should not be treated as an implementation already present in MultiAgentELBO or as proof that the repository's gauge-coupled recognition law decomposes into the VBNG protocol.

## Cross-links

- Concepts: [[Collective active inference]], [[Multi-agent variational free energy]], [[Belief Propagation]], [[Meta-agents and hierarchical emergence]]
- Related sources: [[hasenclever-2017-snep-posterior-server]]

## BibTeX

```bibtex
@article{fukuoka2026vbng,
  author  = {Fukuoka, Keita and Nagano, Masatoshi and Nakamura, Tomoaki and Taniguchi, Akira and Taniguchi, Tadahiro},
  title   = {Variational Bayes naming game: decentralized multi-agent inference for symbol emergence},
  journal = {Advanced Robotics},
  volume  = {40},
  number  = {9},
  pages   = {435--453},
  year    = {2026},
  doi     = {10.1080/01691864.2026.2661967}
}
```
