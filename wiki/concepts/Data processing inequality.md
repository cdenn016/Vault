---
type: concept
title: "Data processing inequality"
aliases:
  - "DPI"
tags:
  - cluster/info-geometry
  - cluster/multi-agent
  - project/transformer
  - project/multi-agent
status: draft
created: 2026-06-21
updated: 2026-08-18
---

# Data processing inequality

The data processing inequality (DPI) states that for any Markov chain X -> Y -> Z, the mutual information cannot increase under processing: I(X;Z) <= I(X;Y). No transformation of Y (deterministic or stochastic) can create information about X that was not already present. It is the formal backbone of the information-bottleneck view of deep learning, where each layer is a processing stage and the DPI bounds how much task-relevant information can survive successive representations. More generally it expresses the monotonicity (contraction) of f-divergences and Fisher information under stochastic maps, linking it to Cencov's characterization of the Fisher metric. Standard reference: [[cover-thomas-2006-elements-information-theory]].

## In the rescaling laboratory: retention bounded by one as a theorem

In the MultiAgentELBO rescaling step the coarse law is the exact pushforward of the fine law
through the per-block Bayes kernels, and each parent label depends only on its own block's
children, so the DPI applies across any block boundary: $I(P_1;P_2) \le I(X_{B_1};X_{B_2})$,
making the mutual-information retention $R_{\mathrm{MI}} \le 1$ a theorem rather than a
measurement ([[2026-08-18-minfo-information-retention]], amendment 9). Measured retention is
2–7% at the declared seed — an order of magnitude below the sup-norm coupling retention,
because mutual information is quadratic in weak coupling. The structural consequence: the
regenerated-attention mechanism restores *interaction* at coarse levels without restoring
*information* — nothing operating on the coarse law can recover what the pushforward
discarded, so the rebuilt coupling is synthesized from coarse state (the conserved connection
and coarse beliefs), not relayed from below. Hierarchies maintain structure upward while
microscale information dies within a few levels.

Two published senses in which higher levels nevertheless "have more" do not contradict the
DPI: synergy — joint configurations carry information no part carries
([[Partial information decomposition]], [[williams-beer-2010-pid]]) and higher levels are
where joint readout lives — and causal emergence, where a macro model's *interventional*
effective information can exceed the micro model's ([[hoel-2013-causal-emergence]]); the
latter uses do-distributions, not the observational pushforward the DPI governs. The
throughput anchor from neuroscience is [[zheng-meister-2025-unbearable-slowness]]: $10^9$
bits/s consumed against ~10 bits/s emitted — higher levels are information compressors that
generate, not amplifiers that relay.

## Related
[[Quantum information geometry]], [[Fisher information metric]], [[Mutual information]], [[Meta-agents and hierarchical emergence]], [[Coarse Graining]]

## Sources
[[tishby2015-deep-learning-ib]], [[cover-thomas-2006-elements-information-theory]], [[2026-08-18-minfo-information-retention]], [[hoel-2013-causal-emergence]], [[zheng-meister-2025-unbearable-slowness]]
