---
type: paper
title: "A Mathematical Perspective on Transformers"
aliases:
  - "Geshkovski et al. 2023"
  - "Geshkovski (2023) Transformers as Interacting Particles"
authors:
  - Borjan Geshkovski
  - Cyril Letrouit
  - Yury Polyanskiy
  - Philippe Rigollet
year: 2023
arxiv: "2312.10794"
url: https://arxiv.org/abs/2312.10794
tags:
  - cluster/multi-agent
  - cluster/attention
  - project/transformer
  - project/multi-agent
  - field/mathematics
  - field/cs-ml
status: stable
created: 2026-06-19
updated: 2026-06-20
---

# A Mathematical Perspective on Transformers

> [!info] Citation
> Borjan Geshkovski, Cyril Letrouit, Yury Polyanskiy, and Philippe Rigollet (2023). "A Mathematical Perspective on Transformers." arXiv:2312.10794. <https://arxiv.org/abs/2312.10794>

## TL;DR

This paper models a transformer as an **interacting particle system**: each token is a particle on the sphere, and the stack of attention layers is the time-discretization of a mean-field flow in which particles attract one another with weights set by a softmax over inner products. Under this dynamics tokens **cluster**, and in the long-depth limit they collapse onto a small number of points — interpreted as the emergence of "leaders" or consensus clusters. The work supplies rigorous theorems (clustering, metastability, the geometry of the limiting configurations) for what attention does to a population of tokens as depth grows.

## Problem & setting

Transformers are usually analyzed as function approximators; here the authors instead treat the *evolution of the token cloud through depth* as the primary object. Residual connections make the layer update a small step, so the deep network is read as an Euler discretization of a continuous-time flow on $(\mathbb{S}^{d-1})^n$, and the question becomes the asymptotic behavior of that flow.

## Method

They write the attention update as a gradient-type interacting-particle dynamics with a softmax interaction kernel of inverse temperature set by the query-key scaling, pass to the mean-field (continuity-equation) limit, and analyze the resulting nonlinear transport. Tools come from dynamical systems, optimal transport, and the theory of consensus/aggregation models.

## Key results

- **Clustering / consensus.** For a range of temperatures the particles converge to a single cluster as depth tends to infinity; the all-to-all softmax attraction drives the token cloud toward consensus.
- **Metastable multi-cluster configurations.** At finite depth and intermediate temperature the system lingers in long-lived states with several clusters before eventual collapse — a structured intermediate regime.
- **Geometry of limits.** The limiting point configurations and their rates of approach are characterized, tying the inverse-temperature (the attention scaling) to how sharply and how fast consensus forms.

## Relevance to this research

This is the strongest pure-mathematics neighbor of the PIFB ([[participatory-it-from-bit]]) consensus and meta-agent story. PIFB reads attention weights $\beta_{ij}$ as a coupling that pulls beliefs together, and its tower forms **meta-agents** by coarse-graining clusters of agents — exactly the leaders/clusters that Geshkovski et al. prove emerge from the attention flow. The mean-field interacting-particle limit is the continuum shadow of PIFB's discrete belief-coupling term $\sum_{ij}\beta_{ij}\,\mathrm{KL}(q_i \,\|\, \Omega_{ij} q_j)$ in the [[Variational free energy]] functional: minimizing pairwise KL between transported beliefs is a consensus/aggregation dynamics on the [[Statistical manifold]] of Gaussians, with $\beta_{ij}$ the softmax interaction weight. Their metastable multi-cluster states correspond to PIFB's emergent-structure regime — multiple coherent groups before any global collapse — and their single-cluster collapse is the same failure mode PIFB calls "heat death," the degenerate consensus the entropy regularizer is meant to forestall (compare the rank-collapse account in [[dong-2021-rank-collapse]]). The temperature dependence maps onto PIFB's $\tau = \kappa\sqrt{K}$ control over how aggressively beliefs are pulled together, connecting to [[Renormalization-group flow of beliefs]] and [[Meta-agents and hierarchical emergence]].

## Cross-links

- Concepts: [[Meta-agents and hierarchical emergence]], [[Renormalization-group flow of beliefs]], [[Variational free energy]]
- Sources: [[dong-2021-rank-collapse]], [[vaswani-2017-attention]], [[degroot-1974-consensus]], [[hegselmann-2002-opinion|hegselmann-krause-2002]]
- Project: [[participatory-it-from-bit]], [[Gauge-Theoretic Multi-Agent VFE Model]]

```bibtex
@article{geshkovski2023mathematical,
  title         = {A Mathematical Perspective on Transformers},
  author        = {Geshkovski, Borjan and Letrouit, Cyril and Polyanskiy, Yury and Rigollet, Philippe},
  journal       = {arXiv preprint arXiv:2312.10794},
  year          = {2023},
  eprint        = {2312.10794},
  archivePrefix = {arXiv},
  primaryClass  = {cs.LG},
  url           = {https://arxiv.org/abs/2312.10794}
}
```
