---
type: paper
title: "The Free Energy Principle Made Simpler but Not Too Simple"
aliases:
  - Friston 2023
  - FEP simpler
  - friston-2023-active-inference
  - Friston 2023 active inference
  - Active Inference and Intentional Behaviour
  - friston2023activeinference
  - friston-2023-path-integrals
  - friston2023pathintegrals
  - friston-2022-bayesian-mechanics
  - friston2022bayesianmechanics
  - friston2022free
  - friston-2023-path-integrals-particular-physics
  - friston2023pathintegralsparticularphysics
  - Friston 2023 path integrals
  - friston-2023-path-integrals-active-inference
  - friston2023pathintegralsactiveinference
  - Friston et al. 2023 (Path Integrals)
  - Friston et al. 2023
  - Friston (2023) FEP Made Simpler
authors:
  - Friston, Karl
  - Da Costa, Lancelot
  - Sajid, Noor
  - Heins, Conor
  - Ueltzhöffer, Kai
  - Pavliotis, Grigorios A.
  - Parr, Thomas
year: 2023
arxiv: "2201.06387"
url: https://arxiv.org/abs/2201.06387
tags:
  - cluster/vfe
  - cluster/participatory
  - cluster/participatory/consciousness
  - cluster/info-geometry
  - project/multi-agent
  - project/transformer
  - field/physics
  - field/neuroscience
  - field/mathematics
  - field/biology
  - field/statistics
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# The Free Energy Principle Made Simpler but Not Too Simple

> [!info] Citation
> Friston, K., Da Costa, L., Sajid, N., Heins, C., Ueltzhöffer, K., Pavliotis, G. A., & Parr, T. (2023). "The free energy principle made simpler but not too simple." *Physics Reports*, **1024**, 1–29. DOI: [10.1016/j.physrep.2023.07.001](https://doi.org/10.1016/j.physrep.2023.07.001). arXiv:2201.06387.

## TL;DR
This paper provides a concise, pedagogically accessible derivation of the free energy principle (FEP), starting from random dynamical systems expressed as a Langevin equation and arriving at a Bayesian mechanics interpretable as a physics of sentience. The derivation proceeds through (i) establishing a particular partition of states via conditional independencies from sparse coupling, (ii) unpacking the Bayesian inference implications of that partition, and (iii) describing the paths of particular states via a variational principle of least action. The FEP offers a normative account of self-organisation as self-evidencing — the maximisation of Bayesian model evidence.

## Problem & setting
The free energy principle has a reputation for being difficult to understand, despite resting on straightforward results from statistical physics. The paper addresses this gap by presenting the FEP as simply as possible without sacrificing technical rigor. Prior accounts scattered across multiple publications are synthesised here, with simplifications that replace earlier treatments. The starting question is: if things exist (in the sense of having a pullback attractor and a nonequilibrium steady-state density), what dynamics must they possess?

## Method
The derivation begins with the Langevin equation for a random dynamical system with Gaussian white noise (covariance $2\Gamma$) and uses both the Fokker-Planck (forward Kolmogorov) equation and the path-integral formulation. The key steps are:

1. **NESS density**: For a system to persist as a "thing," the Fokker-Planck density must reach a nonequilibrium steady-state (NESS), admitting a Helmholtz decomposition of the flow into solenoidal (curl-free) and gradient components relative to the surprisal $\mathfrak{I}(x) = -\ln p(x)$:
$$\dot{p}(x)=0 \;\Leftrightarrow\; f(x) = Q(x)\nabla\mathfrak{I}(x) - \Gamma\nabla\mathfrak{I}(x) - \Lambda(x),$$
where $Q=-Q^T$ encodes solenoidal (non-equilibrium) circulation.

2. **Particular partition**: Sparse coupling — absence of Jacobian coupling $J_{uv}=0$ — implies via the Hessian of surprisal that two states are conditionally independent if one does not influence the other. This yields a partition into external ($\eta$), sensory ($s$), active ($a$), and internal ($\mu$) states, with the Markov blanket $b=(s,a)$ separating internal from external states: $({\mu} \perp {\eta})\mid b$.

3. **Bayesian mechanics**: The conditional independence of internal and external paths (given blanket paths) means internal states must encode a recognition density over external states. Minimising variational free energy — the negative ELBO — with respect to internal states constitutes active inference: internal states act to minimise surprisal about sensory states.

## Key results
The paper establishes that sparse coupling in a random dynamical system with a NESS density is necessary and sufficient for the existence of a particular partition (Markov blanket structure). From this partition, internal dynamics can be interpreted as performing variational Bayesian inference over external states, with active states modulating sensory input to reduce surprisal. The path-integral formulation shows that internal and external paths are conditionally independent given blanket paths and initial conditions, without needing to invoke the NESS density explicitly. This provides a clean, self-contained derivation of the FEP that unifies it with quantum, statistical, and classical mechanics via the same Langevin/Fokker-Planck starting point.

## Relevance to this research
This paper is the primary theoretical substrate for the multi-agent active inference framework underlying the VFE transformer program. The particular partition (Markov blanket) formalism directly motivates the hierarchical belief structure in the VFE free energy functional — the $h \to s \to p \to q \to o$ hierarchy mirrors the FEP's internal/blanket/external partition at multiple scales. The NESS density and Helmholtz decomposition (solenoidal + gradient flow) are the statistical-physics foundation for the variational free energy $F$ used in the VFE transformer, where minimisation of $F$ with respect to Gaussian belief tuples $(\mu, \Sigma, \phi)$ is the E-step. The path-integral / least-action variational principle is directly analogous to the variational principle that underlies Bayesian mechanics in the transformer setting. The nonequilibrium (solenoidal) flow distinguishing NESS from equilibrium also has bearing on gauge-theoretic structure: solenoidal flow is divergence-free in state space, resonating with gauge-covariant transport in the GL(K) attention mechanism.

## Cross-links
- Concepts: [[Variational Free Energy]] [[Markov Blanket]] [[Active Inference]] [[Nonequilibrium Steady State]] [[Bayesian Mechanics]] [[Hamiltonian belief dynamics]] [[Belief inertia]] [[Markov blanket interpretation debate]] [[Natural gradient]] [[Fisher information metric]]
- Related sources: [[friston-2022-bayesian-mechanics]] [[parr-2022-active-inference-book]] [[friston-2019-particular-physics]] [[dacosta-2021-bayesian-mechanics]] [[parr-2020-markov-blankets-thermodynamics]] [[ramstead-2023-bayesian-mechanics]]
- Manuscript/Project: [[VFE Transformer Program]] [[GL(K) Attention]]

## BibTeX
```bibtex
@article{Friston2023PhysReports,
  author  = {Friston, Karl and Da Costa, Lancelot and Sajid, Noor and Heins, Conor and Ueltzhöffer, Kai and Pavliotis, Grigorios A. and Parr, Thomas},
  title   = {The free energy principle made simpler but not too simple},
  journal = {Physics Reports},
  volume  = {1024},
  pages   = {1--29},
  year    = {2023},
  doi     = {10.1016/j.physrep.2023.07.001},
  publisher = {Elsevier},
  note    = {arXiv:2201.06387},
}
```
