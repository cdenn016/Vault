---
type: paper
title: "Opening the Black Box of Deep Neural Networks via Information"
aliases:
  - "Shwartz-Ziv & Tishby 2017"
  - "Shwartz-Ziv (2017) IB Black Box"
authors:
  - Ravid Shwartz-Ziv
  - Naftali Tishby
year: 2017
arxiv: "1703.00810"
url: https://arxiv.org/abs/1703.00810
tags:
  - cluster/info-geometry
  - project/transformer
  - project/multi-agent
  - field/cs-ml
  - field/statistics
status: stable
created: 2026-06-19
updated: 2026-06-19
---

# Opening the Black Box of Deep Neural Networks via Information

> [!info] Citation
> Ravid Shwartz-Ziv and Naftali Tishby (2017). "Opening the Black Box of Deep Neural Networks via Information." arXiv:1703.00810. <https://arxiv.org/abs/1703.00810>

## TL;DR

This paper applies the [[Information bottleneck]] to deep learning, tracking each hidden layer as a point in the **information plane** with coordinates $\big(I(X; T),\, I(T; Y)\big)$ — how much a layer retains about the input $X$ versus how much it keeps about the label $Y$. The authors report that training proceeds in two phases: a short **fitting** phase where layers gain label information, followed by a long **compression** phase where layers discard input information they do not need for the label, drifting toward the IB-optimal trade-off. It is the paper that made the IB a candidate theory of representation learning in deep nets.

## Problem & setting

Deep nets are opaque; the authors propose information-theoretic coordinates as a model-agnostic way to watch what each layer represents during training, using the IB trade-off between compression of the input and prediction of the output as the organizing principle.

## Method

For small networks they estimate $I(X;T)$ and $I(T;Y)$ per layer (via binning of activations) and plot their trajectories in the information plane over training epochs, comparing across depth and width.

## Key results

- Two distinct training phases: a brief error-minimization (fitting) phase, then a prolonged representation-compression phase.
- Deeper layers compress more, ending nearer the IB bound; depth is read as successive bottlenecking.
- Compression is associated with generalization in their setting. (The universality of these claims was later contested for certain activations and estimators — the note records the result as reported.)

## Relevance to this research

PIFB ([[participatory-it-from-bit]]) posits a **capacity floor**: an irreducible free-energy / loss level set by how much the belief representation can compress while staying predictive. The information-plane picture is the canonical visualization of exactly that compression-versus-relevance trade-off, and Shwartz-Ziv & Tishby give it a per-layer, per-epoch dynamics. PIFB's layer-by-layer descent of the [[Variational free energy]] is a candidate mechanism realizing an IB-like trajectory in belief coordinates: the self-coupling term $\alpha\,\mathrm{KL}(q_i\|p_i)$ penalizes deviation from the prior (a compression pressure toward the prior code), while the observation-likelihood term $-\mathbb{E}_q[\log p(o\mid x)]$ supplies the relevance pressure, the two combining like the IB Lagrangian (see [[tishby-1999-information-bottleneck]]). This grounds the [[Information bottleneck]] reading of PIFB and connects the capacity-floor claim to the scaling-law genre ([[kaplan-2020-scaling-laws]], [[hoffmann-2022-chinchilla]]): a power-law loss-versus-capacity curve is what an IB trade-off predicts as the compression budget is relaxed.

## Cross-links

- Concepts: [[Information bottleneck]], [[Variational free energy]], [[Neural scaling laws]]
- Sources: [[tishby-1999-information-bottleneck]], [[chechik-2005-gaussian-ib]], [[kaplan-2020-scaling-laws]]
- Project: [[participatory-it-from-bit]], [[Gauge-Theoretic Multi-Agent VFE Model]]

```bibtex
@article{shwartzziv2017opening,
  title         = {Opening the Black Box of Deep Neural Networks via Information},
  author        = {Shwartz-Ziv, Ravid and Tishby, Naftali},
  journal       = {arXiv preprint arXiv:1703.00810},
  year          = {2017},
  eprint        = {1703.00810},
  archivePrefix = {arXiv},
  primaryClass  = {cs.LG},
  url           = {https://arxiv.org/abs/1703.00810}
}
```
