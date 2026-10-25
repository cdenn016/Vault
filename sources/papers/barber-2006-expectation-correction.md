---
type: paper
title: "Expectation Correction for Smoothed Inference in Switching Linear Dynamical Systems"
aliases:
  - "Barber 2006"
  - "Expectation correction"
  - "Gaussian sum smoother"
authors:
  - "Barber, David"
year: 2006
url: https://www.jmlr.org/papers/v7/barber06a.html
pdf: sources/pdfs/barber-2006-expectation-correction.pdf
tags:
  - cluster/vfe
  - project/transformer
  - field/cs-ml
  - field/statistics
created: 2026-10-25
---

# Expectation Correction for Smoothed Inference in Switching Linear Dynamical Systems

> [!info] Citation
> Barber, D. (2006). *Expectation correction for smoothed inference in switching linear dynamical systems*. Journal of Machine Learning Research, 7, 2515–2540. The local PDF is from JMLR.

## TL;DR
Smoothing in a switching linear dynamical system is intractable because the posterior over the continuous state is a mixture whose size grows exponentially with time. Expectation correction is a Gaussian-sum smoother: an assumed-density forward pass keeps a fixed number of Gaussian components per switch state, and a single backward pass, modeled on the Rauch–Tung–Striebel correction, collapses the smoothed posterior back to a mixture. It drops one of the approximations of Kim's smoother and so uses more of the future information.

## Method
The forward pass propagates each component through each regime's linear-Gaussian dynamics, conditions on the observation, and collapses the $I_{t-1}\times S$ resulting components to $I_t$ (by merging low-weight components). The backward pass needs $p(s_t\mid s_{t+1},h_{t+1},v_{1:t})$, which is not Gaussian in $h_{t+1}$; an extra conditional-independence assumption gives a simpler variant. Switch transitions may depend on the continuous state.

## Relevance to this research
A candidate smoother for the switching linear-Gaussian stage recorded as future work in [[vfe3-2026-10-25-local-learner-test]] and in `VFE_3.0/TODO.md`: local EM on regime-weighted lag-one moments needs a smoothed mixture posterior, and the existing RTS window extends to the switching case through this construction. It is also the inference family of the discrete edge-link bank on the VFE roadmap.

## Cross-links
- Themes: [[Inference machinery — variational EM and filtering]]
- Methods: [[Variational EM]]
- Related sources: [[ghahramani-2000-switching-state-space]], [[minka-2001-expectation-propagation]], [[rauch-1965-rts-smoother]], [[vfe3-2026-10-25-local-learner-test]]

## BibTeX
```bibtex
@article{barber2006expectation,
  author  = {Barber, David},
  title   = {Expectation Correction for Smoothed Inference in Switching Linear Dynamical Systems},
  journal = {Journal of Machine Learning Research},
  volume  = {7},
  pages   = {2515--2540},
  year    = {2006}
}
```
