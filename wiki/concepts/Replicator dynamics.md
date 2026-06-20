---
type: concept
title: "Replicator dynamics"
aliases:
  - "Replicator equation"
  - "Evolutionary game dynamics"
  - "Selection dynamics"
  - "Replicator-mutator dynamics"
tags: [cluster/social-physics, project/social-physics]
status: stable
created: 2026-06-19
updated: 2026-06-19
---

# Replicator dynamics

## Definition

**Replicator dynamics** is the canonical continuous-time selection equation of evolutionary game theory: it describes how the relative frequencies of competing strategies in a large population change over time when strategies reproduce in proportion to the payoff (fitness) they earn against the current population mix. The state is a frequency vector $x = (x_1, \dots, x_n)$ living on the probability simplex $\Delta^{n-1}$, and the dynamics is
$$
\dot{x}_i = x_i\left[(Ax)_i - x^\top A x\right],
$$
where $A$ is the payoff matrix, $(Ax)_i$ is the fitness of strategy $i$ against the current population, and $x^\top A x$ is the population mean fitness. The bracket is a frequency-weighted comparison to the mean: a strategy whose fitness exceeds the population average grows, one below it shrinks, and the simplex is invariant because the per-capita growth rates are measured relative to the mean. The equation was derived by [[taylor-jonker-1978-replicator-dynamics]] to supply the dynamical foundation that the static **evolutionarily stable strategy** (ESS) concept of [[maynard-smith-price-1973-logic-animal-conflict]] had initially lacked, and the rigorous dynamical-systems theory — fixed points, limit cycles, permanence, the equivalence to Lotka-Volterra ecology, and the folk theorem linking Nash equilibria and ESS to rest points and their stability — is developed in the standard reference [[hofbauer-sigmund-1998-evolutionary-games-population-dynamics]]. The ESS itself, introduced through the hawk-dove game where injury cost exceeding resource value ($C > V$) makes the stable outcome a mixed strategy with Hawk frequency $p^* = V/C$, is the population-level uninvadability criterion that anchors the equilibrium side of the theory.

## Why it matters here

The connection to the SocialPhysics / [[belief-inertia]] program runs at two strengths, and they should not be conflated. The strong link is geometric. The replicator equation is not merely a first-order flow that happens to resemble the program's overdamped opinion-dynamics limit; it is a **natural-gradient flow** — the gradient ascent of mean fitness with respect to the **Shahshahani metric**, which is exactly the restriction of the [[Fisher information metric]] to the probability simplex ([[hofbauer-sigmund-1998-evolutionary-games-population-dynamics]]). That places replicator dynamics inside the same information-geometric family as the program's core machinery: in both cases an objective is descended (or ascended) along the [[Natural gradient]] of an information metric rather than the naive Euclidean gradient. The program's [[Multi-agent variational free energy]] flow is precisely a natural-gradient descent of free energy on a [[Statistical manifold]], so replicator dynamics is a genuine relative — the same mathematical idea on a different manifold. The honest caveat is the manifold: the Shahshahani/Fisher flow of selection lives on the **discrete simplex of strategy frequencies**, whereas the belief-inertia model flows on the **SPD/Gaussian manifold of $(\mu, \Sigma)$** with GL(K)-gauge-transported KL coupling $\mathrm{KL}(q_i \| \Omega_{ij}[q_j])$. So the equations are cousins sharing a metric philosophy, not the same equation, and the gauge-transport structure that defines the program has no counterpart in the plain replicator setting.

The weaker links are conceptual and parallel rather than mechanical. The replicator equation is a **first-order (overdamped)** population flow, so it sits on the same side of the program's central dichotomy as DeGroot, Friedkin-Johnsen, and bounded-confidence models ([[Opinion dynamics]]) — it is a dissipative selection dynamics with no inertial term, and it therefore *cannot* produce the oscillation, overshoot, and momentum transfer that the program's underdamped ansatz claims as its novel signature ([[Hamiltonian belief dynamics]], [[Mass as Fisher information]]). Promoting replicator dynamics to second order (reading a Fisher/precision tensor as inertial mass) would be the EGT analogue of the belief-inertia move, but that is the program's contribution, not something the classical replicator literature does. Finally, the ESS of [[maynard-smith-price-1973-logic-animal-conflict]] is the population-level **fixed-point / stable-configuration** notion of EGT, and it parallels — by intuition, not by identity — the program's interest in stable consensus configurations as gradient-flow rest points. The belief-inertia machinery characterizes stability through flow rest points and Fisher-inertia rather than through uninvadability against mutants, so this is adjacent vocabulary, not shared theorem. Replicator dynamics belongs to the broader theme of the [[Statistical physics of social systems and collective behavior]] as a foundational selection-dynamics neighbor of the program's overdamped recovery results.

## Details

The replicator equation arose to dynamize a static concept. [[maynard-smith-price-1973-logic-animal-conflict]] asked why animal contests are so often ritualized rather than escalated to injury, and answered with the ESS: a strategy is evolutionarily stable if, adopted by most of a population, no mutant strategy can invade — formally, the resident does at least as well against itself as any mutant does against it, with strict advantage breaking ties. In the hawk-dove game with resource value $V$ and injury cost $C$, neither pure Hawk nor pure Dove is an ESS when $C > V$; the stable state is the mixed strategy (or polymorphism) at Hawk frequency $p^* = V/C$, which explains restraint as equilibrium rather than as group-level benevolence. This gives a fixed-point notion but no account of how a population reaches it.

[[taylor-jonker-1978-replicator-dynamics]] supplied that account by writing the selection flow $\dot{x}_i = x_i[(Ax)_i - x^\top A x]$ and proving the central bridge theorem: **every ESS is an asymptotically stable rest point** of the replicator dynamics. The converse fails in general — there are asymptotically stable rest points that are not ESS — so the dynamic and static pictures agree but are not identical, and the ESS is best read as a sufficient condition for dynamic stability. [[hofbauer-sigmund-1998-evolutionary-games-population-dynamics]] then develops the full mathematical structure: the replicator equation on $\Delta^{n-1}$ is diffeomorphic to a Lotka-Volterra system in one lower dimension, tying evolutionary game dynamics to the predator-prey and competition equations of mathematical ecology; the **folk theorem** organizes the equilibrium correspondences (Nash equilibria are rest points; strict Nash equilibria and ESS are asymptotically stable; the limits of convergent interior trajectories are Nash); and **permanence** characterizes when every strategy persists rather than going extinct. The textbook also makes the information-geometric face explicit through the **Shahshahani inner product**, under which the replicator equation is the gradient flow of mean fitness — the cleanest single statement of why selection is a Fisher/natural-gradient flow on the simplex, and the precise sense in which it is kin to the program's natural-gradient VFE descent. Variants the textbook treats (replicator-mutator, imitation, best-response, and adjustment dynamics) extend the same skeleton to learning and cultural transmission, which is the doorway through which replicator-type equations enter social rather than strictly biological modeling, alongside the opinion-dynamics models the program recovers in [[Opinion dynamics]].

## Sources

- [[taylor-jonker-1978-replicator-dynamics]] — derives the replicator equation and proves every ESS is an asymptotically stable rest point of the flow.
- [[hofbauer-sigmund-1998-evolutionary-games-population-dynamics]] — authoritative dynamical-systems treatment: Lotka-Volterra equivalence, the folk theorem, permanence, and the Shahshahani-gradient (Fisher/natural-gradient) structure of selection.
- [[maynard-smith-price-1973-logic-animal-conflict]] — founds evolutionary game theory and the ESS via the hawk-dove game; the population-level fixed-point concept the dynamics later anchors.

## See also

- [[Multi-agent variational free energy]] — the program's natural-gradient flow on the statistical manifold; the Fisher-flow relative of the replicator equation.
- [[Fisher information metric]] · [[Natural gradient]] — the Shahshahani metric is the simplex restriction of the Fisher metric, under which replicator dynamics is a gradient flow.
- [[Opinion dynamics]] — the other overdamped first-order population flows the program recovers; replicator dynamics sits on the same dissipative side.
- [[Hamiltonian belief dynamics]] · [[Mass as Fisher information]] — the underdamped/inertial regime that first-order replicator dynamics cannot reach.
- [[Statistical manifold]] — the SPD/Gaussian manifold the program flows on, versus the discrete simplex of replicator dynamics.
- [[belief-inertia]] · [[Sociophysics]] · [[SocialPhysics]] — the founding manuscript, the broader tradition, and the project hub.
