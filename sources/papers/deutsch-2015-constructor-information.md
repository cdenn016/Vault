---
type: paper
title: "Constructor Theory of Information"
aliases:
  - Deutsch 2015
  - Constructor Information Theory
  - deutsch-marletto-2015-constructor-information
  - Deutsch & Marletto 2015
  - Constructor theory
  - Information constructor theory
authors:
  - Deutsch, David
  - Marletto, Chiara
year: 2015
arxiv: "1405.5563"
url: https://doi.org/10.1098/rspa.2014.0540
tags:
  - cluster/participatory/quantum-foundations
  - cluster/participatory/philosophy-of-mind
  - project/multi-agent
  - field/physics
  - field/philosophy
  - field/mathematics
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Constructor Theory of Information

> [!info] Citation
> Deutsch, D. & Marletto, C. (2015). "Constructor Theory of Information." *Proceedings of the Royal Society A*, 471(2174), 20140540. https://doi.org/10.1098/rspa.2014.0540

## TL;DR
Deutsch and Marletto reformulate information theory entirely in constructor-theoretic terms — specifying which physical transformations are possible or impossible rather than reasoning about probabilities or initial conditions. The framework resolves the foundational circularity in Shannon's theory (distinguishability defined in terms of information, and vice versa) by grounding information in constructor-theoretic computation and cloning primitives. It reveals that quantum information is an instance of a more general concept, "superinformation," characterized by the impossibility of certain cloning tasks.

## Problem & setting
Classical (Shannon) information theory cannot describe quantum information because quantum prohibitions (e.g. no-cloning) violate the interoperability assumed by Shannon. More deeply, Shannon's theory defines distinguishability in terms of information and information in terms of distinguishability — a circularity. Previous attempts to ground information in physics (Wheeler's "it from bit," Wootters, Hardy, Clifton et al.) treated information as an a priori mathematical concept rather than something whose properties are determined by physical law. Constructor theory (Deutsch 2013) provides the substrate-independent language — laws expressed as which transformations are possible/impossible — that can break this circularity.

## Method
Constructor theory describes the world via *tasks* — sets of ordered input-output attribute pairs on substrates — and classifies them as possible ($A\checkmark$) or impossible ($A\times$). A *constructor* performs a task while remaining capable of repeating it. Key definitions built in this language:

- **Computation variable**: a set $S$ of attributes for which all permutations $C_\Pi^S = \{x \to \Pi(x)\}_{x \in S}$ are possible tasks.
- **Clonable set**: attributes $S$ for which the cloning task $R_S(x_0) = \{(x, x_0) \to (x, x)\}_{x \in S}$ is possible.
- **Information variable**: a clonable computation variable; an **information medium** is a substrate possessing at least one.
- **Distinguishability**: a set $X$ of attributes is distinguishable if $\{x \to \psi_x\}_{x \in X}$ is possible for some information variable $\{\psi_x\}$ — defined without reference to distinguishability, breaking the circularity.
- **Measurement**: distinguished from distinguishability by requiring the original substrate to persist and the result to be stored in a separate output information medium.

Five conjectured physical principles (I–VII in the paper) govern information: substrate-independence (locality, Principle II), interoperability ($S_1 \times S_2$ is an information variable whenever $S_1, S_2$ are, Principle III), pairwise-to-joint distinguishability (Principle IV), and unlimited generic resources and composition (Principles VI–VII). *Superinformation media* are information media on which certain natural tasks are impossible; quantum systems are the canonical example.

## Key results
- A non-circular, purely constructor-theoretic definition of classical information capacity as $\log|S|$ for the largest information variable $S$ — locality implies capacities add for disjoint substrates.
- Measurement is shown to be a form of cloning to a different (information) medium, and non-perturbing measurement of information variables is always possible by construction.
- All characteristic features of quantum information (no-cloning, complementary variables with no simultaneous sharp values, irreducible measurement disturbance, entanglement as locally inaccessible information) follow as corollaries from the single constructor-theoretic property that defines superinformation media — the impossibility of certain tasks — without invoking the Hilbert-space formalism.
- The framework places information on the same footing as energy: a substrate-independent principle that constrains subsidiary theories rather than directly predicting measurement outcomes, yet without which understanding is incomplete.

## Relevance to this research
Constructor theory's reformulation of information as "which transformations are possible/impossible" is philosophically adjacent to the participatory-realism and "it from bit" tradition explored in the PIFB manuscript and the broader VFE research program. The constructor-theoretic notion of an *information variable* (a clonable computation variable) provides a rigorous substrate-independent counterpart to the belief-state variables $(μ, Σ, φ)$ that the VFE transformer manipulates. The substrate-independence and interoperability principles mirror the gauge-equivariance requirements of the GL(K) attention mechanism — information structure is preserved under the group action just as constructor-theoretic information is preserved under medium changes. The impossibility-based definition of distinguishability resonates with the KL-divergence geometry of belief coupling: two beliefs are "distinguishable" exactly to the degree that the VFE cost of transporting one to the other is large. The superinformation/quantum-information connection is relevant to any extension of the VFE framework toward quantum substrates.

> [!note] Why the project cites it — the *contrast class* (from manuscript-citation note)
> Constructor theory is the contrast class the project explicitly defines itself against. Both programs are "information-first," but they differ sharply on what grounds information: Deutsch and Marletto ground it in *objective, agent-independent* possibility/impossibility facts about physical transformations, whereas [[participatory-it-from-bit]] grounds objectivity in *consensus among coupled agents* — information is fundamentally perspectival, and shared structure is an achievement of inter-agent [[Parallel transport]] rather than a pre-given physical invariant. Citing Deutsch–Marletto lets the manuscript stake out its participatory position: it accepts the "it from bit" priority of information ([[wheeler-1990-it-from-bit]]) but rejects locating information in observer-independent physical possibility, siding instead with relational and QBist accounts ([[rovelli-1996-relational-qm]], [[fuchs-2014-qbism]], [[adlam-rovelli-2022-cross-perspective]]), with [[Holonomy]] measuring where that construction fails to globalize.

## Cross-links
- Concepts: [[Participatory Realism]], [[It from Bit]], [[Information Geometry]], [[Gauge Equivariance]], [[VFE Functional]], [[Parallel transport]], [[Holonomy]], [[Agents as fibre-bundle sections]], [[Participatory realism (it from bit)]]
- Related sources: [[wheeler-1989-it-from-bit]], [[wheeler-1990-it-from-bit]], [[marletto-2021-constructor-reality]], [[rovelli-1996-relational-qm]], [[fuchs-2014-qbism]], [[adlam-rovelli-2022-cross-perspective]]
- Manuscript/Project: [[PIFB]], [[VFE Transformer Program]], [[GL(K) Attention]]

## BibTeX
```bibtex
@article{Deutsch2015,
  author  = {Deutsch, David and Marletto, Chiara},
  title   = {Constructor Theory of Information},
  journal = {Proceedings of the Royal Society A},
  volume  = {471},
  number  = {2174},
  pages   = {20140540},
  year    = {2015},
  doi     = {10.1098/rspa.2014.0540},
}
```
