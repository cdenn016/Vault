---
type: paper
title: "Deep Kalman Filters"
aliases:
  - "krishnan2015deep"
  - "Krishnan 2015"
  - "Deep Kalman Filters"
authors:
  - "Krishnan, R. G."
  - "Shalit, U."
  - "Sontag, D."
year: 2015
url: https://arxiv.org/abs/1511.05121
venue: "arXiv preprint arXiv:1511.05121"
tags:
  - cluster/vfe
  - project/transformer
  - field/cs-ml
  - field/statistics
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Deep Kalman Filters

> [!info] Citation
> Krishnan, R. G., Shalit, U., Sontag, D. (2015). "Deep Kalman Filters." arXiv preprint arXiv:1511.05121. https://arxiv.org/abs/1511.05121

## TL;DR
Generalizes the linear-Gaussian Kalman filter by parameterizing the latent transition and emission distributions with deep neural networks, fitting the resulting deep generative state space model by amortized variational inference (a recognition network producing the approximate posterior over latent trajectories). Demonstrates learning nonlinear latent dynamics, including counterfactual reasoning about interventions.

## Relevance to this research
A precursor to structured deep state space models (krishnan2017structured) and sequential VAEs relevant to the VFE transformer program: it shows how variational free-energy minimization fits nonlinear latent-dynamics priors over sequences, the same machinery the program reuses for belief dynamics.

## Cross-links
[[State space models]], [[Variational free energy]], [[Amortized inference]]

## BibTeX
```bibtex
@article{krishnan2015deep,
  title={Deep Kalman Filters},
  author={Krishnan, Rahul G. and Shalit, Uri and Sontag, David},
  journal={arXiv preprint arXiv:1511.05121},
  year={2015}
}
```
