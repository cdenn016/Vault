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
updated: 2026-11-11
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

## Hierarchical consensus with finitely many rounds, November 11, 2026

Consensus on information contributions, in which each agent holds the information vector and information matrix of its own sensor and the common prior is added once, reproduces the centralized Gaussian posterior when the sums are exact ([[olfati-saber-2005-distributed-kalman-filter]]). [[dennis-2026-collective-agents-renormalization-results]] treats a hierarchy that runs finitely many consensus rounds at each level and passes one representative's estimate of each unit's sum upward. The belief at the top is then a pool in which the contribution of agent $j$ is counted $\mathfrak c_{Ij}$ times by the top-level member $I$, a product over the levels of entries of powers of the consensus matrices. Let $\mathsf d_l$ be the largest value, over the units of level $l$, of the number of children minus one times the mixing factor of the unit raised to the number of rounds. Every count satisfies $\lvert\mathfrak c_{Ij}-1\rvert\le\prod_l(1+\mathsf d_l)-1$, and the bound is attained. Errors of the levels therefore compound multiplicatively: each level amplifies the error inherited from below and adds its own. The error of the top-level mean is an exact linear expression in the count errors, the top-level precision lies between explicit multiples of the exact one, and a bound on the relative entropy to the centralized posterior follows when the total count error is below one. For $L$ levels and a target total error $\mathfrak k_\star\le1$ it suffices to run $\ln(2L(n_J-1)/\mathfrak k_\star)/\ln(1/\rho_{\perp,J})$ rounds in every unit with $n_J\ge2$ children and mixing factor $\rho_{\perp,J}>0$, and one round in a unit with $n_J\ge2$ and $\rho_{\perp,J}=0$.

The hypotheses are symmetric, doubly stochastic, entrywise nonnegative consensus matrices, one representative per unit, noiseless rounds and the information form. Two properties of flat consensus do not carry over. The counts sum to the number of agents only when the units of each level have equal numbers of children, and the average of the top-level estimates no longer obeys the centralized filter pathwise, because it inherits the errors of the lower representatives. The companion statement for literal reading of posted beliefs is that a regular hierarchy counts the common prior once per agent, as flat literal consensus does, and that with unequal groups the group whose graph has the largest spectral radius dominates the top-level belief exponentially in the number of lower-level rounds, the persuasion bias of [[demarzo-2003-persuasion-bias-social]] multiplied across levels. With exact sums the information form is closed under hierarchy and the posterior form is not.

This is the evidence-lineage problem of the diagnostics section above inside a hierarchical protocol. The information form adds no error of its own; the error enters through the representatives and the finite number of rounds, and the bound on the relative entropy is not sharp.

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
