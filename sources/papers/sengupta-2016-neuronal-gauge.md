---
type: paper
title: "Towards a Neuronal Gauge Theory"
aliases:
  - Sengupta 2016
  - Neuronal Gauge Theory
  - sengupta2016neuronal-gauge
  - sengupta2016neuronalgauge
  - sengupta-2016-neuronal-gauge-theory
  - Sengupta et al. 2016
  - Sengupta (2016) Neuronal Gauge Theory
authors:
  - Sengupta, Biswa
  - Tozzi, Arturo
  - Cooray, Gerald K.
  - Douglas, Pamela K.
  - Friston, Karl J.
year: 2016
arxiv: null
url: https://doi.org/10.1371/journal.pbio.1002400
tags:
  - cluster/gauge-theory
  - cluster/vfe
  - cluster/info-geometry
  - cluster/participatory
  - cluster/participatory/consciousness
  - project/multi-agent
  - project/transformer
  - field/neuroscience
  - field/physics
  - field/mathematics
  - field/cs-ml
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Towards a Neuronal Gauge Theory

> [!info] Citation
> Sengupta B, Tozzi A, Cooray GK, Douglas PK, Friston KJ (2016). "Towards a Neuronal Gauge Theory." *PLoS Biology* 14(3): e1002400. doi:10.1371/journal.pbio.1002400

## TL;DR
This essay proposes that the brain and other self-organised biological systems can be characterised via the mathematical apparatus of gauge theory, with variational free energy minimisation serving as the Lagrangian. The core argument is that because variational free energy is a functional of probability distributions, the manifold of sufficient statistics is inherently curved (hyperbolic/Riemannian), and maintaining invariance under local perturbations (sensory stimuli) requires compensatory gauge fields. These gauge fields are identified with precision-weighted prediction errors, and attention emerges as a necessary consequence of the curvature of the information-geometric manifold — in direct analogy to how gravity arises from spacetime curvature.

## Problem & setting
Neuroscience lacks a unifying formal principle analogous to gauge theories in physics (electromagnetism, GR, QFT), which consolidate disparate phenomena under a single invariance framework. The free energy principle (Friston) offers a candidate Lagrangian — variational free energy bounds surprise and drives homeostatic self-organisation — but its relationship to gauge symmetry had not been formalised. Prior work on the Bayesian brain (Knill & Pouget 2004, Ma et al. 2006) and predictive coding (Friston 2010) lacked the differential-geometric and group-theoretic scaffolding that a gauge-theoretic treatment supplies.

## Method
The paper constructs a neuronal gauge theory around three ingredients: (1) a system with continuous symmetry (the nervous system, with sensory entropy / variational free energy as the Lagrangian); (2) local forces (sensory perturbations / prediction errors that break global symmetry locally); (3) gauge fields (precision-weighted compensatory signals that restore Lagrangian invariance). The geometry is developed using information geometry: the manifold of sufficient statistics has negative curvature, so Euclidean gradient descent on free energy is replaced by Riemannian gradient descent weighted by the inverse Fisher information metric. The Cramér-Rao bound enters naturally — perception is optimal only up to asymptotic dispersion. Predictive coding hierarchies are reread as gauge-field compensation: bottom-up messages carry prediction errors (local symmetry-breaking forces), top-down messages are the gauge field that explains them away. Appendices (referenced but not reproduced in the essay) cover: Levi-Civita connections, parallel transport, conjugate gradient descent on manifolds, exponential/logarithmic maps, and Schild's ladder.

Key mathematical relationship: Euclidean gradient descent on the free energy landscape is replaced by
$$\tilde{\nabla} F = G^{-1}(\theta)\,\nabla F$$
where $G(\theta)$ is the Fisher information matrix (the metric tensor), yielding dispersion- and precision-weighted prediction errors. This is the natural gradient (Amari), here given gauge-theoretic interpretation.

## Key results
The paper is primarily theoretical/conceptual rather than empirical, so results are formal arguments:

1. Variational free energy minimisation on a curved (information-geometric) manifold is formally equivalent to a gauge theory, with the Fisher information metric playing the role of the gauge field curvature (Levi-Civita connection).
2. Attention is derived as an emergent necessity: precision-weighting of prediction errors is the neuronal correlate of the gauge field required to maintain Lagrangian invariance under local sensory perturbations. Attention "is a force that manifests from the curvature of information geometry, in exactly the same way that gravity is manifest when the space-time continuum is curved by massive bodies."
3. The Cramér-Rao bound arises naturally — there is a necessary limit to perceptual certainty set by the asymptotic dispersion (inverse Fisher information).
4. Symmetry equivalence classes among generative models: after selecting the best model by VFE, gauge symmetry transformations (via the Levi-Civita connection) generate a family of models with equal model evidence — potentially corresponding to biological species occupying equivalent ecological niches.
5. Hierarchical predictive coding architectures are a natural consequence: at each level, bottom-up prediction errors are local symmetry-breaking forces, and top-down predictions are the gauge field restoring invariance.

## Relevance to this research
This paper is a direct conceptual precursor to the GL(K) gauge-equivariant VFE transformer program. Specific connections:

- **Gauge-equivariant attention**: Sengupta et al. derive attention as a gauge field on the information-geometric manifold. The V3 transformer realises this concretely: GL(K) parallel transport $\Omega_{ij}$ is exactly the gauge field that makes belief coupling $\sum_{ij}\beta_{ij}\,\mathrm{KL}(q_i\|\Omega_{ij}q_j)$ invariant under local (per-token) GL(K) gauge transformations, with $\beta_{ij}$ (softmax attention weights) playing the role of the compensating field.
- **Fisher information / SPD geometry**: The paper's emphasis on the Fisher information metric as the Riemannian metric on the space of sufficient statistics directly motivates the SPD belief geometry in V3, where covariance matrices $\Sigma$ are points on the SPD manifold and distances are Fisher-Rao or log-Euclidean.
- **VFE as Lagrangian**: The essay's proposal that VFE is the gauge-theory Lagrangian is precisely the foundation of the V3 transformer's design — every layer performs iterative VFE minimisation, not a forward pass through learned weights.
- **Precision-weighting and attention**: The identification of attention with precision-weighted prediction errors under the gauge-field interpretation connects to the $\alpha_i$ self-coupling (precision of beliefs relative to priors) and $\beta_{ij}$ coupling weights in the free energy functional.
- **Information geometry and natural gradient**: The replacement of Euclidean gradient descent by Riemannian gradient descent (natural gradient, $G^{-1}\nabla F$) is exactly the E-step update rule in V3's belief geometry.
- **Hierarchical gauge theory**: The nested, hierarchical application of the gauge theory (system $\subset$ environment, recursively) prefigures the multi-agent active inference model (MAgent_Model), where each agent is a gauge-theoretic inference system embedded in a larger one.

## Cross-links
- Concepts: [[Gauge Theory]], [[Variational Free Energy]], [[Information Geometry]], [[Fisher Information Metric]], [[Predictive Coding]], [[Active Inference]], [[Attention as Precision]], [[Riemannian Manifold]], [[Gauge transformation]], [[Parallel transport]], [[Holonomy]], [[Agents as fibre-bundle sections]], [[Participatory realism (it from bit)]]
- Related sources: [[friston-2010-free-energy-principle]], [[amari-2000-information-geometry]], [[friston-2023-active-inference]], [[sengupta2017gauge]] (the technical follow-up, Sengupta & Friston 2017, arXiv:1705.06614, which develops the connection/transport mathematics)
- Manuscript/Project: [[GL(K) Attention Manuscript]], [[VFE Transformer Program]], [[MAgent Model]], [[participatory-it-from-bit]]

> [!note] Framing (from refs/ note): This is the project's **named closest precursor on the gauge–FEP axis** — the explicit proposal that active inference and gauge theory should be unified. Where Sengupta et al. argue *that* the brain admits a gauge description, the project supplies *which* group (GL(K)), *which* connection, and a working multi-agent VFE minimizer respecting gauge equivariance; the participatory reading — physical content is what survives the gauge freedom of any observer's belief frame — extends this paper's invariance principle.

## BibTeX
```bibtex
@article{Sengupta2016NeuronalGauge,
  author  = {Sengupta, Biswa and Tozzi, Arturo and Cooray, Gerald K. and Douglas, Pamela K. and Friston, Karl J.},
  title   = {Towards a Neuronal Gauge Theory},
  journal = {PLoS Biology},
  year    = {2016},
  volume  = {14},
  number  = {3},
  pages   = {e1002400},
  doi     = {10.1371/journal.pbio.1002400},
}
```
