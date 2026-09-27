---
type: reference
title: "Reinforcement Learning and Control as Probabilistic Inference: Tutorial and Review"
aliases:
  - "Levine 2018"
  - "Reinforcement Learning and Control as Probabilistic Inference"
  - "Levine2018"
authors:
  - Sergey Levine
year: 2018
arxiv: "1805.00909"
url: https://arxiv.org/abs/1805.00909
tags:
  - cluster/vfe
  - project/transformer
  - field/cs-ml
  - field/statistics
created: 2026-09-23
updated: 2026-09-23
---

# Reinforcement Learning and Control as Probabilistic Inference: Tutorial and Review

> [!info] Citation
> Sergey Levine (2018). "Reinforcement Learning and Control as Probabilistic Inference: Tutorial and Review." arXiv preprint [arXiv:1805.00909](https://arxiv.org/abs/1805.00909) (v3 read).

## TL;DR

A tutorial that embeds a control problem in a graphical model by adding binary "optimality" variables whose likelihood is the exponentiated reward. Conditioning on optimality turns planning into posterior inference, exact inference yields soft value functions, and variational inference yields maximum-entropy reinforcement learning and its algorithms (soft Q-learning and maximum-entropy actor-critic methods).

## What it establishes

Section 2.2 adds to the state–action model a binary variable $\mathcal O_t$ with $p(\mathcal O_t=1\mid s_t,a_t)=\exp(r(s_t,a_t))$ (Eq. 3). Conditioning on $\mathcal O_{1:T}=1$ gives the trajectory posterior $p(\tau\mid o_{1:T})\propto p(s_1)\prod_tp(s_{t+1}\mid s_t,a_t)\exp\big(\sum_tr(s_t,a_t)\big)$ (Eq. 4), so MAP inference is planning when the dynamics are deterministic. Section 2.3 computes the action posterior by backward messages, which give soft (log-sum-exp) value functions. Section 2.5 notes that Eq. 3 is a valid probability only for non-positive rewards, and that an undirected factor $\mathbb 1[\mathcal O_t=1]\exp(r)$ removes this restriction with the same inference procedure. Section 3 shows that variational inference with the true dynamics fixed yields the maximum-entropy reinforcement learning objective, Section 4 derives maximum-entropy policy gradients, actor-critic algorithms, and soft Q-learning, and Section 5 reviews the earlier control-as-inference literature. The tutorial cites [[kappen-2012-optimal-control-inference]] as KL-divergence control and, in Section 5.2, notes that [[toussaint-storkey-2006-probabilistic-inference-mdp]] gives an EM algorithm for control as inference that yields maximum expected reward solutions.

## Relevance to this research

The September 2026 v2 revision of the GL(K) attention manuscript uses the same optimality-variable device. Each receiver and head carries a binary compatibility record with $P(o=1\mid J=j)=\exp(-D_{ij}/\tau)$. Because $D_{ij}\ge0$, this is a valid probability, which is the non-positive-reward case of Section 2.5 with $r=-D_{ij}/\tau$. Conditioning on $o=1$ makes Gibbs routing the exact posterior of the source label $J$ at every temperature. See [[GL(K) gauge-equivariant attention]], [[Softmax]], and [[Active Inference]] for the neighboring free-energy reading of control.

## Local full text

The arXiv v3 PDF is stored at `sources/pdfs/Levine2018.pdf` ([local PDF](../pdfs/Levine2018.pdf)). Source: [arXiv:1805.00909](https://arxiv.org/pdf/1805.00909). SHA-256: `98f4831608edb32de2d80fd5bfd1a7661968f6c4b32559c68d15cee974dc60e2`.

## BibTeX

```bibtex
@misc{Levine2018,
  author = {Levine, Sergey},
  title = {Reinforcement Learning and Control as Probabilistic Inference: Tutorial and Review},
  year = {2018},
  howpublished = {arXiv preprint arXiv:1805.00909},
  eprint = {1805.00909},
  archivePrefix = {arXiv}
}
```
