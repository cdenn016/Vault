---
type: paper
title: "Dropout: A Simple Way to Prevent Neural Networks from Overfitting"
aliases:
  - "Srivastava 2014"
  - "Dropout"
authors:
  - Srivastava, Nitish
  - Hinton, Geoffrey
  - Krizhevsky, Alex
  - Sutskever, Ilya
  - Salakhutdinov, Ruslan
year: 2014
arxiv: null
url: https://jmlr.org/papers/v15/srivastava14a.html
tags:
  - cluster/attention
  - project/transformer
  - field/cs-ml
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Dropout: A Simple Way to Prevent Neural Networks from Overfitting

> [!info] Citation
> Srivastava, N., Hinton, G., Krizhevsky, A., Sutskever, I., & Salakhutdinov, R. (2014). "Dropout: A Simple Way to Prevent Neural Networks from Overfitting." *Journal of Machine Learning Research*, 15(56), 1929–1958. https://jmlr.org/papers/v15/srivastava14a.html

## TL;DR

Dropout regularizes a neural network by randomly zeroing each unit with probability $1-p$ on every training step, so the network cannot rely on fixed co-adapted feature combinations. Training under this noise approximates sampling from an exponentially large ensemble of thinned subnetworks that share weights; at test time the full network with weights scaled by $p$ approximates averaging that ensemble. The technique reduced overfitting and set records on several supervised vision and speech benchmarks, and became a standard ingredient of the transformer block (residual and attention dropout).

## Problem & setting

Large neural networks trained on limited data overfit severely: units co-adapt to correct errors made by other units, creating brittle feature detectors that fail to generalize. Prior remedies — L2 regularization, early stopping, Bayesian model averaging — either require extensive tuning or are computationally intractable for deep nets. The paper asks whether a single, cheap, architecture-agnostic mechanism can provide the generalization benefit of ensemble averaging without the cost of training multiple models.

## Method

At each training step, each unit $i$ in a layer is independently retained with probability $p$ (the keep probability) and set to zero otherwise, giving a "thinned" network. Formally, for a unit with pre-activation $z_i$, the dropped output is $\tilde{y}_i = r_i \cdot y_i$ where $r_i \sim \text{Bernoulli}(p)$. Because each binary mask is sampled independently, a network with $n$ units implicitly trains $2^n$ parameter-sharing sub-networks simultaneously. At test time all units are active but their outgoing weights are multiplied by $p$, which approximates the geometric mean of the ensemble's predictions. The authors also describe an "inverted dropout" variant — scaling active units by $1/p$ at train time instead — which leaves test-time inference unchanged. A Bayesian motivation is offered: dropout can be interpreted as placing a mean-field approximate posterior over binary unit-selection variables, with the test-time weight scaling corresponding to the posterior mean under a Bernoulli prior.

## Key results

Dropout improved generalization over baseline networks without dropout on MNIST, CIFAR-10/100, SVHN, ImageNet (with convolutional nets), and TIMIT speech recognition, in each case matching or surpassing then-state-of-the-art regularized models. On MNIST the best dropout network achieved 0.95% error, compared to 1.60% for a comparable regularized net without dropout. The technique was shown to be complementary to max-norm weight constraints and to benefit from larger networks (dropout makes it cheaper to use more parameters by preventing co-adaptation). The ensemble-averaging interpretation was validated by showing that the geometric-mean approximation is accurate when sub-network predictions are near-independent.

## Relevance to this research

The VFE transformer is a no-neural-network model (all capacity comes from iterative free-energy minimization over Gaussian belief tuples $(mu, \Sigma, \phi)$), so it does not employ dropout as an architectural layer. The conventional-transformer baseline against which the VFE transformer is positioned — Vaswani-style blocks ([[vaswani-2017-attention]]) — applies residual and attention dropout as standard regularization furniture, making this paper part of the background context for comparing against that baseline. Conceptually, dropout's ensemble-averaging reading offers a loose but instructive contrast with the project's treatment of uncertainty: in the VFE framework, epistemic confidence is represented explicitly in the precision matrix $\Sigma^{-1}$ and propagated through the free-energy functional, whereas dropout injects multiplicative Bernoulli noise as a proxy for model uncertainty. The Bayesian interpretation of dropout (mean-field posterior over unit-selection masks) connects distantly to the variational inference foundations of the VFE hierarchy, but the correspondence is loose — dropout does not optimize an explicit ELBO over a structured latent space.

## Cross-links

- Concepts: [[Transformer interpretability and scaling]], [[Variational Free Energy]]
- Related sources: [[vaswani-2017-attention]], [[clark-2019-bert-attention]], [[dong-2021-rank-collapse]]
- Manuscript/Project: [[VFE Transformer Program]]

## BibTeX

```bibtex
@article{srivastava2014dropout,
  author  = {Srivastava, Nitish and Hinton, Geoffrey and Krizhevsky, Alex and
             Sutskever, Ilya and Salakhutdinov, Ruslan},
  title   = {Dropout: A Simple Way to Prevent Neural Networks from Overfitting},
  journal = {Journal of Machine Learning Research},
  volume  = {15},
  number  = {56},
  pages   = {1929--1958},
  year    = {2014},
  url     = {https://jmlr.org/papers/v15/srivastava14a.html}
}
```
