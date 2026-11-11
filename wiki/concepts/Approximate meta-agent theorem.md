---
type: concept
title: "Approximate meta-agent theorem"
aliases:
  - "Approximate H5a"
  - "Excess relative entropy of a Markov filter"
  - "Memory of a level-0 average"
tags:
  - cluster/multi-agent
  - cluster/vfe
  - project/multi-agent
status: draft
created: 2026-11-11
updated: 2026-11-11
---

# Approximate meta-agent theorem

## Definition

A meta-agent is a set of agents that is itself an agent: it has coarse internal, sensory, active and external states, its external states obey a law of their own given its act, and its internal states encode a belief about them (see [[Meta-agents and hierarchical emergence]]). In the linear-Gaussian framework of the collective-agents manuscript this holds exactly under hypotheses that include exact closure of the coarse exterior and of the coarse internal state. The approximate meta-agent theorem is the family of statements in [[dennis-2026-collective-agents-approximate-meta-agent]] that replace exact closure by a declared coarse model with a measured defect and bound the resulting errors.

The declared model asserts that a retained variable $y=Cx$ of a fine process $x_{t+1}=Ax_t+Bu_t+\mathfrak n_t$ obeys $y_{t+1}=\bar Ay_t+\bar Bu_t+\hat w_t$. Its closure defect is $D=CA-\bar AC$ and its input defect is $E=CB-\bar B$. The quantity bounded for the belief is the excess relative entropy, the expected relative entropy from the exact predictive law of $y_t$ given the record to the belief of the stationary [[Kalman filter]] of the declared model.

## Why it matters here

[[Coarse Graining]] generically produces memory, so a summary of many agents is closed only in special cases, and a theory in which collectives are agents needs to say what a collective that models a non-closed summary with a Markov law loses. Before these results the manuscript had separate bounds for the blanket, for the memory of the exterior and for agency, and an error term for the belief that held only under a smallness condition. The results summarized here give an error term without that condition, assemble it with the exact parts into one theorem, and treat the case in which the internal summary, not the external one, fails to close.

## Details

### The filter bound

The difference between the exact and the declared predictive covariances obeys an exact quadratic matrix equation, and the declared filter contracts in the metric of its own predictive covariance. These two facts bound the upper limit of the excess relative entropy by a covariance term and a mean term, the latter proportional to the square of the forgetting time of the declared filter and to the energy of the part of the defect that the record resolves. The bound is finite for every declared model with a detectable filter and is of second order in the defect and the noise mismatch. In the upper limit it holds from every Gaussian start and for a fine process that is detectable and not necessarily stable; at a finite round only a bound that depends on the start is available ([[dennis-2026-collective-agents-approximate-meta-agent]]).

### The assembled theorem

For a stable linear-Gaussian collective whose members run a consensus filter on information contributions ([[olfati-saber-2005-distributed-kalman-filter]] is the classical antecedent), with exact blanket conditions, the five properties of the exact theorem hold in the following form. The coarse [[Markov Blanket]] and the closure of the coarse internal state remain exact. The path law of the coarse exterior, the belief encoded by the members' average and the law of the joint act carry error terms in the defects of the declared model and in the members' computation noise, with no smallness condition. The exterior need not be stable on its own: stability of the joint process and the blanket hypothesis together make the exterior detectable through the coarse sensory state.

### Members that fuse literally

When members fuse messages literally with fixed gains, their average is a fixed linear filter and its recursion is not closed. Its departure from closure is controlled by three structural quantities of the update of the members' means, the dispersions of its row sums and of its column sums and a mixing constant on the members' deviations, together with two second moments of the process. The memory of the average on its own past needs both dispersions; the memory through the inputs needs only the column dispersion. The closure defect in its information form has a floor that mixing does not lower, which separates it from the energy of the defect as a measure of memory ([[dennis-2026-collective-agents-approximate-meta-agent]]).

> [!note] Editorial: Reading of the floor
> The floor arises because the deviations injected by one round of internal noise reach the average in the next round before any mixing, at a size comparable with the fresh noise of the average. It is a property of the one-step information measure, in line with the observation of the manuscript that information-form defects misstate the memory of aggregates. This reading is the wiki's summary of the proof and is not a separate claim of the source.

### Relation to closure notions

Exact closure of a coarse variable of a linear system is invariance of the kernel of the coarse map, the linear-Gaussian case of lumpability ([[kemeny-snell-1960-finite-markov-chains]]) and of aggregation of nearly decomposable systems ([[simon-1961-aggregation-variables-dynamic-systems]]). Its approximate forms are ordered measures of memory, of which the one-step closure defect is the largest. The projection identities behind the memory terms are those of [[zwanzig-1961-memory-effects]] and [[mori-1965-transport-collective-motion]], and the dynamical-independence and informational-closure notions of [[barnett-2023-dynamical-independence-discovering]] and [[rosas-2024-software-natural-world]] coincide with exact closure in the stationary linear-Gaussian case without input.

## What is not established

Approximate blanket conditions are not combined with the theorem. The closed-form bound on the belief is asymptotic. Collectives of literal members have no bound on the error of their belief. Nonlinear and non-Gaussian dynamics are outside all of these statements, and the open problem of the manuscript on an approximate meta-agent theorem is narrowed and not closed.

## In this work

The results belong to the multi-agent line of the program ([[Gauge-Theoretic Multi-Agent VFE Model]]). They concern a linear-Gaussian model of communicating agents and are not a statement about the gauge-theoretic free-energy functional or its implementation.

## Sources

- [[dennis-2026-collective-agents-approximate-meta-agent]]
- [[kalman-1960-approach-linear-filtering]]
- [[olfati-saber-2005-distributed-kalman-filter]]
- [[zwanzig-1961-memory-effects]]
- [[mori-1965-transport-collective-motion]]
- [[kemeny-snell-1960-finite-markov-chains]]
- [[simon-1961-aggregation-variables-dynamic-systems]]
- [[barnett-2023-dynamical-independence-discovering]]
- [[rosas-2024-software-natural-world]]

## See also

- [[Meta-agents and hierarchical emergence]]
- [[Coarse Graining]]
- [[Markov Blanket]]
- [[Kalman filter]]
- [[Collective active inference]]
- [[Collective agents literature map]]
