---
type: concept
title: "Bounded confidence"
aliases:
  - "Bounded-confidence dynamics"
  - "Hegselmann-Krause model"
  - "Deffuant-Weisbuch model"
  - "Confidence threshold"
tags:
  - cluster/social-physics
  - project/social-physics
status: stable
created: 2026-06-19
updated: 2026-11-18
---

# Bounded confidence

## Definition

**Bounded confidence** names a family of opinion-dynamics models in which agents influence one another only when their current opinions lie within a fixed tolerance, the *confidence threshold* $\varepsilon$. Unlike unconditional averaging models, where every agent pulls on every other, bounded-confidence agents simply ignore opinions too far from their own, so the interaction structure is state-dependent: the set of who listens to whom changes as opinions move. This single nonlinearity is enough to turn a homogenizing averaging rule into one that can hold a population apart, producing consensus, polarization into a few stable camps, or fragmentation into many isolated clusters depending on the threshold and the initial distribution.

Two canonical realizations differ in their update schedule. The **Hegselmann-Krause (HK)** model ([[hegselmann-2002-opinion|hegselmann-krause-2002]]) is synchronous: at each step every agent $i$ replaces its scalar opinion with the mean of all opinions inside its confidence set $I(i,x) = \{ j : |x_i - x_j| \le \varepsilon \}$,
$$
x_i(t+1) = \frac{1}{|I(i,x(t))|} \sum_{j \in I(i,x(t))} x_j(t).
$$
The **Deffuant-Weisbuch** model ([[deffuant2000-bounded-confidence|deffuant-2000-bounded-confidence]]) is pairwise and asynchronous: at each step a random pair $(i,j)$ meets, and if $|x_i - x_j| \le \varepsilon$ they each move a fraction $\mu$ of the way toward the other,
$$
x_i \leftarrow x_i + \mu\,(x_j - x_i), \qquad x_j \leftarrow x_j + \mu\,(x_i - x_j),
$$
while encounters across the threshold leave both unchanged. HK mixes whole neighborhoods at once and tends to coarsen quickly into a handful of clusters; Deffuant mixes one dyad at a time and traces a slower, more stochastic path to a similar cluster structure. In both, the number of surviving opinion clusters scales roughly inversely with $\varepsilon$: a wide confidence window collapses the population to consensus, a narrow one fixes many camps, and the transition between regimes is sharp rather than gradual.

The authoritative consolidation of this family is the survey by Lorenz ([[lorenz-2007-bounded-confidence-survey]]), which unifies the HK and Deffuant-Weisbuch variants under a single framework and treats both as positive linear (averaging) systems with state-dependent, opinion-gated coupling. Lorenz's organizing empirical law makes the cluster-counting behavior quantitative: large $\varepsilon$ yields one consensus, decreasing $\varepsilon$ produces an increasing number of distinct clusters — roughly $\sim 1/(2\varepsilon)$ for HK on a uniform initial distribution — and very small $\varepsilon$ gives fragmentation into many isolated views.

## Details

Beyond the agent-based realizations, the same confidence mechanism admits a continuum, statistical-physics reading through the [[Kinetic theory of opinion dynamics]]. Rather than tracking individual agents, one writes a master/rate equation for the opinion density $P(x,t)$ in which only pairs within the confidence range compromise; Ben-Naim, Krapivsky, and Redner ([[ben-naim-2003-bifurcations-compromise]]) solve this kinetic limit and show the long-time state is always a finite set of sharply localized clusters whose count undergoes a regular bifurcation cascade — major clusters interspersed by small "nomadic" minority clusters — as the width of the initial distribution grows.

## Sources

- [[hegselmann-2002-opinion|hegselmann-krause-2002]] — synchronous bounded-confidence (HK) averaging; consensus, polarization, and fragmentation regimes set by the confidence radius $\varepsilon$.
- [[deffuant2000-bounded-confidence|deffuant-2000-bounded-confidence]] — pairwise asynchronous bounded-confidence (Deffuant-Weisbuch) mixing with convergence parameter $\mu$.
- [[lorenz-2007-bounded-confidence-survey]] — authoritative survey unifying the HK and Deffuant-Weisbuch variants, with the consolidated cluster-count-vs-$\varepsilon$ phenomenology.
- [[ben-naim-2003-bifurcations-compromise]] — kinetic rate-equation treatment whose steady-state cluster count undergoes a bifurcation cascade as the initial spread grows.

## See also

- [[Opinion dynamics]]
- [[Cellular sheaves and sheaf Laplacians]] — bounded confidence on discourse sheaves, whose equilibria are global sections of the below-threshold subsheaf.
- [[Kinetic theory of opinion dynamics]]
- [[Echo chambers and polarization]]
- [[Fisher information metric]]

