---
type: paper
title: "An Alternative Model for Mixtures of Experts"
aliases:
  - Xu 1995
  - xu1995alternative
  - Generative-gating mixture of experts
authors:
  - Xu, Lei
  - Jordan, Michael I.
  - Hinton, Geoffrey E.
year: 1995
url: https://proceedings.neurips.cc/paper/1994/hash/c8fbbc86abe8bd6a5eb6a3b4d0411301-Abstract.html
pdf: sources/pdfs/xu-1995-alternative-mixtures-of-experts.pdf
tags:
  - cluster/attention
  - project/transformer
  - field/cs-ml
  - field/statistics
created: 2026-10-24
---

# An Alternative Model for Mixtures of Experts

> [!info] Citation
> Xu, L., Jordan, M. I., & Hinton, G. E. (1995). *An alternative model for mixtures of experts*. In Advances in Neural Information Processing Systems 7 (NIPS 1994), pp. 633–640.

## TL;DR
The softmax gating network of a mixture of experts is replaced by a generative gate: the gate weight of expert $j$ is the posterior probability that input $x$ came from that expert's input density. This makes the gating M-step analytic, so EM becomes a single loop with no learning-rate choice, and convergence is faster in the reported simulations.

## Method
The modified gate (their Eq. 5) is
$$g_j(x,v)=\frac{\alpha_jP(x\mid v_j)}{\sum_i\alpha_iP(x\mid v_i)},\qquad\sum_j\alpha_j=1,$$
with $P(x\mid v_j)$ an exponential-family density, so that $g_j$ is literally $P(j\mid x)$ under a joint model of inputs and outputs. The paper applies it to piecewise nonlinear regression and to combining previously trained classifiers.

## Relevance to this research
The `gaussian_template` block MLP of [[VFE Transformer Program|vfe3]] is this architecture with Gaussian input densities $P(x\mid j)=\mathcal N(\nu_j,\Lambda_j)$ (evaluated through the belief's KL) and constant experts (the value vectors $w_j$). It is the precise precedent for reading a softmax-gated feed-forward block as Bayesian component assignment under a declared joint, rather than an arbitrary gate ([[Template routing]]). It differs from [[jacobs-1991-mixtures-of-local-experts]], whose softmax gate is discriminative.

## Cross-links
- Methods: [[Template routing]]
- Concepts: [[Associative Memory]]
- Related sources: [[jacobs-1991-mixtures-of-local-experts]], [[ghahramani-1994-incomplete-data-em]], [[geva-2021-ffn-key-value-memories]]

## BibTeX
```bibtex
@inproceedings{xu1995alternative,
  author    = {Xu, Lei and Jordan, Michael I. and Hinton, Geoffrey E.},
  title     = {An Alternative Model for Mixtures of Experts},
  booktitle = {Advances in Neural Information Processing Systems 7},
  pages     = {633--640},
  year      = {1995}
}
```
