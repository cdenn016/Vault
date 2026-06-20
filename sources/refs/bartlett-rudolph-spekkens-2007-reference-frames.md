---
type: reference
title: "Reference Frames, Superselection Rules, and Quantum Information"
aliases: ["Bartlett, Rudolph & Spekkens 2007", "BRS 2007", "Reference frames review"]
authors: ["Stephen D. Bartlett", "Terry Rudolph", "Robert W. Spekkens"]
year: 2007
arxiv: "quant-ph/0610030"
url: https://arxiv.org/abs/quant-ph/0610030
tags: [cluster/participatory, cluster/gauge-theory, project/multi-agent, project/transformer, field/physics, cluster/participatory/quantum-foundations]
created: 2026-06-19
updated: 2026-06-19
---

# Reference Frames, Superselection Rules, and Quantum Information

> [!info] Citation
> Bartlett, S. D., Rudolph, T., & Spekkens, R. W. (2007). "Reference frames, superselection rules, and quantum information." *Reviews of Modern Physics* **79**(2), 555–609. DOI: 10.1103/RevModPhys.79.555. Preprint: arXiv:quant-ph/0610030.

## TL;DR

This canonical review establishes the operational theory of *quantum reference frames* (QRFs). It distinguishes "speakable" information (bit strings that can be communicated in the abstract) from "unspeakable" information (a direction in space, a phase, a moment in time) that is meaningful only relative to a shared physical reference frame. Lacking a shared frame between parties induces an effective *superselection rule* — a restriction on the operations and states accessible to them — which can be lifted by establishing or sharing a frame, itself a physical quantum system that degrades with use. The review systematizes how the symmetry group of the missing frame (e.g. $U(1)$ for phase, $SU(2)$ for orientation, the Galilei group for spacetime) controls which information is frame-dependent and how much can be recovered.

## What it establishes

- **Frames as physical systems.** A reference frame is not an abstract coordinate choice but a physical token (a gyroscope, a clock, a phase reference) carrying quantum degrees of freedom; aligning frames is a communication task with quantifiable resource cost.
- **Superselection from missing frames.** Absence of a shared frame for a symmetry group $G$ is operationally equivalent to a $G$-superselection rule restricting accessible states/operations; the review makes the frame ↔ superselection correspondence precise.
- **Group-theoretic accounting.** The relevant symmetry group fixes the decomposition of states into invariant ("speakable") and frame-relative ("unspeakable") parts, with explicit machinery for orientation, phase, and chirality references.

## Why the project cites it

This is the foundation that licenses the project to read its per-agent gauge frame $\phi_i$ as a *genuine physical reference frame* rather than a bookkeeping convenience — the central interpretive claim of [[participatory-it-from-bit]]. BRS make precise that frame-relative ("unspeakable") content requires a shared physical frame to compare, and that the missing-frame symmetry group governs what survives comparison. The project's [[Gauge transformation]] $\Omega_{ij} = \exp(\phi_i)\exp(-\phi_j)$ is exactly a change of reference frame in this sense, and [[Parallel transport]] of an agent's belief from frame $i$ to frame $j$ is the inferential analogue of aligning two physical reference frames; the unremovable residue when frames cannot be globally aligned is [[Holonomy]]. The speakable/unspeakable split maps onto the project's distinction between frame-invariant belief content (objective, shareable) and frame-dependent content (agent-local) — the operational substrate of [[Participatory realism (it from bit)]] and of treating [[Agents as fibre-bundle sections]]. Because the framework is fully group-theoretic, it also connects to the project's block-$GL(K)$ gauge structure in the [[VFE Transformer Program]] and underwrites the [[Quantum reference frames]] strand alongside [[giacomini-2019-qrf-covariance]] and [[vanrietvelde-2020-change-of-perspective]].

```bibtex
@article{bartlett2007reference,
  author  = {Bartlett, Stephen D. and Rudolph, Terry and Spekkens, Robert W.},
  title   = {Reference frames, superselection rules, and quantum information},
  journal = {Reviews of Modern Physics},
  volume  = {79},
  number  = {2},
  pages   = {555--609},
  year    = {2007},
  doi     = {10.1103/RevModPhys.79.555},
  eprint  = {quant-ph/0610030},
  archivePrefix = {arXiv},
  primaryClass  = {quant-ph}
}
```
