---
type: run
title: "M-anchor and M-flow: the environment binds, and the process reorders the landscape (2026-08-18)"
aliases:
  - "M-anchor measurement"
  - "M-flow measurement"
  - "environmental blocking"
  - "amendment 12 results"
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

# M-anchor and M-flow: the environment binds, and the process reorders the landscape (2026-08-18)

> [!warning] Tentative — not independently verified
> A single-implementation finding: reproduced and cross-checked only inside the MultiAgentELBO
> codebase (the M-flow sampler is validated against the exactly computed marginal, but both
> live in the same implementation). No independent implementation, external replication,
> cross-model verification, or verification-ledger closure exists; treat every number and
> verdict as tentative. This applies to the entire 2026-08-17/18 rescaling-laboratory chain.

> [!info] Provenance and evidence boundary
> Repository `MultiAgentELBO`, amendment 12 pre-registered before running; implementation
> `src/multiagent_elbo/finite/environmental_blocking.py`, committed at `e14b6b2`. Motivated by
> the same-day theory-fidelity assessment, which named the two gaps repaired here: coarse
> levels were closed systems in an ontology where observation *is* environmental coupling
> (the record "consumed at the fine level"), and the lab evaluated the theory's landscape
> without ever running its process. Declared controls throughout; the M-flow sampler is
> validated against the exactly computed annealed marginal (agreement 0.01–0.02).

## The construction

Under the agent-only ontology an observation is a coupling to an environmental agent of
effectively infinite belief inertia. The dressing: one pinned agent per site, identity
transport, site field $F_a(x) = \kappa_{\mathrm{env}}[\mathrm{KL}(b_x \| b_{\epsilon_a}) +
\mathrm{KL}(m_x \| m_{\epsilon_a})]$, folded into the anchored site sector so every audited
instrument applies unchanged. Under blocking the environment blocks too: the coarse pin is
the MAP parent of the pinned children under the declared downward kernels — the point-mass
limit of the audited Bayes kernel — and re-dressing the undressed coarse reproduces the
audited coarse exactly (a tested identity, since the field is a site function).

## M-anchor: environmental binding licensed

Class masses on the declared 6-cycle ($\lambda = 1$), modal class bolded:

| pattern | $\kappa_{\mathrm{env}} = 0.5$ | $2$ | $8$ |
|---|---|---|---|
| uniform $(0^6)$ | singletons 0.565 | **direct 0.552** | **direct 0.840** |
| shared pairs $(0,0,4,4,8,8)$ | singletons 0.590 | singletons 0.633 | singletons 0.622, aligned $r2$ 0.196 |
| distinct $(0..5)$ control | singletons 0.592 | singletons 0.667 | **singletons 0.902** |

Per the declared rule, binding is licensed: uniform anchors flip the modal class to direct
collapse (realized anchored path $6 \to 1$) while the distinct control anti-binds. Shared-pair
anchors pull the anchor-aligned ratio-2 blocking eightfold ($0.025 \to 0.196$) without
crossing at the declared strengths, and the placement gap becomes physics ($0.19$): the
posterior selects the *placement matching the environment*, not just the ratio. Condensation
follows shared evidence — everything binds under one anchor, pairs pull toward the aligned
pairing, agents with nothing in common anti-bind.

## M-flow: the process reorders the landscape

Joint Metropolis dynamics on $(x, R)$ targeting the annealed joint $e^{-A} P(R) e^{-U}$
(3 replicas × 20,000 steps, acceptance 0.43–0.47). On the bare instance the annealed verdict
**reverses the quenched one**: direct is modal (0.441 exact, 0.461 sampled, unanimous
replicas) where the amendment-10 quenched update gave singletons 0.586 — the Jensen gap
between $e^{-\mathbb E_w[U]}$ and the joint is qualitative: when states and partition
co-fluctuate, configurations adapt to the current blocking and large blocks become cheap in a
way the frozen flow never shows. With shared-pair anchors at $\kappa_{\mathrm{env}} = 2$ the
annealed marginal returns to singletons modal (0.489 exact), direct suppressed.

## Relevance to this research

Resolves the formation story of [[2026-08-18-mpart-participatory-blocking]] and
[[2026-08-18-mbind-coupling-sweep]] with scopes attached: those negatives were true of the
*quenched update on environment-free levels*; restoring the environment (statics) or running
the process (dynamics) each produces aggregation in the directions the agent-only ontology
predicts. This is the program's "agents condense around shared evidence, not mutual
attraction" made a measured statement, and the annealed/quenched split is the lab's first
measured process-versus-landscape gap. Open follow-ups, declared: the shared-pairs
condensation crossing (above $\kappa_{\mathrm{env}} = 8$ or absent), the regenerated channel
composed with the dressing, and the sight-limited participatory variant.
