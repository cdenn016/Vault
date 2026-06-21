---
type: paper
title: "Building up Spacetime with Quantum Entanglement"
aliases:
  - Van Raamsdonk 2010
  - spacetime from entanglement
  - vanraamsdonk-2010-entanglement-spacetime
authors:
  - Van Raamsdonk, Mark
year: 2010
arxiv: "1005.3035"
url: https://doi.org/10.1007/s10714-010-1034-0
tags:
  - cluster/participatory/quantum-foundations
  - project/multi-agent
  - field/physics
  - field/philosophy
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Building up Spacetime with Quantum Entanglement

> [!info] Citation
> Van Raamsdonk, Mark (2010). "Building up Spacetime with Quantum Entanglement." *General Relativity and Gravitation*, 42(10), 2323–2329. https://doi.org/10.1007/s10714-010-1034-0. arXiv:1005.3035. (First Award, 2010 Gravity Research Foundation Essay Competition.)

> [!note] Editorial: This is a short essay (a Gravity Research Foundation award piece), so it advances a conceptual thesis with illustrative holographic arguments rather than a fully formalized theorem. The claims above reflect its argued thesis, not derived proofs.

## TL;DR
Van Raamsdonk argues, within the AdS/CFT framework, that the classical connectedness of spacetime is not fundamental but emergent: it is the geometric manifestation of quantum entanglement between degrees of freedom in the dual non-perturbative description. Reducing entanglement between two boundary regions causes the corresponding bulk regions to pinch off and disconnect, while maximal entanglement corresponds to a smoothly connected geometry. The essay won first prize in the 2010 Gravity Research Foundation competition and launched the modern "spacetime from entanglement" research programme.

## Problem & setting
Within the AdS/CFT correspondence, a single CFT on the boundary is dual to a connected bulk geometry. But one can also consider two decoupled copies of the CFT: their joint state, if entangled (as in the thermofield double), is dual to an eternal black hole with a wormhole (Einstein-Rosen bridge) connecting two exterior regions. Van Raamsdonk asks what happens to the bulk geometry as the inter-copy entanglement is varied — interpolating from maximal entanglement (connected wormhole) down to zero entanglement (two completely disconnected spacetimes). The Ryu–Takayanagi formula for holographic entanglement entropy provides the quantitative handle.

## Method
The paper exploits the Ryu–Takayanagi relation, which equates the entanglement entropy $S_A$ of a boundary region $A$ to the area of the minimal bulk surface homologous to $A$:
$$S_A = \frac{\text{Area}(\gamma_A)}{4G_N}.$$
By studying how this area changes as entanglement is reduced — via a "disentangling" deformation of the quantum state — Van Raamsdonk shows that the proper distance between the two bulk regions grows without bound as $S \to 0$, and the spacetime pinches off into two disconnected pieces. The argument is largely qualitative and uses the two-sided eternal black hole (thermofield double state) as the central example, but the conclusion is stated as a general principle: entanglement $\Leftrightarrow$ geometric connectivity.

## Key results
The central claim is the ER = EPR precursor: a smoothly connected spacetime requires quantum entanglement between the degrees of freedom associated with its parts. Concretely, (1) the thermofield double state, maximally entangled across two CFT copies, is dual to the connected eternal black hole geometry; (2) decreasing the entanglement entropy continuously deforms the geometry so that the Einstein-Rosen bridge elongates and eventually severs; (3) a completely unentangled product state corresponds to two disconnected, causally independent spacetimes. The paper thereby gives a quantum-information origin to classical spacetime topology and connectivity.

## Relevance to this research
This paper is a foundational reference for the participatory-realism / it-from-bit strand of the research program, where the question is whether physical reality — including the arena (spacetime) itself — is constituted by information-theoretic or inferential relations rather than by an independently existing substrate. Van Raamsdonk's argument that spacetime connectivity = quantum entanglement is perhaps the sharpest extant example of an ontological claim about physical geometry deriving from a purely relational/informational quantity. In the PIFB manuscript and the broader participatory-realism framing, this provides a concrete case study of how "geometry emerges from correlations" — directly analogous to the thesis that belief geometry (the SPD Riemannian structure over Gaussian beliefs in the VFE transformer) encodes relational structure rather than intrinsic substance. The Ryu–Takayanagi formula is also an instance of an information-geometric identity (entropy = area), and the role of entanglement entropy as a measure of "how connected" two regions are is structurally parallel to the role of KL divergence in measuring how coupled two belief distributions are in the VFE free-energy functional. This paper does not bear directly on the transformer architecture or GL(K) attention, but is central to the philosophy-of-physics motivation in PIFB.tex and the `cluster/participatory/quantum-foundations` thread.

## Cross-links
- Concepts: [[Emergent spacetime and holography|Holography]], [[Entanglement Entropy]], [[Emergent spacetime and holography|AdS-CFT Correspondence]], [[Emergent spacetime and holography|Emergent Spacetime]], [[fuchs-2017-participatory-realism|Participatory Realism]], [[wheeler-1990-it-from-bit|It-from-Bit]]
- Related sources: [[maldacena-1999-adscft|Maldacena-1997-adscft]], [[ryu-takayanagi-2006-holographic-entanglement-entropy|Ryu-Takayanagi-2006-holographic-entropy]], [[wheeler-1990-it-from-bit|Wheeler-1989-it-from-bit]], [[wheeler-1990-it-from-bit]], [[rovelli-1996-relational-qm]], [[fuchs2014-qbism-locality|fuchs-2014-qbism]]
- Concepts (participatory): [[Participatory realism (it from bit)]], [[Fisher information metric]], [[Mass as Fisher information]], [[Meta-agents and hierarchical emergence]], [[Renormalization-group flow of beliefs]]
- Manuscript/Project: [[Participatory realism (it from bit)|PIFB]], [[participatory-it-from-bit|Participatory It-From-Bit]], [[participatory-it-from-bit]], [[VFE Transformer Program]]

## BibTeX
```bibtex
@article{VanRaamsdonk2010,
  author  = {Van Raamsdonk, Mark},
  title   = {Building up Spacetime with Quantum Entanglement},
  journal = {General Relativity and Gravitation},
  year    = {2010},
  volume  = {42},
  number  = {10},
  pages   = {2323--2329},
  doi     = {10.1007/s10714-010-1034-0},
  note    = {First Award, 2010 Gravity Research Foundation Essay Competition},
  eprint  = {1005.3035},
  archivePrefix = {arXiv},
  primaryClass  = {hep-th},
}
```
