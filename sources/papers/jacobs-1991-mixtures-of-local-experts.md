---
type: paper
title: "Adaptive Mixtures of Local Experts"
aliases:
  - Jacobs 1991
  - jacobs1991
  - Mixture of experts
authors:
  - Jacobs, Robert A.
  - Jordan, Michael I.
  - Nowlan, Steven J.
  - Hinton, Geoffrey E.
year: 1991
url: https://doi.org/10.1162/neco.1991.3.1.79
tags:
  - cluster/attention
  - project/transformer
  - field/cs-ml
  - field/neuroscience
created: 2026-09-27
---

# Adaptive Mixtures of Local Experts

> [!info] Citation
> Jacobs, R. A., Jordan, M. I., Nowlan, S. J., & Hinton, G. E. (1991). *Adaptive mixtures of local experts*. Neural Computation, 3(1), 79–87. doi:10.1162/neco.1991.3.1.79.

## TL;DR
A supervised system is built from several expert networks and a gating network. The gate assigns each input a softmax distribution over experts, and training under a mixture likelihood makes the experts specialize to subsets of the input space rather than cooperate on every case.

## Method
Output density $p(y\mid x)=\sum_a g_a(x)\,p_a(y\mid x)$ with softmax gates $g_a$; the error function is the negative log of this mixture likelihood, which induces competition among experts.

## Key results
The experts partition the task (a vowel-discrimination task in the paper) and the system learns faster than a single back-propagation network of comparable size.

## Relevance to this research
A softmax-gated combination of local experts is the structure of the [[Template routing]] block: the gates are KL responsibilities to Gaussian templates, and with regression blocks $B_a\neq0$ each template is a local linear expert (see [[ghahramani-1994-incomplete-data-em]]). The competitive, one-expert-explains-the-input character of softmax gating is the modeling statement that distinguishes template routing from independently gated MLP units.

## Cross-links
- Concepts: [[Gating Mechanisms]], [[Softmax]]
- Methods: [[Template routing]]
- Related sources: [[ghahramani-1994-incomplete-data-em]], [[hinton-2002-products-of-experts]], [[dennis-2026-template-routing]]

## BibTeX
```bibtex
@article{jacobs1991adaptive,
  author  = {Jacobs, Robert A. and Jordan, Michael I. and Nowlan, Steven J. and Hinton, Geoffrey E.},
  title   = {Adaptive Mixtures of Local Experts},
  journal = {Neural Computation},
  volume  = {3},
  number  = {1},
  pages   = {79--87},
  year    = {1991},
  doi     = {10.1162/neco.1991.3.1.79}
}
```
