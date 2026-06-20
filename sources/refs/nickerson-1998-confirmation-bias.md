---
type: reference
title: "Confirmation Bias: A Ubiquitous Phenomenon in Many Guises"
aliases:
  - "Nickerson 1998"
authors:
  - Raymond S. Nickerson
year: 1998
tags:
  - cluster/social-physics
  - project/social-physics
  - field/psychology
  - cluster/social-physics/social-influence
created: 2026-06-19
updated: 2026-06-19
---

# Confirmation Bias: A Ubiquitous Phenomenon in Many Guises

> [!info] Citation
> Nickerson, R. S. (1998). "Confirmation Bias: A Ubiquitous Phenomenon in Many Guises." *Review of General Psychology* **2**(2), 175–220. DOI: [10.1037/1089-2680.2.2.175](https://doi.org/10.1037/1089-2680.2.2.175).

## TL;DR

Nickerson's review synthesizes the psychological literature on confirmation bias, the pervasive tendency of people to seek, weight, and interpret evidence in ways that favor beliefs, expectations, or hypotheses already held. He argues that the bias is not a single mechanism but a family of related phenomena — restricting attention to a favored hypothesis, preferentially recalling confirming instances, overweighting supportive evidence while discounting disconfirming evidence, and persevering in a belief after its original grounds have been discredited — and that this family is implicated across reasoning, judgment, science, medicine, law, and everyday social life.

## What it establishes

The paper's organizing claim is that confirmation bias is best understood as a cluster of distinct but interrelated information-processing tendencies that share a common signature: the asymmetric treatment of evidence as a function of its agreement with a prior position. Nickerson catalogs the guises — the failure to search for disconfirming cases (as in the classic selection-task and rule-discovery experiments), the tendency to interpret ambiguous evidence as supporting one's view, the differential scrutiny applied to congenial versus uncongenial findings, the overweighting of positive confirming instances, and the persistence of discredited beliefs — and shows that each has been documented across many experimental paradigms and applied domains. He distinguishes motivated forms of the bias, in which people protect a belief they are invested in, from unmotivated forms that arise from ordinary limits on attention, memory, and hypothesis testing, and he reviews candidate explanations ranging from the cognitive economy of a positive-test strategy to the desire to preserve a coherent self-consistent worldview.

A throughline of the review is that confirmation bias functions less as a deliberate evaluation of competing hypotheses than as a one-sided case-building exercise in which a favored hypothesis is treated as the default and evidence is recruited to sustain it. The same disposition that helps people maintain stable, actionable beliefs in a noisy world also makes those beliefs resistant to revision, so that the bias is simultaneously adaptive and a source of systematic error. Nickerson presents this not as a peripheral quirk but as a deeply entrenched feature of human cognition with consequences for collective epistemics wherever beliefs are formed, shared, and contested.

## Why the project cites it

For the **SocialPhysics** program and its founding manuscript [[belief-inertia]], Nickerson's review supplies the empirical phenomenology that the project's geometry is meant to explain. The manuscript's distinctive move is to recast confirmation bias and belief perseverance not as ad hoc cognitive defects but as geometric consequences of *epistemic inertia*: when the Fisher/precision tensor is read as an inertial [[Mass as Fisher information]] in a [[Hamiltonian belief dynamics]] ansatz, a sharply peaked, high-precision belief is a high-mass state that resists displacement by incoming evidence. The asymmetric, prior-favoring evidence processing Nickerson documents across so many guises is, on this reading, the behavioral signature of [[Belief inertia]] — the same quantity that, in the overdamped limit, slows convergence in classical opinion-dynamics models, and that in the underdamped regime produces momentum, overshoot, and resistance to disconfirmation. The note thus grounds the project's claim that confirmation bias is a structural feature of inertial belief on a statistical manifold rather than a free-standing psychological postulate.

Within the wider modeling picture, Nickerson connects to the project's treatment of opinion dynamics on the [[Fisher information metric]]. The differential weighting of confirming versus disconfirming evidence corresponds to a precision-modulated [[Natural gradient]] step: high precision in the direction of the held belief flattens the effective response to contrary evidence, so the update preferentially moves along directions already favored by the prior. Read through [[Multi-agent variational free energy]], an agent's reluctance to incorporate a neighbor's disconfirming belief — the gauge-transported coupling $\mathrm{KL}(q_i \,\|\, \Omega_{ij}\, q_j)$ — is damped by exactly this inertial mass, which is the microscopic origin of [[Echo chambers and polarization]] in the limiting sociophysics models the program subsumes. The phenomenology Nickerson reviews is the descriptive target that the manuscript's [[Belief perseverance and confirmation bias]] mechanism is built to recover.

The note sits in the SocialPhysics social-cognition lineage alongside the belief-perseverance and attitude-dynamics references the manuscript draws on — [[anderson-1980-belief-perseverance]], [[kaplowitz-fink-1992-attitude-change]], and the social-influence surveys [[flache-2017-social-influence-models]] and [[friedkin-johnsen-2011-social-influence-network]] — and complements the opinion-dynamics source notes [[degroot-1974-consensus]], [[friedkin-johnsen-1990]], [[deffuant-2000-bounded-confidence]], [[hegselmann-krause-2002]], and [[galam-2008-sociophysics]]. See also the project hub [[SocialPhysics]] and the concept pages [[Opinion dynamics]], [[Sociophysics]], [[Bounded confidence]], and [[Belief perseverance and confirmation bias]].

```bibtex
@article{nickerson1998confirmation,
  author  = {Nickerson, Raymond S.},
  title   = {Confirmation Bias: A Ubiquitous Phenomenon in Many Guises},
  journal = {Review of General Psychology},
  year    = {1998},
  volume  = {2},
  number  = {2},
  pages   = {175--220},
  doi     = {10.1037/1089-2680.2.2.175}
}
```
