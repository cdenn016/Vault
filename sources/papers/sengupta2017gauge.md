---
type: paper
title: "Approximate Bayesian inference as a gauge theory"
aliases:
  - Sengupta 2017
  - ABI gauge theory
  - sengupta-friston-2017-bayesian-gauge-theory
  - Sengupta & Friston 2017
  - Sengupta-Friston (2017) Bayesian Gauge Theory
authors:
  - Sengupta, Biswa
  - Friston, Karl
year: 2017
arxiv: "1705.06614"
url: https://arxiv.org/abs/1705.06614
tags:
  - cluster/gauge-theory
  - cluster/vfe
  - cluster/info-geometry
  - cluster/participatory
  - cluster/participatory/consciousness
  - project/transformer
  - project/multi-agent
  - field/neuroscience
  - field/mathematics
  - field/physics
  - field/cs-ml
  - field/statistics
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Approximate Bayesian inference as a gauge theory

> [!info] Citation
> Sengupta, B. & Friston, K. (2017). "Approximate Bayesian inference as a gauge theory." ICML 2017 Computational Biology Workshop, Sydney, Australia. arXiv:1705.06614.

> [!note] Editorial (provenance, resolved 2026-06-19): This 2017 preprint (arXiv:1705.06614) is the technical follow-up to [[sengupta-2016-neuronal-gauge]] ("Towards a Neuronal Gauge Theory," *PLoS Biology*) and is the project's most direct gauge–FEP precursor. The "belief-state synchronization" paper the domain brief tentatively listed *does* exist and is a **distinct** work: Sengupta & Friston, "How Belief States Get Synchronized through Active Inference" (arXiv:1810.08750), carried in the manuscript bibliography under key `SenguptaFriston2018`. Manuscript-side check (GL(K) peer review, 2026-06-19): the `GL(K)_attention.tex` body cited **no** Sengupta work; `references.bib` held `Sengupta2016NeuronalGauge` and the 2018 synchronization entry but **not** this 1705.06614 gauge-theory preprint. `Participatory_it_from_bit.tex` cites the 2016 and 2018 entries. Fix applied: 1705.06614 added to the manuscript bib under key `sengupta2017gauge` and cited in the GL(K) Introduction.

## TL;DR

This paper casts approximate Bayesian inference — specifically variational free-energy minimization — as a gauge theory in which the Lagrangian is the entropy of sensory samples (upper-bounded by variational free energy). The central novel contribution is an algorithm for parallel transport of sufficient statistics (means, covariances) on a statistical manifold using Schild's ladder, enabling Riemannian conjugate gradient descent on the free-energy landscape without requiring knowledge of the ambient tangent structure. Attention is identified as the cognitive correlate of precision-weighting that emerges from the curvature of the information-geometric manifold.

## Problem & setting

The paper addresses how neuronal dynamics can be formalized as gauge-invariant optimization on a curved statistical manifold. Prior variational inference schemes (e.g., generalized Bayesian filtering in SPM) use Fisher-scoring — pre-multiplying the free-energy gradient by the inverse Fisher information metric — but treat the manifold as locally Euclidean and do not explicitly handle the non-commutativity of tangent vectors across different base points. The problem of conjugate gradient descent on a Riemannian manifold requires parallel-transporting previous descent directions to the current tangent space, which in turn requires a connection (gauge field). The paper builds on Sengupta et al. (2016, PLoS Biology) which proposed a neuronal gauge theory but did not provide the full computational algorithm.

## Method

The free-energy Lagrangian `L = -ln p(s)` is minimized by bounding surprise with variational free energy `F(s, θ)` where `θ = {μ, Σ}` are the sufficient statistics of a Gaussian approximate posterior. The Fisher information metric `g_ij(θ)` gives the Riemannian structure, so that gradient descent becomes the natural gradient `∇̃F = g^{-1}(θ) ∇F`, and the symmetric KL divergence provides the local distance:

```
KL_sym(θ, θ') ≈ dθ^T g(θ) dθ
```

Conjugate gradient descent on the manifold requires transporting the previous descent direction `H_{i-1}` (living in a different tangent space) to the current tangent space before forming the linear combination `H_i = -G_i + β H_{i-1}`. The paper implements this via **Schild's ladder**: starting from `θ_I` and `θ_F` on the geodesic, one iteratively constructs midpoints using the Riemannian exponential and logarithmic maps

```
exp_θ(A) = θ^{1/2} exp(θ^{-1/2} A θ^{-1/2}) θ^{1/2}
log_θ(A) = θ^{1/2} log(θ^{-1/2} A θ^{-1/2}) θ^{1/2}
```

to shuttle the vector field along the geodesic without requiring the Christoffel symbols explicitly. The Levi-Civita connection plays the role of the gauge field compensating for local perturbations to the Lagrangian.

## Key results

The paper establishes three main conceptual-theoretical results rather than empirical benchmarks. First, the free-energy Lagrangian is invariant under reparametrization of the approximate distribution, identifying gauge symmetry as reparametrization invariance and the gauge fields as the Levi-Civita connections that compensate local perturbations (prediction errors) to keep the Lagrangian invariant. Second, attention is formally derived as the cognitive manifestation of precision-weighting, itself a consequence of the Cramér-Rao bound on the curved information manifold — the bound means perception cannot be more optimal than the inverse Fisher information (asymptotic dispersion), and attention arises as the force that exploits or adjusts this curvature. Third, the Schild's ladder algorithm achieves discrete parallel transport of sufficient statistics without an ambient space, and Riemannian conjugate gradient descent differs from its Euclidean counterpart only at third order near convergence, implying quadratic convergence near extrema.

## Relevance to this research

This paper is a direct conceptual ancestor of the V3_Transformer's gauge-equivariant attention architecture. The identification of attention with precision-weighting arising from information-geometric curvature provides the Fristonian FEP grounding for the GL(K) gauge-equivariant transport used in the VFE transformer: the GL(K) parallel transport `Ω_{ij}` in the VFE free energy is the discretization of the Levi-Civita connection described here. The exponential/logarithm maps on SPD matrices (equations 4 above) are precisely the retraction operations used in the SPD belief geometry of the VFE transformer. The Schild's ladder construction for transporting sufficient statistics is conceptually equivalent to the VFE3 transport of `(μ, Σ)` belief tuples across the attention graph. The gauge-theoretic identification of the Lagrangian with variational free energy anticipates the manuscript GL(K)_attention.tex's treatment of the VFE functional as a gauge-invariant objective. The paper also motivates the hierarchical extension of gauge theory (each level a separate Markov blanket) that underlies the multi-agent active inference program.

## Cross-links

- Concepts: [[Gauge Theory]], [[Variational Free Energy]], [[Information Geometry]], [[Parallel Transport]], [[Fisher Information Metric]], [[Schild's Ladder]], [[Precision weighting|Attention as Precision-Weighting]], [[Gauge transformation]], [[Holonomy]], [[Agents as fibre-bundle sections]], [[Participatory realism (it from bit)]]
- Related sources: [[sengupta-2016-neuronal-gauge]] (the 2016 PLoS Biology predecessor), [[friston-2010-free-energy-principle|friston2010free-energy]]
- Manuscript/Project: [[gl-k-attention|GL(K) Attention Manuscript]], [[VFE Transformer Program]], [[participatory-it-from-bit]], [[Multi-agent variational free energy]]

## BibTeX

```bibtex
@article{sengupta2017gauge,
  author  = {Sengupta, Biswa and Friston, Karl},
  title   = {Approximate {B}ayesian inference as a gauge theory},
  journal = {ICML 2017 Computational Biology Workshop},
  year    = {2017},
  note    = {arXiv:1705.06614},
}
```
