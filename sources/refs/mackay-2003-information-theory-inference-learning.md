---
type: reference
title: "Information Theory, Inference, and Learning Algorithms"
aliases:
  - "MacKay 2003"
  - "ITILA"
authors:
  - David J. C. MacKay
year: 2003
url: https://www.inference.org.uk/itila/
tags:
  - cluster/vfe
  - cluster/info-geometry
  - cluster/multi-agent
  - project/transformer
  - project/multi-agent
  - field/cs-ml
  - field/statistics
  - field/physics
created: 2026-07-19
updated: 2026-07-19
---

# Information Theory, Inference, and Learning Algorithms

> [!info] Citation
> David J. C. MacKay (2003). *Information Theory, Inference, and Learning Algorithms*. Cambridge University Press. ISBN 978-0-521-64298-9.

## TL;DR

MacKay provides an unusually coherent conceptual bridge among information theory, Bayesian inference, coding, graphical models, Monte Carlo methods, variational approximations, neural learning, and statistical mechanics. The emphasis is on deriving algorithms from probability and information rather than presenting disconnected recipes.

## What it establishes

The book develops entropy, KL divergence, Bayesian model comparison, message passing, sampling, variational methods, and energy-based probabilistic models through worked examples and exercises. Its comparisons between inference algorithms make approximation assumptions visible and tie free-energy language to both coding and statistical physics.

## Relevance to this research

MacKay is a conceptual companion rather than a substitute for [[wainwright-2008-graphical-models-variational]], [[amari-2016-information-geometry-applications]], or rigorous geometry texts. It helps explain why message passing, variational bounds, entropy regularization, and statistical-mechanical free energies recur across the gauge-VFE program. It supports [[Variational free energy]], [[Information bottleneck]], [[Belief Propagation]], and [[Statistical physics of social systems and collective behavior]].

## Access

The [author's site](https://www.inference.org.uk/itila/) provides a complete PDF for personal reading under ordinary book copyright. A private local copy is stored at `sources/pdfs/mackay-2003-information-theory-inference-learning.pdf`; it must not be redistributed as a public repository artifact.

## Cross-links

- Concepts: [[Variational free energy]] · [[Information bottleneck]] · [[Belief Propagation]]
- Themes: [[Variational free energy and predictive coding]] · [[Information geometry and natural gradient]]
- Related sources: [[murphy-2022-probabilistic-machine-learning-introduction]] · [[wainwright-2008-graphical-models-variational]]

## BibTeX

```bibtex
@book{MacKay2003Information,
  author    = {David J. C. MacKay},
  title     = {Information Theory, Inference, and Learning Algorithms},
  publisher = {Cambridge University Press},
  address   = {Cambridge},
  year      = {2003},
  isbn      = {9780521642989},
  url       = {https://www.inference.org.uk/itila/}
}
```
