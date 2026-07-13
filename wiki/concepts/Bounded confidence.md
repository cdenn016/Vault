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
updated: 2026-07-13
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

The authoritative consolidation of this family is the survey by Lorenz ([[lorenz-2007-bounded-confidence-survey]]), which unifies the HK and Deffuant-Weisbuch variants under a single framework and treats both as positive linear (averaging) systems with state-dependent, opinion-gated coupling. Lorenz's organizing empirical law makes the cluster-counting behavior quantitative: large $\varepsilon$ yields one consensus, decreasing $\varepsilon$ produces an increasing number of distinct clusters — roughly $\sim 1/(2\varepsilon)$ for HK on a uniform initial distribution — and very small $\varepsilon$ gives fragmentation into many isolated views. This consolidated phenomenology, the number of surviving clusters as a function of the confidence threshold, is precisely the benchmark any subsuming VFE functional must reproduce.

## Why it matters here

The current theorem-first record [[belief-inertia-2026-07-12-theorem-first-revision]] gives only a **soft, finite-temperature analog** of bounded confidence, not an overdamped recovery of HK or Deffuant. Where those models impose a discontinuous indicator $\mathbf{1}[|x_i-x_j|\le\varepsilon]$, [[Multi-agent variational free energy]] weights source $j$ by
$$
\beta_{ij} = \mathrm{softmax}_j\!\Big({-\tfrac{1}{\tau}\,\mathrm{KL}\big(q_i \,\|\, \Omega_{ij}\, q_j\big)}\Big),
$$
so coupling decays continuously with post-transport divergence rather than vanishing at a confidence wall. At every positive $\tau$ and positive candidate prior, distant sources retain nonzero weight. This supports graded similarity selectivity, but it does not prove the HK/Deffuant phase structure, stable polarization, or fragmentation.

This soft reading carries bounded-confidence intuition into a geometric setting: selectivity depends on transported KL divergence between distributions rather than only Euclidean opinion difference. Any persistent camps or meta-agent coarse-graining require additional support truncation, anchors, repulsion, or active sampling; they do not follow from the positive soft kernel alone ([[Meta-agents and hierarchical emergence]], [[Echo chambers and polarization]]).

## Details

Temperature $\tau$ controls the sharpness of the Gibbs selector. As $\tau\to0$, weight concentrates on minimum-energy candidates. That nearest-source argmin is not an HK ball average and does not supply a fixed confidence radius: multiple sources within a radius are not averaged merely because they lie below a threshold. Exact bounded confidence would require hard support or an explicit thresholded candidate set. The low-temperature limit is therefore a sharper selector, not a theorem that recovers HK or Deffuant.

Synchronous and pairwise schedules can be used as comparison protocols, but choosing such a schedule does not make the underlying update identical to HK or Deffuant. A conditional [[Hamiltonian belief dynamics]] extension may be studied only after a separate kinetic metric and damping law are specified; overshoot is not a consequence of the soft-confidence analogy.

Beyond the agent-based realizations, the same confidence mechanism admits a continuum, statistical-physics reading through the [[Kinetic theory of opinion dynamics]]. Rather than tracking individual agents, one writes a master/rate equation for the opinion density $P(x,t)$ in which only pairs within the confidence range compromise; Ben-Naim, Krapivsky, and Redner ([[ben-naim-2003-bifurcations-compromise]]) solve this kinetic limit and show the long-time state is always a finite set of sharply localized clusters whose count undergoes a regular bifurcation cascade — major clusters interspersed by small "nomadic" minority clusters — as the width of the initial distribution grows. This kinetic-limit signature sharpens the cluster-counting benchmark from a monotone $\sim 1/\varepsilon$ trend (Lorenz) into a structured cascade with critical widths at which the cluster number jumps, giving the soft KL/softmax coupling a more demanding target than mere consensus-versus-fragmentation: at low temperature the gauge-VFE population should settle into a comparable discrete number of belief clusters with the same qualitative dependence on the spread of initial beliefs. The correspondence is at the level of phenomenology and the overdamped regime, since these kinetic and agent-based treatments use scalar opinions and a hard threshold with no gauge transport, belief covariance, or inertia.

## Sources

- [[hegselmann-2002-opinion|hegselmann-krause-2002]] — synchronous bounded-confidence (HK) averaging; consensus, polarization, and fragmentation regimes set by the confidence radius $\varepsilon$.
- [[deffuant2000-bounded-confidence|deffuant-2000-bounded-confidence]] — pairwise asynchronous bounded-confidence (Deffuant-Weisbuch) mixing with convergence parameter $\mu$.
- [[belief-inertia-2026-07-12-theorem-first-revision]] — current source for the soft-analog status and explicit exclusion of an exact HK/Deffuant recovery.
- [[belief-inertia-2026-07-13-final-verification-addendum]] — final-panel confirmation of that soft-analog boundary.
- [[lorenz-2007-bounded-confidence-survey]] — authoritative survey unifying the HK and Deffuant-Weisbuch variants, with the consolidated cluster-count-vs-$\varepsilon$ phenomenology.
- [[ben-naim-2003-bifurcations-compromise]] — kinetic rate-equation treatment whose steady-state cluster count undergoes a bifurcation cascade as the initial spread grows.

## See also

- [[Opinion dynamics]]
- [[Kinetic theory of opinion dynamics]]
- [[Echo chambers and polarization]]
- [[SocialPhysics]]
- [[Multi-agent variational free energy]]
- [[Fisher information metric]]
- [[Hamiltonian belief dynamics]]
- [[Meta-agents and hierarchical emergence]]
