---
type: concept
title: "Decentralized Bayesian inference"
aliases:
  - "Distributed Bayesian inference"
tags:
  - cluster/vfe
  - cluster/multi-agent
  - project/multi-agent
status: draft
created: 2026-08-10
updated: 2026-08-10
---

# Decentralized Bayesian inference

## Definition

Decentralized Bayesian inference asks a network of agents to approximate a common posterior when observations, computation, and communication are distributed and no fusion center has all raw data. It is not one algorithm. A complete specification must state the shared generative model and prior, which evidence each agent observes, what posterior representation or sufficient statistics it transmits, the communication graph and schedule, how common information is tracked, and what centralized posterior or decision is the reference.

If data sets \(D_i\) are conditionally independent given \(\theta\) and every local posterior uses the same prior \(p_0\), then the batch posterior satisfies

\[
p(\theta\mid D_{1:n}) \propto p_0(\theta)^{1-n}\prod_{i=1}^n p(\theta\mid D_i).
\]

The prior correction is essential. Even with it, multiplication of approximate posteriors need not reproduce a centralized approximation: local factorization can discard dependencies, agents can select incompatible representatives of a symmetric model, and repeated network fusion can double-count evidence.

## Why it matters here

MultiAgentELBO currently supplies an exact finite joint-law oracle and variational objectives. Those are valuable ground truth for a decentralized extension, but they do not define a communication protocol. [[campbell-how-2014-decentralized-bayes]] shows that separately optimized approximations can require symmetry alignment before fusion. In this program, that creates a useful test boundary: mixture-label alignment, parameter-coordinate alignment, and [[Gauge transformation|gauge-frame transport]] must be typed as distinct group actions unless a formal identification is constructed.

## Algorithmic families

- **Posterior or natural-parameter fusion:** multiply exponential-family approximations with explicit shared-prior correction. This can be exact only under restrictive representation and independence conditions.
- **Density consensus:** repeatedly compute linear or logarithmic pools over a connected graph. [[battistelli-chisci-2014-kl-density-consensus]] gives a KL-average consensus target, but consensus with the neighbors is not automatically the centralized Bayesian posterior.
- **Likelihood consensus or Bayesian filtering:** exchange new likelihood information separately from historical posteriors. [[bandyopadhyay-chung-2018-logop-filtering]] makes this distinction explicit for dynamic filtering.
- **Conservative fusion:** when dependence or common-information lineage is unknown, use a rule such as [[Conservative information fusion|covariance intersection]] that sacrifices sharpness to avoid unjustified information gain.
- **Communication-limited protocols:** treat the messages and bit budget as part of the statistical model rather than assuming free exchange; see [[Communication-constrained inference]].

## Diagnostics and baselines

A decentralized experiment should report distance to a centralized exact or high-accuracy posterior, calibration and coverage, consensus disagreement separately from posterior error, sensitivity to graph connectivity and dropped messages, communication volume or bits, and a data-lineage stress test with duplicated observations. Negative controls should include naive posterior multiplication, missing prior correction, and deliberately permuted local mixture labels. A low inter-agent disagreement is not evidence that the agreed distribution is correct.

## Scope boundaries

Static [[Probabilistic opinion pooling]] aggregates opinions without specifying an evidence-generating protocol. [[Non-Bayesian social learning]] studies truth learning under deliberately simplified social updates rather than exact distributed Bayes. [[Common knowledge and Bayesian agreement]] establishes agreement under a common prior and common knowledge, not convergence of a decentralized algorithm. These theories answer related but noninterchangeable questions.

## Sources

- [[campbell-how-2014-decentralized-bayes]] — approximate posterior fusion, shared-prior correction, and permutation alignment.
- [[battistelli-chisci-2014-kl-density-consensus]] — distributed KL-average density consensus.
- [[bandyopadhyay-chung-2018-logop-filtering]] — logarithmic pooling for distributed Bayesian filtering with communication-aware variants.
- [[julier-uhlmann-1997-covariance-intersection]] — conservative fusion when cross-correlation is unknown.
- [[duchi-2014-distributed-estimation]] — minimax communication limits for distributed estimation.

## See also

- [[Probabilistic opinion pooling]]
- [[Communication-constrained inference]]
- [[Conservative information fusion]]
- [[Gaussian Belief Propagation]]
- [[Non-Bayesian social learning]]
