---
type: paper
title: "Sinkhorn Distances: Lightspeed Computation of Optimal Transportation Distances"
aliases:
  - "Cuturi 2013"
  - "Sinkhorn Distances"
authors:
  - Cuturi, Marco
year: 2013
arxiv: "1306.0895"
url: https://arxiv.org/abs/1306.0895
tags:
  - cluster/info-geometry
  - project/transformer
  - field/cs-ml
  - field/statistics
  - field/mathematics
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Sinkhorn Distances: Lightspeed Computation of Optimal Transportation Distances

> [!info] Citation
> Cuturi, M. (2013). "Sinkhorn Distances: Lightspeed Computation of Optimal Transportation Distances." *Advances in Neural Information Processing Systems (NeurIPS)*. arXiv:1306.0895.

## TL;DR
This paper introduces Sinkhorn distances, a family of regularized optimal transport distances obtained by adding an entropic penalty to the classical Earth Mover's Distance (EMD) linear program. The entropic regularization converts the LP into a strictly convex problem solvable by the Sinkhorn-Knopp matrix scaling algorithm, achieving speedups of several orders of magnitude over classical solvers and lending itself naturally to GPU parallelization. On the MNIST benchmark, Sinkhorn distances match or exceed EMD classification accuracy while being dramatically faster to compute.

## Problem & setting
Classical optimal transport distances (Wasserstein / Earth Mover's Distance) are theoretically appealing and geometry-aware, but their computational cost scales as O(d^3 log d) for d-dimensional histograms, making them prohibitive for large-scale machine learning. Existing workarounds (structural constraints on the ground metric, approximation methods) sacrifice generality or performance. The paper asks whether the optimal transport problem can be reformulated to admit efficient, parallelizable computation without abandoning the geometric structure that makes it useful.

## Method
The key idea is to restrict the feasible set of transportation plans to those whose entropy is sufficiently large — equivalently, those whose KL divergence to the independence table r c^T is at most alpha. This defines the Sinkhorn distance:

    d_{M,alpha}(r, c) = min_{P in U_alpha(r,c)} <P, M>

where U_alpha(r,c) = {P in U(r,c) | KL(P || rc^T) <= alpha}. Introducing a Lagrange multiplier lambda for the entropic constraint gives the dual-Sinkhorn divergence:

    d^lambda_M(r, c) = <P^lambda, M>,   P^lambda = argmin_{P in U(r,c)} <P, M> - (1/lambda) h(P)

The KKT conditions show the optimum has the form P^lambda = diag(u) exp(-lambda M) diag(v), which is precisely the fixed-point structure exploited by the Sinkhorn-Knopp matrix scaling algorithm: alternating row and column normalizations of the kernel matrix K = exp(-lambda M). The algorithm is O(d^2) per iteration, trivially vectorizable to handle a batch of histograms simultaneously, and maps directly onto GPGPU matrix operations. Metric properties are established: for any alpha >= 0 and metric cost matrix M, d_{M,alpha} is symmetric and satisfies the triangle inequality (via a gluing lemma adapted to the entropic constraint). At alpha = 0 the distance reduces to the independence kernel r^T M c, which is negative definite when M is a Euclidean distance matrix. At large alpha it recovers the classical EMD.

## Key results
Theorem 1 establishes that d_{M,alpha} is symmetric and satisfies all triangle inequalities for any alpha >= 0 and metric M; the function that equals d_{M,alpha} for r != c and 0 otherwise is a proper distance. On MNIST (up to 25,000 digits, SVM classification), Sinkhorn distances with lambda ~ 9/median(M) outperform EMD and all classical histogram distances (Hellinger, chi^2, Total Variation, Gaussian). Computationally, for large histogram dimension d, Sinkhorn distances on CPU are more than 100,000x faster than FastEMD; using a GPU adds another order-of-magnitude speedup. The number of Sinkhorn iterations to convergence increases with lambda but remains modest for practically useful lambda values.

## Relevance to this research
Optimal transport and entropic regularization appear in several threads of the VFE transformer program. The entropic regularization strategy here — converting a hard transport constraint to a KL-penalized convex problem solved by a fixed-point iteration — is structurally analogous to the VFE E-step, where belief updates minimize a KL-regularized free energy functional via iterative Gaussian moment matching. The Sinkhorn-Knopp iteration (alternating scaling of a kernel matrix) is formally dual to softmax attention: the attention weight matrix beta_ij = softmax(score_ij / tau) is itself a doubly-stochastic-like normalization of a kernel exp(score / tau), and the entropic regularization parameter lambda here maps directly to the inverse temperature 1/tau in the VFE attention derivation. Understanding Sinkhorn distances therefore illuminates the information-geometric structure underlying the attention entropy term tau * beta_ij * log(beta_ij / pi_ij) in the VFE free energy. Additionally, the ground-metric parameterization of Sinkhorn distances provides a blueprint for geometry-aware belief coupling: the cost matrix M plays the same structural role as the KL divergence KL(q_i || Omega_ij q_j) in the VFE attention kernel, where the gauge transport Omega_ij encodes the geometric cost of coupling belief q_j to query position i.

## Cross-links
- Concepts: [[Optimal Transport]], [[Entropic Regularization]], [[Information Geometry]], [[Attention Mechanism]]
- Related sources: [[villani-2009-optimal-transport]]
- Manuscript/Project: [[VFE Transformer Program]], [[GL(K) gauge-equivariant attention|GL(K) Attention]]

## BibTeX
```bibtex
@inproceedings{Cuturi2013,
  author    = {Cuturi, Marco},
  title     = {Sinkhorn Distances: Lightspeed Computation of Optimal Transportation Distances},
  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
  year      = {2013},
  eprint    = {1306.0895},
  archivePrefix = {arXiv},
  primaryClass  = {stat.ML},
}
```
