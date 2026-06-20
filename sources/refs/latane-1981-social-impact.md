---
type: reference
title: "The Psychology of Social Impact"
aliases:
  - "Latané 1981"
authors:
  - Bibb Latané
year: 1981
tags:
  - cluster/social-physics
  - project/social-physics
  - field/psychology
  - field/sociology
  - cluster/social-physics/social-influence
created: 2026-06-19
updated: 2026-06-19
---

# The Psychology of Social Impact

> [!info] Citation
> Latané, B. (1981). "The Psychology of Social Impact." *American Psychologist* **36**(4), 343–356. DOI: [10.1037/0003-066X.36.4.343](https://doi.org/10.1037/0003-066X.36.4.343).

## TL;DR

Bibb Latané's foundational statement of Social Impact Theory, which posits that the total influence other people exert on an individual is a multiplicative function of three properties of the source population — its strength (status, power, persuasiveness), its immediacy (closeness in space and time), and its number — and that the effect of number grows sublinearly, as a power law with exponent below one, so that each additional person adds progressively less marginal impact. The same multiplicative law, run in reverse, predicts diffusion of responsibility: when many targets share the impact of a single source, the load on each target is divided.

## What it establishes

Latané distills a wide range of social-psychological phenomena — conformity, persuasion, stage fright, bystander intervention, social loafing — into a single quantitative ansatz. Impact $I$ on a target is written as a multiplicative function $I = f(S, I_m, N)$ of the strength $S$, immediacy $I_m$, and number $N$ of the sources, by explicit analogy with physical field laws in which an effect intensifies with the magnitude, proximity, and multiplicity of its sources. The number term is the distinctive empirical claim: impact scales as $I \propto N^{t}$ with $t < 1$, a "psychosocial law" of diminishing returns in which the marginal effect of the $N$th other person is smaller than that of the $(N-1)$th, mirroring the compression of physical intensity in psychophysical power laws.

The theory is deliberately two-sided. When the individual is the target of impact from many sources, influence accumulates (sublinearly) with their number; when the individual is one of many targets jointly receiving impact from a source, the impact is divided among them — the *division of impact* principle that grounds diffusion of responsibility and social loafing. By casting social influence as a field-like quantity sourced by an aggregate of others and decaying with social distance, Latané supplied a compact, parameterized law that later work translated into explicitly spatial and dynamical lattice models of opinion formation, in which agents update under the summed, distance-weighted impact of their neighbors. That dynamical-systems descendant of the theory is what the statistical-physics literature on social dynamics (see [[castellano-fortunato-loreto-2009-social-dynamics]]) carries forward as a many-body model.

> [!note] The page extent is 343–356; "36:343" denotes the opening page.

## Why the project cites it

Social Impact Theory is one of the classical opinion-dynamics models that the **SocialPhysics** program, founded by [[belief-inertia]] ("The Inertia of Belief"), recovers as a limiting case of multi-agent variational-free-energy minimization. In the manuscript's synthesis, the influence one agent exerts on another is the gauge-transported coupling term $\mathrm{KL}(q_i \,\|\, \Omega_{ij}\, q_j)$ in the collective free energy; minimizing $F$ over agent $i$'s belief produces an update in which each neighbor $j$ contributes a pull whose magnitude depends on the coupling weight $\beta_{ij}$. Reading those weights as Latané's strength-and-immediacy factors, and summing the contributions over the $N$ neighbors, reproduces the structure of social impact as an aggregated, distance-weighted field — with the sublinear $N^{t}$ compression emerging from the precision-weighted, saturating form of the variational pull rather than being imposed by hand. The division-of-impact side likewise appears: when a single source's belief is shared as a prior across many targets, the variational coupling distributes the influence, the free-energy analogue of diffusion of responsibility.

The link to [[belief-inertia]]'s distinctive new physics is through [[Belief inertia]] and [[Mass as Fisher information]]. Latané's law specifies the *force* of social influence — how strongly the aggregate of others pushes on a target — but is silent on the target's resistance to being moved. The manuscript supplies that missing factor by reading the Fisher/precision tensor as an inertial mass in a [[Hamiltonian belief dynamics]] ansatz: the same impact field, applied to an agent with belief momentum, produces not the instantaneous overdamped relaxation of the classical theory but oscillation, overshoot, and resonance. Social Impact Theory thus enters the project as the force law whose overdamped (gradient-flow) limit it must reproduce and whose underdamped extension it predicts.

The theory also anchors the project's relational geometry. Latané's strength and immediacy are exactly the social-network weights and distances that the gauge-theoretic treatment encodes in the connection $\Omega_{ij}$ and the coupling graph; treating agents as [[Agents as fibre-bundle sections]] coupled through a [[Gauge transformation]]-covariant connection generalizes Latané's scalar impact field to a geometry-aware influence on a statistical manifold equipped with the [[Fisher information metric]]. Citing Latané (1981) places SocialPhysics in continuity with the [[Sociophysics]] and [[Opinion dynamics]] traditions, and connects to the [[Echo chambers and polarization]] literature, where bounded, distance-weighted impact (cf. [[Bounded confidence]]) drives fragmentation. Within the wider research program, the same impact-as-field intuition recurs in the [[Gauge-Theoretic Multi-Agent VFE Model]], whose Hamiltonian integrator implements the underdamped belief dynamics, and the project as a whole sits beside the [[VFE Transformer Program]] and the [[Free-energy principle active inference]] account of self-organizing agents.

> [!warning] Bibliography flag: the [[belief-inertia]] BibTeX key `latane1981psychology` is referenced in the manuscript text but the entry was missing from `references.bib`. The verified entry below should be added.

```bibtex
@article{latane1981psychology,
  author  = {Latan{\'e}, Bibb},
  title   = {The Psychology of Social Impact},
  journal = {American Psychologist},
  volume  = {36},
  number  = {4},
  pages   = {343--356},
  year    = {1981},
  doi     = {10.1037/0003-066X.36.4.343}
}
```

## Sources / cross-links

- Project page: [[belief-inertia]] · [[SocialPhysics]]
- Concept pages: [[Opinion dynamics]] · [[Sociophysics]] · [[Bounded confidence]] · [[Echo chambers and polarization]] · [[Belief perseverance and confirmation bias]]
- Dynamics concepts: [[Belief inertia]] · [[Mass as Fisher information]] · [[Hamiltonian belief dynamics]]
- Geometry / theory: [[Multi-agent variational free energy]] · [[Fisher information metric]] · [[Agents as fibre-bundle sections]] · [[Gauge transformation]] · [[Variational free energy]] · [[Free-energy principle active inference]]
- Sibling source notes: [[castellano-fortunato-loreto-2009-social-dynamics]] · [[galam-2008-sociophysics]] · [[degroot-1974-consensus]] · [[friedkin-johnsen-1990]] · [[deffuant-2000-bounded-confidence]] · [[hegselmann-krause-2002]]
- Related projects: [[Gauge-Theoretic Multi-Agent VFE Model]] · [[VFE Transformer Program]]
