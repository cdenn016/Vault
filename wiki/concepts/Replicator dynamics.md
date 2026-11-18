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
updated: 2026-11-18
---

# Replicator dynamics

## Definition

**Replicator dynamics** is the canonical continuous-time selection equation of evolutionary game theory: it describes how the relative frequencies of competing strategies in a large population change over time when strategies reproduce in proportion to the payoff (fitness) they earn against the current population mix. The state is a frequency vector $x = (x_1, \dots, x_n)$ living on the probability simplex $\Delta^{n-1}$, and the dynamics is
$$
\dot{x}_i = x_i\left[(Ax)_i - x^\top A x\right],
$$
where $A$ is the payoff matrix, $(Ax)_i$ is the fitness of strategy $i$ against the current population, and $x^\top A x$ is the population mean fitness. The bracket is a frequency-weighted comparison to the mean: a strategy whose fitness exceeds the population average grows, one below it shrinks, and the simplex is invariant because the per-capita growth rates are measured relative to the mean. The equation was derived by [[taylor-jonker-1978-replicator-dynamics]] to supply the dynamical foundation that the static **evolutionarily stable strategy** (ESS) concept of [[maynard-smith-price-1973-logic-animal-conflict]] had initially lacked, and the rigorous dynamical-systems theory — fixed points, limit cycles, permanence, the equivalence to Lotka-Volterra ecology, and the folk theorem linking Nash equilibria and ESS to rest points and their stability — is developed in the standard reference [[hofbauer-sigmund-1998-evolutionary-games-population-dynamics]]. The ESS itself, introduced through the hawk-dove game where injury cost exceeding resource value ($C > V$) makes the stable outcome a mixed strategy with Hawk frequency $p^* = V/C$, is the population-level uninvadability criterion that anchors the equilibrium side of the theory.

## Information geometry

The replicator equation is a **natural-gradient flow**: the gradient ascent of mean fitness with respect to the **Shahshahani metric**, which is exactly the restriction of the [[Fisher information metric]] to the probability simplex ([[hofbauer-sigmund-1998-evolutionary-games-population-dynamics]]). Selection is therefore an ascent along the [[Natural gradient]] of an information metric rather than the naive Euclidean gradient.

## Details

The replicator equation arose to dynamize a static concept. [[maynard-smith-price-1973-logic-animal-conflict]] asked why animal contests are so often ritualized rather than escalated to injury, and answered with the ESS: a strategy is evolutionarily stable if, adopted by most of a population, no mutant strategy can invade — formally, the resident does at least as well against itself as any mutant does against it, with strict advantage breaking ties. In the hawk-dove game with resource value $V$ and injury cost $C$, neither pure Hawk nor pure Dove is an ESS when $C > V$; the stable state is the mixed strategy (or polymorphism) at Hawk frequency $p^* = V/C$, which explains restraint as equilibrium rather than as group-level benevolence. This gives a fixed-point notion but no account of how a population reaches it.

[[taylor-jonker-1978-replicator-dynamics]] supplied that account by writing the selection flow $\dot{x}_i = x_i[(Ax)_i - x^\top A x]$ and proving the central bridge theorem: **every ESS is an asymptotically stable rest point** of the replicator dynamics. The converse fails in general — there are asymptotically stable rest points that are not ESS — so the dynamic and static pictures agree but are not identical, and the ESS is best read as a sufficient condition for dynamic stability. [[hofbauer-sigmund-1998-evolutionary-games-population-dynamics]] then develops the full mathematical structure: the replicator equation on $\Delta^{n-1}$ is diffeomorphic to a Lotka-Volterra system in one lower dimension, tying evolutionary game dynamics to the predator-prey and competition equations of mathematical ecology; the **folk theorem** organizes the equilibrium correspondences (Nash equilibria are rest points; strict Nash equilibria and ESS are asymptotically stable; the limits of convergent interior trajectories are Nash); and **permanence** characterizes when every strategy persists rather than going extinct. The textbook also makes the information-geometric face explicit through the **Shahshahani inner product**, under which the replicator equation is the gradient flow of mean fitness — the cleanest statement of why selection is a Fisher/natural-gradient flow on the simplex. Variants such as replicator-mutator, imitation, best-response, and adjustment dynamics connect evolutionary games to social learning.

## Sources

- [[taylor-jonker-1978-replicator-dynamics]] — derives the replicator equation and proves every ESS is an asymptotically stable rest point of the flow.
- [[hofbauer-sigmund-1998-evolutionary-games-population-dynamics]] — authoritative dynamical-systems treatment: Lotka-Volterra equivalence, the folk theorem, permanence, and the Shahshahani-gradient (Fisher/natural-gradient) structure of selection.
- [[maynard-smith-price-1973-logic-animal-conflict]] — founds evolutionary game theory and the ESS via the hawk-dove game; the population-level fixed-point concept the dynamics later anchors.

## See also

- [[Fisher information metric]] · [[Natural gradient]] — the Shahshahani metric is the simplex restriction of the Fisher metric, under which replicator dynamics is a gradient flow.
- [[Opinion dynamics]] — first-order averaging models of social influence; replicator dynamics is an adjacent selection model.
- [[Statistical manifold]] — the general information-geometric setting; replicator dynamics lives on the discrete simplex.
- [[Sociophysics]] — the broader tradition.
