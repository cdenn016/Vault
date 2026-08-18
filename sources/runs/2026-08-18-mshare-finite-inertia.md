---
type: run
title: "M-share: alignment and correlation compete, and alignment wins at this seed (2026-08-18)"
aliases:
  - "M-share measurement"
  - "finite-inertia environments"
  - "amendment 14 results"
tags:
  - cluster/multi-agent
  - cluster/vfe
  - cluster/gauge-theory
  - project/multi-agent
  - field/physics
  - field/statistics
created: 2026-08-18
updated: 2026-08-18
---

# M-share: alignment and correlation compete, and alignment wins at this seed (2026-08-18)

> [!warning] Tentative — not independently verified
> A single-implementation finding: reproduced and cross-checked only inside the MultiAgentELBO
> codebase (exact identities, verified limits, declared controls). No independent
> implementation, external replication, cross-model verification, or verification-ledger
> closure exists; treat every number and verdict as tentative. This applies to the entire
> 2026-08-17/18 rescaling-laboratory chain.

> [!info] Provenance and evidence boundary
> Repository `MultiAgentELBO`, amendment 14 pre-registered before running; implementation and
> results committed at `3548cc5`; the figure suite rendering the whole chain committed at
> `9171363` (`figures/rescaling-lab/`, regenerable by `run_rescaling_figures.py`, which
> refuses to draw if the seed fails its published invariants). Tested before measuring: the
> dressed action matches the direct marginalization to $10^{-10}$, the $m \to \infty$ limit
> reproduces the amendment-13 pinned dressing to four decimals, and the private-duplicate
> control induces exactly zero pair coupling.

## The construction

A finite-inertia shared environment: one environmental agent per declared site group, with
Gibbs prior $\rho(y) \propto e^{-m F(y, \epsilon)}$ and coupling $\kappa_{\mathrm{env}} F(x_a,
y)$ per attached site, integrated out exactly; the induced group potential decomposes by the
anchored Moebius route into site components (alignment) and, for pair groups, the pair
component that is the correlation channel a point-mass environment cannot carry.

## Results (declared 6-cycle, shared pair groups, preferred states 0/4/8)

Per the pre-registered rule, **correlation binding is not licensed**: the aligned placement's
mass rises monotonically in inertia toward the pinned plateau ($0.110 \to 0.194$ at
$\kappa_{\mathrm{env}} = 8$) and never exceeds it. The decomposition inside the negative is
the finding: at $m = 0$ shared agents give the aligned pairing **9×** the private-duplicate
control ($0.1105$ vs $0.0125$) on an induced pair sup of $12.6$, and free strong sharing tips
**direct** collapse modal ($0.366$). The induced pair coupling vanishes as the environment
freezes. Reading: **alignment and correlation are competing channels for the
aligned-placement statistic, not composing ones** — maximal alignment (the pinned limit)
beats maximal correlation at this seed, no pattern condenses the aligned pairing, and the
formation barrier that survives every instrument of the week is the derived energy's width
penalty, pointing at the level-invariant kernel family itself.

## Relevance to this research

Completes the environment arc of [[2026-08-18-environmental-blocking]]: point-mass evidence
aligns ([[2026-08-18-rescaling-audit-capacity-reversal]] chain), fluctuating shared evidence
correlates, and on this seed the two channels trade off rather than add. In the
mass-as-Fisher-information language: evidence with infinite mass is a frame, not a bond, and
evidence light enough to be moved is a bond that anchors nothing — at this seed there is no
inertia at which it is both. The figure suite (`figures/rescaling-lab/`, seven figures with
captions) renders the full chain for review.
