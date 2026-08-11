---
type: concept
title: "Non-Bayesian social learning"
aliases:
  - "Distributed non-Bayesian learning"
  - "Log-linear social learning"
tags:
  - cluster/vfe
  - cluster/multi-agent
  - cluster/social-physics
  - project/multi-agent
status: draft
created: 2026-08-10
updated: 2026-08-10
---

# Non-Bayesian social learning

## Definition

Non-Bayesian social learning studies networked agents who receive private signals and repeatedly update beliefs using a tractable local rule that is not the posterior of one centralized Bayesian observer with the complete signal history. The "non-Bayesian" qualifier usually describes the social aggregation step: agents may update on private data by Bayes' rule but combine neighbors' beliefs by arithmetic or geometric averaging while ignoring higher-order dependence and the full provenance of social information.

## Why it matters here

This literature provides truth-learning and convergence baselines for MultiAgentELBO, but its goal differs from exact distributed posterior reconstruction. [[jadbabaie-2012-non-bayesian-social-learning]] blends a private Bayesian update with a DeGroot-like arithmetic average. [[lalitha-2018-distributed-hypothesis-testing]] uses multiplicative or log-linear belief aggregation and obtains error-exponent results for finite hypotheses. Their dynamics should not be described as interchangeable instances of one ELBO without an explicit derivation.

## Canonical update families

An arithmetic rule has the schematic form

\[
\mu_{i,t+1}=a_{ii}\,\operatorname{Bayes}(\mu_{i,t},s_{i,t+1})
 +\sum_{j\ne i} a_{ij}\mu_{j,t},
\]

whereas a log-linear rule averages log beliefs or multiplies powers of neighbor beliefs before normalization. Arithmetic pooling preserves convex mixtures; logarithmic pooling turns evidence ratios into additive consensus variables. The graph weights, self-reliance, signal identifiability, and whether observations are independent across time all affect the theorem.

## What the guarantees mean

Typical results establish almost-sure concentration on a true state or characterize its exponential rate when the truth is distinguishable by the network's aggregate observations and the graph communicates information adequately. This is not the same as recovering the centralized posterior at each finite time. Consensus can occur on a false state under misspecification or insufficient identifiability, while exact posterior agreement can fail even when asymptotic decisions agree.

## In this work

A social-learning benchmark should use a finite state space with controlled private-signal KL divergences, vary graph connectivity, and report belief on the truth, agent disagreement, and centralized-posterior discrepancy separately. Arithmetic, log-linear, and full Bayesian-history baselines should be labeled by their actual information assumptions. A natural-gradient energy decrease does not by itself imply truth learning.

## Sources

- [[jadbabaie-2012-non-bayesian-social-learning]] — private Bayesian updating combined with local averaging.
- [[lalitha-2018-distributed-hypothesis-testing]] — distributed hypothesis testing and network-dependent learning rates.
- [[aumann-1976-agreeing-disagree]] — common-prior agreement under common knowledge, a distinct epistemic result.

## See also

- [[Decentralized Bayesian inference]]
- [[Probabilistic opinion pooling]]
- [[Common knowledge and Bayesian agreement]]
- [[Communication-constrained inference]]
- [[Opinion dynamics]]
