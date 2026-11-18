---
type: concept
title: "Markov blanket interpretation debate"
aliases:
  - "Pearl blanket vs Friston blanket"
  - "Markov blanket realism debate"
  - "Are Markov blankets real?"
tags:
  - cluster/vfe
  - cluster/participatory
  - cluster/methodology
  - project/multi-agent
  - project/transformer
status: stable
created: 2026-06-19
updated: 2026-11-18
---

# Markov blanket interpretation debate

## Definition

The **Markov blanket interpretation debate** is the foundational dispute over what a Markov blanket *is* when the free-energy principle (FEP) uses one to carve an agent out of its environment. A Markov blanket is the minimal set of variables (sensory plus active states) that render a system's internal states conditionally independent of external states. The contested question is whether such a partition is an **ontological** feature of the world — a real boundary that makes a system a genuine, mind-independent individual — or merely an **instrumental** modelling choice — a perspectival device a modeller imposes to describe conditional independence. A second, partly separable strand asks whether well-defined blankets even *exist* for the dynamical systems the FEP cares about, and whether they nest cleanly across scales. [[bruineberg-2022-emperors-markov-blankets]] crystallised the conceptual axis as the distinction between a **"Pearl blanket"** (Pearl's epistemic, modeller-relative construct from graphical models) and a **"Friston blanket"** (a putatively system-defining, metaphysical boundary), charging the FEP literature with an illicit slide from the former to the latter.

## Details

The critiques form a graded trio. [[bruineberg-2022-emperors-markov-blankets]] supplies the *conceptual* worry (Pearl vs Friston, the metaphysics is unlicensed by the math). [[aguilera-2022-particular-physics]] supplies the *quantitative* one: solving linear Ornstein–Uhlenbeck non-equilibrium systems in closed form, they show the blanket-and-belief structure holds only when solenoidal (irreversible) coupling is small, so the inference reading is not generic. [[biehl-2021-technical-critique]] supplies the *surgical* objection: the foundational derivations equivocate between inequivalent blanket definitions, and "internal states parametrize beliefs about external states" does not follow as stated. Together they qualify the constructive [[Bayesian mechanics]] lineage that treats any blanketed steady state as performing inference. Against them, [[kirchhoff-2018-markov-blankets-of-life|kirchhoff-2018-markov-blankets-life]] is the constructive precedent for nested blankets and [[Renormalization group flow|scale-spanning]] individuality within the [[Free-energy principle active inference]] tradition.

It is worth recalling that the *deflationary* reading the critics urge — a blanketed system as a thing that merely *tracks* or *forecasts* its environment, without any metaphysical commitment to inner beliefs — already has a long, fully respectable statistical pedigree. Dynamic Bayesian forecasting models ([[west-harrison-1997-bayesian-forecasting]]) and their steady-state limits ([[smith-1979-steady-forecasting]]) describe systems whose internal state recursively updates a predictive distribution over external observations, which is operationally just the synchronization map without the "physics-of-beliefs" gloss. Reading the FEP's internal states as forecasting filters is thus the minimal, least-contested interpretation; the debate is over whether anything *more* — real individuality, genuine belief — is licensed on top of it.

## Sources

- [[bruineberg-2022-emperors-markov-blankets]] — the conceptual Pearl-vs-Friston critique; the canonical instrumental-vs-ontological worry.
- [[aguilera-2022-particular-physics]] — quantitative critique: the blanket condition holds only in a narrow parameter region for non-equilibrium systems.
- [[biehl-2021-technical-critique]] — technical critique: inequivalent blanket definitions, the belief-encoding claim is not automatic.
- [[kirchhoff-2018-markov-blankets-of-life|kirchhoff-2018-markov-blankets-life]] — the constructive nested-blanket precedent for multi-scale, recursively composed agents.
- [[west-harrison-1997-bayesian-forecasting]] — dynamic Bayesian forecasting: the deflationary "internal state tracks/forecasts the environment" reading of the blanket.
- [[smith-1979-steady-forecasting]] — steady-state forecasting limit; the minimal, least-contested synchronization-map interpretation.
- [[friston-2021-interesting-observations-fep]] — reply to the technical critique; concedes that sparsity and conditional independence are inequivalent and that the bound need not be constant.
- [[sakthivadivel-2022-regarding-flows-fep]] — reply to the quantitative critique; concedes its derivations and conjectures a path-based formulation.
- [[ramstead-2022-notation-minima-comment]] — reply to the quantitative critique; accepts the linear results and states the principle is silent on real versus describable minimization.
- [[heins-2022-particular-flows-attracting-sets]] — partial rebuttal of the block-diagonal claim on one numerical linear example.
- [[sakthivadivel-2022-weak-markov-blankets]] — probabilistic reply to the rarity objection over an assumed random ensemble.
- [[friston-2020-sentience-markovian-monism]] — the belief geometry described by its authors as an as-if description.
- [[sakthivadivel-2023-worked-example-classical-objects]] — footnote granting the as-if reading for non-agential objects.
- [[friston-2026-generative-modelling-nonequilibrium]] — generative model as the modeler's map; inference as an as-if description; examples called constructions.
- [[baltieri-2020-predictions-eye-beholder]] — worked instrumentalist case: an active inference model of the Watt governor.
- [[millidge-2021-mathematical-walkthrough-fep]] — assumption-by-assumption audit of the free energy lemma.
- [[virgo-2021-interpreting-dynamical-systems-bayesian]] — consistent Bayesian interpretations depend on the machine alone and are not unique.
- [[biehl-2023-interpreting-systems-pomdps]] — model chosen independently of the environment and judged by consistency.
- [[baltieri-2025-bayesian-internal-model-principle]] — internal model as a map between system descriptions held by a designer.
- [[pearson-2026-flux-defined-markov-blanket]] — computational test of the screening condition in a nonlinear spatially extended system.

## See also

- [[Bayesian mechanics]]
- [[Free-energy principle active inference]]
- [[Participatory realism (it from bit)]]
- [[Gauge transformation]]
- [[Renormalization group flow]]

## Replies, concessions and tests from the Bayesian mechanics batch, November 13, 2026

The replies to the technical and quantitative critiques are now in the vault, and each concedes part of its target. Answering [[biehl-2021-technical-critique]], [[friston-2021-interesting-observations-fep]] grants that flow sparsity and steady-state conditional independence do not imply one another, that the KL bound is unbounded and need not be constant, and that the principle does not claim that self-organization minimizes variational free energy; it restricts the principle to blankets that arise from sparse coupling. Answering [[aguilera-2022-particular-physics]], [[sakthivadivel-2022-regarding-flows-fep]] calls the two critiques mathematically correct and conjectures a path-based remedy, [[ramstead-2022-notation-minima-comment]] accepts the linear results and traces one disputed assumption to notation, and [[heins-2022-particular-flows-attracting-sets]] accepts the statement about marginal flows at the conditional mode while contesting, on one numerical example, that only block-diagonal solenoidal coupling is admissible. [[sakthivadivel-2022-weak-markov-blankets]] answers the rarity objection with a concentration bound over an assumed random ensemble of couplings.

Lineage authors also state the as-if reading themselves. [[ramstead-2022-notation-minima-comment]] says the principle is silent on whether systems minimize free energy or are only describable so. [[friston-2020-sentience-markovian-monism]] calls the belief description as-if unless further conditions hold, and [[sakthivadivel-2023-worked-example-classical-objects]] grants the same for non-agential objects in a footnote. [[friston-2026-generative-modelling-nonequilibrium]] separates the modeler's generative model from the variational density attributed to the particle, obtains the free-energy flow by stipulating that a KL term vanishes, and adds that models built with the principle can still be reified.

From outside the lineage, [[baltieri-2020-predictions-eye-beholder]] recovers, under two chosen assumptions, the linearized engine equation of a Watt governor from the action update of a linear-Gaussian active inference model and argues that the generative model belongs to the observer. [[millidge-2021-mathematical-walkthrough-fep]] audits the derivation step by step: the inference reading is exact only for conditional modes, given an invertible differentiable synchronization map, a Laplace density and, by its Appendix 10.3.2, block-diagonal solenoidal coupling. [[virgo-2021-interpreting-dynamical-systems-bayesian]] and [[biehl-2023-interpreting-systems-pomdps]] keep the reasoner's model separate from the true environment, so beliefs can be consistent and wrong, and the first adds that interpretations are not unique; [[baltieri-2025-bayesian-internal-model-principle]] places the control-theoretic internal model in an external designer's description of the systems. [[pearson-2026-flux-defined-markov-blanket]] tests screening numerically in Gray-Scott spots: neither a flux-defined nor a concentration-defined boundary renders interior and exterior conditionally independent, and a linear-Gaussian free energy that tracks the spot life cycle is computable, which the author states is not evidence of inference.
