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
updated: 2026-06-19
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

[[belief-inertia]] recovers bounded confidence not as an exact hard cutoff but as a **soft, finite-temperature analog** of it, and the manuscript is careful to state the claim in exactly those terms: the classical sociological models are obtained from the overdamped (gradient-flow) limit of the same variational-free-energy functional, with bounded-confidence dynamics appearing "as a soft finite-temperature analog rather than an exact hard-threshold limit." The mechanism is the gauge-transported KL coupling and its attention weights. Where HK and Deffuant impose a discontinuous indicator $\mathbf{1}[|x_i - x_j| \le \varepsilon]$ that switches influence fully on or off, the [[Multi-agent variational free energy]] functional weights agent $j$'s pull on agent $i$ by
$$
\beta_{ij} = \mathrm{softmax}_j\!\Big({-\tfrac{1}{\tau}\,\mathrm{KL}\big(q_i \,\|\, \Omega_{ij}\, q_j\big)}\Big),
$$
so the coupling decays *continuously* with the post-transport divergence $\mathrm{KL}(q_i \| \Omega_{ij} q_j)$ rather than vanishing at a wall. Beliefs that are far apart in the [[Fisher information metric]] receive exponentially small weight, which reproduces the qualitative content of a confidence radius — distant opinions are effectively ignored — without the discontinuity. The result is the same phase structure (consensus, polarization, fragmentation) governed now by a smooth competition between the divergence scale and the temperature $\tau$.

This soft reading carries the bounded-confidence intuition into the geometric setting that distinguishes this program. The "distance" that gates influence is not Euclidean opinion difference but a KL divergence on a statistical manifold, transported between agents by the [[Gauge transformation]] $\Omega_{ij}$, so an agent's confidence neighborhood is defined in belief space with its uncertainty structure intact. Cluster formation under bounded confidence then becomes the social-physics face of [[Meta-agents and hierarchical emergence]] and [[Echo chambers and polarization]]: stable camps separated by more than the effective confidence scale are precisely the candidates for coarse-graining into meta-agents.

## Details

The soft-to-hard correspondence is controlled by the temperature $\tau = \kappa\sqrt{K}$. As $\tau \to 0$ the softmax over $-\mathrm{KL}/\tau$ sharpens toward a hard selection rule: weight concentrates on the nearest neighbors and collapses to (near) zero for all others, so the continuous decay approaches an indicator with an effective radius set by where the divergence reaches the prevailing energy scale. This is the **hardening limit** in which the finite-temperature coupling reproduces a confidence cutoff; at any positive $\tau$ the threshold is soft and far-apart agents retain a small but nonzero influence. The correspondence is therefore careful rather than exact — bounded confidence is recovered as the low-temperature shadow of the KL/softmax coupling, and the mapping from $(\tau, \kappa, K)$ to an equivalent $\varepsilon$ is approximate, not an identity. One should not overclaim a derivation of HK or Deffuant; what the framework supplies is a smooth functional whose low-temperature, overdamped limit behaves like bounded confidence and whose finite-temperature behavior is the more faithful model of graded social influence.

The choice between an HK-style synchronous sweep and a Deffuant-style pairwise meeting maps onto the update schedule of the belief dynamics rather than onto the coupling itself: synchronous mean-field updating mirrors HK, while stochastic pairwise interaction mirrors Deffuant, with both sharing the same soft confidence kernel $\beta_{ij}$. The overdamped (first-order, gradient-flow) regime is where these classical models live; the underdamped, [[Hamiltonian belief dynamics]] extension of [[belief-inertia]] adds momentum on top, so a soft-confidence population can overshoot a cluster and oscillate before settling, a behavior absent from the purely dissipative HK and Deffuant rules.

Beyond the agent-based realizations, the same confidence mechanism admits a continuum, statistical-physics reading through the [[Kinetic theory of opinion dynamics]]. Rather than tracking individual agents, one writes a master/rate equation for the opinion density $P(x,t)$ in which only pairs within the confidence range compromise; Ben-Naim, Krapivsky, and Redner ([[ben-naim-2003-bifurcations-compromise]]) solve this kinetic limit and show the long-time state is always a finite set of sharply localized clusters whose count undergoes a regular bifurcation cascade — major clusters interspersed by small "nomadic" minority clusters — as the width of the initial distribution grows. This kinetic-limit signature sharpens the cluster-counting benchmark from a monotone $\sim 1/\varepsilon$ trend (Lorenz) into a structured cascade with critical widths at which the cluster number jumps, giving the soft KL/softmax coupling a more demanding target than mere consensus-versus-fragmentation: at low temperature the gauge-VFE population should settle into a comparable discrete number of belief clusters with the same qualitative dependence on the spread of initial beliefs. The correspondence is at the level of phenomenology and the overdamped regime, since these kinetic and agent-based treatments use scalar opinions and a hard threshold with no gauge transport, belief covariance, or inertia.

## Sources

- [[hegselmann-2002-opinion|hegselmann-krause-2002]] — synchronous bounded-confidence (HK) averaging; consensus, polarization, and fragmentation regimes set by the confidence radius $\varepsilon$.
- [[deffuant2000-bounded-confidence|deffuant-2000-bounded-confidence]] — pairwise asynchronous bounded-confidence (Deffuant-Weisbuch) mixing with convergence parameter $\mu$.
- [[belief-inertia]] — recovers bounded confidence as a soft finite-temperature analog via the KL/softmax coupling, with the overdamped limit as the classical case.
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
