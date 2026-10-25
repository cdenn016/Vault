---
type: paper
title: "Variational Learning for Switching State-Space Models"
aliases:
  - Ghahramani 2000
  - ghahramani2000variational
  - Switching state-space model
authors:
  - Ghahramani, Zoubin
  - Hinton, Geoffrey E.
year: 2000
url: https://doi.org/10.1162/089976600300015619
pdf: sources/pdfs/ghahramani-2000-switching-state-space.pdf
tags:
  - cluster/vfe
  - project/transformer
  - field/cs-ml
  - field/statistics
created: 2026-10-24
---

# Variational Learning for Switching State-Space Models

> [!info] Citation
> Ghahramani, Z., & Hinton, G. E. (2000). *Variational learning for switching state-space models*. Neural Computation, 12(4), 831–864. doi:10.1162/089976600300015619. The local PDF is the author-hosted version from Hinton's Toronto page, described there as an extension of technical report CRG-TR-96-3.

## TL;DR
A discrete switch variable that evolves as a Markov chain selects which of several linear-Gaussian dynamical systems generates the observations at each time. Exact inference is intractable because the posterior is a mixture over exponentially many switch histories, so the paper uses a structured variational approximation that decouples the switch chain from the continuous chains and alternates hidden-Markov forward–backward recursions with Kalman smoothing.

## Method
The model generalizes both hidden Markov models and linear dynamical systems. The structured variational posterior keeps the temporal structure of each part and couples them through variational parameters, which play the role of soft switch responsibilities in the Kalman recursions and of pseudo-likelihoods in the forward–backward pass. The lower bound on the log likelihood is maximized by EM. Experiments use artificial data and respiration data from a sleep-apnea patient.

> [!note] Editorial: The local PDF uses bitmap fonts and does not yield extractable text; the summary is based on the abstract on the author's page and the published record. Equation-level claims should be checked against the PDF pages directly.

## Relevance to this research
This is the generative model behind carrying a model belief through depth. If a token's template label at layer $\ell$ is a switch and the next layer's label follows a transition kernel $T^\ell$, the label belief becomes a persistent state whose prior at layer $\ell+1$ is $T^\ell s^\ell$, the switching analogue of the current per-layer label posterior. The paper also shows the cost: the joint label/content posterior is a growing mixture, and a tractable method must state which coupling it drops ([[Template routing]], [[Hierarchical generative model]]).

## Cross-links
- Themes: [[Inference machinery — variational EM and filtering]]
- Concepts: [[Hierarchical generative model]]
- Related sources: [[minka-2001-expectation-propagation]], [[ghahramani-1994-incomplete-data-em]]

## BibTeX
```bibtex
@article{ghahramani2000variational,
  author  = {Ghahramani, Zoubin and Hinton, Geoffrey E.},
  title   = {Variational Learning for Switching State-Space Models},
  journal = {Neural Computation},
  volume  = {12},
  number  = {4},
  pages   = {831--864},
  year    = {2000},
  doi     = {10.1162/089976600300015619}
}
```
