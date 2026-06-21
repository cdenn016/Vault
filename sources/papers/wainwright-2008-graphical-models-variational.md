---
type: paper
title: "Graphical Models, Exponential Families, and Variational Inference"
aliases:
  - "Wainwright 2008"
  - "Wainwright Jordan 2008"
authors:
  - Wainwright, Martin J.
  - Jordan, Michael I.
year: 2008
arxiv: null
url: https://doi.org/10.1561/2200000001
tags:
  - cluster/vfe
  - cluster/info-geometry
  - project/transformer
  - project/multi-agent
  - field/statistics
  - field/cs-ml
  - field/mathematics
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Graphical Models, Exponential Families, and Variational Inference

> [!info] Citation
> Wainwright, M. J. and Jordan, M. I. (2008). "Graphical Models, Exponential Families, and Variational Inference." *Foundations and Trends in Machine Learning*, Vol. 1, Nos. 1–2, pp. 1–305. DOI: 10.1561/2200000001.

## TL;DR
This monograph presents a unified treatment of variational inference for probabilistic graphical models, grounding all major algorithms — sum-product, belief propagation, mean field, expectation-propagation, max-product, linear programming relaxations, and conic programming relaxations — in a single variational principle derived from exponential family theory. The key duality exploited is the conjugate duality between the cumulant (log-partition) function and the entropy functional for exponential families, which yields general variational representations for computing likelihoods, marginal probabilities, and modes. The framework provides a principled alternative to MCMC for approximate inference in large-scale statistical models.

## Problem & setting
Exact probabilistic inference in graphical models — computing marginals, likelihoods, and modes — is intractable for general graphs because it requires summation or maximization over an exponential number of configurations. The junction tree algorithm solves this exactly but has complexity exponential in the treewidth of the graph, making it infeasible for dense, large, or loopy graphs. The paper asks: can the full diversity of approximate inference algorithms be understood from a single principled variational perspective, and can this perspective guide the design of new algorithms with provable guarantees?

Prior art addressed specific algorithms in isolation (belief propagation, mean field, EP); the contribution here is a unified framework covering all of them and connecting to convex analysis, conic programming, and statistical physics (Bethe/Kikuchi approximations).

## Method
The central object is the cumulant function (log-partition function) $A(\theta) = \log \int \exp\langle \theta, \phi(x) \rangle \, d\nu(x)$ of an exponential family, which is convex. Its convex conjugate is the negative entropy $A^*(\mu) = \sup_\theta \{ \langle \theta, \mu \rangle - A(\theta) \}$ over the marginal polytope $\mathcal{M}$ of realizable mean parameters. This conjugate duality yields the variational representation:

$$A(\theta) = \sup_{\mu \in \mathcal{M}} \{ \langle \theta, \mu \rangle - A^*(\mu) \}$$

which is exact when $\mathcal{M}$ and $A^*$ are exact. Approximate inference algorithms arise from two types of relaxation: (1) replacing $\mathcal{M}$ with a tractable outer bound (the local polytope for Bethe/BP, semidefinite relaxations for conic methods), and (2) replacing $A^*$ with a tractable surrogate entropy (Bethe entropy, naive mean field entropy). The Bethe approximation substitutes the exact entropy with a sum of single-node entropies minus pairwise mutual information terms and optimizes over the local consistency polytope — yielding the sum-product/belief propagation algorithm as the stationary-point equations. Mean field methods use a fully factored surrogate $q = \prod_s q_s$ and optimize a lower bound on the likelihood. Max-product and linear programming relaxations address mode computation by working in the max-plus semiring. Convex relaxations (Section 7) based on tree-reweighted approximations yield upper bounds on the log-likelihood with convergence guarantees, unlike the nonconvex Bethe/mean-field objectives.

## Key results
The sum-product algorithm on trees computes exact marginals; on loopy graphs it computes fixed points of the Bethe variational problem, which may be multiple and does not in general correspond to the true marginals. Mean field provides a lower bound on the log-likelihood by optimizing over a tractable family; the bound is tight when the family contains the true posterior. Tree-reweighted belief propagation (Section 7) yields an upper bound on the log-likelihood and has a unique fixed point achievable by convex optimization. Conic/semidefinite relaxations via moment matrices provide a hierarchy of increasingly tight bounds. For mode computation, the max-product algorithm on loopy graphs computes fixed points of a linear programming relaxation of the MAP integer program, whose LP bound can be tightened using the Sherali–Adams or Lasserre hierarchies.

## Relevance to this research
This monograph is foundational background for the VFE transformer and GL(K) gauge-equivariant attention in several direct ways. First, the VFE framework minimizes a variational free energy $F = \mathrm{KL}(q \| p)$ that is precisely an instance of the conjugate dual variational principle developed here: $F[\mu] = A^*(\mu) - \langle \theta_{\mathrm{obs}}, \mu \rangle$, placing VFE squarely within the exponential family variational framework. The Bethe free energy and its cluster variational method (CVM) generalizations are the direct statistical-physics predecessors of the VFE functional used in the transformer. Second, the attention weights $\beta_{ij}$ in the GL(K) manuscript arise as the solution to a row-constrained variational problem (the softmax is the stationary point of an entropy-regularized coupling objective), exactly mirroring the variational derivation of belief propagation fixed points here. Third, the paper's treatment of the marginal polytope $\mathcal{M}$ and its local polytope outer bound is directly relevant to the constraint geometry of the E-step belief update in the VFE transformer. Fourth, for the multi-agent active inference setting, this framework provides the formal basis for understanding how distributed message-passing agents (each minimizing local VFE) collectively approximate a joint variational inference computation. The exponential family structure is also central to the Gaussian belief tuples $(\mu, \Sigma)$ used as the natural parameterization of beliefs throughout the VFE code.

## Cross-links
- Concepts: [[Variational Free Energy]] [[Exponential Families]] [[Belief Propagation]] [[Mean Field Theory]] [[Information Geometry]]
- Related sources: [[amari-2016-information-geometry]] [[blei-2017-variational-inference-review]]
- Manuscript/Project: [[VFE Transformer Program]] [[GL(K) Attention Manuscript]]

## BibTeX
```bibtex
@article{Wainwright2008,
  author  = {Wainwright, Martin J. and Jordan, Michael I.},
  title   = {Graphical Models, Exponential Families, and Variational Inference},
  journal = {Foundations and Trends in Machine Learning},
  year    = {2008},
  volume  = {1},
  number  = {1--2},
  pages   = {1--305},
  doi     = {10.1561/2200000001},
}
```
