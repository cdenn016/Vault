---
type: paper
title: "Importance Weighted Autoencoders"
aliases:
  - "burda-2015-iwae"
  - "Importance Weighted Autoencoders"
  - "IWAE"
  - "Burda 2015"
  - "burda2015iwae"
authors:
  - "Burda, Yuri"
  - "Grosse, Roger"
  - "Salakhutdinov, Ruslan"
year: 2016
url: https://arxiv.org/abs/1509.00519
venue: "ICLR"
tags:
  - cluster/vfe
  - project/transformer
  - field/cs-ml
  - field/statistics
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Importance Weighted Autoencoders

> [!info] Citation
> Burda, Yuri, Grosse, Roger, Salakhutdinov, Ruslan (2016). "Importance Weighted Autoencoders." *International Conference on Learning Representations (ICLR) 2016*. First posted as arXiv:1509.00519 (2015). https://arxiv.org/abs/1509.00519

## TL;DR
Introduces a tighter, importance-sampling-based lower bound on the marginal likelihood (the IWAE bound) for variational autoencoders, using k weighted posterior samples. As k grows the bound becomes tighter than the standard ELBO, yielding richer approximate posteriors and better generative models.

## Relevance to this research
Directly sharpens the variational free-energy bound at the heart of the program: the IWAE bound is a tighter surrogate for the ELBO/VFE, relevant to how accurately the model's Gaussian beliefs approximate true posteriors.

## Cross-links
[[Variational free energy]], [[Variational autoencoder (VAE)|Variational autoencoder]], [[Amortized inference]]

## BibTeX
```bibtex
@inproceedings{burda2015iwae,
  title={Importance Weighted Autoencoders},
  author={Burda, Yuri and Grosse, Roger and Salakhutdinov, Ruslan},
  booktitle={International Conference on Learning Representations (ICLR)},
  year={2016},
  note={arXiv:1509.00519}
}
```
