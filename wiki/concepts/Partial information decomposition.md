---
type: concept
title: "Partial information decomposition"
aliases:
  - "PID"
  - "Partial information atoms"
tags:
  - cluster/vfe
  - cluster/multi-agent
  - project/multi-agent
status: draft
created: 2026-08-10
updated: 2026-08-10
---

# Partial information decomposition

## Definition

Partial information decomposition (PID) seeks to partition the mutual information that a set of sources \(X_1,\ldots,X_n\) provides about a designated target \(Y\) into components that are redundant across sources, unique to particular sources, or synergistic—available only from joint observation. For two sources the schematic identity is

\[
I(X_1,X_2;Y)=R+U_1+U_2+S,
\]

with consistency constraints such as \(I(X_1;Y)=R+U_1\) and \(I(X_2;Y)=R+U_2\).

The decomposition is not determined by Shannon identities alone. A redundancy or unique-information functional and its axioms must be chosen.

## Foundational construction

[[williams-beer-2010-pid]] defines a specific-information minimum \(I_{\min}\), organizes collections of source subsets into a redundancy lattice, and uses Möbius inversion to obtain nonnegative partial-information atoms in that construction. It established the modern vocabulary and exposed how interaction information can confound redundancy and synergy.

## Nonuniqueness and high-order obstructions

Multiple later definitions satisfy different desirable properties and disagree on examples; there is no estimator-independent object called simply "the PID." [[lyu-2026-pid-inconsistencies]] gives closed-form results for a two-source axiomatic setting, revisits a three-source overcounting counterexample, and proves an incompatibility for the lattice-based consistency requirements it studies when the number of sources exceeds three. This is a serious warning against naively scaling a two-source lattice construction to many agents. It is not a proof that every nonlattice or operational measure of redundancy and synergy is impossible.

## Relation to other interaction measures

[[O-information]] is symmetric and target-free; PID is source-target structured and atom-level. Hoeffding or ANOVA interaction terms decompose a function or variance relative to a measure, not mutual information into redundant and synergistic source contributions. Interaction information is a signed inclusion-exclusion quantity. These tools can be compared empirically but should not be renamed as one another.

## Why it matters here

PID could ask whether individual agents contribute unique evidence about a meta-agent target or whether the target is recoverable only jointly. The question is meaningful only after specifying the target, source representation, redundancy definition, estimator, and sampling distribution. In a gauge model, source variables should be transported to a declared common frame when the statistic is not representation-invariant; transport does not resolve the choice of PID axioms.

## In this work

Start with two-source synthetic distributions having known redundant, unique, and XOR-like synergistic structure. Validate the estimator there before using learned agent states. For more than two sources, report the precise construction and its consistency limitations, and prefer preregistered low-order slices or clearly labeled aggregate measures over an unexplained high-order lattice. Include finite-sample intervals and null-model controls.

## Sources

- [[williams-beer-2010-pid]] — redundancy lattice and nonnegative PID proposal.
- [[lyu-2026-pid-inconsistencies]] — recent constructions, lattice consistency obstructions, and alternative measures.
- [[rosas-2019-o-information]] — target-free aggregate redundancy/synergy statistic.

## See also

- [[O-information]]
- [[Mutual information]]
- [[Meta-agents and hierarchical emergence]]
- [[Information geometry]]
