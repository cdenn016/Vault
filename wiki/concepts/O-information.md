---
type: concept
title: "O-information"
aliases:
  - "Organizational information"
tags:
  - cluster/vfe
  - cluster/multi-agent
  - project/multi-agent
status: draft
created: 2026-08-10
updated: 2026-08-10
---

# O-information

## Definition

O-information is a symmetric scalar summary of whether the dependence in a multivariate distribution is globally redundancy-dominated or synergy-dominated. For \(X^n=(X_1,\ldots,X_n)\), [[rosas-2019-o-information]] defines

\[
\Omega(X^n)=\mathrm{TC}(X^n)-\mathrm{DTC}(X^n),
\]

the difference between total correlation and dual total correlation. An equivalent entropy form is

\[
\Omega(X^n)=(n-2)H(X^n)+\sum_{i=1}^n\bigl[H(X_i)-H(X_{-i})\bigr],
\]

where \(X_{-i}\) omits variable \(i\). Positive \(\Omega\) indicates redundancy dominance and negative \(\Omega\) synergy dominance in the aggregate convention of the paper.

## Why it matters here

Because no target variable is selected, O-information can summarize ensemble-wide dependence among agents or scales. This makes it attractive for testing a meta-agent or collective representation. It is algebraically compact—the number of entropy terms grows linearly with \(n\)—but that does not remove the statistical difficulty of estimating high-dimensional joint and leave-one-out entropies.

## Interpretation boundaries

O-information is one signed total. Redundant and synergistic structures can cancel, so \(\Omega\approx0\) does not establish independence or absence of high-order organization. The statistic is distributional, not causal. A negative value does not by itself prove mechanistic emergence, downward causation, or improved task performance. It also has no source-target decomposition, unlike [[Partial information decomposition]].

## Estimation and diagnostics

Any empirical use should name the entropy estimator, representation and binning or density model, sample-splitting procedure, bias correction, and uncertainty interval. Permutation or factorized-null controls should measure estimator bias. Scaling with agent count must hold sample size and state dimension under control, because an apparent trend can be produced by deteriorating entropy estimation.

## In this work

Candidate variables include agent belief summaries, transported common-frame states, or coarse-grained meta-agent features. The choice changes the measured distribution and must be declared. Report total correlation and dual total correlation alongside their difference, include bootstrap or repeated-seed uncertainty, and compare against pairwise and PID diagnostics rather than treating \(\Omega\) as a complete account.

## Sources

- [[rosas-2019-o-information]] — original definition, properties, and redundancy/synergy interpretation.
- [[williams-beer-2010-pid]] — target-based decomposition into partial-information atoms.
- [[lyu-2026-pid-inconsistencies]] — limitations of lattice-based multivariate PID.

## See also

- [[Partial information decomposition]]
- [[Mutual information]]
- [[Meta-agents and hierarchical emergence]]
- [[Meta-entropy]]
