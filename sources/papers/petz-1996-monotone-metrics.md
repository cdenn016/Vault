---
type: paper
title: "Monotone Metrics on Matrix Spaces"
aliases:
  - Petz 1996
  - Petz monotone metrics
  - Petz (1996) Monotone Metrics
authors:
  - Petz, Dénes
year: 1996
arxiv: null
url: https://doi.org/10.1016/0024-3795(94)00211-8
tags:
  - cluster/info-geometry
  - cluster/participatory
  - cluster/participatory/quantum-foundations
  - project/transformer
  - project/multi-agent
  - field/mathematics
  - field/physics
  - field/statistics
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Monotone Metrics on Matrix Spaces

> [!info] Citation
> Petz, D. (1996). "Monotone Metrics on Matrix Spaces." *Linear Algebra and Its Applications*, 244, 81–96.

## TL;DR
Petz characterizes all monotone Riemannian metrics on the space of density matrices (the quantum state space) by establishing a one-to-one correspondence between such metrics and operator monotone functions. The main result shows that any monotone metric can be expressed via an operator-valued positive superoperator built from an operator monotone function, vastly generalizing earlier partial results of Morozova–Chentsov. It follows that all candidate metrics proposed by Morozova and Chentsov are indeed monotone.

## Problem & setting
The quantum state space for an $n$-level system is identified with the set $\mathcal{D}_n$ of positive definite $n\times n$ density matrices of trace one. A Riemannian metric on $\mathcal{D}_n$ is called *monotone* (or *quantum Fisher information metric*) if it is non-increasing under completely positive stochastic (trace-preserving) maps — the quantum analog of the classical requirement that a statistical metric be non-increasing under sufficient statistics. The Hilbert–Schmidt (Frobenius) inner product $\langle A,B\rangle = \mathrm{Tr}(A^*B)$ is unitarily invariant but is not monotone. Morozova and Chentsov initiated the study and proposed several candidate monotone metrics but could not prove monotonicity for their proposals. Prior to this work the only fully established monotone metric on $\mathcal{D}_n$ was the unique (up to scale) Markovian-invariant metric on classical probability simplices (the Fisher information metric); the quantum analog lacked a systematic theory.

## Method
Petz works in the inner-product space $\mathcal{M}_n$ of all complex $n\times n$ matrices with the Hilbert–Schmidt scalar product. A metric is written in the form $\mathbf{K}_\rho(A,B) = \mathrm{Tr}(A^*\, \mathbf{J}_\rho^{-1} B)$ where $\mathbf{J}_\rho$ is a positive (super)operator on $\mathcal{M}_n$ depending on the base-point density matrix $\rho$. The key operators are the left and right multiplication superoperators $\mathbf{L}_\rho$ and $\mathbf{R}_\rho$. Monotonicity of the metric under stochastic maps reduces to a *transformer inequality* $\Phi^*\mathbf{J}_{\Phi(\rho)}\Phi \geq \mathbf{J}_\rho$ for every stochastic map $\Phi$. Petz shows that this holds if and only if the superoperator $\mathbf{J}_\rho$ takes the form

$$\mathbf{J}_\rho = \mathbf{R}_\rho\, f(\mathbf{L}_\rho \mathbf{R}_\rho^{-1})$$

for an *operator monotone function* $f : \mathbb{R}^+ \to \mathbb{R}^+$ satisfying the symmetry condition $f(t) = t f(t^{-1})$. The proof uses the theory of operator means (Kubo–Ando), quasi-entropy methods (Petz 1986), and the quasi-entropy inequality from the earlier paper on Cramér–Rao in the quantum setting. An explicit one-to-one (affine) correspondence is established between normalized monotone metrics and symmetric operator monotone functions.

## Key results
The main theorem (Theorem 1 and its converse, Theorem 5) states: every monotone metric on $\mathcal{D}_n$ is of the form $\mathbf{K}_\rho(A,B) = \mathrm{Tr}(A^* \mathbf{J}_\rho^{-1} B)$ with $\mathbf{J}_\rho = \mathbf{R}_\rho f(\mathbf{L}_\rho\mathbf{R}_\rho^{-1})$, where $f$ is a symmetric operator monotone function. Conversely, every such $f$ yields a monotone metric. This gives an *abundance* of monotone metrics parameterized by the cone of symmetric operator monotone functions. Specific metrics recovered include: (i) the Bures–Helstrom metric ($f(t)=(1+t)/2$, arithmetic mean, smallest monotone metric); (ii) the Bogoliubov–Kubo–Mori metric / logarithmic mean metric ($f(t)=(t-1)/\log t$, harmonic-logarithmic mean); (iii) the metric from the right logarithmic derivative ($f(t)=t$, largest monotone metric). The Morozova–Chentsov function $m(\lambda,\mu)=1/f(\lambda/\mu)\mu$ relates to the inverse. There is a one-to-one correspondence between symmetric operator means and symmetric monotone metrics; under this correspondence the Bures/SLD member ($f(t)=(1+t)/2$, arithmetic mean) is the **smallest** monotone metric and the right-logarithmic-derivative member ($f(t)=t$) is the **largest**, with the Bogoliubov–Kubo–Mori metric lying strictly between. All five candidates of Morozova–Chentsov are confirmed monotone. The symmetrized metric ($f(t)=2t/(1+t)$, harmonic mean) is also monotone, being related to the Bogoluibov metric via symmetrization.

## Relevance to this research
This paper is foundational for the **information geometry of SPD/density-matrix belief states** in the VFE transformer. In the GL(K) gauge-equivariant attention model, belief states are Gaussian tuples $(\mu, \Sigma, \phi)$ with $\Sigma$ a symmetric positive definite matrix. The monotone metrics characterized here are exactly the quantum analogs of the Fisher–Rao metric on SPD belief manifolds; the operator-monotone-function parameterization of metrics directly mirrors the family of divergences and retractions configurable in the VFE codebase (the `divergence` and `retraction` registries). The Kubo–Ando operator mean structure underlying Petz's theorem is related to the SPD geodesics and parallel transport (gauge connection) used in the VFE belief coupling term $\sum_{ij}\beta_{ij}\mathrm{KL}(q_i \| \Omega_{ij} q_j)$. The smallest monotone metric (Bures) and its connection to quantum Cramér–Rao bounds are relevant to understanding the information-geometric optimality of the VFE minimization. The correspondence between operator monotone functions and Riemannian metrics on state spaces also informs the theoretical basis for the `f-divergence` module choices in the codebase.

## Cross-links
- Concepts: [[SPD-manifold geometry and Riemannian optimization|SPD Geometry]], [[Information Geometry]], [[Fisher Information Metric]], [[Operator Monotone Functions]], [[Quantum information geometry]]
- Related sources: [[amari-1985-differential-geometric-methods|amari-1985-differential-geometry]], [[uhlmann-1976-transition-probability]], [[braunstein-caves-1994-quantum-fisher]], [[cencov-1982-statistical-decision-rules]]
- Manuscript/Project: [[VFE Transformer Program]], [[GL(K) gauge-equivariant attention|GL(K) Attention]], [[participatory-it-from-bit]]

> [!note] Editorial: For the participatory/quantum-foundations thread, this classification is the foil to the *classical* Čencov uniqueness theorem ([[cencov-1982-statistical-decision-rules]]): in the quantum extension, metric uniqueness fails — a metric must be *chosen* from the monotone family (most naturally the minimal Bures/SLD member, via [[braunstein-caves-1994-quantum-fisher]]), so PIFB cannot transplant the classical "the geometry is forced" rhetoric unchanged.

## BibTeX
```bibtex
@article{Petz1996,
  author  = {Petz, D{\'e}nes},
  title   = {Monotone Metrics on Matrix Spaces},
  journal = {Linear Algebra and Its Applications},
  year    = {1996},
  volume  = {244},
  pages   = {81--96},
  doi     = {10.1016/0024-3795(94)00211-8},
}
```
