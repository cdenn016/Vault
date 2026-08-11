---
type: concept
title: "Process-space variational inference"
aliases:
  - "Stochastic-process variational inference"
  - "Process-space KL"
tags:
  - cluster/vfe
  - cluster/info-geometry
  - project/transformer
  - project/multi-agent
status: draft
created: 2026-08-10
updated: 2026-08-10
---

# Process-space variational inference

## Definition

**Process-space variational inference** compares probability laws over an entire stochastic process rather than treating one selected finite vector of evaluations as the complete random object. If $P$ and $Q$ are process laws on a declared measurable function or path space, the variational objective uses a measure-level relative entropy $D_{\mathrm{KL}}(Q\|P)$ together with the appropriate likelihood functional. Every finite set of indices induces projected finite-dimensional laws, but those marginals do not by themselves specify a usable continuum variational problem without compatibility, extension, and regularity conditions.

## Why it matters here

MultiAgentELBO currently establishes exact identities for finite normalized laws. A continuum of agents, contexts, or bundle sections requires more than taking $N\to\infty$ in a finite sum. The project must declare a process or section law, its sigma-algebra and topology, a compatible family of finite restrictions, normalizability, and enough control for the relevant KL and observables to exist. [[matthews-2016-stochastic-process-kl]] sharpens one specific part of this obligation: a marginally consistent augmentation need not preserve the original variational problem.

## Details

### Finite restrictions are diagnostics, not the continuum object

For an index set $T$ and a finite design $S\subset T$, evaluation gives a projection $\pi_S$ and finite laws $Q_S=(\pi_S)_\#Q$, $P_S=(\pi_S)_\#P$. These restrictions can test compatibility and finite KL behavior. They do not establish tightness, the existence of a law on smooth sections, or compatibility with a gauge action.

### Augmentation requires conditional agreement

Suppose $V$ is the original variable and $U$ an auxiliary or inducing variable. The KL chain rule gives

$$
D_{\mathrm{KL}}(Q_{U,V}\|P_{U,V})
=D_{\mathrm{KL}}(Q_V\|P_V)
+\mathbb E_{Q_V}D_{\mathrm{KL}}(Q_{U\mid V}\|P_{U\mid V}).
$$

Matching the marginal on $V$ controls only the first term. Equality with the original variational objective additionally requires the conditional term to vanish under the relevant law. This is the augmentation-consistency warning established in [[matthews-2016-stochastic-process-kl]].

### What remains open

The process-KL framework does not construct a measure on smooth gauge sections, prove tightness of a refining family, or show that a reference measure and Radon-Nikodym derivative are gauge compatible. Those are separate continuum obligations.

## In this work

The exact finite [[Multi-agent variational free energy]] and its tests remain the oracle. A future continuum lane should record nested finite designs, projective compatibility, finite KL values, auxiliary conditional laws, topology/tightness assumptions, and convergence of the observables used by the theory. No current finite test is evidence that this continuum object already exists.

## Sources

- [[matthews-2016-stochastic-process-kl]]

## See also

- [[Evidence lower bound (ELBO)]]
- [[Variational free energy]]
- [[Gaussian process]]
- [[Recognition Density]]
- [[Multi-agent variational free energy]]
- [[Statistical manifold]]
