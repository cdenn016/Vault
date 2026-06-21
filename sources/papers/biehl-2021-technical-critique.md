---
type: paper
title: "A technical critique of some parts of the free energy principle"
aliases:
  - "Biehl et al. 2021"
  - "Biehl 2021 Technical Critique"
authors:
  - Biehl, Martin
  - Pollock, Felix A.
  - Kanai, Ryota
year: 2021
arxiv: null
url: https://doi.org/10.3390/e23030293
tags:
  - cluster/vfe
  - cluster/participatory
  - cluster/participatory/philosophy-of-mind
  - project/multi-agent
  - field/neuroscience
  - field/statistics
  - field/philosophy
status: stable
created: 2026-06-19
updated: 2026-06-20
---

# A technical critique of some parts of the free energy principle

> [!info] Citation
> Biehl, M., Pollock, F. A., & Kanai, R. (2021). "A technical critique of some parts of the free energy principle." *Entropy* **23**(3): 293. DOI: [10.3390/e23030293](https://doi.org/10.3390/e23030293).

## TL;DR

A close technical reading that finds the foundational FEP derivations rest on inequivalent, sometimes inconsistent definitions of the Markov blanket and of the maps connecting internal and external states. The authors reconstruct the key steps of the free-energy-principle derivations and identify points where different (and not interchangeable) notions of "blanket" are used at different stages, where claimed identities require unstated assumptions, and where the conclusion that internal states parametrize beliefs about external states does not follow as stated. It is the most surgical of the technical critiques in the [[Markov blanket interpretation debate]].

## Problem & setting

The FEP literature offers several constructions of the blanket and of the synchronization (or "bold") map; Biehl et al. ask whether they are mutually consistent and whether the central conclusions are validly derived from any single consistent definition. Prior to this critique, the claim that any system with a Markov blanket implements approximate Bayesian inference was often treated as an automatic consequence of the blanket's conditional-independence structure.

## Method

Step-by-step reconstruction of the derivations, isolating each definition and assumption and checking whether the chain of implications holds. The critique is constructive in form: it states what would need to be true for each step to go through, rather than simply asserting failure.

## Key results

- Competing blanket definitions are inequivalent. The notion of Markov blanket used to establish conditional independence is not the same as the one used downstream to license the inference reading; substituting one for the other is not valid.
- Hidden assumptions. Several claimed equalities require additional, unstated conditions on the form of the steady-state density or the drift decomposition.
- The belief-encoding claim is not automatic. The conclusion that internal states encode a posterior over external states does not follow generically from the premises as written.

## Relevance to this research

Biehl et al. complete the trio of technical objections — alongside [[bruineberg-2022-emperors-markov-blankets]] (conceptual) and [[aguilera-2022-particular-physics]] (quantitative) — that [[participatory-it-from-bit]] must navigate. Their specific contribution is to warn that "Markov blanket" is not one thing: a program that, like PIFB, leans on internal states parametrizing beliefs about external states across a blanket must fix one consistent definition and check that its conclusions actually follow from it, rather than borrowing different blanket notions at convenience. This matters for the project's [[Agents as fibre-bundle sections]] and [[Multi-agent variational free energy]], where the blanket separating each agent from the rest must be defined precisely enough to support the gauge-covariant belief comparison the model performs. The note qualifies the constructive [[Bayesian mechanics]] lineage and is directly relevant to the multi-agent VFE framework's formal justification of agent individuation.

## Cross-links

- Concepts: [[Variational free energy]], [[Participatory realism (it from bit)]], [[Agents as fibre-bundle sections]], [[Multi-agent variational free energy]], [[Markov blanket interpretation debate]], [[Bayesian mechanics]]
- Related sources: [[bruineberg-2022-emperors-markov-blankets]], [[aguilera-2022-particular-physics]], [[friston-2019-particular-physics]], [[dacosta-2021-bayesian-mechanics]]
- Manuscript/Project: [[participatory-it-from-bit]], [[VFE Transformer Program]]

## BibTeX
```bibtex
@article{biehl2021technical,
  author    = {Biehl, Martin and Pollock, Felix A. and Kanai, Ryota},
  title     = {A technical critique of some parts of the free energy principle},
  journal   = {Entropy},
  volume    = {23},
  number    = {3},
  pages     = {293},
  year      = {2021},
  doi       = {10.3390/e23030293},
  publisher = {MDPI},
}
```
