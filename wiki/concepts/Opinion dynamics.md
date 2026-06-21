---
type: concept
title: "Opinion dynamics"
aliases:
  - "Opinion dynamics"
  - "Social learning dynamics"
  - "Opinion formation"
  - "Social Opinion Dynamics"
tags:
  - cluster/social-physics
  - cluster/multi-agent
  - project/social-physics
  - project/multi-agent
status: stable
created: 2026-06-19
updated: 2026-06-19
---

# Opinion dynamics

## Taxonomy

The most current broad map of the field is the survey of [[noorazar-2020-opinion-dynamics-survey]], which organizes the whole opinion-dynamics landscape along two axes: the state space of an opinion (binary or finite-discrete versus continuous) and the update mechanism (full averaging, confidence-gated averaging, pairwise imitation, majority rule, persuasion). The discrete-state branch holds the imitation and spin models — the [[Voter model]] and its kin, where an agent copies the opinion of a randomly chosen neighbor, together with Sznajd and majority-rule variants — and the closely related [[Threshold models and complex contagion|threshold and complex-contagion models]], where adoption fires only once a sufficient fraction of neighbors has already switched. The continuous branch holds the averaging models treated below (DeGroot, Friedkin–Johnsen) and the bounded-confidence family ([[Bounded confidence]]). Cutting across both is the continuum-limit machinery the survey points to as the analytical face of these microscopic rules: the [[Kinetic theory of opinion dynamics|kinetic theory]] that derives Boltzmann- and Fokker–Planck-type equations for the opinion density from binary-interaction rules, the [[Mean-field games and continuum limits|mean-field-game]] reading in which each agent best-responds to the population distribution, and [[Replicator dynamics]], the evolutionary-game flow that governs competition between discrete opinions or strategies. This taxonomy supplies the checklist of collective behaviours — consensus, clustering into a few groups, full fragmentation — that any unifying functional, including the [[Multi-agent variational free energy]] of [[belief-inertia]], must reproduce, and it flags the open frontiers (online-network structure, stubborn or zealot agents, the spread of misinformation) where the gauge-theoretic framing might add value beyond reproduction.

## Definition

**Opinion dynamics** is the study of how opinions, attitudes, or beliefs evolve in a population of coupled agents, where each agent updates its position by some rule that mixes its own view with the views of the others it is connected to. The classical models share a common skeleton — a network of trust or influence, a fixed point or attractor structure, and an update map applied repeatedly — but differ in the boundary conditions they impose. In **DeGroot social learning** ([[degroot-1974-consensus]]) every agent replaces its opinion with a weighted average of its neighbors' opinions, $x_i(t+1) = \sum_j W_{ij}\, x_j(t)$ with a row-stochastic trust matrix $W$; under mild connectivity the iteration converges to consensus, the stationary distribution of the Markov chain $W$. **Friedkin–Johnsen opinion dynamics** ([[friedkin1990-social-influence-opinions|friedkin-johnsen-1990]], [[friedkin-johnsen-2011-social-influence-network]]) breaks unanimous consensus by anchoring each agent to its *initial* opinion: $x_i(t+1) = \lambda_i \sum_j W_{ij}\, x_j(t) + (1-\lambda_i)\, x_i(0)$, where the susceptibility $\lambda_i$ trades off social conformity against stubborn attachment to one's starting belief, so the equilibrium is generally a persistent diversity of opinions rather than a single point. **Bounded-confidence** models (Hegselmann–Krause, Deffuant) make the influence weights themselves opinion-dependent — an agent averages only over neighbors whose opinions lie within a confidence radius — which produces clustering into several stable opinion groups rather than global consensus, and is treated separately in [[Bounded confidence]].

## Why it matters here

These models matter to this project because [[belief-inertia]] derives each of them as the **overdamped (gradient-flow) limit** of [[Multi-agent variational free energy]] with gauge-transported KL coupling. When agents carry Gaussian beliefs and disagreement is measured by the gauge-covariant divergence $\mathrm{KL}(q_i \,\|\, \Omega_{ij}[q_j])$, the first-order descent $\dot\mu_i \propto -\partial F/\partial\mu_i$ of the coupling term $\sum_{ij}\beta_{ij}\,\mathrm{KL}(q_i\|\Omega_{ij}[q_j])$ reduces, in the scalar-belief flat-connection limit, to exactly the DeGroot averaging law, with the [[Attention mechanisms — theory and positional structure|softmax attention weights]] $\beta_{ij}$ playing the role of the influence/trust matrix $W_{ij}$. Adding the self-coupling term $\alpha\,\mathrm{KL}(q_i\|p_i)$ that anchors each belief to its prior reproduces the Friedkin–Johnsen anchoring term, with the precision ratio $\alpha/(\alpha+\sum_j\beta_{ij})$ acting as the complement of the susceptibility $\lambda_i$. The consequence drawn out in the manuscript is that consensus and polarization are not separate phenomena requiring separate models but one principle under different boundary conditions: tune the prior anchoring, the confidence structure of the attention weights, and the connection, and the same free-energy descent moves between global agreement, persistent disagreement, and fragmentation into [[Echo chambers and polarization|echo chambers]].

A distinctive feature of the gauge-theoretic reading is that the influence weights are not postulated but **emergent**. In DeGroot and Friedkin–Johnsen the matrix $W$ is exogenous; here $\beta_{ij} = \mathrm{softmax}_j(-\mathrm{KL}(q_i\|\Omega_{ij}[q_j])/(\kappa\sqrt{K}))$ is determined by the current beliefs themselves, so trust is endogenous and opinion-dependent — agents weight most heavily those neighbors they already agree with after transport. This makes the bounded-confidence phenomenology continuous rather than thresholded: the soft attention kernel smoothly down-weights distant opinions where Hegselmann–Krause imposes a hard cutoff.

## Details

The averaging skeleton of opinion dynamics is the same object that appears in two adjacent literatures the wiki already tracks. **Opinion pooling** asks how to aggregate several agents' distributions into one consensus distribution: linear pooling (a weighted arithmetic mean of densities) is the distributional lift of DeGroot averaging, while logarithmic pooling (a weighted geometric mean, normalized) is its multiplicative counterpart and corresponds to combining beliefs by summing natural-parameter vectors ([[genest-zidek-1986-pooling]], [[dietrich-list-2016-opinion-pooling]], [[bordley-1982-multiplicative-pooling]]). The KL-coupling term of [[Multi-agent variational free energy]] sits between these: minimizing $\sum_j \beta_{ij}\,\mathrm{KL}(q_i\|\Omega_{ij}[q_j])$ over $q_i$ yields, for fixed weights, the logarithmic (multiplicative) pool of the transported neighbor beliefs — the variational fixed point of belief coupling is precisely a weighted geometric mean of the neighbors' transported distributions, which recovers DeGroot averaging in the mean and a precision-weighted combination in the covariance.

**Consensus on networks** is the control-theoretic face of the same averaging dynamics. Olfati-Saber's consensus protocols ([[olfati-saber-2007-consensus]]) write the continuous-time averaging flow as $\dot x = -L x$ with $L$ the graph Laplacian, whose convergence rate is set by the algebraic connectivity (the Fiedler value, [[fiedler-1973-algebraic-connectivity]]); this is the linearization of the gradient flow of the coupling energy about a consensus state, and it ties the speed of opinion convergence to the spectral structure of the attention graph. The same Laplacian governs whether the population splits — a small algebraic connectivity, or a community structure in the influence graph ([[Community detection and modularity]]), signals the onset of metastable opinion clusters and the emergence of [[Meta-agents and hierarchical emergence|meta-agents]] from tightly-coupled subgroups.

## Sources

- [[noorazar-2020-opinion-dynamics-survey]] — current broad survey mapping the discrete, averaging, and bounded-confidence model families into one taxonomy.
- [[degroot-1974-consensus]] — DeGroot social learning: repeated linear averaging over a trust matrix; the canonical consensus model.
- [[friedkin1990-social-influence-opinions|friedkin-johnsen-1990]] — Friedkin–Johnsen opinion dynamics with anchoring to initial opinions; the origin of persistent disagreement.
- [[friedkin-johnsen-2011-social-influence-network]] — social-influence-network theory; the matured Friedkin–Johnsen framework and susceptibility parameterization.
- [[genest-zidek-1986-pooling]] — linear and logarithmic opinion pooling; the belief-aggregation theory underlying the coupling fixed point.
- [[dietrich-list-2016-opinion-pooling]] — axiomatic foundations of probabilistic opinion pooling.
- [[bordley-1982-multiplicative-pooling]] — multiplicative (logarithmic) pooling formula; the natural-parameter combination rule.
- [[olfati-saber-2007-consensus]] — consensus protocols on networks; Laplacian dynamics and convergence on graphs.
- [[fiedler-1973-algebraic-connectivity]] — algebraic connectivity and the spectral bound on consensus speed.

## See also

- [[belief-inertia]] — derives the classical opinion-dynamics models as overdamped limits of gauge-theoretic VFE.
- [[Multi-agent variational free energy]] — the functional whose gradient flow yields the averaging dynamics.
- [[Bounded confidence]] — opinion-dependent influence and clustering into stable groups.
- [[Echo chambers and polarization]] — the fragmented, consensus-failing regime of the same dynamics.
- [[Sociophysics]] · [[SocialPhysics]] — the broader programme and the founding project page.
- [[Collective active inference]] — the active-inference reading of coupled belief-updating populations.
- [[Attention mechanisms — theory and positional structure]] — the softmax weights that play the role of the influence/trust matrix.
- [[Community detection and modularity]] · [[Meta-agents and hierarchical emergence]] — when the population fractures into opinion clusters.
- [[Voter model]] · [[Threshold models and complex contagion]] — the discrete-state imitation and adoption branch of the taxonomy.
- [[Kinetic theory of opinion dynamics]] · [[Mean-field games and continuum limits]] · [[Replicator dynamics]] — the continuum-limit and evolutionary-game machinery for the same microscopic rules.
