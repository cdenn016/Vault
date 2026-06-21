---
type: paper
title: "Holographic Derivation of Entanglement Entropy from AdS/CFT"
aliases:
  - "Ryu-Takayanagi 2006"
  - "Ryu-Takayanagi formula"
  - "RT formula"
  - "ryu-takayanagi-2006-holographic-derivation"
  - "Ryu-Takayanagi-2006-holographic-entropy"
authors:
  - Shinsei Ryu
  - Tadashi Takayanagi
year: 2006
arxiv: hep-th/0603001
url: https://arxiv.org/abs/hep-th/0603001
tags:
  - cluster/participatory
  - project/multi-agent
  - field/physics
  - cluster/participatory/quantum-foundations
created: 2026-06-19
updated: 2026-06-19
---

# Holographic Derivation of Entanglement Entropy from AdS/CFT

> [!info] Citation
> Shinsei Ryu and Tadashi Takayanagi (2006). "Holographic Derivation of Entanglement Entropy from AdS/CFT." *Physical Review Letters* 96(18): 181602. DOI: [10.1103/PhysRevLett.96.181602](https://doi.org/10.1103/PhysRevLett.96.181602). Preprint: [arXiv:hep-th/0603001](https://arxiv.org/abs/hep-th/0603001).

## TL;DR

Ryu and Takayanagi propose that the entanglement entropy of a spatial region $A$ in a holographic conformal field theory equals the area of a minimal bulk surface $\gamma_A$ anchored on $\partial A$, divided by $4 G_N$:
$$S_A = \frac{\mathrm{Area}(\gamma_A)}{4 G_N}.$$
This generalizes the Bekenstein–Hawking black-hole entropy formula to arbitrary boundary regions and is the cleanest statement that *geometry encodes entanglement*: a measure of quantum information (entanglement entropy) is read off a geometric quantity (minimal-surface area). It is the technical keystone beneath the slogan "spacetime is built from entanglement."

## Problem & setting

In AdS/CFT a $d$-dimensional CFT lives on the boundary of a $(d+1)$-dimensional anti-de Sitter bulk. Computing entanglement entropy directly in an interacting CFT is generally intractable. RT supply a geometric prescription in the bulk, later derived from the gravitational path integral (Lewkowycz–Maldacena 2013) and extended to covariant (HRT) and quantum-corrected forms.

## Method

For a boundary region $A$, find the codimension-2 bulk surface $\gamma_A$ of minimal area that is homologous to $A$ and shares its boundary. The entanglement entropy is one quarter of that area in Planck units. The formula ties the first law of entanglement to linearized Einstein equations (see [[faulkner-2014-gravitation-from-entanglement]]) and underlies tensor-network ([[vidal-2007-entanglement-renormalization]]) and ER=EPR readings of holography.

## Key results

The prescription reproduces known 2D CFT entanglement entropies, satisfies strong subadditivity geometrically, and recovers black-hole entropy as a special case. It launched the "it-from-qubit" / entanglement-geometry program.

## Relevance to this research

This is the missing keystone beneath two works the PIFB manuscript ([[participatory-it-from-bit]]) *does* cite — [[vanraamsdonk-2010-entanglement-spacetime]] and Swingle's tensor-network holography — both of which rest on the RT identification of entanglement with geometry. PIFB's Level-3 program proposes an *information-to-geometry* map of its own: the pullback of the [[Fisher information metric]] from a statistical fibre to a base manifold, inducing emergent "spacetime-like" structure. RT is the canonical physics precedent for exactly this move (an information measure determining a metric quantity), and the natural external benchmark against which PIFB's classical-information, gauge-theoretic pullback should be contrasted. It anchors the proposed [[Emergent spacetime and holography]] theme and the [[Participatory realism (it from bit)]] thread.

## Cross-links
- Concepts: [[Participatory realism (it from bit)]], [[Fisher information metric]]
- Themes: [[Emergent spacetime and holography]]
- Related sources: [[vanraamsdonk-2010-entanglement-spacetime]], [[faulkner-2014-gravitation-from-entanglement]], [[vidal-2007-entanglement-renormalization]], [[wheeler-1990-it-from-bit]]

## BibTeX
```bibtex
@article{ryu2006holographic,
  author  = {Ryu, Shinsei and Takayanagi, Tadashi},
  title   = {Holographic Derivation of Entanglement Entropy from {AdS/CFT}},
  journal = {Physical Review Letters},
  year    = {2006},
  volume  = {96},
  number  = {18},
  pages   = {181602},
  doi     = {10.1103/PhysRevLett.96.181602},
  note    = {arXiv:hep-th/0603001}
}
```
