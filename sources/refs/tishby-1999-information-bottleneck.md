---
type: reference
title: "The Information Bottleneck Method"
aliases:
  - "Tishby, Pereira & Bialek 1999"
  - "Tishby (1999) Information Bottleneck"
authors:
  - Naftali Tishby
  - Fernando C. Pereira
  - William Bialek
year: 1999
arxiv: "physics/0004057"
url: https://arxiv.org/abs/physics/0004057
tags:
  - cluster/info-geometry
  - project/transformer
  - project/multi-agent
  - field/statistics
  - field/cs-ml
created: 2026-06-19
updated: 2026-06-19
---

# The Information Bottleneck Method

> [!info] Citation
> Naftali Tishby, Fernando C. Pereira, and William Bialek (1999). "The Information Bottleneck Method." 37th Annual Allerton Conference on Communication, Control and Computing, pp. 368–377. arXiv:physics/0004057. <https://arxiv.org/abs/physics/0004057>

## TL;DR

The information bottleneck (IB) formalizes "extracting the relevant part of a signal." Given a source $X$ and a relevance variable $Y$, one seeks a compressed representation $T$ that minimizes the information kept about $X$ while maximizing the information kept about $Y$, trading the two off through a Lagrangian $\mathcal{L} = I(X; T) - \beta\, I(T; Y)$. The optimal stochastic encoder $p(t\mid x)$ satisfies a self-consistent set of equations — a Boltzmann-like assignment with energy given by the KL divergence $\mathrm{KL}(p(y\mid x)\,\|\,p(y\mid t))$, solvable by an iterative Blahut–Arimoto-style fixed point. It is the founding statement of relevance-driven lossy compression.

## What it establishes

- The IB variational principle: minimize $I(X;T) - \beta\,I(T;Y)$ over encoders $p(t\mid x)$, with $\beta$ the compression-versus-relevance knob.
- Self-consistent optimality equations with a **soft, KL-distortion-driven** cluster assignment, $p(t\mid x) \propto p(t)\exp(-\beta\,\mathrm{KL}(p(y\mid x)\,\|\,p(y\mid t)))$.
- A convergent alternating-projection algorithm; the trade-off curve (the information plane) as the object of interest.

## Why the project cites it

The IB Lagrangian is PIFB's ([[participatory-it-from-bit]]) **complexity-versus-accuracy free energy in another guise**. PIFB's [[Variational free energy]] balances a compression pressure — the self-coupling $\alpha\,\mathrm{KL}(q_i\|p_i)$ that penalizes deviation of beliefs from priors, a cost on representational complexity — against an accuracy pressure, the observation-likelihood term $-\mathbb{E}_q[\log p(o\mid x)]$. That is structurally the IB trade-off $I(X;T)$ (complexity) versus $I(T;Y)$ (relevance), with the project's $\alpha$ (or its inverse) playing Tishby's $\beta$. The IB's defining feature — that optimal assignment is a **softmax over a KL distortion** — is also exactly the form of PIFB's attention weight $\beta_{ij} = \mathrm{softmax}(-\mathrm{KL}(\cdot)/\tau)$, so the IB supplies the variational pedigree for both the capacity floor and the KL-distortion-softmax structure of belief coupling. This grounds the [[Information bottleneck]] page and links to the Gaussian specialization closest to PIFB's belief tuples ([[chechik-2005-gaussian-ib]]) and the deep-learning information-plane reading ([[shwartz-ziv-2017-opening-black-box]]).

```bibtex
@inproceedings{tishby1999information,
  title         = {The Information Bottleneck Method},
  author        = {Tishby, Naftali and Pereira, Fernando C. and Bialek, William},
  booktitle     = {Proceedings of the 37th Annual Allerton Conference on
                   Communication, Control and Computing},
  pages         = {368--377},
  year          = {1999},
  eprint        = {physics/0004057},
  archivePrefix = {arXiv},
  primaryClass  = {physics.data-an},
  url           = {https://arxiv.org/abs/physics/0004057}
}
```
