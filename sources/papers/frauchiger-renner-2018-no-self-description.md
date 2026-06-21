---
type: paper
title: "Quantum Theory Cannot Consistently Describe the Use of Itself"
aliases:
  - "Frauchiger & Renner 2018"
  - "Frauchiger-Renner no-go"
  - "FR thought experiment"
  - "frauchiger-renner-2018-self-consistent"
authors:
  - Frauchiger, Daniela
  - Renner, Renato
year: 2018
arxiv: "1604.07422"
url: https://doi.org/10.1038/s41467-018-05739-8
tags:
  - cluster/participatory/quantum-foundations
  - project/multi-agent
  - field/physics
  - field/philosophy
status: stable
created: 2026-06-19
updated: 2026-06-20
---

# Quantum Theory Cannot Consistently Describe the Use of Itself

> [!info] Citation
> Frauchiger, D., & Renner, R. (2018). "Quantum theory cannot consistently describe the use of itself." *Nature Communications* **9**, 3711. DOI: 10.1038/s41467-018-05739-8. Preprint: arXiv:1604.07422.

## TL;DR

Frauchiger and Renner construct an extended Wigner's-friend Gedankenexperiment in which agents who themselves reason with quantum theory — and who model *other agents as quantum systems* — are driven to mutually contradictory conclusions about a single measurement outcome. The thought experiment shows that three natural assumptions cannot jointly hold: (Q) an agent may certify a prediction by quantum theory; (C) the predictions of different agents are consistent (one agent may adopt another's certified conclusion); and (S) an agent's measurement yields a single definite outcome. The upshot is a sharpened no-go result: there is no observer-independent assignment of facts that survives agents applying quantum mechanics to one another. Interpretations must give up at least one of Q, C, or S, and the paper sorts the major interpretations by which assumption they sacrifice.

## Problem & setting

The original Wigner's-friend puzzle pits an external observer (Wigner) who describes a sealed laboratory unitarily against the friend inside who experiences a definite outcome. Frauchiger and Renner nest two such friends and two outside observers in a protocol where each agent reasons about what the others have concluded. The setting is universal quantum theory taken at face value: every system, including agents and their memories, evolves unitarily until a measurement is recorded, and agents are licensed to chain inferences about one another's certified statements.

## Method

The protocol uses a quantum coin and two spin-1/2 systems with carefully chosen entangling measurements. Agent F measures the coin and, conditioned on the result, prepares a spin; agent F-bar measures that spin; outside observers W and W-bar then perform incompatible "Wigner" measurements on the entire sealed laboratories. By chaining the agents' Born-rule-certified conclusions (agent A knows that agent B knows that ...), the authors reach a round in which one agent is certain the outcome is one value while another is certain, with nonzero probability, that it is the opposite. The contradiction is exhibited as a logically airtight inference, not a statistical anomaly, and the three assumptions Q/C/S are isolated as the load-bearing premises.

## Key results

The central theorem is that assumptions Q, C, and S are mutually inconsistent within universal quantum theory applied to agents-as-systems. Copenhagen-style views that deny universal validity of unitary evolution reject Q; many-worlds rejects S (no single outcome); Bohmian and collapse theories face their own tensions; and the relational/QBist family escapes by rejecting C — there is simply no agent-independent fact for different observers to share. The paper thereby converts an interpretational debate into a precise trilemma and frames "no observer-independent facts" as a live, theorem-backed option rather than mere philosophy.

## Relevance to this research

This is the sharpest statement of the problem that the project's participatory thread, [[Participatory realism (it from bit)]], must confront head-on. The manuscript [[participatory-it-from-bit]] proposes that objectivity is *consensus among coupled agents* rather than a pre-given observer-independent ledger of facts. Frauchiger-Renner is precisely the no-go that such a proposal must answer: if quantum agents modelling each other cannot share certified conclusions (assumption C fails), then any account of inter-agent agreement must explain *how consensus is built* rather than assuming it is read off a common reality. The project's answer is structural — agreement is not given but transported: comparing one agent's belief to another's requires [[Parallel transport]] of beliefs along a connection ([[Gauge transformation]]), with residual disagreement measured by [[Holonomy]]. In that reading, FR's failure of assumption C is the foundational-physics shadow of nonzero holonomy between agent frames, and the multi-agent coupling that drives the project's beliefs toward a shared centroid ([[Multi-agent variational free energy]]) is the constructive mechanism by which approximate, never-perfect consensus emerges. The result also motivates treating "facts" as agent-indexed from the outset, aligning the project with the relational ([[rovelli-1996-relational-qm]], [[adlam-2022-cross-perspective|adlam-rovelli-2022-cross-perspective]]) and QBist ([[fuchs2014-qbism-locality|fuchs-2014-qbism]], [[fuchs-2017-participatory-realism]]) responses, and against any "view from nowhere."

## Cross-links

- Concepts: [[Observer-dependent facts and Wigner's friend]], [[QBism]], [[Quantum reference frames]]
- Related sources: [[brukner-2018-no-go-observer-facts]], [[rovelli-1996-relational-qm]], [[adlam-2022-cross-perspective|adlam-rovelli-2022-cross-perspective]], [[fuchs2014-qbism-locality|fuchs-2014-qbism]]
- Manuscript: [[participatory-it-from-bit]]
- Project: [[Participatory realism (it from bit)]]

## BibTeX

```bibtex
@article{frauchiger2018quantum,
  author        = {Frauchiger, Daniela and Renner, Renato},
  title         = {Quantum theory cannot consistently describe the use of itself},
  journal       = {Nature Communications},
  volume        = {9},
  pages         = {3711},
  year          = {2018},
  doi           = {10.1038/s41467-018-05739-8},
  eprint        = {1604.07422},
  archivePrefix = {arXiv},
  primaryClass  = {quant-ph}
}
```
