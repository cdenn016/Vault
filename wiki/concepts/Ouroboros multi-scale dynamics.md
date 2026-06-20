---
type: concept
title: "Ouroboros multi-scale dynamics"
aliases:
  - Ouroboros tower
  - Multi-scale ouroboros
  - Bidirectional multi-scale flow
tags:
  - cluster/multi-agent
  - cluster/vfe
  - cluster/gauge-theory
  - project/multi-agent
status: draft
created: 2026-06-18
updated: 2026-06-19
---

# Ouroboros multi-scale dynamics

## Definition

**Ouroboros multi-scale dynamics** is the mode of the gauge-theoretic multi-agent variational free energy framework in which agents are stacked into a *multi-scale tower* with **bidirectional flow** between scales and **multi-generation hyperpriors**. In the [[Gauge-Theoretic Multi-Agent VFE Model]] codebase it is one of four experiment classes, selected by `CONFIG['mode'] = 'ouroboros'`, and it corresponds to manuscript sections §4.5–4.7. The name evokes the ouroboros — the serpent eating its own tail — capturing Wheeler's participatory image of "agents observing themselves into existence" as a closed loop running across scales.

Operationally, the tower runs an inner base-scale dynamics (a [[Natural gradient]]/`natural_gradient` first-order descent or a [[Hamiltonian belief dynamics|hamiltonian]] symplectic integrator) and then couples scales together: information flows *up* the tower (coarse-graining beliefs into higher-scale structure) and *down* the tower (higher scales propagating priors back onto lower scales as hyperpriors).

> [!note] Editorial: The detailed implementation lives in `gauge_agent/ouroboros.py` (`OuroborosTower`), which is referenced in the README module map but was not in the read scope. The claims below are grounded in the README; equation-level internals are deferred to that module and the manuscript.

## Why it matters here

Ouroboros dynamics is what turns the framework from a flat, single-scale system of interacting agents into a genuinely *hierarchical, self-referential* one — the structural payoff of the whole [[Gauge-Theoretic Multi-Agent VFE Model]]. Where the `'basic'` mode exercises "flat single-scale dynamics" (§2.10 / §3), the `'ouroboros'` mode supplies the multi-scale closure in which lower-scale agents condense into higher-scale structure and that structure feeds back down. It is the concrete computational realisation of the participatory loop the project formalizes from [[wheeler-1990-it-from-bit]] — Wheeler's "It From Bit" implemented as a participatory loop of agents observing themselves into existence.

It sits alongside, and composes with, the other multi-scale machinery of the model:
- the soft [[Meta-agents and hierarchical emergence|hierarchy]] mode (`'hierarchy'`, §4.2), which forms meta-agents via gated species × coalition membership and condensation;
- the [[Renormalization-group flow of beliefs|renormalization-group]] mode (`'rg'`, §4.3.2), which coarse-grains by KL-proximity blocking.

Ouroboros is distinguished from these by its emphasis on *bidirectional* flow and *multi-generation hyperpriors* — the top-down half of the loop is as load-bearing as the bottom-up half.

The bidirectional, multi-scale closure has a natural reading as [[Collective active inference]] across nested scales, where each scale acts as the generative context (priors) for the scale below; recent work on multi-scale active inference ([[waade-2025-as-one-and-many]], [[friston-2024-federated-inference]]) gives an external vantage on this "as one and many" structure.

## Details

**Bidirectional flow.** The tower carries up to `max_scales` levels (`OuroborosConfig(enable, max_scales, hyperprior_depth, hyperprior_decay, ...)`). The base scale runs the chosen inner integrator; coarser scales receive aggregated belief structure from below, and in turn push priors back down.

**Multi-generation hyperpriors.** The top-down half of the loop propagates priors across several generations of the tower with a geometric decay. The README ties this to the manuscript's hyperprior-weight expression $\rho^k$ (line 1990), implemented in `OuroborosTower._propagate_hyperpriors`, with `hyperprior_depth` setting how many generations deep the propagation reaches and `hyperprior_decay` controlling the per-generation weighting. Intuitively, a scale-$k$ ancestor influences a descendant with a weight that falls off like

$$
w_k \;\sim\; \rho^{\,k},
$$

so distant generations contribute progressively less, giving a finite-range but multi-generation top-down prior.

**Top-down propagation on both fibres.** The downward leg propagates priors on *both* the belief and model fibres — consistent with the agent construction in which each agent is a smooth section of two associated fibre bundles ([[Agents as fibre-bundle sections]]) carrying Gaussian beliefs on belief and model fibres with [[Gauge transformation|GL(K)]] gauge frames. The README maps this to `TopDownFeedback.propagate_prior` (both fibers, line 1965).

**Mass under the ouroboros convention.** When the inner dynamics is Hamiltonian, the mass that plays the role of [[Belief inertia|inertia]] can be set with `cfg.dynamics.hamiltonian.mass_convention = 'ouroboros'` (versus the default `'hessian'`). The README's module map names `ouroboros_effective_mass` in `gauge_agent/mass.py` as the multi-scale counterpart to the four-term Hessian mass — i.e. the multi-scale tower has its own effective-mass convention for the second-order, [[Hamiltonian belief dynamics]] regime, where the [[Fisher information metric]] / precision acts as the inertial [[Mass as Fisher information|mass]].

## In this work

- **Mode / config.** Selected by `CONFIG['mode'] = 'ouroboros'`; configured through `OuroborosConfig(enable, max_scales, hyperprior_depth, hyperprior_decay, ...)`. The inner base-scale integrator is still chosen by `dynamics.dynamics` (`'natural_gradient'` or `'hamiltonian'`).
- **Code.** `gauge_agent/ouroboros.py` (`OuroborosTower`, the multi-scale tower with bidirectional flow; `_propagate_hyperpriors`); `gauge_agent/meta_agents.py` (`TopDownFeedback.propagate_prior`); `gauge_agent/mass.py` (`ouroboros_effective_mass`). `OuroborosTower` is part of the exported public API in `gauge_agent.__init__`.
- **Manuscript correspondence.** Hyperprior weights $\rho^k$ — manuscript line 1990 → `OuroborosTower._propagate_hyperpriors`; top-down propagation — line 1965 → `TopDownFeedback.propagate_prior` (both fibers). The mode as a whole corresponds to §4.5–4.7 of `Participatory_it_from_bit.tex` ([[participatory-it-from-bit]]).
- **Relation to neighbouring concepts.** Ouroboros builds the self-referential loop on top of [[Belief inertia]] / [[Hamiltonian belief dynamics]] (inner second-order regime), connects upward to [[Meta-agents and hierarchical emergence]] and [[Renormalization-group flow of beliefs]] (the other coarse-graining modes), and is the multi-scale embodiment of [[Participatory realism (it from bit)]]. The thermodynamic-limit counting of belief configurations developed in [[meta-entropy-manuscript]] supplies the statistical-mechanical lens on such multi-scale belief populations.

## Sources

- [[participatory-it-from-bit]] — Dennis, the manuscript (`Participatory_it_from_bit.tex`) the framework implements; develops the gauge-covariant multi-agent variational-inference construction and the Ouroboros meta-agent emergence simulation. §4.5–4.7, lines 1965 / 1990.
- [[wheeler-1990-it-from-bit]] — Wheeler's participatory "It From Bit" essay motivating the self-observing loop.
- [[meta-entropy-manuscript]] — configurational meta-entropy / thermodynamic-limit lens on populations of variational beliefs.
- [[belief-inertia]] — the inertial-mass and Hamiltonian belief-dynamics regime that the inner base-scale step can run in.
- [[waade-2025-as-one-and-many]] — multi-scale collective active inference ("as one and many") as an external account of nested-scale agents.
- [[friston-2024-federated-inference]] — federated / shared-belief inference across agents, relevant to the top-down prior-propagation half of the loop.
- [[vidal-2007-entanglement-renormalization]] — entanglement renormalization (MERA): a real-space coarse-graining tower that parallels the up-the-tower belief condensation.

## See also

- [[Meta-agents and hierarchical emergence]]
- [[Renormalization-group flow of beliefs]]
- [[Hamiltonian belief dynamics]]
- [[Belief inertia]]
- [[Mass as Fisher information]]
- [[Agents as fibre-bundle sections]]
- [[Multi-agent variational free energy]]
- [[Participatory realism (it from bit)]]
- [[Collective active inference]]
- [[Emergent spacetime and holography]]
- [[Gauge-Theoretic Multi-Agent VFE Model]]
