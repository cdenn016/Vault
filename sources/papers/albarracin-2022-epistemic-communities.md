---
type: paper
title: "Epistemic Communities under Active Inference"
aliases:
  - "Albarracin et al. 2022"
  - "Albarracin (2022) Epistemic Communities"
authors:
  - Mahault Albarracin
  - Daphne Demekas
  - Maxwell J. D. Ramstead
  - Conor Heins
year: 2022
arxiv: null
url: https://www.mdpi.com/1099-4300/24/4/476
tags:
  - cluster/social-physics
  - cluster/multi-agent
  - cluster/vfe
  - project/multi-agent
  - project/social-physics
  - field/neuroscience
  - field/psychology
  - field/sociology
  - cluster/social-physics/networks-and-contagion
status: stable
created: 2026-06-19
updated: 2026-06-19
---

# Epistemic Communities under Active Inference

> [!info] Citation
> Albarracin, M., Demekas, D., Ramstead, M. J. D., & Heins, C. (2022). "Epistemic Communities under Active Inference." *Entropy* **24**(4), 476. DOI: [10.3390/e24040476](https://doi.org/10.3390/e24040476).

## TL;DR

An in-silico active-inference model of **confirmation bias** and its collective consequence, **echo-chamber formation**. Agents sample information so as to justify their existing view of reality; this self-confirming sampling drives them toward high certainty in their own beliefs and, at the population level, partitions the community into mutually reinforcing epistemic clusters that no longer exchange corrective evidence. The paper gives a first-principles, free-energy account of polarization and belief-community fragmentation.

## Problem & setting

Why do communities of communicating agents polarize into echo chambers rather than converging on shared beliefs? The authors model agents as active-inference systems that choose which information to sample (epistemic actions). When the policy that minimizes expected free energy favors confirming evidence, agents preferentially attend to belief-consistent signals. The setting is a population of such agents whose information environment is partly shaped by whom they listen to.

## Method

Each agent runs discrete active inference with a generative model over states and observations and selects information-sampling policies by minimizing expected free energy. Confirmation bias is induced by the structure of preferences/precision so that belief-consistent observations are sought. Simulating a population of these agents traces how individual self-confirming sampling aggregates into stable, segregated belief communities, and how parameters (e.g. precision on priors) tune the strength of clustering.

## Key results

- Confirmation bias emerges naturally as an expected-free-energy-minimizing information-sampling policy, not as an imposed irrationality.
- At the collective level this produces echo chambers: the population fragments into high-certainty, internally homogeneous epistemic clusters with suppressed cross-cluster influence.
- The degree of polarization is controlled by model parameters (notably prior precision), giving a tunable account of when communities cohere versus splinter.

## Relevance to this research

This paper is the active-inference microfoundation for the **"heat death" of belief diversity** discussed in [[participatory-it-from-bit]]. The project's coupled-agent dynamics ([[Multi-agent variational free energy]]) admit both a consensus collapse (all beliefs converging, diversity lost) and a fragmentation regime (isolated belief clusters); Albarracin et al. supply the mechanism for the latter at the level of individual epistemic action — confirmation-biased sampling — and show it yields exactly the echo-chamber fragmentation the project reads as one terminal phase of its dynamics. In the project's terms, high prior precision and selective attention $\beta_{ij}$ that down-weights dissonant neighbors are the levers that push the system from gauge-coupled consensus toward frozen, mutually non-influencing clusters, the social-physics analogue of the cluster transitions in [[deffuant-2000-bounded-confidence]] and [[hegselmann-krause-2002]] but derived from free energy. This grounds the project's claim that polarization and consensus are not separate phenomena but opposite limits of a single free-energy-minimizing belief dynamics, and connects to the NEW [[Collective active inference]] page.

## Cross-links

- Concepts: [[Collective active inference]], [[Multi-agent variational free energy]], [[Meta-agents and hierarchical emergence]]
- Related sources: [[friston-2024-federated-inference]], [[heins-2024-surprise-minimization]], [[waade-2025-as-one-and-many]], [[deffuant-2000-bounded-confidence]], [[hegselmann-krause-2002]]
- Manuscript: [[participatory-it-from-bit]]
- Project: [[Gauge-Theoretic Multi-Agent VFE Model]]

```bibtex
@article{albarracin2022epistemic,
  author  = {Albarracin, Mahault and Demekas, Daphne and Ramstead, Maxwell J. D. and Heins, Conor},
  title   = {Epistemic Communities under Active Inference},
  journal = {Entropy},
  volume  = {24},
  number  = {4},
  pages   = {476},
  year    = {2022},
  doi     = {10.3390/e24040476},
  publisher = {MDPI}
}
```
