---
type: paper
title: "Towards a Geometry and Analysis for Bayesian Mechanics"
aliases:
  - "Sakthivadivel 2022"
  - "Bayesian Mechanics Geometry"
authors:
  - Sakthivadivel, Dalton A R
year: 2022
arxiv: "2204.11900"
url: https://arxiv.org/abs/2204.11900
tags:
  - cluster/vfe
  - cluster/gauge-theory
  - cluster/info-geometry
  - project/multi-agent
  - field/physics
  - field/mathematics
  - field/cs-ml
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Towards a Geometry and Analysis for Bayesian Mechanics

> [!info] Citation
> Sakthivadivel, D. A. R. (2022). "Towards a Geometry and Analysis for Bayesian Mechanics." arXiv:2204.11900 [math-ph]. https://arxiv.org/abs/2204.11900

## TL;DR
This paper formulates a simple case of Bayesian mechanics under the free energy principle (FEP) in axiomatic terms, grounding it in differential geometry, functional calculus, and category theory. The central results show that approximate Bayesian inference is equivalent to constrained entropy maximisation, that the constraints constitute a gauge degree of freedom, and that the drive to remain self-organised can be read as a gauge force acting on the system. The work provides a formal, proof-based path towards Bayesian mechanics as a field theory of complex self-organising systems.

## Problem & setting
The theory of complex systems lacks a formal, mathematical foundation comparable to classical mechanics. While the free energy principle offers a promising inferential account of self-organisation, its mathematical articulation has remained informal or heuristic. This paper asks what a formal geometric and analytic foundation for the FEP would look like, drawing on dynamical systems theory, statistical mechanics, differential geometry, and gauge field theory. The prior art includes the random-dynamical-systems formulation of Friston (2019) and Da Costa et al. (2021), which this work extends and partially formalises.

## Method
The paper proceeds in three main steps. First, it establishes that constrained maximum entropy (the Shannon entropy functional $S[p; J] = -\int \ln\{p(x)\}p(x)\,dx - \sum_k \lambda_k\bigl(\int J_k(x)p(x)\,dx - C_k\bigr)$) is an equivalent language for the FEP: approximate Bayesian inference equals gradient ascent on entropy under a constraint (Theorems 4.1 and 4.2). Second, it uses geometric notions from dynamical systems theory to show that this constraint serves as a potential for the inferential process and is the generator of a gradient flow (Theorems 4.3 and 6.2). Third, it connects constraints to gauge symmetry: the constraints on a system's states constitute a gauge degree of freedom, and the tendency to remain self-organised acts on probabilistic dynamics exactly as a gauge field interacts with a matter field (Theorem 6.1). The Shannon entropy functional is recast as the action of a semi-classical field theory, with the Lagrangian $\mathcal{L} = (f(\phi) + V)\phi$ providing the direct analogy to classical least-action variational calculus.

## Key results
The three principal theorems are: (1) approximate Bayesian inference is equivalent to entropy maximisation under an appropriate constraint (Theorems 4.1–4.2); (2) this constraint acts as a Lyapunov potential driving a gradient flow on entropy (Theorems 4.3 and 6.2); and (3) the constraint shapes inferential dynamics exactly as a gauge field couples to a matter field (Theorem 6.1). Additionally, Theorem 4.4 addresses the propagation of Markov blankets (the "passing down" of system-ness), and Section 6.3 provides results on non-equilibrium steady states under this gauge-theoretic framing. The paper also formally classifies FEP systems into four subclasses (stationary/non-stationary crossed with inert/adaptive) and gives worked examples (stone at equilibrium, control circuits, life-like systems).

## Relevance to this research
This paper is directly relevant to the gauge-theoretic VFE transformer program on multiple levels. The core claim — that the constraints on a self-organising system constitute a gauge degree of freedom and generate a gauge force — is the conceptual precursor to the GL(K) gauge-equivariant attention mechanism, where gauge symmetry in the belief-coupling transport is the architectural foundation. The equivalence between free energy minimisation and constrained entropy maximisation provides formal grounding for the VFE objective used throughout the V3 transformer. The field-theoretic Lagrangian formulation of maximum entropy (Section 5) is mathematically consonant with the variational free energy functional in the manuscripts, including the KL coupling terms and the attention-entropy regulariser. The category-theoretic duality between system and environment (Section 2.3) connects to the multi-agent active inference framing and the hyper-prior / model / belief hierarchy ($h \to s \to p \to q$). The non-equilibrium steady-state results (Section 6.3) are relevant to understanding the stability of belief dynamics in the transformer at convergence.

## Cross-links
- Concepts: [[Variational Free Energy]], [[Gauge Theory]], [[Free Energy Principle]], [[Information Geometry]], [[Markov Blanket]], [[Maximum Entropy]]
- Related sources: [[friston2019-free-energy-principle]], [[da-costa2021-bayesian-mechanics]]
- Manuscript/Project: [[VFE Transformer Program]], [[GL(K) Attention]]

## BibTeX
```bibtex
@article{Sakthivadivel2022,
  author  = {Sakthivadivel, Dalton A R},
  title   = {Towards a Geometry and Analysis for {B}ayesian Mechanics},
  year    = {2022},
  eprint  = {2204.11900},
  archivePrefix = {arXiv},
  primaryClass  = {math-ph},
  url     = {https://arxiv.org/abs/2204.11900},
}
```
