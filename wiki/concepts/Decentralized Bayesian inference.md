---
type: concept
title: "Decentralized Bayesian inference"
aliases:
  - "Distributed Bayesian inference"
  - "Federated Bayesian inference"
tags:
  - cluster/vfe
  - cluster/multi-agent
  - project/multi-agent
status: draft
created: 2026-08-10
updated: 2026-08-20
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
- **Site-factor and partitioned inference:** represent a global approximation through local factors and update them with EP- or VI-style schedules. [[hasenclever-2017-snep-posterior-server]], [[vehtari-2020-ep-partitioned-data]], and [[ashman-2022-partitioned-variational-inference]] make factor ownership and the declared global target explicit.
- **Distributed variational optimization:** distribute ELBO or message-passing updates over a graph or compute network. [[hua-li-2016-distributed-variational-bayes]], [[masegosa-2016-distributed-vmp]], and [[paritosh-2025-distributed-variational-inference]] supply representative batch, message-passing, and online constructions.
- **Private, robust, and generalized federated inference:** [[heikkila-2023-dp-partitioned-vi]] adds differential privacy, while [[mildner-2025-fedgvi]] generalizes local losses and divergence choices. [[wu-uribe-2025-distributed-inference-guarantees]] studies frequentist guarantees under networked belief updates.
- **Structured applications:** [[cao-2024-multi-robot-slam-vi]] treats cooperative localization and mapping; [[rao-2026-federated-variational-mixtures]] exposes mixture-component alignment in a federated setting.

## Diagnostics and baselines

A decentralized experiment should report distance to a centralized exact or high-accuracy posterior, calibration and coverage, consensus disagreement separately from posterior error, sensitivity to graph connectivity and dropped messages, communication volume or bits, and a data-lineage stress test with duplicated observations. Negative controls should include naive posterior multiplication, missing prior correction, and deliberately permuted local mixture labels. A low inter-agent disagreement is not evidence that the agreed distribution is correct.

Evidence lineage belongs in the formal state rather than in bookkeeping outside the model. Each site or factor should carry an immutable identity, owner, prior exponent, version, and ancestry sufficient to determine whether a received update contains evidence already incorporated locally. Cyclic communication otherwise permits repeated reuse of the same observation even after density consensus is reached.

## Scope boundaries

Static [[Probabilistic opinion pooling]] aggregates opinions without specifying an evidence-generating protocol. [[Non-Bayesian social learning]] studies truth learning under deliberately simplified social updates rather than exact distributed Bayes. [[Common knowledge and Bayesian agreement]] establishes agreement under a common prior and common knowledge, not convergence of a decentralized algorithm. These theories answer related but noninterchangeable questions.

## Sources

- [[campbell-how-2014-decentralized-bayes]] — approximate posterior fusion, shared-prior correction, and permutation alignment.
- [[battistelli-chisci-2014-kl-density-consensus]] — distributed KL-average density consensus.
- [[bandyopadhyay-chung-2018-logop-filtering]] — logarithmic pooling for distributed Bayesian filtering with communication-aware variants.
- [[julier-uhlmann-1997-covariance-intersection]] — conservative fusion when cross-correlation is unknown.
- [[duchi-2014-distributed-estimation]] — minimax communication limits for distributed estimation.
- [[hasenclever-2017-snep-posterior-server]] — asynchronous natural-gradient EP with site factors and a posterior server.
- [[hua-li-2016-distributed-variational-bayes]] — distributed variational Bayes over a sensor network.
- [[masegosa-2016-distributed-vmp]] — distributed variational message passing.
- [[vehtari-2020-ep-partitioned-data]] — expectation propagation for partitioned data and local approximations.
- [[ashman-2022-partitioned-variational-inference]] — site-factor formulation of partitioned variational inference.
- [[heikkila-2023-dp-partitioned-vi]] — differentially private partitioned variational inference.
- [[mildner-2025-fedgvi]] — federated generalized variational inference.
- [[wu-uribe-2025-distributed-inference-guarantees]] — asymptotic guarantees for distributed Bayesian inference.
- [[paritosh-2025-distributed-variational-inference]] — online distributed ELBO and consensus optimization.
- [[cao-2024-multi-robot-slam-vi]] — distributed VI for online multi-robot cooperative localization.
- [[rao-2026-federated-variational-mixtures]] — federated variational inference for Bayesian mixture models.

## See also

- [[Probabilistic opinion pooling]]
- [[Communication-constrained inference]]
- [[Conservative information fusion]]
- [[Gaussian Belief Propagation]]
- [[Non-Bayesian social learning]]
