---
type: paper
title: "On Information and Sufficiency"
aliases:
  - "Kullback 1951"
  - "KL divergence"
  - "Kullback-Leibler"
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
> Kullback, S. & Leibler, R. A. (1951). "On Information and Sufficiency." *The Annals of Mathematical Statistics*, 22(1), 79–86. https://doi.org/10.1214/aoms/1177729694

## TL;DR
Kullback and Leibler introduce a measure of the "information" in one probability distribution relative to another — now universally called the KL divergence — defined as $D_\mathrm{KL}(P \| Q) = \int p(x) \log \frac{p(x)}{q(x)} \, dx$. They ground it in Fisher's notion of information and show it quantifies the expected log-likelihood ratio, linking it directly to sufficiency and statistical efficiency. The paper establishes the non-negativity of the divergence (by Jensen's inequality) and its role as a discrimination measure between hypotheses.

## Problem & setting
The paper addresses how to measure the "information for discrimination" between two probability distributions $P$ and $Q$ — that is, how much information a sample provides for distinguishing $P$ from $Q$. Prior art includes Fisher's information (a local, differential notion tied to the score function) and Shannon's entropy (average self-information). The authors seek a global measure that captures the directed discrepancy between two distributions and relates naturally to likelihood-ratio tests and sufficient statistics.

## Method
The central object is the mean information per observation from $P$ for discrimination in favor of $P$ against $Q$:

$$I(1:2) = \int p(x) \log \frac{p(x)}{q(x)} \, d\mu(x),$$

which is the expected log-likelihood ratio under $P$ — precisely $D_\mathrm{KL}(P \| Q)$ in modern notation. The authors prove $I(1:2) \geq 0$ with equality iff $P = Q$ a.e., using Jensen's inequality applied to the convex function $-\log$. They also introduce the symmetric "J-divergence" $J(1,2) = I(1:2) + I(2:1)$, relate $I(1:2)$ to Fisher information via a local quadratic approximation ($I(1:2) \approx \tfrac{1}{2} J(\theta) \, (\Delta\theta)^2$ for nearby distributions in a parametric family), and connect the measure to sufficiency: a statistic $T$ is sufficient iff the information for discrimination computed from the marginal distribution of $T$ equals that from the full sample.

## Key results
The paper establishes the following central results. (1) Non-negativity: $I(1:2) \geq 0$ for all distributions, with equality iff $P = Q$. (2) The relationship to Fisher information: for a one-parameter family $p(x;\theta)$, $I(\theta:\theta') \approx \tfrac{1}{2}(\theta'-\theta)^2 J(\theta)$ where $J(\theta)$ is the Fisher information, showing KL divergence is the global extension of the local Fisher metric. (3) Characterization of sufficiency: $T$ is sufficient for the family $\{P_\theta\}$ iff $I_T(1:2) = I_X(1:2)$ for all pairs $P,Q$ — no information for discrimination is lost by reduction to $T$. (4) The J-divergence is symmetric and satisfies analogous properties, useful when no natural direction between hypotheses is privileged.

## Relevance to this research
The KL divergence introduced here is the foundational building block of the entire VFE (variational free energy) framework used in this research program. Concretely: (a) the variational free energy functional $F$ is a sum of KL terms — $\alpha \, D_\mathrm{KL}(q_i \| p_i)$ (belief-to-prior self-coupling), $\lambda_h \, D_\mathrm{KL}(s_i \| h)$ (hyper-prior coupling), and pairwise $D_\mathrm{KL}(q_i \| \Omega_{ij} q_j)$ terms (gauge-transported belief coupling) — so every gradient step in the VFE transformer minimizes KL terms derived from this paper's definition; (b) the GL(K) gauge-equivariant attention mechanism derives softmax attention weights $\beta_{ij}$ as the stationary point of $F$ with respect to those weights, a derivation whose correctness depends critically on the $I(1:2) \geq 0$ lower bound guaranteeing the free energy is bounded below; (c) information geometry (the Fisher–Rao metric, natural gradient, SPD belief manifolds) is the geometric elaboration of the local approximation $I \approx \tfrac{1}{2}(\Delta\theta)^T J(\theta) \Delta\theta$ established here; (d) the f-divergence registry in the codebase (KL, reverse-KL, alpha-divergences) is a generalization of this paper's construction; (e) in the multi-agent active inference model, agents minimize expected free energy which again reduces to KL terms between posterior beliefs and prior preferences.

## Cross-links
- Concepts: [[KL Divergence]], [[Variational Free Energy]], [[Information Geometry]], [[Fisher Information]]
- Related sources: [[shannon-1948-mathematical-theory-communication]], [[amari-2016-information-geometry]]
- Manuscript/Project: [[VFE Transformer Program]], [[GL(K) Attention]]

## BibTeX
```bibtex
@article{Kullback1951,
  author  = {Kullback, Solomon and Leibler, Richard A.},
  title   = {On Information and Sufficiency},
  journal = {The Annals of Mathematical Statistics},
  volume  = {22},
  number  = {1},
  pages   = {79--86},
  year    = {1951},
  doi     = {10.1214/aoms/1177729694},
}
```
