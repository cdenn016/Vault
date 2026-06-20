---
type: reference
title: "A No-Go Theorem for Observer-Independent Facts"
aliases: ["Brukner 2018", "Brukner no-go theorem", "Observer-independent facts"]
authors: ["Časlav Brukner"]
year: 2018
arxiv: "1804.00749"
url: https://arxiv.org/abs/1804.00749
tags: [cluster/participatory, project/multi-agent, field/physics, field/philosophy, cluster/participatory/quantum-foundations]
created: 2026-06-19
updated: 2026-06-19
---

# A No-Go Theorem for Observer-Independent Facts

> [!info] Citation
> Brukner, Č. (2018). "A no-go theorem for observer-independent facts." *Entropy* **20**(5), 350. DOI: 10.3390/e20050350. Preprint: arXiv:1804.00749.

## TL;DR

Brukner turns the extended Wigner's-friend scenario into a *Bell-type inequality* whose violation rules out the joint existence of observer-independent facts. He considers two Wigners, each with a friend in a sealed lab, and shows that a small set of assumptions — that each friend's measurement yields a definite fact, that these facts are observer-independent (shared across Wigner and friend), together with the usual Bell premises of locality and free choice — implies an inequality that quantum mechanics predicts will be violated. There is therefore no consistent way to assign observer-independent facts to the outcomes of measurements performed by agents who are themselves treated as quantum systems. The result converts the philosophical "whose fact is it?" question into an experimentally meaningful, testable statement.

## What it establishes

- **A testable no-go.** Unlike the logical Frauchiger-Renner contradiction, Brukner's result is an *inequality*, giving an in-principle experimental signature: a violation would demonstrate that observer-independent facts cannot coexist with locality and free choice.
- **The facts are relational.** The natural escape is to deny observer-independence: a friend's outcome is a fact *relative to the friend*, not an absolute fact shared with Wigner. This aligns the result with relational ([[rovelli-1996-relational-qm]]) and QBist ([[fuchs-2014-qbism]]) readings.
- **Connection to FR.** Brukner relates the inequality to the Frauchiger-Renner trilemma, locating their shared premise (some version of consistency/shareability of certified facts) as the one quantum mechanics forces us to abandon.

## Why the project cites it

This theorem is the *operational, falsifiable* version of the challenge that [[participatory-it-from-bit]] must meet: it shows there is no pre-given ledger of observer-independent facts, so any account of objectivity must be built from inter-agent relations rather than assumed. The project's answer — objectivity as *transported consensus* among coupled agents — treats agreement as something constructed by [[Parallel transport]] of beliefs between [[Agents as fibre-bundle sections]], with residual disagreement measured by [[Holonomy]] under a [[Gauge transformation]]. Brukner's inequality is, in that reading, the foundational-physics statement that holonomy between observer frames is generically nonzero: facts certified in one frame need not survive transport to another. The result thus directly motivates the project's [[Multi-agent variational free energy]] coupling, the mechanism by which approximate (never absolute) consensus is dynamically reached, and it anchors the [[Observer-dependent facts and Wigner's friend]] strand of the [[Participatory realism (it from bit)]] cluster. It is cited alongside [[frauchiger-renner-2018-no-self-description]] as the pair of no-go results the manuscript's notion of consensus-as-objectivity is designed to be compatible with.

```bibtex
@article{brukner2018nogo,
  author  = {Brukner, {\v{C}}aslav},
  title   = {A no-go theorem for observer-independent facts},
  journal = {Entropy},
  volume  = {20},
  number  = {5},
  pages   = {350},
  year    = {2018},
  doi     = {10.3390/e20050350},
  eprint  = {1804.00749},
  archivePrefix = {arXiv},
  primaryClass  = {quant-ph}
}
```
