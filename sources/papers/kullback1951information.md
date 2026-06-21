---
type: paper
title: "On Information and Sufficiency"
aliases:
  - "Kullback Leibler 1951"
  - "KL divergence"
authors:
  - Kullback, Solomon
  - Leibler, Richard A.
year: 1951
arxiv: null
url: https://doi.org/10.1214/aoms/1177729694
tags:
  - cluster/info-geometry
  - project/transformer
  - project/multi-agent
  - field/statistics
  - field/mathematics
  - field/cs-ml
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# On Information and Sufficiency

> [!info] Citation
> Kullback, S. & Leibler, R. A. (1951). "On Information and Sufficiency." *Annals of Mathematical Statistics*, 22(1), 79–86. https://doi.org/10.1214/aoms/1177729694

## TL;DR
Kullback and Leibler introduce a measure of the "information" in one probability distribution relative to another, now universally called the KL divergence (or relative entropy). They show this quantity arises naturally from sufficiency considerations in statistics, unifying Fisher information with Shannon's entropy framework, and establish its fundamental asymmetry and non-negativity.

## Problem & setting
The paper addresses how to quantify the "amount of information" supplied by data for discriminating between two statistical hypotheses or probability measures. Prior art includes Fisher's concept of information, Shannon's entropy (1948), and Wiener's related work — but none provided a coherent measure applicable directly to comparing two arbitrary distributions.

## Method
The authors define the directed divergence (mean information for discrimination in favour of hypothesis 1 against hypothesis 2) as:

$$I(1:2) = \int \log\frac{dP_1}{dP_2} \, dP_1$$

which is the expected log-likelihood ratio under $P_1$. They establish non-negativity $I(1:2) \geq 0$ with equality if and only if $P_1 = P_2$ almost everywhere (via Jensen's inequality / convexity of $-\log$). They also define the symmetric "J-divergence":

$$J(1,2) = I(1:2) + I(2:1)$$

They connect this to sufficiency: a statistic $T$ is sufficient for discriminating between $P_1$ and $P_2$ if and only if $I(1:2)$ is preserved under $T$, providing an information-theoretic characterisation of Fisher sufficiency.

## Key results
The KL divergence $I(1:2) = \mathbb{E}_{P_1}[\log(p_1/p_2)]$ is non-negative, equals zero iff $P_1 = P_2$, and is not symmetric. The symmetric J-divergence satisfies $J = I(1:2) + I(2:1) \geq 0$. For exponential families, $I(1:2)$ reduces to a Bregman divergence in the natural parameters, linking directly to later information-geometric work. The paper shows that sufficiency preserves information in the KL sense: $I_T(1:2) = I(1:2)$ iff $T$ is sufficient, and $I_T(1:2) \leq I(1:2)$ in general (data processing inequality, implicit).

## Relevance to this research
The KL divergence is the central quantity in the VFE transformer's free energy functional: every term in $F$ (belief self-coupling $\alpha \cdot \text{KL}(q_i \| p_i)$, hyper-prior coupling $\lambda_h \cdot \text{KL}(s_i \| h)$, pairwise belief coupling $\beta_{ij} \cdot \text{KL}(q_i \| \Omega_{ij} q_j)$, model coupling $\gamma_{ij} \cdot \text{KL}(s_i \| \Omega_{ij} s_j)$) is a KL divergence. The gauge transport $\Omega_{ij}$ acts on the arguments of KL, and gauge equivariance of the free energy rests on the transformation properties of KL under the GL(K) group action. In information geometry (Amari), the KL divergence defines the dually-flat structure on the statistical manifold, connecting directly to the SPD belief geometry used in VFE3. The attention weights $\beta_{ij}$ arising as softmax over KL gradients inherit their interpretation from this foundational definition.

## Cross-links
- Concepts: [[KL Divergence]], [[Information Geometry]], [[Variational Free Energy]], [[Sufficient Statistic]]
- Related sources: [[shannon1948mathematical]], [[amari1985differential]], [[cover2006elements]]
- Manuscript/Project: [[VFE Transformer Program]], [[GL(K) Attention Manuscript]]

## BibTeX
```bibtex
@article{kullback1951information,
  author  = {Kullback, Solomon and Leibler, Richard A.},
  title   = {On Information and Sufficiency},
  journal = {The Annals of Mathematical Statistics},
  year    = {1951},
  volume  = {22},
  number  = {1},
  pages   = {79--86},
  doi     = {10.1214/aoms/1177729694},
}
```
