---
type: paper
title: "On the Natural Gradient of the Evidence Lower Bound"
aliases:
  - "Ay et al. 2025 natural gradient ELBO"
authors:
  - Nihat Ay
  - Jesse van Oostrum
  - Adwait Datar
year: 2025
arxiv: 2307.11249
url: https://jmlr.org/papers/v26/24-0606.html
tags:
  - cluster/info-geometry
  - cluster/vfe
  - project/transformer
  - project/multi-agent
  - field/mathematics
  - field/statistics
  - field/cs-ml
created: 2026-08-10
---

# On the Natural Gradient of the Evidence Lower Bound

> [!info] Citation
> Ay, N., van Oostrum, J., & Datar, A. (2025). On the Natural Gradient of the Evidence Lower Bound. *Journal of Machine Learning Research*, 26(222), 1-37. https://jmlr.org/papers/v26/24-0606.html

## TL;DR

Ay, van Oostrum, and Datar compare the Fisher-Rao gradient of an ELBO with the natural gradient of the target-distribution KL objective. In the unconstrained ambient distribution space, the variational gap contributes essentially no natural-gradient component to the visible-law objective. After restriction to a statistical model, that equivalence can fail; the paper gives a sufficient geometric condition, formalized as a cylindrical model, under which it is preserved.

## Problem & setting

The learning target is a distribution on visible variables, while a latent-variable model and its ELBO live on a larger joint space. Ordinary scalar ELBO identities do not by themselves imply that their projected natural-gradient vector fields agree after optimization is restricted to a model family. The paper asks when maximizing the constrained ELBO follows the same Fisher-Rao direction as minimizing KL from the target visible distribution.

## Method

The authors study the marginalization map from joint visible-hidden laws to visible laws using information geometry. They separate the ambient-space relation from the constrained-model relation and introduce cylindrical models to express a compatibility between tangent directions along the marginal fibers and directions that change the visible marginal.

## Key results

The ambient ELBO and target-KL objectives induce the same relevant natural-gradient field in the paper's setting. Under model restriction, the paper provides a sufficient cylindrical-model condition for this equivalence to persist. This is not a claim that every latent, structured, gauge-constrained, or coarse recognition family is cylindrical, nor is it a generic convergence theorem for natural-gradient optimization.

## Relevance to this research

The result sharpens the distinction between a scalar [[Evidence lower bound (ELBO)|ELBO]] identity and a projected [[Natural gradient]] identity. Any proposed structured or coarse [[Recognition Density|recognition family]] in the gauge-VFE program must establish the required tangent compatibility before treating ELBO natural-gradient flow as interchangeable with target-KL flow. The condition is especially relevant near the nonidentifiable strata collected in [[Singular statistical models]], where regular Fisher projections may not exist.

## Cross-links

- Concepts: [[Natural gradient]], [[Evidence lower bound (ELBO)]], [[Recognition Density]], [[Statistical manifold]], [[Singular statistical models]]
- Related sources: [[amari-1998-natural-gradient]]

## BibTeX

```bibtex
@article{ay2025naturalgradientelbo,
  author  = {Ay, Nihat and van Oostrum, Jesse and Datar, Adwait},
  title   = {On the Natural Gradient of the Evidence Lower Bound},
  journal = {Journal of Machine Learning Research},
  volume  = {26},
  number  = {222},
  pages   = {1--37},
  year    = {2025},
  url     = {https://jmlr.org/papers/v26/24-0606.html}
}
```
