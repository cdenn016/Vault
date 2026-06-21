---
type: paper
title: "Weight Uncertainty in Neural Networks"
aliases:
  - "blundell2015weight"
  - "Bayes by Backprop"
  - "Weight Uncertainty in Neural Networks"
authors:
  - "Blundell, Charles"
  - "Cornebise, Julien"
  - "Kavukcuoglu, Koray"
  - "Wierstra, Daan"
year: 2015
url: https://arxiv.org/abs/1505.05424
venue: "ICML 2015 (PMLR)"
tags:
  - cluster/vfe
  - cluster/info-geometry
  - project/transformer
  - field/cs-ml
  - field/statistics
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Weight Uncertainty in Neural Networks

> [!info] Citation
> Blundell, Charles, Cornebise, Julien, Kavukcuoglu, Koray, Wierstra, Daan (2015). "Weight Uncertainty in Neural Networks." ICML 2015 (PMLR). https://arxiv.org/abs/1505.05424

## TL;DR
Introduces Bayes by Backprop, a backpropagation-compatible algorithm for learning a probability distribution over the weights of a neural network. It uses a variational approximation to the posterior over weights with a reparameterization-style unbiased gradient estimator, yielding calibrated uncertainty and a regularization effect that competes with dropout.

## Relevance to this research
A foundational Bayesian-deep-learning method that frames weight learning as variational inference; it sits alongside Gal & Ghahramani's dropout-as-Bayesian view and exemplifies the variational-free-energy minimization at the core of the VFE transformer program.

## Cross-links
[[Approximate Bayesian inference]], [[Variational free energy]], [[Amortized inference]]

## BibTeX
```bibtex
@inproceedings{blundell2015weight,
  title={Weight Uncertainty in Neural Networks},
  author={Blundell, Charles and Cornebise, Julien and Kavukcuoglu, Koray and Wierstra, Daan},
  booktitle={Proceedings of the 32nd International Conference on Machine Learning (ICML)},
  series={PMLR},
  volume={37},
  pages={1613--1622},
  year={2015}
}
```
