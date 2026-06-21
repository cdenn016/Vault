---
type: paper
title: "An Introduction to QBism with an Application to the Locality of Quantum Mechanics"
aliases:
  - "Fuchs 2014"
  - "QBism introduction"
  - "QBism locality"
authors:
  - Fuchs, Christopher A.
  - Mermin, N. David
  - Schack, Rüdiger
year: 2014
arxiv: "1311.5253"
url: https://arxiv.org/abs/1311.5253
tags:
  - cluster/participatory/quantum-foundations
  - cluster/participatory/philosophy-of-mind
  - project/multi-agent
  - field/physics
  - field/philosophy
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# An Introduction to QBism with an Application to the Locality of Quantum Mechanics

> [!info] Citation
> Fuchs, C. A., Mermin, N. D., & Schack, R. (2014). "An Introduction to QBism with an Application to the Locality of Quantum Mechanics." *American Journal of Physics* 82, 749. arXiv:1311.5253.

## TL;DR
QBism (Quantum Bayesianism) reinterprets quantum mechanics as a single-agent tool for organizing personal probabilistic beliefs about future experience, rather than as a description of an observer-independent world. Quantum states are personal judgments, measurement outcomes are agent-created experiences, and "quantum nonlocality" dissolves because quantum correlations are necessarily between time-like separated events in one agent's experience. The paper argues this resolves nearly all foundational paradoxes of quantum mechanics — including EPR, Bell, and the measurement problem — without introducing new ontology.

## Problem & setting
The paper addresses the foundational paradoxes that have plagued quantum mechanics for nine decades: nonlocality, the measurement problem, wave-function collapse, and the EPR/Bell conundrum. Prior interpretations (Copenhagen, Many-Worlds, Bohmian mechanics, Consistent Histories) either fail to remove the paradoxes or require strong additional ontological commitments. QBism is positioned as a consistent local interpretation that takes subjective (personalist, de Finetti-style) probability as primitive.

## Method
QBism's core interpretive moves are:

1. **Personalist probability.** Probabilities are agents' degrees of belief constrained only by Dutch-book coherence (no guaranteed loss), following the tradition of Savage, de Finetti, and Jeffrey. The quantum state is therefore the agent's personal probability assignment, not an objective feature of the world.

2. **Measurement as agent action.** A measurement is any action an agent takes to elicit an experience; the outcome is the experience itself, created only when it enters that agent's awareness. There is no pre-existing result.

3. **Collapse as Bayesian update.** "Wave-function collapse" is simply an agent updating her state assignment after gaining new experience — not a physical process.

4. **Locality through the single-agent constraint.** Because quantum mechanics organizes one agent's experience, and because an agent's world-line is necessarily time-like, quantum correlations cannot be space-like separated. Bell-inequality violations are explained by noting that the hidden variable $\lambda$ in the factorization
$$p(x,y|i,j) = \langle p(x|i,\lambda)\,p(y|j,\lambda)\rangle$$
corresponds to nothing in any agent's experience and therefore lies outside the scope of physical science. Its nonexistence implies nothing about nonlocality.

## Key results
- QBism dissolves "quantum nonlocality" without invoking faster-than-light influences or additional ontology; nonlocality arguments rest on reifying probability-1 assignments as objective facts or on invoking undefined parameters $\lambda$.
- Wigner's-friend and EPR paradoxes are shown to be artifacts of treating measurement outcomes as agent-independent.
- A positive philosophical program is sketched: science is about the relation between agents and world, not about agent-free objective reality. Schrödinger (1931), Bohr, and Freud are cited as historical antecedents.
- The paper is explicitly introductory; technical elaboration (SIC-POVMs, quantum-Bayesian coherence) is deferred to companion works (Fuchs & Schack, arXiv:1301.3274; Caves, Fuchs & Schack 2002).

## Relevance to this research
QBism is directly relevant to the participatory-realism thread of the VFE research program (see `PIFB.tex` / *Participatory It-from-Bit*). Several specific connections:

- **Agent-relative beliefs as VFE beliefs.** VFE beliefs $(μ, Σ, φ)$ are formal probability distributions personal to an agent/layer; the QBist insistence that quantum states are personal judgments of a single agent maps naturally onto the per-node belief tuples in the multi-agent active inference architecture.
- **Measurement = VFE minimization.** QBism treats measurement as an action that creates an outcome in experience; VFE minimization is the formal mechanism by which an agent updates beliefs upon "acting" on sensory data. The two share the same conceptual structure.
- **Locality through single-agent scope.** The VFE multi-agent model preserves locality by coupling agents only through belief-transport operators $\Omega_{ij}$; there is no global hidden state, mirroring QBism's dissolution of $\lambda$.
- **Participatory realism.** QBism's "agents co-create reality through experience" is the philosophical stance underlying the PIFB manuscript; that paper explicitly invokes QBism as a quantum-foundations grounding for the participatory it-from-bit program.
- **No objective collapse.** QBism's rejection of physical collapse parallels the VFE program's avoidance of hard decision/argmax steps — beliefs propagate probabilistically, not via winner-take-all collapse.

## Cross-links
- Concepts: [[Participatory Realism]], [[QBism]], [[Bayesian Probability]], [[Active Inference]]
- Related sources: [[fuchs2010-qbism-perimeter]], [[caves2002-quantum-bayesian]]
- Manuscript/Project: [[PIFB]], [[VFE Transformer Program]]

## BibTeX
```bibtex
@article{Fuchs2014,
  author  = {Fuchs, Christopher A. and Mermin, N. David and Schack, R{\"u}diger},
  title   = {An Introduction to {QBism} with an Application to the Locality of Quantum Mechanics},
  journal = {American Journal of Physics},
  volume  = {82},
  pages   = {749},
  year    = {2014},
  eprint  = {1311.5253},
  archivePrefix = {arXiv},
  primaryClass  = {quant-ph},
}
```
