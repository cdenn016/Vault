---
type: paper
title: "Poincaré Embeddings for Learning Hierarchical Representations"
aliases:
  - Nickel 2017
  - Poincaré Embeddings
  - nickel-kiela-2017-poincare-embeddings
  - Nickel & Kiela 2017
authors:
  - Nickel, Maximilian
  - Kiela, Douwe
year: 2017
arxiv: "1705.08039"
url: https://arxiv.org/abs/1705.08039
tags:
  - cluster/info-geometry
  - cluster/spd-geometry
  - project/transformer
  - project/multi-agent
  - field/cs-ml
  - field/mathematics
  - field/statistics
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Poincaré Embeddings for Learning Hierarchical Representations

> [!info] Citation
> Nickel, Maximilian and Kiela, Douwe (2017). "Poincaré Embeddings for Learning Hierarchical Representations." *Advances in Neural Information Processing Systems 30 (NeurIPS 2017)*, pp. 6338–6347. arXiv:1705.08039 [cs.AI].

## TL;DR
This paper introduces Poincaré embeddings: representations of symbolic data (text, graphs, taxonomies) in hyperbolic space — specifically the Poincaré ball model — rather than Euclidean space. The core insight is that hyperbolic geometry is a continuous analog of tree structure, so hierarchical data can be embedded far more parsimoniously there. The method uses Riemannian stochastic gradient descent on the Poincaré ball and dramatically outperforms Euclidean embeddings on WordNet taxonomy reconstruction, link prediction in social networks, and lexical entailment, often with an order-of-magnitude smaller embedding dimension.

## Problem & setting
Euclidean embedding methods (Word2Vec, GloVe, DeepWalk, TransE, etc.) are bounded by their dimensionality when modeling complex hierarchical or power-law-distributed symbolic data. Large taxonomies such as WordNet exhibit exponential growth in the number of nodes with tree depth, which Euclidean geometry — where circle length grows only linearly with radius — cannot efficiently represent. The paper aims to exploit the fact that hyperbolic space inherently mirrors the exponential volume growth of trees, allowing hierarchical structure to be captured with low-dimensional, parsimonious embeddings learned in an unsupervised setting (no explicit hierarchy labels needed).

## Method
The Poincaré ball model uses the open unit ball $\mathcal{B}^d = \{x \in \mathbb{R}^d \mid \|x\| < 1\}$ equipped with the Riemannian metric tensor

$$g_x = \left(\frac{2}{1 - \|x\|^2}\right)^2 g_E,$$

giving the Poincaré distance

$$d(u, v) = \mathrm{arcosh}\!\left(1 + \frac{2\|u - v\|^2}{(1 - \|u\|^2)(1-\|v\|^2)}\right).$$

Distance grows exponentially near the boundary $\partial\mathcal{B}$, so the root of a hierarchy sits near the origin (small norm) and leaf nodes near the boundary (large norm). Hierarchy is thus encoded in the norm and similarity in the distance. Embeddings are learned by minimizing a soft-ranking loss (negative log-softmax over distances to positive vs. sampled negative pairs). Optimization is Riemannian SGD: the Euclidean gradient is rescaled by $g_\theta^{-1} = ((1-\|\theta\|^2)/2)^2$ (natural gradient) and a projection $\mathrm{proj}(\theta) = \theta/\|\theta\| - \varepsilon$ enforces the constraint $\|\theta\| < 1$. Full update:

$$\theta_{t+1} \leftarrow \mathrm{proj}\!\left(\theta_t - \eta_t \frac{(1-\|\theta_t\|^2)^2}{4} \nabla_E\right).$$

A "burn-in" phase (reduced learning rate, 10 epochs) is used to establish a good angular layout before embeddings move toward the boundary.

## Key results
On the transitive closure of the WordNet noun hierarchy (82,115 nouns, 743,241 hypernymy relations), Poincaré embeddings achieve mean rank 4.9 and MAP 0.823 in 5 dimensions for reconstruction, compared to rank 3542 / MAP 0.024 for Euclidean and rank 206 / MAP 0.517 for translational embeddings at the same dimension. A 5-dimensional Poincaré embedding matches or exceeds 200-dimensional Euclidean embeddings. On four scientific collaboration networks (AstroPh, CondMat, GrQc, HepPh), Poincaré embeddings outperform Euclidean embeddings for link prediction particularly in low dimensions (MAP 0.671 vs. 0.508 at d=10 on AstroPh). For lexical entailment on HyperLex, Poincaré embeddings (using WordNet-pretrained 5-dim embeddings) achieve Spearman's $\rho = 0.512$, far above all prior state-of-the-art methods (best competitor 0.389).

## Relevance to this research
Poincaré embeddings are directly relevant to the SPD/Riemannian belief geometry at the core of the VFE transformer. The Poincaré ball is a Riemannian manifold, and the paper's RSGD optimizer (natural gradient + retraction) is a direct instance of the Riemannian optimization framework used for belief-space E-steps in VFE3. The conformal metric $g_x = \lambda(x)^2 g_E$ with scalar conformal factor is structurally analogous to information-geometric metrics on Gaussian belief manifolds. The paper demonstrates that the choice of manifold geometry is not cosmetic — it encodes structural bias (hierarchical vs. flat) that propagates into generalization performance, which mirrors the VFE program's claim that gauge-equivariant geometry of the belief manifold shapes representation quality. The norm-as-hierarchy and distance-as-similarity dual encoding has a loose analog in the VFE framework where the precision $\Sigma^{-1}$ (norm-like) and belief distance (KL divergence) play separable geometric roles. The Fermi-Dirac edge probability used for network embedding (Eq. 7) is also structurally related to softmax attention with a temperature parameter.

## Cross-links
- Concepts: [[Riemannian Geometry]], [[Hyperbolic Geometry]], [[Information Geometry]], [[SPD-manifold geometry and Riemannian optimization|SPD Belief Geometry]], [[Meta-agents and hierarchical emergence]]
- Related sources: [[vilnis-2015-gaussian-embeddings]], [[pennec-2006-affine-invariant-tensor]], [[amari-1998-natural-gradient]], [[absil-2008-optimization-matrix-manifolds]], [[bialek2001predictability|bialek-2001-predictability-complexity]]
- Manuscript/Project: [[participatory-it-from-bit]], [[VFE Transformer Program]]

> [!note] Manuscript usage (PIFB): cited as the geometric warrant that hierarchical structure is most faithfully represented on a curved, non-Euclidean manifold rather than in flat space — supporting the project's hierarchical tower of agents/meta-agents and its use of curved manifolds (affine-invariant SPD belief covariances; Lie-group gauge frames), with Riemannian-optimization the same family as the project's natural-gradient retractions for $(\mu, \Sigma, \phi)$.

## BibTeX
```bibtex
@inproceedings{Nickel2017,
  author        = {Nickel, Maximilian and Kiela, Douwe},
  title         = {Poincar\'{e} Embeddings for Learning Hierarchical Representations},
  booktitle     = {Advances in Neural Information Processing Systems 30 (NeurIPS)},
  pages         = {6338--6347},
  year          = {2017},
  eprint        = {1705.08039},
  archivePrefix = {arXiv},
  primaryClass  = {cs.AI},
  url           = {https://arxiv.org/abs/1705.08039},
}
```
