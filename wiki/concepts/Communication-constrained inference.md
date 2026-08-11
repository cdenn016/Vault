---
type: concept
title: "Communication-constrained inference"
aliases:
  - "Communication-limited inference"
  - "Distributed estimation under bit constraints"
tags:
  - cluster/vfe
  - cluster/multi-agent
  - project/multi-agent
status: draft
created: 2026-08-10
updated: 2026-08-10
---

# Communication-constrained inference

## Definition

Communication-constrained inference treats messages as a limited statistical resource. Samples are distributed across machines or agents, but only a prescribed number of bits, rounds, messages, or graph-local transmissions may be exchanged. The protocol is therefore part of the estimator: its message alphabet, interactivity, topology, and coding assumptions must be stated before its statistical error can be interpreted.

## Why it matters here

A multi-agent model is not decentralized merely because its objective decomposes into agent-indexed terms. If each update reads every other agent's full-precision state, the implementation is effectively centralized or all-to-all. [[duchi-2014-distributed-estimation]] proves that restricted communication can change minimax estimation rates, so communication cannot be treated as a harmless implementation detail. MultiAgentELBO can use its exact finite model as an oracle against which quantized or graph-local protocols are measured.

## Distinct constraints

- A **bit budget** limits the cardinality of messages and produces quantization or compression error.
- A **round budget** limits adaptivity and diffusion of distant information.
- A **graph constraint** restricts which agents can communicate, so mixing time and bottlenecks matter.
- **Packet loss, delay, or asynchronous updates** create stale or absent information and are not equivalent to quantization.
- A **privacy constraint** may limit information in a message but is not identical to a communication budget.

These constraints should not be collapsed into a single scalar "communication noise" without a derived observation channel.

## Statistical consequences

[[duchi-2014-distributed-estimation]] uses information-theoretic lower bounds to show regimes in which achieving centralized rates requires communication scaling with local problem size or dimension. [[bandyopadhyay-chung-2018-logop-filtering]] provides a different layer: filtering performance under intermittent or constrained network exchange. [[lalitha-2018-distributed-hypothesis-testing]] studies finite-hypothesis learning over a network and characterizes exponential belief concentration. Their loss functions, parameter spaces, and messages differ, so none is a universal bound for the others.

## In this work

A communication-aware benchmark should declare the payload (samples, gradients, natural parameters, moments, or log beliefs), bits per agent per step, number of rounds, graph, and failure model. It should plot posterior or decision error against communication, with an unlimited-communication oracle and a no-communication baseline. Consensus error, estimation error, and numerical compression error should be logged separately. Continuous-time free-energy dissipation alone yields no communication-rate guarantee.

## Sources

- [[duchi-2014-distributed-estimation]] — minimax lower and upper bounds under communication constraints.
- [[bandyopadhyay-chung-2018-logop-filtering]] — distributed filtering under time-varying communication.
- [[lalitha-2018-distributed-hypothesis-testing]] — networked hypothesis learning and concentration rates.

## See also

- [[Decentralized Bayesian inference]]
- [[Conservative information fusion]]
- [[Non-Bayesian social learning]]
- [[Probabilistic opinion pooling]]
