---
type: paper
title: "Sociophysics: A New Approach of Sociological Collective Behaviour. I. Mean-Behaviour Description of a Strike"
aliases: ["Galam, Gefen & Shapir 1982", "Founding sociophysics paper"]
authors: ["Galam S.", "Gefen Y.", "Shapir Y."]
year: 1982
url: https://doi.org/10.1080/0022250X.1982.9989929
tags: [cluster/social-physics, cluster/vfe, project/social-physics, field/physics, field/sociology, cluster/social-physics/opinion-dynamics]
created: 2026-06-19
updated: 2026-06-19
---

# Sociophysics: A New Approach of Sociological Collective Behaviour. I. Mean-Behaviour Description of a Strike

> [!info] Citation
> Galam, S., Gefen, Y., & Shapir, Y. (1982). *Sociophysics: A New Approach of Sociological Collective Behaviour. I. Mean-Behaviour Description of a Strike*. Journal of Mathematical Sociology 9(1), 1-13. DOI: [10.1080/0022250X.1982.9989929](https://doi.org/10.1080/0022250X.1982.9989929).

## TL;DR
This is the founding paper of sociophysics. Galam, Gefen, and Shapir model a collective social decision — whether the workers of a plant go on strike or keep working — by writing down a "dissatisfaction function" for the group and minimizing it, in direct analogy with minimizing the free energy of an Ising magnet. Individual workers are spin-like variables coupled to their colleagues and to external fields (working conditions, salary, social pressure). The mean-field analysis yields a phase structure with a critical point separating a regime of genuinely collective behaviour (a coherent strike or coherent work, like an ordered magnetic phase) from a regime where individuals decide more or less independently (a disordered phase). The paper proposes, for the first time, that the apparatus of statistical mechanics and phase transitions can predict the qualitative states of a social system.

## What it establishes
Each worker carries a two-state variable (strike / work), and the collective dissatisfaction plays the role of a Hamiltonian with pairwise coupling between colleagues and a coupling to external conditions. Within mean-field theory the equilibrium fraction of strikers is the self-consistent minimizer of this functional, and the coupling-versus-field plane contains a critical point: above a critical coupling the group responds collectively and discontinuously (a small change in conditions can trigger an all-or-nothing strike), while below it the response is smooth and individual. The strike is thus an emergent ordered phase, and the transition between collective and individual regimes is a phase transition driven by the strength of inter-worker coupling relative to the external field.

## Relevance to this research
This is the historical origin of treating collective social states through statistical-mechanics free-energy minimization and phase transitions, and it is the conceptual seed of the program's central object: a population whose collective configuration is selected by minimizing a single cost functional. Honestly assessed, the machinery is adjacent rather than identical — a mean-field Ising free energy over binary spins, not a gauge-covariant variational free energy over Gaussian beliefs with transported KL coupling — so the correspondence is genealogical, not a mathematical identity. But as the intellectual progenitor of using a minimized functional to predict consensus and polarization phases, it is core context: the belief-inertia $F$ is the modern, information-geometric descendant of exactly this idea. See [[Sociophysics]], [[Multi-agent variational free energy]], [[Collective active inference]].

## Cross-links
- Concept: [[Discrete spin and majority-rule models of opinion]]
- Related sources: [[galam-1986-majority-rule-hierarchical]], [[castellano-marsili-vespignani-2000-axelrod-transition]]

## BibTeX
```bibtex
@article{galam1982sociophysics,
  author  = {Galam, Serge and Gefen, Yuval and Shapir, Yonathan},
  title   = {Sociophysics: A New Approach of Sociological Collective Behaviour. I. Mean-Behaviour Description of a Strike},
  journal = {Journal of Mathematical Sociology},
  year    = {1982},
  volume  = {9},
  number  = {1},
  pages   = {1--13},
  doi     = {10.1080/0022250X.1982.9989929}
}
```
