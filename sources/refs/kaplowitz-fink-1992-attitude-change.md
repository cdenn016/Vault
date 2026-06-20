---
type: reference
title: "A Spatial-Linkage Model of the Dynamics of Attitude Change / Oscillation in Beliefs"
aliases:
  - "Kaplowitz & Fink 1992"
  - "Fink, Kaplowitz & Hubbard 2002"
  - "Kaplowitz-Fink attitude dynamics"
authors:
  - Stan A. Kaplowitz
  - Edward L. Fink
  - Susan M. Hubbard
year: 1992
tags:
  - cluster/social-physics
  - project/social-physics
  - field/psychology
  - field/physics
  - cluster/social-physics/social-influence
created: 2026-06-19
updated: 2026-06-19
---

# A Spatial-Linkage Model of the Dynamics of Attitude Change / Oscillation in Beliefs

> [!info] Citation
> Kaplowitz, S. A., & Fink, E. L. (1992). "Dynamics of Attitude Change." In R. L. Levine & H. E. Fitzgerald (Eds.), *Analysis of Dynamic Psychological Systems, Vol. 2: Methods and Applications* (pp. 341–369). New York: Plenum. DOI: [10.1007/978-1-4615-6440-9_14](https://doi.org/10.1007/978-1-4615-6440-9_14).
>
> Companion synthesis: Fink, E. L., Kaplowitz, S. A., & Hubbard, S. M. (2002). "Oscillation in Beliefs and Decisions." In J. P. Dillard & M. Pfau (Eds.), *The Persuasion Handbook: Developments in Theory and Practice* (pp. 17–37). Thousand Oaks, CA: Sage.
>
> [!note] Identifier check: the 1992 Plenum chapter carries the Springer chapter DOI `10.1007/978-1-4615-6440-9_14` (book DOI `10.1007/978-1-4615-6440-9`), verified to resolve. The 2002 Sage handbook chapter has no DOI registered in the sources consulted; page range `17–37` is reported by Sage but a few catalogues list `17–38`.

## TL;DR

The Kaplowitz-Fink program treats an attitude not as a quantity that relaxes monotonically toward a persuasive message but as a *dynamical variable with inertia*: when a discrepant message displaces a belief, the belief can overshoot its eventual resting point and settle through a series of damped oscillations rather than a smooth approach. Across two decades of theory and experiment, the authors model attitude change as the trajectory of a mass on a spring — a second-order system in which the observed wavering, overshoot, and settling time are signatures of momentum, restoring force, and damping — and report empirical belief trajectories that exhibit exactly these damped-oscillatory patterns, with oscillation amplitude rising under more credible or more discrepant messages and correlating positively with the magnitude of final change.

## What it establishes

The starting observation is that classical attitude-change theory, built on information-integration and weighted-averaging accounts, predicts a *monotone* approach to a new equilibrium: a message moves the attitude part-way toward its position, and repeated or stronger messages move it further, but the attitude never passes its target and swings back. Kaplowitz and Fink argue this is an artifact of treating attitude dynamics as first-order (overdamped) relaxation. Their alternative is explicitly mechanical. An attitude is modeled as a particle whose position is the current belief, subject to a restoring force toward an equilibrium set by the integrated information, a damping force, and — the decisive addition — an inertial term, so that the governing equation is second-order in time. The resulting trajectory is the familiar damped harmonic oscillator: depending on the damping ratio it approaches equilibrium monotonically (overdamped), critically, or through decaying oscillations (underdamped), and only the underdamped regime produces overshoot.

The spatial-linkage component generalizes this from a single attitude to a *system* of linked beliefs. Rather than a strict hierarchy in which superordinate attitudes drive subordinate ones top-down, the spatial-linkage model embeds beliefs as points in a multidimensional cognitive space (the Galileo framework) in which any two associated concepts exert force on each other regardless of hierarchical rank; a message that moves one belief propagates through the linkages and sets neighboring beliefs oscillating as well. The empirical work — pursued through the 1980s and synthesized in the 2002 handbook chapter and later *Communication Monographs* studies — sampled belief positions densely in time after a persuasive message and fit oscillatory trajectories, finding damped oscillation, finding that amplitude grew with source credibility and message discrepancy, and reporting a positive amplitude-to-final-change relationship (on the order of $r \approx 0.45$). The throughline is that the second-order, inertial description is not a metaphor but a fitted dynamical model whose oscillatory predictions distinguish it from every first-order account.

## Why the project cites it

This is the empirical anchor for the central novel claim of [[belief-inertia]]. The manuscript's distinctive move is to read the Fisher/precision tensor of a belief as an inertial **mass** ([[Mass as Fisher information]]) and to write a Hamiltonian, rather than purely gradient-flow, dynamics for beliefs on a statistical manifold — see [[Belief inertia]] and [[Hamiltonian belief dynamics]]. That move has a sharp, falsifiable consequence: where the overdamped (gradient-flow) limit recovers the classical sociophysics and opinion-dynamics models exactly, the *underdamped* (Hamiltonian) regime predicts phenomena that first-order models structurally cannot produce — oscillation, overshoot, resonance, and momentum transfer between coupled agents. The Kaplowitz-Fink line is the place in the existing human-attitude literature where precisely those signatures — damped oscillation and overshoot following a persuasive perturbation — have already been observed and modeled with a second-order equation of motion.

The correspondence is structural rather than a borrowed result. Kaplowitz and Fink posit a phenomenological mass-spring-damper for a scalar (or low-dimensional spatial) attitude and fit its parameters; [[belief-inertia]] *derives* a second-order dynamics from the geometry of the [[Fisher information metric]] on the manifold of belief distributions, with the inertial term supplied by the precision tensor rather than assumed. Their underdamped trajectories are thus a concrete, decades-old human-subjects instance of the regime the project's Hamiltonian ansatz predicts, and the overdamped case they contrast against is the same first-order limit in which [[Multi-agent variational free energy]] minimization reproduces DeGroot, Friedkin-Johnsen, and bounded-confidence dynamics ([[degroot-1974-consensus]], [[friedkin-johnsen-1990]], [[hegselmann-krause-2002]], [[deffuant-2000-bounded-confidence]]). Citing this work lets the manuscript point to existing evidence that belief inertia is not merely a formal possibility opened by the geometry but a measured feature of real attitude change — while being honest that the gauge-theoretic, multi-agent generalization of it (momentum transfer across [[Agents as fibre-bundle sections]] coupled by transported KL) remains the not-yet-empirically-validated extension. The reference also supplies the spatial-linkage picture of beliefs-as-points-in-a-space whose mutual forces propagate change, a finite-dimensional precursor to the project's [[SocialPhysics]] treatment of coupled agents on a shared manifold ([[Opinion dynamics]], [[Belief perseverance and confirmation bias]]).

## Sources / cross-links

- Founding manuscript: [[belief-inertia]] ("The Inertia of Belief")
- Project: [[SocialPhysics]]
- Core concepts: [[Belief inertia]] · [[Hamiltonian belief dynamics]] · [[Mass as Fisher information]] · [[Fisher information metric]] · [[Multi-agent variational free energy]]
- Domain concepts: [[Opinion dynamics]] · [[Sociophysics]] · [[Belief perseverance and confirmation bias]]
- Overdamped-limit companions: [[degroot-1974-consensus]] · [[friedkin-johnsen-1990]] · [[hegselmann-krause-2002]] · [[deffuant-2000-bounded-confidence]] · [[galam-2008-sociophysics]]
- Sibling new notes (this build): [[kaplowitz-fink-1992-attitude-change|self]] · [[castellano-fortunato-loreto-2009-social-dynamics]] · [[flache-2017-social-influence-models]] · [[friedkin-johnsen-2011-social-influence-network]] · [[strogatz-2015-nonlinear-dynamics]]

```bibtex
@incollection{kaplowitz1992dynamics,
  author    = {Kaplowitz, Stan A. and Fink, Edward L.},
  title     = {Dynamics of Attitude Change},
  booktitle = {Analysis of Dynamic Psychological Systems, Vol. 2: Methods and Applications},
  editor    = {Levine, Ralph L. and Fitzgerald, Hiram E.},
  pages     = {341--369},
  publisher = {Plenum Press},
  address   = {New York},
  year      = {1992},
  doi       = {10.1007/978-1-4615-6440-9_14}
}

@incollection{fink2002oscillation,
  author    = {Fink, Edward L. and Kaplowitz, Stan A. and Hubbard, Susan M.},
  title     = {Oscillation in Beliefs and Decisions},
  booktitle = {The Persuasion Handbook: Developments in Theory and Practice},
  editor    = {Dillard, James Price and Pfau, Michael},
  pages     = {17--37},
  publisher = {Sage},
  address   = {Thousand Oaks, CA},
  year      = {2002},
  note      = {No DOI located; page range 17--37 per Sage, some catalogues list 17--38}
}
```
