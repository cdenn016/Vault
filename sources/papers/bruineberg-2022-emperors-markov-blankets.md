---
type: paper
title: "The Emperor's New Markov Blankets"
aliases:
  - "Bruineberg et al. 2022"
  - "Emperor's New Markov Blankets"
authors:
  - Jelle Bruineberg
  - Krzysztof Dolega
  - Joe Dewhurst
  - Manuel Baltieri
year: 2022
url: https://www.cambridge.org/core/journals/behavioral-and-brain-sciences/article/abs/emperors-new-markov-blankets/715C589A73DDF861DCF8997271DE0B8C
tags:
  - cluster/vfe
  - cluster/participatory
  - project/multi-agent
  - field/philosophy
  - field/neuroscience
  - cluster/participatory/consciousness
status: stable
created: 2026-06-19
updated: 2026-06-19
---

# The Emperor's New Markov Blankets

> [!info] Citation
> Bruineberg, J., Dolega, K., Dewhurst, J., & Baltieri, M. (2022). "The Emperor's New Markov Blankets." *Behavioral and Brain Sciences* **45**: e183. DOI: [10.1017/S0140525X21002351](https://doi.org/10.1017/S0140525X21002351).

## TL;DR

This is the canonical philosophical critique of how Markov blankets are deployed in the free-energy-principle / Bayesian-mechanics literature. The authors draw a sharp distinction between a **"Pearl blanket"** — the original, purely epistemic notion from Pearl's graphical models, a tool the modeller uses to describe conditional independence — and a **"Friston blanket"** — a putatively *ontological* boundary said to carve a real agent out of the world. Their charge is that the FEP literature slides illicitly from the former (an unobjectionable formal device) to the latter (a substantive metaphysical claim about where agents are), and that the metaphysical reading is not licensed by the mathematics. Any "physics of beliefs" program, PIFB included, has to say which blanket it means.

## Problem & setting

Markov blankets have been used to settle disputes in philosophy of mind — about the boundaries of cognition, the reality of the self, the location of the agent. The paper asks whether the technical object can bear that metaphysical weight.

## Method

Conceptual analysis tracing the genealogy of "Markov blanket" from Pearl's epistemic, modeller-relative construct to its use in the FEP as a system-defining boundary. The authors argue the two are systematically conflated, and that arguments which appear to establish ontological conclusions (real agents, real boundaries) actually trade on the epistemic reading and so prove nothing of the sort.

## Key results

- **Pearl vs Friston blankets.** A blanket as an artefact of a modeller's chosen variables (epistemic, perspectival) is categorically different from a blanket as a mind-independent partition of the world (ontological).
- **The illicit slide.** Much FEP rhetoric, they argue, equivocates between the two, granting ontological conclusions on epistemic premises.
- **A standing challenge.** Programs that treat internal states as *really* believing things about a *really* separate external world owe an account of which blanket licenses that, and why.

## Relevance to this research

This is the **canonical instrumental-vs-ontological worry that [[participatory-it-from-bit]] must answer**. PIFB's whole architecture rests on internal/observer states encoding beliefs about an external world across a [[Markov blanket interpretation debate|Markov-blanketed]] boundary; Bruineberg et al. press exactly the question of whether that boundary is a real feature of the world or an artefact of the description. The participatory stance gives PIFB a distinctive option unavailable to a naive realist reading: if the program is genuinely *participatory* (observer-relative, "it from bit"), the perspectival/Pearl reading may be a feature rather than a bug — the blanket is observer-indexed by design, and the project's [[Gauge transformation]] freedom (no privileged frame for comparing beliefs) is the formal expression of that perspectivalism. The note belongs to the [[Markov blanket interpretation debate]] cluster alongside [[aguilera-2022-particular-physics]] and [[biehl-2021-technical-critique]], and stands against the constructive [[Bayesian mechanics]] lineage ([[dacosta-2021-bayesian-mechanics]], [[friston-2019-particular-physics]]). It also bears on the project's notion of [[Agents as fibre-bundle sections]] and [[Multi-agent variational free energy]]: if blankets are perspectival, "which agent" is itself frame-dependent.

## Cross-links

- Concepts: [[Participatory realism (it from bit)]], [[Gauge transformation]], [[Agents as fibre-bundle sections]], [[Multi-agent variational free energy]]
- New pages: [[Markov blanket interpretation debate]], [[Bayesian mechanics]]
- Related sources: [[aguilera-2022-particular-physics]], [[biehl-2021-technical-critique]], [[friston-2019-particular-physics]], [[dacosta-2021-bayesian-mechanics]], [[ramstead-2019-enactive-inference|ramstead-2019-variational-neuroethology]]
- Manuscript: [[participatory-it-from-bit]]

```bibtex
@article{bruineberg2022emperor,
  title   = {The Emperor's New Markov Blankets},
  author  = {Bruineberg, Jelle and Dolega, Krzysztof and Dewhurst, Joe and Baltieri, Manuel},
  journal = {Behavioral and Brain Sciences},
  volume  = {45},
  pages   = {e183},
  year    = {2022},
  doi     = {10.1017/S0140525X21002351},
  publisher = {Cambridge University Press}
}
```
