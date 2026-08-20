---
type: paper
title: "Federated Generalised Variational Inference: A Robust Probabilistic Federated Learning Framework"
aliases:
  - "Mildner et al. 2025 FedGVI"
  - "Federated generalized variational inference"
authors:
  - Mildner, Terje
  - Hamelijnck, Oliver
  - Giampouras, Paris
  - Damoulas, Theodoros
year: 2025
arxiv: null
url: https://proceedings.mlr.press/v267/mildner25a.html
tags:
  - cluster/vfe
  - cluster/multi-agent
  - cluster/info-geometry
  - project/multi-agent
  - field/cs-ml
  - field/statistics
created: 2026-08-20
---

# Federated Generalised Variational Inference: A Robust Probabilistic Federated Learning Framework

> [!info] Citation
> Terje Mildner, Oliver Hamelijnck, Paris Giampouras, and Theodoros Damoulas (2025). "Federated Generalised Variational Inference: A Robust Probabilistic Federated Learning Framework." *Proceedings of the 42nd International Conference on Machine Learning*, PMLR **267**, 44134--44174. https://proceedings.mlr.press/v267/mildner25a.html

## TL;DR

FedGVI generalizes PVI by allowing robust local losses and divergence choices designed for prior and likelihood misspecification. The paper analyzes fixed points, cavity optimality, and robustness, and reports improved calibration and predictive performance under misspecification.

## Problem & setting

Probabilistic federated learning inherits model-misspecification problems from ordinary Bayes and additional heterogeneity across clients. Standard PVI uses a Bayesian KL-based objective whose robustness can degrade when local likelihoods are wrong.

## Method

Generalized variational inference replaces the log-likelihood and KL components with robust losses and divergences while preserving partitioned site updates. Conjugate update options reduce client cost, and the paper studies fixed-point convergence and cavity distributions.

## Key results

The authors provide theoretical robustness results and empirical gains on synthetic and real classification data. The framework changes the inferential target intentionally; robustness under misspecification is not evidence of exact recovery of the ordinary Bayesian posterior.

## Relevance to this research

FedGVI gives a disciplined route for testing alternatives to the KL sector in [[Multi-agent variational free energy]]. Any use of alpha or robust divergences should state whether the project is approximating the original Bayes posterior or defining a generalized posterior. Gauge invariance and statistical robustness are independent requirements.

## Cross-links

- Concepts: [[Decentralized Bayesian inference]], [[Alpha-divergence]], [[Approximate Bayesian inference]]
- Related sources: [[ashman-2022-partitioned-variational-inference]], [[heikkila-2023-dp-partitioned-vi]]
- Project: [[Gauge-Theoretic Multi-Agent VFE Model]]

## BibTeX

```bibtex
@inproceedings{MildnerEtAl2025FedGVI,
  author    = {Mildner, Terje and Hamelijnck, Oliver and Giampouras, Paris and Damoulas, Theodoros},
  title     = {Federated Generalised Variational Inference: A Robust Probabilistic Federated Learning Framework},
  booktitle = {Proceedings of the 42nd International Conference on Machine Learning},
  series    = {Proceedings of Machine Learning Research},
  volume    = {267},
  pages     = {44134--44174},
  year      = {2025},
  publisher = {PMLR},
  url       = {https://proceedings.mlr.press/v267/mildner25a.html}
}
```
