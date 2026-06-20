---
type: reference
title: "A Change of Perspective: Switching Quantum Reference Frames via a Perspective-Neutral Framework"
aliases: ["Vanrietvelde et al. 2020", "Perspective-neutral framework", "QRF switching"]
authors: ["Augustin Vanrietvelde", "Philipp A. Höhn", "Flaminia Giacomini", "Esteban Castro-Ruiz"]
year: 2020
arxiv: "1809.00556"
url: https://arxiv.org/abs/1809.00556
tags: [cluster/participatory, cluster/gauge-theory, project/multi-agent, field/physics, cluster/participatory/quantum-foundations]
created: 2026-06-19
updated: 2026-06-19
---

# A Change of Perspective: Switching Quantum Reference Frames via a Perspective-Neutral Framework

> [!info] Citation
> Vanrietvelde, A., Höhn, P. A., Giacomini, F., & Castro-Ruiz, E. (2020). "A change of perspective: switching quantum reference frames via a perspective-neutral framework." *Quantum* **4**, 225. DOI: 10.22331/q-2020-01-27-225. Preprint: arXiv:1809.00556.

## TL;DR

This paper recasts quantum-reference-frame changes in the language of *constrained systems and gauge symmetry*. The authors introduce a "perspective-neutral" structure: a redundant, gauge-invariant description of the total system from which any individual frame's perspective is recovered by *gauge-fixing* (choosing which subsystem plays the role of the reference). Switching from frame A to frame B is then a two-step operation — undo A's gauge-fixing to return to the perspective-neutral description, then re-fix to B. This makes QRF transformations a special case of the Dirac quantization of gauge theories, with the reference-frame choice literally a choice of gauge.

## What it establishes

- **Perspective-neutral = gauge-invariant.** There is a redundant description, invariant under the symmetry group, that contains no chosen frame; each observer's perspective is one gauge slice of it.
- **Frame change = gauge transformation.** Switching reference frames is gauge-fixing followed by re-fixing, placing QRF physics squarely within constrained-Hamiltonian / principal-bundle formalism.
- **Reduction and embedding maps.** The paper gives explicit quantum maps reducing the perspective-neutral state to a given frame's description and back, generalizing the operator-level QRF transformations of [[giacomini-2019-qrf-covariance]].

## Why the project cites it

This is the quantum-mechanics analogue of the project's principal-bundle picture and the cleanest precedent for treating *frame choice as gauge-fixing*. The manuscript [[participatory-it-from-bit]] models agents as [[Agents as fibre-bundle sections]] over a shared base, where no global section is canonical; Vanrietvelde et al. supply exactly this structure on the physics side — a perspective-neutral (gauge-invariant) total description, with each agent's view obtained by a [[Gauge transformation]] (gauge-fixing). Their two-step frame switch (reduce to neutral, re-embed to a new frame) is structurally identical to the project's composition of transports $\Omega_{ij} = \exp(\phi_i)\exp(-\phi_j)$, which likewise factors a perspective change through a common reference, and the obstruction to a single global gauge slice is the project's [[Holonomy]]. The constrained-system framing also legitimizes reading the project's belief-coupling as living on a quotient/gauge-invariant space rather than on raw frame-dependent coordinates, sharpening what "objective content" means in the [[Participatory realism (it from bit)]] cluster. It extends the [[Quantum reference frames]] strand begun with [[giacomini-2019-qrf-covariance]] and [[bartlett-rudolph-spekkens-2007-reference-frames]] toward the explicit gauge-theoretic language the project uses throughout.

```bibtex
@article{vanrietvelde2020change,
  author  = {Vanrietvelde, Augustin and H{\"o}hn, Philipp A. and Giacomini, Flaminia and Castro-Ruiz, Esteban},
  title   = {A change of perspective: switching quantum reference frames via a perspective-neutral framework},
  journal = {Quantum},
  volume  = {4},
  pages   = {225},
  year    = {2020},
  doi     = {10.22331/q-2020-01-27-225},
  eprint  = {1809.00556},
  archivePrefix = {arXiv},
  primaryClass  = {quant-ph}
}
```
