---
type: paper
title: "Stochastic Backpropagation and Approximate Inference in Deep Generative Models"
aliases:
  - "rezende-2014-stochastic-backprop"
  - "rezende2014stochasticbackprop"
  - "Rezende et al. 2014"
authors:
  - "Rezende, Danilo Jimenez"
  - "Mohamed, Shakir"
  - "Wierstra, Daan"
year: 2014
url: https://arxiv.org/abs/1401.4082
venue: "ICML"
tags:
  - cluster/vfe
  - project/transformer
  - field/cs-ml
  - field/statistics
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Stochastic Backpropagation and Approximate Inference in Deep Generative Models

> [!info] Citation
> Rezende, Danilo Jimenez, Mohamed, Shakir, Wierstra, Daan (2014). "Stochastic Backpropagation and Approximate Inference in Deep Generative Models." ICML. https://arxiv.org/abs/1401.4082

## TL;DR
Introduces deep latent Gaussian models trained by stochastic backpropagation: a reparameterization of Gaussian latents that lets gradients flow through sampling, enabling scalable amortized variational inference. Developed concurrently with the VAE (Kingma & Welling 2014) and providing its complementary gradient-estimation foundation.

## Relevance to this research
A foundational reference for amortized variational inference and the reparameterization trick that underlie the VFE transformer's belief-inference machinery; pairs with the VAE method page and the sequential VRNN model (chung-2015) that cites it.

## Cross-links
[[Variational autoencoder (VAE)]], [[Variational free energy]], [[Amortized inference]]

## BibTeX
```bibtex
@inproceedings{rezende2014stochasticbackprop,
  author    = {Rezende, Danilo Jimenez and Mohamed, Shakir and Wierstra, Daan},
  title     = {Stochastic Backpropagation and Approximate Inference in Deep Generative Models},
  booktitle = {Proceedings of the 31st International Conference on Machine Learning (ICML)},
  pages     = {1278--1286},
  year      = {2014},
  eprint    = {1401.4082},
}
```
