---
type: concept
title: "Propagation of chaos"
aliases:
  - "Kac chaos"
  - "McKean-Vlasov particle limit"
tags:
  - cluster/vfe
  - cluster/multi-agent
  - project/multi-agent
status: draft
created: 2026-08-10
updated: 2026-08-10
---

# Propagation of chaos

## Definition

Propagation of chaos is a precise asymptotic independence statement for exchangeable interacting-particle systems. A symmetric \(N\)-particle law is chaotic with limiting one-particle law \(\mu\) when, for every fixed \(k\), its \(k\)-particle marginals converge as \(N\to\infty\) to \(\mu^{\otimes k}\). Propagation means that chaotic initial data remain chaotic under the finite-particle dynamics and that representative particles converge to independent copies of a nonlinear McKean--Vlasov process.

It does not say that finite agents do not interact. Their weak \(1/N\)-scaled interactions persist through the limiting law, while correlations among any fixed finite subset vanish asymptotically.

## Why it matters here

This is the main proof obligation behind replacing many stochastic agents by a deterministic population law. [[sznitman-1991-propagation-chaos]] systematizes equivalences and coupling methods. [[bayraktar-2023-graphon-mean-field-systems]] adapts the program to heterogeneous graphon interactions. Without an explicit particle system, stochastic scaling, initial-law hypothesis, and convergence topology, "agents become independent in the large-population limit" is only an analogy.

## Typical hypotheses and proof routes

Classical results assume exchangeable or suitably typed independent initial conditions, Lipschitz or otherwise controlled drift and diffusion, normalized weak interactions, and well-posed limiting dynamics. Synchronous coupling compares each finite particle with a limiting nonlinear process driven by the same noise. Martingale-problem and compactness methods handle broader settings. Quantitative results may bound Wasserstein or path-space errors, but rates depend on dimension, regularity, topology, and graph regime.

Graphon models weaken full exchangeability by conditioning on a continuum type. The appropriate conclusion is then type-indexed asymptotic independence, not necessarily a single identical marginal for every agent.

## In this work

A MultiAgentELBO propagation-of-chaos program would first define stochastic finite-\(N\) dynamics and their interaction normalization, then derive a McKean--Vlasov or graphon-indexed limit and prove well-posedness. It should test fixed-\(k\) marginal discrepancies or coupled trajectory error over time. A deterministic natural-gradient descent, a continuum free-energy analogy, or convergence of empirical means alone is insufficient evidence.

## Sources

- [[sznitman-1991-propagation-chaos]] — foundational lecture notes on chaos, nonlinear processes, and coupling arguments.
- [[bayraktar-2023-graphon-mean-field-systems]] — propagation of chaos for graphon-interacting stochastic systems.
- [[caines-huang-2021-graphon-mean-field-games]] — related finite/infinite approximation in a strategic game, not itself the same theorem.

## See also

- [[Graphon limits of agent networks]]
- [[Mean-field games and continuum limits]]
- [[Multi-agent variational free energy]]
