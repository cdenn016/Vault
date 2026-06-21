---
type: paper
title: "Federated Inference and Belief Sharing"
aliases:
  - "Friston et al. 2024"
  - "Friston (2024) Federated Inference"
authors:
  - Friston, Karl J.
  - Parr, Thomas
  - Heins, Conor
  - Constant, Axel
  - Friedman, Daniel
  - Isomura, Takuya
  - Fields, Chris
  - Verbelen, Tim
  - Ramstead, Maxwell J. D.
  - Clippinger, John
  - Frith, Christopher D.
year: 2024
arxiv: null
url: https://doi.org/10.1016/j.neubiorev.2023.105500
tags:
  - cluster/multi-agent
  - cluster/vfe
  - cluster/social-physics
  - cluster/social-physics/opinion-dynamics
  - project/multi-agent
  - project/social-physics
  - field/neuroscience
  - field/cs-ml
status: stable
created: 2026-06-19
updated: 2026-06-20
---

# Federated Inference and Belief Sharing

> [!info] Citation
> Friston, K. J., Parr, T., Heins, C., Constant, A., Friedman, D., Isomura, T., Fields, C., Verbelen, T., Ramstead, M. J. D., Clippinger, J., & Frith, C. D. (2024). "Federated inference and belief sharing." *Neuroscience & Biobehavioral Reviews* **156**, 105500. DOI: [10.1016/j.neubiorev.2023.105500](https://doi.org/10.1016/j.neubiorev.2023.105500).

## TL;DR

A position-and-simulation paper arguing that distributed intelligence — "federated inference" — emerges when agents who share a common world and a common world-model broadcast their beliefs to one another and treat received beliefs as observations. All of the needed machinery (when to share, what to share, how to integrate others' beliefs) is shown to follow from minimizing variational free energy. Numerical studies simulate the emergence, acquisition, and communication of a shared language among synthetic agents, demonstrating that joint inference and learning across a population is itself a free-energy-minimizing process. This is the direct FEP statement of belief-coupling between agents.

## Problem & setting

Multiple active-inference agents inhabit a shared environment and each maintain a generative model of it. They cannot read one another's internal states directly; instead an agent can broadcast its posterior beliefs, and a receiving agent can treat the broadcast as additional sensory evidence about the shared hidden state. The question is how belief-sharing should be governed so that the collective performs better joint inference than any isolated agent — and whether that governance can be derived rather than designed.

## Method

The authors cast belief-sharing as part of each agent's free-energy minimization. An agent's generative model is augmented so that other agents' communicated beliefs are observations with their own likelihood; integrating them is then ordinary variational inference. Decisions about communication (whether to speak, what to encode) are framed as actions selected to minimize expected free energy. Simulations instantiate synthetic agents that develop a shared lexicon — the emergence of a common code is shown to reduce collective free energy, and joint inference outperforms solitary inference on shared tasks.

## Key results

- Belief-sharing among agents with a common world-model is a free-energy-minimizing operation: received beliefs enter as observations and are integrated by standard variational updating.
- A shared language / communication code emerges spontaneously from the population's drive to minimize collective surprise, rather than being imposed.
- Federated inference yields distributed intelligence: the collective infers and learns more effectively than its members in isolation, with the whole behaving as a coherent inferential system.

## Relevance to this research

This is the cleanest free-energy-principle statement of exactly the coupling term the [[Gauge-Theoretic Multi-Agent VFE Model]] is built around. The project's belief-coupling energy $\sum_{ij}\beta_{ij}\,\mathrm{KL}(q_i \| \Omega_{ij} q_j)$ in [[Multi-agent variational free energy]] is federated inference written as a single functional: each agent treats its neighbors' (transported) beliefs as priors/evidence and pays a KL price for disagreement, with the attention weights $\beta_{ij}$ governing whom to listen to — the project's analogue of Friston et al.'s "when and to whom to broadcast." What this paper supplies in words, the project supplies in a closed variational form; what the project adds is the missing geometric ingredient, the gauge transport $\Omega_{ij}$ that re-expresses a neighbor's belief in the receiver's frame before integration. Federated inference assumes a literally common world-model and hence a common frame; PIFB (see [[participatory-it-from-bit]]) relaxes that to agents holding beliefs in distinct local frames related by a connection, recovering federated belief-sharing as the flat-connection ($\Omega_{ij}=I$) special case. This reference is therefore the anchor for the [[Collective active inference]] page and the FEP-side justification of the project's coupling, attention, and emergent-communication claims.

## Cross-links

- Concepts: [[Collective active inference]], [[Multi-agent variational free energy]], [[Variational free energy]]
- Related sources: [[heins-2024-surprise-minimization]], [[waade-2025-as-one-and-many]], [[albarracin-2022-epistemic-communities]], [[friston-2010-free-energy-principle]]
- Manuscript: [[participatory-it-from-bit]]
- Project: [[Gauge-Theoretic Multi-Agent VFE Model]]

## BibTeX
```bibtex
@article{friston2024federated,
  author    = {Friston, Karl J. and Parr, Thomas and Heins, Conor and Constant, Axel and Friedman, Daniel and Isomura, Takuya and Fields, Chris and Verbelen, Tim and Ramstead, Maxwell J. D. and Clippinger, John and Frith, Christopher D.},
  title     = {Federated inference and belief sharing},
  journal   = {Neuroscience \& Biobehavioral Reviews},
  volume    = {156},
  pages     = {105500},
  year      = {2024},
  doi       = {10.1016/j.neubiorev.2023.105500},
  publisher = {Elsevier}
}
```
