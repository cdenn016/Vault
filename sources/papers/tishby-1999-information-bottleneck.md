---
type: paper
title: "The Information Bottleneck Method"
aliases:
  - "Tishby 1999"
  - "IB"
  - "Information Bottleneck"
  - "tishby-2000-information-bottleneck"
  - "Tishby 2000"
  - "tishby2000information"
  - "tishby1999information"
authors:
  - Tishby, Naftali
  - Pereira, Fernando C.
  - Bialek, William
year: 1999
arxiv: "physics/0004057"
url: https://arxiv.org/abs/physics/0004057
tags:
  - cluster/info-geometry
  - project/transformer
  - project/multi-agent
  - field/statistics
  - field/cs-ml
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# The Information Bottleneck Method

> [!info] Citation
> Tishby, Naftali, Fernando C. Pereira, and William Bialek (1999). "The Information Bottleneck Method." *Proceedings of the 37th Annual Allerton Conference on Communication, Control and Computing*, pp. 368–377. arXiv:physics/0004057. <https://arxiv.org/abs/physics/0004057>

## TL;DR

The information bottleneck (IB) formalizes relevance-driven lossy compression. Given a source $X$ and a relevance variable $Y$, one seeks a compressed representation $T$ that minimizes information retained about $X$ while maximizing information retained about $Y$, trading the two via a Lagrangian $\mathcal{L} = I(X;T) - \beta\,I(T;Y)$. The optimal stochastic encoder $p(t\mid x)$ satisfies a self-consistent set of equations — a Boltzmann-like soft assignment whose energy is $\mathrm{KL}(p(y\mid x)\,\|\,p(y\mid t))$ — solvable by an iterative Blahut–Arimoto-style fixed point. The compression-relevance trade-off curve, traced in the information plane $(I(X;T), I(T;Y))$ as $\beta$ varies, is the central object of interest.

## Problem & setting

The paper asks: what information in a signal $X$ is relevant to predicting another variable $Y$, and how should one compress $X$ to discard only irrelevant information? Classical rate-distortion theory requires a fixed distortion metric, which is application-specific and often arbitrary. The IB replaces the metric with a relevance variable $Y$, making "relevant" a purely information-theoretic concept: retain what predicts $Y$. The prior state of the field had no principled, metric-free framework for relevance-driven compression.

## Method

The IB functional is minimized over the encoder $p(t\mid x)$ subject to a Markov chain $Y \to X \to T$:

$$\min_{p(t\mid x)}\; I(X;T) - \beta\, I(T;Y), \qquad \beta > 0.$$

Stationarity yields the self-consistent equations

$$p(t\mid x) \propto p(t)\exp\!\bigl(-\beta\,\mathrm{KL}(p(y\mid x)\,\|\,p(y\mid t))\bigr),$$
$$p(t) = \sum_x p(x)\,p(t\mid x),$$
$$p(y\mid t) = \sum_x p(y\mid x)\,p(x\mid t).$$

Iterating these three equations in alternation converges to a fixed point (analogous to the Blahut–Arimoto algorithm for rate-distortion). The parameter $\beta$ continuously interpolates from maximal compression ($\beta \to 0$, $T$ is a single point) to no compression ($\beta \to \infty$, $T = X$). The boundary of the achievable $(I(X;T), I(T;Y))$ region — the IB curve — generalizes the rate-distortion function.

## Key results

The main theoretical contributions are: (i) the existence and characterization of the IB optimal encoder as a softmax over KL divergences; (ii) proof that the iterative algorithm converges monotonically; (iii) the IB curve as a universal relevance measure, independent of any task-specific distortion; (iv) the observation that the slope $dI(T;Y)/dI(X;T) = \beta^{-1}$ at each optimal point, giving $\beta$ a precise operational meaning as marginal value of complexity. The paper also notes that for Gaussian $X$ and $Y$ the IB optimal $T$ is linear (a precursor to the Gaussian IB developed by Chechik et al.).

## Relevance to this research

The IB Lagrangian maps directly onto the PIFB variational free energy. The VFE self-coupling term $\alpha\,\mathrm{KL}(q_i \| p_i)$ penalizes representational complexity (analogous to $I(X;T)$), while the observation-likelihood term $-\mathbb{E}_q[\log p(o\mid x)]$ drives accuracy (analogous to $\beta\,I(T;Y)$), with $\alpha$ (or its inverse) playing the role of Tishby's $\beta$. The IB's defining structural result — that the optimal compression assignment is a **softmax over a KL distortion** — is also the exact form of the GL(K) attention weight $\beta_{ij} = \mathrm{softmax}(-\mathrm{KL}(\cdot)/\tau)$, supplying the variational pedigree for both the capacity floor and the KL-distortion-softmax structure of belief coupling in the [[GL(K) Attention]] manuscript. The Gaussian specialization closest to PIFB's Gaussian belief tuples $(μ, Σ, φ)$ is developed in [[chechik-2005-gaussian-ib]], and the deep-learning information-plane interpretation is developed in [[shwartz-ziv-2017-opening-black-box]].

## Cross-links

- Concepts: [[Information bottleneck]], [[Variational free energy]], [[KL divergence]], [[Natural gradient]]
- Related sources: [[chechik-2005-gaussian-ib]], [[shwartz-ziv-2017-opening-black-box]], [[neal-1998-variational-em]]
- Manuscript/Project: [[VFE Transformer Program]], [[GL(K) Attention]]

## BibTeX

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
